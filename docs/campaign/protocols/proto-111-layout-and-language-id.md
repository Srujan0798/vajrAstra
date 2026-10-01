---
name: proto-111-layout-and-language-id
description: "2026-10-01 — Vinay: 'first we need to add a really good layout and language detection model'. Track L (runs now, ahead of Bodhan LoRA): pick and prove the layout detector (Bodhan IndicDocLayout vs IndicDLP-trained vs DocLayout-YOLO/PP-DocLayout) and a two-level language ID (image script-ID before OCR + text LID after OCR) on labelled eval sets, with gates; no training before G-2.5; downloads need the boss."
metadata:
  node_type: memory
  type: project
---

# PROTO-111 — LAYOUT + LANGUAGE DETECTION — STATUS: PROPOSED / ON HOLD (planner self-correction, 2026-10-01)

**HOLD:** I accepted Vinay's line without testing it against our evidence; that was a mistake. Until he answers the clarification questions in §0, this track does NOT displace Track A (handwriting) and does NOT become "first".
- Only L0 (read-only eval-set building) may run, because it is cheap.
- L1–L4 wait for his answers.

## 0. Critical review of "first a really good layout + language detection model"
- **On the test file it moves nothing.** The official test file is 5,344 single handwritten word crops (16/16 viewed are Bengali). A word crop has no layout to detect. Language on one word = its script, and if the set is all Bengali that is a constant. Neither model moves the score on the file we were given. (`TEST_SET_PROFILE.md:35-47`; `W4.md:431`)
- **We already have a strong Indic layout model and have not measured it.** Bodhan IndicDocLayout: 37 classes, reading order, Indic-trained, on disk. "Add a really good one" before measuring ours is building blind. Our benchmark has no layout ground truth, so nothing can be scored yet.
- **Same-script language ID is an unsolved research problem** (bn/as/mni; hi/mr/sa/ne/mai/doi/kok/brx). It is a time sink with no published OCR evidence. Distinct-script language ID is nearly free (Unicode ranges).
- **Where he is right:**
  - layout + language detection are named official focus areas (jury/product);
  - Bodhan's page CER 0.69 vs crop 0.054 (O-1) may be a reading-order/layout problem, so layout matters for PAGES;
  - his own PPT had DocLayout-YOLO + an IndicDLP stage.
- **Questions for Vinay** (must be answered before L1):
  1. Does he know the official test file is single handwritten word crops? Or does he know the final evaluation uses full pages or forms?
  2. Is "first" for the product demo, or for the test submission?
  3. "Really good" against what? Which dataset and metric (IndicDLP mAP, reading-order accuracy)? Does he have a model in mind?
  4. Is language ID needed per page, per block or per word, and must it separate same-script languages?
  5. Can we use IndicDLP / IndicLID (licences), and is a layout fine-tune inside the G-2.5 training gate?
- **Planner recommendation:** keep Track A (handwriting recogniser) as the score item. Run L0 now. Measure Bodhan layout + Unicode script ID (L1) only after he answers. Build or fine-tune nothing for layout or LID until a measured gap exists.


**Vinay (2026-10-01, WhatsApp, PRIMARY via the boss):** "first we need to add a really good layout and language detection model".
**Planner reading:**
- This matches the official focus areas: layout-preserving JSON plus language detection (`RQ1_official_rules.md:247-271`).
- It matches his own PPT stage 1: DocLayout-YOLO + an IndicDLP LoRA (`docs/architecture/PPT_SPEC.md`; proto-108 rev 1 §3).
- Track L becomes the FIRST build item of Track B/C. It runs in parallel with Track A (handwriting) and does not block it.

## 1. What we already know (cite before quoting)
**Layout:**
- **Bodhan IndicDocLayout:** 33M parameters, PP-DocLayoutV3 / RT-DETR, 37 classes, reading order, Indic-trained. It is on disk with the Bodhan weights. (`proto-89-plan-v3-bodhan-base.md:17,20`; `DISPATCH_LOG.md:590-599`)
- **IndicDLP** (arXiv 2512.20236): 119,806 images, 42 classes, MIT. It is the strongest public Indic layout dataset. (`docs/campaign/RESEARCH_DECISIONS.md:89-93`; `docs/research/level7/c/c3/LEDGER.md:403`)
- Layout + reading order is rated 8/10 evidence. Fusion of OCR engines is not a lever; adaptive selection is. (`RESEARCH_DECISIONS.md:89-93,98,102`)
- **Our benchmark pages carry NO layout ground truth.** Layout claims need an external labelled set (IndicDLP test split, eval-only) or a hand-labelled sample.

**Language ID:**
- **IndicPhotoOCR script-ID:** a ViT with 12 classes and NO Ol Chiki or Meetei Mayek class. Code is MIT; the weight licence is open. (`RQ9_licences.md:215-233`)
- **Script from Unicode ranges** on the recognised text is free and exact for distinct scripts: Ol Chiki U+1C50–1C7F, Mayek U+ABC0–ABFF, Perso-Arabic block. (`RESEARCH_DECISIONS.md:43`)
- **Same-script languages are NOT solved in OCR output:**
  - Bengali-script: bn / as / mni-Bengali;
  - Devanagari: hi / mr / sa / ne / mai / doi / kok / brx;
  - Perso-Arabic: ur / ks / sd. (Sindhi in the bench is Devanagari.)
  - Source: `docs/sources/consensus/2026-09-30_Q3_system-layout-postcorrection-langid-eval.tex:482-484,614`; `docs/benchmark_docs/LIST.md:7,29`
