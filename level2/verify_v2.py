#!/usr/bin/env python3
"""Verification Suite v2 — beyond verify_all.py.

Adds:
  - coverage_ge6 (>=6/10 engines produce nonempty text; renamed from 'consensus')
  - true consensus (>=6 engines AND median pairwise token Jaccard >= 0.5)
  - repetition-loop detection (n-gram redundancy)
  - charset hallucination (script X output on script Y page), with
    manifest dominant_script cross-check and manifest_tag_suspects
  - JSON schema validation of every pack (missing tracked explicitly)
  - per-page runtime telemetry from HEARTBEAT.jsonl (median ms/page, pages/hour)
  - script-sliced leaderboard (LEADERBOARD_BY_SCRIPT.md)
  - consolidated CSV: page_id x engine matrix
Outputs: reports/VERIFY_V2_SUMMARY.json, reports/MATRIX.csv, reports/LEADERBOARD.md,
         reports/LEADERBOARD_BY_SCRIPT.md, reports/TRUE_CONSENSUS.json, reports/FAILURE_TAXONOMY.md
"""
from __future__ import annotations

import csv
import hashlib
import json
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
REPORTS = L2 / "reports"

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

SCRIPT_RANGES = {
    "Telugu": (0x0C00, 0x0C7F), "Tamil": (0x0B80, 0x0BFF),
    "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0D7F),
    "Devanagari": (0x0900, 0x097F), "Latin": (0x0041, 0x007A),
}

SCRIPT_BUCKETS = ["Latin", "Telugu", "Tamil", "Kannada", "Malayalam", "Devanagari"]

REQUIRED_KEYS = {"page_id", "source", "lang", "script", "quality_tier",
                 "image", "regions", "ocr_engine"}
REQ_REGION_KEYS = {"region_id", "cls", "bbox_xyxy", "text"}


def build_index() -> dict[str, dict[str, Path]]:
    """engine -> {page_id: pack path} for every pack on disk."""
    idx = {}
    for e in ENGINES:
        m: dict[str, Path] = {}
        d = OUT / e
        if d.exists():
            for p in sorted(d.rglob("*.json")):
                m.setdefault(p.stem, p)
        idx[e] = m
    return idx


def pack_text(path: Path) -> str | None:
    """Joined region text; None when the pack JSON is unreadable."""
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        return "\n".join(r.get("text", "") for r in obj.get("regions", []))
    except Exception:
        return None


def schema_state(path: Path | None) -> str:
    """'ok' | 'bad_schema' | 'bad_json' | 'missing' for one pack path."""
    if path is None:
        return "missing"
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return "bad_json"
    if not REQUIRED_KEYS.issubset(obj.keys()):
        return "bad_schema"
    for r in obj.get("regions", []):
        if not REQ_REGION_KEYS.issubset(r.keys()):
            return "bad_schema"
        bb = r.get("bbox_xyxy")
        if not (isinstance(bb, list) and len(bb) == 4):
            return "bad_schema"
    return "ok"


def script_of(text: str) -> str | None:
    h = Counter()
    for ch in text:
        cp = ord(ch)
        for name, (lo, hi) in SCRIPT_RANGES.items():
            if lo <= cp <= hi:
                h[name] += 1
                break
    return h.most_common(1)[0][0] if h else None


def normalized_tokens(text: str) -> set[str]:
    """NFC, lowercase, whitespace tokens with punctuation/symbols stripped."""
    t = unicodedata.normalize("NFC", text).lower()
    out = set()
    for w in t.split():
        w = "".join(c for c in w if unicodedata.category(c)[0] not in ("P", "S"))
        if w:
            out.add(w)
    return out


def jaccard(a: set[str], b: set[str]) -> float:
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def loop_redundancy(text: str) -> float:
    """0..1 — fraction of 8-grams that repeat. >0.6 = collapse loop."""
    words = text.split()
    if len(words) < 16:
        return 0.0
    grams = [" ".join(words[i:i+8]) for i in range(len(words) - 7)]
    uniq = len(set(grams))
    return 1 - (uniq / len(grams))


def garbage_ratio(text: str) -> float:
    """0..1 — chars that are neither letter/mark/number nor common punct/space vs total."""
    t = text.strip()
    if not t:
        return 0.0
    ok = set(" \n\t.,;:!?\"'()-–—/|।॥%₹")
    letters = sum(1 for c in t if unicodedata.category(c)[0] in ("L", "M", "N"))
    noise = sum(1 for c in t if unicodedata.category(c)[0] not in ("L", "M", "N", "Z") and c not in ok)
    return round(noise / max(len(t), 1), 3)


