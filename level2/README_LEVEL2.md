# Level 2 — Indian OCR benchmark outputs (Vaultstack / vajrAstra)

## Mission
Run free Indic OCR engines on the **same 400 South pages** used in Level 1.  
Save Level-1-style JSON packs. Those packs = **benchmarks**.  
Later (Level 3): paid/top Indian APIs. Later still: train Vaultstack on gaps.

**Success metric now:** max flushed OCR text packs (coverage + nonempty rate),  
**not** perfect human-gold accuracy.

## Engines (core 5)

| Engine | Folder | Status target |
|--------|--------|---------------|
| tesseract_indic | `out/tesseract_indic/` | 400 JSON |
| easyocr | `out/easyocr/` | 400 JSON |
| openbharatocr | `out/openbharatocr/` | 400 JSON (note: full-page path may mirror Tesseract) |
| indicphotoocr | `out/indicphotoocr/` | 400 JSON |
| paddleocr_indic | `out/paddleocr_indic/` | 400 JSON |

Optional +3 (research): **Surya**, **docTR**, **Indic-OCR tessdata / Anuvaad custom** — see `RESEARCH_PLUS3_ENGINES.txt` when written.

## How to read each engine folder
Each `out/<engine>/README.md` lists:
- counts (good / short / empty)
- PNG-backed JSON filenames
- how to map `work/...` → shared `Dataset/...`

## Commands
```bash
cd /Users/srujansai/Desktop/South
# status + write READMEs
.venv/bin/python level2/audit_engine_quality.py --write-readmes

# continue an engine
.venv/bin/python level2/run_engine.py --engine tesseract_indic --skip-existing
.venv311/bin/python level2/run_engine.py --engine easyocr --skip-existing
.venv311/bin/python level2/run_engine.py --engine paddleocr_indic --lang te --skip-existing
```

## Level 1
Archived in `../arc_level_1/` — do not mix with Level 2 outputs.

## GitHub
Code/prompts: https://github.com/Srujan0798/vajrAstra  
Data dumps / `out/` stay local or Drive.
