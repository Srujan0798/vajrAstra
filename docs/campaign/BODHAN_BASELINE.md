# BODHAN_BASELINE.md

## Variants on Disk

| Variant | Safetensors | Size | Licence | Status |
|---|---|---|---|---|
| indic-ocr | 2 | 1868 MB | Apache-2.0 | on disk |
| indic-ocr-bench | 0 | 0 MB | Apache-2.0 | on disk |
| indic-ocr-mlx-4bit | 2 | 767 MB | Apache-2.0 | on disk |
| indic-ocr-mlx-8bit | 0 | 0 MB | Apache-2.0 | on disk |
| indic-ocr-mlx-bf16 | 2 | 1868 MB | Apache-2.0 | on disk |

## Gate 1 numbers (from DISPATCH_LOG.md §36)

| Run | n | 4-bit CER | bf16 CER | Notes |
|---|---|---|---|---|
| sample-100 (same 99) | 99 | 0.6878 | 0.6863 | delta 0.0015 — B-01 PASS |
| pair-only (300 gold) | 300 | 0.4034 | 0.4010 | beats surya 0.5660 |
| bench small_rep | 1173 | 0.0540 (WER 0.1356) | — | official metrics.py; 0.52 s/crop |
| official-path | 99 | — | — | vendor assert; parity waits GPU day |

**Gate 1: CONDITIONAL PASS.**

## Next-steps
- Agent 2 S5 — **DONE** (see  §S5)
- Agent 1: retrieve the 12 existing completed Sarvam results only — honest-empty if the endpoint refuses
- Leftover-lang engines wait R-16
- **A7 closed**
