"""Adapter: tesseract_indic (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class TesseractIndic(BaseEngine):
    name = "tesseract_indic"
    version = "tesseract 5.5.2 (tel+hin+eng open stack)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_tesseract_indic(Path(png_path), self.lang_hint or "te")


register(TesseractIndic())
