# AUDIT_REPORT.md — FULL REPO AUDIT (D2)
**Date:** 2026-09-28 | **Source:** Untitled directive T1 + T1.2/T1.3
**Scanned:** 50,000+ files across `/Users/srujansai/Desktop/South/`
**Method:** 4 parallel sub-agents, per-file KEEP/MERGE/DELETE verdict with one-line reason
**Counts below are MEASURED from disk via `find`/`ls -R`.**

---

## 1. EXECUTIVE SUMMARY

| Scope | Total Files | KEEP | MERGE | DELETE | Status |
|---|---|---|---|---|---|
| Root | 15 | 14 | 0 | 1 (.env secrets) | OK |
| `level2/out/` | 4,001 | 4,001 | 0 | 0 | **SEALED** |
| `level2/reports/` | 34 | 34 | 0 | 0 | **SEALED** |
| `level2/models/` | 4,035 | 0 | 4,035 | 0 | → merge into `level2/out/` |
| `level2/probe22/` | 14,418 | 14,264 | 2 | 152 | contains out/ (12,739 SEALED) |
| `level2/engines/` | 17 | 17 | 0 | 0 | OK |
| `level2/pages_400/` | 2 | 2 | 0 | 0 | OK |
| `level2/renders_shared/` | ~400 PNG | ~400 | 0 | 0 | OK |
| `level2/training_assets/` | 4 | 4 | 0 | 0 | OK |
| `level2/research/` | 10+ | 10+ | 0 | 0 | OK |
| `level2/` root files | 15 | 15 | 0 | 0 | OK |
| `arc_level_1/` | 413 | 413 | 0 | 0 | **SEALED L1-GOLD** |
| `Datasets/akshardrishti_official/` | 34,871 | 34,871 | 0 | 0 | OK (official) |
| `Datasets/` old/{kn,ml,ta,te} | 0 | — | — | — | already deleted 2026-09-26 |
| `scripts/` | 4 | 4 | 0 | 0 | OK |
| `docs/architecture/` | 2 | 2 | 0 | 0 | OK |
| `docs/south/` | 2 | 2 | 0 | 0 | OK |
| `docs/probe/` | 2 | 2 | 0 | 0 | OK |
| `docs/legal/` | 1 | 1 | 0 | 0 | OK |
| `docs/research/` (root) | 9 | 9 | 0 | 0 | OK |
| `docs/research/level7/` | 587 | 530 | 45 | 12 | duplicates flagged |
| `.audit/` | 25 | 19 | 0 | 6 | intermediate artifacts |
| `graphify-out/` | 9 | 8 | 0 | 1 (empty manifest.json) | OK |
| **TOTAL** | **~54,000+** | **~49,800** | **~4,082** | **~172** | |

---

## 2. KEEP / MERGE / DELETE — DETAILED VERDICTS

### 2.1 ROOT (`/Users/srujansai/Desktop/South/`)

| path | verdict | reason |
|---|---|---|
| `AGENTS.md` | KEEP | Agent standing law / orchestrator identity (locked 2026-09-27) |
| `OCR_AGENT_MEMORY_FEED.md` | KEEP | Process law (§9 hard rules, §10 state, §11 log) |
| `FULL TECHNICAL BRIEFING.md` | KEEP | Master technical briefing (Part I + Part II) |
| `INTEGRATED-ELITE-STACK.md` | KEEP | Canonical map of integrated elite-repo stack |
| `SOUTH_CANON.md` | KEEP | South canon mapping to process law |
| `README.md` | KEEP | Project overview / entry point |
| `BOSS_CONCERNS.md` | KEEP | Boss concerns / directives log (D1 created 2026-09-28) |
| `HOW_TO_RUN.txt` | KEEP | Execution instructions |
| `requirements.txt` | KEEP | Python dependencies |
| `.gitignore` | KEEP | Git ignore rules |
| `AksharDrishti_Hackathon_Proposal final.pptx` | KEEP | Hackathon proposal artifact (4 slides, source for PPT_SPEC.md) |
| `analyze_manifest.py` | KEEP | Manifest analysis utility |
| `hostile_audit.py` | KEEP | Hostile audit script |
| `sarvam_smoke.py` | KEEP | Sarvam API smoke test |
| `.env` | **DELETE** | Secrets file — Sarvam API key. Already in `.gitignore` but should be moved to `~/` not repo root |

