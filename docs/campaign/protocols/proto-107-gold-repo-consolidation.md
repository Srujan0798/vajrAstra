---
name: proto-107-gold-repo-consolidation
description: "Added 2026-10-01 ~14:40 IST (boss: 'merge into 24k gold … read all lines, all content … don't summarize or skip … 56,000 files who the hell will use them … write protocol for the agents end to end with 30-40 subagents in parallel using all skills') — the measured repo (203,380 files: junk vs data vs envs), the NO-LOSS merge law (fact ledger), 10 gated waves W0–W9 (30–40 Sonnet-class subagents for read-only waves, ONE serialized executor for every mutation), skills per wave, hazards (recursive level2/level2 symlink, 15,789 untracked benchmark files, 17,297 dead symlinks, 5 extra worktrees, a remote branch ahead), the official startup-grade tree, boss GO gates, done-when, paste lines. Supersedes the PARKED status of proto-98 (reuses its T1–T14, WORTH, tree)."
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-10-01T10:45:28.992Z
---

# PROTO-107 — 24K GOLD REPO: consolidate everything, lose nothing

**Boss, 2026-10-01 ~14:30 IST (intent, verbatim pieces):**
- "not even 1k gold… everything is shit hole and junk variant";
- "either u are deleting the variants without taking the values/content, or misled them, or archiving them";
- "don't summarize or skip or fast — take ur own time, read all lines, all content, compact, merge the relevant md files and make them official, original startup or a high-level repo way";
- "those 56,000 files who the hell will use or link them";
- "write protocol so the agent do them so carefully end to end with 30-40 sub agents parallel… using all skills for max output and efficiency".

**Skills used to write this:**
- readchk — understood as: a NO-LOSS consolidation of every authored file, not a deletion spree;
- graphify — 8,669 nodes / 9,890 edges / 802 communities, graph built 2026-10-01 04:47;
- ssotize — method: one fact = one home, variants become references;
- mandela — the merge is verified by agents who did NOT write it;
- verification-before-completion — every wave has a reproducing check.

## 0. The measured repo (planner, 2026-10-01 ~14:25 IST; W1 re-measures)
There are **203,380 files** (excluding `.git`). Most are NOT junk: they are the data and environments the project runs on, and deleting them breaks every engine. The real document mess is about 2,000 authored files.
- **`.venv311` — 83,263 files:** THE Python env (surya, paddle, easyocr, torch…). Keep; git-ignored; not project content.
- **`.venv` — 47,576 files:** the second env (Python 3.14 + mlx). Kept; W8 decides one env + a lock file.
- **`Datasets/` — 34,871 files:** the official hackathon data. SEALED, read-only, git-ignored.
- **`level2/` — 22,382 files:**
  - `benchmark/` 17,838 (pages, packs, scores);
  - `out/` 4,001 (South v1, retires at proto-104 S6);
  - `models_bodhan/` 387 (weights + Sarvam bench).

  This is data: keep it, and give the data dirs `.gitignore` rules (W0).
- **`.claude/` 4,119 · `.kilo/` 4,117 · `.opencode/` 3,650:** a Claude worktree copy, a Kilo worktree copy, and plugin node_modules. The worktrees are pruned after a clean check (W6, GO-G); `.opencode` is a tool and stays.
- **`_archive/` — 952 files, plus 17,297 DEAD symlinks:** facts get harvested into the finals; the dead symlinks are deleted (GO-D).
- **`graphify-out/` — 827:** generated; regenerate it, never hand-edit it.
- **`docs/` — 744:** research/level7 554 · research 19 · campaign 149 · others. THE main merge target.
- **`arc_level_1/` — 413:** Level-1 labelling archive. SEALED.
- **`.deps/` — 259 files, 4.4 GB:** the IndicPhotoOCR engine. Keep (it may move to `third_party/` later).
- **`_reports/` — 58:** their facts go into the T12 final, then they are archived.
- **Code:** `src/` 46 (archive per U3) · `product/` 30 (keep) · `scripts/` 8 (keep) · `tests/` 2 · `configs/` 1.
- **Root:** 18 md files plus misc, including stale and misleading ones. Target: an official root of 4–6 files (W8).

