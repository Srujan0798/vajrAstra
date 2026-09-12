# PROMPT — indicphotoocr

prompt_version: L2-SEAL-v2
model_id: indicphotoocr
invoke: `.venv311/bin/python level2/run_engine.py --engine indicphotoocr --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/indicphotoocr/json/<page_id>.json
png_out: level2/models/indicphotoocr/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: IndicPhotoOCR 1.3.1 (IIIT-H, editable install from .deps/IndicPhotoOCR)
- init: OCR(verbose=False, identifier_lang="auto", device="cpu") — init once per process; script ID is auto, not page-lang-forced — run_engine.py ocr_indicphotoocr
- venv: .venv311
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: auto script-ID verified working (outputs Devanagari on Devanagari pages — IMPROVEMENTS_CURRENT_WORK.md item 11); ~16 s/page

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
