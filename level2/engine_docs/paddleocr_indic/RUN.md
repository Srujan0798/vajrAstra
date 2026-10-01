# paddleocr_indic — RUN

## Counts
- n_json: 400
- empty: 7 (1.8%)
- non_empty: 393
- total_chars: ~1,000,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | ta_055 | 3679 | Dense Telugu govt form |
| best | ta_057 | 3398 | Telugu form page 2 |
| best | ta_034 | 3368 | Telugu form page 3 |
| worst (empty) | ml_020 | 0 | Malayalam — no ML model, falls back to en |
| worst (empty) | ml_025 | 0 | Malayalam — no ML model, falls back to en |
| worst (empty) | ml_035 | 0 | Malayalam — no ML model, falls back to en |

## Notes
- Two-stage graceful degradation: full pipeline (300s) → light retry (900s, mobile det, capped input)
- ml pages: no Malayalam model → falls back to en stack (warned once per run)
- kn uses ka (PP-OCRv3); te/ta use PP-OCRv5
- Poisoned-mode set prevents re-entering timed-out instances
- Version: paddleocr 3.7.0 / paddlepaddle 3.3.1
