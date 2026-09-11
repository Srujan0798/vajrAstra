# LEVEL2 KN B1 slot2 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/kn/kn_021.json ... kn_040.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- kn_021 | work/kn/s_kannada0022pro_raw.pdf | page_index=0 | pdf_pages=144
- kn_022 | work/kn/s_kannada0023pro_raw.pdf | page_index=261 | pdf_pages=1047
- kn_023 | work/kn/s_kannada0024pro_raw.pdf | page_index=32 | pdf_pages=64
- kn_024 | work/kn/s_kannada0025pro_raw.pdf | page_index=66 | pdf_pages=88
- kn_025 | work/kn/s_kannada0026pro_raw.pdf | page_index=63 | pdf_pages=64
- kn_026 | work/kn/s_kannada0027pro_raw.pdf | page_index=0 | pdf_pages=72
- kn_027 | work/kn/s_kannada0028pro_raw.pdf | page_index=16 | pdf_pages=64
- kn_028 | work/kn/s_kannada0029pro_raw.pdf | page_index=32 | pdf_pages=64
- kn_029 | work/kn/s_kannada0030pro_raw.pdf | page_index=54 | pdf_pages=72
- kn_030 | work/kn/s_kannada0031pro_raw.pdf | page_index=79 | pdf_pages=80
- kn_031 | work/kn/s_kannada0032pro_raw.pdf | page_index=0 | pdf_pages=80
- kn_032 | work/kn/s_kannada0033pro_raw.pdf | page_index=20 | pdf_pages=80
- kn_033 | work/kn/s_kannada0034pro_raw.pdf | page_index=52 | pdf_pages=104
- kn_034 | work/kn/s_kannada0035pro_raw.pdf | page_index=99 | pdf_pages=133
- kn_035 | work/kn/s_kannada0036pro_raw.pdf | page_index=132 | pdf_pages=133
- kn_036 | work/kn/s_kannada0037pro_raw.pdf | page_index=0 | pdf_pages=54
- kn_037 | work/kn/s_kannada0038pro_raw.pdf | page_index=108 | pdf_pages=432
- kn_038 | work/kn/s_kannada0039pro_raw.pdf | page_index=258 | pdf_pages=516
- kn_039 | work/kn/s_kannada0040pro_raw.pdf | page_index=712 | pdf_pages=950
- kn_040 | work/kn/s_kannada0041pro_raw.pdf | page_index=106 | pdf_pages=107

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/kn/s_kannada0022pro_raw.pdf --page 0 --dpi 200 --out /tmp/kn_021.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/kn/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "kn_021",
  "source": "S5_govt",
  "lang": "kn",
  "script": "Knda",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/kn/s_kannada0022pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
