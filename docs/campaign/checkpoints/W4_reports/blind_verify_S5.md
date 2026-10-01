# Blind verification of W4.md §S5 (Tiered scoring, never pooled, 2026-10-01)

Verifier: independent subagent, did not author S5.
Scope: every numeric claim in W4.md lines 761–775 against the source files on disk.

## Method

The S5 claims are about per-engine CER on the South tier (ta/te/kn/ml, 100 items each = 400). They are not in `metrics_*_normalized.json` / `metrics_*_normalized.summary.tsv` (those cover only the v1 manifest's 18 languages; ta/te/kn/ml are absent from `lang_wise_scores`). The South CERs are recoverable from the per-prediction JSONs under `level2/benchmark/packs/<engine>/<lang>/*.json`. I read those files, summed CER, divided by n. Bodhan numbers cross-checked against `level2/unified/out/preds_bodhan_*_pair.metrics.normalized.json` and `DISPATCH_LOG.md` §36.

## Per-line verdicts

| # | Claim (W4.md:767–775) | Verdict | Evidence |
|---|---|---|---|
| 1 | tesseract_indic n=400, CER 0.1450 | **PASS** | `packs/tesseract_indic/{ta,te,kn,ml}/` 100 JSONs each. CER mean: ta 0.1706, te 0.1558, kn 0.1245, ml 0.1292. Pooled = (100×0.1706+100×0.1558+100×0.1245+100×0.1292)/400 = 0.14502 ≈ 0.1450. |
| 2 | openbharatocr — alias of tesseract_indic, n=400, CER 0.1450 | **PASS** | `packs/openbharatocr/{ta,te,kn,ml}/` has identical per-item CER (same lang-level means 0.1706/0.1558/0.1245/0.1292). Pooled = 0.14502. |
| 3 | easyocr te n=100, CER 0.2437 | **PASS** | `packs/easyocr/te/` 100 files; mean CER 0.2437. |
| 3b | easyocr kn n=100, CER 0.2096 | **PASS** | `packs/easyocr/kn/` 100 files; mean CER 0.2096. |
| 3c | easyocr ta BROKEN (tamil.pth mismatch) | **PASS** | `packs/easyocr/ta/` absent. Cause documented in `run_engines_south.py:54-59` ("tamil.pth state_dict mismatch vs installed code — verified 2026-09-30"). |
| 3d | easyocr ml skipped | **PASS** | `packs/easyocr/ml/` absent. Cause documented in `run_engines_south.py:57` ("malayalam.pth not cached; downloading needs boss approval"). |
| 4 | anuvaad_tesseract n=355, CER 0.1956 | **PASS** | ta 100, te 100, kn 100, ml 55 = 355 files. Pooled = (100×0.2237+100×0.2305+100×0.1533+55×0.1579)/355 = 0.1956. (45 ml items produced no file, i.e. 100−55=45 missing — not 45 empty predictions. The 55 produced files all have non-empty text.) |
| 5 | rapidocr n≈395, CER 0.8427 | **PASS** | `packs/rapidocr/{ta,te,kn,ml}/` 100 files each = 400. 5 have empty `text` (ta:4, te:1). Excluding those 5 → n=395; mean CER = 0.8427 exactly. "≈" honest about the 5 excluded empties. |
| 6 | doctr n=400, CER 0.8236 | **PASS** | `packs/doctr/{ta,te,kn,ml}/` 100 files each = 400; no empties. Pooled = (100×0.8812+100×0.7419+100×0.8093+100×0.8620)/400 = 0.8236 exactly. |
| 7 | Bodhan (pair-only) n=300 gold, 4-bit CER 0.4034 / bf16 CER 0.4010 (from §36) | **PASS** | `level2/unified/out/preds_bodhan_4bit_pair.metrics.normalized.json` → `total_sample_count=300`, `avg_metrics.cer=0.40343048…`. `preds_bodhan_bf16_pair.metrics.normalized.json` → `total_sample_count=300`, `avg_metrics.cer=0.40097704…`. DISPATCH_LOG.md §36 (line 704) and BODHAN_BASELINE.md:18 carry them too. |

## Caveats

- The South numbers do not appear in `level2/benchmark/scores/metrics_*_normalized.summary.tsv` (which lists only the v1 manifest's 18 langs, no ta/te/kn/ml) nor in `sheet_v2.csv` (7 engines, 1227 rows, no ta/te/kn/ml). Anyone re-verifying must read the per-prediction JSONs directly. The CER values are stored in each JSON's `"CER"` field.
- S5 line 4 "ml 45 empty" is interpreted as "45 ml items produced no output file" (100 target − 55 files = 45), since 0 of the 55 ml files have empty predictions. The honest-empty reading is preserved either way (55 valid, 45 absent).
- S5 line 5 "n≈395" is consistent with 5 rapidocr items having empty text (4 in ta, 1 in te) being excluded from the average.
- The `metrics_*.json` and `metrics_*.summary.tsv` files in `level2/benchmark/scores/` do **not** include ta/te/kn/ml — S5's numbers were computed outside the summary layer (direct per-prediction average), so the summaries are not a verification cross-check; only the per-prediction JSONs are.

## Overall verdict

**PASS** on all 7 S5 lines. Every CER and n number reconciles exactly (or to ≤1e-3 rounding) with the per-prediction JSONs on disk, except where the source itself does not exist (Bodhan pair-only is verified via its own pair metrics files and DISPATCH_LOG §36, not via the packs/<engine> tree).