# tesseract_bilingual — PROMPT

## Engine
Tesseract 5.5.2 with official tessdata bilingual models (eng+indic via GitHub tessdata method)

## Policy
Official tessdata bilingual: eng+indic (same GitHub tessdata method as tesseract_indic)
Stack: eng + TESS_STACK[lang] (deduped preserving order)

Language stacks:
- te: eng+tel+hin
- ta: eng+tam+hin
- kn: eng+kan+hin
- ml: eng+mal+hin

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Output Format
Level-1-style JSON (same as tesseract_indic)
