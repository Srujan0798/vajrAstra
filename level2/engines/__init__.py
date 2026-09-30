"""Engine plugin interface for Level-2 and Level-3 engines.

Contract (see engines/README.md): BaseEngine, REGISTRY, register().
Importing this package registers all 12 adapters (10 local + 2 Level-3);
no OCR model loads on import (local adapters import run_engine lazily).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional

class BaseEngine(ABC):
    """Base class for all OCR engines (Level-2 local + Level-3 paid)."""
    name: str
    version: str
    lang_hint: Optional[str] = None  # optional default page language (te/ta/kn/ml)

    @abstractmethod
    def run(self, png_path: Path) -> str:
        """Run OCR on a PNG, return raw text."""
        pass

REGISTRY: Dict[str, 'BaseEngine'] = {}
_ENGINES = REGISTRY  # backward-compat alias

def register(engine: 'BaseEngine'):
    REGISTRY[engine.name] = engine

def get_engine(name: str) -> 'BaseEngine':
    return REGISTRY[name]

def list_engines() -> List[str]:
    return list(REGISTRY.keys())

def get_all_engines() -> Dict[str, 'BaseEngine']:
    return REGISTRY.copy()

# Self-registration: adapters do `from . import BaseEngine, register`, so these
# imports must stay below the definitions above.
from . import local, sarvam_api, bhashini_api  # noqa: E402,F401
