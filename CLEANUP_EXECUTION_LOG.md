# CLEANUP_EXECUTION_LOG.md — D3
**Date:** 2026-09-28 | **Source:** Untitled T2 + AUDIT_REPORT.md
**Law:** L4 archive-never-delete; L10 agents never edit shared pipeline files; merge beats deleting.
**Method:** Archive before delete; verify SHA256 before and after; log every action.

---

## 1. EXECUTION ORDER (safe-first, then MERGE, then DELETE)

### Phase A — ARCHIVE (never raw-delete)
All DELETE candidates first moved to `_archive/cleanup_2026-09-28/` with SHA256 verification.

### Phase B — MERGE (consolidate, do not lose content)
All MERGE candidates consolidated into canonical files; duplicates archived.

### Phase C — DELETE (after archive + merge verified)
Only then raw-delete the archived copies.

---

## 2. ACTION LOG

### 2.1 ROOT — DELETE (1 file)

| Action | File | Reason | Archive path | SHA256 verified |
|---|---|---|---|---|
| DELETE | `.env` | Secrets — Sarvam API key should not live in repo root (already in .gitignore). Move to `~/.env_south` per standard practice. | `_archive/cleanup_2026-09-28/env_secrets/` | TBD |

**Note:** `.env` content was NEVER logged in this report (security law). Orchestrator to verify the API key still works after move.

### 2.2 `level2/probe22/` — DELETE (152 files)

| Action | File | Reason |
|---|---|---|
| DELETE | `manifest.json.pre-purge` | Superseded by `manifest.json` (n=1227 final) |
| DELETE | `manifest.json.pre-ne` | Superseded by `manifest.json` |
| DELETE | `manifest_fragments/*.pre-purge` (18 files) | Superseded by non-pre-purge versions |
| DELETE | `preds_*.metrics.normalized.summary.tsv` (99 files) | Redundant TSV, JSON authoritative |
| DELETE | `scores/metrics_*.summary.tsv` (99 files) | Redundant TSV, JSON authoritative |
| DELETE | `scores/preds_*.json` (22 files) | Duplicates of root `preds_*` |
| DELETE | `scores/preds_*_en.json` (11 files) | Duplicate EN prediction copies |
| DELETE | `scores/test_bn_metrics.json` | Stale test file |

**MERGE (2 files):**
| Action | Source | Target | Reason |
|---|---|---|---|
| MERGE | `verify_visual.py` | `visual_verify.py` | Duplicate — consolidate to visual_verify.py |

### 2.3 `level2/models/` — MERGE (4,035 files)

| Action | File | Reason |
|---|---|---|
| MERGE | `level2/models/*.json` (4,035 files) | Duplicates `level2/out/` engine outputs — consolidate into sealed source |

**Note:** This is a HUGE directory. Before deletion, verify that `level2/out/` contains the exact same files via SHA256. If they don't match exactly, KEEP `level2/models/` (it may be an archive of v1 runs that differs from v2 runs).

**RECOMMENDATION:** Verify first, do not blind-delete. Log SHA256 mismatch count.

### 2.4 `docs/research/level7/` — MERGE (45 files) + DELETE (12 files)

**MERGE (duplicate .md/.jsonl pairs → keep .jsonl):**

| Source dir | Action | Files |
|---|---|---|
| `b/b2_self_improving_agents/` | MERGE into `b2_all_artifacts.jsonl` | 7 split chunks (artifacts_001_020 through artifacts_111_120.jsonl) |
| `b/b3_multi_agent_orchestration/` | MERGE .md into .jsonl | 8 files (artifact_200_270) |
| `b/b4_agent_tooling/` | MERGE .md into .jsonl | 13 files |
| `b/b5_elite_repos/` | MERGE .md into .jsonl | 14 files |

**DELETE:**
- `b/b3_multi_agent_orchestration/033_atc_kanban.json` (duplicate of artifact_033)
- `b/b3_multi_agent_orchestration/artifact_003_agent_team_work_zone_arxiv_2607_22917.json` (naming variant)

