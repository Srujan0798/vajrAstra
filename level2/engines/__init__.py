"""Engine plugin interface for Level-2 and Level-3 engines."""
from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List

class BaseEngine(ABC):
    """Base class for all OCR engines (Level-2 local + Level-3 paid)."""
    name: str
    version: str
    
    @abstractmethod
    def run(self, png_path: Path) -> str:
        """Run OCR on a PNG, return raw text."""
        pass

_ENGINES: Dict[str, 'BaseEngine'] = {}

def register(engine: 'BaseEngine'):
    _ENGINES[engine.name] = engine

def get_engine(name: str) -> 'BaseEngine':
    return _ENGINES[name]

def list_engines() -> List[str]:
    return list(_ENGINES.keys())

def get_all_engines() -> Dict[str, 'BaseEngine']:
    return _ENGINES.copy()
