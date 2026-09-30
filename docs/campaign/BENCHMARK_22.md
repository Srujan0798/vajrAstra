<!-- GENERATED FILE — do not hand-edit. Source: level2/unified/build_benchmark_22.py -->

# BENCHMARK_22 — all 22 Eighth-Schedule languages in one table

- **generated-by:** Engine subagent (Sonnet) · `level2/unified/build_benchmark_22.py`
- **date:** 2026-09-29 (ISO; weekday not asserted)
- **protocol:** `docs/campaign/protocols/proto-12-w1b-benchmark22.md` (Step 1B)
- **regenerate:** `python3 level2/unified/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md`
- **sources (read-only, never written):**
  - `level2/probe22/manifest.json` (1,283 items, key `gt_source`) — labelled n, GT tier
  - `level2/probe22/sheet.csv` (12,324 CSV records) — per-language x model CER
  - `level2/reports/CER_STAGE3B.json` (sealed) — South-400 per-page CER, 10 engines x 400
  - `level2/pages_script_map.json`, `level2/pages_manifest.json` — page_id -> lang_tag / dominant_script
  - `arc_level_1/labeled/<tag>/` — South labelled JSON file counts (100/tag)
  - `level2/probe22/metrics.py` (our scorer, a fork of Sarvam's — see normalisation diff)

---

## SUMMARY FOR THE LEAD

1. **22 languages**, 18 from probe22 (`19`–`100` scored items each) + 4 South tags (ta 70, te 26, kn 25, ml 5 scored of 100 labelled).
2. **Scored n ranges 5–100**; **13 of 22** languages clear the n>=50 winner-claim bar, **1** is below n=10 (ml=5).
3. **Best local engine is surya on 14 of 22** cells (surya is weakest on South te/kn/ml; tesseract-family wins mr, or, doi, mni, ne, sat).
4. **South small-n finding (the one that matters):** only **126 of 400** South pages carry a CER — 219 nulled `gt_thin`, 55 nulled `legacy_mojibake_layer`. By lang tag that is ta 70 / te 26 / kn 25 / ml 5. **By dominant script it is a different corpus entirely**: Tamil 53, Latin 43, Devanagari 16, Telugu 6, Kannada 4, Malayalam 4. **kn's 25 scored pages are 4 Kannada + 20 Latin + 1 Telugu; te's 26 are 5 Telugu + 17 Latin + 4 Devanagari.** The 'kn/ml ~4 pages' figure in the packet is the *script-pure* subset, not the lang-tag count. Both views are in Table 2b.
5. **Sarvam, paired, n=54** (3 items x 18 langs, same scorer, `sarvam_vision` never counted as a local contender). Sarvam mean CER **0.2640** on n=54 in `sheet.csv` (0.2400 on n=51 in the older `scores/metrics_sarvam_vision_normalized.json` — the 3-row difference is the loop-exclusion divergence, check C11). Against **surya** on the same items: Sarvam better 28, surya better 21, tie 5; surya's 3-item mean is lower in **10/18** languages (brx, gu, ks, mai, mr, ne, or, pa, sd, ur). Against the **best local engine per language** it is Sarvam better 31 / local better 21 / tie 2, and the local mean is lower in 9/18. The surya pairing reproduces `CAMPAIGN_DIRECTIVE.md` A3/K1 exactly (checks C14/C15). With n=3/lang this is directional noise, not a win claim. Full table below.
6. **Normalisation caveat (the real blocker on comparability):** our `level2/probe22/metrics.py` is a **modified fork** of Sarvam's `metrics.py`, not the same file. We count empty predictions and tail loops as CER=1.0 (Sarvam excludes them from the mean) and we drop GT<50-char rows (Sarvam does not). **Our CER is therefore systematically higher than Sarvam's on the same items** — see the normalisation diff table below. No head-to-head against the published 87.39 is valid until one of us re-scores.
7. **Two bases, never one ranking:** probe22 (clean rendered pairs / PDF layers) and South-400 (old 200-dpi book & government scans vs PDF text layer) are different populations with different GT and different nulling. Table 3 is the guard.

---

## TABLE 1 — coverage: labelled n vs scored n, per language

`scored n` = items for which a CER was actually computed. probe22 labelled n comes from the manifest (includes the 56 additions that were never scored); South labelled n is the JSON file count in `arc_level_1/labeled/<tag>/`.

| # | code | language | script | basis | labelled n | scored n | unscored | GT tier mix (scored subset) | low-n flag |
|---:|---|---|---|---|---:|---:|---:|---|---|
| 1 | `as` | Assamese | Bengali-Assamese | probe22 | 19 | **19** | 0 | fill 19 | no winner claim (D4) |
| 2 | `bn` | Bengali | Bengali-Assamese | probe22 | 100 | **100** | 0 | gold pair 100 |  |
| 3 | `brx` | Bodo | Devanagari | probe22 | 67 | **67** | 0 | PDF layer 47 · fill 20 |  |
| 4 | `doi` | Dogri | Devanagari | probe22 | 27 | **27** | 0 | fill 20 · PDF layer 7 | no winner claim (D4) |
| 5 | `gu` | Gujarati | Gujarati | probe22 | 24 | **24** | 0 | fill 20 · PDF layer 4 | no winner claim (D4) |
| 6 | `hi` | Hindi | Devanagari | probe22 | 100 | **100** | 0 | gold pair 100 |  |
| 7 | `kok` | Konkani | Devanagari | probe22 | 100 | **100** | 0 | PDF layer 100 |  |
| 8 | `ks` | Kashmiri | Perso-Arabic | probe22 | 100 | **100** | 0 | PDF layer 100 |  |
| 9 | `mai` | Maithili | Devanagari | probe22 | 100 | **100** | 0 | PDF layer 100 |  |
| 10 | `mni` | Manipuri | Meitei-Mayek | probe22 | 20 | **20** | 0 | fill 20 | no winner claim (D4) |
| 11 | `mr` | Marathi | deva | probe22 | 100 | **79** | 21 | PDF layer 79 |  |
| 12 | `ne` | Nepali | Devanagari | probe22 | 37 | **37** | 0 | fill 20 · PDF layer 17 | no winner claim (D4) |
| 13 | `or` | Odia | Odia | probe22 | 69 | **69** | 0 | PDF layer 50 · fill 19 |  |
| 14 | `pa` | Punjabi | guru | probe22 | 100 | **90** | 10 | PDF layer 90 |  |
| 15 | `sa` | Sanskrit | Devanagari | probe22 | 100 | **100** | 0 | gold pair 100 |  |
| 16 | `sat` | Santhali | Ol Chiki | probe22 | 20 | **20** | 0 | fill 20 | no winner claim (D4) |
| 17 | `sd` | Sindhi | arab | probe22 | 100 | **75** | 25 | PDF layer 75 |  |
| 18 | `ur` | Urdu | Perso-Arabic | probe22 | 100 | **100** | 0 | PDF layer 100 |  |
| 19 | `ta` | Tamil | mixed (see 2b) | South-400 | 100 | **70** | 30 | PDF text layer (page-level nulls, not per-item) |  |
| 20 | `te` | Telugu | mixed (see 2b) | South-400 | 100 | **26** | 74 | PDF text layer (page-level nulls, not per-item) | no winner claim (D4) |
| 21 | `kn` | Kannada | mixed (see 2b) | South-400 | 100 | **25** | 75 | PDF text layer (page-level nulls, not per-item) | no winner claim (D4) |
| 22 | `ml` | Malayalam | mixed (see 2b) | South-400 | 100 | **5** | 95 | PDF text layer (page-level nulls, not per-item) | no winner claim (D4) |

Manifest-level GT tier mix (1,283 items, before the unscored additions were dropped):

| code | language | manifest n | gold pair | PDF layer | fill | scored n |
|---|---|---:|---:|---:|---:|---:|
| `as` | Assamese | 19 | 0 | 0 | 19 | 19 |
| `bn` | Bengali | 100 | 100 | 0 | 0 | 100 |
| `brx` | Bodo | 67 | 0 | 47 | 20 | 67 |
| `doi` | Dogri | 27 | 0 | 7 | 20 | 27 |
| `gu` | Gujarati | 24 | 0 | 4 | 20 | 24 |
| `hi` | Hindi | 100 | 100 | 0 | 0 | 100 |
| `kok` | Konkani | 100 | 0 | 100 | 0 | 100 |
| `ks` | Kashmiri | 100 | 0 | 100 | 0 | 100 |
| `mai` | Maithili | 100 | 0 | 100 | 0 | 100 |
| `mni` | Manipuri | 20 | 0 | 0 | 20 | 20 |
| `mr` | Marathi | 100 | 0 | 100 | 0 | 79 |
| `ne` | Nepali | 37 | 0 | 17 | 20 | 37 |
| `or` | Odia | 69 | 0 | 50 | 19 | 69 |
| `pa` | Punjabi | 100 | 0 | 100 | 0 | 90 |
| `sa` | Sanskrit | 100 | 100 | 0 | 0 | 100 |
| `sat` | Santhali | 20 | 0 | 0 | 20 | 20 |
| `sd` | Sindhi | 100 | 0 | 100 | 0 | 75 |
| `ur` | Urdu | 100 | 0 | 100 | 0 | 100 |
| **total** | 18 langs | **1283** | 300 | 825 | 158 | **1227** |

`mr`, `pa`, `sd` are the only languages where manifest n > scored n: their additions (mr +21, pa +10, sd +25 = 56) exist in the manifest but were never scored.

---

## TABLE 2 — CER by language (mean / median), all 22 languages, 10 local engines

Lower is better. Every cell is `mean / median` of the per-item CER on that language's scored set. The `tess-family` column is the byte-identical family (`openbharatocr` == `tesseract_indic` == `tesseract_bilingual`; `EVIDENCE_SUMMARY.md:24,78` + `CER_BY_SCRIPT.md:57`) — the three names are one engine, so they are collapsed into one column here and their individual values are in 2c.

| code | lang | n | surya | anuvaad | tess-family | IPO | paddle | rapid | doctr | easy | best local (mean) | sarvam_vision (n=3) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| `as` | Assamese | 19 | 0.253 / 0.007 | 1.000 / 1.000 | 0.200 / 0.018 | 0.189 / 0.038 | 1.000 / 1.000 | 1.000 / 1.000 | 0.888 / 0.867 | 0.250 / 0.118 | **indicphotoocr** 0.189 | 0.334 (n=3) |
| `bn` | Bengali | 100 | 0.476 / 0.425 | 1.000 / 1.000 | 0.888 / 0.871 | 0.657 / 0.697 | 1.000 / 1.000 | 1.000 / 1.000 | 0.909 / 0.903 | 0.667 / 0.692 | **surya** 0.476 | 0.089 (n=3) |
| `brx` | Bodo | 67 | 0.165 / 0.057 | 0.363 / 0.265 | 0.361 / 0.263 | 0.413 / 0.365 | 1.000 / 1.000 | 0.513 / 0.580 | 0.820 / 0.831 | 0.340 / 0.280 | **surya** 0.165 | 0.379 (n=3) |
| `doi` | Dogri | 27 | 0.335 / 0.156 | 0.327 / 0.248 | 0.322 / 0.300 | 0.508 / 0.459 | 1.000 / 1.000 | 0.492 / 0.438 | 0.832 / 0.831 | 0.367 / 0.393 | **tesseract_indic** 0.322 | 0.056 (n=3) |
| `gu` | Gujarati | 24 | 0.255 / 0.105 | 1.000 / 1.000 | 0.263 / 0.206 | 0.266 / 0.225 | 1.000 / 1.000 | 1.000 / 1.000 | 0.748 / 0.834 | 0.754 / 0.812 | **surya** 0.255 | 0.222 (n=3) |
| `hi` | Hindi | 100 | 0.220 / 0.181 | 0.883 / 0.945 | 0.877 / 0.918 | 0.713 / 0.741 | 0.504 / 0.523 | 0.649 / 0.658 | 0.877 / 0.869 | 0.515 / 0.503 | **surya** 0.220 | 0.084 (n=3) |
| `kok` | Konkani | 100 | 0.425 / 0.428 | 0.648 / 0.848 | 0.644 / 0.896 | 0.662 / 0.813 | 0.622 / 0.829 | 0.657 / 0.744 | 0.914 / 0.917 | 0.619 / 0.850 | **surya** 0.425 | 0.239 (n=3) |
| `ks` | Kashmiri | 100 | 0.589 / 0.580 | 1.000 / 1.000 | 0.781 / 0.790 | 0.926 / 0.928 | 1.000 / 1.000 | 0.872 / 0.887 | 0.927 / 0.916 | 0.678 / 0.700 | **surya** 0.589 | 0.630 (n=3) |
| `mai` | Maithili | 100 | 0.030 / 0.028 | 0.075 / 0.075 | 0.058 / 0.057 | 0.262 / 0.259 | 0.050 / 0.048 | 0.097 / 0.091 | 0.819 / 0.828 | 0.038 / 0.036 | **surya** 0.030 | 0.257 (n=3) |
| `mni` | Manipuri | 20 | 0.977 / 1.000 | 1.000 / 1.000 | 0.858 / 0.855 | 0.923 / 0.913 | 1.000 / 1.000 | 1.000 / 1.000 | 0.947 / 0.951 | 0.908 / 0.916 | **tesseract_indic** 0.858 | 0.023 (n=3) |
| `mr` | Marathi | 79 | 0.215 / 0.019 | 0.272 / 0.132 | 0.205 / 0.027 | 0.340 / 0.228 | 0.213 / 0.039 | 0.296 / 0.141 | 0.853 / 0.855 | 0.208 / 0.023 | **tesseract_bilingual** 0.205 | 0.248 (n=3) |
| `ne` | Nepali | 37 | 0.228 / 0.145 | 0.243 / 0.220 | 0.166 / 0.160 | 0.302 / 0.291 | 0.174 / 0.147 | 0.629 / 0.602 | 0.870 / 0.865 | 0.210 / 0.202 | **tesseract_bilingual** 0.161 | 0.210 (n=3) |
| `or` | Odia | 69 | 0.285 / 0.195 | 1.000 / 1.000 | 0.259 / 0.224 | 0.366 / 0.337 | 1.000 / 1.000 | 1.000 / 1.000 | 0.809 / 0.810 | 0.810 / 0.809 | **tesseract_indic** 0.259 | 0.447 (n=3) |
| `pa` | Punjabi | 90 | 0.145 / 0.137 | 1.000 / 1.000 | 0.226 / 0.212 | 0.234 / 0.238 | 1.000 / 1.000 | 1.000 / 1.000 | 0.779 / 0.783 | 0.817 / 0.820 | **surya** 0.145 | 0.160 (n=3) |
| `sa` | Sanskrit | 100 | 1.000 / 1.000 | 0.365 / 0.349 | 0.261 / 0.240 | 0.465 / 0.450 | 0.178 / 0.147 | 0.368 / 0.353 | 0.903 / 0.901 | 0.175 / 0.136 | **easyocr** 0.175 | 0.019 (n=3) |
| `sat` | Santhali | 20 | 0.762 / 0.752 | 1.000 / 1.000 | 0.878 / 0.847 | 0.651 / 0.498 | 1.000 / 1.000 | 1.000 / 1.000 | 0.868 / 0.840 | 0.888 / 0.863 | **indicphotoocr** 0.651 | 0.477 (n=3) |
| `sd` | Sindhi | 75 | 0.315 / 0.265 | 1.000 / 1.000 | 0.468 / 0.475 | 0.828 / 0.829 | 0.420 / 0.359 | 0.479 / 0.432 | 0.872 / 0.873 | 0.436 / 0.379 | **surya** 0.315 | 0.344 (n=3) |
| `ur` | Urdu | 100 | 0.623 / 0.621 | 1.000 / 1.000 | 0.792 / 0.785 | 0.935 / 0.943 | 0.872 / 0.884 | 0.921 / 0.935 | 0.936 / 0.950 | 0.681 / 0.675 | **surya** 0.623 | 0.533 (n=3) |
| `ta` | Tamil | 70 | 0.331 / 0.322 | 0.362 / 0.335 | 0.396 / 0.358 | 0.536 / 0.554 | 0.578 / 0.642 | 0.598 / 0.651 | 0.859 / 0.875 | 0.830 / 0.945 | **surya** 0.331 | not run |
| `te` | Telugu | 26 | 0.634 / 0.749 | 0.647 / 0.729 | 0.657 / 0.741 | 0.682 / 0.798 | 0.706 / 0.852 | 0.708 / 0.866 | 0.720 / 0.854 | 0.648 / 0.751 | **surya** 0.634 | not run |
| `kn` | Kannada | 25 | 0.647 / 0.796 | 0.672 / 0.787 | 0.676 / 0.793 | 0.715 / 0.822 | 0.727 / 0.817 | 0.720 / 0.772 | 0.738 / 0.833 | 0.808 / 0.903 | **surya** 0.647 | not run |
| `ml` | Malayalam | 5 | 0.629 / 0.639 | 0.638 / 0.647 | 0.632 / 0.620 | 0.682 / 0.671 | 0.825 / 0.923 | 1.000 / 1.000 | 0.824 / 0.896 | 0.834 / 0.895 | **surya** 0.629 | not run |

The `tess-family` column value for each row:

| code | lang | n | openbharatocr mean/med | tesseract_indic mean/med | tesseract_bilingual mean/med |
|---|---|---:|---:|---:|---:|
| `as` | Assamese | 19 | 0.200 / 0.018 | 0.203 / 0.029 | 0.200 / 0.018 |
| `bn` | Bengali | 100 | 0.888 / 0.871 | 0.884 / 0.855 | 0.888 / 0.871 |
| `brx` | Bodo | 67 | 0.361 / 0.263 | 0.358 / 0.256 | 0.361 / 0.263 |
| `doi` | Dogri | 27 | 0.322 / 0.300 | 0.333 / 0.333 | 0.322 / 0.300 |
| `gu` | Gujarati | 24 | 0.263 / 0.206 | 0.279 / 0.206 | 0.263 / 0.206 |
| `hi` | Hindi | 100 | 0.877 / 0.918 | 0.876 / 0.904 | 0.877 / 0.918 |
| `kok` | Konkani | 100 | 0.644 / 0.896 | 0.644 / 0.888 | 0.644 / 0.896 |
| `ks` | Kashmiri | 100 | 0.781 / 0.790 | 0.782 / 0.791 | 0.781 / 0.790 |
| `mai` | Maithili | 100 | 0.058 / 0.057 | 0.057 / 0.056 | 0.058 / 0.057 |
| `mni` | Manipuri | 20 | 0.858 / 0.855 | 0.858 / 0.855 | 0.858 / 0.855 |
| `mr` | Marathi | 79 | 0.205 / 0.027 | 0.205 / 0.028 | 0.205 / 0.027 |
| `ne` | Nepali | 37 | 0.166 / 0.160 | 0.161 / 0.156 | 0.166 / 0.160 |
| `or` | Odia | 69 | 0.259 / 0.224 | 0.261 / 0.224 | 0.259 / 0.224 |
| `pa` | Punjabi | 90 | 0.226 / 0.212 | 0.227 / 0.212 | 0.226 / 0.212 |
| `sa` | Sanskrit | 100 | 0.261 / 0.240 | 0.245 / 0.226 | 0.261 / 0.240 |
| `sat` | Santhali | 20 | 0.878 / 0.847 | 0.878 / 0.847 | 0.878 / 0.847 |
| `sd` | Sindhi | 75 | 0.468 / 0.475 | 0.468 / 0.471 | 0.468 / 0.475 |
| `ur` | Urdu | 100 | 0.792 / 0.785 | 0.793 / 0.786 | 0.792 / 0.785 |
| `ta` | Tamil | 70 | 0.396 / 0.358 | 0.396 / 0.358 | 0.396 / 0.358 |
| `te` | Telugu | 26 | 0.657 / 0.741 | 0.657 / 0.748 | 0.657 / 0.741 |
| `kn` | Kannada | 25 | 0.676 / 0.793 | 0.671 / 0.793 | 0.676 / 0.793 |
| `ml` | Malayalam | 5 | 0.632 / 0.620 | 0.632 / 0.620 | 0.632 / 0.620 |

Empty-prediction counts (probe22 only — a blank `prediction` scored CER 1.0; South-400 out/*.json carries no equivalent field):

| code | lang | surya | anuvaad_t | tesseract | openbhara | tesseract | indicphot | paddleocr | rapidocr | doctr | easyocr | sarvam_vision |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `as` | Assamese | 0 | 19 | 0 | 0 | 0 | 0 | 19 | 19 | 0 | 0 | 0 |
| `bn` | Bengali | 0 | 100 | 1 | 0 | 0 | 0 | 100 | 100 | 0 | 0 | 0 |
| `brx` | Bodo | 4 | 0 | 0 | 0 | 0 | 0 | 67 | 0 | 0 | 0 | 0 |
| `doi` | Dogri | 4 | 0 | 0 | 0 | 0 | 1 | 27 | 0 | 0 | 0 | 0 |
| `gu` | Gujarati | 3 | 24 | 1 | 1 | 1 | 0 | 24 | 24 | 0 | 0 | 0 |
| `hi` | Hindi | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `kok` | Konkani | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `ks` | Kashmiri | 0 | 100 | 0 | 0 | 0 | 0 | 100 | 0 | 0 | 0 | 0 |
| `mai` | Maithili | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `mni` | Manipuri | 11 | 20 | 0 | 0 | 0 | 0 | 20 | 20 | 0 | 0 | 0 |
| `mr` | Marathi | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `ne` | Nepali | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| `or` | Odia | 1 | 69 | 0 | 0 | 0 | 1 | 69 | 69 | 1 | 0 | 0 |
| `pa` | Punjabi | 0 | 90 | 0 | 0 | 0 | 0 | 90 | 90 | 0 | 0 | 0 |
| `sa` | Sanskrit | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `sat` | Santhali | 2 | 20 | 0 | 0 | 0 | 0 | 20 | 20 | 0 | 0 | 0 |
| `sd` | Sindhi | 0 | 75 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `ur` | Urdu | 0 | 100 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

---

## TABLE 2b — South-400: the lang-tag view vs the dominant-script view

`CER_BY_SCRIPT.md` buckets the South-400 by each page's **dominant script**, not by its lang tag. Those are two different partitions of the same 400 pages and they give very different n. Both are printed; neither is a correction of the other.

**2b-1 — by lang tag (from `page_id` prefix), 400 pages = 100 labelled per tag:**

| lang tag | language | labelled n | scored n (non-null cer) | null `gt_thin` | null `legacy_mojibake_layer` | best local engine | mean | median |
|---|---|---:|---:|---:|---:|---|---:|---:|
| `ta` | Tamil | 100 | **70** | 24 | 6 | surya | 0.331 | 0.322 |
| `te` | Telugu | 100 | **26** | 49 | 25 | surya | 0.634 | 0.749 |
| `kn` | Kannada | 100 | **25** | 55 | 20 | surya | 0.647 | 0.796 |
| `ml` | Malayalam | 100 | **5** | 91 | 4 | surya | 0.629 | 0.639 |
| **total** | 4 langs | **400** | **126** | **219** | **55** | | | |

**2b-2 — by dominant script (reconciles row-for-row with `CER_BY_SCRIPT.md` s1):**

| dominant script | n | surya | anuvaad_tesseract | tess* | tess* | tess* | indicphotoocr | paddleocr_indic | rapidocr | doctr | easyocr | row winner |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Tamil | 53 | 0.345 | 0.301 | 0.356 | 0.356 | 0.356 | 0.625 | 0.479 | 0.534 | 0.915 | 0.961 | **anuvaad_tesseract** (0.301) |
| Latin | 43 | 0.855 | 0.859 | 0.874 | 0.874 | 0.874 | 0.881 | 0.886 | 0.869 | 0.822 | 0.892 | **doctr** (0.822) |
| Devanagari | 16 | 0.222 | 0.252 | 0.261 | 0.261 | 0.256 | 0.377 | 0.871 | 0.917 | 0.831 | 0.334 | **surya** (0.222) |
| Telugu | 6 | 0.748 † | 0.759 † | 0.758 † | 0.758 † | 0.757 † | 0.826 † | 0.729 † | 0.750 † | 0.856 † | 0.870 † | **paddleocr_indic** (0.729) |
| Kannada | 4 | 0.398 † | 0.475 † | 0.459 † | 0.459 † | 0.443 † | 0.542 † | 0.546 † | 0.607 † | 0.725 † | 0.920 † | **surya** (0.398) |
| Malayalam | 4 | 0.636 † | 0.642 † | 0.620 † | 0.620 † | 0.620 † | 0.664 † | 0.937 † | 1.000 † | 0.905 † | 0.899 † | **tesseract_indic** (0.620) |
| **ALL (writer basis)** | 126 | 0.430 | 0.475 | 0.493 | 0.493 | 0.493 | 0.655 | 0.707 | 0.712 | 0.853 | 0.902 | **surya** (0.430) |

† `n<10` in that row — do not rank engines on it (`CER_BY_SCRIPT.md:21`). `tess*` = the three byte-identical aliases.

**2b-3 — the cross-tab that explains the discrepancy:**

| lang tag | Tamil | Latin | Devanagari | Telugu | Kannada | Malayalam | row n |
|---|---:|---:|---:|---:|---:|---:|---:|
| `ta` | 53 | 5 | 12 | 0 | 0 | 0 | 70 |
| `te` | 0 | 17 | 4 | 5 | 0 | 0 | 26 |
| `kn` | 0 | 20 | 0 | 1 | 4 | 0 | 25 |
| `ml` | 0 | 1 | 0 | 0 | 0 | 4 | 5 |

Read: **kn's 25 scored pages are 4 Kannada + 20 Latin + 1 Telugu.** `te`'s 26 are 5 Telugu + 17 Latin + 4 Devanagari. The Kannada- and Malayalam-*script* rows that look like 'kn=4, ml=4' in `CER_BY_SCRIPT.md` are the **script-pure** subsets, not the language scores. The `kn=4 / ml=4` line in `CAMPAIGN_DIRECTIVE.md` A5 is therefore **true only on the script view**; on the lang-tag view kn=25 (above the lead's 5–10 floor) and ml=5 (below it). This is a CONTRADICTION between the directive text and the lang-tag reading, resolved here by printing both.

---

## TABLE 3 — basis differences: probe22 vs South-400

**Never merge these two into one ranking without this table.** A South-400 CER is not comparable to a probe22 CER.

| dimension | probe22 (18 langs) | South-400 (ta/te/kn/ml) |
|---|---|---|
| source / rendering | clean rendered page crops + validated PDF text layers; `print_or_hand=printed`, `quality=unknown`, `has_table` flagged per item | 200-dpi renders of old (19th–20th c.) book & government/government-exam PDFs; whole pages, not blocks |
| GT type | 3 tiers: `official_pair_txt` (bn/hi/sa, human gold), `official_pdf_layer` (machine text layer), `sarvam_bench` fill (README: "reviewed twice by human language experts") | single tier: PDF text layer only |
| metric | per-item CER from `level2/probe22/metrics.py` (NFC/NFKC + content folds, empty pred = 1.0, capped at 1.0) | per-page CER from `verify_v2.py` writer: "NFC, lowercase, whitespace-collapsed; Levenshtein" (`CER_STAGE3B.json` `definition`) — a **different, simpler** normaliser |
| nulling rule | none — every scored item has a CER; empty predictions score 1.0 | page-level: 219 pages nulled `gt_thin` (GT < 200 chars) + 55 nulled `legacy_mojibake_layer`; 400 -> 126 |
| labelled n | 1,283 (manifest) | 400 (100/tag) |
| scored n | 1,227 (base set; 56 additions never scored) | 126 of 400 |
| corpus effect | honest-empty is common and **is scored as CER 1.0** — empty predictions over the 1,227 scored items: anuvaad_tesseract 617, rapidocr 343, paddleocr_indic 536, surya 129; easyocr 0 | not measurable from this basis — `CER_STAGE3B.json` stores `cer`/`wer`/`gt_chars` only, no prediction text. No basis page carries a loop/short-GT reason for any engine, which is *consistent* with no abstentions but is not a direct measurement (UNKNOWN) |
| what the score means | engine vs provided GT on a given rendering | engine vs **PDF text layer** of the same page — the GT is a by-product of the scan, so layer errors propagate into the score (this is why Latin n=43 is the largest bucket and is called weaker-GT evidence at `CER_BY_SCRIPT.md:25`) |

---

## CONSISTENCY CHECKS

Each row is recomputed from disk by this script and compared against the printed number in the named file. `TOL_ROUND=0.0005` (EVIDENCE_SUMMARY s3 prints 3 dp).

| check | result | detail |
|---|---|---|
| C1 sheet.csv record count = 12,324 | **PASS** | counted 12324 = 10 x 1,227 + 54 sarvam |
| C2 sheet.csv local rows = 10 x 1,227 | **PASS** | counted 12270 |
| C3 sarvam_vision rows = 54 (3 x 18 langs) | **PASS** | counted 54 |
| C4 manifest n_total = 1,283 | **PASS** | counted 1283 (manifest n_total field = 1283) |
| C5 South labelled = 100 x 4 tags | **PASS** | {'ta': 100, 'te': 100, 'kn': 100, 'ml': 100} |
| C6 South per_page entries = 400 x 10 engines | **PASS** | 400 pages, engine counts [10] |
| C7 South writer basis n = 126 of 400 | **PASS** | 126 scored, 219 gt_thin, 55 legacy_mojibake_layer |
| C8 null reasons match verify_v2 (219 gt_thin / 55 mojibake) | **PASS** | gt_thin=219, mojibake=55 |
| C9 bn winner vs EVIDENCE_S3 | **PASS** | surya mean 0.4763 vs printed 0.476, n=100 (3-dp round, same n) |
| C9 brx winner vs EVIDENCE_S3 | **FAIL** | surya: CER 0.1653 != 0.153 (delta +0.0123); n 67 != EVIDENCE n 66 — EVIDENCE_S3 was read from scores/metrics_*_normalized.json lang_wise_scores, frozen at a smaller per-language basis |
| C9 hi winner vs EVIDENCE_S3 | **PASS** | surya mean 0.2198 vs printed 0.220, n=100 (3-dp round, same n) |
| C9 kok winner vs EVIDENCE_S3 | **PASS** | surya mean 0.4248 vs printed 0.425, n=100 (3-dp round, same n) |
| C9 ks winner vs EVIDENCE_S3 | **PASS** | surya mean 0.5894 vs printed 0.589, n=100 (3-dp round, same n) |
| C9 mai winner vs EVIDENCE_S3 | **PASS** | surya mean 0.0298 vs printed 0.030, n=100 (3-dp round, same n) |
| C9 mr winner vs EVIDENCE_S3 | **PASS** | tesseract_bilingual mean 0.2046 vs printed 0.205, n=79 (3-dp round, same n) |
| C9 or winner vs EVIDENCE_S3 | **FAIL** | tesseract_indic: CER 0.2588 != 0.256 (delta +0.0028); n 69 != EVIDENCE n 66 — EVIDENCE_S3 was read from scores/metrics_*_normalized.json lang_wise_scores, frozen at a smaller per-language basis |
| C9 pa winner vs EVIDENCE_S3 | **PASS** | surya mean 0.1447 vs printed 0.145, n=90 (3-dp round, same n) |
| C9 sa winner vs EVIDENCE_S3 | **FAIL** | easyocr: CER 0.1751 != 0.168 (delta +0.0071); n 100 != EVIDENCE n 99 — EVIDENCE_S3 was read from scores/metrics_*_normalized.json lang_wise_scores, frozen at a smaller per-language basis |
| C9 sd winner vs EVIDENCE_S3 | **PASS** | surya mean 0.3155 vs printed 0.315, n=75 (3-dp round, same n) |
| C9 ur winner vs EVIDENCE_S3 | **PASS** | surya mean 0.6232 vs printed 0.623, n=100 (3-dp round, same n) |
| C10 South median surya vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.4299 vs printed 0.4299 |
| C10 South median anuvaad_tesseract vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.4751 vs printed 0.4751 |
| C10 South median tesseract_indic vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.4930 vs printed 0.4930 |
| C10 South median openbharatocr vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.4930 vs printed 0.4930 |
| C10 South median tesseract_bilingual vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.4931 vs printed 0.4931 |
| C10 South median indicphotoocr vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.6547 vs printed 0.6547 |
| C10 South median paddleocr_indic vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.7070 vs printed 0.7070 |
| C10 South median rapidocr vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.7116 vs printed 0.7116 |
| C10 South median doctr vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.8532 vs printed 0.8532 |
| C10 South median easyocr vs CER_BY_SCRIPT s1 | **PASS** | recomputed 0.9025 vs printed 0.9025 |
| C11 Sarvam mean CER reconciles EVIDENCE s6 0.2400 | **PASS** | sheet.csv gives 0.2640 on n=54; dropping the 3 loop rows (2.0 CER mass) gives 0.24034 on n=51 = EVIDENCE s6 0.2400. The delta is the loop-exclusion divergence, not a data error |
| C12 languages with scored n >= 50 | **PASS** | counted 13: bn, brx, hi, kok, ks, mai, mr, or, pa, sa, sd, ur, ta |
| C13 languages with scored n < 10 | **PASS** | counted 1: ml |
| C14 Sarvam-vs-surya item tally vs DIRECTIVE A3/K1 (28/21/5) | **PASS** | recomputed Sarvam better 28, surya better 21, tie 5 on n=54 — exact match |
| C15 Sarvam-vs-surya lang tally vs DIRECTIVE A3/K1 (10/18) | **PASS** | recomputed 10/18: brx, gu, ks, mai, mr, ne, or, pa, sd, ur |

**32 PASS / 3 FAIL** of 35.

### Why the C9 FAILs happen (all three are the same cause)

`EVIDENCE_SUMMARY.md:28` (via `level2/probe22/scores/LEADERBOARD.md:28`) states its source is the `lang_wise_scores` block of `level2/probe22/scores/metrics_<engine>_normalized.json`. Those files were written by a run of `metrics.py` over an **earlier pack state**: their per-language `sample_count` is brx 66, or 66, sa 99, gu 20, ne 34, mni 14, while `sheet.csv` today holds brx 67, or 69, sa 100, gu 24, ne 37, mni 20. Same language, same engine, same metric, **smaller denominator**. Verified directly: `scores/metrics_surya_normalized.json` has brx `cer 0.15265… sample_count 66` and `scores/metrics_tesseract_indic_normalized.json` has or `cer 0.25641… sample_count 66` — these are byte-for-byte the 0.153 and 0.256 printed in EVIDENCE_SUMMARY s3. So the C9 FAILs on brx / or / sa are a **basis drift in the older artifact**, not a metric error in this recomputation. The direction matters: the older, smaller basis makes brx look *better* (0.153 vs 0.165 today). gu / ne / mni are not in the check list because EVIDENCE_SUMMARY s3 applies no winner claim at n<50 (D4).

### Sarvam paired table — surya vs `sarvam_vision` on the same 3 items per language

This is the only comparison on this disk where both sides went through one scorer. `local` = surya's mean over the 3 paired items; `sarvam` = the 3-item mean. Both from `level2/probe22/sheet.csv`.

| code | lang | n paired | surya mean | sarvam mean | local lower? |
|---|---|---:|---:|---:|---|
| `as` | Assamese | 3/3 | 0.3341 | 0.3339 | no |
| `bn` | Bengali | 3/3 | 0.3412 | 0.0891 | no |
| `brx` | Bodo | 3/3 | 0.1079 | 0.3794 | **yes** |
| `doi` | Dogri | 3/3 | 0.0669 | 0.0564 | no |
| `gu` | Gujarati | 3/3 | 0.1733 | 0.2223 | **yes** |
| `hi` | Hindi | 3/3 | 0.2627 | 0.0836 | no |
| `kok` | Konkani | 3/3 | 0.2552 | 0.2387 | no |
| `ks` | Kashmiri | 3/3 | 0.5602 | 0.6305 | **yes** |
| `mai` | Maithili | 3/3 | 0.0242 | 0.2568 | **yes** |
| `mni` | Manipuri | 3/3 | 1.0000 | 0.0230 | no |
| `mr` | Marathi | 3/3 | 0.2114 | 0.2477 | **yes** |
| `ne` | Nepali | 3/3 | 0.2062 | 0.2099 | **yes** |
| `or` | Odia | 3/3 | 0.2303 | 0.4475 | **yes** |
| `pa` | Punjabi | 3/3 | 0.1565 | 0.1597 | **yes** |
| `sa` | Sanskrit | 3/3 | 1.0000 | 0.0195 | no |
| `sat` | Santhali | 3/3 | 0.8546 | 0.4773 | no |
| `sd` | Sindhi | 3/3 | 0.2326 | 0.3441 | **yes** |
| `ur` | Urdu | 3/3 | 0.5292 | 0.5332 | **yes** |
| **total** | 18 langs | **54** | item-level: sarvam better **28**, surya better **21**, tie **5** | lang-level: surya lower in **10/18** | |

### Doc-vs-code contradictions found while checking

| # | claim | where | code says | tag |
|---|---|---|---|---|
| 1 | "GT<179c pages" | `CER_BY_SCRIPT.md:5`, `research/metrics_rigor_gen.py:8`, `CAMPAIGN_DIRECTIVE.md` A5 | `verify_v2.py:462,480,524` all test `len(gtn) < 200`, and `CER_STAGE3B.json` `definition` says "<200 GT chars" | CONTRADICTION (code wins; 179 is wrong) |
| 2 | `kn` and `ml` have ~4 scored pages | `CAMPAIGN_DIRECTIVE.md` A5 / A8, `CER_BY_SCRIPT.md:15-16` | true for the **script** buckets (Kannada 4, Malayalam 4); the **lang-tag** counts are kn 25, ml 5 (Table 2b) | CONTRADICTION (two partitions of the same 400 pages reported as one) |
| 3 | `dominant_script` for te_024, te_065 is Telugu | `level2/pages_script_map.json` | `level2/pages_manifest.json` says Devanagari for both (same `l1_chars` 285 / 212) | CONTRADICTION (2 of 400 pages; CER_BY_SCRIPT.md:230 tiers te at n=6, this moves at most 2 pages) |
| 4 | sarvam_bench fill GT is "machine GT" | `AGENT_PROTOCOL.md` / probe22 protocol | indic-ocr-bench README, fetched 2026-09-29: "All ground-truth text has been **reviewed twice by human language experts**" | CONTRADICTION resolved toward the card; s6.4 stays LOCKED per the directive |

## NORMALISATION DIFF — ours vs Sarvam

Both files were opened in this run:

- ours: `level2/probe22/metrics.py` (975 lines, sha256 `de3c8ad1c5eae694…`)
- theirs: <https://huggingface.co/datasets/sarvamai/indic-ocr-bench/raw/main/metrics.py> (30,067 bytes, 935 lines, fetched 2026-09-29)
- their card: <https://huggingface.co/datasets/sarvamai/indic-ocr-bench> (`README.md`, fetched 2026-09-29)

A whole-file `diff` gives **104 changed lines in 6 semantic groups**. Rows below are the steps the task asked for; the last four are the ones that actually move the number.

| normalisation / scoring step | ours (`level2/probe22/metrics.py`) | Sarvam (`metrics.py`, fetched 2026-09-29) | impact on comparability |
|---|---|---|---|
| Unicode NFC / NFKC | `normalize_for_metrics` NFC → folds; `normalize_for_scoring` NFKC then NFC; `_content_base_normalize` `nfkc_nfc` | **identical** | none |
| control characters | **extra line not in Sarvam**: `"".join(ch for ch in text if ord(ch) >= 32 or ch in "\n\t\r")` in both `normalize_for_metrics` and `normalize_for_scoring` (our lines 130, 143) | not present | ours deletes C0 controls from both sides; slightly *lowers* both, tiny and near-symmetric |
| whitespace / newline flattening | `apply_replace_n` + `collapse_whitespace` (`[\u200B-\u200D\uFEFF]` removed, `\s+`->` `, strip) | **identical** | none |
| quote / dash unification | `fold_quotes` (“ ” « » ‘ ’), `fold_dashes` (— – ―) | **identical** | none |
| Indic punctuation | `normalize_indic_punctuation` (`\|\|`→`॥`, Indic-context `\|`→`।`, pad both to spaced form); `unify_danda_pipe` in content folds | **identical** | none — **danda and double danda are handled the same on both sides** |
| ZWJ / ZWNJ | `collapse_whitespace` strips U+200B–200D; content fold `strip_zwj_zwnj` removes U+200C/U+200D | **identical** | none |
| nukta handling | none — no nukta normalisation anywhere in either file | none | none; both score क़ and क़ as different (2 edits) |
| digit normalisation | none in either file (no Devanagari/Bengali-digit folding) | none | none; both count १ vs 1 as an error |
| case | **not lowercased** by `metrics.py` (only by the South-400 writer, see Table 3) | not lowercased | none for probe22-vs-probe22; matters only when compared to South-400 |
| **empty / missing prediction** | scored **`cer=1.0, wer=1.0`**, `invalid=False`, `missing_prediction=True` — it **counts in the mean** | `metrics=None, invalid=True` — it is **excluded from every mean** | **LARGE.** Our denominators include every abstention as a 100 % error; Sarvam silently drops them. Over the 1,227 scored items our sheet has 617 empty anuvaad, 343 empty rapidocr, 536 empty paddle, 129 empty surya (easyocr 0) — Sarvam's rule would have deleted all of those rows |
| **tail loops / catastrophic output** | counted as errors in `avg_metrics` and in `lang_wise_scores` (only excluded from `valid_samples_*`) | **excluded from `lang_wise_scores` entirely** (`if row["invalid"] or row["loop_or_catastrophic"] …: continue`) | **LARGE.** Their README: "Predictions that exhibit runaway repetition (tail loops) are flagged separately and excluded from valid-sample metrics." |
| **short GT** | rows with <50 non-space GT chars get `short_gt=True` and are **dropped from all means** (`primary` list, reported as `short_gt_count`) | **no short-GT rule at all** | **LARGE.** Sarvam has no GT floor; they keep near-empty GT rows (which inflate CER) and we delete them |
| **word split/merge fallback** | `equalize_space_only_issues` final fallback returns `gt2, pred2` — our comment: "Never overwrite pred with GT — that forged CER to 0 for real word-segmentation errors." | returns **`gt2, gt2`** — i.e. it substitutes the GT for the prediction on that branch | **Sarvam's version reports CER 0 for a class of real errors.** This inflates their score; our fix is correct and makes us look worse. Unknown how many rows hit it |
| `cer_uncapped` | extra metric, unbounded per-sample CER | not present | none for `avg_metrics.cer` (still capped at 1.0 by `_bound_rate` on both sides) |
| `LANG_ORDER` / TSV columns | probe22 ISO codes + legacy full names | top-10 Indic full names | cosmetic |

### What the headline score is

From their README (fetched 2026-09-29): **Word Accuracy = 100 × (1 − WER)**, with CER and WER both reported. Per-sample CER and WER are **capped at 1.0** on both sides (`_bound_rate`), and the two headline aggregates Sarvam publishes are `avg_metrics` (all scored samples) and `valid_samples_cer` (loops excluded). **What "87.39" is: UNKNOWN.** The number appears in this repo only at `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:18`, which itself calls it DEAD for direct comparison; their README (opened this run) defines no single headline score and does not state 87.39 anywhere. Until the Sarvam source for 87.39 is opened and its metric and denominator are named, it is not comparable to any number in Table 2 — it may be word accuracy, 1-CER, or a mean over a subset, and this table carries no WER column.

### Net direction of the divergence

Rows 1–8 are cosmetic and cancel out. Rows 9–11 all move in the same direction: **our scorer is harsher.** We count abstentions and runaway loops as errors where Sarvam drops the row, and we delete their short-GT rows that we would otherwise be punished for. Row 12 goes the other way and is a genuine **bug in the Sarvam file** that inflates their number. Conclusion for the boss: **any "we vs Sarvam 87.39" statement is invalid until both sides are re-scored through one scorer.** The only defensible statement today is the *paired, same-scorer* one in the summary: on the 54 items Sarvam actually ran, our own scorer gives Sarvam CER 0.2640 and our best local engine a lower mean in 9/18 languages — directional noise at n=3/lang.

## UNRESOLVED

| # | item | status | why it is open |
|---|---|---|---|
| 1 | How many rows hit Sarvam's `return gt2, gt2` word-split/merge branch | UNKNOWN | requires re-scoring the Sarvam published run; the dataset was not downloaded (no downloads without approval) and the 87.39 run is not on this disk |
| 2 | The correct `gt_thin` threshold (179 vs 200 chars) | CONTRADICTION | code says 200 in three places, two docs say 179; changing it re-opens the writer basis and is outside this read-only wave |
| 3 | `dominant_script` for te_024 / te_065 | CONTRADICTION | `pages_script_map.json` and `pages_manifest.json` disagree; the CER_BY_SCRIPT te bucket (n=6) could be 6 or 4 Telugu pages |
| 4 | Per-language Sarvam comparison on all 6,909 bench items | DEAD (out of budget) | the 54-call cap is reached (`CAMPAIGN_DIRECTIVE.md` A8); 3/lang is all we will ever have without the boss's explicit yes |
| 5 | Whether the 56 unscored manifest additions should be scored | UNKNOWN | engine output packs for them are partial (surya 43/56); outside this wave's read-only scope |
| 6 | CER for the 274 South pages with no CER | DEAD (GT absent) | 219 have GT < 200 chars, 55 are mojibake PDF layers; no re-sourcing is possible without new PDFs, and `AGENT_PROTOCOL.md` forbids lowering the gates |
| 7 | `EVIDENCE_SUMMARY.md` s3 brx/or/sa values | KNOWN-STALE | they are correct for `scores/metrics_*_normalized.json` and wrong for `sheet.csv` today; the fix belongs to the lead, not this agent (I write only this md and the script) |

---

*Regenerate: `python3 level2/unified/build_benchmark_22.py > docs/campaign/BENCHMARK_22.md`. The script reads its five sources and writes nothing but stdout.*

---

## ERRATUM 2026-09-30 (Sonnet lead) — the "byte-identical" legend is WRONG

This document's legend says the three Tesseract aliases (`tesseract_bilingual`, `tesseract_indic`, `openbharatocr`) are **byte-identical**. **They are not.** Measured on `sheet.csv` 2026-09-30: their `prediction` strings **differ on 857 of 1,227 items** (`tesseract_bilingual` vs `tesseract_indic`, and `tesseract_bilingual` vs `openbharatocr`, both 857/1,227) — they are the same engine family with **different language packs**, which is why their *mean* CERs coincide on many languages while their per-item outputs do not.

Consequence for the reader: the "10 independent engines" framing still holds as a *count of model strings minus the two known aliases*, but the three must not be treated as interchangeable per item, and any per-item comparison involving them is measuring language-pack choice, not engine quality.

`CAMPAIGN_DIRECTIVE.md:118` carries the same superseded "byte-identical" wording. **The directive is law and is not edited** — ERRATUM-F2 filed in the feed.
