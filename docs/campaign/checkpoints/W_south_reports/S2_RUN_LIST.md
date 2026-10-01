# S2 Run List (proto-104 rev 3, R-7)

**Date:** 2026-09-30
**Agent:** Agent 3 (Miss)
**Status:** DONE

## Summary
- Drew 400 South items from Sarvam Indic OCR Bench (ta/te/kn/ml × 100 each)
- Seed: 20260926 (same as v1 manifest build)
- Rendered pages into `level2/benchmark/pages/{ta,te,kn,ml}/` (400 PNG files)
- Updated `level2/benchmark/manifest_v2.json` with 1,683 items (1,283 v1 + 400 South)
- Source: Sarvam Indic OCR Bench (proto-104 R-7: South GT = Sarvam-bench fill)

## Run List (for DISPATCH_LOG)
Images drawn per language (100 each):
- ta: indic_ocr_bench_test_tam_105 through indic_ocr_bench_test_tam_204 (100 items)
- te: indic_ocr_bench_test_tel_10 through indic_ocr_bench_test_tel_109 (100 items)
- kn: indic_ocr_bench_test_kan_1 through indic_ocr_bench_test_kan_100 (100 items)
- ml: indic_ocr_bench_test_mal_1 through indic_ocr_bench_test_mal_100 (100 items)

All drawn from Sarvam Indic OCR Bench using seed 20260926, same draw pattern as existing 158 sarvam_fill items.

## Artifacts Created
- `level2/benchmark/pages/ta/*.png` (100 files)
- `level2/benchmark/pages/te/*.png` (100 files)
- `level2/benchmark/pages/kn/*.png` (100 files)
- `level2/benchmark/pages/ml/*.png` (100 files)
- `level2/benchmark/manifest_v2.json` (1,683 items: v1 1,283 + South 400)

## DISPATCH_LOG entry
$(date -u +%Y-%m-%dT%H:%M:%SZ) | Agent 3 (Miss) | S2 END | South items drawn (ta/te/kn/ml × 100 each from Sarvam bench, seed 20260926). manifest_v2.json = 1,683 items. Pages rendered to level2/benchmark/pages/.

