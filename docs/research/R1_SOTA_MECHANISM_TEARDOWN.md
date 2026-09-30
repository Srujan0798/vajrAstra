# R1 — SOTA Mechanism Teardown: Sarvam Vision 2.1 vs PaddleOCR-VL 1.6

Status: research only. No training. No backbone invention. Sources are primary only (official blogs, model cards, papers, benchmark submissions). Every claim carries URL + number/quote. Where Sarvam/Paddle publish nothing, this file says NOT DISCLOSED instead of inferring.
Date: 2026-09-26. Requestor weak cells: Santali ~53.91, Kashmiri ~54.82, OldScan ~55.3, Odia ~80.01.

---

## TARGET 1 — Sarvam Vision 2.1

### 1.1 Base VLM arch + size

- **3B-parameter state-space VLM**, built on the "base Sarvam sovereign 3B model."
  Quote (v1 blog): "we performed a round of continual pretraining on the base Sarvam sovereign 3B model; followed by supervised fine-tuning and reinforcement learning using verifiable rewards."
  URL: https://www.sarvam.ai/blogs/sarvam-vision
- Model card confirms: "Sarvam Vision is a 3B parameter state-space Vision Language Model (VLM) purpose-built for high-accuracy Document Intelligence," 23 languages (22 Indic + English), Digitise/Extract APIs, 10 pages / 200 MB per-file input limits.
  URL: https://docs.sarvam.ai/api/getting-started/models/sarvam-vision.md
- **Harness-with-VLM, not a bare page-guesser.** 2.1 blog: "our architecture follows the harness-with-VLM paradigm. The semantic layout parser and a pointer reading order network make for the primary harnesses."
  URL: https://www.sarvam.ai/blogs/sarvam-vision-2-1
- v1 already had the same two harness modules: "(a) semantic layout parser and (b) reading order network."
  URL: https://www.sarvam.ai/blogs/sarvam-vision
- No public weight release; API-only (Digitise/Extract). No tokenizer, encoder (ViT variant), or context-length disclosure found in either blog or the model card. **NOT DISCLOSED.**

### 1.2 SFT data mixture (human vs synthetic ratio)

What is published (2.1 blog, "Data and Model Architecture"):

- "we carefully crafted high-quality and large-scale datasets for KV extraction and Indic handwritten. These comprised data of both types — synthetic and real-world."
- "we built handwritten and printed synthetic forms in large quantities in various languages."
- "we further obtained forms from the web and filled them in synthetically to achieve high variance."
- "for Indic handwritten, we leveraged videos and other sources which contain a rich variety of handwritten content."
- "These novel sources of data, along with refinements to our existing training corpus, allowed for training new capabilities and overcoming weaknesses."
  URL: https://www.sarvam.ai/blogs/sarvam-vision-2-1
- v1 data domains: "scientific literature, financial documents, government bulletins, historical manuscripts, textbooks, magazines, newspapers, among others. Each domain underwent data generation tailored to the specific use case," with "high-quality synthetic and real-world document image-text samples for all Indian languages, alongside English."
  URL: https://www.sarvam.ai/blogs/sarvam-vision

What is NOT published:

- **No human-vs-synthetic ratio.** No percentages, no sample counts per source, no per-language data volume. **NOT DISCLOSED.**
- **No curriculum order** (word → line → block → page, or any other staging). The only stated order is "supervised fine-tuning followed by RLVR" (large-scale post-training). **NOT DISCLOSED beyond SFT→RLVR.**
- New capabilities in 2.1 vs 1.0 are named (structured/KV extraction, complex tables incl. cross-page tables and fixed-field forms, Indic handwriting) with consistency/hallucination fixes, but per-capability data ablations are absent. **NOT DISCLOSED.**

### 1.3 RLVR reward design

- Published: "we performed large-scale post-training: supervised fine-tuning followed by RLVR."
  URL: https://www.sarvam.ai/blogs/sarvam-vision-2-1
