# GT EXPANSION QUEUE — human verification worklist
generated 2026-09-30T14:22:04+00:00 by `research/gt_expansion_queue.py` (do not hand-edit)

Scored own-script pages today (clean_v2): {'te': 5, 'ta': 53, 'ml': 4, 'kn': 7}. Target n≥20 per script to allow any per-script claim → need {'te': 15, 'ta': 0, 'kn': 13, 'ml': 16}.

| class | pages | by lang | route |
|---|---|---|---|
| scan_only | 200 | {'kn': 56, 'ml': 78, 'ta': 23, 'te': 43} | lane A: human verifies engine draft |
| legacy_font | 76 | {'kn': 30, 'ml': 4, 'ta': 8, 'te': 34} | lane B: identify font (pymupdf font names), verified font-map conversion, 4-page gate vs human text; human fallback |
| contentless | 24 | {'kn': 2, 'ml': 13, 'ta': 2, 'te': 7} | dropped (no family ≥50 chars; 300-dpi probe 0/10) |

## Batch 1 — closes the n≥20 gap (effort at 100 chars/min, an assumption)

### ml — 16 pages, ≈4.0 h — reviewer: native reviewer — NOT NAMED (H-2)
| page | class | draft engine | draft chars | families agreeing (τ≤0.2) | est. min |
|---|---|---|---|---|---|
| ml_049 | scan_only | surya | 1690 | 3 | 16.9 |
| ml_067 | scan_only | surya | 1289 | 3 | 12.9 |
| ml_083 | legacy_font | surya | 1685 | 3 | 16.9 |
| ml_029 | scan_only | surya | 1623 | 3 | 16.2 |
| ml_100 | legacy_font | surya | 1885 | 3 | 18.9 |
| ml_030 | scan_only | surya | 1685 | 3 | 16.9 |
| ml_048 | scan_only | tesseract_indic | 2053 | 3 | 20.5 |
| ml_050 | scan_only | surya | 676 | 3 | 6.8 |
| ml_047 | legacy_font | surya | 2533 | 3 | 25.3 |
| ml_099 | scan_only | surya | 1302 | 3 | 13.0 |
| ml_081 | scan_only | surya | 1126 | 3 | 11.3 |
| ml_082 | scan_only | surya | 1354 | 3 | 13.5 |
| ml_003 | scan_only | surya | 897 | 2 | 9.0 |
| ml_002 | scan_only | surya | 1210 | 2 | 12.1 |
| ml_028 | legacy_font | surya | 1713 | 2 | 17.1 |
| ml_058 | scan_only | surya | 1392 | 2 | 13.9 |

### te — 15 pages, ≈2.8 h — reviewer: Srujan (can gold-check Telugu, SOUTH_CANON §D)
| page | class | draft engine | draft chars | families agreeing (τ≤0.2) | est. min |
|---|---|---|---|---|---|
| te_003 | legacy_font | surya | 646 | 5 | 6.5 |
| te_079 | legacy_font | surya | 1412 | 5 | 14.1 |
| te_088 | legacy_font | paddleocr_indic | 770 | 5 | 7.7 |
| te_047 | legacy_font | tesseract_indic | 849 | 5 | 8.5 |
| te_054 | legacy_font | surya | 837 | 4 | 8.4 |
| te_053 | legacy_font | surya | 1816 | 4 | 18.2 |
| te_062 | legacy_font | surya | 1994 | 4 | 19.9 |
| te_034 | legacy_font | surya | 1153 | 4 | 11.5 |
| te_092 | scan_only | surya | 1174 | 4 | 11.7 |
| te_002 | scan_only | surya | 1311 | 4 | 13.1 |
| te_004 | legacy_font | paddleocr_indic | 816 | 4 | 8.2 |
| te_091 | scan_only | paddleocr_indic | 989 | 4 | 9.9 |
| te_027 | legacy_font | easyocr | 302 | 3 | 3.0 |
| te_059 | legacy_font | paddleocr_indic | 1629 | 3 | 16.3 |
| te_084 | legacy_font | tesseract_indic | 1366 | 3 | 13.7 |

### kn — 13 pages, ≈3.2 h — reviewer: native reviewer — NOT NAMED (H-2)
| page | class | draft engine | draft chars | families agreeing (τ≤0.2) | est. min |
|---|---|---|---|---|---|
| kn_038 | legacy_font | surya | 1940 | 3 | 19.4 |
| kn_050 | scan_only | surya | 2326 | 3 | 23.3 |
| kn_076 | scan_only | surya | 1532 | 3 | 15.3 |
| kn_063 | scan_only | surya | 897 | 3 | 9.0 |
| kn_006 | scan_only | surya | 1602 | 3 | 16.0 |
| kn_007 | scan_only | surya | 621 | 3 | 6.2 |
| kn_046 | scan_only | tesseract_indic | 811 | 3 | 8.1 |
| kn_047 | scan_only | surya | 1699 | 3 | 17.0 |
| kn_027 | legacy_font | surya | 1728 | 3 | 17.3 |
| kn_072 | legacy_font | surya | 1509 | 3 | 15.1 |
| kn_098 | legacy_font | surya | 2460 | 3 | 24.6 |
| kn_062 | legacy_font | surya | 983 | 3 | 9.8 |
| kn_097 | legacy_font | surya | 925 | 3 | 9.2 |

Shortfall after batch 1: none — batch 1 alone brings every South script to n≥20.

## Rules
- The draft is a review aid. The reviewer types/corrects the verified text; nothing is pre-accepted.
- Verified pages become a NEW tier-stamped GT file (reviewer, date, tier). L1-frozen labels are never edited.
- Bench firewall: verified pages are referee data, never training food.
- Full ranked list (all classes) in GT_EXPANSION_QUEUE.json.
