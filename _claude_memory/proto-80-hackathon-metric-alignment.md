---
name: proto-80-hackathon-metric-alignment
description: "Added 2026-09-30, corrected same day — build one writer script reporting CER with bootstrap 95% CI, WER, substitution/deletion/insertion breakdown, seconds per page, median and abstention per engine × language × GT tier. NOTE: this is OUR chosen metric set; the official AksharDrishti scoring rules are unknown (the rubric sentence came from a student project)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:11:40.190Z
---

# PROTO-80 — A COMPLETE, DEFENSIBLE METRIC SET (Engine writes the writer, Verdict verifies)

**CORRECTION 2026-09-30 (factchk, Opus): the sentence "CER with a bootstrap 95% CI, WER, substitution/deletion/insertion breakdown, and seconds per page" comes from a student B.Tech project repo (github.com/Ayush-04-spec/akshardrishti, K. K. Wagh Institute) describing ITS OWN evaluation — it is NOT the official AksharDrishti rubric. The official scoring rules are UNKNOWN (not found on any opened official page). Never state them as the hackathon's rules; ask Vinay/the organisers (U2).**
The metric set below is still worth building: confidence intervals, error-type breakdown and speed are what any serious reviewer asks for, and speed matters for a 5,344-image test set.

**Evidence withdrawn:** the rubric quote previously here was from a student project (see correction above). Official rules: UNKNOWN — U2.
**Gap:** `docs/campaign/BENCHMARK_22.md` has mean/median CER but no bootstrap CI, no S/D/I, no seconds/page. Law L2 (one writer, one truth) and L9b (freshness stamped): numbers come from a script, never by hand.

## Engine subagent — TASK (paste after the shared context block)
> Write `level2/unified/rubric_report.py` (stdlib + `level2/probe22/metrics.py` only; deterministic; `generated_at` stamp) producing `docs/campaign/RUBRIC_REPORT.md`:
> 1. For every engine × language (and overall, and per GT tier per proto-62): n, CER mean, **CER bootstrap 95% CI** (1,000 resamples over items, seed 20260926; report the method),
>    CER median, **abstention rate** (empty predictions; see proto-82 table), WER, and **S/D/I counts and rates** from the character alignment (edit-operation breakdown; if `metrics.py`
>    has no op breakdown, implement Levenshtein backtrace and test it on 5 hand-checked pairs).
> 2. **Seconds per page** per engine: from run logs (`level2/probe22/logs/`, `engine_health_log.jsonl`, pack JSON `engine_meta` timing fields) and South `level2/reports/LATENCY.md`;
>    state n timed and the hardware (Apple M2 Max). Never re-run engines for timing in this step.
> 3. Input CER source: `sheet.csv` (v1) and, if present, `level2/unified/sheet_v2.csv` from proto-61 — report both side by side until U9 decides.
> 4. Consistency: overall numbers must reproduce `BENCHMARK_22.md` means within rounding; print PASS/FAIL.
> Writes only the script and `docs/campaign/RUBRIC_REPORT.md`.

## Verdict check
Re-run; hand-check S/D/I on 5 items; check CI width is plausible for n (e.g. n=3 Sarvam cells must show very wide intervals); confirm no hand-typed numbers.

Related: [[proto-12-w1b-benchmark22]], [[proto-61-sheet-provenance-forensics]], [[proto-62-gt-tier-stratified-reporting]], [[proto-82-engine-empty-output-patterns]]
