---
name: proto-108-plan-v4-final
description: "PLAN V4 (FINAL, 2026-10-01 ~15:45 IST, planner = head strategist) — supersedes Plan v3's strategy (proto-89 stays as Bodhan technical detail). The cracked edge: the official test set is 5,344 Bengali HANDWRITTEN WORDS, where general document VLMs score 58–75 word accuracy (Sarvam 58.3, Bodhan 71.3, Gemini 74.8 on Bodhan's HW bench) while handwriting specialists trained on the public CC-BY IIIT-INDIC-HW-WORDS data reach 92–96% WRR (ICDAR 2023 IHTR, Bengali). Architecture = two experts under one router (Page Expert: Bodhan layout+recogniser; Handwriting Expert: PARSeq per script from the local IndicPhotoOCR checkpoints), portable PyTorch product; data/training/eval plan with leak gates; mandela + factchk; owners, gates, boss decisions, paste lines."
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-10-01T11:04:33.036Z
---

# PLAN V4 — WIN AKSHARDRISHTI: specialist where the test is, generalist where the product is

**Skills used:**
- **readchk** — understood as: the boss wants the final strategy, built from all research + meetings + concerns; no team mates; portable product; win, honestly.
- **factchk** — every external number below was opened 2026-10-01 unless marked.
- **mandela** — see §8.
- **graphify** — a query-routed reading list.
- **ssotize** — this file is THE strategy. proto-104 stays THE execution order; proto-89 stays the Bodhan technical detail.

**Read in full:**
- `level2/ULTIMATE_HYBRID_CONCERN.md`, `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt`, `SOUTH_CANON.md`;
- `docs/research/MEETING_2026-09-29_STRUCTURED.md`, `BOSS_CONCERNS.md`;
- `docs/campaign/{RESEARCH_DECISIONS, EDGE_THESIS, COMPETITOR_INTEL, DRAFT_RESEARCH_PLAN}.md`, `docs/architecture/PPT_SPEC.md`;
- `docs/research/R7_W6_TRAINING_TREE.md`, `docs/research/level7/c/c3/STRATEGY.md`;
- the 3 Consensus exports (`docs/sources/consensus/*.tex`);
- the Bodhan card tables (`level2/models_bodhan/indic-ocr/README.md:255-346`);
- the ICDAR 2023 IHTR report (12 pages).

**Searched, not read whole:** the level7 lane ledgers (1.1 MB), for every handwriting / HTR / IIIT / PARSeq / TrOCR record. Their line-by-line harvest is the agents' proto-107 W3 fact ledger, folded in during the 3-hour integration loop.

## 0. The thesis in five lines
1. **The contest is product-weighted.** No metric or deadline is published. The jury scores approach/innovation · technical feasibility · product roadmap · team · addressable market. The only named evaluation target is "accuracy, layout detection, multilingual text handling" (RQ-1, official page).
2. **The official test set is 5,344 Bengali HANDWRITTEN word images.** The planner viewed 3; Agent 1 viewed 13 across every ID range: 13/13 Bengali handwriting.
3. **On handwriting the big general models are weak.** Bodhan's own IndicOCR-HW bench (word accuracy):
   - overall: Gemini 3.1 Pro 72.0 · Bodhan 66.7 · **Sarvam 55.4**;
   - Bengali: 74.8 · 71.3 · **58.3**.
4. **Handwriting specialists are not.** ICDAR 2023 IHTR, Bengali words, word recognition rate:
   - Upstage PARSeq **96.10** · PERO 92.02 · light (TrOCR) 91.62 · SRUKR 88.06;
   - the organisers' CVIT baseline: 75.34.

   They trained on the public **IIIT-INDIC-HW-WORDS** (Bengali train: 82,554), licensed **CC BY 4.0** (IndiaAI AIKosh, published via the Digital India BHASHINI division).
5. **So: two experts under one router.**
   - **Handwriting Expert:** PARSeq per script, initialised from the 11 PARSeq checkpoints already on this Mac (`.deps/IndicPhotoOCR`, MIT). It wins the test the organisers gave us.
   - **Page Expert:** Bodhan, which reproduced ≈86.4 on Sarvam's bench here. It wins the document product the jury scores.
   - Shipped portable (PyTorch, CUDA/CPU, Docker), offline, free.

