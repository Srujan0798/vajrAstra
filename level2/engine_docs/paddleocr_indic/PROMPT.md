# paddleocr_indic — PROMPT

## Engine
PaddleOCR 3.7.0 / PaddlePaddle 3.3.1

## Policy
OPEN POLICY (operator directive): read any script on the page.
- te/ta: PP-OCRv5
- kn->ka: PP-OCRv3
- ml unsupported by Paddle → en stack (fallback disclosed once per run)

## Language Mapping
- te: te (PP-OCRv5)
- ta: ta (PP-OCRv5)
- kn: ka (PP-OCRv3)
- ml: en (fallback — no Malayalam model exists)

## Two-Stage Graceful Degradation (Paddle-only)
1. Full pipeline (server det + lang rec) — timeout 300s
2. Light retry (mobile det, det input capped at 960) — timeout 900s

Light config models:
- te: te_PP-OCRv5_mobile_rec
- ta: ta_PP-OCRv5_mobile_rec
- ka: ka_PP-OCRv3_mobile_rec
- en: default rec, mobile det, capped input

Poisoned-mode set: never re-enter a paddle instance whose thread was abandoned on timeout.

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
Full: 300s, Light: 900s (paddle-only budgets; other engines keep shared 300s)

## Output Format
Level-1-style JSON (same as tesseract_indic)
