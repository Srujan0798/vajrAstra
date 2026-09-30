---
name: proto-95-research-harvest-decisions
description: "Added 2026-09-30 (boss: 'no one is using the research output md files… take clear decisions and merge/condense/delete/archive') — W4, supersedes proto-40: every research file (86 md in docs/research + ledgers + Lane-B records + W1/W2 papers + level2 research) is read; each finding becomes a row (ADOPTED/ALREADY-IN/REJECTED/OPEN/CONTEXT) in RESEARCH_DECISIONS.md; each file gets one fate (KEEP ≤15 / MERGE / CONDENSE / ARCHIVE-to-bundle / DELETE-DUP / DELETE-CONVERSION); Verdict decides, Miss executes, Verdict re-verifies"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:07:22.046Z
---

# PROTO-95 — RESEARCH HARVEST: every research file → decisions → one fate (W4; supersedes [[proto-40-w4-research-corpus]])

**Boss, 2026-09-30:** "no one is using all the research output md files … I need them [to] take clear decisions and merge or condense or delete those after taking a clear decision, or archive them … we have done a huge research and also some more to do … all should be sorted out."
Concerns: CO-002, CO-004, CO-013, CO-066, HC14.9, H1 ([[proto-99-concern-crosswalk]] §H). The missing research lives in [[proto-97-research-still-to-do]]; compacting archives and reports afterwards is [[proto-96-archive-reports-compaction]].

**Why (measured 2026-09-30 ~15:30 IST):**
- `docs/research/` holds 571 files and 4.7 MB: 86 md, 446 .json, 36 .jsonl, 2 .py and 1 other. Plan v3 ([[proto-89-plan-v3-bodhan-base]]) cites almost none of it.
- Between 14:46 and 15:09 today, agents wrote or edited documents that compete with Plan v3 and with the GT-tier rule:
  - `docs/research/W6_STRATEGY_UNIFIED.md` ("Final Plan")
  - `PROBE22_EDGE_ANALYSIS.md` ("Where We Beat Sarvam Vision 2.1")
  - `ACTUAL_PROBE22_RESULTS.md` ("vs Sarvam" column)
  - `SURYA_LIVE_INFERENCE_RESULTS.md` (n = 3 brx images)
- `AGENTS.md` "KEY FILES" points at two files that no longer exist: `_reports/research/MEETING_2026-09-29_STRUCTURED.md` and `docs/research/uni_v3_ORIGINAL_2026-09-29.md`.
- Research that changes no decision is noise; research that should change a decision but is not wired in is waste. This protocol removes both.

