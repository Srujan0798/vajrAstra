---
name: proto-20-w2-sampling-reconcile
description: "Wave 2 part 1 (Engine + Verdict, after the meeting) — reconcile manifest 1,283 vs scored 1,227 vs per-engine coverage of the 56 additions, explain rapidocr extras, and derive the single 22-language manifest level2/unified/manifest_22.json without touching the locked manifest"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:15:15.376Z
---

# WAVE 2 · PART 1 — RECONCILE AND UNIFY (Engine subagent; Verdict verifies) → inputs for `docs/campaign/SAMPLING_PLAN.md`

**When:** after the Vinay meeting (Wave 1 COMPLETE). **Closes:** CO-003, CO-025, CO-068 (one order, one place, one hierarchy); prepares U5.
**Precursor (do not redo, correct it):** `SAMPLE_PLAN_18_LANGS.md` (root, 2026-09-28, stale at 1,227).
**Writes only:** `level2/unified/reconcile_22.py`, `level2/unified/manifest_22.json`, `docs/campaign/checkpoints/W2_reports/reconcile.md`.

## Facts to start from (planner-measured 2026-09-29; re-verify)
- `level2/probe22/manifest.json` = dict with `items` (1,283). Item keys: gt, gt_source, has_table, image_id, language, language_name, mixed_script,
  print_or_hand, quality, script, set, source_page, source_pdf. `source_pdf` is null for pair and fill items (an earlier agent dedup'd on null and destroyed 447 items — never dedup on null).
- `manifest_additions.json` = {created 2026-09-29, n_total 56, items}: sd 25, mr 21, pa 10, all official_pdf_layer.
- `sheet.csv` covers 1,227 base items × 10 engines + 54 Sarvam rows. Images: `level2/probe22/images/<lang>/` (pair items are symlinks into `Datasets/akshardrishti_official/`).
- Engine outputs `level2/probe22/out/<engine>/<lang>/<image_id>.json`: surya has 43/56 additions; `out/rapidocr/` holds mr 121, pa 110, sd 125 files (extras unexplained).
- South: `arc_level_1/labeled/{ta,te,kn,ml}/` 100 GT JSONs each; outputs `level2/out/<engine>/<lang>/`; scored basis n=126 of 400 (see [[proto-12-w1b-benchmark22]]).

## TASK block (paste after the shared context block)
> You are the Engine agent. Reconcile every count and build one 22-language manifest. Read-only on all sources.
> 1. **Per-language reconciliation table (18 probe languages):** manifest n (base + additions) · scored n in `sheet.csv` (per model; they must agree across local models —
>    list any that differ) · additions present per engine (`out/<engine>/<lang>/<id>.json` exists for each addition id) · orphan outputs per engine (files in `out/` whose id is
>    not in the manifest — explains rapidocr 121/110/125?) · images present per item.
> 2. **South table (4 languages):** labelled n, outputs per engine, scored n from `level2/reports/CER_STAGE3B.json` with null reasons.
> 3. **`level2/unified/manifest_22.json`** (new file, deterministic, sorted by language code then image_id): schema
>    `{"created": "...", "sources": [...], "n_total": N, "languages": {code: {name, script, n_labelled, n_scored, tiers: {...}}}, "items": [{"uid": "<lang>:<image_id>", "language", "script",
>    "origin": "probe22|south400", "gt_source", "gt_path_or_inline": "...", "image_path", "scored_in": "sheet.csv|CER_STAGE3B.json|none", "tier": "gold_pair|pdf_layer|fill|south_label"}]}`.
>    Never copy images; reference paths. Never alter `manifest.json`.
> 4. **Checks printed as PASS/FAIL:** n_total == 1,283 + 400; every probe item appears once; every uid unique; every image_path exists (count missing).
> 5. Report: both tables, check results, every anomaly with a hypothesis and the command that would test it. Under 1,200 words.

## Verdict check
Re-count 3 languages independently; confirm no write to locked/sealed paths (`git status --short` shows only the named files); confirm the additions finding.
Then continue with [[proto-21-w2-variance-and-resource]].

Related: [[proto-21-w2-variance-and-resource]], [[proto-12-w1b-benchmark22]], [[proto-92-boss-decisions]]
