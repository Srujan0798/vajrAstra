# LEVEL2 ML B0 slot1 — Indian OCR outputs (same Dataset pages)
Paste everything below this line.

---

ROLE
Produce Level-1-style page JSON labels by running an **Indian / Indic OCR engine** on the listed pages.
Operator: Srujan. Language=ml script=Mlym.
Workspace: /Users/srujansai/Desktop/South
This is Level 2: OCR-model outputs on the same data (for benchmarks). Not chat invention.


ENGINES (OSS first — run ONE engine per assignment)
1) tesseract_indic
2) indicphotoocr
3) openbharatocr
4) paddleocr_indic
5) easyocr

Output root for this engine:
  level2/out/<ENGINE>/{te,ta,kn,ml}/<page_id>.json


BEFORE YOU START
Set ENGINE to exactly one of:
tesseract_indic | indicphotoocr | openbharatocr | paddleocr_indic | easyocr
Write all outputs under:
  level2/out/<ENGINE>/ml/

YOUR JOB (this batch only)
Create ALL 20 files from scratch:
level2/out/<ENGINE>/ml/ml_001.json ... ml_020.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ml_001 | work/ml/s_malayalam0001pro_raw.pdf | page_index=0 | pdf_pages=3
- ml_002 | work/ml/s_malayalam0002pro_raw.pdf | page_index=1 | pdf_pages=3
- ml_003 | work/ml/s_malayalam0004pro_raw.pdf | page_index=7 | pdf_pages=15
- ml_004 | work/ml/s_malayalam0005pro_raw.png | page_index=0 | pdf_pages=1
- ml_005 | work/ml/s_malayalam0006pro_raw.png | page_index=0 | pdf_pages=1
- ml_006 | work/ml/s_malayalam0007pro_raw.png | page_index=0 | pdf_pages=1
- ml_007 | work/ml/s_malayalam0008pro_raw.png | page_index=0 | pdf_pages=1
- ml_008 | work/ml/s_malayalam0009pro_raw.png | page_index=0 | pdf_pages=1
- ml_009 | work/ml/s_malayalam0010pro_raw.png | page_index=0 | pdf_pages=1
- ml_010 | work/ml/s_malayalam0011pro_raw.png | page_index=0 | pdf_pages=1
- ml_011 | work/ml/s_malayalam0012pro_raw.png | page_index=0 | pdf_pages=1
- ml_012 | work/ml/s_malayalam0013pro_raw.png | page_index=0 | pdf_pages=1
- ml_013 | work/ml/s_malayalam0014pro_raw.pdf | page_index=16 | pdf_pages=32
- ml_014 | work/ml/s_malayalam0015pro_raw.pdf | page_index=89 | pdf_pages=119
- ml_015 | work/ml/s_malayalam0016pro_raw.pdf | page_index=240 | pdf_pages=241
- ml_016 | work/ml/s_malayalam0017pro_raw.pdf | page_index=0 | pdf_pages=64
- ml_017 | work/ml/s_malayalam0018pro_raw.pdf | page_index=13 | pdf_pages=52
- ml_018 | work/ml/s_malayalam0019pro_raw.pdf | page_index=94 | pdf_pages=188
- ml_019 | work/ml/s_malayalam0020pro_raw.pdf | page_index=6 | pdf_pages=9
- ml_020 | work/ml/s_malayalam0021pro_raw.pdf | page_index=461 | pdf_pages=462

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ml/s_malayalam0001pro_raw.pdf --page 0 --dpi 200 --out /tmp/ml_001.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ml/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ml_001",
  "source": "S5_govt",
  "lang": "ml",
  "script": "Mlym",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ml/s_malayalam0001pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
  "regions": [{
    "region_id": "r1",
    "cls": "paragraph",
    "bbox_xyxy": [0, 0, 1654, 2339],
    "reading_order": 1,
    "modality": "printed",
    "text": "OCR text from this page",
    "text_nfc": "NFC of text",
    "provenance": "distilled_vlm"
  }]
}
For tesseract_indic, tess language code hint: mal

HALT
page_id | engine | file | page_index | text_chars | json_path
n_files=20 gate=yes
STOP only when gate=yes.
