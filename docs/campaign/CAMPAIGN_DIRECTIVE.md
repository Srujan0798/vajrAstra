# CAMPAIGN DIRECTIVE v5 — ACTIVE LAW

**Supersedes:** v4 (archived verbatim at `_archive/directives/CAMPAIGN_DIRECTIVE_v4_2026-09-29.md`) and `uni` v3
(archived verbatim at `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt`, 713 lines, all 96 concerns).

**Issued:** 2026-09-29 ~20:45 IST · **Authority:** BOSS · **Planner:** Opus 5.5 (read + verify + plan only) · **Executor:** Sonnet
**Why v5 exists:** v4 was written before a full read of the repo. The full read found that v4's Wave 1 would duplicate
a meeting packet that already exists, that the packet carries claims that would not survive cross-examination, and that
the two things the lead actually asked for (a 22-language benchmark and a multi-LLM evaluation) do not exist on disk.
v5 keeps v4's law and fixes its state and its waves.

**Model tiering (hard rule):** Opus plans and writes prompts. **Sonnet executes and spawns all subagents, every one with
`model: "sonnet"`.** Never spawn a subagent on Opus — credits are the campaign's binding constraint.

**Where to start (Sonnet):** Part S. It tells you the next open wave and the paste-line for it.

---

## PART A — VERIFIED STATE (measured on disk 2026-09-29 by the planner; re-verify before acting)

### A1. The clock — and a date error that is in 43 files
| When | What | Evidence |
|---|---|---|
| **Wed 2026-09-30 (tomorrow)** | **Vinay meeting — nearest hard gate** | `OCR_AGENT_MEMORY_FEED.md` §15 (user pivot directive) |
| after the meeting | W5 freeze, then W6 training decision | §12.7, §15 |
| **UNKNOWN** | Real hackathon submission deadline | CONTRADICTION: feed §15/§16 say "Oct 4 (Sat)" (Oct 4 is a **Sunday**); `INTEGRATION_REPORT.md:146` says "2026-10-15 Bhashini qualifier deadline"; feed log R132 says "qualifiers close 30/09" → **boss decision U2** |

**Calendar truth:** 2026-09-29 = Tue · 09-30 = **Wed** · 10-01 = **Thu** · 10-04 = **Sun**. At least 43 docs say
"Wed 2026-10-01"; `VINAY_MEETING_PACKET.md` says "Tue 2026-09-30". The source of the Oct-1 date is the lead's own
words in the raw transcript: *"I'll join after next Wednesday."* That phrase is ambiguous (Sep 30 or Oct 7) → **boss decision U1**.
Until U1 is answered, write dates as weekday-correct ISO dates and do not invent a weekday.

### A2. What the lead actually asked for (raw transcript, `MEETING_2026-09-29_STRUCTURED.md`) — and its real status
He did **not** ask for a decision menu. His words: *"you first do some, like, this initial draft research plan. I'll discuss it
with you, and then we will finalize"* · *"a 15-20 minute session… you present the plan, we can cross question each other"* ·
*"you have done for South Indian languages only, no? So just cover the other languages also before giving your final"* ·
*"five or ten samples, that's enough"* · *"research on existing models and what are the best hybrid way of integrations"* ·
*"use multiple LLMs as an evaluator… by the process mentioned, not by the AI mentioned"*.

| # | Lead's action | Status on disk (planner-verified) |
|---|---|---|
| A1 | Research sprint: Consensus.app + arXiv → OCR-training flowchart, last-6-weeks breakthroughs, Indic advances, hybrid patterns | PARTIAL — heavy live research exists (`docs/research/LIVE_LATEST_2026-09-29.md`, `DEEPER_LIVE_RESEARCH_2026-09-29.md`, `docs/research/level7/` ledgers). **No training flowchart document. No evidence Consensus.app was used** (verify in 1C). |
| A2 | Diff findings vs his PPT architecture | DONE — `PPT_VS_SPEC_DIFF.md`, `PPT_FULL_DUMP.md` |
| A3 | Multi-LLM evaluation (OpenCode + Claude + ChatGPT) of the plan | **NOT DONE.** Planned as "W4" in `docs/PLAN.md:23`; no evaluation artifact exists anywhere. |
| A4 | 15–20 min review: present plan, cross-question | PARTIAL — `VINAY_MEETING_PACKET.md` exists (READY) but is framed as "4 decisions in 5 minutes", not a draft research plan to cross-question. |
| A5 | Benchmarks for **all 22** languages, 5–10 samples each | **Data: MET** — all 22 languages have ≥19 labelled samples. **Artifact: NOT DONE** — no single 22-language score table exists; `level2/unified/` is symlinks split into `probe22/` and `south_400/`. |
| A6 | Ping Krishna / Aryan | UNKNOWN — boss's personal action |
| A7 | Feed context to agents | STALE — `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` belong to the finished Level-7 mission. This directive replaces them for new work. |

### A3. The meeting packet exists — and has defects that would not survive cross-examination
`VINAY_MEETING_PACKET.md` (root, 26.8 KB, "READY", last edited 20:08 IST by the OpenCode agents) + `EVIDENCE_SUMMARY.md`.
Planner-found defects (Verdict must reproduce each, not trust the planner):
- **K1 "Beats Sarvam on 9/18 langs"** (packet §1 table). Planner's paired measurement from `level2/probe22/sheet.csv`
  on the 54 items where Sarvam ran (3 per language): surya's mean CER is lower than Sarvam's in **10/18** languages
  (brx, gu, ks, mai, mr, ne, or, pa, sd, ur); item-level **Sarvam better 28, surya better 21, tie 5**. With n=3 per
  language this is directional noise, not a win. `EVIDENCE_SUMMARY` §3 "surya wins" is surya vs *other local engines*,
  not vs Sarvam. The sentence must be rewritten to what the data supports.
- **K2** Packet says "1,227 items"; `manifest.json` has **1,283**. Both true of different things (A4) — the packet must say which.
- **K3** Weekday errors: "Tue 2026-09-30", "Sat 2026-10-04", "Wed 2026-10-01".
- **K4 Strategy conflict:** Miss recommends **Option A** (wrap-only + QLoRA kok+pa, root `W5_STRATEGY_OPTIONS.md` / packet);
  Verdict recommended **Option D** (wrap + script-router + R4 restoration + Sarvam-API subsidy for sat/mni,
  `docs/architecture/W5_STRATEGY_OPTIONS.md`, feed §15 Verdict entry). The packet presents only A.
