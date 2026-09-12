"""Adapter: easyocr (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class EasyOCR(BaseEngine):
    name = "easyocr"
    version = "easyocr 1.7.2 (all-Indic open reader)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_easyocr(Path(png_path), self.lang_hint or "te")


register(EasyOCR())
