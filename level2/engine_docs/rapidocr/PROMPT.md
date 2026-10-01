# rapidocr — PROMPT

## Engine
RapidOCR 3.9.x multilingual ONNX, per-language rec models

## Language Models
- te: LangRec.TE, OCRVersion.PPOCRV5
- ta: LangRec.TA, OCRVersion.PPOCRV5
- kn: LangRec.KA, OCRVersion.PPOCRV4
- ml: NO Malayalam model exists → returns honest-empty (no wrong-script mojibake)

## Config
- Rec.model_type: MOBILE
- Det.ocr_version: PPOCRV5, Det.model_type: MOBILE, Det.lang_type: CH
- Cls.use_cls: False

## Image Preprocessing
- Render PDF to PNG at 200 DPI (shared renders)
- On failure: binarize with Otsu threshold (no deskew)

## Timeout
300s per page, 1 retry with binarized variant

## Note
No Malayalam model — ml pages return empty string (honest empty, not mojibake)

## Output Format
Level-1-style JSON (same as tesseract_indic)
