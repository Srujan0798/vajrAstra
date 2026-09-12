# PROMPT — paddleocr_indic

prompt_version: L2-SEAL-v2
model_id: paddleocr_indic
invoke: `.venv311/bin/python level2/run_engine.py --engine paddleocr_indic --lang <te|ta|kn|ml> --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/paddleocr_indic/json/<page_id>.json
png_out: level2/models/paddleocr_indic/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: paddleocr 3.7.0 + paddlepaddle 3.3.1 (CPU)
- model routing: te/ta → PP-OCRv5; kn → ka (PP-OCRv3); ml → NO ml model exists in paddleocr 3.7.0 → en fallback (probed 12 Sep, documented honestly) — run_engine.py _PADDLE_LANG
- degrade path: full pipeline (300s) → light retry (mobile det, det input capped 960/max, 900s paddle-only budget); timed-out predictor modes are poisoned, never re-entered
- venv: .venv311 (paddle needs py3.11, not .venv py3.14)
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: ml pages read via en stack only; ~96 s/page (slowest engine); 89 English-leak pages (RUN.md)

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