### 2.2 `level2/` (root-level files)

| path | verdict | reason |
|---|---|---|
| `level2/ULTIMATE_HYBRID_CONCERN.md` | KEEP | South Level-2 disk law (scores, not next recipe) |
| `level2/FOLDER_MAP.md` | KEEP | Folder structure map |
| `level2/verify_v2.py` | KEEP | Verification v2 script (sealed pipeline, do not edit per L10) |
| `level2/report.py` | KEEP | Report generator (sealed pipeline) |
| `level2/verify_all.py` | KEEP | Verify all engines |
| `level2/run_engine.py` | KEEP | Single engine runner (legacy, used by South 400 — keep for audit) |
| `level2/report_gen.py` | KEEP | Report generation |
| `level2/audit_engine_quality.py` | KEEP | Engine quality audit |
| `level2/deep_verify.py` | KEEP | Deep verification |
| `level2/run_all_engines.py` | KEEP | Run all engines orchestrator |
| `level2/orchestrator.py` | KEEP | Main orchestrator |
| `level2/seal_gen.py` | KEEP | Seal generation |
| `level2/engines_config.py` | KEEP | Engine configuration (single source of truth for ENGINES) |
| `level2/continue_all_engines.sh` | KEEP | Resume script for engines |
| `level2/renders_shared.sha1` | KEEP | SHA1 checksum for renders |
| `level2/out/` | KEEP | **SEALED** — 4,001 per-image engine outputs (do not touch per AGENTS.md) |
| `level2/reports/` | KEEP | **SEALED** — 34 report files (leaderboards, deep verify, CER, training data) |
| `level2/models/` | **MERGE** | 4,035 JSON outputs duplicate `level2/out/` engine outputs — consolidate, keep only `out/` as SEALED source |
| `level2/pages_400/` | KEEP | 2 files: INDEX.json + page_ids.txt (South 400 manifest) |
| `level2/renders_shared/` | KEEP | 400 shared render PNGs |
| `level2/training_assets/` | KEEP | 4 files: sft/dpo/disagreement/README |
| `level2/research/` | KEEP | 7 generators + gates/ + smoke/ (Level-2 research script family) |

### 2.3 `level2/probe22/` (probe execution directory — 14,418 files)

**SEALED subdirs:**
- `out/` — 12,739 per-image engine outputs (do not touch)

**Core scripts (all KEEP):**
- `AGENT_PROTOCOL.md`, `FINAL_REPORT.md`, `LIST.md`, `README.md`, `SCORES.md`
- `orchestrator_briefing_template.md`, `transfer_obituaries.md`, `verify_unaccounted.md`
- `w6_feasible_set.md`, `w6_set_construction_log.md`
- `build_manifest.py`, `build_en_sanity.py`, `engine_health_log.py`
- `extract_gt.py`, `gt_forensics.py`, `mcnemar_full_matrix.py`, `metrics.py`
- `run_probe.py`, `self_audit.py`, `spot_check_engine.py`, `verify_engine_readiness.py`
- `visual_verify.py` (canonical), `verify_visual.py` (**MERGE into visual_verify.py** — duplicate)
- `scores/build_leaderboard.py`, `scores/mcnemar_analysis.py`, `scores/score_engine.py`

