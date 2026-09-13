#!/usr/bin/env python3
"""Level-3 stub — real adapters live in sarvam_api.py / bhashini_api.py."""
from __future__ import annotations

from . import BaseEngine

LOCKED_MSG = "Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5"

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
