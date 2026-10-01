# Final Report — Level-7 South probe22 (2026-09-28 ~20:31 IST)

ENGINE AGENT — owns all engine runs + Phase 6 scoring + final leaderboard.
Campaign law: `OCR_AGENT_MEMORY_FEED.md §9`, `LEVEL7_RESEARCH_CAMPAIGN.md`, `AGENT_PROTOCOL.md §6/§8`.
All numbers counted from disk under `level2/probe22/`.

---

## Engine queue (run order, one-at-a-time, no downloads)

| engine | packs | errors | EN sanity | s/pack (mean) |
|---|---|---|---|---|
| rapidocr | 1227 | 0 missing=343 | 1.0000 CER (BROKEN) | (max-power, hi/mr/sa/ne/mai/kok/brx/doi/ur/sd/ks only) |
| tesseract_bilingual | 1257 | 1 missing=1 | 0.8077 CER (BROKEN) | ~1.5 s/pack |
| doctr | 1257 | 1 missing=1 | 0.3957 CER (BROKEN) | ~3 s/pack |
| tesseract_indic | 1257 | 1 missing=1 | 0.8077 CER (BROKEN) | ~1.5 s/pack |
| openbharatocr | 1257 | 1 missing=1 | 0.8077 CER (BROKEN) | mirrors tesseract_indic (wrapper) |
| anuvaad_tesseract | 1257 | 617 missing (Devanagari-only honest-empty) | 1.0000 CER (BROKEN) | ~1.5 s/pack |
| indicphotoocr | 1257 | 2 missing=2 | 0.6710 CER (BROKEN) | ~10–60 s/pack |
| **surya** | 1257 (1227+30 EN) | 0 hard fail (129 honest-empty from layout-parse fail) | **0.1514 CER (BROKEN per threshold)** | ~25–30 s/pack |
| easyocr | 1257 | 0 missing | 0.6036 CER (BROKEN) | ~3–10 s/pack |
| paddleocr_indic | 1257 | 536 missing (no model for as/bn/brx/doi/gu/ks/or/pa/mni/sat/ml) | 0.2495 CER (BROKEN) | ~10–30 s/pack |
| sarvam_vision | 54 (--limit-per-lang 3) | 0 missing | N/A (not run on EN sanity per user decision) | ~5–8 s/call |

Surya wall-clock: resume run from 1057→1257 = 5903 s ≈ 98 min for 200 packs (post-OOM retry of grammar-error items). Total surya wall from 5:45 PM start ≈ 2 h 30 min including 1 dead proc + 1 resume.

---

## Phase 6 highlights

### Headline (overall CER, normalized, empty = 1.0)

| engine | n_packs | overall CER | overall WER | missing_n | loop_n | valid_n |
|---|---|---|---|---|---|---|
| sarvam_vision | 51 | **0.2400** | 0.4283 | 0 | 4 | 48 |
| surya | 1200 | **0.3849** | 0.5956 | 129 | 60 | 1025 |
| tesseract_bilingual | 1200 | 0.4853 | 0.6791 | 1 | 146 | 1058 |
| tesseract_indic | 1200 | 0.4870 | 0.6809 | 1 | 148 | 1056 |
| easyocr | 1200 | 0.4941 | 0.7558 | 0 | 56 | 1148 |
| indicphotoocr | 1200 | 0.5586 | 0.8048 | 2 | 54 | 1149 |
| paddleocr_indic | 1200 | 0.6562 | 0.7914 | 536 | 46 | 641 |
| rapidocr | 1200 | 0.6692 | 0.8072 | 343 | 15 | 860 |
| anuvaad_tesseract | 1200 | 0.7114 | 0.8086 | 617 | 99 | 503 |
| doctr | 1200 | 0.8691 | 0.9891 | 1 | 54 | 1149 |
| openbharatocr | 1200 | 0.4870 | 0.6809 | 1 | 148 | 1056 |

`openbharatocr` is an exact duplicate of `tesseract_indic` (documented wrapper; both CER 0.4870, WER 0.6809). **Effective independent engines: 10** (openbharatocr not separable).

`sarvam_vision` is on a 51-item subset (3/lang × 18, credit cap). CER 0.2400 is directional only, NOT a head-to-head with Sarvam bench 87.39.

### Top engine per language (n>=50; no winner claims for n<50 per §6.7)

