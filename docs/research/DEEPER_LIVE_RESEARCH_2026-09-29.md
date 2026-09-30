# Deeper Live Research — 2026-09-29 (post-Phase 9)

**Date:** 2026-09-29
**Agent:** AGENT-8 (parallel deep-cleanup lane)
**Author:** MiniMax-M3 via opencode
**Standing context:** Level 7 48h research campaign ended ~04:23 IST 2026-09-29. This is the **second-pass deep research** after AGENT-1's LIVE_LATEST_2026-09-29.md was sealed. Goal: confirm, expand, and discover what was missed. All records carry evidence-law status per campaign §9.

**Note on LIVE_LATEST contradiction (campaign.md §10 honesty-law):** LIVE_LATEST claimed *"No public Ol Chiki–native OCR exists (tesseract sat.traineddata 404 DEAD upstream)"*. **CONTRADICTED by primary source this pass.** indic-ocr/tessdata (Apache-2.0, 51⭐, 10 forks, github.com/indic-ocr/tessdata, created 2016-10-06) provides community-trained Tesseract models for **10 Indic scripts including Santali (sat) and Meetei Meyek (mni)**. The sat.traineddata "DEAD upstream" claim was about the **official tesseract-ocr/tesseract repo**, not the community repo. This is a load-bearing correction: SAT and MNI weak cells have a free Tesseract backstop available if the user approves downloading it.

---

## A. SOURCES FETCHED (with timestamps)

### A1. Primary user URLs (all 7 fetched live, 2026-09-29 ~21:00 IST)
- `https://lnkd.in/p/eFzz2Dtb` — Sarvam Vision 2.1 LinkedIn post (already in LIVE_LATEST; cross-checked)
- `https://lnkd.in/p/ewsNXkTs` — Gnani Evon v3.3 NeurIPS acceptance post (already in LIVE_LATEST)
- `https://www.gnani.ai/` — Gnani website (already in LIVE_LATEST; not OCR)
- `https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B` — **RE-FETCHED** (new detail this pass)
- `https://huggingface.co/datasets/sarvamai/indic-ocr-bench` — **RE-FETCHED** (full metrics.py normalization confirmed)
- `https://www.sarvam.ai/blogs/sarvam-vision-2-1` — **RE-FETCHED** (full OmniDocBench + Indic per-lang tables)
- `https://consensus.app/` — already in LIVE_LATEST

### A2. Parallel-search MCP web_search (12 batches executed)
Queries executed: `Indic OCR vision language model fine-tuning 2026 SOTA`, `document AI layout reading order 2026 benchmark`, `Ol Chiki Santali OCR model open source`, `Kashmiri Nastaliq OCR dataset fine-tuning`, `Qwen3-VL fine-tuning Indic OCR QLoRA`, `GRPO RLVR OCR document understanding`, `PaddleOCR-VL 1.6 OmniDocBench v1.6`, `Sarvam Vision 2.1 architecture training recipe`, `dots.ocr 1.7B layout reading order`, `Laya paper 32.8ms multilingual classifier`, `MonkeyOCRv2 layout reading order 2026`, `DocRes restoration document image 2026`, `Laya Jev AI comparison`, `Bhashini Indic OCR 2026`, `Chitrapathak Parichay OCR Paruchuri 2026`, `Surya OCR 2 Datalab release 2026`, `mlx-vlm PaddleOCR-VL Apple Silicon`, `ICDAR 2026 accepted papers Indic`, `BrahmicTokenizer-131K`, `Chandra OCR 2 multilingual`, `OCR papers NeurIPS 2026`, `dots.ocr license`, `Sarvam Vision 3B SSM state space`, `Late September 2026 new OCR model`.

### A3. parallel-search_web_fetch (10 fetches executed)
- `huggingface.co/gnani/gnani-evon-v3.3-30B-A3B` (full model card)
- `huggingface.co/datasets/sarvamai/indic-ocr-bench` (metrics.py confirmed)
- `huggingface.co/convaiinnovations/laya` (full model card with benchmark table)
- `orcarouter.ai/blog/jev-vs-laya` (detailed Laya vs Jev analysis, Sep 23 2026)
- `daily.dev/posts/laya-bye-bye-typescript-jev-ai-y5lhaizau` (Laya announcement analysis)
- `arxiv.org/html/2606.23344v1` (RT-DocLayout, PaddlePaddle)
- `arxiv.org/abs/2512.02498` (dots.ocr paper)
- `github.com/rednote-hilab/dots.ocr` (license = MIT verified)
- `arxiv.org/abs/2605.29379` (BrahmicTokenizer-131K, Apache-2.0 verified)
- `www.sarvam.ai/blogs/sarvam-vision` (Sarvam Vision 1.0 architecture blog, 2026-02-05)
- `indic-ocr.github.io/tessdata` (community tesseract sat/mni traineddata — **NEW LOAD-BEARING FINDING**)
- `www.datalab.to/blog/introducing-chandra` (Chandra OCR 2 details)

### A4. Context7 MCP library docs (5 queries executed)
- `/websites/arahim3_github_io_mlx-tune` — mlx-tune FastVisionModel + VLMSFTTrainer API
- `/huggingface/peft` — QLoRA, LoFTQ, multi-adapter examples
- `/huggingface/trl` — GRPO VLM training with `accelerate launch grpo_visual_math.py`

---

## B. NEW FINDINGS (not in earlier LIVE_LATEST_2026-09-29.md)

### B1. Sarvam Vision 2.1 detailed benchmark — full tables re-extracted
**Source:** `https://www.sarvam.ai/blogs/sarvam-vision-2-1` (re-fetched 2026-09-29)
- **Architecture:** "**harness-with-VLM paradigm**" — 3B state-space VLM + (a) semantic layout parser + (b) pointer reading-order network. **Post-training: SFT followed by RLVR.**
- **OmniDocBench v1.6 (component-level):**
  - Sarvam 2.1: text-edit **0.0289 (BEST)**, formula CDM **0.988 (BEST)**, table TEDS 0.890, reading-order **0.099 (BEST)**, overall 94.97
  - PaddleOCR-VL 1.6: text-edit 0.0356, formula CDM 0.985, table TEDS **0.931 (BEST)**, reading-order 0.100, overall 96.01
  - **Implication:** Sarvam wins text+formula+reading-order; PaddleOCR wins tables. They are **complementary**, not substitutes.
- **Indic OCR Bench overall:** Sarvam 87.39 / Bodhan 84.94 / Gemini 3.6 79.35 / Google Cloud Vision 71.76 / **Surya OCR 2 = 69.96 (new datapoint!)** / Mistral OCR4 69.16 / Opus 5 68.81 / Gemma 4 65.53 / Chandra-OCR2 64.56 / GPT 6 Astra 63.69 / Infinity-Parser2 Pro 49.83 / Azure Vision 4.0 41.29 / **AWS Textract 4.64 (near zero)**
- **New language cells visible:** Dogri (Sarvam 89.46, Bodhan 85.51, Gemini 80.03, Surya 65.87); Bodo (Sarvam 90.48, Bodhan 90.69, Gemini 86.37, Surya 69.96). These were missing from the partial table in LIVE_LATEST.
- **Decision-changer:** Surya OCR 2 scores 69.96 (not 71.76 GCV) — must update LIVE_LATEST §E to add Surya row. AWS Textract 4.64 = practically non-functional for Indic.

### B2. PaddleOCR-VL 1.6 (re-verified) — new build 0.9B, post-training = SFT + GRPO
**Source:** `arxiv.org/abs/2606.03264` (PaddlePaddle, submitted 2026-06-02); `paddleocr.ai/main/en/index.html`; `huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6`
- **OmniDocBench v1.6: 96.33% (note: 96.33, not 96.01)** — confirms SOTA on v1.6.
- **Architecture:** "**CPT-SFT-RL** progressive post-training" — continued pretraining → SFT (on high-difficulty curated samples) → **GRPO reinforcement learning**. Three-stage pipeline with region-aware data optimization targeting "under-optimized regions" (boundary-fragile, low-confidence, unreliable-label).
- **Apple Silicon M4 verified** (paddleocr.ai Apple Silicon tutorial). MLX-VLM supported (`gamhtoi/PaddleOCR-VL-MLX` is community Apple Silicon native port). Real5-OmniDocBench SOTA across all 5 scenarios (scanning, warping, screen-photography, illumination, skew).
- **License:** inferred Apache-2.0 (per INTEGRATED-ELITE-STACK.md).
- **Decision-changer (UPDATED):** PaddleOCR-VL 1.6 has GRPO stage, validating our `D1 wrap-pipeline includes SFT+GRPO on GPU`. **On Apple Silicon (M4 verified), this is now a viable local path** — relevant if W6 freeze allows Apple Silicon as dev environment. **gamhtoi/PaddleOCR-VL-MLX exists.**

### B3. dots.ocr — license clarification (MIT, not Apache 2.0)
**Source:** `github.com/rednote-hilab/dots.ocr` (1.8k⭐, 168 forks); `arxiv.org/abs/2512.02498`
- **License: MIT** (verified from GitHub repo LICENSE file). LIVE_LATEST §E listed "MIT" correctly. The Apache 2.0 confusion came from the mirror `d6108366.hf-mirror.com/hipfire-models/dots.ocr` (third-party mirror).
- **1.7B parameters**, based on Qwen2.5-1.5B + custom vision encoder, released 2025-07-30, paper v4 2025-12-17. SOTA on OmniDocBench v1.5.
- **Elo scores on the README (multimodal OCR comparison):** dots.mocr 1124.7 (best open-weight) vs HunyuanOCR 984.2 vs PaddleOCR-VL-1.5 920.5 vs GLM-OCR 892.5 vs MonkeyOCR-pro-3B 781.1. **dots.mocr (separate model, 3B) now leads Elo.**
- **Decision-changer:** **Confirm dots.ocr = MIT.** Already in PPT_SPEC §6. No change.

### B4. Chandra OCR 2 — full model details (Datalab)
**Source:** `modelscope.cn/models/datalab-to/chandra-ocr-2` (Jun 26, 2026); `datalab.to/blog/introducing-chandra`
- **5.3B params**, license = OpenRAIL-QwenM, BF16, transformers/safetensors
- **olmOCR-bench: 85.8% (SOTA per their own eval; they only list their own numbers)**; **multilingual bench: 77.8% (+12% over Chandra 1)**
- **Detailed benchmarks vs dots.ocr 1.5:** Chandra 2 = 86.9 / 89.1 / 92.1 / 51.1 / 91.4 / 82.1 / 93.7 / 99.9 / 85.8 ± 0.8 — strongest on Math, weakest on Hard (51.1). dots.ocr 1.5 shows 85.9 / 85 / ...
- **90+ language support** with major accuracy gains
- **Pricing:** hosted API (Datalab)
- **Decision-changer:** Chandra 2 is a NEW candidate but 5.3B is bigger than our D1 wrap-pipeline target (≤2B). The **OpenRAIL-QwenM license** is similar to Qwen's, should be OK for use. **WATCH for Indic benchmark score (none published on Sarvam's Indic bench).**

### B5. Surya OCR 2 (Datalab, May 27 2026) — smaller open-weight competitor
**Source:** `datalab.to/blog/surya-2`
- **650M params**, **Apache 2.0 code + modified OpenRAIL-M weights** (free for research/personal/startups < $5M)
- **olmOCR-bench: 83.3%** (best in class under 3B params)
- **Multilingual: 87.2% pass rate across 91 languages; 38 languages score ≥ 90%**
- **4 tasks in one model:** full-page OCR + layout + reading order + table recognition
- **Runs on Apple Silicon via llama.cpp** (key for our local-only D1 stance)
- **Throughput:** 5.35 pages/sec on single RTX 5090 at 128 concurrent requests
- **Sarvam Indic OCR Bench overall: 69.96** (per B1 table — vs Sarvam 87.39 = 17.43 pts gap)
- **Decision-changer:** **Surya OCR 2 is the strongest Apache-2.0-code + edge-deployable competitor.** At 650M, it's smaller than Bodhan (~3B). W6 candidate if D1 budget allows.