- v1 predecessor: "reinforcement learning using verifiable rewards."
  URL: https://www.sarvam.ai/blogs/sarvam-vision
- Granularity (char / token / word-level rewards): **NOT DISCLOSED.** No reward equation, no metric named as the reward (CER/WER/TEDS/1−NED not stated for Sarvam's own RL).
- Length penalties: **NOT DISCLOSED.**
- Anti-reward-hacking (validity gates, repetition penalties, truncation handling): **NOT DISCLOSED.** The 2.1 blog claims consistency/hallucination improvements as an outcome, with no mechanism given.
- Rollout counts, temperature, KL coefficient, baseline/advantage estimator: **NOT DISCLOSED.**

### 1.4 Curriculum order

- Only ordering attested: continual-pretrain (v1) → SFT → RL/RLVR. No intra-SFT staging published. **NOT DISCLOSED.**

### 1.5 Published ablations explaining the Santali/Kashmiri ~30pt lag

- **No such ablation exists in either blog.** There is no per-language error analysis, no data-volume-vs-accuracy curve, no script-family ablation, no tokenizer-fertility analysis. **NOT DISCLOSED — the lag is measured but unexplained by the vendor.**
- What IS published is the measurement itself, on the vendor's own Indic OCR Bench (6,909 samples = 6,609 Indic + 300 English; semantic-block level; pages spanning 1800–present; word accuracy = 100×(1−WER)):
  URL bench card: https://huggingface.co/datasets/sarvamai/indic-ocr-bench
  URL scores: https://www.sarvam.ai/blogs/sarvam-vision-2-1
- 2.1 language table (word accuracy, selected cells):
  | cell | Sarvam 2.1 | Bodhan | Gemini 3.6 Flash | GCV |
  |---|---|---|---|---|
  | Overall | **87.39** | 84.94 | 79.35 | 71.76 |
  | Kashmiri | **54.82** | 48.04 | 36.04 | 24.22 |
  | Odia | **80.01** | 75.45 | 81.01 | 68.32 |
  | Konkani (ceiling ref) | 97.41 | 95.99 | 93.93 | 93.72 |
  | Marathi (ceiling ref) | 95.06 | 90.76 | 93.14 | 86.50 |
  All four rows quoted verbatim from the 2.1 blog table. Santali 53.91 (Sarvam) / 68.30 (Bodhan wins) is the requestor-stated cell from the same bench family and is consistent with the blog's long-tail pattern (Kashmiri-class collapse); the fetched blog excerpt truncates the Santali row, so Santali is carried as **requestor-provided, vendor-table-unverified-in-this-pass** — re-verify against the HF `test` split before citing in W5.
- OldScan (English olmOCR-Bench, same 2.1 blog): Sarvam 2.1 **55.3** vs Opus 5 54.0 vs Chandra-OCR2 49.2 vs Mistral OCR4 48.9; overall olmOCR 87.3. OldScan is the global worst column for every model in the table — i.e. the 55.3 is a field-wide failure, not a Sarvam-only bug.
- OmniDocBench v1.6 (same blog): Sarvam 2.1 overall **94.97** (text edit-dist 0.0289 — best in table; formula CDM 0.988; table TEDS 0.890 / TEDS-struct 0.935; reading order 0.099) vs PaddleOCR-VL 1.6 at 96.01 in that table (see §3 conflict note).
- Structural read of the lag (analyst inference, NOT vendor ablation): Kashmiri Perso-Arabic/Nastaliq + Santali Ol Chiki are tokenizer-rare, training-sparse scripts; the harness (layout + reading order) cannot recover glyphs the VLM never learned. Supporting signal: Bodhan beats Sarvam on Santali 68.30 vs 53.91 — a specialist/data-composition effect, not a harness effect. But without Sarvam's per-language data counts this remains a hypothesis to test on OUR probe (W3), not a cited mechanism.

### 1.6 Mechanism summary (Sarvam, citable)

1. 3B state-space VLM + semantic layout parser + pointer reading-order network (harness-with-VLM).
2. Synthetic+real SFT (KV/forms/handwriting emphasis; web forms filled synthetically; handwriting from videos) → RLVR.
3. Block-level Indic bench (6,909) as the eval unit — matches our probe's block packs better than page-level CER.

---

## TARGET 2 — PaddleOCR-VL 1.6

Primary source: Zhang et al., arXiv:2606.03264 (2026-06-02). URLs: https://arxiv.org/html/2606.03264 / https://arxiv.org/html/2606.03264v1 / paper page https://arxiv.org/abs/2606.03264v1. Architecture companion: PaddleOCR-VL-1.5 report arXiv:2601.21957. Model card: https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6. Official docs: https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html and Context7 `/paddlepaddle/paddleocr` pipeline docs (doc_parser CLI, `pipeline_version v1/v1.5/v1.6`, layout+recognition two-stage workflow).

### 2a. Weak-region mining algorithm (paper §3)

Design principle (§3.1): "From Uniform Scaling to Under-Optimized Region Optimization" — "explicitly mine and refine the current model's weak regions" from PaddleOCR-VL-1.5 instead of indiscriminate corpus expansion. Three mined region types:

1. **Boundary-Fragile Regions (§3.2).** "for different combinations of model architectures and training data distributions, it can identify regions where the current model has not yet learned robust invariance," evaluated "from two complementary views" (perturbation/boundary-stability probes around 1.5's decision boundaries).
2. **Coverage-Sparse Regions (§3.3 + Algorithm 1).** Encode samples with a "document-specific feature encoder f(·)", "measures sample similarity in the resulting feature space and discovers small, weakly connected outlier clusters as candidate Coverage-Sparse Regions." Algorithm 1 ("Coverage-Sparse Region Mining", inputs D, f(·), K_target, τ0, Δτ): "gradually increases the similarity threshold to reveal fine-grained clusters. Instead of forcing all samples into a fixed partition at once, it progressively splits the similarity graph and identifies small outlier components that has low local density." Goal stated as exposing "weakly supported tail neighborhoods that are easily hidden by dominant distributions" — i.e. the long tail by construction.
3. **Unreliable-Supervision Regions (§3.4).** Relabel/correct supervision for 1.5-training samples flagged as noisy; corrected samples re-enter the SFT corpus (see §2b). This is the anti-label-noise arm, distinct from the two distributional arms above.

### 2b. Progressive post-training stages — what trained when, what data (paper §4)

"progressive post-training pipeline covering CPT, SFT, and RL" (§6), with PP-DocLayoutV3 **frozen/unchanged** — all 1.6 gains are in the 0.9B VLM and its data:

| stage | corpus | size | purpose (paper) |
|---|---|---|---|
| CPT — Continued Pre-Training (§4.1) | full 1.5 SFT data + part of 1.5 pre-training data + ALL newly retrieved data-engine output | **16.8M samples** | "absorbs broad curated data to expand distributional coverage and incorporate corrected supervision" |
| SFT (§4.2) | (i) UACS-mined hard samples from the CPT corpus (UACS = Uncertainty-Aware Cluster Sampling from 1.5); (ii) + corrected-label samples from Unreliable-Supervision mining | **7.3M samples** | "focuses on high-quality hard samples to refine document parsing behavior" |
| RL / GRPO (§4.3) | per-task top-ranked high-potential samples (OCR, chart, table, formula, seal, text spotting separately) | **top 8K per task** | "further optimizes high-potential samples with verifiable rewards" |

RL sampling protocol (§4.3.1): SFT model as rollout policy; **16 rollouts per sample, temperature 0.85, top-p 0.9, top-k 32**; filter over-hard (r_max below threshold — policy never succeeds), over-easy (r_mean above threshold — no headroom), low-potential (r_max − r_mean small), and reward-flat (variance ≈ 0 kills GRPO advantages). Mining score: leading term r_max − r_mean with exponential upweighting of generation-uncertainty × reward-variance, **α=1, β=2**. Selection done **per task** to preserve balance.

Ablations (§5.3, overall score points): **CPT +0.69** (Table-TEDS 91.67% → 93.03%) — "broad distributional expansion and corrected supervision … provide a strong foundation"; **SFT +0.63** (Table-TEDS → 94.74%, TEDS-S → 97.19%) — "high-quality hard samples are particularly effective"; RL gains smaller/high-potential polish (paper frames RL as stabilizing reward-driven learning for the compact 0.9B policy, which is "more sensitive to noisy, over-easy, over-hard, or reward-flat RL samples").

### 2c. Detection/recognition split vs end-to-end (architecture)

- Inherited 0.9B VLM: "Native Resolution Visual Encoder, an Adaptive MLP Connector, and the lightweight ERNIE-4.5-0.3B Language Model" (§2; 1.5 paper names the encoder NaViT-style dynamic-resolution). Full system = **PP-DocLayoutV3 (layout analysis) + PaddleOCR-VL-1.6-0.9B (vision-language understanding)**; 1.6 keeps "PP-DocLayoutV3 unchanged."
- **Document Parsing = two-stage, split.** Per official docs (Context7 `/paddlepaddle/paddleocr`, PaddleOCR-VL pipeline page): "the first stage is layout analysis: the model takes the entire image as input, detects and localizes various layout elements …, determines their reading order, and crops … The second stage is VLM-based recognition: each sub-image is independently fed into the VLM … after which all element-level outputs are merged according to the reading order." CLI: `paddleocr doc_parser` with `use_layout_detection` default True and `pipeline_version v1/v1.5/v1.6`. Docs warn: "to fully leverage the capabilities of PaddleOCR-VL, it is necessary to adopt the complete pipeline … rather than using the VLM component alone."
- **Text Spotting = end-to-end exception.** "For text spotting, PaddleOCR-VL-1.6 directly uses PaddleOCR-VL-1.6-0.9B for end-to-end text detection and recognition" (paper §2; identical in 1.5 report §2.1).
- Post-processing: "lightweight post-processing engine then organizes these outputs into structured formats such as Markdown and JSON, with additional support for cross-page table merging and heading hierarchy refinement" (paper §2).
- 1.5→1.6 also moved layout toward instance segmentation + integrated reading-order prediction (1.5 report §2.1: "transitioning from standard rectangular detection to a robust instance segmentation framework, while simultaneously integrating reading order prediction").

### 2d. Nastaliq + low-resource script handling

- Multilingual coverage: PaddleOCR-VL supports **109 languages** (HF card https://huggingface.co/PaddlePaddle/PaddleOCR-VL); official docs list an Arabic-script cluster: "Arabic: Arabic, Persian, Uyghur, **Urdu**, Pashto, Kurdish, **Sindhi**, Balochi," plus "Tamil, Telugu" among supported scripts.
  URL: https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html
- **Nastaliq-specific handling: NOT DISCLOSED.** No Nastaliq vs Naskh distinction, no Perso-Arabic shaping/joining treatment, no Urdu/Sindhi/Kashmiri accuracy table in the 1.6 paper — OmniDocBench v1.6 is English-centric (text/table/formula/reading-order), and the paper's weak regions are document-element regions (tables, formulas, seals, spotting), not script regions.
- **Ol Chiki (Santali) / Meitei Mayek: NOT DISCLOSED.** No Indic-script ablation of any kind in the 1.6 paper. Transferability to our Santali/Kashmiri cells is therefore by-analogy (coverage-sparse mining + 109-lang encoder), not by-measurement.

### Score conflict (reported both, per method)

- Paper abstract (§1/§5): PaddleOCR-VL-1.6 achieves **96.33%** on OmniDocBench v1.6 ("a new state-of-the-art score of 96.33%").
  URL: https://arxiv.org/abs/2606.03264v1
- Sarvam 2.1 blog's OmniDocBench v1.6 table: PaddleOCR-VL 1.6 overall **96.01** (text edit-dist 0.0356, formula CDM 0.985, table TEDS 0.931, TEDS-struct 0.961, reading order 0.100) vs Sarvam 2.1 94.97.
  URL: https://www.sarvam.ai/blogs/sarvam-vision-2-1
- Read: 96.33 = vendor-paper number on v1.6; 96.01 = independently-tabulated number in Sarvam's table (possibly different split/scoring cut, e.g. English-subset vs full — neither side pins the split precisely enough to reconcile; Bodhan's card quotes yet another cut: "OmniDocBench 1.6 (english subset)" with PaddleOCR-VL-1.6 at 96.36. URL: https://huggingface.co/bodhan-ai/indic-ocr). **Three numbers, three cuts — quote the cut with the number.**
- Real5-OmniDocBench (robustness: scanning, warping, skew, screen photo, illumination): 1.6 claims SOTA across all five scenarios (paper §5; docs). No per-scenario numbers extracted in this pass — follow-up if OldScan transfer is contested.

### Reward design detail (paper §4.3.2, for PPT-2b reuse)

Representation-aware verifiable reward, per task t: **R_t(y,y*) = Valid_t(y) · Struct_t(φ_t(y)) · Sim_t(φ_t(y), φ_t(y*))**, where φ_t is a task canonicalizer. Valid = binary gate (degeneration, truncation, malformed LaTeX/format → 0 — the anti-hacking arm). Struct = soft penalty (e.g. OTSL rectangularity edit cost; LaTeX validity). Sim = task metric: **TEDS (tables), 1−NED (seal), edit-similarity-weighted F1 (spotting: geometrically matched box pairs weighted by 1−NED — jointly rewards localization + recognition)**. Rationale stated: "overly sparse binary rewards provide limited learning signals" for the compact 0.9B policy.

---

## Comparison table

| mechanism | Sarvam Vision 2.1 | PaddleOCR-VL 1.6 | transferable at zero/low GPU | maps to our weak cell |
|---|---|---|---|---|
| System shape | Harness-with-VLM: 3B state-space VLM + semantic layout parser + pointer reading-order net (blogs) | Two-stage: frozen PP-DocLayoutV3 detect+order → crop → 0.9B VLM recognize; spotting end-to-end (paper §2 + docs) | **Zero-GPU (inference harness).** Wrap Bodhan/Paddle detector + any VLM; pointer-order merge is CPU post-processing. Same pattern as PPT Stage 1 | table, reading_order, mixed_script |
| Data engine | Synthetic+real, KV/forms/handwriting focus; web forms filled synthetically; handwriting from videos. No ratio published | **Under-optimized-region mining**: boundary-fragile probes + coverage-sparse graph clustering (Alg. 1) + supervision correction (§3) | **Low-GPU.** Mining is encoder-forward + graph clustering on OUR probe (no training). Re-ranks what to label/SFT next | Santali, Kashmiri, Odia, old_scan, handwriting (tail neighborhoods by construction) |
| Post-training order | SFT → RLVR (large-scale; no sizes published) | CPT 16.8M → SFT 7.3M (UACS hard + corrected) → GRPO top-8K/task (16 rollouts, T 0.85; α=1 β=2) with ablations CPT +0.69 / SFT +0.63 (§4–§5.3) | **Low-GPU at RL scale.** Full CPT/SFT is not low-GPU; the *recipe shape* (hard-sample SFT, then GRPO on 8K/task high-potential) is. GRPO on ≤50K gold samples fits <100 GPU-h on a 0.8–1B policy | hallucination, repetition, table (reward-shaped), PPT 2b |
| Reward | "Verifiable rewards" / RLVR — no equation published | R = Valid·Struct·Sim; TEDS / 1−NED / edit-weighted F1; binary degeneration/truncation gate (§4.3.2) | **Zero-GPU to adopt as metric.** Use Valid-gated edit-weighted F1 + TEDS as our scorer/RL reward on gold GT (cf. protocol §6.5–§6.6) | hallucination, repetition, table, charset |
| Long-tail script story | Measured collapse (Kashmiri 54.82; Santali 53.91-class), unexplained; Bodhan wins Santali 68.30 | 109-lang encoder incl. Urdu/Sindhi cluster; zero Indic-script ablations published | **Router, not retrain.** Bodhan-vs-Sarvam Santali split (+14pt) is the evidence for a script specialist/router over more shared training | Santali, Kashmiri, Manipuri-Meitei, Urdu/Sindhi Nastaliq (PPT script-router arm) |
| Worst-category honesty | OldScan 55.3 worst column on olmOCR for ALL models (field-wide) | Real5 robustness SOTA claim (5 distortion scenarios); OldScan-class still weakest | **Zero-GPU.** Keep Stage-0 OpenCV geometry (deskew/contrast) as KEEP; deep denoisers unproven on our 200-dpi scans | old_scan |

Bodhan reference (third-party anchor, HF card https://huggingface.co/bodhan-ai/indic-ocr): two-stage **33M PP-DocLayoutV3/RT-DETR (37-class, education taxonomy) + 0.8B Qwen3.5 block OCR with Sarvam-30B tokenizer**, fp32/bf16; OmniDocBench-1.6-English-subset 92.17 per Sarvam's table. Relevant because its Santali win + Indic tokenizer + open weights make it the stealable specialist, not just a score.

---

## The 3 stealable mechanisms (<100 GPU-hours each)

1. **Weak-region mining loop on our own probe (Paddle §3, zero training).**
   Run boundary-fragility probes (perturb/crop/threshold sweeps) + coverage-sparse clustering (document encoder + similarity-graph outlier components, Alg. 1 pattern) + supervision-correction triage over the 1,227-item W3 manifest. Output is a ranked re-label / re-sample queue, not a model. Cost: encoder inference + CPU clustering (<10 GPU-h). Maps to: Santali, Kashmiri, Odia, old_scan, handwriting — the tail neighborhoods the miner is built to expose.
2. **GRPO high-potential mining + Valid·Struct·Sim rewards on gold-only (Paddle §4.3, Sarvam RLVR-shaped, PPT 2b).**
   16 rollouts (T 0.85 / top-p 0.9 / top-k 32) per candidate; keep only r_max−r_mean high, variance non-flat, per-task top-8K; reward = binary validity gate (degeneration/truncation/malformed → 0) × structural factor × TEDS / 1−NED / edit-weighted F1. Train ONLY on human-verified gold (protocol §9 guard already reconciled). A ≤1B policy on ≤50K samples fits <100 GPU-h. Maps to: hallucination, repetition, table, charset + PPT box 2b (rename SCST→RLVR per W1).
3. **Frozen-detector two-stage harness + pointer reading order (both systems agree; Sarvam harness + Paddle §2/docs).**
   Keep PP-DocLayoutV3/Bodhan-IndicDocLayout/DocLayout-YOLO frozen; detect + order + crop; VLM recognizes crops; merge by reading order; end-to-end VLM only for text-spotting-style dense regions. Post-process to Markdown/JSON with cross-page table merge. Cost: zero training GPU; CPU merge. Maps to: table, reading_order, mixed_script + PPT Stage 1 (HYBRID label stands — swap the detector, keep the stage).

## Honest non-steals (do not propose at freeze)

- Sarvam's 3B state-space VLM weights (API-only, no open path) and its undisclosed SFT mixture/RLVR reward — cannot replicate, only wrap via API baseline (engine #11 already wired).
- Paddle's full CPT-16.8M/SFT-7.3M (hundreds of GPU-days at 0.9B) — steal the recipe shape and the 8K/task GRPO tail, not the corpus.
- Any claim that either vendor "solved" Santali/Kashmiri/Nastaliq/Ol Chiki — neither published a mechanism for those scripts. Our router/specialist decision waits for the W3 probe numbers (protocol §6.2 tier scoring + §6.4 verification), not for vendor prose.
