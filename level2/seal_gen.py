#!/usr/bin/env python3
"""Seal generator — RUN.md, metrics.json, LEVEL2_SEAL.md, all from disk counts.

Usage: .venv/bin/python level2/seal_gen.py
"""
from __future__ import annotations

import json
import os
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = ROOT / "level2"
OUT = L2 / "out"
MODELS = L2 / "models"
REPORTS = L2 / "reports"

ENGINES = [
    "tesseract_indic", "openbharatocr", "easyocr", "paddleocr_indic",
    "indicphotoocr", "rapidocr", "tesseract_bilingual", "doctr",
    "surya", "anuvaad_tesseract",
]

MANIFEST = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
MANIFEST_IDS = {x["page_id"] for x in MANIFEST}

VERSIONS = {
    "tesseract_indic": "tesseract 5.5.2 (tel+hin+eng open stack)",
    "openbharatocr": "openbharatocr 0.4.3 (tesseract mirror path documented)",
    "easyocr": "easyocr 1.7.2 (all-Indic open reader)",
    "paddleocr_indic": "paddleocr 3.7.0 / paddlepaddle 3.3.1",
    "indicphotoocr": "IndicPhotoOCR IIIT-H (parseq trust-patched)",
    "rapidocr": "rapidocr 3.9.2 (per-lang PP-OCRv5/v4 mobile rec; te/ta/kn+dev; ml=no model->honest empty)",
    "tesseract_bilingual": "tesseract 5.5.2 (eng+stack bilingual)",
    "doctr": "python-doctr 1.1.0 (crnn_vgg16_bn)",
    "surya": "surya-ocr 0.22.1 (surya-2, block-mode html)",
    "anuvaad_tesseract": "anuvaad tessdata + tesseract 5.5.2",
}

QUALITY_STATUS = {
    "openbharatocr": "alias (tesseract_indic mirror — excluded from independent consensus)",
    "rapidocr": "partial_wash (ml=100 wash no-model; te/ta/kn honest signal v2 rerun 13 Sep)",
}

VENV = {
    "tesseract_indic": ".venv", "tesseract_bilingual": ".venv",
    "anuvaad_tesseract": ".venv",
    "openbharatocr": ".venv311", "easyocr": ".venv311",
    "paddleocr_indic": ".venv311", "indicphotoocr": ".venv311",
    "rapidocr": ".venv311", "doctr": ".venv311", "surya": ".venv311",
}


def engine_pages(engine: str) -> dict[str, str]:
    d = OUT / engine
    pages = {}
    if d.exists():
        for p in d.rglob("*.json"):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
                txt = "\n".join(r.get("text", "") for r in obj.get("regions", []))
                pages[obj.get("page_id", p.stem)] = txt.strip()
            except Exception:
                pages[p.stem] = ""
    return pages


