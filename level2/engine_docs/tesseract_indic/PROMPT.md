# tesseract_indic — PROMPT

## Engine
Tesseract 5.5.2 with Indic language stack (tel+hin+eng for te, tam+hin+eng for ta, kan+hin+eng for kn, mal+hin+eng for ml)

## Policy
OPEN POLICY (operator directive): read whatever glyphs are on the page — any language, no restriction.
Stack every Indic model we have + English so mixed books (Telugu/Marathi/Hindi/English) all get read.

## Language Stack per Script
- te: tel+hin+eng
- ta: tam+hin+eng
- kn: kan+hin+eng
- ml: mal+hin+eng

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew — skew correction was never implemented)

## Timeout
300s per page, 1 retry with binarized variant

## Output Format
Level-1-style JSON with:
- page_id, source, lang, script, modality, domain, quality_tier
- missing: ["L2"] if empty, else []
- unreadable_reason: "ocr_empty" if empty, else null
- engine_meta: engine, policy, dpi=200, version
- regions: single paragraph region with full-page bbox and OCR text
