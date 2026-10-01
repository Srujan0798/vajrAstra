# doctr — PROMPT

## Engine
docTR 1.1.0 (crnn_vgg16_bn)

## Policy
docTR document OCR (OSS). Pretrained predictor.

## Pipeline
1. DocumentFile.from_images()
2. ocr_predictor(pretrained=True)
3. Export nested structure, iterate pages → blocks → lines → words

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)

## Timeout
300s per page, 1 retry with binarized variant

## Output Format
Level-1-style JSON (same as tesseract_indic)
