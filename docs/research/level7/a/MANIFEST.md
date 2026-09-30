# Lane A — OCR/DocAI SOTA 2025–2026 MANIFEST

Lane: A (Engine Agent). Scope: OCR/DocAI systems 2025–2026 with Indic-script emphasis. Date: 2026-09-27 (record upgrade: 2026-09-29).

## Inventory (post §9 evidence-law upgrade 2026-09-29)

- LEDGER.md — main record ledger, **984 records** across A0–A6 sections (≥400 target met, 979 with all 10 §9 fields)
- 8 standing-law records (A0-001..008) — pointer refs to disk truth
- 125+ DocAI/OCR system records (A1) — Qwen, InternVL, GOT-OCR2, MonkeyOCR, PaddleOCR-VL, olmOCR, Surya 2, Mistral OCR 3, dots.ocr, Chandra, DeepSeek-OCR, OCRVerse, GLM-OCR, OCRFlux, LightOnOCR, MinerU2.5-Pro, UniT, DocRes, Uni-DocDiff, etc.
- 70+ Indic OCR records (A2) — Sarvam, Bodhan, AI4Bharat (IndicBERT/IndicBERTv2/IndicConformer/IndicWav2Vec/IndicTrans2/IndicDLP/MILU), Krutrim (Krutrim-1/Krutrim-2), Bhashini ULCA, Aksharamukha, IndicNLP, etc.
- 35+ Benchmark records (A3) — ICDAR 2017/2019/2023 MLT, OmniDocBench v1.6/v1.7, olmOCR-Bench, Real5-OmniDocBench, Indic OCR Bench, KITAB-Bench, ICDAR 2023/2025 IHTR/IHDR, MILU, IndicGenBench, L3Cube-IndicQuest v2, Bharat Scene Text, etc.
- 30+ Restoration records (A4) — DocRes, DocDiff, Uni-DocDiff, RDDM, TextSR, DocRevive, UniT, SauvolaNet, D2Dewarp, DvD, ESRGAN, Real-ESRGAN, SwinIR, DocGeoNet, etc.
- 30+ Indic-script specifics records (A5) — Brahmic, conjuncts, matra/halant, akshara segmentation, aksharamukha normalization, Ol Chiki, Meitei Mayek, etc.
- 115+ Training recipe records (A6) — LLaVA-NeXT, Qwen2-VL/2.5-VL/3-VL, InternVL2/3, GOT-OCR2, Nanonets-OCR2, Sarvam Vision 2.1, ScriptMoE, synthetic data (BED-LM, SyntheticDoG, Scrambled text), DPO/SimPO, RLVR, etc.

## Score breakdown (record quality distribution)

- Score ≥90: 95+ records (5/5/4 or 5/5/5)
- Score 60-89: 180+ records (4/5/4, 5/4/5, etc.)
- Score 30-59: 100+ records (4/3/4, 3/4/3, etc.)
- Score <30: 45+ records (context-only, kept per contradiction rule)

## Coverage map (against probe weak cells)

- Santali 53.91: A1-014 (Surya 2 detail), A1-046 (IIIT-H low-resource), A1-073 (ScriptMoE), A1-100 (olmOCR-2), A2-009/010/015 (Bodhan IndicOCR), A2-024 (Sarkar), A5-011 (Ol Chiki script), A5-017/018 (Santali script-mixing)
- Kashmiri 54.82: A1-040 (Devanagari stress-test), A1-097 (Scrambled text synthetic corruption), A2-009/010 (Bodhan), A2-024 (Sarkar Kashmiri 87.71), A3-002 (Indic OCR Bench), A5-017/018 (Kashmiri Devanagari+Perso-Arabic)
- OldScan 55.3: A1-014 (Surya 2 OldScan 42.8), A1-051 (olmOCR-Bench OldScan 42.8), A1-053 (OmniDocBench warp), A4-001 (DocRes), A4-007 (DocRevive), A4-008 (UniT), A4-013 (TextSR), A4-019 (DvD), A4-024 (UniRestore)
- Odia 80.01: A1-010 (Chitrapathak-2), A1-088 (Chitrapathak-2 detail), A2-018 (Chitrapathak-2 Odia coverage), A3-002 (Indic OCR Bench), A6-044 (Chitrapathak-2 HF card)

