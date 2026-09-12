"""Adapter: surya (local, free)."""
from __future__ import annotations

from pathlib import Path

from .. import BaseEngine, register


class Surya(BaseEngine):
    name = "surya"
    version = "surya-ocr 0.22.1 (surya-2, block-mode html)"

    def run(self, png_path: Path) -> str:
        from level2 import run_engine

        return run_engine.ocr_surya(Path(png_path), self.lang_hint or "te")


register(Surya())
