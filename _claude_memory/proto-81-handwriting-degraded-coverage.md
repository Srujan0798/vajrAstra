---
name: proto-81-handwriting-degraded-coverage
description: "Added 2026-09-30 — the hackathon targets handwritten and low-quality documents but all 1,283 probe items are printed (0 handwriting, 0 tables, 983 quality \"unknown\"); measure what the test set contains, find honest handwritten/degraded evaluation data already on disk, and put the scope decision to the boss (U13)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:11:51.175Z
---

# PROTO-81 — HANDWRITING + DEGRADED-DOCUMENT COVERAGE (Engine measures, Verdict checks, boss decides scope)

**Facts (monitor 2026-09-30):** `level2/probe22/manifest.json` → `print_or_hand`: printed 1,283 · `has_table`: False 1,283 · `quality`: unknown 983, clean 300. `sheet.csv` `mixed_script` False on all rows.
Search summaries say the AksharDrishti challenge targets "handwritten and low-quality texts" — UNVERIFIED (the official page could not be opened; the X post returns HTTP 402). The test-set profile (step 2) is the independent truth. Sarvam's bench is reported as 0% handwriting / 0% tables (COMPETITOR_INTEL). Bodhan publishes
a handwriting bench (IndicOCR-HW) per 1D. So neither our probe nor Sarvam's bench measures what the hackathon emphasises. It is unknown whether these fields were measured or defaulted.

## Engine subagent — TASK (read-only; no training; no labels created for the test set)
> 1. **Field provenance:** find where `print_or_hand`, `quality`, `has_table` were set (`build_manifest.py`, `extract_gt.py`) — measured or defaulted? Report file:line.
> 2. **Test-set profile** (joins [[proto-78-submission-readiness]] step 2): view 60 random test images (`Datasets/akshardrishti_official/test/test/`, seed 20260926) and classify each:
>    printed / handwritten / mixed; clean / degraded (blur, stains, low contrast, skew); tables yes/no; script (by eye + Unicode block of a fast engine's output). Report counts with n.
> 3. **Our data vs that profile:** do any official pair images look handwritten (view 20 each of bn, hi, sa, en pairs)? How many probe items are visibly degraded (view 50)? Any handwritten items in
>    `arc_level_1/labeled/` or South renders?
> 4. **Honest options (no downloads without approval):** (a) handwritten items already on disk with GT; (b) public handwriting benches (name, licence, size, URL opened) — download needs the boss;
>    (c) engines with handwriting support among the 10 (evidence from their docs). Output `docs/campaign/COVERAGE_GAP.md`: profile tables, our coverage, options with cost, recommendation.

## Boss decision U13
Include handwriting/degraded evaluation in scope before the freeze? Recommendation depends on step 2: if the test set has a material handwritten share (say >10%), yes — at least an evaluation slice.

Related: [[proto-78-submission-readiness]], [[proto-80-hackathon-metric-alignment]], [[proto-92-boss-decisions]]
