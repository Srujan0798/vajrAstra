#!/usr/bin/env python3
"""
Build the W3 probe manifest: draw 100 samples per language, materialize images,
fill shortfall cells from the leftover Sarvam-bench images, and merge fragments.

Phase 2-3 of the W3 probe protocol (level2/benchmark/docs/AGENT_PROTOCOL.md).

Reads  level2/benchmark/pipeline/candidates/<code>.json      (from extract_gt.py)
Reads  level2/benchmark/manifest_v1.json              (only for Sarvam-fill GT)
Writes level2/benchmark/pipeline/manifest_fragments/<code>.json
       level2/benchmark/pages/<code>/<code>_oNNN.png   (PDF renders, 200 dpi)
       level2/benchmark/pages/<code>/<code>_dNNN.jpg    (symlinks to pair images)
       level2/benchmark/manifest_v1.json                 (with --merge)

No downloads. No network. Writes benchmark/ only.

Usage:
  python build_manifest.py --code as          # draw + materialize one language
  python build_manifest.py --merge            # combine all fragments -> manifest.json
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

from extract_gt import LANGS, MIN_CHARS, MIN_SCRIPT_RATIO, MAX_LATIN_RATIO, valid_page

N_PER_LANG = 100
SEED = 20260926
DPI = 200

SCRIPT_NAME = {
    "deva": "Devanagari", "beng": "Bengali-Assamese", "gujr": "Gujarati",
    "guru": "Gurmukhi", "orya": "Odia", "arab": "Perso-Arabic",
    "olck": "Ol Chiki", "mtei": "Meitei Mayek",
}


def draw_pdf_pages(items: list[dict], n: int, rng: random.Random) -> list[dict]:
    """Stratified draw: round-robin across source PDFs, shuffled within each."""
    by_pdf: dict[str, list[dict]] = {}
    for it in items:
        by_pdf.setdefault(it["pdf"], []).append(it)
    for pdf in by_pdf:
        rng.shuffle(by_pdf[pdf])
    pdf_order = sorted(by_pdf, key=lambda p: rng.random())
    drawn: list[dict] = []
    while len(drawn) < n and any(by_pdf.values()):
        for pdf in pdf_order:
            if by_pdf[pdf] and len(drawn) < n:
                drawn.append(by_pdf[pdf].pop())
    return drawn


def draw_pairs(pairs: list[dict], n: int, rng: random.Random) -> list[dict]:
    pool = list(pairs)
    rng.shuffle(pool)
    return pool[:n]


def sarvam_fill_gt(code: str) -> dict[str, str]:
    """image_id -> gt from the existing manifest (Sarvam bench leftovers)."""
    if not MANIFEST.exists():
        return {}
    data = json.loads(MANIFEST.read_text())
    out = {}
    for it in data.get("items", []):
        if it.get("language") == code and it.get("gt"):
            out[it["image_id"]] = it["gt"]
    return out


def materialize_pdf_page(code: str, idx: int, item: dict) -> dict:
    """Rasterize one official PDF page and extract its validated text layer."""
    pdf_path = OFFICIAL / item["pdf"]
    doc = pymupdf.open(pdf_path)
    page = doc[item["page"]]
    text = page.get_text().strip()
    doc.close()

    lang_name, scripts = LANGS[code]
    ranges = [r for s in scripts for r in _ranges_for(scripts)]
    ok, ratio, total = valid_page(text, ranges)
    if not ok:
        return {"error": f"page failed revalidation (ratio={ratio:.2f}, chars={total})"}

    image_id = f"{code}_o{idx:03d}"
    dest = IMAGES / code / f"{image_id}.png"
    doc = pymupdf.open(pdf_path)
    pg = doc[item["page"]]
    zoom = DPI / 72.0
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
    dest.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(dest))
    doc.close()

    return {
        "image_id": image_id,
        "language": code,
        "language_name": lang_name,
        "script": SCRIPT_NAME[scripts[0]],
        "set": "official_pdf",
        "gt": text,
        "gt_source": "official_pdf_layer",
        "source_pdf": item["pdf"],
        "source_page": item["page"],
        "print_or_hand": "printed",
        "quality": "unknown",
        "has_table": False,
        "mixed_script": False,
    }


def _ranges_for(scripts: list[str]) -> list[tuple[int, int]]:
    from extract_gt import SCRIPT_RANGES
    return [r for s in scripts for r in SCRIPT_RANGES[s]]


def materialize_pair(code: str, idx: int, pair: dict) -> dict:
    """Symlink an official image+txt pair into the probe images dir."""
    lang_name, scripts = LANGS[code]
    image_id = f"{code}_d{idx:03d}"
    src = OFFICIAL / pair["image"]
    ext = src.suffix.lower()  # keep the real extension (.jpg / .jpeg)
    dest = IMAGES / code / f"{image_id}{ext}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.symlink_to(src.resolve())
    gt = (OFFICIAL / pair["txt"]).read_text(encoding="utf-8").strip()

    return {
        "image_id": image_id,
        "language": code,
        "language_name": lang_name,
        "script": SCRIPT_NAME[scripts[0]],
        "set": "official_pair",
        "gt": gt,
        "gt_source": "official_pair_txt",
        "source_pdf": None,
        "source_page": None,
        "print_or_hand": "printed",
        "quality": "clean",
        "has_table": False,
        "mixed_script": False,
    }


def build_language(code: str, n: int) -> dict:
    cand_path = CAND / f"{code}.json"
    if not cand_path.exists():
        raise SystemExit(f"run extract_gt.py --code {code} first")
    cand = json.loads(cand_path.read_text())
    rng = random.Random(SEED)
    lang_name, scripts = LANGS[code]

    items: list[dict] = []
    failures: list[dict] = []

    # 1. Direct pairs first (human GT, highest quality).
    if cand["pair_items"]:
        for idx, pair in enumerate(draw_pairs(cand["pair_items"], n, rng), 1):
            items.append(materialize_pair(code, idx, pair))

    # 2. PDF-layer pages for the remainder.
    if len(items) < n and cand["items"]:
        need = n - len(items)
        drawn = draw_pdf_pages(cand["items"], need, rng)
        for idx, it in enumerate(drawn, len(items) + 1):
            res = materialize_pdf_page(code, idx, it)
            if "error" in res:
                failures.append({"source": it, **res})
            else:
                items.append(res)

    # 3. Shortfall -> Sarvam-bench leftovers (honest gt_source).
    if len(items) < n:
        gt_map = sarvam_fill_gt(code)
        fill_dir = IMAGES / code
        fills = sorted(
            p for p in fill_dir.glob("*.jpg") if p.name.split(".")[0] in gt_map
        )
        rng.shuffle(fills)
        for jpg in fills:
            if len(items) >= n:
                break
            image_id = jpg.name.split(".")[0]
            items.append(
                {
                    "image_id": image_id,
                    "language": code,
                    "language_name": lang_name,
                    "script": SCRIPT_NAME[scripts[0]],
                    "set": "sarvam_fill",
                    "gt": gt_map[image_id],
                    "gt_source": "sarvam_bench",
                    "source_pdf": None,
                    "source_page": None,
                    "print_or_hand": "printed",
                    "quality": "unknown",
                    "has_table": False,
                    "mixed_script": False,
                }
            )

    frag = {
        "language": code,
        "language_name": lang_name,
        "n_target": n,
        "n_drawn": len(items),
        "n_official_pairs": sum(1 for i in items if i["set"] == "official_pair"),
        "n_official_pdf": sum(1 for i in items if i["set"] == "official_pdf"),
        "n_sarvam_fill": sum(1 for i in items if i["set"] == "sarvam_fill"),
        "n_failures": len(failures),
        "failures": failures[:10],
        "seed": SEED,
        "items": items,
    }
    FRAG.mkdir(parents=True, exist_ok=True)
    (FRAG / f"{code}.json").write_text(json.dumps(frag, ensure_ascii=False, indent=2))
    return frag


def merge() -> None:
    if not FRAG.is_dir():
        raise SystemExit("no fragments directory")
    codes = sorted(p.stem for p in FRAG.glob("*.json"))
    all_items: list[dict] = []
    for code in codes:
        frag = json.loads((FRAG / f"{code}.json").read_text())
        all_items.extend(frag["items"])
    manifest = {
        "created": "2026-09-26",
        "seed": SEED,
        "source": "Datasets/akshardrishti_official (user-provided official hackathon data)",
        "n_per_language": N_PER_LANG,
        "languages_probe": codes,
        "n_total": len(all_items),
        "note": "W3 probe: 100/lang x 18 languages. GT from official pairs, validated PDF "
                "text layers, and Sarvam-bench fill for shortfall cells (Dogri, Santali). "
                "Do not train on this split. Do not write into level2/out/.",
        "items": all_items,
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"merged {len(codes)} fragments, {len(all_items)} items -> {MANIFEST}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", choices=sorted(LANGS))
    ap.add_argument("--n", type=int, default=N_PER_LANG)
    ap.add_argument("--merge", action="store_true")
    args = ap.parse_args()

    if args.merge:
        merge()
        return
    if not args.code:
        ap.error("--code or --merge required")

    frag = build_language(args.code, args.n)
    print(f"language:        {frag['language_name']}")
    print(f"drawn:           {frag['n_drawn']}/{frag['n_target']}")
    print(f"official pairs:  {frag['n_official_pairs']}")
    print(f"official pdf:    {frag['n_official_pdf']}")
    print(f"sarvam fill:     {frag['n_sarvam_fill']}")
    print(f"failures:        {frag['n_failures']}")
    print(f"saved -> {FRAG / (args.code + '.json')}")


if __name__ == "__main__":
    main()