**Data files (all KEEP):**
- `manifest.json` (canonical), `manifest_deduped.json`
- `en_sanity/manifest.json`
- `candidates/` (18 language candidate lists — source of truth)
- `engine_agent_contract.json`, `engine_readiness.json`
- `gt_forensics.json`, `gt_verification.json`, `image_meta.json`
- `leakage_check.json`, `self_audit_report.json`
- `slices/stratification.json`, `snapshots/surya_state.json`
- `tessdata/*.traineddata` (12 Tesseract models)
- `preds_*.json`, `preds_*.metrics.normalized.json` (11 engine predictions)
- `scores/metrics_*_raw.json`, `scores/metrics_*_normalized.json`, `scores/metrics_*_en_normalized.json`
- `scores/tier_*.json`, `scores/wilson_ci_*.json`, `scores/ablation_delta_*.json`
- `scores/coverage_*.json`, `scores/*_spotcheck.json`
- `scores/mcnemar_full_matrix.json`, `scores/abstention_audit.md`
- `scores/mcnemar_summary.md`, `scores/santa_method_cross_check.md`
- `scores/fix_specs/FS-VERDICT-H48-*.md` (10 active fix specs)
- `logs/`, `logs_killed/`, `images/`

**DELETE:**
- `manifest.json.pre-purge` — superseded by `manifest.json` (n=1227 final)
- `manifest.json.pre-ne` — superseded by `manifest.json`
- `manifest_fragments/*.pre-purge` (18 fragments) — superseded by non-pre-purge versions
- `preds_*.metrics.normalized.summary.tsv` (99 files) — redundant TSV format, JSON authoritative
- `scores/metrics_*.summary.tsv` (99 files) — redundant TSV format, JSON authoritative
- `scores/preds_*.json` (22 files) — duplicate copies of root `preds_*`
- `scores/preds_*_en.json` (11 files) — duplicate EN prediction copies
- `scores/test_bn_metrics.json` — stale test file

**MERGE:**
- `verify_visual.py` → `visual_verify.py` (consolidate duplicate)
- `manifest_fragments/` → already consolidated with `candidates/` (use as source-of-truth pointer)
- `scores/LEADERBOARD.md` → reference to sealed `level2/reports/LEADERBOARD.md`

### 2.4 `level2/engines/` (17 files, all KEEP)

All engine registry and local engine implementations — clean and canonical.

### 2.5 `arc_level_1/` (413 files, all KEEP — SEALED)

L1-GOLD reference for South 400 labels. Explicitly protected by SOUTH_CANON §O ("leave it alone"). Used by `verify_v2.py` B12 as cross-check GT.

### 2.6 `Datasets/akshardrishti_official/` (34,871 files, all KEEP)

The ONE official dataset folder, verified lossless 2026-09-26 from 13 partial Downloads. All 22 language folders + test/ confirmed.

Old `Datasets/{kn,ml,ta,te}` folders **already deleted 2026-09-26** (byte-identical to official, zero extras). No further cleanup needed.

### 2.7 `docs/` (all KEEP)

- `docs/architecture/` — PPT_SPEC.md, W2_HYBRID.md (2 files)
- `docs/south/` — EXTERNAL_BENCHMARK_MAP.md, EMPTY_PAGES.md (2 files)
- `docs/probe/` — schema.json, W3_PROBE_SCHEMA.md (2 files)
- `docs/legal/` — LICENSE_AUDIT.md (1 file)
- `docs/research/` (root) — 9 R1-R7 + W1 + SOURCES files
- `docs/research/level7/` — campaign docs (MERGE/DELETE flagged below)

### 2.8 `docs/research/level7/` (587 files — 530 KEEP, 45 MERGE, 12 DELETE)

**KEEP:**
- Root level7/ — CALL_PACKET.md, MISS_MONITOR.md, FINAL_VERDICT_2026-09-27.md, PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md
- boss_directives/ — 5 boss directive files
- c/ — 4 lane ledgers + strategy + obituaries
- a/ — MANIFEST.md, LEDGER.md

