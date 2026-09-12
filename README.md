# vajrAstra — Vaultstack / BHASHINI AksharDrishti (South track)

Private working repo for **Srujan Sai** (Vaultstack AI) on South Indian document OCR.

## Layout (clean — see level2/FOLDER_MAP.md)

```
SOUTH_CANON.md               # the law (read first)
Datasets/                    # source PDFs (te/ta/kn/ml) — renamed from work/
arc_level_1/                 # Level-1 labels (frozen) + L1 scripts archive
scripts/                     # active utilities (inventory, rasterize, verify)
level2/                      # ALL current work — see level2/FOLDER_MAP.md
  pages_manifest.json        # 400-page frozen set (+ script tags)
  renders_shared/            # the 400 PNG renders (single shared copy)
  run_engine.py              # engine harness (open policy, timeout/retry/heartbeat)
  orchestrator.py            # one-push: status / fill / migrate
  verify_all.py              # mass verification vs ground truth
  deep_verify.py             # per-pack deep verify vs original page
  out/                       # live engine outputs
  out_archive/               # superseded runs (kept)
  models/                    # seal structure per engine
  reports/                   # verification + seal reports
  _archive/                 # dead logs/reports/docs (kept, out of the way)
```
(Level-2 seal done-line: level2/ULTIMATE_HYBRID_CONCERN.md §10-11)

## Engines (10, free OSS, latest versions)
tesseract_indic · openbharatocr · easyocr · paddleocr_indic · indicphotoocr ·
rapidocr · tesseract_bilingual · doctr · surya · anuvaad_tesseract

## Quick start
```bash
source .venv311/bin/activate
python level2/orchestrator.py status   # dashboard
python level2/orchestrator.py fill     # parallel fills (resumes, skip-existing)
python level2/verify_all.py            # verification suite
```

## Not in git
Datasets/, out/, out_archive/, models/png, renders — data stays local/Drive.
GitHub (code only): https://github.com/Srujan0798/vajrAstra
