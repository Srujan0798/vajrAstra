# LEVEL2 TE B2 slot3 — Indian OCR outputs (same Dataset pages)
Paste everything below this line.

---

ROLE
Produce Level-1-style page JSON labels by running an **Indian / Indic OCR engine** on the listed pages.
Operator: Srujan. Language=te script=Telu.
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
  level2/out/<ENGINE>/te/

YOUR JOB (this batch only)
Create ALL 20 files from scratch:
level2/out/<ENGINE>/te/te_041.json ... te_060.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- te_041 | work/te/s_telugu0041pro_raw.pdf | page_index=0 | pdf_pages=66
- te_042 | work/te/s_telugu0042pro_raw.pdf | page_index=12 | pdf_pages=50
- te_043 | work/te/s_telugu0043pro_raw.pdf | page_index=33 | pdf_pages=66
- te_044 | work/te/s_telugu0044pro_raw.pdf | page_index=37 | pdf_pages=50
- te_045 | work/te/s_telugu0045pro_raw.pdf | page_index=147 | pdf_pages=148
- te_046 | work/te/s_telugu0046pro_raw.pdf | page_index=0 | pdf_pages=66
- te_047 | work/te/s_telugu0047pro_raw.pdf | page_index=24 | pdf_pages=98
- te_048 | work/te/s_telugu0048pro_raw.pdf | page_index=50 | pdf_pages=100
- te_049 | work/te/s_telugu0049pro_raw.pdf | page_index=78 | pdf_pages=104
- te_050 | work/te/s_telugu0050pro_raw.pdf | page_index=99 | pdf_pages=100
- te_051 | work/te/s_telugu0051pro_raw.pdf | page_index=0 | pdf_pages=124
- te_052 | work/te/s_telugu0052pro_raw.pdf | page_index=36 | pdf_pages=144
- te_053 | work/te/s_telugu0053pro_raw.pdf | page_index=70 | pdf_pages=140
- te_054 | work/te/s_telugu0054pro_raw.pdf | page_index=87 | pdf_pages=116
- te_055 | work/te/s_telugu0055pro_raw.pdf | page_index=171 | pdf_pages=172
- te_056 | work/te/s_telugu0056pro_raw.pdf | page_index=0 | pdf_pages=50
- te_057 | work/te/s_telugu0057pro_raw.pdf | page_index=16 | pdf_pages=66
- te_058 | work/te/s_telugu0058pro_raw.pdf | page_index=62 | pdf_pages=124
- te_059 | work/te/s_telugu0059pro_raw.pdf | page_index=87 | pdf_pages=116
- te_060 | work/te/s_telugu0060pro_raw.pdf | page_index=115 | pdf_pages=116

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/te/s_telugu0041pro_raw.pdf --page 0 --dpi 200 --out /tmp/te_041.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/te/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "te_041",
  "source": "S5_govt",
  "lang": "te",
  "script": "Telu",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/te/s_telugu0041pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
For tesseract_indic, tess language code hint: tel

HALT
page_id | engine | file | page_index | text_chars | json_path
n_files=20 gate=yes
STOP only when gate=yes.
