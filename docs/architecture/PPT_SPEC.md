# PPT one-page spec — AksharDrishti architecture

Source: `/Users/srujansai/Desktop/South/AksharDrishti_Hackathon_Proposal final.pptx` (4 slides, dumped 2026-09-25). This is the architecture the team already designed (~mid-August 2026). Diff it. Do not overwrite it. Do not invent a new backbone.

Team: Vaultstack AI — Vinay Gahlot (CEO), Akshay Gahlot (CTO), David Babu (advisor). Product: OCR for all 22 scheduled Indic languages.

## Pipeline boxes (slides 3–4)

| # | Stage | Base | Technique | Why (as written) |
|---|---|---|---|---|
| 0 | Preprocess | OpenCV | deskew, denoise, binarize | quality without a net |
| 1 | Layout | DocLayout-YOLO (YOLOv10) | SFT on IndicDLP; LoRA | Indian document layout. Iterate: if IndicDLP rows/records are good enough, stop; else distill extra layout from Gemini |
| 2 | Recognition SFT (parallel) | TrOCR (ViT/BEiT+RoBERTa) + Qwen 3.5 VL + PaddleOCR-VL 1.6 | seq2seq SFT, quality-tiered loss, **akshara-boundary auxiliary loss** on Qwen3-VL-8B and PaddleOCR | crops from Stage 1; option A distill extraction from Gemini; option B human extract for langs Gemini/ChatGPT miss; Kashmiri: layout boxes + PDF text under box as GT |
| 2b | Recognition RL | same three | SCST / RL on CER | optimize the judged metric after SFT |
| 3 | Post SFT | IndicBERT / Airavata / small LLM | SFT noisy text → corrected JSON | structured fields |
| 3b | Pref alignment | same | SimPO or DPO on ranked JSON (CER-tagged) | pick best JSON; Bhashini-shaped |
| — | Eval | Sarvam, IndicDLP, Indic Vision Bench | direct inference, **no fine-tune on test** | CER / WER |

## Data boxes (slide 2)

S1 BSTD scene · S2 IIIT-HW / INDIC-HW-WORDS · S3 Sangraha/IndicCorp (text→synth) · S4 Bhashadaan · S5 govt/exam scans 5–10k pages/domain · S6 synthetic unlimited. Proprietary: gazette, courts, DigiLocker, land records, board exams. HITL double annotation.

## Product claims (slide 1)

Akshara-aware layout+recognition (conjuncts, matras, sandhi). Calibrated confidence, visual lookup, per-language morphology. Structured fields. Low-confidence spans always to human review.

## Preliminary box labels vs Sep-2026 field (DRAFT — freeze at W5)

| Box | Draft label | Why |
|---|---|---|
| 0 OpenCV | KEEP | OldScan is still the global worst category (Sarvam 2.1 olmOCR OldScan 55.3). Cheap pixels still matter. |
| 1 DocLayout-YOLO / IndicDLP LoRA | HYBRID | Layout harness is confirmed SOTA (Sarvam semantic parser + pointer reading-order; Bodhan 33M PP-DocLayoutV3). Prefer swapping the *detector* to 2026 defaults over training YOLO from scratch. Keep the stage. |
| 2 TrOCR from-scratch + Qwen 3.5 VL + PaddleOCR-VL 1.6 | HYBRID / drop TrOCR-from-scratch | Chitrapathak-2: fine-tune an OCR-specialized VLM (Nanonets-OCR2-3B / Qwen2.5-VL) beats LLaVA-from-scratch on accuracy and 3–6× latency. PaddleOCR-VL 1.6 still leads OmniDocBench (96.01). Qwen 3.5 VL is already Bodhan’s recognizer family. Akshara-boundary aux is the Indic-specific KEEP if we SFT. |
| 2b SCST/RL on CER | KEEP, after SFT | Sarvam 2.1: SFT then RLVR. Do not start at RL. |
| 3 noisy→JSON SFT | KEEP if product is forms | Sarvam 2.1 made KV/table/handwriting first-class. Citizen docs need a schema head. |
| 3b SimPO/DPO | KEEP | preference on ranked JSON still valid |
| Bench set | UPDATE | Add HuggingFace `sarvamai/indic-ocr-bench` (6,909 blocks, 22 langs + EN). Keep no-FT-on-test. |

W2 draft (full table): `docs/architecture/W2_HYBRID.md`. Freeze at W5.
