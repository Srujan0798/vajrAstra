# RUN.md — `indicphotoocr`

## Identity
- **model/version:** IndicPhotoOCR IIIT-H (parseq trust-patched)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine indicphotoocr --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/indicphotoocr/ | **models:** level2/models/indicphotoocr/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 10 | short(<50): 22 | good(>=50): 368
- nonempty_rate: 0.975 | collapse_rate: 0.025
- capture ratio vs PDF layer (median): ?

## 5 example page_ids
- best: kn_084 (3649 chars)
- worst(nonempty): ml_090 (1 chars)
- empty: ['ml_020', 'ml_055', 'ml_046']
- english-leak: ['te_096', 'ta_005', 'ta_040']
- table-ish: ['te_003', 'te_005', 'te_038']

## Strengths
- low empty rate (2.5%)
- median 1051 chars/page
- 15700 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- none (single policy run) (active run in level2/out/indicphotoocr/)