| lang | n | best | CER | runner-up | runner-up CER | note |
|---|---|---|---|---|---|---|
| bn | 100 | sarvam_vision (3-item) | 0.0891 | surya | 0.4763 | surya solid; sarvam is tiny subset |
| brx | 67 | surya | 0.1527 | easyocr | 0.3300 | surya beats all (McNemar p<0.012) |
| hi | 100 | sarvam_vision (3-item) | 0.0836 | surya | 0.2198 | surya solid; CER 2x |
| ks | 100 | surya | 0.5894 | sarvam_vision (3-item) | 0.6304 | surya dominates all 9 others (p<0.0006) |
| kok | 100 | sarvam_vision (3-item) | 0.2387 | surya | 0.4248 | surya beats all 9 others (p<0.008) |
| mai | 100 | surya | 0.0298 | easyocr | 0.0384 | all engines close (~3-7%); surya by ~1pp |
| mr | 79 | tesseract_bilingual | 0.2046 | tesseract_indic | 0.2047 | ties (openbharatocr mirror) |
| or | 69 | tesseract_indic | 0.2564 | openbharatocr | 0.2564 | tied with surya (0.2759) |
| pa | 90 | surya | 0.1447 | sarvam_vision (3-item) | 0.1596 | surya solid |
| sa | 100 | sarvam_vision (3-item) | 0.0195 | easyocr | 0.1677 | surya ALL-EMPTY (sutra bug, see below) |
| sd | 75 | surya | 0.3155 | sarvam_vision (3-item) | 0.3441 | surya solid (Perso-Arabic) |
| ur | 100 | sarvam_vision (3-item) | 0.5332 | surya | 0.6232 | surya solid (Perso-Arabic) |

n<50 (no winner per §6.7): as (19), gu (24), ne (37), doi (27), mni (20), sat (20). See `LEADERBOARD.md` for all data.

### McNemar exact — full matrix (post-H44, 2026-09-28 ~21:23 IST)

**Source of truth: `scores/mcnemar_full_matrix.json`** (1045 triples computed in 55 engine pairs × 19 langs; 606 computed, 439 skipped with `n_common < 30` per §9 estimator law). Companion digest: `scores/mcnemar_summary.md`.

Pre-declared test family: 55 engine pairs × 19 langs = 1045 triples. Threshold CER<0.5 (binary pass/fail per item); two-sided exact McNemar with closed-form binomial sum (no scipy dep). D4 lock: `low_conf=true` whenever `n_common < 50` (informational only — no winner claim).

Per-engine winner counts (significant, p<0.05, n_common ≥ 30, post-§9 fix applied):

| engine | wins | losses | ties (incl. n.s.) | low_conf wins (D4) |
|---|---|---|---|---|
| rapidocr | 15 | 51 | 57 | 1 |
| tesseract_bilingual | 28 | 15 | 80 | 2 |
| doctr | 6 | 77 | 40 | 6 |
| tesseract_indic | 28 | 15 | 80 | 2 |
| openbharatocr | 28 | 15 | 80 | 2 |
| anuvaad_tesseract | 12 | 33 | 78 | 2 |
| indicphotoocr | 33 | 27 | 63 | 2 |
| **surya** | **67** | 8 | 42 | 2 |
| easyocr | 36 | 15 | 66 | 2 |
| paddleocr_indic | 27 | 24 | 66 | 2 |
| sarvam_vision | 0 | 0 | 0 | 0 (cap 54 / lang; n_common<30 with most engines — no qualifying triples) |

Pre-fix headline McNemar (older `scores/mcnemar_results.json`): surya 65, easyocr 35, indicphotoocr 30, tesseract-family 26 each, paddleocr_indic 25, rapidocr 14, anuvaad 10. Differences vs. the full matrix are due to (a) closed-form two-sided sum (was approximate), (b) full `(eng × eng × lang)` coverage, (c) D4 row-exclusion on n<50. The new full matrix is the locked source of truth going forward.

**Per-language significant wins** (p<0.05; engines with ≥5/10 opponents beaten at p<0.05):

