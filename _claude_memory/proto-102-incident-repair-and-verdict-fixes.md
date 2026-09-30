---
name: proto-102-incident-repair-and-verdict-fixes
description: "Added 2026-09-30 ~16:55 IST — INCIDENT + FIX LIST: Agent 3 ran proto-101 out of order (no backup, no feasibility, no gates, 16:36–16:39) and permanently deleted level2/probe22/scores (~143 MB, untracked) via 'mv scores scores_tmp; rm -rf scores_tmp'; archived live data (sheet_v2.csv, manifest_22.json, metrics_80.csv); nested packs/out; left run_probe.py on dead paths. Part A repairs (restore, regenerate, recover from transcripts, fix paths, clean the junk it made); Part B turns every finding of the Verdict report (16:21) into a fix with an owner; Part C adds binding execution rules (proto-01 rules 17–21); Part D lists the planner's own memory updates"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T11:18:19.869Z
---

# PROTO-102 — INCIDENT REPAIR (proto-101 run, 16:36–16:39) + FIXES FROM THE VERDICT REPORT + EXECUTION DISCIPLINE

**Boss, 2026-09-30:** "write all protocols to sort out and fix all these".

## Incident facts (planner, 16:40–16:55 IST, from the OpenCode DB command trace of `ses_f16bc20e…` + disk)
Agent 3 (MiniMax-M3) ran [[proto-101-south-unification-and-level2-tree]] in ~3 minutes, from 16:36:44 to 16:39:05.
- **It skipped P0.** No pre-move bundle or sha manifest: `_archive/bundles/` was empty.
- **It skipped P1** (feasibility) and every Verdict gate.
- **It "did" P2 in 24 seconds**, then ran P4 and P6.