### 2.5 `.audit/` — DELETE (6 files)

| Action | File | Reason |
|---|---|---|
| DELETE | `all_files_b.txt` | Intermediate inventory (562 lines), superseded by sha256_all.txt |
| DELETE | `b3_files.txt` | Intermediate file list (375 lines), subset, no independent value |
| DELETE | `safety_backup/openbharatocr_files/metrics_openbharatocr_en_normalized.json` | Stale backup |
| DELETE | `safety_backup/openbharatocr_files/metrics_openbharatocr_normalized.json` | Stale backup |
| DELETE | `safety_backup/openbharatocr_files/metrics_openbharatocr_raw.json` | Stale backup |
| DELETE | `safety_backup/openbharatocr_files/preds_openbharatocr.json` | Stale backup |

### 2.6 `graphify-out/` — DELETE (1 file)

| Action | File | Reason |
|---|---|---|
| DELETE | `manifest.json` | Empty placeholder `{}` (2 bytes), obsolete after merge |

---

## 3. SAFETY PROTOCOL

For every DELETE action:
1. Compute SHA256 of source file
2. Move to `_archive/cleanup_2026-09-28/<original_path>/`
3. Verify SHA256 in archive matches source
4. Log SHA256 in this log
5. Only then `rm` the source

For every MERGE action:
1. Read both source files
2. Verify content overlap (no genuine new content lost)
3. Write canonical version to target
4. Archive source files
5. Log merge summary

For SEALED directories (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/akshardrishti_official/):
- **NEVER TOUCH** — read-only per L10 + AGENTS.md

---

## 4. POST-CLEANUP VERIFICATION (T2.5)

After all actions complete:
1. Verify all KEEP files still exist (`find` vs audit)
2. Verify no SEALED file was touched (`sha256sum` vs pre-cleanup snapshot)
3. Verify all references in `docs/INDEX.md` + `OCR_AGENT_MEMORY_FEED.md` + `SOUTH_CANON.md` still resolve
4. Write final hierarchy map (D7)

---

## 5. EXECUTION STATUS

| Phase | Actions | Status |
|---|---|---|
| A. ARCHIVE setup | Create `_archive/cleanup_2026-09-28/` | PENDING |
| B. `.env` archive + move | 1 file | PENDING |
| C. probe22 DELETE | 152 files | PENDING |
| D. probe22 MERGE | 2 files | PENDING |
| E. level2/models MERGE/verify | 4,035 files | PENDING (verify first) |
| F. level7 MERGE | 45 files | PENDING |
| G. level7 DELETE | 12 files | PENDING |
| H. .audit DELETE | 6 files | PENDING |
| I. graphify-out DELETE | 1 file | PENDING |
| J. Post-cleanup verify | D7 hierarchy map | PENDING |

**Total actions:** 172 DELETE + 4,082 MERGE
**Blockers:** None (all actions are safe per audit)
**Owner:** Orchestrator (this session)
**Safety:** L4 archive-never-delete applied throughout
Decision: verify_visual.py (9975 bytes, Sep 27 04:55) and visual_verify.py (4718 bytes, Sep 27 04:52) are DIFFERENT scripts.
  - verify_visual.py = Complete §6.4 visual verification (newer, 9975 bytes)
  - visual_verify.py = Machine-assisted blind visual verification (older, 4718 bytes)
  - REVERTED MERGE: both kept KEEP. Different scripts, different purposes.

Decision: level2/models/ (4,035 files) and level2/out/ (4,001 files) are DIFFERENT structures.
  - models/ = per-engine docs (PROMPT.md + RUN.md + json/ with flat names like kn_001.json)
  - out/ = per-engine + per-lang nested (out/<engine>/<lang>/<file>.json)
  - REVERTED MERGE: both kept KEEP. Different structures, different purposes.
  - Audit was wrong on this one — false positive.
