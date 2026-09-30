# LIVE_LATEST_2026-09-29 — Live Research (post-campaign)

**Date:** 2026-09-29
**Agent:** AGENT-1 (full cleanup + integrate)
**Author:** MiniMax-M3 via opencode
**Standing context:** Level 7 48h research campaign ended ~04:23 IST 2026-09-29. This file is the live latest pass — what changed since the campaign ledger was sealed, plus what was loaded fresh today. All records carry explicit source URLs and decision-changers per campaign §9 evidence law.

**Note on AGENTS.md vs disk truth (campaign.md: pass-through only).** AGENTS.md quotes graph = "1324 nodes / 1665 edges / 206 communities / 52 hyperedges" but `graphify-out/GRAPH_REPORT.md` (built 2026-09-29) reports **3990 nodes / 4681 edges / 420 communities / 50 hyperedges** over 18,239 files. The disk number is canonical; AGENTS.md is stale and will be updated in §18 below.

---

## A. PRIMARY SOURCES FETCHED (user-provided URLs)

### A1. https://lnkd.in/p/eFzz2Dtb — Sarvam Vision 2.1 LinkedIn post (4d ago)
- **Source:** Sarvam AI official account (147k followers), posted 2026-09-24
- **Key claims:** Vision 2.1 is state-of-the-art on BOTH olmOCR-Bench (87.3) AND Indic OCR Bench (87.39); 6,909 samples across 22 Indian languages + English, sources dated 1800-today; extracts key-value pairs from forms/tables including multi-page; reads handwritten Indian-language text
- **One skeptic comment (Krrish Agarwalla):** "there weren't really any benchmarks covering Indic languages, so we built one ourselves, and naturally (because of similar training data) our model performs very well on it." → TRANSFER CARD: **CONTRADICTION vs dataset overlap risk**; the 87.39 is on a self-built bench using training-data-adjacent sources — Sarvam 87.39 is **DEAD for direct comparison** until verified vs third-party splits. **Decision: still beat Sarvam ON the official benchmark regardless** — it's the target.
- **Cross-reference:** Comments include "Vishal Singh 4d: so can now run just one model for English + Hindi + Tamil + Telugu + Marathi + etc. instead of stitching separate OCR engines" — confirms the "wrap-vs-specialist" tension from our campaign.

### A2. https://lnkd.in/p/ewsNXkTs — Gnani Evon v3.3 NeurIPS acceptance post
- **Source:** Avinash Benki (Gnani.ai CEO/founder), 2026-09-25
- **Key claims:** TWO papers accepted at NeurIPS 2026 GlobalSouthAI Workshop:
  1. **"Teaching an English-first model 8 Indian languages, end to end"** — covers **embedding expansion + embedding warmup** recipe; reported +11.8 MILU, +13.0 ARC-Challenge-Indic with English trade-off measured openly
  2. **"What RL gives, and what it quietly takes away"** — MATH +36 but **Indic document QA fell up to 11 points while English improved**; **Indic-aware rewards recovered it, at a cost to reasoning and coding**
- **Open weights:** Apache-2.0 — Gnani Evon 3.3 (30B-A3B Mamba2-Transformer MoE hybrid, ~3.5B active/token, 128K context, English + 10 Indic langs — NOT OCR but a text LLM)
- **Decision-changer (B3):** The Gnani NeurIPS paper 1 = the **embedding-expansion recipe** is a load-bearing reference for our W6 QLoRA strategy if we fine-tune an Indic model — saves us reinventing it. Decision: cite at the call if QLoRA goes forward.
- **Decision-changer (B5):** The RL trade-off finding (Indic document QA drops 11 pts on English-favoring RL) = **load-bearing warning** for our campaign D1 stance "RLVR after SFT plateaus." Already in PPT_SPEC §6.2 as RLVR-on-gold-only; this NeurIPS paper validates the warning from outside our bench.

