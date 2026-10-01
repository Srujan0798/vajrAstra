# openbharatocr — PROMPT

## Engine
OpenBharatOCR 0.4.3 (primarily ID-card extraction library)

## Policy
OpenBharatOCR is mainly for Indian ID cards (Aadhaar, PAN, DL, passport, voter ID).
For full pages we fall back to its underlying tesseract/paddle stack if exposed,
else use tesseract_indic so the pipeline still produces packs.

## Language Stack
Fallback to tesseract_indic: TESS_STACK per language (tel+hin+eng for te, tam+hin+eng for ta, kan+hin+eng for kn, mal+hin+eng for ml)

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Note
WEAK / near-duplicate benchmark. Upstream package designed for ID cards, not dense book/govt multipage OCR. Falls back to tesseract_indic for full pages — output is effectively a twin of tesseract_indic.

## Output Format
Level-1-style JSON (same as tesseract_indic)
