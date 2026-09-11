# LEVEL2 KN B3 slot4 — Indian OCR outputs (same Dataset pages)
Paste everything below this line.

---

ROLE
Produce Level-1-style page JSON labels by running an **Indian / Indic OCR engine** on the listed pages.
Operator: Srujan. Language=kn script=Knda.
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
  level2/out/<ENGINE>/kn/

YOUR JOB (this batch only)
Create ALL 20 files from scratch:
level2/out/<ENGINE>/kn/kn_061.json ... kn_080.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- kn_061 | work/kn/s_kannada0022pro_raw.pdf | page_index=36 | pdf_pages=144
- kn_062 | work/kn/s_kannada0023pro_raw.pdf | page_index=523 | pdf_pages=1047
- kn_063 | work/kn/s_kannada0024pro_raw.pdf | page_index=48 | pdf_pages=64
- kn_064 | work/kn/s_kannada0025pro_raw.pdf | page_index=87 | pdf_pages=88
- kn_065 | work/kn/s_kannada0026pro_raw.pdf | page_index=0 | pdf_pages=64
- kn_066 | work/kn/s_kannada0027pro_raw.pdf | page_index=18 | pdf_pages=72
- kn_067 | work/kn/s_kannada0028pro_raw.pdf | page_index=32 | pdf_pages=64
- kn_068 | work/kn/s_kannada0029pro_raw.pdf | page_index=48 | pdf_pages=64
- kn_069 | work/kn/s_kannada0030pro_raw.pdf | page_index=71 | pdf_pages=72
- kn_070 | work/kn/s_kannada0031pro_raw.pdf | page_index=0 | pdf_pages=80
- kn_071 | work/kn/s_kannada0032pro_raw.pdf | page_index=20 | pdf_pages=80
- kn_072 | work/kn/s_kannada0033pro_raw.pdf | page_index=40 | pdf_pages=80
- kn_073 | work/kn/s_kannada0034pro_raw.pdf | page_index=78 | pdf_pages=104
- kn_074 | work/kn/s_kannada0035pro_raw.pdf | page_index=132 | pdf_pages=133
- kn_075 | work/kn/s_kannada0036pro_raw.pdf | page_index=0 | pdf_pages=133
- kn_076 | work/kn/s_kannada0037pro_raw.pdf | page_index=13 | pdf_pages=54
- kn_077 | work/kn/s_kannada0038pro_raw.pdf | page_index=216 | pdf_pages=432
- kn_078 | work/kn/s_kannada0039pro_raw.pdf | page_index=387 | pdf_pages=516
- kn_079 | work/kn/s_kannada0040pro_raw.pdf | page_index=949 | pdf_pages=950
- kn_080 | work/kn/s_kannada0041pro_raw.pdf | page_index=0 | pdf_pages=107

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/kn/s_kannada0022pro_raw.pdf --page 36 --dpi 200 --out /tmp/kn_061.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/kn/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "kn_061",
  "source": "S5_govt",
  "lang": "kn",
  "script": "Knda",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/kn/s_kannada0022pro_raw.pdf", "page_index": 36, "width": 1654, "height": 2339},
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
For tesseract_indic, tess language code hint: kan

HALT
page_id | engine | file | page_index | text_chars | json_path
n_files=20 gate=yes
STOP only when gate=yes.
