# LEVEL2 TE B3 slot4 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/te/te_061.json ... te_080.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- te_061 | work/te/s_telugu0061pro_raw.pdf | page_index=0 | pdf_pages=92
- te_062 | work/te/s_telugu0062pro_raw.pdf | page_index=38 | pdf_pages=152
- te_063 | work/te/s_telugu0063pro_raw.pdf | page_index=33 | pdf_pages=66
- te_064 | work/te/s_telugu0064pro_raw.pdf | page_index=43 | pdf_pages=58
- te_065 | work/te/s_telugu0065pro_raw.pdf | page_index=65 | pdf_pages=66
- te_066 | work/te/s_telugu0066pro_raw.pdf | page_index=0 | pdf_pages=58
- te_067 | work/te/s_telugu0067pro_raw.pdf | page_index=29 | pdf_pages=116
- te_068 | work/te/s_telugu0068pro_raw.pdf | page_index=29 | pdf_pages=58
- te_069 | work/te/s_telugu0069pro_raw.pdf | page_index=43 | pdf_pages=58
- te_070 | work/te/s_telugu0070pro_raw.pdf | page_index=99 | pdf_pages=100
- te_071 | work/te/s_telugu0071pro_raw.pdf | page_index=0 | pdf_pages=116
- te_072 | work/te/s_telugu0072pro_raw.pdf | page_index=33 | pdf_pages=132
- te_073 | work/te/s_telugu0073pro_raw.pdf | page_index=44 | pdf_pages=88
- te_074 | work/te/s_telugu0074pro_raw.pdf | page_index=111 | pdf_pages=148
- te_075 | work/te/s_telugu0075pro_raw.pdf | page_index=65 | pdf_pages=66
- te_076 | work/te/s_telugu0076pro_raw.pdf | page_index=0 | pdf_pages=66
- te_077 | work/te/s_telugu0077pro_raw.pdf | page_index=37 | pdf_pages=148
- te_078 | work/te/s_telugu0078pro_raw.pdf | page_index=74 | pdf_pages=148
- te_079 | work/te/s_telugu0079pro_raw.pdf | page_index=105 | pdf_pages=140
- te_080 | work/te/s_telugu0080pro_raw.pdf | page_index=127 | pdf_pages=128

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/te/s_telugu0061pro_raw.pdf --page 0 --dpi 200 --out /tmp/te_061.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/te/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "te_061",
  "source": "S5_govt",
  "lang": "te",
  "script": "Telu",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/te/s_telugu0061pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
