# surya — RUN

## Counts
- n_json: 400
- empty: 11 (2.8%)
- non_empty: 389
- total_chars: ~1,100,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | kn_084 | 3894 | Kannada textbook page |
| best | kn_001 | 3891 | Kannada exam instructions |
| best | ta_055 | 3731 | Telugu govt form |
| worst (empty) | ml_020 | 0 | Malayalam — empty output |
| worst (empty) | ml_025 | 0 | Malayalam — empty output |
| worst (empty) | ml_035 | 0 | Malayalam — empty output |

## Notes
- Block mode: LayoutPredictor → RecognitionPredictor (full_page=False)
- Extracts text from block.html (strip tags)
- Fallback: full_page=True if block mode yields <5 chars
- License: Apache-2.0 code; weights under modified AI Pubs OpenRAIL-M (free for research/startups <$5M)
- Version: surya-ocr 0.22.1 (surya-2, block-mode html)
