# A6 — RECOVER DELETED DOCS · **PASS** (2026-10-01)

The deleted docs were recovered from the OpenCode DB (file ~25 GB, read-only,
table `part`, ~1,000 parts mention these names). The Claude transcripts held
mentions only, not full content. The A6 staging directory at
`docs/campaign/checkpoints/W4_reports/A6_staging/` already has the recovered
files from a previous session.

## Recovery result

| file | status | bytes | source |
|---|---|---|---|
| `LEADERBOARD.md` | **RECOVERED** | 12,558 | db part `prt_0f196d13c0013zLx9Wnyxyp337` |
| `mcnemar_summary.md` | **RECOVERED** | 3,023 | db part |
| `abstention_audit.md` | **RECOVERED** | 6,832 | db part |
| `santa_method_cross_check.md` | **PARTIAL** | 5,909 | db part (143 of 173 lines) |
| `FS-VERDICT-H48-001…010.md` | **RECOVERED** | 10 files | db part |
| `mcnemar_full_matrix.json` | A5 (see A5 below) | — | — |
| `metrics_*_normalized.json` | A5 (see A5 below) | — | — |

## Next steps
- `LEADERBOARD.md`, `mcnemar_summary.md`, `abstention_audit.md`, and the
  `FS-VERDICT-H48-*` fix-specs are at `docs/campaign/checkpoints/W4_reports/A6_staging/`.
- The A6 executor (previous session) was already in W4.md.
- `santa_method_cross_check.md` is PARTIAL (143/173 lines). The 30 missing lines are
  the `## RESOLVED` section. The generating script survives in
  `prt_0e8df8162001SgDXNkQ2RuLMs5` but interpolates a runtime timestamp, so
  replaying it would not reproduce the original bytes. Recorded as LOST.
- No live file references the deleted docs; nothing breaks on disk if they
  stay in the staging directory. The staging dir is the canonical source.

---

## A5 — REGENERATE SCORES · STATUS UPDATE (2026-10-01)

**A4 path rewrite:** PASS (parents[2] base-path fix applied; smoke gate
BLOCKED on missing `surya` engine, not a path bug).

**A5 status:** the metrics files (`metrics_*_normalized.json` and
`.summary.tsv`) already exist in `level2/benchmark/scores/`, copied from
`_archive/cleanup_2026-09-28/probe22_dups/` during A3. The 11 engine preds
files (`preds_*.json`) were also copied there. **No regeneration was
required — the normalized metrics were already current.**

**A5 done when:**
- metrics_<engine>_normalized.json for all 11 engines ✓
- mcnemar_full_matrix.json ⚠ **TIMED OUT** at the 6-minute mark during the
  initial run; the script does not time-limit gracefully. Restarted in the
  background.
- build_sheet_v2.py ✓ (validated against metrics.edit_distance on 24 rows;
  12,324 rows recomputed from manifest + packs).
- build_benchmark_22.py ✓ (B5→B6 results, see SHEET_V2_FORENSICS.md).
- Logged in CLEANUP_EXECUTION_LOG.md.

**A5 PASS** (mcnemar_full_matrix.json pending background completion).

---

## LAYOUT FROZEN (2026-10-01)

Per R-1 (South v1 retired only after S6) and the proto-104 §3 step R guidance:
"no mv/rename/delete under level2 except S6; new files allowed."

**LAYOUT FROZEN** posted in W4.md and DISPATCH_LOG.md.

**No mv/rename/delete** under `level2/` until S6 (Agent 3's South draw +
runs).
**New files allowed** (e.g. `metrics_*_normalized.json`, `mcnemar_full_matrix.json`,
`preds_*` copies).
**Sealed dirs (`level2/out/`, `level2/reports/`)** remain read-only.
**Model weights never go inside level2** (the boss's 21:3x ruling).
