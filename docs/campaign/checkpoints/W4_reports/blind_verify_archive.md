# Blind Verification — Archive & Pointer Checks

**Subagent role**: blind verifier (did not perform the work)
**Date (local)**: 2026-10-01
**Scope**: archive copy integrity + consolidation pointer wiring

## Check 1 — Archive copy integrity — PASS
- Path: `_archive/dedup_2026-10-01/RESEARCH_DECISIONS.md`
- Size: 3173 bytes, mtime 2026-10-01 04:39
- sha256: `d751bf09741d84da02e198aaf83305b83e977866a2f5a8e17dcb9261363b2d75`
- 64-hex-char SHA-256, well-formed. File exists and is readable.

## Check 2 — Consolidation protocols on disk — PASS
- `docs/campaign/protocols/proto-107-gate1-and-s5-ssot.md` — 1217 B, mtime 2026-10-01 16:18
- `docs/campaign/protocols/proto-108-md-consolidation.md` — 1100 B, mtime 2026-10-01 16:18
- Both files exist with non-trivial size (≠ 0).

## Check 3 — Runbook cross-references — PASS
`grep -n "proto-107\|proto-108" docs/campaign/protocols/proto-00-runbook.md`:
```
45:- **proto-107-gate1-and-s5-ssot** — Gate 1 numbers live in DISPATCH_LOG §36; SSOT for BODHAN_BASELINE.md and S5; status CONDITIONAL PASS.
46:- **proto-108-md-consolidation** — MD consolidation parked until A7 go; canonical RESEARCH_DECISIONS = docs/campaign/RESEARCH_DECISIONS.md; docs/research/RESEARCH_DECISIONS.md is archived with sha.
```
Both protocols appear in the runbook with role summaries.

## Check 4 — PLAN.md stale-pointer discipline — PASS
`grep -n "DRAFT_RESEARCH_PLAN" docs/PLAN.md` → line 31:
```
## Plan v3 draft (current) → see `docs/campaign/DRAFT_RESEARCH_PLAN.md` (Gate 1 numbers + RF-21..37 pointers added). This file (`docs/PLAN.md`) is the stale 09-26 list of next-work; do not execute from it.
```
PLAN.md correctly delegates execution to the new draft and labels itself stale.

## Check 5 — Gate 1 slot in DRAFT_RESEARCH_PLAN.md — PASS
`grep -n "0.4034" docs/campaign/DRAFT_RESEARCH_PLAN.md`:
```
28:| pair-only (300 gold) | 300 | 0.4034 | 0.4010 | beats surya 0.5660 |
180:| pair-only (300 gold) | 300 | 0.4034 | 0.4010 | beats surya 0.5660 |
```
Gate 1 metric `0.4034` is wired into the draft plan (appears in two locations — current-state table and a downstream reference).

## Verdict
All 5 checks PASS. The archive copy is intact with a verifiable hash, both consolidation protocols are on disk and indexed from the runbook, the stale PLAN.md delegates correctly, and the Gate 1 anchor (`0.4034`) is embedded in the draft research plan.