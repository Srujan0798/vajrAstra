# PPT_VS_SPEC_DIFF — AksharDrishti_Hackathon_Proposal final.pptx vs docs/architecture/PPT_SPEC.md

**Dumped 2026-09-29 by AGENT-1.** Source PPTX: `AksharDrishti_Hackathon_Proposal final.pptx` (4 slides, 13.33in×7.5in widescreen). Author metadata: PptxGenJS (template/programmatic), created 2026-07-23 10:19:54, revision 0. **No speaker notes present.**

---

## A. WHAT PPTX CONTAINS (FULL DUMP at `PPT_FULL_DUMP.md`)

### Slide 1 — Team & Idea (intro)

- **Title text:** "Multimodal OCR Intelligence for Indian Languages"
- **Brand:** "AksharDrishti · BHASHINI Hackathon Technical Proposal · VaultSatck AI" (note typo "Satck" — appears verbatim in source)
- **Team (3):**
  - Vinay Gahlot — CEO | IIM Ahmedabad | MIT AI/ML TA | MERCOR | AI Advisor
  - Akshay Gahlot — CTO | IIT Delhi CSE | AI systems development and deployment in Trading Firms
  - David Babu — AI Advisor | Global Hackathon winner — Kaggle 1B param reasoning model development
- **The idea, briefly:** "A novel OCR system for all 22 scheduled Indic languages — closing the gap between what general-purpose and frontier OCR/VLM engines achieve on Indian scripts today, and what production, citizen-facing digitization actually requires."
- **3 capability icons (NEW IN PPTX — not in PPT_SPEC):**
  1. **Layout Detection** — "Akshara-aware recognition, tuned to resolve conjuncts, matras & sandhi."
  2. **Fine Text Recognition** — "Calibrated confidence, visual lookup & per-language morphological checks."
  3. **Finetune Semantic and removing errors** — "Structured fields & low-confidence spans route to human review, always."

### Slide 2 — Dataset Preparation (intro)

- **Title:** "Dataset Preparation" + tagline "Six external sources, layered by role — plus a proprietary corpus grounded in real government and examination documents."
- **TABLE (6 sources, 5 cols Source|Type|Scripts/Scale|Primary use):**
  1. **BSTD** (AI4Bharat / Bhashini-IITJ) — Scene text real photos, 11 Indian languages, benchmark-scale growing → Scene-text branch fine-tune + eval
  2. **IIIT-HW-Dev / -Telugu / -INDIC-HW-WORDS** (IIIT-H CVIT) — Handwritten words, 10 Indic scripts, ~872K word images → Handwriting branch pretrain/fine-tune
  3. **AI4Bharat Sangraha / IndicCorp** — Text corpus (no images), 22 languages, billions of tokens → Source text for synthetic rendering
  4. **Bhashadaan – Dekho India (extended)** — Crowdsourced images + labels, all scheduled languages, continuously growing → Real-world diversity, ongoing flywheel
  5. **Govt / institutional partner scans** — Real domain documents, priority 8–10 languages first, 5K–10K pages/domain → Domain-specific fine-tuning (forms, land records, courts)
  6. **Synthetic rendered + augmented corpus** — Synthetic images, all 13+ scripts incl. long-tail, effectively unlimited → Cold-start for low-resource scripts, degradation robustness
- **Proprietary section:** "Direct crawl + partnership acquisition — real-world degradation and domain vocabulary no synthetic pipeline replicates."
- **3 proprietary sources (icons):**
  - Government portals: "e-Gazette, e-Courts filings, DigiLocker-linked records, land record portals (Bhulekh / Bhoomi-type), RTI response archives."
  - School / board exams: "State Board exam answer scripts, mark-sheets, admit cards — handwritten + printed, mixed quality, real degradation."
  - Verification method: "Human-in-the-loop double annotation against source scans before entering the quality-tiered training pool."

### Slide 3 — Model Planning (FULL 5-COLUMN TABLE, the authoritative version)

