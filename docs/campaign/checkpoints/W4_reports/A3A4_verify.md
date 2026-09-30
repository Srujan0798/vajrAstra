# A3/A4 blind verification — independent report (2026-09-30, verifier subagent)

Method: read-only. Never watched the executor. All numbers below re-measured.
One side effect to declare: my own `python3 -m py_compile` re-runs refreshed
`level2/benchmark/pipeline/__pycache__/*.pyc` mtimes (no content change, no other writes).

## A3 — layout repair

| # | A3-claim | VERIFIED/FALSIFIED | my number |
|---|---|---|---|
| 1 | packs total = 13,289, unchanged | VERIFIED | `find level2/benchmark/packs -type f \| wc -l` = **13,289** |
| 2 | `packs/out` does NOT exist | VERIFIED | `test -d` → ABSENT |
| 3 | `docs/benchmark_docs/` exactly LIST.md + 4 QLORA_*.md | VERIFIED | 5 files, exactly those names |
| 4 | `training_assets/w6_sets/` exactly 3 w6_*.jsonl | VERIFIED | 3 files, exactly those names |
| 5 | `logs/` contains the 4 engine/paddle files | VERIFIED | all 4 present (+ pre-existing *.log, untouched) |
| 6 | `scores/` sheet_v2.csv (853,307 B) + metrics_80.csv undisturbed | VERIFIED | sheet_v2.csv = **853,307 B**; metrics_80.csv = 24,514 B, present |
| 7 | per-engine counts match the 11 expected values | VERIFIED | all 11 match (1313×7, 1426, 57, 1300, 1315; sum = 13,289) |
| 8 | 3 moved files spot-opened, content intact | VERIFIED | LIST.md 12,758 B (probe-list prose, sane); QLORA_EVAL_SPEC.md 16,598 B; w6_sft_conditional.jsonl 2,183,169 B parses as JSON array, 342 items; engine_readiness.json + engine_agent_contract.json both valid JSON. Non-empty, well-formed. Note: the w6 file is a pretty-printed JSON **array**, not strict one-object-per-line JSONL — extension quirk, not corruption (no pre-image size to compare; content is coherent). |
| 9 | before/after reconciliation (BEFORE 14,663 per A3 report) | VERIFIED with amendment | `find level2/benchmark -type f` now = **14,673**. Reconciliation: 14,673 (now) = 14,663 (BEFORE) − 8 (5 docs + 3 w6 moved out of tree) + **18 (.pyc in `pipeline/__pycache__/`, all timestamped 20:17–20:19 Sep 30 = A4's py_compile window)**. Cross-check: 14,673 − 18 = **14,655 = executor's A3-after number exactly**. Only files newer than 19:00 Sep 30 in-tree are the 17 edited .py + 2 edited .sh + 18 .pyc. **No data loss; delta fully explained.** Executor's "FAIL on literal equality" framing was honest and correct — equality is unachievable by design; conservation holds. |

## A4 — stale path rewrite

| # | A4-claim | VERIFIED/FALSIFIED | my evidence |
|---|---|---|---|
| 1 | 19 files / 103 lines per table | PLAUSIBLE, partially verified | All 17 pipeline .py + 2 scripts .sh show Sep-30-evening mtimes (`.sh` = 20:17:54). I did not recount all 103 lines. |
| 2 | 6 edited files spot-checked, new paths exist | VERIFIED | Opened gt_forensics.py (L16–20 → manifest_v1.json/pages/scores), self_audit.py (L19–22, L97), engine_health_log.py (L5), plus build_sheet_v2, reconcile_22, extract_gt references; `test -e` on 10 referenced paths (manifest_v1.json, pages/, scores/gt_forensics.json, logs/engine_health_log.jsonl, pipeline/tessdata, docs/MLX_*.md, docs/MEMORY_*.md, en_sanity/, scores/sheet_v1.csv, pipeline/candidates) → **all OK**. |
| 3 | py_compile green | VERIFIED | Re-ran `python3 -m py_compile` on 4 files (gt_forensics, reconcile_22, self_audit, build_sheet_v2) → **COMPILE-OK**. |
| 4 | final grep residual = locked + retired-source only | VERIFIED | Re-ran the exact binding grep → **17 lines, identical** to executor's quoted list (4× run_probe.py locked + 13× retired-source). Editable-file residual **0**. |
| 5 | smoke SMOKE-BLOCKED finding is real | VERIFIED (see §Smoke) | Code-read confirmed; no protocol-legal bypass found. |
| 6 | parity 0.012605 vs stored 0.0126 plausible | VERIFIED | Re-ran independently: gt_len=233 pred_len=238 norm 238/238, recomputed_CER=**0.012605**; stored sheet_v1.csv row (as_01/surya) CER=**0.0126** WER=**0.0968**. Delta = 4-dp rounding only. **MATCH.** |

## Forbidden-file table

Git is weak here: the whole `level2/benchmark/` tree is **untracked** (`??`), so `git status` cannot prove non-modification. Verdicts below rest on mtimes vs the repair window (~20:17 Sep 30, marked by __pycache__ + .sh mtimes) plus content inspection.

| path | status | evidence |
|---|---|---|
| `level2/benchmark/pipeline/run_probe.py` | NO CHANGE | mtime Sep 28 21:10 — pre-repair; content still carries the stale constants (grep hits L2/17/230/407 intact) |
| `level2/benchmark/docs/AGENT_PROTOCOL.md` (only copy on disk) | NO CHANGE | mtime Sep 27 19:04 — pre-repair |
| `level2/benchmark/manifest_v1.json` | NO CHANGE by repair (mtime predates window) | mtime Sep 30 16:36 — before the ~20:17 repair window; `mv` ops don't touch remaining files' mtimes |
| `scores/sheet_v1.csv` | NO CHANGE | mtime Sep 28 21:54 |
| `scores/sheet_v2.csv`, `scores/metrics_80.csv` | NO CHANGE by repair | mtimes Sep 30 15:13 / 15:50 — pre-window; sheet_v2 size 853,307 B as claimed |
| `level2/unified/run_bodhan.py` | NO CHANGE by repair | mtime Sep 30 17:03 — pre-window |
| `level2/benchmark/scores/` (whole dir) | NO UNEXPECTED CHANGE | scoped `git status` shows only the pre-existing untracked marker; no new/modified files inside beyond pre-window mtimes |
| sealed `Datasets/`, `arc_level_1/` | NO CHANGE | scoped `git status --short` on both → clean, no output lines |
| `level2/level2/` (smoke side-effect check) | NOT CREATED | ABSENT — executor's no-side-effects claim holds |

## Smoke verdict (own words)

`run_probe.py` computes `ROOT = parents[2]` of its own path. Since the file now lives at `level2/benchmark/pipeline/`, parents[2] is `level2/`, not the repo root — so every derived constant (`L2`, `PROBE`, `MANIFEST`, `IMAGES`, `OUT`, `TESSDATA`) dangles under a nonexistent `level2/level2/probe22/`, exactly as the executor's traceback shows. The `--manifest` CLI flag can override only the manifest read; image lookup (`L106: base = IMAGES / ...`) and pack output (`L114-115: OUT / ...`) are hardcoded from the same broken constants with no override, and `level2/probe22/` does not exist anywhere, so no CWD choice fixes it. The only workarounds (symlink forests with renamed targets, editing the file) either touch the locked file or create stray dirs and risk writes into `packs/` — outside the protocol. **SMOKE-BLOCKED confirmed; the block is structural, not a one-line default.**

## Overall verdict

**CONDITIONAL (rewrite verified, gate blocked).** A3: all counts, moves, sizes, and per-engine tallies verify; the before/after delta is fully explained (−8 legitimate moves out + 18 A4 .pyc artifacts; non-pyc count matches the executor's after-number exactly). A4: spot-checked rewrites resolve to real files, compile-green re-confirmed, final grep reproduces the executor's 17 lines exactly with zero editable residual, parity reproduces to the digit, and no forbidden file shows repair-window modification. The gate that stays red is the smoke test, blocked structurally by the locked `run_probe.py` path bug (parents[2] + hardcoded PROBE constants) — unblocking requires the locked-file erratum (U10) to be approved, which is outside A4's mandate. Nothing in A3/A4 needs rework; the next step is a decision on the run_probe.py/AGENT_PROTOCOL.md errata, not a rewrite.
