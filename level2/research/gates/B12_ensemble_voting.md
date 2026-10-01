# GATE G-B12 — ENSEMBLE VOTING: does ≥3-family agreement beat the best single engine?

Date: 2026-09-13 · Runner: EXEC (opencode) · Env: `.venv/bin/python` (stdlib + pymupdf only)
Basis: 115 clean-GT dense pages (CER_CLEAN_GT_RECOMPUTE.json clean_pages minus ml_091, which
is gt_thin cer:null in CER_STAGE3B — the 61 artifact pages were never touched, per gate law).
CER basis = CER_STAGE3B exactly: NFC + lowercase + whitespace-collapsed Levenshtein / len(GT),
GT = PDF text layer (pymupdf). Reproducibility: recomputed surya CER on ta_012/kn_014/ml_028
matches CER_STAGE3B to 4 decimals before any ensemble run.
Families (7 independent, tesseract-family = 1 vote per DECISIONS engine-count law,
tesseract_indic as representative — openbharatocr is a byte-identical alias):
tesseract_indic, easyocr, paddleocr_indic, indicphotoocr, doctr, surya, rapidocr.
Raw data: `research/gates/b12_results.json` · Script: `research/gates/b12_ensemble.py`
(idempotent, no shared .py touched, no engine reruns).

## Method (ROVER-style, simple, as specified)

