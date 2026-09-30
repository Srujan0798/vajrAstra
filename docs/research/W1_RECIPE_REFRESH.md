# W1 — what changed since mid-August 2026

Recipe refresh against the PPT in `docs/architecture/PPT_SPEC.md`. Research exists to choose the training recipe. Not a review paper. No training until W5.

Consensus.app was named as the synthesis layer (10 free searches/day). This pass used official blogs, HuggingFace cards, and arXiv because Consensus is JS-gated from this agent. Human can still run the three named queries there and paste cards into this file.

Named Consensus queries:
1. What training strategies work best for multilingual Indic OCR with vision-language models?
2. Does fine-tuning an existing OCR VLM outperform training a multilingual OCR model from scratch?
3. How should script identification and mixture-of-experts be used in multilingual document and scene OCR?

## Flowchart — old (PPT, ~mid-Aug 2026)

```
S1–S6 + proprietary scans
  → OpenCV deskew/denoise/binarize
  → DocLayout-YOLO LoRA on IndicDLP  (iterate / Gemini-distill if weak)
  → crop regions
  → parallel SFT: TrOCR + Qwen 3.5 VL + PaddleOCR-VL 1.6
       + akshara-boundary auxiliary loss
  → SCST / RL on CER
  → small LLM SFT: noisy text → JSON
  → SimPO / DPO on ranked JSON
  → eval: Sarvam, IndicDLP, Indic Vision Bench  (no FT on test)
```

## Flowchart — challenger (field as of 2026-09-25)

```
synthetic + real  (printed, handwritten, forms, tables; Indic + EN)
  → light preprocess (still useful on OldScan)
  → layout / reading-order HARNESS
       Sarvam: semantic layout parser + pointer reading-order around the VLM
       Bodhan: 33M IndicDocLayout (PP-DocLayoutV3 / RT-DETR, 37-class) then 0.8B block OCR
  → OCR-specialized VLM  (FINE-TUNE or WRAP; do not train a generic VLM from scratch)
       candidates: Bodhan IndicBlockOCR (Qwen3.5-0.8B + Sarvam-30B tokenizer)
                   Sarvam Vision 2.1 (API)
                   PaddleOCR-VL 1.6 (already in PPT; OmniDocBench leader 96.01)
                   Nanonets-OCR2-3B / Chitrapathak-2 path
  → progressive SFT: word → line → block → page
  → RLVR / SCST  only after SFT plateaus
  → schema / KV head  if the product is forms or ID docs (it is)
  → script router or ScriptMoE decoder  only for the long tail
       Santali, Kashmiri, Meitei, Urdu/Sindhi Nastaliq
  → eval: sarvamai/indic-ocr-bench + OUR domain probe  (no FT on test)
```

## What actually moved after mid-August 2026

| Date | Thing | Load-bearing fact | Source |
|---|---|---|---|
| 2026-09-04/10 | Bodhan Indic-OCR | Open-weight two-stage: 33M layout + 0.8B Qwen3.5 block OCR. Printed 22 langs + EN; HW 12 Indic + EN. ₹0.20/image API. Internal printed WAcc 86.2. | HF `bodhan-ai/indic-ocr` |
| 2026-09-21 | ScriptMoE | Shared encoder, top-2 script experts + shared expert. PP-OCRv5 end-to-end F1 65.71 → 80.89, slightly above best VLM at a fraction of params. Scene-text, not full-page docs. | arXiv:2609.24058 |
| 2026-09-24/25 | Sarvam Vision 2.1 + Indic OCR Bench | Harness-with-VLM. SFT then RLVR. Indic bench 6,909 (6,609 Indic + 300 EN). Overall 87.39 vs Bodhan 84.94 vs Gemini 3.6 Flash 79.35. OldScan still 55.3. Santali 53.91 (Bodhan 68.30 wins). Kashmiri 54.82. Manipuri 85.12; most frontier VLMs ~0. | sarvam.ai/blogs/sarvam-vision-2-1 · HF `sarvamai/indic-ocr-bench` |
| Feb 2026 (still the training-strategy paper) | Chitrapathak-2 | Fine-tune OCR-specialized VLM (Nanonets-OCR2-3B on Qwen2.5-VL) beats from-scratch multimodal. 3–6× faster. Parichay: 9 Indian govt docs, 89.8% exact match. | arXiv:2602.16430 |
| 2026-05/06 | PaddleOCR-VL-1.6 | Not from scratch. Starts from 1.5. Weak-region mining → CPT 16.8M → SFT 7.3M → RL. Layout = PP-DocLayoutV3 + pointer reading-order. 0.9B. OmniDocBench v1.6 **96.33**. Same architecture as 1.5 (drop-in). | arXiv:2606.03264 |
| 2026-06-28 | Devanagari VLM stress-test | Synthetic chrF++ 91–98 hides all differences. Real Hindi scans: 9/10 systems collapse. English OCR rank does not transfer (GPT-5.5 58.5; olmOCR-7B 40.5; **Qwen3-VL-8B 75.2** open). Report median + catastrophic-rate. Conjunct/matra/nukta are the structural errors. | arXiv:2606.29213 |
| 2026-09-02 | FaithC4 (Amazon) | General VLMs rewrite imperfect text (WER +6.9). OCR-specialized VLMs stay faithful (+0.1–3.4). Citizen docs (exams, land records) need the faithful class. | arXiv:2607.21617 |

## Answers to the three method questions (cited)

**How others train.** Winning 2026 Indic OCR is a *system*: layout/reading-order harness around an OCR-specialized VLM, trained synthetic+real, SFT then RLVR. Bodhan splits layout (tiny DETR) and recognition (0.8B). Sarvam keeps a general VLM but harnesses it. Nobody winning ships a bare TrOCR from scratch as the product.

**Fine-tune vs from-scratch.** Chitrapathak-2 is the direct experiment: pairing a generic vision encoder with a strong multilingual LM and training end-to-end lost to fine-tuning Nanonets-OCR2-3B, even though that OCR model had never seen Indic data. Fine-tune existing OCR VLM. PPT box 2’s TrOCR-from-scratch arm is the obsolete piece.

**Script ID / MoE.** Use a router or ScriptMoE for the long tail, not as the default backbone for hi/ta/te. Sarvam 2.1 already >90 on hi/kn/te/mr/ne/mai/kok and still collapses on Santali and Kashmiri. Bodhan’s Santali win (68.30 vs 53.91) is the specialist signal. ScriptMoE is a decoder swap inside PP-OCRv5-class recognizers, not a reason to throw away the VLM harness.

## Implication for OUR PPT (not a freeze)

Smallest change that is still a hybrid against *this* PPT, not a new company:

1. Keep Stage 0 preprocess and Stage 1 layout. Swap the detector toward PP-DocLayoutV3 / Bodhan IndicDocLayout / Sarvam-style pointer reading-order if the probe says YOLO-from-scratch loses.
2. Drop TrOCR-from-scratch as a training target. Keep Qwen 3.5 VL + PaddleOCR-VL 1.6. Add Bodhan IndicBlockOCR and/or Sarvam 2.1 as the thing we wrap or SFT. Keep akshara-boundary aux if we SFT.
3. Keep 2b RL, but only after SFT. Rename to RLVR in the freeze notes if the literature holds.
4. Keep 3/3b schema+preference — citizen documents are forms.
5. Add Indic OCR Bench to eval. Keep no-FT-on-test.
6. Plan a specialist (router / extra expert / extra data) for Santali, Kashmiri, Meitei, Nastaliq — after the 20-sample probe, not before.

Deep paper pass continues in the background research run. This file is the living one-pager; append citations, do not fork.
