# LEVEL2 TA B3 slot4 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ta/ta_061.json ... ta_080.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ta_061 | work/ta/s_tamil0028pro_raw.pdf | page_index=0 | pdf_pages=344
- ta_062 | work/ta/s_tamil0029pro_raw.pdf | page_index=72 | pdf_pages=288
- ta_063 | work/ta/s_tamil0030pro_raw.pdf | page_index=164 | pdf_pages=328
- ta_064 | work/ta/s_tamil0031pro_raw.pdf | page_index=270 | pdf_pages=360
- ta_065 | work/ta/s_tamil0032pro_raw.pdf | page_index=335 | pdf_pages=336
- ta_066 | work/ta/s_tamil0033pro_raw.pdf | page_index=0 | pdf_pages=240
- ta_067 | work/ta/s_tamil0034pro_raw.pdf | page_index=58 | pdf_pages=232
- ta_068 | work/ta/s_tamil0035pro_raw.pdf | page_index=156 | pdf_pages=312
- ta_069 | work/ta/s_tamil0036pro_raw.pdf | page_index=204 | pdf_pages=272
- ta_070 | work/ta/s_tamil0037pro_raw.pdf | page_index=335 | pdf_pages=336
- ta_071 | work/ta/s_tamil0038pro_raw.pdf | page_index=0 | pdf_pages=288
- ta_072 | work/ta/s_tamil0005pro_raw.pdf | page_index=3 | pdf_pages=12
- ta_073 | work/ta/s_tamil0006pro_raw.pdf | page_index=6 | pdf_pages=12
- ta_074 | work/ta/s_tamil0007pro_raw.pdf | page_index=11 | pdf_pages=15
- ta_075 | work/ta/s_tamil0008pro_raw.pdf | page_index=6 | pdf_pages=7
- ta_076 | work/ta/s_tamil0010pro_raw.pdf | page_index=0 | pdf_pages=14
- ta_077 | work/ta/s_tamil0011pro_raw.pdf | page_index=3 | pdf_pages=15
- ta_078 | work/ta/s_tamil0012pro_raw.pdf | page_index=6 | pdf_pages=12
- ta_079 | work/ta/s_tamil0013pro_raw.pdf | page_index=20 | pdf_pages=27
- ta_080 | work/ta/s_tamil0014pro_raw.pdf | page_index=17 | pdf_pages=18

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ta/s_tamil0028pro_raw.pdf --page 0 --dpi 200 --out /tmp/ta_061.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ta/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ta_061",
  "source": "S5_govt",
  "lang": "ta",
  "script": "Taml",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ta/s_tamil0028pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