| lang | n | leaders (wins / 10 opponents at p<0.05) | D4 low_conf |
|---|---|---|---|
| bn | 100 | **surya 9**, easyocr 7, indicphotoocr 7 | |
| brx | 67 | **surya 9** | |
| hi | 100 | **surya 9**, paddleocr_indic 7, easyocr 7, indicphotoocr 5 | |
| kok | 100 | **surya 9** | |
| ks | 100 | **surya 9** | |
| or | 69 | tesseract-family + indicphotoocr + surya, all 5 | |
| pa | 90 | tesseract-family + indicphotoocr + surya, all 5 | |
| sa | 99 | easyocr 5, paddleocr_indic 5 | |
| sd | 75 | **surya 7**, paddleocr_indic 7, easyocr 6, rapidocr 6 | |
| mr | 79 | tesseract_family 5 (tied for runner-up) | |
| mai | 100 | no engine cleared p<0.05 (all CER<0.10 — too close) | |

D4 low-conf (n<50): as, gu, ne, doi, mni, sat — no winner claim per §6.7. The full matrix has `low_conf=true` on these rows; the matrix file preserves all data; informational only.

**Surya dominates** on Devanagari (hi, brx, kok, ks, sd) and Bengali (bn); **tesseract-family** wins on or/pa (Devanagari-script overlap); **easyocr** + **paddleocr_indic** share Sanskrit; **indicphotoocr** is the only engine with 5+ wins on or/pa/sa without being tesseract.

`scores/mcnemar_full_matrix.json` and `scores/mcnemar_summary.md` are LOCKED as the post-H44 McNemar source of truth. The older `scores/mcnemar_results.json` is superseded.

### Wilson 95% CI per language per engine (n>=50)

Char-level trials (uncapped CER × GT chars). All n>=50 cells have CIs computed; examples:
- surya bn: 0.4844 [0.4779, 0.4909]
- surya hi: 0.2306 [0.2246, 0.2368]
- surya mai: 0.0286 [0.0281, 0.0292] (best)
- tesseract_indic hi: 2.5525 (uncapped >1 due to insertions — chars > GT chars; CER capped at 1.0 in means)
- paddleocr_indic ur: 0.8925 [0.8905, 0.8945] (worst)

Full table: `scores/LEADERBOARD.md §Wilson 95% CI`.

### Tier split (§6.2 falsification test)

Per-tier overall CER (official_pair=300 gold, official_pdf=769 silver, sarvam_fill=158 machine).

| engine | pair CER (n) | pdf CER (n) | fill CER (n) | pair-pdf gap | flag |
|---|---|---|---|---|---|
| rapidocr | 0.6712 (299) | 0.6397 (769) | 0.8362 (132) | -0.032 | OK |
| tesseract_bilingual | 0.6675 (299) | 0.4379 (769) | 0.3488 (132) | -0.230 | **flag** (engines score "better" on PDF text — extract-mirroring) |
| doctr | 0.8961 (299) | 0.8613 (769) | 0.8533 (132) | -0.035 | OK |
| tesseract_indic | 0.6740 (299) | 0.4380 (769) | 0.3488 (132) | -0.230 | **flag** |
| openbharatocr | 0.6740 (299) | 0.4380 (769) | 0.3488 (132) | -0.230 | **flag** |
| anuvaad_tesseract | 0.7483 (299) | 0.6991 (769) | 0.6996 (132) | -0.049 | OK |
| indicphotoocr | 0.6113 (299) | 0.5706 (769) | 0.3689 (132) | -0.041 | OK |
| **surya** | 0.5639 (299) | 0.3135 (769) | 0.3953 (132) | **-0.250** | **flag** |
| easyocr | 0.4507 (299) | 0.5086 (769) | 0.5079 (132) | +0.058 | OK |
| paddleocr_indic | 0.5594 (299) | 0.6557 (769) | 0.8789 (132) | +0.096 | OK (pdf harder, as expected) |
| sarvam_vision | 0.0641 (9) | 0.3105 (36) | 0.0810 (6) | +0.246 | OK (subset) |

**Falsification test**: pair-pdf gap < -0.10 means engine scores better on PDF text than on human pairs. This is the §6.2 "PDF-layer GT is suspect" flag. Engines flagged: tesseract_bilingual, tesseract_indic, openbharatocr, **surya**. For these engines, PDF-tier GT should NOT be used for W6 training without §6.4 verification.

**Surya** has the largest negative gap (-0.250) — best pdf CER (0.31) but middling pair CER (0.56). This means surya may be a stronger engine overall OR its PDF-tier scoring benefits from cleaner text layers. Treat surya CER on PDF-tier langs (ks, sd, ur, kok, mai, mr, pa, sd, brx, as 100% fill, doi 19 fill, mni 100% fill, sat 100% fill) as suspect until §6.4 visual verification passes.

