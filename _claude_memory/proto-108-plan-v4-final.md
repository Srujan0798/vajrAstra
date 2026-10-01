---
name: proto-108-plan-v4-final
description: "PLAN V4 rev 2 (INTEGRATED, 2026-10-01, cloud planner): built from a full read of 320 research files (50 Sonnet readers + 50 fact-checkers + 7 theme digests). Three tracks never mixed: A handwriting (official test = 5,344 handwritten word crops; HW-ID/HW0/HW1/G-2.5/HW2 with paired-test kill gates), B printed 22-language (Bodhan base on PyTorch, per-cell sat/mni/ks/or/sa/kok/R4 recipes with kills, GT-trust lock), C product & jury (6 official criteria, cost, dry run). Evaluation law, kill table, licence ledger, compute, contradictions, boss decisions, paste lines. rev 1 kept below as HISTORY."
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-10-01T11:04:33.036Z
---

# PLAN V4 rev 2 — INTEGRATED (2026-10-01, cloud planner, built from the full corpus pass)

**Status:** this section is THE strategy. rev 1 (below, `# HISTORY`) is kept word for word for audit. proto-104 stays the execution order; proto-89 stays the Bodhan technical detail.

**How this rev was built:**
- 50 partitions, 320 files, every line read by a Sonnet reader. Each partition was then checked by a separate Sonnet fact-checker against path:line.
  - 2,654 findings; 0 dropped as invented.
  - P49 and P50 (memory files) are NOT fact-checked: the permission classifier blocked the verifier.
- 7 Sonnet theme digests, then planner synthesis. No Opus subagents.
- Raw material is in the repo:
  - `docs/campaign/handoff_2026-10-01_v4_integration/digests/` (digest_*.json, gaps_misc.txt, partitions/P*.extract|verify.json)
  - `corpus_extract.md`, `v4_notes.md`
- Citations below are repo-relative path:line, as given by the digests. Where a digest cited only a file, the line is missing and is marked "(file)".

## 0. The plan in eight lines
1. **The judging is product-weighted.** There are six criteria (approach, business use case, technical feasibility, product roadmap, team, addressable market) and no published metric, deadline or submission format. The only named evaluation target is "accuracy, layout detection, multilingual text handling". (`docs/campaign/checkpoints/W4_reports/RQ1_official_rules.md:20-50,82-131`)
2. **The official test file is 5,344 unlabelled handwritten word crops.**
   - Crops are 296–300 px tall. 13 of 13 viewed are Bengali, blue pen.
   - The full script mix is NOT measured; only 0.24% has been viewed. (`docs/campaign/TEST_SET_PROFILE.md:35-47`; `DISPATCH_LOG.md:467,505-508`; `docs/campaign/checkpoints/W4.md:431`)
3. **The official page's scope is wider than the test file:** full-page handwriting, mixed typed+handwritten, forms, low-quality scans. (`RQ1_official_rules.md:257-260,280`)
4. **So there are three tracks, each with its own gates, never mixed in one number:**
   - **A — Handwriting:** wins the test file.
   - **B — Printed 22-language page OCR:** the product and the "multilingual" claim.
   - **C — Product & jury:** how we are actually scored.
