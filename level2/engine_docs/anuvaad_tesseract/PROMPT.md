# anuvaad_tesseract — PROMPT

## Engine
Anuvaad-tuned Tesseract models for Indic (project-anuvaad S3 weights) + Tesseract 5.5.2

## Policy
OPEN POLICY (operator directive): read whatever glyphs are on the page — any language, no restriction.
Stack every Indic model we have + English so mixed books (Telugu/Marathi/Hindi/English) all get read.

## Language Models (Anuvaad)
- te: anuvaad_tel
- ta: anuvaad_tam
- kn: anuvaad_kan
- ml: anuvaad_mal

Stack: anuvaad_xxx + hin + eng (fallback to anuvaad_xxx only if stack fails)

## Tessdata Directory
level2/research/smoke/anuvaad_tesseract/tessdata

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Output Format
Level-1-style JSON (same as tesseract_indic)
