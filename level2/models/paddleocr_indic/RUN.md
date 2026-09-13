# RUN.md — `paddleocr_indic`

## Identity
- **model/version:** paddleocr 3.7.0 / paddlepaddle 3.3.1
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine paddleocr_indic --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/paddleocr_indic/ | **models:** level2/models/paddleocr_indic/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 7 | short(<50): 29 | good(>=50): 364
- nonempty_rate: 0.983 | collapse_rate: 0.017
- capture ratio vs PDF layer (median): ?

## 5 example page_ids
- best: ta_055 (3679 chars)
- worst(nonempty): ml_090 (1 chars)
- empty: ['ml_046', 'ml_065', 'ml_020']
- english-leak: ['te_024', 'te_041', 'te_042']
- table-ish: ['te_044', 'te_057', 'te_064']

## Strengths
- low empty rate (1.8%)
- median 584 chars/page
- 95182 ms/page

## Weaknesses
- 89 English-leak pages (Latin-only recognition)
- NO ml model in paddle 3.7.0: all 100 ml pages run the en stack (ml script ratio 0.0 in packs — coverage hole, not model failure)

## Rerun history
- none (single policy run) (active run in level2/out/paddleocr_indic/)
