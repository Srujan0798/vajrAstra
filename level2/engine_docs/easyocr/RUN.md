# easyocr — RUN

## Counts
- n_json: 400
- empty: 9 (2.3%)
- non_empty: 391
- total_chars: ~1,200,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | ta_055 | 4466 | Dense Telugu govt form |
| best | ta_057 | 4188 | Telugu form page 2 |
| best | ta_068 | 3910 | Telugu form page 3 |
| worst (empty) | ml_020 | 0 | Malayalam — empty output |
| worst (empty) | ml_025 | 0 | Malayalam — empty output |
| worst (empty) | ml_035 | 0 | Malayalam — empty output |

## Notes
- Combos run: te+en, ta+en, kn+en, hi+mr+ne+en — keep longest
- Tamil charset patched at runtime (143 classes vs 126 bundled)
- Version: easyocr 1.7.2 (all-Indic open reader)