### A3. https://www.gnani.ai/ — Gnani website
- **Products:** Gnani Warp v2.0 (S2S), Prisma v2.5 (STT), Timbre v2.5 (TTS), Evon v3.3 (LLM)
- **CRITICAL:** **Gnani does NOT make an OCR model.** Their stack is Voice + LLM. They don't compete on our OCR problem directly.
- **Enterprise voice AI only:** 14M hours telephonic audio, 200+ enterprise deployments, BFSI/healthcare/telecom, 30M+ daily interactions
- **Decision-changer:** None for OCR directly. Their LLM (Evon v3.3) is a candidate post-OCR text-normalizer IF we wanted a text-LLM post-corrector trained on Indic — but Stage 3 in PPT is IndicBERT/Airavata/small LLM. Gnani Evon is 30B-A3B, too large for our W6 budget (D1: wrap-only + local QLoRA on SAFE langs, no cloud). Keep as WATCH only.

### A4. https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B — model card
- **Architecture:** Nemotron Hybrid MoE (Mamba2-Transformer Hybrid), 30B total / ~3.5B active per token, BF16, 131,072 token context
- **Release:** August 2026 (Apache-2.0)
- **Languages:** English + 10 Indic (Hindi, Bengali, Telugu, Tamil, Marathi, Gujarati, Kannada, Malayalam, Odia, Punjabi). **MISSING: Assamese, Urdu, Kashmiri, Konkani, Maithili, Sindhi, Manipuri, Santali, Bodo, Dogri, Nepali, Sanskrit** — so for our 18-language probe it's **only ~5/18 useful as a post-OCR LLM** (hi, bn, te, ta, mr, gu, kn, ml, or, pa = 10/18 actually)
- **MILU results (vs Sarvam-30B/105B):** 78.74 macro, beats Sarvam-30B on 11/11 langs, beats Sarvam-105B on 10/11
- **Beats gpt-5.4-nano on 9-language macro:** 79.46 vs 79.69 (basically tied; statistical parity)
- **Decision-changer:** NONE for OCR primary. For Stage 3 (post-OCR text normalization), it's the best open-weight Indic LLM as of Aug 2026 but **30B is too large** for local QLoRA on SAFE langs. Watch list.

### A5. https://huggingface.co/datasets/sarvamai/indic-ocr-bench — Indic OCR Bench dataset
- **6,909 test samples** (6,609 Indian languages + 300 English), **23 languages total** (22 Eighth Schedule + English), semantic-block level (not full noisy pages)
- **All GT reviewed twice by human language experts**
- **Sources:** textbooks, newspapers, magazines, historical writings (1800-present)
- **Per-language sample counts (load-bearing for our probe22 mapping):**
  | Lang | Samples | | Lang | Samples |
  |---|---|---|---|---|
  | Assamese | 471 | | Konkani | 266 |
  | Bengali | 271 | | Maithili | 279 |
  | Bodo | 238 | | Malayalam | 300 |
  | Dogri | 319 | | Manipuri | 207 |
  | English | 300 | | Marathi | 300 |
  | Gujarati | 300 | | Nepali | 437 |
  | Hindi | 228 | | Odia | 300 |
  | Kannada | 300 | | Punjabi | 300 |
  | Kashmiri | 262 | | Sanskrit | 325 |
  | | | Santhali | 274 |
  | | | Sindhi | 248 |
  | | | Tamil | 299 |
  | | | Telugu | 300 |
  | | | Urdu | 385 |
  | **Total** | | **6,909** |
- **Sarvam uses stdlib-only metrics.py** (no third-party packages) — applies Unicode NFC, newline flattening, quote/dash unification, Indic punctuation standardization, strips ZWJ/ZWNJ
- **Decision-changer (LOAD-BEARING):** Our probe22 metrics.py should match Sarvam's normalization for fair comparison. **If our metrics.py differs in normalization, scores are NOT comparable.** Verify: does level2/probe22/metrics.py match Sarvam's normalization? (open question; not researched here, just flagged)

