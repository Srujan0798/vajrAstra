# A3 layout repair — executor report

## Pre-state verification (measured before touching anything)
- `test -d level2/benchmark/packs/out` → exit 1 (does NOT exist). PASS.
- `find level2/benchmark/packs -type f | wc -l` → **13,289**. PASS.
- `find level2/benchmark -type f | wc -l` → **14,663** (recorded as BEFORE).
- `docs/benchmark_docs` did not exist; `level2/training_assets/w6_sets` did not exist; `level2/benchmark/logs/` existed; `scores/sheet_v2.csv` and `scores/metrics_80.csv` present.
- Note: source files were all under `level2/benchmark/` (LIST.md, 4× QLORA_*.md, 3× w6_*.jsonl, engine_* + paddle_smoke.log), not at repo root. Moved from their measured locations.

## Moves executed (each command run separately, exit 0, no 2>/dev/null)
Task 2 → `docs/benchmark_docs/` (mkdir, new dir):
1. `level2/benchmark/LIST.md` → `docs/benchmark_docs/LIST.md`
2. `level2/benchmark/QLORA_EVAL_SPEC.md` → `docs/benchmark_docs/QLORA_EVAL_SPEC.md`
3. `level2/benchmark/QLORA_READINESS.md` → `docs/benchmark_docs/QLORA_READINESS.md`
4. `level2/benchmark/QLORA_SMOKE_TEST.md` → `docs/benchmark_docs/QLORA_SMOKE_TEST.md`
5. `level2/benchmark/QLORA_TRAINING_DATA.md` → `docs/benchmark_docs/QLORA_TRAINING_DATA.md`

Task 3 → `level2/training_assets/w6_sets/` (mkdir -p, new dir):
6. `level2/benchmark/w6_rlvr_unconditional.jsonl` → `level2/training_assets/w6_sets/w6_rlvr_unconditional.jsonl`
7. `level2/benchmark/w6_sft_conditional.jsonl` → `level2/training_assets/w6_sets/w6_sft_conditional.jsonl`
8. `level2/benchmark/w6_sft_unconditional.jsonl` → `level2/training_assets/w6_sets/w6_sft_unconditional.jsonl`

Task 4 → `level2/benchmark/logs/` (pre-existing keep folder):
9. `level2/benchmark/engine_agent_contract.json` → `level2/benchmark/logs/engine_agent_contract.json`
10. `level2/benchmark/engine_health_log.jsonl` → `level2/benchmark/logs/engine_health_log.jsonl`
11. `level2/benchmark/engine_readiness.json` → `level2/benchmark/logs/engine_readiness.json`
12. `level2/benchmark/paddle_smoke.log` → `level2/benchmark/logs/paddle_smoke.log`

Task 5 compliance: `logs_killed/` untouched (still present); `manifest.json` untouched; `scores/` untouched (`sheet_v2.csv`, `metrics_80.csv` verified present after); no README.md created (verified absent in both `level2/benchmark/` and `docs/benchmark_docs/`).

## Post-conditions (measured)
- `find level2/benchmark/packs -type f | wc -l` → **13,289** (before/after equal). PASS.
- `find level2/benchmark -type f | wc -l` → **14,655** vs BEFORE **14,663** (delta −8).
- Conservation check: 14,655 (benchmark after) + 5 (docs/benchmark_docs) + 3 (w6_sets) = **14,663 = BEFORE**. The 4 log files moved within the benchmark tree. Zero deletions.
- `test -d level2/benchmark/packs/out` → still absent (exit 1).
- Final `ls level2/benchmark/`: docs, image_meta.json, logs, logs_killed, manifest.json, manifest_22.json, manifest_additions.json, manifest_v1.json, manifest_v2.json, packs, pages, pipeline, scores.

## Verdict
**FAIL on the literal post-condition** ("benchmark total must equal BEFORE"): 14,655 ≠ 14,663. This equality is unachievable under the ordered tasks, because Tasks 2 and 3 explicitly relocate 8 files out of the `level2/benchmark/` tree (5 to `docs/benchmark_docs/`, 3 to `level2/training_assets/w6_sets/`). The measured delta (−8) exactly equals the files moved out, and the conservation equation balances (14,655 + 5 + 3 = 14,663), proving moves, not deletions. All 12 moves succeeded with exit 0; no other step failed.
