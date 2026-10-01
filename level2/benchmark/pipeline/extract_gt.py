#!/usr/bin/env python3
"""
Extract GT candidates for one probe language from the official hackathon dataset.

Phase 1 of the W3 probe protocol (level2/benchmark/docs/AGENT_PROTOCOL.md).

Scans every PDF under Datasets/akshardrishti_official/<Language>/, extracts the
text layer of every page, applies the honesty gates, and writes the candidate
pool to level2/benchmark/pipeline/candidates/<code>.json. Direct image+txt pairs under
"Images and transcriptions/" are also collected.

No downloads. No network. Writes candidates/ only.

Usage:
  python extract_gt.py --code as
  python extract_gt.py --code hi --max-pages 0   # 0 = no page cap
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "Datasets" / "akshardrishti_official"
BENCH = ROOT / "level2" / "benchmark"
CAND = BENCH / "pipeline" / "candidates"

# Unicode script ranges used for validation (mojibake / wrong-script gate).
SCRIPT_RANGES = {
    "deva": [(0x0900, 0x097F)],              # hi mr ne sa brx mai doi kok
    "beng": [(0x0980, 0x09FF)],               # bn as (mni when Bengali script)
    "gujr": [(0x0A80, 0x0AFF)],              # gu
    "guru": [(0x0A00, 0x0A7F)],              # pa
    "orya": [(0x0B00, 0x0B7F)],              # or
    "arab": [(0x0600, 0x06FF), (0x0750, 0x077F), (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)],  # ur sd ks
    "olck": [(0x1C50, 0x1C7F)],              # sat
    "mtei": [(0xABC0, 0xABFF)],               # mni Meitei Mayek
}

LANGS = {
    "as": ("Assamese", ["beng"]),
    "bn": ("Bengali", ["beng"]),
    "brx": ("Bodo", ["deva"]),
    "doi": ("Dogri", ["deva"]),
    "gu": ("Gujarati", ["gujr"]),
    "hi": ("Hindi", ["deva"]),
    "ks": ("Kashmiri", ["arab"]),
    "kok": ("Konkani", ["deva"]),
    "mai": ("Maithili", ["deva"]),
    "mni": ("Manipuri", ["beng", "mtei"]),
    "mr": ("Marathi", ["deva"]),
    "ne": ("Nepali", ["deva"]),
    "or": ("Odia", ["orya"]),
    "pa": ("Punjabi", ["guru"]),
    "sa": ("Sanskrit", ["deva"]),
    "sat": ("Santali", ["olck"]),
    "sd": ("Sindhi", ["arab"]),
    "ur": ("Urdu", ["arab"]),
}

MIN_CHARS = 50          # a candidate page must have at least this many chars
MIN_SCRIPT_RATIO = 0.5  # target-script chars / all non-space chars
MAX_LATIN_RATIO = 0.6   # Latin chars / all non-space chars (blocks all-English pages)
MAX_CTRL_CHARS = 3       # C0 control chars (legacy-font mojibake marker); >3 = corrupt layer


def classify(text: str, target_ranges: list[tuple[int, int]]) -> tuple[int, int, int]:
    """Return (target_chars, latin_chars, total_chars) for non-whitespace chars."""
    target = latin = total = 0
    for ch in text:
        if ch.isspace():
            continue
        total += 1
        o = ord(ch)
        if any(lo <= o <= hi for lo, hi in target_ranges):
            target += 1
        elif 0x0041 <= o <= 0x007A:  # A-Z a-z
            latin += 1
    return target, latin, total


def valid_page(text: str, target_ranges: list[tuple[int, int]]) -> tuple[bool, float, int]:
    target, latin, total = classify(text, target_ranges)
    if total < MIN_CHARS:
        return False, 0.0, total
    ratio = target / total
    if ratio < MIN_SCRIPT_RATIO:
        return False, ratio, total
    if latin / total > MAX_LATIN_RATIO:
        return False, ratio, total
    n_ctrl = sum(1 for ch in text if ord(ch) < 32 and ch not in "\n\t\r")
    if n_ctrl > MAX_CTRL_CHARS:
        return False, ratio, total  # legacy-font mojibake layer — reject
    return True, ratio, total


def scan_language(code: str, max_pages: int) -> dict:
    lang_name, scripts = LANGS[code]
    ranges = [r for s in scripts for r in SCRIPT_RANGES[s]]
    lang_dir = OFFICIAL / lang_name
    if not lang_dir.is_dir():
        raise SystemExit(f"missing language dir: {lang_dir}")

    pdfs = sorted(str(p) for p in lang_dir.rglob("*.pdf"))
    items: list[dict] = []
    pages = with_text = rejected_mojibake = rejected_short = errors = 0
    err_list: list[dict] = []

    for pdf in pdfs:
        try:
            doc = pymupdf.open(pdf)
        except Exception as e:
            errors += 1
            err_list.append({"pdf": Path(pdf).name, "error": str(e)[:120]})
            continue
        for pno in range(doc.page_count):
            if max_pages and pages >= max_pages:
                doc.close()
                break
            pages += 1
            try:
                text = doc[pno].get_text().strip()
            except Exception:
                rejected_short += 1
                continue
            if len(text) <= 20:
                continue
            with_text += 1
            ok, ratio, total = valid_page(text, ranges)
            if ok:
                items.append(
                    {
                        "pdf": str(Path(pdf).relative_to(OFFICIAL)),
                        "page": pno,
                        "chars": len(text),
                        "script_ratio": round(ratio, 3),
                    }
                )
            elif ratio < MIN_SCRIPT_RATIO and total >= MIN_CHARS:
                rejected_mojibake += 1
            else:
                rejected_short += 1
        doc.close()
        if max_pages and pages >= max_pages:
            break

    # Direct image+txt pairs (official GT transcriptions).
    pairs: list[dict] = []
    for img in sorted(lang_dir.rglob("*.jpg")) + sorted(lang_dir.rglob("*.jpeg")):
        txt = img.with_suffix(".txt")
        if txt.exists():
            try:
                gt = txt.read_text(encoding="utf-8").strip()
            except Exception:
                continue
            if len(gt) >= 20:
                pairs.append(
                    {
                        "image": str(img.relative_to(OFFICIAL)),
                        "txt": str(txt.relative_to(OFFICIAL)),
                        "chars": len(gt),
                    }
                )

    return {
        "language": code,
        "language_name": lang_name,
        "scripts": scripts,
        "pdfs": len(pdfs),
        "pages_scanned": pages,
        "pages_with_text": with_text,
        "candidates": len(items),
        "rejected_mojibake_or_wrong_script": rejected_mojibake,
        "rejected_short_or_latin": rejected_short,
        "pdf_errors": errors,
        "pdf_error_list": err_list[:10],
        "pairs": len(pairs),
        "items": items,
        "pair_items": pairs,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", required=True, choices=sorted(LANGS))
    ap.add_argument("--max-pages", type=int, default=0, help="cap pages scanned (0 = all)")
    args = ap.parse_args()

    result = scan_language(args.code, args.max_pages)
    CAND.mkdir(parents=True, exist_ok=True)
    out = CAND / f"{args.code}.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2))

    print(f"language:            {result['language_name']}")
    print(f"pdfs:                {result['pdfs']}")
    print(f"pages scanned:       {result['pages_scanned']}")
    print(f"pages with text:     {result['pages_with_text']}")
    print(f"clean candidates:    {result['candidates']}")
    print(f"rejected (mojibake): {result['rejected_mojibake_or_wrong_script']}")
    print(f"rejected (short/latin): {result['rejected_short_or_latin']}")
    print(f"pdf errors:          {result['pdf_errors']}")
    print(f"direct pairs:        {result['pairs']}")
    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
