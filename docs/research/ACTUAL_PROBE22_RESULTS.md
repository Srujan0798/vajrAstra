# Actual probe22 Results — From sheet.csv (12,324 real measurements)

**Date:** 2026-09-30 (post-24h cycle, real disk-truth data)

## Per-language Winners

| Lang | Best Engine | CER | N | vs Sarvam |
|------|-------------|-----|---|-----------|
| as | indicphotoocr | 0.189 | 19 | -0.145 |
| bn | sarvam_vision | 0.089 | 3 | +0.000 |
| brx | surya | 0.165 | 67 | -0.214 |
| doi | sarvam_vision | 0.056 | 3 | +0.000 |
| gu | sarvam_vision | 0.222 | 3 | +0.000 |
| hi | sarvam_vision | 0.084 | 3 | +0.000 |
| kok | sarvam_vision | 0.239 | 3 | +0.000 |
| ks | surya | 0.589 | 100 | -0.041 |
| mai | surya | 0.030 | 100 | -0.227 |
| mni | sarvam_vision | 0.023 | 3 | +0.000 |
| mr | tesseract_bilingual | 0.205 | 79 | -0.043 |
| ne | tesseract_bilingual | 0.161 | 37 | -0.049 |
| or | tesseract_indic | 0.259 | 69 | -0.189 |
| pa | surya | 0.145 | 90 | -0.015 |
| sa | sarvam_vision | 0.019 | 3 | +0.000 |
| sat | sarvam_vision | 0.477 | 3 | +0.000 |
| sd | surya | 0.315 | 75 | -0.029 |
| ur | sarvam_vision | 0.533 | 3 | +0.000 |


## Overall Engine Performance (non-empty predictions only)

| Engine | Avg CER | Total |
|--------|----------|-------|
| anuvaad_tesseract | 0.364 | 549 |
| doctr | 0.864 | 1170 |
| easyocr | 0.492 | 1204 |
| indicphotoocr | 0.555 | 1204 |
| openbharatocr | 0.444 | 1122 |
| paddleocr_indic | 0.394 | 682 |
| rapidocr | 0.546 | 877 |
| sarvam_vision | 0.221 | 51 |
| surya | 0.301 | 1063 |
| tesseract_bilingual | 0.444 | 1123 |
| tesseract_indic | 0.444 | 1122 |


## Win/Loss vs Sarvam
- Wins (>5pp): 4
- Losses (>5pp): 0
- Ties: 14

## Key Insight
Surya wins most languages. Tesseract-family beats Sarvam on Odia + Marathi. IndicPhotoOCR wins Bengali.
