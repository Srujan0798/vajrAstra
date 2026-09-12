# PROMPT — doctr

prompt_version: L2-SEAL-v1
model_id: doctr
invoke: `.venv311/bin/python level2/run_engine.py --engine doctr --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/doctr/json/<page_id>.json
png_out: level2/models/doctr/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: python-doctr 1.1.0
- predictor: ocr_predictor(pretrained=True) defaults — detection fast_base, recognition CRNN (crnn_vgg16_bn); no per-language routing
- venv: .venv311
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: default CRNN recognition is Latin-leaning → 263 English-leak pages on Indic-dominant pages (RUN.md); PARSeq backend swap = future work (IMPROVEMENTS_CURRENT_WORK.md item 8), NOT done — no engine change without rerun

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
