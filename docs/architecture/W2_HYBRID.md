# W2 — hybrid vs the existing PPT

**Status: DRAFT CLOSED 2026-09-25.** Humans accept or reject at W5. Probe (W3) can still flip a HYBRID cell.

Diff against `docs/architecture/PPT_SPEC.md`. Not a new backbone. Not a freeze. Probe (W3) can still flip a HYBRID to KEEP or REPLACE.

Research pass 2026-09-25: `docs/research/W1_RECIPE_REFRESH.md`. Honest gaps listed there.

| Box | PPT today | Label | Hybrid |
|---|---|---|---|
| 0 Preprocess | OpenCV deskew / denoise / binarize | **KEEP** (geometry). **HYBRID** on binarize | Keep deskew/rotation. Native-resolution VLMs (Nanonets, PaddleOCR-VL) do not need classical binarize; Parichay uses a learned rotation head. OldScan is still the worst global cell (Sarvam 2.1 olmOCR OldScan 55.3) — do not drop cheap geometry. |
| 1 Layout | DocLayout-YOLO + IndicDLP LoRA | **REPLACE detector, KEEP the stage** | Ship **PP-DocLayoutV3 + reading-order** (Bodhan IndicDocLayout 33M; PaddleOCR-VL-1.6 leaves this module unchanged). IndicDLP still scores YOLO ~54.5–55.0 mAP; 2026 production stacks do not ship YOLO as the detector. LoRA/SFT that detector on Indic crops if our probe says it misses Indian forms. |
| 2 Recognition SFT | TrOCR + Qwen 3.5 VL + PaddleOCR-VL 1.6, akshara-boundary aux | **DROP TrOCR arm. KEEP the other two. ADD one OCR-VLM init** | Parallel SFT of: **Qwen 3.5 VL** (Bodhan-style, Sarvam-30B tokenizer, layout crops), **PaddleOCR-VL 1.6** (CPT→SFT→GRPO from the 1.5 ckpt), **Nanonets-OCR2-3B** (Chitrapathak-2 path). PPT slide says TrOCR is seq2seq *fine-tune*, not random-init; still drop it as a training target — Chitrapathak-2 beat CLIP+LM from-scratch (Telugu char ANLS 6.69 vs 11.00, 3–6× faster). Akshara-boundary aux: **KEEP as unvalidated Indic add-on** (no 2026 paper ablates it). |
| 2b RL | SCST / RL on CER | **KEEP order. HYBRID algorithm** | RL **after** SFT only. 2026 scoring leaders use GRPO or RLVR, not proven-equal to SCST. Do not start at RL. |
| 3 Post SFT | IndicBERT / Airavata / small LLM: noisy text → JSON | **HYBRID: schema on the OCR VLM** | Parichay hits 89.8% exact match on 9 Indian ID/vehicle docs by schema-conditioning the OCR VLM, not a second small LLM. Keep a JSON head. Do not treat a transcription VLM as the form extractor without that SFT. |
| 3b Pref | SimPO / DPO on ranked JSON | **KEEP** | Still valid. Sarvam put KV data into SFT+RLVR rather than a separate DPO paper; absence ≠ ablation. |
| Eval | Sarvam, IndicDLP, Indic Vision Bench; no FT on test | **UPDATE set. KEEP the firewall** | Add `sarvamai/indic-ocr-bench` + our 20×18 probe + South 400. Never train on those splits. |
| Long tail | Kashmiri called out as Gemini-miss | **ADD after probe, not as backbone** | Santali (Bodhan 68.30 vs Sarvam 53.91), Kashmiri (~54), Manipuri-Meitei, Nastaliq: extra data + small LoRA, not a 22-language from-scratch train. ScriptMoE is scene-STR; do not replace the document VLM with it. |

## Smallest change that is still this PPT

```
OpenCV rotation/deskew
  → PP-DocLayoutV3 + reading order  (Stage 1 stays)
  → parallel SFT: Qwen 3.5 VL + PaddleOCR-VL 1.6 + Nanonets-OCR2-3B
       + akshara-boundary aux if we SFT
  → GRPO / RLVR on CER after SFT
  → schema JSON on the same OCR VLM (Parichay-style)
  → SimPO/DPO or GRPO on ranked JSON
  → tail LoRAs only where the 20-sample probe fails
  → eval: Indic OCR Bench + our probe + South 400  (no FT on test)
```

## Not decided until W3 + W5

Which Stage-2 student actually wins on **our** pages (Bodhan 0.8B vs Paddle 0.9B vs Nanonets 3B vs Sarvam API). Public benches are not our 200-dpi South scans.

W4 audit uses this file + the probe sheet. Humans accept or reject at W5.
