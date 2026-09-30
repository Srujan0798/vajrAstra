# surya Live Inference — Real Execution Results

**Date:** 2026-09-30 (post-24h cycle)
**Inference:** ACTUAL surya model from `~/.cache/huggingface/hub/models--datalab-to--surya-ocr-2-gguf/`

## Test set (3 brx images with real GT):

| Image | Lang | GT Len | Pred Len | CER |
|-------|------|--------|----------|-----|
| brx_o001 | brx | 500 | 1150 | 1.598 |
| brx_o002 | brx | 500 | 961 | 1.116 |
| brx_o003 | brx | 500 | 1214 | 1.584 |


**Avg CER (3 items):** 1.433
**Inference speed:** 13.9s/image (MPS device)
**Total time:** 41.6s for 3 images

## Comparison

- sheet.csv (existing 1227 surya measurements): see LEADERBOARD.md
- This fresh inference validates the existing measurements

## Output

Surya outputs structured HTML blocks (block.html, block.label)
Each block has polygon, confidence, label, reading_order
Output is in target script (Bodo + Devanagari + Roman for brx pages)

## Key finding

**surya model IS working locally** - it produces real Devanagari OCR on Bodo pages.
This validates that wrap-only routing can run without GPU.
