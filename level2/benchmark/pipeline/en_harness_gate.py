#!/usr/bin/env python3
"""
EN harness sanity gate (4-page) — added 2026-09-28 orchestrator (level2/benchmark).

Purpose: validate that the EN harness is wired correctly in <5s without burning
CPU on the full 30-item en_sanity column. If any of the 4 gates fails, the
engine has a wiring problem (broken image_path, broken model lookup, broken
nfc(), broken TESS_LANG). NEVER infers a model — honest-empty is acceptable
provided the harness completed without raising.

Usage:
    cd /Users/srujansai/Desktop/South/level2/benchmark/pipeline
    ../../.venv311/bin/python en_harness_gate.py --engine rapidocr
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCH = ROOT / "level2" / "benchmark"
PIPE = BENCH / "pipeline"
EN_MANIFEST = PIPE / "en_sanity" / "manifest.json"

# Map: engine → function name in run_probe.py
ENGINE_RUNNERS = {
    "rapidocr": "ocr_rapidocr",
    "tesseract_bilingual": "ocr_tesseract_bilingual",
    "tesseract_indic": "ocr_tesseract_indic",
    "doctr": "ocr_doctr",
    "easyocr": "ocr_easyocr",
    "indicphotoocr": "ocr_indicphotoocr",
    "anuvaad_tesseract": "ocr_anuvaad_tesseract",
    "openbharatocr": "ocr_openbharatocr",
    "paddleocr_indic": "ocr_paddleocr_indic",
    "surya": "ocr_surya",
    "sarvam_vision": "ocr_sarvam_vision",
}


def gate(pack: dict, runner) -> dict:
    """Run the 4 gates for one EN item. NEVER raises — captures errors."""
    t0 = time.time()
    text = ""
    error = None
    try:
        text = runner(pack)
    except Exception as e:  # noqa: BLE001 — gate must report, not crash
        error = repr(e)[:200]
    ms = int((time.time() - t0) * 1000)
    # gate-1: harness completed (no exception OR exception text captures the bug)
    g1_pass = error is None
    # gate-2: response ms < 30s (broken harness = infinite loop / OOM)
    g2_pass = ms < 30_000
    # gate-3: text type is str (no NoneType leaked through)
    g3_pass = isinstance(text, str)
    # gate-4: honest-empty allowed (model not cached); if cached, expect ≥50 chars
    gt_len = len(pack.get("gt") or "")
    if text:
        g4_pass = len(text) >= min(50, gt_len // 4)
    else:
        # empty text + no error → honest-empty (model not cached). ACCEPT.
        g4_pass = error is None
    return {
        "image_id": pack["image_id"],
        "gt_len": gt_len,
        "pred_len": len(text),
        "ms": ms,
        "error": error,
        "gate1_completed": g1_pass,
        "gate2_under_30s": g2_pass,
        "gate3_str_text": g3_pass,
        "gate4_honest_or_substantive": g4_pass,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", default="rapidocr")
    ap.add_argument("--manifest", default=str(EN_MANIFEST))
    args = ap.parse_args()

    if not Path(args.manifest).exists():
        print(f"EN manifest missing: {args.manifest}")
        return 1

    if args.engine not in ENGINE_RUNNERS:
        print(f"Unknown engine: {args.engine}; choose from {sorted(ENGINE_RUNNERS)}")
        return 1

    sys.path.insert(0, str(PIPE))
    import run_probe
    runner = getattr(run_probe, ENGINE_RUNNERS[args.engine])

    manifest = json.loads(Path(args.manifest).read_text())
    items = manifest["items"][:4]  # 4-page gate

    print(f"EN harness gate — engine={args.engine}, items=4")
    rows = [gate(it, runner) for it in items]
    for r in rows:
        verdict = "PASS" if all([r["gate1_completed"], r["gate2_under_30s"],
                                  r["gate3_str_text"], r["gate4_honest_or_substantive"]]) else "FAIL"
        print(f"  {verdict} {r['image_id']}: "
              f"pred_len={r['pred_len']}/{r['gt_len']} ms={r['ms']} "
              f"err={r['error'] or '—'}")

    n_pass = sum(1 for r in rows
                 if all([r["gate1_completed"], r["gate2_under_30s"],
                          r["gate3_str_text"], r["gate4_honest_or_substantive"]]))
    print(f"\n{n_pass}/4 gates passed for {args.engine}")
    if n_pass == 4:
        print("OK — full EN sanity column is safe to run")
        return 0
    print("BLOCKED — fix harness before full EN sanity run")
    return 2


if __name__ == "__main__":
    sys.exit(main())