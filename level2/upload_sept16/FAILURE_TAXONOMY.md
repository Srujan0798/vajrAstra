# Failure Taxonomy — per engine (disk-truth)

Labels: EMPTY (no text) | LOOP (8-gram redundancy >0.6) | GARBAGE (>30% noise chars) |
ENG_LEAK (Indic page, >90% ASCII words) | LINES_SHORT (<50% of PDF-layer lines
on dense pages, GT >= 10 lines — B16) | NFC_BAD (text_nfc not normalized) |
DUP (same text on many pages).

| engine | empty | loop | garbage | eng-leak | lines-short | nfc-bad | max-dup | p10/med/p90 chars |
|---|---|---|---|---|---|---|---|---|
| tesseract_indic | 31 | 0 | 0 | 2 | 15 | 0 | 2 | 111/1142/2379 |
| openbharatocr | 31 | 0 | 0 | 2 | 15 | 0 | 2 | 111/1142/2379 |
| easyocr | 9 | 0 | 0 | 3 | 156 | 0 | 2 | 89/1113/2293 |
| paddleocr_indic | 7 | 0 | 0 | 89 | 7 | 0 | 2 | 60/584/1946 |
| indicphotoocr | 10 | 0 | 0 | 2 | 52 | 0 | 2 | 78/1051/2039 |
| rapidocr | 100 | 0 | 1 | 27 | 12 | 0 | 2 | 50/787/2053 |
| tesseract_bilingual | 31 | 0 | 0 | 2 | 15 | 0 | 2 | 111/1140/2380 |
| doctr | 11 | 0 | 0 | 263 | 10 | 0 | 2 | 89/1035/2063 |
| surya | 11 | 0 | 0 | 5 | 139 | 0 | 2 | 98/1135/2371 |
| anuvaad_tesseract | 31 | 0 | 0 | 6 | 15 | 0 | 2 | 106/1132/2336 |
