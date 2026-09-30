---
name: proto-98-clean-repo-master
description: "PARKED until the boss says 'resume cleanup' or proto-104 Day 5 passes — ONE cleanup master merging proto-50/63/70/72/73/74/77/84/95/96/98/101: official target tree, WORTH score and 14 topic finals (98), research harvest (95), archive + reports compaction (96), South unification + level2 tree (101/70), per-file audit (72), md fact consolidation (73), root/hidden hygiene (74), single canonical files (63), law hierarchy (84), graph concerns (77), link/drift proof (50); when resumed Agent 3 does a read-only inventory first and every mutating phase needs the boss's 'go' + proto-01 rules 17-21"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
---

# PROTO-98 — THE CLEANUP MASTER (PARKED): one file for every repo-cleanup protocol

> **PARKED by proto-104** (boss 2026-09-30 18:15: "complete the project first"). Resume only when the boss says "resume cleanup" or the proto-104 Day 5 gate has passed.
>
> **When resumed:** Agent 3 does the read-only inventory first. Every mutating phase (move, merge, bundle, delete) needs the boss's "go" and follows proto-01 rules 17-21: a sha manifest + a verified bundle + a log line BEFORE any delete or move; no `2>/dev/null` on `mv`, `rm`, `cp` or `tar`.
>
> **Path caveat:** the section bodies were written 2026-09-30 morning/evening with the paths of that time. The proto-101 P2 move has since happened (probe22 is now level2/benchmark), so re-grep every path constant before acting on a body. Wiki links inside the bodies point at old ids and are kept as written.
>
> **Merged 2026-09-30 ~22:00 IST** from proto-50, 63, 70, 72, 73, 74, 77, 84, 95, 96, 98 and 101 (bodies verbatim; the originals except this file are in _archive_2026-09-30/). Where an older section says a different home or method than the proto-98 section, the proto-98 section wins (it was later and boss-directed).

## Status of each merged protocol (verified against disk 2026-09-30 ~22:00 IST)

- proto-98 (itself) — official target tree, WORTH score, 14 topic finals, graphify + Laya trial, gated 6-phase order — NOT DONE — only the Phase 0 snapshot of BOSS_CONCERNS exists at _archive/proto-98_phase0_2026-09-30/
- proto-95 — research harvest: every research file to decisions to one fate — PARTIAL — docs/campaign/RESEARCH_DECISIONS.md has 20 RF rows; Phase 2 gated
- proto-96 — archive + reports compaction — NOT DONE
- proto-101 — one benchmark for all 22 languages + the final level2 tree — PARTIAL — P1 South feasibility done for real (0/23,001 official South PDF pages clean); P2 one-tree move happened via the incident + proto-102 A3 PASS; P3 draw/runs = proto-104 step S (South from Sarvam-bench fill, R-7); P4 retire South v1 = proto-104 S6; P5-P7 parked
- proto-70 — level2 restructure (inventory and path-dependency reference) — PARTIAL — probe22 → level2/benchmark done; rest superseded by 101/104
- proto-72 — per-file audit — NOT DONE — scripts/repo_inventory.py does not exist
- proto-73 — md fact consolidation — NOT DONE
- proto-74 — repo root + hidden folders hygiene — NOT DONE — root strays remain; small bits in proto-104 step R
- proto-77 — graph the concerns — NOT DONE
- proto-84 — one law hierarchy — NOT DONE — read order now set by proto-00/proto-104
- proto-63 — single canonical files — NOT DONE
- proto-50 — repo map, link proof, drift fixes — NOT DONE

## proto-98-clean-repo-master.md (its own original body) — STATUS: NOT DONE (only the Phase 0 snapshot of BOSS_CONCERNS exists at _archive/proto-98_phase0_2026-09-30/)

# PROTO-98 — CLEAN-REPO MASTER: official tree · a WORTH score for every file · one final md per topic · graphify + Laya · the gated order

**Boss, 2026-09-30 evening:**
> "check the hierarchy and the flow … are you using graphify or not — if you used that I shouldn't have seen this much junk … I need everything so clean and official and perfect … read all the relevant variants and write the final md file … merging all the variants should go to archive … I need every file's rating, ranking, its worth to stay … use Laya, it can give the decisions so fast … also use graphify and all we can."

This covers H6–H10 in [[proto-99-concern-crosswalk]] §H. It also covers the uni v3, re-pasted the same day: T1.2–T1.6, T2.1–T2.6, D02/D03/D07.

**Where proto-63, proto-73 and proto-74 propose a different home or method, this protocol wins.** It is later, and it is boss-directed.

## The junk, measured (2026-09-30 ~16:00 IST — re-measure in Phase 1)
- **graphify** (`graphify-out/graph.json`, report rebuilt 14:34): 6,796 nodes · 7,633 edges · 597 communities.
  - **367 md files are in the graph; 101 md on disk are not.** The missing ones include every doc agents wrote today: ACTUAL_PROBE22_RESULTS, W6_STRATEGY_UNIFIED, PROBE22_EDGE_ANALYSIS, SURYA_LIVE_INFERENCE_RESULTS, DEEP_RESEARCH_STRATEGY, MONITOR_2026-09-30.
- **204 md files are graph islands** (no edge to any other file): `_archive` 69 · `docs` 47 · `_reports` 44 · `level2` 31 · root 13. An island is a junk signal, not proof; Phase 2 reads every one.
- **Agent run-reports posing as documents:** report-template headings ("token spend", "summary", "counts", "verdict check", "required change", "owner", "output format") recur in 10–12 md files each.
- **At least 20 live plan documents.** The boss cannot tell which plan is real (T1 lists them).
- **A primary source is filed as junk.** The first mentor meeting, `sync - ocr - September 10.docx`, sits in `_archive/cleanup_2026-09-28/root_clutter/` (original also in `~/Downloads/`). The boss's own notes `Untitled-1.ini` (47 KB) sit beside it. The boss looks for the meeting files at the repo root; the 09-29 meeting notes are in `docs/research/`.
- **Archive and reports:** `_archive/` has 519 files and `_reports/` 58, none of them in git. The repo holds 69 exact-duplicate md/txt groups (F66). There are four map files: `docs/INDEX.md`, `level2/FOLDER_MAP.md`, `level2/UNIFIED_INDEX.md`, `level2/MODELS_VS_OUT.md`.

## Law for every phase (no exceptions)
1. **Full reads only.** A verdict needs the whole file (ledgers: record by record). A reader who read only part writes `PARTIAL-READ` in the row, and that row does not count. The planner's notes in these protocols are metadata-level; readers re-check them.
2. **Evidence in every row:** inbound refs (inventory), graph signals, the facts checked, the WORTH components. "Looks fine" is not evidence.
3. **Every live file is exactly one of:** the final for its topic · a primary source · code or data in use · sealed/locked. Everything else goes into a bundle (proto-96) or is deleted under U29.
4. **Primary sources are sacred.** Meeting documents, the proposal PPTX, the boss's notes and directives are never bundled or deleted. They live in `docs/sources/`, read-only. Text extractions beside them are verbatim, never summaries.
5. **Nothing new at the root** (C5). New files go only where this protocol names them. Status words are claims (proto-01 rule 14). Research lands as decisions (rule 16).
6. **Monitors veto.** One Verdict monitor per 3 readers re-reads a random 10% of each reader's rows in full. If more than 10% are vetoed, the reader's whole batch is redone ([[proto-72-per-file-audit]] Step 3).
7. **No execution before the verdict. No deletion outside U29** ([[proto-92-boss-decisions]]). Every executed action is one line in `CLEANUP_EXECUTION_LOG.md` (D03): action · path · target · reason · WORTH · sha256.
8. **Sonnet subagents only, never Opus.** 10–15 readers + 4–5 monitors may run in parallel (uni T1.2). Each registers in `DISPATCH_LOG.md` first (proto-01 rule 15).

## The official target tree (what the boss sees when this is done)
```
South/
├── README.md                 entry page ≤ 40 lines: what this is · read order · how to run (absorbs HOW_TO_RUN.txt)
├── AGENTS.md                 agent law pointer (START HERE)
├── BOSS_CONCERNS.md          D01 concern register (Miss)             ┐
├── AUDIT_REPORT.md           D02 per-file audit + WORTH ranking      │ the uni's root deliverables —
├── CLEANUP_EXECUTION_LOG.md  D03 every executed merge/move/delete    │ C5: they stay at the root
├── PROTOCOL_UPGRADES.md      D05                                     │
├── DISPATCH_LOG.md           D06 who does what                       ┘
├── requirements.txt · .gitignore · .env (U12)
├── docs/
│   ├── INDEX.md              THE map — D07 delivered here (one map, not two: C13)
│   ├── PLAN.md               THE plan (T1) — human-readable; commands stay in memory proto-89
│   ├── BRIEFING.md           THE state briefing (T2) — was "FULL TECHNICAL BRIEFING.md" at the root
│   ├── campaign/             CAMPAIGN_DIRECTIVE.md (law) · RESEARCH_DECISIONS.md · BENCHMARK_22.md · SAMPLING_PLAN.md (D04) · COMPETITOR_INTEL.md (D11)
│   │                         EDGE_THESIS.md (D12) · MENTOR_PLAYBOOK.md (D13) · SKILL_STACK.md (D10) · audit/ · checkpoints/ · protocols/ (mirror of memory)
│   ├── architecture/         PPT_SPEC.md · ARCHITECTURE_FREEZE.md (D09 — only at the call)
│   ├── research/             ≤ 15 KEEP files, each cited by a live protocol (proto-95)
│   ├── sources/              PRIMARY, read-only:
│   │   ├── meetings/         2026-09-10_sync_ocr.docx + .md (verbatim text) · 2026-09-29_meeting_structured.md
│   │   ├── proposal/         AksharDrishti_Hackathon_Proposal.pptx + PPT_FULL_DUMP.md
│   │   └── boss/             Untitled-1.ini (the boss's notes)
│   ├── legal/ · probe/ · south/
├── level2/                   the proto-70 target tree (after U10) — one South + probe hierarchy
├── scripts/ · configs/ · src/ (U3) · tests/
├── _archive/                 INDEX.md · directives/ (uni .txt + v4 directive) · bundles/ (proto-96)
├── Datasets/ · arc_level_1/ · test/        sealed data
└── graphify-out/ · .deps/ · .claude/       generated / dependencies
```
**Leaves the root** (each goes to its topic final, `docs/sources/`, `scripts/`, or a bundle):
- `PROJECT_COMPLETE.md`, `W5_FREEZE_PLAN.md`, `LOOP_SPEC_W5_W6_W7.md`, `W5_W6_W7_LOOP.yaml`
- `SAMPLE_PLAN_18_LANGS.md`, `LIVE_LATEST_2026-09-29.md`, `PAPERTHIN_AUDIT.md`, `INTEGRATED-ELITE-STACK.md`, `VINAY_MEETING_PACKET.md`
- `FULL TECHNICAL BRIEFING.md` → `docs/BRIEFING.md`
- `HOW_TO_RUN.txt` → `README.md`
- `sarvam_smoke.py` → `scripts/`, with the header "do not run — cap spent"
- the PPTX → `docs/sources/proposal/`
- `OCR_AGENT_MEMORY_FEED.md` + `SOUTH_CANON.md` (tracked law docs) → follow the [[proto-84-law-hierarchy-consolidation]] ruling

