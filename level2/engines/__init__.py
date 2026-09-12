"""vajraAstra Level-2/3 engine socket: BaseEngine + REGISTRY.

Level-3 engines (Sarvam, Bhashini, ...) drop in here with zero harness
surgery. Project law: level2/ULTIMATE_HYBRID_CONCERN.md §5 — Level 3 is
LOCKED until Level 2 seals.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class BaseEngine(ABC):
    """Contract every OCR engine (local or paid-API) must satisfy."""

    name: str = "base"
    version: str = "0.0.0"
    lang_hint: Optional[str] = None

    @abstractmethod
    def run(self, png_path: Path) -> str:
        """OCR a rendered page PNG and return the extracted text (NFC)."""
        raise NotImplementedError

    def label(self) -> str:
        return f"{self.name} v{self.version}"


REGISTRY: dict[str, BaseEngine] = {}


def register(engine: BaseEngine) -> BaseEngine:
    if engine.name in REGISTRY:
        raise ValueError(f"duplicate engine id: {engine.name}")
    REGISTRY[engine.name] = engine
    return engine


def _load_builtin_plugins() -> None:
    from . import local  # noqa: F401  (each module registers its adapter)
    from . import level3_stub  # noqa: F401


_load_builtin_plugins()
