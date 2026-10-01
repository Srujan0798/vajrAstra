#!/usr/bin/env python3
"""
Re-source shortfall langs by drawing additional clean PDF pages from undrawn candidates.

Strictly obeys all locked gates:
- MIN_CHARS=50, MIN_SCRIPT_RATIO=0.5, MAX_LATIN_RATIO=0.6, MAX_CTRL_CHARS=3
- Strict §6.2 tier scoring (pdf/pair/fill)

Reads:  candidates/<code>.json (must include n_ctrl_chars per item)
Writes: manifest_fragments/<code>.json + manifest.json (only if user-approved)

Usage:
    .venv311/bin/python resource_shortfall.py --code mr
    .venv311/bin/python resource_shortfall.py --code pa --add-to-manifest
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OFFICIAL = ROOT / "Datasets" / "akshardrishti_official"
BENCH = ROOT / "level2" / "benchmark"
PIPE = BENCH / "pipeline"
CAND = PIPE / "candidates"
FRAG = PIPE / "manifest_fragments"
IMAGES = BENCH / "pages"
MANIFEST = BENCH / "manifest_v1.json"

from extract_gt import LANGS, SCRIPT_RANGES, MIN_CHARS, MIN_SCRIPT_RATIO, MAX_LATIN_RATIO, MAX_CTRL_CHARS

SEED = 20260926
DPI = 200


def ranges_for(scripts):
    return [r for s in scripts for r in SCRIPT_RANGES[s]]


def classify(text, target_ranges):
    target = latin = total = 0
    for ch in text:
        if ch.isspace():
            continue
        total += 1
        o = ord(ch)
        if any(lo <= o <= hi for lo, hi in target_ranges):
            target += 1
        elif 0x0041 <= o <= 0x007A:
            latin += 1
    return target, latin, total


def valid_page_strict(text, target_ranges):
    target, latin, total = classify(text, target_ranges)
    if total < MIN_CHARS:
        return False, ("short", total, 0)
    ratio = target / total if total else 0
    if ratio < MIN_SCRIPT_RATIO:
        return False, ("script_ratio", total, ratio)
    if latin / total > MAX_LATIN_RATIO:
        return False, ("latin_ratio", total, latin / total)
    n_ctrl = sum(1 for ch in text if ord(ch) < 32 and ch not in "\n\t\r")
    if n_ctrl > MAX_CTRL_CHARS:
        return False, ("ctrl_chars", total, n_ctrl)
    return True, ("ok", total, ratio)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", required=True, choices=sorted(LANGS))
    ap.add_argument("--add-to-manifest", action="store_true",
                    help="FINAL: only run if user has approved modifying the manifest at 1227.")
    args = ap.parse_args()

    code = args.code
    lang_name, scripts = LANGS[code]
    cand = json.loads((CAND / f"{code}.json").read_text())
    frag = json.loads((FRAG / f"{code}.json").read_text())
    mf = json.loads(MANIFEST.read_text())
    mf_items_mr = [it for it in mf["items"] if it["language"] == code]
    target_n = 100

    print(f"== {code} ({lang_name}) ==")
    print(f"candidates:    {len(cand['items'])}")
    print(f"fragment:      {len(frag['items'])}")
    print(f"manifest:      {len(mf_items_mr)}")
    print(f"target:        {target_n}")
    print(f"gap to target: {target_n - len(frag['items'])}")

    if len(frag["items"]) >= target_n:
        print("ALREADY AT TARGET — no re-source needed")
        return 0

    drawn_keys = set((it["source_pdf"], it["source_page"]) for it in frag["items"])
    rng = random.Random(SEED + hash(code) % 10000)
    undrawn = [it for it in cand["items"] if (it["pdf"], it["page"]) not in drawn_keys]
    rng.shuffle(undrawn)
    print(f"undrawn candidates: {len(undrawn)}")

    n_target = target_n
    new_items = []
    failures = {"short": 0, "script_ratio": 0, "latin_ratio": 0, "ctrl_chars": 0, "page_error": 0, "ok": 0}

    for c in undrawn:
        if len(frag["items"]) + len(new_items) >= n_target:
            break
        pdf_path = OFFICIAL / c["pdf"]
        try:
            doc = pymupdf.open(pdf_path)
            page = doc[c["page"]]
            text = page.get_text().strip()
            zoom = DPI / 72.0
            ok, info = valid_page_strict(text, ranges_for(scripts))
            if not ok:
                tag = info[0]
                failures[tag] = failures.get(tag, 0) + 1
                doc.close()
                continue
            # Use IDs starting at 101 (or 100 + count of existing fragment items)
            # to avoid collision with already-drawn items mr_o001..mr_o100.
            idx = 100 + len(frag["items"]) + len(new_items) + 1
            image_id = f"{code}_o{idx:03d}"
            dest = IMAGES / code / f"{image_id}.png"
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
                pix.save(str(dest))
            doc.close()
            failures["ok"] += 1
            new_items.append({
                "image_id": image_id,
                "language": code,
                "language_name": lang_name,
                "script": scripts[0],
                "set": "official_pdf",
                "gt": text,
                "gt_source": "official_pdf_layer",
                "source_pdf": c["pdf"],
                "source_page": c["page"],
                "print_or_hand": "printed",
                "quality": "unknown",
                "has_table": False,
                "mixed_script": False,
            })
        except Exception as e:
            failures["page_error"] += 1
            continue

    print(f"\nRESULTS — strict-gate validation of {len(undrawn)} undrawn:")
    for k, v in failures.items():
        print(f"  {k:>15s}: {v}")
    print(f"\nNEW clean items drawn: {len(new_items)} (target gap={target_n - len(frag['items'])})")
    if len(new_items) < target_n - len(frag["items"]):
        print(f"  STILL SHORT by {target_n - len(frag['items']) - len(new_items)} — pool cannot fully fill target")

    if args.add_to_manifest and new_items:
        # Final: only if user has approved modifying manifest at 1227
        print(f"\n=== APPLYING TO MANIFEST (user-approved) ===")
        new_image_ids = [it["image_id"] for it in new_items]
        # Extend fragment
        frag["items"].extend(new_items)
        frag["n_drawn"] = len(frag["items"])
        frag["n_official_pdf"] = sum(1 for i in frag["items"] if i["set"] == "official_pdf")
        (FRAG / f"{code}.json").write_text(json.dumps(frag, ensure_ascii=False, indent=2))
        # Extend manifest
        mf["items"].extend(new_items)
        mf["n_total"] = len(mf["items"])
        MANIFEST.write_text(json.dumps(mf, ensure_ascii=False, indent=2))
        print(f"  fragment {code}.json: now {len(frag['items'])} items")
        print(f"  manifest.json: now {len(mf['items'])} items")
        print(f"  new image_ids: {new_image_ids[:5]}{'...' if len(new_image_ids) > 5 else ''}")
    elif new_items and not args.add_to_manifest:
        print(f"\nDry-run only. Use --add-to-manifest to apply (requires user approval).")

    return 0


if __name__ == "__main__":
    sys.exit(main())