## Scope — 10 groups (re-count in Step 1; numbers drift)
| G | Files | Size | Notes |
|---|---|---|---|
| G1 live-research passes | `docs/research/{DEEPER_LIVE_RESEARCH_2026-09-29 (1,057 lines), DEEP_RESEARCH_STRATEGY_2026-09-29, W1_RECIPE_REFRESH (git-tracked), SOURCES}.md` + root `LIVE_LATEST_2026-09-29.md` | ~150 KB | the docs/research copy of LIVE_LATEST no longer exists (root copy is the only one); DEEP_RESEARCH_STRATEGY's errors are listed in proto-89 |
| G2 agent plans/results of 2026-09-30 — **HIGH RISK** | `docs/research/{W6_STRATEGY_UNIFIED, PROBE22_EDGE_ANALYSIS, ACTUAL_PROBE22_RESULTS, SURYA_LIVE_INFERENCE_RESULTS}.md` | ~40 KB | a competing "Final Plan" + "beat Sarvam" headlines |
| G3 research lanes R1–R7 | `docs/research/R1_SOTA_MECHANISM_TEARDOWN, R2_NASTALIQ_FORENSICS, R3_OLCHIKI_MAYEK_SYNTHETIC, R4_OLDSCAN_RESTORATION, R6_COMPETITION_INTEL, R7_W6_TRAINING_TREE` (.md) | ~140 KB | directly relevant to Plan v3: Kashmiri, sat/mni, degraded scans, hackathon rules |
| G4 Level-7 control docs | `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md`; `docs/research/level7/*.md` (15: CALL_PACKET, FINAL_VERDICT_2026-09-27, FIX_SPECS_FOR_MISS, FIX_SPECS_R2_LEADERBOARD, H48_ENGINE_SPOTCHECK, H48_HOSTILE_PASS, HUMAN_SPOTCHECK_PACKET, KILL_CRITERIA, MISS_MONITOR, PROMPT_{ENGINE,MISS,VERDICT}_AGENT, SANTA_METHOD_FINAL, W5_FREEZE_AGENDA, W6_QLORA_SPEC); `level7/boss_directives/` (5) | ~340 KB | boss_directives hold the boss's own words |
| G5 lane ledgers | `level7/a/{LEDGER (655 KB, 7,070 lines), MANIFEST}`, `level7/c/c1/{LEDGER, 5× NOTE_*}`, `c/c2/LEDGER`, `c/c3/{LEDGER, STRATEGY}`, `c/c4/{LEDGER, LEDGER_FORMAT, OBITUARIES}`, `level7/{audit,repair}_section9.py` | ~1.15 MB | the bulk |
| G6 Lane-B raw records | `level7/b/`: b3 multi-agent orchestration, b4 agent tooling (incl. `laya_detailed`, `laya_gates`), b5 elite repos + `ELITE_REPO_REFRESH_2026-09-27.md` | 446 json + 36 jsonl + 35 md | **34 of the 35 md say "converted from X.jsonl — all records, fields verbatim"** = format copies |
| G7 `_reports/research/` | VAJRASTRA_INTERROGATION_PROTOCOL, PROTOCOL_1_RESEARCH, PPT_VS_SPEC_DIFF, PPT_FULL_DUMP, LEVEL7_RESEARCH_FINDINGS | 116 KB | PPT_FULL_DUMP feeds [[proto-75-vinay-plan-baseline]] |
| G8 Wave-1/2 outputs | `docs/campaign/{BENCHMARK_22, COMPETITOR_INTEL, EDGE_THESIS, MENTOR_PLAYBOOK, MULTI_LLM_EVAL, CHATGPT_EVAL_PROMPT, DRAFT_RESEARCH_PLAN, SAMPLING_PLAN, SHEET_V2_FORENSICS}.md`; `checkpoints/W1_reports/` (10); `checkpoints/W2_reports/variance.md`; **`MONITOR_2026-09-30.md` exists twice** (`docs/campaign/` 12 KB and `docs/campaign/checkpoints/` 1 KB, 14:58) | ~0.45 MB | W1 is VERIFIED (W1.md) |
| G9 level2 research + W6 prep | `level2/research/gates/` (B1, B3, B4, B12 + json, 09-13/14); `level2/probe22/{LEADERBOARD_REFRESH_2026-09-29, MLX_INSTALL_RESULT, QLORA_EVAL_SPEC, QLORA_READINESS, QLORA_SMOKE_TEST, QLORA_TRAINING_DATA, MEMORY_AUDIT, MEMORY_RECLAIM_RESULT, FINAL_REPORT, transfer_obituaries, w6_feasible_set, w6_set_construction_log, verify_unaccounted}.md`; `level2/probe22/scores/*.md`; `level2/probe22/fix_specs/` (3) | ~0.4 MB | **fates recorded here; moves ONLY via [[proto-70-level2-restructure]] after U10.** Never the 4 locked files or `probe22/out/` |
| G10 root research/plan docs | `PAPERTHIN_AUDIT, LOOP_SPEC_W5_W6_W7, W5_FREEZE_PLAN, INTEGRATED-ELITE-STACK, SAMPLE_PLAN_18_LANGS, AUDIT_REPORT, PROTOCOL_UPGRADES, PROJECT_COMPLETE` (.md, root) | ~95 KB | harvest findings only; file fates belong to [[proto-74-root-hidden-hygiene]] |

