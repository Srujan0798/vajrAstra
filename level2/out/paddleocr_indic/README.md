# Level 2 OCR outputs — `paddleocr_indic`

## Purpose
Benchmark outputs from this Indic/OSS OCR engine on the same South Dataset pages.
Goal is **max raw output** for later gap analysis / training — not perfect human gold.

## Counts
- Total JSON: **218 / 400**
- By lang: `{'te': 7, 'ta': 11, 'kn': 100, 'ml': 100}`
- Nonempty (>=1 char): **211**
- Good (>=50 chars): **197**
- Short (<50): **14**
- Empty: **7**
- Coverage missing IDs: **182**
- Recommendation: **CONTINUE_RUN**

## Folder layout
```
level2/out/paddleocr_indic/
  te/  te_001.json ... te_100.json
  ta/  ta_001.json ... ta_100.json
  kn/  kn_001.json ... kn_100.json
  ml/  ml_001.json ... ml_100.json
```

## PNG-backed JSON packs (open these + Dataset PNG)
Count: **13**

- `level2/out/paddleocr_indic/ta/ta_001.json` ← `work/ta/s_tamil0001pro_raw.png` (chars=1477)
- `level2/out/paddleocr_indic/ta/ta_003.json` ← `work/ta/s_tamil0003pro_raw.png` (chars=509)
- `level2/out/paddleocr_indic/ta/ta_002.json` ← `work/ta/s_tamil0002pro_raw.png` (chars=987)
- `level2/out/paddleocr_indic/ta/ta_004.json` ← `work/ta/s_tamil0004pro_raw.png` (chars=641)
- `level2/out/paddleocr_indic/ml/ml_010.json` ← `work/ml/s_malayalam0011pro_raw.png` (chars=678)
- `level2/out/paddleocr_indic/ml/ml_006.json` ← `work/ml/s_malayalam0007pro_raw.png` (chars=439)
- `level2/out/paddleocr_indic/ml/ml_007.json` ← `work/ml/s_malayalam0008pro_raw.png` (chars=693)
- `level2/out/paddleocr_indic/ml/ml_011.json` ← `work/ml/s_malayalam0012pro_raw.png` (chars=714)
- `level2/out/paddleocr_indic/ml/ml_004.json` ← `work/ml/s_malayalam0005pro_raw.png` (chars=318)
- `level2/out/paddleocr_indic/ml/ml_012.json` ← `work/ml/s_malayalam0013pro_raw.png` (chars=426)
- `level2/out/paddleocr_indic/ml/ml_008.json` ← `work/ml/s_malayalam0009pro_raw.png` (chars=638)
- `level2/out/paddleocr_indic/ml/ml_009.json` ← `work/ml/s_malayalam0010pro_raw.png` (chars=692)
- `level2/out/paddleocr_indic/ml/ml_005.json` ← `work/ml/s_malayalam0006pro_raw.png` (chars=773)

## How to read one pack
1. Open the JSON
2. `image.raw_path` + `image.page_index` → find page in shared `Dataset/`
3. `regions[].text` = OCR output from this engine

## Notes
- `work/...` in raw_path maps to shared Drive `Dataset/<Language>/...`
- Empty/short pages are expected on hard scans; we maximize nonempty rate, then improve prompts/runners and re-run weak IDs.

