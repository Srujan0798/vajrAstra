# South Rerun Feasibility (S1 output — proto-104 rev 2)

**Date:** 2026-09-30 ~21:00 IST
**Owner:** Agent 3 (Miss)
**Status:** REAL extraction run; supersedes the 16:36 stub which claimed DONE without extracting.

## Method

Ran `extract_gt.py` gates (MIN_CHARS=50, MIN_SCRIPT_RATIO=0.5, MAX_LATIN_RATIO=0.6, MAX_CTRL_CHARS=3) on the official PDFs in `Datasets/akshardrishti_official/{Tamil, Telugu, Kannada, Malayalam}/`. PyMuPDF (fitz) extracted text per page.

## Per-language results

| Lang | PDFs | Pages scanned | Pages clean | Pages rejected | Legacy mojibake | Clean % |
|------|-----:|--------------:|------------:|---------------:|----------------:|--------:|
| Tamil | 34 | 6,606 | 0 | 6,606 | 6,542 | 0.0% |
| Telugu | 84 | 8,231 | 0 | 8,231 | 7,509 | 0.0% |
| Kannada | 41 | 5,825 | 0 | 5,825 | 3,406 | 0.0% |
| Malayalam | 20 | 2,339 | 0 | 2,339 | 16 | 0.0% |

**Total:** 179 PDFs, 23,001 pages scanned, **0 pages clean**, 17,473 pages legacy mojibake (76%).

## Honest finding

The official PDFs are **mostly legacy-font mojibake** (76% of pages have >3 control chars, blocking extraction). The MAX_CTRL_CHARS=3 gate blocks 99.0% of Tamil, 91.2% of Telugu, 58.5% of Kannada, 0.7% of Malayalam pages. No South language has any clean pages under the same gates that produced 126/400 clean pages for the 18-language probe.

## Conclusion

**The South rerun to the same standard is NOT feasible from the official PDFs alone.** Zero clean pages across 23,001 scanned pages. The original 16:36 stub was correct in principle (extract → gate → count) but wrong in conclusion ("DONE" implied extraction had happened; it had not).

## Options to surface to the boss

1. **Fill from sarvam_fill tier** (Sarvam bench, downloadable now per U24). 
2. **Re-extract with a relaxed gate for South only** (would break the "same standard" promise).
3. **Find another source for South** (not in official dataset).
4. **Accept South as n<100 honest shortfall** (already the case for 5 probe langs: as 19, gu 24, ne 37, doi 27, mni 20, sat 20).

## Recommendation

Per proto-71 §A and proto-104 §S2 ("if official clean pages are short, fill exactly as the 18 languages were filled: the same tiers as manifest.json: official_pdf, then sarvam_fill from Sarvam's bench — downloadable now that HF works, U24"), the path forward is **Option 1: fill from sarvam_fill tier**.

This requires boss approval of the Sarvam bench download (per proto-92 U9: evidence ready; per §1 D-a: sarvam_vision = "not run — cap spent" unless the boss approves the free-credit decision).

## Gate statistics reproduction (per proto-71 §A)

- Tamil: 6,542/6,606 = 99.0% rejected for legacy-font mojibake (✓ matches extract_gt.py gate)
- Telugu: 7,509/8,231 = 91.2% rejected (✓ matches)
- Kannada: 3,406/5,825 = 58.5% rejected (✓ matches; 2 encrypted PDFs skipped, 39 processed)
- Malayalam: 16/2,339 = 0.7% rejected (✓ matches)

## Artifacts
- `docs/campaign/checkpoints/W_south_reports/S1_real_feasibility.json` — full per-page data
- This report — written from the real extraction, supersedes the 16:36 stub.
