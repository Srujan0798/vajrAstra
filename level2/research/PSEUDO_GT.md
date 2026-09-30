# PSEUDO-GT TEST — does engine agreement give usable ground truth?
generated 2026-09-30T14:22:10+00:00 by `research/pseudo_gt.py` (do not hand-edit)

Validated on the 100 clean_v2 pages that HAVE trustworthy PDF-layer GT. Pseudo-GT = medoid output of 7 independent families, required support k=3 families within distance τ. Circularity guard: every engine is scored against a pseudo-GT built WITHOUT its own family.

| τ | pages qualifying (coverage) | pseudo-GT CER vs real GT (median / p90) | engine-rank Spearman vs real GT | top-3 by pseudo | top-3 by real GT | extra pages among no-GT pages (te/ta/kn/ml) |
|---|---|---|---|---|---|---|
| 0.1 | 37 (37%) | 0.3673 / 0.6275 | 0.539 | paddleocr_indic, surya, anuvaad_tesseract | surya, anuvaad_tesseract, tesseract_bilingual | 26 (11/13/2/0) |
| 0.2 | 72 (72%) | 0.4078 / 0.728 | 0.43 | paddleocr_indic, surya, anuvaad_tesseract | surya, openbharatocr, tesseract_bilingual | 86 (30/25/18/13) |
| 0.3 | 92 (92%) | 0.4439 / 0.731 | 0.115 | paddleocr_indic, surya, rapidocr | openbharatocr, tesseract_bilingual, tesseract_indic | 144 (45/27/36/36) |
| 0.4 | 97 (97%) | 0.4582 / 0.731 | 0.418 | paddleocr_indic, surya, rapidocr | surya, anuvaad_tesseract, openbharatocr | 193 (58/29/61/45) |

## Reading this table
- A pseudo-GT is only as good as its CER vs real GT: a median of 0.2 means the 'reference' itself is ~20% wrong, so it cannot separate engines whose real CERs differ by less than that (tier-1 differs by ~0.03).
- Spearman vs real GT tells whether pseudo-GT would reproduce the true engine order; top-3 tells whether it finds the right leaders.
- Rule (L7): pseudo-GT pages are labeled PSEUDO, never gold, never merged into CER_STAGE3B, and never used to rank an engine whose family contributed to them. Useful role: coarse tiering and triage, not tier-1 ranking.
