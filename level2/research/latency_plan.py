#!/usr/bin/env python3
"""RED (T3, law §14.3): latency sweep plan from models/<engine>/metrics.json.

    python3 level2/research/latency_plan.py

Reads the sealed per-engine median ms/page, projects a full 400-page timed
sweep, and emits the protocol. Writes research/LATENCY_SWEEP_PLAN.md.
Numbers come only from metrics.json (+ Sarvam's documented rate limit).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import r1_common as C  # noqa: E402

from engines.sarvam_api import MIN_REQ_INTERVAL_S, PRICE_INR_PER_PAGE, POLL_S  # noqa: E402

PAGES = 400


def main() -> None:
    rows = []
    for e in C.ENGINES:
        mj = json.loads((C.L2 / "models" / e / "metrics.json").read_text(encoding="utf-8"))
        ms = mj.get("median_ms_per_page")
        rows.append((e, C.family_of(e), ms))
    L = ["# LATENCY SWEEP PLAN (RED, law §14.3)",
         f"generated {datetime.now(timezone.utc).isoformat(timespec='seconds')} by `research/latency_plan.py` "
         "from models/<engine>/metrics.json (do not hand-edit)", "",
         "| engine | family | sealed median ms/page | pages/hour (1 worker) | 400-page wall-clock h | status |",
         "|---|---|---|---|---|---|"]
    total_h = 0.0
    for e, fam, ms in rows:
        if ms:
            h = PAGES * ms / 3.6e6
            total_h += h
            L.append(f"| {e} | {fam} | {ms:,} | {3.6e6 / ms:,.0f} | {h:.1f} | measured |")
        else:
            L.append(f"| {e} | {fam} | — | — | — | **NO TIMING — sweep required** |")
    s_min = 3 * MIN_REQ_INTERVAL_S + POLL_S  # submit + >=1 status + download, throttled
    L += [f"| sarvam_api (L3) | paid | ≥{s_min * 1000:,.0f} (throttle floor) | ≤{3600 / s_min:,.0f} | ≥{PAGES * s_min / 3600:.1f} | "
          f"₹{PRICE_INR_PER_PAGE}/page, 10 req/min — measure at gate |",
          "", f"Sum of measured engines, sequential single worker: **{total_h:.1f} h** for 400 pages.",
          "", "## Protocol (run on the full tree; one engine at a time, machine otherwise idle)",
          "1. Same 4-page gate pages first (te_087, ta_092, kn_048, ml_019) × 3 repeats; drop the first (model load).",
          "2. Record per page: wall ms, CPU model, threads, RAM peak → append to HEARTBEAT.jsonl (existing telemetry).",
          "3. Full sweep only for engines marked NO TIMING or whose sealed median rests on <20 timed pages.",
          "4. Report p50/p90 ms/page and ₹/page (CPU-hour cost stated as an explicit assumption) next to Sarvam's ₹0.5/page.",
          "5. Quote latency only with machine spec; never mix timings from different machines in one table."]
    (HERE / "LATENCY_SWEEP_PLAN.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[4:4 + len(rows) + 2]))


if __name__ == "__main__":
    main()
