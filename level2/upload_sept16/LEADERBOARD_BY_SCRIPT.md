# Leaderboard by script

Pages are grouped by the script that dominates each page (per-language tables would mix scripts — e.g. 'te' pages are 47 Telugu + 42 Latin + 11 Devanagari).
Capture ratio is measured vs the PDF text layer (pages with a >=200-char layer only).

## Latin — 124 pages (capture computed on 43 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| tesseract_indic | 124 | 17 | 9 | 998 | 0.856 |
| openbharatocr | 124 | 17 | 9 | 998 | 0.856 |
| tesseract_bilingual | 124 | 17 | 9 | 998 | 0.855 |
| surya | 124 | 4 | 11 | 980 | 0.892 |
| anuvaad_tesseract | 124 | 17 | 9 | 979 | 0.846 |
| easyocr | 124 | 3 | 9 | 930 | 0.939 |
| indicphotoocr | 124 | 3 | 4 | 801 | 0.886 |
| doctr | 124 | 5 | 6 | 774 | 0.853 |
| rapidocr | 124 | 23 | 8 | 676 | 0.699 |
| paddleocr_indic | 124 | 2 | 8 | 551 | 0.758 |

winner by median chars: **tesseract_indic** (998 chars)

## Telugu — 60 pages (capture computed on 29 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| surya | 60 | 0 | 1 | 1137 | 1.267 |
| anuvaad_tesseract | 60 | 4 | 3 | 1094 | 1.241 |
| tesseract_indic | 60 | 4 | 3 | 1093 | 1.262 |
| openbharatocr | 60 | 4 | 3 | 1093 | 1.262 |
| tesseract_bilingual | 60 | 4 | 3 | 1093 | 1.267 |
| easyocr | 60 | 0 | 1 | 992 | 1.234 |
| paddleocr_indic | 60 | 0 | 1 | 965 | 1.255 |
| indicphotoocr | 60 | 0 | 1 | 953 | 1.088 |
| doctr | 60 | 0 | 1 | 897 | 1.035 |
| rapidocr | 60 | 0 | 3 | 800 | 1.053 |

winner by median chars: **surya** (1137 chars)

## Tamil — 67 pages (capture computed on 53 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| easyocr | 67 | 0 | 2 | 1579 | 1.1 |
| doctr | 67 | 0 | 2 | 1501 | 0.998 |
| tesseract_indic | 67 | 1 | 2 | 1481 | 0.991 |
| openbharatocr | 67 | 1 | 2 | 1481 | 0.991 |
| tesseract_bilingual | 67 | 1 | 2 | 1481 | 0.989 |
| surya | 67 | 0 | 2 | 1463 | 0.953 |
| paddleocr_indic | 67 | 0 | 1 | 1428 | 0.942 |
| rapidocr | 67 | 0 | 2 | 1425 | 0.925 |
| anuvaad_tesseract | 67 | 1 | 2 | 1408 | 0.952 |
| indicphotoocr | 67 | 0 | 2 | 1352 | 0.906 |

winner by median chars: **easyocr** (1579 chars)

## Kannada — 42 pages (capture computed on 19 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| easyocr | 42 | 0 | 0 | 1381 | 1.156 |
| surya | 42 | 0 | 0 | 1361 | 1.164 |
| tesseract_indic | 42 | 0 | 0 | 1236 | 1.174 |
| openbharatocr | 42 | 0 | 0 | 1236 | 1.174 |
| tesseract_bilingual | 42 | 0 | 0 | 1236 | 1.143 |
| anuvaad_tesseract | 42 | 0 | 0 | 1224 | 1.134 |
| indicphotoocr | 42 | 0 | 0 | 1130 | 0.945 |
| doctr | 42 | 0 | 0 | 1130 | 0.976 |
| paddleocr_indic | 42 | 0 | 0 | 913 | 0.874 |
| rapidocr | 42 | 0 | 2 | 902 | 0.824 |

winner by median chars: **easyocr** (1381 chars)

## Malayalam — 77 pages (capture computed on 9 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| surya | 77 | 7 | 2 | 1280 | 0.456 |
| easyocr | 77 | 6 | 4 | 1253 | 0.46 |
| doctr | 77 | 6 | 4 | 1207 | 0.461 |
| tesseract_bilingual | 77 | 8 | 0 | 1186 | 0.481 |
| tesseract_indic | 77 | 8 | 0 | 1184 | 0.481 |
| openbharatocr | 77 | 8 | 0 | 1184 | 0.481 |
| indicphotoocr | 77 | 7 | 2 | 1174 | 0.43 |
| anuvaad_tesseract | 77 | 8 | 0 | 1138 | 0.455 |
| paddleocr_indic | 77 | 5 | 5 | 191 | 0.119 |
| rapidocr | 77 | 77 | 0 | 0 | — |

winner by median chars: **surya** (1280 chars)

## Devanagari — 30 pages (capture computed on 24 pages with >=200-char PDF text layer)

| engine | packs | empty | thin(<30c) | median chars | median capture |
|---|---|---|---|---|---|
| surya | 30 | 0 | 4 | 895 | 0.973 |
| easyocr | 30 | 0 | 0 | 863 | 0.962 |
| doctr | 30 | 0 | 1 | 838 | 0.862 |
| indicphotoocr | 30 | 0 | 0 | 806 | 0.902 |
| tesseract_indic | 30 | 1 | 1 | 754 | 0.926 |
| openbharatocr | 30 | 1 | 1 | 754 | 0.926 |
| tesseract_bilingual | 30 | 1 | 1 | 753 | 0.93 |
| anuvaad_tesseract | 30 | 1 | 1 | 748 | 0.953 |
| paddleocr_indic | 30 | 0 | 1 | 441 | 0.383 |
| rapidocr | 30 | 0 | 2 | 237 | 0.179 |

winner by median chars: **surya** (895 chars)