- **IndicLID** (text, AI4Bharat) and **GlotLID** are candidates. Their licences are unverified and each needs a download. Laya is rejected (text-only, near-random on non-Latin). (`RESEARCH_DECISIONS.md:46,103`; `proto-92:37`)
- **Labelled language eval already on disk:**
  - the Sarvam bench: 6,909 blocks, 22 languages + en, eval-only forever;
  - manifest_v2: 1,683 items with lang tags.

  Both are EVAL ONLY: never train on them. (`proto-104 R-7, R-12`)

## 2. Design (two levels, portable)
- **L-layout (pages only):** a detector that returns blocks with type, bbox, reading order and a handwritten/printed flag.
  - Default: Bodhan IndicDocLayout, already Indic-trained and on disk.
  - Challengers: a model trained on IndicDLP (MIT), DocLayout-YOLO, PP-DocLayout.
  - Choose by measured score, not by name.
- **L-script (before OCR, per block or crop):** an image script classifier routes each block to the right recogniser. Candidates:
  - the IndicPhotoOCR ViT (12 classes) plus an "other" fallback;
  - Bodhan's own output script (Unicode ranges), used as a second opinion after a first pass.
- **L-lang (after OCR, per block):**
  - distinct scripts → language follows from the script (Ol Chiki = sat, Mayek = mni, Gurmukhi = pa, Odia = or, Tamil = ta…);
  - same-script → text LID (IndicLID or GlotLID) on the recognised text, with a confidence;
  - below threshold → output the script plus a top-2 language with "uncertain"; never a silent guess.
- **Word crops (the official test):** language = script for nearly all; text LID on one word is weak. The JSON carries script + language + confidence.

## 3. Steps (owners = the boss's agents; no training before G-2.5)
- **L0 — Eval sets** (Agent 2, read-only, now):
  - Language: build `level2/benchmark/docs/LID_EVAL.md` from the Sarvam bench blocks (lang labels) + manifest_v2 lang tags. Per-language n; same-script groups marked.
  - Layout: state what labelled layout set we can use (IndicDLP test split → needs a download; else hand-label 50 benchmark pages for block type + reading order).
- **L1 — Baselines on what is local** (Agent 1, no training, no downloads):
  - Bodhan IndicDocLayout on 50 pages: block counts, reading order, timing.
  - IndicPhotoOCR script-ID on the Sarvam-bench blocks.
  - Unicode-range script on Bodhan's outputs for the same blocks.
  - Report script accuracy per language and the confusion matrix, with Wilson CIs and n per cell.