5. **Track A edge, labelled DIRECTIONAL:**
   - Published handwriting specialists reach 88–96% WRR on Bengali words (ICDAR'23 Table 2).
   - General document VLMs score 58–75 on a vendor handwriting bench (Bodhan card).
   - These are other people's benches, so they are a hypothesis until our own same-scorer run on independent writers. (`_claude_memory/proto-108-plan-v4-final.md:34-41`; `docs/research/level7/c/c4/OBITUARIES.md:1-8`)
6. **Track B is honest, not a claim of a win:**
   - On human-verified printed items Sarvam is 2.51× better than our best local engine (CER 0.171 vs 0.430, n=18).
   - All 21 of our item-level wins sit in the PDF-text-layer tier.
   - Bodhan is the open base; weak cells get per-cell recipes with kill rules. (`docs/campaign/checkpoints/W1.md:92`; `docs/campaign/BOSS_EXPLAINER.md:7,13`)
7. **Nothing trains before G-2.5,** which needs both:
   - the multi-LLM-by-process evaluation of this plan with its data package;
   - the 15–20 min Vinay cross-question session.

   It also needs the boss's go per download. (`BOSS_CONCERNS.md:148`; `docs/campaign/checkpoints/W4.md:117`; `proto-01-law-and-guardrails.md:28`)
8. **Every number we publish:**
   - comes from one committed scorer;
   - carries set, n, metric, tier and a confidence interval;
   - is reproducible by a command.

   Vendor numbers are directional only. (`docs/campaign/SHEET_V2_FORENSICS.md:3-56`; `docs/research/level7/c/c4/LEDGER.md:1035-1077`)

## 1. Facts this plan stands on (status-tagged; re-verify before quoting)
**Test file and data on disk:**
- **MEASURED** — The official test is 5,344 JPGs at `Datasets/akshardrishti_official/test/test/`, IDs 0–14806 (sparse). 20,656 is the whole official dataset, so the "5,344 not reproduced" claim is withdrawn. (`docs/campaign/checkpoints/W1.md:169`; `TEST_SET_PROFILE.md:8-15`)
- **RETIRED** — Tesseract's "35.7% Devanagari" reading was a method artefact. `hin` forces Devanagari, and the install had no Bengali model. Never quote it. (`W4.md:449`; `TEST_SET_PROFILE.md:85-87`)
- **MEASURED** — `Bodo/gu` is IIIT-INDIC-HW-WORDS Gujarati, labelled.
  - Splits: train 82,563 / val 17,643 / test 16,490 lines; vocab 10,963.
  - Only 4,645 images are on disk. They are mispathed (`gu/test/test/N.jpg`) and carry no writer_id.
  - sha256 overlap with the official test is 0 (the old "4,645 overlap" was filename-only).
  - (`TEST_SET_PROFILE.md:51-74`; `W4_reports/blind_verify_H2.md:7-35`; `corpus_extract.md:6-9`)
- **MEASURED** — No Bengali labelled handwriting is on disk. (`TEST_SET_PROFILE.md:72-74`)
- **MEASURED** — All 1,283 probe22 items and the South-400 are printed: 0 handwritten, 0 tables. No printed table transfers to the handwriting test. (`proto-81:13-14`; `docs/campaign/MENTOR_PLAYBOOK.md:217`; `W1_reports/PROTO86_VERIFY.md:92`)

**Handwriting landscape:**
- **PRIMARY (planner read of the paper):** ICDAR'23 IHTR, Bengali CRR/WRR.
  - Upstage 98.99/96.10 (PARSeq+SwinV2, synthetic then real pretrain, multilingual then per-language fine-tune, ensemble).
  - PERO 92.02 (trained on IIIT val/test too, so not clean) · TrOCR 91.62 · SRUKR 88.06 · CRNN baseline 75.34.
  - The 10-script winner average is 88.31 WRR / 95.94 CRR.
  - The ledger has no per-language Bengali WRR, so 96.10 rests on Table 2 only. (`proto-108:37-39`; `docs/research/level7/a/LEDGER.md:6113-6114`)
- **PRIMARY (vendor card):** Bodhan IndicOCR-HW, word accuracy, Gemini / Bodhan / Sarvam.
  - Overall 72.0 / 66.7 / 55.4.
  - Bengali 74.8 / 71.3 / 58.3.
  - Bodhan's handwriting covers 12 Indic languages and loses 11 of 13 to Gemini. (`proto-108:34-36,54-64`; `docs/campaign/COMPETITOR_INTEL.md:14,28,42,79`)
- **MEASURED (ledger):** IIIT-INDIC-HW-WORDS.
  - 868K–872K words, 135 writers.
  - In-domain CER 4.97% with 82K pretrain; IAM pretrain gives 4.85%.
  - Same-script initialisation dominates: 92% WRR vs cross-lingual 51% vs scratch 6%. (`LEDGER.md:6161-6177`; `docs/sources/consensus/2026-09-30_Q1_model-and-training.tex:334`)
- **MEASURED (local):** IndicPhotoOCR is a SCENE-TEXT toolkit (11 PARSeq/ViT recognisers on disk), not handwriting-trained. Its weight licence (STocr releases) is unverified. (`LEDGER.md:3665`; `level2/engine_docs/indicphotoocr/RUN.md:4-7`; `RQ9_licences.md:199-201`)
- **MEASURED (trap):** a PARSeq with a re-initialised Indic head showed script ratio 0.53 but Jaccard 0.00 against the GT, i.e. glyph salad. Script ratio is not a content gate. (`level2/research/gates/B1_doctr_parseq.md:43-52,76-79`)
- **Unused assets** worth keeping on the roadmap:
  - page-level: PLATTER/CHIPS, ICDAR-2025 IHDR (13 scripts), UniLipi;
  - semi-supervised: SemiHastakshar (IIIT-INDIC-HW-WILD/UC);
  - label cleaning: up to 1.8 CER points. (`LEDGER.md:3599,3623,3647,6129-6153`; `Q2.tex:448,470`)

**Printed landscape:**
- **DIRECTIONAL** — Sarvam's Indic OCR bench, macro word accuracy over 22 languages, run by Sarvam:
  - Sarvam 87.39 · Bodhan 84.94 · Gemini 79.35 · GCV 71.76 · surya 69.96.
  - On Bodhan's own bench: Sarvam 86.6 / Bodhan 86.2.
  - 8 of 22 per-language winners flip between the two benches. (`COMPETITOR_INTEL.md:10,14,16,28-42`)
  - Sarvam's weak cells there: sat 53.91 (Bodhan 68.30) · ks 54.82 (Bodhan 48.04) · or 80.01 (Bodhan 75.45, Gemini 81.01) · mni 85.12 (Bodhan 82.85).
  - kok 97.41 is Sarvam's best cell, not a weak one.
  - OldScan 55.3 is an English olmOCR column. (`LEDGER.md:1188-1191,1257-1260`; `W1_reports/1G_verify.md:204-213`; `W1A_PACKET_AUDIT.md:175,206`)
- **MEASURED (ours, printed probe22, sheet basis):**
  - Engine CER: Sarvam 0.2640 (n=54, directional) · surya 0.3944 · tesseract_bilingual 0.4907 · tesseract_indic 0.4918 · easyocr 0.5013 · indicphotoocr 0.5634.
  - Surya wins 9 languages at n≥50, the tesseract family 2 (mr, or), easyocr 1 (sa).
  - No winner claim for as, doi, mni, sat, gu, ne (n<50). (`level2/benchmark/docs/LEADERBOARD_REFRESH_2026-09-29.md:127-141`; `W4_reports/A6_staging/LEADERBOARD.md:31-55`)
- **MEASURED** — Bodhan (MLX), Gate 1 = CONDITIONAL PASS:
  - bench small_rep CER 0.0540 / WER 0.1356 (≈86.4);
  - 300 gold printed pairs: 0.4034 vs surya 0.5660;
  - sample-100 pages CER 0.6878, unexplained (O-1);
  - PyTorch/CUDA parity blocked. (`docs/campaign/BODHAN_BASELINE.md:15-22`; `W4_reports/blind_verify_gate1.md:10-47`)
- **MEASURED** — No open engine emits Ol Chiki (0/1,755) or Meetei Mayek.
  - Nastaliq is 0.59–0.94 CER on every local engine.
  - Script-mismatch routing gives exactly 0.0000 gain on Nastaliq. (`EDGE_THESIS.md:21,33`; `W1_reports/1E_lensB.md:61-71,243-254`)
- **MEASURED** — All four printed "edges" were killed.
  - Fusion: ensemble beat the best single engine on 0/115 pages.
  - Blanket routing: −0.0351 CER.
  - Akshara-validity argmax: 0.6766 vs 0.4190 single. (`EDGE_THESIS.md:8-17`; `level2/research/gates/B12_ensemble_voting.md:31-47`)
- **MEASURED** — Surya is 100% empty on Sanskrit (Devanagari), not an Ol Chiki issue. That one cell holds 67% of the fusion-oracle gap; without it the gap is 0.0332. (`W1_reports/1F_sonnet.md:91,234`; `W1_reports/1E_lensC.md:95-131`)
- **MEASURED** — GT-trust lock §6.4:
  - BARRED: ks, mni, ur, sat, mr, ne-PDF.
  - SAFE: as, brx, doi, kok, mai, or, pa.
  - VERIFY-FIRST: gu, sd.
  - sarvam_fill never trains. (`docs/research/level7/FINAL_VERDICT_2026-09-27.md:55-77,152-156`)
- **MEASURED** — K1 erratum: only Konkani survives (31 discordant, p=0.003327). Punjabi is a tie (87/90 tied, p=1.0). (`level2/benchmark/docs/fix_specs/W1H_PLAN_FIXES.md:12,25-26`; `KILL_CRITERIA.md:232-238`)
- **MEASURED** — Speed:
  - surya 24.3 s/page ≈ 36 h for 5,344 (another log: 16.3 s);
  - tesseract family ≈ 3.8 h; rapidocr 0.4 s/page;
  - Bodhan 0.52 s/crop on the Mac. (`docs/campaign/RESEARCH_DECISIONS.md:49`; `DISPATCH_LOG.md:299,706`)

**Licences:**
- surya weights: evaluation-only (Modified OpenRAIL-M §2(c) competing product, §8 share-alike to output). The "$5M cap" was never the blocker.
- Bodhan: Indic Open Model License v1.0 — attribution §2.2, hosted API needs written approval §3.1, internal component §3.2; training on its outputs makes a Derivative.
- indic-ocr tessdata sat/mni: Apache-2.0, cleared.
- 600K-KS: HOLD (embedded research-only licence).
- EasyOCR and IndicPhotoOCR weights: UNKNOWN.
- PARSeq code: Apache-2.0.
- IIIT-INDIC-HW-WORDS: CC BY 4.0 on AIKosh (planner read); the ICFHR-2022 page says All Rights Reserved; the IHTR-2023/IHDR-2025 cards say academic-use, so those are eval-only.
- (`RQ9_licences.md:23-28,140-173,199-213,265-314,316-321`; `proto-92-boss-decisions.md:27,34-35`; `LEDGER.md:6121-6142`)

## 2. Architecture v4 rev 2 (portable; each stage mapped to Vinay's PPT)
1. **Input + quality gate** (PPT stage 0, kept and gated).
   - Measure resolution, blur, contrast.
   - Restoration runs only on low-quality inputs and only after R4 passes. Restoration evidence is Latin-only, and super-resolution hurts high-res pages. (`RESEARCH_DECISIONS.md:99`; `Q2.tex:567-569,597-599`)
2. **Route** (PPT stage 1 → Bodhan IndicDocLayout, already Indic-trained, 37 classes, reading order).
   - Crop vs page by aspect ratio and height (test crops are ~300 px, one word).
   - On pages: layout blocks plus a handwritten/printed flag.
   - Script by Unicode ranges on the recognised text (Ol Chiki U+1C50–1C7F, Mayek U+ABC0–ABFF, Arabic block). IndicPhotoOCR script-ID has no sat/mni class.
   - Same-script language ID (bn/as/mni; hi/mr/sa/ne) is NOT solved: flag it, never assume. (`RQ9_licences.md:215-233`; `RESEARCH_DECISIONS.md:43`; `Q3.tex:482-484,614`)
3. **Recognise:**
   - **Handwritten → Handwriting Expert** (§3, Track A). The PPT already had this branch (IIIT-HW / INDIC-HW-WORDS), so this is continuity, not a pivot. (`_reports/research/PPT_FULL_DUMP.md` slide 2; `docs/architecture/PPT_SPEC.md:21,25`)
   - **Printed → Page Expert** (§4, Track B): Bodhan IndicBlockOCR (Qwen3.5-0.8B) on the official PyTorch path. Per-cell work only where a kill-gated recipe exists.
   - **Fallback** (per block, deterministic triggers): empty, wrong-script share, invalid Unicode sequence, repetition loop, low log-prob → licence-clean Tesseract FAST, routed by output script.
     - easyocr for sa (licence check first); indic-ocr sat/mni pack.
     - No ensemble/voting text: agreement is a review flag only.
     - A learned router is built only if the RQ-11 oracle gap is ≥0.02 CER somewhere. (`proto-100-research-to-build.md:39-40`; `history-completed-protocols.md:741-750`; `B12_ensemble_voting.md:31-47`)
4. **Optional RL** (PPT stage 2b, last). Only after SFT plateaus, on human-verified gold only, with an Indic-aware reward.
   - Never on any bench split: "RLVR on small_representative then evaluate on it" is train-on-test and FORBIDDEN.
   - English-favouring RL cost up to 11 points on Indic. (`LEVEL7_RESEARCH_FINDINGS.md:30-36`; `R7_W6_TRAINING_TREE.md:62-68`; `DEEP_RESEARCH_STRATEGY_2026-09-29.md:120`; `LIVE_LATEST_2026-09-29.md:22-27`)
5. **Post-correction** (PPT stages 3/3b → B-18): a separate, separately scored product stage, so raw output stays the benchmark (HL7).
   - Trained only on the same engine's own errors; cross-engine correctors did not transfer.
   - For word crops expect a small gain (little context). (`ULTIMATE_HYBRID_CONCERN.md:36`; `RESEARCH_DECISIONS.md:101`; `Q3.tex:479`)
6. **Outputs** (official focus area 5):
   - layout-preserving JSON per the SOUTH_CANON §G schema; searchable PDF (PyMuPDF); Markdown; per-block language;
   - CLI + Python API + Docker (CPU/CUDA, pinned torch); NOTICE.
   - For the test file: per-image JSON plus an `image,text` CSV.
   - MLX is a Mac accelerator only. (`proto-100:43`; `boss-rules.md:21-27`; `docs/campaign/checkpoints/W4.md:460,551`)
7. **Evaluation layer** (§6): one scorer, tiers, CIs, independent sets, transfer obituaries for every outside number.

## 3. Track A — Handwriting (the official test file)
**Data:**
- **Train** (after U-HW1 and the licence check): the AIKosh CC-BY release of IIIT-INDIC-HW-WORDS Bengali — train 82,554 / val 12,947; test 17,575 or 18,574, to be confirmed from the zip README.
  - Label cleaning before training (up to 1.8 CER points; `Q2.tex:470`).
- **Evaluate only:**
  - BN-HTRd (108,181 Bangla words, 150 writers; licence to check);
  - ICDAR'23 IHTR val/test (100 new writers; academic-use = eval-only, if obtainable);
  - the Bodhan HW bench as an external reference.
- **Pretraining only:** synthetic Bengali words (Pango/HarfBuzz + OFL fonts, aging/ink augmentation per B21). Never evaluation. B21 forbids IIIT-HW text as a synthetic seed. (`product/docs/B21_SYNTHETIC_LINES_SPEC.md:20,32,49-69,136`)
- **Local wiring/regression test:** Gujarati `Bodo/gu` (4,645 images). Fix the paths; never count it as Bengali evidence. ICDAR's best Gujarati WRR is only 62.80.

**Steps** (owners = the boss's agents; no training before G-2.5):
1. **HW-ID — script/word audit of the 5,344** (Agent 1, read-only, now).
   - Vision-check a stratified ≥300-image sample (≥10 per ID bucket); record script, word vs multi-word, and pen/quality.
   - Kill (a): < 80% single handwritten Bengali words → re-plan the router before any training. (`B12_HANDWRITING_SHARE.md:22-41`; proto-108 rev 1 §2)
2. **HW0 — leak gate** (Agent 2, read-only, once candidate sets exist).
   - pHash (crop/scale-tolerant) + SHA of all 5,344 against IIIT bn train/val/test, ICDAR'23, BN-HTRd and `Bodo/gu`; fail closed; exclude and disclose any hit.
   - Also sweep the code: no `gt_text` reads in routers or prompts (the old LayaRouter leak); a B21-style grep gate; a `gt_source` guard so machine/sarvam_fill GT cannot enter a train file. (`proto-98:722`; `QLORA_EVAL_SPEC.md:36-58,309-312`)
3. **HW1 — zero-shot baselines** (Agent 1, no training):
   - IndicPhotoOCR bengali PARSeq; Bodhan handwriting mode on the official PyTorch path; Tesseract `ben` (needs tessdata).
   - On IIIT bn val + an independent-writer set once downloaded; on the 200 official crops, view-only.
   - Report WRR+CRR, CER+WER, median, catastrophic rate (CER>0.5), empty rate, s/word, Wilson/bootstrap 95% CI. Content gates only (Jaccard-5 ≥ 0.3), never script ratio.
4. **G-2.5** (the boss): the multi-LLM evaluation of THIS plan (OpenCode + a fresh hostile Sonnet + a ChatGPT paste), with a data package and verdicts logged, plus the Vinay session.
   - Only Plan v2 was ever evaluated this way (`W1.md:27,80`; `W4.md:117`).
   - G-2.5 explicitly lifts the older "no training before W6 freeze" law.
5. **HW-SMOKE** (Agent 1): 5 items, ≤10 min, memory and disk caps (abort if disk < 20 GB), adapter written; ≥3 failures → abort to baseline; at most 2 re-attempts. (`docs/benchmark_docs/QLORA_SMOKE_TEST.md:53-59,108-115,164-177`)
6. **HW2 — Bengali fine-tune** (Agent 1, GPU):
   - PARSeq from `bengali.ckpt` (if its licence clears; else the PARSeq Apache base) on IIIT bn train, with augmentation; select on IIIT val.
   - Order: synthetic → real → per-script.
   - Optional LM rescoring with the train lexicon; kept only if WRR rises.
7. **HW3 — other scripts:** same recipe, only where IIIT data plus a checkpoint exist and HW2 passed.
8. **HW-P2 levers** (only if HW2 misses the independent-writer gate): SemiHastakshar-style unlabeled writers (licence permitting); per-expert post-correction.
9. **Expected-score statement** (Agent 2): map internal proxies to the unknown official metric. Publish WRR and CRR (exact-word WRR is much lower than CRR: 88.31 vs 95.94 at ICDAR'23).

**Gates** (pre-registered; the operator signs the thresholds before reading results):
- **G-HW0:** overlap = 0 after exclusion.
- **G-HW2 (proxy):** IIIT bn val WRR ≥ 92%.
- **G-HW2 (claim gate):** independent-writer WRR ≥ 85%, writer-disjoint, n ≥ 300 words, 95% CI reported.
- **Promote** an adapter only if a paired test (McNemar exact or paired bootstrap) on the same items gives p < 0.05 AND the gain is ≥ 3 points vs the HW1 zero-shot. Otherwise keep the baseline.
- **Kill:** < 85% IIIT val after 2 epoch-equivalents → switch recipe (CRNN + LM, PERO-style) or init from the PARSeq base.
- Expectation: do NOT promise 96.10. A single PARSeq from scene-text weights is expected near PERO/TrOCR (≈91–92); 96.10 was an ensemble with heavy pretraining.

## 4. Track B — Printed 22-language (product + "multilingual" story; does not move the test score)
**Base:**
- Bodhan on the official PyTorch path.
- First explain O-1 (page 0.69 vs crop 0.054) with an order-invariant page CER.
- Then run Bodhan on the same 99 pages and 300 gold pairs as the MLX run (R-13 parity).
- Then run it on the full manifest_v2 with tiers. (`proto-104:22-25,68-71`; `BODHAN_BASELINE.md:17-18`)

**Baseline panel** (labelled printed-only, eval-only for surya):
- per-language CER with n and tier from sheet_v2;
- surya 0.3944 as the evaluation reference;
- tesseract family for or/mr/ne;
- honest-n: as 19, sat 20, mni 20, gu 24, doi 27, ne 37, brx 67, or 69.
- (`SAMPLING_PLAN.md:11,19,49`; `docs/campaign/BENCHMARK_22.md:94-115`)

**Per-cell plan** (each: in-scope / fallback / non-goal, its recipe and its kill):
- **sat (Ol Chiki): in-scope via Bodhan.**
  - Day-1 zero-shot on the 20 probe items: charset errors, script adherence ≥ 0.95 reported apart from CER.
  - Baseline: the indic-ocr Apache sat pack (boss download).
  - Synthetic Ol Chiki (R3: Noto Sans Ol Chiki, HarfBuzz, ≥80% script gate, font-disjoint val) only if Bodhan shows charset errors; needs a real-scan validation set.
  - sat is BARRED from SFT on fill GT, and the K2(b) micro-repair is killed.
  - (`proto-100:36-37`; `R3_OLCHIKI_MAYEK_SYNTHETIC.md` via `corpus_extract.md:92-96`; `KILL_CRITERIA.md:198-199`)
- **mni (Meetei Mayek): in-scope via Bodhan.**
  - Compare NE-OCR (CC-BY-4.0, 86M, 95.56% char accuracy) against Bodhan on the 20 items.
  - The router sends U+ABC0–ABFF to the winner.
  - The indic-ocr mni pack is the fallback. (`docs/research/level7/c/c2/LEDGER.md:91-93`)
- **ks / ur (Nastaliq): fallback only now; a P2 specialist later.**
  - First B-02: an opt-in Arabic-normalised scorer (raw + normalised; 3–8 points may be scoring artefact).
  - B-01: bf16/8-bit only for Perso-Arabic; QARI 4-bit gave CER 3.45 vs 0.091 at 8-bit.
  - Training only after the boss's go: QARI-style 50k synthetic lines from KS-PRET-5M + Awami Nastaliq ≥3.300 (U+0620 in every batch) + 300–500 verified real lines, autoregressive decoder.
  - Gate: ks CER ≤ 0.20 on held-out real lines; abort > 0.30.
  - 600K-KS stays on HOLD. Routing gives 0 gain here.
  - (`B02_ARABIC_NORMALIZATION.md:5-12,132`; `B01_4BIT_ANALYSIS.md:5`; `proto-100:33-35`; `c3/LEDGER.md:164,765`)
- **or (Odia): fallback.** The tesseract family wins locally (0.2588, n=69). Any fine-tune must beat Gemini 81.01 and Chitrapathak-2, not just Sarvam 80.01. Not planned. (`1G_verify.md:66-74`; `a/LEDGER.md:3803`)
- **sa (Sanskrit): fix the routing.**
  - Surya is 100% empty there (cause untested: layout parse vs coverage); easyocr holds 0.175.
  - Route sa away from any empty-prone engine; the deterministic empty-trigger covers it.
- **kok (Konkani): non-goal for training.** The K1 pass (19.4 points) is local only, and Sarvam already scores 97.41. The QLoRA stays an optional printed-side option, not the default. (`W1A_PACKET_AUDIT.md:175-176`)
- **Old scans / restoration (R4): gated experiment.**
  - Arms A0 none / A1 deskew+Otsu / A2 deskew+Sauvola / A3 DocRes pilot.
  - Adopt only if median ΔCER ≤ −0.03, the 95% CI excludes 0, on ≥2 of 3 frozen engines, with no dot/matra regression, and CPU ≤60 s.
  - Build the ~40-page labelled old-scan slice first. Never apply to Nastaliq/Ol Chiki without our own evidence. (`proto-100:38`; `LEDGER.md:53-58,3414`)
- **South (ta/te/kn/ml):**
  - Ground truth from the Sarvam-bench fill: eval-only forever, tier `sarvam_bench`, counted once (it sits inside the 6,909).
  - The official South PDFs are 0/23,001 clean. (`SOUTH_RERUN_FEASIBILITY.md:9-24`)
- **Alternate backbones** (PaddleOCR-VL 1.6, GLM-OCR, dots.mocr, MonkeyOCRv2): post-freeze hedges only, head-to-head on our manifest, after a boss-approved download. Never chosen from OmniDocBench numbers. (`ELITE_REPO_REFRESH_2026-09-27.md:15,23`)

**Printed gates:**
- **G-P1 (Bodhan LoRA, if ever):** held-out CER improves with a CI excluding 0; no language regresses by > 1 point; promotion by paired test p < 0.05 and gap ≥ 3 points.
- **Quantisation:** no 4-bit without per-script parity. Calibrate on Bengali, Ol Chiki, Nastaliq, Mayek and Odia. KV cache in bf16. (`c/c1/LEDGER.md:34-37,237-240`)

## 5. Track C — Product & jury (how we are actually scored)
**One artifact per official criterion:**
- **Approach / innovation:** the two-expert architecture (§2), the PPT → v4 stage table (§2 notes), and the honest evaluation layer nobody else publishes — handwriting + abstention + CIs + independent writers. (`COMPETITOR_INTEL.md:42,77-83`)
- **Business use case:** governance/archive handwriting (forms, exam scripts, records); lead the demo with that, not a CER table. (`c2/LEDGER.md:10,298`)
- **Technical feasibility:** a 50-image timed dry run on CPU/CUDA giving JSON + PDF + MD, s/page, memory, extrapolated to 5,344; pinned torch; parity vs MLX. (`proto-99:30-36,188`)
- **Product roadmap:** page-level handwriting (PLATTER/IHDR-2025), transliteration, the weak cells (§4), Bhashini Udyat/dhruva-api-shaped endpoint.
- **Team:** the solo operator plus an agent workforce with an audit trail (W4/DISPATCH_LOG).
- **Addressable market:** a 4-year deployment and customisation cost, IPR, O&M.
  - Cost anchors: ₹0 offline vs Sarvam ₹0.5/page (≈₹2,672 for 5,344), Bodhan ₹0.20/image, Mistral $2/1000.
  - The real prize in comparable hackathons is a deployment contract. (`a/LEDGER.md:882-885,4109`; `c2/LEDGER.md:13,26-28,287,290`)

**Packaging:**
- Bodhan ships only as an unmodified internal component (§3.2), with a NOTICE line.
- No hosted Bodhan endpoint without written approval.
- surya never ships. (`RESEARCH_DECISIONS.md:42`)

**Claims:**
- Allowed: "we do not claim to beat 87.39; we compete on handwriting, independent evaluation, offline cost and deployability".
- Never:
  - a cross-bench head-to-head;
  - "we lead 10/18";
  - winners at n<50;
  - the student-repo CER rubric presented as official;
  - Oct 4 / Oct 15 / "qualifiers 30/09" as our deadline. (`RQ1_official_rules.md:311-317,400-423`; `W1.md:246`)

**Other jury-room items:**
- A one-page EXPLAIN_CARD and a 25-question drill for the jury. (`proto-85:12-22`)
- Confirm VaultStack's stage before any "finalist" wording; one uncorroborated post says Finals. (`c2/LEDGER.md:20-24,299`)

## 6. Evaluation law (applies to every number in every track)
1. **One scorer.** One committed, self-validating scorer: numpy Levenshtein, uncapped CER, empty = CER 1.0, one denominator, an NFC statement, a danda whitelist. sheet_v2 semantics; sheet.csv is never presented as checkable (62.9% of its rows don't re-derive). (`SHEET_V2_FORENSICS.md:3-56`)
2. **What to report:** set, n, tier, CER+WER (WRR+CRR for handwriting), median, catastrophic rate (CER>0.5), abstain/coverage, Wilson or bootstrap 95% CI with a fixed seed. (`c4/LEDGER.md:1035-1077`; `W1_reports/1E_lensC.md:159-169`)
3. **Winners and comparisons:** n ≥ 50 to name a winner; paired McNemar exact or paired bootstrap on the same items; GT tiers are never pooled.
4. **Win-claim law R-12:** a published split + scorer AND a win on an independent set. (`proto-104:63-67`)
5. **Transfer obituaries:** every outside number (Sarvam 87.39, Bodhan 84.94/86.4, Bodhan-HW 74.8/71.3/58.3, ICDAR 96.10) is labelled DIRECTIONAL until re-measured with our scorer on our split. (`level2/benchmark/docs/transfer_obituaries.md:169-184`; `OBITUARIES.md:1-8,350-351`)
6. **Sampling proof for any set we build:** per-source/page/writer table, top-1 share ≤ 50%, no first-page-only, no one-document sets. (`SAMPLING_PLAN.md:12-16,61-76`)
7. **Self-evaluation guard:** a separate verifier re-runs every number from scripts it did not write; at most 2 fix rounds; no LLM self-judgement promotes a model. In one study agents claimed improvement in every cycle while 56% of cycles had Δ ≤ 0. (`artifact_200_orchestra_bench.md:124-125`)
8. **GT hygiene before any PDF-layer GT is reused:** a legacy-font mojibake detector (52/115 "clean" South pages were mojibake), a script-purity check, and `GT_DEFECTS.md` (step Q) before D2. (`B12_ensemble_voting.md:88-98`; `proto-65:19-27`)

## 7. Kill table (pre-registered; the operator signs T-values before results)
- **K-ID:** HW-ID sample < 80% single Bengali handwritten words → re-plan the router and data.
- **K-HW0:** any overlap → exclude and disclose; if the official test ⊂ IIIT train, the headline rests on independent writers only.
- **K-HW2:**
  - < 85% IIIT val after 2 epoch-equivalents → switch recipe;
  - independent writers < 85% → no claim;
  - no paired win of ≥ 3 points at p < 0.05 vs zero-shot → ship the zero-shot.
- **K-SMOKE:** ≥ 3 of 6 smoke criteria fail, or > 2× wall-clock → abort to baseline; 2 retries max.
- **K-P1:** Bodhan LoRA lowers held-out CER with a CI excluding 0 and no language regresses > 1 point; otherwise no adapter.
- **K-ROUTER:** a learned router only if the oracle gap is ≥ 0.02 CER somewhere; blanket routing measured −0.0351.
- **K-R4:** restoration adopted only on median ΔCER ≤ −0.03, CI excluding 0, ≥ 2/3 engines, no dot/matra regression.
- **K-KS:** ks CER ≤ 0.20 on held-out real lines to keep; abort > 0.30.
- **K-POSTCORR:** ships only if it wins on held-out items in a separately scored stage.
- **K-SHIP:** the 50-image dry run fits the time budget; JSON/PDF valid; licence ledger has no open row for a shipped component; every artifact number has its command.

## 8. Licence ledger (ship-blocking; an open row blocks shipping that component)
- Bodhan weights: Indic Open Model License v1.0 → internal component, attribution, no hosting without written approval. **OPEN:** read the three HF cards (an Apache / CC-BY-SA mismatch appears in older notes).
- surya: evaluation-only. Never shipped, never a label source; no pseudo-labels from it.
- Tesseract + tessdata (incl. indic-ocr sat/mni): Apache-2.0, attribution copy required. Downloads need the boss.
- PARSeq code: Apache-2.0. IndicPhotoOCR / STocr recognition weights: **OPEN.**
- IIIT-INDIC-HW-WORDS: CC BY 4.0 (AIKosh) → train. **OPEN:** confirm from the AIKosh page and the zip README. ICFHR-2022 / IHTR-2023 / IHDR-2025 → eval-only.
- BN-HTRd: **OPEN.** EasyOCR .pth and CRAFT weights: **OPEN.**
- 600K-KS: HOLD. UTRSet/UTRNet, Odia-Lipi, IndicCorp: NC lineage, barred from product weights.
- Fonts: Noto (OFL), Awami Nastaliq ≥3.300 (OFL); provenance logged per batch.

## 9. Compute, time, environment
- **Training happens on the 24 GB GPU over SSH.** The hardware is confirmed second-hand; the login is still missing (O-3).
  - Fallback if it never arrives: PARSeq fine-tuning on Mac MPS is feasible (small model), but it is a dev path; product claims must reproduce on PyTorch CPU/CUDA.
  - All old time estimates (3 h / 6 h / 7–8 h / 5–7 days) were MLX printed-page estimates and do not transfer. (`proto-99:208-213`; `W6_QLORA_SPEC.md:33-46`)
- **Budget per stage, logged in RUN_STATE:**
  - HW1 inference only;
  - HW2 GPU-hours cap set by the boss at G-2.5;
  - P1 only after HW2;
  - night-run rules R-15 apply (resumable, device tag, heartbeat, 20 GB disk floor).
- **Separate pinned environments or containers** for the HW expert: the MLX install pushed numpy to 2.2.6 and broke IndicPhotoOCR (pin 1.26.4). (`level2/benchmark/docs/MLX_INSTALL_RESULT.md:103-122,266-286`)
- **Before training, bundle with checksums:** the eval assets (benchmark pages, test hash manifest, scorer, sheet_v2) and the GT. Data moves by rsync, never GitHub. (`W4_reports/A1_verify.md:101-129`)

## 10. Contradictions (resolved → working rule; open → owner)
- **Bengali 96.10 vs 88.31 WRR:** resolved. Bengali Table 2 vs the 10-script average; cite Table 2.
- **"Bodo/gu = copy of the test set":** resolved, false (sha256 overlap 0). HW0 still hashes it.
- **Tesseract trio byte-identical:** false. They differ on 857/1,227 items; only openbharatocr ≈ tesseract_indic. 9 independent engines; the tesseract family counts as 1 vote.
- **pa K1:** a tie (p = 1.0). QLoRA scope = Konkani only.
- **IIIT licence (CC BY 4.0 vs academic-use):** working rule = train on the AIKosh release only; confirm before HW2. OPEN, Agent 2.
- **Bodhan licence (Indic Open Model License vs Apache vs CC-BY-SA):** the Indic Open Model License is binding until the cards are read. OPEN, Agent 2.
- **Post-correction vs HL7 "no spell-correction":** resolved. A separately scored product stage; raw is the benchmark.
- **"No training until W6 freeze" vs HW2:** resolved by G-2.5 being the sole training gate (with the boss's go).
- **Surya speed 24.3 vs 16.3 s/page; Mac memory 24 GiB vs "M2 Max 32 GB":** OPEN. Use measured hardware only; re-time on the GPU.
- **Sarvam bench 6,909 vs 6,609 vs 20,267 samples:** 6,609 is 6,909 minus 300 English; 20,267 is unexplained. Use 6,909.
- **Meeting date Sep 25 vs Sep 29:** the transcript wins (Sep 29).
- **A4 "PASS" posted while the smoke test was structurally blocked** (`run_probe.py` parents[2]): OPEN, U10 locked-file erratum, Agent 2.
- **Repo lineage:** README/INDEX/gold-repo T1 still cite "proto-104 rev 4 + Plan v3". Add proto-108 to the law chain (Agent 2 applies; the planner owns the text).

## 11. Boss decisions (one line each)
- **U-HW1:** download IIIT-INDIC-HW-WORDS Bengali from AIKosh after Agent 2 confirms the licence and size — recommend YES.
- **U-HW2:** eval-only sets (BN-HTRd after its licence check; ICDAR'23 val/test if obtainable) — recommend YES.
- **U-HW3 / G-2.5:** run the multi-LLM evaluation of this plan, then the Vinay session; set the HW2 GPU-hour cap.
- **U-TESS:** indic-ocr sat/mni pack (~4.4 MB) + `ben` tessdata — recommend YES.
- **U-ORG:** ask Vinay whether to email gic.dibd@gmail.com about metric/format/deadline.
- **Carried:** O-2 (the 12 South Sarvam outputs were lost with the old key; a re-run of about ₹6 only on the boss's yes), O-3 (GPU SSH), GO-A/GO-D/GO-G (proto-107), U14/U27/U28 (surya / 600K-KS / Bodhan hosting).

## 12. Paste lines (one per agent)
1. **Agent 1:** `Read proto-108 (rev 2, top section). Now, read-only, no downloads/training: HW-ID — vision-check a stratified sample of >=300 of the 5,344 official test crops (>=10 per ID bucket), record script / single-word vs multi-word / quality per image in level2/benchmark/docs/HW_ID_AUDIT.md with the image IDs; then HW1 on what is local: IndicPhotoOCR bengali PARSeq + Bodhan handwriting mode on 200 viewed official crops (outputs + s/word only, no accuracy claims). Report the AIKosh URL + size for IIIT-INDIC-HW-WORDS Bengali. Log every step with its command in W4.md.`
2. **Agent 2:** `Read proto-108 rev 2. (1) Licence ledger rows: read and quote the AIKosh IIIT-INDIC-HW-WORDS licence, the IIIT bn zip README counts, the STocr/IndicPhotoOCR weight licence, PARSeq LICENSE, BN-HTRd licence, the three Bodhan HF cards — write RESEARCH_DECISIONS rows. (2) Write the HW0 script (pHash+SHA, stdlib+PIL, fail-closed) and the gt_text/gt_source code sweep. (3) Prepare the G-2.5 multi-LLM package (plan + data, not conclusions). (4) Add proto-108 to the law chain in docs/INDEX.md and AGENTS.md (pre-images first).`
3. **Agent 3:** `Rename, do not delete: docs/campaign/protocols/proto-107-gate1-and-s5-ssot.md -> ecc-note-gate1-and-s5-ssot.md and proto-108-md-consolidation.md -> ecc-note-md-consolidation.md (sha manifest + log line first, git mv if tracked), add an alias line to proto-00; then the 50-image timed dry run of product/ on CPU (JSON+PDF+MD, s/page, peak RAM) with a pinned torch requirement; no Bodhan hosting, no downloads.`

## 13. Still open after this pass (from the critic and the digests)
- The memory partitions (P49, P50) are not fact-checked; their claims stay "unchecked" until a verifier can read `_claude_memory/`.
- Several digest citations are file-level only or come via corpus_extract; re-anchor before slides.
- No Bengali labelled handwriting, no writer-disjoint Bengali set, no handwriting baseline yet: Track A numbers are all future.
- The official metric, format and deadline are UNKNOWN; the 92%/85% gates are internal proxies.
- O-1 (Bodhan page 0.69 vs crop 0.054) is unexplained; the Page Expert claim waits on it.
- Critic (`digests/critic.json`): 71 corpus files had no partition. Most were read in full by the previous planner and are summarised in `corpus_extract.md` (R1–R7, W6_STRATEGY_UNIFIED, PPT dumps, architecture docs), and about 45 are protocol copies mirrored in memory. A second pass over the 71 is P2.
- P04 and P08 had many line-anchor corrections (14/41 and 22/54); facts held but anchors drift.

Related: [[proto-104-project-first-critical-path]], [[proto-89-plan-v3-bodhan-base]], [[proto-100-research-to-build]], [[proto-105-consensus-results-to-decisions]], [[proto-106-vinay-call-and-gpu-day1]], [[proto-107-gold-repo-consolidation]], [[boss-rules]]

---

# HISTORY — Plan v4 rev 1 (2026-10-01 ~15:45 IST; superseded by rev 2 above; kept for audit, do not execute from it)


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

## Artifacts (published 2026-10-01 ~16:15 IST; both Docs updated to rev 2 by the cloud planner — Plan v4 doc rev 16, showcase rev 30)
- Showcase for Vinay (the previous plan Doc, rebuilt + renamed): https://claude.ai/artifact/Fn257YXfs4RD5htjZMUR3i — "AksharDrishti by Vaultstack — Project Showcase"
- Plan v4 (separate Doc): https://claude.ai/artifact/X3Bg1Mg58pPzrB6AcGEan9 — "AksharDrishti — Plan v4 (final)"
- The 3-hour integration loop (boss order) refreshes both from agents' results: HW1 numbers, HW0 overlap, licence checks, proto-107 gold facts.
