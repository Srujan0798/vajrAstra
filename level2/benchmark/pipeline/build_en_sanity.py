#!/usr/bin/env python3
"""Build the EN sanity mini-set (protocol §6.8): 30 human-verified English
pairs from the official dataset, gated by the same rules as the probe.

Read-only wrt the official dataset; writes only to benchmark/pipeline/en_sanity/.
Deterministic: seed 20260926. Run: .venv311/bin/python build_en_sanity.py
"""
from __future__ import annotations

import json
import random
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EN_DIR = ROOT / "Datasets" / "akshardrishti_official" / "English" / "Images And Transcriptions"
DEST = Path(__file__).resolve().parent / "en_sanity"
SEED = 20260926
N = 30
MIN_CHARS = 50
MAX_CTRL_CHARS = 3


def gate(gt: str) -> bool:
    if not gt.strip():
        return False
    non_space = re.sub(r"\s+", "", gt)
    if len(non_space) < MIN_CHARS:
        return False
    ctrl = sum(1 for ch in gt if unicodedata.category(ch) == "Cc" and ch not in "\n\t")
    if ctrl > MAX_CTRL_CHARS:
        return False
    letters = [ch for ch in non_space if ch.isalpha()]
    if not letters:
        return False
    latin = sum(1 for ch in letters if "LATIN" in unicodedata.name(ch, ""))
    if latin / len(letters) < 0.6:
        return False
    return True


def main() -> None:
    pairs = sorted(EN_DIR.glob("*.jpg"))
    cands = []
    for jpg in pairs:
        txt = jpg.with_suffix(".txt")
        if not txt.exists():
            continue
        gt = txt.read_text(encoding="utf-8", errors="replace").strip()
        if gate(gt):
            cands.append((jpg.name, gt))
    rng = random.Random(SEED)
    picks = rng.sample(cands, N)
    img_dir = DEST.parent / "images" / "en"  # shared images tree read by image_path()
    img_dir.mkdir(parents=True, exist_ok=True)
    items = []
    for i, (name, gt) in enumerate(picks, 1):
        src = EN_DIR / name
        iid = f"en_s{i:03d}"
        link = img_dir / f"{iid}.jpg"
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(src.resolve())
        items.append({
            "image_id": iid,
            "image_name": f"{iid}.jpg",
            "language": "en",
            "language_name": "English",
            "script": "Latin",
            "set": "en_sanity",
            "gt": unicodedata.normalize("NFC", gt),
            "gt_source": "akshardrishti_official_pair",
            "source_pdf": None,
            "source_page": None,
            "print_or_hand": "printed",
            "quality": "unknown",
            "has_table": False,
            "mixed_script": False,
        })
    manifest = {
        "created": "2026-09-26",
        "seed": SEED,
        "source": "Datasets/akshardrishti_official/English/Images And Transcriptions (3,500 human pairs)",
        "purpose": "EN sanity reference column (protocol §6.8): if engines fail here, the harness is broken",
        "n_total": len(items),
        "note": "Not part of the 1,227-item probe. Scored separately via --manifest en_sanity/manifest.json.",
        "items": items,
    }
    (DEST / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"en_sanity: {len(items)} items from {len(cands)} gated candidates -> {DEST / 'manifest.json'}")


if __name__ == "__main__":
    main()