## 1. Where everyone stands (never mix benches)
- **Printed — Sarvam's Indic OCR bench** (word accuracy 100×(1−WER), macro over 22 languages; Sarvam blog 2026-09-24):
  - Sarvam Vision 2.1 87.39 · Bodhan 84.94 · Gemini 3.6 Flash 79.35 · GCV 71.76 · surya 69.96;
  - Sarvam per language: bn 93.47 · hi 93.52 · ta 87.70 · te 91.55 · ml 90.24 · kn 90.54;
  - Sarvam's weak cells: sat 53.91, ks 54.82, or 80.01.
- **Printed — Bodhan's IndicOCR-PR bench:** Sarvam 86.6 · Bodhan 86.2 · Gemini 80.4. 8 of 22 per-language winners flip between the two vendor benches (COMPETITOR_INTEL §1).
- **Handwriting — Bodhan's IndicOCR-HW bench** (Gemini / Bodhan / Sarvam):
  - Assamese 71.6 / 66.1 / 47.8
  - Gujarati 60.0 / 55.9 / 39.2
  - Hindi 83.1 / 77.6 / 72.3
  - Kannada 73.8 / 69.6 / 57.7
  - Malayalam 63.9 / 60.5 / 45.6
  - Marathi 79.0 / 70.2 / 61.8
  - Odia 66.7 / 68.2 / 40.6
  - Punjabi 70.1 / 69.4 / 54.8
  - Tamil 80.5 / 76.8 / 60.5
  - Telugu 72.0 / 53.5 / 59.1
  - Urdu 54.4 / 46.4 / 44.4
- **Handwriting specialists — ICDAR 2023 IHTR** (word recognition rate; 5,000 new test words per language from 100 writers):
  - Bengali 96.10 · Devanagari 93.16 · Gurmukhi 95.28 · Kannada 94.54 · Malayalam 97.16 · Odia 83.38 · Tamil 98.08 · Telugu ~91.4;
  - **Gujarati 62.80 (hard)**;
  - winner average 88.31 WRR / 95.94 CRR.
- **Ours, measured** (DISPATCH_LOG §36; MLX port):
  - Bodhan on Sarvam's bench small_rep (1,173 items): CER 0.054, WER 0.1356 → word accuracy ≈ **86.4**, reproducing 84.94 within +1.5;
  - on our 300 human gold pairs: CER **0.40 vs surya 0.57**;
  - on 99 full benchmark pages: CER **0.69**, an unexplained page-level gap (O-1);
  - 4-bit ≈ bf16; 0.52 s per crop;
  - the PyTorch official path is not run yet (vendor asserts CUDA → GPU day).
- **What nobody publishes:** handwriting + tables + code-mixed together, independent (non-vendor) Indic benchmarks, abstention rates, CIs. Our 22-language table with GT tiers, abstention and CIs is new — a credibility asset, not an accuracy claim.