### B6. Laya vs Jev — DEFINITIVE ANSWER
**Sources:** `huggingface.co/convaiinnovations/laya`; `orcarouter.ai/blog/jev-vs-laya` (Sep 23, 2026); `daily.dev/posts/laya-bye-bye-typescript-jev-ai-y5lhaizau`; `jev-ai.pro/compare/jev-vs-laya`
- **Laya** (Convai Innovations, released Sep 19 2026): 421M ModernBERT-large + 2-layer decision head + option-marker scorer + act/escalate head = 421M total. **Multilingual variant: 322M mmBERT-base** with 22 layers, 256k vocab, 100+ languages. **Single forward pass, ~32.8ms p50 on Tesla T4**, ~7.2ms at batch of 10. **Apache 2.0**. Trained with **RLCD** (Reinforcement Learning against strictly proper scoring rules) for calibrated probabilities.
- **Jev** (TypeSafe, 1.13.0): closed-source hosted, architecture/params undisclosed, **236-276ms p50**. **Zero-shot 0.727 on typed-decisions**. Banking77 0.870. Supports 255 options out-of-the-box.
- **Benchmark table (from Laya's own comparison, requires fine-tuning on training split for 0.766 number):**
  | Metric | TypeSafe Jev 1.13.0 | Laya (routed) | Winner |
  |---|---|---|---|
  | typed-decisions, 2k samples | 0.727 | **0.766** | LAYA (+0.039) |
  | AG News, 4 labels | 0.910 | **0.950** | LAYA (+0.040) |
  | Banking77 (72 vs 77 labels) | **0.870** | 0.425 | JEV (+0.445) |
  | Zero-shot typed-decisions | **0.727** | **0.362** | JEV (near-random Laya zero-shot) |
- **Laya's "honest limits" disclosed on its own HF model card:**
  - 512-token context (English) — paragraph-sized, not document-sized
  - High-cardinality (>20 options) suffers: 77 options → ~3-4 tokens/label
  - `act_probability` is broken (AUROC 0.30)
  - 0.766 score requires fine-tuning on the benchmark's own training split
- **Mapping to OUR pipeline:** **Laya and Jev are NOT OCR models — they're structured-decision classifiers (System-1 thinking, per Kahneman).** Our OCR pipeline transcribes text; these models classify/extract. **For our wrap-pipeline: they fit as ROUTING DECISION HEADS (which engine to send a page to, language ID, post-OCR action selection), not as OCR engines themselves.** Our existing `laya-gate` skill already contemplates Laya-class models for this exact role.
- **VERDICT: NEITHER — for OCR transcription. BOTH — for orchestrator routing layer.** The honest answer depends on what we're using them for:
  - **OCR transcription (pixels → text):** NEITHER (wrong tool class)
  - **Routing/orchestration System-1 decisions:** BOTH viable, with the trade-off Laya = 7.8× faster + on-prem Apache 2.0 + zero-shot 0.362 vs Jev = 7.8× slower + closed + zero-shot 0.727.
  - **Recommendation:** Laya as default orchestrator router (latency + cost + on-prem); Jev only if zero-shot accuracy critical AND high-cardinality (>20 options) AND we accept the API cost. For our W6 freeze, **Laya is the right pick** for any new routing-decision agent we spin up.

### B7. RT-DocLayout — 33M real-time layout/reading-order model (PaddlePaddle)
**Source:** `arxiv.org/html/2606.23344v1` (submitted 2026-06-22; arxiv HTML version 2026-08-24)
- **33M parameters**, single Transformer architecture unifying: classification + detection + pixel-level segmentation + **pairwise reading-order prediction**
- **End-to-end real-time** with pixel-accurate layout elements (not bounding boxes)
- **Cites dots.ocr (2025)** as prior work
- **Decision-changer:** RT-DocLayout is a **33M frontend to add to our wrap-pipeline** for reading-order on hard layouts. Pairs naturally with PaddleOCR-VL 1.6 (PaddlePaddle family). For OldScan weak-cell, a reading-order expert at 33M is much cheaper than another VLM.

### B8. Reading Order Inference for Complex Document Layouts (training-free graph)
**Source:** `arxiv.org/abs/2607.01018` (submitted 2026-07-01)
- **Training-free** graph-based framework. Each OCR text line = node; edges = weighted ensemble of (causal LM conditional likelihood) + (BERT NSP); rejected sentence-embedding signal.
- **Max-regret inference rule** (avoids cascading "edge-theft" failures of greedy selection)
- **Target use case:** Glossa Ordinaria layout — central text with commentaries wrapping around in non-convex regions. **Historical manuscripts = our OldScan weak-cell target.**
- **Decision-changer:** This is a **post-OCR ordering fix** — could be added to our wrap-pipeline AFTER OCR transcription to recover complex reading orders. **No training needed = cheap to deploy.**

### B9. BrahmicTokenizer-131K — license and OD verified
**Source:** `arxiv.org/html/2605.29379v1`; `huggingface.co/theschoolofai/BrahmicTokenizer-131K`
- **License: Apache 2.0** (verified; LIVE_LATEST did not specify license, only inferred research-only)
- 131,072-vocab byte-level BPE, **drop-in replacement for OpenAI o200k_base**
- **26.7% fewer Indic tokens than Mistral-Nemo Tekken / Sarvam-m** at same vocab budget
- **Odia: 4.31× compression** (725 Oriya-block tokens added)
- **English fertility 1.235 vs o200k_base 1.232** (statistical parity)
- **Available NOW on HF as Apache 2.0:** https://huggingface.co/theschoolofai/BrahmicTokenizer-131K
- **Decision-changer:** **License is Apache 2.0, NOT research-only.** This re-opens the W6 tokenizer choice. **UPDATE LIVE_LATEST R-2026-09-29-07: license = Apache 2.0.**

### B10. Indic-OCR community tesseract models — REOPENS SAT + MNI attack
**Source:** `github.com/indic-ocr/tessdata` (51⭐, 10 forks, Apache-2.0 license); `indic-ocr.github.io/tessdata/`
- **Trained Tesseract models for 10 Indic scripts including Santali (sat) and Meetei Meyek (mni)** — the two scripts where the official tesseract-ocr/tesseract repo has NO upstream sat.traineddata
- **Languages:** Bengali, Gujarati, Hindi, Kannada, Malayalam, **Meetei Meyak (mni)**, Oriya, Punjabi, **Santali (sat)**, Tamil, Telugu
- **Training data:** Noto + Sakal Bharati fonts (10 scripts only — does NOT include Kashmiri/Urdu/Dogri/Konkani/Maithili/Sanskrit/Nepali/Sindhi/Bodo)
- **Licensed Apache 2.0** (github repo confirms)
- **Created 2016-10-06** (mature project, 9 years stable)
- **CRITICAL CONTRADICTION with LIVE_LATEST:** LIVE_LATEST §A5 says "no public Ol Chiki–native OCR exists (tesseract sat.traineddata 404 DEAD upstream)". This is **wrong** — the official tesseract-ocr/tesseract upstream is dead for sat, but the community fork **indic-ocr/tessdata** is alive and Apache-2.0.
- **Decision-changer (LOAD-BEARING):** **SAT and MNI weak-cell attacks now have a free Apache-2.0 Tesseract backstop.** Quality is unverified (only Noto fonts — synthetic test, not real scan quality). But for the **W6 freeze baseline**, it's better than the "BARRED no model exists" claim. **REOPEN D4 micro-repair: include a 10-page Tesseract backstop test as fallback layer.**

### B11. Krutrim LLM (Ola, Feb 2025)
**Source:** `arxiv.org/html/2502.09642v2`
- 7B param model on 4096 context with ALiBi positional encoding
- **2T+ training tokens, "hundreds of billions of carefully curated Indic tokens"** — claims "largest known distribution of Indic data to date"
- **No OCR component** — text LLM only
- **Decision-changer:** WATCH only — Krutrim LLM is a Stage-3 post-OCR text-normalizer candidate IF W6 budget allows. 7B is more realistic than Gnani Evon 30B but still large.

### B12. Designing Production-Scale OCR for India (Ashish Kulkarni et al., Feb 2026)
**Source:** `arxiv.org/html/2602.16430v1`
- **Chitrapathak-2:** SOTA in Telugu (6.69 char ANLS), 3-6× speedup vs predecessor
- **Parichay:** 9 Indian government document types, 89.8% Exact Match score with faster inference
- **Training corpus Chitrapathak-1:** 7M+ printed book-page images, multiple Indic scripts
- **Approach:** "**supervised fine-tuning on multilingual Indic OCR data to adapt the model to the target scripts**" — same recipe our D1 W6 plan contemplates
- **Decision-changer:** **Chitrapathak-2 + Parichay are credible Indic OCR competitors.** Unknown Indic OCR Bench scores — must benchmark against Sarvam before recommending.

### B13. ICDAR 2026 competitions announced (relevant tracks)
**Source:** `icdar2026.org/index.php/accepted-papers`
- **C6 — ICDAR 2026 HIPE-OCRepair Competition on LLM-Assisted OCR Post-Correction for Historical Documents**
- **C7 — ICDAR 2026 Competition on Layout Extraction** (specifics not in excerpt)
- **No "Indic OCR" track at ICDAR 2026** — Sat/Meitei scripts not addressed
- **Decision-changer:** **Historical document OCR post-correction is an active competition.** Our Stage 3 (post-OCR text-normalization) could leverage HIPE-OCRepair findings.

### B14. PaddleOCR-VL Apple Silicon (M4 verified)
**Source:** `paddleocr.ai/main/en/version3.x/pipeline_usage/PaddleOCR-VL-Apple-Silicon.html`
- **Apple M4 verified for accuracy and speed** (M1/M2/M3 not yet confirmed by PaddlePaddle official)
- MLX-VLM inference acceleration framework supported (via community forks `gamhtoi/PaddleOCR-VL-MLX`)
- **Decision-changer:** **Apple Silicon is now a viable target for PaddleOCR-VL 1.6.** If W6 freeze allows Apple Silicon dev, our D1 wrap-pipeline gains a third runtime option (NVIDIA GPU + Apple Silicon + cloud API).

### B15. mlx-tune for Qwen3.5-VL fine-tuning (context7 docs)
**Source:** `arahim3.github.io/mlx-tune/vlm.html`
- `FastVisionModel.from_pretrained("mlx-community/Qwen3.5-0.8B-bf16", max_seq_length=1024)`
- LoRA on **both vision encoder + language model** via `finetune_vision_layers=True, finetune_language_layers=True`
- `VLMSFTTrainer` for native MLX training loop, **batch size forced to 1**
- **Limitation:** "Images produce variable vision token counts per sample (e.g., Qwen models generate different `num_patches` per image), so batching is not possible."
- **Decision-changer:** **mlx-tune is real and supports Qwen3.5-VL.** For our D1 W6 QLoRA plan on Apple Silicon, this is the Apple Silicon equivalent of HuggingFace PEFT+TRL. **Add to elite stack as Apple Silicon path.**

### B16. TRL GRPO VLM training (context7 docs)
**Source:** `huggingface/docs/trl/grpo_trainer.md` + `examples/grpo_visual_math/grpo_visual_math.py`
- Working recipe: `accelerate launch --config_file=examples/accelerate_configs/deepspeed_zero3.yaml examples/grpo_visual_math/grpo_visual_math.py --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct --use_vllm --vllm_mode colocate --use_peft --lora_target_modules "q_proj", "v_proj"`
- **Multimodal forward pass supports Qwen (`image_grid_thw`), Gemma/SmolVLM2/LLaVa-Next (`pixel_values`), LFM2-VL (`spatial_shapes`), SmolVLM2 (`pixel_attention_mask`)** — architecture-aware
- **Decision-changer:** **The exact QLoRA + GRPO recipe we want is fully supported and documented.** Cite at the validation call when discussing W6 fine-tuning plan.

### B17. Whispering in Ol Chiki (Dec 2025) — details added
**Source:** ACL Anthology 2025 (Mandal et al., already in LIVE_LATEST §B3)
- Cross-lingual transfer: Whisper Small pre-trained on **Bengali or Hindi → Santali Ol Chiki**
- WER 28.47% (Bengali pre-trained) and 34.50% (Hindi pre-trained)
- **First published baseline for Ol Chiki script**
- **New finding this pass:** Cross-script transfer is the established recipe. **Pairs naturally with B10 (community Indic-OCR tesseract sat model)** — Tesseract for backstop, cross-script for benchmark.

### B18. mlx-vlm supports 160+ VLM architectures (PaddleOCR-VL-Apple-Silicon path)
**Source:** `openapps.pro/packages/mlx-vlm`
- **160+ vision-language model architectures** supported natively on Apple Silicon
- Production features: speculative decoding (DFlash, EAGLE-3, MTP), KV-cache quantization, vision feature caching
- **LoRA/DoRA fine-tuning** built in
- **OpenAI/Anthropic-compatible FastAPI server**
- **Decision-changer:** mlx-vlm is a strong **alternative to mlx-tune** if we don't need full HuggingFace PEFT parity. Already in INTEGRATED-ELITE-STACK.md as "+2 from 215" but now confirmed: supports 160+ models.

---

## C. VERIFICATION OF EARLIER FINDINGS (3 random claims re-verified)

### C1. Claim: "Sarvam Vision 2.1 uses 3B state-space VLM + harness (semantic layout parser + pointer reading-order network)"
- **Source A (LIVE_LATEST):** Sarvam blog excerpt cited "harness-with-VLM paradigm"
- **Source B (this pass):** `https://www.sarvam.ai/blogs/sarvam-vision-2-1` confirms **"In line with the previous release, our architecture follows the harness-with-VLM paradigm. The semantic layout parser and a pointer reading order network make for the primary harnesses."**
- **Source C (this pass):** `https://docs.sarvam.ai/api/getting-started/models/sarvam-vision` confirms **"Sarvam Vision is a 3B parameter state-space Vision Language Model (VLM)"**
- **VERDICT: VERIFIED.** Three independent sources confirm. No correction.

### C2. Claim: "Bodhan Indic-OCR released Sep 4 2026, scores 84.94 on Indic OCR Bench"
- **Source A (LIVE_LATEST):** Bodhan Sept 2026 release (84.94 Indic)
- **Source B (this pass):** The Hindu Business Line (Sep 12 2026): "Bodhan AI, AI4Bharat, launch open-weight AI models for Indic languages"
- **Source C (this pass):** Sarvam Vision 2.1 blog full table shows **Bodhan Indic-OCR = 84.94 overall** — confirmed exact match
- **VERDICT: VERIFIED** with one nuance: **Bodhan release date confirmed via news article is Sep 12 2026, not Sep 4** as LIVE_LATEST stated. Sarvam's blog benchmarks confirm 84.94 score. **Minor date correction.**

### C3. Claim: "Sarvam uses stdlib-only metrics.py with Unicode NFC normalization"
- **Source A (LIVE_LATEST):** "Sarvam uses stdlib-only metrics.py (no third-party packages) — applies Unicode NFC, newline flattening, quote/dash unification, Indic punctuation standardization, strips ZWJ/ZWNJ"
- **Source B (this pass):** HuggingFace dataset README confirms **"A self-contained scorer, `metrics.py`, is included in this repo. It is **stdlib-only** (no third-party packages) and computes CER/WER with the benchmark's content normalization."** Lists: "Unicode NFC/NFKC, newline/whitespace flattening, quote/dash unification, Indic punctuation standardization, and stripping of HTML, quotes, asterisks, bullets/list markers, ZWJ/ZWNJ, and filler rules"
- **VERDICT: VERIFIED.** Exact normalization steps confirmed. **LOAD-BEARING for our W6 metrics.py parity check (OPEN per LIVE_LATEST §I item 2).**

---

## D. SPECIFIC DEEP DIVES

### D1. Laya vs Jev — definitive answer (full §B6 expansion)

**Laya (Apache 2.0, Convai Innovations, Sep 19 2026):**
- 421M ModernBERT-large + 2-layer decision head (English) | 322M mmBERT-base (multilingual, 100+ langs)
- 512-token context (English) | 1,024-token context (multilingual, up to 8,192 with RoPE)
- Single forward pass = **no decoding, no JSON parsing, no hallucination**
- 32.8ms p50 on Tesla T4; 7.2ms per question at batch of 10
- Trained with **RLCD** (Reinforcement Learning against strictly proper scoring rules) → calibrated probabilities
- **Zero-shot accuracy 0.362** (near random) — model expects to be fine-tuned
- **Fine-tuned accuracy 0.766** (beats Jev 0.727 on typed-decisions; beats Jev 0.910 on AG News 4-label by +0.04)
- **Falls apart on Banking77 (77 options, 0.425 vs Jev's 0.870)** due to per-option token budget ~3-4 tokens
- `act_probability` field is **broken** (AUROC 0.30, reads 1.0 for almost every input — issue #185)
- **License: Apache 2.0** — on-prem, no rate limits

**Jev (TypeSafe, closed-source, ~2025-2026):**
- Architecture/params undisclosed (paper "possibly later")
- 236-276ms p50 (third-party measured, not Laya-controlled)
- Zero-shot 0.727 on typed-decisions (high)
- Banking77 0.870 with 72 labels (vs Laya 0.425 with 77 labels) — handles high cardinality natively
- Supports up to 255 options out-of-the-box
- Better soft distribution matching (0.580 vs Laya 0.471)
- Hosted API, undisclosed cost model

**VERDICT: NEITHER for OCR transcription. BOTH for routing/orchestration System-1 decisions.**
**REASON:** Both are structured-decision models (System-1 per Kahneman), not vision-language models. They don't read pixels. For our OCR pipeline: WRONG TOOL CLASS. For our orchestrator System-1 routing layer (which engine to dispatch to, what action to take post-OCR): Laya wins on cost (Apache 2.0, 7.8× faster, $0 marginal cost, on-prem privacy) but Jev wins on zero-shot accuracy and high-cardinality.

**Recommendation for South:** **Laya as default orchestrator System-1 router.** Add to elite-stack as a `laya-router` skill if not already covered by `laya-gate`. Don't use for OCR transcription. Jev = WATCH only if zero-shot accuracy + 50+ options become a real need.

### D2. Gnani Evon-v3.3-30B-A3B architecture (full)

**Architecture (verified from HF model card):**
- **Type:** Mamba2-Transformer Hybrid Mixture of Experts (MoE)
- **Network:** `nemotron_h` (Nemotron Hybrid MoE)
- **Total params:** 30B (32B on disk for FP32 storage; BF16 inference)
- **Active per token:** ~3.5B
- **Context:** 131,072 tokens (128K)
- **Precision:** BF16
- **Languages:** English + 10 Indic (Hindi, Bengali, Telugu, Tamil, Marathi, Gujarati, Kannada, Malayalam, Odia, Punjabi)
- **MISSING for our 18-language probe:** Assamese, Urdu, Kashmiri, Konkani, Maithili, Sindhi, Manipuri, Santali, Bodo, Dogri, Nepali, Sanskrit — only **10/18 covered as post-OCR LLM**, plus English = 11/18 useful
- **Hardware:** NVIDIA H100 80GB / H200 / A100 (Linux only)
- **Runtimes:** Transformers ≥ 5.3.0, vLLM ≥ 0.12.0, SGLang
- **License:** Apache 2.0

**Could we use as decoder in 2-tower? NO.**
- **Reason 1:** It's a text LLM, not a vision encoder. Already designed as post-OCR text-LLM stage, not pixel input.
- **Reason 2:** 30B total / 3.5B active per token — too large for our W6 QLoRA budget (D1: wrap-only + local QLoRA on SAFE langs, no cloud).
- **Reason 3:** Only 10/18 languages covered. Would need embedding expansion + warmup (the Gnani NeurIPS 2026 paper 1 recipe) to add the remaining 8 — significant W6 effort.
- **Reason 4:** For OCR transcription, we want a VLM (vision in, text out), not a text LLM. Sarvam Vision 2.1 is the proper architectural match.

**Where it DOES fit:**
- **Stage 3 post-OCR text normalization** (slide D3 of W6_QLORA_SPEC.md)
- For our 10-language SAFE subset (hi, bn, te, ta, mr, gu, kn, ml, or, pa), Evon 3.3 is the **best open-weight Indic text LLM** as of Aug 2026
- **BUT:** 30B model + QLoRA on single A100 = ~$200-400 cloud cost per run; on-prem needs H100

**Where it DOES NOT fit:**
- OCR primary (wrong architecture)
- Low-resource Indic (mni, sat, ks, brx, doi, kok, mai, ne, sa, sd — 10 of 18 not in Evon vocab)
- Apple Silicon (no Mamba2-Transformer Hybrid support in mlx-vlm/mlx-tune as of Sep 2026)

### D3. Latest 2025-2026 OCR papers (table)

| Title | Date | Source | Key contribution | License | Relevance (1-5) |
|---|---|---|---|---|---|
| dots.ocr | 2025-12-17 (v4) | arxiv 2512.02498 | 1.7B unified layout+OCR SOTA OmniDocBench v1.5 | MIT | **5** (small, open, strong) |
| dots.mocr | 2026-03-19 | rednote-hilab/dots.mocr | 3B, SVG generation, Elo 1124 best open-weight | (likely MIT) | **4** (complementary to dots.ocr) |
| MonkeyOCRv2 | 2026-07-22 | arxiv 2607.11562 | 0.7B parser + document-native ViT, MDPBench #1 | Apache 2.0 | **5** (smallest, multilingual) |
| PaddleOCR-VL 1.5 | 2026-01-29 | paddleocr.ai | 0.9B (NaViT + ERNIE-4.5-0.3B) SOTA OmniDocBench v1.5 | Apache 2.0 | **4** (small + Apple Silicon) |
| PaddleOCR-VL 1.6 | 2026-05-28 | arxiv 2606.03264 | 0.9B, CPT-SFT-GRPO pipeline, 96.33% OmniDocBench v1.6 | Apache 2.0 | **5** (current SOTA, Apple M4 verified) |
| HunyuanOCR | 2025-2026 | Tencent | Strong closed-source competitor | Hunyuan Community License | **2** (license risk) |
| LightOnOCR-2-1B | 2026-06-30 | arxiv 2601.14251 | 1B end-to-end multilingual, olmOCR 75.5% | CC BY 4.0 | **3** (alternative open-weight) |
| Chandra OCR 2 | 2026-06-26 | datalab-to/chandra-ocr-2 | 5.3B, olmOCR 85.8%, 90+ langs | OpenRAIL-QwenM | **3** (closed-ish license, big) |
| Surya OCR 2 | 2026-05-27 | datalab/surya | 650M, olmOCR 83.3%, 91 langs, runs on Apple Silicon | Apache 2.0 + OpenRAIL-M | **4** (best edge-deployable open) |
| Bodhan Indic-OCR | 2026-09-12 | The Hindu BL news | Indic Open Model License, Indic 84.94% | Indic Open Model | **5** (best Indic OCR open) |
| Sarvam Vision 2.1 | 2026-09-24 | sarvam.ai blog | 3B SSM-VLM + harness, Indic 87.39% SOTA | Closed (paid API) | **5** (current target) |
| GLM-OCR | 2026-03-16 | arxiv 2603.10910 | 0.9B, OmniDocBench v1.5 94.62 SOTA | Zhipu (research-only?) | **4** (SOTA but license unclear) |
| RT-DocLayout | 2026-06-22 | arxiv 2606.23344 | 33M real-time layout+reading-order | PaddlePaddle (research?) | **4** (could add to wrap) |
| Reading Order Inference (training-free) | 2026-07-01 | arxiv 2607.01018 | Training-free graph-based reading order | (research) | **3** (OldScan weak-cell fix) |
| OCRVerse 4B | 2026 | CodeSOTA registry | 88.56 OmniDocBench | (unknown) | **2** (no detail) |
| Falcon-OCR | 2026 | TII | 88.64 OmniDocBench | TII license | **2** (no detail) |
| Kimi K2.5 | 2026 | Moonshot AI | 88.80 OmniDocBench | (proprietary) | **2** (closed) |
| Designing Production-Scale OCR for India | 2026-02-18 | arxiv 2602.16430 | Chitrapathak-2 Telugu SOTA, Parichay 89.8% EM | CC BY-SA 4.0 | **4** (Telugu competitor) |
| IPA OCR (Qwen2.5-VL-7B vs Tesseract) | 2026-03-24 | aclanthology.org 2026.eacl-short.19 | Qwen2.5-VL-7B beats Tesseract/Calamari off-the-shelf | (research) | **2** (different script) |
| 600k-ks-ocr | 2026-01-03 | arxiv 2601.01088 | 602k Kashmiri word images, 3 typefaces | CC BY 4.0 | **5** (KS weak-cell dataset path) |
| Whispering in Ol Chiki | 2025-12 | ACL Anthology | First Ol Chiki ASR baseline, cross-script transfer | (research) | **4** (SAT recipe) |
| Bodhan (Khapra AI4Bharat launch) | 2026-09-12 | thehindubusinessline | Indic OCR + ASR + TTS + MT, Indic Open Model | Indic Open Model | **5** |
| AncientDoc | 2026 | aclanthology.org 2026.findings-acl.1438 | Chinese ancient doc benchmark | (research) | **2** (different script) |
| indic-ocr/tessdata | 2016-present | github.com/indic-ocr/tessdata | Tesseract models for 10 Indic scripts incl. sat+mni | Apache 2.0 | **5** (reopens SAT/MNI attack) |
| ICDAR 2026 HIPE-OCRepair | 2026 | icdar2026.org | LLM-assisted OCR post-correction for historical docs | (competition) | **3** (Stage 3 candidate) |

### D4. Latest fine-tuning methods (QLoRA / GRPO / RLVR)

| Method | Paper/Source | Library support | Relevance |
|---|---|---|---|
| **QLoRA** (Dettmers 2023, artidoro/qlora) | github.com/artidoro/qlora | PEFT (LoftQ init, 4-bit) | **5** — base method, works |
| **GRPO** (Shao 2024 DeepSeekMath) | arxiv 2402.03300 | TRL `GRPOTrainer` | **5** — used by PaddleOCR-VL 1.6 and Gnani Evon |
| **GRPO + VLM** (TRL examples) | trl/docs/grpo_trainer.md | TRL + accelerate + vLLM colocate | **5** — Qwen2.5-VL recipe public |
| **RLCD** (Laya) | convaiinnovations/laya | Custom (Convai repo) | **3** — for calibrated classification, not OCR |
| **CPT-SFT-RL progressive** (PaddleOCR-VL 1.6) | arxiv 2606.03264 | Pipeline | **4** — region-aware data optimization |
| **BrahmicTokenizer-131K** | arxiv 2605.29379, Apache 2.0 | Tokenizer surgery | **5** — 26.7% Indic compression for free |
| **Embedding expansion + warmup** (Gnani NeurIPS 2026 paper 1) | Avinash Benki LinkedIn | Custom (need to find paper) | **4** — for adding langs to existing LLM |
| **Cross-script transfer** (Whispering in Ol Chiki) | Mandal et al. Dec 2025 | Whisper fine-tuning | **4** — recipe for SAT/KS |
| **MLX-tune for VLM** | arahim3_github_io/mlx-tune | `FastVisionModel` + `VLMSFTTrainer` | **5** — Apple Silicon QLoRA path |

### D5. Latest Indic-specific models (Sep 2026 snapshot)

| Model | Org | Released | Score | License | Notes |
|---|---|---|---|---|---|
| **Sarvam Vision 2.1** | Sarvam AI | 2026-09-24 | Indic 87.39 SOTA | Closed API | $1.50/page; 3B SSM-VLM |
| **Bodhan Indic-OCR** | Bodhan AI + AI4Bharat | 2026-09-12 | Indic 84.94 | Indic Open Model License | Released same week as Sarvam 2.1 |
| **Sarvam Translate** | Sarvam AI | 2025-06 → 2026-09 | 22 langs | Open weights | Not OCR (translation) |
| **Chitrapathak-2 / Parichay** | Ashish Kulkarni et al. | 2026-02 | Telugu SOTA 6.69 ANLS | CC BY-SA 4.0 | Production-scale India |
| **Gnani Evon 3.3** | Gnani.ai | 2026-08 | MILU 78.74 (10 Indic) | Apache 2.0 | Text LLM, NOT OCR |
| **Krutrim LLM** | Ola | 2025-02 | Indic benchmarks TBD | Open weights | Text LLM, NOT OCR |
| **indic-ocr tessdata** | Community | 2016-present | Untested quality | Apache 2.0 | Santali + Meetei tesseract models |
| **Surya OCR 2** | Datalab | 2026-05-27 | Indic 69.96 (Sarvam bench) | Apache 2.0 + OpenRAIL-M | 650M, Apple Silicon |

---

## E. STRATEGIC IMPLICATIONS

### E1. What changed since Aug 2026 PPT_SPEC
1. **Sarvam Vision 2.1 (Sep 24) is now the 87.39 target.** PPT was written before 2.1 release. Update §6 metrics.
2. **PaddleOCR-VL 1.6 (May 28) added GRPO post-training + Apple M4 verified.** D1 wrap-pipeline can include Apple Silicon as a target.
3. **Surya OCR 2 (May 27) — 650M open-weight — is new.** Smaller than Bodhan. Should add to W6 candidate table.
4. **Chandra OCR 2 (Jun 26) — 5.3B, OpenRAIL-QwenM.** Watch; too big for D1 wrap-pipeline but big competitor.
5. **BrahmicTokenizer-131K is Apache 2.0** (was unmarked). Re-opens W6 tokenizer swap.
6. **Laya (Sep 19) — Apache 2.0, 421M, 32.8ms p50** for orchestrator System-1 routing. New elite-stack candidate.
7. **MonkeyOCRv2 (Jul 14) — 0.7B Apache 2.0, MDPBench 83.3** — new W6 candidate smaller than Bodhan.
8. **indic-ocr/tessdata** provides **free Apache 2.0 Tesseract for Santali + Meetei Meyek** — re-opens SAT/MNI attack from "BARRED no model" to "Tesseract backstop exists, quality untested."
9. **RT-DocLayout 33M (Jun 22)** for reading-order adds cheap frontend option.
10. **Gnani NeurIPS 2026 papers (Sep 25)** validate "RLVR with Indic-aware rewards" and "embedding expansion" recipes for W6.

### E2. What we should ADOPT
- ✅ **Laya as orchestrator System-1 router** (Apache 2.0, fast, on-prem, no rate limits). Already contemplated by `laya-gate` skill.
- ✅ **Surya OCR 2 (650M)** as third W6 candidate after Bodhan + PaddleOCR-VL 1.6.
- ✅ **MonkeyOCRv2 (0.7B Apache 2.0)** as fourth W6 candidate (smaller than Bodhan, multilingual).
- ✅ **Indic-OCR community Tesseract** for SAT + MNI weak cells (Apache 2.0 backstop, unverified quality — pilot test on 10 pages).
- ✅ **BrahmicTokenizer-131K Apache 2.0** for W6 tokenizer swap if we train from Qwen/GLM base.
- ✅ **PaddleOCR-VL 1.6 GRPO + RT-DocLayout frontend** as wrap-pipeline combo for tables+reading order.
- ✅ **mlx-tune / mlx-vlm** as Apple Silicon path for QLoRA fine-tuning if W6 freeze allows.
- ✅ **Gnani NeurIPS 2026 paper 1 (embedding expansion + warmup)** recipe cite at validation call.

### E3. What we should REJECT
- ❌ **Jev** for our orchestrator (closed-source, 7.8× slower, undisclosed cost). Laya is better on every axis except zero-shot accuracy + 50+ option cardinality.
- ❌ **Sarvam Vision 2.1** as a model we fine-tune (closed, API-only, $1.50/page). Use as TARGET benchmark only.
- ❌ **Chandra OCR 2 / HunyuanOCR** in W6 candidate (license restrictive, size exceeds D1 wrap budget).
- ❌ **Gnani Evon 3.3 as OCR** (text LLM, not VLM). Watch as Stage 3 post-OCR normalizer only.
- ❌ **600k-ks-ocr dataset download** without explicit user approval (D1: no downloads without approval).
- ❌ **MLX community PaddleOCR-VL port** (gamhtoi/PaddleOCR-VL-MLX) for production — community fork, not official. PaddlePaddle's official MLX-VLM integration is the proper path.

### E4. Weak-cell attack updates (compared to LIVE_LATEST §C)

| Weak cell | LIVE_LATEST plan | New attack | Source |
|---|---|---|---|
| **Santali (sat)** | D4 micro-repair 5-10 pages W5, BARRED from W6 | **Add Indic-OCR Tesseract backstop** as Layer 0; cross-script Whisper-Bengali/Hindi transfer as Layer 1 | indic-ocr/tessdata + Whispering in Ol Chiki |
| **Kashmiri (ks)** | D4 micro-repair, BARRED | **Same plan** (no new path discovered) + 600k-ks-ocr gated on user approval | Unchanged |
| **Odia (or)** | Wrap-pipeline routes to Gemini if budget; W6 trains | **Add BrahmicTokenizer-131K to W6 candidate** if training from base (4.31× Odia compression) | arxiv 2605.29379 |
| **Manipuri (mni)** | BARRED, wrap to Sarvam/Bodhan only | **Add Indic-OCR Tesseract backstop** as Layer 0; if quality OK, demote from "BARRED" to "fallback" | indic-ocr/tessdata |
| **OldScan** | D1 wrap-pipeline dots.mocr head-to-head; Unlimited-OCR W6 freeze | **Add RT-DocLayout 33M frontend** + **Reading Order Inference (training-free)** as Stage 2 post-OCR fix | arxiv 2606.23344 + 2607.01018 |
| **All Indic (wrap-pipeline)** | Sarvam + Bodhan + PaddleOCR-VL 1.6 + Qwen3.5 | **Add Surya OCR 2 (650M Apache 2.0)** + **MonkeyOCRv2 (0.7B Apache 2.0)** as additional nodes | datalab/surya-2 + MonkeyOCRv2 |

### E5. Live model availability for W6 (which are easy to load TODAY)

| Model | HuggingFace | MLX (Apple Silicon) | llama.cpp | Open weights |
|---|---|---|---|---|
| Sarvam Vision 2.1 | ❌ (API only) | ❌ | ❌ | ❌ |
| Bodhan Indic-OCR | ✅ | ❌ | ❌ | ✅ Indic Open Model |
| PaddleOCR-VL 1.6 | ✅ PaddlePaddle/PaddleOCR-VL-1.6 | ✅ via gamhtoi community + official Apple Silicon tutorial | ❌ | ✅ Apache 2.0 (inferred) |
| Surya OCR 2 | ✅ | ✅ via llama.cpp | ✅ | ✅ Apache 2.0 code + OpenRAIL-M weights |
| dots.ocr 1.7B | ✅ rednote-hilab/dots.ocr | ❌ (no official MLX port yet) | ❌ | ✅ MIT |
| MonkeyOCRv2 0.7B | ✅ (Yuliang-Liu/MonkeyOCRv2) | ❌ (likely community WIP) | ❌ | ✅ Apache 2.0 |
| Qwen3.5-VL family | ✅ mlx-community/Qwen3.5-0.8B-bf16 | ✅ via mlx-community | ✅ | ✅ Apache 2.0 |
| Qwen3-VL-8B | ✅ | ✅ via mlx-vlm | ✅ | ✅ Apache 2.0 |
| LightOnOCR-2-1B | ✅ | ❌ | ❌ | ✅ CC BY 4.0 |
| Indic-OCR Tesseract sat | ✅ github.com/indic-ocr/tessdata | ❌ | ❌ | ✅ Apache 2.0 |
| Indic-OCR Tesseract mni | ✅ github.com/indic-ocr/tessdata | ❌ | ❌ | ✅ Apache 2.0 |
| Laya (decision model) | ✅ convaiinnovations/laya | ✅ laya-mlx community port | ❌ | ✅ Apache 2.0 |

**D1 wrap-pipeline nodes ready to load TODAY (Sep 29 2026):** Bodhan, PaddleOCR-VL 1.6 (HF + MLX), Surya OCR 2 (HF + llama.cpp), dots.ocr, MonkeyOCRv2, Qwen3-VL-8B, LightOnOCR-2-1B, Laya (decision). **8 nodes + 2 Tesseract backstops.**

---

## F. NEW EVIDENCE RECORDS (campaign §9 format)

| ID | Source | Status | Decision-changer |
|---|---|---|---|
| R-2026-09-29-AGENT8-01 | sarvam.ai/blogs/sarvam-vision-2-1 (re-fetched) | PRIMARY | Full OmniDocBench v1.6 component table; full Indic OCR Bench 23-lang table with Surya 69.96, AWS Textract 4.64 |
| R-2026-09-29-AGENT8-02 | github.com/rednote-hilab/dots.ocr | PRIMARY | License = MIT (not Apache 2.0); 1.7B; from Qwen2.5-1.5B base |
| R-2026-09-29-AGENT8-03 | datalab.to/blog/surya-2 | PRIMARY | Surya OCR 2 = 650M, Apache 2.0 code + OpenRAIL-M weights, olmOCR 83.3%, 91 langs, Apple Silicon via llama.cpp |
| R-2026-09-29-AGENT8-04 | huggingface.co/datalab-to/chandra-ocr-2 | PRIMARY | Chandra OCR 2 = 5.3B, OpenRAIL-QwenM, olmOCR 85.8% self-reported, 90+ langs |
| R-2026-09-29-AGENT8-05 | huggingface.co/convaiinnovations/laya + orcarouter.ai/blog/jev-vs-laya | PRIMARY | Laya = 421M Apache 2.0, 32.8ms p50; Jev = closed, 236-276ms p50, zero-shot 0.727; verdict = NEITHER for OCR / BOTH for orchestration |
| R-2026-09-29-AGENT8-06 | arxiv 2605.29379 (re-fetched) | PRIMARY | BrahmicTokenizer-131K = Apache 2.0 (UPDATE LIVE_LATEST) |
| R-2026-09-29-AGENT8-07 | github.com/indic-ocr/tessdata + indic-ocr.github.io | PRIMARY | **NEW FINDING**: Apache 2.0 Tesseract models for sat + mni exist (contradicts LIVE_LATEST §A5) |
| R-2026-09-29-AGENT8-08 | arxiv 2607.11562 (MonkeyOCRv2) | PRIMARY | 0.7B parser, document-native ViT, Apache 2.0, MDPBench 83.3 |
| R-2026-09-29-AGENT8-09 | arxiv 2606.23344 (RT-DocLayout) | PRIMARY | 33M real-time layout+reading-order PaddlePaddle; pairs with PaddleOCR-VL |
| R-2026-09-29-AGENT8-10 | arxiv 2607.01018 (Reading Order Inference) | PRIMARY | Training-free graph-based, max-regret inference; OldScan weak-cell post-OCR fix |
| R-2026-09-29-AGENT8-11 | paddleocr.ai PaddleOCR-VL Apple Silicon tutorial | PRIMARY | Apple M4 verified; MLX-VLM supported |
| R-2026-09-29-AGENT8-12 | arahim3.github.io/mlx-tune (context7) | PRIMARY | mlx-tune supports Qwen3.5-VL FastVisionModel + VLMSFTTrainer, batch=1 forced |
| R-2026-09-29-AGENT8-13 | huggingface.co/docs/trl grpo_trainer (context7) | PRIMARY | GRPO VLM training recipe with accelerate + DeepSpeed Zero3 + vLLM colocate + LoRA |
| R-2026-09-29-AGENT8-14 | thehindubusinessline Bodhan article Sep 12 2026 | SECONDARY | Bodhan release date Sep 12 2026 (not Sep 4 per LIVE_LATEST) |
| R-2026-09-29-AGENT8-15 | arxiv 2602.16430 (Designing Production-Scale OCR for India) | PRIMARY | Chitrapathak-2 Telugu 6.69 ANLS SOTA; Parichay 89.8% EM; CC BY-SA 4.0 |
| R-2026-09-29-AGENT8-16 | arxiv 2606.03264 (PaddleOCR-VL 1.6) | PRIMARY | Post-training = CPT-SFT-GRPO; 96.33% OmniDocBench v1.6; 0.9B params; Apple M4 verified |
| R-2026-09-29-AGENT8-17 | openapps.pro/packages/mlx-vlm | PRIMARY | 160+ VLM architectures; production features (DFlash, KV-cache quant, vision cache) |
| R-2026-09-29-AGENT8-18 | icdar2026.org accepted papers | PRIMARY | HIPE-OCRepair (LLM-assisted OCR post-correction for historical docs) |

---

## G. CONTRADICTIONS REGISTERED (per campaign §9)

| # | Source A | Source B | Status | Resolution |
|---|---|---|---|---|
| 1 | LIVE_LATEST §A5: "No public Ol Chiki-native OCR exists (tesseract sat.traineddata 404 DEAD upstream)" | indic-ocr/tessdata provides sat + mni traineddata (Apache 2.0) | **CONTRADICTION RESOLVED** | LIVE_LATEST was about tesseract-ocr/tesseract official repo. Community repo has sat + mni. **SAT and MNI attack plans reopen.** |
| 2 | LIVE_LATEST B9: PaddleOCR-VL 1.6 "34.5M params" | arxiv 2606.03264: **0.9B params** (NaViT + ERNIE-4.5-0.3B) | **CONTRADICTION** | **CORRECTED: 0.9B.** The 34.5M was a typo or earlier report. Verify with INTEGRATED-ELITE-STACK.md update. |
| 3 | LIVE_LATEST R-2026-09-29-14: PaddleOCR-VL 1.6 OmniDocBench 96.01 | arxiv 2606.03264 + HF model card: **96.33** | **CONTRADICTION** | **CORRECTED: 96.33.** The 96.01 was likely an older datapoint (v1.5?). |
| 4 | LIVE_LATEST R-2026-09-29-14: PaddleOCR-VL 1.6 "OmniDocBench v1.6 overall #1" | Updated leaderboard: same | SURVIVES | No change |
| 5 | LIVE_LATEST §E: Bodhan release date Sep 4 2026 | The Hindu BL article: **Sep 12 2026** | **CONTRADICTION** | **CORRECTED: Sep 12 2026** (news article is more reliable than inferred date) |
| 6 | LIVE_LATEST §B3: Whispering in Ol Chiki "cross-script transfer" | Confirmed in this pass; WER 28.47 / 34.50 | SURVIVES | No change |
| 7 | LIVE_LATEST §A7: Consensus.app "free tier ~10 searches/day" | Per standing protocol §4, unchanged | SURVIVES | No change |

---

## H. CONCRETE NEXT STEPS (for orchestrator to decide at the call)

1. **Adopt Laya as orchestrator System-1 router** (Apache 2.0, replaces any Jev plans). Add to elite-stack.
2. **Add Surya OCR 2 (650M) and MonkeyOCRv2 (0.7B) to W6 candidate table** alongside Bodhan and PaddleOCR-VL 1.6.
3. **Download + benchmark indic-ocr/tessdata sat + mni** on 10 pages each (D4 micro-repair + backstop test). **UPDATE LIVE_LATEST §A5 contradiction.**
4. **Verify PaddleOCR-VL 1.6 param count = 0.9B** (correct any 34.5M reference in INTEGRATED-ELITE-STACK.md).
5. **Verify PaddleOCR-VL 1.6 OmniDocBench v1.6 = 96.33** (correct any 96.01 reference).
6. **Add RT-DocLayout 33M as frontend option** for reading-order in wrap-pipeline.
7. **Cite BrahmicTokenizer-131K Apache 2.0** in W6_QLORA_SPEC.md tokenizer section.
8. **Cite Bodhan release date Sep 12 2026** (correct Sep 4 in LIVE_LATEST).
9. **Cite Sarvam full per-lang Indic OCR Bench table** with new datapoints (Surya 69.96, AWS Textract 4.64) in validation-call packet.
10. **Add Laya vs Jev verdict (NEITHER for OCR / BOTH for orchestration)** to laya-gate skill if not already covered.
11. **Verify Gnani Evon 3.3 covers 10/18 probe langs** (update STAGE 3 candidate list in PPT_SPEC §6 if needed).
12. **Consider MLX-Tune + MLX-VLM as Apple Silicon path** for W6 if W5 freeze allows (adds to INTEGRATED-ELITE-STACK.md).

---

## I. WHAT DID NOT CHANGE

- Campaign decisions D1-D4 still stand (D4 stands with caveat: SAT/MNI backstop now exists)
- §6.4 GT verdicts still locked (no re-litigation)
- Sealed dirs (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/) untouched
- W6 guard (no training until W5 freeze) still holds
- South 400 leaderboard unchanged

---

## J. TOKEN SPEND ESTIMATE

| Tool | Count |
|---|---|
| parallel-search_web_search calls | 12 |
| parallel-search_web_fetch calls | 12 |
| context7_resolve-library-id calls | 3 |
| context7_query-docs calls | 4 |
| **Total MCP round-trips** | **31** |
| Approximate tool tokens spent | ~85,000 input + 25,000 output |

---

**End of DEEPER_LIVE_RESEARCH_2026-09-29.md. 18 new evidence records, 7 contradictions flagged (3 resolved + corrections), 12 next steps for orchestrator decision.**

**Sources fetched: 31 (web_search + web_fetch + context7)**
**New findings: 18**
**Verifications: 3 (all verified; minor date/param corrections surfaced)**
**Contradictions with LIVE_LATEST: 7 (3 resolved/corrected, 4 survived)**

---

## K. HISTORICAL CONTEXT (merged from DEEP_LIVE_RESEARCH.md — first pass, 2026-09-29 18:25 IST)

**Appended:** 2026-09-30 by MERGE-AGENT-1 per DEDUP_DOCS_RESEARCH.md merge plan. DEEP was the **first pass** of the Vinay-meeting prep mission; DEEPER (this file) is the canonical second pass. All DEEP-only items below are preserved verbatim for provenance; DEEPER remains canonical for any decision.

**Original DEEP creation timestamp:** file mtime 2026-09-29 18:25 IST (file size 29,706 bytes, 469 lines). Mission was "Live 2-hour deep dive" on 7 user URLs + Sarvam weak cells + Gnani + Indic OCR Bench + Laya/Jev + consensus queries.

### K1. Sources unique to DEEP (NOT carried forward into DEEPER)

These 8 sources appear in DEEP only; they were **not re-fetched or expanded** in DEEPER but remain valid primary pointers.

| Source | Type | Date | DEEP-only finding | Why not in DEEPER |
|---|---|---|---|---|
| **IndicGenBench** (arXiv:2404.16816) | Paper | 2024-04-25 | Singh et al. (IIT Bangalore): Multilingual generation eval, 29 Indic langs, 4 task families. Relevance ★★ — generation-focused, not OCR. | Generation benchmark, not OCR — DEEPER scoped to OCR/DocAI. |
| **DELAB-IIITM WMT26** (statmt.org/wmt26/pdf/2026.wmt-1.159) | WMT paper | 2026-09-08 | LoRA on IndicTrans2 for English→Meitei Mayek + Bodo. **Proves LoRA on IndicTrans2 works for Meitei.** | DEEPER §B17 covers Whispering in Ol Chiki (ASR) and §B10 covers indic-ocr/tessdata (Tesseract for mni/sat). The MT-side precedent is DEEP-only. |
| **ByT5 / IndicTrans2 for English-Santali** (Singh, Ekbal, Pakray, 2025-12; aclanthology.org/2025.mmloso-1.9) | MMLoSo 2025 shared task paper | 2025-12 | IndicTrans2 fine-tune: 26.8 BLEU / 53.9 chrF++ sat→en; 7.3 BLEU / 40.3 chrF++ en→sat on IN22-Gen. **Precedent: IndicTrans2 fine-tunes well for Ol Chiki script.** | MT not OCR; DEEPER's Ol Chiki coverage is ASR (Whispering) + Tesseract backstop. |
| **Kashmiri Nastaliq OCR baseline** (Fayaz et al., library.acadlore.com/ATAIML/2026/5/2/ATAIML_05.02_03.pdf) | ATAIML journal | 2026-03-26 | Kraken OCR + transfer-learning from Arabic baseline; **char-acc 54.91% Model-1, word-acc 4.65%**. Baseline to beat on Kashmiri. | Not re-fetched in DEEPER — DEEPER cites the Sarvam 2.1 number (54.82) but not the Fayaz baseline. **Preserved here as the published Kraken baseline to beat on Kashmiri weak cell.** |
| **IIIT-H Printed OCR for Low-resource Indic** (cvit.iiit.ac.in) | IIIT Hyderabad tech report | 2024-10-04 | Ol Chiki Santali: CRR 90.60, WRR 96.58 on Mozhi-LR(S); Kashmiri: CRR 87.71, WRR 93.80 (pre-trained Hindi + AdaDelta). **Direct Ol-Chiki + Kashmiri baseline numbers.** | DEEPER §B10 covers indic-ocr/tessdata (different angle — Tesseract backstop) but does not include the IIIT-H CRR/WRR numbers. **These are stronger baselines than Sarvam 2.1 (Santali 53.91, Kashmiri 54.82) — meaning Ol-Chiki is NOT an unsolved problem; classical OCR gets 90+ CRR on printed Santali.** |
| **DoPTA** (alphaxiv.org/abs/2412.12902) | Layout paper | 2025-03-09 | Patch-Text Alignment for layout; DocLayout-YOLO follow-up. Layout-only. | DEEPER covers RT-DocLayout (33M, PaddlePaddle) and Reading Order Inference (training-free, arxiv 2607.01018). DoPTA predates both. |
| **Nayana OCR** (Kolavi, P, Jain; aclanthology.org/2025.lm4uc-1.11) | LM4UC 2025 @ EMNLP workshop | 2025-04 | Synthetic-data pipeline + LoRA on 10 Indic langs (bn, gu, hi, kn, ml, mr, or, pa, ta, te). **Proven LoRA-on-synthetic recipe for Indic.** | DEEPER D3 covers multilingual OCR-aware fine-tuning (arXiv 2605.16409) and PaddleOCR-VL 1.6 GRPO. Nayana OCR (the original LoRA-on-Indic-synthetic precedent) not re-cited. |
| **LightOnOCR-bbox-bench** | Bench artifact | 2026 | Bounding-box localization pretraining + IoU-RLVR. Apache-2.0 (public). | DEEPER covers LightOnOCR-2-1B (the model) but not the bbox-bench artifact specifically. |

**Verdict on K1 (unique sources):** These 8 sources remain valid primary citations but were **out of DEEPER's expansion scope** (either non-OCR or DEEPER chose a more recent/coarser variant). All are reproducible from the URLs cited above.

### K2. Findings in DEEP that were later SUPERSEDED by DEEPER (DEEPER is canonical)

| # | DEEP claim | DEEPER correction (canonical) | DEEPER §ref |
|---|---|---|---|
| 1 | PaddleOCR-VL 1.6 OmniDocBench v1.6 = **96.01** | **96.33** (per arXiv 2606.03264 + HF model card) | §B2 |
| 2 | Laya recommendation = "**LAYA ✅**" (unqualified) | **NEITHER for OCR transcription; BOTH for orchestration System-1 routing.** Laya wins on cost/speed; Jev wins on zero-shot accuracy + high-cardinality. | §B6 + §D1 |
| 3 | "Zero Ol-Chiki script support in any commercial engine" | **CONTRADICTED** — indic-ocr/tessdata (github.com/indic-ocr/tessdata, Apache-2.0) provides trained Tesseract models for sat + mni. Reopens SAT/MNI attack. **LOAD-BEARING correction.** | §B10 + §G #1 |
| 4 | Sarvam 2.1 partial per-lang table: Santali, Kashmiri, Odia, OldScan only | **Full 22-lang + English table** with new datapoints: **Surya OCR 2 = 69.96**, **AWS Textract = 4.64**, Dogri 89.46, Bodo 90.48. | §B1 |
| 5 | Sarvam 2.1 architecture = "harness-with-VLM + pointer reading-order" (vague) | **3B state-space VLM** + (a) semantic layout parser + (b) pointer reading-order network + **SFT followed by RLVR** (full 3-stage post-training). | §B1 + §C1 |
| 6 | Laya "32.8ms p50" (single number) | **32.8ms p50 T4 single / 7.2ms batch-of-10**, plus **Jev = 236-276ms p50** (3rd-party measured). Laya is 7.2-7.8× faster than Jev, not just fast. | §B6 + §D1 |
| 7 | Laya "fine-tuned 0.766 vs Jev 0.727" (winner declared) | Same numbers, **but honest disclosure**: 0.766 requires fine-tuning on the benchmark's own training split; **zero-shot Laya = 0.362** (near-random). | §B6 + §D1 |
| 8 | Gnani Evon "could be a decoder in a hybrid OCR" (speculative) | **NO** — Reason: 30B/3.5B too large for D1 wrap-pipeline; only 10/18 probe langs covered; Apple Silicon not supported. Use only as Stage 3 post-OCR normalizer. | §D2 |
| 9 | Kashmiri attack: "use 600k-ks-ocr + QLoRA" (plan stated, no baseline) | Plan intact, but with **Fayaz et al. 54.91% char-acc baseline** (DEEP K1 above) to compare against. **Opening WIDENS** vs Sarvam 54.82 — a 5-10pt VLM fine-tune improvement is realistic. | DEEP §"How to beat" + DEEPER §K1 above |
| 10 | "Bodhan release date Sep 4 2026" (DEEP implied) | **Sep 12 2026** (The Hindu Business Line news article). **Minor date correction.** | §C2 |
| 11 | Indic OCR Bench size = "6,909 samples (22 langs)" | **6,909 samples (22 8th-Schedule langs + 300 English = 23 langs total)**. Apache-2.0. | DEEPER §B1 (consistent with DEEP) |
| 12 | dots.ocr license not explicitly stated | **MIT** (verified from github.com/rednote-hilab/dots.ocr LICENSE file). Apache 2.0 confusion came from a third-party HF mirror. | §B3 |
| 13 | "use Evon as decoder in 2-tower" speculative path | **Explicit NO** in DEEPER §D2 with 4 reasons (no vision encoder, 30B too big, 10/18 langs, no Apple Silicon). | §D2 |

**Verdict on K2:** All 13 superseded claims have DEEPER-corrected versions. **DEEPER is canonical for every decision.** DEEP's original speculative paths (e.g., Evon-as-decoder) are recorded here for provenance and explicitly closed in DEEPER.

### K3. DEEP-only strategic context preserved

DEEP's original "Strategic implications" sections (the 6 numbered items under "What's new since Aug 2026 PPT" + the adopt/reject table) are **fully consistent with DEEPER**. The adopt/reject calls map cleanly:

| DEEP strategy call | DEEPER equivalent | Status |
|---|---|---|
| **ADOPT LoRA on existing OCR-specialized model** (Chitrapathak 2026) | §E2 #2 — PaddleOCR-VL 1.6 GRPO + dots.ocr | CONFIRMED + EXTENDED |
| **ADOPT Synthetic data + LoRA for low-resource** (Nayana OCR 2025) | §E2 #3 — Indic-OCR Tesseract backstop + Whisper cross-script | CONFIRMED + EXTENDED |
| **ADOPT RLVR with binary unit tests** (olmOCR 2, LightOnOCR-2-1B) | §E2 + D4 — TRL GRPO VLM recipe + mlx-tune | CONFIRMED + EXTENDED |
| **ADOPT Laya as router/gate** (madewithjev.com) | §E2 #1 — Laya as orchestrator System-1 router (NOT OCR) | CONFIRMED + CLARIFIED |
| **ADOPT 600k-ks-ocr for Kashmiri** (arXiv 2601.01088) | §E3 #5 — WATCH only (no downloads without user approval) | **DOWNGRADED to gated** |
| **ADOPT Indic OCR Bench for evaluation** (HF sarvamai) | §B1 — confirmed; specific per-lang pipeline | CONFIRMED |
| **REJECT Train OCR VLM from scratch** | §E3 — REJECT | SURVIVES |
| **REJECT Sarvam/Bodhan/paid APIs in pipeline** | §E3 — REJECT (post-Vinay; target benchmark only) | SURVIVES |
| **REJECT End-to-end LLaVA-style Indic OCR training** | §E3 — REJECT | SURVIVES |
| **REJECT Use Gnani Evon as OCR backbone** | §E3 + §D2 — REJECT | SURVIVES (more explicit reasons in DEEPER) |
| **REJECT Synthetic only, no real-scan test** | §B17 + §E3 — confirmed (real-scan Devanagari test exposes 76-pt gap) | SURVIVES |

### K4. DEEP file provenance

- **Original path:** `docs/research/DEEP_LIVE_RESEARCH.md`
- **Original size:** 29,706 bytes, 469 lines
- **Original mtime:** 2026-09-29 18:25 IST
- **Mission:** 2-hour live deep dive on 7 user URLs + Sarvam weak cells + Gnani + Indic OCR Bench + Laya/Jev + consensus queries
- **Author context:** First agent pass; immediately followed by AGENT-1's LIVE_LATEST_2026-09-29.md (18:27 IST, sealed per campaign §10) and AGENT-8's DEEPER_LIVE_RESEARCH_2026-09-29.md (19:02 IST, this file)
- **Status post-merge:** **SUPERSEDED.** Archived copy retained at `_archive/cleanup_2026-09-30/merge_superseded/DEEP_LIVE_RESEARCH.md` per AGENTS.md archive law.

---

**Merge complete (MERGE-AGENT-1, 2026-09-30).** DEEPER remains the sole canonical live-research file at `docs/research/`. LIVE_LATEST_2026-09-29.md handling is out of scope for this merge (per Exec-1's separate archive task; current ls confirms it still exists at `docs/research/LIVE_LATEST_2026-09-29.md` as of this merge).

---

# APPENDIX A — Pre-merge historical snapshot (from DEEP_LIVE_RESEARCH.md)

**Merged 2026-09-30 by DEDUP-EXEC-AGENT-1.**
**Provenance:** `DEEP_LIVE_RESEARCH.md` was the first-pass 2-hour deep research on the 7 user-provided URLs + 2025-2026 OCR/DocAI literature. This DEEPER file is its successor (second-pass, post-Phase 9, with 18 new evidence records, 7 contradiction resolutions, and the indic-ocr/tessdata load-bearing correction).
**Status:** DEEPER supersedes DEEP. This appendix preserves DEEP verbatim for full provenance; readers should treat DEEPER §A–§J as canonical and DEEP below as the historical first-pass record.

**Merged file archived at:** `_archive/cleanup_2026-09-30/dedup_topic_superseded/DEEP_LIVE_RESEARCH.md` (original deleted after merge).

---

# Deep Live Research — 2026-09-29

**Mission**: Live 2-hour deep dive on (a) the 7 user-provided URLs, (b) the latest
2025-2026 OCR/document-AI research, (c) Sarvam Vision 2.1 vs Sarvam 2.0 weak cells,
(d) Gnani Evon-v3.3-30B-A3B as a potential backend, (e) Indic OCR Bench structure,
(f) Laya vs Jev as a router/classifier, (g) consensus.app queries on three topics.

**Method**: parallel-search MCP `web_fetch` + `web_search` against live sources;
context7 MCP NOT triggered (no library/framework code work in this mission —
pure evidence gathering for Vinay-meeting prep). All findings cite URLs;
uncertainty flagged with `status: UNKNOWN`.

---

## Sources fetched (with timestamps)

| # | URL | Type | When | 1-line summary |
|---|-----|------|------|----------------|
| 1 | https://lnkd.in/p/eFzz2Dtb | LinkedIn post | 2026-09-24 | Sarvam Vision 2.1 launch post; 87.39 Indic / 87.3 olmOCR-Bench; 6,909-sample Indic bench released |
| 2 | https://lnkd.in/p/ewsNXkTs | LinkedIn post (Avinash Benki, Gnani) | 2026-09-25 | Gnani Evon 3.3 announcement: 8-language continued-pretraining + RL trade-offs; "token tax" math |
| 3 | https://www.gnani.ai/ | Homepage | 2026-09-27 | Voice-AI company; ASR/TTS/LLM; 14M hrs telephony; 8/9 langs Kathbath Noisy; SOC2/ISO27001 |
| 4 | https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B | HF model card | — | Apache-2.0, Mamba2-Transformer Hybrid MoE; 30B/3.5B-active; 11 langs (incl. Odia); v3.3 Aug 2026 |
| 5 | https://huggingface.co/datasets/sarvamai/indic-ocr-bench | HF dataset | — | Apache-2.0; 6,909 samples; 23 langs (22 8th-Sch + English); CER/WER; stdlib scorer |
| 6 | https://www.sarvam.ai/blogs/sarvam-vision-2-1 | Sarvam blog | 2026-09-24 | Full architecture, bench tables, per-language weak cells, 22-lang support |
| 7 | https://consensus.app/ | Homepage | — | 250M+ paper search; used 3 consensus-style queries via web_search below |

**Live web_search sessions (parallel)**: 4 batches × 5–10 queries → ~33 distinct
queries; top-5 excerpts per query captured.

---

## Per-source analysis

### 1. Sarvam Vision 2.1 (blog + LinkedIn)

**Architecture** (blog):
- "Harness-with-VLM" paradigm — semantic layout parser + pointer reading-order
  network. NOT a pure end-to-end VLM like PaddleOCR-VL.
- VLM core trained for: OCR, table parsing, multilingual visual reasoning,
  structured outputs.
- Data pipeline: synthetic + real (handwritten/printed forms, multi-page tables).
- Released alongside the model: 6,909-sample Indic OCR Bench.

**Benchmarks** (Sarvam blog, verbatim where possible):
- **olmOCR-Bench (87.3 overall)**:
  - Math 90.5, Base 99.8, Hdr/Ftr 96.3, TinyTxt 92.5, MultCol 82.1, **OldScan 55.3**,
    OldMath 89.7, Tables 91.9
  - Beats Opus 5 (85.1), Chandra-OCR2 (84.5), Mistral OCR4 (83.1)
  - Bodhan Indic-OCR: 78.8 (Math 82.0, OldScan 45.8)
- **OmniDocBench v1.6**: 94.97 (Text 0.0289, Formula 0.988, Table TEDS 0.890,
  Reading-order 0.099). Beats DeepSeek-OCR2 (87.91) and Azure Vision 4.0 (44.95);
  loses to PaddleOCR-VL 1.6 (96.01).
- **Sarvam Indic OCR Bench (22 langs + 300 English)**:
  - Overall accuracy: **87.39** (Sarvam 2.1), 84.94 (Bodhan), 79.35 (Gemini 3.6 Flash),
    71.76 (Google Cloud Vision), 69.96 (Surya OCR 2), 69.16 (Mistral OCR4),
    68.81 (Opus 5), 65.53 (Gemma 4), 64.56 (Chandra-OCR2), 63.69 (GPT 6 Astra),
    49.83 (Infinity-Parser2 Pro), 41.29 (Azure Vision 4.0), 4.64 (AWS Textract).

**Weak cells** (per-language accuracy on Sarvam Indic OCR Bench — selected):
| Language | Sarvam 2.1 | Bodhan | Gemini 3.6 Flash | Surya OCR 2 | Chandra-OCR2 | GPT 6 Astra |
|---|---|---|---|---|---|---|
| **Santali** | 53.91 | status: UNKNOWN (below fold in excerpt) | — | — | — | — |
| **Kashmiri** | 54.82 | status: UNKNOWN | — | — | — | — |
| **Odia** | 80.01 | 75.45 | 81.01 | 69.34 | 68.09 | 69.74 |
| **OldScan (English)** | 55.3 (olmOCR) | 45.8 (olmOCR) | — | — | 49.2 | — |

**Confirmed weak cells (verbatim from blog excerpt)**:
- Santali 53.91 ✅
- Kashmiri 54.82 ✅
- OldScan 55.3 (olmOCR) ✅
- Odia 80.01 ✅ (note: Gemini beats Sarvam on Odia 81.01 > 80.01 — opening)

**How to beat** (tactics, derived):
1. **Santali (Ol Chiki script)** — Sarvam scores 53.91. Zero Ol-Chiki script
   support in any commercial engine we've seen. Open via: synthetic Ol-Chiki
   data (R3_OLCHIKI_MAYEK_SYNTHETIC.md), then QLoRA on a 0.5B–1B OCR VLM.
2. **Kashmiri (Nastaliq)** — Sarvam 54.82. We have R2_NASTALIQ_FORENSICS.md;
   also the **600k-ks-ocr dataset (CC-BY-4.0, 602K word images)** released
   2026-01-03 (arXiv 2601.01088) gives us free specialist data.
3. **OldScan (historical)** — Sarvam 55.3. R4_OLDSCAN_RESTORATION.md already
   maps this. Use DocEnRestore (image) + Surya layout → SFT Qwen3-VL-8B on
   degraded patches.
4. **Odia** — Sarvam 80.01 < Gemini 81.01. Margin is tiny. A 1.5–3 point
   improvement on Odia would close the gap. Use the **Gnani Evon-v3.3**
   Odia pretraining (66.94 MILU) as a decoder backbone.

**Verdict per finding (Sarvam 2.1)**:
- "87.39 on 6,909-block Indic bench" → SURVIVES (blog, dated 2026-09-24).
- "weak cells match probe22 disk truth" → SURVIVES (sat 53.91, ks 54.82,
  OldScan 55.3, or 80.01 — all match).
- "harness + pointer reading-order is proprietary" → SURVIVES (specific to Sarvam
  family; we should NOT clone it but should adopt the *idea* of explicit
  layout-parser + reading-order-pointer split).

### 2. Gnani Evon-v3.3-30B-A3B (model card + LinkedIn)

**Architecture** (HF model card, verbatim):
- Mamba2-Transformer Hybrid Mixture of Experts (MoE)
- Network arch: `nemotron_h` (Nemotron hybrid)
- **30B total / ~3.5B active per token**
- Context: 131,072 tokens (128K)
- Precision: BF16
- License: **Apache-2.0** ✅ (open weights)
- Release: August 2026

**Training (3 stages)**:
1. Continued pretraining on blended English + Indic corpus
2. SFT on instruction + capability-focused (QA/summarization/safety/multi-turn
   dialogue in native scripts)
3. GRPO RL on Indic-heavy prompts

**Training infra**: H200 GPU clusters, NVIDIA NeMo (Curator + Megatron Bridge + NeMo RL).

**Indic language coverage** (explicit):
> English, Hindi, Bengali, Telugu, Tamil, Marathi, Gujarati, Kannada,
> Malayalam, **Odia**, Punjabi. **(11 langs)**

> ⚠️ **NO Santali, NO Kashmiri, NO Meitei, NO Sindhi, NO Dogri, NO Bodo, NO
> Assamese** in the 11-lang coverage. Evon is a South-Indic / Hindi-belt + Odia
> model. It does NOT cover our weakest cells' scripts (Ol Chiki, Nastaliq).

**Benchmarks (MILU, 11 langs macro mean)**:
- **gnani-evon-v3.3: 78.74** (beats Sarvam-30B 67.15 and Sarvam-105B 75.71 on 10/11 langs)
- Odia specifically: 66.94 (Sarvam-30B 65.83, Sarvam-105B 73.70)
- Hindi 81.99, Telugu 79.78, Bengali 82.30, Tamil 78.12, Malayalam 77.00
- ALSO: xquad_in F1 64.59 (beats Sarvams), xorqa_in F1 41.83

**Gnani AI company context (homepage)**:
- Voice-AI company, NOT a vision company. ASR/TTS/voice-agents are core.
- LLM is *one* of their products.
- 14M hrs telephony data, 30M+ daily voice interactions.
- SOC 2, ISO 27001, GDPR, HIPAA, PCI-DSS compliant.
- 40+ language ASR; 21+ language TTS.

**OCR capability**: ❌ **None stated**. Evon is a text-only chat model
(pipeline_tag = text-generation). No vision encoder, no OCR claims.
It could in principle serve as the *text decoder* of a two-tower
OCR system (vision encoder → Evon decoder), but Evon has NOT been trained
on image inputs per its HF card.

**Comparison to our needs**:
| Need | Evon verdict |
|---|---|
| OCR on Indic print | ❌ No vision encoder; not an OCR model |
| Decoder for OCR VLM (Qwen3-VL + Evon hybrid) | ⚠️ Possible (3.5B-active MoE decoder) but no public OCR fine-tunes |
| Sanskrit/Hindi/Odia language modeling | ✅ MILU 81.99 / 66.94 / strong |
| Santali/Kashmiri script support | ❌ NOT in 11-lang coverage |
| Open-weight, fine-tune-able | ✅ Apache-2.0 |
| Long context (128K) | ✅ Yes (useful for full-page context) |
| Tokenizer efficiency | ✅ 2.18 tok/word (vs OpenAI ~3.1, Gemini ~2.7) |

**Verdict per finding (Gnani Evon)**:
- "Apache-2.0 open weights" → SURVIVES (HF model card).
- "30B/3.5B MoE, 128K ctx, 11 Indic langs" → SURVIVES.
- "OCR capability" → DIES (no vision encoder, no OCR claims; not applicable).
- "Could we use Evon as a decoder in a hybrid OCR stack?" → UNKNOWN (no public
  precedent for Qwen3-VL-8B vision + Evon-decoder; would need to write our own
  projector). NOT recommended for W6 — too speculative.
- "Replace Sarvam 2.1 as a target to beat?" → NO. Evon is *text*, not *vision*;
  Sarvam 2.1 is *vision-text*. Apples to oranges.

### 3. Indic OCR Bench (HF dataset card)

**Structure**:
- **6,909 total samples** (test split) — 6,609 across 22 Indian languages +
  300 in English. (Sarvam blog says 22 langs, dataset card says "23 languages
  = 22 + English".) ✅
- A `small_representative` split: 1,173 samples (~51 per language, stratified by word length).
- **Block-level** (not page-level): "samples are curated at the **semantic block
  level** so that models are evaluated on coherent units of text rather than
  full noisy pages."
- Sources: newspapers, brochures, textbooks, historical writings; **dated 1800
  to present day**.
- License: **Apache-2.0** ✅
- Ground truth: **reviewed twice by human language experts**.

**Fields per record**: image, ground-truth text, language tag.
**Evaluation**: **CER** + **WER** (with content normalization: NFC, whitespace,
quote/dash unification, Indic punctuation, strip HTML/quotes/asterisks/ZWJ,
caps at 1.0 per sample).
**Scorer**: `metrics.py` stdlib-only in the repo, can be used standalone.
**Word accuracy**: `100 × (1 − WER)`.

**How to use for our eval** (tactics):
1. Download (Apache-2.0, free). 
2. Run any OCR model on `small_representative` first (1,173 samples ≈ 51/lang)
   to see per-language gap. Then run full 6,909 for final numbers.
3. We need a per-language block-level pipeline: layout parser → per-block
   image → OCR → CER/WER.
4. Compare against the published Sarvam 2.1 / Bodhan / Gemini 3.6 Flash table.
   **Our SOUTH plan**: reproduce the per-language table; the languages where we
   can BEAT Sarvam 2.1 are our openings.

**Verdict per finding (Indic OCR Bench)**:
- "6,909 blocks, 22 langs + English, Apache-2.0" → SURVIVES.
- "Reviewed twice by human experts" → SURVIVES (high-quality GT).
- "Stratified by word length" → SURVIVES (good for `small_representative`
  sanity check).
- "Scoring is CER + WER with normalization" → SURVIVES; this is what we should
  also use for our own internal bench to enable apples-to-apples with Sarvam.

### 4. Laya vs Jev (decision classifier)

**Laya** (madewithjev.com + jevmodel.org + GitHub DDnim):
- **Open-source**, Apache-2.0, installable with `pip install laya`.
- 13.7k GitHub stars (as of 2026-09-22).
- Three checkpoints: **421M English** (ModernBERT-large), **322M multilingual**
  (mmBERT-base, 100+ langs), 421M typed-decisions.
- Router dispatches by script in <0.5ms.
- **Latency**: 32.8 ms / question on T4; 7.2 ms in batches of 10.
- **Cost**: ~$0.0029 per 1,000 decisions in compute (JevBench estimate).
- Calibration: probabilities trained against strictly proper scoring rules.
  Branch on confidence at 0.85 threshold.
- Three typed primitives: **choice, score, noul**.
- **Lost battles**: Banking77 (77 labels, head budget 192/256 tokens, accuracy
  0.425 vs Jev 0.870); Khmer (0.000 accuracy at 0.952 confidence — confidently
  wrong on out-of-distribution scripts).

**Jev** (TypeSafe AI):
- **Closed proprietary API** (TypeSafe System One model).
- 1.13.0; JevBench v1.3.0 (Sept 22, 2026) — claims rank #1.
- **74.4 answers on day one** with no labelled data and no training run.
- **64k tokens per request** (vs Laya 512).
- Higher cost than Laya but managed.

**Per user's quote**:
> "if laya is almost better and free so laya is better than jev"

**Live evidence confirms**:
- Laya is **free** (Apache-2.0, self-host).
- Jev is **paid** (closed API).
- Laya is **multilingual** (100+ langs mmBERT-base checkpoint).
- Jev is **English-strong, multilingual less reliable** (per Jev vs Laya FAQ).
- Laya is **fast** (32.8ms T4, 7.2ms batched).
- Jev has longer context (64k vs 512).

**Recommendation: LAYA** ✅
- Reasoning: free + open + multilingual + faster + router dispatch. The user
  already chose Laya; live research confirms it. Caveats: needs fine-tuning
  for our specific labels; not reliable on out-of-distribution scripts (Khmer
  example — flag our Santali/Nastaliq as OOD until we calibrate).

**Where Laya could plug in** (specific to our pipeline):
1. Script-classifier: dispatch each block to "Indic-print / Ol-Chiki / Nastaliq
   / Latin" before OCR.
2. Confidence-gate: only run heavy OCR (e.g., Qwen3-VL-8B) when Laya's P(true)
   < 0.85.
3. Layout-block-type classifier: text/table/formula/figure.

### 5. Latest papers (2025-2026) — OCR / Document AI

| Title | Authors | Date | URL | Method | Benchmark / License | Relevance to South |
|---|---|---|---|---|---|---|
| **PaddleOCR-VL** | Cui et al. (Baidu) | 2025-10-16 (v4 2025-11-25) | arXiv:2510.14528 | NaViT dynamic-res vision encoder + ERNIE-4.5-0.3B decoder, 0.9B total; LLaVA-style; 109 langs incl. Hindi | Apache-2.0; OmniDocBench SOTA | ★★★★ — open weights, supports Hindi, beats Sarvam on OmniDocBench |
| **PaddleOCR-VL-1.6** | Zhang et al. (Baidu) | 2026-06-02 | arXiv:2606.03264 | Region-aware data optimization + progressive post-training + RL | 96.33% OmniDocBench v1.6 (new SOTA) | ★★★★ — newer checkpoint; same Apache-2.0 |
| **olmOCR 2** (Unit Test Rewards) | Poznanski, Soldaini, Lo | 2025-10-22 | arXiv:2510.19817 | 7B VLM, SFT → RLVR with binary unit tests (text presence, position, format) | olmOCR-Bench SOTA; permissive open | ★★★ — RLVR technique directly applicable |
| **LightOnOCR-2-1B** | Taghadouini et al. (LightOn) | 2026-01-20 (v2 2026-06-30) | arXiv:2601.14251v2 | Mistral-Small-3.1 vision + Qwen3 + 2-layer MLP; SFT → GRPO RLVR; checkpoint averaging + task-arithmetic merge | olmOCR-Bench SOTA at 1B (9× smaller than priors); Apache-2.0 | ★★★★★ — perfect template for our W6: small, open, RLVR-trained |
| **LightOnOCR-bbox-bench** | same | 2026 | (linked from arxiv) | Bounding-box localization pretraining + IoU-RLVR | Apache-2.0 (public) | ★★★ — could extend our eval to bboxes |
| **dots.ocr / dots.mocr** | Li et al. (rednote-hilab / Xiaohongshu) | 2025-10-31 → 2026-03-19 | arXiv:2512.02498 | 1.2B vision + 1.7B LLM; single VLM, layout+text+reading-order; Qwen2.5-VL-7B distil; **126 langs** | XDocParse SOTA (+7.4 over next-best) | ★★★★ — multilingual, open weights |
| **MonkeyOCR / MonkeyOCR-pro-3B** | Yuliang Liu (HUST) | 2025-06-05 → 2026-07-14 | arXiv:2506.05218 + GitHub | Structure-Recognition-Relation (SRR) triplet paradigm | Open weights, English+Chinese | ★★★ — SRR idea similar to Sarvam's "harness + pointer reading-order" |
| **GLM-OCR (Zhipu/THUDM)** | listed in CodeSOTA registry | 2026-04 | codesota.com | Open weights, self-host; en+CJK strong | Open | ★★ — Chinese-first, less Indic |
| **Chandra-OCR / Chandra-OCR2** | (Paruchuri / Nanonets) | 2025-2026 | HF + arXiv | OCR-specialized VLM | Open weights | ★★★ — Chandra-OCR2 is in Sarvam's competitive table (84.5 olmOCR) |
| **Multilingual OCR-Aware Fine-Tuning** | Xu, Jiang, Ren | 2026-05-13 | arXiv:2605.16409 | 5M synthetic multilingual OCR samples + LoRA SFT + visual-CoT prompt; OCR completeness 71.3 → 84.6 | CC-BY-NC-ND 4.0 | ★★★★ — exact W6 recipe template |
| **Designing Production-Scale OCR for India: Chitrapathak** | (Krutrim AI / Ola Electric) | 2026 | arXiv:2602.16430 | Compares (a) LLaVA-style end-to-end vs (b) fine-tune OCR-specialized; (b) wins accuracy-latency | — | ★★★★★ — directly relevant: "fine-tune existing OCR > train from scratch" |
| **Nayana OCR (low-resource Indic)** | Kolavi, P, Jain (CognitiveLab) | 2025-04 | aclanthology.org/2025.lm4uc-1.11 | Synthetic-data pipeline + LoRA on 10 Indic langs (incl. Odia) | — | ★★★ — proven LoRA-on-synthetic for Indic |
| **Impact of Iterative Fine-Tuning on Historical Sanskrit Manuscripts** | (FLAME-CAI) | 2026-08-19 | arXiv:2608.18696 | GNN + CNN-BiLSTM-CTC iterative fine-tuning on Sanskrit historical MSS; benchmarks Sarvam Vision | — | ★★★ — direct comparison to Sarvam on old-script |
| **Can OCR-VLMs Read Devanagari?** | Singh | 2026-06-28 | arXiv:2606.29213 | Stress-test: 10 systems on Hindi; finds: (a) clean renders don't separate, (b) DeepSeek-OCR has catastrophic repetitions, (c) **real scans: field collapses 76-point range**, (d) GPT-5.5 chrF++ 58.5 ≈ EasyOCR; olmOCR-7B chrF++ 40.5; **Qwen3-VL-8B beats GPT-5.5** | — | ★★★★★ — confirms our hypothesis: synthetic benchmarks lie, real scans expose gaps |
| **600k-ks-ocr (Kashmiri)** | Malik | 2026-01-03 | arXiv:2601.01088 | 602K word-level synthetic Kashmiri images, 3 traditional typefaces, 10.6 GB | CC-BY-4.0 | ★★★★★ — direct training data for our Kashmiri weak cell |
| **Kashmiri Nastaliq OCR baseline** | Fayaz et al. | 2026-03-26 | library.acadlore.com/ATAIML | Kraken OCR + transfer-learning from Arabic baseline; char-acc 54.91% Model-1, word-acc 4.65% | — | ★★★ — baseline to beat on Kashmiri |
| **Printed OCR for Extremely Low-resource Indic Languages** (IIIT-H) | (IIIT Hyderabad) | 2024-10-04 | cvit.iiit.ac.in | Ol Chiki Santali: CRR 90.60, WRR 96.58 on Mozhi-LR(S); Kashmiri: CRR 87.71, WRR 93.80 (pre-trained Hindi + AdaDelta) | — | ★★★★★ — direct Ol-Chiki Santali baseline + Kashmiri baseline |
| **IndicVisionBench (Krutrim / Ola Electric)** | Faraz, Akash, Khan et al. | 2026-04-21 (ICLR 2026) | iclr.cc media | OCR: 876 doc images across 10 Indic scripts from Wikisource | ICLR 2026 | ★★★ — published Indic bench (smaller than Sarvam's 6,909) |
| **Modeling Layout Reading Order as Ordering Relations** | (EMNLP 2024) | 2024 | aclanthology.org/2024.emnlp-main.540 | Reading-Order-Prediction (ROP) as relation extraction with global pointer network | — | ★★★ — same architecture as Sarvam's pointer reading-order |
| **IndicGenBench** | Singh et al. (IIT Bangalore) | 2024-04-25 | arXiv:2404.16816 | Multilingual generation eval, 29 Indic langs | — | ★★ — generation-focused, not OCR |
| **AncientDoc (Chinese ancient docs)** | Yu et al. | 2026 | aclanthology.org/2026.findings-acl.1438 | 5 tasks on Chinese ancient (similar to OldScan problem) | — | ★★ — analog of OldScan for Chinese |
| **DoPTA (Layout Analysis)** | (2025-03-09) | 2025-03-09 | alphaxiv.org/abs/2412.12902 | Patch-Text Alignment for layout; DocLayout-YOLO follow-up | — | ★★ — layout-only |
| **DELAB-IIITM WMT26 (English→Meitei Mayek, Bodo)** | (WMT 2026) | 2026-09-08 | statmt.org/wmt26/pdf/2026.wmt-1.159 | LoRA on IndicTrans2 for Meitei + Bodo | — | ★★ — proves LoRA on IndicTrans2 works for Meitei/Bodo |

### 6. Consensus-style academic findings (3 queries)

**Q1: "multilingual Indic OCR vision language model fine-tuning"**
- **Xu, Jiang, Ren 2026** (arXiv:2605.16409): 5M synthetic OCR + LoRA SFT +
  visual-CoT prompt → OCR completeness 71.3 → 84.6. **Method: data-centric
  + LoRA on existing MLLM.**
- **Krutrim Chitrapathak 2026** (arXiv:2602.16430): explicit comparison —
  "fine-tune existing OCR-specialized model" beats "train end-to-end
  LLaVA-style." **Conclusion: don't reinvent the backbone; QLoRA an existing
  SOTA.**
- **Nayana OCR 2025** (aclanthology:2025.lm4uc-1.11): synthetic-data pipeline
  + LoRA on 10 Indic langs (Bengali, Gujarati, Hindi, Kannada, Malayalam,
  Marathi, Odia, Punjabi, Tamil, Telugu). **Precedent for synthetic-data +
  LoRA on Indic.**
- **Singh 2026** (arXiv:2606.29213): real-scan Devanagari chrF++ 40.5 for
  olmOCR-7B vs 75.2 for Qwen3-VL-8B. **Conclusion: Qwen3-VL family is the
  open baseline that beats GPT-5.5 on Indic.**

**Q2: "layout reading order document AI 2026"**
- **Sarvam Vision 2.1** (2026-09-24): "semantic layout parser + pointer
  reading-order network" — proprietary but documented.
- **dots.ocr** (arXiv:2512.02498, 2025-12): single VLM, layout + text +
  reading-order in one model. **+7.4 over next-best on XDocParse.**
- **MonkeyOCR-SRR** (arXiv:2506.05218, 2025-06): Structure-Recognition-Relation
  triplet paradigm. 3B beats Qwen2.5-VL-72B on English doc parsing.
- **ROP as Relation Extraction** (EMNLP 2024, aclanthology:2024.emnlp-main.540):
  global pointer network for reading-order-prediction (ROP). **Same idea as
  Sarvam's pointer reading-order.**
- **LayoutLMv3 / DocLayout-YOLO** (legacy 2022-2024, still cited): predecessors.

**Q3: "Santali Kashmiri Meitei OCR specialist model"**
- **IIIT-H Printed OCR for Low-resource Indic** (2024-10): Ol Chiki Santali
  CRR 90.60; Kashmiri CRR 87.71; trained on Mozhi-LR(S) + Mozhi-LR(R).
- **600k-ks-ocr** (arXiv:2601.01088, 2026-01): 602K Kashmiri word images,
  CC-BY-4.0. **Direct training data, free.**
- **Kashmiri Nastaliq baseline** (Fayaz et al. 2026): Kraken + Arabic
  transfer-learning; char-acc 54.91%, word-acc 4.65%. **Baseline to beat.**
- **DELAB-IIITM WMT26** (2026-09): LoRA on IndicTrans2 for Meitei (Meitei Mayek
  script) + Bodo. **Precedent: LoRA works for Meitei.**
- **ByT5 / IndicTrans2** for English-Santali (Singh, Ekbal, Pakray 2025-12):
  IndicTrans2 fine-tune achieves 26.8 BLEU / 53.9 chrF++ for Santali→English.
  **Precedent: IndicTrans2 fine-tunes well for Santali.** ⚠️ This is MT, not
  OCR — but the *script support* is proven.

---

## Strategic implications

### What's new since Aug 2026 PPT
1. **Sarvam 2.1 (Sep 24) is a credible threat**: 87.39 on the only public Indic
   bench; multilingual (22 8th-Schedule langs + English); handwriting support;
   table parsing; 0.099 reading-order edit-dist (better than GPT 6 Astra 0.098).
2. **Gnani Evon 3.3 (Aug 2026)** is an open-weight **text-only** MoE; not an
   OCR model. Could be a *decoder* in a two-tower OCR but no public precedent.
3. **PaddleOCR-VL 1.6 (Jun 2026)**: 96.33% OmniDocBench — open weights,
   Apache-2.0, 109 langs incl. Hindi. **A real baseline to compare against.**
4. **LightOnOCR-2-1B (Jun 2026)**: 1B, Apache-2.0, GRPO RLVR — **the closest
   recipe template for our W6**.
5. **dots.ocr (Mar 2026 → dots.mocr)**: single VLM, layout+text+reading-order
   in one model, 126 langs — open weights.
6. **MonkeyOCRv2 (Jul 2026)**: SRR triplet paradigm.
7. **600k-ks-ocr (Jan 2026)**: free CC-BY-4.0 Kashmiri OCR data — **we should
   add this to our training set.**
8. **Can OCR-VLMs Read Devanagari?** (Jun 2026): real scans expose gaps that
   synthetic benchmarks hide. **Confirms we should test on real scans, not
   only on the 6,909-block Indic OCR Bench.**

### Which methods we should adopt
| Method | Source | Apply to South |
|---|---|---|
| **LoRA on existing OCR-specialized model (Qwen3-VL-8B / LightOnOCR-2-1B)** | Chitrapathak 2026 (Krutrim) | W6 main path: QLoRA Qwen3-VL-8B or LightOnOCR-2-1B on our 4 weak cells |
| **Synthetic data + LoRA for low-resource** | Nayana OCR 2025 | W6: synthetic Ol Chiki + synthetic Kashmiri-Nastaliq for sat/ks |
| **RLVR with binary unit tests** | olmOCR 2 2025, LightOnOCR-2-1B | W6.5 if we have time: GRPO on unit-test rewards for CER ↓ |
| **Laya as router/gate** | madewithjev.com | W6 router layer: script-classify + confidence-gate at P<0.85 |
| **600k-ks-ocr (CC-BY-4.0) for Kashmiri** | arXiv:2601.01088 | W6 training data, free |
| **Indic OCR Bench (Apache-2.0) for evaluation** | HF sarvamai | W6 eval: `small_representative` (1,173) first, full 6,909 for final |

### Which methods we should reject
| Method | Source | Reject reason |
|---|---|---|
| Train an OCR VLM from scratch | L7 ("no novel backbone") | L7 hard rule |
| Use Sarvam/Bodhan/paid APIs in pipeline | L3 ("LEVEL 3 LOCKED OUT") | Not allowed in W6 (post-Vinay) |
| End-to-end LLaVA-style Indic OCR training | Chitrapathak 2026 finding | Krutrim explicitly says this is *worse* than fine-tuning |
| Use Gnani Evon as OCR backbone | L7 + Evon is text-only | No vision encoder; not an OCR model |
| Synthetic only, no real-scan test | Singh 2026 Devanagari paper | Synthetic overstates quality; real scans collapse 76-pt range |

### Weak-cell attack updates

**Santali (53.91 — Sarvam 2.1; our weakest)**:
- Plan: synthetic Ol Chiki (R3_OLCHIKI_MAYEK_SYNTHETIC.md) + QLoRA Qwen3-VL-8B
  → expected 65–75.
- New evidence: IIIT-H 2024 baseline CRR 90.60 on Mozhi-LR(S) Santali
  *printed*. IndicTrans2 fine-tune works for Ol Chiki script (Singh et al.
  2025-12). Open path: copy IIIT-H recipe but in VLM.
- **Status: open path SURVIVES.**

**Kashmiri (54.82 — Sarvam 2.1; Nastaliq)**:
- Plan: R2_NASTALIQ_FORENSICS.md + 600k-ks-ocr (free, CC-BY-4.0) + QLoRA.
- New evidence: Fayaz et al. 2026 Kraken+Arabic-transfer baseline char-acc
  54.91% (matches Sarvam 2.1!). We can beat this with a VLM fine-tune.
- **Status: opening WIDENS.**

**OldScan (55.3 — olmOCR-Bench subset)**:
- Plan: R4_OLDSCAN_RESTORATION.md + DocEnRestore → SFT Qwen3-VL-8B on degraded patches.
- New evidence: LightOnOCR-2-1B achieves SOTA on olmOCR-Bench at 1B (9× smaller
  than competitors). Confirms small + RLVR is the right shape.
- **Status: opening SURVIVES.**

**Odia (80.01 — Sarvam 2.1)**:
- Plan: Gnani Evon has Odia in 11-lang coverage (MILU 66.94). Use Evon
  *language-model prior* for Odia post-correction.
- New evidence: PaddleOCR-VL 1.6 / dots.ocr / LightOnOCR-2-1B all open-weight
  with Hindi coverage (Odia not explicitly tested but Indic-script-adjacent).
  Sarvam 80.01 < Gemini 81.01 — only **1% opening**.
- **Status: thin opening; unlikely to beat Sarvam by >5 points.**

### Laya vs Jev decision (per user quote: "if laya is almost better and free so laya is better than jev")

**Recommendation: LAYA** ✅
- Confirmed by live research:
  - Free (Apache-2.0), self-host, 32.8ms T4 latency
  - Multilingual (100+ langs) — fits our Indic scope
  - Router dispatches by script in <0.5ms
  - Branch on P(true) < 0.85 → escalate (Laya gate = confidence gate)
- Caveats to record:
  - Head budget 512 tokens / 192 English / 256 multilingual → not for long
    docs (we need block-level not page-level classification)
  - Out-of-distribution scripts get confidently wrong (Khmer 0.000 @ 0.952
    confidence) → **must calibrate on our 4 weak cells before relying**
  - Needs task-specific fine-tuning to overcome base overconfidence
- Use case: **router layer** in W6 pipeline:
  - Laya classifies each block: language/script, block-type (text/table/figure),
    confidence score
  - If P < 0.85, send to Qwen3-VL-8B or Surya
  - If P ≥ 0.85, use lightweight Surya OCR

### Citations (full URL list)

**User-provided URLs (7)**:
1. https://lnkd.in/p/eFzz2Dtb
2. https://lnkd.in/p/ewsNXkTs
3. https://www.gnani.ai/
4. https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B
5. https://huggingface.co/datasets/sarvamai/indic-ocr-bench
6. https://www.sarvam.ai/blogs/sarvam-vision-2-1
7. https://consensus.app/

**Papers / models surfaced by live search**:
8. arXiv:2510.14528 — PaddleOCR-VL
9. arXiv:2606.03264 — PaddleOCR-VL-1.6
10. arXiv:2510.19817 — olmOCR 2
11. arXiv:2601.14251v2 — LightOnOCR-2-1B
12. arXiv:2512.02498 — dots.ocr
13. arXiv:2506.05218 — MonkeyOCR
14. arXiv:2605.16409 — Multilingual OCR-Aware Fine-Tuning + CoT
15. arXiv:2602.16430 — Chitrapathak / Krutrim Production-Scale OCR for India
16. arXiv:2606.29213 — Can OCR-VLMs Read Devanagari?
17. arXiv:2601.01088 — 600k-ks-ocr (Kashmiri)
18. arXiv:2608.18696 — Iterative Fine-Tuning Historical Sanskrit MSS
19. aclanthology.org/2025.lm4uc-1.11 — Nayana OCR
20. aclanthology.org/2024.emnlp-main.540 — Modeling Layout Reading Order
21. aclanthology.org/2025.mmloso-1.9 — IndicTrans2 + ByT5 for English-Santali
22. library.acadlore.com/ATAIML/2026/5/2/ATAIML_05.02_03.pdf — Kashmiri Nastaliq baseline
23. cvit.iiit.ac.in/.../Printed-OCR-for-Extremely-Low-resource-Indic-Languages.pdf — IIIT-H Ol Chiki + Kashmiri
24. iclr.cc/media/iclr-2026/Slides/10010008.pdf — IndicVisionBench (Krutrim)
25. arXiv:2606.29213 — Devanagari OCR-VLM stress test
26. arXiv:2404.16816 — IndicGenBench
27. arXiv:2601.14251v1 — LightOnOCR-1B
28. github.com/rednote-hilab/dots.ocr — dots.ocr GitHub
29. github.com/Yuliang-Liu/MonkeyOCRv2 — MonkeyOCRv2 GitHub
30. huggingface.co/PaddlePaddle/PaddleOCR-VL — PaddleOCR-VL HF
31. madewithjev.com/builds/laya — Laya spec page
32. jevmodel.org/jev-vs-laya/ — Jev vs Laya comparison
33. thejevai.com/jev-vs-laya — Jev vs Laya alternate source
34. github.com/DDnim/jev-vs-laya — Jev vs Laya SQL-review benchmark
35. huggingface.co/blog/sora-2/jev-vs-laya-hosted-api-or-open-weights-2026-guide — Jev vs Laya 2026 guide
36. hermes-ai.net/news/open-source-laya-beats-closed-jev-api-at-7x-faster-decision-speed
37. regolo.ai/jev-and-system-one-models-benchmarks-open-source-alternatives-and-when-to-use-them/
38. huggingface.co/blog/dddffgassa/what-jev-terms-of-use-jev-playground-and-laya-ai-v
39. codesota.com/tasks/document-ocr — OCR & Document Parsing APIs 2026
40. codesota.com/ocr/benchmark/omnidocbench — OmniDocBench leaderboard
41. github.com/PaddlePaddle/PaddleOCR/blob/main/docs/index/index.en.md — PaddleOCR docs

---

## Token spend (this turn)

- **In**: ~14,800 tokens (1 batched web_fetch ×7 URLs + 4 batched web_search
  ×5–10 queries + 1 follow-up web_fetch + supporting ls/cat).
- **Out**: ~9,400 tokens (DEEP_LIVE_RESEARCH.md write + §18 append + REPORT
  block).
- **Total**: ~24,200 tokens.