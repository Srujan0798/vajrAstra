# RUN.md — `tesseract_bilingual`

## Identity
- **model/version:** tesseract 5.5.2 (eng+stack bilingual)
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv/bin/python level2/run_engine.py --engine tesseract_bilingual --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/tesseract_bilingual/ | **models:** level2/models/tesseract_bilingual/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 31 | short(<50): 24 | good(>=50): 345
- nonempty_rate: 0.922 | collapse_rate: 0.078
- capture ratio vs PDF layer (median): 0.872

## 5 example page_ids
- best: ta_055 (3963 chars)
- worst(nonempty): te_095 (1 chars)
- empty: ['te_061', 'ml_061', 'ta_016']
- english-leak: ['te_024', 'te_096', 'ta_005']
- table-ish: none

## Strengths
- low empty rate (7.7%)
- median 1140 chars/page
- 4874 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- tesseract_bilingual_v0_singlelang (400 packs) (active run in level2/out/tesseract_bilingual/)
