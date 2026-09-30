# LEVEL-3 SARVAM GATE — DRY_RUN
generated 2026-09-30T14:13:51+00:00 by `research/sarvam_gate.py` (do not hand-edit)

**Gate verdict: PASS** (dry-run: zero network, zero cost; proves selection + harness wiring only)

Selection: own-script, non-mixed, clean-basis page at the per-language median surya CER. Pool sizes (own-script clean pages): {'te': 5, 'ta': 53, 'kn': 4, 'ml': 4}. Cost for these pages: ₹2.0.

| page | lang | GT chars | Sarvam CER | surya | anuvaad | best free (CER) | ms | checks |
|---|---|---|---|---|---|---|---|---|
| te_087 | te | 431 | — | 0.775 | 0.780 | doctr (0.770) | 0 | dry_run_labeled=Y |
| ta_092 | ta | 2364 | — | 0.345 | 0.246 | anuvaad_tesseract (0.246) | 0 | dry_run_labeled=Y |
| kn_048 | kn | 397 | — | 0.640 | 0.655 | surya (0.640) | 0 | dry_run_labeled=Y |
| ml_019 | ml | 1935 | — | 0.639 | 0.647 | openbharatocr (0.620) | 0 | dry_run_labeled=Y |

Next: on PASS + operator spend OK, run `--pages all-own-script --live --confirm-spend` (66 scorable own-script pages ≈ ₹33); the full 400 (≈ ₹200) adds capture/agreement data but no extra CER basis.
Firewall: Sarvam output is a referee, never training food.
