# RUN.md — `tesseract_indic`

## Identity
- **model/version:** tesseract 5.5.2 (tel+hin+eng open stack)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv/bin/python level2/run_engine.py --engine tesseract_indic --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/tesseract_indic/ | **models:** level2/models/tesseract_indic/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 31 | short(<50): 23 | good(>=50): 346
- nonempty_rate: 0.922 | collapse_rate: 0.078
- capture ratio vs PDF layer (median): ?

## 5 example page_ids
- best: ta_055 (3963 chars)
- worst(nonempty): te_095 (1 chars)
- empty: ['te_076', 'te_071', 'ml_020']
- english-leak: ['te_024', 'te_096', 'ta_005']
- table-ish: none

## Strengths
- low empty rate (7.7%)
- median 1142 chars/page
- 3455 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- tesseract_indic_v0_singlelang (400 packs) (active run in level2/out/tesseract_indic/)
