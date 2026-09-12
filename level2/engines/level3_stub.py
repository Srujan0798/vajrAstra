"""Level-3 socket stubs: Sarvam, Bhashini. ZERO API calls, ZERO keys.

Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5.
These classes exist so the harness, registry, cost sheet, and dashboards
can be wired NOW; kickoff = replace run() with a real client.
"""
from __future__ import annotations

from pathlib import Path

from . import BaseEngine, register

LOCKED_MSG = "Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5"


class SarvamBatchAPI(BaseEngine):
    name = "sarvam_batch_api"
    version = "stub (Level-3 socket)"

    def run(self, png_path: Path) -> str:
        raise NotImplementedError(LOCKED_MSG)


class BhashiniAPI(BaseEngine):
    name = "bhashini_api"
    version = "stub (Level-3 socket)"

    def run(self, png_path: Path) -> str:
        raise NotImplementedError(LOCKED_MSG)


register(SarvamBatchAPI())
register(BhashiniAPI())
