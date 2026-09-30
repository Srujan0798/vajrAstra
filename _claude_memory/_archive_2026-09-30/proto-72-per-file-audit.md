---
name: proto-72-per-file-audit
description: "Added 2026-09-30 — the per-file audit uni T1.3 demanded and nobody delivered (AUDIT_REPORT is directory-level): WHAT/WHY/WHERE-used/WHO-references/WORTH + KEEP/MERGE/ARCHIVE/DELETE for every working file, flags a–f, waste-of-space list, 10% monitor re-check"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:53:28.912Z
---

# PROTO-72 — PER-FILE AUDIT (Miss subagents score, Verdict monitors) → `docs/campaign/audit/AUDIT_PER_FILE.csv` + rebuilt `AUDIT_REPORT.md`
> **Runs as Phase 2 of [[proto-98-clean-repo-master]]**, which defines the WORTH score (0–100, components C/D/U/F/T/G), `graph_signals.tsv`, the Laya advisory column (U31) and the T-topic of each file. Primary sources in `docs/sources/` are exempt from fates.

**Boss (uni T1.3):** "For EVERY file, the audit answers in writing: WHAT is this, WHY does it exist, WHERE is it used, WHO references it, and is it WORTH its space. Boss demands the reason
for every file's existence — deliver it per file, not per folder." CO-006, CO-016, CO-018, CO-067. Today `AUDIT_REPORT.md` (16 KB) is directory-level and says "54,000+ files … per file" — false.

## Scope (measured 2026-09-30)
Per-file rows for: repo root (all files), `docs/` (659), `_reports/` (39), `level2/` code + docs + json/csv/jsonl + loose files (not the payload trees), `scripts/` (6), `configs/` (1),
`src/` (49) + `tests/` (1), `graphify-out/` top-level files, `arc_level_1/` docs/scripts, `.claude/`.
**Payload trees are audited as groups with sampled verification**, one row per group: `level2/out`, `level2/probe22/out`, `level2/models/*/json|png`, `level2/unified`, `level2/pages_400`,
`level2/renders_shared`, `level2/probe22/images`, `level2/probe22/scores`, `arc_level_1/labeled`, `Datasets/**` (sealed, one row per language folder), `_archive/**` (one row per archive folder),
`.deps/IndicPhotoOCR` (engine dependency used by `level2/run_engine.py:31`), `.kilo/worktrees` (another agent tool's worktrees — see proto-76), `graphify-out/cache`.
Excluded: `.git`, `.venv*`.
**Imported, not re-judged (2026-09-30):** research files take their fate from [[proto-95-research-harvest-decisions]] (`docs/campaign/audit/RESEARCH_FATES.csv`); `_archive/` + `_reports/` from [[proto-96-archive-reports-compaction]] (`docs/campaign/audit/archive_inventory.tsv`).

## Skills for this protocol (load first — boss 2026-09-30: "I installed ECC and graphify, use them")
- `graphify --update` first (the bootstrap says when the graph is stale); use its orphan nodes, duplicate labels and communities to pre-sort files.
- ECC `living-docs-governance` for md verdicts, `ssotize` (Claude) for consolidation plans, the boss's gates in proto-92 (U29 deletion rule) before any move/delete, `verification-loop` before reporting done.

## Step 1 — enumerate + reference graph (Engine, one script `docs/campaign/audit/build_inventory.py`)
For each in-scope file: path, size, mtime, sha256, git-tracked, extension, first heading/docstring line, **inbound references** (count + up to 5 referrers: grep of basename and repo-relative path
across all md/py/json/yaml/sh/txt), **outbound references** (paths it mentions that exist / do not exist), duplicate group (same sha256), near-duplicate (same basename elsewhere).
Also use graphify: `graphify-out/graph.json` node for the file (degree, community) where present. Output `docs/campaign/audit/INVENTORY.csv`.

## Step 2 — per-file verdicts (Miss subagents, ≤5 in flight, ≤200 files each, grouped by directory)
Each row: `path | WHAT (one line, from reading it) | WHY it exists (the decision/task it serves) | WHERE used (script/doc/process) | WHO references it (from Step 1) | WORTH 0–100 with its six components C/D/U/F/T/G (proto-98) + size · T-topic · Laya suggestion (advisory) |
FLAGS a–f | VERDICT KEEP / MOVE→target / MERGE→target / ARCHIVE / DELETE-DUP (sha-identical to <path>) | reason (evidence)`.
Flags (uni T1.4): (a) duplicate (same content) · (b) variant (diverged copy, canonical unclear) · (c) trash (no purpose, no links, no history value) · (d) misleading name/path ·
(e) ordering/hierarchy violation · (f) orphan (no inbound, no outbound).
Known misleading names to rule on: `PROJECT_COMPLETE.md` (project not complete), `level2/UNIFIED_INDEX.md` ("one tree" false), `level2/MODELS_VS_OUT.md` ("KEEP BOTH"), `SAMPLE_PLAN_18_LANGS.md`
(now 22 languages, superseded), `level2/probe22/` (18 langs + en, not 22), `AUDIT_REPORT.md` (claims per-file), `sheet.sarvam_bench.discarded.csv`, `logs_killed/`, `FINAL_REPORT.md` (not final).
The subagent must READ each md/py (first 60 lines at least) before judging — no verdicts from names alone.

## Step 3 — monitors (Verdict, 1 per 3 scorers)
Re-open a random 10% of each scorer's rows; re-check WHO-references with grep; veto wrong verdicts; every MERGE/DELETE is link-checked (no live file references it, or references are updated
in the same change). A scorer with >10% vetoed rows gets its whole batch redone.

## Step 4 — outputs
- `docs/campaign/audit/AUDIT_PER_FILE.csv` (every row) + `docs/campaign/audit/FILE_WORTH_RANKING.csv` (every file, WORTH + components, sorted — proto-98). The WASTE list (uni T1.5: lowest WORTH × largest bytes) goes inside `AUDIT_REPORT.md`, not into a separate md.
- Rebuild `AUDIT_REPORT.md` (pre-image archived): summary counts by verdict and flag, per-directory tables, the misleading-names table, the waste list, and a pointer to the CSV.
- **No deletion or move happens in this protocol.** Execution goes through proto-70 (level2), proto-63 (duplicates), proto-74 (root/hidden) with the boss gates there.

Related: [[proto-70-level2-restructure]], [[proto-73-md-fact-consolidation]], [[proto-74-root-hidden-hygiene]], [[proto-50-w5-repo-map-and-drift]]
