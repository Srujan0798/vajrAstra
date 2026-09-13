# vajrAstra — Vaultstack / BHASHINI AksharDrishti (South track)

Private working repo for **Srujan Sai** (Vaultstack AI) on South Indian document OCR.

## Layout (clean — see level2/FOLDER_MAP.md)

```
SOUTH_CANON.md               # the law (read first; L2 ops law: level2/ULTIMATE_HYBRID_CONCERN.md supersedes where conflicting)
HOW_TO_RUN.txt                # ops card (venvs, one-push commands, 4-page gate, engine socket)
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

## How Level 2 feeds Vaultstack (deck stages)
- `level2/out/` packs → **Stage-3 SFT** noisy-corpus source (raw engine text is the training input)
- CER table (vs PDF-layer + L1-gold) → **Stage-3b preference pairs** for SimPO/DPO ranking
- capture / gap analysis (`reports/GAP_*`) → the **pitch slide** (what all free engines miss)
- disagreement pages (cross-engine conflict, `reports/REVIEW_QUEUE.md`) → **Stage-1 layout training queue**
- L1 gold labels → **audit layer** (ground truth the benchmark answers to)
- Firewall: bench data is **never fine-tuned on** — it stays the referee, not the food

## Not in git
Datasets/, out/, out_archive/, models/png, renders — data stays local/Drive.
GitHub (code only): https://github.com/Srujan0798/vajrAstra