- **Title:** "Model Planning"
- **Tagline:** "Four-stage pipeline. Supervised fine-tuning does the foundational work throughout; RL-family techniques apply only where the scored metric diverges from the training loss."
- **TABLE (8 rows × 5 cols — #|Stage|Base model|Technique|Why):**

| # | Stage | Base model | Technique | Why |
|---|---|---|---|---|
| 0 | Preprocessing | None (OpenCV) | Deskew, denoise, binarize | Improving recognition quality without using neural network inference. |
| 1 | Layout detection | DocLayout-YOLO (YOLOv10-based) | Supervised fine-tuning on IndicDLP; LoRA/adapter | enabling it to recognize layout patterns unique to Indian documents. Iteration -1 Indic DPL — how much rows and records. If good enough, stop. If not, iteration 2 from stage 1 checkpoint and dataset process is given below. Non clean additional dataset layout detection distilled from gemini. |
| 2 | Text recognition (SFT) - Parallel | TrOCR (ViT/BEiT + RoBERTa) + Qwen 3.5 VL + Paddle OCR VL 1.6 | Supervised seq2seq fine-tuning, quality-tiered loss weighting, incorporating the akshara-boundary auxiliary loss into the continued pre-training of Qwen3-VL-8B and Paddle OCR (Mitigating the Indic Tokenization Mismatch solving Complex Spatial Overlaps, and hallucination reduction) | Translate image regions cropped by Stage 1 into digital text using a multi-model ensemble running in parallel. Indic scripts are structured as syllabic units (aksharas). Standard subword tokenizers misalign with these visual units, causing hallucinations or visual overlaps. The auxiliary loss forces the model to respect character/syllable spatial boundaries. |
| 2b | Recognition (refinement) | Same fine-tuned TrOCR + Qwen 3.5 VL + Paddle OCR VL 1.6 | Self-critical sequence training (SCST) — RL | Convert visual pixels into raw text using multi-modal visual models and Directly optimize the vision model for the metric it will be judged on (Character Error Rate). |
| 3 | Post-processing (SFT) | IndicBERT / Airavata / small LLM | SFT on (noisy text → corrected JSON) pairs | Take noisy, unstructured text from the OCR stage and map it into structured, clean JSON. We will run the extraction inference on all the dataset used in step 2, then we will tag a good vs bad extraction (based on CER) to create a preference sample. No additional dataset required, inference step 2 output and run preference tuning (SIMPO on the actual target extraction from gemini). |
| 3b | Post-processing (pref alignment) | Same SFT model | SimPO or DPO on ranked candidates | Fine-tune the SFT model to choose the best possible JSON output when multiple plausible outputs exist. Aligning the model for bhashini requirements. |
| — | Benchmark | Sarvam, IndicDLP, Indic Vision Bench | Direct inference, no fine-tuning | The benchmark we measure against — CER / WER. |

- **Kashmiri special note (embedded in Stage 2):** "for kashmiri — create a dataset with, we have layout detector, create target labels by extracting the content inside the labels from pdf."

### Slide 4 — Model Planning (CLEAN 4-COLUMN TABLE — duplicates slide 3 stripped of Why column)

- Same Stage 0–3b + Bench rows as slide 3, but the **Why column is dropped** to 4 cols (#|Stage|Base model|Technique).
- Identical to slide 3 in content; appears to be a presentation-ready version for slide export.

---

## B. WHAT PPT_SPEC.md HAS (summary of current 39-line spec)

- **Pipeline table (slides 3–4):** collapsed to 8 rows with brief "Why (as written)" column. Does NOT reproduce slide 3's full free-text "Why" cells (only paraphrases).
- **Data boxes (slide 2):** "S1 BSTD scene · S2 IIIT-HW / INDIC-HW-WORDS · S3 Sangraha/IndicCorp · S4 Bhashadaan · S5 govt/exam scans 5–10k pages/domain · S6 synthetic unlimited. Proprietary: gazette, courts, DigiLocker, land records, board exams. HITL double annotation."
- **Product claims (slide 1):** "Akshara-aware layout+recognition (conjuncts, matras, sandhi). Calibrated confidence, visual lookup, per-language morphology. Structured fields. Low-confidence spans always to human review."
- **W2 box labels:** KEEP/HYBRID/DROP verdicts already on the 7 stages.

---

## C. DIFF — WHAT PPT_SPEC.md MISSES vs PPTX

### C1. CRITICAL — slide 3 "Why" column full text (the most important gap)

| Stage | What PPT_SPEC paraphrased | What PPTX actually says |
|---|---|---|
| 1 | "Indian document layout. Iterate: if IndicDLP rows/records are good enough, stop; else distill extra layout from Gemini" | "enabling it to recognize layout patterns unique to Indian documents. Iteration -1 Indic DPL — how much rows and records. If good enough, stop. If not, iteration 2 from stage 1 checkpoint and dataset process is given below. Non clean additional dataset layout detection distilled from gemini." |
| 2 | "crops from Stage 1; option A distill extraction from Gemini; option B human extract for langs Gemini/ChatGPT miss; Kashmiri: layout boxes + PDF text under box as GT" | "Translate image regions cropped by Stage 1 into digital text using a multi-model ensemble running in parallel. Indic scripts are structured as syllabic units (aksharas). Standard subword tokenizers misalign with these visual units, causing hallucinations or visual overlaps. The auxiliary loss forces the model to respect character/syllable spatial boundaries." **Plus Kashmiri special-case methodology embedded in this cell** (not its own row). |
| 2b | "optimize the judged metric after SFT" | "Convert visual pixels into raw text using multi-modal visual models and Directly optimize the vision model for the metric it will be judged on (Character Error Rate)." |
| 3 | "structured fields" (3 words) | **38 words** of detail: "we will run the extraction inference on all the dataset used in step 2, then we will tag a good vs bad extraction (based on CER) to create a preference sample. No addition dataset required, inference step 2 output and run preference tuning ( SIMPO on the actual target extraction from gemini)" — this is the **operational loop** for the post-processor. |
| 3b | "preference on ranked JSON still valid" | "Fine-tune the SFT model to choose the best possible JSON output when multiple plausible outputs exist. aling the model for bhashini requirements" — note typo "aling" (verbatim). |

### C2. Stage 2 critical nuance — "Indic Tokenization Mismatch"

PPTX names it explicitly in Stage 2 Technique column: **"Mitigating the Indic Tokenization Mismatch solving Complex Spatial Overlaps, and hallucination reduction"** via the akshara-boundary aux loss.

PPT_SPEC.md does NOT name "tokenization mismatch" as a problem. The PPTX frames akshara-boundary as solving a specific tokenizer failure mode, not just adding aux loss. This is **important for W6 recipe evaluation** — it's a precise hypothesis, not a vague technique.

### C3. Slide 1 has 3 explicit capability titles (not paraphrased in PPT_SPEC)

PPT_SPEC only gives generic claims ("Akshara-aware, calibrated confidence, visual lookup"). PPTX has three named capabilities that map to pipeline stages:

1. **Layout Detection** → Stage 1
2. **Fine Text Recognition** → Stage 2
3. **Finetune Semantic and removing errors** → Stages 3+3b

This is the **user-facing capability stack**, not the technical one. Useful for the validation call slides.

### C4. Slide 4 is a stripped copy of slide 3

PPT_SPEC.md does NOT note that slides 3 and 4 are the same Stage table, slide 4 just dropping the "Why" column. The current spec says "Pipeline boxes (slides 3–4)" as if they're two different views — actually slide 4 is just a slide-3 export with the column dropped. **Decision-changer:** any W2/W5 diff needs to note this and not re-process slide 4 as new info.

### C5. Slide 2 has specific data source tables (6 rows × 5 cols) not in PPT_SPEC

PPT_SPEC.md gives a "S1-S6" shorthand list. PPTX has a full 6×5 table with explicit:
- **Scripts per source:** "11 Indian languages" (BSTD), "10 Indic scripts" (IIIT-HW), "22 languages" (Sangraha), "all scheduled languages" (Bhashadaan), "priority 8–10 languages first" (Govt/Inst), "all 13+ scripts incl. long-tail" (Synthetic)
- **Scale:** "~872K word images" (IIIT-HW), "billions of tokens" (Sangraha), "5K–10K pages/domain" (Govt/Inst), "effectively unlimited" (Synthetic)
- **Primary use:** explicit per source (Scene-text branch / Handwriting branch / Source text / Real-world diversity / Domain-specific fine-tuning / Cold-start low-resource)

This is critical for W3 probe planning — we need to know what scale to expect.

### C6. Slide 2 proprietary section names specific portals

PPTX names: **"Bhulekh / Bhoomi-type"** land record portals; **"RTI response archives"**. PPT_SPEC lists "gazette, courts, DigiLocker, land records, board exams" — Bhulekh/Bhoomi are the actual Indian state implementations of land record portals (Maharashtra Bhulekh, Karnataka Bhoomi). This is **operational detail** for Vinay/Krishna data sourcing, not just abstract categories.

### C7. Slide 1 "22 scheduled Indic languages" — no mention of priority

PPTX says "all 22 scheduled Indic languages" — uniform scope, no priority breakdown. But Slide 2 govt/inst says "priority 8–10 languages first." **Inconsistency to flag at call:** does "all 22" mean equal-coverage, or 8–10 priority + rest best-effort? The 100/lang probe lock (Sep 25) makes this concrete: 18 langs × 100 = 1800, not "all 22." 22 - 4 South = 18 (matches the probe). EN is the 19th but probe-not-eval.

### C8. PPTX author metadata is PptxGenJS (template/programmatic), created 2026-07-23

PPTX was generated programmatically on 2026-07-23 — **5 weeks before** the 2026-09-25 meeting that produced the standing protocol. **Slide 1 capability titles and slide 3 full-text content are pre-meeting Vinay content.** The mid-August "1.5 months old" recipe = mid-July (estimated). This means **the architecture predates the Sept 2026 SOTA wave** (PaddleOCR-VL 1.6 was late July, but ScriptMoE arXiv 2609.24058 = Sep 21, Chitrapathak-2 = 2602.16430 = Feb 2026, Devanagari stress-test = 2606.29213 = late June 2026). So the recipe is **2-3 months old** at the meeting.

### C9. PPTX Stage 2 model name confusion — "Qwen 3.5 VL" + "Qwen3-VL-8B"

Stage 2 Base model column: "TrOCR (ViT/BEiT + RoBERTa) + Qwen 3.5 VL + Paddle OCR VL 1.6"
Stage 2 Technique column: "incorporating the akshara-boundary auxiliary loss into the continued pre-training of Qwen3-VL-8B and Paddle OCR"

**There are TWO Qwen model names in the same row.** "Qwen 3.5 VL" (in base model) and "Qwen3-VL-8B" (in technique). The actual model in the field as of Sep 2026 is **Qwen2.5-VL-3B / Qwen2.5-VL-7B** (Qwen3-VL exists but is newer). **This is the biggest gap in the PPTX.** Vinay's spec mixes model names; we need to lock to one family at W5. INTEGRATED-ELITE-STACK.md already says GLM-OCR (0.9B OmniDocBench #1) is the D1 W6 primary candidate, replacing Qwen2.5-VL-3B in R7. So **the recipe in the PPTX is already being upgraded** to Qwen2.5-VL/GLM-OCR. Confirm at call.

### C10. TrOCR base column from-scratch (not fine-tune)

Stage 2 base model = "TrOCR (ViT/BEiT + RoBERTa)" — no fine-tune qualifier. The W2_HYBRID draft (in docs/architecture/) already flags TrOCR-from-scratch for DROP (Chitrapathak-2 evidence: fine-tuning beats from-scratch by 3–6× latency). **PPT_SPEC.md already has this as HYBRID / drop TrOCR-from-scratch. But the PPTX itself does NOT mark it as fine-tune.** This is an honest textual gap in the source — the original team may have meant to fine-tune but wrote "from-scratch" by accident, or vice versa. **Ask Vinay at the call.**

### C11. PPTX slide 4 is a duplicate

Slide 4 is identical content to slide 3 minus the "Why" column. PPT_SPEC currently treats slides 3 and 4 as "Pipeline boxes (slides 3–4)" — implying they're two views. **In fact slide 4 is a slide-3 export with column dropped.** No new information. Recommend merging slides 3+4 in any future deck refresh.

---

## D. WHAT'S NEW (added since PPT_SPEC was written 2026-09-25)

| Item | Source | W6-impact |
|---|---|---|
| **GLM-OCR 0.9B OmniDocBench #1** | INTEGRATED-ELITE-STACK.md | D1 W6 primary candidate, replaces Qwen2.5-VL-3B |
| **mlx-tune 1.4k★** | INTEGRATED-ELITE-STACK.md | D1 QLoRA tool, MLX-native |
| **liteparse 12.7k★** | INTEGRATED-ELITE-STACK.md | PDF front-end harness |
| **dots.mocr 3B MIT** | INTEGRATED-ELITE-STACK.md | Head-to-head vs GLM-OCR for OldScan 55.3 |
| **MonkeyOCRv2 0.7B Apache-2.0** | INTEGRATED-ELITE-STACK.md | Smallest strong fine-tune backbone |
| **HunyuanOCR-1.5** | INTEGRATED-ELITE-STACK.md | Weak-cell attack (sat/ks class adjacents) — license review first |
| **Unlimited-OCR 26.4k★** | INTEGRATED-ELITE-STACK.md | OldScan 55.3 cross-page context |
| **Sarvam Vision 2.1** | sarvam.ai 87.39 Indic bench | Already in PPT_SPEC §6/§10, confirmed by Sarvam blog 2026-09-24/25 |
| **ScriptMoE arXiv:2609.24058** | Sep 21 2026 paper | PP-OCRv5 F1 65.71 → 80.89 — script-aware MoE |
| **Chitrapathak-2 arXiv:2602.16430** | Krutrim Feb 2026 | Fine-tune Nanonets-OCR2-3B / Qwen2.5-VL beats LLaVA-from-scratch |
| **Devanagari VLM stress-test arXiv:2606.29213** | June 2026 | English OCR quality does NOT predict Indic OCR; real scans collapse models |
| **Level 7 48h research campaign** | docs/research/LEVEL7_RESEARCH_CAMPAIGN.md | 1,000+ papers / 5,000+ artifacts; ended ~04:23 Sep 29 |
| **Probe22 results (1,227 items × 11 engines)** | level2/probe22/scores/ | §6.4 GT verdicts LOCKED; sat/ks/mni/ur/mr + ne-PDF-tier BARRED from W6 |
| **Sarvam 2.1 on probe22** | level2/probe22/scores/ | Sarvam_ks 0.63, Sarvam_ur 0.53 on 3/lang subset (falsification-relevant) |
| **Tesseract-bilingual ≡ tesseract-indic ≡ openbharatocr** | level2/ULTIMATE_HYBRID_CONCERN.md | Family-confirm: effective engine count on probe = < nominal |

---

## E. WHAT PPTX VALIDATES (PPTX content confirms PPT_SPEC §6 evidence)

- **Sarvam as benchmark target:** Slide 3 Bench row names "Sarvam, IndicDLP, Indic Vision Bench" — directly aligned with PPT_SPEC §6 challenger list.
- **HITL double annotation:** Slide 2 explicitly says "Human-in-the-loop double annotation against source scans before entering the quality-tiered training pool." — matches SOUTH_CANON §F F1+T1/T0 model.
- **Akshara-boundary aux loss:** Slide 3 Stage 2 explicitly names it; PPT_SPEC §6 already had ScriptMoE + akshara-aux as KEEP-with-scope-abugidas.
- **Indic tokenization mismatch hypothesis:** Slide 3 Stage 2 names the exact failure mode (subword tokenizer misalignment with akshara visual units). This is a load-bearing claim for W6.
- **No fine-tune on test:** Slide 3 Bench row says "Direct inference, no fine-tuning." PPT_SPEC §6 table reinforces this.

---

## F. WHAT PPTX CONTRADICTS (vs current law)

| PPTX claim | Current law (W2_HYBRID, INTEGRATED-ELITE-STACK) | Action |
|---|---|---|
| TrOCR from-scratch (Slide 3 Stage 2) | DROP per Chitrapathak-2 (fine-tune > from-scratch) | Confirm with Vinay — likely typo |
| "Qwen 3.5 VL" + "Qwen3-VL-8B" both named | GLM-OCR is D1 primary candidate | Lock to one family at W5 freeze |
| Layout detector = DocLayout-YOLO IndicDLP SFT | HYBRID per W2 (use 2026 default detector, don't train YOLO from scratch) | Already covered by PPT_SPEC §6 row 1 |
| Stage 3 preference sample = SIMPO from Gemini outputs | SimPO/DPO KEEP but data sourcing needs review (Gemini outputs as training signal = contaminates eval if Gemini is a benchmark) | Flag at call |

---

## G. ACTION ITEMS (for orchestrator to surface at call)

1. **Lock the Qwen model name.** "Qwen 3.5 VL" + "Qwen3-VL-8B" both appear; pick one. Likely Qwen2.5-VL-3B/7B family given current SOTA; or GLM-OCR per INTEGRATED-ELITE-STACK.
2. **Lock TrOCR role.** Fine-tune existing TrOCR vs from-scratch — PPTX wording ambiguous, Chitrapathak-2 says fine-tune wins.
3. **Reconcile "all 22" vs "priority 8–10".** Slide 1 says all 22 uniformly; slide 2 govt/inst says priority 8–10. The probe lock = 18 langs × 100 = matches 22-4 South. EN = 19th.
4. **Flag the akshara-boundary aux loss as our testable W6 intervention.** Slide 3 Stage 2 names "Indic Tokenization Mismatch" — load-bearing hypothesis.
5. **Note slide 4 = slide 3 stripped.** No new content; future decks should not have slide-4-style duplicates.
6. **Note proprietary sources by name** (Bhulekh/Bhoomi, RTI archives) for Krishna's North-track data sourcing.
7. **Gemini in the training loop.** Stage 2 says "distill extraction from Gemini" and Stage 3 says "SIMPO on the actual target extraction from gemini." This means **Gemini outputs become training signal.** If Gemini is also a benchmark target, this contaminates eval. Verify Gemini is NOT a benchmark target (PPT bench = "Sarvam, IndicDLP, Indic Vision Bench" — no Gemini; OK).

---

**End of PPT_VS_SPEC_DIFF.md. Total diff: 11 missing items + 4 contradictions + 7 action items.**