# CER by dominant script — WRITER basis (C6) + rigor add-ons (C7, C2 FULL AKER)

_generated_at: 2026-09-13T21:26:32+00:00 · generator: `research/metrics_rigor_gen.py` · bootstrap seed 20260914, 1000 resamples (deterministic)_

**Basis (disk truth, v2 — SUPERSEDES gates/CER_CLEAN_GT_RECOMPUTE.json):** fresh reports/CER_STAGE3B.json per-page entries with non-null `cer` (the verify_v2.py writer nulls page-level: `reason:legacy_mojibake_layer` on 55 pages, `reason:gt_thin` on 219 GT<179c pages). Writer basis = **n=126** pages (surya/anuvaad/IPO/…: nulls are page-level, never engine-level — every basis page has non-null CER for ALL 10 engines, asserted at generation). CER = Levenshtein/NFC/lowercase/whitespace-collapsed vs PDF text-layer GT (definition in CER_STAGE3B.json). GT density = `gt_chars` (PDF layer) — NOT manifest `l1_chars` (L1 is distilled-VLM gold, circular per RED A3).

## 1. Per-script median CER (C6 — the Bhashini/David table)

Rows = manifest `dominant_script` buckets of the writer-basis pages; columns ordered by overall writer-basis median (ascending = best first). **n per cell is the row's n (same pages for every engine — CER nulls are page-level, not engine-level).**

| script (n126 basis) | surya | anuvaad_tesseract | tesseract_indic | openbharatocr | tesseract_bilingual | indicphotoocr | paddleocr_indic | rapidocr | doctr | easyocr | row winner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Telugu (n=6) **small-n** | 0.748 † | 0.759 † | 0.758 † | 0.758 † | 0.757 † | 0.826 † | 0.729 † | 0.750 † | 0.856 † | 0.870 † | **paddleocr_indic** (0.729) |
| Tamil (n=53) | 0.345 | 0.301 | 0.356 | 0.356 | 0.356 | 0.625 | 0.479 | 0.534 | 0.915 | 0.961 | **anuvaad_tesseract** (0.301) |
| Kannada (n=4) **small-n** | 0.398 † | 0.475 † | 0.459 † | 0.459 † | 0.443 † | 0.542 † | 0.546 † | 0.607 † | 0.725 † | 0.920 † | **surya** (0.398) |
| Malayalam (n=4) **small-n** | 0.636 † | 0.642 † | 0.620 † | 0.620 † | 0.620 † | 0.664 † | 0.937 † | 1.000 † | 0.905 † | 0.899 † | **tesseract_indic** (0.620) |
| Devanagari (n=16) | 0.222 | 0.252 | 0.261 | 0.261 | 0.256 | 0.377 | 0.871 | 0.917 | 0.831 | 0.334 | **surya** (0.222) |
| Latin (n=43) | 0.855 | 0.859 | 0.874 | 0.874 | 0.874 | 0.881 | 0.886 | 0.869 | 0.822 | 0.892 | **doctr** (0.822) |
| **ALL (overall)** | 0.430 | 0.475 | 0.493 | 0.493 | 0.493 | 0.655 | 0.707 | 0.712 | 0.853 | 0.902 | **surya** (0.430) |

† small-n: n<10 per cell (te=6, kn=4, ml=4) — do not rank engines on those rows; medians >1.0 on ml = over-capture vs GT length. Per-script winners inside ±0.01 margins are ties, not wins (no per-cell CI at this n; section 2 gives CIs on the pooled basis).

Reading notes (from disk, cross-cited):
- **Tamil n=53 is the one solvable script** and the biggest honest bucket — consistent with surya's own published best-Indic Tamil score (EXTERNAL_BENCHMARK_MAP.md §a: ordinal direction matches).
- **Latin n=43 keeps sane-Unicode legacy layers** that survived the writer's mojibake filter — treat that row as weaker-GT evidence, not engine skill (RED A2/A12 direction).
- Devanagari n=16: legacy-Hindi exam pages, sane GT.
- te/kn remain the hard scripts for every engine (hard-scans, mixed books).

## 2. Bootstrap 95% CIs on the writer basis (C7 — the honest 55-null deck claim)

1000 paired resamples of per-page CERs on the n=126 writer basis (seed fixed, nearest-rank percentiles). Pairwise = **paired** resampling (same pages resampled for both engines, difference of medians per resample).

