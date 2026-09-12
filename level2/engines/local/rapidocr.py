"""Adapter: rapidocr (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class RapidOCR(BaseEngine):
    name = "rapidocr"
    version = "rapidocr-onnxruntime 1.4.4"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_rapidocr(Path(png_path), self.lang_hint or "te")


register(RapidOCR())
