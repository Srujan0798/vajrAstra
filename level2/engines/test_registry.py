"""Registry test: 12 engines registered, stubs LOCKED, tesseract real OCR.

Run (from repo root OR anywhere):
    .venv/bin/python level2/engines/test_registry.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from level2.engines import REGISTRY  # noqa: E402
from level2.engines.level3_stub import LOCKED_MSG  # noqa: E402

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
EXPECTED_STUBS = ["sarvam_batch_api", "bhashini_api"]


def main() -> None:
    t0 = time.time()

    assert len(REGISTRY) == 12, f"expected 12 engines, got {len(REGISTRY)}: {sorted(REGISTRY)}"
    for eid in EXPECTED_LOCAL + EXPECTED_STUBS:
        assert eid in REGISTRY, f"missing engine id: {eid}"
    for eid, eng in REGISTRY.items():
        assert isinstance(eng.name, str) and eng.name == eid, f"name mismatch: {eid} vs {eng.name}"
        assert isinstance(eng.version, str) and eng.version, f"empty version: {eid}"
    print(f"[1] 12/12 engines registered (10 local + 2 stubs) — OK")

    for sid in EXPECTED_STUBS:
        try:
            REGISTRY[sid].run(Path("x.png"))
            raise AssertionError(f"stub {sid} did not raise")
        except NotImplementedError as e:
            assert str(e) == LOCKED_MSG, f"wrong locked message from {sid}: {e}"
            assert "LOCKED" in str(e) and "§5" in str(e)
        print(f"[2] stub {sid} raises LOCKED message — OK")

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
