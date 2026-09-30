---
name: proto-70-level2-restructure
description: "Added 2026-09-30 — the boss's level2 concern (M8, CO-001/002/004/009/010/025/068, uni T2.1/T2.2): end the old-South-out vs new-probe-out split and the symlink layers with ONE physical hierarchy; full inventory, dependency map of ~30 path constants, phased moves with sha256 proof, boss gate U10 for sealed paths"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:52:29.105Z
---

# PROTO-70 — LEVEL2 RESTRUCTURE: ONE ORDER, ONE PLACE, ONE HIERARCHY
> **2026-09-30 evening:** the execution order, owners and end state are in [[proto-101-south-unification-and-level2-tree]] (U10/U11 now). This file stays the reference for its inventory and path-dependency lists.

**Boss, 2026-09-30:** "I still see many unwanted and old and unnecessary files and folders just in the level 2 folder… you would have merged and redone… sort out the
old south out and the new current out… many misleading… hierarchy misleading." **uni T2.1:** "The boss must never again see parallel versions and ask which is real."
**T2.2:** "No special branch. No old/new split. No separate output islands."

## What is wrong today (monitor inventory, 2026-09-30 03:40)
| Item | Size / files | Problem |
|---|---|---|
| `level2/out/` | 29 MB · 4,001 (git-tracked) | South 400 outputs (ta/te/kn/ml) — one island |
| `level2/probe22/out/` | 115 MB · 13,289 (NOT in git) | probe outputs (18 langs + en) — second island |
| `level2/models/` | 4,035 files, 4,000 are symlinks | duplicate view of `out/` (`<engine>/json/` + `png/` symlinks) + 35 real files (PROMPT.md, RUN.md, metrics.json per engine) — "KEEP BOTH" contradicts CO-004 |
| `level2/unified/` | 17,289 symlinks + `build_benchmark_22.py` | a third view; `UNIFIED_INDEX.md` claims "one tree" but it has two subtrees `probe22/` and `south_400/` — misleading |
| `level2/pages_400/` | 400 symlinks + INDEX.json + page_ids.txt | fourth view of `renders_shared/` |
| `level2/renders_shared/` | 545 MB · 400 PNG (not in git) | South pages, flat names; probe pages live elsewhere (`probe22/images/`, 574 MB) |
| `level2/reports/` | 33 MB · 48 (not in git) | South scores; probe scores in `probe22/scores/` (143 MB) — two score islands |
| `level2/training_assets/` + `level2/reports/training_data/` + `probe22/w6_*.jsonl` | 3 places | training sets scattered |
| level2 root | `HEARTBEAT.jsonl` 1.4 MB, `DECISIONS.log`, 8 .py, 5 md, 2 json | logs and 3 overlapping index docs (FOLDER_MAP, UNIFIED_INDEX, MODELS_VS_OUT) at top level |
| `level2/probe22/` root | 98 loose items | scripts + 24 `preds_*.json` + 13 metrics tsv/json + 11 W6/QLoRA/MLX/memory docs + 5 `w6_*` training sets + `sheet.sarvam_bench.discarded.csv` + `logs_killed/` + `paddle_smoke.log` + 133 MB `tessdata/` + `__pycache__/` all flat |
| name `probe22` | — | holds 18 languages + en, not 22 — misleading name (CO-010) |
| `level2/research/smoke/` | 45 MB | looks like junk but `run_probe.py:218` reads `research/smoke/anuvaad_tesseract/tessdata` — KEEP (document why) |

## Path dependencies (monitor grep 2026-09-30 — the Engine subagent must re-grep; this is a starting list)
level2 root: `orchestrator.py:29-32,51,68,269,270,298` (out, models, logs_active, logs_archive, pages_manifest.json, reports, HEARTBEAT.jsonl) · `report.py:21` · `report_gen.py:20-21` ·
`deep_verify.py:20-23,86` (out, reports, renders_shared, models/<e>/json) · `verify_v2.py:39-40` · `seal_gen.py:16-18,43` · `run_engine.py:31,40` (`.deps/IndicPhotoOCR`, pages_manifest.json).
probe22: `run_probe.py:17-20,218` (LOCKED: probe22, manifest.json, images, out, research/smoke tessdata) · `build_manifest.py:33-37` · `extract_gt.py:30` · `gt_forensics.py:17-19` ·
`resource_shortfall.py:28-32` · `verify_visual.py`, `visual_verify.py` (images) · `mcnemar_full_matrix.py:29-30` (scores) · `en_harness_gate.py:24-25` · `build_en_sanity.py:18` ·
**absolute paths:** `engine_health_log.py:5`, `spot_check_engine.py:12-14`, `verify_engine_readiness.py:12-13`.
research/: `gap_report_gen.py`, `latency_gen.py`, `showcase_gen.py`, `one_screen_gen.py`, `whatsapp_gen.py`, `metrics_rigor_gen.py`, `training_assets_gen.py` (reports, out, training_assets, gates).
Also check: `pages_manifest.json` / `manifest.json` / `sheet.csv` / `preds_*.json` for embedded paths; docs that cite paths (fix in [[proto-50-w5-repo-map-and-drift]]).
git: only `level2/out/` (4,001) and 35 files of `level2/models/` are tracked — every other move has NO git safety net → sha256 manifests are mandatory.

