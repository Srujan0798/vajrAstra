---
name: proto-104-project-first-critical-path
description: "THE ONE PLAN (rev 4, 2026-09-30 ~21:45 IST) — finish the project, win against every competitor, ship a PORTABLE Vaultstack product (MLX = Mac dev convenience only); South re-built from Sarvam-bench fill (0/23,001 official South PDF pages clean); the official test set is handwritten words → handwriting track; external bench on all 22 languages; night-run rules; tools-in-use; one-line paste lines. Rev 1–3 text kept below as HISTORY."
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
---

# PROTO-104 (rev 4) — THE ONE PLAN: finish it, win it, ship it portable

**Understood as (readchk, 2026-09-30 ~21:40):** the boss wants the other session's final plans (verdict, handoff v2, the Mac overnight plan) folded into OUR plan — not a switch to its A0–A10 roster. His 3 agents do all labour; the planner writes protocols; no subagents; no team mates. The product must beat all competitors and run anywhere, not only on this Mac.
**Skills used for this revision:** readchk · factchk (bench card + metrics.py on disk, Sarvam blog fetched) · mandela (bench fairness) · ssotize (rev 1–3 merged here; the old text is kept below as HISTORY, nothing deleted) · verification-before-completion at the end.

## 0. Goal and hard boundaries (the boss, 2026-09-30)
- **Win.** Beat Sarvam Vision 2.1 (87.39 overall on its own bench; its weak cells: Santali 53.91, Kashmiri 54.82, old scans, Odia 80.01) and every open model (Bodhan 84.94, Chitrapathak-2, Gemini 3.6 Flash 79.35, surya 69.96).
  - "At any cost" means effort, compute (Vinay's 24 GB GPU) and depth.
  - It never means breaking the law: no leakage, no fake claims, no unapproved downloads or Sarvam spend, sealed dirs read-only.
- **A portable Vaultstack product.** It goes to the organisers and then to everyone.
  - The SHIPPED system runs on standard hardware: Linux + PyTorch/transformers (CUDA GPU, CPU fallback), a pinned requirements file, a Docker image.
  - **MLX is a local accelerator on this Mac only** — never a product dependency, never the only path for a result we claim.
  - Bodhan in the product = the OFFICIAL `bodhan-ai/indic-ocr` weights, not the third-party MLX ports.
  - LoRA for the product is trained with PEFT on CUDA (Vinay's GPU). An MLX-trained adapter counts only after it is converted AND a parity check on the PyTorch model passes.
- **What the product does:**
  - handwritten + printed + degraded Indian-language documents → layout JSON (the SOUTH_CANON §G page schema: L0 meta, L1 regions with bbox/reading order/modality, L2 NFC text + provenance/tier);
  - a searchable PDF;
  - per-block language/script;
  - offline, 22 languages + English.

  This is the Sep 10 proposal's promise (SOUTH_CANON §A) and the official focus areas (RQ-1).
- **Free only.** Sarvam free credit ₹67 left. **No team mates:** [[feedback-no-team-mates]]. **Vinay:** fold in his inputs when they arrive; the only gate he owns is the plan session before training (L12).

## 1. Measured facts this plan stands on (evidence; re-verify before quoting)
- **The official test set** `Datasets/akshardrishti_official/test/test/`: 5,344 JPEG word crops, 296–300 px tall, IDs 0–14806.
  - The planner viewed 10001/12407/1361.jpg: each is ONE HANDWRITTEN Bengali-script word in blue pen.
  - The script mix across all buckets is UNKNOWN until H1.
  - `TEST_SET_PROFILE.md`'s heuristic numbers are REJECTED (R-11).
- **Labelled handwriting on disk:** `Datasets/akshardrishti_official/Bodo/gu/` — Gujarati handwritten words, IIIT-HW format: train.txt 82,563 · val.txt 17,643 · test.txt 16,490 lines (`path, vocab-index`), vocab 10,963. Only 4,645 images are on disk (under `test/test/`).
- **South official PDFs:** 0/23,001 pages pass the gates (76% legacy-font encodings) — `W_south_reports/SOUTH_RERUN_FEASIBILITY.md` + `S1_real_feasibility.json`.
- **Sarvam indic-ocr-bench, downloaded** (rev 84ce7ce4; at `level2/models_bodhan/indic-ocr-bench/`, not git-ignored yet):
  - Apache-2.0; "reviewed twice by human language experts"; 6,909 test items (block crops); small_representative 1,173 (51 per language).
  - Per language: as 471 · bn 271 · brx 238 · doi 319 · en 300 · gu 300 · hi 228 · kn 300 · ks 262 · kok 266 · mai 279 · ml 300 · mni 207 · mr 300 · ne 437 · or 300 · pa 300 · sa 325 · sat 274 · sd 248 · ta 299 · te 300 · ur 385.
  - Headline metric = **Word Accuracy = 100 × (1 − WER)** after `--normalize` (NFKC→NFC, quote/dash/Indic-punctuation folding); runaway-repetition outputs are flagged and excluded (README lines 103–149; metrics.py stdlib-only). → RQ-7 ANSWERED.
- **Sarvam Vision 2.1** (blog, dated Sep 24 2026, fetched 2026-09-30): overall 87.39; olmOCR-Bench 87.3; SFT then RLVR; ta 87.70 · te 91.55 · ml 90.24 · kn 90.54 · bn 93.47 · hi 93.52.
  - The other session's South numbers (ta 93.42, te 87.70, ml 91.60, kn 89.89, "character accuracy") are WRONG — do not use them.
- **Our state:**
  - benchmark = 18 languages + en (1,283 items); South absent;
  - `product/` layer exists (schema, cli, pdf_writer, script_id, tesseract + bodhan recognisers);
  - Bodhan weights: 403 for Maya0769 (gated=auto → the access form was never submitted from that account);
  - mlx 0.32.3 + mlx-vlm 0.7.4 installed;
  - our Sarvam probe calls went through the doc-ai digitise API; the served model version is not recorded (the South v1 adapter says "sarvam-vision-1.5").

## 2. Rulings (binding; R-1…R-6 from rev 2, R-7…R-11 from rev 3, new R-12…R-15)
- **R-1** South v1 (`level2/out`) is not valid for the 22-language table. Retire it only after the new South is scored (S6), local only (git keeps history), no push.
- **R-2/R-3** The `run_probe.py` base-path fix is an approved path erratum. A4 PASS = 0 old-path hits in `run_probe.py` + the smoke test passes; the 13 RETIRED-SOURCE hits are exempt until S6.
- **R-4** Bodhan Day 1 does not wait for A4. **R-5** Installs allowed for Day 1: mlx + mlx-vlm (done). Nothing else without the boss.
- **R-6** No commit/push/merge/issue edits without the boss. PR #12 stays a reference.
- **R-7** South GT = Sarvam-bench fill, drawn exactly like the 158 existing sarvam_fill items, ≤100 per language, seed 20260926, evaluation-only forever.
- **R-8** Sarvam on South: 3 per language = 12 calls (free credit, ≈₹6); record the SERVED model version from the API response; one DISPATCH_LOG line per call.
- **R-9** No team mates. **R-10** Nothing waits on Vinay except the pre-training session. **R-11** Heuristic test-set profile rejected.
- **R-12 (mandela) — Bench fairness:**
  - Every item from Sarvam's bench is tier `sarvam_bench`, reported SEPARATELY; it never enters an "overall" number without the tier breakdown.
  - Sarvam's own scores on its bench (and our 12 calls) are "home bench — possible training exposure".
  - A claim "we beat Sarvam" needs BOTH: the published split + scorer (`metrics.py --normalize`, the test split, the valid-sample count), AND a win on an independent set (the official human pairs bn/hi/sa, the official handwriting slice).
  - Gate 1's bench check proves reproducibility only; its 300-human-pairs check is the independent quality check.
- **R-13 — Portable product (the boss 21:3x):**
  - see §0; every result we claim must reproduce on the PyTorch path;
  - the MLX-vs-PyTorch parity number is logged when both run;
  - shipped weights = official repos with licences recorded (Bodhan: attribution + §3.2 internal-component shape; hosting needs §3.1 approval).
- **R-14 — Environments:**
  - `.venv311` (Python 3.11.10: torch, transformers, surya, paddleocr, easyocr, pytesseract, datasets, jiwer, pandas, pyarrow, fitz, mlx, mlx-vlm) = THE env for engines, scoring, bench, data prep;
  - `.venv` (Python 3.14.3) = only what already runs there, never mixed into a result without saying so;
  - `product/` gets its own pinned `requirements.txt` + a Dockerfile targeting Linux/CUDA (step D4).
- **R-15 — Night runs** (adopted from the other session's Mac plan; applies to every job > 30 min):
  - `caffeinate -dimsu` + `nohup`/tmux, charger in; stop if free disk < 20 GB;
  - resumable only: one output file per item, `--skip-existing`, progress in `level2/benchmark/logs/RUN_STATE/<job>.json` (done/total/last item/machine/start/last-update);
  - every output tagged `device` (`mac-m4-cpu` / `mac-m4-mps` / `gpu-24gb`); never mix timing across machines;
  - heartbeat line every 5 min; a 10-min stall → kill and resume;
  - at the end, `level2/benchmark/logs/RUN_STATE/HANDOFF.md`: done / in progress (resume command) / not started / needs-GPU.

## 3. The steps (owner → output → done-when)
- **R (Agent 2):** A4 (R-2/R-3) → A5 → LAYOUT FROZEN.
  - Plus: add `level2/models_bodhan/` to `.gitignore`;
  - move the root strays `out_level3/` + `W4_reports/` into `_archive/stray_2026-09-30/` with a log line.
- **S (South):**
  - **S2 — Agent 3:** draw per R-7; `manifest_v2.json` + crops into `level2/benchmark/`; NEW files only; post the run list.
  - **S3 — Agent 2:** verify (10 per language viewed, counts, leak check).
  - **S4 — Agent 1:** all local engines on South (R-15 rules) + the 12 Sarvam calls (R-8).
  - **S5 — Agent 2:** score with the same scorer, tiered (R-12); regenerate BENCHMARK_22.
  - **S6 — Agent 2 + the boss's guard clicks:** retire v1.
- **H (Handwriting — the test set says this matters most):**
  - **H1 — Agent 1, now, read-only:** profile `test/test/` properly (≥10 images per ID bucket, viewed with a vision-capable model or script-read by an engine); map `Bodo/gu`; search `Datasets/` for any other handwriting set.
  - **H2 — Agent 2:** a labelled handwriting eval slice `official_hw` (writer/page-disjoint from any training split) into `level2/benchmark/`.
  - **H3 — Agent 1:** Bodhan handwriting mode + surya/Tesseract on H2 → the handwriting baseline.
  - **H4 — Day 3:** B-19 handwriting LoRA (PEFT on CUDA; train split only; eval on H2). Public Indic handwriting sets (proto-105 C2-3) need licence checks + the boss's download approval.
- **D1 (Agent 1, the moment Bodhan downloads):**
  - official `bodhan-ai/indic-ocr` on the PyTorch path (the product path; CPU/MPS tonight, CUDA tomorrow) AND the MLX port (speed); parity logged (R-13);
  - `--sample 100` + `--pair-only` first → BODHAN_BASELINE.md → Gate 1.
- **X — External bench, all 22 languages + en (adopted from the other session's "A9"; Agent 1 after S4; R-15 rules):**
  - every local engine + Bodhan on the bench `test` split (6,909), block crops, no layout step;
  - scored with the bench's own `metrics.py --normalize`;
  - per-language table beside Sarvam 2.1's published numbers (§1) and Bodhan's 84.94, labelled "Sarvam's own bench (home advantage)" (R-12);
  - an engine × language coverage matrix: honest-empty cells where an engine has no model for the script;
  - order: tesseract family → rapidocr → doctr → easyocr → surya last; paddle and any VLM candidate on the GPU tomorrow.
- **C — Consensus** → [[proto-105-consensus-results-to-decisions]] (Agent 2).
- **G — Plan v3 draft (Agent 2):**
  - `docs/campaign/DRAFT_RESEARCH_PLAN.md`: the flowchart first;
  - then each PPT stage (SOUTH_CANON §A) → the v3 choice → evidence:
    - Stage 1 DocLayout-YOLO/IndicDLP → Bodhan IndicDocLayout (PP-DocLayoutV3 + reading order);
    - Stage 2 Qwen 3.5 VL SFT → Bodhan IndicBlockOCR (Qwen3.5-0.8B) + LoRA;
    - Stage 2b SCST/RL on CER → GRPO with a CER reward, last and optional;
    - Stage 3 LLM noisy-text→JSON → post-correction (B-18) + the §G JSON writer;
  - the handwriting finding; South; the bench fairness rule; Consensus rows; Day-1 numbers.
- **GPU (Agent 1 when the SSH details arrive):**
  - clone code only; data by rsync (never GitHub); keys in env vars only;
  - `.venv311`-equivalent env with CUDA builds;
  - continuity check: rerun 1 item per language per engine already run on the Mac, diff, record;
  - then paddle + the VLM candidates (dots.ocr, PaddleOCR-VL 1.6 — downloads need the boss), official Bodhan under vLLM/transformers, the PEFT LoRA runs (after Gate 2.5), and a one-machine latency table.
- **D2 → D3 → D4 → D5:** as rev 1–2 (leak-free split + audit → LoRA after Gate 1 + Gate 2.5 + D2 → product integration: Bodhan + fallback + post-correction trial B-18 + a 50-image dry run of the handwritten test images + `product/requirements.txt` + Dockerfile (R-13/14) → proof: re-score from scripts, pitch).
- **PARKED:** all cleanup (proto-95/96/98, proto-101 P0/P2/P5/P6/P7, 72–74/77/84/63/66, proto-102 A6/A7/A8/A10, most of Part B), GitHub housekeeping (PR #12, issues).

## 4. Tools — who uses what (full status table: [[proto-88-skill-routing]] §STATUS)
- **graphify: USED, but stale:** the graph is from 14:34; the Claude skill is 0.9.45 vs package 0.9.65. Refresh: `graphify install --platform claude` (planner), then Agent 2 runs `graphify update .` once after LAYOUT FROZEN, and uses `graphify query "<question>"` for navigation.
- **ECC: USED.** OpenCode (217 skills): `verification-loop` before any "done", `council-multi-model` for Gate 2.5, `deep-research` for proto-105 papers, `benchmark-methodology` + `eval-harness` for X/H2, `gateguard` before moves/deletes, `unified-memory` for handoffs. Claude: the ECC plugin + the `ecc-memory` MCP.
- **Laya: NOT used** in the pipeline (text-only classifier, cannot read images; proto-31). Its file-triage trial is parked with the cleanup.
- **Consensus: USED**, 3 per day; results in `docs/sources/consensus/` → proto-105.
- **paperthin** (anti-slop on the plan draft) and **looper** (long-run monitoring) in OpenCode: USED in G and in the night runs.

## 5. The boss's actions
1. **Hugging Face, account Maya0769** (the check at 21:3x still says "not in the authorized list"). In the browser, top-right avatar must show **Maya0769**. Open each of the 3 pages → fill the short form → submit. gated=auto, so access is instant:
   - huggingface.co/bodhan-ai/indic-ocr
   - huggingface.co/hari31416/indic-ocr-mlx-4bit
   - huggingface.co/hari31416/indic-ocr-mlx-bf16

   The first one matters most (the portable product path). Then tell Agent 1 "Bodhan access granted".
2. When Vinay sends the SSH details: paste them into Agent 1's GPU step. Keys and passwords go into env vars on the server, never into chat logs or the repo.

## 6. Paste lines (one agent at a time)
1. **Agent 2:** `Read docs/campaign/protocols/proto-104-project-first-critical-path.md (rev 4 — the top section only). Do step R now (A4 under R-2/R-3, A5, LAYOUT FROZEN, .gitignore level2/models_bodhan/, root strays to _archive/stray_2026-09-30/), then S3 when Agent 3 posts, then proto-105, then G. Use verification-loop before every PASS line.`
2. **Agent 3:** `Read proto-104 rev 4 (top section). Do S2 under R-7 (South from the Sarvam bench, drawn exactly like the 158 sarvam_fill items, ≤100/lang, seed 20260926, NEW files only), post the run list in DISPATCH_LOG, then stop and report.`
3. **Agent 1:** `Read proto-104 rev 4 (top section). Now: H1 (real test-set profile, read-only). Then S4 when Agent 3 posts (R-15 night-run rules, 12 Sarvam calls per R-8), then X (external bench, all engines, R-12 labels). The moment Bodhan access works: D1 with the OFFICIAL weights on the PyTorch path plus the MLX port, parity logged (R-13).`

## 7. From the other session — dropped, and why
- "South sealed, never merged": the boss ordered the merge (R-1).
- The A0–A10 roster and "done = pushed PR": we use 3 agents, and done = command output in W4.md (R-6).
- "Confirm scope with Vinay" and a "correction note for Vinay/David": no team mates. The Sep-16 correction goes to Vinay only, after Agent 2 reproduces it.
- Its South Sarvam numbers: wrong (§1).
- "Keep the ₹67 for old pages": superseded by R-8.
- Laya as a router: not possible (text-only).
- Code-execution rewards and best-of-8 without a verifier: no fit to our documents.

---

# APPENDIX A — merged protocols (verbatim; sources archived to `_archive_2026-09-30/`)

- **Step Q (new, before D2):** write `level2/benchmark/docs/GT_DEFECTS.md` per A.1 (proto-65); K-19 closes on it.


## A.1 — proto-65-gt-defects-register (verbatim)

# PROTO-65 — GROUND-TRUTH DEFECTS REGISTER (Verdict builds; decisions go to the boss) → `docs/campaign/GT_DEFECTS.md`

**Why:** GT defects are scattered across 1A, 1B, EDGE_THESIS, gt_forensics.json, gt_verification.json and the feed. Every score is only as good as its GT; the boss needs
one list with scope and decisions. §6.4 stays LOCKED — this register proposes, the boss decides.

## Known entries to verify and measure (starting list)
| ID | Defect | Source | Scope to measure |
|---|---|---|---|
| G1 | Marathi PDF-layer GT with injected Ol Chiki code points; the 18 items are table pages (7.4× Latin, 7.9× digits) | EDGE_THESIS C4, lens reports | count items; CER with/without them per engine |
| G2 | `gt_thin` threshold: 179 chars (CER_BY_SCRIPT.md, docs) vs 200 (code, 3 places) | BENCHMARK_22 UNRESOLVED #2 | which value ran; how many South pages change basis |
| G3 | te_024 / te_065 dominant script: `pages_script_map.json` vs `pages_manifest.json` disagree | BENCHMARK_22 UNRESOLVED #3 | Telugu scored n = 6 or 4 |
| G4 | ne PDF-tier BARRED (R5: ctrl chars, trust 26.6) | gt_forensics.json | unchanged — confirm |
| G5 | `sarvam_bench` fill GT is human-reviewed twice (HF card) — contradicts protocol's "machine GT"; §6.4 BARRED mni/sat partly on an LLM-vision verifier that cannot read Ol Chiki/Meetei Mayek | COMPETITOR_INTEL §0.1; gt_verification.json | which §6.4 verdicts depend on the "machine GT" premise → U6 |
| G6 | PDF-text-layer GT may favour layout-literal engines | [[proto-62-gt-tier-stratified-reporting]] | result of the 30-item classification |
| G7 | `sheet.csv` gt column vs manifest gt byte equality | [[proto-61-sheet-provenance-forensics]] step 2 | mismatch count |
| G8 | South 274/400 pages without CER (219 thin GT, 55 mojibake) | CER_BY_SCRIPT.md | per language |
| G9 | Items whose GT came from the same source Sarvam built its bench on (sarvam_bench) — potential home-turf for Sarvam | manifest `gt_source` | count per language; exclude-or-flag rule for comparisons |

## Verdict subagent — TASK (paste after the shared context block)
> For each entry: reproduce the defect with a command, measure its scope (items, languages, engines affected, effect on mean CER with/without), classify
> SEVERITY (changes a winner / changes a number / cosmetic), and write the decision it needs (boss / Verdict / none). Add any new defect you find while measuring.
> Write only `docs/campaign/GT_DEFECTS.md`: summary (≤10 lines) → register table → per-entry evidence → decisions list.

Related: [[proto-61-sheet-provenance-forensics]], [[proto-62-gt-tier-stratified-reporting]], [[proto-92-boss-decisions]]


## A.2 — proto-71-south-rerun-same-standard (verbatim)

# PROTO-71 — SOUTH LANGUAGES UNDER THE SAME STANDARD (feasibility by Engine → boss gate U11 → execution)
> **2026-09-30 evening:** the execution order, owners and end state are in [[proto-101-south-unification-and-level2-tree]] (U10/U11 now). This file stays the reference for its inventory and path-dependency lists.

**Why:** the boss's own words: CO-003 "merge into new **or run them fresh in the same flow**"; CO-025 "rerun under the same standard — delete old versions";
uni T6.4 "THE SOUTH LANGUAGES meet this exact same bar — same 100-per-language standard, same verification, no leftovers from older standards."
Today South = 400 self-labelled pages from other sources (Level 1 `arc_level_1/labeled/`, sources like S5_govt), rendered at a different basis, scored by a different writer
(`verify_v2.py`), and **only 126/400 pages carry a CER** (kn ≈4, ml ≈4, te ≈6 scored). The 18 other languages come from the official hackathon dataset through
`level2/probe22/` (extract_gt gates → build_manifest → run_probe → metrics). A symlink view cannot fix a standards difference.

## Official-dataset sources for the 4 languages (monitor, 2026-09-30)
`Datasets/akshardrishti_official/`: Tamil 34 PDF + 4 PNG · Telugu 84 PDF · Kannada 41 PDF · Malayalam 20 PDF + 9 PNG. No image+transcription pairs.
Unknown: how many PDF pages pass the honesty gates (Gujarati: 3,567 text pages → 10 clean because of legacy font encodings — South PDFs may behave the same).

## Phase A — feasibility (Engine subagent, read-only except candidate files in a scratch folder)
> 1. Check `level2/probe22/extract_gt.py` and `build_manifest.py` language tables: do they support `ta`, `te`, `kn`, `ml` (script Unicode ranges, codes)? If not, list the exact
>    additions needed (do not edit yet).
> 2. Run the extract stage for the 4 languages writing ONLY to `docs/campaign/checkpoints/W_south_reports/candidates_<code>.json` (copy the script to a scratch path or pass an output
>    flag — never overwrite `level2/probe22/candidates/`). Report per language: PDFs, pages scanned, pages with text, rejected by reason, clean candidates, distinct PDFs among clean.
> 3. Engines: which of the 10 local engines support each script? Tesseract traineddata for `tam`, `tel`, `kan`, `mal` — `level2/probe22/tessdata/` has none; find what the South run used
>    (`level2/engines_config.py`, `run_engine.py`, system tessdata e.g. `/opt/homebrew/share/tessdata`, `level2/research/smoke/anuvaad_tesseract/tessdata`). `run_probe.py` (LOCKED) language map:
>    does it route ta/te/kn/ml? List exact edits needed. No downloads.
> 4. Time estimate: per engine ms/page from `level2/reports/LATENCY.md` and probe logs × 400 items.
> 5. Write `docs/campaign/SOUTH_RERUN_FEASIBILITY.md`: per language clean-candidate count vs 100, engine coverage, required code edits (with file:line), time, risks, recommendation.

## Boss gate U11 — APPROVED 2026-09-30 ("Yes, feasibility first"): run Phase A, then Phase B for every language the feasibility report marks feasible; report the rest
Present: feasible yes/partial/no per language; edits to LOCKED files needed (`run_probe.py`, possibly `AGENT_PROTOCOL.md` scope); compute hours; what happens to old South 400
(recommended: becomes `benchmark/scores/south400_v1/` history + `_archive/level2_south400_v1/`, cited as "Level 2 v1 (own-labelled, different standard)", never mixed into the 22-language table).

## Phase B — execution (only after U11 yes)
1. Add the 4 languages to extract/build/run tables (fix-specs, Verdict-verified). 2. Extract → draw 100/lang with the same seed and stratification (SEED 20260926), same gates.
3. Run all local engines one at a time (AGENT_PROTOCOL engine discipline), outputs into the probe output tree (or `benchmark/packs/` after proto-70). 4. Score with the same `metrics.py`.
5. Regenerate `BENCHMARK_22.md` so all 22 languages share one standard; old South numbers shown only in a clearly labelled history section.
6. Where a language cannot reach 100 clean pages: record the honest n and why (same rule as the 8 short languages; no gate relaxation, no fabrication).

## Verdict check
Visual spot-check of 10 drawn pages per language (GT vs image), gate statistics reproduce, engine outputs complete (counts per engine × lang), no sealed/locked file edited without the approved fix-spec.

Related: [[proto-70-level2-restructure]], [[proto-20-w2-sampling-reconcile]], [[proto-21-w2-variance-and-resource]], [[proto-92-boss-decisions]]


## A.3 — proto-75-vinay-plan-baseline (verbatim)

# PROTO-75 — BASELINE AGAINST VINAY'S PLAN (research + Verdict) → `docs/campaign/VINAY_PLAN_BASELINE.md`

**Boss:** CO-089 "First benchmark/analysis: baseline against VINAY'S plan — we must cross his plan to even cross Sarvam and the entire India model field." uni C10.3: "full analysis of
EVERY relevant model — starting with VINAY'S PLAN… Prove it with analysis, not confidence." CO-090 is superseded by C9 (prove, then claim).
Note: Vinay is the CEO of the boss's own team; his PPT is the team's baseline architecture — "crossing" it means a demonstrably better plan he will adopt, not a rivalry.

## Inputs
`AksharDrishti_Hackathon_Proposal.pptx` (root) · `docs/research/…/PPT_FULL_DUMP.md` and `PPT_VS_SPEC_DIFF.md` (now under `_reports/research/`; use `find`) · `docs/architecture/PPT_SPEC.md` ·
`docs/campaign/BENCHMARK_22.md` · `docs/campaign/COMPETITOR_INTEL.md` · `docs/campaign/EDGE_THESIS.md` · `docs/campaign/MENTOR_PLAYBOOK.md` (flowchart) · research precursors
(`docs/research/R1_SOTA_MECHANISM_TEARDOWN.md`, `DEEPER_LIVE_RESEARCH_2026-09-29.md`, `LIVE_LATEST_2026-09-29.md`).

## Research subagent — TASK (paste after the shared context block)
> 1. Decompose the PPT architecture into its stages exactly as written (quote slide text): preprocessing (OpenCV), layout (DocLayout-YOLO), recognition (parallel SFT TrOCR + Qwen-VL + PaddleOCR-VL),
>    training (SCST/RL), data plan, evaluation plan, languages covered.
> 2. For each stage: (a) what we have measured on disk that bears on it (engine CERs by script and GT tier, failure taxonomy `level2/reports/FAILURE_TAXONOMY.md`, latency);
>    (b) what 2025–2026 evidence says (open the sources; e.g. current small OCR VLMs, layout models, RL for OCR) — PRIMARY/DERIVED/UNKNOWN;
>    (c) risk for Indic specifically (conjuncts, Nastaliq, Ol Chiki, Meetei Mayek, degraded scans); (d) what the plan omits (e.g. script/language ID for unlabelled test images,
>    confidence routing, normalisation aligned to the evaluation metric, 22-language coverage).
> 3. A comparison table: stage × {Vinay PPT, Sarvam Vision 2.1 (published architecture), Bodhan, our measured wrap-only routing, Option A, Option D} with evidence per cell.
> 4. "What crosses his plan": the smallest set of changes to the PPT that the evidence supports, each with its measured or cited basis and cost in days. No claim without evidence.
> Write only `docs/campaign/VINAY_PLAN_BASELINE.md` (≤2,000 words + tables).

## Verdict check
Every PPT quote verbatim; every cell sourced; "crosses" claims labelled as hypotheses unless measured.

Related: [[proto-19-w1h-draft-research-plan]], [[proto-14-w1d-competitor-intel]], [[proto-78-submission-readiness]]


## A.4 — proto-76-workstreams-and-agent-health (verbatim)

# PROTO-76 — WORKSTREAMS AND AGENT HEALTH (Miss, read-only) → `docs/campaign/WORKSTREAMS.md`

**Boss:** uni T8.1 "Every stream checked every cycle. Silence from a stream = flagged event, not peace." T8.5 "Find the boss's other parallel workstreams, read their concern docs, confirm none
stalled." C15 "you have 2 parallel works — see one you have done, what about the other." Monitor 2026-09-30: 3 OpenCode processes (since 07:29, 18:56, 21:02 on 09-29), Claude daemon sessions,
`.kilo/worktrees` (31 MB), untracked `src/`+`tests/` written by an unknown agent, a cleanup agent that moved 27 docs, and duplicates created "for discoverability".

## Miss subagent — TASK (paste after the shared context block)
> 1. Processes: `ps aux | grep -E 'claude|opencode|kilo|python' | grep -v grep` (start time, command, cwd via `lsof -p <pid> | grep cwd`).
> 2. OpenCode sessions (read-only MCP): ToolSearch `select:mcp__opencode__opencode_sessions_overview,mcp__opencode__opencode_session_list,mcp__opencode__opencode_session_get`;
>    list sessions for this repo, their titles/last activity; summarise what each is doing (do not send them messages).
> 3. Claude sessions: `ls -t ~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl | head` → title (ai-title rows) + last timestamp (small python, never cat).
> 4. Kilo: `git worktree list`; for each `.kilo/worktrees/*` branch, last commit date and whether it has unmerged changes.
> 5. Attribution: for files created/modified in the last 48 h outside `docs/campaign/`, attribute to a workstream (timestamps vs session activity; DISPATCH_LOG entries).
> 6. Write `docs/campaign/WORKSTREAMS.md`: table `workstream · tool · started · last activity · task (from its own log/title) · files it writes · status ACTIVE / IDLE / STALLED / CONFLICTING ·
>    owner lane (Engine/Verdict/Miss/boss) · action needed`. Flag every CONFLICTING pair (two streams writing the same files) and every STALLED stream.

## Standing rule (add to every wave's pre-flight)
Every workstream registers in `DISPATCH_LOG.md` before it writes (who, what files, until when). Unregistered writers are reported to the boss the same turn.

Related: [[proto-60-monitor-and-checkpoint-discipline]], [[proto-74-root-hidden-hygiene]], [[proto-02-preflight-and-checkpoints]]


## A.5 — proto-78-submission-readiness (verbatim)

# PROTO-78 — SUBMISSION READINESS (Engine builds, Verdict verifies; gated on U2 for format)

**Why:** uni E14.2 "COMPLETE the project". `Datasets/akshardrishti_official/test/test/` = 5,344 unlabelled JPGs (numbered `0.jpg`…), described in `FULL TECHNICAL BRIEFING.md:37` as the
hackathon eval set — "NEVER train on it". `docs/research/R6_COMPETITION_INTEL.md:62` "Submission format — NOT published". Every plan so far routes by a KNOWN language label (per-language
routing table); the test images carry no label → the pipeline needs script/language identification first. No protocol covered this.

## Step 1 — requirements (Miss) → `docs/campaign/SUBMISSION_REQUIREMENTS.md`
Collect everything known about the submission: output format, metric, languages in test, deadline, page vs block unit, file naming. Sources: official hackathon pages (live, opened),
`SOUTH_CANON.md`, `FULL TECHNICAL BRIEFING.md`, `R6_COMPETITION_INTEL.md` §4, `_reports/research/VAJRASTRA_INTERROGATION_PROTOCOL.md` F1, the boss (U2). UNKNOWN is allowed; list questions for the boss/Vinay.

## Step 2 — test-set profile (Engine, read-only, no training, no labels created)
Sample 200 test images (seed 20260926): image sizes, colour/greyscale, printed vs handwritten (visual check of 30), and **script distribution** estimated by running the existing engines'
script detection or a Unicode-block vote over 2–3 fast engines' outputs on the sample. Output `docs/campaign/TEST_SET_PROFILE.md`. Never write predictions for the test set into any training asset.

## Step 3 — pipeline dry run (Engine)
For the chosen path (U4): script/language ID → route → engine(s) → normalisation → output writer in the (assumed) format. Run on 50 test images: wall time per image per engine on this Mac,
failure modes, memory. Extrapolate to 5,344. Output `docs/campaign/SUBMISSION_DRYRUN.md` with the exact command, timings, and the gap list (e.g. no engine for Ol Chiki/Meetei Mayek → U7).

## Verdict check
No test image used for training or tuning; timings reproducible; format assumptions labelled ASSUMED until U2 confirms.

Related: [[proto-75-vinay-plan-baseline]], [[proto-51-w5-architecture-freeze]], [[proto-92-boss-decisions]]


## A.6 — proto-80-hackathon-metric-alignment (verbatim)

# PROTO-80 — A COMPLETE, DEFENSIBLE METRIC SET (Engine writes the writer, Verdict verifies)

**CORRECTION 2026-09-30 (factchk, Opus): the sentence "CER with a bootstrap 95% CI, WER, substitution/deletion/insertion breakdown, and seconds per page" comes from a student B.Tech project repo (github.com/Ayush-04-spec/akshardrishti, K. K. Wagh Institute) describing ITS OWN evaluation — it is NOT the official AksharDrishti rubric. The official scoring rules are UNKNOWN (not found on any opened official page). Never state them as the hackathon's rules; ask Vinay/the organisers (U2).**
The metric set below is still worth building: confidence intervals, error-type breakdown and speed are what any serious reviewer asks for, and speed matters for a 5,344-image test set.

**Evidence withdrawn:** the rubric quote previously here was from a student project (see correction above). Official rules: UNKNOWN — U2.
**Gap:** `docs/campaign/BENCHMARK_22.md` has mean/median CER but no bootstrap CI, no S/D/I, no seconds/page. Law L2 (one writer, one truth) and L9b (freshness stamped): numbers come from a script, never by hand.

## Engine subagent — TASK (paste after the shared context block)
> Write `level2/unified/rubric_report.py` (stdlib + `level2/probe22/metrics.py` only; deterministic; `generated_at` stamp) producing `docs/campaign/RUBRIC_REPORT.md`:
> 1. For every engine × language (and overall, and per GT tier per proto-62): n, CER mean, **CER bootstrap 95% CI** (1,000 resamples over items, seed 20260926; report the method),
>    CER median, **abstention rate** (empty predictions; see proto-82 table), WER, and **S/D/I counts and rates** from the character alignment (edit-operation breakdown; if `metrics.py`
>    has no op breakdown, implement Levenshtein backtrace and test it on 5 hand-checked pairs).
> 2. **Seconds per page** per engine: from run logs (`level2/probe22/logs/`, `engine_health_log.jsonl`, pack JSON `engine_meta` timing fields) and South `level2/reports/LATENCY.md`;
>    state n timed and the hardware (Apple M2 Max). Never re-run engines for timing in this step.
> 3. Input CER source: `sheet.csv` (v1) and, if present, `level2/unified/sheet_v2.csv` from proto-61 — report both side by side until U9 decides.
> 4. Consistency: overall numbers must reproduce `BENCHMARK_22.md` means within rounding; print PASS/FAIL.
> Writes only the script and `docs/campaign/RUBRIC_REPORT.md`.

## Verdict check
Re-run; hand-check S/D/I on 5 items; check CI width is plausible for n (e.g. n=3 Sarvam cells must show very wide intervals); confirm no hand-typed numbers.

Related: [[proto-12-w1b-benchmark22]], [[proto-61-sheet-provenance-forensics]], [[proto-62-gt-tier-stratified-reporting]], [[proto-82-engine-empty-output-patterns]]


## A.7 — proto-81-handwriting-degraded-coverage (verbatim)

# PROTO-81 — HANDWRITING + DEGRADED-DOCUMENT COVERAGE (Engine measures, Verdict checks, boss decides scope)

**Facts (monitor 2026-09-30):** `level2/probe22/manifest.json` → `print_or_hand`: printed 1,283 · `has_table`: False 1,283 · `quality`: unknown 983, clean 300. `sheet.csv` `mixed_script` False on all rows.
Search summaries say the AksharDrishti challenge targets "handwritten and low-quality texts" — UNVERIFIED (the official page could not be opened; the X post returns HTTP 402). The test-set profile (step 2) is the independent truth. Sarvam's bench is reported as 0% handwriting / 0% tables (COMPETITOR_INTEL). Bodhan publishes
a handwriting bench (IndicOCR-HW) per 1D. So neither our probe nor Sarvam's bench measures what the hackathon emphasises. It is unknown whether these fields were measured or defaulted.

## Engine subagent — TASK (read-only; no training; no labels created for the test set)
> 1. **Field provenance:** find where `print_or_hand`, `quality`, `has_table` were set (`build_manifest.py`, `extract_gt.py`) — measured or defaulted? Report file:line.
> 2. **Test-set profile** (joins [[proto-78-submission-readiness]] step 2): view 60 random test images (`Datasets/akshardrishti_official/test/test/`, seed 20260926) and classify each:
>    printed / handwritten / mixed; clean / degraded (blur, stains, low contrast, skew); tables yes/no; script (by eye + Unicode block of a fast engine's output). Report counts with n.
> 3. **Our data vs that profile:** do any official pair images look handwritten (view 20 each of bn, hi, sa, en pairs)? How many probe items are visibly degraded (view 50)? Any handwritten items in
>    `arc_level_1/labeled/` or South renders?
> 4. **Honest options (no downloads without approval):** (a) handwritten items already on disk with GT; (b) public handwriting benches (name, licence, size, URL opened) — download needs the boss;
>    (c) engines with handwriting support among the 10 (evidence from their docs). Output `docs/campaign/COVERAGE_GAP.md`: profile tables, our coverage, options with cost, recommendation.

## Boss decision U13
Include handwriting/degraded evaluation in scope before the freeze? Recommendation depends on step 2: if the test set has a material handwritten share (say >10%), yes — at least an evaluation slice.

Related: [[proto-78-submission-readiness]], [[proto-80-hackathon-metric-alignment]], [[proto-92-boss-decisions]]


## A.8 — proto-82-engine-empty-output-patterns (verbatim)

# PROTO-82 — EMPTY-OUTPUT PATTERNS: BUG OR HONEST-EMPTY? (Engine diagnoses, Verdict classifies, boss approves re-runs)

**Laws that apply:** L8 open policy ("engines read any script on any page; lang tag = ID label, never a content constraint"); L3 4-page gate ("no engine/config change touches the full set until it
wins on 4"); honest-empty is correct ONLY when the engine truly has no model for the script; operator law "Useless ⇒ engine is wrong ⇒ fix ⇒ re-run; keep old in json_vN; never fake counts."

## Measured (monitor, `sheet.csv`, % empty predictions, cells with ≥20 rows; ≥80% marked *)
| engine | 100%-empty languages | partial | reading |
|---|---|---|---|
| paddleocr_indic | bn*, brx*, doi*, gu*, ks*, mni*, or*, pa*, sat* (overall 43%) | — | **brx and doi are Devanagari**, yet hi/kok/mai/mr/ne (Devanagari) are 0% empty → likely a language→model mapping bug, not missing capability |
| surya | sa* (100%) | mni 55, doi 14, gu 12, sat 10, ne 8, brx 5 | **sa is Devanagari** and surya reads hi at 0% empty, but surya ignores the language code (see code evidence below) → cause is image/model-side, not mapping; the "fusion ceiling" is 67% this one bug (EDGE_THESIS) |
| anuvaad_tesseract | bn*, gu*, ks*, mni*, or*, pa*, sat*, sd*, ur* (overall 50%) | — | only kan/mal/tam/tel/hin/eng traineddata exist → mostly honest-empty; verify it isn't run with the wrong traineddata for Devanagari languages (brx/doi/kok/mai/mr/ne are 0% empty → fine) |
| rapidocr | bn*, gu*, mni*, or*, pa*, sat* (overall 27%) | ne 2 | check its model list for Bengali/Gujarati/Gurmukhi/Odia |
| others | — | doctr, easyocr, indicphotoocr, tesseract family ≤4% | fine |

## Code evidence already found by the monitor (2026-09-30 ~05:15)
- **paddleocr_indic — confirmed MAPPING-BUG for brx and doi:** `level2/probe22/run_probe.py:84-88` `PADDLE_LANG` maps hi/mr/ne/mai/sa/kok(gom) to paddle's Devanagari models but omits
  `brx` and `doi`; the comment at `run_probe.py:80-83` wrongly lists them among "languages without any paddle model … honest-empty". Both are Devanagari-script → map them to a Devanagari
  model (e.g. `hi` or `mr`) per law L8. (as/bn/gu/pa/or/ks/mni/sat: check paddle 3.7 `_utils/langs.py` for Bengali/Gujarati/Gurmukhi/Odia models before accepting honest-empty.)
- **surya — NOT a language-mapping bug:** `level2/run_engine.py` `ocr_surya(image_path, lang)` never uses `lang` (layout → block recognition, full-page fallback if <5 chars). So the 100% empty
  output on `sa` comes from the images or the model path, not codes. The `sa` items are official pair JPEGs (`Datasets/akshardrishti_official/Sanskrit/Images and Transcription/*pro_labelled.jpeg`)
  — check size/aspect, whether they are line crops or annotated ("labelled") images, EXIF rotation, and what layout returns (0 blocks?) on 4 items; same for `mni` (55% empty).

## Engine subagent — TASK (diagnosis read-only; then 4-page tests only)
> 1. For each * cell: find how `level2/probe22/run_probe.py` (LOCKED — read only) maps the language code to the engine's model/language argument (file:line). Classify:
>    NO-MODEL (the engine has no model for that script — honest-empty, document it) · MAPPING-BUG (a model for the script exists but the code isn't mapped, e.g. paddle brx/doi → Devanagari) ·
>    OTHER (crash/timeout — check logs `level2/probe22/logs/`).
> 2. For each MAPPING-BUG: run the engine with the corrected script argument on **4 items** of that language (L3 gate) in a scratch output folder (never `level2/probe22/out/`), score with `metrics.py`,
>    and report CER before/after. No full re-run.
> 3. Write `docs/campaign/EMPTY_OUTPUT_DIAGNOSIS.md`: the table above re-measured, per-cell classification with evidence, 4-page results, the exact `run_probe.py` edits needed (fix-spec format),
>    expected impact on the benchmark cell, and the re-run cost (items × engine time).

## Gate and execution
A full re-run of a fixed cell changes `level2/probe22/out/` and `sheet.csv` (sealed/locked) → it rides on the boss's U5 approval (score/re-score after the meeting) — old outputs kept as `out_archive/<engine>_v1/`
(law L5 "reruns versioned"). The Sanskrit/surya cell is the highest-value item (the plan's "only real engineering item").

Related: [[proto-80-hackathon-metric-alignment]], [[proto-61-sheet-provenance-forensics]], [[proto-70-level2-restructure]], [[proto-92-boss-decisions]]


# HISTORY — rev 1–3 text (superseded by rev 4 above; kept for audit, do not execute from it)

# PROTO-104 (rev 3) — PROJECT FIRST, SOUTH INCLUDED, HANDWRITING CENTRAL

## REV 3 (2026-09-30 ~21:15 IST) — read this first; rev 2 below still holds where not changed
**Boss 21:0x:** "for South, do as you recommended — the same way we got Sarvam outputs for the other languages" · "Vinay side: whatever we get comes tomorrow, don't bother" · "forget about team mates, we are the ones doing all" · Consensus answers saved at the root → store them relevantly.
**Status (planner's own reads):**
- **Agent 1:**
  - D0 DONE: the stray scripts are archived; `scripts/profile_test_images.py` is canonical.
  - D1: the Sarvam `indic-ocr-bench` is DOWNLOADED (rev 84ce7ce4); mlx 0.32.3 + mlx-vlm 0.7.4 are installed.
  - **All 3 Bodhan repos return 403 for the account Maya0769 → the boss must request access on each HF page.**
- **Agent 3:**
  - S1 REAL run: **0 of 23,001 official South PDF pages are clean** (76% legacy-font encodings: ta 6,542/6,606 · te 7,509/8,231 · kn 3,406/5,825 · ml 16/2,339 legacy); `W_south_reports/SOUTH_RERUN_FEASIBILITY.md` + `S1_real_feasibility.json`.
  - S2 paused "for U9/U24" — both were ALREADY approved.
  - The `product/` layer exists (built 20:43: schema, cli, pdf_writer, script_id, tesseract + bodhan recognisers).
- **Consensus:** stored in `docs/sources/consensus/` (3 `.tex` + README + MOVE_LOG, sha MATCH) → processing = [[proto-105-consensus-results-to-decisions]].
- **Strays at the repo root:**
  - `out_level3/dry_run/gate_plan.json` (a 20:43 dry run of the vajrAstra PR #12 Sarvam gate, pointing at deleted South v1 renders);
  - an empty `W4_reports/`.

**Rulings rev 3:**
- **R-7 South GT source = Sarvam-bench fill.** Why: the official South PDFs yield 0 clean pages under the same gates. Relaxing a gate only for South would break "same standard".
  - So South items = the sarvam_fill tier from the downloaded `sarvamai/indic-ocr-bench`, drawn by EXACTLY the procedure that produced the 158 sarvam_fill items of the 18 languages (read their manifest records for split, seed, crop type), ≤100 per language, seed 20260926.
  - Bench items are evaluation-only, forever (never training data).
  - Record in the manifest that South has no official_pdf tier and why.
- **R-8 Sarvam on South APPROVED (D-a):** the same as the others = **3 items per language × 4 = 12 calls** through the existing sarvam_vision harness, from the free credit (≈₹6 of ₹67). Nothing beyond 12; a ledger line per call in DISPATCH_LOG.
- **R-9 No team mates:** the boss + his AI agents do everything. No Krishna/Aryan/David lanes, owners or questions anywhere (supersedes rev 2 §4 "Open for the call").
- **R-10 Vinay:** nothing to prepare for him tonight. Step G (the Plan v3 draft) stays; whatever he sends tomorrow (GPU SSH etc.) gets folded in then.
- **R-11 The heuristic test-set profile is REJECTED as evidence.** `TEST_SET_PROFILE.md` labels images with PIL heuristics ("mojibake/cutoff" on images is meaningless).
  - The planner viewed 3 test images (10001.jpg, 12407.jpg, 1361.jpg): each is **one handwritten word in Bengali script**, blue pen, ~300 px tall; all 5,344 are ~296–300 px tall word/line crops, IDs 0–14806.
  - The only labelled handwriting set on disk is `Datasets/akshardrishti_official/Bodo/gu/` — Gujarati handwritten words, IIIT-HW format: train.txt 82,563 · val.txt 17,643 · test.txt 16,490 lines (`path, vocab-index`), vocab.txt 10,963 words — but only 4,645 images on disk.

### §H — Handwriting track (new; the test set says this is what the product must do well)
- **H1 (Agent 1, now, read-only):**
  - Profile `test/test/` properly: per ID bucket (0–999, 1000–1999, 10000–10999 … 14000–14806), view ≥10 images per bucket with a vision-capable model, or read the script by running Tesseract/Bodhan on them.
  - Record script/language, printed vs handwritten, word vs line.
  - Rewrite TEST_SET_PROFILE.md: its heuristic numbers are marked REJECTED (R-11).
  - Map `Bodo/gu/` (which split the 4,645 images are; whether images and labels match) and search the whole `Datasets/` tree for any other handwriting set.
  - Never use test images for training or tuning.
- **H2 (Agent 2, after R/A5):** build a LABELLED handwriting eval slice from the official handwriting data we hold (`Bodo/gu` labelled split; any Bengali handwriting found by H1) → `level2/benchmark/` as its own tier `official_hw`, same scorer, CER + WER + median + failure rate (proto-105 C3-6). Leak rule: a writer/page never in both train and eval.
- **H3 (Agent 1, Day 1 extension):** run Bodhan's handwriting mode on the H2 slice (Bodhan claims handwriting for English + 12 languages, HW score 66.7) beside Tesseract/surya → the handwriting baseline.
- **H4 (Day 3):** proto-100 **B-19** handwriting fine-tune (LoRA on the labelled handwriting train split; licence of the official data confirmed; eval on H2 only). Candidates from proto-105 C2-3 (PARSeq transfer, ICDAR-2023 Indic HTR data) need licence checks + boss download approval.

### Paste lines rev 3 (replace §6 of rev 2)
1. **Agent 3:** `Read proto-104 (rev 3 section at the top). U9 and U24 are ALREADY approved and the Sarvam bench is downloaded — continue S2 under ruling R-7: draw the South items (ta/te/kn/ml, ≤100 each, seed 20260926) from the Sarvam bench exactly the way the existing 158 sarvam_fill items were drawn, write manifest_v2.json + the page/crop files into level2/benchmark/ (NEW files only), post the run list in DISPATCH_LOG. Then S2 is done — Agent 2 verifies.`
2. **Agent 1:** `Read proto-104 rev 3. (a) Bodhan is 403 until I grant access — meanwhile do §H H1 (real test-set profile; the heuristic one is rejected per R-11). (b) When Agent 3 posts the South run list, run S4 (all local engines on South) and the 12 approved Sarvam calls (R-8, 3 per South language, ledger line each). (c) The moment Bodhan downloads, run D1 (--sample 100, --pair-only) + H3.`
3. **Agent 2:** `Read proto-104 rev 3 and proto-105. Order: finish A4/A5 → LAYOUT FROZEN; move the root strays out_level3/ and W4_reports/ into _archive/stray_2026-09-30/ with a log line; verify Agent 3's S2; process the Consensus results per proto-105 (files in docs/sources/consensus/ — open the papers before any row); then step G (Plan v3 draft) and §H H2 (labelled handwriting eval slice).`

---

# (rev 2 text follows)
# PROTO-104 (rev 2) — PROJECT FIRST, SOUTH INCLUDED

**Boss 2026-09-30:** 18:15 "stop everything, we should complete the project first" · 20:40 "why are these 4 South languages still separate… if not valid, regenerate South and add them with the remaining languages" · 20:50 "for South we should run them again? we will do that perfectly".
The planner runs NO subagents ([[feedback-no-subagents-boss-assigns]]); the boss assigns everything below to Agents 1–3.
All laws hold: proto-01 rules 17–21 · no training before Gate 2.5 · approved downloads only · no Sarvam calls without the boss · sealed dirs read-only · NEXT.md planner/boss only · **no git commit or push without the boss**.

**Finished =**
1. ONE benchmark: all 22 languages (+ en) drawn by one pipeline from the official data, scored by one scorer, in one table.
2. The product command: page image → layout JSON + searchable PDF + per-block language, offline.
3. Bodhan-based recognition, sharpened where it trails Sarvam, with a licence-cleared fallback.
4. Vinay's gates passed before training.
5. Every number reproducible from a command.

## 0. Status measured by the planner at 20:50 IST (own reads, no agents)
- **Agent 2 (repair):**
  - A2 PASS, A3 PASS: `packs/out` flattened; the benchmark root has 13 entries.
  - A4 is CONDITIONAL. The path rewrite is verified, but the smoke test is BLOCKED: `run_probe.py` builds its paths from `parents[2]`, which resolves to a non-existent `level2/level2/probe22/`.
  - A5 not done (`scores/mcnemar_full_matrix.json` absent). Last active 20:26.
- **Agent 1 (Engine):**
  - HF now logged in (`hf auth whoami` → user=Maya0769). Free disk 32 GiB. `level2/models_bodhan/` holds only empty dirs from 16:20; nothing is downloaded yet.
  - D0 half-done: three `profile_test_images*.py` versions sit at the REPO ROOT (20:11–20:15, stray); `docs/campaign/TEST_SET_PROFILE.md` is not written; `level2/training_assets/v3/` is empty.
  - Rewrote `scripts/install_mlx_stack.sh` + `scripts/reclaim_memory.sh` at 20:17. The headers claim "USER-APPROVED 2026-09-29"; proto-92 only records U23 (Bodhan incl. the MLX port) and U25 (mlx-vlm[train] extra). mlx is not installed yet. Last active 20:33.
- **Agent 3:** nothing since 20:16. `product/` does not exist. Its `W_south_reports/SOUTH_RERUN_FEASIBILITY.md` (16:36) says "Status: DONE" but also "no actual page extraction performed" — a FALSE done.
- **Benchmark languages on disk:** as bn brx doi gu hi kok ks mai mni mr ne or pa sa sat sd ur (18, 1,283 items) + en. **ta/te/kn/ml are absent.**
- **Git:** local main = origin/main. The working tree has 44 tracked files deleted, 35 of them `level2/models` docs. A careless `git add -A && push` would delete them from the team repo. PR #12 (another session's reference draft, 19:56 IST) is open and not merged.

## 1. Planner rulings (binding)
- **R-1 South v1 is not valid for the 22-language table.**
  - Why: different sources (Level-1 own-labelled), a different scorer (`verify_v2.py`), only 126/400 pages scorable, and legacy-font GT inside those.
  - So: **run South fresh (step S)** and retire v1 AFTER the new South has engine results (S6). Old numbers survive only as one labelled history line.
- **R-2 The run_probe.py fix is a path erratum.**
  - The `parents[2]` / base-path constant fix is a PATH ERRATUM and is covered by U10 ("path errata only"). Agent 2 applies it with a pre-image.
  - No logic change. The language maps already contain ta/te/kn/ml (lines 44, 75, 85, 282).
- **R-3 A4 PASS criterion:**
  - `run_probe.py` has 0 old-path hits and the 1-item-per-engine smoke test passes.
  - The 13 "RETIRED-SOURCE" hits are exempt until S6: the South v1 scripts `deep_verify.py`, `run_engine.py`, `seal_gen.py`, `verify_v2.py`, `engines/test_registry.py`, and the historical `research/gates/*`.
- **R-4 Day 1 no longer waits for A4.** `run_bodhan.py` has its own paths and A3 is done. It writes new files only.
- **R-5 Allowed installs for Day 1:** installing `mlx` + `mlx-vlm` into `.venv` is covered by U23 (the MLX port cannot run without it). Log exact versions. **Not covered:** cloning/installing mlx-tune, and anything else.
- **R-6 Git:** no commit, no push, no PR merge, no issue edits without the boss. PR #12 stays a reference.

## 2. Step S — South, run fresh to the same standard (the boss's "perfectly")
Same rules as the 18 languages ([[proto-71-south-rerun-same-standard]] Phase A/B, [[proto-101-south-unification-and-level2-tree]] P1/P3/P4):
- **S1 — Real feasibility (Agent 3; read-only, plus writes in `docs/campaign/checkpoints/W_south_reports/` only).**
  - Run the SAME `extract_gt.py` gates (MIN_CHARS 50, MIN_SCRIPT_RATIO 0.5, MAX_LATIN_RATIO 0.6, MAX_CTRL_CHARS 3) on `Datasets/akshardrishti_official/{Tamil 34 PDF + 4 img, Telugu 84 PDF, Kannada 41 PDF, Malayalam 20 PDF + 9 img}` → `candidates_<code>.json`.
  - Per language, record: pages scanned, rejected by reason (legacy-font count separately), clean candidates, distinct PDFs.
  - Rewrite `SOUTH_RERUN_FEASIBILITY.md`. Its first line: "supersedes the 16:36 stub, which claimed DONE without extracting".
- **S2 — Draw + pages (Agent 3; NEW files only).**
  - Draw ≤ 100 per language: seed 20260926, the same stratification as the 18.
  - If official clean pages are short, fill exactly as the 18 languages were filled (the same tiers as manifest.json: official_pdf, then sarvam_fill from Sarvam's bench — downloadable now that HF works, U24). Record the honest n; never relax a gate; never fabricate.
  - Re-gated South v1 pages do NOT enter (different sources).
  - Render pages into `level2/benchmark/pages/{ta,te,kn,ml}/` in the same format/dpi as `image_meta.json`.
  - Write `level2/benchmark/manifest_v2.json` = v1 items + South items, same schema. `manifest.json` and `manifest_v1.json` stay untouched.
  - Post the run list in DISPATCH_LOG.
- **S3 — Verdict (Agent 2):**
  - the gate statistics reproduce;
  - 10 drawn pages per language viewed against their GT;
  - leak check: no South item from a PDF that feeds training.
  - → "S2 AUDIT PASS" in W4.md.
- **S4 — Engine runs (Agent 1).**
  - The same engines as the 18, one at a time, into `level2/benchmark/packs/<engine>/ta|te|kn|ml/`.
  - Order: Bodhan (after Day-1 download), surya, tesseract_indic, rapidocr, doctr, easyocr, indicphotoocr, paddleocr_indic, anuvaad_tesseract.
  - openbharatocr = recorded alias of tesseract_indic.
  - sarvam_vision = "not run — cap spent" unless the boss approves the free-credit decision (§5 D-a).
  - An engine without the script = honest-empty, recorded.
- **S5 — Score (Agent 2).**
  - Same `metrics.py`, per GT tier → `scores/sheet_v2.csv` for all 22 languages + en.
  - Regenerate `docs/campaign/BENCHMARK_22.md` from `benchmark/` only.
  - One history line: "South v1 (Sep 11–14, own-labelled sources, 126/400 scorable; 26 legacy-font pages per the vajrAstra audit, if reproduced) — archived, not comparable".
- **S6 — Retire South v1 (Agent 2 executes, the boss clicks the guard prompts; only after S5).**
  - `git rm -r level2/out` + the South v1 scripts listed in proto-101 P4 — LOCAL ONLY; git history keeps them.
  - Bundle the untracked v1 files (`level2/reports`, `level2/renders_shared` …) sha-verified into `_archive/bundles/`, then remove them.
  - One `_archive/INDEX.md` line each.
  - Pushing this to GitHub = the boss's decision (it would break PR #12's CI, which guards the 4,000 packs).

## 3. The other steps (unchanged from rev 1 unless noted)
- **R — Repair (Agent 2, NOW):**
  1. A4 with ruling R-2/R-3 → "A4 PASS".
  2. A5 → "A5 PASS".
  3. Then "LAYOUT FROZEN": no mv/rename/delete under level2 except S6; new files allowed.
- **D0 (Agent 1, now, 15 min):**
  1. Put the stray root scripts away: `profile_test_images_v3.py` → `scripts/profile_test_images.py`; v1/v2 → `_archive/stray_2026-09-30/`, with sha + a log line. Nothing is deleted.
  2. Finish RQ-2 → `docs/campaign/TEST_SET_PROFILE.md` (read-only on `test/test/`; coarse stats; never used for training).
- **D1 (Agent 1, NOW — R-4):**
  1. Download the 3 Bodhan repos + Sarvam `indic-ocr-bench` (U23/U24). Record revision/sha256/size. If a 401 persists, the boss must click "agree" on that repo's HF page with the Maya0769 account.
  2. Install mlx + mlx-vlm per R-5.
  3. **Tonight, for tomorrow's call:** `--mode probe --sample 100` + `--pair-only` (300 gold pairs) → first numbers in `BODHAN_BASELINE.md`.
  4. Then the full 1,227 + the bench `small_representative` with the official scorer, 4-bit vs bf16 per script → **Gate 1**.
  5. If Gate 1 FAILS: stop and report. The surya fallback is NOT cleared for a product (RQ-9), so it needs the boss.
- **G (Agent 2, TONIGHT — the call is tomorrow morning):**
  - `docs/campaign/DRAFT_RESEARCH_PLAN.md` becomes the Plan v3 draft (pre-image first). Content:
    - the flowchart;
    - PPT recipe → v3 choice → evidence, per stage;
    - the 22-language benchmark;
    - Bodhan vs Sarvam;
    - the South re-run;
    - Day-1 numbers if they have landed;
    - the M10/B4/B5/RQ-9 fixes.
  - Then a proto-17 multi-LLM check (OpenCode + a fresh reviewer + the boss's ChatGPT paste) — **a quick pass tonight, the full one after the call if needed**.
  - The session with Vinay tomorrow = L12's 15–20 min cross-question session. **No training before it.**
- **D2/D3/D4/D5:** as rev 1 — leak-free split + audit; LoRA after both gates (Vinay's 24 GB GPU can host it when SSH arrives); product integration + 50-image dry run; proof. Agent 3's product layer (step P, rev 1 text: new files only under `product/`, Tesseract stand-in, Bodhan stub) starts AFTER S2.
- **PARKED** (unchanged): proto-95/96/98, proto-101 P0/P2/P5/P6/P7 (P1/P3/P4 are now step S), 72–74/77/84/63/66, proto-102 A6/A7/A8/A10 and Part B except what step G needs, GitHub issue housekeeping.

## 4. The vajrAstra handoff (another session, 2026-09-30 ~20:00, GitHub-only view) — aligned
- **Carried in:**
  - FREE ONLY: Sarvam free credit, ₹67 left (₹0.5/page), no card.
  - Vinay: 24 GB GPU over SSH arriving tomorrow (answers U33); call tomorrow morning; you're a registered company (sign-ups + the Bodhan §3.1 approval route go through it); ~10-day wait on an unconfirmed item (probably Bhashini).
  - GPU guardrails: data by rsync, never GitHub; keys only in env vars; ask Vinay whether the server may hold Datasets.
  - The finding "26 of 126 Sep-16 CER pages have legacy-font GT" — a trust correction owed to Vinay's team, **quoted only after Agent 2 reproduces it** (during S5).
  - Reading order is where paddle/rapidocr lose (F7) — supports using Bodhan's layout + reading-order model.
  - Pseudo-GT from engine agreement is worse than the best single engine (F8) — matches our voting 0/115.
- **Superseded:**
  - "the law locks scope to te/ta/kn/ml, North = Krishna" (Vinay L13 on 09-29: cover all languages; boss: no Krishna/Aryan);
  - A8 "find the other-language outputs" — they are the 18-language benchmark on this Mac, untracked in git;
  - the Round-2 A/B/C branches (replaced by Plan v3 gates);
  - the A0–A8 roster (replaced by Agents 1–3);
  - "done = pushed PR" (ours: done = command output in W4.md; push only on the boss's word).
- **Open for the call:** Bodhan is a vision-language model — any overlap with Aryan's work? May Datasets live on the GPU server? Spend the free ₹67 on a South Sarvam reference?
- **Parked:** PR #12 socket fix / CI / closing issues #2–#4, #6 (GitHub housekeeping, after the call).

## 5. Boss decisions + actions
- **D-a Sarvam free credit:** spend ≤ ₹50 on 25 South pages per language as the Sarvam reference (the 18 languages have one; South has none)? Default: NO until you say.
- **D-b GitHub:** nothing is pushed until you say; the 44 locally deleted tracked files must be reconciled before any push.
- **Actions:**
  - run the 3 Consensus queries (proto-97 RQ-12);
  - confirm the call time with Vinay;
  - if any Bodhan download returns 401, click "agree" on that HF page with the Maya0769 account;
  - optional: restart Agent 1's window so the delete guard covers it.

## 6. Paste lines (in this order)
1. **Agent 2:** `Read docs/campaign/protocols/proto-104-project-first-critical-path.md (rev 2). Do step R now: finish A4 under rulings R-2/R-3 (the run_probe.py parents[2] base-path fix is an approved path erratum — pre-image first), then A5, then post LAYOUT FROZEN. Then step G tonight (the plan doc for tomorrow's Vinay call). Verify S1/S2 when Agent 3 posts them.`
2. **Agent 1:** `Read proto-104 rev 2. Do D0 (stray root scripts to scripts/ and _archive/stray_2026-09-30/, finish TEST_SET_PROFILE.md), then D1 NOW: HF is logged in — download the 3 Bodhan repos + Sarvam bench, install mlx + mlx-vlm only (R-5), run --sample 100 and --pair-only tonight so numbers exist for tomorrow's call, then continue to Gate 1. When Agent 3 posts the South run list, run step S4.`
3. **Agent 3:** `Read proto-104 rev 2. You own step S1 then S2: extract ta/te/kn/ml from the official data with the same gates, write the real feasibility report (the 16:36 one claimed DONE without extracting), then draw ≤100 per language and render the pages into level2/benchmark/pages/ — NEW files only; never mv, rm or edit an existing file; stop and ask if you think you must. Post the run list in DISPATCH_LOG when done.`
4. **Agent 2 (when you paste Consensus results):** `RQ-12 Q<n> result (Consensus, 2026-09-30): <paste>`

Related: [[proto-89-plan-v3-bodhan-base]], [[proto-102-incident-repair-and-verdict-fixes]], [[proto-71-south-rerun-same-standard]], [[proto-101-south-unification-and-level2-tree]], [[proto-97-research-still-to-do]], [[proto-92-boss-decisions]], [[proto-103-meeting2-verbatim-truth-and-application]], [[feedback-no-subagents-boss-assigns]]
