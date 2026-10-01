---
name: proto-99-concern-crosswalk
description: Added 2026-09-30 — MASTER crosswalk proving every boss concern has an owner: CO-001…096, C1–C17 (77 turns of 09-27/28), uni task items, chat meta-concerns M1–M8, BOSS_CONCERNS #1–81 → status (disk-checked by the Opus monitor 2026-09-30) → protocol file(s) that close it
metadata:
  type: project
  modified: 2026-09-29T21:56:20.906Z
---

# PROTO-99 — CONCERN → STATUS → PROTOCOL CROSSWALK (read with proto-66; the register in BOSS_CONCERNS.md is rebuilt from this)

Statuses (monitor, 2026-09-30 ~04:00): **OPEN** · **PARTIAL** · **DONE** (reproduced on disk) · **STANDING** (a rule; never "done") · **SUPERSEDED** (by a settled conflict C#) · **BLOCKED** (boss decision U#) ·
**OVERCLAIMED** (marked done somewhere; not true on disk). Protocol numbers = memory files `proto-NN-*`.

## §0 — CONCERN THEMES K-01…K-30 (merged 2026-09-30 night by the planner; every older ID below maps into exactly one theme)
How to read this:
- Status is taken from the latest disk evidence the planner read (W4.md, DISPATCH_LOG.md, NEXT.md at ~22:35 IST, 2026-09-30).
- Each theme has a **verify** command. The owner re-runs it and pastes the output into W4.md before changing the status.
- Status words: DONE-VERIFIED · PARTIAL · OPEN · BLOCKED (U#/boss) · STANDING (a rule, never "done") · PARKED (proto-98 cleanup; waits for "resume cleanup").
- Owner = Agent 1 (Engine) · Agent 2 (Verdict + repair) · Agent 3 (Miss/builder) · planner · boss.
- The older IDs (CO-###, C#, T#, R0.#, M#, #n, HL#, HC#, H#, S10/S29, EG#) keep their full rows in Part 1 / §A–§I (append-only history).

- **K-01 Win: beat Sarvam Vision 2.1 and every competitor.**
  - Sources: CO-061, CO-091, #21, E14.2, S4, EG7.
  - Status: OPEN.
    - Targets are Sarvam 87.39 on its own bench (weak cells: sat 53.91, ks 54.82, or 80.01, old scans) and Bodhan 84.94.
    - No number of ours exists yet on the same split.
  - Rule (proto-104 R-12): a win claim needs the published split + scorer AND a win on an independent set.
  - Verify: `grep -n "87.39\|84.94" docs/campaign/BODHAN_BASELINE.md docs/campaign/BENCHMARK_22.md`
  - Owner: Agent 1 (X, D1) → Agent 2 (S5).
- **K-02 Portable product (Vaultstack): runs anywhere; MLX is only a Mac accelerator.**
  - Sources: R-13, R-14, U35, B-11, boss 21:3x.
  - Status: PARTIAL.
    - `product/` exists (schema, cli, pdf_writer, script_id, tesseract + bodhan recognisers).
    - Missing: `product/requirements.txt`, the Dockerfile, and a parity number between the official PyTorch weights and the MLX port.
  - Verify: `ls product/ product/requirements.txt product/Dockerfile 2>&1`
  - Owner: Agent 3 (P) → Agent 1 (D1 parity, D4).
- **K-03 Handwriting and the official test set.**
  - Sources: EG2, EG3, U13, B-12, RQ-2, RQ-10, §H.
  - Status: PARTIAL.
    - 5,344 word crops, 296–300 px tall.
    - The planner viewed 3: handwritten Bengali.
    - H1 (Tesseract on 70 samples) reads 35.7% as "Devanagari" and 55.7% as unknown. This does not agree with the planner's viewing, so the script mix is still UNKNOWN.
    - `Bodo/gu` is labelled Gujarati handwriting, but only 4,645 of ~116k images are on disk.
    - H2, H3 and H4 are open.
  - Verify: `python3 -c "import json;print(json.load(open('docs/campaign/H1_TEST_PROFILE.json')).keys())"`
  - Owner: Agent 1 (H1 redo with a vision check, H3) · Agent 2 (H2).
- **K-04 The lead's method (Sep 29 L1–L14): draft plan → multi-LLM evaluation by the process → 15–20 min session → execute.**
  - Sources: S29-a..j, D1–D7, A1–A7, B-16, B-17, CO-083.
  - Status: PARTIAL.
    - The Plan v3 draft (step G) is not written.
    - Gate 2.5 (the multi-LLM evaluation) has not been run for v3.
    - The session with Vinay has not happened.
  - Verify: `grep -c '```mermaid' docs/campaign/DRAFT_RESEARCH_PLAN.md docs/PLAN.md`
  - Owner: Agent 2 (G, then Gate 2.5) → boss (session).
- **K-05 ONE 22-language benchmark, with South merged in.**
  - Sources: CO-003, CO-025, CO-068, C4, M8, H13, #3, #12, #68, T2.2, T6.4, U10, U11.
  - Status: PARTIAL.
    - S2 done: `manifest_v2.json` = 1,683 items, South 4 × 100 from the Sarvam bench (R-7).
    - S4: tesseract_indic only (400 packs, weighted CER 0.1450); the other 7 local engines wait on A4; Bodhan waits on HF access.
    - S5 and S6 are open.
  - Verify: `python3 - <<'E'` / `import json,collections;d=json.load(open('level2/benchmark/manifest_v2.json'));it=d['items'] if isinstance(d,dict) else d;print(len(it),collections.Counter(i.get('language') or i.get('lang') for i in it))` / `E`
  - Owner: Agent 1 (S4) → Agent 2 (S3, S5, S6).
- **K-06 100 INDEPENDENT samples per language.**
  - Sources: CO-020…024, C1, C16, T6.1–T6.3, #9–#11, #49, #50.
  - Status: PARTIAL.
    - 7 languages are short in v2: as 19, sat 20, mni 20, gu 24, doi 27, brx 67, or 69.
    - kok and pa draw from 2 PDFs each.
    - The honest-n rule applies: never relax a gate.
  - Verify: the same manifest_v2 Counter as K-05.
  - Owner: Agent 2 (report honest n) · boss (re-source decision).
- **K-07 Evidence and honesty: no fake claims.**
  - Sources: CO-086, CO-073, R0.3, R0.11, C10.1, HL1, HVII.8, boss-rules.
  - Status: STANDING.
  - Evidence tags and "done = reproduced" are in proto-01 §B and §C.
  - Verify: `grep -c "DONE-VERIFIED" BOSS_CONCERNS.md` (Part 1 has 1 DONE-VERIFIED vs 35 bare DONE per proto-66 check D2).
  - Owner: all agents; Agent 2 audits.
- **K-08 Leakage and fair evaluation.**
  - Sources: EG8, R-12, proto-62, C1-3, C3-6, U6, C12.
  - Status: OPEN, with two new risks:
    - (a) The South benchmark items ARE Sarvam-bench items. The same blocks sit inside step X's 6,909, so they must never be counted twice or pooled with the `official_pdf` tier.
    - (b) Sarvam's own bench is home ground for Sarvam and possibly training exposure. The Sep 29 tier table shows local engines only "lead" on PDF-layer GT.
  - Verify: `grep -n "sarvam_bench\|tier" docs/campaign/BENCHMARK_22.md | head`
  - Owner: Agent 2 (S5 tiering, X labels).
- **K-09 Incident safety (proto-102): the untracked scores folder was deleted.**
  - Sources: H14, rules 17–21, U37.
  - Status: PARTIAL.
    - A0, A1 (claims), A2 and A3 PASS.
    - A4 CONDITIONAL: the approved erratum is not yet applied (R-2/R-3).
    - A5 and A6 are open; A7 is parked until the boss says "go".
    - A1's bundle was judged inadequate; `benchmark/pages` has since been bundled.
    - A second writer wrote into `level2/unified/` during the repair.
  - Verify: `grep -c probe22 level2/benchmark/pipeline/run_probe.py; ls level2/benchmark/scores/mcnemar_full_matrix.json`
  - Owner: Agent 2.
- **K-10 Repo cleanliness and hierarchy.**
  - Sources: CO-001…019, CO-066…072, C9, T1.x, T2.x, H3, H6–H8, H10, #1–#8, #66–#71.
  - Status: PARKED (proto-98 master; resume only on the boss's "resume cleanup").
  - Exception done tonight: the doc hierarchy (AGENTS.md, docs/INDEX.md, README.md), K-14.
  - Verify: `ls *.md | wc -l`
  - Owner: Agent 3, when unparked.
- **K-11 Research: harvest it and use it.**
  - Sources: H1, H2, CO-045…058, R11.x, proto-95, proto-97, proto-105.
  - Status: PARTIAL.
    - `RESEARCH_DECISIONS.md` has RF-01…RF-24.
    - The Consensus results are stored but not processed (proto-105: target ≥20 C-rows).
    - The 88 `docs/research` md files were never harvested.
    - B-01, B-02 and B-12 prep analyses exist.
  - Verify: `grep -c "^| *RF-\|C[123]-[0-9]" docs/campaign/RESEARCH_DECISIONS.md`
  - Owner: Agent 2 (proto-105 first, then the un-parked harvest).
- **K-12 Tools: graphify, ECC, Laya, skills.**
  - Sources: CO-075…077, CO-088, CO-094, M4, H4, H9, EG9, U26, U30, U31.
  - Status: PARTIAL.
    - graphify 0.9.65 is installed, but the graph is the 14:34 version and `graphify update .` is still owed.
    - ECC is in use.
    - Laya is NOT used in the pipeline; its file-triage trial is parked.
  - Verify: `ls -la graphify-out/graph.json`
  - Owner: Agent 2 (graph update after LAYOUT FROZEN).
- **K-13 Agent process.**
  - Sources: CO-026…040, CO-078, C5, C8, C11–C13, T7.x, T8.x, M1, H5, H12, #13–#20.
  - Status: STANDING.
  - The rules:
    - three agents only;
    - one-line paste lines;
    - the planner does no labour and runs no subagents;
    - every writer registers in DISPATCH_LOG;
    - no "what next".
  - Verify: `tail -5 DISPATCH_LOG.md`
  - Owner: all.
- **K-14 Concerns and memory stored, cold-readable, one connected doc hierarchy.**
  - Sources: CO-032, CO-065, CO-080, C14, C17, T3.x, M2, M3, M7, HC14.12, H10, boss 22:30 "AGENTS.md is total trash… hierarchy not connected".
  - Status: PARTIAL. Task B, Task C and the MEMORY rebuild were written tonight. The rewrites of AGENTS.md, INDEX.md and README.md are drafted; Agent 2 applies them.
  - Verify: `head -20 AGENTS.md`
  - Owner: planner (memory) → Agent 2 (apply + graphify).
- **K-15 Meeting truth and the PPT baseline.**
  - Sources: CO-083, CO-089, C10.3, H15, proto-103 M1–M10, proto-75, L11.
  - Status: PARTIAL.
    - The meeting table is in proto-103 §0.
    - The M1–M10 attribution fixes are unverified in the repo docs.
    - Whether `VINAY_PLAN_BASELINE.md` exists is unknown.
  - Verify: `grep -rn "novel backbone\|AI itself is enough\|H44\|Decisions Locked" docs/research/MEETING_2026-09-29_STRUCTURED.md docs/campaign/MENTOR_PLAYBOOK.md VINAY_MEETING_PACKET.md`
  - Owner: Agent 2.
- **K-16 Levels in order; no training before validation.**
  - Sources: CO-059, CO-060, CO-064, CO-043, P12.x, E14.1, F13.x, S29-RL, B-17.
  - Status: STANDING. The Gate 2.5 red line still holds: no LoRA/RL before the Plan v3 evaluation and the session with Vinay.
  - Verify: `ls docs/campaign/MULTI_LLM_EVAL.md; grep -n "Plan v3" docs/campaign/MULTI_LLM_EVAL.md`
  - Owner: boss gate.
- **K-17 Licences.**
  - Sources: EG4, U14, U27, U28, RQ-9, proto-83.
  - Status: PARTIAL.
    - surya is evaluation-only (OpenRAIL-M §2(c)).
    - Bodhan as a §3.2 internal component; hosting needs written approval.
    - 600K-KS is on HOLD (research-only licence embedded).
    - sat/mni tessdata: Apache-2.0, CLEARED.
    - The weight licence for the EasyOCR `.pth` is still open.
  - Verify: `grep -n "CLEARED\|NOT CLEARED\|CONDITIONAL" docs/campaign/checkpoints/W4_reports/RQ9_licences.md | head`
  - Owner: Agent 2.
- **K-18 Sealed dirs, locked files, past work.**
  - Sources: HL4, HL5, R0.6, R0.7, CO-017, CO-044, #36–#38.
  - Status: STANDING, with a caveat: the sealed set changed during the P4 run and the incident (`level2/reports` and `level2/models` were removed into `_archive/bundles/2026-09-30_south_v1.tar.gz`). The current sealed list is in proto-01 §A (rewritten tonight).
  - Verify: `for d in level2/out Datasets/akshardrishti_official arc_level_1; do echo $d $(find $d -type f | wc -l); done`
  - Owner: all; Agent 2 checks.
- **K-19 GT defects register.**
  - Sources: proto-65 G1–G9, HC14.1, the South legacy-font finding, the 26-page Sep-16 finding.
  - Status: OPEN. `docs/campaign/GT_DEFECTS.md` does not exist; step Q must precede D2.
  - Verify: `ls docs/campaign/GT_DEFECTS.md`
  - Owner: Agent 2.
- **K-20 Empty-output patterns: bug or honest-empty.**
  - Sources: proto-82, HL8, HVII.2, HVII.7, F40, F47, F48.
  - Status: OPEN.
    - paddle brx/doi is a mapping bug.
    - surya sa is image or model side.
    - Both must be fixed before the X coverage matrix.
  - Verify: `ls docs/campaign/EMPTY_OUTPUT_DIAGNOSIS.md`
  - Owner: Agent 1.
- **K-21 Metric set.**
  - Sources: proto-80, EG1, HL2, HVII.3, HC14.3, HC14.5, HC14.6, C3-6.
  - Status: OPEN.
    - Needed: CER mean + median + bootstrap CI, WER, S/D/I, catastrophic-failure rate (CER > 0.5), an NFC statement, s/page.
    - The bench's own headline is Word Accuracy = 100 × (1 − WER) after `--normalize`.
  - Verify: `ls docs/campaign/RUBRIC_REPORT.md level2/unified/rubric_report.py`
  - Owner: Agent 1 builds, Agent 2 verifies.
- **K-22 Submission readiness.**
  - Sources: proto-78, EG3, U2, U35, B-11, RQ-1.
  - Status: PARTIAL.
    - The official metric, format and deadline are all UNKNOWN (RQ-1).
    - The jury scores the product.
    - No 50-image dry run yet.
  - Verify: `ls docs/campaign/SUBMISSION_DRYRUN.md`
  - Owner: Agent 1 (D4), Agent 3 (product).
- **K-23 The boss can explain everything.**
  - Sources: proto-85, HVII.5, HC14.10, HL11b.
  - Status: PARTIAL. `BOSS_EXPLAINER.md` exists; the E–H question bank has not been asked.
  - Verify: `ls docs/campaign/BOSS_EXPLAINER.md`
  - Owner: Agent 2 (refresh after S5).
- **K-24 Other workstreams and concurrent writers.**
  - Sources: proto-76, CO-033, C15, T8.5, second-writer incident, the vajrAstra cloud session.
  - Status: OPEN.
    - Two sessions wrote into level2 during the repair.
    - The cloud planner session (vajrAstra) owns PR #12 (a reference only, R-6).
  - Verify: `ps aux | grep -E 'claude|opencode' | grep -v grep | wc -l`
  - Owner: planner monitors.
- **K-25 Dates and deadlines.**
  - Sources: U1, U2, C7, F17, #53–#56, RQ-1.
  - Status: OPEN.
    - No official deadline exists; 10 of 12 official timeline rows are TBD.
    - Ask the organiser (gic.dibd@gmail.com), and only if Vinay agrees.
  - Verify: `grep -n "deadline" docs/campaign/checkpoints/W4_reports/RQ1_official_rules.md | head -3`
  - Owner: boss.
- **K-26 GPU.**
  - Sources: U33, S10-6, Vinay's answer 1.
  - Status: BLOCKED on SSH details (24 GB VRAM, arriving 2026-10-01).
  - Data moves by rsync, never GitHub. Keys go in env vars only.
  - Verify: the boss confirms receipt.
  - Owner: Agent 1 (GPU step).
- **K-27 Sarvam budget: ₹67 free credit, 12 approved South calls (R-8).**
  - Status: BLOCKER.
    - 12/12 jobs completed (≈₹6 spent).
    - None of the 12 predictions could be retrieved: the status response has no `download_url`. Agent 1 tried `/result`, `/output`, `/{id}`, `/download` and `/file`, but not `/download-url`.
  - The fix must come from the official docs or SDK and must not resubmit anything (no extra spend).
  - Verify: `python3 -c "import json;d=json.load(open('level2/benchmark/scores/south_sarvam_12_results.json'));print(sum(1 for r in (d if isinstance(d,list) else d.get('results',[])) if (r.get('pred') or r.get('prediction'))))"`
  - Owner: Agent 2 (investigate), Agent 1 (retrieve).
- **K-28 Concerns visible in the graph.**
  - Sources: C3, proto-77, M4.
  - Status: PARKED with the cleanup.
  - Verify: `grep -c "K-0" graphify-out/GRAPH_REPORT.md`
  - Owner: Agent 3, when unparked.
- **K-29 The Sep-16 correction owed to Vinay.**
  - The Sep-16 package scores 26 of the 126 CER pages against legacy-font GT, and South v1 is not comparable to the new benchmark.
  - Status: OPEN. Quote it only after Agent 2 reproduces it (in S5); it goes to Vinay only.
  - Verify: the vajrAstra reference `level2/research/STRATIFIED_BOOTSTRAP.md` (branch `claude/stoic-keller-xwovqu`) plus Agent 2's own reproduction.
  - Owner: Agent 2 → boss.
- **K-30 Time budget and speed.**
  - Sources: F52, #57–#59, P12.1, HC14.3.
  - Status: OPEN.
    - surya ≈ 24 s/page on this Mac, so ≈ 36 h for 5,344 images; rapidocr ≈ 0.4 s/page.
    - No single-machine latency table exists yet; the GPU step owns it.
  - Verify: `ls level2/benchmark/logs/RUN_STATE/ 2>&1`
  - Owner: Agent 1.

**Crosswalk rule:** every older concern ID maps to one theme through its source list above. A concern that fits no theme is a planning bug: add a theme and tell the boss.

---

## A. CO-001 … CO-096 (uni Parts 18–20, verbatim text in docs/campaign/CAMPAIGN_DIRECTIVE.md Part G)
| CO | Short | Status | Protocols |
|---|---|---|---|
| 001 | old folder at level 2 | PARTIAL — no dir named old, but old/new parallel trees remain | 70, 101 |
| 002 | keep only new, merged | OPEN | 95, 96, 70, 72, 74, 63 |
| 003 | South separate — merge or run fresh | OPEN (symlink view only) | 71, 70, 101 |
| 004 | old/new unchanged → merge/delete old | OVERCLAIMED ("models vs out KEEP BOTH") | 95, 96, 70, 63, 101 |
| 005 | full re-scan | PARTIAL (scale corrected; per-file missing) | 72 |
| 006 | every file's purpose | OPEN | 72 |
| 007 | duplicates | PARTIAL | 63, 72, 73 |
| 008 | unnecessary files | OPEN | 72, 74, 70 |
| 009 | order/hierarchy | OPEN | 70, 50 |
| 010 | misleading names/flows | OPEN | 72, 74, 73 |
| 011 | many subagents; link-check | OPEN | 72, 50 |
| 012 | clean hybrid-concern md | OPEN | 73 |
| 013 | merge duplicate md | PARTIAL | 95, 96, 73, 63 |
| 014 | verify linking/flow | OPEN | 50 |
| 015 | waste of space | OPEN | 72 (WASTE_OF_SPACE.md) |
| 016 | detail+value per file | OPEN | 72 |
| 017 | don't delete foolishly | STANDING | 01, 72 |
| 018 | trash md/json/scripts scored | OPEN | 72 |
| 019 | variant/unlinked files | OPEN | 72, 73 |
| 020 | 100/lang; why only 1,200–1,300 | PARTIAL (1,283 manifest / 1,227 scored of 2,200) | 20, 21, 71 |
| 021 | 18 × 100 = 1,800 | SUPERSEDED by C4 → 22 × 100 = 2,200 | 20, 21, 71 |
| 022 | varied pages from existing PDFs | PARTIAL | 21 |
| 023 | no first-page-only | PARTIAL (pair tier disproven; ur 34% page≤1) | 21 |
| 024 | no one-paper-per-file | PARTIAL (kok, pa: 2 PDFs each) | 21 |
| 025 | South: one flow or rerun; delete old | OPEN | 71, 70, 101 |
| 026 | Verdict keeps asking | STANDING | 79 |
| 027 | Verdict autonomy + nerve | STANDING | 79, 91 |
| 028 | adopt Verdict suggestions | STANDING | 79 |
| 029 | maximize using all suggestions | STANDING | 79, 17 |
| 030 | one-line prompts | STANDING | 00 (paste lines), 01 |
| 031 | don't repeat md in prompts | STANDING | 01 |
| 032 | recall all concerns; store | PARTIAL | 66, 99 |
| 033 | do previously assigned parallel work | OPEN | 76 |
| 034 | orchestrator dispatches, not labour | STANDING | 00, model-tiering |
| 035 | new agents only for unowned work | STANDING | 00, campaign-law |
| 036 | clear environment/lanes | PARTIAL | 60, 76 |
| 037 | fix the flow/automation | STANDING | 79 §2, 60 |
| 038 | 3 agents simultaneously | STANDING (bounded waves, C2) | 00 |
| 039 | names Engine/Verdict/Miss | STANDING | campaign-law |
| 040 | maximize parallel work | STANDING | 00 §2 |
| 041 | align hybrid-concern protocol | PARTIAL | 73, 66 |
| 042 | align all agents to the 10-day goal | STANDING | 00, 64 |
| 043 | training not started — don't rush | STANDING; conflict: untracked `src/` W6 build | U3 |
| 044 | past work is gold | STANDING | 01 |
| 045 | fresh dense research where plans faded | PARTIAL (Wave 1 research done) | 14, 15, 40 |
| 046–048 | 1,000+ papers / 48 h / 2 months | SUPERSEDED by C3 | 40 |
| 049 | current-era papers | STANDING | 15, 40 |
| 050 | cover OCR/Indic/RVL/NVIDIA/Jais/layout/memory/agents/repos | OPEN | 40 |
| 051 | specialised threads, ranked + verified | OPEN | 40 |
| 052 | integrate research, then proceed | OPEN | 40, 19 |
| 053 | all-agents architecture call | OPEN (gated) | 51 |
| 054 | architecture others would steal | OPEN | 51, 16 |
| 055 | integrate new methods fully | OPEN | 51 |
| 056–057 | 10× / 5,000+ papers | SUPERSEDED by C3 | — |
| 058 | verdicts/rankings on research | PARTIAL | 40, 16 |
| 059 | hold Level 7; Levels 1–2 now | STANDING | 51; Levels 1–2 = W2 + structure waves |
| 060 | divide levels across agents | STANDING | 00 |
| 061 | all levels in order; beat Sarvam | OPEN (honest framing C9) | 64, 62, 78 |
| 062 | forward-only | STANDING | 01 |
| 063 | don't ask "what next" | STANDING | 79 |
| 064 | 10-day hackathon; training not started | STANDING | — |
| 065 | update memory first | STANDING | 60, memory |
| 066 | compact/merge md; brutal per-file assessment | OPEN | 95, 96, 72, 73 |
| 067 | a reason for every file | OPEN | 72 |
| 068 | South outputs separate — one order/place/hierarchy | OPEN | 70, 71, 101 |
| 069 | Untitled ingest + delete | DONE (path absent; merged into FULL TECHNICAL BRIEFING Part III) | — |
| 070 | md cleanup level by level | OPEN | 73 |
| 071 | 10–15 subagents for 24 h | SUPERSEDED by C2 | — |
| 072 | reorganize all files | PARTIAL | 72, 70 |
| 073 | not vibe coding | STANDING | 01 |
| 074 | full potential; read every file | STANDING | 72 |
| 075 | map every skill to its use | OPEN | 30 |
| 076 | LAYA vs JEV — decide and deploy | OPEN | 31 |
| 077 | LAYA/JEV as a pipeline layer | OPEN | 31 |
| 078 | do main work; assign the rest in DISPATCH_LOG | STANDING | 00 |
| 079 | cycle-graph workflow | STANDING | 60, 91 |
| 080 | repo md memory, cold-readable | PARTIAL | 66, 50, `docs/campaign/protocols/` mirror |
| 081 | council deliberation | STANDING | 79 §3 |
| 082 | best methodologies; eternal process | PARTIAL | 79, 60 |
| 083 | PPTX + meeting details deeply | PARTIAL (1C done) | 13, 75 |
| 084 | latest agentic research strategies | PARTIAL | 15, 40 |
| 085 | recon URLs | DONE except LinkedIn (UNKNOWN) | 14 |
| 086 | no fake claims | STANDING | 01, 61, 62 |
| 087 | beneath-the-ground research | PARTIAL (4 candidates, 0 survived) | 15, 16, 40 |
| 088 | how JEV/LAYA crossed into relevance | OPEN | 31 step 6 |
| 089 | baseline against Vinay's plan | OPEN | 75 |
| 090 | overconfident, then prove | SUPERSEDED by C9 | — |
| 091 | overpower their plan | OPEN (Vinay is the team CEO: "cross his plan" = a better plan he adopts) | 75, 16, 19 |
| 092 | first 2-hour research block | DONE (Wave 1 research) | — |
| 093 | check Gnani/bench/Consensus/LinkedIn | DONE except LinkedIn (UNKNOWN) | 14 |
| 094 | use every skill/plugin/repo | OPEN | 30 |
| 095 | life-stakes standard | STANDING | all |
| 096 | mind everything | STANDING | 99 |

## B. C1–C17 (SESSION_DIRECTIVES_2026-09-28 §3 — 77 boss turns)
| C | Concern | Status | Protocols |
|---|---|---|---|
| C1 | 100 per language through ALL engines, one shot | OPEN (additions unscored; South different standard; 8 short langs) | 20, 21, 71, U5 |
| C2 | one big complete run, not 20+20+20 pieces | STANDING — data runs are one complete pass per language set (proto-71 phase B); bounded waves apply to docs/research only | 71 |
| C3 | all concerns visible in the graph | OPEN | 77 |
| C4 | each language handled properly, none skipped | OPEN | 12, 21, 71 |
| C5 | do ALL the work; act on everything pasted | STANDING | 18 (apply every spec) |
| C6 | everything linked; no silos | OPEN | 50, 70 |
| C7 | honest, complete report of what was done | STANDING | 79 §1, 66 |
| C8 | process Verdict findings; don't re-ask | STANDING | 79 |
| C9 | audit trash/variants/dupes; don't delete foolishly | OPEN | 72 |
| C10 | apply Verdict self-improvement plan | DONE (verify_engine_readiness.py, spot_check_engine.py, self_audit.py, engine_agent_contract.json exist in `level2/probe22/`) | re-verify in 72 |
| C11 | no meta-verdicts / redundant files; act | STANDING | 60 rule 4, 63 |
| C12 | prompts on disk; boss pastes one line | STANDING | 00 |
| C13 | orchestrator does not dispatch | STANDING (Opus never dispatches; the Sonnet lead dispatches when the boss says so) | model-tiering |
| C14 | memory loss — re-read everything | STANDING | memory, 66 |
| C15 | check both parallel tracks | OPEN | 76 |
| C16 | 100 INDEPENDENT pages per language | PARTIAL | 21 |
| C17 | save all concerns clearly | PARTIAL | 66, 99 |

## C. uni task items not already covered by a CO row
T1.3 per-file WHAT/WHY/WHERE/WHO/WORTH → 72 · T1.4 flags a–f → 72 · T1.5 waste list → 72 · T1.6 monitors re-check + link-check → 72 step 3 · T2.3 Untitled → DONE ·
T2.6 FINAL_REPO_MAP → 50 · T3.2 every agent reads the register every turn → 66 + proto-01 · T6.3 source + page-offset distribution per language → 21 ·
T7.2 (a–d, g) scripts → DONE (C10) · T7.2(e) briefing format → 79 §1 · T7.2(f) proactive fix-specs < 1 h → 79/91 · T7.4 prompt maintenance → 79 §2 · T7.5 council → 79 §3 ·
T8.2 DISPATCH_LOG before work starts → 76 standing rule · T8.5 other parallel workstreams → 76 · C10.2 recon → 14 · C10.3 Vinay baseline → 75 · C10.4 edge → 16 ·
R11.6 mentor PPTX implemented → 13, 75 · R11.7 Verdict ranks research → 40 · F13.1 call when corpus ≥80% and edge evidence-backed → 51 · E14.1 Levels 1–2 to gold → W2 + 70/71/72 ·
E14.2 complete the project → 78 (submission readiness) · P12.4 no half-done levels → 00 ordering.

## D. Chat meta-concerns M1–M8 (2026-09-29/30)
M1 Opus plans, Sonnet executes, never Opus subagents → model-tiering, 00 · M2 many deep protocols in memory → this proto set + mirror · M3 read everything important before planning →
00 §0 read order, 72 · M4 use graphify → 77, 73 · M5 plan to 100% completion → 00 step table incl. 78 · M6 monitor agents; add protocols → 60, `MONITOR_<date>.md` ·
M7 all concerns considered → 99 + 66 · M8 level2 old/unwanted/misleading; old South out vs new out → 70, 71, 72.

## E. BOSS_CONCERNS.md #1–81 (current file)
#1–8 cleanup → 72, 70, 73, 66 · #9–12 sampling → 20, 21, 71 · #13–16 protocol upgrades → 79 · #17–20 dispatch → 76, 00 · #21–23 end goal → 64, 78 · #24–35 engine/state items (historical;
re-verify only) · #36–45 locks and laws → STANDING (#36/#37 seals may be lifted only by U10) · #46–52 deliverables → OVERCLAIMED items listed in proto-66 · #53–65 W5/Vinay meeting → 64 ·
#66–81 cleanup diary → OVERCLAIMED items in proto-66 (0 duplicates, South unified, KEEP BOTH, R3 deferred).

## How agents use this file
Before starting any step, find the concerns it closes here; after finishing, update the matching rows in `BOSS_CONCERNS.md` (proto-66) with evidence. A concern that has no protocol row
here is a planning bug — add a protocol (proto-79 §2) and tell the boss.

Related: [[proto-66-concern-register-rebuild]], [[proto-00-runbook]], [[boss-standard]]

## F. ADDED 2026-09-30 (second pass) — South-era operator law and concerns (level2/ULTIMATE_HYBRID_CONCERN.md, Sep 12–14, "never to be lost")
| ID | Concern / law (short) | Status (monitor 2026-09-30) | Protocols |
|---|---|---|---|
| HL1 | disk truth only; re-verify cited numbers | STANDING | 01, 91 |
| HL2 | ONE WRITER ONE TRUTH — patch the writer, never the output | OPEN — `sheet.csv` has no writer on disk | 61, 80 |
| HL3 | 4-page gate before touching the full set | STANDING — applies to every engine fix | 82 |
| HL4/HL5 | archive never delete · datasets immutable, reruns versioned (out_archive/<eng>_vN) | STANDING — HL4 narrowed by U29 (2026-09-30): delete only exact twins / conversions / git-held / empties; everything else bundled | 70, 82, 96 |
| HL6 | family = 1 vote; "9 engines, 7 independent families", never "10 independent" | OVERCLAIMED — probe docs say "10 independent" | 73, 86 |
| HL7 | no training in L2, no invented GT, no spell-correction (raw is the benchmark) | STANDING | 01 |
| HL8 | open policy — lang tag is an ID, never a content constraint | OPEN — engines are mapped by language code; brx/doi/sa empty-output bugs | 82 |
| HL9/HL9b | consensus law · freshness stamped | STANDING | 80 |
| HL10/HL10b | agents never edit shared pipeline files · external plans audited against disk first | STANDING (seal lifted only for U10 move) | 70, 91 |
| HL11 | one fact one file | OPEN | 73, 63, 84 |
| HL11b | Group = counts · David = receipts · Vinay = five lines | OPEN | 85 |
| HL12 | ≥5 same-signature failures → stop spawns · D12: no new scope inside T-4 of a demo | STANDING — broken 2026-09-30 03:30 (W2 started before the meeting) | 64, 60 |
| HC14.1 | GT ceiling: CER basis only 126/400 South pages | OPEN | 71, 65 |
| HC14.2 | Malayalam weakest, small-n caveat must travel | OPEN | 71, 86 |
| HC14.3 | latency asymmetry; full timing sweep | OPEN | 80 |
| HC14.5 | regression alarm unproven | OPEN | 80 (writer with PASS/FAIL) |
| HC14.6 | stratified (script × density) bootstrap | OPEN | 80 |
| HC14.7 | always say "9 engines, 7 independent families" | OVERCLAIMED | 73, 86 |
| HC14.9 | archive INDEX (one line per item) | OPEN | 96, 50, 72 |
| HC14.10 | ~150-question bank, categories E–H never asked | OPEN | 85 |
| HC14.11 | empty subagent twice → run inline | STANDING | 79 §2 |
| HC14.12 | concern file > ~200 lines → consolidate | OPEN (BOSS_CONCERNS 517 lines) | 66 |
| HVII.1 | "Max raw output" = L2 success metric | STANDING | 80 (abstention rate) |
| HVII.2 | "Useless ⇒ engine is wrong ⇒ fix ⇒ re-run; keep old in json_vN" | OPEN | 82 |
| HVII.3 | no hand-written reports; one writer; freshness or fiction | OPEN | 61, 80 |
| HVII.4 | parallel lanes, max ~7 subagents, never stack work | STANDING (≤5 in flight) | 00 |
| HVII.5 | operator explains everything as if he owns it | OPEN | 85 |
| HVII.6 | work like a top startup; one-push execution | STANDING | 00 |
| HVII.7 | verify EVERY output of EVERY engine against the page; find 1 → assume 1000; fix pattern-wide | OPEN | 82, 65, 81 |
| HVII.8 | counts from disk | STANDING | 01 |
| HVII.9 | if a fact lives in two files, delete one | OPEN | 73, 63 |

## G. ADDED 2026-09-30 (second pass) — end-goal gaps not voiced as concerns but required to "complete the project and win"
| ID | Gap | Protocols |
|---|---|---|
| EG1 | hackathon rubric (CER + bootstrap 95% CI, WER, S/D/I, seconds/page) not reported | 80 |
| EG2 | handwriting / low-quality documents: 0 in our benchmark; the hackathon targets them | 81 (U13) |
| EG3 | 5,344 unlabelled test images: no script-ID/routing/output path | 78 |
| EG4 | licence of the best engine (surya, $5M cap) and 8 unverified licences | 83 (U14) |
| EG5 | locked K1 verdict for Punjabi is wrong (tie p=1.0) → W6 QLoRA scope = kok only | 86 D3 |
| EG6 | law spread over 6+ docs; stale master doc | 84 |
| EG7 | Build on the strongest open model (Bodhan 84.94) instead of surya (69.96) — CO-087/089/091 "crack the edge, cross their plan" | 89 |
| EG8 | Never train or tune on any benchmark split or test image (the unread strategy doc proposed RL on Sarvam's split) | 89 §B, 87 §B |
| EG9 | Boss 2026-09-30: research and install the best current tools, agents, skills | 94, 88 |

## H. ADDED 2026-09-30 (third pass) — the boss's afternoon turns
| ID | Concern (boss's words, condensed) | Status | Protocols |
|---|---|---|---|
| H1 | "no one is using all the research output md files … take clear decisions and merge or condense or delete … or archive them" | OPEN | 95 |
| H2 | "we have done a huge research and also some more to do" | OPEN | 97 |
| H3 | "after all these … archive and reports also to compact, merge them and make some low variants … bunch of junk" | OPEN | 96 |
| H4 | "pip install laya — are we using it in the model and for developing the project? … can we use it or not; if yes write it in protocols" | DECIDED: NOT used (U30); measured reopen path | 31 |
| H5 | "why the hell are you doing the work … I said I will assign to the agent" | STANDING (model-tiering) | — |
| H6 | "are you using graphify or not — if you used that I shouldn't have seen this much junk"; "you are just reading offset 50 lines" | OPEN — graphify signals + before/after in proto-98 Phases 1/5; full reads only (proto-98 law 1) | 98 |
| H7 | "I need every file's rating, ranking, its worth to stay" | OPEN — WORTH 0–100 + FILE_WORTH_RANKING.csv + WASTE list | 98, 72, 95 |
| H8 | "read all the relevant variants and write the final md file … merging all the variants should go to archive" | OPEN — 14 topic finals (≥ 20 plan docs → docs/PLAN.md) | 98 |
| H9 | "use Laya, it can give the decisions so fast after reading the content" | DECIDED: measured trial, advisory only (U31); OCR model NO (U30) | 98, 31 |
| H10 | "check the hierarchy and the flow … so clean and official and perfect"; meeting files looked for at the root (MEETING_2026-09-29_STRUCTURED.md, sync - ocr - September 10.docx — the docx was filed as root_clutter) | OPEN — official tree + docs/sources/ (U32) | 98 |
| H11 | uni v3 re-pasted 2026-09-30 as "ACTIVE LAW" | STANDING — every line already mapped (§A CO-001…096, §C uni items); counters C1–C15 stand | 99 |
| H12 | "you don't do the labour — use your brain for the top-level stuff" | STANDING (model-tiering) | — |
| H13 | "why am I seeing South out [in a] separate place and other languages in other folders… delete them and do newly for South and merge/store them along with other languages" (asked many times); "many unwanted, unrecognised folders — I need clear details why they exist" | OPEN — proto-101 (P0–P7, owners assigned; whole-repo folder verdict table) | 101, 98 |
| H14 | "read these clearly … write all protocols to sort out and fix all these" (the Verdict report of 16:21 + the proto-101 incident) | OPEN — proto-102 Parts A–D | 102 |
| H15 | "check meeting 2 details, sort this relevantly and apply … to not mislead" | OPEN — proto-103 (verbatim L/S/U table, 10 corrections M1–M10, application table) | 103 |

## I. ADDED 2026-09-30 evening — both meetings, read in full by the planner (every item → status → protocol)
| ID | Item (source) | Status | Protocols |
|---|---|---|---|
| S10-1 | Label data first; one page = one sample; language-wise paragraph boxes; start 100/lang (Sep 10) | PARTIAL — probe22 page samples ≤100/lang; VLM-API labelling SUPERSEDED for layout and REJECTED as GT (B-14) | 100, 20, 21 |
| S10-2 | Benchmark existing VLMs on 20–22 samples/lang with one pipeline; own benchmark on own data (Sep 10) | DONE (probe22 11 engines × 18 langs + South; BENCHMARK_22.md) — verify per proto-62 | 12, 62 |
| S10-3 | Find where VLMs lag, then add layers: tokenizer / refinement / semantic (Sep 10) | OPEN — Plan v3 sharpens where Bodhan trails; refinement layer = B-13 | 89, 100 |
| S10-4 | Keep lab-style records: data vs working_experiments, named experiments, sample tracking (Sep 10) | PARTIAL — manifests + DISPATCH_LOG; experiment registry = B-15 | 70, 100 |
| S10-5 | Use free-tier APIs/models (Grok, NVIDIA Build, Gemini, GLM, OpenCode free models) (Sep 10) | STANDING — OpenCode sessions run GLM/MiniMax; Sarvam cap spent | — |
| S10-6 | "We have our own GPU resources" (Vinay, Sep 10) | OPEN — U33 | 92 |
| S10-7 | Team logistics: repo, language sheet, data sharing, David call, 20-sample sets (Sep 10) | HISTORICAL | — |
| S29-a..j | The lead's method (Sep 29): a read others ✓ · b Consensus.app 2–3 searches ✗ (U36) · c training flowchart PARTIAL (B-16) · d scan advances ✓ · e diff vs built ✓ · f multi-LLM eval: Plan v2 ✓ / Plan v3 ✗ (B-17, Gate 2.5) · g 22-lang benchmark ✓ · i 15–20 min cross-question session on a DRAFT plan OPEN (U36) — NOTE (proto-103): "hybrid of existing" (S5) and "AI-only team" (S2) are the BOSS's words, not the lead's method; Bodhan base applies S5 | MIXED | 89, 100, 92 |
| S29-D1..D7 | D1 research-first ✓ · D2 22-lang benchmark ✓ · D3 PPT baseline ✓ (proto-75 finishes the stage-by-stage) · D4 multi-LLM validation → Gate 2.5 · D5 human session → U36 · D6 hybrid = the boss's S5, accepted by the lead ✓ · D7 "AI itself is enough" = the boss's S2 (the lead offered more people, L9) | MIXED | 75, 89, 92 |
| S29-A1..A7 | A1 ✓ (Consensus part ✗ → U36) · A2 ✓ · A3 Plan v3 → Gate 2.5 · A4 deck = docs/PLAN.md + Claude Doc re-export (proto-98 T1) · A5 ✓ · A6 UNKNOWN → U36 · A7 ✓ (AGENTS.md START HERE + protocols) | MIXED | 98, 92 |
| S29-RL | Red lines: no training before research validation (→ Gate 2.5) · no novel backbone ✓ · no 400-page collection ✓ · Sarvam cap ✓ · no root essays ✓ · no downloads without approval ✓ · sealed dirs ✓ | STANDING | 01, 89 |
| RES-1 | Research that must be built, not archived (R1–R4, R6, R7, B12) | OPEN — 17 build items | 100 |