## Target hierarchy (proposal — Verdict may improve it; the boss approves the final shape in U10)
```
level2/
├── README.md                     ← the ONE map (replaces FOLDER_MAP.md, UNIFIED_INDEX.md, MODELS_VS_OUT.md — merged, then archived)
├── benchmark/
│   ├── manifest_22.json          ← one manifest, 22 languages, origin + tier per item (from proto-20)
│   ├── pages/<lang>/<id>.<ext>   ← South renders (from renders_shared/, per-lang) + probe images (from probe22/images/)
│   ├── packs/<engine>/<lang>/<id>.json   ← ALL engine outputs, all languages, ONE physical tree (from level2/out + probe22/out)
│   └── scores/
│       ├── south400_v1/          ← was level2/reports (historical South scoring, sealed content)
│       ├── probe/                ← was probe22/scores + sheet.csv + preds_*.json + metrics_* files
│       └── combined/             ← BENCHMARK_22 outputs, sheet_v2 (proto-61)
├── pipeline/
│   ├── south400/                 ← run_engine.py, engines_config.py, orchestrator.py, report*.py, seal_gen.py, verify_v2.py, deep_verify.py, pages_manifest.json, pages_script_map.json
│   ├── probe/                    ← extract_gt.py, build_manifest.py, run_probe.py, metrics.py, mcnemar…, candidates/, manifest_fragments/, tessdata/, en_sanity/, slices/, snapshots/
│   └── engines/                  ← engine adapters (was level2/engines/)
├── engine_docs/<engine>/         ← PROMPT.md, RUN.md, metrics.json (the 35 real files from models/)
├── training_assets/{sft,dpo,disagreement,w6_sets,archived_sep13}/
├── research/                     ← generators + gates + smoke (smoke kept: run_probe depends on it)
├── docs/                         ← ULTIMATE_HYBRID_CONCERN.md, probe docs (AGENT_PROTOCOL, FINAL_REPORT, LIST, README, …), w6/ (QLORA_*, MLX_*, MEMORY_*, w6_*.md)
└── logs/                         ← HEARTBEAT.jsonl, DECISIONS.log, probe logs/, logs_killed/, paddle_smoke.log, engine_health_log.jsonl
```
Removed after the move (archived, not deleted raw): `models/<engine>/json|png` symlink layers, `unified/`, `pages_400/`, `__pycache__/`, the three superseded index docs.
If proto-71 (South re-run under the probe standard) is approved and done FIRST, the old South 400 packs/scores go to `benchmark/scores/south400_v1/` + `_archive/level2_south400_v1/`
as history, and `packs/` holds only same-standard outputs — the cleanest end state (CO-025 "delete old versions").

## Phases (each: verdict table → Verdict approval → execute → verify → log). No phase starts while any engine run or other agent touches level2 (proto-60 Rule 3).
**Phase 0 — inventory & baseline (read-only, Engine):** `level2/unified` excluded, everything else: `docs/campaign/level2/INVENTORY.csv` = path, type (file/dir/symlink→target), size, sha256 (files),
git-tracked yes/no, mtime, referenced-by (grep of all .py/.md/.json for the basename or relative path). Plus `docs/campaign/level2/DEPENDENCIES.md` = every path constant (re-grep; the list above is a start).
**Phase 1 — verdicts (Verdict):** every top-level item and every loose file in level2 root and probe22 root gets `KEEP-MOVE→<target> | MERGE→<target> | ARCHIVE | DELETE-DUP (sha-identical to <path>)`
with a one-line reason (uni R0.6/T1.3). Output `docs/campaign/level2/MOVE_PLAN.md` (a table the boss can read in 5 minutes + the full table).
**Phase 2 — boss gate U10: APPROVED by the boss 2026-09-30 ("Yes, after the meeting").** Still send the MOVE_PLAN summary to the boss before Phase 3 as information (not a new question) — one message: the target tree, what moves, which ~30 path constants change (incl. LOCKED `run_probe.py`), what gets archived, disk impact, rollback plan. Wait for yes.
**Phase 3 — execute (Engine, one mover, no parallel writers):**
1. Pre-move manifest: `find level2 -type f -o -type l | sort | xargs shasum -a 256 > _archive/level2_premove_<date>.sha256` (symlinks: record `readlink`).
2. Moves with `git mv` for tracked paths, `mv` otherwise (same filesystem = atomic rename; no copying of 1.2 GB).
3. Path constants: introduce ONE `level2/paths.py` (single source of all directory constants) and change each script to import it — or, if the boss prefers minimal edits,
   edit each constant in place. Absolute paths → relative to `Path(__file__)`. Record every edit as a fix-spec row.
4. Transitional compatibility symlinks at the 3 old output/page paths only (`level2/out`, `level2/probe22/out`, `level2/probe22/images`) — each with a `README_MOVED.md` beside it;
   removed in Phase 5. No other symlinks.
**Phase 4 — verify (Verdict):** post-move sha256 manifest == pre-move for every moved file (compare by content hash, path-mapped); counts per engine × lang match; every script
imports and runs its read-only/status/`--help` path without error (`orchestrator.py status`, `run_probe.py --help`, `metrics.py` self-test if any, report generators with `--dry-run` if available — never re-run engines);
`build_benchmark_22.py` reproduces `BENCHMARK_22.md` byte-identically after updating its paths; `grep -rn` finds no remaining references to old paths in live code.
**Phase 5 — close:** remove compat symlinks and the archived layers; `level2/README.md` written; `DISPATCH_LOG.md` + CLEANUP_EXECUTION_LOG entries; update `AGENTS.md`/docs paths
([[proto-50-w5-repo-map-and-drift]]); rebuild graphify ([[proto-77-graph-concerns]]).

## Hard rules for this protocol
Never delete a file whose sha256 is not present elsewhere or in `_archive/`. Never move `Datasets/`. Never run engines during the move. One executor only. If any verify step fails:
stop, move back using the pre-move manifest, report.

Related: [[proto-71-south-rerun-same-standard]], [[proto-72-per-file-audit]], [[proto-63-single-canonical-files]], [[proto-92-boss-decisions]]
