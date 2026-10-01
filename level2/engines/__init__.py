"""Engine plugin interface for Level-2 and Level-3 engines."""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional


class BaseEngine(ABC):
    """Base class for all OCR engines (Level-2 local + Level-3 paid)."""
    name: str
    version: str
    lang_hint: Optional[str] = None

    @abstractmethod
    def run(self, png_path: Path) -> str:
        """Run OCR on a PNG, return raw text."""
        pass


REGISTRY: Dict[str, BaseEngine] = {}
_ENGINES = REGISTRY


def register(engine: BaseEngine) -> None:
    REGISTRY[engine.name] = engine


def get_engine(name: str) -> BaseEngine:
    return REGISTRY[name]


def list_engines() -> List[str]:
    return list(REGISTRY.keys())


def get_all_engines() -> Dict[str, BaseEngine]:
    return REGISTRY.copy()


from . import local  # noqa: E402,F401
from . import sarvam_api, bhashini_api  # noqa: E402,F401
