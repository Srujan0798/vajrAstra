# LEVEL2 TA B4 slot5 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ta/ta_081.json ... ta_100.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ta_081 | work/ta/s_tamil0015pro_raw.pdf | page_index=0 | pdf_pages=130
- ta_082 | work/ta/s_tamil0016pro_raw.pdf | page_index=39 | pdf_pages=157
- ta_083 | work/ta/s_tamil0017pro_raw.pdf | page_index=9 | pdf_pages=18
- ta_084 | work/ta/s_tamil0018pro_raw.pdf | page_index=12 | pdf_pages=16
- ta_085 | work/ta/s_tamil0019pro_raw.pdf | page_index=279 | pdf_pages=280
- ta_086 | work/ta/s_tamil0020pro_raw.pdf | page_index=0 | pdf_pages=368
- ta_087 | work/ta/s_tamil0021pro_raw.pdf | page_index=72 | pdf_pages=288
- ta_088 | work/ta/s_tamil0022pro_raw.pdf | page_index=136 | pdf_pages=272
- ta_089 | work/ta/s_tamil0023pro_raw.pdf | page_index=240 | pdf_pages=320
- ta_090 | work/ta/s_tamil0024pro_raw.pdf | page_index=311 | pdf_pages=312
- ta_091 | work/ta/s_tamil0025pro_raw.pdf | page_index=0 | pdf_pages=336
- ta_092 | work/ta/s_tamil0026pro_raw.pdf | page_index=78 | pdf_pages=312
- ta_093 | work/ta/s_tamil0027pro_raw.pdf | page_index=164 | pdf_pages=328
- ta_094 | work/ta/s_tamil0028pro_raw.pdf | page_index=258 | pdf_pages=344
- ta_095 | work/ta/s_tamil0029pro_raw.pdf | page_index=287 | pdf_pages=288
- ta_096 | work/ta/s_tamil0030pro_raw.pdf | page_index=0 | pdf_pages=328
- ta_097 | work/ta/s_tamil0031pro_raw.pdf | page_index=90 | pdf_pages=360
- ta_098 | work/ta/s_tamil0032pro_raw.pdf | page_index=168 | pdf_pages=336
- ta_099 | work/ta/s_tamil0033pro_raw.pdf | page_index=180 | pdf_pages=240
- ta_100 | work/ta/s_tamil0034pro_raw.pdf | page_index=231 | pdf_pages=232

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ta/s_tamil0015pro_raw.pdf --page 0 --dpi 200 --out /tmp/ta_081.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ta/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ta_081",
  "source": "S5_govt",
  "lang": "ta",
  "script": "Taml",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ta/s_tamil0015pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
