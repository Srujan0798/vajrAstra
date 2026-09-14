# RUN.md — `doctr`

## Identity
- **model/version:** python-doctr 1.1.0 (crnn_vgg16_bn)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine doctr --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/doctr/ | **models:** level2/models/doctr/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 11 | short(<50): 22 | good(>=50): 367
- nonempty_rate: 0.973 | collapse_rate: 0.027
- capture ratio vs PDF layer (median): ?

## 5 example page_ids
- best: ta_055 (4033 chars)
- worst(nonempty): ml_056 (2 chars)
- empty: ['ml_046', 'ml_090', 'ml_065']
- english-leak: ['te_001', 'te_002', 'te_003']
- table-ish: none

## Strengths
- low empty rate (2.8%)
- median 1035 chars/page
- 3138 ms/page

## Weaknesses
- 263 English-leak pages (Latin-only recognition)

## Rerun history
- doctr_v0_restricted_lang (400 packs) (active run in level2/out/doctr/)