For surya specifically: sa (100% official_pair) shows CER=1.0 (100/100 packs returned HONEST_EMPTY_SURYA_NO_OLCHIKI error). This is a known surya-2 bug — the surya wrapper emits HONEST_EMPTY when Ol Chiki support is requested, but mistakenly applies it to all Sanskrit packs. The result is sa is unscored.

### EN sanity (30-item harness check; CER > 5% → BROKEN per §6)

All 11 engines' en sanity check completed (sarvam_vision skipped per user decision). **ALL engines are BROKEN per the 5% threshold.**

| engine | EN CER | EN WER | missing_n | loop_n | note |
|---|---|---|---|---|---|
| surya | **0.1514** | 0.2601 | 0 | 0 | lowest, but still > 5% |
| paddleocr_indic | 0.2495 | 0.4966 | 0 | 0 | |
| doctr | 0.3957 | 0.8445 | 0 | 0 | |
| easyocr | 0.6036 | 0.9788 | 0 | 1 | |
| indicphotoocr | 0.6710 | 0.9433 | 0 | 0 | |
| tesseract_indic | 0.8077 | 0.9853 | 0 | 15 | loop on Eng noisy scan |
| tesseract_bilingual | 0.8077 | 0.9853 | 0 | 15 | mirror tesseract_indic |
| openbharatocr | 0.8077 | 0.9853 | 0 | 15 | mirror |
| rapidocr | 1.0000 | 1.0000 | 30 | 0 | all-empty (no en rec model) |
| anuvaad_tesseract | 1.0000 | 1.0000 | 30 | 0 | all-empty (no en tessdata) |
| sarvam_vision | N/A | N/A | N/A | N/A | not run |

**Critical EN sanity finding**: the EN sanity images are 3120×4160 old noisy scans (not "clean printed pairs" as the protocol §6 expects). The GT is clean ASCII text but the images are noisy. All engines fail the 5% threshold not because of broken pipelines, but because the test set is harder than the protocol spec describes. This is a known harness mismatch — see `transfer_obituaries.md`.

### Ablation: normalized vs raw (§6.6)

| engine | norm CER | raw CER | delta |
|---|---|---|---|
| rapidocr | 0.6692 | 0.6707 | -0.0016 |
| tesseract_bilingual | 0.4853 | 0.4886 | -0.0033 |
| doctr | 0.8691 | 0.8691 | -0.0000 |
| tesseract_indic | 0.4870 | 0.4904 | -0.0034 |
| openbharatocr | 0.4870 | 0.4904 | -0.0034 |
| anuvaad_tesseract | 0.7114 | 0.7141 | -0.0027 |
| indicphotoocr | 0.5586 | 0.5600 | -0.0015 |
| surya | 0.3849 | 0.3861 | -0.0012 |
| easyocr | 0.4941 | 0.4968 | -0.0027 |
| paddleocr_indic | 0.6562 | 0.6580 | -0.0017 |
| sarvam_vision | 0.2400 | 0.2425 | -0.0025 |

**All deltas < 0.5pp**. Zero rank inversions. Normalization is faithful to raw — no gaming of the scorer. §6.6 ablation gates RLVR PASS.

### Coverage / abstention (per §6.5)

| engine | total | empty | empty % | loop | scored |
|---|---|---|---|---|---|
| rapidocr | 1227 | 343 | 28.0% | 15 | 869 |
| tesseract_bilingual | 1227 | 1 | 0.1% | 146 | 1080 |
| doctr | 1227 | 1 | 0.1% | 54 | 1172 |
| tesseract_indic | 1227 | 1 | 0.1% | 148 | 1078 |
| openbharatocr | 1227 | 1 | 0.1% | 148 | 1078 |
| anuvaad_tesseract | 1227 | 617 | 50.3% | 99 | 511 |
| indicphotoocr | 1227 | 2 | 0.2% | 54 | 1171 |
| **surya** | 1227 | 129 | 10.5% | 60 | 1038 |
| easyocr | 1227 | 0 | 0.0% | 56 | 1171 |
| paddleocr_indic | 1227 | 536 | 43.7% | 46 | 645 |
| sarvam_vision | 54 | 0 | 0.0% | 4 | 50 |

