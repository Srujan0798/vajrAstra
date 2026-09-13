"""Single source of truth for engine roster (plan P3-21/P3-22).

Every module that iterates engines imports from here — one list, one
version map, one venv map. Adding an engine = edit this file only.
(law: counts from disk; roster from config; never hand-duplicated again)
"""
from __future__ import annotations

ENGINES = [
    "tesseract_indic",
    "openbharatocr",
    "easyocr",
    "paddleocr_indic",
    "indicphotoocr",
    "rapidocr",
    "tesseract_bilingual",
    "doctr",
    "surya",
    "anuvaad_tesseract",
]

# tesseract-family = byte-identical mirrors (one family, one vote in family consensus)
TESSERACT_FAMILY = ["tesseract_indic", "openbharatocr", "anuvaad_tesseract", "tesseract_bilingual"]

# engine -> version string (union of seal_gen + run_engine maps; run_engine's
# rapidocr string kept here verbatim as RUNTIME_VERSIONS override below —
# the sealed RUN.md labels diverge intentionally: disk-truth labels per consumer)
ENGINE_VERSIONS = {
    "tesseract_indic": "tesseract 5.5.2 (tel+hin+eng open stack)",
    "openbharatocr": "openbharatocr 0.4.3 (tesseract mirror path documented)",
    "easyocr": "easyocr 1.7.2 (all-Indic open reader)",
    "paddleocr_indic": "paddleocr 3.7.0 / paddlepaddle 3.3.1",
    "indicphotoocr": "IndicPhotoOCR IIIT-H (parseq trust-patched)",
    "rapidocr": "rapidocr 3.9.2 (per-lang PP-OCRv5/v4 mobile rec; te/ta/kn+dev; ml=no model->honest empty)",
    "tesseract_bilingual": "tesseract 5.5.2 (eng+stack bilingual)",
    "doctr": "python-doctr 1.1.0 (crnn_vgg16_bn)",
    "surya": "surya-ocr 0.22.1 (surya-2, block-mode html)",
    "anuvaad_tesseract": "anuvaad tessdata + tesseract 5.5.2",
}

# run_engine's runtime labels (rapidocr onnxruntime build differs from seal label;
# stub engines exist only in the runner for future wiring — not in the sealed 10)
RUNTIME_ENGINE_VERSIONS = dict(ENGINE_VERSIONS)
RUNTIME_ENGINE_VERSIONS["rapidocr"] = "rapidocr-onnxruntime 1.4.4"
RUNTIME_ENGINE_VERSIONS["sarvam_api"] = "Sarvam Vision 1.5 (doc-ai digitise API; dry-run until SARVAM_API_KEY)"
RUNTIME_ENGINE_VERSIONS["bhashini_api"] = "Bhashini/ULCA OCR (adapter dry-run; endpoint TODO-VERIFY)"