`_reports/` disappears. The four map files become `docs/INDEX.md` alone.

## WORTH score — every file gets one (the boss's "rating, ranking, worth to stay")
| Component | Points | Measured by |
|---|---|---|
| **C** cited by live files | 0 / 10 / 20 / 30 for 0 / 1 / 2–4 / ≥ 5 live inbound refs. Always 30 if `AGENTS.md`, `CAMPAIGN_DIRECTIVE.md`, a protocol step or a pipeline script cites or imports it | inventory script |
| **D** decision value | 25 = holds a fact, number or finding that a live decision depends on and that exists nowhere else · 10 = decision-relevant, but also elsewhere · 0 = none | full read (Verdict reader) |
| **U** uniqueness | 15 = unique · 5 = a variant of its topic final · 0 = sha twin or format copy | script + read |
| **F** currency | 10 = current · 5 = dated but still true · 0 = superseded | read |
| **T** truth | 10 = clean · 5 = minor errors · 0 = contradicts proto-93 facts, or carries a false status word or misleading name | read + `factchk` |
| **G** graph | 10 = hub (top 10% cross-file degree) · 6 = connected · 2 = island · 0 = not in graph after the Phase 1 rebuild | `graph_signals.tsv` |

**WORTH = C + D + U + F + T + G (0–100).** Default fate by band:

| WORTH | Default fate |
|---|---|
| ≥ 70 | KEEP (or it becomes the topic final) |
| 45–69 | MERGE into its topic final, then bundle |
| 20–44 | ARCHIVE (bundle) |
| < 20 | ARCHIVE, or DELETE-DUP / DELETE-CONV if it is a twin or copy (U29) |

- A reader may override the band only with a written reason; monitors check every override.
- **Exempt from bands (always kept in place):** primary sources, sealed dirs, locked files, datasets, code imported by a live pipeline.
- **Ranking output:** `docs/campaign/audit/FILE_WORTH_RANKING.csv` holds every file with all six components, sorted by WORTH.
- `AUDIT_REPORT.md` shows, per directory, the top 10 and bottom 10, plus the **WASTE list**: lowest WORTH × largest bytes (uni T1.5).

## The 14 topic finals — read ALL variants in full, write ONE final, bundle the variants
Every final file carries this header:
- title · owner · `Last verified: <date> by <command>` · measured status
- `Supersedes:` the variant paths, and the bundle they went to
- a Sources section at the end

| T | Topic | Variants today (read every one in full) | ONE final |
|---|---|---|---|
| T1 | **The plan** | memory proto-87 (Plan v2) and proto-89 (Plan v3) · the shared Claude Doc · `docs/PLAN.md` (09-26 "Next work") · `docs/architecture/{W2_HYBRID, W5_BEAT_SARVAM_PLAN, W5_STRATEGY_OPTIONS}` · `docs/campaign/DRAFT_RESEARCH_PLAN` · `docs/research/{W6_STRATEGY_UNIFIED, DEEP_RESEARCH_STRATEGY_2026-09-29, R7_W6_TRAINING_TREE}` · `level7/{W6_QLORA_SPEC, KILL_CRITERIA, W5_FREEZE_AGENDA}` · root `W5_FREEZE_PLAN`, `LOOP_SPEC_W5_W6_W7`, `W5_W6_W7_LOOP.yaml`, `VINAY_MEETING_PACKET` (plan parts), `PROJECT_COMPLETE` · `level2/probe22/QLORA_{EVAL_SPEC, READINESS, SMOKE_TEST, TRAINING_DATA}` | `docs/PLAN.md` — Plan v3: the honest position, market table, steps + gates, the U-decisions that shape it, schedule, what we don't do. ≤ 250 lines, tables. Commands stay in proto-89 (PLAN.md links to them and does not restate them). The Claude Doc is re-exported from PLAN.md (Miss). |
| T2 | **Where we stand** | `FULL TECHNICAL BRIEFING.md` · `PROJECT_COMPLETE.md` · `README.md` · `SOUTH_CANON.md` · `OCR_AGENT_MEMORY_FEED.md` §10 · CAMPAIGN_DIRECTIVE Part A · `checkpoints/W1.md` status · memory campaign-state | `docs/BRIEFING.md`; `README.md` is the entry and points to it |
| T3 | **Law** | `AGENTS.md` · `CAMPAIGN_DIRECTIVE.md` · `OCR_AGENT_MEMORY_FEED.md` §9 · `SOUTH_CANON.md` §P · `LEVEL7_RESEARCH_CAMPAIGN.md` · `level2/ULTIMATE_HYBRID_CONCERN.md` · `PROTOCOL_UPGRADES.md` · `level7/PROMPT_*_AGENT.md` · `level2/probe22/AGENT_PROTOCOL.md` (locked) | as ruled by [[proto-84-law-hierarchy-consolidation]]: `CAMPAIGN_DIRECTIVE.md` + `AGENTS.md` + memory proto-01 |
| T4 | **Results / numbers** | `BENCHMARK_22` · `level2/probe22/{scores/LEADERBOARD, LEADERBOARD_REFRESH_2026-09-29, FINAL_REPORT}` · `docs/research/{ACTUAL_PROBE22_RESULTS, PROBE22_EDGE_ANALYSIS, SURYA_LIVE_INFERENCE_RESULTS}` · `SHEET_V2_FORENSICS` · sealed `level2/reports/{LEADERBOARD, CER_BY_SCRIPT}` | `docs/campaign/BENCHMARK_22.md` (every probe + South number, per GT tier, proto-62). The sealed South files stay as the sealed record it cites. |
| T5 | **Sampling** | `SAMPLING_PLAN` · root `SAMPLE_PLAN_18_LANGS` · `W2_reports/variance` · `level2/probe22/{w6_feasible_set, w6_set_construction_log}` | `docs/campaign/SAMPLING_PLAN.md` (D04) |
| T6 | **Competitors / market** | `COMPETITOR_INTEL` · `R6_COMPETITION_INTEL` · `R1_SOTA_MECHANISM_TEARDOWN` · `level7/c/c2/LEDGER` · `LIVE_LATEST_2026-09-29` · `DEEPER_LIVE_RESEARCH_2026-09-29` · `docs/south/EXTERNAL_BENCHMARK_MAP` | `docs/campaign/COMPETITOR_INTEL.md` (D11) |
| T7 | **The edge** | `EDGE_THESIS` · `PROBE22_EDGE_ANALYSIS` · `W1_reports/1E_*` | `docs/campaign/EDGE_THESIS.md` (D12), rewritten on Plan v3 (Bodhan base) with GT-tier-true claims only |
| T8 | **Mentor / Vinay** | `MENTOR_PLAYBOOK` · `PPT_SPEC` · `PPT_FULL_DUMP` · `PPT_VS_SPEC_DIFF` · `VINAY_MEETING_PACKET` · `level7/CALL_PACKET` · `boss_directives/VALIDATION_CALL_*` · the sources in `docs/sources/` | `docs/campaign/MENTOR_PLAYBOOK.md` (D13: what the mentor taught + how the plan implements each point); meeting sources stay in `docs/sources/` |
| T9 | **Tools / skills** | `INTEGRATED-ELITE-STACK` · memory proto-88/94 · `level7/b/b4`, `b5` + `ELITE_REPO_REFRESH` · `level7/c/c4/{LEDGER, OBITUARIES}` | `docs/campaign/SKILL_STACK.md` (D10; the W3 proto-30/31 outputs go here) |
| T10 | **Concerns** | `BOSS_CONCERNS` · CAMPAIGN_DIRECTIVE Part G · the uni .txt (source) · `boss_directives/SESSION_DIRECTIVES_2026-09-28` · memory proto-99 | `BOSS_CONCERNS.md` (D01), a verbatim register with status ([[proto-66-concern-register-rebuild]]) |
| T11 | **Map / hierarchy** | `docs/INDEX.md` · `level2/{FOLDER_MAP, UNIFIED_INDEX, MODELS_VS_OUT}` · `README` read-order | `docs/INDEX.md`: every directory's purpose + the Phase 5 linkage check (D07). Level2 map files merge in after proto-70. |
| T12 | **Audit / cleanup records** | `AUDIT_REPORT` · `CLEANUP_EXECUTION_LOG` · `_reports/cleanup_cycle1–3` · `_reports/analysis/*` · `DEDUP_DOCS_RESEARCH` · `_archive/.audit_2026-09-29/*` | `AUDIT_REPORT.md` (D02, rebuilt with the WORTH ranking) + `CLEANUP_EXECUTION_LOG.md` (D03) + the CSVs in `docs/campaign/audit/` |
| T13 | **Status / monitoring** | `DISPATCH_LOG` · `checkpoints/*` · `MONITOR_2026-09-30` ×2 · `level7/{MISS_MONITOR, H48_*}` | `DISPATCH_LOG.md` (D06) + `checkpoints/W*.md` + `NEXT.md`; one MONITOR file, in `checkpoints/` |
| T14 | **Research findings** | everything in proto-95 G1–G10 | `docs/campaign/RESEARCH_DECISIONS.md` ([[proto-95-research-harvest-decisions]]) |

