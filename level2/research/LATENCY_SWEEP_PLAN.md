# LATENCY SWEEP PLAN (RED, law §14.3)
generated 2026-09-30T14:16:35+00:00 by `research/latency_plan.py` from models/<engine>/metrics.json (do not hand-edit)

| engine | family | sealed median ms/page | pages/hour (1 worker) | 400-page wall-clock h | status |
|---|---|---|---|---|---|
| tesseract_indic | tesseract_family | 3,455 | 1,042 | 0.4 | measured |
| openbharatocr | tesseract_family | 3,302 | 1,090 | 0.4 | measured |
| easyocr | easyocr | 30,726 | 117 | 3.4 | measured |
| paddleocr_indic | paddleocr_indic | 95,182 | 38 | 10.6 | measured |
| indicphotoocr | indicphotoocr | 15,700 | 229 | 1.7 | measured |
| rapidocr | rapidocr | 444 | 8,108 | 0.0 | measured |
| tesseract_bilingual | tesseract_family | 2,978 | 1,209 | 0.3 | measured |
| doctr | doctr | 3,138 | 1,147 | 0.3 | measured |
| surya | surya | 16,329 | 220 | 1.8 | measured |
| anuvaad_tesseract | tesseract_family | 3,674 | 980 | 0.4 | measured |
| sarvam_api (L3) | paid | ≥23,000 (throttle floor) | ≤157 | ≥2.6 | ₹0.5/page, 10 req/min — measure at gate |

Sum of measured engines, sequential single worker: **19.4 h** for 400 pages.

## Protocol (run on the full tree; one engine at a time, machine otherwise idle)
1. Same 4-page gate pages first (te_087, ta_092, kn_048, ml_019) × 3 repeats; drop the first (model load).
2. Record per page: wall ms, CPU model, threads, RAM peak → append to HEARTBEAT.jsonl (existing telemetry).
3. Full sweep only for engines marked NO TIMING or whose sealed median rests on <20 timed pages.
4. Report p50/p90 ms/page and ₹/page (CPU-hour cost stated as an explicit assumption) next to Sarvam's ₹0.5/page.
5. Quote latency only with machine spec; never mix timings from different machines in one table.
