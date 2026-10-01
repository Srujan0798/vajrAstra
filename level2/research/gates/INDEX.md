# Gates INDEX (H8 law — every gate verdict lives here)

## Retro-index (pre-existing loose gates, 2026-09-13)
| gate | verdict | evidence |
|---|---|---|
| rapidocr 20-page script-fidelity (v1 Chinese config) | WASH 400/400 zero Indic chars | research/gate_results_final.json + RAPIDOCR_VERDICT.md |
| rapidocr 3-page v5 multilang | OK te 78%/ta 87%/kn real | research/test_v5_multilang.py |
| rapidocr 4-page law (post-fix) | PASS te/ta/kn real-script, ml honest-empty | out/rapidocr 4 packs 13 Sep 04:03 |
| 300-dpi empty-page rescue probe (10 pages) | 0/10 recovered — truly blank/photo pages | research/300DPI_PROBE.md |
| surya grammar-400 | fixed via SURYA_GUIDED_LAYOUT=false | upstream issue #542 cited in COMMUNITY_FAILURE_MODES.md |
| timing probe (21 measurements, 7 engines) | DONE 13 Sep — tesseract-family 2× faster than heartbeat single-sample | TIMING_PROBE.jsonl |

## Open gates (scheduled)
| gate | question | status |
|---|---|---|
| G-B1 doctr PARSeq vs CRNN | B1: accuracy leader never tested | **DONE 13 Sep — NO CONTEST: both Latin-mojibake (0/4 pages, ratio 0.000); PARSeq shipped in 1.1.0 but zoo has NO Indic weights (French vocab); telugu-vocab probe = fake fidelity (ratio .53, Jaccard-5 0.00); detect_layout text-identical +5% ms. No rerun.** B1_doctr_parseq.md |
| G-B3 tesseract tessdata_best × PSM{1,3,6} | B3: LSTM best models never tested | **DONE 13 Sep — LOSS 0/12 configs (chars −0..−9%, ratio ±.03 noise, 1.4–1.7× slower; homebrew mal was ALREADY best by md5); PSM6 helps only te_001 (+17% chars); PSM1≡PSM3 elsewhere. No rerun.** B3_tessdata_best.md |
| G-B2 rapidocr server-rec | B2: server weights never tried | **DONE 14 Sep — NO-SERVER-INDIC: every `_rec_server` model in rapidocr 3.9.2 default_models.yaml is `ch_*` (Chinese); te/ta/ka ship mobile-only rec weights; nothing to test, mobile stays. Closed negative.** |
| G-B4 paddle server-det retest | B4: does full (server det) beat shipped post-timeout-fix? | **DONE 14 Sep — NO-GAIN: full mode byte-identical to shipped packs 4/4 (incl. te_053 historical-timeout page); timeouts were load-transients; 7–79s/page unloaded; light fallback stays. No rerun.** B4_paddle_server_det.md |
| G-B12 ensemble voting | does ≥3-family agreement beat single engine? | **DONE 13 Sep — NO: 0/115 pages beat all singles; agreement-text CER 0.897 vs best-single 0.628 (full union 3.92, worse than WORST single on 115/115 — segmentation-granularity mismatch). Consolation: agreement = precision instrument (5-gram prec 0.60 vs 0.36) but 34% coverage; 6/115 pages pseudo-GT-grade (prec≥.9∧rec≥.9). Sub-finding: 52/115 "clean" GT pages are legacy-font mojibake → C2 conflict. No deck claim of voting-as-GT.** B12_ensemble_voting.md |

## Gate-results register (new artifacts, 2026-09-13)
- B1: gates/{b1_doctr_parseq_gate.py, b1_parseq_telugu_vocab_gate.py, b1_results.json,
  b1_parseq_telugu_vocab.json, b1_quality_jac.json, B1_doctr_parseq.md}
- B3: gates/{b3_tessdata_best_gate.py, b3_results.json (24 runs), b3_quality_jac.json,
  B3_tessdata_best.md} · /tmp/tessdata_best weights deleted post-gate (kept docs only)
- B12: gates/{b12_ensemble.py, b12_results.json (115 pages, per-page + per-script),
  B12_ensemble_voting.md} · spawned C2 (mojibake-GT in clean list), Q-B12.1/.2/.3
- B4: gates/{b4_paddle_server_gate.py (standalone, .venv311), b4_results.json, B4_paddle_server_det.md} — spawned B4.1 (load-stress threshold for server det; parked LOW)
