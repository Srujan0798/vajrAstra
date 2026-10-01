---
name: proto-82-engine-empty-output-patterns
description: "Added 2026-09-30 — \"find 1 problem, assume 1000, fix pattern-wide\" (operator law): measured empty-output table per engine × language shows script-mapping bugs (paddleocr_indic 100% empty on Devanagari brx/doi while 0% on hi/kok/mai/mr/ne; surya 100% empty on Sanskrit, 55% on mni) vs genuine no-model cases; root-cause, 4-page gate, fix, re-run under approval"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:12:06.662Z
---

# PROTO-82 — EMPTY-OUTPUT PATTERNS: BUG OR HONEST-EMPTY? (Engine diagnoses, Verdict classifies, boss approves re-runs)

**Laws that apply:** L8 open policy ("engines read any script on any page; lang tag = ID label, never a content constraint"); L3 4-page gate ("no engine/config change touches the full set until it
wins on 4"); honest-empty is correct ONLY when the engine truly has no model for the script; operator law "Useless ⇒ engine is wrong ⇒ fix ⇒ re-run; keep old in json_vN; never fake counts."

## Measured (monitor, `sheet.csv`, % empty predictions, cells with ≥20 rows; ≥80% marked *)
| engine | 100%-empty languages | partial | reading |
|---|---|---|---|
| paddleocr_indic | bn*, brx*, doi*, gu*, ks*, mni*, or*, pa*, sat* (overall 43%) | — | **brx and doi are Devanagari**, yet hi/kok/mai/mr/ne (Devanagari) are 0% empty → likely a language→model mapping bug, not missing capability |
| surya | sa* (100%) | mni 55, doi 14, gu 12, sat 10, ne 8, brx 5 | **sa is Devanagari** and surya reads hi at 0% empty, but surya ignores the language code (see code evidence below) → cause is image/model-side, not mapping; the "fusion ceiling" is 67% this one bug (EDGE_THESIS) |
| anuvaad_tesseract | bn*, gu*, ks*, mni*, or*, pa*, sat*, sd*, ur* (overall 50%) | — | only kan/mal/tam/tel/hin/eng traineddata exist → mostly honest-empty; verify it isn't run with the wrong traineddata for Devanagari languages (brx/doi/kok/mai/mr/ne are 0% empty → fine) |
| rapidocr | bn*, gu*, mni*, or*, pa*, sat* (overall 27%) | ne 2 | check its model list for Bengali/Gujarati/Gurmukhi/Odia |
| others | — | doctr, easyocr, indicphotoocr, tesseract family ≤4% | fine |

## Code evidence already found by the monitor (2026-09-30 ~05:15)
- **paddleocr_indic — confirmed MAPPING-BUG for brx and doi:** `level2/probe22/run_probe.py:84-88` `PADDLE_LANG` maps hi/mr/ne/mai/sa/kok(gom) to paddle's Devanagari models but omits
  `brx` and `doi`; the comment at `run_probe.py:80-83` wrongly lists them among "languages without any paddle model … honest-empty". Both are Devanagari-script → map them to a Devanagari
  model (e.g. `hi` or `mr`) per law L8. (as/bn/gu/pa/or/ks/mni/sat: check paddle 3.7 `_utils/langs.py` for Bengali/Gujarati/Gurmukhi/Odia models before accepting honest-empty.)
- **surya — NOT a language-mapping bug:** `level2/run_engine.py` `ocr_surya(image_path, lang)` never uses `lang` (layout → block recognition, full-page fallback if <5 chars). So the 100% empty
  output on `sa` comes from the images or the model path, not codes. The `sa` items are official pair JPEGs (`Datasets/akshardrishti_official/Sanskrit/Images and Transcription/*pro_labelled.jpeg`)
  — check size/aspect, whether they are line crops or annotated ("labelled") images, EXIF rotation, and what layout returns (0 blocks?) on 4 items; same for `mni` (55% empty).

## Engine subagent — TASK (diagnosis read-only; then 4-page tests only)
> 1. For each * cell: find how `level2/probe22/run_probe.py` (LOCKED — read only) maps the language code to the engine's model/language argument (file:line). Classify:
>    NO-MODEL (the engine has no model for that script — honest-empty, document it) · MAPPING-BUG (a model for the script exists but the code isn't mapped, e.g. paddle brx/doi → Devanagari) ·
>    OTHER (crash/timeout — check logs `level2/probe22/logs/`).
> 2. For each MAPPING-BUG: run the engine with the corrected script argument on **4 items** of that language (L3 gate) in a scratch output folder (never `level2/probe22/out/`), score with `metrics.py`,
>    and report CER before/after. No full re-run.
> 3. Write `docs/campaign/EMPTY_OUTPUT_DIAGNOSIS.md`: the table above re-measured, per-cell classification with evidence, 4-page results, the exact `run_probe.py` edits needed (fix-spec format),
>    expected impact on the benchmark cell, and the re-run cost (items × engine time).

## Gate and execution
A full re-run of a fixed cell changes `level2/probe22/out/` and `sheet.csv` (sealed/locked) → it rides on the boss's U5 approval (score/re-score after the meeting) — old outputs kept as `out_archive/<engine>_v1/`
(law L5 "reruns versioned"). The Sanskrit/surya cell is the highest-value item (the plan's "only real engineering item").

Related: [[proto-80-hackathon-metric-alignment]], [[proto-61-sheet-provenance-forensics]], [[proto-70-level2-restructure]], [[proto-92-boss-decisions]]
