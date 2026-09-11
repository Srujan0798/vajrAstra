# LEVEL2 TA B2 slot3 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ta/ta_041.json ... ta_060.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ta_041 | work/ta/s_tamil0007pro_raw.pdf | page_index=0 | pdf_pages=15
- ta_042 | work/ta/s_tamil0008pro_raw.pdf | page_index=1 | pdf_pages=7
- ta_043 | work/ta/s_tamil0010pro_raw.pdf | page_index=7 | pdf_pages=14
- ta_044 | work/ta/s_tamil0011pro_raw.pdf | page_index=11 | pdf_pages=15
- ta_045 | work/ta/s_tamil0012pro_raw.pdf | page_index=11 | pdf_pages=12
- ta_046 | work/ta/s_tamil0013pro_raw.pdf | page_index=0 | pdf_pages=27
- ta_047 | work/ta/s_tamil0014pro_raw.pdf | page_index=4 | pdf_pages=18
- ta_048 | work/ta/s_tamil0015pro_raw.pdf | page_index=65 | pdf_pages=130
- ta_049 | work/ta/s_tamil0016pro_raw.pdf | page_index=117 | pdf_pages=157
- ta_050 | work/ta/s_tamil0017pro_raw.pdf | page_index=17 | pdf_pages=18
- ta_051 | work/ta/s_tamil0018pro_raw.pdf | page_index=0 | pdf_pages=16
- ta_052 | work/ta/s_tamil0019pro_raw.pdf | page_index=70 | pdf_pages=280
- ta_053 | work/ta/s_tamil0020pro_raw.pdf | page_index=184 | pdf_pages=368
- ta_054 | work/ta/s_tamil0021pro_raw.pdf | page_index=216 | pdf_pages=288
- ta_055 | work/ta/s_tamil0022pro_raw.pdf | page_index=271 | pdf_pages=272
- ta_056 | work/ta/s_tamil0023pro_raw.pdf | page_index=0 | pdf_pages=320
- ta_057 | work/ta/s_tamil0024pro_raw.pdf | page_index=78 | pdf_pages=312
- ta_058 | work/ta/s_tamil0025pro_raw.pdf | page_index=168 | pdf_pages=336
- ta_059 | work/ta/s_tamil0026pro_raw.pdf | page_index=234 | pdf_pages=312
- ta_060 | work/ta/s_tamil0027pro_raw.pdf | page_index=327 | pdf_pages=328

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ta/s_tamil0007pro_raw.pdf --page 0 --dpi 200 --out /tmp/ta_041.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ta/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ta_041",
  "source": "S5_govt",
  "lang": "ta",
  "script": "Taml",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ta/s_tamil0007pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