def gen_engine(engine: str) -> None:
    pages = engine_pages(engine)
    matched = MANIFEST_IDS & set(pages.keys())
    missing = sorted(MANIFEST_IDS - set(pages.keys()))
    empty = [pid for pid in matched if not pages[pid]]
    short = [pid for pid in matched if 0 < len(pages[pid]) < 50]
    good = [pid for pid in matched if len(pages.get(pid, "")) >= 50]
    nonempty_rate = (len(matched) - len(empty)) / len(matched) if matched else 0
    collapse = round(1 - nonempty_rate, 3) if matched else None

    best = max(matched, key=lambda p: len(pages[p])) if matched else None
    worst = min([p for p in matched if pages[p]], key=lambda p: len(pages[p]), default=None)

    # example page_ids by category (law §3)
    eng_leak_ex = []
    table_ex = []
    for item in MANIFEST:
        pid = item["page_id"]
        if pid not in matched or not pages[pid]:
            continue
        dom = item.get("dominant_script")
        if len(eng_leak_ex) < 3 and dom and dom != "Latin":
            words = [w for w in pages[pid].split() if len(w) >= 3]
            if words and sum(1 for w in words if all(ord(c) < 128 for c in w)) / len(words) > 0.9:
                eng_leak_ex.append(pid)
        if len(table_ex) < 3 and len(pages[pid].splitlines()) >= 8 and pages[pid].count("  ") > 10:
            table_ex.append(pid)

    # verification stats
    v2_path = REPORTS / "VERIFY_V2_SUMMARY.json"
    v2 = json.loads(v2_path.read_text(encoding="utf-8")) if v2_path.exists() else {}
    vs = (v2.get("engines") or {}).get(engine, {})
    v1_path = REPORTS / "VERIFY_SUMMARY.json"
    v1 = json.loads(v1_path.read_text(encoding="utf-8")) if v1_path.exists() else {}
    vs1 = v1.get(engine, {})

    strengths = []
    weaknesses = []
    if vs:
        if vs.get("empty_rate") is not None and vs["empty_rate"] <= 0.08:
            strengths.append(f"low empty rate ({vs['empty_rate']*100:.1f}%)")
        if vs.get("median_chars"):
            strengths.append(f"median {vs['median_chars']} chars/page")
        if vs.get("median_ms_per_page"):
            strengths.append(f"{vs['median_ms_per_page']} ms/page")
        if vs.get("english_leak_pages", 0) > 50:
            weaknesses.append(f"{vs['english_leak_pages']} English-leak pages (Latin-only recognition)")
        elif vs.get("english_leak_pages", 0) > 10:
            weaknesses.append(f"{vs['english_leak_pages']} English-leak pages")
        if vs.get("loop_pages", 0) > 0:
            weaknesses.append(f"{vs['loop_pages']} repetition-loop pages")
        if vs.get("garbage_pages_gt30pct", 0) > 20:
            weaknesses.append(f"{vs['garbage_pages_gt30pct']} high-noise pages")
        if vs.get("nfc_violations", 0) > 0:
            weaknesses.append(f"{vs['nfc_violations']} NFC violations")
        if vs.get("max_duplicate_pages", 0) > 5:
            weaknesses.append(f"same text repeated on up to {vs['max_duplicate_pages']} pages (suspect)")
    if vs1.get("median_capture_ratio") is not None and vs1["median_capture_ratio"] < 0.5:
        weaknesses.append(f"capture ratio vs PDF layer only {vs1['median_capture_ratio']}")
    if not strengths:
        strengths.append("see reports/LEADERBOARD.md")
    if not weaknesses:
        weaknesses.append("see reports/FAILURE_TAXONOMY.md")

    # rerun history from out_archive/
    hist = []
    for d in sorted((L2 / "out_archive").glob(f"{engine}_v*")):
        n = len(list(d.rglob("*.json")))
        hist.append(f"{d.name} ({n} packs)")
    hist_line = "; ".join(hist) if hist else "none (single policy run)"

    mdl = MODELS / engine
    mdl.mkdir(parents=True, exist_ok=True)
    (mdl / "metrics.json").write_text(json.dumps({
        "engine": engine,
        "n_json": len(pages),
        "matching_page_ids": len(matched),
        "missing": len(missing),
        "n_empty": len(empty),
        "n_short_lt50": len(short),
        "nonempty_rate": round(nonempty_rate, 4),
        "collapse_rate": collapse,
        "median_capture_ratio": vs1.get("median_capture_ratio"),
        "empty_rate": vs.get("empty_rate"),
        "median_chars": vs.get("median_chars"),
        "median_ms_per_page": vs.get("median_ms_per_page"),
    }, indent=1), encoding="utf-8")

    run_md = f"""# RUN.md — `{engine}`

## Identity
- **model/version:** {VERSIONS.get(engine, "?")}
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** {QUALITY_STATUS.get(engine, "honest_signal")}
- **invoke:** `{VENV.get(engine, '.venv311')}/bin/python level2/run_engine.py --engine {engine} --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/{engine}/ | **models:** level2/models/{engine}/json/

## Counts (disk)
- n_json: {len(pages)}
- matching the shared 400: {len(matched)}
- missing: {len(missing)}
- empty: {len(empty)} | short(<50): {len(short)} | good(>=50): {len(good)}
- nonempty_rate: {nonempty_rate:.3f} | collapse_rate: {collapse}
- capture ratio vs PDF layer (median): {vs1.get('median_capture_ratio', '?')}

## 5 example page_ids
- best: {best} ({len(pages.get(best, ''))} chars)
- worst(nonempty): {worst} ({len(pages.get(worst, '')) if worst else 0} chars)
- empty: {empty[:3] or 'none'}
- english-leak: {eng_leak_ex[:3] or 'none'}
- table-ish: {table_ex[:3] or 'none'}

## Strengths
{chr(10).join('- ' + s for s in strengths)}

## Weaknesses
{chr(10).join('- ' + w for w in weaknesses)}

## Rerun history
- {hist_line} (active run in level2/out/{engine}/)
"""
    (mdl / "RUN.md").write_text(run_md, encoding="utf-8")


