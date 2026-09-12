"""Adapter: doctr (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class DocTR(BaseEngine):
    name = "doctr"
    version = "python-doctr 1.1.0 (crnn_vgg16_bn)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_doctr(Path(png_path), self.lang_hint or "te")


register(DocTR())
