# PROMPT — easyocr

prompt_version: L2-SEAL-v2
model_id: easyocr
invoke: `.venv311/bin/python level2/run_engine.py --engine easyocr --skip-existing`
shared_pages: level2/pages_400/ (400 page_ids)
json_out: level2/models/easyocr/json/<page_id>.json
png_out: level2/models/easyocr/png/<page_id>.png

ENGINE CONTRACT (documented; Level 2 sends NO prompts to engines — engines are programs):
- engine + version: easyocr 1.7.2 (CPU, gpu=False)
- model strategy: per-script readers, longest output wins — readers te+en, ta+en, kn+en, hi+mr+ne+en (validated 12 Sep: Dravidian models are pairwise-incompatible — te/ta/kn only work with en; Devanagari family hi+mr+ne bundles work) — run_engine.py ocr_easyocr
- quirk patch: run_engine.py patches easyocr 1.7 tamil.pth charset (143 classes vs 126 bundled) before reader init
- venv: .venv311
- policy: OPEN — any script, any page (operator directive 12 Sep 2026); page lang tag = ID label only
- known limits: reader combos must be valid or Reader() raises ValueError (this killed the first all-Indic reader attempt — kept per-script readers instead); current fill status 0/400 (LEADERBOARD.md)

MAX RAW OUTPUT rules (not gold):
- Use this engine only; do not copy arc_level_1
- Force page language/script; do NOT translate to English
- Do NOT describe the page; put OCR text in JSON only
- If unread: use [UNREAD], not an English essay
- Keep native digits; never spell-correct into "proper" language
- 1 JSON = 1 page
