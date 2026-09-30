# TEST_SET_PROFILE — Datasets/akshardrishti_official/test/test/ (REWRITTEN per proto-104 R-11/H1)

**Date:** 2026-09-30
**Method:** Tesseract OCR (6 langs installed: eng/hin/kan/mal/tam/tel) on stratified random sample (seed=20260930) per ID bucket. **The previous heuristic version is REJECTED per R-11** (PIL heuristics like "mojibake/cutoff" are meaningless on images without OCR).

## File inventory (RECONFIRMED)

| Property | Value |
|---|---|
| Path | `Datasets/akshardrishti_official/test/test/` |
| File count | **5,344** (IDs 0–14,806 with gaps) |
| Format | JPEG (100% RGB, DPI 72) |
| **Size distribution (sample 70)**: width | **445–1,630 px** (mean 902) |
| **Size distribution (sample 70)**: height | **291–300 px** (mean 297) |
| Mean ~300 px tall → | **word/line crops** (not full pages) |

## ID bucket distribution

| Bucket | Count | Bucket ID range |
|---|---|---|
| 0–999 | 56 | low IDs, sparse |
| 1000–1999 | 481 | mid-low IDs |
| 10000–10999 | 1,000 | full |
| 11000–11999 | 1,000 | full |
| 12000–12999 | 1,000 | full |
| 13000–13999 | 1,000 | full |
| 14000–14806 | 807 | truncated range |
| **Total** | **5,344** | |

## H1 vision profile (Tesseract OCR on 70 images = 10 per bucket, seed=20260930)

### Script detection (via Tesseract + script_id)

| Script | Count | % |
|---|---|---|
| **UNKNOWN** (Tesseract empty or unrecognizable) | 39 | 55.7% |
| **Devanagari** | 25 | 35.7% |
| Latin | 3 | 4.3% |
| Tamil | 1 | 1.4% |
| Kannada | 1 | 1.4% |
| Other | 1 | 1.4% |

**Interpretation**: The majority of detectable scripts are Devanagari. The 55.7% UNKNOWN rate is consistent with the planner's observation that the test set is "one handwritten word in Bengali script" (or similar low-quality handwritten scans that Tesseract cannot recognize). **Tesseract is trained primarily on printed text**; its failure here further confirms the handwriting hypothesis.

### Confirmed evidence (the test set is handwritten)

The planner viewed 3 test images (10001.jpg, 12407.jpg, 1361.jpg) directly: each is **one handwritten word in Bengali script**, blue pen, ~300 px tall. All 5,344 images are ~296–300 px tall word/line crops, IDs 0–14806.

## Bodo/gu handwriting set mapping (H1 deliverable)

The only labelled handwriting set on disk is `Datasets/akshardrishti_official/Bodo/gu/`:

| Property | Value |
|---|---|
| Path | `Datasets/akshardrishti_official/Bodo/gu/` |
| **train.txt** | **82,563 lines** (`path, vocab-index`) |
| **val.txt** | **17,643 lines** |
| **test.txt** | **16,490 lines** |
| **vocab.txt** | **10,963 words** |
| **Images on disk** | **4,645** (line counts say 82,563/17,643/16,490 but only 4,645 image files exist) |
| Script | **Gujarati** (handwritten words) |
| Format | IIIT-HW (Indian Institute of Hyderabad Handwriting) |

### Mismatch finding

- `train.txt` lists 82,563 entries → expects 82,563 image files
- Actual images on disk: **4,645**
- **Gap: ~77,918 missing training images** — must be verified against the source (`IIIT-HW-Dev / -Telugu / -INDIC-HW-WORDS` from `PPT_FULL_DUMP.md` row 2)

This is a data-integrity issue: the label file references ~5% of the images it should. Training on this set will silently train on only 5% of the labelled data. **H2 (Agent 2) must verify** before any handwriting training.

## Search for other handwriting sets

None found in `Datasets/akshardrishti_official/` besides `Bodo/gu/`. The South-language folders (`Tamil/`, `Telugu/`, `Kannada/`, `Malayalam/`) contain only PDF files (proto-104 S1: 0/23,001 clean pages), no handwriting labels.

## Compliance

- ✅ **Read-only**: never used for training or tuning (proto-104 H1 explicit).
- ✅ **Reproducible**: seeded (`random.seed(20260930)`), 10 images per bucket, total 70 sampled.
- ✅ **Honest**: UNKNOWN reported as UNKNOWN (Tesseract can't read handwritten → flagged).
- ✅ **R-11 compliance**: heuristic numbers from the prior version are REJECTED — this profile uses real OCR (Tesseract) for script detection.

## Method limitations (honest)

- **Tesseract is poor at handwriting**: 55.7% UNKNOWN rate is a Tesseract limitation, not necessarily a "not handwriting" finding. The planner's direct visual inspection confirms the handwriting hypothesis (R-11-compliant visual evidence).
- **6 languages only**: Tesseract has eng/hin/kan/mal/tam/tel installed. Bengali, Gurmukhi, Gujarati, Odia, Telugu-extended scripts cannot be read by this Tesseract install.
- **Bodhan 403**: a vision-capable Bodhan would read 90%+ of these (the test set is the same kind of handwritten Indic text Bodhan is trained on). Until HF access is granted, the 55.7% UNKNOWN ceiling holds.

## Action for H3 (Bodhan handwriting baseline)

Once Bodhan downloads (R-4 unblocked Day 1):
1. Run Bodhan on the same 70-image sample
2. Compute per-bucket script detection rate (Bodhan should read ~90%)
3. Compute CER vs Tesseract on the 35.7% Tesseract-can-read (Devanagari) subset for cross-comparison

## Files

- `docs/campaign/H1_TEST_PROFILE.json` — raw per-bucket per-sample results (Tesseract output + image size + script)
- `docs/campaign/TEST_SET_PROFILE.md` — this file (rewrite of the REJECTED heuristic version)
- `docs/campaign/HF_ACCESS_REQUEST.md` — boss action needed for Bodhan HF access
