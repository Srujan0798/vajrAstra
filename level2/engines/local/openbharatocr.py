"""Adapter: openbharatocr (local, free; tesseract mirror path)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class OpenBharatOCR(BaseEngine):
    name = "openbharatocr"
    version = "openbharatocr 0.4.3 (tesseract mirror path documented)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_openbharatocr(Path(png_path), self.lang_hint or "te")


register(OpenBharatOCR())
