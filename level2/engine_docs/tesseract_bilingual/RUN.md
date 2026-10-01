# tesseract_bilingual — RUN

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
- Official tessdata bilingual: eng+indic (GitHub tessdata method)
- Stack: eng + TESS_STACK[lang] (deduped preserving order)
- Version: tesseract 5.5.2 (eng+stack bilingual)
