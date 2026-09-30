---
name: proto-98-clean-repo-master
description: "Added 2026-09-30 evening (boss: 'check the hierarchy and the flow … are you using graphify … every file's rating, ranking, its worth to stay … read all the variants and write the final md … variants go to archive … use Laya … so clean, official, perfect') — THE clean-repo master: measured junk (graphify: 204 island md, 101 md not in graph, 20+ plan docs), the official target tree, primary-source protection (docs/sources/), the WORTH score 0–100 for every file + ranking, 14 topic finals (one final md per topic written from ALL variants), graphify signals, the Laya triage trial (U31), and the gated 6-phase order that runs proto-95/72/73/63/74/70/96/50"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T10:21:31.844Z
---

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
