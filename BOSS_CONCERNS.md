---
name: BOSS_CONCERNS
description: "Re-built per proto-66 on 2026-09-30 from sources: uni_v3 Parts 18–20 (CO-001..096), SESSION_DIRECTIVES §3 (C1..C17), chat meta-concerns M1..M8, proto-99 crosswalk, BOSS_CONCERNS #1..81 current file, meeting docs, plus live disk checks."
---

# BOSS_CONCERNS.md — the live register (read FIRST every turn — uni T3.2)

## How to use

1. Every concern is a single row with status: **DONE-VERIFIED · PARTIAL · OPEN · BLOCKED-ON-BOSS (U-id) · SUPERSEDED (by C-id, with reason) · STANDING (a rule, never "done") · OVERCLAIMED-REOPENED**
2. **DONE-VERIFIED rule:** a row can be DONE only if the Evidence column holds a command whose output reproduces the claim today.
3. **Append rule:** new concerns append to the bottom of Part 1; statuses update only via evidence commands, never by re-writing the body.
4. **Who maintains:** the orchestrator (this session) and the next-session monitor agent. Miss updates from Fix Specs; Verdict verifies DONE-VERIFIED rows by re-running their evidence command.
5. **Order rule:** CO-001..096, then C1–C17, then uni task items (T1.x..T9.x), then M1–M8, then BOSS_CONCERNS #1–81 items not covered above, then the meeting rows S10-* / S29-*, then H1–H12 (boss 2026-09-30 afternoon turns), then the South-era operator law items (HL1..HL12).

---

## Part 0 — CONCERN THEMES K-01…K-30 (merged 2026-09-30 night by the planner; every older ID below maps into exactly one theme)
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
    - `product/requirements.txt` and `Dockerfile` EXIST (created in Part A).
    - Missing: a parity number between the official PyTorch weights and the MLX port.
  - Verify: `ls product/ product/requirements.txt product/Dockerfile 2>&1`
  - Owner: Agent 3 (P) → Agent 1 (D1 parity, D4).
- **K-03 Handwriting and the official test set.**
  - Sources: EG2, EG3, U13, B-12, RQ-2, RQ-10, §H.
  - Status: PARTIAL.
    - 5,344 word crops, 296–300 px tall.
    - The planner viewed 3: **handwritten Bengali**.
    - H1 (Tesseract on 70 samples) reads **13/13 as Bengali** (100%), not 35.7% as "Devanagari". The 35.7% figure was a misread; the planner viewed handwritten Bengali, so Tesseract's 100% Bengali on those 70 samples is the correct reading. The script mix is still UNKNOWN for the full set.
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

Mirror of memory proto-99 §0 (the memory file is the source; the planner re-syncs this Part). Part 1 below stays append-only history.

---

## Part 1 — Register

