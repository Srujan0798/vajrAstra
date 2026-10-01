# rapidocr — RUN

## Counts
- n_json: 400
- empty: 100 (25.0%)
- non_empty: 300
- total_chars: ~850,000

## Example page_ids (5)
| Category | page_id | chars | Notes |
|----------|---------|-------|-------|
| best | ta_055 | 3555 | Dense Telugu govt form |
| best | ta_057 | 3424 | Telugu form page 2 |
| best | ta_068 | 3354 | Telugu form page 3 |
| worst (empty) | ml_001 | 0 | Malayalam — NO MODEL (honest empty) |
| worst (empty) | ml_002 | 0 | Malayalam — NO MODEL (honest empty) |
| worst (empty) | ml_003 | 0 | Malayalam — NO MODEL (honest empty) |

## Notes
- 100 Malayalam pages ALL empty — no Malayalam model exists (by design, returns honest-empty)
- Language models: te/ta (PP-OCRv5), kn (PP-OCRv4), ml (none)
- Mobile configs for all
- Version: rapidocr-onnxruntime 1.4.4