- **K5 Backbone conflict:** feed §12.2 locks **Qwen2.5-VL-3B @4-bit** as PRIMARY; the packet says **GLM-OCR 0.9B** primary.
- **K6** `EVIDENCE_SUMMARY` §3 `sa` row note "surya all-empty (Ol Chiki bug)" — `sa` is Sanskrit/Devanagari, Ol Chiki is Santali.
  The fact under it is real: surya CER = 1.000 on all 3 `sa` Sarvam-paired items. Label is wrong.
- **K7** kok gap stated as 0.32 (feed §12.2) and 0.194 (EVIDENCE §3, DISPATCH_LOG P5). One is wrong.

### A4. probe22 — manifest vs scored set
- `manifest.json` = **1,283** items = 1,227 base + **56 additions** (`manifest_additions.json`, 2026-09-29 02:45: sd +25, mr +21, pa +10).
- `sheet.csv` = **12,324 rows = 10 engines × 1,227 + 54 Sarvam** → scoring covers the **1,227 base only**.
  Scored n per language (EVIDENCE §3): mr 79, pa 90, sd 75, or 66, sa 99, brx 67; others 100 or low-n.
- Engine outputs for the 56 additions are **partial** (surya has 43/56 packs; `out/rapidocr/` holds 121/110/125 files for mr/pa/sd — extras unexplained).
- `AGENT_PROTOCOL.md` still gates on `n_total == 1227` (6 mentions of 1227, 0 of 1283). It is on the CANNOT-apply list (feed §12.9) → erratum only.
- `AGENTS.md` claims "18 langs × 100/lang lock" — false for the scored set.

### A5. Sampling — 22 languages, and why the gap cannot be closed from PDFs alone
- Manifest-level: 1,283 (18 langs) + South 4 × 100 in `level2/out/` = **1,683 / 22 languages**. Boss target 100 × 22 = 2,200 → deficit **517**:
  as 19 · mni 20 · sat 20 · gu 24 · doi 27 · ne 37 · brx 67 · or 69.
- **South is 100/lang labelled but NOT 100/lang scored.** Only **126 of 400** South pages carry a CER (`level2/reports/CER_BY_SCRIPT.md`, basis
  `CER_STAGE3B.json`: 55 pages nulled as legacy_mojibake_layer, 219 as gt_thin < 179 chars). By dominant script: Tamil 53, Telugu 6, **Kannada 4, Malayalam 4**,
  Devanagari 16, Latin 43. So kn/ml are below even the lead's 5–10 floor at the scored level, and "22 languages covered" holds only for labelled data.
  The 22-language table (D14) must show labelled n and scored n separately.
- gu example of why the gap is structural: 220 PDFs, 3,567 pages with text, **3,486 rejected as mojibake/wrong script** (legacy font encodings), 10 clean candidates (`candidates/gu.json`).
- **Why short:** the honesty gates (≥50 chars, script ratio ≥0.5, Latin ≤0.6, ctrl chars ≤3) reject their PDF text layers — not page offsets.
  `AGENT_PROTOCOL` forbids lowering gates. `SAMPLE_PLAN_18_LANGS.md` (precursor, stale at 1,227) already concluded: accept low-n for
  as/doi/gu/mni/sat with permanent caveats; re-source ne/or/brx where clean candidates remain.
- **Variance (per language, from manifest):** pair tier (bn/hi/sa) = 100 distinct images spread across the whole pool
  (bn ids 32→3088, hi 18→3461, sa 22→506; seeded shuffle SEED 20260926) → **CO-023/024 disproven for pair tier.**
  PDF tier concentration is real: **kok 100 pages from 2 PDFs, pa 100 from 2 PDFs**; or 2, ne 2, gu 2, doi 4, brx 7 PDFs;
  **ur 34/100 items on page ≤1** (first-page bias), ks 15/100. Fill tier (as, mni, sat + parts of others) = single source (sarvam_bench).
- CONTRADICTION (open): protocol calls sarvam_fill "machine GT", but the indic-ocr-bench card reportedly says GT was human-reviewed
  twice. If true, fill items are better than silver and the mni/sat "BARRED" verdicts may be a verifier-competence artefact
  (an LLM-vision verifier that cannot read Ol Chiki / Meetei Mayek). **Record evidence only; §6.4 stays LOCKED unless the boss reopens it.**

### A6. Other actors are writing to this repo right now
- Two **OpenCode** processes (running since 07:29 and 18:56 IST) are active. At ~20:20 they logged an "AGENT-1 integration pass"
  in `DISPATCH_LOG.md` declaring D08/D10/D12/D13 "mapped to existing files, no new files".
- An **untracked `src/` tree** appeared 19:53–20:07 IST: `src/training/trainer.py` (QLoRA, GRPO RLVR, SFT), `src/training/grpo_trainer.py`,
  `src/models/{base,bodhan,glm_ocr,lighton_ocr,paddle_vl,qwen_vl}.py`, plus `src/{data,evaluation,inference,pipeline,utils}`.
  No Claude session wrote it. It conflicts with feed §15 "STOP all W6 fine-tuning prep" → **boss decision U3**. Do not run it, do not delete it.
- Rule for Sonnet: before each wave, check `ps aux | grep -E 'claude|opencode' | grep -v grep` and `tail -30 DISPATCH_LOG.md`.
  If another agent is editing a file your wave will edit, stop and tell the boss.

### A7. Already DONE — do not re-run (carried from v4, re-verified)
- 24-hour cleanup completed 2026-09-29 (~97.3 MB freed, 234+ files archived then deleted; `DEEP_REPORT.md`).
- `Untitled` ingested and deleted (CO-069). No `old` folder at level 2 (CO-001). `uni` archived.
- Graph rebuilt 18:24 IST: 3,990 nodes / 4,681 edges / 420 communities (`graphify-out/`).
- LAYA vs JEV was already researched: `docs/research/DEEPER_LIVE_RESEARCH_2026-09-29.md` §B6. JEV wins accuracy
  (Banking77 0.870 vs 0.425; zero-shot typed decisions 0.727 vs 0.362) but is closed-source, hosted, ~236–276 ms p50;
  Laya is Apache-2.0, 32.8 ms on T4, runs locally. **Neither is an OCR model** — both fit only as routing/decision heads.
  `LAYA_GATE_DECISIONS.md` applies the laya-gate skill to cleanup actions.
- `ecc-memory` MCP server: was ENOENT (stale npx cache path); **fixed 2026-09-29 20:25 IST** by pointing it at
  `~/.claude/plugins/cache/ecc/ecc/2.2.2/scripts/memory-mcp.mjs`. Connected. Not a finding any more.
- Sealed, never edit: `level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`, `Datasets/akshardrishti_official/`.