- **L2 — Candidates** (after the boss's downloads):
  - IndicLID and GlotLID on the same blocks (text LID, same-script groups reported separately);
  - IndicDLP test split + one challenger layout model;
  - licence rows written first (proto-108 §8).
- **L3 — Decision** (the planner, from the numbers):
  - Layout: keep Bodhan unless a challenger wins by ≥ 3 mAP or reading-order accuracy, with a CI excluding 0, on the same pages.
  - LID: pick per script group; report macro accuracy and the same-script groups separately.
- **L4 — Fine-tune** (only after G-2.5 and the boss's go):
  - Layout LoRA on IndicDLP train (MIT) if Bodhan trails on Indic forms or tables.
  - LID fine-tune only on licensed text, never on bench text.

## 4. Gates
- **G-L0:** the eval sets exist with per-language n; the same-script groups are listed.
- **G-L1:** a script-ID confusion matrix exists. The ship bar is script accuracy ≥ 98% on distinct-script languages, with n and CI reported.
- **G-L2:** for same-script groups, report top-1 and top-2 accuracy. A model ships only if it beats "most frequent language in the group" by ≥ 10 points with p < 0.05.
- **G-L3 (layout):** a challenger replaces Bodhan only with the ≥ 3-point win above. No language or document type may regress by > 2 points.
- **Always:** one scorer, eval-only bench data, no training on test or bench text, portable PyTorch path, licences cleared before shipping.

## 5. Boss decisions
- **U-L1:** downloads, with sizes reported first:
  - IndicLID (or GlotLID) — recommend YES after its licence row;
  - the IndicDLP test split (eval) — recommend YES.
- **U-L2:** IndicDLP train for a layout LoRA — only after G-2.5.

## 6. Paste lines
1. **Agent 2:** `Read _claude_memory/proto-111-layout-and-language-id.md. Do L0 now (read-only): build level2/benchmark/docs/LID_EVAL.md from the Sarvam-bench block language labels + manifest_v2 lang tags (per-language n, same-script groups marked, EVAL-ONLY); state the usable layout eval set; write licence rows for IndicLID, GlotLID, IndicDLP, IndicPhotoOCR script-ID weights. Log in W4.md.`
2. **Agent 1 (after its current HW-ID/HW1 step):** `Read proto-111. L1 on local models only, no downloads, no training: Bodhan IndicDocLayout on 50 benchmark pages (blocks, reading order, s/page); IndicPhotoOCR script-ID on the Sarvam-bench blocks; Unicode-range script on Bodhan outputs for the same blocks; per-language script accuracy + confusion matrix with Wilson CI and n. Log in W4.md.`

Related: [[proto-108-plan-v4-final]], [[proto-104-project-first-critical-path]], [[proto-89-plan-v3-bodhan-base]], [[proto-105-consensus-results-to-decisions]]

## UPDATE 2026-10-01 (later) — Vinay's answer and the hybrid decision (planner)
**Vinay (verbatim):**
- "we have 2L images dataset";
- "overall plan is to go step by step doing each step properly which helps in our final goal to identifying the right character, word and sentence";
- "1. Localize: Use DocLayout-YOLO to extract the precise structural bounding boxes.
  2. Crop & Predict: Pass each cropped bounding box straight into AI4Bharat's IndicLID to tag it (e.g., Block 1 = Marathi, Block 2 = English, Block 3 = Gujarati).
  fallback: If the document scan is low quality and text-based OCR might output gibberish, … QuickHawk/trocr-indic … decodes [text lines] while prefixing the correct <LANGUAGE TOKEN>."

**Review (what holds, what does not):**
- **NEW FACT:** a 2-lakh (200,000) image dataset. Unknown: what it is, its labels, its rights, and its relation to the 5,344 test crops. It could be the biggest lever in the project. Ask before anything else.
- **Holds:** step-by-step character → word → sentence. This matches the curriculum word → line → block in R7 (50/35/15).
- **Does NOT hold as written:** AI4Bharat IndicLID is a TEXT language identifier (native + romanised text). It cannot read an image crop.
  - So the order must be: layout → visual script ID → OCR → IndicLID on the OCR text.
  - Verify on the IndicLID card before quoting.
- **Visual language ID** (trocr-indic token, IndicPhotoOCR ViT) can only separate SCRIPTS. Hindi / Marathi / Sanskrit / Nepali look identical, and so do Bengali / Assamese. Those need text LID after good OCR.
- **DocLayout-YOLO:** a strong general layout model (DocSynth-300K pretraining), but not Indic-trained.
  - Its licence is believed AGPL-3.0 (YOLO/ultralytics lineage). VERIFY: it may be unsuitable for a closed product.
  - Bodhan IndicDocLayout (Indic-trained, 37 classes, reading order) is already on disk.
- **QuickHawk/trocr-indic:** a community HF model with unknown training data, accuracy and licence. Line-level TrOCR. Candidate only, until its card is read and it is measured.
- **On the 5,344 test crops** (single handwritten words) layout does nothing and LID = script. The pipeline above is for documents (the product and possibly the 2L set).

**Hybrid decision (fair bake-off, keep what wins, his pipeline in the right order):**
1. **Layout:** DocLayout-YOLO (his choice) vs Bodhan IndicDocLayout (ours) on the same labelled pages (IndicDLP test split or 50 hand-labelled pages).
   - Pick by mAP@0.5 and reading-order accuracy, with a CI.
   - If neither wins clearly on Indic pages, use Bodhan (licence and Indic) and keep YOLO as the fallback.
2. **Visual script ID per block** (before OCR): IndicPhotoOCR ViT (12 scripts) vs trocr-indic's language token. Measured on the Sarvam-bench blocks (labelled, eval-only).
3. **OCR per block** with the recogniser for that script (Bodhan for printed, the handwriting expert for handwritten).
4. **Text LID:** IndicLID on the OCR text, for same-script languages.
5. **Agreement check:**
   - visual script ≠ OCR-text script → low-confidence flag → fallback model (trocr-indic) + "uncertain" in the JSON;
   - never a silent guess.

**Status change:** proto-111 is no longer on hold. It runs as a product-side bake-off.
- Owner: **Agent 3**, after its D0 truth check.
- Agent 2 builds the eval sets (L0) after the scorer.
- Agent 1 stays on Track A (the test score).
- Downloads needing the boss: DocLayout-YOLO weights, IndicLID, trocr-indic, IndicDLP test split. Each one only after its licence row.

**Questions to Vinay (send before building):**
1. The 2L images: what are they (pages / lines / words; printed / handwritten), which languages, which labels (text? layout boxes? language?), may we train on them, and are the 5,344 test crops separate from them?
2. Will the final evaluation use full documents like these 2L images, rather than the 5,344 word crops?
3. IndicLID reads text, not images. OK to run layout → script ID → OCR → IndicLID, with a visual model only as the fallback?
4. DocLayout-YOLO's licence looks like AGPL-3.0. Is that acceptable for the product? We'll benchmark it against Bodhan's Indic layout model on the same pages and keep the better one.
5. trocr-indic: do you know its training data or accuracy? We'll measure it as the fallback.