**Writer method** (one Sonnet writer per topic, ≤ 5 topics at once):
1. Read every variant in full.
2. Build a fact table: fact · value · variant:line · truth-check (proto-93, BENCHMARK_22, proto-92).
3. Write the final.
4. List every variant's fate.

**Verdict checks each final:**
- (a) every decision-relevant fact from the variants is in the final, or rejected in RESEARCH_DECISIONS with its reason;
- (b) the [[proto-73-md-fact-consolidation]] scan shows 0 live conflicts on the topic;
- (c) every referrer points at the final.

## graphify — used, not just installed (boss: "are you using graphify or not")
1. **Phase 1:** run the `/graphify` skill with `--update` on the repo (`~/.claude/skills/graphify/SKILL.md`) — run by a Sonnet agent, never Opus, because the skill may spawn subagents.
2. Then `scripts/graph_signals.py` (Miss, stdlib only) writes `docs/campaign/audit/graph_signals.tsv`. Per file: `in_graph`, node count, cross-file degree, island flag, community id + name, report-template hits (the headings above).
3. **Topic clusters:** a graph community that spans ≥ 3 live md files is a variant cluster. It must map to one T-topic; a cluster with no T-topic is added as T15+ by Verdict.
4. **Phase 5:** run `--update` again and report before → after: islands among live md, live md not in the graph, communities with ≥ 3 live md files. Targets: islands 0 (primary sources excepted), not-in-graph 0.

## Laya triage trial — U31 (boss: "use Laya, it can give the decisions so fast")
Run it, measure it, and trust it only as far as the numbers go. Laya is **never** used in the OCR model (proto-31, U30).
- **Environment** — reuse the working `~/Desktop/swa-erp/.venv-laya/bin/python` (torch 2.14.0, transformers 5.17.0, laya 0.3.5, MPS), read-only. No package install, and never modify swa-erp. If the checkpoint is not cached, the first load downloads it; log the size in `DISPATCH_LOG.md` before pulling (covered by U31).
- **Input** — one "state card" per file (≤ 1,500 chars): `path | title | bytes | mtime | live inbound refs | sha twin Y/N | in_graph | island | template hits | first 1,000 chars`.
- **Questions:**
  - `fate`: choice of keep / merge / archive / delete_duplicate, each with a one-line criterion from the fate table.
  - `worth`: score over worthless / low / medium / high / essential.
  - Use the typed-decisions checkpoint (`laya/router.py` DEFAULT_MODELS key `typed-decisions`). Confirm the constructor and `predict` signature with `help(laya.Router)` first; the API in 0.3.5 may differ from the 0.3.22 README.
- **Run** on every file in the inventory; record decision, confidence and ms per file.
- **Measure** against the full-read fates from Phase 2, once ≥ 150 files are fated: accuracy, per-class precision/recall, confusion matrix, and precision at confidence ≥ 0.9, with n.
- **Bar** — accuracy ≥ 0.80 AND precision ≥ 0.95 at confidence ≥ 0.9.
  - **Pass:** Laya becomes the first-pass triage for **new** files: a daily hygiene gate that flags new md for a full read.
  - **Fail:** REJECTED, with the numbers written into proto-31 and U31.
  - **Either way:** Laya never decides alone, never deletes, and never overrides a full read. The laya-gate skill forbids irreversible deletes; Laya's README says the base checkpoints are near-chance zero-shot; swa-erp's own labelled eval is 0.75 on n = 12.
- **Owners:** Engine runs it; Verdict scores it.