**Earlier cleanup plans are INPUTS — read, don't redo:** `docs/research/DEDUP_DOCS_RESEARCH.md` (12 topic groups for docs/research, 2026-09-29), `_reports/analysis/{MD_CONSOLIDATION_PLAN, DUPLICATE_MAP, FILE_INVENTORY}.md`, `_reports/cleanup_cycle1–3/`. Take their verdicts; re-check only what changed since.
**Out of scope:** the protocols and their mirror `docs/campaign/protocols/` (the memory directory is the source), `CAMPAIGN_DIRECTIVE.md`, `OCR_AGENT_MEMORY_FEED.md`, `BOSS_CONCERNS.md`, `DISPATCH_LOG.md`, sealed dirs, locked files, and primary sources (they move to `docs/sources/` in [[proto-98-clean-repo-master]] Phase 1: `docs/research/MEETING_2026-09-29_STRUCTURED.md`, `_reports/research/PPT_FULL_DUMP.md`, the Sep 10 docx, `Untitled-1.ini`, the proposal PPTX).

## Outputs — exactly two new files
1. **`docs/campaign/RESEARCH_DECISIONS.md`** — the register. One row per decision-relevant finding:
   `RF-### | finding (one plain line) | source file:line (+ URL if external) | evidence tag | decision it touches (Plan v3 day/gate · U# · proto step · C#) | verdict | where it landed | owner`.
   Verdicts:
   - **ADOPTED** — applied; name the file and line changed.
   - **ALREADY-IN** — name where.
   - **REJECTED** — one-line reason plus the evidence.
   - **OPEN** — becomes an RQ in proto-97.
   - **CONTEXT** — true, but changes no decision; lives only in the bundle.

   The top of the file carries the counts per verdict and a "what the research changed" summary for the boss (≤ 10 lines).
2. **`docs/campaign/audit/RESEARCH_FATES.csv`** — one row per in-scope file:
   `path, group, bytes, sha256, live_inbound_refs (count + 3 referrers), fate, target, reason, executed(Y/N), bundle`.

| Fate | When |
|---|---|
| KEEP | A live protocol, plan step or open decision cites it, and nothing else holds that content. **Target: ≤ 15 live md in `docs/research/` (from 86).** |
| MERGE→file | Its live content (decisions, numbers, sources) moves into a named canonical file with a source line; the file then goes into the bundle. |
| CONDENSE | A long file whose decisions go to RESEARCH_DECISIONS and whose remainder is history → bundle. |
| ARCHIVE | History only → bundle. |
| DELETE-DUP | sha256-identical to a kept file (name it). |
| DELETE-CONVERSION | A format copy of a kept source (name the source). |

Nothing else is deleted (U29 in [[proto-92-boss-decisions]]). Every file also gets its WORTH score (0–100, six components C/D/U/F/T/G) per [[proto-98-clean-repo-master]]; the band gives the default fate, and an override needs a written reason.

**Standing rule from now on (already proto-01 rule 16; Miss adds it to the AGENTS.md hard rules via the Step 2 fix-spec):** research results go into `RESEARCH_DECISIONS.md` rows. No new md file under `docs/research/` without a KEEP reason in RESEARCH_FATES.csv.

## Step 0 — Pre-flight (Miss, ~10 min)
> This protocol runs as Phase 2 of [[proto-98-clean-repo-master]]. If proto-98's Phase 0 global snapshot exists, skip items 4–5 below — it covers them.
1. Run the [[proto-02-preflight-and-checkpoints]] pre-flight.
2. Confirm no agent is writing under `docs/research`, `docs/campaign` or `_reports`. The bootstrap counted 7 agent processes at 15:13 IST; check `DISPATCH_LOG.md` and `ps`.
3. Run `graphify --update` (the graph was STALE).
4. Take ONE safety snapshot — the pre-image for every later change. No per-file copies: per-file copies are how `_archive/` filled with junk.
   ```
   mkdir -p _archive/bundles
   tar -czf _archive/bundles/2026-09-30_research_pre_harvest.tar.gz docs _reports level2/research level2/probe22/*.md level2/probe22/scores level2/probe22/fix_specs *.md
   ```
5. Record the snapshot's sha256 (`shasum -a 256`) and its entry count (`tar -tzf … | wc -l`) in `DISPATCH_LOG.md`.
6. Create checkpoint `docs/campaign/checkpoints/W4.md` with `STATUS: proto-95 STARTED`.

