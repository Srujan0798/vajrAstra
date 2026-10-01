# surya — PROMPT

## Engine
Surya OCR 0.22.1 (surya-2, block-mode html)

## Policy
Multilingual document OCR (OSS). Block mode: layout → per-block recognition.
Blocks carry HTML text (surya-2 model), so we extract text from html.

## Language Support
All four South Indian scripts: te, ta, kn, ml (explicit codes in multilingual eval)
Full-page OCR + layout + reading order + tables in one ~650M VLM

## Pipeline
1. LayoutPredictor() → layout blocks
2. RecognitionPredictor() with layout_results, full_page=False (block mode)
3. Extract text from block.html (strip tags)
4. Fallback: full_page=True if block mode yields <5 chars

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- Convert to RGB for Surya

## Timeout
300s per page, 1 retry with binarized variant

## License Caveat
Code: Apache-2.0
Model weights: modified AI Pubs OpenRAIL-M — FREE for research, personal use, and startups under ~$5M funding/revenue; NOT free for large commercial/competitive-with-Datalab-API use without paid weight license.

## Output Format
Level-1-style JSON (same as tesseract_indic)
