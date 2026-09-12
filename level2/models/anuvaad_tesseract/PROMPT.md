# PROMPT — anuvaad_tesseract

prompt_version: L2-SEAL-v1
model_id: anuvaad_tesseract
invoke: `.venv/bin/python level2/run_engine.py --engine anuvaad_tesseract --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/anuvaad_tesseract/json/<page_id>.json
png_out: level2/models/anuvaad_tesseract/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: tesseract 5.5.2 + project-anuvaad tessdata (anuvaad_tel/tam/kan/mal traineddata in level2/research/smoke/anuvaad_tesseract/tessdata/)
- model stack: anuvaad_<lang>+hin+eng; on stack failure falls back to anuvaad_<lang> alone — run_engine.py ocr_anuvaad_tesseract
- venv: .venv (py3.14) — tesseract family runs here
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: anuvaad weights cover te/ta/kn/ml only; hin/eng read via the fallback stack

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
