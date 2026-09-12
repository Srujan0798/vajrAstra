"""Adapter: anuvaad_tesseract (local, free; project-anuvaad S3 weights)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class AnuvaadTesseract(BaseEngine):
    name = "anuvaad_tesseract"
    version = "anuvaad tessdata + tesseract 5.5.2"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_anuvaad_tesseract(Path(png_path), self.lang_hint or "te")


register(AnuvaadTesseract())
