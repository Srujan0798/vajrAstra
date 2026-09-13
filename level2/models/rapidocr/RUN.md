# RUN.md — `rapidocr`

## Identity
- **model/version:** rapidocr 3.9.2 (per-lang PP-OCRv5/v4 mobile rec; te/ta/kn+dev; ml=no model->honest empty)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** partial_wash (ml=100 wash no-model; te/ta/kn honest signal v2 rerun 13 Sep)
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine rapidocr --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/rapidocr/ | **models:** level2/models/rapidocr/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 100 | short(<50): 30 | good(>=50): 270
- nonempty_rate: 0.750 | collapse_rate: 0.25
- capture ratio vs PDF layer (median): 0.289

## 5 example page_ids
- best: ta_055 (3555 chars)
- worst(nonempty): te_041 (6 chars)
- empty: ['ml_067', 'ml_069', 'ml_099']
- english-leak: ['te_020', 'te_024', 'te_041']
- table-ish: ['te_006', 'te_019', 'te_023']

## Strengths
- median 787 chars/page
- 444 ms/page

## Weaknesses
- 27 English-leak pages
- capture ratio vs PDF layer only 0.289

## Rerun history
- rapidocr_v0_restricted_lang (400 packs); rapidocr_v1_chinese_mojibake (400 packs) (active run in level2/out/rapidocr/)
