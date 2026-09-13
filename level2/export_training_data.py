#!/usr/bin/env python3
"""Export training data CSVs for Vaultstack pipeline stages.

Outputs (to level2/reports/training_data/):
- sft_noisy_to_gold.jsonl — (noisy OCR text, gold JSON) pairs for Stage 3 SFT
- cer_rewards.csv — per-engine CER vs PDF-GT for SCST RL (Stage 2b)
- simpo_pairs.jsonl — preference pairs (good vs bad CER) for SimPO (Stage 3b)
"""
from __future__ import annotations

import csv
import json
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"
REPORTS_TRAIN = REPORTS / "training_data"
REPORTS_TRAIN.mkdir(exist_ok=True)

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

ENGINE_ORDER = [
    "easyocr", "surya", "tesseract_bilingual", "tesseract_indic",
    "openbharatocr", "anuvaad_tesseract", "indicphotoocr", "doctr",
    "paddleocr_indic", "rapidocr",
]

def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)

def edit_distance(a: str, b: str) -> int:
    """Levenshtein via Myers bit-vector."""
    if a == b:
        return 0
    m, n = len(a), len(b)
    if m == 0: return n
    if n == 0: return m
    if m > 950:
        a, b, m, n = b, a, n, m
    peq = {}
    for i, c in enumerate(a):
        peq[c] = peq.get(c, 0) | (1 << i)
    full = (1 << m) - 1
    msb = 1 << (m - 1)
    pv, mv, score = full, 0, m
    for c in b:
        eq = peq.get(c, 0)
        xv = eq | mv
        xh = (((eq & pv) + pv) ^ pv) | eq
        ph = mv | (~(xh | pv) & full)
        mh = pv & xh
        if ph & msb: score += 1
        elif mh & msb: score -= 1
        ph = ((ph << 1) | 1) & ((1 << m) - 1)
        mh = (mh << 1) & ((1 << m) - 1)
        pv = mh | (~(xv | ph) & ((1 << m) - 1))
        mv = xv & ph
    return score

def cer(a: str, b: str) -> float:
    if not b: return 1.0
    return edit_distance(nfc(a).lower(), nfc(b).lower()) / len(b)

def wer(a: str, b: str) -> float:
    if not b: return 1.0
    aw = nfc(a).lower().split()
    bw = nfc(b).lower().split()
    return edit_distance(" ".join(aw), " ".join(bw)) / len(bw)

def load_packs():
    """engine -> {page_id: text}"""
    idx = {}
    for e in ENGINES:
        m = {}
        for p in (OUT / e).rglob("*.json"):
            try:
                o = json.loads(p.read_text(encoding="utf-8"))
                t = "\n".join(r.get("text", "") for r in o.get("regions", [])).strip()
                m[p.stem] = t
            except Exception:
                pass
        idx[e] = m
    return idx

def load_manifest():
    return json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))

def load_pdf_gt():
    import pymupdf
    man = {x["page_id"]: x for x in load_manifest()}
    gt = {}
    by_raw = {}
    for it in man.values():
        by_raw.setdefault(it["raw_path"], []).append(it)
    for raw, items in by_raw.items():
        try:
            doc = pymupdf.open(ROOT / raw)
        except Exception:
            continue
        for it in items:
            try:
                gt[it["page_id"]] = doc[int(it["page_index"])].get_text().strip()
            except Exception:
                gt[it["page_id"]] = ""
        doc.close()
    return gt

def main():
    print("Loading data...")
    packs = load_packs()
    pdf_gt = load_pdf_gt()
    man = {x["page_id"]: x for x in load_manifest()}

    # 1. SFT noisy→gold pairs
    print("Generating SFT pairs...")
    l1_labels = {}
    for e in ["te", "ta", "kn", "ml"]:
        for p in (L2.parent / "arc_level_1" / "labeled" / e).glob("*.json"):
            try:
                o = json.loads(p.read_text(encoding="utf-8"))
                l1_labels[o["page_id"]] = "\n".join(r.get("text", "") for r in o.get("regions", []))
            except Exception:
                pass

    sft_pairs = []
    for pid, gt_text in l1_labels.items():
        for e in ENGINE_ORDER:
            noisy = packs[e].get(pid, "")
            if noisy and gt_text:
                sft_pairs.append({
                    "page_id": pid,
                    "engine": e,
                    "noisy_text": nfc(noisy),
                    "gold_text": nfc(gt_text),
                    "gold_json": json.dumps({"text": gt_text}, ensure_ascii=False)
                })

    with open(REPORTS_TRAIN / "sft_noisy_to_gold.jsonl", "w", encoding="utf-8") as f:
        for pair in sft_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")
    print(f"  SFT pairs: {len(sft_pairs)}")

    # 2. CER rewards for SCST
    print("Generating CER rewards...")
    cer_rows = []
    for pid in pdf_gt:
        gt = pdf_gt[pid]
        if len(gt) < 50:  # thin GT
            continue
        for e in ENGINE_ORDER:
            noisy = packs[e].get(pid, "")
            if not noisy:
                continue
            c = cer(noisy, gt)
            w = wer(noisy, gt)
            cer_rows.append({
                "page_id": pid,
                "engine": e,
                "cer": round(c, 4),
                "wer": round(w, 4),
                "gt_chars": len(gt),
                "out_chars": len(noisy),
                "reward": round(1.0 - c, 4)  # SCST reward = 1 - CER
            })

    with open(REPORTS_TRAIN / "cer_rewards.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["page_id", "engine", "cer", "wer", "gt_chars", "out_chars", "reward"])
        w.writeheader()
        w.writerows(cer_rows)
    print(f"  CER rewards: {len(cer_rows)}")

    # 3. SimPO preference pairs (good CER vs bad CER per page)
    print("Generating SimPO pairs...")
    simpo_pairs = []
    for pid in pdf_gt:
        gt = pdf_gt[pid]
        if len(gt) < 50:
            continue
        engine_cers = []
        for e in ENGINE_ORDER:
            noisy = packs[e].get(pid, "")
            if noisy:
                c = cer(noisy, gt)
                engine_cers.append((e, c, packs[e][pid]))
        if len(engine_cers) < 2:
            continue
        engine_cers.sort(key=lambda x: x[1])  # sort by CER ascending (best first)
        best_e, best_cer, best_text = engine_cers[0]
        worst_e, worst_cer, worst_text = engine_cers[-1]
        if best_cer < 0.15 and worst_cer > 0.30:
            simpo_pairs.append({
                "page_id": pid,
                "chosen_engine": best_e,
                "chosen_cer": round(best_cer, 4),
                "chosen_text": nfc(best_text),
                "rejected_engine": worst_e,
                "rejected_cer": round(worst_cer, 4),
                "rejected_text": nfc(worst_text),
                "gt_chars": len(pdf_gt[pid])
            })

    with open(REPORTS_TRAIN / "simpo_pairs.jsonl", "w", encoding="utf-8") as f:
        for pair in simpo_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")
    print(f"  SimPO pairs: {len(simpo_pairs)}")

    # Summary
    summary = {
        "sft_pairs": len(sft_pairs),
        "cer_rewards": len(cer_rows),
        "simpo_pairs": len(simpo_pairs),
        "engines_used": ENGINE_ORDER,
        "pages_with_gt": len([p for p in pdf_gt if len(pdf_gt[p]) >= 50]),
    }
    (REPORTS_TRAIN / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Summary: {summary}")
    print(f"Outputs in {REPORTS_TRAIN}")

if __name__ == "__main__":
    main()
