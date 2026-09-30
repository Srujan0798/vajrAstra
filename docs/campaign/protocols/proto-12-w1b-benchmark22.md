---
name: proto-12-w1b-benchmark22
description: "Step 1B (Engine subagent) — build the first single 22-language benchmark table (probe22 18 langs from sheet.csv + South 4 from sealed CER_STAGE3B.json), showing labelled n vs scored n, mean+median CER, Sarvam with n, and diff our metrics.py normalisation vs Sarvam's"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:11:55.719Z
---

# STEP 1B — THE 22-LANGUAGE BENCHMARK TABLE (Engine subagent) → `docs/campaign/BENCHMARK_22.md`

**Why:** the lead explicitly asked for benchmarks covering all 22 languages before "the final". The data exists in two separate places and was never put in
one table. This is also CO-003/025/068 ("South separate — one order, one place").
**Dispatch:** one Sonnet subagent, role Engine. Prompt = shared context block + TASK block.
**Writes only:** `level2/unified/build_benchmark_22.py` and `docs/campaign/BENCHMARK_22.md`.

## Facts the planner measured (verify, don't trust)
- probe22: `level2/probe22/sheet.csv` — 12,324 rows = 10 local engines × 1,227 scored items + 54 sarvam_vision rows (3/lang). Columns: image_id, language, script,
  print_or_hand, quality, has_table, mixed_script, gt, model, prediction, CER, WER, error_tag. 18 languages: as bn brx doi gu hi kok ks mai mni mr ne or pa sa sat sd ur.
- Manifest tiers (`level2/probe22/manifest.json`, key `gt_source`): official_pair_txt (bn, hi, sa = human gold), official_pdf_layer, sarvam_bench (fill; "machine GT" per protocol).
- South: 400 pages (ta, te, kn, ml × 100) labelled in `arc_level_1/labeled/<lang>/<lang>_NNN.json`; engine outputs in `level2/out/<engine>/<lang>/<lang>_NNN.json`
  (keys: page_id, source, lang, script, …, regions[text, text_nfc, …]) — **no CER stored there**. `level2/reports/MATRIX.csv` holds character counts, not CER.
- **South CER basis is tiny:** `level2/reports/CER_BY_SCRIPT.md` — CER comes from `level2/reports/CER_STAGE3B.json` per-page entries with non-null `cer`;
  the verify_v2 writer nulled 55 pages (legacy_mojibake_layer) and 219 pages (gt_thin, GT < 179 chars) → **writer basis n=126 of 400**. By dominant script:
  Tamil 53, Telugu 6, Kannada 4, Malayalam 4, Devanagari 16, Latin 43. So **kn and ml have ~4 scored pages** — below the lead's own 5–10 floor.
  The table must show this honestly; it is a finding for the boss, not a formatting problem.

## TASK block (paste)
You are the Engine agent. Build the first single benchmark table covering all 22 languages. Everything read-only on its sources.

1. **Inspect before computing.** Print the structure of `level2/reports/CER_STAGE3B.json` (top-level keys, one per-page entry: which fields hold page_id, lang,
   engine, cer, null reason). Print 2 lines of `sheet.csv`. Print `level2/probe22/metrics.py` function names and its normalisation steps.
2. **Script `level2/unified/build_benchmark_22.py`** (python3 stdlib only; deterministic; prints the markdown tables to stdout; the lead redirects into the md):
   - probe22 part: per language × model → n scored, CER mean, CER median, empty-prediction count. Exclude sarvam_vision from "best local engine".
     Sarvam column separately: CER mean with its n (3/lang).
   - South part: from CER_STAGE3B.json per-page entries → per **lang tag** (ta/te/kn/ml, from page_id prefix) × engine → n scored (non-null cer), mean, median;
     plus labelled n (100) and the null counts by reason. Also report the dominant-script view to reconcile with `CER_BY_SCRIPT.md`.
   - Labelled n per language: probe22 from manifest (1,283 incl. additions) and scored n from sheet (1,227 basis); South labelled 100 each.
   - GT tier per language (gold pair / PDF layer / fill / mixed with counts).
3. **Consistency checks (must print PASS/FAIL):** probe22 per-language winner CERs reproduce `EVIDENCE_SUMMARY.md` §3 (e.g. bn surya 0.476, hi surya 0.220,
   kok surya 0.425, pa surya 0.145); South medians reproduce `CER_BY_SCRIPT.md` §1 ALL row (surya 0.430, anuvaad 0.475). Explain every FAIL (basis, mean vs median).
4. **Normalisation diff.** Read `level2/probe22/metrics.py`. Then open Sarvam's indic-ocr-bench scoring code: WebFetch `https://huggingface.co/datasets/sarvamai/indic-ocr-bench`
   and its file tree (look for `metrics.py` / evaluation code; open the raw file page). Reading a page is allowed; do not download the dataset.
   Compare step by step: Unicode NFC/NFKC, whitespace/newline flattening, quote/dash unification, Indic punctuation (danda ।, double danda ॥), ZWJ/ZWNJ stripping,
   nukta handling, digit normalisation, case, and what the headline score is (CER, 1−CER, word accuracy?). Table: step | ours | Sarvam | impact on comparability.
   If the file cannot be opened, write UNKNOWN with the URL tried.
5. **The md (`docs/campaign/BENCHMARK_22.md`)**, in this order:
   - Header: generated-by, date, sources, command to regenerate (`python3 level2/unified/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md` or equivalent).
   - **Summary for the lead (≤10 lines, plain):** languages covered, scored n range, where our best local engine is strong/weak, the South small-n finding,
     the Sarvam comparison with its n, the normalisation caveat.
   - **Table 1 — coverage:** 22 rows: code, language, script, labelled n, scored n, GT tier mix, low-n flag (scored n < 50 → "no winner claim (D4)"; < 10 → "below lead's 5–10 floor" if < 5).
   - **Table 2 — CER by language:** rows 22 languages; columns = the 10 local engines (mean; median in a second table or as "mean / median"), best local engine,
     Sarvam CER (n). Mark byte-identical family (tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr) once.
   - **Table 3 — basis differences:** probe22 vs South (rendering/source type, GT type, metric, nulling rules). Never merge the two into one ranking without this table.
   - Consistency check results. Normalisation diff table. UNRESOLVED.
6. Final message: the summary paragraph, PASS/FAIL list, path of both files.

## Lead's acceptance check
Re-run the script yourself; confirm stdout == md tables. Spot-check 3 cells against `sheet.csv` by hand. Verdict cross-check per [[proto-91-verdict-cross-check]].
Record in the checkpoint the three numbers the boss most needs: languages with scored n ≥ 50, languages with scored n < 10, and the Sarvam paired result.

Related: [[proto-10-w1-overview]], [[proto-93-measured-facts]], [[proto-19-w1h-draft-research-plan]], [[proto-20-w2-sampling-reconcile]]
