# LEVEL2 TE B1 slot2 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/te/te_021.json ... te_040.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- te_021 | work/te/s_telugu0021pro_raw.pdf | page_index=0 | pdf_pages=112
- te_022 | work/te/s_telugu0022pro_raw.pdf | page_index=20 | pdf_pages=82
- te_023 | work/te/s_telugu0023pro_raw.pdf | page_index=74 | pdf_pages=148
- te_024 | work/te/s_telugu0024pro_raw.pdf | page_index=36 | pdf_pages=48
- te_025 | work/te/s_telugu0025pro_raw.pdf | page_index=86 | pdf_pages=87
- te_026 | work/te/s_telugu0026pro_raw.pdf | page_index=0 | pdf_pages=100
- te_027 | work/te/s_telugu0027pro_raw.pdf | page_index=29 | pdf_pages=116
- te_028 | work/te/s_telugu0028pro_raw.pdf | page_index=74 | pdf_pages=148
- te_029 | work/te/s_telugu0029pro_raw.pdf | page_index=105 | pdf_pages=140
- te_030 | work/te/s_telugu0030pro_raw.pdf | page_index=91 | pdf_pages=92
- te_031 | work/te/s_telugu0031pro_raw.pdf | page_index=0 | pdf_pages=92
- te_032 | work/te/s_telugu0032pro_raw.pdf | page_index=31 | pdf_pages=124
- te_033 | work/te/s_telugu0033pro_raw.pdf | page_index=48 | pdf_pages=96
- te_034 | work/te/s_telugu0034pro_raw.pdf | page_index=75 | pdf_pages=100
- te_035 | work/te/s_telugu0035pro_raw.pdf | page_index=99 | pdf_pages=100
- te_036 | work/te/s_telugu0036pro_raw.pdf | page_index=0 | pdf_pages=140
- te_037 | work/te/s_telugu0037pro_raw.pdf | page_index=27 | pdf_pages=108
- te_038 | work/te/s_telugu0038pro_raw.pdf | page_index=46 | pdf_pages=92
- te_039 | work/te/s_telugu0039pro_raw.pdf | page_index=75 | pdf_pages=100
- te_040 | work/te/s_telugu0040pro_raw.pdf | page_index=139 | pdf_pages=140

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/te/s_telugu0021pro_raw.pdf --page 0 --dpi 200 --out /tmp/te_021.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/te/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "te_021",
  "source": "S5_govt",
  "lang": "te",
  "script": "Telu",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/te/s_telugu0021pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
