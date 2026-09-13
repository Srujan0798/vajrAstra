# RUN.md — `surya`

## Identity
- **model/version:** surya-ocr 0.22.1 (surya-2, block-mode html)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv311/bin/python level2/run_engine.py --engine surya --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/surya/ | **models:** level2/models/surya/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 11 | short(<50): 26 | good(>=50): 363
- nonempty_rate: 0.973 | collapse_rate: 0.027
- capture ratio vs PDF layer (median): 0.0

## 5 example page_ids
- best: kn_084 (3894 chars)
- worst(nonempty): te_024 (9 chars)
- empty: ['ml_079', 'ml_095', 'ml_065']
- english-leak: ['te_096', 'ta_005', 'ta_040']
- table-ish: none

## Strengths
- low empty rate (2.8%)
- median 1135 chars/page
- 16329 ms/page

## Weaknesses
- capture ratio vs PDF layer only 0.0

## Rerun history
- surya_v0_grammar_broken (182 packs) (active run in level2/out/surya/)