## Source quality

- Primary sources: arXiv papers, official model cards (HF), official blogs (sarvam.ai, krutrim, paddleocr.ai, mistral.ai, datalab.to), GitHub repos
- Secondary sources: India Today, CNBC, MoneyControl, Hindu BusinessLine (press); AnalyticsVidhya, MarketersIndex, E2E Networks (analyst blogs); Tracxn, Wikipedia (corporate)
- Tertiary: ICADAR proceedings, ACM DL, Springer LNCS, OpenAccess CVF

## Top themes

1. **Harness-with-VLM** is the dominant 2025-2026 pattern (Sarvam Vision 2.1, Bodhan, PaddleOCR-VL-1.6, MonkeyOCR). Single VLM is no longer competitive.
2. **SFT → RLVR** is the universal training recipe (Sarvam, PaddleOCR-VL-1.6, olmOCR-2, OCRVerse). Ablation evidence: RLVR gives +0.08 on top of saturated SFT.
3. **Fine-tune OCR-specialized VLM > from-scratch** (Chitrapathak-2 ablation: 3–6× faster, better accuracy).
4. **Open-source pool is now SOTA-competitive** (Oct 2025 inflection: Nanonets OCR2, PaddleOCR-VL, DeepSeek-OCR, Chandra, OlmOCR-2, LightOnOCR-1B).
5. **Data engineering > new architecture** (MinerU2.5-Pro: same architecture +2.71 via data alone).
6. **Synthetic + real** is the universal training data mixture (Sarvam, PaddleOCR-VL-1.6, Nanonets-OCR2, Bodhan).
7. **OCR-specialized VLMs stay faithful** vs general VLMs rewriting text (FaithC4).
8. **Restoration pre-pass for OldScan** is universally accepted (DocRes, Uni-DocDiff, TextSR, DvD).
9. **Specialists for low-resource scripts** (Santali, Kashmiri, Meitei Mayek) — Bodhan wins Santali 68.30, specialist beats shared.
10. **Synthetic corruption > real data** for OCR post-correction (Scrambled text: −55% CER on Hindi).

## Open questions for W6 recipe freeze

1. **Base model**: PaddleOCR-VL-1.6 (Apache-2.0, 0.9B, OmniDocBench 96.33) vs Qwen2.5-VL (foundation for dots.ocr/Chitrapathak-2/Chandra/Nanonets OCR2) vs Bodhan IndicOCR (open-weight Indic specialist).
2. **Recipe**: CPT→SFT→RLVR (Sarvam/Paddle) vs fine-tune OCR-specialized VLM (Chitrapathak-2).
3. **Specialists**: Santali + Kashmiri + Meitei Mayek specialists via synthetic-first + real anchor (per R2/R3 mixing rules).
4. **Restoration pre-pass**: A0 (none) / A1 (Otsu+deskew) / A2 (Sauvola-frozen) / A3 (DocRes-head pilot) per R4 ablation chain.
5. **Stage 3 LLM**: Krutrim-2-12B vs Gemma4-31B vs Sarvam 30B (per L3Cube-IndicQuest v2 results).
6. **Post-correction**: Scrambled-text-style synthetic corruption LM (R3 verdict: synthetic > real).
7. **Evaluation**: Indic OCR Bench (Sarvam 87.39 / Bodhan 84.94 / Gemini 79.35 / GCV 71.76 baseline) + our probe weak cells.
8. **Inference cost**: PaddleOCR-VL-1.6 ~2GB VRAM FP16, ~45 pg/min L40S (per Spheron).
9. **Indic OCR Bench fetch**: P1 user approval needed (per §9 hard rule).
10. **Data label audit**: machine-GT trust scores (ne BARRED 26.6, ks/mr/gu/ur VERIFY-FIRST per R5).
