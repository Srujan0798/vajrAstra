"""Level-2 local engine adapters (thin wrappers over level2/run_engine.py).

Each adapter lazily imports run_engine inside run() — importing this
package never loads OCR models. Engine ids match run_engine.py exactly.
"""
from . import (
    anuvaad_tesseract,
    doctr,
    easyocr,
    indicphotoocr,
    openbharatocr,
    paddleocr_indic,
    rapidocr,
    surya,
    tesseract_bilingual,
    tesseract_indic,
)
