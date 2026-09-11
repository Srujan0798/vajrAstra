# LEVEL2 ML B1 slot2 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ml/ml_021.json ... ml_040.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ml_021 | work/ml/s_malayalam0022pro_raw.pdf | page_index=0 | pdf_pages=138
- ml_022 | work/ml/s_malayalam0023pro_raw.pdf | page_index=12 | pdf_pages=48
- ml_023 | work/ml/s_malayalam0024pro_raw.pdf | page_index=157 | pdf_pages=314
- ml_024 | work/ml/s_malayalam0025pro_raw.pdf | page_index=154 | pdf_pages=206
- ml_025 | work/ml/s_malayalam0026pro_raw.pdf | page_index=199 | pdf_pages=200
- ml_026 | work/ml/s_malayalam0027pro_raw.pdf | page_index=0 | pdf_pages=114
- ml_027 | work/ml/s_malayalam0028pro_raw.pdf | page_index=31 | pdf_pages=124
- ml_028 | work/ml/s_malayalam0029pro_raw.pdf | page_index=3 | pdf_pages=7
- ml_029 | work/ml/s_malayalam0001pro_raw.pdf | page_index=1 | pdf_pages=3
- ml_030 | work/ml/s_malayalam0002pro_raw.pdf | page_index=2 | pdf_pages=3
- ml_031 | work/ml/s_malayalam0004pro_raw.pdf | page_index=0 | pdf_pages=15
- ml_032 | work/ml/s_malayalam0014pro_raw.pdf | page_index=8 | pdf_pages=32
- ml_033 | work/ml/s_malayalam0015pro_raw.pdf | page_index=59 | pdf_pages=119
- ml_034 | work/ml/s_malayalam0016pro_raw.pdf | page_index=180 | pdf_pages=241
- ml_035 | work/ml/s_malayalam0017pro_raw.pdf | page_index=63 | pdf_pages=64
- ml_036 | work/ml/s_malayalam0018pro_raw.pdf | page_index=0 | pdf_pages=52
- ml_037 | work/ml/s_malayalam0019pro_raw.pdf | page_index=47 | pdf_pages=188
- ml_038 | work/ml/s_malayalam0020pro_raw.pdf | page_index=4 | pdf_pages=9
- ml_039 | work/ml/s_malayalam0021pro_raw.pdf | page_index=346 | pdf_pages=462
- ml_040 | work/ml/s_malayalam0022pro_raw.pdf | page_index=137 | pdf_pages=138

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ml/s_malayalam0022pro_raw.pdf --page 0 --dpi 200 --out /tmp/ml_021.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ml/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ml_021",
  "source": "S5_govt",
  "lang": "ml",
  "script": "Mlym",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ml/s_malayalam0022pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
