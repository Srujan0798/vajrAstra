"""Adapter: tesseract_bilingual (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class TesseractBilingual(BaseEngine):
    name = "tesseract_bilingual"
    version = "tesseract 5.5.2 (eng+stack bilingual)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_tesseract_bilingual(Path(png_path), self.lang_hint or "te")


register(TesseractBilingual())
