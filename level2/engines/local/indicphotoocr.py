"""Adapter: indicphotoocr (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class IndicPhotoOCR(BaseEngine):
    name = "indicphotoocr"
    version = "IndicPhotoOCR IIIT-H (parseq trust-patched)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_indicphotoocr(Path(png_path), self.lang_hint or "te")


register(IndicPhotoOCR())
