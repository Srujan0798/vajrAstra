# LEVEL2 TA B1 slot2 — Indian OCR outputs (same Dataset pages)
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
level2/out/<ENGINE>/ta/ta_021.json ... ta_040.json
Overwrite if exists. Do not leave any id missing.

SUCCESS GATE
- 20/20 JSON files exist
- each text_chars >= 1 (prefer >=50 if page has text)
- 1 JSON = 1 page only
- width/height not 0; bbox not [0,0,0,0]
- text comes from the OCR engine on that page image (not copied from arc_level_1)

PAGES
- ta_021 | work/ta/s_tamil0021pro_raw.pdf | page_index=0 | pdf_pages=288
- ta_022 | work/ta/s_tamil0022pro_raw.pdf | page_index=68 | pdf_pages=272
- ta_023 | work/ta/s_tamil0023pro_raw.pdf | page_index=160 | pdf_pages=320
- ta_024 | work/ta/s_tamil0024pro_raw.pdf | page_index=234 | pdf_pages=312
- ta_025 | work/ta/s_tamil0025pro_raw.pdf | page_index=335 | pdf_pages=336
- ta_026 | work/ta/s_tamil0026pro_raw.pdf | page_index=0 | pdf_pages=312
- ta_027 | work/ta/s_tamil0027pro_raw.pdf | page_index=82 | pdf_pages=328
- ta_028 | work/ta/s_tamil0028pro_raw.pdf | page_index=172 | pdf_pages=344
- ta_029 | work/ta/s_tamil0029pro_raw.pdf | page_index=216 | pdf_pages=288
- ta_030 | work/ta/s_tamil0030pro_raw.pdf | page_index=327 | pdf_pages=328
- ta_031 | work/ta/s_tamil0031pro_raw.pdf | page_index=0 | pdf_pages=360
- ta_032 | work/ta/s_tamil0032pro_raw.pdf | page_index=84 | pdf_pages=336
- ta_033 | work/ta/s_tamil0033pro_raw.pdf | page_index=120 | pdf_pages=240
- ta_034 | work/ta/s_tamil0034pro_raw.pdf | page_index=174 | pdf_pages=232
- ta_035 | work/ta/s_tamil0035pro_raw.pdf | page_index=311 | pdf_pages=312
- ta_036 | work/ta/s_tamil0036pro_raw.pdf | page_index=0 | pdf_pages=272
- ta_037 | work/ta/s_tamil0037pro_raw.pdf | page_index=84 | pdf_pages=336
- ta_038 | work/ta/s_tamil0038pro_raw.pdf | page_index=144 | pdf_pages=288
- ta_039 | work/ta/s_tamil0005pro_raw.pdf | page_index=9 | pdf_pages=12
- ta_040 | work/ta/s_tamil0006pro_raw.pdf | page_index=11 | pdf_pages=12

HOW
1) Rasterize PDF page or open PNG:
```bash
cd /Users/srujansai/Desktop/South && source .venv/bin/activate
python scripts/rasterize_page.py work/ta/s_tamil0021pro_raw.pdf --page 0 --dpi 200 --out /tmp/ta_021.png
```
2) Run the chosen ENGINE OCR on that image.
3) Write JSON in the Level-1 shape below.
4) If page password/unopenable: substitute next openable page from work/ta/, keep same page_id, set substituted=true.

JSON FORMAT
{
  "page_id": "ta_021",
  "source": "S5_govt",
  "lang": "ta",
  "script": "Taml",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T2",
  "missing": [],
  "unreadable_reason": null,
  "ocr_engine": "<ENGINE>",
  "image": {"raw_path": "work/ta/s_tamil0021pro_raw.pdf", "page_index": 0, "width": 1654, "height": 2339},
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