## Step 1 — Inventory (Miss; script `scripts/research_inventory.py`, stdlib only, ≤ 80 lines)
For every in-scope file, record:
- group (G1–G10 per the table), bytes, lines, mtime, git-tracked, sha256, first heading;
- **live inbound references** — grep the basename and the repo path across live md/py/json/yaml/sh. Exclude `_archive/`, `.venv*`, `graphify-out/cache`, `.kilo/` and the protocols mirror. Count append-only logs (`DISPATCH_LOG.md`, `MISS_MONITOR.md`, `W*.md` checkpoints) separately as HISTORICAL;
- **dead outbound links** — paths the file mentions that do not exist;
- for ledgers, the **record count**. Learn each ledger's delimiter from its first 60 lines; C4's format is in `c4/LEDGER_FORMAT.md`.

Output: `docs/campaign/audit/research_inventory.tsv`. Done when per-group totals equal `find` counts; paste the totals into W4.md.

**Step 1b — Laya triage trial (U31).** Run as defined in proto-98 §Laya. Laya's suggestion and confidence are recorded per file as an advisory column only; they never decide a fate. Join `graph_signals.tsv` (proto-98 Phase 1) onto the inventory for the G component.

## Step 2 — Read and decide (Verdict lead + ≤ 5 Sonnet subagents in parallel; never Opus)
Split the work into six subagent slots:
1. G1 + G2
2. G3
3. G4 + G7 + G10
4. G5 ledger A (two subagents, split at a record boundary)
5. G5 C-ledgers + G6
6. G8 + G9

Each subagent gets:
> TASK (paste after the shared context block of proto-01). You are a Verdict harvester for group(s) ⟨G…⟩. Files: ⟨list from research_inventory.tsv⟩.
> Truth set to check every finding against: proto-89 (Plan v3), proto-92 (decisions), proto-93 (measured facts), conflicts-register C1–C12, proto-62 (GT-tier rule), proto-31 (Laya ruling).
> 1. Read every file in full (ledgers record by record, see 2). No verdict from a filename or a heading.
> 2. Ledgers and Lane-B records: tag each record with one Plan v3 keyword family:
>    Indic scripts/languages · Bodhan/Sarvam/surya/Qwen/VLM recognisers · LoRA/QLoRA/MLX/training · layout/reading order · handwriting/degraded/restoration · synthetic data · licences · benchmarks/metrics · hackathon rules/deadline/competitors · agent tooling.
>    Records with no family are CONTEXT in bulk. Read a random 5% of those CONTEXT records in full. If more than 5% of that sample was decision-relevant, widen the families and redo the pass.
> 3. Each decision-relevant finding → one RESEARCH_DECISIONS row:
>    - ALREADY-IN (say where);
>    - ADOPTED candidate (exact fix-spec: file, old → new);
>    - a new U# draft if it changes scope, cost, a download or training (the boss decides);
>    - REJECTED (evidence);
>    - OPEN (the question, for proto-97);
>    - CONTEXT.
> 4. Known traps — check hard:
>    - Any "we beat Sarvam" needs the same GT tier and metric. proto-62: on human GT, Sarvam 0.064 vs best local 0.243; locals lead only on PDF-layer GT.
>    - Per-language claims at n ≤ 5 are DIRECTIONAL.
>    - "11 independent engines" is false: openbharatocr ≈ tesseract_indic on 1,225/1,227.
>    - Punjabi K1 is a tie (p = 1.0).
>    - The hackathon rubric is UNKNOWN: the CER/WER/S-D-I/sec-per-page list came from a student repo (F43).
>    - Probe = 1,227 scored / 1,283 manifest. South scored n = 126/400.
>    - Sarvam bench n appears as both 6,609 and 6,909 in our files. Don't repeat either until proto-97 RQ-7 settles it.
> 5. Give each file its fate (proto-95 table), with the evidence: live inbound refs, and what part of it is still live.
> Report: your RESEARCH_DECISIONS rows, your RESEARCH_FATES rows, and the claims you could not verify. Under 1,500 words plus the rows.

