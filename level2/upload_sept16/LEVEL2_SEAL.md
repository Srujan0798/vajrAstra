# LEVEL2_SEAL.md

Generated from disk counts. Do not invent.

| model_id | n_json | matching | missing | empty | RUN.md |
|---|---|---|---|---|---|
| tesseract_indic | 400 | 400 | 0 | 31 | `level2/models/tesseract_indic/RUN.md` |
| openbharatocr | 400 | 400 | 0 | 31 | `level2/models/openbharatocr/RUN.md` |
| easyocr | 400 | 400 | 0 | 9 | `level2/models/easyocr/RUN.md` |
| paddleocr_indic | 400 | 400 | 0 | 7 | `level2/models/paddleocr_indic/RUN.md` |
| indicphotoocr | 400 | 400 | 0 | 10 | `level2/models/indicphotoocr/RUN.md` |
| rapidocr | 400 | 400 | 0 | 100 | `level2/models/rapidocr/RUN.md` |
| tesseract_bilingual | 400 | 400 | 0 | 31 | `level2/models/tesseract_bilingual/RUN.md` |
| doctr | 400 | 400 | 0 | 11 | `level2/models/doctr/RUN.md` |
| surya | 400 | 400 | 0 | 11 | `level2/models/surya/RUN.md` |
| anuvaad_tesseract | 400 | 400 | 0 | 31 | `level2/models/anuvaad_tesseract/RUN.md` |

Total packs (matching): 4000 / 4000
Incomplete engines: none

## Forbidden checks
- Paid Gemini/Claude/GPT/Sarvam/Bhashini keys: **not used**
- Training: **not started**
- Aryan pipeline: **not touched**

## Seal gates (machine-checked)
| gate | check | state |
|---|---|---|
| G1 | 10 engines x 400 matching page_ids in models/ | GREEN |
| G2 | classification (signal|alias|wash) in every RUN.md | GREEN |
| G3 | core reports same-tick fresh (mtime spread <120s) | GREEN |
| G4 | leaderboard script-sliced (6 strata) | GREEN |
| G5 | true consensus (5-gram + word) computed; family-deduped | GREEN |
| G6 | schema clean (missing = ABSENT rows) | GREEN |
| G7 | manifest integrity 400/400 | GREEN |
| G8 | pages_400 symlinks all resolve | GREEN |
| G9 | LEVEL 3 NOT STARTED line present | GREEN |
| G10 | all code committed (auto-regen artifacts excluded) | GREEN |
| G11 | setup.sh smoke-tested (flag file) | GREEN |

## Seal status
LEVEL 3 NOT STARTED

LEVEL2_SEALED = **true**

<!-- generated_at: 2026-09-14T10:41:38Z | generator: seal_gen.py -->