def nfc_ok(text: str) -> bool:
    return unicodedata.normalize("NFC", text) == text


NATIVE_DIGIT_RANGES = [(0x0C66, 0x0C6F), (0x0BE6, 0x0BEF), (0x0CE6, 0x0CEF),
                       (0x0D66, 0x0D6F), (0x0966, 0x096F)]


def digit_profile(text: str) -> dict:
    native = ascii_ = 0
    for ch in text:
        cp = ord(ch)
        if any(lo <= cp <= hi for lo, hi in NATIVE_DIGIT_RANGES):
            native += 1
        elif "0" <= ch <= "9":
            ascii_ += 1
    return {"native": native, "ascii": ascii_}


def english_leak(text: str, page_script: str) -> bool:
    """Indic-script page whose output is overwhelmingly ASCII words (not digits/punct)."""
    if page_script == "Latin":
        return False
    words = [w for w in text.split() if len(w) >= 3]
    if len(words) < 5:
        return False
    ascii_words = sum(1 for w in words if all(ord(c) < 128 for c in w))
    return ascii_words / len(words) > 0.9


def heartbeat_stats() -> dict:
    """Per-engine median ms/page + pages/hour from HEARTBEAT.jsonl (latest per page wins)."""
    hb = L2 / "HEARTBEAT.jsonl"
    acc = {e: {"dur_entries": 0, "fail_entries": 0,
               "pages": {}}
           for e in ENGINES}
    if hb.exists():
        with hb.open(encoding="utf-8") as f:
            for line in f:
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                e = o.get("engine")
                if e not in acc:
                    continue
                if o.get("fail"):
                    acc[e]["fail_entries"] += 1
                d = o.get("dur_ms")
                if d is None:
                    continue
                acc[e]["dur_entries"] += 1
                pid = o.get("page_id")
                prev = acc[e]["pages"].get(pid)
                if prev is None or o.get("t", 0) >= prev[0]:
                    acc[e]["pages"][pid] = (o.get("t", 0), d)
    out = {}
    for e in ENGINES:
        durs = sorted(d for _, d in acc[e]["pages"].values())
        m = median(durs) if durs else None
        out[e] = {
            "heartbeat_dur_entries": acc[e]["dur_entries"],
            "heartbeat_fail_entries": acc[e]["fail_entries"],
            "distinct_pages_timed": len(durs),
            "median_ms_per_page": round(m) if m is not None else None,
            "pages_per_hour": round(3_600_000 / m, 1) if m else None,
        }
    return out


def pdf_text_by_page(manifest: list[dict]) -> dict[str, str]:
    """page_id -> PDF text-layer text ('' when unavailable); one open per unique raw PDF."""
    out = {it["page_id"]: "" for it in manifest}
    try:
        import pymupdf
    except ImportError:
        return out
    by_raw = defaultdict(list)
    for it in manifest:
        by_raw[it["raw_path"]].append(it)
    for raw, items in by_raw.items():
        rp = ROOT / raw
        if not rp.exists():
            continue
        try:
            doc = pymupdf.open(rp)
        except Exception:
            continue
        for it in items:
            try:
                out[it["page_id"]] = doc[int(it["page_index"])].get_text()
            except Exception:
                pass
        doc.close()
    return out