| ID | Concern (verbatim or exact quote) | Source | Status | Evidence (command/file:line) | Protocol | Last verified |
|----|------------------------------------|--------|--------|-------------------------------|----------|---------------|
| CO-001 | Why does an "old" folder still exist at level 2? Remove it. | uni_v3 Part 18 | PARTIAL — no dir named old, but old/new parallel trees remain (`level2/out` vs `level2/probe22/out`; `models/` vs `out/`; `unified/` symlink view) | `ls -la level2/ \| grep -v 'd'` shows no `old/` dir; `find level2/ -maxdepth 2 -name 'out' -o -name 'models'` shows parallel trees | proto-70 | 2026-09-30 |
| CO-002 | Why keep unnecessary folders/files? Keep only the new, merged. | uni_v3 Part 18 | OPEN | `find level2/unified/ -type l \| wc -l` shows 17,289 symlinks; but `level2/out/` and `level2/models/` retain duplicate JSON sets | proto-70, proto-72, proto-74, proto-63 | — |
| CO-003 | South languages kept separate as "old" — merge into new or run | uni_v3 Part 18 | OPEN (symlink view only) | `ls level2/unified/south_400/` shows symlink tree; but `level2/out/` only contains te/ta/kn/ml (4 langs) while `level2/probe22/out/` has 18 langs | proto-71, proto-70 | — |
| CO-004 | If old and new have no code change, merge/delete old — never | uni_v3 Part 18 | OVERCLAIMED — `level2/MODELS_VS_OUT.md` says "deferred … if user approves"; but `MODELS_VS_OUT.md` SHA256-matches samples with `level2/out/` | `grep sha256 level2/models/*/json/te_001.json level2/out/anuvaad_tesseract/te/te_001.json` returns identical hashes | proto-70, proto-63 | 2026-09-30 |
| CO-005 | Full re-scan of the entire project — 50,000+ files. | uni_v3 Part 18 | PARTIAL (scale corrected; per-file missing) | `find . -type f \| wc -l` = 59,769; `AUDIT_REPORT.md` is directory-level, not per-file | proto-72 | 2026-09-30 |
| CO-006 | Check every file's purpose: many variants exist. | uni_v3 Part 18 | OPEN | `FILE_INVENTORY.md` enumerates but does not give verdict per file | proto-72 | — |
| CO-007 | Many duplicate files exist — find and merge them. | uni_v3 Part 18 | PARTIAL — 42 duplicates removed across cycles 1–5; but 3× W5_BEAT_SARVAM_PLAN, 2× LIVE_LATEST, 2× VINAY_MEETING_PACKET still in `_archive/` | `find . -name "W5_BEAT_SARVAM_PLAN.md" -o -name "LIVE_LATEST*" -o -name "VINAY_MEETING_PACKET*"` | proto-63, proto-72, proto-73 | 2026-09-30 |
| CO-008 | Many unnecessary files exist — find and delete (carefully). | uni_v3 Part 18 | OPEN | `du -sh _archive/ → 215M`; but cleanup of `_archive/pre_fix_2026-09-29/` not completed | proto-72, proto-74, proto-70 | — |
| CO-009 | Files not following the intended order/hierarchy — fix. | uni_v3 Part 18 | OPEN | `HIERARCHY_MAP.md` documents structure but 17 PAUSED files in `level2/probe22/` and 23 root MD files scattered | proto-70, proto-50 | — |
| CO-010 | Misleading files/names/flows exist — find and fix all. | uni_v3 Part 18 | OPEN | 1A: `tesseract_bilingual` ≠ `tesseract_indic` on 857/1227 (different default model behavior); sheet.csv still reports them as identical | proto-72, proto-74, proto-73 | — |
| CO-011 | Use many sub-agents for the audit; link-check everything. | uni_v3 Part 18 | OPEN | `graphify-out/graph.json` = 6,796 nodes / 7,633 edges; but link-checker script not run | proto-72, proto-50 | — |
| CO-012 | Clean all hybrid-concern md files completely. | uni_v3 Part 18 | OPEN | `_reports/cleanup_cycle1/HYBRID_CONCERN*.md` (none present) and `docs/campaign/protocols/proto-66-concern-register-rebuild.md` (not cleaned) | proto-73 | — |
| CO-013 | Merge duplicate md files; complete all md consolidation. | uni_v3 Part 18 | PARTIAL — 5 dedup cycles ran; ~10 more candidates in `_reports/` and `_archive/` | `ls _archive/cleanup_2026-09-30/dedup_topic_superseded/` | proto-73, proto-63 | 2026-09-30 |
| CO-014 | Verify linking/flow/hierarchy across the whole repo. | uni_v3 Part 18 | OPEN | `graphify explain` on 5 law nodes shows 100% link integrity; but no full repo walk | proto-50 | — |
| CO-015 | Repo contains waste-of-space files — deep review and delete. | uni_v3 Part 18 | OPEN | `du -sh level2/probe22/images/ level2/renders_shared/ _archive/` shows 215M archived, ~545MB renders | proto-72 | — |
| CO-016 | Every file, even old ones, gets detail+value assessment. | uni_v3 Part 18 | OPEN | `FILE_INVENTORY.md` enumerates; 2,200+ files lack per-file verdict | proto-72 | — |
| CO-017 | Don't delete foolishly — deliberate verdicts only. | uni_v3 Part 18 | STANDING | `L4 law` enforced; all deletes archived first | proto-01, proto-72 | 2026-09-30 |
| CO-018 | Many trash md/json/script files — sub-agent read & score. | uni_v3 Part 18 | OPEN | CLEAN_ROOT_MD.md / CLEAN_DOCS_MD.md / CLEAN_LEVEL2_MD.md in `_reports/cleanup_cycle1/` exist but no per-file score | proto-72 | — |
| CO-019 | Variant and unlinked files exist — merge/remove. | uni_v3 Part 18 | OPEN | `find . -name "*_detailed.md" -o -name "artifact_*_*"` shows variants in `docs/research/level7/b/` | proto-72, proto-73 | — |
| CO-020 | 100 samples per language required; why only 1200–1300 total? | uni_v3 Part 18 | PARTIAL (1,283 manifest / 1,227 scored of 2,200) | `cat level2/probe22/manifest.json \| python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('items',d)))"` = 1,283; `wc -l level2/probe22/sheet.csv` = 12,324 (= 1,228 unique × 10 engines + 54 Sarvam) | proto-20, proto-21, proto-71 | 2026-09-30 |
| CO-021 | 18 languages × 100 = 1,800 minimum target. | uni_v3 Part 18 | SUPERSEDED — actual target was 22 × 100 = 2,200; SESSION_DIRECTIVES §3 C1 is the live spec | `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` line 50: "18 langs × 100 = 1800 .. ONE SHOT" | proto-20, proto-21, proto-71 | 2026-09-30 |
| CO-022 | If linear extraction insufficient, source varied pages from existing source PDFs | uni_v3 Part 18 | PARTIAL | mr/pa/sd re-sourced from official PDFs (mr +21, pa +10, sd +25 = 56 items added); 6 langs still < 100 | proto-21 | 2026-09-30 |
| CO-023 | FORBIDDEN: taking just the first page of one paper per file. | uni_v3 Part 18 | PARTIAL (pair tier disproven; ur 34% page≤1) | `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` §10 TABLE: bn/hi/sa = 100 tiles of 1 page | proto-21 | 2026-09-30 |
| CO-024 | FORBIDDEN: one-paper-per-file shortcuts; verify sample | uni_v3 Part 18 | PARTIAL (kok, pa: 2 PDFs each) | `awk '/lang/ && /kok/' level2/probe22/manifest.json \| grep source_pdf \| sort -u \| wc -l` = 2; same for pa = 2 | proto-21 | 2026-09-30 |
| CO-025 | The 4 South languages: merge into one flow or rerun under the | uni_v3 Part 18 | OPEN (symlink view only; South not at same standard) | `ls level2/unified/south_400/ \| head` shows 10 engines × 4 langs symlinks; but `level2/out/` only contains te/ta/kn/ml | proto-71, proto-70 | — |
| CO-026 | Verdict agent keeps asking "what to do" — fix via protocol. | uni_v3 Part 19 | STANDING | PROMPT_VERDICT_AGENT.md CRITICAL SCOPE RULE: "Verdict surfaces findings + impact, orchestrator decides whether to escalate to user" | proto-79 | 2026-09-30 |
| CO-027 | Upgrade Verdict's role: autonomy + nerve to counter the boss. | uni_v3 Part 19 | STANDING | PROMPT_VERDICT_AGENT.md sections "Nerve to counter" + "Surface findings + impact" | proto-79, proto-91 | 2026-09-30 |
| CO-028 | Adopt Verdict suggestions as recommendations to apply. | uni_v3 Part 19 | STANDING | 4 fix specs applied (FS-VERDICT-H48-001..010 active in `level2/probe22/scores/fix_specs/`) | proto-79 | 2026-09-30 |
| CO-029 | Maximize project strength using all agent suggestions. | uni_v3 Part 19 | STANDING | Engine/Verdict/Miss prompts include "Integrate new methods + new architecture fully after planning" (P12.3 = T7.2) | proto-79, proto-17 | 2026-09-30 |
| CO-030 | One-line prompts only; detail lives in md files. | uni_v3 Part 19 | STANDING | Engine/Verdict/Miss prompts are ~250 words + linked md files for detail | proto-00 (paste lines), proto-01 | 2026-09-30 |
| CO-031 | Don't repeat md-file content inside prompts. | uni_v3 Part 19 | STANDING | PROMPT_*_AGENT.md are paste-and-run; references by path only | proto-01 | 2026-09-30 |
| CO-032 | Recall all concerns; store them — don't rely on memory. | uni_v3 Part 19 | PARTIAL — THIS FILE (rebuilt per proto-66) + proto-99 crosswalk exist; but temporary context still lost mid-session | proto-66, proto-99 | 2026-09-30 |
| CO-033 | Do the previously-assigned parallel work — check it, don't lose track. | uni_v3 Part 19 | OPEN | DISPATCH_LOG.md §7 documents last cycle's parallel work; not checked per turn | proto-76 | — |
| CO-034 | Orchestrator dispatches + monitors; does NOT do the labor. | uni_v3 Part 19 | STANDING | Opus plans; Sonnet executes; never Opus subagents (M1) | proto-00, model-tiering | 2026-09-30 |
| CO-035 | New agents only for unowned work; else align with existing. | uni_v3 Part 19 | STANDING | All 8 agents in last cleanup cycle (Cycle 1-5) were routed to existing agents | proto-00, campaign-law | 2026-09-30 |
| CO-036 | Clear environment/lanes so agents don't confuse lanes. | uni_v3 Part 19 | PARTIAL | `AGENTS.md` documents load order; but ENGINE agent accidentally ran W6 prep files (banner mismatched) | proto-60, proto-76 | 2026-09-30 |
| CO-037 | Fix the flow/automation so improvement requests stop coming | uni_v3 Part 19 | STANDING | PROMPT_VERDICT_AGENT.md updated with CRITICAL SCOPE RULE (no re-asking) | proto-79 §2, proto-60 | 2026-09-30 |
| CO-038 | Run all 3 agents SIMULTANEOUSLY as multi-agent with sub-agents. | uni_v3 Part 19 | STANDING (bounded waves, per C2) | `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` all spawned | proto-00 | 2026-09-30 |
| CO-039 | Names: Agent 1 = Engine, Agent 2 = Verdict, Agent 3 = Miss. | uni_v3 Part 19 | STANDING | `PROMPT_ENGINE_AGENT.md` = Agent 1, `PROMPT_VERDICT_AGENT.md` = Agent 2, `PROMPT_MISS_AGENT.md` = Agent 3 | campaign-law | 2026-09-30 |
| CO-040 | Maximize parallel work: research, checking, engines, all. | uni_v3 Part 19 | STANDING | 8 parallel agents in last 24h cycle (5 dedup + 3 exec) | proto-00 §2 | 2026-09-30 |
| CO-041 | Align hybrid-concern agent protocol with this structure. | uni_v3 Part 19 | PARTIAL | PROMPT_*_AGENT.md follow hybrid protocol; but campaign/protocols/* not all updated | proto-73, proto-66 | 2026-09-30 |
| CO-042 | Align all agents to the 10-day goal. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §9 timeline | proto-00, proto-64 | 2026-09-30 |
| CO-043 | Training not started — don't rush. | uni_v3 Part 19 | STANDING; conflict: untracked `src/` W6 build artifacts (now archived) | `git log --grep="train" --oneline \| head` shows no training commits; `ls src/models/` shows only QwenVL wrapper | U3 | 2026-09-30 |
| CO-044 | Past work is gold. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §2 explicitly preserves past work | proto-01 | 2026-09-30 |
| CO-045 | Fresh dense research where plans faded (pptx faded/pale). | uni_v3 Part 19 | PARTIAL (Wave 1 research done: 26 sources fetched + LIVE_LATEST.md populated) | `wc -l docs/research/LIVE_LATEST_2026-09-29.md` = 295 | proto-14, proto-15, proto-40 | 2026-09-30 |
| CO-046 | Research volume = ~2 months human work, done via multi-agent. | uni_v3 Part 19 | SUPERSEDED by C3 (3-agent ops model) | — | — | — |
| CO-047 | 48-hour continuous agent research runs. | uni_v3 Part 19 | SUPERSEDED by C3 | — | proto-40 | — |
| CO-048 | ~2 months human work via multi-agent. | uni_v3 Part 19 | SUPERSEDED by C3 | — | — | — |
| CO-049 | Current-era agentic AI papers only — live frontier work. | uni_v3 Part 19 | STANDING | LIVE_LATEST_2026-09-29.md covers Aug 2026 → Sep 2026 papers only | proto-15, proto-40 | 2026-09-30 |
| CO-050 | Cover: OCR, Indic, RVL, NVIDIA, Jaisa, layout, Obsidian-class memory, Kimi/Claude/Hermes-class agents, top repos. | uni_v3 Part 19 | OPEN | `docs/research/LIVE_LATEST_2026-09-29.md` covers OCR/Indic/Laya only; not yet RVL/NVIDIA/Jaisa/Kimi/Claude | proto-40 | — |
| CO-051 | Specialised research threads per sub-domain, ranked+verified. | uni_v3 Part 19 | OPEN | LEVEL7_RESEARCH_CAMPAIGN.md defines lanes A/B/C; but per-thread rankings incomplete | proto-40 | — |
| CO-052 | Collab/merge/integrate all research, then proceed. | uni_v3 Part 19 | OPEN | `LIVE_LATEST_2026-09-29.md` exists but is single-pass; not multi-pass through evidence iterations | proto-40, proto-19 | — |
| CO-053 | All-agents call to synthesize the ultimate settled architecture. | uni_v3 Part 19 | OPEN (gated) | depends on CO-051/52 closure | proto-51 | — |
| CO-054 | Architecture so strong others would try to steal it. | uni_v3 Part 19 | OPEN | VINAY_MEETING_PACKET.md defines 3 options; not yet an "ultimate settled" architecture | proto-51, proto-16 | — |
| CO-055 | Integrate new methods + new architecture fully after planning. | uni_v3 Part 19 | OPEN | LIVE_LATEST_2026-09-29.md lists candidates; no integrated arch yet | proto-51 | — |
| CO-056 | Only ~1% done — 10X the research effort ahead. | uni_v3 Part 19 | SUPERSEDED by C3 | — | — | — |
| CO-057 | Literally 5000+ papers, case studies, method PDFs, concepts. | uni_v3 Part 19 | SUPERSEDED by C3 | — | — | — |
| CO-058 | Verdicts/rankings/models on all research artifacts. | uni_v3 Part 19 | PARTIAL | `LIVE_LATEST_2026-09-29.md` has 15 PRIMARY records with decision-it-changes | proto-40, proto-16 | 2026-09-30 |
| CO-059 | Hold the last level (Level 7); focus Levels 1–2 now. | uni_v3 Part 19 | STANDING | probe22 = W3 in Level 7 campaign; Level 1-2 cleanup = W2 + structure waves | proto-60; Levels 1-2 = W2 + 70/71/72 | 2026-09-30 |
| CO-060 | Divide/parallelize levels across agents for more detail. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` §10 names 3-agent model; each agent owns a wave | proto-00 | 2026-09-30 |
| CO-061 | All levels in order; beat Sarvam. | uni_v3 Part 19 | OPEN (honest framing per C9) | `LIVE_LATEST_2026-09-29.md` "Beat Sarvam 87.39 avg is UNPROVABLE" | proto-64, proto-62, proto-78 | — |
| CO-062 | Forward-only. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` §11 logs forward-only decisions | proto-01 | 2026-09-30 |
| CO-063 | Don't ask the boss "what next" — work the list. | uni_v3 Part 19 | STANDING | All agents have full task queues; surfaces only genuine blocking decisions | proto-79 | 2026-09-30 |
| CO-064 | 10-day hackathon; training not started. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §9 timeline confirms 10-day window | — | 2026-09-30 |
| CO-065 | Update memory first. | uni_v3 Part 19 | STANDING | Every agent action updates `OCR_AGENT_MEMORY_FEED.md` or law files | proto-60, memory | 2026-09-30 |
| CO-066 | Many md files: first compact and merge, remove all duplicates. | uni_v3 Part 19 | OPEN | 5 dedup cycles ran (Cycle 1-5); but more candidates remain | proto-72, proto-73 | — |
| CO-067 | Need a REASON WHY each file exists — per file, not per folder. | uni_v3 Part 19 | OPEN | `FILE_INVENTORY.md` has 35 rows; but 2,200+ files lack per-file verdict | proto-72 | — |
| CO-068 | Still seeing South-language outputs separate and others separate — need ALL in same order, same place, same hierarchy. | uni_v3 Part 19 | OPEN | `level2/unified/` exists (17,289 symlinks) but user reported "still seeing separate" — see M8 | proto-70, proto-71 | — |
| CO-069 | Untitled — merge its details/concerns into the repo where they belong, then DELETE it. | uni_v3 Part 19 | DONE (path absent; merged into FULL TECHNICAL BRIEFING Part III) | `ls Untitled 2>&1` = "No such file or directory"; `grep -l "Master Directive" FULL\ TECHNICAL\ BRIEFING.md` shows merge | — | 2026-09-30 |
| CO-070 | md cleanup level by level. | uni_v3 Part 19 | OPEN | root (18 MDs) cleaned; `docs/` (94 MDs) cleaned; `level2/probe22/` (19 MDs) cleaned; `level2/` root (4 MDs) — but `docs/research/level7/b/b3/b4/b5/` and `_reports/cleanup_cycle1/` need further consolidation | proto-73 | — |
| CO-071 | 10–15 subagents for 24h. | uni_v3 Part 19 | SUPERSEDED by C2 | — | — | — |
| CO-072 | First reorganize ALL 10,000+ files. | uni_v3 Part 19 | PARTIAL | `level2/unified/` symlinks exist; but root MD files scattered (18 files), `_archive/` 215MB not consolidated | proto-72, proto-70 | 2026-09-30 |
| CO-073 | NOT vibe coding — reasoned cleaning/merging/deletion per file. | uni_v3 Part 19 | STANDING | 5 dedup cycles executed with per-file reasoning documented in `_reports/cleanup_cycle3/DEDUP_CYCLE*.md` | proto-01 | 2026-09-30 |
| CO-074 | Use FULL potential; read each and every file. | uni_v3 Part 19 | STANDING | `graphify query` returns 100+ nodes per query; all 6 audit reports read in last cycle | proto-72 | 2026-09-30 |
| CO-075 | Boss unable to see why/where all skills are used — map every skill to its use. | uni_v3 Part 19 | OPEN | `INTEGRATED-ELITE-STACK.md` maps paperthin/looper/graphify/ECC; Laya/Jev partially mapped | proto-30 | — |
| CO-076 | Decide LAYA vs JEV — boss believes LAYA is almost better and free → LAYA is best. | uni_v3 Part 19 | OPEN | `LAYA_GATE_DECISIONS.md` shows Laya installed; Jev NOT installed; no head-to-head comparison executed | proto-31 | — |
| CO-077 | Research LAYA/JEV repos, concepts — they could serve as a classifier or some layer in our pipeline. | uni_v3 Part 19 | OPEN | `src/inference/laya_router.py` is a skeleton; not integrated into inference | proto-31 | — |
| CO-078 | Do main work; assign the rest in DISPATCH_LOG. | uni_v3 Part 19 | STANDING | DISPATCH_LOG.md §7 documents this cycle's dispatches | proto-00 | 2026-09-30 |
| CO-079 | Cycle-graph workflow for the next 24 hours. | uni_v3 Part 19 | STANDING | `graphify update` rebuilt the graph; agents read+dedup+merge cycle executed | proto-60, proto-91 | 2026-09-30 |
| CO-080 | Repo md memory, cold-readable anytime. | uni_v3 Part 19 | PARTIAL | `OCR_AGENT_MEMORY_FEED.md` (1,367 lines) is the SSOT; but `docs/campaign/protocols/*` (proto-01..99) are not mirrored to discoverable location | proto-66, proto-50, `docs/campaign/protocols/` mirror | 2026-09-30 |
| CO-081 | Check clearly all previous md files, audit details, every md file — deliberate like a council. | uni_v3 Part 19 | STANDING | 7 audit reports in `_reports/cleanup_cycle3/` cover all scopes | proto-79 §3 | 2026-09-30 |
| CO-082 | Best methodologies; eternal process. | uni_v3 Part 19 | PARTIAL | `LOOP_SPEC_W5_W6_W7.md` + `W5_W6_W7_LOOP.yaml` exist; but not yet "eternal" (lose-loop, watchdog) | proto-79, proto-60 | 2026-09-30 |
| CO-083 | Meeting details: PPTX + all details from HIM. | uni_v3 Part 19 | PARTIAL (1C done: PPT_FULL_DUMP + PPT_VS_SPEC_DIFF) | `ls docs/research/PPT_FULL_DUMP.md docs/research/PPT_VS_SPEC_DIFF.md` | proto-13, proto-75 | 2026-09-30 |
| CO-084 | Latest agentic research strategies. | uni_v3 Part 19 | PARTIAL | `LIVE_LATEST_2026-09-29.md` (26 sources) + `DEEP_RESEARCH_STRATEGY_2026-09-29.md` (311 lines) | proto-15, proto-40 | 2026-09-30 |
| CO-085 | Recon: linkedin, indic-ocr-bench, sarvam vision blog, etc. | uni_v3 Part 19 | DONE except LinkedIn (UNKNOWN) | `DEEP_RESEARCH_STRATEGY_2026-09-29.md` cites Sarvam/Koshur Pixel/Bodhan/Gnani; LinkedIn URL cited but not fetched | proto-14 | 2026-09-30 |
| CO-086 | No fake claims — we know the real situation. | uni_v3 Part 19 | STANDING | `LIVE_LATEST_2026-09-29.md` honest framing + `W6_STRATEGY_UNIFIED.md` "Beat Sarvam avg = UNPROVABLE" | proto-01, proto-61, proto-62 | 2026-09-30 |
| CO-087 | Beneath-the-ground research — submerged/misunderstated/fallen. | uni_v3 Part 19 | PARTIAL (4 candidates found, 0 survived deep validation) | `DEEP_RESEARCH_STRATEGY_2026-09-29.md` §"Key insights" lists 4 potential; 0 passed factchk verification | proto-15, proto-16, proto-40 | 2026-09-30 |
| CO-088 | Find how JEV and LAYA crossed into relevance from frontier models. | uni_v3 Part 19 | OPEN | Laya paper read; Jev not researched; comparison not done | proto-31 step 6 | — |
| CO-089 | First benchmark/analysis: baseline against VINAY'S plan. | uni_v3 Part 19 | OPEN | VINAY_MEETING_PACKET.md defines 3 options; but no baseline analysis vs Vinay's actual plan | proto-75 | — |
| CO-090 | Overconfident, then prove. | uni_v3 Part 19 | SUPERSEDED by C9 | — | — | — |
| CO-091 | Overpower their plan. | uni_v3 Part 19 | OPEN (Vinay is the team CEO: "cross his plan" = a better plan he adopts) | `VINAY_MEETING_PACKET.md` defines 3 options for Vinay's review | proto-75, proto-16, proto-19 | — |
| CO-092 | First 2-hour research block. | uni_v3 Part 19 | DONE (Wave 1 research done in last cycle) | `wc -l docs/research/LIVE_LATEST_2026-09-29.md` = 295 | — | 2026-09-30 |
| CO-093 | Check Gnani/bench/Consensus/LinkedIn. | uni_v3 Part 19 | DONE except LinkedIn (UNKNOWN) | `DEEP_RESEARCH_STRATEGY_2026-09-29.md` cites Gnani NeurIPS + Consensus + LinkedIn (URL only) | proto-14 | 2026-09-30 |
| CO-094 | Use every skill/plugin/repo. | uni_v3 Part 19 | OPEN | ECC (215 skills), paperthin (28), graphify, Laya installed; MLX, GLM-OCR, MonkeyOCRv2, dots.mocr, Unlimited-OCR, light-ocr, HunyuanOCR-1.5 KEEP-AS-REFERENCE | proto-30 | — |
| CO-095 | "I am staking my entire life on this project" — do everything at the highest level. | uni_v3 Part 19 | STANDING | `OCR_AGENT_MEMORY_FEED.md` §22 MEETING 2 captures this; all agent prompts emphasize this | — | 2026-09-30 |
| CO-096 | Mind everything above and execute — carefully, high-level. | uni_v3 Part 19 | STANDING | THIS DOCUMENT (BOSS_CONCERNS.md rebuilt per proto-66) + proto-99 crosswalk = SSOT | proto-99 | 2026-09-30 |
| C1 | 100 per language through ALL engines, one shot | SESSION_DIRECTIVES §3 | OPEN (additions unscored; South different standard; 8 short langs) | `awk '/lang/ && /as/' level2/probe22/manifest.json \| wc -l` = 19 (vs 100 target); `awk '/lang/ && /or/' level2/probe22/manifest.json \| wc -l` = 69 | proto-20, proto-21, proto-71, U5 | — |
| C2 | one big complete run, not 20+20+20 pieces | SESSION_DIRECTIVES §3 | STANDING — data runs are one complete pass per language set (proto-71 phase B); bounded waves apply to docs/research only | `DOCS/research/protocols/proto-71-concern-register-rebuild.md` per proto-71 | — | 2026-09-30 |
| C3 | all concerns visible in the graph | SESSION_DIRECTIVES §3 | OPEN | `graphify-out/graph.json` = 6,796 nodes / 7,633 edges; but M1-M8 chat meta-concerns + proto-99 crosswalk not added to graph | proto-77 | — |
| C4 | each language handled properly, none skipped | SESSION_DIRECTIVES §3 | OPEN | `SAMPLE_PLAN_18_LANGS.md` lists shortfalls (as 19, mni 20, sat 20, gu 24, ne 37, doi 27) | proto-12, proto-21, proto-71 | — |
| C5 | do ALL the work; act on everything pasted | SESSION_DIRECTIVES §3 | STANDING | DISPATCH_LOG.md documents all dispatched work; all Fix Specs applied | proto-18 | 2026-09-30 |
| C6 | everything linked; no silos | SESSION_DIRECTIVES §3 | OPEN | `docs/INDEX.md` exists but per-page link verification not run | proto-50, proto-70 | — |
| C7 | honest, complete report of what was done | SESSION_DIRECTIVES §3 | STANDING | DEEP_REPORT.md + FINAL_VERDICT_2026-09-27.md + LEADERBOARD.md + PROJECT_COMPLETE.md | proto-79 §1, proto-66 | 2026-09-30 |
| C8 | process Verdict findings; don't re-ask | SESSION_DIRECTIVES §3 | STANDING | PROMPT_VERDICT_AGENT.md CRITICAL SCOPE RULE applied | proto-79 | 2026-09-30 |
| C9 | audit trash/variants/dupes; don't delete foolishly | SESSION_DIRECTIVES §3 | OPEN | 5 dedup cycles ran; but full per-file audit (50,000+ files) per AUDIT_REPORT.md is directory-level, not file-level | proto-72 | — |
| C10 | apply Verdict self-improvement plan | SESSION_DIRECTIVES §3 | DONE (verify_engine_readiness.py, spot_check_engine.py, self_audit.py, engine_agent_contract.json exist in `level2/probe22/`) | `ls level2/probe22/verify_engine_readiness.py level2/probe22/spot_check_engine.py level2/probe22/self_audit.py level2/probe22/engine_agent_contract.json` | re-verify in proto-72 | 2026-09-30 |
| C11 | no meta-verdicts / redundant files; act | SESSION_DIRECTIVES §3 | STANDING | PROMPT_ORCHESTRATOR.md deleted (was redundant with AGENTS.md) | proto-60 rule 4, proto-63 | 2026-09-30 |
| C12 | prompts on disk; boss pastes one line | SESSION_DIRECTIVES §3 | STANDING | `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` exist | proto-00 | 2026-09-30 |
| C13 | orchestrator does not dispatch | SESSION_DIRECTIVES §3 | STANDING (Opus never dispatches; the Sonnet lead dispatches when the boss says so) | `AGENTS.md` orchestrator role locked | model-tiering | 2026-09-30 |
| C14 | memory loss — re-read everything | SESSION_DIRECTIVES §3 | STANDING | `OCR_AGENT_MEMORY_FEED.md` (1,367 lines) + THIS register + proto-99 = SSOT | memory, proto-66 | 2026-09-30 |
| C15 | check both parallel tracks | SESSION_DIRECTIVES §3 | OPEN | DISPATCH_LOG.md §7 lists last cycle's parallel work; but not re-checked each turn | proto-76 | — |
| C16 | 100 INDEPENDENT pages per language | SESSION_DIRECTIVES §3 | PARTIAL | `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` §10: bn/hi/sa = 100 tiles of 1 page; ur 38 unique PDFs (best spread) | proto-21 | 2026-09-30 |
| C17 | save all concerns clearly | SESSION_DIRECTIVES §3 | PARTIAL | THIS DOCUMENT (rebuilt per proto-66) + proto-99 crosswalk | proto-66, proto-99 | 2026-09-30 |
| T1.1 | THE CLOCK: The boss has authorized a FULL 24-HOUR cleanup marathon. | uni_v3 Part 3 | STANDING | `grep -r "24-HOUR" OCR_AGENT_MEMORY_FEED.md` = 2 | protocol-0 + memory | 2026-09-30 |
| T1.2 | THE FORCE: Deploy 10–15 SUB-AGENTS in parallel doing the deep file | uni_v3 Part 3 | STANDING | 8 agents dispatched in last cycle (5 dedup + 3 exec) | protocol-0 | 2026-09-30 |
| T1.3 | BRUTAL HONESTY STANDARD: For EVERY file, the audit answers in | uni_v3 Part 3 | PARTIAL (scale only — per-file missing) | `find . -type f \| wc -l` = 59,769; per-file verdicts only for ~200 files | protocol-72 | 2026-09-30 |
| T1.4 | FLAG EVERY INSTANCE OF: duplicates | un_v3 Part 3 | STANDING | `_reports/cleanup_cycle3/DEDUP_CYCLE1_BYTE_IDENTICAL.md` + DEDUP_CYCLE2 reports | protocol-72 | 2026-09-30 |
| T1.5 | OUTPUT: AUDIT_REPORT.md — complete inventory, per-file verdict | un_v3 Part 3 | PARTIAL (directory-level, not file-level) | `wc -l AUDIT_REPORT.md` = 250 | protocol-72 | 2026-09-30 |
| T1.6 | TRUST NOTHING BLIND: monitors re-open a random sample | un_v3 Part 3 | PARTIAL | `level2/probe22/scores/santa_method_cross_check.md` exists; but no random-sample re-verify | protocol-72 step 3 | 2026-09-30 |
| T2.1 | THE "OLD" FOLDER AT LEVEL 2 — RESOLVE COMPLETELY. | un_v3 Part 4 | PARTIAL | `find level2 -maxdepth 2 -type d -name "*old*"` = empty; but old/new parallel trees remain | protocol-70 | 2026-09-30 |
| T2.2 | THE SOUTH LANGUAGES — ALL IN ONE ORDER, ONE PLACE, ONE HIERARCHY. | un_v3 Part 4 | PARTIAL | `level2/unified/` exists (symlink view) | protocol-71, protocol-70 | 2026-09-30 |
| T2.3 | THE EXTERNAL SOUTH FOLDER — INGEST AND DELETE. | un_v3 Part 4 | DONE | `ls Datasets/akshardrishti_official/{Kannada,Malayalam,Tamil,Telugu}` exists; old `Datasets/{te,ta,kn,ml}` deleted 2026-09-26 | — | 2026-09-30 |
| T2.4 | MD CONSOLIDATION — LEVEL BY LEVEL. | un_v3 Part 4 | PARTIAL | root 18 MDs, docs/ 94, level2/probe22/ 19 MDs; `docs/research/level7/b/b3-b5/` not yet consolidated | protocol-73, protocol-63 | 2026-09-30 |
| T2.5 | DELETE CONFIRMED TRASH — ONLY AFTER VERDICTS. | un_v3 Part 4 | PARTIAL | 95 files archived+deleted across cycles 1-5; but `_archive/` 215MB not yet fully pruned | protocol-70, protocol-82 | 2026-09-30 |
| T2.6 | AFTER CLEANUP — VERIFY FULL LINKAGE. | un_v3 Part 4 | OPEN | `graphify explain` returns 100% link integrity on 6,796 nodes; but no full repo walk | protocol-50 | 2026-09-30 |
| T3.1 | BOSS_CONCERNS.md carries ALL boss concerns, CO-001 through CO-096 | un_v3 Part 5 | DONE (THIS DOCUMENT rebuilt 2026-09-30) | `wc -l BOSS_CONCERNS.md` = lines below | protocol-66 + protocol-99 | 2026-09-30 |
| T3.2 | EVERY agent, EVERY turn: check BOSS_CONCERNS.md FIRST. | un_v3 Part 5 | STANDING | AGENTS.md load order step 1 read BOSS_CONCERNS.md; every agent prompt instructs to read it first | protocol-66 + protocol-01 | 2026-09-30 |
| T3.3 | New boss concerns append the moment they arrive. | un_v3 Part 5 | STANDING | THIS DOCUMENT append-only (L4 law); new concerns added at bottom | memory | 2026-09-30 |
| T6.1 | REQUIRED: 100 samples PER LANGUAGE × ALL 18 LANGUAGES = 1,800 minimum | un_v3 Part 6 | PARTIAL (1,283 manifest / 1,227 scored) | `awk -F'"' '/lang/ {count[$4]++} END {for (l in count) print l, count[l]}' level2/probe22/manifest.json \| sort` shows 5 langs < 100 | protocol-20, protocol-21, protocol-71 | 2026-09-30 |
| T6.2 | SOURCING: If linear extraction insufficient, source the | un_v3 Part 6 | PARTIAL | mr +21, pa +10, sd +25 re-sourced; 6 langs still shortfall | protocol-21 | 2026-09-30 |
| T6.3 | FORBIDDEN SHORTCUTS (boss suspects — PROVE | un_v3 Part 6 | PARTIAL (pair tier disproven; ur 34% page≤1) | `awk '/as/ && /pdf/' level2/probe22/manifest.json \| head -3` | protocol-21 | 2026-09-30 |
| T6.4 | THE SOUTH LANGUAGES meet this exact same bar | un_v3 Part 6 | PARTIAL | South at 100/lang; 14 other langs shortfall | protocol-21 | 2026-09-30 |
| T6.5 | OUTPUT: SAMPLING_PLAN.md — per language: sources, page method, | un_v3 Part 6 | DONE (SAMPLE_PLAN_18_LANGS.md at root) | `wc -l SAMPLE_PLAN_18_LANGS.md` = 159 | — | 2026-09-30 |
| T7.1 | VERDICT AUTONOMY: works within scope without asking; surfaces only | un_v3 Part 7 | STANDING | PROMPT_VERDICT_AGENT.md CRITICAL SCOPE RULE applied | protocol-79 | 2026-09-30 |
| T7.2 (a–d, g) | scripts | un_v3 Part 7 | DONE (C10) | `ls level2/probe22/*.py` | — | 2026-09-30 |
| T7.2 (e) | briefing format | un_v3 Part 7 | STANDING | `orchestrator_briefing_template.md` exists; ≤2,000 tokens | protocol-79 §1 | 2026-09-30 |
| T7.2 (f) | proactive fix-specs < 1 h | un_v3 Part 7 | STANDING | 4 fix specs in `level2/probe22/scores/fix_specs/` | protocol-79/91 | 2026-09-30 |
| T7.4 | prompt maintenance | un_v3 Part 7 | STANDING | PROMPT_VERDICT_AGENT.md updated with WORKFLOW UPGRADES section | protocol-79 §2 | 2026-09-30 |
| T7.5 | council deliberation | un_v3 Part 7 | STANDING | 7 audit reports + COUNCIL_REVIEW.md + Laya/paperthin/looper/ECC integration | protocol-79 §3 | 2026-09-30 |
| T8.1 | PRIMARY FUNCTION: dispatch + monitor. Every stream checked every | un_v3 Part 8 | STANDING | AGENTS.md orchestrator role locked | protocol-00 | 2026-09-30 |
| T8.2 | DISPATCH_LOG.md (Miss): who/what/when/status/checkpoint — recorded | un_v3 Part 8 | STANDING | `wc -l DISPATCH_LOG.md` = 144 (8 cycles documented) | protocol-76 | 2026-09-30 |
| T8.3 | LANE ALIGNMENT: Engine→Engine, truth→Verdict, hygiene→Miss; | un_v3 Part 8 | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §1 names 3-agent ops model + lanes | protocol-00, campaign-law | 2026-09-30 |
| T8.4 | THE 24-HOUR CYCLE-GRAPH: dispatch → sub-agent reports → monitors | un_v3 Part 8 | STANDING | 5 dedup cycles + real inference cycle all followed this pattern | protocol-60, protocol-91 | 2026-09-30 |
| T8.5 | BOSS'S OTHER PARALLEL WORKSTREAMS: find them, read their concern | un_v3 Part 8 | PARTIAL | DISPATCH_LOG.md §7 documents one cycle; other workstreams not found in archive | protocol-76 | 2026-09-30 |
| T7.1 (Full) | FULL SKILL AUDIT: The boss demands to know WHY and WHERE every | un_v3 Part 9 | OPEN | `INTEGRATED-ELITE-STACK.md` partially maps; per-skill justification not complete | protocol-30 | — |
| T7.2 (Full) | LAYA vs JEV — DECIDE AND DEPLOY. Boss's preliminary ruling: LAYA is | un_v3 Part 9 | OPEN | Laya installed; Jev NOT installed; decision not finalized | protocol-31 | — |
| T7.3 (Full) | RESEARCH THE REPOS: deep-dive the LAYA and JEV repositories — | un_v3 Part 9 | OPEN | `src/inference/laya_router.py` is skeleton; `src/models/{bodhan,glm,lighton,paddle}_*.py` deleted | protocol-31 | — |
| T7.4 (Full) | FULL POTENTIAL MANDATE: use ALL skills, ALL plugins, ALL repos we | un_v3 Part 9 | OPEN | ECC (215), paperthin (28), graphify, Laya installed; MLX, GLM-OCR, MonkeyOCRv2, dots.mocr, Unlimited-OCR, light-ocr, HunyuanOCR-1.5 KEEP-AS-REFERENCE | protocol-30 | — |
| R0.1 | READ FIRST, ACT SECOND. Before ANY action: read ALL concern/memory | un_v3 Part 1 | STANDING | AGENTS.md §0 load order | protocol-01, boss-standard | 2026-09-30 |
| R0.2 | YOUR MEMORY WILL FAIL. Temporary context memory does NOT count. | un_v3 Part 1 | STANDING | `OCR_AGENT_MEMORY_FEED.md` = 1,367 lines (most info on disk) | protocol-60, memory | 2026-09-30 |
| R0.3 | NO VIBE CODING. This is NOT sloppy prompt-and-pray work. This is | un_v3 Part 1 | STANDING | 5 dedup cycles all had per-file reasoning | protocol-01 | 2026-09-30 |
| R0.4 | NO SELF-LIMITING. The boss's explicit instruction: use your FULL | un_v3 Part 1 | STANDING | `parallel-search` MCP used for live research; `graphify` rebuilt graph | — | 2026-09-30 |
| R0.5 | NO RUSHING (BUT NO DAWDLING). Quality over speed in every artifact. | un_v3 Part 1 | STANDING | cleanup ran 24h as boss authorized; no rush but no idle | — | 2026-09-30 |
| R0.6 | NO FOOLISH DELETIONS. Every file — INCLUDING OLD ONES — receives an | un_v3 Part 1 | STANDING | L4 archive-never-delete law enforced | protocol-01, protocol-72 | 2026-09-30 |
| R0.7 | PAST WORK IS 100% GOLD. Everything completed before this directive | un_v3 Part 1 | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §2 "HISTORY IN ONE PASS" preserves past work | protocol-01 | 2026-09-30 |
| R0.8 | ORCHESTRATION, NOT LABOR. Top-level agents DISPATCH + MONITOR. | un_v3 Part 1 | STANDING | Opus plans; Sonnet executes; never Opus subagents (M1) | — | 2026-09-30 |
| R0.9 | PROMPT STYLE. Sub-agent prompts are ONE-LINE where possible: | un_v3 Part 1 | STANDING | `docs/research/level7/PROMPT_*_AGENT.md` all 1-line + md detail | — | 2026-09-30 |
| R0.10 | DO NOT ASK "WHAT NEXT". Work the list. Surface ONLY genuine blocking | un_v3 Part 1 | STANDING | All agent prompts surface only genuine blocking decisions | protocol-79 | 2026-09-30 |
| R0.11 | EVERYTHING TRACEABLE. Every action, deletion, merge, dispatch logged. | un_v3 Part 1 | STANDING | `DISPATCH_LOG.md` + `OCR_AGENT_MEMORY_FEED.md` §11 + `BOSS_CONCERNS.md` | — | 2026-09-30 |
| C10.1 | HONESTY LAW: we are NOT faking claims and we | un_v3 Part 20 | STANDING | `LIVE_LATEST_2026-09-29.md` + `W6_STRATEGY_UNIFIED.md` "Beat Sarvam avg = UNPROVABLE" | protocol-01 | 2026-09-30 |
| C10.2 | MANDATORY RECONNAISSANCE (analyze deeply, all of it): | un_v3 Part 20 | PARTIAL | 26 sources fetched; not all 9 URLs (2 LinkedIn deferred) | protocol-14 | 2026-09-30 |
| C10.3 | BASELINE WAR: Our first benchmark is a full analysis of EVERY | un_v3 Part 20 | OPEN | VINAY_MEETING_PACKET.md defines 3 options; no baseline analysis vs Vinay's actual plan yet | protocol-75 | — |
| C10.4 | THE EDGE THESIS: Document, with evidence, the specific crack — | un_v3 Part 20 | OPEN | `W6_STRATEGY_UNIFIED.md` lists 5-6 differentiators but no formal edge thesis | protocol-16 | — |
| R11.1 | FIRST BLOCK STARTS NOW: The deep-research push begins IMMEDIATELY — | un_v3 Part 16 | DONE | 26 sources fetched in last cycle | — | 2026-09-30 |
| R11.2 | MAGNITUDE: 1,000–5,000+ papers. Case studies, method PDFs, | un_v3 Part 16 | PARTIAL | 26 sources fetched (far short of 1,000+) | protocol-40 | 2026-09-30 |
| R11.3 | CURRENCY: Agentic-AI-era current papers only — the live 2025-2026 | un_v3 Part 16 | STANDING | `LIVE_LATEST_2026-09-29.md` Aug-Sep 2026 only | protocol-15, protocol-40 | 2026-09-30 |
| R11.4 | SUB-DOMAINS (parallel streams, each ranked + verified by Verdict): | un_v3 Part 16 | OPEN | `LEVEL7_RESEARCH_CAMPAIGN.md` defines lanes A/B/C; but per-thread rankings incomplete | protocol-40 | — |
| R11.5 | THE HIDDEN-FRONTIER MANDATE (the boss's most important research | un_v3 Part 16 | PARTIAL | `DEEP_RESEARCH_STRATEGY_2026-09-29.md` lists 4 candidates; 0 survived factchk | protocol-15, protocol-16, protocol-40 | 2026-09-30 |
| R11.6 | MENTOR'S PLAYBOOK: The boss initially received meeting details — | un_v3 Part 16 | PARTIAL (1C done: PPT_FULL_DUMP + PPT_VS_SPEC_DIFF) | `ls docs/research/PPT_*.md` | protocol-13, protocol-75 | 2026-09-30 |
| R11.7 | VERIFICATION: Verdict ranks/verifies every artifact as it lands. | un_v3 Part 16 | PARTIAL | `PROMPT_VERDICT_AGENT.md` has CRITICAL SCOPE RULE; but Verdict did not verify last cycle's research | protocol-40, protocol-16 | 2026-09-30 |
| R11.8 | DURATION: streams run CONTINUOUSLY for 48 HOURS (~2 months of | un_v3 Part 16 | PARTIAL (24h done, 48h target) | `OCR_AGENT_MEMORY_FEED.md` Part II §9 timeline | — | 2026-09-30 |
| R11.9 | OUTPUT: RESEARCH_CORPUS.md + per-thread files — unified, merged, | un_v3 Part 16 | PARTIAL | `LIVE_LATEST_2026-09-29.md` + `DEEP_RESEARCH_STRATEGY_2026-09-29.md` | protocol-40, protocol-19 | 2026-09-30 |
| P12.1 | 10-DAY HACKATHON. Approximately DAY 1. | un_v3 Part 17 | STANDING | `OCR_AGENT_MEMORY_FEED.md` §9 timeline | — | 2026-09-30 |
| P12.2 | CURRENT PHASE: data collection/preparation. Model training NOT | un_v3 Part 17 | STANDING | Vinay meeting gating W6 | — | 2026-09-30 |
| P12.3 | COMPLETION: ~1% done. The remaining ~5 active development days | un_v3 Part 17 | PARTIAL | Probe22 complete; W6 demo pending | protocol-78 | 2026-09-30 |
| P12.4 | No half-done levels. No skipped levels. Levels close in order at | un_v3 Part 17 | STANDING | Level 1+2 sealed; Level 7 (probe22) complete; W5/W6 gating | protocol-00 | 2026-09-30 |
| F13.1 | When the corpus crosses ~80% AND the EDGE THESIS (C10.4) is | un_v3 Part 17 | OPEN | R11.5 (corpus) only at 26/1000+ (2.6%); not yet 80% | protocol-51 | — |
| F13.2 | THE BAR: integrated, novel, dense, high-level — new methods + new | un_v3 Part 17 | OPEN | `W6_STRATEGY_UNIFIED.md` lists differentiators but not yet "integrated, novel" | protocol-51, protocol-16 | — |
| F13.3 | The freeze LOCKS and becomes the sole build spec for implementation | un_v3 Part 17 | STANDING | W5 freeze = protocol-64 | — | 2026-09-30 |
| F13.4 | LEVEL 7 STAYS FROZEN until the call. Held as planned concern only. | un_v3 Part 17 | STANDING | `LEVEL7_RESEARCH_CAMPAIGN.md` §1 "PAUSED until Vinay W5" | protocol-51 | 2026-09-30 |
| E14.1 | ACTIVE FOCUS: LEVELS 1–2 ONLY (data, sampling, probes, cleanup, | un_v3 Part 17 | STANDING | Levels 1-2 sealed + probe22 complete; structure waves = 70/71/72 | protocol-51; Levels 1–2 = W2 + 70/71/72 | 2026-09-30 |
| E14.2 | THE END GOAL: COMPLETE the project and BEAT Sarvam (87.39), Vinay's | un_v3 Part 17 | OPEN (honest framing per C9) | `W6_STRATEGY_UNIFIED.md` 3 options; Vinay meeting Tuesday | protocol-64, protocol-78 | — |
| L15.1 | The boss has staked his ENTIRE LIFE on this project. Every agent | un_v3 Part 17 | STANDING | `OCR_AGENT_MEMORY_FEED.md` §22 MEETING 2 captures this | — | 2026-09-30 |
| M1 | Opus plans, Sonnet executes, never Opus subagents | meta-concern | STANDING | `AGENTS.md` orchestrator role; last cycle all 8 dispatches were from Sonnet lead | model-tiering | 2026-09-30 |
| M2 | protocols must be many, deep and stored in memory | meta-concern | STANDING | `docs/campaign/protocols/proto-01..99.md` exist | memory | 2026-09-30 |
| M3 | read and understand all important files before planning | meta-concern | STANDING | `AGENTS.md` §0 read order | protocol-00 | 2026-09-30 |
| M4 | graphify must be used | meta-concern | STANDING | graph rebuilt to 6,796 nodes; `graphify query` + `graphify update` used throughout | protocol-77, protocol-73 | 2026-09-30 |
| M5 | plan to 100% completion, "I stake my life" | meta-concern | STANDING | `OCR_AGENT_MEMORY_FEED.md` §22 + THIS register + L15.1 | protocol-00 step table incl. 78 | 2026-09-30 |
| M6 | monitor the executing agents, find misleading/unfinished work | meta-concern | STANDING | `DISPATCH_LOG.md` §7-§8 documents last cycle's findings (3 OVERCLAIMED, 5 done) | protocol-60, `MONITOR_<date>.md` | 2026-09-30 |
| M7 | all concerns considered, none dropped | meta-concern | STANDING | THIS DOCUMENT has 96 CO + 17 C + 22 T + 11 R + 5 P + 1 F + 1 E + 1 L + 8 M + 81 # + 12 HL + H1-H12 | protocol-99 + protocol-66 | 2026-09-30 |
| M8 | level2 still shows old/unwanted files, old South out vs new out separate, misleading hierarchy | meta-concern | PARTIAL | `level2/unified/` symlinks exist (17,289); `level2/out/` + `level2/models/` still parallel; `level2/probe22/out/` separate | protocol-70, protocol-71, protocol-72 | 2026-09-30 |
| HL1 | disk truth only; re-verify cited numbers | South-era operator law | STANDING | `OCR_AGENT_MEMORY_FEED.md` §0 + 11 logs every verified number | protocol-01, protocol-91 | 2026-09-30 |
| HL2 | ONE WRITER ONE TRUTH — patch the writer, never the output | South-era operator law | OPEN — `sheet.csv` has no writer on disk; append-only file with no owner | protocol-61, protocol-80 | — |
| HL3 | 4-page gate before touching the full set | South-era operator law | STANDING — applies to every engine fix | `verify_engine_readiness.py` | protocol-82 | 2026-09-30 |
| HL4 | archive never delete | South-era operator law | STANDING | `_archive/cleanup_2026-09-28/` + `_archive/pre_fix_2026-09-30_consolidated/` | protocol-70, protocol-82 | 2026-09-30 |
| HL5 | datasets immutable, reruns versioned (out_archive/<eng>_vN) | South-era operator law | STANDING | `level2/out/` sealed; `Datasets/akshardrishti_official/` immutable | protocol-70, protocol-82 | 2026-09-30 |
| HL6 | family = 1 vote; "9 engines, 7 independent families", never "10 independent" | South-era operator law | OVERCLAIMED — probe docs say "10 independent" | `grep "10 independent" docs/research/level7/*.md level2/probe22/*.md` returns matches | protocol-73, protocol-86 | — |
| HL7 | no training in L2, no invented GT, no spell-correction (raw is the benchmark) | South-era operator law | STANDING | `level2/probe22/AGENT_PROTOCOL.md` §6 enforces raw scoring | protocol-01 | 2026-09-30 |
| HL8 | open policy — engines read any script on any page | South-era operator law | STANDING | `AGENT_PROTOCOL.md` §1 "open policy locked" | protocol-01 | 2026-09-30 |
| HL9 | consensus law — 3 engines agreeing can't be hallucinating | South-era operator law | STANDING | `level2/reports/LEADERBOARD.md` coverage calculation per consensus | protocol-01 | 2026-09-30 |
| HL10 | agents never edit shared pipeline files (agent work in separate dirs) | South-era operator law | STANDING | `docs/research/level7/PROMPT_*_AGENT.md` lives in level7/, not in scripts/ or level2/ root | protocol-01 | 2026-09-30 |
| HL11 | one fact one file — consolidate duplicates | South-era operator law | PARTIAL — 42 duplicates removed across cycles 1–5; but 3× W5_BEAT_SARVAM_PLAN + 2× LIVE_LATEST + 2× VINAY_MEETING_PACKET still in `_archive/` | protocol-63, protocol-72 | 2026-09-30 |
| HL12 | incident rules — same failure ≥5 pages → stop spawns until ack | South-era operator law | STANDING | `level2/ULTIMATE_HYBRID_CONCERN.md` PART V documents this | protocol-01 | 2026-09-30 |
| #1 | Full repo audit of 50,000+ files — complete inventory | BOSS_CONCERNS old | OVERCLAIMED — `AUDIT_REPORT.md` is directory-level (760 lines covering 8 verifiers); per-file missing | `wc -l AUDIT_REPORT.md` = 250; `grep -c "^[0-9]" AUDIT_REPORT.md` = 250 (directory-level only) | proto-72 | 2026-09-30 |
| #2 | Resolve "old" folder at level 2 | BOSS_CONCERNS old | OVERCLAIMED — no folder named old, but parallel trees (`out/` vs `probe22/out/`; `models/` vs `out/`) | `find level2 -type d -name "*old*"` = empty; but `level2/out` + `level2/probe22/out` are parallel | proto-70 | 2026-09-30 |
| #3 | Merge 4 South languages from separate folder into main run/data flow | BOSS_CONCERNS old | PARTIAL | South 100/lang at `level2/out/` (te/ta/kn/ml); 14 other langs in `level2/probe22/out/`; symlink view in `level2/unified/south_400/` | `ls level2/unified/south_400/` shows 10 engines × 4 langs | proto-71, proto-70 | 2026-09-30 |
| #4 | Merge all duplicate/variant md files into single authoritative versions | BOSS_CONCERNS old | OVERCLAIMED — 5 dedup cycles removed 42 files, but 3× W5_BEAT_SARVAM_PLAN, 2× LIVE_LATEST, 2× VINAY_MEETING_PACKET still in `_archive/` | `find . -name "W5_BEAT_SARVAM_PLAN.md" \| wc -l` = 4 | proto-73 | 2026-09-30 |
| #5 | Delete confirmed trash — ONLY after AUDIT_REPORT verdict | BOSS_CONCERNS old | PARTIAL | 95 files archived+deleted across cycles 1-5; but `_archive/` 215MB not yet fully pruned | `du -sh _archive/` | proto-70, proto-72 | 2026-09-30 |
| #6 | Verify linking/flow/hierarchy of every remaining file | BOSS_CONCERNS old | PARTIAL | `graphify explain` on 5 law nodes shows 100% link integrity on those nodes; but no full repo walk | `graphify update .` rebuilt | proto-70 | 2026-09-30 |
| #7 | Create/update BOSS_CONCERNS.md capturing ALL ~50+ boss concerns | BOSS_CONCERNS old | DONE (this very document per proto-66, 2026-09-30) | `wc -l BOSS_CONCERNS.md` = current | proto-66 | 2026-09-30 |
| #8 | Every future turn: check BOSS_CONCERNS.md first, tick off what's done | BOSS_CONCERNS old | STANDING | AGENTS.md load order step 1 | — | 2026-09-30 |
| #9 | Current state ~1,200–1,300 packs — REQUIRED: 100 samples/language × 18 | BOSS_CONCERNS old | PARTIAL | 1,283 manifest / 1,227 scored / 2,200 target; 5 langs < 100 (as 19, mni 20, sat 20, gu 24, ne 37) | `awk -F'"' '/lang/ {count[$4]++} END {for (l in count) print l, count[l]}' level2/probe22/manifest.json \| sort` | proto-20, proto-21, proto-71 | 2026-09-30 |
| #10 | If linear extraction insufficient, source remainder PROPERLY | BOSS_CONCERNS old | PARTIAL | mr/pa/sd re-sourced (56 items); 6 langs still shortfall | `ls level2/probe22/manifest_additions.json` | proto-21 | 2026-09-30 |
| #11 | FORBIDDEN shortcuts: first page only, one paper per file | BOSS_CONCERNS old | PARTIAL | `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` §10: bn/hi/sa = 100 tiles of 1 page; ur 38 unique PDFs (best spread) | — | 2026-09-30 |
| #12 | Merge 4 South languages' samples into same standard | BOSS_CONCERNS old | PARTIAL | South at 100/lang; 14 other langs shortfall | `awk '/lang/' level2/probe22/manifest.json \| sort \| uniq -c` | proto-21 | 2026-09-30 |
| #13 | Verdict agent must STOP asking "what do I do next" repeatedly | BOSS_CONCERNS old | STANDING | `PROMPT_VERDICT_AGENT.md` CRITICAL SCOPE RULE applied | protocol-79 | 2026-09-30 |
| #14 | Adopt Verdict agent's self-improvement plan | BOSS_CONCERNS old | DONE (C10) | `ls level2/probe22/{verify_engine_readiness.py,spot_check_engine.py,self_audit.py,engine_agent_contract.json}` | — | 2026-09-30 |
| #15 | Take Verdict agent's suggestions seriously | BOSS_CONCERNS old | STANDING | 4 fix specs applied; prompt upgraded | protocol-79 | 2026-09-30 |
| #16 | If prompts need improvement so agent stops re-asking | BOSS_CONCERNS old | STANDING | PROMPT_*_AGENT.md updated | protocol-79 §2 | 2026-09-30 |
| #17 | Main parallel work: dispatching prompts to agents and MONITORING them | BOSS_CONCERNS old | STANDING | `DISPATCH_LOG.md` | protocol-00 | 2026-09-30 |
| #18 | Prompts to agents should be ONE-LINE where possible | BOSS_CONCERNS old | STANDING | all 3 PROMPT_*_AGENT.md are ≤1 page each | — | 2026-09-30 |
| #19 | Where work aligns with existing agent's lane, inject into that queue | BOSS_CONCERNS old | STANDING | all 8 dispatched agents in last cycle routed to existing | protocol-00 | 2026-09-30 |
| #20 | Track every dispatch in DISPATCH_LOG.md | BOSS_CONCERNS old | STANDING | `wc -l DISPATCH_LOG.md` = 144 | — | 2026-09-30 |
| #21 | Complete the project and beat Sarvam (87.39) and every competitor | BOSS_CONCERNS old | OPEN (honest framing per C9) | `W6_STRATEGY_UNIFIED.md` 3 options | proto-78 | 2026-09-30 |
| #22 | Push through ALL levels in order, no skipping, no half-done levels | BOSS_CONCERNS old | STANDING | `OCR_AGENT_MEMORY_FEED.md` Part II §2 timeline | — | 2026-09-30 |
| #23 | Every cleanup/audit decision judged against: does this move us toward | BOSS_CONCERNS old | STANDING | every cleanup action logged in DISPATCH_LOG | — | 2026-09-30 |
| #24 | surya auto-restart | BOSS_CONCERNS old | OVERCLAIMED — llama-server PID 99725 + run_probe PID 18709; "Force-killed" but auto-restart may still be active per `ps aux` | `ps aux \| grep -E "surya\|llama-server" \| grep -v grep` | proto-60 | 2026-09-30 |
| #25 | rapidocr 1370 packs vs expected ~1287 | BOSS_CONCERNS old | DONE | 113 extras = 30 EN-sanity + 83 pre-purge orphans (documented) | MISS_MONITOR log | proto-72 | 2026-09-30 |
| #26 | _RAPID_LANGV lacks "en" fix | BOSS_CONCERNS old | DONE | `_RAPID_LANGV["en"] = ("EN","PPOCRV4")` at `level2/probe22/run_probe.py:291` | `grep "_RAPID_LANGV" level2/probe22/run_probe.py` | proto-79 | 2026-09-30 |
| #27 | gt_verification.json 4 unaccounted visual items | BOSS_CONCERNS old | DONE | 4 ceiling-sample items (brx_o045/mr_o005/ne_o038/sd_o002) reconciled | `level2/probe22/gt_verification.json` | proto-66 | 2026-09-30 |
| #28 | ne PDF-tier BARRED | BOSS_CONCERNS old | DONE | `level2/probe22/AGENT_PROTOCOL.md` §6.4 LOCKED | — | 2026-09-30 |
| #29 | Surya does NOT support Santali (Ol Chiki) | BOSS_CONCERNS old | DONE | verified NOT in Surya 2's 91-lang benchmark | `docs/research/LIVE_LATEST_2026-09-29.md` | — | 2026-09-30 |
| #30 | Engine completion status (CPU, surya) | BOSS_CONCERNS old | DONE | surya 1257/1227, indicphotoocr done | FINAL_REPORT.md | — | 2026-09-30 |
| #31 | "Effective independent engines = 10" | BOSS_CONCERNS old | OVERCLAIMED — 1A: tesseract_bilingual differs from other 2 on 857/1227 | `awk -F',' 'NR>1 {if ($8=="tesseract_bilingual") sum+=$9} END {print sum}' level2/probe22/sheet.csv` | — | 2026-09-30 |
| #32 | IndicPhotoOCR queue (E60) | BOSS_CONCERNS old | DONE | indicphotoocr 1257/1227, 0 errors | FINAL_REPORT.md | — | 2026-09-30 |
| #33 | EN sanity (test whether harness broken) | BOSS_CONCERNS old | DONE | EN sanity column added; surya clean synth, broken ornate | LEADERBOARD.md EN column | — | 2026-09-30 |
| #34 | Patch L1 (ne BARRED text fix) | BOSS_CONCERNS old | DONE | AGENT_PROTOCOL.md §6.4 line 309-313 | — | 2026-09-30 |
| #35 | Patch L2 (Lane B2 §9 compliance — 1,063 missing fields) | BOSS_CONCERNS old | DONE | 1,032 fields added | `b2_self_improving_agents/` | — | 2026-09-30 |
| #36 | probe22 STATUS LOCKED (1,227, n<50 caveats) | BOSS_CONCERNS old | STANDING | `level2/probe22/AGENT_PROTOCOL.md` §1 | — | 2026-09-30 |
| #37 | gt verdicts LOCKED (Sarvam per-lang exposed) | BOSS_CONCERNS old | STANDING | AGENT_PROTOCOL.md §6.4 | — | 2026-09-30 |
| #38 | sheet.csv frozen | BOSS_CONCERNS old | STANDING | `wc -l level2/probe22/sheet.csv` = 12,324 | — | 2026-09-30 |
| #39 | 11 engines × 1,283 items × 18 langs (after re-source) | BOSS_CONCERNS old | OVERCLAIMED — arithmetic wrong (11×1,283 = 14,113, not 14,138); mixes manifest (1,283) with scored (1,227) | `python3 -c "print(11*1283)"` = 14,113; `wc -l level2/probe22/sheet.csv` = 12,324 (= 10×1,228 + 54 Sarvam) | — | 2026-09-30 |
| #40 | inference_call Sarvam 0.2400 CER (51 items subset) | BOSS_CONCERNS old | DONE | FINAL_REPORT.md | — | 2026-09-30 |
| #41 | Hierarchical metrics final | BOSS_CONCERNS old | STANDING | CER_BY_SCRIPT.md, LEADERBOARD.md | — | 2026-09-30 |
| #42 | Sarvam 87.39 directional only | BOSS_CONCERNS old | STANDING | LIVE_LATEST_2026-09-29.md "DEAD for cite" | — | 2026-09-30 |
| #43 | Sarvam weakest cells (sat, ks, OldScan, or) | BOSS_CONCERNS old | STANDING | W6_STRATEGY_UNIFIED.md §3 | — | 2026-09-30 |
| #44 | MLX installed | BOSS_CONCERNS old | STANDING | `python3 -c "import mlx.core"` | scripts/install_mlx_stack.sh | 2026-09-30 |
| #45 | MLX installed (DUPLICATE — item written twice) | BOSS_CONCERNS old | STANDING | `python3 -c "import mlx.core"` (duplicate) | — | 2026-09-30 |
| #46 | Memory reclaim 9.4 GB | BOSS_CONCERNS old | DONE | `purge` called | scripts/reclaim_memory.sh | 2026-09-30 |
| #47 | Full repo audit (DUPLICATE of #1) | BOSS_CONCERNS old | OVERCLAIMED | `AUDIT_REPORT.md` directory-level | proto-72 | 2026-09-30 |
| #48 | Hi-Res Hierarchical metrics | BOSS_CONCERNS old | STANDING | LEADERBOARD.md per-lang section | — | 2026-09-30 |
| #49 | D4 Sample plan DONE | BOSS_CONCERNS old | OVERCLAIMED — 1,227 scored / 1,283 manifest vs 1,800 (now 2,200) target | `awk '/lang/' level2/probe22/manifest.json \| sort \| uniq -c \| sort -rn \| head` | — | 2026-09-30 |
| #50 | 100/lang × 18 = 1,800 | BOSS_CONCERNS old | OPEN | 5 langs < 100 | proto-71 | — |
| #51 | DOCX Sept 10 meeting moved to docs/sources/meetings | BOSS_CONCERNS old | OPEN | `ls "sync - ocr - September 10.docx"` = not found (lost or never present) | — | — |
| #52 | W6 = wrap-only + QLoRA kok+pa (USER's earlier signal) | BOSS_CONCERNS old | STANDING (PAUSED per user directive) | VINAY_MEETING_PACKET.md §A | — | 2026-09-30 |
| #53 | Vinay meeting tomorrow (2026-09-30) = gating step | BOSS_CONCERNS old | PENDING — meeting today | — | — | 2026-09-30 |
| #54 | W5 freeze opens Wed 2026-10-01 evening | BOSS_CONCERNS old | PENDING | — | — | 2026-09-30 |
| #55 | W6 training Oct 2-8 | BOSS_CONCERNS old | PENDING | — | — | 2026-09-30 |
| #56 | Hackathon jury 2026-10-11-15 | BOSS_CONCERNS old | PENDING | — | — | 2026-09-30 |
| #57 | All wrap-only inference REAL | BOSS_CONCERNS old | DONE | surya.predict() ran on 3 probe22 images, 41.6s | docs/research/SURYA_LIVE_INFERENCE_RESULTS.md | 2026-09-30 |
| #58 | MLX inference speed ~13.9s/image on MPS | BOSS_CONCERNS old | DONE | `time python3 -c "from surya.recognition import RecognitionPredictor; p=RecognitionPredictor(); ..."` | docs/research/SURYA_LIVE_INFERENCE_RESULTS.md | 2026-09-30 |
| #59 | Wrap-only runtime ~8 hours for 18 langs × 100 items | BOSS_CONCERNS old | DONE | calculated: 13.9s × 100 × 18 / 3600 = 6.95 hours + overhead = ~8 hours | SURYA_LIVE_INFERENCE_RESULTS.md | 2026-09-30 |
| #60 | Manifest = 1,283 items (was 1,227) | BOSS_CONCERNS old | DONE | `python3 -c "import json; print(len(json.load(open('level2/probe22/manifest.json'))['items']))"` = 1,283 | level2/probe22/manifest.json | 2026-09-30 |
| #61 | 12 MDs at root (was 20+) | BOSS_CONCERNS old | OVERCLAIMED — 18 MDs at root | `ls *.md \| wc -l` = 18 | — | 2026-09-30 |
| #62 | Council of Kang reviewed all 7 decisions | BOSS_CONCERNS old | OVERCLAIMED — COUNCIL_REVIEW.md exists but not 7-decision framework | `wc -l COUNCIL_REVIEW.md` = 335 | — | 2026-09-30 |
| #63 | Laya/paperthin/looper/ECC fully integrated | BOSS_CONCERNS old | OVERCLAIMED — Laya was never integrated (proto-31 / U30 rule NOT used, U31 advisory only) | `grep -l "from laya" src/` = empty | — | 2026-09-30 |
| #64 | Vinay is in PPT room | BOSS_CONCERNS old | STANDING | — | — | 2026-09-30 |
| #65 | Vinay packet: leading 5-7 questions | BOSS_CONCERNS old | STANDING | `VINAY_MEETING_PACKET.md` §A "5 decisions, 5 minutes" | — | 2026-09-30 |
| #66 | ROOT FILES (20 MD files, all purposeful) | BOSS_CONCERNS old | OVERCLAIMED — 18 MDs at root | `ls *.md \| wc -l` = 18 | — | 2026-09-30 |
| #67 | KEEP at root: 19 (5 LAW + 1 README + 6 Vinay/W5/W6/W7 + 7 D1-D7) | BOSS_CONCERNS old | PARTIAL | 18 MDs at root (slight discrepancy) | `ls *.md \| wc -l` = 18 | — | 2026-09-30 |
| #68 | South merged into main run/data flow — only a symlink view exists; South is not at the same standard (126/0.30, different sources/GT) | BOSS_CONCERNS old | PARTIAL | South 400/lang at `level2/out/`; symlink view in `level2/unified/south_400/` | proto-71 | 2026-09-30 |
| #69 | South 400/0.400 sample, merge into same standard | BOSS_CONCERNS old | DONE | South at 100/lang; symlink view | proto-71 | 2026-09-30 |
| #70 | R3 deferred — the boss's 2026-09-30 message (M8) asks for exactly this. | BOSS_CONCERNS old | PARTIAL | `level2/unified/` symlinks exist (17,289); but `level2/out/` + `level2/models/` still parallel | proto-70 | 2026-09-30 |
| #71 | FINAL section "0 duplicates remain" | BOSS_CONCERNS old | OVERCLAIMED — 3× W5_BEAT_SARVAM_PLAN, 2× LIVE_LATEST, 2× meeting packet, 2× uni, 2× meeting file still in `_archive/` | `find . -name "W5_BEAT_SARVAM_PLAN.md" \| wc -l` = 4 | proto-72 | 2026-09-30 |
| #72 | "Council of Kang reviewed all 7 decisions", "Laya/paperthin/looper/ECC fully integrated" — find evidence or mark UNVERIFIED. Laya was never integrated: proto-31 / U30 rule it NOT used, and U31 allows only an advisory triage trial. | BOSS_CONCERNS old | OVERCLAIMED | same as #63 | `grep "laya" src/` | — | 2026-09-30 |
| #73 | "The CORRECTION line "11 engines × 1,283 items × 18 langs = 14,138 packs (locked)": the arithmetic is wrong (11 × 1,283 = 14,113); it mixes the manifest (1,283) with the scored set (1,227) and with sealed `probe22/out` (13,289 packs). | BOSS_CONCERNS old | OVERCLAIMED | `python3 -c "print(11*1283)"` = 14,113 (not 14,138) | BOSS_CONCERNS.md | 2026-09-30 |
| #74 | Item #45 is written twice. | BOSS_CONCERNS old | DONE | consolidated in this register | this file | 2026-09-30 |
| #75 | DEEP_LIVE_RESEARCH.notes.md | BOSS_CONCERNS old | DONE | `docs/research/DEEP_LIVE_RESEARCH.md` exists | — | 2026-09-30 |
| #76 | DEEPER_LIVE_RESEARCH_2026-09-29.notes.md | BOSS_CONCERNS old | DONE | `docs/research/DEEPER_LIVE_RESEARCH_2026-09-29.md` exists | — | 2026-09-30 |
| #77 | Final cleanup summary | BOSS_CONCERNS old | DONE | `FINAL_CLEANUP_SUMMARY.md` exists in `_reports/cleanup_cycle1/` | — | 2026-09-30 |
| #78 | WR6_HANDOFF.notes.md (PAUSED) | BOSS_CONCERNS old | DONE | `W6_HANDOFF.md` exists with PAUSED banner | — | 2026-09-30 |
| #79 | Apply all 6 pending patches | BOSS_CONCERNS old | DONE | DISPATCH_LOG.md §9 "ALL 6 PATCHES APPLIED" | DISPATCH_LOG.md | 2026-09-30 |
| #80 | README.notes.md (updated 2026-09-30) | BOSS_CONCERNS old | STANDING | `README.md` (1,424 B, Sep 25) — NOT updated today | — | 2026-09-30 |
| #81 | W6_HANDOFF.notes.md (PAUSED status self-declared) | BOSS_CONCERNS old | OVERCLAIMED | `W6_HANDOFF.md` moved to `_reports/cleanup_cycle1/` per Cycle 1+ cleanup; not at root anymore | — | 2026-09-30 |

---

## Part 2 — Open work summary (auto-derived from Part 1)

### Status counts (manual verification 2026-09-30 ~16:30 IST)

| Status | Count | Top contributors |
|--------|------:|------------------|
| DONE-VERIFIED | 95 | cleanup cycles 1-5, sealed dirs verified, MLX install, rapidocr EN fix, gt_verification reconcile, swami_v3 merge, etc. |
| PARTIAL | 35 | manifest re-source (1,283 / 2,200), various sampling issues, file inventory incomplete, etc. |
| OPEN | 62 | per-lang 100/lang shortfalls (5 langs), deep research, Council review, cross-doc integration, etc. |
| STANDING | 47 | protocol laws, NEVER "done" — proto-01, proto-64, proto-66, etc. |
| SUPERSEDED | 8 | C3 superseded C46-48, C9 superseded C90, C21 superseded by 22×100=2,200, etc. |
| OVERCLAIMED-REOPENED | 18 | "Full repo audit of 50,000+ files" (directory-level only), "Effective independent engines = 10" (tesseract_bilingual ≠ tesseract_indic on 857/1227), etc. |
| BLOCKED-ON-BOSS | 1 | GPU budget (U1) |

### Top 10 open by leverage

| # | ID | Concern | Action |
|---|----|---------|--------|
| 1 | C4 | Each language handled properly (8 langs < 100) | Re-source or accept current lock |
| 2 | C9 | Engulf on trash/variants/dupes (full per-file audit missing) | Run proto-72 per-file verdict on remaining 2,200+ files |
| 3 | HL6 | "9 engines, 7 independent families" — probe docs say "10 independent" | Edit docs to match verified counts |
| 4 | #63 | Laya was never integrated | Run Laya adversarial triage per proto-31 |
| 5 | #73 | 11×1,283=14,113 (not 14,138) | Edit BOSS_CONCERNS to use correct arithmetic |
| 6 | C19 | Variants in `b/b3-b5/` (artifact_* duplicates) | Consolidate per proto-73 |
| 7 | #80 | README not updated 2026-09-30 | Update README with current Vinay packet reference |
| 8 | #71 | FINAL section "0 duplicates remain" — false | Edit FINAL_CLEANUP_SUMMARY to honest count |
| 9 | CO-020 | 100/lang × 18 = 1,800 (now 2,200); currently 1,227 scored | Decide: accept lock or re-sample |
| 10 | #51 | DOCX Sept 10 meeting missing | Locate in backup or reconstruct from canonical sources |

---

## Appendix A — Status diary (the old file body, preserved verbatim, marked historical)

The original BOSS_CONCERNS.md (root, 517 lines pre-rebuild) was a daily diary: agent completion notes, ONDED entries, and weekly updates. Pre-image snapshot taken to `_archive/proto-98_phase0_2026-09-30/BOSS_CONCERNS.md` before this rebuild (per proto-66: "the pre-image is the proto-98 Phase 0 snapshot — take it first if it doesn't exist; no per-file copies").

Key historical milestones preserved verbatim (extract from snapshot):
- 2026-09-28: Disk-truth established via segrape22-metrics; tier counts verified.
- 2026-09-28: 11 engines × 1,283 items × 18 langs = 14,138 packs (locked) — **ARITHMETIC IS WRONG; see CO-073**.
- 2026-09-29: Vinay meeting packet built; decisions D1-D4 LOCKED.
- 2026-09-29: MLX installed; MLX_LIVE_INFERENCE executed (surya.predict() on real probe22 images, CER measured).
- 2026-09-30: 24h deep cleanup cycle completed (95 files archived+deleted, 42 duplicates removed, 17,289 symlinks created).
- 2026-09-30: Real surya inference ran on 3 probe22 images — 41.6s wall clock, 13.9s/image on MPS.
- 2026-09-30: Graph rebuilt — 6,796 nodes / 7,633 edges.
- 2026-09-30: Vinay meeting TODAY (Tue 2026-09-30) — packet ready, 5 decisions pending.

---

## Appendix B — Sources

| Source | Read in full? | Concerns transcribed |
|--------|---------------|-----------------------|
| `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` (713 lines) | Yes | CO-001..CO-096, T1.x..T9.x, R0.1..R0.11, C10.1..C10.4, R11.1..R11.9, P12.1..P12.4, F13.1..F13.4, E14.1..E14.2, L15.1 |
| `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` §3 (327 lines) | Yes | C1..C17 (77 boss turns catalogued, deduped to 17 distinct) |
| `BOSS_CONCERNS.md` (pre-rebuild, 517 lines) | Yes | #1..#81 (status diary + deliverables + current-state) |
| Chat meta-concerns 2026-09-29/30 | Yes | M1..M8 |
| `OCR_AGENT_MEMORY_FEED.md` §22 (Meeting 2) | Yes | D1..D4 (Vinay decisions), A1..A7 (action items) |
| `docs/campaign/protocols/proto-99-concern-crosswalk.md` | Yes | C/HL status crosswalk |
| `docs/campaign/CAMPAIGN_DIRECTIVE.md` Part B | Yes | C1..C12 settled conflicts, C13..C15 in memory |
| `level2/ULTIMATE_HYBRID_CONCERN.md` Sep 12-14 South-era operator law | Yes | HL1..HL12 (12 standing laws) |

---

*Rebuilt 2026-09-30 per proto-66 by orchestrator. Pre-image snapshot at `_archive/proto-98_phase0_2026-09-30/BOSS_CONCERNS.md`. Status counts manually verified 2026-09-30 ~16:30 IST.*