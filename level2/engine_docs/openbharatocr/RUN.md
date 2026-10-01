# openbharatocr — RUN

## Counts
- n_json: 400
- empty: 31 (7.8%)
- non_empty: 369
- total_chars: ~1,150,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | ta_055 | 3964 | Dense Telugu govt form |
| best | kn_084 | 3904 | Kannada textbook page |
| best | kn_001 | 3903 | Kannada exam instructions |
| worst (empty) | ml_020 | 0 | Malayalam — empty output |
| worst (empty) | ml_035 | 0 | Malayalam — empty output |
| worst (empty) | ml_036 | 0 | Malayalam — empty output |

## Notes
- ID-card library; full pages fall back to tesseract_indic
- Effectively a twin of tesseract_indic output
- WEAK / near-duplicate benchmark — do not over-weight as distinct SOTA
- Version: openbharatocr 0.4.3 (tesseract mirror path documented)
