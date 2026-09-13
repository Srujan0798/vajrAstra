# RUN.md — `openbharatocr`

## Identity
- **model/version:** openbharatocr 0.4.3 (tesseract mirror path documented)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** alias (tesseract_indic mirror — excluded from independent consensus)
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine openbharatocr --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/openbharatocr/ | **models:** level2/models/openbharatocr/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 31 | short(<50): 23 | good(>=50): 346
- nonempty_rate: 0.922 | collapse_rate: 0.078
- capture ratio vs PDF layer (median): 0.866

## 5 example page_ids
- best: ta_055 (3963 chars)
- worst(nonempty): te_095 (1 chars)
- empty: ['ml_055', 'ml_036', 'ml_040']
- english-leak: ['te_024', 'te_096', 'ta_005']
- table-ish: none

## Strengths
- low empty rate (7.7%)
- median 1142 chars/page
- 5026 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- openbharatocr_v0_singlelang (400 packs) (active run in level2/out/openbharatocr/)
