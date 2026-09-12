"""Adapter: paddleocr_indic (local, free; needs .venv311)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class PaddleOCRIndic(BaseEngine):
    name = "paddleocr_indic"
    version = "paddleocr 3.7.0 / paddlepaddle 3.3.1"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_paddleocr_indic(Path(png_path), self.lang_hint or "te")


register(PaddleOCRIndic())