| engine | median CER (writer n=126) | 95% CI on median |
|---|---|---|
| surya | 0.4299 | [0.3690, 0.5001] |
| anuvaad_tesseract | 0.4751 | [0.3725, 0.5339] |
| tesseract_indic | 0.4930 | [0.4016, 0.5791] |
| openbharatocr | 0.4930 | [0.4016, 0.5791] |
| tesseract_bilingual | 0.4931 | [0.4016, 0.5790] |
| indicphotoocr | 0.6547 | [0.5788, 0.7105] |
| paddleocr_indic | 0.7070 | [0.6412, 0.7417] |
| rapidocr | 0.7116 | [0.6730, 0.7471] |
| doctr | 0.8532 | [0.8309, 0.8724] |
| easyocr | 0.9025 | [0.8890, 0.9178] |

Pairwise, the three deck-relevant pairs:

| pair | Δ median (CER) | 95% CI of Δ median | verdict |
|---|---|---|---|
| surya vs anuvaad_tesseract | -0.0451 (lower=better: surya ahead) | [-0.0864, +0.0201] | TIED (CI includes 0) |
| surya vs indicphotoocr | -0.2248 (lower=better: surya ahead) | [-0.2985, -0.1599] | SEPARABLE |
| anuvaad_tesseract vs indicphotoocr | -0.1796 (lower=better: anuvaad_tesseract ahead) | [-0.2766, -0.1171] | SEPARABLE |

**Verdict: 2/3 deck pairs separable (surya vs indicphotoocr, anuvaad_tesseract vs indicphotoocr); surya-vs-anuvaad stays TIED** — the honest writer-basis (n=126) deck claim: **tier-1 = {surya, anuvaad} tied leaders**, tesseract family at the tier-1 boundary (separable from the leaders only marginally: surya−tess CI [-0.1199, -0.0045], anuvaad−tess CI [-0.0514, -0.0006] — lower bounds graze 0), then a DECISIVE drop to indicphotoocr and below (both leaders separate from IPO by −0.18 to −0.22). Two tiers survive; 'one winner' does not.

Tier picture (paired bootstrap vs each bottom engine, computed here): tesseract_indic separable-from-3/3 tier-1; openbharatocr separable-from-3/3 tier-1; tesseract_bilingual separable-from-3/3 tier-1; paddleocr_indic separable-from-2/3 tier-1; doctr separable-from-3/3 tier-1; rapidocr separable-from-3/3 tier-1; easyocr separable-from-3/3 tier-1.
Alias note (RED A4): openbharatocr ≡ tesseract_indic byte-identical 400/400 — identical CI rows are one engine, not two independent confirmations.

## 3. Clean-vs-HARD split (rival flank #1 — 'our benchmark is HARDER')

**Hardness definition from data, non-circular features only** (no engine outputs involved): a writer-basis page is HARD if `mixed_book_page=true` (multi-script book page) OR GT density in the bottom quartile (gt_chars ≤ Q1=774); EASY = pure-script AND above Q1. Split: EASY n=47, HARD n=79.

| engine | median CER EASY | median CER HARD | Δ (hard−easy) |
|---|---|---|---|
| surya | 0.2057 | 0.5252 | +0.3195 |
| anuvaad_tesseract | 0.2356 | 0.6409 | +0.4053 |
| tesseract_indic | 0.2683 | 0.6469 | +0.3786 |
| openbharatocr | 0.2683 | 0.6469 | +0.3786 |
| tesseract_bilingual | 0.2680 | 0.6469 | +0.3789 |
| indicphotoocr | 0.6701 | 0.6512 | -0.0189 |
| paddleocr_indic | 0.6398 | 0.8167 | +0.1769 |
| rapidocr | 0.6336 | 0.8459 | +0.2123 |
| doctr | 0.9245 | 0.8218 | -0.1027 |
| easyocr | 0.9571 | 0.8370 | -0.1201 |

- EASY scripts = {'Kannada': 1, 'Malayalam': 3, 'Tamil': 41, 'Telugu': 2}; HARD scripts = {'Telugu': 4, 'Latin': 43, 'Kannada': 3, 'Malayalam': 1, 'Tamil': 12, 'Devanagari': 16}.
**Hardness here is script-driven (te/kn hard for everyone) and scan-age-driven, not density-driven** — 'mixed/low-density' ≠ 'harder' in this corpus.

**Hardness evidence line (cite-only, not recomputed):** our benchmark's hardness does not come from cherry-picked 'hard' pages — the ENTIRE 400-page corpus is old-scan-class 200-dpi book/govt renders, i.e. surya's own single WORST published olmOCR-bench category (OldScan pass rate **41.8**, 58 points below their Base 99.7; research/EXTERNAL_BENCHMARK_MAP.md §a, fetched 2026-09-13). Metric caveat stands (their pass-rate ≠ our CER; ordinal direction matches — their best Indic language is Tamil on both sides). Rival answer for SEP16: 'our EASY is their worst category.'

