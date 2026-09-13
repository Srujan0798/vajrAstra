"""Registry test: 12 engines registered, Level-3 adapters dry-run predictably, tesseract real OCR.

Run (from repo root OR anywhere):
    .venv/bin/python level2/engines/test_registry.py
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from level2.engines import REGISTRY  # noqa: E402
from level2.engines.bhashini_api import DRY_RUN_TEXT as BHASHINI_DRY  # noqa: E402
from level2.engines.sarvam_api import DRY_RUN_TEXT as SARVAM_DRY  # noqa: E402

EXPECTED_LOCAL = [
    "tesseract_indic",
    "openbharatocr",
    "easyocr",
    "paddleocr_indic",
    "indicphotoocr",
    "rapidocr",
    "tesseract_bilingual",
    "doctr",
    "surya",
    "anuvaad_tesseract",
]
EXPECTED_L3 = ["sarvam_api", "bhashini_api"]


def main() -> None:
    t0 = time.time()

    assert len(REGISTRY) == 12, f"expected 12 engines, got {len(REGISTRY)}: {sorted(REGISTRY)}"
    for eid in EXPECTED_LOCAL + EXPECTED_L3:
        assert eid in REGISTRY, f"missing engine id: {eid}"
    for eid, eng in REGISTRY.items():
        assert isinstance(eng.name, str) and eng.name == eid, f"name mismatch: {eid} vs {eng.name}"
        assert isinstance(eng.version, str) and eng.version, f"empty version: {eid}"
    print(f"[1] 12/12 engines registered (10 local + 2 Level-3 real adapters) — OK")

    for sid, dry in (("sarvam_api", SARVAM_DRY), ("bhashini_api", BHASHINI_DRY)):
        assert os.environ.get("SARVAM_API_KEY") is None and os.environ.get("BHASHINI_API_KEY") is None, "real key in env — not allowed in tests"
        text = REGISTRY[sid].run(Path("x.png"))
        assert text == dry, f"wrong dry-run output from {sid}: {text!r}"
        assert "<dry-run" in text and "not configured" in text, f"unlabeled dry-run from {sid}"
        print(f"[2] {sid} dry-run (no key) returns labeled synthetic text — OK")

    png = ROOT / "level2" / "renders_shared" / "te_001.png"
    assert png.exists(), f"test page missing: {png}"
    text = REGISTRY["tesseract_indic"].run(png)
    assert len(text) > 100, f"tesseract_indic returned only {len(text)} chars"
    print(f"[3] tesseract_indic real OCR on te_001.png: {len(text)} chars (>100) — OK")
    print(f"    sample: {text.strip()[:80]!r}")

    ids = ", ".join(sorted(REGISTRY))
    print(f"[4] registry: {ids}")
    print(f"ALL PASS in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