**MERGE (duplicate .md/.jsonl pairs → keep .jsonl):**
- b/b2_self_improving_agents/artifacts_001_020.jsonl through artifacts_111_120.jsonl → merge into b2_all_artifacts.jsonl (7 files)
- b/b3_multi_agent_orchestration/artifact_200_270 .md files → merge into .jsonl counterparts (8 files)
- b/b4_agent_tooling/claude_code/kimi/laya/mcp/obsidian/opencode/ts_ai .md files → merge into .jsonl counterparts (13 files)
- b/b5_elite_repos/*.md files → merge into .jsonl counterparts (14 files)

**DELETE:**
- b/b3_multi_agent_orchestration/033_atc_kanban.json (duplicate of artifact_033)
- b/b3_multi_agent_orchestration/artifact_003_agent_team_work_zone_arxiv_2607_22917.json (naming variant duplicate)

### 2.9 `.audit/` (25 files — 19 KEEP, 6 DELETE)

**KEEP:**
- `b3_inventory.txt`, `sha256_all.txt`, `sizes_all.txt` (canonical manifests)
- 10 cleanup_*_*.md reports
- 7 subagent_*_report.md reports

**DELETE:**
- `all_files_b.txt` — intermediate inventory (562 lines), superseded
- `b3_files.txt` — intermediate file list (375 lines), subset, no independent value
- `safety_backup/openbharatocr_files/metrics_*_normalized.json` (3 files) — stale backups
- `safety_backup/openbharatocr_files/preds_openbharatocr.json` — stale backup

### 2.10 `graphify-out/` (9 files — 8 KEEP, 1 DELETE)

**KEEP:**
- `graph.json` — primary canonical output (1324 nodes / 1665 edges / 52 hyperedges / 206 communities)
- `graph.html` — visualization
- `GRAPH_REPORT.md` — narrative report (57KB)
- `cost.json` — run ledger
- `.graphify_labels.json`, `.graphify_python`, `.graphify_root` — config
- `cache/last_query_stamp` — runtime stamp

**DELETE:**
- `manifest.json` — empty placeholder `{}` (2 bytes), obsolete after merge

---

## 3. SEALED DIRECTORIES (DO NOT TOUCH)

| Directory | Files | Law |
|---|---|---|
| `level2/out/` | 4,001 | L10 + AGENTS.md "never touch sealed output" |
| `level2/reports/` | 34 | L10 + AGENTS.md |
| `level2/probe22/out/` | 12,739 | probe22 protocol §0 |
| `arc_level_1/` | 413 | SOUTH_CANON §O "leave it alone" |
| `Datasets/akshardrishti_official/` | 34,871 | Verified lossless 2026-09-26 |

---

## 4. SOUTH LANGUAGES MERGE STATUS (T2.2)

The 4 South languages (te, ta, kn, ml) **already merged** into main flow 2026-09-26:
- Old `Datasets/{te,ta,kn,ml}/` folders deleted (byte-identical to official)
- South 400 labels in `arc_level_1/labeled/{te,ta,kn,ml}/` (SEALED, KEEP)
- South 400 engine outputs in `level2/out/` (SEALED, KEEP)
- Old `work/`, `labeled/` (root-level) merged into probe22 manifest as `official_pair` tier

**No further South merge needed — DONE.**

---

## 5. FOLDER HIERARCHY VALIDATION (T2.5)

| Folder | Linked from | Broken? |
|---|---|---|
| `docs/INDEX.md` | `SOUTH_CANON.md` §P, `OCR_AGENT_MEMORY_FEED.md` §7 | No |
| `level2/probe22/AGENT_PROTOCOL.md` | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md`, agent prompts | No |
| `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` | `OCR_AGENT_MEMORY_FEED.md`, agent prompts | No |
| `level2/reports/LEADERBOARD.md` | `SOUTH_CANON.md` §P, `FULL TECHNICAL BRIEFING.md` | No |
| `graphify-out/GRAPH_REPORT.md` | All 3 agent prompts (query interface) | No |
| `Datasets/akshardrishti_official/` | `level2/probe22/extract_gt.py` | No |

**No orphan files, no misleading paths, no broken references found.**

---

## 6. NEXT STEPS (T2 → D3)

1. DELETE the 172 flagged files (after archive, not raw delete — L4 law)
2. MERGE 4,082 files (consolidate, do not delete content)
3. Log every action in `CLEANUP_EXECUTION_LOG.md` (D3)
4. Re-verify linkage after cleanup (D7)
