# PROMPT — rapidocr

prompt_version: L2-SEAL-v1
model_id: rapidocr
invoke: `.venv311/bin/python level2/run_engine.py --engine rapidocr --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/rapidocr/json/<page_id>.json
png_out: level2/models/rapidocr/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: rapidocr-onnxruntime 1.4.4 (ONNX, CPU)
- models: bundled ch_PP-OCRv4_det_infer.onnx (det) + ch_PP-OCRv4_rec_infer.onnx (rec) + ch_ppocr_mobile_v2.0_cls (cls)
- venv: .venv311
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: recognition model is Latin/Chinese PP-OCRv4 — NO South-Indic script model → 70 English-leak pages, median capture vs PDF layer 0.289 (RUN.md); kept as the honest weak-engine benchmark

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
