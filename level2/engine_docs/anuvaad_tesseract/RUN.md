# anuvaad_tesseract — RUN

## Counts
- n_json: 400
- empty: 31 (7.8%)
- non_empty: 369
- total_chars: ~1,150,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | kn_084 | 3851 | Kannada textbook page |
| best | kn_001 | 3849 | Kannada exam instructions |
| best | ta_055 | 3766 | Telugu govt form |
| worst (empty) | ml_020 | 0 | Malayalam — empty output |
| worst (empty) | ml_035 | 0 | Malayalam — empty output |
| worst (empty) | ml_036 | 0 | Malayalam — empty output |

## Notes
- Anuvaad-tuned models: anuvaad_tel, anuvaad_tam, anuvaad_kan, anuvaad_mal
- Stack: anuvaad_xxx + hin + eng (fallback to anuvaad_xxx only if stack fails)
- Tessdata: level2/research/smoke/anuvaad_tesseract/tessdata
- Version: anuvaad tessdata + tesseract 5.5.2