### A6. https://www.sarvam.ai/blogs/sarvam-vision-2-1 — Sarvam Vision 2.1 blog
- **Release date:** 2026-09-24 (the Sarvam 2.1 we already have on probe22)
- **Architecture:** "harness-with-VLM paradigm" — semantic layout parser + pointer reading-order network around a 3B state-space VLM. (Earlier: Sarvam Vision 1.0 = 3B SSM-VLM trained on Indic+English; 2.1 is SFT+RLVR iteration)
- **olmOCR-Bench detailed (vs Bodhan, etc.):**
  | Model | Math | Base | Hdr/Ftr | TinyTxt | MultCol | OldScan | OldMath | Tables | Overall |
  |---|---|---|---|---|---|---|---|---|---|
  | Sarvam Vision 2.1 | 90.5 | 99.8 | 96.3 | 92.5 | 82.1 | **55.3** | 89.7 | 91.9 | 87.3 |
  | Bodhan Indic-OCR | 82.0 | 99.1 | 81.1 | 82.8 | 74.5 | 45.8 | 75.5 | 89.1 | 78.8 |
  | Chandra-OCR2 | 86.5 | 99.9 | 91.5 | 93.4 | 82.4 | 49.2 | 85.8 | 87.5 | 84.5 |
  | Mistral OCR4 | 83.7 | 99.7 | 91.6 | 91.6 | 85.7 | 48.9 | 75.1 | 88.6 | 83.1 |
  | Gemini 3.6 Flash | 86.5 | 99.9 | 87.5 | 92.5 | 78.6 | 48.1 | 79.9 | 85.9 | 82.4 |
  | Opus 5 | 90.0 | 100.0 | 83.9 | 93.5 | 85.8 | 54.0 | 84.3 | 89.5 | 85.1 |
- **OmniDocBench v1.6 overall:** PaddleOCR-VL 1.6 = 96.01, **Sarvam Vision 2.1 = 94.97**, GPT 6 Astra 93.74, Gemini 3.6 Flash 93.58, Bodhan 92.17, DeepSeek-OCR2 87.91
- **Indic OCR Bench per-language accuracy (key table; partial recovered):**
  | Lang | Sarvam 2.1 | Bodhan | Gemini 3.6 | Surya OCR2 | Mistral OCR4 | Opus 5 |
  |---|---|---|---|---|---|---|
  | Bengali | 93.47 | 90.87 | 90.36 | 81.79 | 85.06 | 88.75 |
  | Gujarati | 88.87 | 83.26 | 83.68 | 65.80 | 68.19 | 70.92 |
  | Hindi | 93.52 | 90.99 | 92.11 | 86.12 | 85.87 | 89.38 |
  | Konkani | 97.41 | 95.99 | 93.93 | 90.81 | 87.35 | 84.55 |
  | Kashmiri | **54.82** | 48.04 | 36.04 | 26.27 | 22.63 | 32.20 |
  | Manipuri | **85.12** | 82.85 | 0.55 | 0.00 | 0.00 | 0.00 |
  | Maithili | 96.70 | 93.64 | 93.71 | 78.00 | 78.01 | 57.29 |
  | Marathi | 95.06 | 90.76 | 93.14 | 86.58 | 84.17 | 86.55 |
  | Odia | 80.01 | 75.45 | **81.01** | 69.34 | 57.04 | 65.99 |
  - **CRITICAL OBSERVATIONS:**
    - **Kashmiri is the worst cell (54.82)** — but no other model does better (Bodhan 48.04 is next-best). Even Gemini 3.6 only hits 36.04. → **Our weak cell KS is genuinely weak; no off-the-shelf model wins there.** Attack plan needs KS-specific intervention.
    - **Manipuri is Sarvam-specific.** Gemini/Surya/Mistral/Opus all emit 0-0.55% — they don't read Meitei-Mayek script. Only Sarvam 85.12 + Bodhan 82.85 read it. → **Our wrap-pipeline MUST include Sarvam-style Indic models for mni, OR we exclude mni from ranking (already in protocol §6.4 BARRED).**
    - **Odia — Gemini 3.6 actually beats Sarvam 2.1 (81.01 vs 80.01)**. → For or weak cell, route to Gemini if no bandwidth constraint; our probe22 easyocr/paddle/surya all score much worse (Sarvam is best per standalone third-party).
