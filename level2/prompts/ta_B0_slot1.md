# LEVEL2 TA B0 slot1 — Indian OCR outputs (same Dataset pages)
Paste everything below this line.

---

ROLE
Produce Level-1-style page JSON labels by running an **Indian / Indic OCR engine** on the listed pages.
Operator: Srujan. Language=ta script=Taml.
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
  level2/out/<ENGINE>/ta/

YOUR JOB (this batch only)
Create ALL 20 files from scratch:
level2/out/<ENGINE>/ta/ta_001.json ... ta_020.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ta_001 | work/ta/s_tamil0001pro_raw.png | page_index=0 | pdf_pages=1
- ta_002 | work/ta/s_tamil0002pro_raw.png | page_index=0 | pdf_pages=1
- ta_003 | work/ta/s_tamil0003pro_raw.png | page_index=0 | pdf_pages=1
- ta_004 | work/ta/s_tamil0004pro_raw.png | page_index=0 | pdf_pages=1
- ta_005 | work/ta/s_tamil0005pro_raw.pdf | page_index=11 | pdf_pages=12
- ta_006 | work/ta/s_tamil0006pro_raw.pdf | page_index=0 | pdf_pages=12
- ta_007 | work/ta/s_tamil0007pro_raw.pdf | page_index=3 | pdf_pages=15
- ta_008 | work/ta/s_tamil0008pro_raw.pdf | page_index=3 | pdf_pages=7
- ta_009 | work/ta/s_tamil0009pro_raw.pdf | page_index=0 | pdf_pages=1
- ta_010 | work/ta/s_tamil0010pro_raw.pdf | page_index=13 | pdf_pages=14
- ta_011 | work/ta/s_tamil0011pro_raw.pdf | page_index=0 | pdf_pages=15
- ta_012 | work/ta/s_tamil0012pro_raw.pdf | page_index=3 | pdf_pages=12
- ta_013 | work/ta/s_tamil0013pro_raw.pdf | page_index=13 | pdf_pages=27
- ta_014 | work/ta/s_tamil0014pro_raw.pdf | page_index=13 | pdf_pages=18
- ta_015 | work/ta/s_tamil0015pro_raw.pdf | page_index=129 | pdf_pages=130
- ta_016 | work/ta/s_tamil0016pro_raw.pdf | page_index=0 | pdf_pages=157
- ta_017 | work/ta/s_tamil0017pro_raw.pdf | page_index=4 | pdf_pages=18
- ta_018 | work/ta/s_tamil0018pro_raw.pdf | page_index=8 | pdf_pages=16
- ta_019 | work/ta/s_tamil0019pro_raw.pdf | page_index=210 | pdf_pages=280
- ta_020 | work/ta/s_tamil0020pro_raw.pdf | page_index=367 | pdf_pages=368

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
# open work/ta/s_tamil0001pro_raw.png directly
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ta/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ta_001",
  "source": "S5_govt",
  "lang": "ta",
  "script": "Taml",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ta/s_tamil0001pro_raw.png", "page_index": 0, "width": 1654, "height": 2339},
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
For tesseract_indic, tess language code hint: tam

HALT
page_id | engine | file | page_index | text_chars | json_path
n_files=20 gate=yes
STOP only when gate=yes.
