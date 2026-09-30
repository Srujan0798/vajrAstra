# METRIC ROBUSTNESS — char-CER vs order-invariant bag-of-words error
generated 2026-09-30T14:22:28+00:00 by `research/metric_robustness.py` on clean_v2 (n=100); do not hand-edit

| engine | CER (sealed, order-sensitive) | rank | char-3gram error (order+segmentation-invariant) | rank | BoW word error (order-invariant) | rank |
|---|---|---|---|---|---|---|
| surya | 0.347 | 1 | 0.155 | 1 | 0.402 | 1 |
| anuvaad_tesseract | 0.351 | 2 | 0.211 | 2 | 0.455 | 2 |
| paddleocr_indic | 0.635 | 8 | 0.244 | 3 | 0.552 | 4 |
| rapidocr | 0.633 | 7 | 0.252 | 4 | 0.527 | 3 |
| tesseract_bilingual | 0.376 | 4 | 0.288 | 5 | 0.662 | 7 |
| openbharatocr | 0.376 | 3 | 0.288 | 6 | 0.662 | 6 |
| tesseract_indic | 0.376 | 5 | 0.288 | 7 | 0.662 | 8 |
| indicphotoocr | 0.567 | 6 | 0.358 | 8 | 0.650 | 5 |
| easyocr | 0.898 | 10 | 0.891 | 9 | 0.861 | 9 |
| doctr | 0.850 | 9 | 0.933 | 10 | 0.884 | 10 |

PDF-layer extraction artifact: 43/100 GT pages contain a doubled dependent vowel sign (e.g. ாா); surya output has it on 0, anuvaad on 4. Those characters are charged to the engine by CER.

## Pseudo-GT re-tested with the order-invariant metric

| τ (CER agreement) | pages | pseudo-GT char-3gram error vs real GT | best single engine on same pages | pseudo-GT BoW error |
|---|---|---|---|---|
| 0.1 | 37 | 0.1439 | 0.1323 | 0.3004 |
| 0.2 | 72 | 0.1777 | 0.1447 | 0.4418 |
| 0.3 | 92 | 0.1826 | 0.1439 | 0.4446 |
| 0.4 | 97 | 0.1879 | 0.146 | 0.4571 |

## Verdict inputs for Srujan / David
- Compare CER rank with char-3gram rank: engines that rise under the order-invariant measure are being charged by CER for reading order, not recognition.
- Line-matched CER was tried and discarded: block-mode engines (surya) emit paragraphs as single lines, so line pairing fails (same trap as G-B12).
- Deck CER numbers stay as sealed (one-writer law) until an H-decision adopts an order-invariant metric; proposed: add flexible character accuracy (reading-order-independent CER) as a second column in the writer.
