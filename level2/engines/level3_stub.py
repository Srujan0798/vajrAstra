#!/usr/bin/env python3
"""Level-3 stub (historical, not registered) — real adapters: sarvam_api.py / bhashini_api.py.

Kept per archive law. Level 3 status now lives in ULTIMATE_HYBRID_CONCERN.md §3 + §13 H4
(Sarvam approved post-demo; paid calls still need operator key + spend OK).
"""
from __future__ import annotations

from . import BaseEngine

LOCKED_MSG = "Level-3 stub is not wired — use engines/sarvam_api.py (see ULTIMATE_HYBRID_CONCERN.md §3, §13 H4)"

class SarvamBatchAPI(BaseEngine):
    name = "sarvam_batch_api"
    version = "stub (Level-3 socket)"
    def run(self, png_path) -> str:
        raise NotImplementedError(LOCKED_MSG)

class BhashiniAPI(BaseEngine):
    name = "bhashini_api"
    version = "stub (Level-3 socket)"
    def run(self, png_path) -> str:
        raise NotImplementedError(LOCKED_MSG)

# Export for backward compat
SarvamBatchAPI = SarvamBatchAPI
BhashiniAPI = BhashiniAPI
LOCKED_MSG = LOCKED_MSG