def manifest_render_check() -> dict:
    """Items 41/58/59/60: manifest integrity + render checksum sanity from disk."""
    manifest = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
    renders = L2 / "renders_shared"
    out = {"n_manifest": len(manifest), "missing_raw": [], "bad_page_index": [],
           "locked_pdfs": [], "missing_render": [], "stale_render": [],
           "render_noise": 0}
    seen_raw = {}
    locked = set()
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    for item in manifest:
        raw = ROOT / item["raw_path"]
        if not raw.exists():
            out["missing_raw"].append(item["page_id"])
            continue
        if not (0 <= int(item["page_index"]) < int(item["pdf_pages"])):
            out["bad_page_index"].append(item["page_id"])
        rp = str(raw)
        if rp not in seen_raw:
            seen_raw[rp] = True
            if pymupdf is not None:
                try:
                    doc = pymupdf.open(raw)
                    if doc.needs_pass:
                        locked.add(rp)
                    doc.close()
                except Exception:
                    pass
        png = renders / f"{item['page_id']}.png"
        if not png.exists():
            out["missing_render"].append(item["page_id"])
        else:
            if png.stat().st_size < 2000:
                out["stale_render"].append(item["page_id"])
    out["locked_pdfs"] = sorted(locked)
    out["render_noise"] = len([p for p in renders.glob("*_bin.png")]) if renders.exists() else 0
    if renders.exists():
        out["n_renders"] = len([p for p in renders.glob("*_*.png") if not p.name.endswith("_bin.png")])
    else:
        out["n_renders"] = 0
    return out


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    manifest = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
    idx = build_index()
    gt = pdf_text_by_page(manifest)

    agg = {e: {"empty": 0, "thin": 0, "loop": 0, "checked": 0, "missing": 0,
               "chars": [], "garbage": [], "nfc_bad": 0, "eng_leak": 0,
               "lines_vs_gt_short": 0, "native_digits": 0,
               "ascii_digits_on_indic": 0, "cap_l1": [], "cap_pdf": [],
               "by_script": defaultdict(list), "by_script_packs": defaultdict(int),
               "by_script_thin": defaultdict(int),
               "by_script_cap": defaultdict(list)} for e in ENGINES}
    coverage_count = 0
    coverage_pages = []
    true_consensus_pages = []
    family_consensus_pages = []
    fam_detail: dict[str, dict] = {}
    true_consensus_detail: dict[str, dict] = {}
    matrix_rows = []
    halluc = []
    suspect_pages: dict[str, dict] = {}
    schema_bad = []
    schema_missing = []
    text_hash: dict[str, set[str]] = {e: set() for e in ENGINES}
    dup_texts: dict[str, dict[str, int]] = {e: {} for e in ENGINES}
    # tesseract-family engines mirror one model — one vote in family consensus
    FAMILY = {
        "tesseract_family": {"tesseract_indic", "tesseract_bilingual",
                             "anuvaad_tesseract", "openbharatocr"},
    }
    def family_of(e: str) -> str:
        for fam, members in FAMILY.items():
            if e in members:
                return fam
        return e

    for item in manifest:
        pid = item["page_id"]
        dom = item.get("dominant_script")
        row = {"page_id": pid, "dominant_script": dom,
               "mixed_book": item.get("mixed_book_page", False)}
        live_engines = 0
        page_tokens: dict[str, set[str]] = {}
        page_scripts: dict[str, str] = {}
        fam_tokens: dict[str, set[str]] = {}
        for e in ENGINES:
            p = idx[e].get(pid)
            state = schema_state(p)
            if state == "missing":
                schema_missing.append(f"{e}/{pid}")
                agg[e]["missing"] += 1
                row[e] = None
                continue
            if state != "ok":
                schema_bad.append(f"{e}/{pid}")
            row[e] = 0
            txt = (pack_text(p) or "").strip()
            agg[e]["checked"] += 1
            if dom:
                agg[e]["by_script_packs"][dom] += 1
            if not txt:
                agg[e]["empty"] += 1
                continue
            row[e] = len(txt)
            live_engines += 1
            agg[e]["chars"].append(len(txt))
            if len(txt) < 30:
                agg[e]["thin"] += 1
            if dom:
                agg[e]["by_script"][dom].append(len(txt))
                if len(txt) < 30:
                    agg[e]["by_script_thin"][dom] += 1
            gt_txt = gt.get(pid, "").strip()
            if len(gt_txt) >= 200:
                ratio = round(len(txt) / len(gt_txt), 3)
                agg[e]["cap_pdf"].append(ratio)
                if dom:
                    agg[e]["by_script_cap"][dom].append(ratio)
                gt_lines = len([l for l in gt_txt.splitlines() if l.strip()])
                if gt_lines >= 6:
                    eng_lines = len([l for l in txt.splitlines() if l.strip()])
                    if eng_lines < gt_lines / 3:
                        agg[e]["lines_vs_gt_short"] += 1
            l1 = item.get("l1_chars") or 0
            if l1 > 200:
                agg[e]["cap_l1"].append(round(len(txt) / l1, 3))
            if loop_redundancy(txt) > 0.6:
                agg[e]["loop"] += 1
            gr = garbage_ratio(txt)
            if gr > 0.3:
                agg[e]["garbage"].append(f"{pid}({gr})")
            if not nfc_ok(txt):
                agg[e]["nfc_bad"] += 1
            if english_leak(txt, dom or "Latin"):
                agg[e]["eng_leak"] += 1
            dp = digit_profile(txt)
            if dp["native"]:
                agg[e]["native_digits"] += 1
            if dom and dom != "Latin" and dp["ascii"] > 10 and dp["native"] == 0:
                agg[e]["ascii_digits_on_indic"] += 1
            h = hashlib.sha1(txt[:400].encode("utf-8")).hexdigest()
            text_hash[e].add(h)
            dup_texts[e][h] = dup_texts[e].get(h, 0) + 1
            toks = normalized_tokens(txt)
            if toks:
                page_tokens[e] = toks
                fam = family_of(e)
                # family union: tesseract-mirror engines pool their tokens as ONE vote
                fam_tokens[fam] = fam_tokens.get(fam, set()) | set(toks)
            s = script_of(txt)
            if s:
                page_scripts[e] = s
        if live_engines >= 6:
            coverage_count += 1
            coverage_pages.append(pid)
        if len(page_tokens) >= 6:
            engs = sorted(page_tokens)
            js = [jaccard(page_tokens[engs[i]], page_tokens[engs[j]])
                  for i in range(len(engs)) for j in range(i + 1, len(engs))]
            mj = median(js)
            true_consensus_detail[pid] = {
                "engines_with_text": len(page_tokens),
                "median_pairwise_jaccard": round(mj, 4)}
            if mj >= 0.5:
                true_consensus_pages.append(pid)
        # family-grouped consensus: tesseract-family mirrors count as ONE engine
        if len(fam_tokens) >= 6:
            fams = sorted(fam_tokens)
            fjs = [jaccard(fam_tokens[fams[i]], fam_tokens[fams[j]])
                   for i in range(len(fams)) for j in range(i + 1, len(fams))]
            fmj = median(fjs)
            fam_detail[pid] = {
                "independent_votes": len(fams),
                "median_pairwise_jaccard": round(fmj, 4)}
            if fmj >= 0.5:
                family_consensus_pages.append(pid)
        if not item.get("mixed_book_page", False) and dom and dom != "unknown":
            votes = Counter(s for s in page_scripts.values()
                            if s and s != "Latin" and s != dom)
            for s, n in votes.most_common():
                if n >= 3:
                    suspect_pages[pid] = {
                        "page_id": pid, "lang_tag": item["lang"],
                        "dominant_script": dom, "output_script": s,
                        "engines": sorted(e for e, sc in page_scripts.items()
                                          if sc == s),
                        "note": ">=3 engines independently output this script; "
                                "suspected manifest dominant_script tag error"}
                else:
                    halluc.extend(
                        {"page": pid, "engine": e, "page_script": dom,
                         "output_script": s}
                        for e, sc in sorted(page_scripts.items()) if sc == s)
        matrix_rows.append(row)

    with open(REPORTS / "MATRIX.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(matrix_rows[0].keys()))
        w.writeheader()
        w.writerows(matrix_rows)

    hb = heartbeat_stats()
    summary = {}
    for e in ENGINES:
        a = agg[e]
        chars = sorted(a["chars"])
        med = chars[len(chars)//2] if chars else 0
        p10 = chars[len(chars)//10] if chars else 0
        p90 = chars[int(len(chars)*0.9)] if chars else 0
        dup_max = max(dup_texts[e].values()) if dup_texts[e] else 0
        caps_l1 = sorted(a["cap_l1"])
        med_cap_l1 = caps_l1[len(caps_l1)//2] if caps_l1 else None
        caps_pdf = sorted(a["cap_pdf"])
        med_cap_pdf = caps_pdf[len(caps_pdf)//2] if caps_pdf else None
        by_script_med = {s: (sorted(v)[len(v)//2] if v else 0)
                         for s, v in sorted(a["by_script"].items())}
        summary[e] = {
            "checked": a["checked"],
            "missing_packs": a["missing"],
            "empty_rate": round(a["empty"] / a["checked"], 3) if a["checked"] else None,
            "thin_pages_lt30": a["thin"],
            "loop_pages": a["loop"],
            "median_chars": med,
            "median_capture_vs_l1": med_cap_l1,
            "median_capture_vs_pdf": med_cap_pdf,
            "by_script_median_chars": by_script_med,
            "p10_chars": p10,
            "p90_chars": p90,
            "total_output_chars": sum(chars),
            "garbage_pages_gt30pct": len(a["garbage"]),
            "garbage_examples": a["garbage"][:5],
            "nfc_violations": a["nfc_bad"],
            "english_leak_pages": a["eng_leak"],
            "lines_short_vs_gt": a["lines_vs_gt_short"],
            "native_digit_pages": a["native_digits"],
            "ascii_digits_on_indic_pages": a["ascii_digits_on_indic"],
            "distinct_output_hashes": len(text_hash[e]),
            "max_duplicate_pages": dup_max,
            **hb[e],
        }

    (REPORTS / "TRUE_CONSENSUS.json").write_text(
        json.dumps({
            "definition": ">=6 engines with tokenizable output AND "
                          "median pairwise token-Jaccard >= 0.5 "
                          "(NFC, lowercase, punct-stripped, whitespace tokens)",
            "count": len(true_consensus_pages),
            "page_ids": true_consensus_pages,
            "per_page": true_consensus_detail,
            "family_consensus": {
                "definition": "tesseract-family (tesseract_indic, tesseract_bilingual, "
                              "anuvaad_tesseract, openbharatocr) pooled as ONE vote; "
                              ">=6 independent votes AND median pairwise Jaccard >= 0.5",
                "count": len(family_consensus_pages),
                "page_ids": family_consensus_pages,
                "per_page": fam_detail,
            },
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    out = {
        "coverage_ge6": coverage_count,
        "coverage_ge6_definition": "pages where >=6 engines produced nonempty OCR text",
        "coverage_ge6_page_ids": coverage_pages,
        "true_consensus_pages": len(true_consensus_pages),
        "true_consensus_definition": ">=6 engines with text AND median pairwise "
                                     "token Jaccard >= 0.5 (see TRUE_CONSENSUS.json)",
        "true_consensus_page_ids": true_consensus_pages,
        "consensus_pages": {
            "consensus_pages_ge6_engines": coverage_count,
            "consensus_page_ids": coverage_pages,
            "deprecated": True,
            "note": "legacy key: old 'consensus' was coverage, not agreement; "
                    "kept one release for dashboard compat — use coverage_ge6 "
                    "or true_consensus_pages",
        },
        "consensus_pages_ge6_engines": coverage_count,
        "consensus_page_ids": coverage_pages,
        "consensus_pages_deprecated": True,
        "manifest_render_check": manifest_render_check(),
        "schema_violations": len(schema_bad),
        "schema_violation_examples": schema_bad[:20],
        "schema_missing_packs": len(schema_missing),
        "schema_missing_examples": schema_missing[:20],
        "hallucination_events": len(halluc),
        "hallucination_examples": halluc[:10],
        "manifest_tag_suspects": sorted(suspect_pages.values(),
                                        key=lambda x: x["page_id"]),
        "heartbeat": hb,
        "engines": summary,
    }
    (REPORTS / "VERIFY_V2_SUMMARY.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    tax_lines = ["# Failure Taxonomy — per engine (disk-truth)", "",
                 "Labels: EMPTY (no text) | LOOP (8-gram redundancy >0.6) | GARBAGE (>30% noise chars) |",
                 "ENG_LEAK (Indic page, >90% ASCII words) | LINES_SHORT (<1/3 of PDF-layer lines) |",
                 "NFC_BAD (text_nfc not normalized) | DUP (same text on many pages).", "",
                 "| engine | empty | loop | garbage | eng-leak | lines-short | nfc-bad | max-dup | p10/med/p90 chars |",
                 "|---|---|---|---|---|---|---|---|---|"]
    for e, s in summary.items():
        empty_n = round(s["empty_rate"] * 400) if s["empty_rate"] is not None else "—"
        tax_lines.append(f"| {e} | {empty_n} | {s['loop_pages']} | "
                         f"{s['garbage_pages_gt30pct']} | {s['english_leak_pages']} | {s['lines_short_vs_gt']} | "
                         f"{s['nfc_violations']} | {s['max_duplicate_pages']} | {s['p10_chars']}/{s['median_chars']}/{s['p90_chars']} |")
    (REPORTS / "FAILURE_TAXONOMY.md").write_text("\n".join(tax_lines) + "\n", encoding="utf-8")

    lines = ["# Engine Leaderboard (open policy, disk-truth)", "",
             "**per-language numbers mix scripts; see LEADERBOARD_BY_SCRIPT.md**", "",
             "| engine | checked | empty% | thin | loops | median chars | total chars | med capture vs PDF | ms/page | pages/hour |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for e, s in sorted(summary.items(), key=lambda kv: -(kv[1]["total_output_chars"] or 0)):
        cap = s.get("median_capture_vs_pdf")
        if cap is None:
            cap = s.get("median_capture_vs_l1")
        empty_pct = f"{s['empty_rate']*100:.1f}" if s['empty_rate'] is not None else "?"
        lines.append(f"| {e} | {s['checked']} | {empty_pct}% | {s['thin_pages_lt30']} | "
                     f"{s['loop_pages']} | {s['median_chars']} | {s['total_output_chars']} | "
                     f"{cap if cap is not None else '—'} | {s['median_ms_per_page'] or '—'} | "
                     f"{s['pages_per_hour'] or '—'} |")
    lines += ["", f"coverage pages (>=6 engines nonempty; renamed from 'consensus'): {coverage_count}/400",
              f"true consensus pages (>=6 engines, median pairwise Jaccard >= 0.5): "
              f"{len(true_consensus_pages)}/400 — reports/TRUE_CONSENSUS.json",
              f"schema violations: {len(schema_bad)} | missing packs: {len(schema_missing)}",
              f"hallucination events: {len(halluc)} | manifest tag suspects: {len(suspect_pages)}",
              "", "details: FAILURE_TAXONOMY.md, LEADERBOARD_BY_SCRIPT.md"]
    (REPORTS / "LEADERBOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["# Leaderboard by dominant script (manifest dominant_script buckets)", "",
             "Per-language tables mix scripts (e.g. 'te' pages are 47 Telugu + 42 Latin + 11 Devanagari).",
             "This is the script-sliced view; capture ratio vs PDF text layer "
             "(pages with >=200-char layer only).", ""]
    for b in SCRIPT_BUCKETS:
        pids = [it["page_id"] for it in manifest if it.get("dominant_script") == b]
        n_gt = sum(1 for p in pids if len(gt.get(p, "").strip()) >= 200)
        lines += [f"## {b} — {len(pids)} pages "
                  f"(capture computed on {n_gt} pages with >=200-char PDF text layer)", "",
                  "| engine | packs | empty | thin(<30c) | median chars | median capture |",
                  "|---|---|---|---|---|---|"]
        rows = []
        for e in ENGINES:
            a = agg[e]
            packs = a["by_script_packs"].get(b, 0)
            lens = sorted(a["by_script"].get(b, []))
            caps = sorted(a["by_script_cap"].get(b, []))
            med = lens[len(lens)//2] if lens else 0
            mcap = caps[len(caps)//2] if caps else None
            rows.append((e, packs, packs - len(lens),
                         a["by_script_thin"].get(b, 0), med, mcap))
        for e, packs, empty_n, thin, med, mcap in sorted(rows, key=lambda r: -r[4]):
            lines.append(f"| {e} | {packs} | {empty_n} | {thin} | {med} | "
                         f"{mcap if mcap is not None else '—'} |")
        winner = max(rows, key=lambda r: r[4])
        lines += ["", f"winner by median chars: **{winner[0]}** ({winner[4]} chars)", ""]
    (REPORTS / "LEADERBOARD_BY_SCRIPT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"coverage_ge6 (was 'consensus'): {coverage_count}/400")
    print(f"true_consensus_pages (median pairwise Jaccard >= 0.5): {len(true_consensus_pages)}/400")
    print(f"schema violations: {len(schema_bad)} | missing packs: {len(schema_missing)}")
    print(f"hallucinations: {len(halluc)} | manifest tag suspects: {len(suspect_pages)} "
          f"({', '.join(sorted(suspect_pages)) or 'none'})")
    mc = out["manifest_render_check"]
    print(f"manifest: missing_raw={len(mc['missing_raw'])} bad_index={len(mc['bad_page_index'])} "
          f"locked_pdfs={len(mc['locked_pdfs'])} missing_render={len(mc['missing_render'])} "
          f"tiny_render={len(mc['stale_render'])}")
    for e, s in summary.items():
        print(f"{e:<22} chk={s['checked']:>3} miss={s['missing_packs']:>3} empty={s['empty_rate']} "
              f"thin={s['thin_pages_lt30']:>3} loops={s['loop_pages']:>3} medChars={s['median_chars']:>5} "
              f"leak={s['english_leak_pages']:>2} dup={s['max_duplicate_pages']:>2} "
              f"ms={s['median_ms_per_page'] or '—'} pph={s['pages_per_hour'] or '—'}")
    print("\nwrote: MATRIX.csv, VERIFY_V2_SUMMARY.json, TRUE_CONSENSUS.json, "
          "LEADERBOARD.md, LEADERBOARD_BY_SCRIPT.md, FAILURE_TAXONOMY.md")


if __name__ == "__main__":
    main()