1. Lines normalized (NFC, strip, collapse spaces).
2. Greedy clustering in fixed family order: incoming line joins FIRST existing cluster with
   pairwise char 5-gram Jaccard ≥ 0.5, else opens new cluster. (A best-match variant was
   probed on 6 pages: CER moved ≤0.4pt — greedy kept, per METHOD's simplicity clause.)
3. Two ensemble texts per page:
   - **full ensemble** = all clusters, majority variant per cluster (classic ROVER union);
   - **agreement text** = clusters backed by ≥3 families only (the gate's actual question).
   Plus a robustness variant: **reference-skeleton voting** (tesseract_indic anchor, other
   families best-match onto unused slots, majority per slot) — bounds length by construction.
4. Per page: ensemble/agreement/skeleton CER vs GT, best-single CER (oracle over the 7
   family representatives), and char 5-gram precision/recall of agreement text vs GT
   (the "is the agreed content itself clean" lens that raw CER hides, because CER punishes
   low coverage even when every agreed character is right).

## 1. Headline: ensemble vs best single (115 pages)

| metric (median) | value |
|---|---|
| full-ensemble CER | **3.921** (ensemble text ~4–5× GT length — duplicate cluster inflation) |
| agreement-text CER (≥3 families) | 0.8973 (median coverage 34% — CER dominated by missing GT) |
| skeleton-ROVER CER | 0.7671 |
| **best single engine (oracle)** | **0.6278** |
| agreement beats best single on | 9/115 pages (margins mostly <2%; >5% only on ta_066, ta_091, te_077) |
| full ensemble beats ALL singles on | **0/115 pages** |
| full ensemble worse than WORST single on | **115/115 pages** |

**VERDICT G-B12: NO.** Ensemble voting does NOT beat the best single engine on median CER
by ≥5% — it doesn't beat it at all (0.897 agreement / 3.92 full vs 0.628 best-single; the
≥5% bar would need ≤0.596). The verdict survives all three alignment schemes. "Free
pseudo-GT expansion for Stage 3" via consensus-as-GT is REJECTED for page-level text
replacement.

**Why (mechanism, not excuse):** engines disagree on *line segmentation* at wildly different
granularity (te_001: surya 15 lines vs tesseract 32 vs paddle 46; kn_014: surya 3 mega-lines
vs doctr 44). Jaccard-5 line matching cannot align a 3-line and a 44-line reading of the same
page, so most clusters are singletons; the union then carries every engine's hallucinations
and dropouts in duplicate → CER > worst single on 115/115. The ≥3-family agreement filter
kills the noise but also the coverage (median 34%).

## 2. Per-script table (median CER; agreement coverage & precision in parens)

| script | n | best-single | agreement-text | full ensemble | agreement prec / rec |
|---|---|---|---|---|---|
| Tamil | 24 | **0.3311** | 0.5938 | 4.042 | 0.767 / 0.593 (cov 0.65) |
| Devanagari | 24 | **0.3769** | 0.8924 | 3.109 | 0.669 / 0.120 (cov 0.15) |
| Latin-bucket | 34 | **0.8225** | 0.9283 | 3.758 | 0.069 / 0.294 (cov 0.29) |
| Kannada | 17 | **0.8589** | 0.9777 | 4.538 | 0.018 / 0.131 (cov 0.13) |
| Malayalam | 4 | **0.8513** | 0.9991 | 5.236 | 0.000 / 0.000 (cov 0.00) |
| Telugu | 12 | **0.8407** | 0.9062 | 3.265 | 0.024 / 0.296 (cov 0.50) |
| **ALL** | **115** | **0.6278** | 0.8973 | 3.921 | 0.598 / 0.046 |

Best single wins in every script bucket. (Latin bucket = manifest dominant_script, mostly
mixed-language kn/te textbook pages.)

## 3. The consolation precision finding (the real mini-result)

Agreement text is *cleaner per character written* — it just writes too little:

| 5-gram lens (median, 115p) | agreement text | best single |
|---|---|---|
| precision (of what it writes, how much is right) | **0.598** | 0.355 |
| recall (of GT, how much it covers) | 0.046 | 0.276 |

On 17/115 pages the agreement text has precision ≥0.9 (best single: 8/115). Pages where
agreement text is BOTH ≥0.9 precision AND ≥0.9 recall — i.e. genuinely pseudo-GT-grade —
**6/115: kn_033, kn_066, kn_067, kn_073, te_012, te_077** (at prec≥0.8∧rec≥0.8: 9; at
prec≥0.9∧rec≥0.5: 12). Eyeball check te_077 (English literature reader): agreement text
reads verbatim-correct; kn_073 identical to GT modulo a page number. These are real but
scarce, and on 5 of the 6, some single engine already achieves equal-or-better CER — the
agreement filter's job there is *telling us which pages are safe*, not out-writing the engines.

## 4. The poisoned-GT sub-finding (inverted twin, fission law)

The clean-GT filter (FFFD/PUA <0.5%) does NOT catch **legacy-font mojibake layers**: 52 of
the 115 "clean" pages have GT with ≥5% Latin-1-supplement/symbol characters after excluding
legit typography (curly quotes, dashes, ©®°×…). Examples: te_022 GT is `§óþÔ¶ý…õ³Ææÿ$…`
(Telugu page, legacy font); ml_028 GT is `a[ptcmZmcw' F∂ hm°v…`; kn_026 GT is
`gÁdå ²PÀët ¸ÀA±ÉÆÃzsÀ£É…`. On these 52 pages engines that READ THE PAGE CORRECTLY get
CER ~0.85–1.0 against mojibake GT — the CER-based "best engine" is inverted. Non-mojibake
subset (63 pages): best-single median 0.306, agreement 0.645, agreement precision 0.741 ≈
best-single precision 0.747 (the precision advantage evaporates once GT is sane — it was
mostly "engines agreeing with each other against broken GT").

## 5. Worst-3 ensemble failures (inspect duty)

| page | full-ens CER | best single | cause |
|---|---|---|---|
| te_022 | 7.22 | surya 0.864 | **bad GT** (legacy-font mojibake layer) + 380 clusters from 7 segmentations; nothing aligns; union = 5× mojibake-GT noise |
| kn_014 | 5.30 | surya 0.159 | surya reads the Sanskrit śloka page nearly perfectly in 3 mega-lines; tesseract/doctr emit 34–44 fragment lines; 180 clusters, only 1 agreement cluster → ensemble = 5× dup noise over a page one engine already nailed |
| ml_028 | 5.41 | paddleocr 0.765 | bad GT (mojibake) + rapidocr emits ZERO lines on the page (empty pack) + easyocr 1 mega-line vs paddle 73 fragments → alignment impossible |

Failure-mode taxonomy: (1) bad GT so "failure" is partly an artifact of the metric;
(2) segmentation-granularity mismatch — the dominant, structural cause; (3) empty/degenerate
packs (rapidocr ml_028) that drag the union. In NO inspected case did the ensemble make
text *worse* than its inputs line-by-line — it made it *longer and duplicated*, which CER
punishes as insertion errors.

## 6. VERDICT + consequences

- **G-B12 = NO.** Ensemble voting is not a pseudo-GT generator at page level in this engine
  field: 0/115 pages beat all singles, median CER ~43% WORSE than best single (agreement) /
  6× worse (full union). Not within any margin of the ≥5% win bar.
- **NO free pseudo-GT expansion for Stage 3 deck wiring.** The honest pipeline stays:
  CER-vs-PDF-layer for preference pairs (already shipped), L1 human labels for gold.
- **DO adopt the agreement filter as a CONFIDENCE MARKER, not a text source**: 6 pages
  (5% of clean corpus) are consensus-verified pseudo-GT-grade at zero human cost — usable as
  extra DPO pairs or as "high-agreement" strata in sampling; and agreement-precision ≥0.9
  (17 pages) is a cheap flag for "no human check needed here" triage in Stage-1 queueing.
- **Mini-result for the paper (defensible, honest):** "Cross-family OCR agreement is a
  precision instrument, not a coverage instrument: ≥3-family consensus text is ~1.7× cleaner
  per-character than the best single engine (5-gram precision 0.60 vs 0.36 median) but covers
  only ~5% of GT content; and 45% of 'clean' PDF text layers in South-Indian gov/textbook
  scans are legacy-font mojibake that standard GT-hygiene filters miss."
- Consequence for claims: SEP16 deck must NOT say "10 engines vote = free ground truth."

## Conflicts found / spawned (fission duty)

- C2 (P0, feeds RED): the 52-page mojibake-GT census means CER_CLEAN_GT_RECOMPUTE's "clean"
  list is only half-clean → every CER-based ranking (incl. surya #1) carries a GT-quality
  caveat on ~45% of its basis. Successor gate: re-run clean-GT recompute with the
  legacy-font detector added; check if the honest engine ranking flips again.
- Q-B12.1 (deeper): would region-level (not line-level) voting — clustering on engine
  region bboxes instead of text lines — fix the granularity mismatch? Parked; needs bbox
  truthing, not a 100-line script.
- Q-B12.2 (inverted): can consensus DISAGREEMENT (low agreement-cluster count) serve as a
  cheap page-difficulty proxy for the Stage-1 human-labelling queue? Measurable now from
  b12_results.json (n_agreement_clusters per page) — candidate for REVIEW_QUEUE.md triage.
- Q-B12.3 (broader): does the 6-page pseudo-GT set grow enough at 8 families (add
  Sarvam/Bhashini at L3) to matter? Re-gate after L3 engine drop-in.
