# A3-SCORER: evaluation machinery audit

Answer: NO. There is no single committed, self-validating scorer. Metric pieces are scattered across five scripts, half the required metrics are absent, and no test exercises metrics.py. Snapshot has no data (no manifest_v1/v2.json, packs/, pages/), so nothing below was executed.

## STATE (verified in code)
- Core per-item scorer exists: `level2/benchmark/pipeline/metrics.py` (975 lines, stdlib + optional `editdistance`). `calculate_cer` / `calculate_wer` / `calculate_cer_uncapped` at :545-:568. CER and WER are capped at 1.0 (`_bound_rate` :540). Normalization is `normalize_for_scoring` (:140: NFKC+NFC, control chars, punct spacing, whitespace).
- Mean CER/WER, word_accuracy (= 100*(1-mean WER), :~755), empty handling (empty pred = CER 1.0, `missing_prediction`), catastrophic flag (`is_loop_or_catastrophic` :494: pipeline_error / tail_loop / length_explosion), `cer_100_count`, per-language means: `compute_metrics` :676. CLI `python metrics.py --input X.gt_pred.json --normalize` (:857). Input = JSON list of {image_name, gt, pred, language}; accepts several key aliases (:583).
- Median, bootstrap 95% CI (10,000 resamples, seed 20260926), empty_rate, S/D/I: `level2/benchmark/pipeline/build_metrics_80.py` (:47 `boot_ci`, :~88 median/empty). Caveats: hardcoded to `manifest_v1.json`, `sheet_v1.csv`, `packs/`; "empty" is really `cer>=0.999999` (a proxy, also counts wrong-but-total-failure) not text==""; S/D/I is a difflib approximation on only 25 items per language (:30, :36).
- Paired McNemar exact two-sided on CER<0.5 pass/fail: `level2/benchmark/pipeline/mcnemar_full_matrix.py` (:55 `mcnemar_exact_two_sided`, :142 `triple_mcnemar`), n_common>=30 gate, low_conf <50. Hardcodes 11 engine names (:36-48). Silent fallback: if `from metrics import calculate_cer` fails (:84) it uses a NON-normalized edit distance (:96-112), so results can silently change normalizer.
- Fast Levenshtein with startup self-validation: `build_sheet_v2.py` `np_lev` (:~30, validates 24 rows vs `metrics.edit_distance`, hard-abort), claim 400/400 agreement in `docs/campaign/SHEET_V2_FORENSICS.md:16`. This is the only self-validating component. It is a rebuild script for the 22-lang sheet (reads manifest_v1 + packs/), not a general scorer.
- Probe runner `run_probe.py`: engines -> packs only (`write_pack` :120); it does NOT score. Default manifest `benchmark/manifest_v2.json` (:18). The repo contains no manifest_v2 file and no description of it beyond that default and the `--manifest` help (:407).
- Tests: `level2/tests/run_tests.py` has 5 tests (registry, Sarvam contract, pack schema, sealed-basis medians vs 0.4299/0.4751 using `level2.verify_v2.cer_norm` — NOT metrics.py :131, L10 guard). Hand-rolled, no pytest.
- `level2/research/` contains zero .py files (README says "generators and gates only"; only gates/*.md). Nothing there scores.
- Other scorers (separate normalizers, so numbers can diverge): `level2/verify_v2.py` (cer_norm, empty_rate, per-engine), `seal_gen.py`, `audit_engine_quality.py`, `build_benchmark_22.py` (mean/median tables, :163/:247), `variance_22.py`.

## CLAIMED-BUT-UNPROVEN
- Wilson 95% CI: claimed as "estimator law" (OCR_AGENT_MEMORY_FEED.md:229, :407, :623; `wilson_ci_surya.json` named at :335). `grep -ri wilson --include=*.py` over the whole repo returns NOTHING. No code generates it. Also the Wilson interval is for a proportion, but the memory feed applies it to "per-item CER" (:623, :723) which is conceptually wrong; it is valid only on pass-rate/WRR-type binaries.
- "Estimator law" / `QLORA_EVAL_SPEC.md` (McNemar + Wilson, :723): spec only; scripts `mcnemar_results.json`, `coverage_surya.json`, `tier_surya.json` are cited but no generator exists in pipeline/.
- SHEET_V2_FORENSICS.md:3 says artefacts are at `level2/unified/build_sheet_v2.py` and `level2/unified/sheet_v2.csv`, and :7/:65 cite `probe22/metrics.py`. Real locations: `level2/benchmark/pipeline/build_sheet_v2.py`; `level2/unified/` holds only `run_bodhan.py`; `probe22/` holds only README.md. Paths were relocated; docs are stale. sheet_v2.csv (12,324 rows) is not in the snapshot.
- "sheet.csv has no generator, CER not re-derivable" (SHEET_V2_FORENSICS.md:7, :53): the headline leaderboard numbers rest on an unreproducible column; v2 is the proposed fix but its output is not verifiable here.
- AGENT_PROTOCOL.md (`level2/benchmark/docs/AGENT_PROTOCOL.md`) describes §6/§9 estimator law and 100 samples x 18 langs x 10 engines but its probe22/ paths (rule 7) predate the benchmark/ layout; and it is a task spec for an agent, not a scorer.

## GAPS
P0
- No WRR and no CRR anywhere (grep WRR/CRR in *.py: zero hits). Only `word_accuracy = 100*(1-mean WER)` — a mean-of-rates, not word-recognition-rate. For single-word crops the correct metric is exact-match WRR plus CRR (1 - total edits / total ref chars, micro-averaged). Mean of capped per-item rates is not CRR.
- No Wilson CI code. No single script outputs CI for pass-rate/WRR.
- No single entry point. Metric set is split across metrics.py (CER/WER/catastrophic), build_metrics_80.py (median/bootstrap/empty), mcnemar_full_matrix.py (McNemar). None of them import each other cleanly (build_metrics_80 loads metrics.py and build_sheet_v2.py via importlib file paths; mcnemar uses a bare `from metrics import` that only works with cwd/pipeline on sys.path, else silently degrades :84).
- No test for metrics.py at all (`tests/run_tests.py` never imports it). No known-answer tests (e.g. "kitten"/"sitting" = 3 edits; empty pred => CER 1; McNemar b=0,c=10 => p=0.00195).
P1
- Catastrophic definition is loop/length-explosion/pipeline-error (`metrics.py:494`), not "CER>=threshold". No catastrophic_rate field emitted by metrics.py; it has `loop_failure_count` and `cer_100_count` only; per-language scores exclude loops (note build_benchmark_22.py:841-843 text). Needs one stated definition (suggest: cer_uncapped >= 1.0 OR loop flag), reported separately from empty.
- Empty-rate is a CER proxy in build_metrics_80.py; metrics.py counts true empties (`missing_prediction_count`) but not as a rate.
- Printed blocks vs word crops use the same CER but metrics.py short-GT rule (`short_gt`: <50 non-space chars, excluded from means :~718) would DROP ALL word crops from the primary denominator. Handwriting word-crop eval cannot run through `compute_metrics` as-is. Also `detect_length_explosion` needs pred_w>=20 so never fires on crops, and `PUNCTUATIONS`/bullet/quote folds under `--normalize` may strip legit single-char GT.
- Bootstrap resamples items i.i.d.; no paired bootstrap for CER deltas between engines (McNemar thresholds at CER<0.5, which is arbitrary and loses magnitude).
- mcnemar `SCORES = PROBE/"scores"` (:~20) resolves to `pipeline/scores/`, whereas the committed summary lives at `benchmark/scores/mcnemar_summary.md` -> output path mismatch.
- Seed/normalizer provenance is not stamped into outputs (no `scorer_version`, no hash of normalizer).
P2
- `editdistance` optional; fallback is pure-Python O(nm) (slow on pages, fine on crops).
- No multiple-comparison correction across the 11x10/2 x lang McNemar grid.
- Stale docs path references listed above.

## CONCRETE NEXT ACTIONS
1. Create `level2/benchmark/pipeline/eval_harness.py` (stdlib + optional editdistance/numpy; imports `metrics.py` via `Path(__file__).parent`, no sys.path reliance, no silent fallback). Done-when: `python eval_harness.py selftest` exits 0 and prints "N/N known-answer checks passed".
   Functions:
   - `load_rows(path) -> list[Row]`: JSONL/JSON/CSV with fields id, gt, pred, group (lang/script), optional engine. Reuse `metrics.load_gt_pred_rows` aliases.
   - `norm(text, mode)`: mode `strict` = `metrics.normalize_for_scoring` (default), `none`, `content` = `metrics.preprocess(...normalize=True)`. Record mode in output.
   - `score_row(gt, pred, norm_mode) -> {cer_raw, cer, wer, exact, edits, ref_len, empty, catastrophic}`: cer_raw uncapped = edits/ref_len; cer = min(1, cer_raw); exact = normalized equality (this is word-level correctness for crops); empty = not pred.strip(); catastrophic = cer_raw>=1.0 or `metrics.is_loop_or_catastrophic`. Empty pred => cer 1, exact False, counted (never excluded). Empty GT rows: reported as `n_bad_gt`, excluded loudly.
   - `aggregate(rows, mode)`: mode `crop` (no short_gt exclusion; headline = WRR, CRR) or `block` (headline = mean/median CER, WER). Always emit all: n, mean_cer, median_cer, mean_wer, WRR = exact/n, CRR = 1 - sum(edits)/sum(ref_len) (micro), empty_rate, catastrophic_rate, plus p90 CER.
   - `wilson(k, n, z=1.96) -> (lo, hi)`: for WRR, empty_rate, catastrophic_rate.
   - `bootstrap_ci(values, stat=mean|median, B=10000, seed=20260926)` using stdlib `random.Random` (no numpy dependence).
   - `mcnemar_exact(b, c) -> p` (use `math.comb`, two-sided = min(1, 2*P(X<=min(b,c)))) and `paired(rows_a, rows_b, key="exact"|"cer<t")`: join on id, report n_common, b, c, p; default pass criterion = exact for crops, CER<0.5 for blocks (flag stated). Also paired bootstrap on delta CER.
   - `selftest()`: known answers (lev("kitten","sitting")=3; Devanagari NFC-equivalent strings => 0; empty pred => cer 1, empty True; wilson(0,10) lo=0, wilson(10,10) hi=1, wilson(5,10)~(0.237,0.763); mcnemar_exact(0,10)=0.00195, (5,5)=1.0; WRR/CRR on a 4-row toy set). Also cross-check `edit_distance` against a pure-Python reference on 400 random strings (reproduces the build_sheet_v2 gate).
   CLI:
   - `eval_harness.py score --preds P --gt G [--engine E] --mode crop|block --norm strict|none|content --group-by lang --out out.json [--md out.md]`
   - `eval_harness.py compare --a A.jsonl --b B.jsonl --mode ...` (paired)
   - `eval_harness.py selftest`
   Output JSON stamps: scorer_version, norm_mode, seed, B, n_dropped with reasons, sha1 of input files.
2. Add `level2/tests/test_eval_harness.py` (or add T7 to `tests/run_tests.py`) that calls `selftest()` and one fixture-based golden run. Done-when: `VAJRA_CODE_ONLY=1 python3 level2/tests/run_tests.py` includes T7 green.
3. Re-point `build_metrics_80.py` and `mcnemar_full_matrix.py` to import `eval_harness` (delete duplicate McNemar/bootstrap; remove the silent normalizer fallback at mcnemar_full_matrix.py:84-112). Done-when: grep shows one `mcnemar_exact` definition.
4. Fix stale paths in `docs/campaign/SHEET_V2_FORENSICS.md:3,:7,:65` (unified/ -> benchmark/pipeline/; probe22/metrics.py -> benchmark/pipeline/metrics.py). Done-when: every path cited exists with `ls`.
5. Add a pred-pack adapter (`from_packs(dir)`) reading `{image_id,text}` packs so `run_probe.py` output (`write_pack` :120) feeds `score` directly. Done-when: one engine's packs scored end to end on the Mac with n matching manifest count.
6. On the Mac (data present), run `score` for one engine on handwriting crops and one on printed blocks; commit outputs; confirm CER per row matches `sheet_v2.csv` within 1e-4 for block mode.

## RISKS
- Normalization changes the number: strict NFKC folds (e.g. Indic ligature/compat forms) and the `content` mode strips bullets/quotes/ZWJ; ZWJ/ZWNJ stripping can erase real distinctions in Indic scripts. Pick one default and print it with every number.
- Capped mean CER hides hallucination; always report uncapped catastrophic_rate beside it.
- Handwriting crop GT of 1-3 chars makes CER highly granular; use WRR with Wilson as the headline, not mean CER.
- Numbers already in circulation (sheet.csv, leaderboards) came from unreproducible or mixed normalizers (verify_v2.cer_norm vs metrics.normalize_for_scoring); do not compare them with harness output without a re-score.
- Not verified: anything requiring data or weights (absent from snapshot); hence claims about runtime behavior are code-read only.
