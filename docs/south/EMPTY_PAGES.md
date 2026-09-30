# Empty pages — engine vs our dump

Disk: `level2/reports/LANG_LEADERBOARD.md` (generated 2026-09-14). Empty = 100 − nonempty. Seal JSON counts (4000 packs) stand. One false line in the 2026-09-25 seal write-up is corrected here: **te/ta/kn are not 0-empty on every engine.**

## Empty counts by folder tag (of 100)

| engine | te | ta | kn | ml | total empty |
|---|---|---|---|---|---|
| tesseract_indic / openbharatocr / tesseract_bilingual / anuvaad | 13 | 2 | 0 | 16 | 31 |
| easyocr | 0 | 0 | 0 | 9 | 9 |
| paddleocr_indic | 0 | 0 | 0 | 7 | 7 |
| indicphotoocr | 0 | 0 | 0 | 10 | 10 |
| surya | 0 | 0 | 0 | 11 | 11 |
| doctr | 0 | 0 | 0 | 11 | 11 |
| rapidocr | 0 | 0 | 0 | **100** | 100 |

Kannada is 0 empty on all 10. Tamil empty is tess-family only (2 pages). Telugu empty is tess-family only (13 pages). Malayalam empty is on every engine.

## What is whose

**Engine (honest).**
- rapidocr: no Malayalam weights. 100/100 ml empty by design.
- paddleocr: no `lang=ml` model; nonempty ml median **175 chars** vs ~1100 on other engines — it “fills” with a thin/en fallback, it does not read Malayalam.
- openbharatocr = tesseract_indic byte twin (ID-card lib). Not a second engine.
- doctr: 263/400 pages flagged English-leak. Nonempty ≠ Indic.

**Our dump (honest).**
- 300-dpi rescue on 10 empty pages: **0/10 recovered** (`ULTIMATE_HYBRID_CONCERN` gate). Those pages are contentless, photo, or no usable print.
- Folder names lie: some `te`/`ta` pages are Latin/Devanagari books. Tess empty on te is partly “wrong book in the Telugu folder,” partly tess miss.
- Coverage ≥6 engines nonempty = 382/400. The other 18 are the shared-hard / empty-content cell.

**Not a pipeline bug.** Renders exist, schema is clean, 400/400 packs exist. Empty string on a blank last page is correct. Empty string on a dense Malayalam page from rapidocr is the model.

## Can we “max” them

Empty rate is the small leak. The product gap is **accuracy on nonempty pages** (surya median CER 0.43, easyocr 0.90, te/kn still ~0.75+ on the thin clean-GT slice).

Already tried and closed: 300-dpi re-render, tessdata_best × PSM, paddle server-det, rapidocr Chinese-config, ensemble union (0/115 beat best single).

Still allowed later, not now:
- Level-3 paid APIs (Sarvam 2.1, Bhashini) — freeze / W5.
- Training / hybrid in `docs/architecture/W2_HYBRID.md` — freeze / W6.
- Binarize-only retry already in the harness; new preprocess needs a 4-page gate.

Do not rerun the 400 to chase empty%. The seal already records the weakness. Next labor stays W3 probe images, not another South flush.