**Rulings each group must make (so nothing is skipped)**

**G2** — there is ONE plan: Plan v3 (proto-89 + the shared doc).
- W6_STRATEGY_UNIFIED: harvest any sourced idea Plan v3 lacks (a new U# if it changes scope). The file becomes ARCHIVE, "superseded by proto-89".
- PROBE22_EDGE_ANALYSIS and ACTUAL_PROBE22_RESULTS: re-check every "vs Sarvam" number per GT tier.
  - A misleading headline becomes a REJECTED row carrying the corrected statement.
  - Correct per-tier numbers MERGE into `BENCHMARK_22.md` only if missing there.
  - Then ARCHIVE.
- SURYA_LIVE_INFERENCE_RESULTS: keep the facts "surya ran from `models--datalab-to--surya-ocr-2-gguf`" and "brx output empty or not". MERGE them into [[proto-82-engine-empty-output-patterns]] evidence, then ARCHIVE.

**G4**
- `boss_directives/`: first confirm every directive is verbatim in `BOSS_CONCERNS.md` ([[proto-66-concern-register-rebuild]]). Append any that are missing, then bundle.
- `PROMPT_*_AGENT.md`: superseded by the AGENTS.md START HERE block + protocols. ARCHIVE, plus a fix-spec for AGENTS.md "Load in this order" item 8.
- KILL_CRITERIA (its Punjabi line was corrected by proto-86): decide one of two —
  - its still-valid gates MERGE into proto-89's gates, or
  - it stays KEEP as the W6 gate file.
- HUMAN_SPOTCHECK_PACKET (20 items for the boss): if it was never reviewed, it becomes an OPEN boss item in proto-92, not a silent archive.

**G5** — CONDENSE every ledger:
- its decisions go to RESEARCH_DECISIONS;
- its record count, date range and URL-less count go on one line in the bundle index.

No ledger stays live unless a protocol cites a specific record.

**G6**
- The 34 "converted from .jsonl" md files → DELETE-CONVERSION. Their .jsonl sources go into the bundle.
- ELITE_REPO_REFRESH: tooling decisions → RESEARCH_DECISIONS + `INTEGRATED-ELITE-STACK.md` / [[proto-94-tool-integration]].
- `laya_detailed` / `laya_gates` → REJECTED rows citing [[proto-31-w3-laya-jev-verdict]] (Laya NOT used).

**G7**
- PPT_FULL_DUMP: a primary-source text dump → moves to `docs/sources/proposal/` in proto-98 Phase 1 (not a research file).
- PPT_VS_SPEC_DIFF → MERGE into proto-75's output.
- The other three: rule on each.

**G8**
- KEEP (confirm they are live and cited): BENCHMARK_22, COMPETITOR_INTEL, SAMPLING_PLAN, SHEET_V2_FORENSICS.
- W1_reports and W2_reports → CONDENSE (W1.md already holds the verdicts; citations from proto-86 verification are historical).
- EDGE_THESIS, MENTOR_PLAYBOOK, MULTI_LLM_EVAL, CHATGPT_EVAL_PROMPT, DRAFT_RESEARCH_PLAN → rule each against Plan v3.
- The two MONITOR_2026-09-30.md → one canonical file.

**G9**
- QLORA_* and MLX_INSTALL_RESULT: findings still true for mlx-vlm + Bodhan (install steps, memory limits, smoke-test outcome) → ADOPTED into proto-89 §C.
- B12 ensemble voting → a Day-4 routing row with its numbers.
- File moves belong to proto-70.

**G10** — findings only.

**Fix-specs to write (Miss applies in Step 4)**

AGENTS.md:
- Replace the two dead KEY FILES pointers with `docs/research/MEETING_2026-09-29_STRUCTURED.md` and `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt`.
- Update item 8 (see G4).
- Add the standing rule above to the hard rules.
- The stale "Current state … campaign ends ~04:23 Sep 29" paragraph belongs to [[proto-84-law-hierarchy-consolidation]].


## Step 3 — Assemble and cross-check (Verdict lead)
1. Write RESEARCH_DECISIONS.md and RESEARCH_FATES.csv.
2. Every ADOPTED row has a fix-spec; every new U# is drafted for proto-92.
3. Cross-check per [[proto-91-verdict-cross-check]]: a fresh Sonnet subagent re-reads 10% of the files (≥ 1 per group) blind and re-derives fates and findings. If more than 10% disagree in a group, that group is redone.

## Step 4 — Execute (Miss)
Only U# rows wait for the boss. The boss's 2026-09-30 order approves merge / condense / archive / delete-after-decision. Skip G9 (proto-70 executes after U10) and G10 (proto-74 executes).

1. **Apply ADOPTED fix-specs** ([[proto-18-w1g-apply-verify]] method). **Protocol files are edited ONLY in the memory directory** `~/.claude/projects/-Users-srujansai-Desktop-South/memory/`. The repo mirror `docs/campaign/protocols/` is overwritten from memory by `scripts/agent_bootstrap.sh`, so an edit made only in the mirror is lost at the next sync.
2. **MERGE:** paste the live content into the target under a dated line `Merged from <path> (sha256 <first 16>) on <date>`. Keep numbers verbatim, with their source.
3. **Harvest bundle:**
   - Build it: `tar -czf _archive/bundles/2026-09-30_research_harvest.tar.gz --null -T <NUL-separated list of MERGE+CONDENSE+ARCHIVE files>` (names contain spaces).
   - Verify it: extract into the session scratch dir and compare every sha256 with RESEARCH_FATES.csv. Stop on any mismatch.
   - Only then remove the originals: `git rm` if tracked, `rm` if untracked. Never `rm -rf` a folder.
4. **DELETE-DUP / DELETE-CONVERSION:** re-check the sha256, or that the source is present, immediately before each removal.
5. **Referrers:** update every live referrer of a removed path (from Step 1) to its new home or to `<bundle>:<path>`.
   - Append-only logs stay as they are (historical).
   - No pointer stubs, except where a locked file cites the path.
6. **Index:** add one line per removed or bundled file to `_archive/INDEX.md` (format in [[proto-96-archive-reports-compaction]]).
7. **Log:** add a `DISPATCH_LOG.md` entry and set W4.md `STATUS: proto-95 APPLIED — awaiting Verdict`.

## Step 5 — Verify (Verdict)
- (a) `find docs/research -name '*.md' | wc -l` ≤ 15, and each survivor is cited by a live protocol, plan step or decision (paste the grep).
- (b) Bundle integrity: extract and compare sha256 against the CSV = 100%.
- (c) No live file references a removed path (the [[proto-50-w5-repo-map-and-drift]] link checker).
- (d) Every RESEARCH_DECISIONS row has a destination, and each ADOPTED fix-spec's new string is present in its target (grep).
- (e) `git status` and mtimes show nothing touched in sealed dirs or locked files.
- (f) Every AGENTS.md path resolves.

Two fix rounds at most, then the lead decides.

**Done when:**
- W4.md shows `proto-95 VERIFIED` with the commands above, and
- the boss has 5 lines: files before → after, verdict counts, the top 3 changes to the plan, and the new U# rows.

**Skills:**
- `graphify` — update; use communities for topic clusters.
- `ssotize` — merge plans.
- ECC `living-docs-governance` — md fates.
- `factchk` — every ADOPTED/REJECTED claim about the outside world.
- `mandela` — every evaluation claim, e.g. "beat Sarvam".
- `superpowers:verification-before-completion` / ECC `verification-loop` — before "done".

OpenCode equivalents: [[proto-88-skill-routing]].

**Parallel with:** Engine's Plan v3 Day 1 (different files).
**Must finish before:** [[proto-72-per-file-audit]] judges these files (proto-72 imports RESEARCH_FATES.csv rows and does not re-judge them), and [[proto-96-archive-reports-compaction]].

Related: [[proto-97-research-still-to-do]], [[proto-96-archive-reports-compaction]], [[proto-40-w4-research-corpus]], [[proto-63-single-canonical-files]], [[proto-73-md-fact-consolidation]]