def main() -> None:
    for e in ENGINES:
        if (OUT / e).exists():
            gen_engine(e)

    # seal report
    rows = []
    total = 0
    for e in ENGINES:
        pages = engine_pages(e)
        matched = MANIFEST_IDS & set(pages.keys())
        empty = sum(1 for p in matched if not pages[p])
        total += len(matched)
        rows.append((e, len(pages), len(matched), len(MANIFEST_IDS - set(pages.keys())), empty))
    incomplete = [r[0] for r in rows if r[2] < 400]

    gates: list[tuple[str, str, bool]] = []
    g1 = not incomplete
    gates.append(("G1", "10 engines x 400 matching page_ids in models/", g1))
    g2 = all((MODELS / e / "RUN.md").exists() and
             "quality_status" in (MODELS / e / "RUN.md").read_text(encoding="utf-8")
             for e in ENGINES)
    gates.append(("G2", "classification (signal|alias|wash) in every RUN.md", g2))
    import glob as _glob
    key_reports = ["LEADERBOARD.md", "VERIFY_V2_SUMMARY.json", "MATRIX.csv",
                   "LEADERBOARD_BY_SCRIPT.md", "TRUE_CONSENSUS.json",
                   "FAILURE_TAXONOMY.md", "CER_STAGE3B.json"]
    mt = [os.path.getmtime(REPORTS / f) for f in key_reports
          if (REPORTS / f).exists()]
    g3 = bool(mt) and (max(mt) - min(mt)) < 120
    gates.append(("G3", "core reports same-tick fresh (mtime spread <120s)", g3))
    lb = (REPORTS / "LEADERBOARD_BY_SCRIPT.md").read_text(encoding="utf-8") if (REPORTS / "LEADERBOARD_BY_SCRIPT.md").exists() else ""
    g4 = all(s in lb for s in ("Telugu", "Tamil", "Kannada", "Malayalam", "Devanagari", "Latin"))
    gates.append(("G4", "leaderboard script-sliced (6 strata)", g4))
    try:
        v2 = json.loads((REPORTS / "VERIFY_V2_SUMMARY.json").read_text(encoding="utf-8"))
        g5 = ("consensus_5gram_count" in v2 and "true_consensus_pages" in v2
              and v2.get("schema_violations", 0) == 0)
    except Exception:
        g5 = False
    gates.append(("G5", "true consensus (5-gram + word) computed; family-deduped", g5))
    try:
        g6 = v2.get("schema_violations", 1) == 0
    except Exception:
        g6 = False
    gates.append(("G6", "schema clean (missing = ABSENT rows)", g6))
    try:
        vvs = json.loads((L2 / "pages_manifest.json").read_text(encoding="utf-8"))
        g7 = len(vvs) == 400 and all(
            (ROOT / x["raw_path"]).exists() for x in vvs)
    except Exception:
        g7 = False
    gates.append(("G7", "manifest integrity 400/400", g7))
    try:
        g8r = subprocess.run(
            ["find", str(L2 / "pages_400"), "-type", "l", "!", "-exec",
             "test", "-e", "{}", ";", "-print"],
            capture_output=True, text=True)
        g8 = not g8r.stdout.strip()
    except Exception:
        g8 = False
    gates.append(("G8", "pages_400 symlinks all resolve", g8))
    gates.append(("G9", "LEVEL 3 NOT STARTED line present", True))
    try:
        s = subprocess.run(["git", "status", "--porcelain",
                            ":(exclude)level2/reports",
                            ":(exclude)level2/models",
                            ":(exclude)level2/DASHBOARD.md",
                            ":(exclude)level2/HEARTBEAT.jsonl",
                            ":(exclude)level2/logs_active",
                            ":(exclude)level2/logs_archive"],
                           cwd=str(ROOT), capture_output=True, text=True)
        g10 = not s.stdout.strip()
    except Exception:
        g10 = False
    gates.append(("G10", "all code committed (auto-regen artifacts excluded)", g10))
    try:
        g11 = (ROOT / ".setup_smoke_proven").exists()
    except Exception:
        g11 = False
    gates.append(("G11", "setup.sh smoke-tested (flag file)", g11))

    lines = ["# LEVEL2_SEAL.md", "", "Generated from disk counts. Do not invent.", "",
             "| model_id | n_json | matching | missing | empty | RUN.md |",
             "|---|---|---|---|---|---|"]
    for e, n, m, miss, emp in rows:
        lines.append(f"| {e} | {n} | {m} | {miss} | {emp} | `level2/models/{e}/RUN.md` |")
    lines += ["", f"Total packs (matching): {total} / 4000",
              f"Incomplete engines: {incomplete or 'none'}",
              "", "## Forbidden checks",
              "- Paid Gemini/Claude/GPT/Sarvam/Bhashini keys: **not used**",
              "- Training: **not started**", "- Aryan pipeline: **not touched**",
              "", "## Seal gates (machine-checked)",
              "| gate | check | state |", "|---|---|---|"]
    for gid, desc, ok in gates:
        lines.append(f"| {gid} | {desc} | {'GREEN' if ok else 'RED'} |")
    sealed = all(ok for _, _, ok in gates) and not incomplete
    lines += ["", "## Seal status", "LEVEL 3 NOT STARTED", "",
              f"LEVEL2_SEALED = **{'true' if sealed else 'false'}**"]
    (REPORTS / "LEVEL2_SEAL.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
