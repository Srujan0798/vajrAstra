# LEVEL2 KN B4 slot5 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/kn/kn_081.json ... kn_100.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- kn_081 | work/kn/s_kannada0001pro_raw.pdf | page_index=12 | pdf_pages=24
- kn_082 | work/kn/s_kannada0002pro_raw.pdf | page_index=18 | pdf_pages=24
- kn_083 | work/kn/s_kannada0003pro_raw.pdf | page_index=23 | pdf_pages=24
- kn_084 | work/kn/s_kannada0004pro_raw.pdf | page_index=0 | pdf_pages=24
- kn_085 | work/kn/s_kannada0005pro_raw.pdf | page_index=4 | pdf_pages=16
- kn_086 | work/kn/s_kannada0006pro_raw.pdf | page_index=2 | pdf_pages=5
- kn_087 | work/kn/s_kannada0007pro_raw.pdf | page_index=3 | pdf_pages=5
- kn_088 | work/kn/s_kannada0009pro_raw.pdf | page_index=18 | pdf_pages=19
- kn_089 | work/kn/s_kannada0010pro_raw.pdf | page_index=1 | pdf_pages=3
- kn_090 | work/kn/s_kannada0013pro_raw.pdf | page_index=9 | pdf_pages=10
- kn_091 | work/kn/s_kannada0014pro_raw.pdf | page_index=0 | pdf_pages=43
- kn_092 | work/kn/s_kannada0015pro_raw.pdf | page_index=7 | pdf_pages=28
- kn_093 | work/kn/s_kannada0016pro_raw.pdf | page_index=250 | pdf_pages=500
- kn_094 | work/kn/s_kannada0017pro_raw.pdf | page_index=49 | pdf_pages=66
- kn_095 | work/kn/s_kannada0018pro_raw.pdf | page_index=225 | pdf_pages=226
- kn_096 | work/kn/s_kannada0019pro_raw.pdf | page_index=0 | pdf_pages=168
- kn_097 | work/kn/s_kannada0020pro_raw.pdf | page_index=34 | pdf_pages=136
- kn_098 | work/kn/s_kannada0021pro_raw.pdf | page_index=76 | pdf_pages=152
- kn_099 | work/kn/s_kannada0022pro_raw.pdf | page_index=108 | pdf_pages=144
- kn_100 | work/kn/s_kannada0023pro_raw.pdf | page_index=1046 | pdf_pages=1047

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/kn/s_kannada0001pro_raw.pdf --page 12 --dpi 200 --out /tmp/kn_081.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/kn/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "kn_081",
  "source": "S5_govt",
  "lang": "kn",
  "script": "Knda",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/kn/s_kannada0001pro_raw.pdf", "page_index": 12, "width": 1654, "height": 2339},
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
