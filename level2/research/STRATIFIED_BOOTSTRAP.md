# STRATIFIED BOOTSTRAP — RED verdict on the sealed ranking
generated 2026-09-30T14:22:08+00:00 by `research/stratified_bootstrap.py` (seed 20260930, 2000 paired draws; do not hand-edit)

## 1. Reproduction check (simple page bootstrap, sealed basis)
n=126. Sealed deck line: surya−anuvaad Δ −0.045, CI [−0.086, +0.020], TIED.

| pair | Δ median CER | 95% CI | P(A better) | verdict |
|---|---|---|---|---|
| surya - anuvaad_tesseract | -0.045 | [-0.086, +0.018] | 0.92 | **TIED** |
| anuvaad_tesseract - indicphotoocr | -0.180 | [-0.272, -0.118] | 1.0 | **A better** |
| surya - indicphotoocr | -0.225 | [-0.294, -0.158] | 1.0 | **A better** |
| surya - tesseract_indic | -0.063 | [-0.123, -0.008] | 0.986 | **A better** |
| anuvaad_tesseract - tesseract_indic | -0.018 | [-0.052, -0.002] | 0.985 | **A better** |

## 2. Stratified (dominant_script × GT-density tercile, 15 strata), sealed basis n=126

| pair | Δ median CER | 95% CI | P(A better) | verdict |
|---|---|---|---|---|
| surya - anuvaad_tesseract | -0.045 | [-0.084, +0.011] | 0.945 | **TIED** |
| anuvaad_tesseract - indicphotoocr | -0.180 | [-0.257, -0.130] | 1.0 | **A better** |
| surya - indicphotoocr | -0.225 | [-0.282, -0.169] | 1.0 | **A better** |
| surya - tesseract_indic | -0.063 | [-0.121, -0.015] | 0.992 | **A better** |
| anuvaad_tesseract - tesseract_indic | -0.018 | [-0.051, -0.003] | 0.987 | **A better** |

## 3. South own-script only (te/ta/kn/ml pages in their own script, non-mixed), n=66
This is the ranking the South track actually claims; the sealed basis is ~48% Latin/Devanagari mixed-book pages.

| rank | engine | median CER | 95% CI |
|---|---|---|---|
| 1 | surya | 0.358 | [0.222, 0.409] |
| 2 | anuvaad_tesseract | 0.358 | [0.271, 0.447] |
| 3 | openbharatocr | 0.389 | [0.275, 0.489] |
| 4 | tesseract_bilingual | 0.389 | [0.275, 0.488] |
| 5 | tesseract_indic | 0.389 | [0.275, 0.489] |
| 6 | paddleocr_indic | 0.565 | [0.463, 0.658] |
| 7 | rapidocr | 0.582 | [0.503, 0.678] |
| 8 | indicphotoocr | 0.635 | [0.527, 0.673] |
| 9 | doctr | 0.907 | [0.877, 0.917] |
| 10 | easyocr | 0.954 | [0.933, 0.962] |

| pair | Δ median CER | 95% CI | P(A better) | verdict |
|---|---|---|---|---|
| surya - anuvaad_tesseract | -0.000 | [-0.112, +0.055] | 0.622 | **TIED** |
| anuvaad_tesseract - indicphotoocr | -0.277 | [-0.354, -0.160] | 1.0 | **A better** |
| surya - indicphotoocr | -0.277 | [-0.411, -0.170] | 1.0 | **A better** |
| surya - tesseract_indic | -0.032 | [-0.141, +0.079] | 0.819 | **TIED** |
| anuvaad_tesseract - tesseract_indic | -0.031 | [-0.051, +0.055] | 0.806 | **TIED** |

## 4. CORRECTED basis clean_v2 (n=100): sealed basis minus 26 legacy-font pages the tag-based gate missed
Excluded (PDF layer <15% Indic while >=4 of 7 independent families read Indic): kn_027, kn_061, kn_062, kn_064, kn_065, kn_068, kn_071, kn_072, kn_077, kn_078, kn_097, kn_099, kn_100, ta_073, ta_080, ta_082, te_062, te_073, te_074, te_078, te_079, te_082, te_083, te_084, te_088, te_099
Strata = script the engines actually read × GT-density tercile.

| rank | engine | median CER | 95% CI |
|---|---|---|---|
| 1 | surya | 0.347 | [0.246, 0.408] |
| 2 | anuvaad_tesseract | 0.351 | [0.291, 0.447] |
| 3 | openbharatocr | 0.376 | [0.277, 0.484] |
| 4 | tesseract_bilingual | 0.376 | [0.276, 0.484] |
| 5 | tesseract_indic | 0.376 | [0.277, 0.484] |
| 6 | indicphotoocr | 0.567 | [0.516, 0.625] |
| 7 | rapidocr | 0.633 | [0.572, 0.696] |
| 8 | paddleocr_indic | 0.635 | [0.569, 0.684] |
| 9 | doctr | 0.850 | [0.830, 0.866] |
| 10 | easyocr | 0.898 | [0.866, 0.924] |

| pair | Δ median CER | 95% CI | P(A better) | verdict |
|---|---|---|---|---|
| surya - anuvaad_tesseract | -0.004 | [-0.073, +0.042] | 0.667 | **TIED** |
| anuvaad_tesseract - indicphotoocr | -0.215 | [-0.282, -0.123] | 1.0 | **A better** |
| surya - indicphotoocr | -0.220 | [-0.306, -0.156] | 1.0 | **A better** |
| surya - tesseract_indic | -0.029 | [-0.100, +0.051] | 0.815 | **TIED** |
| anuvaad_tesseract - tesseract_indic | -0.024 | [-0.050, +0.030] | 0.818 | **TIED** |

## 5. Per observed script on clean_v2 (simple bootstrap within script)

| observed script | n | leader | leader CER | runner-up | runner-up CER | surya−anuvaad verdict | small-n |
|---|---|---|---|---|---|---|---|
| Tamil | 53 | anuvaad_tesseract | 0.301 | surya | 0.345 | TIED |  |
| Devanagari | 16 | surya | 0.222 | anuvaad_tesseract | 0.252 | — (n<20) | YES — no deck claim |
| Latin | 15 | anuvaad_tesseract | 0.379 | rapidocr | 0.391 | — (n<20) | YES — no deck claim |
| Kannada | 7 | surya | 0.641 | anuvaad_tesseract | 0.656 | — (n<20) | YES — no deck claim |
| Telugu | 5 | paddleocr_indic | 0.775 | surya | 0.775 | — (n<20) | YES — no deck claim |
| Malayalam | 4 | openbharatocr | 0.625 | tesseract_bilingual | 0.625 | — (n<20) | YES — no deck claim |

Rule: a script with n < 20 carries no ranking claim in any deck/WhatsApp line; quote it only with its n.
