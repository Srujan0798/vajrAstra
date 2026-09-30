# W3 probe schema — 22 Eighth-Schedule languages

Locked 2026-09-25. Probe, not a 400-page replica of South.

## Size

| Set | n | Action |
|---|---|---|
| South: te, ta, kn, ml | 400 pages already scored | KEEP `level2/reports/*`. Do not rescore 400. Optional: add Sarvam Vision 2.1 + Bodhan on a **20-page South subset** (5/lang) so new models sit on the same sheet. |
| Remaining 18 languages | **20 samples each** | New probe only. User lock: 10–20; we take 20. |

18 × 20 = 360 blocks. Plus 20 South add-on for new models = 380 new inferences per new engine.

## Languages

Keep (South, already scored): Kannada, Malayalam, Tamil, Telugu.

Probe (20 each): Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kashmiri, Konkani, Maithili, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Urdu.

Script routing (for sampling, not for training):

| Script | Languages in this probe |
|---|---|
| Devanagari | hi, mr, ne, sa, gom/kok, brx, mai, doi |
| Bengali-Assamese | bn, as; mni if Bengali script |
| Gujarati | gu |
| Gurmukhi | pa |
| Odia | or |
| Perso-Arabic / Nastaliq | ur, sd, ks |
| Ol Chiki | sat |
| Meitei Mayek | mni (must include; Gemini 3.6 Flash scored 0.55 on Manipuri on Sarvam’s bench) |

Must-include failure cells from public SOTA (do not skip): Santali, Kashmiri, Manipuri (Meitei), Odia, old scans, handwriting, tables, mixed script.

## Sample source (priority)

1. HuggingFace `sarvamai/indic-ocr-bench` — test split 6,909 (image, image_name, gt, language). 300 English. Stratify 20 per remaining language from this GT. Prefer `small_representative` (1,170) if it already covers 20/lang; else sample from `test`.
2. Krishna 20-sample working sets if they land in this workspace.
3. Our domain pages if a remaining language already exists on disk.

Do not wait for (2) or (3). Start the sheet from (1).

## Sheet columns

```
image_id | language | script | print_or_hand | quality | has_table | mixed_script | gt | model | prediction | CER | WER | error_tag
```

Error tags: `matra_order | conjunct | old_scan | handwriting | table | reading_order | hallucination | repetition | charset | other`

One row = one (image, model) pair.

## Model list

Already scored on South 400 (do not drop): surya, anuvaad_tesseract, tesseract_indic (openbharatocr = tess alias), tesseract_bilingual, indicphotoocr, paddleocr_indic, rapidocr, doctr, easyocr.

Must add: **Sarvam Vision 2.1**, **Bodhan Indic-OCR** (`bodhan-ai/indic-ocr`).

Optional if weights/API free this week: PaddleOCR-VL 1.6 (already in the PPT), Chitrapathak-2 / Nanonets-OCR2-3B.

Paid APIs wait for W5 unless a free/open path exists.

## Public SOTA snapshot to beat (Sarvam Indic OCR Bench, 2026-09-24)

Overall word accuracy: Sarvam Vision 2.1 **87.39** · Bodhan **84.94** · Gemini 3.6 Flash 79.35 · Google Cloud Vision 71.76 · Surya 2 69.96.

Long tail (Sarvam 2.1 / Bodhan): Santali 53.91 / **68.30** (Bodhan wins) · Kashmiri 54.82 / 48.04 · Manipuri 85.12 / 82.85 (frontier VLMs ~0) · Odia 80.01 / 75.45.

South on that public bench (not our 400): kn 90.54 / 86.51 · ml 90.24 / 86.38 · ta 87.70 / 84.21 · te 91.55 / 86.92. Our South 400 is harder (old-scan 200 dpi; writer-basis CER surya 0.43 overall; te/kn thin-n).

## Output paths

- Manifest: `level2/probe22/manifest.json`
- Rows: `level2/probe22/sheet.csv`
- Per-engine preds: `level2/probe22/out/<engine>/<lang>/*.json`

Do not write probe outputs into `level2/out/` (that tree is the South 400 seal).

## Status

Schema locked. Samples not yet drawn. Engines not yet run. W4 audit waits for this sheet.
