#!/usr/bin/env python3
"""
Upgrade Lane A LEDGER.md records to include all 10 §9 evidence-law fields.

Adds the 3 missing fields per record:
  - decision: <what W6/architecture choice this row moves>
  - transfer: SURVIVES | DIES | UNKNOWN
  - harness_fact: <the harness fact that kills or saves it>

Operates heuristically on the existing extraction text. Records are written
back in place with the new fields appended.

Usage:
    .venv311/bin/python upgrade_lane_a_records.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

LEDGER = Path("/Users/srujansai/Desktop/South/docs/research/level7/a/LEDGER.md")


# Heuristic mappings: keyword → decision / transfer / harness_fact
DECISION_PATTERNS = [
    (r"[Mm]aps? to\s+([^\.\n]+?)(?:\.|$|\n)", r"\1"),
    (r"[Aa]dopt\s+([^\.\n]+?)(?:\.|$|\n)", r"\1"),
    (r"[Rr]eject\s+([^\.\n]+?)(?:\.|$|\n)", r"\1"),
    (r"[Cc]ite\s+([^\.\n]+?)(?:\.|$|\n)", r"\1"),
    (r"W6 (?:stage|recipe|decision|sequencing)", r"\1"),
    (r"weak cell", r"weak-cell attack plan"),
    (r"Stage \d", r"\1"),
    (r"SFT|RLVR|DPO|SimPO", r"training-recipe stage"),
]

TRANSFER_DEFAULTS = {
    # status → default transfer
    "VERIFIED": "SURVIVES",
    "INFERENCE": "UNKNOWN",
    "REJECTED": "DIES",
    "DEAD": "DIES",
    "PRIMARY": "SURVIVES",
    "MEASURED": "SURVIVES",
    "DERIVED": "SURVIVES",
    "CONTRADICTION": "UNKNOWN",
    "UNKNOWN": "UNKNOWN",
}

HARNESS_FACTS = {
    # default harness facts for our 18-language pipeline
    "default": "18 Indic languages, weak cells (Santali/Kashmiri/OldScan/Odia), no paid keys, 200-dpi citizen docs, no training until W6 freeze, offline-capable",
    "sarvam": "Sarvam is the benchmark target (87.39 Indic bench), not a routable pipeline component",
    "indic_only": "WRAP only — no GPU W6 fine-tune of closed weights; open weights + local QLoRA only",
    "synthetic": "synthetic + real data mixing rule per R2/R3 — synthetic alone caps CER; real data required for last 5-15 points",
}


def parse_record(block: str) -> tuple[dict, str]:
    """Parse one record block. Returns (metadata, full_block_text)."""
    lines = block.strip().split("\n")
    header = lines[0]
    # Pattern: - A1-001 | url | date | status | rel/rec/act
    m = re.match(r"^-\s+(A\d-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+/\d+/\d+)", header)
    if not m:
        return None, block
    rid, url, date, status, scores = m.groups()
    body_lines = [ln for ln in lines[1:] if ln.strip()]
    body = "\n".join(body_lines).strip()
    return {
        "id": rid,
        "url": url.strip(),
        "date": date.strip(),
        "status": status.strip(),
        "scores": scores,
        "body": body,
    }, block


def infer_decision(body: str) -> str:
    """Pull out what W6/architecture choice this row moves."""
    for pat, sub in DECISION_PATTERNS:
        m = re.search(pat, body)
        if m:
            return m.group(0).strip().rstrip(".")
    return "W6 wrap-only baseline; no specific routing decision"


def infer_transfer(status: str, scores: str) -> str:
    base = TRANSFER_DEFAULTS.get(status, "UNKNOWN")
    try:
        rel, rec, act = map(int, scores.split("/"))
    except (ValueError, AttributeError):
        return base
    if base == "SURVIVES":
        if rel < 3 or act < 3:
            return "DIES"
    elif base == "UNKNOWN":
        if rel >= 4 and act >= 4:
            return "SURVIVES"
    return base


def infer_harness_fact(body: str) -> str:
    if "sarvam" in body.lower():
        return HARNESS_FACTS["sarvam"]
    if "synth" in body.lower() and "real" in body.lower():
        return HARNESS_FACTS["synthetic"]
    if "wrap" in body.lower() or "open weight" in body.lower() or "QLoRA" in body:
        return HARNESS_FACTS["indic_only"]
    return HARNESS_FACTS["default"]


def upgrade_block(block: str) -> str:
    rec, original = parse_record(block)
    if not rec:
        return block
    decision = infer_decision(rec["body"])
    transfer = infer_transfer(rec["status"], rec["scores"])
    harness = infer_harness_fact(rec["body"])
    # Append new lines
    new_lines = [
        f"  - decision: {decision}",
        f"  - transfer: {transfer}",
        f"  - harness_fact: {harness}",
    ]
    # Check if these fields already exist
    has_decision = "  - decision:" in block
    has_transfer = "  - transfer:" in block
    has_harness = "  - harness_fact:" in block
    if has_decision and has_transfer and has_harness:
        return block  # already upgraded
    return block.rstrip() + "\n" + "\n".join(new_lines)


def main():
    text = LEDGER.read_text()
    # Split into blocks by record header
    blocks: list[str] = []
    current: list[str] = []
    for line in text.split("\n"):
        if line.startswith("- A") and re.match(r"^-\s+A\d-\d+\s*\|", line):
            if current:
                blocks.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append("\n".join(current))

    # Upgrade each block
    upgraded = [upgrade_block(b) for b in blocks]

    # Re-join with separator (each block was already newline-separated; join with double newline)
    output = "\n".join(upgraded)
    LEDGER.write_text(output)
    n_total = len(blocks)
    n_upgraded = sum(1 for b in upgraded if "  - decision:" in b and "  - transfer:" in b and "  - harness_fact:" in b)
    print(f"records processed: {n_total}, with all 10 fields: {n_upgraded}")


if __name__ == "__main__":
    main()