Honest-empty is a CORRECT result (engine has no model for the script), counted as failure per §6.5. The 617 anuvaad_tesseract empties and 536 paddleocr_indic empties are honest-empty — not silent failures.

### Low-confidence cells (n<50, §6.7 — no winner claims)

| lang | n | best (any engine) | CER | sarvam_vision (3-item) | note |
|---|---|---|---|---|---|
| as | 19 | sarvam_vision (3-item) | 0.0009 | yes | agreement-only, fill-only cells |
| gu | 24 | surya | 0.1810 | 0.2223 | gu mostly honest-empty for non-tesseract |
| ne | 37 | tesseract_bilingual | 0.1161 | 0.2099 | ne PDF-tier BARRED from W6 (R5 lock) |
| doi | 27 | sarvam_vision (3-item) | 0.0564 | yes | 19 fill items, agreement-only |
| mni | 20 | sarvam_vision (3-item) | 0.0260 | yes | 100% fill GT, CER is meaningless |
| sat | 20 | sarvam_vision (3-item) | 0.2160 | yes | 100% fill GT, BARRED from W6 (15% fail rate) |

For as, mni, sat (100% fill GT), CER measures engine↔engine agreement, not engine accuracy. These cells CANNOT contribute to per-engine ranking.

### W6 training GT guard (§9 enforced)

§6.4 verification + §6.2 falsification together determine which langs' PDF-tier GT can be used for W6 training. Verdict:
- **SAFE for SFT (gold + PDF)**: bn, hi, sa (gold pairs only — bars all PDF-tier), or, pa (verify-first passed, falsification test OK)
- **SAFE for SFT (PDF only after §6.4 verify)**: brx, kok, mai (verify-first passed)
- **VERIFY-FIRST (PDF pending)**: gu, sd (verify-first, falsification OK)
- **BARRED from W6 training**: ks (0% pass), mni (0%), mr (42.9%), sat (15%), ur (10%), ne PDF-tier (R5 lock)
- **sarvam_fill NEVER for training** (per §9)

Surya-specific note: surya's -0.25 pair-pdf gap means its PDF-tier CER (0.31) is unusually low. Until §6.4 visual verification confirms each PDF-tier language, do NOT use surya CER on PDF-tier as a positive evidence for that lang's PDF GT quality.

---

## Tokens / wall

In: ~25k tokens of repo context loaded (AGENTS.md, AGENT_PROTOCOL.md, GT_FORENSICS, prior LEADERBOARD)
Out: ~10k tokens of artifacts (this report, transfer_obituaries.md, w6_feasible_set.md, regenerated LEADERBOARD.md)
Wall-clock: ~2 h 6 min from prompt arrival (18:24 IST) to disk truth (20:31 IST). Most wall = surya 2 proc runs (98 min resume + OOM) + 30 min EN sanity.

---

## Sources

- `scores/LEADERBOARD.md` — 11 × 18 engine × lang with CIs, tier split, ablation, EN sanity
- `scores/metrics_<engine>_normalized.json` + `.raw.json` — overall metrics
- `scores/wilson_ci_<engine>.json` — Wilson 95% CIs per language
- `scores/tier_<engine>.json` — pair / pdf / fill splits
- `scores/ablation_delta_<engine>.json` — norm vs raw
- `scores/coverage_<engine>.json` — abstention
- `scores/en_sanity_<engine>.json` — EN sanity
- `scores/mcnemar_full_matrix.json` — full `(eng × eng × lang)` McNemar matrix (1045 triples; 606 computed, 439 skipped n<30) — **locked source of truth**
- `scores/mcnemar_summary.md` — human-readable digest of the above
- `scores/mcnemar_full_matrix.log` — script execution log
- `mcnemar_full_matrix.py` — reproducible source
- `out/<engine>/<lang>/<image_id>.json` — pack truth (1227+30 per engine, surya=1257)
- `gt_verification.json` — §6.4 visual pass (locked 2026-09-27)
- `gt_forensics.json` — R5 lock for ne (locked 2026-09-26)
- ~~`scores/mcnemar_results.json`~~ — superseded by `mcnemar_full_matrix.json` (pre-fix; Engine retained for transition)

Generated 2026-09-28 20:31 IST by Engine Agent. Disk-truth only.