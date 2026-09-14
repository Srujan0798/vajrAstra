# RUN.md — `anuvaad_tesseract`

## Identity
- **model/version:** anuvaad tessdata + tesseract 5.5.2
- **policy:** OPEN — read any script on the page (operator directive 12 Sep)
- **quality_status:** honest_signal
- **invoke:** `.venv/bin/python level2/run_engine.py --engine anuvaad_tesseract --skip-existing`
- **source:** level2/pages_manifest.json (400) via level2/renders_shared/
- **out:** level2/out/anuvaad_tesseract/ | **models:** level2/models/anuvaad_tesseract/json/

## Counts (disk)
- n_json: 400
- matching the shared 400: 400
- missing: 0
- empty: 31 | short(<50): 25 | good(>=50): 344
- nonempty_rate: 0.922 | collapse_rate: 0.078
- capture ratio vs PDF layer (median): ?

## 5 example page_ids
- best: kn_084 (3850 chars)
- worst(nonempty): te_095 (1 chars)
- empty: ['te_020', 'ml_086', 'ml_036']
- english-leak: ['te_096', 'ta_005', 'ta_040']
- table-ish: none

## Strengths
- low empty rate (7.7%)
- median 1132 chars/page
- 3674 ms/page

## Weaknesses
- see reports/FAILURE_TAXONOMY.md

## Rerun history
- anuvaad_tesseract_v0_singlelang (400 packs) (active run in level2/out/anuvaad_tesseract/)