**Damage:**
1. **Permanent deletion of the probe scores folder.**
   - The P2 script ran `mv level2/benchmark/scores level2/benchmark/scores_tmp` then `rm -rf level2/benchmark/scores_tmp`, with errors hidden by `2>/dev/null`.
   - The folder was untracked: no bundle, no APFS local snapshot, Time Machine not mounted.
   - Lost: the probe `LEADERBOARD.md`, `mcnemar_full_matrix.json`, `mcnemar_summary.md`, `metrics_<engine>_normalized.json` (11 engines), `abstention_audit.md`, `santa_method_cross_check.md`, `fix_specs/FS-VERDICT-H48-001…010.md`, and anything else in `scores/` (~143 MB per proto-70's measurement).
   - 12 live docs cite these files: KILL_CRITERIA, SANTA_METHOD_FINAL, MISS_MONITOR, CALL_PACKET, W6_QLORA_SPEC, H48_*, FIX_SPECS_*, PROBE22_EDGE_ANALYSIS, BOSS_HANDOFF, PROMPT_MISS_AGENT.
2. **Live data archived by mistake.**
   - `sheet_v2.csv` (adopted for reporting, RF-13/U9), `manifest_22.json` (proto-20 output) and `metrics_80.csv` (proto-80 output) now sit inside `_archive/south_unified_symlinks_2026-09-30/`.
   - The copy into `scores/` had failed, because `scores/` no longer existed.
3. **A broken structure.**
   - The packs are nested one level too deep, at `level2/benchmark/packs/out/<engine>/<lang>/`, because `mv out packs` went into an existing folder.
   - The benchmark root still holds `preds_*`, `metrics_*`, `QLORA_*` and `w6_*`.
   - `pipeline/run_probe.py` still references `probe22` (4 times), so every engine run is broken. The Engine subagent is now searching for `level2/unified/`.
4. **Junk re-created.**
   - `_archive/south_unified_symlinks_2026-09-30/` (17,289 dead symlinks + 9 real files).
   - `_archive/south_pages_400_symlinks_2026-09-30/` (400 dead symlinks + 2 files).
   - `_archive/south_renders_shared_2026-09-30/` (400 PNG, 545 MB — the only copy of the South v1 page renders).
   - `_archive/proto-98_phase0_2026-09-30/` (one copied file, mislabelled as the Phase 0 snapshot).
   - `docs/research/uni_v3_ORIGINAL_2026-09-29.md` re-created — the duplicate proto-63 had removed.
5. **Done right:**
   - `level2/out` (git-tracked South v1 packs) is untouched.
   - `_archive/bundles/2026-09-30_south_v1.tar.gz` (4,076 entries, 6.2 MB) holds the 4,000 duplicate `models/*/json`, the 35 engine docs and `level2/reports` (50 entries).
   - `level2/engine_docs/` was created; `.playwright-mcp` was deleted.
   - The `.kilo` worktree subdued-quince was pruned; screeching-shallot was left in place (dirty) and reported.

## Part A — Repair
**Owners:**
- **Repair lead:** Agent 2 `ses_f1233a0a…`. It uses 2 Sonnet-class subagents: one executes, one verifies blind.
- **Agent 3:** read-only until A9 passes.
- **Engine lane:** no level2 reads or writes until A4 passes.

- **A0 — Stop.** Post `INCIDENT REPAIR START` in DISPATCH_LOG. Confirm no other session is writing under `level2/` or `_archive/`.
- **A1 — Pre-image now.**
  - sha256 manifest of `level2/` and `_archive/south_*_2026-09-30/` → `docs/campaign/audit/incident_pre_repair.sha256`.
  - `tar -czf _archive/bundles/2026-09-30_incident_pre_repair.tar.gz --exclude='level2/benchmark/pages' --exclude='level2/benchmark/packs' level2/benchmark level2/engine_docs`.
  - Extract into scratch and compare sha = 100%.
- **A2 — Restore live data.** Copy `sheet_v2.csv` and `metrics_80.csv` → `level2/benchmark/scores/`, and `manifest_22.json` → `level2/benchmark/`, from `_archive/south_unified_symlinks_2026-09-30/`. The sha256 must equal the archive copy.
- **A3 — Finish the layout** (the proto-101 target).
  1. Check for name clashes, then `mv level2/benchmark/packs/out/* level2/benchmark/packs/ && rmdir level2/benchmark/packs/out`.
  2. `mkdir level2/benchmark/scores`, then move in `sheet.csv` (renamed `sheet_v1.csv`, content unchanged), `preds_*.json`, `metrics_*`, `sheet.sarvam_bench.discarded.csv`, `self_audit_report.json`, `gt_forensics.json`, `gt_verification.json`, `leakage_check.json`.
  3. `QLORA_*.md` + `LIST.md` → `docs/`.
  4. `w6_*.jsonl` → `level2/training_assets/w6_sets/`.
  5. The benchmark root keeps only `README.md`, `manifest_v1.json`, `manifest_v2.json`, `manifest_additions.json`, `manifest_22.json`, `image_meta.json` and the folders.
  6. **No `2>/dev/null` anywhere** — a failed `mv` must stop the script.
- **A4 — Fix paths.**
  - grep all live `.py` / `.sh` under `level2/` and `scripts/`, plus command blocks in docs, for `probe22`, `level2/unified`, `renders_shared`, `pages_400`, `level2/models/` and `level2/reports`, and edit them to the new paths. `run_probe.py` and `AGENT_PROTOCOL.md` get path errata only (U10). Fix the absolute paths in `engine_health_log.py`, `spot_check_engine.py` and `verify_engine_readiness.py`.
  - **Required:** `grep -rn "probe22\|level2/unified\|renders_shared\|pages_400" --include='*.py' --include='*.sh' level2 scripts` → 0 lines.
  - **Smoke test:** `run_probe.py` on 1 item per engine writes to `benchmark/packs/<engine>/<lang>/`. `metrics.py` on one engine reproduces that engine's `sheet_v1.csv` rows.
- **A5 — Regenerate the computed scores** (deterministic, from the surviving `preds_*` / packs).
  - `metrics.py` for all 11 engines → `scores/metrics_<engine>_normalized.json` (+ raw).
  - `mcnemar_full_matrix.py` → `scores/mcnemar_full_matrix.json`.
  - `build_sheet_v2.py` → compare with the restored `sheet_v2.csv`: identical, or report the diff.
  - `build_benchmark_22.py` → tables.
  - Log every command and output sha in CLEANUP_EXECUTION_LOG.
- **A6 — Recover the written docs from transcripts.** For each deleted `.md` — `LEADERBOARD.md`, `abstention_audit.md`, `mcnemar_summary.md`, `santa_method_cross_check.md`, `FS-VERDICT-H48-001…010.md` — find the LAST full-content copy:
  1. Query the OpenCode DB (`~/.local/share/opencode/opencode.db`, table `part`: read/bash tool outputs containing the whole file; ~1,000 parts mention these names).
  2. Then the Claude transcripts `~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl` (3 match).

  Write each to `scores/<name>` with a banner: "RECOVERED 2026-09-30 from <source id>, read at <time>; later edits, if any, are lost".
  - Files with no full copy → listed as **LOST** in the incident record, and each citing doc gets a one-line erratum.
  - `_archive/cleanup_2026-09-28/probe22_dups/` (older metric files) is a last resort, used only if regeneration fails.
- **A7 — Clean the junk this run made** (only after A2–A6 pass).
  - Delete the 17,689 dead symlinks in the two `_archive/south_*_symlinks_2026-09-30/` folders; their 11 real files go into the incident bundle first.
  - Bundle `_archive/south_renders_shared_2026-09-30/` → `_archive/bundles/2026-09-30_south_v1_renders.tar.gz` (sha-verified), then remove the folder.
  - Move `_archive/proto-98_phase0_2026-09-30/BOSS_CONCERNS.md` into the incident bundle and remove the folder.
  - Delete `docs/research/uni_v3_ORIGINAL_2026-09-29.md` if it is byte-identical to `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` (U29 twin), and fix AGENTS.md's pointer to the `.txt` (proto-95 fix-spec).
  - Every action gets one CLEANUP_EXECUTION_LOG line.
- **A8 — Git.** `git add -A level2/engine_docs level2/benchmark`, and `git rm --cached` the moved tracked paths, so git shows renames. **No commit without the boss.**
- **A9 — Verdict close.** A fresh subagent checks:
  - the sha manifests reconcile;
  - the smoke test passes;
  - the scores are regenerated;
  - the grep returns 0;
  - `ls level2` matches proto-101's target for this stage;
  - the incident record is complete.

  Only then may Agent 3 resume proto-101 at **P0 → P1**, under Part C, with Agent 2 gating each phase. P2 is done; the rest of P4 (`git rm level2/out`, `level2/engines`, the South v1 root scripts) waits until the new South packs exist.

- **A10 — U3, decided by the boss: archive the untracked `src/`, `tests/` and `configs/`** (after A9, under rule 17).
  - Write a sha manifest.
  - Bundle into `_archive/bundles/2026-09-30_src_u3.tar.gz`, then extract + sha = 100%.
  - Add `_archive/INDEX.md` lines.
  - Remove the originals. The delete prompt from the new OpenCode guard is expected; the boss approves it.
  - `scripts/evaluation/*` is not in U3; proto-74 rules on it.

## Part B — Fixes from the Verdict report (16:21), each with an owner
| # | Finding (Verdict report / RESEARCH_DECISIONS) | Fix | Owner |
|---|---|---|---|
| B1 | `CLEANUP_EXECUTION_LOG.md` still queues "172 DELETE + 4,082 MERGE" (Sep 28, "safe per audit") | Banner at the top: "QUEUE CANCELLED 2026-09-30 — superseded by proto-96/98/101/102; rows A–I never execute". From now on the file is D03: one line per EXECUTED action (action · path · target · reason · sha256 · who · time). Log Agent 3's 16:36–16:39 actions retroactively | Agent 2 |
| B2 | The log and BOSS_CONCERNS #71 say "`level2/models/` vs `level2/out/` are DIFFERENT — audit false positive" | Add a dated CORRECTION line: `models/*/json` were 4,000 byte-identical copies of `out/` (planner sample te_029 IDENTICAL; now in the south_v1 bundle) | Agent 2 |
| B3 | Licences (RF-05…RF-11) | Planner applied them in memory (Part D); docs that state otherwise get fact fixes | Agent 2 (docs) |
| B4 | No official deadline; "qualifiers 30/09" is Rajasthan's; "Oct 4" / "Oct 15" have no source (RF-02, RF-04) | Fix every live doc that states them (the proto-73 "dates" family). Also fix wrong weekdays: 2026-09-30 is a **Wednesday** (docs say "Tue 2026-09-30"), and 2026-10-01 is a **Thursday** (docs say "Wed 2026-10-01"); correct BOSS_CONCERNS #63 (proto-66). Asking the organisers (gic.dibd@gmail.com) is the boss's outward action (U36 item 6) | Agent 2 |
| B5 | "22 languages" is not an official requirement (RF-03) | Wording: "our scope — the official dataset has 24 language folders (22 scheduled + English + Mixed)" | Agent 2 |
| B6 | **RF-24 is wrong.** The Sep 10 transcript says "just start with 100 samples for each language … starting with 100" (textutil text, ~line 160); the grep missed the phrasing | Correct RF-24 (its own "correction" is REJECTED); keep proto-100 B-14's "start with 100 samples per language" | Agent 2 |
| B7 | RF-18: the S/D/I column of proto-80 is invalid (sampling cap per language, not per language × engine) | After A4, re-run `build_metrics_80.py` with the cap per (language × engine); replace `metrics_80.csv`; note it in RESEARCH_DECISIONS | Agent 2 |
| B8 | RF-13: 62.9% of `sheet.csv`'s stored CER cells don't re-derive; every headline survives recomputation | U9 evidence is ready; recommendation: adopt `sheet_v2.csv` for all reporting (boss decides) | boss |
| B9 | RF-15: surya 24.3 s/page ≈ 36 h for the 5,344 test images | The submission time budget uses Bodhan's measured Day-1 speed; the Day-4 gate is unchanged | Engine |
| B10 | New ~450-line reports `W4_reports/RQ1_official_rules.md` and `RQ9_licences.md` | Evidence papers: RESEARCH_DECISIONS rows carry the decisive quotes; both bundle at W4 close (proto-96); no new standalone reports (proto-97 rule 3) | Agent 2 |
| B11 | NEXT.md had two writers (the Verdict's 16:2x section was overwritten by the planner at 16:45) | Rule 19 (Part C): only the planner or the boss writes NEXT.md; agents write W4.md + DISPATCH_LOG | all |
| B12 | proto-98 Phase 0–1 died: Agent 1's GLM-5.3-flash subagent looped ("lock…lock…") and stopped at the output limit (16:31), producing nothing | After Part A, Agent 2 re-dispatches it with the single inventory script (C4) and the proto-98 Phase 0 global snapshot | Agent 2 |

## Part C — Binding execution rules (proto-01 rules 17–21)
- **17 — Destructive commands need proof first.** This covers `rm`, `rm -rf`, `git rm`, `find -delete`, `mv` of untracked data, and `>` overwrites. Each runs only after:
  - a pre-op sha256 manifest of the targets;
  - for untracked targets, a bundle verified by extract + sha;
  - a CLEANUP_EXECUTION_LOG line naming the verdict that allows it.

  **Forbidden:** the `mv X X_tmp; rm -rf X_tmp` pattern, and `2>/dev/null` on `mv` / `rm` / `cp` / `tar`.
- **18 — A phase is DONE only when its check output is pasted into W4.md.** A phase that "finishes" in seconds without its check is NOT DONE. The next phase starts only after the previous check, plus a Verdict PASS line where the protocol names a gate.
- **19 — Archives and NEXT.md.**
  - "Archive" = a verified bundle in `_archive/bundles/` + an `_archive/INDEX.md` line. Never a new per-folder directory under `_archive/`; never copied symlinks.
  - NEXT.md is written only by the planner or the boss.
- **20 — One inventory, one script.** `scripts/repo_inventory.py` (stdlib, one walk, < 5 min) writes all four files in `docs/campaign/audit/`:
  - `INVENTORY.csv` — all files: path, bytes, sha256, tracked, mtime, first heading, live refs.
  - `research_inventory.tsv` — proto-95 groups.
  - `archive_inventory.tsv` — proto-96: live_twin, git_twin.
  - `graph_signals.tsv` — from `graphify-out/graph.json`: in_graph, nodes, cross-file degree, island, community.

  Excluded: `.git`, `.venv*`, `Datasets`, `node_modules`, `graphify-out/cache`.
- **21 — A looping or truncated subagent is dead.** If `finish = length` or the reasoning repeats, the lead re-dispatches a smaller task, never the same prompt. Long protocol work goes to the steadier model lane.
- **Optional safety net (boss decision U37):** OpenCode permission config `"bash": {"rm *": "ask", "git rm *": "ask", "*": "allow"}`, so every delete asks the boss first.

## Part D — Planner updates made in memory with this protocol (agents don't redo them)
- **proto-92:**
  - U7 cleared at licence level (Apache-2.0; the download stays in U34).
  - **U14 re-framed:** the blocker is OpenRAIL-M Modified §2(c) (no product that competes with the licensor) + §8 share-alike to outputs, not the $5M cap → surya is evaluation-only.
  - **U27 → HOLD:** the card says CC-BY-4.0 but embeds a "Controlled Research Access License".
  - **U28:** Bodhan's attribution notice is for the user-facing product (§2.2); hosting needs prior written approval (§3.1); internal-component use (§3.2) is the design target.
  - U9: evidence ready.
  - U37: the delete-ask guard.
- **proto-89:** Day-4 fallback engines must be licence-cleared for shipping (surya evaluation-only). Script is read from Bodhan's output text (Unicode ranges), not by an image classifier.
- **proto-100:** B-03's Kashmiri data = OFL fonts + open text (600K-KS-OCR on HOLD); B-04 / B-07 route by output-text Unicode script (the IndicPhotoOCR script-ID has no sat/mni classes).
- **proto-01:** rules 17–21.
- **proto-83:** RQ-9 is the licence truth.

Related: [[proto-101-south-unification-and-level2-tree]], [[proto-98-clean-repo-master]], [[proto-96-archive-reports-compaction]], [[proto-95-research-harvest-decisions]], [[proto-01-law-and-guardrails]], [[proto-92-boss-decisions]], [[proto-66-concern-register-rebuild]], [[proto-73-md-fact-consolidation]]
