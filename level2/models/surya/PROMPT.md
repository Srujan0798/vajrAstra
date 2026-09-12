# PROMPT — surya

prompt_version: L2-SEAL-v1
model_id: surya
invoke: `SURYA_GUIDED_LAYOUT=false .venv311/bin/python level2/run_engine.py --engine surya --skip-existing` (orchestrator.py fill sets this env automatically)
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/surya/json/<page_id>.json
png_out: level2/models/surya/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: surya-ocr 0.22.1 (surya-2 weights)
- mode: block mode — LayoutPredictor → RecognitionPredictor per block (full_page=False); full-page fallback when output <5 chars; block text arrives as HTML (surya-2 VLM html blocks) — harness strips tags to plain text (run_engine.py ocr_surya)
- env: SURYA_GUIDED_LAYOUT=false required (grammar-400 fix; orchestrator.py sets it at spawn)
- venv: .venv311
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: no language-hint parameter in 0.22.1 (IMPROVEMENTS_CURRENT_WORK.md item 7); ~17 s/page (RUN.md)

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
