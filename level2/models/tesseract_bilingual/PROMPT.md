# PROMPT — tesseract_bilingual

prompt_version: L2-SEAL-v1
model_id: tesseract_bilingual
invoke: `.venv/bin/python level2/run_engine.py --engine tesseract_bilingual --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/tesseract_bilingual/json/<page_id>.json
png_out: level2/models/tesseract_bilingual/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: tesseract 5.5.2 via pytesseract (official GitHub tessdata)
- model stack: bilingual eng + Indic — "eng" + <tel|tam|kan|mal> + hin + eng, deduped (te page → eng+tel+hin) — run_engine.py ocr_tesseract_bilingual
- venv: .venv (py3.14) — tesseract family runs here
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only, never a constraint
- known limits: none engine-specific (see reports/FAILURE_TAXONOMY.md)

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
