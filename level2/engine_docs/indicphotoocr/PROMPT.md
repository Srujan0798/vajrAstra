# indicphotoocr — PROMPT

## Engine
IndicPhotoOCR (IIIT-H, parseq trust-patched)

## Policy
CPU path — init once per process, reuse across pages.
identifier_lang="auto", device="cpu"

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Output Format
Level-1-style JSON (same as tesseract_indic)
