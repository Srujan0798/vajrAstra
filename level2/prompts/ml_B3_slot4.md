# LEVEL2 ML B3 slot4 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ml/ml_061.json ... ml_080.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ml_061 | work/ml/s_malayalam0024pro_raw.pdf | page_index=0 | pdf_pages=314
- ml_062 | work/ml/s_malayalam0025pro_raw.pdf | page_index=51 | pdf_pages=206
- ml_063 | work/ml/s_malayalam0026pro_raw.pdf | page_index=100 | pdf_pages=200
- ml_064 | work/ml/s_malayalam0027pro_raw.pdf | page_index=85 | pdf_pages=114
- ml_065 | work/ml/s_malayalam0028pro_raw.pdf | page_index=123 | pdf_pages=124
- ml_066 | work/ml/s_malayalam0029pro_raw.pdf | page_index=0 | pdf_pages=7
- ml_067 | work/ml/s_malayalam0004pro_raw.pdf | page_index=3 | pdf_pages=15
- ml_068 | work/ml/s_malayalam0014pro_raw.pdf | page_index=24 | pdf_pages=32
- ml_069 | work/ml/s_malayalam0015pro_raw.pdf | page_index=118 | pdf_pages=119
- ml_070 | work/ml/s_malayalam0016pro_raw.pdf | page_index=0 | pdf_pages=241
- ml_071 | work/ml/s_malayalam0017pro_raw.pdf | page_index=16 | pdf_pages=64
- ml_072 | work/ml/s_malayalam0018pro_raw.pdf | page_index=26 | pdf_pages=52
- ml_073 | work/ml/s_malayalam0019pro_raw.pdf | page_index=141 | pdf_pages=188
- ml_074 | work/ml/s_malayalam0020pro_raw.pdf | page_index=8 | pdf_pages=9
- ml_075 | work/ml/s_malayalam0021pro_raw.pdf | page_index=0 | pdf_pages=462
- ml_076 | work/ml/s_malayalam0022pro_raw.pdf | page_index=34 | pdf_pages=138
- ml_077 | work/ml/s_malayalam0023pro_raw.pdf | page_index=24 | pdf_pages=48
- ml_078 | work/ml/s_malayalam0024pro_raw.pdf | page_index=235 | pdf_pages=314
- ml_079 | work/ml/s_malayalam0025pro_raw.pdf | page_index=205 | pdf_pages=206
- ml_080 | work/ml/s_malayalam0026pro_raw.pdf | page_index=0 | pdf_pages=200

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ml/s_malayalam0024pro_raw.pdf --page 0 --dpi 200 --out /tmp/ml_061.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ml/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ml_061",
  "source": "S5_govt",
  "lang": "ml",
  "script": "Mlym",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ml/s_malayalam0024pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