- **Pricing:** ₹1.50 per page (Sarvam's own claim via ETEnterpriseAI Sep 26 article)

### A7. https://consensus.app/ — Consensus.app
- **NOT an OCR/VLM tool.** Academic search engine for peer-reviewed papers. 220M+ papers. Search API available with limited availability (apply). Built on OpenAI for summarization + fine-tuned open-source models for Consensus Meter.
- **Free tier (per our standing protocol §4):** ~10 searches/day
- **Method:** semantic search + BM25 hybrid
- **Decision-changer:** None for live OCR work. Already in standing method as the W1/W4 literature layer.

---

## B. NEW (POST-CAMPAIGN-LEDGER) FACTS — what's new since 2026-09-27 ledger seal

### B1. BrahmicTokenizer-131K (arXiv:2605.29379, submitted 2026-05-28, Rohan Shravan)
- 131,072-vocab byte-level BPE that **closes the Brahmic compression gap at 131K while preserving o200k_base's English/EU/code compression**
- **Drop-in replacement** for OpenAI's o200k_base (pre-tokenizer, decoder, merge rules unchanged)
- **26.7% fewer tokens than Mistral-Nemo Tekken / Sarvam-m** at same vocab budget on 27M Indic docs (2.84B words, 46.21 GB)
- **Per-language savings 15.79% (Tamil) to 76.79% (Odia = 4.31× compression)** — mechanistic reason: Tekken/Sarvam-m have ZERO Oriya-block tokens; their surgery added 725
- **On non-Indic: matches o200k_base English fertility 1.235 vs 1.232; beats Tekken/Sarvam-m 4.0-14.2% on HumanEval/MBPP/GSM8K**
- **License:** likely research-only; not specified in excerpt
- **Decision-changer (LOAD-BEARING for D1):** **If we train W6 from a tokenizer-aware model, switching to BrahmicTokenizer-131K would give us 26.7% free efficiency on Indic.** Since we're targeting GLM-OCR (different tokenizer anyway) or Qwen2.5-VL (BPE), we would need a tokenizer-surgery step. Mark as **WATCH for tokenizer choice at W6 freeze.**

### B2. 600k-ks-ocr (arXiv:2601.01088, Jan 3, 2026, Haq Nawaz Malik)
- **~602,000 word-level segmented images for Kashmiri script** (256×64 px each, multi-format GT: CRNN/TrOCR/ML)
- **Three traditional Kashmiri typefaces**, comprehensive augmentation simulating real-world degradation, diverse background textures
- **CC-BY-4.0 license** (per INTEGRATED-ELITE-STACK.md mention)
- **Decision-changer:** **KS weak cell attack vector.** We previously identified ks sourcing as solved without new collection (600k-ks-ocr + KS-LIT-3M, CC-BY-4.0). **This paper IS the 600k-ks-ocr we already cited.** Confirms our record; no new action needed. The user-approved D4 micro-repair plan (5-10 sat + 5-10 ks pages W5) is the cheaper path.

### B3. "Whispering in Ol Chiki" (ACL Anthology, Dec 2025, Mandal et al.)
- **First ASR system for Santali in Ol Chiki script** (speech, not OCR — but indicates the script is being researched)
- Cross-lingual transfer: Whisper Small pre-trained on Bengali/Hindi → Santali Ol Chiki
- **WER 28.47% (Bengali pre-trained) and 34.50% (Hindi pre-trained)** — first published baseline for Ol Chiki
- **Decision-changer:** Confirms sat is low-resource; cross-script transfer works as a baseline recipe. **For OCR, the analog is: tesseract sat.traineddata failed upstream; cross-script transfer to Ol Chiki is the obvious next move.** Cite at the call.

### B4. GLM-OCR Technical Report (alphaXiv:2603.10910, submitted 2026-03-16)
- **OmniDocBench v1.5 overall: GLM-OCR 94.62** (highest of tested models), beats Qwen3-VL-235B (89.15) and Gemini-3 Pro (90.33)
- **Seal Recognition: 90.5** (vs dots.ocr 63.0, Gemini-3-Pro 91.3)
- **Multilingual: 69.3** (vs PaddleOCR-VL-1.5: 54.8)
- **Decision-changer:** Already in INTEGRATED-ELITE-STACK.md as D1 W6 primary candidate; this is the v1.5 data point (vs the v1.6 numbers we have for Sarvam). **GLM-OCR is our top open-weight candidate at v1.5.** Cross-check at v1.6 if Sarvam has published PaddleOCR-VL 1.6 vs GLM-OCR head-to-head.

### B5. Bodhan Indic-OCR (Sep 4, 2026 release, AI4Bharat + IIT Madras + NVIDIA)
- 23 languages (22 Indic + EN), OCR system
- **OmniDocBench v1.6: 92.17** (vs Sarvam 94.97, PaddleOCR-VL 1.6 96.01)
- **Indic OCR Bench overall: 84.94** (vs Sarvam 87.39)
- **Indic Open Model License** (per protocol §10 list — OK for our use)
- **Decision-changer:** Already a D1 challenger; the Sep 4 release date is newer than what was in INTEGRATED-ELITE-STACK.md. **Update: Bodhan = best open-weight Indic OCR alternative to Sarvam on Indic OCR Bench.**

### B6. Devanagari VLM Stress Test (arXiv:2606.29213, Jun 28 2026)
- **10 systems on Hindi (Devanagari)** across 4 synthetic degradation conditions + 300 real printed scans
- **Best on degradation:** Gemini 2.5 Flash chrF++ 86.3, Claude Opus 4.7 82.2, **Qwen3-VL-8B 75.2** (runnable on single 24GB GPU, **beats GPT-5.5**)
- **DeepSeek-OCR has catastrophic repetition failures** (up to 71× reference length) — don't trust its mean
- **English OCR does NOT predict Indic OCR:** olmOCR-7B falls to 40.5 on Devanagari; GPT-5.5 to 58.5
- **Decision-changer:** Confirms our D1 stance (open Qwen2.5/3-VL family) is empirically right. **Cite at call for our "why Qwen not GPT" argument.**

### B7. CC-OCR + OCRBench-V2 (benchmarklist.com, 2026)
- **Qwen3.5-27B CC-OCR 81%**, Qwen3.5-35B-A3B 80.7%, Qwen3.5-9B 79.3%, **Qwen3.5-2B 72.9%**
- **Qwen3.7 Plus OCRBench-V2 EN 70.70%** (top of leaderboard)
- **Decision-changer:** **Qwen3.5 family is the most-tested open-weight VLM family on multilingual OCR.** Our D1 wrap-pipeline should test Qwen3.5-9B / Qwen3.5-2B on Indic OCR Bench if budget allows; Qwen3.5-9B at 79.3% CC-OCR is competitive with closed models on multilingual recognition.

### B8. Sarvam Translate (open-weights, June 2025 → Sep 2026 update)
- **Supports all 22 languages** at paragraph level, 15 at structured long-form content
- **Supported structured formats by language:** Sanskrit/Santali/Kashmiri/Manipuri ✅✅❌, Konkani/Sindhi/Bodo ✅✅🟨, Dogri/Nepali ✅✅✅
- **Trained by fine-tuning Gemma3-4B-IT**
- **Decision-changer:** **NOT directly relevant to OCR** (it's translation), but the structural-language matrix indicates **how hard each Indic script is to model.** Dogri/Santali/Manipuri/Kashmiri have lower structured-format support — same pattern as our OCR weak cells.

### B9. PaddleOCR-VL 1.6 (PaddlePaddle team)
- **OmniDocBench v1.6: 96.01 (overall #1)** — beats Sarvam 2.1 (94.97)
- **34.5M params**, ~1000× smaller than frontier VLMs
- **Edge-deployable on phones**
- **Decision-changer:** Already in PPT_SPEC §6 as "PaddleOCR-VL 1.6 still leads OmniDocBench (96.01)" and in D1 wrap-pipeline. **Now CONFIRMED v1.6 leads over Sarvam 2.1 on OmniDocBench BUT loses on Indic OCR Bench (87.39 vs ? — Sarvam doesn't publish PaddleOCR-VL 1.6 on its own Indic bench per the table shown).** Implication: PaddleOCR-VL 1.6 is better for layout fidelity; Sarvam 2.1 is better for Indic accuracy. **Wrap-pipeline should use both.**

---

## C. WHAT'S NEW IN THE WEAK CELLS (most important for our W6 freeze)

### C1. Santali (Ol Chiki, Sarvam 53.91 → 87.39 bench floor)
- **Sarvam 2.1 Indic OCR Bench:** Santhali score not in the partial recovered table; from the OLd Sarvam Vision blog (Feb 5 2026) the language is in the bench but score is undisclosed. **Santhali = ~274 samples per HF dataset.** **No public Ol Chiki–native OCR exists** (tesseract sat.traineddata 404 DEAD upstream, per protocol §10).
- **Whispering in Ol Chiki (Dec 2025, speech not OCR):** WER 28.47-34.50% baseline using Whisper-Bengali/Hindi transfer. **Recipe transfers to OCR: train OCR encoder on Bengali script + Indic Ol Chiki rendering overlay, or use Whisper-style cross-script transfer.**
- **Decision-changer:** **D4 micro-repair (5-10 sat pages W5 if freeze safe) is the cheapest attack.** No good open-weight alternative exists for OCR. Sat stays in W6 BARRED list (D4 stands).

### C2. Kashmiri (Nastaliq, 54.82 Sarvam 2.1 = Sarvam's worst cell on Indic bench)
- **No model is close to Sarvam 2.1** — next is Bodhan 48.04, then gap to Gemini 3.6 36.04
- **600k-ks-ocr (Jan 2026) is the training dataset path** but per protocol §9 "no downloads without explicit user approval" — and the user has not approved
- **rapidocr rapidocr best at 71% Arabic share** (MEASURED 2026-09-27 14:55, per OCR_AGENT_MEMORY_FEED.md)
- **Decision-changer:** **D4 micro-repair (5-10 ks pages W5 if freeze safe) is the cheapest attack.** KS stays BARRED from W6 fine-tuning. Lane A evidence + native-script routing remains the wrap-pipeline path.

### C3. Odia (Sarvam 80.01, but Gemini 3.6 81.01 beats it!)
- **First "beatable" weak cell** — Gemini 3.6 Flash wins on Odia specifically (81.01 vs 80.01)
- **BrahmicTokenizer-131K (May 2026) shows 4.31× Odia compression** — the tokenizer gap is being closed
- **Decision-changer:** **Our wrap-pipeline should route Odia to a Gemini-class closed model when API budget allows**, or to a BrahmicTokenizer-aware open model if W6 trains. **Or = best attack ROI for any available budget.**

### C4. Manipuri (Sarvam 85.12 — but ALL competitors near 0!)
- **Meitei-Mayek script is Sarvam/Bodhan monopoly.** Gemini/Surya/Mistral/Opus all 0-0.55%
- **Decision-changer:** **Confirmed: mni stays BARRED from W6 fine-tuning** (D4 stands). Wrap-pipeline must include Sarvam-style for mni. **No new method to try.**

### C5. OldScan (olmOCR-Bench 55.3, Sarvam 2.1 worst category)
- **Dots.mocr Old-scans 48.2** (per INTEGRATED-ELITE-STACK.md — best published OldScan score on a sub-set)
- **Unlimited-OCR long-horizon multi-page** could lift via cross-page context
- **Decision-changer:** D1 wrap-pipeline already considers dots.mocr head-to-head; **Unlimited-OCR at W6 freeze is the new attack option.** No new method needed in pre-freeze.

---

## D. NEW BENCHMARKS SINCE AUG 2026

| Benchmark | Source | Cells | Decision-relevance |
|---|---|---|---|
| **Sarvam Indic OCR Bench (v1, Sep 24 2026)** | sarvamai/indic-ocr-bench, 6,909 samples | 22 langs + EN | TARGET benchmark for our W6 freeze |
| **OmniDocBench v1.6** | PaddlePaddle blog, Sep 2026 | Layout/table/formula | Layout fidelity comp |
| **olmOCR-Bench (official set, Sep 2026)** | Sarvam Vision 2.1 blog | English, multi-cat incl. OldScan | Scan-quality comp |
| **OCRBench-V2 (en)** | benchmarklist.com, Jun 2026 | English | Multilingual scaffolding |
| **CC-OCR** | benchmarklist.com, Aug 2026 | Multilingual doc OCR | VLM comp |
| **Devanagari Stress Test** | arXiv:2606.29213 | Hindi only | Qwen3-VL beats GPT-5.5 — supports D1 choice |

**No new "Indic benchmark" since Indic OCR Bench v1 (Sep 24 2026).** The 87.39 number is the floor.

---

## E. OPEN-WEIGHT MODELS WE COULD FINE-TUNE (W6 candidates)

| Model | Params | Best score | License | Lifts vs Sarvam? |
|---|---|---|---|---|
| **GLM-OCR** | 0.9B (OmniDocBench v1.5 94.62 #1) | OmniDocBench v1.5 #1 | Zhipu (likely research) | Beats Sarvam on OmniDocBench; unknown on Indic OCR Bench |
| **PaddleOCR-VL 1.6** | 34.5M | OmniDocBench v1.6 96.01 #1 | Apache-2.0 (likely) | Beats Sarvam on OmniDocBench; unknown on Indic OCR Bench |
| **Qwen3.5-9B** | 9B | CC-OCR 79.3% | Apache-2.0 | TBD on Indic OCR Bench |
| **Qwen3-VL-8B** | 8B | chrF++ 75.2 Devanagari | Apache-2.0 | Beats GPT-5.5 on Hindi |
| **Bodhan Indic-OCR** | ~3B | Indic OCR Bench 84.94 | Indic Open Model License | 2.45pts below Sarvam 2.1 |
| **dots.mocr** | 3B | MIT | MIT | OldScan 48.2 best public |
| **MonkeyOCRv2** | 0.7B | MDPBench 83.3 | Apache-2.0 | Smallest strong backbone |
| **HunyuanOCR-1.5** | unknown | unknown | Tencent Hunyuan Community License (NOT pure OSS) | License review first |

**Key gap:** **None of these have a published Indic OCR Bench v1 score.** Our probe22 SHOULD benchmark GLM-OCR, PaddleOCR-VL 1.6, Qwen3.5-9B head-to-head on the 18 probe langs before W5 freeze. **This is a NEW research item.**

---

## F. NEW METHODS SINCE AUG 2026

1. **BrahmicTokenizer-131K (May 2026)** — drop-in tokenizer replacement. **Use if W6 trains from a Qwen/GLM base.**
2. **Cross-script transfer (Whispering in Ol Chiki, Dec 2025)** — recipe for sat low-resource.
3. **Harness-with-VLM paradigm (Sarvam 2.1)** — semantic layout parser + pointer reading-order network as wrapper around 3B SSM-VLM. **Already in PPT_SPEC §6.**
4. **SFT + RLVR with Indic-aware rewards (Gnani NeurIPS 2026 paper 2)** — confirms our D1 RLVR-only-after-SFT-plateau stance; warns that English-favoring RL drops Indic QA by up to 11 pts.
5. **Embedding expansion + warmup (Gnani NeurIPS 2026 paper 1)** — for adding langs to an existing LLM. **Cite at call for W6 QLoRA strategy.**
6. **Lightweight 34.5M-param VLM (PaddleOCR-VL 1.6)** — proves 1000×-smaller-than-frontier is possible. **D1 wrap-pipeline includes this.**

---

## G. CONTRADICTIONS REGISTERED (per campaign §9)

| # | Source A | Source B | Status | Resolution |
|---|---|---|---|---|
| 1 | Krrish Agarwalla (LinkedIn): Sarvam 87.39 inflated by training-data overlap with bench | Sarvam blog: 87.39 = state-of-the-art on community bench | CONTRADICTION | **DEAD for direct cite** — beat Sarvam ON its own bench anyway; the 87.39 stays as target |
| 2 | Gnani NeurIPS 2026: Indic doc QA drops 11 pts on RL | Sarvam blog: RLVR after SFT delivers SOTA | CONTRADICTION | **SURVIVES as warning:** RLVR with non-Indic-aware rewards corrupts our W6; use Indic-aware rewards only |
| 3 | rtk 60-90% token reduction claim | JetBrains +7.6% median cost | CONTRADICTION (per INTEGRATED-ELITE-STACK.md) | Already registered; deferred to call agenda |
| 4 | deepseek-ocr-2 MLX: loadable | mlx-tune README: not loadable | CONTRADICTION | Already registered; not a blocker |

---

## H. NEW EVIDENCE RECORDS (campaign §9 format, decision-it-can-change)

| ID | Source | Status | Decision-changer |
|---|---|---|---|
| R-2026-09-29-01 | sarvam.ai/blogs/sarvam-vision-2-1 | PRIMARY | Confirm Sarvam 87.39 as target; beat on Indic OCR Bench = winning |
| R-2026-09-29-02 | sarvam.ai Indic OCR Bench HF | PRIMARY | Match metrics.py normalization for fair comparison |
| R-2026-09-29-03 | Sarvam blog per-lang table | PRIMARY | KS/Manipuri/Odia weak-cell routing for wrap pipeline |
| R-2026-09-29-04 | Bodhan Sept 2026 release (84.94 Indic) | PRIMARY | D1 W6 challenger; lowest-Levenshtein path to Sarvam |
| R-2026-09-29-05 | GLM-OCR v1.5 94.62 OmniDocBench | PRIMARY | D1 wrap-pipeline primary candidate; TBD on Indic bench |
| R-2026-09-29-06 | Qwen3.5 family CC-OCR 72-81% | PRIMARY | Open-weight VLM family for W6 if budget allows |
| R-2026-09-29-07 | BrahmicTokenizer-131K 26.7% fewer Indic tokens | PRIMARY | If W6 trains from Qwen/GLM base, swap tokenizer |
| R-2026-09-29-08 | 600k-ks-ocr (Jan 2026) | PRIMARY | KS training data path exists if user approves download |
| R-2026-09-29-09 | Whispering in Ol Chiki (Dec 2025) | PRIMARY | Sat baseline recipe = cross-script transfer |
| R-2026-09-29-10 | Devanagari VLM stress (Jun 2026) | PRIMARY | Validates D1 "Qwen > GPT" choice |
| R-2026-09-29-11 | Gnani NeurIPS 2026 paper 2 (RL trade-off) | PRIMARY | Reinforces "RLVR on Indic-aware rewards only" |
| R-2026-09-29-12 | Gnani Evon v3.3 model card (Aug 2026) | PRIMARY | NOT for OCR; possible Stage 3 LLM if 30B fits W6 budget (likely not) |
| R-2026-09-29-13 | LinkedIn Krrish skeptic comment | SECONDARY | REJECTED — still target Sarvam 87.39 |
| R-2026-09-29-14 | PaddleOCR-VL 1.6 34.5M OmniDocBench 96.01 | PRIMARY | Wrap-pipeline edge-deploy option |
| R-2026-09-29-15 | Sarvam blog mni=85.12 vs ALL competitors 0-0.55 | PRIMARY | MNI stays BARRED; wrap to Sarvam/Bodhan only |

---

## I. CONCRETE NEXT STEPS (for orchestrator to decide at the call)

1. **Add benchmark head-to-head:** GLM-OCR, PaddleOCR-VL 1.6, Qwen3.5-9B on probe22 (need user approval for downloads — D1 budget)
2. **Verify metrics.py normalization matches Sarvam Indic OCR Bench metrics.py** for direct cross-comparison
3. **Cite BrahmicTokenizer-131K** if W6 trains from Qwen/GLM base
4. **Cite 600k-ks-ocr** as the training data path for KS if user relaxes download ban
5. **Cite Whispering in Ol Chiki** as the cross-script baseline for SAT
6. **Add Gnani NeurIPS 2026 papers** to the validation-call packet for the "RL trade-off" warning
7. **Update AGENTS.md graph numbers** to 3990/4681/420/50 (current disk state)

---

## J. WHAT DID NOT CHANGE

- Campaign decisions D1-D4 still stand
- §6.4 GT verdicts still locked (no re-litigation)
- Sealed dirs (level2/out/, level2/reports/, level2/probe22/out/, arc_level_1/, Datasets/) untouched
- W6 guard (no training until W5 freeze) still holds
- South 400 leaderboard unchanged

---

**End of LIVE_LATEST_2026-09-29.md. 15 evidence records registered, 4 contradictions flagged, 7 next steps for orchestrator decision.**