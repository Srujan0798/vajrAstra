# LEVEL2 TE B0 slot1 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/te/te_001.json ... te_020.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- te_001 | work/te/s_telugu0001pro_raw.pdf | page_index=0 | pdf_pages=4
- te_002 | work/te/s_telugu0002pro_raw.pdf | page_index=4 | pdf_pages=16
- te_003 | work/te/s_telugu0003pro_raw.pdf | page_index=9 | pdf_pages=19
- te_004 | work/te/s_telugu0004pro_raw.pdf | page_index=12 | pdf_pages=16
- te_005 | work/te/s_telugu0005pro_raw.pdf | page_index=18 | pdf_pages=19
- te_006 | work/te/s_telugu0006pro_raw.pdf | page_index=0 | pdf_pages=16
- te_007 | work/te/s_telugu0007pro_raw.pdf | page_index=1 | pdf_pages=7
- te_008 | work/te/s_telugu0008pro_raw.pdf | page_index=3 | pdf_pages=7
- te_009 | work/te/s_telugu0009pro_raw.pdf | page_index=27 | pdf_pages=36
- te_010 | work/te/s_telugu0010pro_raw.pdf | page_index=63 | pdf_pages=64
- te_011 | work/te/s_telugu0011pro_raw.pdf | page_index=0 | pdf_pages=74
- te_012 | work/te/s_telugu0012pro_raw.pdf | page_index=47 | pdf_pages=188
- te_013 | work/te/s_telugu0013pro_raw.pdf | page_index=32 | pdf_pages=64
- te_014 | work/te/s_telugu0014pro_raw.pdf | page_index=49 | pdf_pages=66
- te_015 | work/te/s_telugu0015pro_raw.pdf | page_index=155 | pdf_pages=156
- te_016 | work/te/s_telugu0016pro_raw.pdf | page_index=0 | pdf_pages=132
- te_017 | work/te/s_telugu0017pro_raw.pdf | page_index=47 | pdf_pages=188
- te_018 | work/te/s_telugu0018pro_raw.pdf | page_index=90 | pdf_pages=180
- te_019 | work/te/s_telugu0019pro_raw.pdf | page_index=93 | pdf_pages=124
- te_020 | work/te/s_telugu0020pro_raw.pdf | page_index=85 | pdf_pages=86

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/te/s_telugu0001pro_raw.pdf --page 0 --dpi 200 --out /tmp/te_001.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/te/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "te_001",
  "source": "S5_govt",
  "lang": "te",
  "script": "Telu",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/te/s_telugu0001pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
