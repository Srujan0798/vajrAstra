# RUN.md — `easyocr`

## Identity
- **model/version:** easyocr 1.7.2 (all-Indic open reader)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine easyocr --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/easyocr/ | **models:** level2/models/easyocr/json/

## Counts (disk)
- n_json: 343
- matching the shared 400: 343
- missing: 57
- empty: 3 | short(<50): 21 | good(>=50): 319
- nonempty_rate: 0.991 | collapse_rate: 0.009
- capture ratio vs PDF layer (median): 0.849

## 5 example page_ids
- best: ta_055 (4466 chars)
- worst(nonempty): ml_040 (2 chars)
- empty: ['ml_035', 'ml_020', 'ml_025']
- english-leak: ['ta_005', 'ta_040', 'kn_005']
- table-ish: ['te_009', 'te_012', 'te_091']

## Strengths
- low empty rate (0.9%)
- median 1102 chars/page
- 31670 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- easyocr_v0_restricted_lang (400 packs) (active run in level2/out/easyocr/)
