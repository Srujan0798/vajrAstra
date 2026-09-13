"""Level-3 stubs RETIRED: sarvam_api.py + bhashini_api.py replaced them.

The real adapters (dry-run until keys exist) live in engines/sarvam_api.py
and engines/bhashini_api.py. This shim keeps the old import path alive
(test_registry imported LOCKED_MSG from here) without double-registering.
"""
from __future__ import annotations

LOCKED_MSG = "Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5"
