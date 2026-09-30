#!/usr/bin/env python3
"""Shared read-only loader for Round-1 research generators.

Rebuilds the sealed CER basis WITHOUT touching shared pipeline files (L10):
- CER functions, engine roster and family map are IMPORTED from verify_v2.py
  (read-only import; verify_v2.main() is never called).
- GT = PDF text layer, taken from training_assets/sft_noisy_to_gold.jsonl
  (written by training_assets_gen.py from the same pymupdf layer that
  CER_STAGE3B.json uses), so this works on checkouts without Datasets/.
- Engine text = level2/out/<engine>/<lang>/<page_id>.json via pack_text().

Clean basis (mirrors verify_v2 GT-quality gate):
  dense  = normalized GT >= 200 chars
  mojibake = Indic dominant_script and PDF layer < 15% Indic codepoints
  clean  = dense and not mojibake
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path

L2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(L2))

import verify_v2 as V  # noqa: E402  (read-only import, L10-safe)

ENGINES = list(V.ENGINES)
family_of = V.family_of
cer_norm = V.cer_norm
edit_distance = V.edit_distance
pack_text = V.pack_text

SFT = L2 / "training_assets" / "sft_noisy_to_gold.jsonl"
DPO = L2 / "training_assets" / "preference_pairs_dpo.jsonl"
MANIFEST = L2 / "pages_manifest.json"
OUT = L2 / "out"
INDIC = ("Telugu", "Tamil", "Kannada", "Malayalam", "Devanagari")


@lru_cache(maxsize=1)
def manifest() -> dict[str, dict]:
    return {m["page_id"]: m for m in json.loads(MANIFEST.read_text(encoding="utf-8"))}


@lru_cache(maxsize=1)
def gold_raw() -> dict[str, str]:
    """page_id -> raw PDF-layer text (dense pages only; thin pages absent)."""
    g: dict[str, str] = {}
    with SFT.open(encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            g.setdefault(r["page_id"], r["gold_text"])
    return g


def is_mojibake(pid: str) -> bool:
    dom = manifest()[pid].get("dominant_script")
    raw = (gold_raw().get(pid) or "").strip()
    if dom not in INDIC or not raw:
        return False
    n_indic = sum(1 for c in raw if 0x0900 <= ord(c) <= 0x0DFF)
    return n_indic / len(raw) < 0.15


def indic_share(text: str) -> float:
    s = "".join(text.split())
    return sum(1 for c in s if 0x0900 <= ord(c) <= 0x0DFF) / len(s) if s else 0.0


# One representative per independent family (L6: tesseract family = 1 vote).
FAMILY_REPS = ["tesseract_indic", "easyocr", "paddleocr_indic", "indicphotoocr",
               "rapidocr", "doctr", "surya"]


def engines_read_indic(pid: str) -> int:
    """How many of the 7 independent families output >= 50% Indic text."""
    return sum(1 for e in FAMILY_REPS if indic_share(engine_text(e, pid)) >= 0.5)


def gt_script_mismatch(pid: str) -> bool:
    """Tag-independent mojibake gate (Round-1 P0 finding): the PDF layer is
    < 15% Indic while a majority (>= 4 of 7) of independent engine families
    read the page as Indic => the layer is a legacy-font encoding, not GT.
    Catches mojibake pages whose dominant_script was mis-derived as Latin."""
    return indic_share(gold_raw().get(pid) or "") < 0.15 and engines_read_indic(pid) >= 4


def observed_script(pid: str) -> str:
    """Script actually read by the independent families (for strata).
    If >= 2 families emit mostly-Indic text, the plurality Indic script among
    THOSE families wins — engines with no model for a script (paddle ml, rapidocr
    ml, doctr) emit Latin and must not outvote the readers. Otherwise plurality."""
    votes, indic_votes = [], []
    for e in FAMILY_REPS:
        s = "".join(engine_text(e, pid).split())
        if not s:
            continue
        cnt = {k: sum(1 for c in s if lo <= ord(c) <= hi) for k, (lo, hi) in V.SCRIPT_RANGES.items()}
        top = max(sorted(cnt), key=cnt.get)
        votes.append(top)
        if indic_share(s) >= 0.5 and top != "Latin":
            indic_votes.append(top)
    pool = indic_votes if len(indic_votes) >= 2 else votes
    return max(sorted(set(pool)), key=pool.count) if pool else "none"


@lru_cache(maxsize=1)
def basis() -> dict[str, list[str]]:
    """Sealed basis ('clean', n=126) plus the Round-1 corrected basis:
    'script_mismatch' = clean pages failing the tag-independent gate,
    'clean_v2' = clean minus script_mismatch."""
    dense = sorted(p for p, t in gold_raw().items() if len(cer_norm(t)) >= 200)
    moj = [p for p in dense if is_mojibake(p)]
    clean = [p for p in dense if p not in set(moj)]
    thin = sorted(set(manifest()) - set(dense))
    mism = [p for p in clean if gt_script_mismatch(p)]
    clean_v2 = [p for p in clean if p not in set(mism)]
    return {"dense": dense, "mojibake": moj, "clean": clean, "thin": thin,
            "script_mismatch": mism, "clean_v2": clean_v2}


@lru_cache(maxsize=None)
def engine_text(engine: str, pid: str) -> str:
    lang = manifest()[pid]["lang"]
    p = OUT / engine / lang / f"{pid}.json"
    return ((pack_text(p) if p.exists() else "") or "").strip()


def cer(engine: str, pid: str) -> float:
    """Uncapped CER vs PDF layer, exactly as verify_v2 (empty text = 1.0)."""
    gtn = cer_norm(gold_raw()[pid])
    txt = engine_text(engine, pid)
    if not txt:
        return 1.0
    return round(edit_distance(cer_norm(txt), gtn) / len(gtn), 4)


@lru_cache(maxsize=1)
def cer_matrix() -> dict[str, dict[str, float]]:
    """page_id -> engine -> CER on the clean basis."""
    return {pid: {e: cer(e, pid) for e in ENGINES} for pid in basis()["clean"]}


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