**557 md files** sit in project areas. Same-name variants:
- README ×16, RUN ×10, PROMPT ×10 (engine docs — legitimately many);
- VINAY_MEETING_PACKET ×6, MENTOR_PLAYBOOK ×5, DRAFT_RESEARCH_PLAN ×5, LEDGER ×5, W5_BEAT_SARVAM_PLAN ×4, COMPETITOR_INTEL ×4, BOSS_CONCERNS ×3, MONITOR_2026-09-30 ×3, INDEX ×3, GRAPH_REPORT ×3, uni_v3 ×2.

**Git:**
- `main` = `origin/main` (8fec177), with 4,116 tracked files.
- 34,350 untracked files that are not ignored: 17,297 dead symlinks in `_archive/south_unified_symlinks_2026-09-30/`, 15,789 under `level2/benchmark/`, 573 in `docs/research`, 149 in `docs/campaign`, and more.
- 174,557 ignored files.
- Branches:
  - local `boss/campaign-docs` is at 41de158, but `origin/boss/campaign-docs` is AHEAD at 2ae8a5b (the cloud planner's commits);
  - `claude/heuristic-kapitsa-b4ef8d` is a worktree in `.claude/worktrees/`;
  - remote `claude/stoic-keller-xwovqu` = PR #12, reference only.
- Worktrees: `/private/tmp/bc` and `/private/tmp/bc_90b` (both marked prunable), `/private/tmp/bc_new`, `.claude/worktrees/heuristic-kapitsa-b4ef8d`, `.kilo/worktrees/screeching-shallot`.

**Hazards:**
- **H-1: `level2/level2 -> .`** — a symlink to ITSELF, created 2026-09-30 20:39, most likely to satisfy the `run_probe.py` `parents[2]` path bug. **A4 PASS may depend on it.** Tools that follow symlinks can loop on it.
  - W0 proves that `run_probe.py` resolves `level2/benchmark/…` WITHOUT the link: print its path constants with `python3 -c`, then run the smoke test with the link renamed aside and restored.
  - Only after that proof is the link removed (GO-D). If the code needs the link, the real path fix (R-2) comes first.
- **H-2:** the 15,789 untracked `level2/benchmark/` files are NOT ignored. One `git add -A` would put data into git, against Vinay's no-data-in-GitHub rule. W0 adds `.gitignore` rules (additive only).
- **H-3:** 17,297 dead symlinks.
- **H-4:** 5 extra worktrees.
- **H-5:** the remote branch is ahead of local.
- **H-6:** `NEXT.md` rev 5 was written by Agent 2 (rule 19 says planner/boss only) and contains errors. The planner rewrites it.

## 1. THE NO-LOSS LAW (why earlier cleanups failed — read twice)
1. **Read every line.** A worker reads each assigned file in full (in chunks if big) and logs coverage `lines_read == wc -l`. A file without full coverage can't be merged, archived or deleted.
2. **Facts before fates.** From every variant, extract an atomic FACT LEDGER: every number, decision, date, quote, command, path, rule, finding and open question, with `source file:line`.
   - Format (JSONL): `{fact_id, topic, kind, text, source, line, date (ISO 8601), status_hint, verify}`.
   - Synthetic example: `{"fact_id":"T6-0042","topic":"T6","kind":"number","text":"Bodhan 84.94 on Sarvam bench","source":"docs/campaign/COMPETITOR_INTEL.md","line":31,"date":"2026-09-30","status_hint":"current","verify":"WebFetch sarvam blog"}`.
3. **Every fact gets exactly one fate in its topic's final.**
   - **INCLUDED:** cited in the final with its source.
   - **REJECTED,** with a reason from a closed list: `DUPLICATE-OF <fact_id>` · `SUPERSEDED-BY <decision/file>` · `CONTRADICTED-BY-DISK <command + output>` · `OUT-OF-SCOPE` · `UNVERIFIABLE`.

   Rejected facts live in the topic's `REJECTED.md`. Nothing silently vanishes.
4. **Contradictions are resolved by disk evidence, never by taste.** Run the command, or apply the latest boss ruling (proto-104 / proto-92). Otherwise the item goes to `BOSS_DECISIONS_PENDING.md`.
5. **Archiving is not loss; deleting is only for provable twins.**
   - A file leaves the working tree only after ALL its facts are INCLUDED or REJECTED-with-reason (script-checked).
   - An archived file goes into a verified tarball bundle + an INDEX line (+ its original path).
   - DELETE is allowed ONLY for: sha256-identical duplicates whose twin is kept; caches (`__pycache__`, `.DS_Store`, `.pytest_cache`); dead symlinks; empty files/dirs; and the H-1 self-link after its proof.
   - Every delete needs the boss's GO-D and proto-01 rules 17–21: sha manifest + verified bundle + log line; no `2>/dev/null` on mv/rm/cp/tar.
6. **Out of scope for merging:** data, envs and sealed dirs — `Datasets/`, `arc_level_1/`, `level2/out/` (until proto-104 S6), `level2/benchmark/{pages,packs,scores}`, `.venv*`, `.deps/`. They get only `.gitignore` rules + map entries.
7. **Single writer.** The 30–40 subagents READ and PROPOSE in parallel. ONE executor (the lead) performs every move, merge and delete, one at a time, with one CLEANUP_EXECUTION_LOG line per action.
8. **Live files are never touched mid-run:**
   - `docs/campaign/checkpoints/*`, `DISPATCH_LOG.md`, `NEXT.md`, `BOSS_CONCERNS.md` Part 1;
   - any file Agent 1 or 2 wrote in the last 30 minutes (check mtimes).

   Their finals go to staging and are swapped in only during the W6 window, with the owning agent's ACK.

## 2. Owners
- **Lead: Agent 3** (`ses_f16bc20e…`).
  - Runs this lane with OpenCode subagents — Sonnet-class or equivalent, NEVER Opus.
  - Up to 40 subagents in parallel for the read-only waves W1–W4.
  - The ONLY executor in W6–W8.
- **Verifier: Agent 2** (`ses_f1233a0a…`). Blind-verifies every wave with its own 5–10 subagents that did NOT produce the work, and posts PASS/FAIL in W4.md.
- **Agent 1** stays on the project (S4/D1/H3). The lead never touches Agent 1's paths: `level2/benchmark/**`, `level2/models_bodhan/**`, the run scripts.
- **The boss** gives three approvals:
  - GO-A: the archive moves;
  - GO-D: the law-5 deletion classes only;
  - GO-G: git — prune worktrees and commit to a LOCAL branch `gold/2026-10-01`; push only on his word.

## 3. The waves
Each wave ends with its check pasted into W4.md. No wave starts before the previous one is PASS.

### W0 — Safety + freeze
Lead + 2 subagents, ~30 min. Skills: `gateguard`, `terminal-ops`, `safety-guard`.
1. Post `GOLD W0 START` in DISPATCH_LOG. List the running agent processes and record Agent 1/2's live paths.
2. Write a sha256 manifest of every authored file (everything except the law-6 list) to `docs/campaign/gold/W0_manifest.sha256`.
3. Bundle those files into `_archive/bundles/2026-10-01_pre_gold.tar.gz`. Extract into scratch and compare sha = 100%.
4. Add `.gitignore` rules (additive only): `level2/benchmark/pages/`, `level2/benchmark/packs/`, `level2/models_bodhan/`, `out_level3/`, `.pytest_cache/`, `**/__pycache__/`, `*.DS_Store`. Check: `git ls-files --others --exclude-standard | wc -l` falls by about 15,800.
5. Run the H-1 proof (§0) and record the result. Do NOT remove the link yet.
6. Run `git fetch origin` (read-only refs). Record local vs `origin/boss/campaign-docs`. No merge.

**Check:** the manifest line count = the authored-file count; the bundle verifies at 100%; the H-1 proof output is pasted.

### W1 — Inventory
Lead + 30–40 subagents IN PARALLEL, read-only. Skills: `graphify` (`graphify query`, GRAPH_REPORT), `workspace-surface-audit`, `repo-scan`.
1. The lead writes ONE stdlib script, `scripts/gold_inventory.py` (≤150 lines).
   - It lists every authored file with: path, size, sha256, git state, mtime, line count, inbound refs (grep of basename + path across the repo, plus graphify neighbours), outbound links.
   - It splits the list into ~35 shards of ≤60 files, grouped by directory.
2. Each subagent takes one shard and fills in, per file:
   - **topic:** T1–T14 from proto-98, or CODE / DATA / TOOL / ENGINE-DOC;
   - **WHAT:** one line;
   - **WHO USES IT:** the referrers, as file:line;
   - **WORTH:** proto-98 formula C+D+U+F+T+G, 0–100;
   - **proposed fate:** CANONICAL / MERGE-INTO <final> / ARCHIVE-AFTER-HARVEST / DELETE-CANDIDATE (law-5 classes only);
   - **coverage:** `lines_read/lines`.

   Output goes to `docs/campaign/gold/inventory/shard_NN.tsv`.
3. The lead concatenates the shards into `docs/campaign/gold/FILE_LEDGER.tsv`.
   - Columns: `path, size, sha256, git_state, mtime, lines, inbound_refs, outbound_links, topic, what, who_uses, worth, fate, coverage`.
   - Synthetic row: `docs/x.md · 2048 · ab12… · untracked · 2026-09-30T18:00 · 64 · 3 · 2 · T6 · competitor table · docs/INDEX.md:12 · 41 · MERGE-INTO docs/campaign/COMPETITOR_INTEL.md · 64/64`.

**Check (Agent 2 + 5 blind subagents):** re-derive a random 10% of rows.
- Row count = the W0 manifest count.
- Coverage is 100% on every row.
- ≥ 95% agreement on topic/fate, with every disagreement resolved in the ledger.

### W2 — Variant clusters
Lead + 4 subagents, read-only. Skills: `graphify`, `ssotize` (AUDIT mode only).
- Cluster by: (a) sha-identical files; (b) the same basename; (c) title/heading similarity (shared H1/H2, date-stripped names like `*_2026-09-29`); (d) graphify communities holding ≥ 2 md files on one topic.
- Output: `docs/campaign/gold/VARIANT_CLUSTERS.tsv` — cluster_id, topic, members, proposed canonical home, why.
- Known clusters to confirm: VINAY_MEETING_PACKET ×6, MENTOR_PLAYBOOK ×5, DRAFT_RESEARCH_PLAN ×5, LEDGER ×5, W5_BEAT_SARVAM_PLAN ×4, COMPETITOR_INTEL ×4, BOSS_CONCERNS ×3, MONITOR ×3, INDEX ×3, uni_v3 ×2, and the 554-file `docs/research/level7/` campaign tree.

**Check:** every md file in the ledger sits in exactly one cluster or is marked SINGLETON.

### W3 — Fact extraction (the heart of "no loss")
Lead + 30–40 subagents IN PARALLEL, read-only. Skills: `search-first`, `iterative-retrieval`, `factchk` (numbers), `deep-research` (only to re-open a cited external source).
- One subagent per cluster or topic shard: T1–T14, plus the level7 tree split into ~15 shards.
- Each reads EVERY member file in full. It writes `docs/campaign/gold/facts/<topic>__<shard>.jsonl` (law-2 format) and a coverage log.
- Every number gets a `verify` field: the command that reproduces it from disk, or `UNVERIFIED`.
- Every Vinay quote must map to proto-103 L1–L14, or be flagged.

**Check (Agent 2 + 8 blind subagents):** for 10 random source files, a blind reader lists every fact independently. The extractor's recall must be ≥ 98%; any miss means that shard is re-run.

### W4 — Write the finals (to STAGING only)
Lead + 14–16 subagents, one per final. Skills: `ssotize` (mutation plan), `living-docs-governance`, `paperthin` (anti-slop), `factchk`.
1. One final per topic, written from its fact ledger into `docs/campaign/gold/staging/<final path>`:
   - **T1** `docs/PLAN.md` — proto-104 rev 4 + Plan v3, human-readable.
   - **T2** `docs/STATE.md` — replaces FULL TECHNICAL BRIEFING, PROJECT_COMPLETE and the README state section.
   - **T3** law: `AGENTS.md` (short) + `docs/LAW.md`. The latter includes `level2/ULTIMATE_HYBRID_CONCERN.md` HL1–HL12 as a section; they are not lost.
   - **T4** `docs/campaign/BENCHMARK_22.md` plus a numbers registry.
   - **T5** `docs/campaign/SAMPLING_PLAN.md`.
   - **T6** `docs/campaign/COMPETITOR_INTEL.md`.
   - **T7** `docs/campaign/EDGE_THESIS.md`.
   - **T8** `docs/MEETINGS.md` — proto-103 §0 + the facts from the meeting packets.
   - **T9** `docs/TOOLS.md` — proto-88 status.
   - **T10** `BOSS_CONCERNS.md` Part 0, refreshed.
   - **T11** `docs/INDEX.md` — THE map.
   - **T12** `docs/HISTORY.md` — audit/cleanup records + what happened when.
   - **T13** `DISPATCH_LOG.md` (unchanged, live) + a checkpoints index.
   - **T14** `docs/campaign/RESEARCH_DECISIONS.md` — all 88 + 554 research files harvested (proto-95 rules).
2. Each final carries a `## Sources` list (every merged file + its fact count) and a `REJECTED.md` (law 3). A final may not say "see the old file" for content: the content moves, and only history links remain.
3. Engine docs (README/RUN/PROMPT ×10, one set per engine) are legitimate per-engine files. They are NOT merged; they get one `level2/engine_docs/INDEX.md`.

**Check:**
- Script first: `scripts/gold_fact_check.py` asserts every fact_id in `facts/<topic>*.jsonl` appears in the final (by cited source) or in REJECTED.md with an allowed reason → 0 unaccounted.
- Then Agent 2: a blind reader confirms 20 random facts per final.

### W5 — The boss reviews
The boss, ~20 min. The lead posts in chat:
- the list of finals with sizes;
- per final: facts in, and facts rejected by reason;
- `BOSS_DECISIONS_PENDING.md`;
- the archive list (count + bytes);
- the DELETE-CANDIDATE list by class.

The boss answers GO-A / GO-D / GO-G; each may be partial.

### W6 — Execute
ONE executor (the lead), serialized, only after the GOs. Skills: `gateguard`, `safety-guard`, `verification-loop`.
1. Window: post `GOLD W6 MOVE WINDOW START`. Agents 1 and 2 ACK that they are not writing the affected paths.
2. Swap the staged finals into place. Put a pre-image of each replaced live file into the bundle first.
3. ARCHIVE:
   - move each file to `_archive/gold_2026-10-01/<original path>`;
   - add its `_archive/INDEX.md` line and a CLEANUP_EXECUTION_LOG line;
   - bundle the batch, sha-verify it, then remove the originals from the working tree.
4. DELETE (GO-D classes only): dead symlinks, caches, sha-twins, empty dirs, and the H-1 self-link (after its W0 proof). One log line each.
5. GO-G:
   - `git worktree prune` for the prunable `/private/tmp/bc*`;
   - remove the `.kilo` and `.claude` worktrees only if `git -C <wt> status --porcelain` is empty;
   - commit the gold state to a LOCAL branch `gold/2026-10-01`. No push.

**Check:**
- before = after + archived + deleted, exactly, in counts and bytes;
- the CLEANUP_EXECUTION_LOG line count = the number of actions.

### W7 — Links
Lead + 5 subagents. Skills: `graphify`, plus a stdlib link checker.
- `scripts/gold_link_check.py` scans every md file for relative links and file mentions.
- Every reference to a moved file is rewritten to point at the final, or at the archive path when it is history.

**Check:** 0 dead links in live docs; `graphify update .`; report islands before → after.

### W8 — The official repo shape
Lead + 2 subagents. Skills: `ecc:update-docs`, `paperthin`.
1. **Root:**
   - `README.md` (≤ 60 lines: what, who it is for, how to run the product, read order);
   - `AGENTS.md` (≤ 60 lines: START HERE, hard rules, pointers);
   - `BOSS_CONCERNS.md`, `DISPATCH_LOG.md`;
   - `LICENSE` / `NOTICE` (Bodhan attribution, Apache tessdata, Sarvam bench Apache-2.0);
   - `requirements.txt`, `.gitignore`.

   Every other root md goes to its final or to `_archive`.
2. **Tree:**
   - `docs/`: INDEX, PLAN, STATE, LAW, MEETINGS, TOOLS, HISTORY, plus `campaign/`, `architecture/`, `sources/`, `legal/`;
   - `product/` (the portable package + Dockerfile);
   - `level2/benchmark/` (data + pipeline);
   - `scripts/`, `tests/`;
   - `_archive/` (INDEX + bundles only).
3. **One Python env:** `.venv311` is THE env, plus a `requirements.lock`. Whether `.venv` is retired or kept is the boss's call. It is 47k files of ignored tooling — not junk to delete blindly.

### W9 — Final verification
Agent 2 + 6 blind subagents. Skills: `verification-before-completion`, `delivery-gate`, `mandela` (were the checks independent?).
1. Reconcile:
   - counts before / after / archived / deleted;
   - facts 100% accounted for;
   - 0 dead links;
   - `git status` clean except the intended changes;
   - the out-of-scope dirs byte-identical (sha samples).
2. Report to the boss in ≤ 15 lines:
   - the new `ls` of root and docs;
   - each final with its fact count;
   - what was archived or deleted, and how to restore it (bundle + INDEX);
   - the open boss decisions.

## 4. Done when
- `scripts/gold_fact_check.py` → 0 unaccounted facts.
- `scripts/gold_link_check.py` → 0 dead links.
- Root md count ≤ 4 (+ LICENSE/NOTICE).
- `docs/research/` holds only sources cited by RESEARCH_DECISIONS.
- 17,297 dead symlinks gone; H-1 resolved; H-2 ignored; worktrees pruned per GO-G.
- W9 PASS is in W4.md, and the boss says "this is gold".

## 5. Paste lines
1. **Agent 3:** `Read docs/campaign/protocols/proto-107-gold-repo-consolidation.md in full. You are the lead and the ONLY executor. Do W0 now (safety + freeze; .gitignore additions; the H-1 proof — do not remove the link). Then W1–W4 with up to 40 Sonnet-class subagents in parallel for reading/extraction, writing only to docs/campaign/gold/. Never touch level2/benchmark/**, level2/models_bodhan/**, Datasets/, live checkpoint files. Post each wave's check in W4.md and wait for Agent 2's PASS before the next wave. Stop at W5 and post the boss review pack.`
2. **Agent 2 (after Agent 3 posts each wave):** `Read proto-107. Blind-verify wave W<n> per its Check with your own 5–10 subagents that did not do the work; post PASS/FAIL in W4.md. Do not edit NEXT.md (planner/boss only).`
3. **The boss:** at W5, answer GO-A / GO-D / GO-G.

Related: [[proto-98-clean-repo-master]] (T1–T14, WORTH formula, earlier target tree), [[proto-104-project-first-critical-path]], [[proto-01-law-and-guardrails]], [[proto-88-skill-routing]], [[boss-rules]]