## The gated order
| Phase | Who | What | Gate to leave the phase |
|---|---|---|---|
| **0 Freeze** (15 min) | Miss | Every running agent registers in DISPATCH_LOG; no new md outside lanes (rule 16). One global snapshot: `tar -czf _archive/bundles/2026-09-30_pre_cleanup_snapshot.tar.gz` of all md/txt/yaml/json/py/sh/ini/docx/pptx outside `.git`, `.venv*`, sealed dirs, `Datasets/`, `test/`, `.deps/`, `graphify-out/cache` (this replaces proto-95's Step 0 snapshot); sha256 logged | snapshot sha256 logged; writers listed |
| **1 Map** (~1 h) | Miss (+ Engine for Laya) | graphify `--update` → `graph_signals.tsv`; inventories (proto-72 `INVENTORY.csv` for all files, proto-95 `research_inventory.tsv`, proto-96 `archive_inventory.tsv`). **Primary sources to `docs/sources/` first**, so no later step bundles them — see the list below. Laya state cards built | inventories reconcile with `find`; sources moved, sha-verified, referrers updated |
| **2 Read + rate** (the long phase, up to the 24 h the boss authorised) | Verdict leads 10–15 Sonnet readers + 4–5 monitors | proto-95 (research files) ∥ proto-72 (all other files). Each row: WHAT/WHY/WHERE/WHO + WORTH components + fate + T-topic + findings. The Laya trial is scored once ≥ 150 fates exist | every in-scope file has a counted (full-read) row; monitor veto rate ≤ 10% |
| **3 Topic finals** | Miss writers, Verdict checks | T1–T14 finals per the table; proto-73 scan → 0 live conflicts | each final passes checks (a)–(c) |
| **4 Execute** | Miss | Moves and merges per fates: proto-74 (root → tree) · proto-63 (twins) · proto-95 Step 4 (research bundle) · topic variants → bundle · proto-96 (archive + reports bundles) · proto-70 (level2) **only after U10**. One `CLEANUP_EXECUTION_LOG.md` line per action | before-count = kept + moved + bundled + deleted, exactly |
| **5 Verify + map** | Verdict | Link check ([[proto-50-w5-repo-map-and-drift]]); graphify `--update`; `docs/INDEX.md` final map (D07); `AUDIT_REPORT.md` rebuilt with the ranking + WASTE list; boss report ≤ 10 lines | the before → after table below, all measured |

**Phase 1 primary-source moves.** Each move gets sha256 before and after, and one CLEANUP_EXECUTION_LOG line.
- `_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx` → `docs/sources/meetings/2026-09-10_sync_ocr.docx`.
  - Also write `2026-09-10_sync_ocr.md` beside it: the verbatim text from `textutil -convert txt -stdout <docx>`, under a 3-line header giving source path, sha256 and command.
  - Compare the file with `~/Downloads/sync - ocr - September 10.docx` and report any difference.
- `…/root_clutter/Untitled-1.ini` → `docs/sources/boss/Untitled-1.ini`.
  - Diff it against `FULL TECHNICAL BRIEFING.md` Part III, where CO-069 says it was merged; list anything missing as new BOSS_CONCERNS rows.
- Root `AksharDrishti_Hackathon_Proposal.pptx` and `_reports/research/PPT_FULL_DUMP.md` → `docs/sources/proposal/`.
- `docs/research/MEETING_2026-09-29_STRUCTURED.md` → `docs/sources/meetings/2026-09-29_meeting_structured.md`.
- `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` stays where it is (AGENTS.md and v5 cite it; the boss opens it there).
- Update every referrer: AGENTS.md KEY FILES, proto-13, MENTOR_PLAYBOOK, CAMPAIGN_DIRECTIVE line ~247, PPT_SPEC.

**Before → after (the boss's scoreboard; Phase 5 fills the "after" column with measured values)**
| Metric | Before (measured 2026-09-30) | Target |
|---|---|---|
| live plan documents | ≥ 20 | 1 (`docs/PLAN.md`) + proto-89 commands |
| map/index files | 4 | 1 (`docs/INDEX.md`) |
| `docs/research` md | 86 | ≤ 15 |
| root md | 18 | 7 (README, AGENTS + the 5 uni deliverables) |
| `_reports/` files | 58 | 0 |
| `_archive/` loose files | 519 | `INDEX.md` + ≤ 7 bundles + 2 directives |
| exact-duplicate md/txt groups | 69 | 0 |
| graph islands among live md | 204 (incl. archive) | 0, primary sources excepted |
| live md not in the graph | 101 | 0 |

**Skills per phase:**
- `graphify` — Phase 1 and Phase 5
- ECC `terminal-ops` — tar and sha work
- `ssotize` + ECC `living-docs-governance` — topic finals
- `factchk` — T components
- `mandela` — any evaluation claim
- `superpowers:verification-before-completion` / ECC `verification-loop` — before any "done"
- OpenCode equivalents: [[proto-88-skill-routing]]

**One-line assignments** (R0.9: the detail lives here):
- **Engine:** "Read docs/campaign/protocols/proto-98-clean-repo-master.md — run the Laya trial; keep Plan v3 Day 1 going (NEXT.md)."
- **Verdict:** "Read docs/campaign/protocols/proto-98-clean-repo-master.md — lead Phases 2, 3 and 5."
- **Miss:** "Read docs/campaign/protocols/proto-98-clean-repo-master.md — do Phases 0, 1 and 4, then proto-96."

Related: [[proto-95-research-harvest-decisions]], [[proto-96-archive-reports-compaction]], [[proto-97-research-still-to-do]], [[proto-72-per-file-audit]], [[proto-73-md-fact-consolidation]], [[proto-63-single-canonical-files]], [[proto-74-root-hidden-hygiene]], [[proto-70-level2-restructure]], [[proto-84-law-hierarchy-consolidation]], [[proto-31-w3-laya-jev-verdict]], [[proto-92-boss-decisions]]


## proto-95-research-harvest-decisions.md — STATUS: PARTIAL (docs/campaign/RESEARCH_DECISIONS.md has 20 RF rows; Phase 2 gated)

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


## proto-96-archive-reports-compaction.md — STATUS: NOT DONE

# PROTO-96 — ARCHIVE + REPORTS COMPACTION (W4 part 2; starts only after [[proto-95-research-harvest-decisions]] is VERIFIED)

**Boss, 2026-09-30:** "after all these I need those archive and reports also to compact, merge them and make some low variants … I am seeing bunch of junk."
Concerns: HC14.9 (archive INDEX, one line per item), HL4 (archive-never-delete; narrowed by U29), CO-002, CO-066, H3 ([[proto-99-concern-crosswalk]] §H).
**The "low variant":** each bundle gets a digest of 5 lines or fewer in `_archive/INDEX.md`, so nobody has to open a bundle to learn what is inside.

## Measured 2026-09-30 ~15:30 IST (re-count in Step 1)
- `_archive/` holds 519 files and `_reports/` holds 58. **0 of them are tracked in git.**
  - So a delete here is permanent. Only a file with an exact twin somewhere else may be deleted.
- Repo-wide there are 69 exact-duplicate md/txt groups (71 redundant copies). Almost all are `_archive/` copies of live files.

| Folder | Files · size | What it is | Fate rule → bundle |
|---|---|---|---|
| `_archive/campaign_drafts_2026-09-30` | 73 · 0.9 MB | protocol copies + W1 papers. **61 are sha-identical to a live file**; 12 have no live twin | DELETE-DUP the 61; the 12 → `2026-09-30_prefix_and_drafts` |
| `_archive/cleanup_2026-09-28` | 335 · ~215 MB | `AUDIT_*.md`, `audit_intermediates/*.txt`, and 45 probe JSONs (194 MB) in `probe22_dups/` + `audit_safety_backup/`. Of those 45: 9 identical to the same-named live file, 20 differ, 16 have no same-named live file | match by sha256 across the whole repo, not by name: twins → DELETE-DUP; the rest → `2026-09-28_cleanup` (JSON compresses well) |
| `_archive/.audit_2026-09-29` (hidden) | 18 · 0.6 MB | subagent audit reports, `sizes_all.txt` | → `2026-09-29_audit` |
| `_archive/cleanup_2026-09-29` | 13 · 68 KB | dead code (`level2_dead_code/*.py`, `src_skeletons/`) | exact blob in git history → DELETE-GIT; else → `2026-09-29_audit` |
| `_archive/root_md_dedupe_2026-09-29` | 1 · 16 KB | `W5_BEAT_SARVAM_PLAN.md` | twin → DELETE-DUP; else → `2026-09-29_audit` |
| `_archive/cleanup_2026-09-30` | 50 · 0.3 MB | `renames/`, `single_file_dups/` (incl. a uni md copy), `dedup_topic_superseded/` | twins → DELETE-DUP; rest → `2026-09-30_prefix_and_drafts` |
| `_archive/pre_fix_2026-09-30` + `_consolidated` | 6 + 21 · 0.5 MB | pre-images of the proto-18/86 fixes (W1 VERIFIED) | → `2026-09-30_prefix_and_drafts` (audit trail) |
| `_archive/directives` | 2 · 80 KB | uni v3 original (.txt) + CAMPAIGN_DIRECTIVE v4 | **KEEP as plain files.** AGENTS.md and the v5 directive cite them, and the boss opens the uni |
| `_reports/cleanup_cycle1/2/3` (+ empty `cycle4/`) | 48 · 0.7 MB | reports about earlier cleanups | → `2026-09-30_cleanup_reports`; delete the empty dir |
| `_reports/analysis` | 5 · 84 KB | DUPLICATE_MAP, FILE_INVENTORY, MEMORY_CONSOLIDATION, MD_CONSOLIDATION_PLAN, MEMORY_FINAL | → `2026-09-30_cleanup_reports` (proto-95 already took their decisions) |
| `_reports/research` | 5 · 116 KB | proto-95 G7 | as proto-95 ruled |
| `docs/campaign/checkpoints/W1_reports`, `W2_reports` | 11 · ~0.3 MB | proto-95 G8 | as proto-95 ruled |

**Out of scope:**
- `.kilo/worktrees` (56 md; another tool's git worktree). [[proto-74-root-hidden-hygiene]] / [[proto-76-workstreams-and-agent-health]] decide: `git worktree list`, remove if stale.
- Sealed `level2/reports`, `level2/out` and `level2/probe22/out`; also `Datasets/` and `arc_level_1/`.
- The Gemma HF cache (the boss keeps it).
- **Primary sources:** `_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx` and `Untitled-1.ini` are NOT archive material. [[proto-98-clean-repo-master]] Phase 1 moves them to `docs/sources/` before any bundling; if they are still here, STOP and move them first.

## Target end state
```
_archive/
  INDEX.md      one line per original + a digest (≤5 lines) per bundle
  directives/   unchanged (2 files)
  bundles/      ≤ 7 × .tar.gz:
                  2026-09-30_pre_cleanup_snapshot  (proto-98 Phase 0 global pre-image)
                  2026-09-28_cleanup
                  2026-09-29_audit
                  2026-09-30_prefix_and_drafts
                  2026-09-30_cleanup_reports   (all of _reports)
                  2026-09-30_research_harvest  (from proto-95)
                  2026-09-30_research_pre_harvest
                    (proto-95 snapshot; drop it only if Verdict shows the harvest bundle + git hold every file it covers)
_reports/       gone
```
- Nothing new at the repo root.
- No new report files except `_archive/INDEX.md` and one `DISPATCH_LOG.md` entry. Writing reports about each cleanup is how the junk grew.
- INDEX line format:
  `| bundle or DELETED-DUP/-CONV/-GIT/-EMPTY | original path | sha256[:16] | bytes | fate | why (≤12 words) | live successor or — |`

## Deletion rule (U29, decided by the boss 2026-09-30)
Delete only these four kinds of file:
1. sha256-identical twins of a file that stays.
2. Pure format conversions whose source stays.
3. Files whose exact blob is in git history. Check it: `git hash-object <file>` must equal the blob at the original path in some commit (`git rev-list --all -- <path>`, then `git ls-tree <commit> <path>`).
4. Empty files and empty dirs.
5. OS metadata junk (`.DS_Store`); also add it to `.gitignore`.

Everything else goes into a bundle. Nothing is deleted without an INDEX line.

## Steps
0. **Pre-flight.**
   - proto-95 must be VERIFIED; its fates decide `_reports/research` and the W1/W2 papers.
   - Run the [[proto-02-preflight-and-checkpoints]] checks. No agent may be writing under `_archive/` or `_reports/`.
   - Check free disk: bundling ~215 MB needs ~300 MB of temp space.
   - Set W4.md `STATUS: proto-96 STARTED`.
1. **Inventory** (Miss). Reuse `scripts/research_inventory.py` with `--root _archive --root _reports`, or write a sibling script.
   - For each file record: path, bytes, sha256.
   - `live_twin`: a path outside `_archive/` and `_reports/` with the same sha256, searched repo-wide. Compare the probe JSONs against `level2/` read-only.
   - `git_twin`: yes/no per rule 3.
   - Output: `docs/campaign/audit/archive_inventory.tsv`. Totals must equal `find _archive _reports -type f | wc -l`.
2. **Fates** (Verdict).
   - Apply the deletion rule mechanically; assign every other file to a bundle by the table.
   - grep all live md/py/yaml for references into `_archive/` and `_reports/`. A referenced file stays citable: update the referrer to `<bundle>:<path>`. If the file is actually live (a report a protocol still uses), move it to its live home under `docs/`.
   - Write the fate column into the TSV.
3. **Build bundles** (Miss). For each bundle:
   - Run `tar -czf _archive/bundles/<name>.tar.gz --null -T <list>`.
   - `tar -tzf <bundle> | wc -l` must equal the length of the list.
   - Extract it into the session scratch dir. Every sha256 must match the TSV (100%); otherwise stop and report.
4. **Remove** (Miss). Never `rm -rf` anything until step 3 has passed for its bundle.
   - First the DELETE rows. Re-check the twin or git match immediately before each `rm`.
   - Then the bundled originals.
   - Then run `find _archive _reports -type d -empty -delete`.
5. **Write `_archive/INDEX.md`.** Every line, plus for each bundle: "Holds / Why kept / Still cited by / Digest (≤ 5 lines)".
   - The `DISPATCH_LOG.md` entry records files before → after, MB before → after, and the bundle list with sha256.
6. **Verify** (Verdict). Check that:
   - before-count = deleted + bundled + kept, exactly;
   - every INDEX line resolves (`tar -tzf` finds it, or it is DELETED and its twin is present);
   - no live reference points at a removed path;
   - `_reports/` is gone;
   - `git status` shows nothing changed in sealed dirs.
   - Then give the boss 3 lines: files, MB and bundles, before → after.

**Done when:** W4.md says `proto-96 VERIFIED`, with the commands above.

**Skills:** ECC `terminal-ops` (tar and sha work) · `verification-loop` · `ssotize` (the few live-home moves) · `graphify --update` afterwards (`_archive` leaves the graph).

**Traps:**
- macOS `tar` is bsdtar. Use `--null -T`, because names contain spaces (`FULL TECHNICAL BRIEFING.md`, `OCR_AGENT_MEMORY_FEED copy.md`).
- On the Mac the checksum command is `shasum -a 256`, not `sha256sum`.
- Bundles stay untracked, like today's `_archive/`. Committing them to git is the boss's call; ask only if they want a copy off the laptop.

Related: [[proto-95-research-harvest-decisions]], [[proto-72-per-file-audit]], [[proto-74-root-hidden-hygiene]], [[proto-63-single-canonical-files]], [[proto-92-boss-decisions]]


## proto-101-south-unification-and-level2-tree.md — STATUS: PARTIAL: P1 South feasibility done for real (0/23,001 official South PDF pages clean); P2 one-tree move happened via the incident + proto-102 A3 PASS; P3 draw/runs = proto-104 step S (South from Sarvam-bench fill, R-7); P4 retire South v1 = proto-104 S6; P5-P7 parked

# PROTO-101 — ONE BENCHMARK FOR ALL 22 LANGUAGES + THE FINAL LEVEL2 TREE (execute now, owner per phase)

**Boss, 2026-09-30 evening:** "why am I seeing South out [in a] separate place and other languages in other folders? If they are separate, delete them and do newly for those South and merge or store them relevantly along with other languages. Why are you keeping them separate? This is just a simple concern." Earlier the same concern appeared as CO-001, CO-003, CO-004, CO-025, CO-068, M8, H10 and H13 ([[proto-99-concern-crosswalk]]).

**Why this file exists:**
- [[proto-70-level2-restructure]] (the tree) and [[proto-71-south-rerun-same-standard]] (South under the probe standard) were written this morning with good inventories. **No session was ever assigned them.**
- This file merges them into one ordered execution with an owner per phase and removes the "after the meeting" hedge. U10 and U11 are now DECIDED-NOW, by the boss's order above.
- proto-70/71 stay as the reference for the dependency lists and details; this file decides the order, the owners and the end state.

## Measured state (planner, 2026-09-30 ~17:00 IST, disk + graphify)
| What | Where | Size | Fact |
|---|---|---|---|
| South v1 packs | `level2/out/<engine>/{kn,ml,ta,te}/*.json` | 4,000 files, git-tracked, newest 09-14 | 10 engines × 400 pages; made by `level2/orchestrator.py` + `run_engine.py` + `level2/engines/`; GT = PDF text layer of Level-1 sources (`arc_level_1/`), ~45% legacy-font mojibake → only **126/400** pages carry a CER |
| **Duplicate** South packs | `level2/models/<engine>/json/*.json` | **4,000 real files** | byte-identical copies of `level2/out` (sample `te_029` IDENTICAL; the old "KEEP BOTH" #71 kept duplicates) |
| South views | `level2/models/<engine>/png` (4,000 links), `level2/pages_400` (400 links), `level2/unified` (17,289 links) | 21,689 symlinks | views, zero data |
| South pages | `level2/renders_shared/*.png` | 400 PNG, 570 MB | 200-dpi renders |
| South scores | `level2/reports/` | 48 files, 34 MB | LEADERBOARD, CER_BY_SCRIPT (sealed) |
| Probe (18 langs + en) | `level2/probe22/{manifest.json, images/ (1,194: 158 jpg + 1,036 png), out/<engine>/<lang>/ (13,289 packs, 11 engines), scores/, sheet.csv}` + 98 loose root items | 1.1 GB | from the OFFICIAL dataset via `extract_gt.py` → `build_manifest.py` → `run_probe.py` → `metrics.py` |
| New today 16:20 | `level2/models_bodhan/{indic-ocr, indic-ocr-mlx-bf16, indic-ocr-mlx-4bit}/.cache/huggingface` | downloading | the Engine subagent is writing Bodhan **weights** into level2, next to `level2/models/` (which holds outputs) — a fourth confusing name |
| Model assets scattered | `.deps/IndicPhotoOCR` (4.7 GB, hidden), `level2/probe22/tessdata` (133 MB), `level2/research/smoke/anuvaad_tesseract/tessdata` (read by `run_probe.py:218`), `~/.cache/huggingface` (surya), `level2/models_bodhan` | 5 places | nobody can see why they exist |
| Official South sources | `Datasets/akshardrishti_official/{Tamil 38, Telugu 84, Kannada 41, Malayalam 29}` files | — | PDFs + PNGs; mojibake risk (B12: 52/115 "clean" South pages had legacy-font GT) |

## The end state (one sentence)
Every language — 18 probe languages + ta/te/kn/ml + en — lives in ONE tree, drawn by ONE pipeline from the official dataset, scored by ONE scorer, reported in ONE table. Nothing else in level2 pretends to be a benchmark.
```
level2/
├── README.md                     the ONE level2 map (FOLDER_MAP.md + UNIFIED_INDEX.md + MODELS_VS_OUT.md merged in, then bundled)
├── benchmark/                    ← level2/probe22/ renamed (it IS the 22-language benchmark; "probe22" misled — 18 langs + en)
│   ├── manifest_v1.json          the locked 1,283-item manifest, unchanged (lock = content never edited)
│   ├── manifest_v2.json          v1 items + the South items (same schema, origin: official | south_v1_regated)
│   ├── pages/<lang>/<id>.<ext>   probe22/images + the new South pages
│   ├── packs/<engine>/<lang>/<id>.json   probe22/out + ALL new runs (South, Bodhan, …) — ONE physical tree
│   ├── scores/                   sheet_v1.csv (locked) · sheet_v2.csv (all langs) · preds_* · metrics_* · mcnemar · tables
│   ├── pipeline/                 extract_gt.py · build_manifest.py · run_probe.py · metrics.py · candidates/ · manifest_fragments/ · en_sanity/ · slices/ · snapshots/
│   └── docs/                     AGENT_PROTOCOL.md (locked; path errata only) · README · FINAL_REPORT · …
├── engine_docs/<engine>/         PROMPT.md · RUN.md · metrics.json (the 35 real files from models/)
├── research/                     gate experiments, after the proto-95 harvest
└── logs/                         HEARTBEAT.jsonl · DECISIONS.log · run logs · engine_health_log.jsonl
third_party/  (repo root, gitignored)   IndicPhotoOCR (from .deps) · tessdata (both copies merged, sha-checked) · README: source · licence · revision · sha256 · used-by
model weights (Bodhan, surya, …)         OUTSIDE the repo, in the standard HF cache (~/.cache/huggingface); revision + sha256 recorded in DISPATCH_LOG + docs/legal/LICENSE_AUDIT.md
RETIRED: level2/out · level2/models/*/json|png · level2/unified · level2/pages_400 · level2/renders_shared · level2/reports · level2/engines · the South v1 scripts
         → git history (tracked files: `git rm`) + `_archive/bundles/2026-10-01_south_v1.tar.gz` (untracked) + one "History: South v1" section in BENCHMARK_22.md
```

## Phases (each ends with its check. Owners are lanes: see "Who" at the bottom)

**P0 — Freeze + pre-image (Agent 3, 20 min)**
1. Post `P0 START` in DISPATCH_LOG; the Engine lane confirms which engine, if any, is running.
2. sha256 manifest of every file under level2 except `.venv*` → `docs/campaign/audit/level2_pre_move.sha256`.
3. Bundle the UNTRACKED sealed data about to move: `tar -czf _archive/bundles/2026-09-30_level2_untracked_pre_move.tar.gz level2/probe22/out level2/reports level2/probe22/scores level2/probe22/sheet.csv level2/probe22/manifest.json`. `level2/out` is in git, so git is its pre-image.
4. Verify the bundle: extract to scratch, compare sha256 = 100%.

**Check:** bundle entries = file count; sha sample of 200 = 100%.

**P1 — South feasibility on the official data (Agent 3, read-only except a scratch dir, ~1–2 h)**
Run [[proto-71-south-rerun-same-standard]] Phase A as written:
- **Language tables:** do `extract_gt.py` and `build_manifest.py` cover ta/te/kn/ml? Write the exact additions as fix-specs.
- **Extraction:** extract to `docs/campaign/checkpoints/W_south_reports/candidates_<code>.json`, never overwriting `probe22/candidates/`.
- **Engine support per script:** system tessdata has tam/tel/kan/mal; the `run_probe.py` language maps (PADDLE_LANG etc.) need entries. Record them as fix-specs; U10/U11 cover edits to locked files.

**Plus:** re-gate the 400 South v1 pages with the SAME `extract_gt.py` gates (MIN_CHARS 50, MIN_SCRIPT_RATIO 0.5, MAX_LATIN_RATIO 0.6, MAX_CTRL_CHARS 3). Pages that pass may enter the benchmark as `origin: south_v1_regated`, in the same tree and to the same standard; pages that fail are retired.

**Output:** `docs/campaign/SOUTH_RERUN_FEASIBILITY.md`, one row per language: official clean candidates · distinct PDFs · re-gated v1 pages · total available vs 100 · engine coverage · fix-specs.

**Check (Verdict):** gate statistics reproduce; 10 random candidates per language eyeballed (GT vs image).

**P2 — Build the ONE tree (Agent 3, the only mover; ~1 h + path fixes)**
1. Post `P2 MOVE WINDOW START`. No engine starts a run until `END` is posted.
2. `mv level2/probe22 level2/benchmark`, then reorganise inside it to the tree above: `images/` → `pages/<lang>/` (per-language subfolders), `out/` → `packs/`, loose root items → `scores/` · `pipeline/` · `docs/` · `logs/`. Copy `manifest.json` → `manifest_v1.json` and `sheet.csv` → `sheet_v1.csv`, content untouched.
3. Fix every path constant. Start from proto-70's "Path dependencies" list, then re-grep the live code and docs for `probe22`, `level2/out`, `renders_shared`, `pages_400`, `unified`.
   - `run_probe.py` and `AGENT_PROTOCOL.md` get path errata only (U10).
   - Absolute paths in `engine_health_log.py`, `spot_check_engine.py` and `verify_engine_readiness.py` are fixed too.
4. `graphify`: query the graph for every doc that cites a moved path and update those referrers. Historical logs are left alone.
5. Smoke test: one item per engine through `run_probe.py` from the new paths; outputs land in `benchmark/packs/`.
6. Post `P2 MOVE WINDOW END`.

**Check (Verdict):**
- sha manifest after = before for every moved file, with paths remapped;
- the smoke test passes for all 11 engines;
- `grep -rn "probe22/" --include=*.py level2` = 0 outside the history docs.

**P3 — South draw + runs (Agent 3 prepares; Engine lane runs)**
1. **Draw.** `manifest_v2.json` = v1 items + South items: 100 per language where the P1 feasibility table allows, seed 20260926, same stratification. Where fewer exist, take the honest n and record why (the same rule as the 8 short languages; no gate relaxation, no fabrication).
2. **Pages.** Render South pages to `benchmark/pages/<lang>/` in the same format and dpi as the probe images (check `image_meta.json`).
3. **Run list.** Hand it to the Engine lane via DISPATCH_LOG. Order:
   1. Bodhan (after Plan v3 Day 1, from the HF cache);
   2. surya;
   3. tesseract_indic;
   4. rapidocr;
   5. doctr;
   6. easyocr;
   7. indicphotoocr;
   8. paddleocr_indic;
   9. anuvaad_tesseract.

   openbharatocr is recorded as an alias of tesseract_indic (1,225/1,227 identical), and sarvam_vision is marked "not run — cap spent".
4. **Engine discipline.** One engine at a time (AGENT_PROTOCOL). Outputs go straight into `benchmark/packs/<engine>/<lang>/`.
5. **Score.** Use the same `metrics.py`, producing `sheet_v2.csv` for all 22 languages + en, per GT tier ([[proto-62-gt-tier-stratified-reporting]]).

**Check (Verdict):** every engine × South language cell has its count; 10 drawn pages per language spot-checked; no South number is compared with a v1 number.

**P4 — Retire South v1 (Agent 3, after the P3 draw and at least the first 3 engines have landed)**
1. Run `git rm -r level2/out` and `git rm` for the 35 tracked `models/` docs. Git keeps the history, and the 35 docs are moved to `engine_docs/` first.
2. The 4,000 duplicate `models/*/json`: re-verify sha256 against the git blobs, then delete them (U29: twins).
3. Delete the symlink views: `models/*/png`, `pages_400/`, `unified/`. The `unified/` scripts and data (`build_*.py`, `manifest_22.json`, `sheet_v2.csv`, `metrics_80.csv`) move to `benchmark/` first.
4. Bundle the untracked South v1 files into `_archive/bundles/2026-10-01_south_v1.tar.gz` (sha-verified), then remove them: `level2/reports`, `level2/renders_shared`, `level2/engines`, the South v1 root scripts (`orchestrator.py`, `run_engine.py`, `report.py`, `report_gen.py`, `seal_gen.py`, `verify_v2.py`, `deep_verify.py`, `engines_config.py`, `pages_manifest.json`, `pages_script_map.json`, `renders_shared.sha1`).
5. `BENCHMARK_22.md` gets ONE history section: "South v1 (Sep 11–14, Level-1 own-labelled sources, 126/400 scorable) — archived, not comparable". Every current table is built from `benchmark/` only.

**Check:** `ls level2` shows exactly the target entries; `_archive/INDEX.md` has a line per retired file.

**P5 — Assets out of level2 (Engine lane; after its Bodhan download finishes)**
- Move `level2/models_bodhan/*` into the standard HF cache layout (`~/.cache/huggingface/hub/models--<org>--<name>`), or re-download into it. Record revision + sha256. Delete `level2/models_bodhan/`, and fix `run_bodhan.py` to load by repo id and revision.
- `.deps/IndicPhotoOCR` → `third_party/IndicPhotoOCR`; both tessdata copies → `third_party/tessdata` (sha-dedupe); fix the paths.
- Write `third_party/README.md`: one row per asset — source, licence, revision, sha256, used-by (file:line).

**Check:** each engine's smoke test passes from the new paths; `du -sh level2` falls by at least the weights size.

**P6 — level2 root + repo-root hidden debris (Agent 3)**
- **level2 root:**
  - `README.md` = the one map;
  - FOLDER_MAP / UNIFIED_INDEX / MODELS_VS_OUT → merged into it, then bundled;
  - `HEARTBEAT.jsonl` + `DECISIONS.log` → `logs/`;
  - delete every `__pycache__`.
- **`.kilo/`** (Kilo Code worktrees; both at `8fec177` = main, one already "prunable"):
  - for each worktree, check `git -C <path> status --porcelain`;
  - if clean: `git worktree remove`, then `git worktree prune`; then delete `.kilo/`;
  - if dirty: report to the boss, don't delete.
- **`.playwright-mcp/`** (browser-tool logs from today) → delete; add to `.gitignore`.
- **`.venv` vs `.venv311`:** don't delete. Find which scripts and engines use each (shebangs, docs, run logs); the root `README.md` states it in one line each; drop one only if nothing uses it (boss gate).

**P7 — Verify + show the boss (Verdict)**
- **Counts:** before = after + retired, exactly.
- **Engine coverage:** every language has packs from the same engines, or an honest "not run".
- **Stale references:** 0 live references to retired paths.
- **graphify:** `/graphify … --update`, then islands and not-in-graph counts before → after.
- **Table:** `BENCHMARK_22.md` regenerated from `benchmark/` only.
- **The boss gets 10 lines:** the new `ls level2`, languages × engines coverage, what was retired and where it can be recovered (git commit + bundle).

## Whole-repo folder verdicts (the boss asked why each folder exists)
| Folder | What it is | Verdict | Where |
|---|---|---|---|
| `Datasets/` (27 GB, sealed) | official hackathon data + `test/test` (5,344 unlabelled) | KEEP, sealed | — |
| `arc_level_1/` (413, sealed) | Level-1 labelled pages (the South v1 source) | KEEP, sealed; one README line | P6 |
| `level2/` | benchmark work | RESTRUCTURE into the tree above | P2–P6 |
| `docs/` (675) | campaign docs + research | proto-95 harvest + proto-98 finals | proto-95/98 |
| `_archive/` (521) · `_reports/` (58) | old archives + reports about cleanups | COMPACT → INDEX + bundles; `_reports/` gone | proto-96 |
| `scripts/` (7) | bootstrap / setup | KEEP | — |
| `src/` (46) · `tests/` (1) · `configs/` (1) | untracked OpenCode-built trainer/pipeline (routes on ground truth; broken Laya router, F63) | recommend ARCHIVE (bundle); Plan v3 does not use it | **U3 — boss** |
| `graphify-out/` (567) | knowledge graph | KEEP (gitignored); rebuild after P7 | P7 |
| `.deps/` (4.7 GB) | IndicPhotoOCR engine | MOVE → `third_party/` (visible, documented) | P5 |
| `.venv/` (1.2 GB) · `.venv311/` (2.8 GB) | two Python envs | KEEP; README says which runs what | P6 |
| `.kilo/` (4,117) | Kilo Code worktrees of this repo (stale) | REMOVE via `git worktree remove` / `prune` | P6 |
| `.playwright-mcp/` (6) | browser-tool logs | DELETE + gitignore | P6 |
| `.claude/` (2) | Claude Code settings + hooks | KEEP | — |

## Who (lanes; one-line assignments in NEXT.md)
- **Agent 3** (`ses_f16bc20e…`): P0, P1, P2, P3 prep, P4, P6. This is the structure/Miss lane, with subagents.
- **Agent 1 Engine lane** (`ses_f12a7b89…`): P3 runs (after Plan v3 Day 1) and P5. Until P2 creates `benchmark/packs/`, new Bodhan outputs go to `level2/probe22/out/bodhan*/`, which P2 then moves along.
- **Agent 2 Verdict** (`ses_f1233a0a…`): the checks after P1, P2, P3 and P7.

Every phase posts START/END in DISPATCH_LOG and a STATUS line in `docs/campaign/checkpoints/W4.md`.

**Skills:**
- **graphify:** referrer queries in P2; `--update` in P7.
- **ECC** (loaded in the OpenCode agents; for Claude sessions it loads in NEW sessions only): `living-docs-governance` (README / map merge) · `verification-loop` (every check) · `architecture-decision-records` (only if the tree decision needs an ADR — put it inside `level2/README.md`, no new essay).
- **Others:** `ssotize` (map merge) · `superpowers:verification-before-completion`.

**Honesty rules:**
- No phase says DONE without its check command output pasted into W4.md.
- A language short of 100 is reported with its honest n.
- No v1 number is ever mixed into v2 tables.

Related: [[proto-70-level2-restructure]], [[proto-71-south-rerun-same-standard]], [[proto-98-clean-repo-master]], [[proto-96-archive-reports-compaction]], [[proto-62-gt-tier-stratified-reporting]], [[proto-92-boss-decisions]], [[proto-74-root-hidden-hygiene]]


## proto-70-level2-restructure.md — STATUS: PARTIAL (probe22 → level2/benchmark done; rest superseded by 101/104)

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


## proto-72-per-file-audit.md — STATUS: NOT DONE (scripts/repo_inventory.py does not exist)

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


## proto-73-md-fact-consolidation.md — STATUS: NOT DONE

# PROTO-73 — MD FACT CONSOLIDATION (Verdict finds conflicts, Miss applies fixes)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Boss:** uni T2.4 "every topic gets exactly ONE authoritative md … After merging, verify: no two md files state different facts about the same thing … at EVERY level of the project."
CO-012 (clean all hybrid-concern md), CO-013 (merge duplicate md), CO-070 (md cleanup level by level). Today the same facts are stated differently across ~300 live md files.

## Fact families to scan (starting list — extend as found)
| Fact | Known variants on disk (2026-09-30) | Truth source |
|---|---|---|
| probe size | 1,227 · 1,283 · "1,800" · "18 × 100 lock" · 12,324 "packs" | proto-93 F1–F3 (1,283 manifest / 1,227 scored / 12,324 sheet rows) |
| independent engines | 11 · 10 · 9 | 1A audit (openbharatocr ≈ tesseract_indic 1,225/1,227; tesseract_bilingual differs 857/1,227) |
| Sarvam numbers | 87.39 (word accuracy, macro-22, n=6,609) vs our CER; "0.2400 n=54" | COMPETITOR_INTEL §0.2; 1A |
| kok gap | 0.32 / 32pt / 19.4pt / 0.194 | 1A K7 |
| dates | "Wed 2026-10-01", "Tue 2026-09-30", "Oct 4 (Sat)", qualifier 30/09 vs 10-15 | U1/U2 answers |
| W6 path / backbone | Option A vs D; Qwen2.5-VL-3B vs GLM-OCR 0.9B | U4 answer |
| South scored n | "100/lang", "400 pages", 126/400 | CER_BY_SCRIPT.md |
| graph size | 1,324 / 3,990 nodes | graphify-out current |
| status words | "COMPLETE", "DONE", "READY", "LOCKED", "FINAL" on unfinished work | proto-66 register |
| md count | 211 / 240 / 303 / 309 / 379 | recount |

## Skills (load first)
`ssotize` (find the canonical source and plan the merge) · ECC `living-docs-governance` · `graphify` duplicate-label/community queries · `factchk` on every fact family's truth source.

## Verdict subagent — TASK (paste after the shared context block)
> 1. List live md files (exclude `_archive/`, `.venv*`, `Datasets/`, `graphify-out/cache/`). For each fact family above, grep all files for its patterns (write the regex list in the report)
>    and build a table: fact · file:line · stated value · matches truth? (MEASURED against the truth source) · live or historical (append-only log lines are historical — never rewrite them;
>    note them as HISTORICAL).
> 2. Find topics with more than one "authoritative" md (e.g. two meeting packets, three W5 plans, two sampling plans, two leaderboards, several INDEX/MAP docs:
>    `docs/INDEX.md`, `HIERARCHY_MAP.md`, `level2/FOLDER_MAP.md`, `level2/UNIFIED_INDEX.md`, `FULL TECHNICAL BRIEFING.md`, `README.md`, `SOUTH_CANON.md`). Propose ONE authority per topic
>    and what each other file becomes (merge / pointer / historical banner).
> 3. Output `docs/campaign/audit/MD_FACT_CONFLICTS.md`: per family the conflict table + the exact fix-specs (old → new) for live statements; per topic the authority decision.
> Use graphify (`graphify-out/GRAPH_REPORT.md` communities; `graph.json` nodes with the same label in several files) to find topic clusters faster.

## Miss applies (after Verdict review)
Fix-specs per [[proto-18-w1g-apply-verify]] method (pre-images, exact strings, re-verify). Historical log lines get no edits — instead a single dated erratum line where the log allows appends.
Topic losers get a pointer or a banner `> SUPERSEDED by <path> on <date> — kept for history.` Then re-run the scan: every live conflict count must be 0.

Related: [[proto-72-per-file-audit]], [[proto-63-single-canonical-files]], [[proto-66-concern-register-rebuild]]


## proto-74-root-hidden-hygiene.md — STATUS: NOT DONE (root strays remain; small bits in proto-104 step R)

# PROTO-74 — REPO ROOT + HIDDEN FOLDERS HYGIENE (Verdict rules, Miss executes after gates)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Boss:** CO-002 keep only the new, merged · CO-008/015 unnecessary/waste files · CO-010 misleading names · AGENTS.md "no new markdown essays at repo root".

## Measured state (2026-09-30)
Root: 20 md + `AksharDrishti_Hackathon_Proposal.pptx`, `HOW_TO_RUN.txt` (09-25, may cite moved paths), `W5_W6_W7_LOOP.yaml`, `requirements.txt`, `sarvam_smoke.py` (stray script at root), `.env` (Sarvam key; gitignored).
Hidden/support: `.deps/IndicPhotoOCR` 4.4 GB (engine dependency — `level2/run_engine.py:31`; KEEP, document) · `.kilo/worktrees` 31 MB (another agent tool's git worktrees — stale? see proto-76) ·
`.claude/` (2 files) · `configs/evaluation/default.yaml` + `scripts/evaluation/{k1_verdict.py,verify_w6_kill.sh,mcnemar_test.py}` + `scripts/{setup_fresh_machine,install_mlx_stack,reclaim_memory}.sh` ·
untracked `src/` (49 files) + `tests/test_basic.py` (W6 build — U3).

## Items needing a verdict (Verdict subagent reads each, then rules)
| Item | Issue | Proposed |
|---|---|---|
| `PROJECT_COMPLETE.md` | name says complete; project is not | rename → `docs/campaign/history/W5_READY_STATE_2026-09-29.md` + banner, or archive |
| `W5_FREEZE_PLAN.md`, `LOOP_SPEC_W5_W6_W7.md`, `W5_W6_W7_LOOP.yaml`, `W5_BEAT_SARVAM_PLAN.md` (root copy) | W5/W6 plans at root; several copies elsewhere | one home `docs/architecture/w5_w6/`; duplicates per proto-63 |
| `LIVE_LATEST_2026-09-29.md` (root) | duplicate of `docs/research/` copy | pointer/archive (proto-63) |
| `PAPERTHIN_AUDIT.md`, `SAMPLE_PLAN_18_LANGS.md`, `AUDIT_REPORT.md`, `CLEANUP_EXECUTION_LOG.md`, `PROTOCOL_UPGRADES.md`, `HIERARCHY_MAP.md` | root docs; some superseded | keep the 5 directive deliverables (D01–D06 per C5) at root; others move to `docs/` with pointers |
| `sarvam_smoke.py` | stray root script; Sarvam cap is spent | move to `scripts/` with a "do not run — cap spent" header, or archive |
| `HOW_TO_RUN.txt` | 09-25; cites paths that moved | refresh after proto-70, or merge into `README.md` |
| `.env` | secret in repo folder (gitignored) | keep gitignored; verify `git log --all -- .env` shows it was never committed; boss decides moving it outside the repo (U12) |
| `.kilo/worktrees` | possibly stale worktrees of another agent tool | proto-76 decides (active? → keep; stale → `git worktree list`, archive) |
| `scripts/evaluation/*`, `configs/evaluation/*` | appear tied to the `src/` W6 build | follow U3 |
| `src/`, `tests/` | untracked W6 build | U3 |

## Execution rules
Pre-image + sha256 for everything moved; pointers left at old paths for any doc referenced elsewhere; `git mv` where tracked; never touch `.env` content; never delete `.deps`.
After execution: root md count and list recorded; `README.md` at root states the reading order in ≤15 lines.

Related: [[proto-72-per-file-audit]], [[proto-63-single-canonical-files]], [[proto-76-workstreams-and-agent-health]], [[proto-92-boss-decisions]]


## proto-77-graph-concerns.md — STATUS: NOT DONE

# PROTO-77 — GRAPH THE CONCERNS (Miss, graphify skill) — uses `graphify-out/`

**Boss:** C3 "if you were working you would have seen all 50, minimum 50 [concerns in the graph]… I have given you 100+"; M4 "I kept graphify". Current graph: 3,990 nodes / 4,681 edges /
420 communities (rebuilt 2026-09-29 18:24, before the 27-doc move and all Wave 1 outputs) — stale paths now.

## Steps
1. Load the graphify skill (`/graphify` instructions in `~/.claude/skills/graphify/SKILL.md`). Read its query/update modes first.
2. After [[proto-66-concern-register-rebuild]] exists: make each register row a first-class node — the register must be in the corpus and each row identifiable
   (ID + short title). Verify with a graph query that CO-001…096, C1–C17, M1–M8 each resolve to a node, and that each has edges to its protocol file and deliverable.
3. Incremental update (`--update`) after each structural wave (proto-70/72/73/74) so moved files are re-linked; full rebuild only if the skill says incremental cannot handle moves.
4. Use the graph as an audit tool: list orphan md nodes (degree 0–1), duplicate-label nodes across files (feeds proto-73), communities that mix superseded and live docs.
5. Report `docs/campaign/checkpoints/GRAPH_STATUS.md`: node/edge counts, concern-node coverage (n of N), orphans, duplicates, and the command used.

## Done when
Every concern ID in the register resolves to a graph node with ≥1 edge to its protocol and ≥1 edge to evidence or deliverable; the graph report is regenerated after the last structural wave.

Related: [[proto-66-concern-register-rebuild]], [[proto-72-per-file-audit]], [[proto-73-md-fact-consolidation]]


## proto-84-law-hierarchy-consolidation.md — STATUS: NOT DONE (read order now set by proto-00/proto-104)

# PROTO-84 — ONE LAW HIERARCHY (Verdict maps conflicts, Miss applies after the boss sees the map)

**Found 2026-09-30:** law documents — `docs/campaign/CAMPAIGN_DIRECTIVE.md` (Part B/C), `AGENTS.md` (load order + identity), `OCR_AGENT_MEMORY_FEED.md` §9 (hard rules) + §10–§19 locks,
`FULL TECHNICAL BRIEFING.md` Part II §3 ("the 12 standing laws"), `level2/ULTIMATE_HYBRID_CONCERN.md` Part II §4 ("THE 12 STANDING LAWS", L1–L12 incl. L6 "never claim 10 independent", L11
"one fact one file", L12 D12 "new scope auto-rejected inside T-4 of a demo") + Parts VIII–IX amendments, `level2/probe22/AGENT_PROTOCOL.md` §0, `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §7/§9/§10,
`SOUTH_CANON.md` §N, memory `proto-01`. Two "12 laws" lists differ in wording and scope. `FULL TECHNICAL BRIEFING.md` Part II (the doc AGENTS.md calls "Master doc") still shows 2026-09-27
evening state ("surya queued", "W5 freeze Oct 1", "LEVEL7_INTEGRATED_ARCHITECTURE.md" — check it exists). Agents obeyed some laws and broke others (e.g. L6 engine count, L11 duplicates).

## Verdict subagent — TASK (paste after the shared context block)
> 1. Extract every rule from each law document above into one table: rule text (verbatim) · source file:line · scope (campaign / process / probe / South bench / agent behaviour) · status
>    (in force / superseded by X / contradicted by Y). Deduplicate identical rules; list CONTRADICTIONS explicitly (e.g. seals vs the boss's U10 approval; "10 independent" vs L6; W5 dates).
> 2. Propose a layered hierarchy: Layer 0 boss decisions (U-table) → Layer 1 campaign directive → Layer 2 process law (feed §9) → Layer 3 domain law (probe AGENT_PROTOCOL; South bench
>    ULTIMATE_HYBRID_CONCERN) → Layer 4 agent execution protocols (memory proto files). "Higher layer wins; later dated amendment wins within a layer."
> 3. Staleness check of every "current state" section in these docs (FULL TECHNICAL BRIEFING Part II §6–§9, README "State", docs/INDEX.md, SOUTH_CANON §L, PROJECT_COMPLETE) against disk.
> Write `docs/campaign/LAW_MAP.md` (≤2,000 words + the rule table as an appendix).

## Miss applies (after Verdict review; append-only law files get errata lines, not rewrites)
- `AGENTS.md` load order points to `LAW_MAP.md` as step 0.5.
- Stale "current state" sections get a dated banner "SUPERSEDED — current state: docs/campaign/CAMPAIGN_DIRECTIVE.md Part A" or a refresh generated from disk (no hand-typed numbers).
- Duplicated laws: the lower-layer copy becomes a pointer to the owning layer.

Related: [[proto-73-md-fact-consolidation]], [[proto-66-concern-register-rebuild]], [[proto-01-law-and-guardrails]]


## proto-63-single-canonical-files.md — STATUS: NOT DONE

# PROTO-63 — SINGLE CANONICAL FILES (Miss applies, Verdict verifies)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Why:** duplicates drift, and the boss (CO-004, CO-010) forbids "misleading parallel versions". Monitor found (2026-09-30 03:25):
| Document | Copies | Canonical (proposed) | Others become |
|---|---|---|---|
| Meeting packet | root `VINAY_MEETING_PACKET.md` (30.9 KB, corrected 09-30 01:33) · `docs/architecture/VINAY_MEETING_PACKET.md` (6.7 KB, Verdict edition, stale "tomorrow") | root (the corrected one) — until `DRAFT_RESEARCH_PLAN.md` exists, then that is the presented doc | architecture copy → archive to `_archive/pre_fix_2026-09-29/` + pointer file |
| uni v3 | `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` · `docs/research/uni_v3_ORIGINAL_2026-09-29.md` | `_archive/directives/…txt` (superseded law) | docs/research copy → 3-line pointer |
| Meeting 2026-09-29 | `_reports/research/MEETING_2026-09-29_STRUCTURED.md` · `docs/research/MEETING_2026-09-29_STRUCTURED.md` (identical, 17,876 B) | `docs/research/` (agents read there) | `_reports` copy → pointer |
| W5 beat-Sarvam plan | root · `docs/architecture/` · `docs/research/level7/` (+ `_archive/root_md_dedupe_2026-09-29/`) | decided in [[proto-50-w5-repo-map-and-drift]] Part B | — |
| LIVE_LATEST 2026-09-29 | root · `docs/research/` | `docs/research/` | root → pointer (after meeting) |

**State 2026-09-30 ~15:30 (measured):** the `docs/research/` copies of uni and LIVE_LATEST no longer exist (uni copy now in `_archive/cleanup_2026-09-30/single_file_dups/`); `_reports/research/` has no meeting copy — only `docs/research/MEETING_2026-09-29_STRUCTURED.md` remains. Still open: `AGENTS.md` KEY FILES points at both missing paths (fix-spec in proto-95 Step 2). Pointer stubs: only when the referrer cannot be edited (a locked file); otherwise update the referrer (proto-95 Step 4.5) — stub files are junk. Archive copies go into one bundle ([[proto-96-archive-reports-compaction]]), not per-file folders.

## Method (never raw delete)
1. `cmp` / `diff` the copies; if they differ, Verdict decides which content wins and whether anything from the loser must be merged first (fix-spec).
2. Archive the loser to `_archive/dedupe_2026-09-30/<original path with / → __>` and record sha256.
3. Replace the loser with a pointer file: `# MOVED — canonical copy: <path>` + date + reason (so old links still resolve).
4. Log each in `DISPATCH_LOG.md`. Verdict re-runs `cmp`/`ls` to confirm.

**Timing:** the meeting-packet row is meeting-critical (do it in [[proto-64-meeting-day-finish]]); the rest after the meeting. Check the OpenCode cleanup agent is idle first (proto-60 Rule 3).

Related: [[proto-50-w5-repo-map-and-drift]], [[proto-60-monitor-and-checkpoint-discipline]]


## proto-50-w5-repo-map-and-drift.md — STATUS: NOT DONE

# WAVE 5 · PART 1 — REPO MAP, LINK PROOF, DRIFT FIXES → `docs/campaign/FINAL_REPO_MAP.md` (D07)

**Closes:** CO-002/004/006–019/066/067/070 remainder (the 24h cleanup ran; what is missing is link proof and a reason per file).
**Precursors:** `HIERARCHY_MAP.md`, `FILE_INVENTORY.md` (root, 353 lines, 186 verdict mentions), `AUDIT_REPORT.md` (directory-level — not per-file), `docs/INDEX.md`, `DEEP_REPORT.md`.

## Part A — link and path checker (Engine subagent) → `level2/unified/check_links.py` + report
> Write a stdlib python checker over every `*.md` outside `_archive/`, `.venv*`, `Datasets/`, `graphify-out/cache/`: extract markdown links `[..](path)` and backticked
> repo paths (`` `docs/…md` ``, `` `level2/…` ``); resolve relative to the file and to repo root; report BROKEN (target missing), OUTSIDE (points outside repo),
> and ORPHAN md files (no inbound reference from any md). Print counts + first 50 of each. Read-only.

## Part B — reason per file (Miss subagent)
> For every file at repo root and every md under `docs/` (not `_archive/`): one row `path | purpose (one line, from its first lines) | owner (Engine/Verdict/Miss/boss) |
> status KEEP / MERGE→target / ARCHIVE | inbound refs count (from Part A)`. Use `FILE_INVENTORY.md` verdicts where present; fill the rest. Known duplicates to rule on:
> `W5_BEAT_SARVAM_PLAN.md` ×3 (root, `docs/architecture/`, `docs/research/level7/` — an earlier verdict says KEEP-BOTH for architecture vs level7, `CLEAN_DOCS_MD.md:153`;
> the root copy is new — diff all three); `LIVE_LATEST_2026-09-29.md` ×2 (root, `docs/research/`); `W5_STRATEGY_OPTIONS.md` ×2. Verdicts only — Miss executes MERGE/ARCHIVE
> after Verdict approval and after archiving (never raw delete).

## Part C — date-drift fix (only after the boss answers U1)
1. Find: `grep -rn --include='*.md' -E 'Wed(nesday)? 2026-10-01|Tue(sday)? 2026-09-30|Sat(urday)? 2026-10-04|Oct 4 \(Sat\)|Oct-1 freeze' . | grep -v _archive`.
2. Build the replacement table from U1/U2 answers (correct weekday + correct date; for unknowns "TBC"). Do not touch append-only historical log lines in
   `OCR_AGENT_MEMORY_FEED.md` §11 — instead append one erratum line listing the correction.
3. Miss applies per file with exact-string edits; Verdict re-runs the grep → must return 0 lines outside errata.

## Part D — errata for locked/law files
- `AGENTS.md`: fix "probe22 … 18 langs × 100/lang lock" to "1,283 manifest / 1,227 scored; 10 of 18 at 100 scored" (numbers from W2), and "11 engines" → "11 engines, 10 independent".
- `level2/probe22/AGENT_PROTOCOL.md` is CANNOT-apply: append an erratum to `OCR_AGENT_MEMORY_FEED.md` §11: "AGENT_PROTOCOL gates n_total==1227; manifest is 1,283 since 2026-09-29 02:45 (+56 additions); scoring still on 1,227 pending U5".
- `SAMPLE_PLAN_18_LANGS.md`: pointer to `docs/campaign/SAMPLING_PLAN.md` (if W2 did not add it).
- `docs/INDEX.md`: add `docs/campaign/` deliverables.

## `FINAL_REPO_MAP.md` layout
1. Summary: counts (files by area, broken links before/after, orphans, merges done). 2. The hierarchy as a tree (depth 2) with one line per folder purpose.
3. Root and `docs/` per-file table (Part B). 4. Link report after fixes. 5. Sealed/locked list. 6. How to navigate (reading order for a newcomer, ≤10 lines).

## Verdict check
Re-run the link checker after fixes (broken count must drop to 0 or each remaining one justified); sample 10 per-file reasons.

Related: [[proto-92-boss-decisions]], [[proto-51-w5-architecture-freeze]]