## 2. The edge, and why it survives where four died
All four Wave-1 theses were killed (EDGE_THESIS.md). This one is different in kind:
- it does not rest on our own benchmark;
- its numbers are published by third parties (the ICDAR organisers; Bodhan's own card shows Sarvam behind);
- it targets the exact distribution of the official test images.

Pre-registered kills:
- **(a) The test set is not IIIT-like.** Kill if a stratified 100-image view shows < 80% single handwritten words. (13/13 so far.)
- **(b) Specialists don't transfer to new writers.** The ICDAR 2023 test is 100 NEW writers and still scored 96.10. Kill if our fine-tune scores < 85% WRR on an independent-writer set (BN-HTRd or the ICDAR test).
- **(c) Test leakage.** If the official images ⊂ the IIIT train split, exclude them and disclose. The edge then rests on independent-writer numbers only (G-HW0).

## 3. Architecture v4 (portable; mapped to Vinay's PPT stages)
1. **Quality gate.**
   - Measure resolution, blur and contrast.
   - Only low-quality inputs get restoration (B-06; super-resolution hurts high-res pages — Rawat 2021).
   - PPT stage 0 (OpenCV): kept, gated.
2. **Route.**
   - Crop vs page: aspect ratio + height (the official crops are ~300 px tall, one word).
   - Pages: Bodhan IndicDocLayout (33M, 37 classes, reading order) gives blocks with a handwritten/printed flag.
   - Script: IndicPhotoOCR ViT script-ID (12 classes, MIT; no sat/mni) plus Unicode ranges after the first pass.
   - Same-script language: IndicLID on the recognised text (C3-4; the download needs the boss).
   - PPT stage 1 (DocLayout-YOLO + IndicDLP LoRA) → replaced by Bodhan's layout model, already Indic-trained.
3. **Recognise.**
   - **Handwritten → Handwriting Expert:** PARSeq per script, Bengali first.
     - Init from `.deps/IndicPhotoOCR/IndicPhotoOCR/recognition/models/<script>.ckpt` (11 scripts on disk).
     - Fine-tune on IIIT-INDIC-HW-WORDS with the ICDAR winner's recipe: synthetic/scene init → multilingual real → per-script fine-tune.
     - Optional LM rescoring: the lexicon comes from the training split only (PERO and SRUKR used word LMs).
   - **Printed → Page Expert:** Bodhan IndicBlockOCR (Qwen3.5-0.8B), plus per-language LoRA only where it trails (proto-89 §C).
   - **Fallback:** Tesseract + Indic tessdata (Apache-2.0) on a bad-output check (empty / wrong script / loop).
   - PPT stage 2 (TrOCR + Qwen3.5-VL + PaddleOCR-VL SFT): kept in spirit. Qwen3.5 is Bodhan's family. PARSeq replaces TrOCR-from-scratch for handwriting (ICDAR Bengali: PARSeq 96.10 > TrOCR 91.62).
4. **Optional RL.** Only after SFT wins and time remains, on verified gold only (R7 N4). PPT stage 2b: kept, ordered last.
5. **Post-correction (B-18).**
   - An LM corrector trained on the experts' own errors, from the training pool only.
   - Ships only if it wins on held-out documents (Bhandari 2026: hi CER 10.20 → 6.73).
   - PPT stages 3/3b → this step plus the JSON writer.
6. **Product outputs** (official focus area 5):
   - layout-preserving JSON per the SOUTH_CANON §G schema: page meta; blocks with bbox, reading order, modality, script/language, NFC text, provenance, confidence;
   - searchable PDF, Markdown, per-block language; transliteration later;
   - CLI + Python API + Docker (PyTorch CUDA/CPU) + a NOTICE (Bodhan §2.2, IIIT CC-BY, Apache tessdata).
7. **Evaluation** (PPT: Sarvam, IndicDLP, Indic Vision Bench, no fine-tune on test): kept, extended with handwriting sets and leak gates (§6).

## 4. Data (licences decide; downloads need the boss)
- **D-HW-bn — IIIT-INDIC-HW-WORDS Bengali** (CC BY 4.0, AIKosh).
  - Splits: train 82,554 · val 12,947 · test 17,575 (ilocr / PLATTER). The ICFHR page says test 18,574 — Agent 2 confirms from the zip README.
  - Use: TRAIN + MODEL-SELECTION.
- **D-HW-all — the other scripts** (Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Odia, Tamil, Telugu, Urdu).
  - Gujarati is already on disk: `Datasets/akshardrishti_official/Bodo/gu` — train 82,563 / val 17,643 match the paper; test.txt has 16,490 lines and 4,645 images are present.
  - Use: TRAIN.
- **D-IND — independent-writer evaluation:** BN-HTRd (Mendeley 743k6dm543; 108,181 Bangla words, 150 writers; licence to check) and the ICDAR 2023 IHTR val/test (100 new writers; "academic-use" per our ledger). **EVAL ONLY.**
- **D-SYN — synthetic Bengali word renders** (Pango/HarfBuzz + OFL Bengali fonts). Pretraining only, never evaluation (R7 L3; C3 rule 1). Font downloads need the boss.
- **Printed:** official bn/hi/sa/en pairs (10,432) + gated PDF-layer blocks, for Bodhan LoRA (proto-89 §B).
- **NEVER train on:** the 5,344 official test images, any Sarvam bench item (including sarvam_fill / South), or any eval split.

## 5. The build (the boss's 3 agents; no training before G-2.5)
- **HW0 — Leak gate** (Agent 2, read-only, once D-HW-bn lands): pHash + SHA of the 5,344 official test images against every candidate set; report the overlaps; exclude them and disclose.
- **HW1 — Zero-shot baselines** (Agent 1; no training):
  - systems: IndicPhotoOCR bengali PARSeq (local), Bodhan handwriting mode (MLX), Tesseract `ben`;
  - data: IIIT bn val (after download) + 200 official test images (viewed only);
  - report: WRR/CRR (CER/WER), median, failure rate, s/word.
- **G-2.5 — Vinay's gate** (the boss): send him the Plan v4 one-pager on WhatsApp. His OK (or the 15–20 min session) is required before any training (his red line, L10/L12). Agent 2 runs a quick multi-LLM check (proto-17 method) in parallel.
- **HW2 — Fine-tune Bengali** (Agent 1):
  - PARSeq from `bengali.ckpt` on IIIT bn train, with augmentation (affine, blur, ink, binarise); select on IIIT val;
  - Mac MPS is feasible (PARSeq is small); the 24 GB GPU is faster;
  - target: ≥ 92% WRR on IIIT val and ≥ 85% on independent writers;
  - then LM rescoring with the train lexicon, kept only if WRR rises.
- **HW3 — Other scripts** (Agent 1): the same recipe for every script with IIIT data and a local checkpoint. Gujarati needs extra care (ICDAR best: 62.80).
- **P1 — Page Expert** (Agents 1 + 2):
  - explain the 0.69 page CER (O-1) with order-invariant CER + a per-script split;
  - Bodhan LoRA (proto-89 §C) on the GPU (PEFT) after G-2.5;
  - post-correction B-18.
- **R1 — Router + product** (Agent 3, after the proto-107 W5 review):
  - crop-vs-page and HW-vs-printed routing, script ID, fallback;
  - JSON/PDF/MD outputs, CLI + Docker;
  - a 50-image timed dry run on the official test → s/word → the 5,344 budget.
- **E1 — Proof** (Agent 2):
  - one table, every system on the SAME independent sets: ours, Bodhan, Sarvam (12-call budget; more only on the boss's yes), Tesseract;
  - WRR/CRR + CIs + failure rate;
  - printed results stay tiered (R-12).
- **PITCH** (Agent 2 drafts, the boss presents):
  - the two artifacts (showcase + Plan v4);
  - a 5-minute demo: camera photo → JSON + searchable PDF in Bengali;
  - the cost story: ₹0 offline vs Sarvam ₹0.5/page and Bodhan API ₹0.20/image;
  - the roadmap.

## 6. Gates (pre-registered)
- **G-HW0 — leak:** overlap = 0 after exclusion.
- **G-HW1 — baselines measured.**
- **G-2.5 — Vinay OK + multi-LLM check.**
- **G-HW2:**
  - IIIT bn val WRR ≥ 92% → continue;
  - < 85% after 2 epoch-equivalents → switch recipe (CRNN + LM, PERO-style) or init from PARSeq-base;
  - independent-writer WRR < 85% → no claim; investigate.
- **G-P1:** Bodhan LoRA lowers held-out CER with a CI excluding 0, and no language regresses by > 1 point.
- **G-SHIP:**
  - the 50-image dry run fits the time budget;
  - JSON and PDF are valid;
  - licences + NOTICE are present;
  - every number in the artifacts has its reproducing command.

## 7. What we may claim, and when
- **Now:**
  - the test set is Bengali handwritten words;
  - published specialists reach 92–96% WRR on Bengali handwriting, while general document VLMs score 58–75 on vendor handwriting benches;
  - Bodhan reproduces its Sarvam-bench score here (≈86.4 vs 84.94);
  - Bodhan beats surya on our human gold (0.40 vs 0.57 CER).
- **After HW2 + E1:** "our handwriting expert: X% WRR (CI) on independent writers vs Bodhan Y and Sarvam Z on the same set."
- **Never:**
  - "we beat 87.39" (a different bench and metric);
  - a pooled printed win without its GT tier;
  - winners at n < 50;
  - "1000% we win" — the measured margin replaces it.

## 8. mandela — patterns that fire (root: the ground truth that matters, the official handwriting test, is unlabelled)
- **#1 Recall, not reason (contamination):** the official test may come from the IIIT/ICDAR collections. Fix: the G-HW0 pHash/SHA gate; exclude + disclose.
- **#6 Shared-pool bias:** IIIT train and val/test share one collection protocol. Fix: the headline goes on independent writers (BN-HTRd 150 writers; ICDAR'23 test from 100 new writers).
- **#4 / #5 Tautology / verifier = designer:** each vendor bench is graded by its maker. Fix: compare everyone on sets none of us built (D-IND); printed results stay tiered (R-12).
- **#3 Shared hallucination** (our agents checking our agents). Fix: Agent 2 re-runs every number from scripts it did not write; the commands are published beside each number.
- **Self-check:** the planner designed this plan (#5 risk). The decisive evidence (ICDAR Table 2, the Bodhan card, the AIKosh licence) is external and was opened today. Our own claim waits for E1.

## 9. factchk ledger (2026-10-01)
**PRIMARY (opened):**
- the ICDAR 2023 IHTR report pp. 1–12 (Table 2 Bengali, Table 1 splits, methods);
- the Bodhan card tables (local README:255-346);
- AIKosh IIIT-INDIC-HW-WORDS — "Attribution 4.0 International (CC BY 4.0)";
- the CVIT page — 872K words, 135 writers, zips with labels + vocab;
- the ICFHR 2022 dataset page — splits, "All Rights Reserved";
- the Sarvam blog — 87.39, per-language values, SFT→RLVR, Sep 24.

**Snippet-only, to verify:**
- PARSeq Apache-2.0 (open the LICENSE file);
- BN-HTRd size, writers, licence;
- the IIIT bn test count (17,575 vs 18,574);
- the IndicPhotoOCR weight licence.

**Contradictions:**
- AIKosh says CC BY 4.0, the ledger says "academic-use" for the competition sets → train only on the AIKosh CC-BY release; competition sets are evaluation-only.
- c3 STRATEGY §4 "Bodo-gu/test-test as GT" (do-not-collect) is superseded for Bodo/gu: it is labelled IIIT Gujarati. `test/test` stays never-GT.

## 10. Open items
- **O-1:** Bodhan page CER 0.69 vs crop 0.054 — run order-invariant CER first.
- **O-2:** Sarvam re-run of the 12 South calls — only on the boss's yes (a new key is saved).
- **O-3:** GPU SSH.
- **O-4:** the submission format is unknown — produce per-image JSON + `image,text` CSV + searchable PDFs.
- **O-5:** proto-107 gold must not touch `level2/benchmark/**` or handwriting data.

## 11. Boss decisions (one line each)
- **U-HW1:** download IIIT-INDIC-HW-WORDS Bengali (CC BY 4.0; Agent 1 states the size first) — recommend YES.
- **U-HW2:** download the eval-only sets (BN-HTRd after its licence check; ICDAR'23 val/test, academic-use, evaluation only) — recommend YES.
- **U-HW3:** G-2.5 — send Vinay the Plan v4 one-pager; his OK unlocks training.
- **U-HW4:** the other scripts' IIIT zips, after HW2 passes.
- **Carried:** O-2, O-3, and GO-A / GO-D / GO-G for proto-107.

## 12. Paste lines
1. **Agent 1:** `Read docs/campaign/protocols/proto-108-plan-v4-final.md. Now (no downloads, no training): HW1 on what is local — run IndicPhotoOCR's bengali PARSeq (.deps/IndicPhotoOCR) and Bodhan handwriting mode on 200 official test images (view only) and report outputs + s/word; and state the exact download URL + size of IIIT-INDIC-HW-WORDS Bengali (AIKosh/CVIT) for the boss's U-HW1. When U-HW1 = yes: download, verify counts vs README, then HW1 on IIIT bn val with WRR/CRR/median/failure rate.`
2. **Agent 2:** `Read proto-108. Prepare HW0 (pHash+SHA overlap script for the 5,344 official test images vs any candidate set, stdlib + PIL only); verify the PARSeq LICENSE, the IndicPhotoOCR weight licence, BN-HTRd licence and the IIIT bn test count; write them as RESEARCH_DECISIONS rows. Then a quick multi-LLM check of Plan v4 (proto-17 method) for G-2.5.`
3. **Agent 3:** `Keep proto-107 (gold) running to W5. Do not touch level2/benchmark/**, .deps/, Datasets/ or any handwriting data.`

Related: [[proto-104-project-first-critical-path]], [[proto-89-plan-v3-bodhan-base]], [[proto-105-consensus-results-to-decisions]], [[proto-100-research-to-build]], [[proto-107-gold-repo-consolidation]], [[proto-103-meeting2-verbatim-truth-and-application]], [[boss-rules]]

## Artifacts (published 2026-10-01 ~16:15 IST)
- Showcase for Vinay (the previous plan Doc, rebuilt + renamed): https://claude.ai/artifact/Fn257YXfs4RD5htjZMUR3i — "AksharDrishti by Vaultstack — Project Showcase"
- Plan v4 (separate Doc): https://claude.ai/artifact/X3Bg1Mg58pPzrB6AcGEan9 — "AksharDrishti — Plan v4 (final)"
- The 3-hour integration loop (boss order) refreshes both from agents' results: HW1 numbers, HW0 overlap, licence checks, proto-107 gold facts.
