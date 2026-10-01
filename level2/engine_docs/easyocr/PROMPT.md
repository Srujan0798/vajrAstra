# easyocr — PROMPT

## Engine
EasyOCR 1.7.2 with all-Indic open reader

## Policy
OPEN POLICY (operator directive): read any script on the page, no language restriction.

## Language Strategy
EasyOCR hard constraints (validated): Dravidian models are pairwise-incompatible (te/ta/kn each only work with en); Devanagari family bundles (hi mr ne + en) work.
Strategy: run every VALID open reader for scripts plausibly on our pages, keep longest output.
Combos tried:
- te+en
- ta+en
- kn+en
- hi+mr+ne+en

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Known Fixes
- Tamil charset patch: EasyOCR 1.7 tamil.pth has 143 classes; bundled charset is only 126 chars. Patched at runtime.

## Output Format
Level-1-style JSON (same as tesseract_indic)