## 4. FULL AKER — all engines, ALL clean-basis pages (C×G verdict basis)

n=83 writer-basis pages (Latin excluded — legacy-mojibake GT makes grapheme metrics meaningless there, RED A7/A2; the writer's mojibake gate already nulled the worst 55, this row cut is the remaining defense). AKER = edit distance over approximate grapheme clusters (base char + Mn/Mc/Me combining marks + ZWJ/ZWNJ; stdlib clustering, no UAX #29) on the same NFC/lower/whitespace basis as CER. GT = full PDF-layer text (training_assets/sft_noisy_to_gold.jsonl; verified to reproduce CER_STAGE3B CERs exactly on sampled pages). Supersedes the 20-page probe that spawned debate C×G.

| engine | median CER (same pages) | median AKER | AKER/CER | CER rank | AKER rank |
|---|---|---|---|---|---|
| surya | 0.3240 | 0.6699 | 2.07 | 1 | 1 |
| anuvaad_tesseract | 0.3413 | 0.7405 | 2.17 | 2 | 2 |
| indicphotoocr | 0.5733 | 1.0607 | 1.85 | 6 | 6 |
| tesseract_indic | 0.3598 | 0.7728 | 2.15 | 3 | 3 |
| openbharatocr | 0.3598 | 0.7728 | 2.15 | 4 | 4 |
| tesseract_bilingual | 0.3598 | 0.7728 | 2.15 | 5 | 5 |
| paddleocr_indic | 0.6845 | 1.1675 | 1.71 | 7 | 8 |
| doctr | 0.8726 | 1.6393 | 1.88 | 9 | 9 |
| rapidocr | 0.6949 | 1.1661 | 1.68 | 8 | 7 |
| easyocr | 0.9321 | 1.7032 | 1.83 | 10 | 10 |

- CER order (full basis): surya < anuvaad_tesseract < tesseract_indic < openbharatocr < tesseract_bilingual < indicphotoocr < paddleocr_indic < rapidocr < doctr < easyocr
- AKER order (same pages): surya < anuvaad_tesseract < tesseract_indic < openbharatocr < tesseract_bilingual < indicphotoocr < rapidocr < paddleocr_indic < doctr < easyocr
- **Top-2 question (surya vs anuvaad):** CER says surya < anuvaad_tesseract (0.3240 vs 0.3413); AKER says surya < anuvaad_tesseract (0.6699 vs 0.7405).
- **AKER does NOT reorder the top-2 on the full basis** (Δ AKER median surya−anuvaad = -0.0706, paired-bootstrap CI [-0.2136, +0.0860], TIED).
- Per-script AKER medians (top-3 engines):
  - Telugu (n=6): surya 0.986; anuvaad_tesseract 0.982; indicphotoocr 1.092
  - Tamil (n=53): surya 0.672; anuvaad_tesseract 0.598; indicphotoocr 1.142
  - Kannada (n=4): surya 0.632; anuvaad_tesseract 0.763; indicphotoocr 0.941
  - Malayalam (n=4): surya 1.525; anuvaad_tesseract 1.541; indicphotoocr 1.627
  - Devanagari (n=16): surya 0.448; anuvaad_tesseract 0.498; indicphotoocr 0.719

## 5. DEBATE C×G VERDICT (metric for deck accuracy claims)

**AKER does NOT reorder the top-2 on the full clean basis (n=83) → deck keeps CER for accuracy claims (continuity + Stage-3b preference pairs are CER), AKER disclosed as the phonetic-fairness check. The 20-page probe reorder that spawned debate C×G does NOT survive the full basis — resolved.**

## 6. Fission spawns (PART 1.5 law)

- C-C6.2: writer-basis per-script cells still lack CIs (te=6/kn=4/ml=4) — a stratified bootstrap or exact permutation on Tamil (n=53) vs Devanagari (n=16) surya gaps is the next separability question.
- C-C7.2: power calc — how many MORE honest pages (L1-gold verified GT or 300-dpi re-OCR of mojibake pages) would make surya-vs-anuvaad separable, if the true Δ is the observed point estimate?
- C-FLANK.3: the 55 legacy_mojibake_layer pages are unrecoverable GT — would David accept an L1-gold (distilled-VLM) GT sub-basis for just those pages as a disclosed robustness check (circularity risk known)?

---
_Inputs: reports/CER_STAGE3B.json (writer basis — non-null cer entries) · pages_manifest.json · training_assets/sft_noisy_to_gold.jsonl · level2/out/*/\*.json (AKER). No engine runs; no shared files modified. Supersedes gates/CER_CLEAN_GT_RECOMPUTE.json-basis editions. Companion numbers: reports/CER_METRICS_RIGOR.json._
