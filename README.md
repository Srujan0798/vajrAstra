# vajrAstra — Vaultstack / BHASHINI AksharDrishti (South track)

Private working repo for **Srujan Sai** (Vaultstack AI) on South Indian document OCR.

## What this repo contains

- `SOUTH_CANON.md` — project rules / labeling law
- `scripts/` — inventory, rasterize, verify helpers
- `level2/` — Indian OCR benchmark **code + 20 batch prompts**
  - `run_engine.py` — run an OCR engine over the same page set → JSON packs
  - `prompts/` — batch prompts (te/ta/kn/ml × B0–B4)
  - `pages_manifest.json` — 400 page targets

## What is NOT in git (local / Drive only)

- `work/` — source Dataset pages (PDFs/PNGs)
- `arc_level_1/` — Level-1 draft labels archive
- `level2/out/` — OCR engine JSON outputs (benchmarks)
- `.venv/` / `.venv311/` — local environments

Vinay rule: **GitHub is for code/pipeline, not multi-GB data dumps.**

## Level 2 (current)

Same Dataset pages → Indic OCR engines → JSON outputs as benchmarks:

1. `tesseract_indic`
2. `easyocr`
3. `openbharatocr`
4. `indicphotoocr`
5. `paddleocr_indic`

See `level2/HOW_TO_RUN.txt` and `level2/EXPLAIN_FOR_SRUJAN.txt`.

## Quick start (code only)

```bash
python3.11 -m venv .venv311
source .venv311/bin/activate
pip install pymupdf pillow pytesseract easyocr paddlepaddle paddleocr

# after local work/ + pages_manifest exist:
python level2/run_engine.py --engine tesseract_indic --skip-existing
```