### A8. Known barred paths (do not re-litigate)
`ne` PDF-tier BARRED (R5). §6.4 BARRED from W6: ks, mni, ur, sat, mr, ne-PDF. Santali has no local engine (only sarvam_vision emits Ol Chiki).
Effective independent engines = **10**, not 11 (tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr, byte-identical).
Sarvam calls used: **57** (54 + 3 EN) — cap reached; no further calls without the boss's explicit yes.

---

## PART B — CONFLICTS COUNTERED AND SETTLED

**C1–C5 from v4 stand** (meeting-first · bounded waves ≤5 subagents with checkpoints · evidence-per-entry, no paper quota ·
keep 100 × 22 but adopt the mentor's breadth · 8 new deliverables go in `docs/campaign/`, root stays clean). Full text in the v4 archive.

**C6 — v4 Wave 1 duplicates work that exists.** The meeting packet, strategy options, evidence summary and beat-Sarvam plan are on disk.
→ **Resolution:** Wave 1 = *audit and correct* what exists + *build only what is missing* (22-language table, multi-LLM evaluation,
draft research plan in the lead's format). New deliverable files in `docs/campaign/` are **thin**: verdict + evidence + links to
precursors. They never copy precursor content. This honours both C5 and the OpenCode "no duplicate files" pass.

**C7 — Date drift.** See A1. → Fix after U1; until then weekday-correct ISO dates only.

**C8 — 1,227 vs 1,283.** → Every number states its set: "1,283 manifest items" or "1,227 scored items". Scoring the 56 additions
changes the LOCKED `sheet.csv` → **boss decision U5**; not before the meeting.

**C9 — "Beats Sarvam on 9/18" is not supported at n=3/lang** (A3 K1). → Say exactly what the paired data shows, with n.
CO-090 ("be structurally overconfident, then prove it") yields to CO-086 (no fake claims): claim only what is proved.

**C10 — Strategy and backbone conflicts (A3 K4, K5).** Not Sonnet's to settle. → The packet presents Option A and Option D side by side
with evidence, Verdict states a recommendation, and **the boss/Vinay decide (U4)**.

**C11 — `src/` training tree vs the W6 pause (A6).** → Untouched, unrun, reported. **U3.**

**C12 — sarvam_fill GT status (A5).** → 1D records the dataset-card evidence as CONTRADICTION. §6.4 stays LOCKED unless the boss reopens it.

---

## PART C — RULE 0 (unchanged, binding on every agent)
R0.1 Read first, act second · R0.2 Persist everything to disk the moment it exists · R0.3 No vibe coding — every decision has a
written reason tied to evidence · R0.4 No self-limiting · R0.5 No rushing, no dawdling · R0.6 No foolish deletions — KEEP/MERGE/DELETE
with a reason before removal · R0.7 Past work is gold; do not re-litigate finished work · R0.8 Orchestration, not labour ·
R0.9 One-line prompts; detail lives in md · R0.10 Do not ask "what next"; surface only blocking decisions, with a recommendation ·
R0.11 Everything traceable.
**Evidence law:** every record carries PRIMARY / MEASURED / DERIVED / CONTRADICTION / UNKNOWN / REJECTED / DEAD and names the decision
it can change. **No fake claims (CO-086):** evidence or silence. Honest-empty is correct. A sharp UNKNOWN beats a soft guess.
**Done means reproduced:** nothing is DONE without a command whose output reproduces the claim. Past failures this rule exists for:
a manifest dedup applied without a hostile pass destroyed 447 items; 6 of 10 Verdict fix-specs were written from stale text;
5 of 9 claimed per-language winners were false; `BOSS_CONCERNS.md` marked a directory-level audit as a "54,000-file per-file audit".

---

## PART D — AGENTS AND HOW SONNET RUNS THEM
The Sonnet session is the **lead**. It dispatches subagents in the three roles below and composes deliverables from their reports.

| Role | Owns | Must not |
|---|---|---|
| **Engine** | engines, scoring, tables, scripts, compute | call a result final without Verdict sign-off |
| **Verdict** | verification, hostile audits, fix-specs, rankings, truth status | apply its own fix-specs; stay silent before a bad directive — it counters with evidence |
| **Miss** | applies fix-specs, doc edits, logs (`DISPATCH_LOG.md`, `BOSS_CONCERNS.md`, feed §11), research consolidation | apply a fix to a truth-bearing file without Verdict verification |

**Cross-check law:** every Engine/Miss output is verified by a Verdict subagent before it counts. Fix loop max 2 rounds, then escalate to the boss.
**Subagent rules:** `model: "sonnet"` always · ≤5 in flight · a subagent writes only the files its prompt names; everything else goes into
its final report for the lead · every report ends with a list of every file:line or URL it relied on.
**Interfaces (append-only):** `DISPATCH_LOG.md` · `level2/probe22/fix_specs/` · `BOSS_CONCERNS.md` · `OCR_AGENT_MEMORY_FEED.md` §11 ·
`docs/campaign/checkpoints/W<n>.md` (one per wave; create the folder on first use).

---

## PART E — DELIVERABLES
| ID | File | Status 2026-09-29 | Wave |
|---|---|---|---|
| D01 | `BOSS_CONCERNS.md` | EXISTS (own numbering; CO register lives in Part G here) | — |
| D02 | `AUDIT_REPORT.md` | EXISTS (directory-level, not per-file — see CO-067) | 5 |
| D03 | `CLEANUP_EXECUTION_LOG.md` | EXISTS | — |
| D04 | `docs/campaign/SAMPLING_PLAN.md` | MISSING — precursor `SAMPLE_PLAN_18_LANGS.md` (stale) | 2 |
| D05 | `PROTOCOL_UPGRADES.md` | EXISTS | — |
| D06 | `DISPATCH_LOG.md` | EXISTS | — |
| D07 | `docs/campaign/FINAL_REPO_MAP.md` | MISSING — precursors `HIERARCHY_MAP.md`, `FILE_INVENTORY.md` | 5 |
| D08 | `docs/campaign/RESEARCH_CORPUS.md` (S1–S12 index) | MISSING — precursors: level7 a/b/c ledgers, `LIVE_LATEST`, `DEEPER_LIVE_RESEARCH` | 4 |
| D09 | `docs/campaign/ARCHITECTURE_FREEZE.md` | MISSING — only at the architecture call | 5 |
| D10 | `docs/campaign/SKILL_STACK.md` | MISSING — precursors `INTEGRATED-ELITE-STACK.md`, `LAYA_GATE_DECISIONS.md`, §B6 | 3 |
| D11 | `docs/campaign/COMPETITOR_INTEL.md` | MISSING — precursors `docs/research/R6_COMPETITION_INTEL.md`, `LIVE_LATEST`, `DEEPER_LIVE_RESEARCH`, `docs/south/EXTERNAL_BENCHMARK_MAP.md`, `PAPERTHIN_VINAY_AUDIT.md` | 1 |
| D12 | `docs/campaign/EDGE_THESIS.md` | MISSING — precursors `docs/architecture/W5_BEAT_SARVAM_PLAN.md`, `W5_STRATEGY_OPTIONS.md` (both), `R1_SOTA_MECHANISM_TEARDOWN.md` | 1 |
| D13 | `docs/campaign/MENTOR_PLAYBOOK.md` | MISSING — precursors `MEETING_2026-09-29_STRUCTURED.md`, `PPT_FULL_DUMP.md`, `PPT_VS_SPEC_DIFF.md` | 1 |
| **D14** | **`docs/campaign/BENCHMARK_22.md`** | **MISSING — the lead's explicit ask** | **1** |
| **D15** | **`docs/campaign/MULTI_LLM_EVAL.md`** (+ `CHATGPT_EVAL_PROMPT.md`) | **MISSING — the lead's explicit ask (A3)** | **1** |
| **D16** | **`docs/campaign/DRAFT_RESEARCH_PLAN.md`** | **MISSING — what the boss presents tomorrow, in the lead's format** | **1** |

---

## PART F — THE WAVE PLAN

**Shared context block — paste at the top of every subagent prompt:**
> You are a subagent on the South / AksharDrishti Indic OCR campaign at `/Users/srujansai/Desktop/South`. First read `AGENTS.md` and
> `docs/campaign/CAMPAIGN_DIRECTIVE.md` Parts A and C — Part A is verified disk truth and overrides any doc that disagrees.
> No fake claims — the hardest rule here. Every claim carries a file:line or a URL you actually opened. Never invent a URL, number,
> paper title or quote. Honest-empty is correct; a sharp UNKNOWN beats a soft guess. Live sources over pretrained knowledge.
> Never: download weights or datasets, train, call Sarvam, edit sealed dirs (`level2/out/`, `level2/reports/`, `level2/probe22/out/`,
> `arc_level_1/`, `Datasets/akshardrishti_official/`), edit `AGENT_PROTOCOL.md`, `manifest.json`, `sheet.csv`, `run_probe.py`, or touch `src/`.
> Write only the files this prompt names. Read big files in slices (`sed -n`, `cut -c1-800`), never whole. Finish with a structured report
> and the list of every file:line / URL you relied on.

### WAVE 1 — tonight, before the 2026-09-30 meeting (gates everything)

**Batch 1α — 4 subagents in parallel**

**1A · VERDICT · hostile audit of the meeting documents → fix-specs**
> Audit `VINAY_MEETING_PACKET.md`, `EVIDENCE_SUMMARY.md`, both `W5_STRATEGY_OPTIONS.md` (root and `docs/architecture/`),
> both `W5_BEAT_SARVAM_PLAN.md` (`docs/architecture/` and `docs/research/level7/`), `PER_LANG_ROUTING.md`, `COMPUTE_BUDGET_ESTIMATE.md`.
> (1) List every numeric or factual claim in the packet. For each, reproduce it from disk with one command (`level2/probe22/sheet.csv`,
> `manifest.json`, `scores/`, `gt_verification.json`, `level2/reports/`) and mark VERIFIED / WRONG / UNSUPPORTED / STALE.
> (2) Reproduce, do not trust, the planner's defects K1–K7 in Directive Part A3. For K1 recompute the paired Sarvam-vs-surya and
> Sarvam-vs-best-local comparison on the 54 Sarvam items, per language and item-level, and write the one sentence the data supports, with n.
> (3) For K4 (Option A vs D) and K5 (Qwen2.5-VL-3B vs GLM-OCR 0.9B), lay out the evidence for each side and give your recommendation.
> Do not decide it; the boss decides.
> (4) Output: numbered fix-specs, each = file · exact old text · exact new text · evidence command + output. Write them to
> `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` (the only file you write). Under 2,000 words.

**1B · ENGINE · the 22-language benchmark table → `docs/campaign/BENCHMARK_22.md` (D14)**
> The lead asked for benchmarks "for all the 22 languages" before the final. The data exists in two places and has never been put in one table.
> Sources (read-only): `level2/probe22/sheet.csv` (18 languages × 11 engines, 1,227 scored items) and the South-4 results
> (ta/te/kn/ml, 100 each × 10 engines) in `level2/out/` + `level2/reports/LEADERBOARD.md` + `CER_BY_SCRIPT.md`.
> (1) Find how South-4 per-pack CER is stored in `level2/out/` (read 2–3 JSONs first). Compute per-language, per-engine CER **mean and median**
> for all 22 languages on one basis. If the South basis cannot be matched to probe22 (different metric, normalisation or rendering), show both
> and label the difference in a column — never silently mix them.
> (2) One table: rows = 22 languages (script, n, GT tier: gold pair / PDF layer / fill), columns = engines, best local engine, Sarvam CER with its n
> where it exists, and a low-n flag (n<50 → no winner claim, per D4). Then a ≤10-line plain summary for the lead.
> (3) Consistency check: your probe22 numbers must reproduce `EVIDENCE_SUMMARY.md` §3. Report every mismatch.
> (4) Diff our scoring normalisation (`level2/probe22/metrics.py`) against Sarvam's published `metrics.py` for indic-ocr-bench
> (open the HF dataset repo page with WebFetch — reading a page is allowed, downloading data is not). List every normalisation step that differs.
> Write only `level2/unified/build_benchmark_22.py` (read-only on its sources) and `docs/campaign/BENCHMARK_22.md`.

**1C · MISS · the mentor's playbook → `docs/campaign/MENTOR_PLAYBOOK.md` (D13)**
> Read in full: `MEETING_2026-09-29_STRUCTURED.md` (the RAW block is one long line — print it wrapped with python `textwrap`), `PPT_FULL_DUMP.md`,
> `PPT_VS_SPEC_DIFF.md`, `docs/architecture/PPT_SPEC.md`, and `_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx`
> (read `word/document.xml` via python zipfile; if unreadable, say so).
> Deliver: (1) his method as ordered steps, each with his quote, what it means here, compliance yes/partial/no with file evidence — including
> the Consensus.app step (search the repo for any evidence it was used), the OCR-training flowchart step, the last-6-weeks breakthroughs step
> and the multi-LLM-evaluator step; (2) **the current training recipe as a mermaid flowchart**, built only from `PPT_SPEC.md`,
> `docs/research/W1_RECIPE_REFRESH.md` and `docs/research/level7/W6_QLORA_SPEC.md` — this is the flowchart he asked for; (3) the A1–A7 table
> from Directive Part A2, re-verified on disk; (4) every constraint he set, quoted (no novel backbone; hybrid integration of existing models;
> 5–10 samples × 22; 15–20 min cross-question session); (5) **where the repo diverges from what he asked**, blunt, with paths.
> Write only `docs/campaign/MENTOR_PLAYBOOK.md`. Under 1,800 words.

**1D · MISS (research) · competitor intel → `docs/campaign/COMPETITOR_INTEL.md` (D11)**
> Consolidate — do not redo — the precursors listed for D11 in Part E. Then **live re-verify only the numbers the meeting packet uses**
> (load WebSearch/WebFetch via ToolSearch `select:WebSearch,WebFetch`): Sarvam Vision 2.1's 87.39 (which metric, which subset, what denominator,
> https://www.sarvam.ai/blogs/sarvam-vision-2-1); per-language Sarvam numbers used in the packet (sat 53.91, ks 54.82, OldScan 55.3, or 80.01, mni 85.12);
> https://huggingface.co/datasets/sarvamai/indic-ocr-bench (languages, per-language sizes, the 6,909-block figure, **how GT was produced — this settles
> Part A5's CONTRADICTION**); Bodhan (84.94, 82.85 mni); Gnani https://www.gnani.ai/ and https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B;
> https://consensus.app/ (is the free tier usable as the lead says?). Per competitor: architecture, training, data, exact numbers with what they measured,
> weaknesses, and **WHAT THEY OVERLOOKED**. PRIMARY / DERIVED / UNKNOWN on every line. An UNRESOLVED section for anything you could not open.
> Write only `docs/campaign/COMPETITOR_INTEL.md`. Under 1,800 words.

**Batch 1β — after 1α returns (lead composes first, then dispatches)**

**1E · edge thesis → `docs/campaign/EDGE_THESIS.md` (D12)**
Step 1 — one research subagent hunts the hidden frontier exactly as v4 Wave 1C specified (verbatim prompt in the v4 archive, lines 165–174:
2025–2026 only; submerged, understated, cross-field, evaluation flaws; REJECTED-AS-WELL-KNOWN list; queries logged; "eight non-obvious beat forty known").
Step 2 — the lead drafts 3–5 candidate theses from 1A–1D + the hunt. Planner-visible seeds to **test, not assume**: (i) an independent-evaluation edge —
Sarvam built and scored its own bench (dataset-overlap CONTRADICTION in `EVIDENCE_SUMMARY` §0), and our probe has 300 human gold pairs;
(ii) per-script routing with a calibrated confidence gate (Laya-style head) over the 10 engines we already run; (iii) restoration pre-pass for
OldScan (R4); (iv) Kashmiri specialist data (600k-ks-ocr, needs a download gate); (v) the 22-language breadth itself (D14).
Disqualified: "we use agentic AI", "combine X and Y" without a mechanism, anything needing a novel backbone, compute or data we lack.
Step 3 — refute each candidate with 3 adversarial subagents (lenses: incumbents already do it · the mechanism fails on real Indic input ·
cannot be built in ~5 days by one operator with no training started and the Sarvam cap spent). ≤5 in flight → run in rounds.
A candidate survives only if fewer than 2 of 3 lenses refute it. Only survivors go in, each with mechanism, why incumbents haven't done it,
evidence URLs, falsifier, cost in dev days. Killed candidates are recorded with the reason. Zero survivors is an acceptable, honest result.

**1F · multi-LLM evaluation (lead's A3) → `docs/campaign/MULTI_LLM_EVAL.md` + `CHATGPT_EVAL_PROMPT.md` (D15)**
The lead composes a one-page plan summary from 1A–1E (current state, 22-language table, proposed hybrid integration vs the PPT, open risks). Evaluators:
(1) **OpenCode** via the `opencode` MCP (`opencode_setup`, then `opencode_provider_list`; use a non-Anthropic model if one is configured, otherwise
record that it used the same model family); (2) a **fresh Sonnet subagent** told to act as a hostile technical reviewer, given only the one-pager and the
evidence files, never the lead's reasoning; (3) **ChatGPT** — write `CHATGPT_EVAL_PROMPT.md`, paste-ready, and ask the boss to paste it and return the answer.
In `MULTI_LLM_EVAL.md`, list each critique → accept / reject → reason. The lead's rule: accept "by the process mentioned, not by the AI mentioned".

**Batch 1γ — apply and verify**
- **1G · MISS** applies the 1A fix-specs to the meeting documents (not to sealed or locked files). **VERDICT** re-verifies every applied fix (max 2 rounds).
- **1H · lead** writes `docs/campaign/DRAFT_RESEARCH_PLAN.md` (D16) — the 15–20 minute document the boss presents, in the lead's order:
  (1) how an OCR model is trained — the 1C flowchart; (2) what changed in the last 6 weeks (1D + research precursors); (3) proposed hybrid integration
  vs the PPT — Option A and Option D side by side (C10); (4) the 22-language benchmark (D14) with honest n; (5) multi-LLM critiques and what changed (D15);
  (6) edge thesis survivors (D12); (7) questions for cross-questioning, and the decisions U1–U5. ≤4 pages. Every number traceable. Then add a pointer to it
  at the top of `VINAY_MEETING_PACKET.md`.
- **Wave 1 exit gate:** D11–D16 exist; every packet claim is VERIFIED or removed; `DISPATCH_LOG.md` appended; `docs/campaign/checkpoints/W1.md` written;
  boss gets a ≤10-line report + the ChatGPT paste request.

### WAVE 2 — after the meeting → `docs/campaign/SAMPLING_PLAN.md` (D04)
Build on `SAMPLE_PLAN_18_LANGS.md`; do not redo it. (1) Reconcile per language: manifest n vs scored n vs per-engine coverage of the 56 additions;
explain the rapidocr extras. (2) Derive `level2/unified/manifest_22.json` (new file; never edit `manifest.json`): 22 languages, one order, tier per item (CO-003/025/068).
(3) Variance evidence per language: distinct PDFs, distinct pages, page-offset distribution, page≤1 share, top-PDF share. Name kok/pa (2 PDFs), ur (34% page≤1), ks (15%).
(4) For the 8 short languages measure: raw pages available, gate rejections by reason, clean candidates not yet drawn. (5) Re-source plan **within the gates** for
languages with clean candidates left (expected ne, or, brx). Accept low-n with a permanent caveat for as/doi/gu/mni/sat unless the boss approves outside sources.
(6) Concentration fixes (kok/pa re-draw) and scoring the additions are **proposals only** → U5. Never fabricate samples. No 400-page collections.

### WAVE 3 → `docs/campaign/SKILL_STACK.md` (D10)
Inventory every skill, plugin, MCP server and repo across Claude (`~/.claude/skills`, `~/.claude/plugins`, `claude mcp list`) and OpenCode
(`~/.config/opencode/`), plus `INTEGRATED-ELITE-STACK.md`. Per tool: what it does, where it belongs in this campaign, used or not (with evidence), and
a written reason for every idle tool (CO-075). **Binding LAYA vs JEV verdict** from §B6 + `LAYA_GATE_DECISIONS.md`, re-checked live only for licence,
pricing and local feasibility on this Mac; rule which one, where, as what component (routing/decision head, not OCR). Evaluate ECC and graphify the same way (CO-076/077/094).

### WAVE 4 → `docs/campaign/RESEARCH_CORPUS.md` (D08)
An **index**, not a new corpus. Map existing records (level7 a/b/c ledgers, `LIVE_LATEST`, `DEEPER_LIVE_RESEARCH`, R1–R7, W1) to threads
S1 agentic/multi-agent · S2 self-improving agents · S3 OCR classical→VLM · S4 Indic OCR & document AI · S5 RVL/document intelligence · S6 NVIDIA ·
S7 Jais-class Indic LLMs · S8 layout · S9 KG/agent memory · S10 long-horizon agents · S11 LAYA & JEV integration · S12 Gnani-class Indic MoE.
Per thread: record count, top 5 with "what WE build from this", gaps. Fill a gap live only where a thread has fewer than 3 decision-relevant entries. No quota (C3).

### WAVE 5 — after the meeting
- `FINAL_REPO_MAP.md` (D07): link-check every md link, every referenced path exists, and a one-line reason per file at root and in `docs/` (CO-067).
- Date-drift fix across all docs once U1 is answered (Miss applies, Verdict verifies with a grep that returns 0).
- `AGENTS.md`: fix the "18 × 100 lock" claim and point at v5. `AGENT_PROTOCOL.md` is CANNOT-apply → append an erratum (1,227 scored / 1,283 manifest) to feed §11.
- `ARCHITECTURE_FREEZE.md` (D09): only at the architecture call, gated on D12 and D16 being evidence-backed. Level 7 stays frozen until then.

---

## PART S — SONNET EXECUTION HANDOFF (start here)

**The detailed, step-by-step execution protocols live in Claude memory**, not in this file:
`~/.claude/projects/-Users-srujansai-Desktop-South/memory/proto-00-runbook.md` (master runbook) → `proto-01` law · `proto-02` pre-flight/checkpoints ·
`proto-10…19` Wave 1 (one file per step 1A–1H, each with full subagent prompts, commands, output layouts, acceptance checks) · `proto-20/21` Wave 2 ·
`proto-30/31` Wave 3 · `proto-40` Wave 4 · `proto-50/51` Wave 5 · `proto-90` templates · `proto-91` Verdict cross-check · `proto-92` boss decisions · `proto-93` measured facts.
Part F below is the summary; where Part F and a proto file differ on procedure, the proto file wins; on facts, Part A wins.

**How the boss starts it:** open a **fresh** session in `/Users/srujansai/Desktop/South` (do not resume an old or backgrounded one — two sessions on one task
caused the 2026-09-29 "exit code 1"), run `/model sonnet`, then paste one line:
> Read your memory, then execute docs/campaign/CAMPAIGN_DIRECTIVE.md Part S from the next open wave.

**What Sonnet does, every time:**
1. Read `AGENTS.md`, then this directive Parts A, C, D, S, then the wave you are running in Part F. Do not read Part G every turn; read it at each wave's end.
2. Find the next open wave: the first `docs/campaign/checkpoints/W<n>.md` that is missing or not marked `COMPLETE`. Resume from its last finished step.
3. Pre-flight (3 commands, results in the checkpoint): other agents running (`ps aux | grep -E 'claude|opencode' | grep -v grep`),
   `tail -30 DISPATCH_LOG.md`, and `git status --short | head -40`. If another agent is editing your wave's files, stop and tell the boss.
4. Dispatch the wave's subagents as written in Part F: shared context block first, `model: "sonnet"`, ≤5 in flight.
5. Compose deliverables yourself from reports. Verdict verifies before anything counts. Fix loop max 2 rounds.
6. After each batch update `docs/campaign/checkpoints/W<n>.md` (steps done, files written, open issues). Append one entry to `DISPATCH_LOG.md` per wave.
7. At the wave's end, tick the Part G0 crosswalk rows the wave closed (only with reproducing evidence) and report to the boss in ≤10 lines:
   what is done, what is open, decisions needed. Then continue to the next wave unless the boss said stop or a U-decision blocks it.

**Wave dispatch lines** (the boss can paste one of these to force a specific wave):
- `Execute CAMPAIGN_DIRECTIVE Part F Wave 1 (meeting-gate) per Part S.`
- `Execute CAMPAIGN_DIRECTIVE Part F Wave 2 (sampling) per Part S.`
- `Execute CAMPAIGN_DIRECTIVE Part F Wave 3 (skill stack) per Part S.`
- `Execute CAMPAIGN_DIRECTIVE Part F Wave 4 (research corpus index) per Part S.`
- `Execute CAMPAIGN_DIRECTIVE Part F Wave 5 (repo map + drift fixes) per Part S.`

**Context hygiene:** read in slices; never `cat` a big file or print huge tool output; keep the session under ~250K tokens — the 2026-09-29 planner
session reached ~390K. If context grows large, write the checkpoint, tell the boss, and continue in a fresh session with the same paste line.

### Boss decisions pending (batched; each has a recommendation)
| # | Decision | Recommendation |
|---|---|---|
| U1 | Which Wednesday did the lead mean ("after next Wednesday")? Fix the dates everywhere. | Meeting Wed 2026-09-30 stands; treat the lead-joins/W5-freeze date as UNKNOWN and ask Vinay tomorrow |
| U2 | Real hackathon submission deadline (Oct 4? Oct 15? qualifiers 30/09?) | Boss confirms from the official page or organiser message; Wave 1 records it |
| U3 | The untracked `src/` QLoRA/GRPO tree written by the OpenCode agents | Leave it unrun and untracked until Vinay picks the W6 path; if the path is wrap-only, archive it |
| U4 | Option A (wrap + QLoRA kok+pa) vs Option D (wrap + router + restoration + Sarvam subsidy); Qwen2.5-VL-3B vs GLM-OCR 0.9B | Present both to Vinay with 1A's evidence; decide at the meeting |
| U5 | Score the 56 additions and regenerate the LOCKED `sheet.csv`; re-draw kok/pa across more PDFs | Yes, after the meeting — not tonight |

---

## PART G0 — STATUS CROSSWALK (CO-001 … CO-096 → status → wave)
Tick only with reproducing evidence. **DONE** = closed on disk · **STANDING** = a rule every agent obeys, never "done" · **SUPERSEDED** = replaced by Part B.

| COs | Theme | Status | Where |
|---|---|---|---|
| 001, 069 | old folder; `Untitled` | DONE | A7 |
| 002, 004, 006–019, 066, 070 | cleanup, duplicates, md consolidation | DONE-PARTIAL (24h cleanup) — remaining gaps: link-check and per-file reasons | W5 |
| 005, 072 | "50,000+ / 10,000+ files" | SUPERSEDED — real scale ~29,500 working files (v4 Part A) | — |
| 067 | a reason for every file | OPEN — `AUDIT_REPORT.md` is directory-level | W5 |
| 003, 025, 068 | South 4 separate; one order, one place | OPEN | W1 (1B table) + W2 (`manifest_22.json`) |
| 020, 021 | 100/lang, 1,800 target | SUPERSEDED by C4 → 100 × 22 | W2 |
| 022–024 | varied pages; no first-page / one-paper shortcuts | PARTIAL — pair tier disproven (A5); PDF-tier concentration real | W2 |
| 026–029, 081 | Verdict autonomy, counters, council | STANDING — Part D | all |
| 030, 031, 063 | one-line prompts; no repeats; no "what next" | STANDING — R0.9, R0.10, Part S | all |
| 032, 033, 065, 080 | persist memory; don't forget assigned work | STANDING — memory + checkpoints + this file | all |
| 034, 078 | orchestrator does not labour | STANDING — Opus plans, Sonnet leads, subagents labour | all |
| 035–042, 060 | 3 agents, lanes, parallel, alignment | STANDING — Part D; bounded parallel waves (C2) | all |
| 043, 064 | no training yet | STANDING — see U3 (`src/` tree) | — |
| 044, 062 | past work is gold; forward-only | STANDING — R0.7 | all |
| 045, 049–052, 082, 084, 087, 088, 092 | fresh, deep, hidden-frontier research | OPEN | W1 (1D, 1E) + W4 |
| 046–048, 056, 057 | paper quotas | SUPERSEDED by C3 | — |
| 071 | 10–15 subagents for 24h | SUPERSEDED by C2 | — |
| 053–055, 059 | all-agent call; architecture others would steal; Level 7 held | OPEN — gated | W5 (D09) |
| 058 | verdicts/rankings on research | OPEN | W1 (1E) + W4 |
| 061 | beat Sarvam and lead | OPEN — honest framing C9 | W1 |
| 073, 074 | no vibe coding; full potential | STANDING — R0.3, R0.4 | all |
| 075–077, 094 | skills map; LAYA vs JEV; use every tool | OPEN | W3 |
| 079 | cycle: report → read → improve → cycle | STANDING — fix loop + checkpoints | all |
| 083 | use the PPTX and the meeting deeply | OPEN | W1 (1C) |
| 085, 093 | recon URLs | OPEN — precursors exist; live re-verify | W1 (1D) |
| 086 | no fake claims | STANDING — C9 is its first application | all |
| 089–091 | baseline vs Vinay's plan; overpower their side | OPEN | W1 (1A, 1H) |
| 090 | "structurally overconfident, then prove it" | SUPERSEDED by C9 — prove, then claim | — |
| 095, 096 | highest level; mind everything | STANDING | all |

---

## PART G — CONCERN REGISTER CO-001 … CO-096 (VERBATIM, NO DROPS)

Transcribed unaltered from `uni` v3 Parts 18–19. `BOSS_CONCERNS.md` carries 81 items in its own numbering; **this is the canonical CO-numbered register.** Every agent reads it every turn (T3.2). Mark `[DONE]` only when verifiably fixed on disk — not merely attempted. A repeated concern is a memory-system bug: fix the system, not just the symptom (T3.3).

**Already closed by the 2026-09-29 cleanup (verified on disk, Part A):** CO-001, CO-069.
**Superseded by Part B:** CO-020/CO-021 (target is now 100 × 22 = 2,200 — see C4) · CO-046/CO-047/CO-048/CO-056/CO-057 (no paper quota — see C3) · CO-071/CO-072 (bounded waves, not 24h — see C2).

```text

CO-001  Why does an "old" folder still exist at level 2? Remove it.
CO-002  Why keep unnecessary folders/files? Keep only the new, merged.
CO-003  South languages kept separate as "old" — merge into new or run
        them fresh in the same flow.
CO-004  If old and new have no code change, merge/delete old — never
        keep misleading parallel versions.
CO-005  Full re-scan of the entire project — 50,000+ files.
CO-006  Check every file's purpose: many variants exist.
CO-007  Many duplicate files exist — find and merge them.
CO-008  Many unnecessary files exist — find and delete (carefully).
CO-009  Files not following the intended order/hierarchy — fix.
CO-010  Misleading files/names/flows exist — find and fix all.
CO-011  Use many sub-agents for the audit; link-check everything.
CO-012  Clean all hybrid-concern md files completely.
CO-013  Merge duplicate md files; complete all md consolidation.
CO-014  Verify linking/flow/hierarchy across the whole repo.
CO-015  Repo contains waste-of-space files — deep review and delete.
CO-016  Every file, even old ones, gets detail+value assessment.
CO-017  Don't delete foolishly — deliberate verdicts only.
CO-018  Many trash md/json/script files — sub-agent read & score.
CO-019  Variant and unlinked files exist — merge/remove.
CO-020  100 samples per language required; why only 1200–1300 total?
CO-021  18 languages × 100 = 1800 minimum target.
CO-022  If linear extraction insufficient, source varied pages from
        existing PDFs/papers properly.
CO-023  FORBIDDEN: taking just the first page of one paper per file.
CO-024  FORBIDDEN: one-paper-per-file shortcuts; verify sample
        representativeness and logic.
CO-025  The 4 South languages: merge into one flow or rerun under the
        same standard — delete old versions.
CO-026  Verdict agent keeps asking "what to do" — fix via protocol.
CO-027  Upgrade Verdict's role: autonomy + nerve to counter the boss.
CO-028  Adopt Verdict's suggestions as recommendations to apply.
CO-029  Maximize project strength using all agent suggestions.
CO-030  Give one-line prompts only; detail lives in md files.
CO-031  Don't repeat md-file content inside prompts.
CO-032  Recall ALL 50+ concerns from this session; store them — don't
        rely on temporary memory.
CO-033  Do the previously-assigned parallel work — check it, don't
        forget it.
CO-034  Orchestrator dispatches + monitors; does NOT do the labor.
CO-035  Assign new agents only where work is unowned; else align with
        existing lanes.
CO-036  Setup the environment clearly so agents don't confuse lanes.
CO-037  Fix the flow/automation so improvement requests stop coming
        back as our fault.
CO-038  Run all 3 agents SIMULTANEOUSLY as multi-agent with sub-agents.
CO-039  Names: Agent 1 = Engine, Agent 2 = Verdict, Agent 3 = Miss.
CO-040  Maximize parallel work: research, checking, engines, all.
CO-041  Align hybrid-concern agent protocol with this structure.
CO-042  Meet/align all agents toward the 10-day hackathon goal.
CO-043  Model training not started — we are in data phase; don't rush.
CO-044  Past done work is 100% gold — maintain that standard.
CO-045  Plan dense new research where plans faded (pptx faded/pale) —
        fresh research for real.
CO-046  Research must be dense, complete, high-level — 1000+ papers.
CO-047  48-hour continuous agent research runs.
CO-048  Research volume = ~2 months human work, done via multi-agent.
CO-049  Current-era agentic AI papers only — live frontier work.
CO-050  Cover: OCR, Indic, RVL, NVIDIA, Jaisa, layout, Obsidian-class
        memory, Kimi/Claude/Hermes-class agents, top repos.
CO-051  Specialized research threads per sub-domain, ranked+verified.
CO-052  Collab/merge/integrate all research, then proceed.
CO-053  All-agents call to synthesize the ultimate settled architecture.
CO-054  Architecture so strong others would try to steal it.
CO-055  Integrate new methods + new architecture fully after planning.
CO-056  Only ~1% done — 10X the research effort ahead.
CO-057  Literally 5000+ papers, case studies, method PDFs, concepts.
CO-058  Verdicts/rankings/models on all research artifacts.
CO-059  Hold the last level (Level 7); focus Levels 1–2 now.
CO-060  Divide/parallelize levels across agents for more detail.
CO-061  Complete all levels 1,2,3... in order — beat Sarvam and lead.
CO-062  No looking back; forward-only, perfect execution.
CO-063  Don't ask the boss "what next" — the plan is this document.
CO-064  10-day hackathon — model training not started; much remains.

─── NEW CONCERN REGISTER (CO-065 … CO-096) ───

CO-065  Don't confuse things once again — update memory first.
CO-066  Many md files: first compact and merge, remove all duplicates,
        keep each and every file clearly and brutally assessed.
CO-067  Need a REASON WHY each file exists — per file, not per folder.
CO-068  Still seeing South-language outputs separate and others separate
        — need ALL in same order, same place, same hierarchy; currently
        clumsy; fix it.
CO-069  /Users/srujansai/Desktop/South/Untitled — merge its details/
        concerns into the repo where they belong, then DELETE it.
CO-070  Complete md cleanup after merging, level by level.
CO-071  Many severe tasks — use 10–15 sub-agents in parallel + 4–5
        monitoring agents; clean deep-dive, complete all.
CO-072  First reorganize ALL 10,000+ files; 24 hours authorized, no
        problem — take the time.
CO-073  NOT vibe coding — reasoned cleaning/merging/deletion per file;
        we are doing multi-agent orchestration agentic AI.
CO-074  Use FULL potential — no self-limiting; read each and every file.
CO-075  Boss unable to see why/where all skills are used (Claude,
        OpenCode, everything installed) — map every skill to its use.
CO-076  Decide LAYA vs JEV — boss believes LAYA is almost better and
        free → LAYA is best; verify and deploy; also check JEV, ECC,
        GrapyThoy, and all others.
CO-077  Research LAYA/JEV repos, concepts — they could serve as a
        classifier or some layer in our pipeline; run in parallel.
CO-078  If you can't cover all work: do only the main work yourself and
        assign the other paths in DISPATCH_LOG — boss will assign them;
        meanwhile you do the higher work.
CO-079  Cycle-graph workflow for the next 24 hours: they report → you
        read → delete/merge/improve → cycle again; make it clean,
        complete, improved, with better implementation plans — all
        cycling and graphing toward ultimate.
CO-080  Update everything into repo md memory so it can be cold-read
        anytime.
CO-081  Check clearly all previous md files, audit details, every md
        file, every concern — deliberate like a council.
CO-082  Study other best-in-class methods/methodologies and make this
        whole process eternal.
CO-083  Meeting details: the PPTX and all details initially received
        from HIM — he said to read and implement these strategies and
        ideas — use them deeply.
CO-084  Use high-level current latest agentic-AI strategies for deep
        research on the current live market.
CO-085  Recon: https://lnkd.in/p/eFzz2Dtb ,
        https://huggingface.co/datasets/sarvamai/indic-ocr-bench ,
        https://www.sarvam.ai/blogs/sarvam-vision-2-1 — and more.
CO-086  No fake claims — we know the real situation; merging best
        strategies and assuming we beat them is nonsense; there is some
        edge/tactic to CRACK — the only way to beat or compete; this
        wins support, funding, the winning lane.
CO-087  Main research lies in model strategies/techniques — most
        important: latest research PLUS beneath-the-ground work —
        submerged, misleading, fallen, understated latest/new findings;
        overlooked basic integrations; unseen combinations.
CO-088  Find how JEV and LAYA crossed into relevance from frontier
        models — that pattern of real integration is what lets us cross
        and beat everyone; plan at that level.
CO-089  First benchmark/analysis: baseline against VINAY'S plan — we
        must cross his plan to even cross Sarvam and the entire India
        model field.
CO-090  Confirm: our current plan is better than his BECAUSE we use
        agentic AI — be structurally overconfident, then PROVE it.
CO-091  Their side has settled their plan toward a million-dollar
        funding hackathon — we must overpower them.
CO-092  Deep research starts now — first block: next 2 hours.
CO-093  Also check: https://lnkd.in/p/ewsNXkTs , https://www.gnani.ai/ ,
        huggingface.co/gnani/gnani-evon-v3.3-30B-A3B , indic-ocr-bench ,
        https://consensus.app/ — check all clearly and do the work.
CO-094  Use all skills, all plugins, all repos we could use — full
        potential.
CO-095  "I am staking my entire life on this project" — do everything
        at the highest level.
CO-096  Mind everything above and execute — carefully, high-level.

```

---

## FINAL WORD (the boss's own, preserved)

> You are authorized. You are expected to counter when wrong — even me.
> You are expected to decide what is yours to decide. You are expected to
> log everything, verify everything, and forget nothing.
>
> "U are the boss, man. Do all clearly, perfectly, originally, in the
> correct way. No old, no duplicate, no misleading, no confusing.
> Use full potential — no self-limiting. I am staking my entire life
> on this project."
