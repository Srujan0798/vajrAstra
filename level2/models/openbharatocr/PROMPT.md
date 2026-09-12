# PROMPT — openbharatocr

prompt_version: L2-SEAL-v2
model_id: openbharatocr
invoke: `.venv311/bin/python level2/run_engine.py --engine openbharatocr --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/openbharatocr/json/<page_id>.json
png_out: level2/models/openbharatocr/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: openbharatocr 0.4.3 pip package
- DECISION (external review item 8, 13 Sep 2026): openbharatocr = documented alias of tesseract_indic (full-page mode). The packaged OpenBharatOCR pip API covers ID cards only (aadhaar/pan/passport/voter — probed 12 Sep, no full-page API); run_engine.py ocr_openbharatocr returns ocr_tesseract_indic output for full pages. EXCLUDE from independent consensus math; count as tesseract-family.
- family: tesseract-family = {tesseract_indic, tesseract_bilingual, anuvaad_tesseract, openbharatocr}; this engine mirrors tesseract_indic exactly (LEADERBOARD.md shows identical 441812 total chars)
- venv: .venv311 (invoke runs the tesseract path via .venv311 per seal_gen.py mapping)
- policy: OPEN — any script, any page; page lang tag = ID label only
- known limits: NOT an independent engine signal — its 400 packs are tesseract_indic's full-page path re-labeled (kept per benchmark-completeness rule)

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
