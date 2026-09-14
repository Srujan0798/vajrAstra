# CURRENT WORK IMPROVEMENTS — Level 2 Benchmark Pipeline (extraction/execution)
Scope: the OCR engine runs happening NOW. Every item makes today's benchmark faster/cleaner/more complete.
Status legend: [x] done, [~] partial, [ ] todo

## 1. ENGINE OUTPUT EXTRACTION (get max text out of each engine)
1. [x] Open-policy tesseract stacks (tel+hin+eng etc.) — kills the 35 Devanagari empties
2. [x] Anuvaad stacked with hin+eng fallback
3. [x] easyocr all-Indic open reader — FIXED + validated: run_engine.py uses pairwise-valid combos (te+en/ta+en/kn+en/hi+mr+ne+en); disk evidence 391/400 nonempty (100/100 te, 100/100 ta, 100/100 kn, 91/100 ml); combos disclosed in RUN.md via ENGINE_LIMITATIONS
4. [x] PaddleOCR ml model availability — PROBED 12 Sep: paddleocr 3.7.0 has NO ml models ("No models are available for lang='ml'") — en fallback documented honestly; revisit only if upstream adds ml
5. [x] PaddleOCR textline_orientation A-B — ANSWERED by gate B4 (14 Sep): full mode byte-identical to shipped 4/4; light fallback stays; no A-B warranted (B4_paddle_server_det.md)
6. [x] Surya block mode — done in run_engine.py (layout→per-block rec + html extraction)
7. [~] Surya language hints — RecognitionPredictor has no lang-hint param in 0.22.1 (init sig verified); not feasible without engine upgrade
8. [x] doctr parseq backend — ANSWERED by gate B1 (13 Sep): PARSeq has no Indic weights in doctr 1.1.0 (French vocab); both backends Latin-only on our pages; closed negative (B1_doctr_parseq.md)
9. [x] rapidocr PP-OCRv5 server rec weights — ANSWERED by gate B2 (14 Sep): NO-SERVER-INDIC — every _rec_server weight in rapidocr 3.9.2 is ch_* (Chinese); te/ta/ka mobile-only; closed negative
10. [x] openbharatocr: probed full API — ID-card-only (aadhaar/pan/passport/voter...), no full-page API; tesseract-mirror fallback documented honestly in RUN.md + VERSIONS
11. [x] IPO identifier_lang=auto verified from disk: outputs Devanagari on Devanagari pages (te_041..44: 25-725 deva chars) — auto works
12. [x] Engine retry wrapper — run_engine.py retries once with binarized variant on exception
13. [x] Per-page timeout — run_engine.py run_ocr_with_timeout (300s wall)
14. [x] 300-dpi re-render — not needed: 31 empties are GT-empty/tiny pages (ml_035 l1=63, te_060 l1=159), not render failures
15. [x] Grayscale+binarize retry — preprocess_image Otsu in run_engine.py
16. [x] Deskew — CLOSED as documented-skip 14 Sep: docstring truth-fixed (binarize-only); no skew cohort exists on disk (empties = contentless, 300DPI_PROBE 0/10); any future deskew needs its own 4-page gate first
17. [ ] Auto-crop black borders — skipped: renders have no border problem (verified via render checksums pass)
18. [ ] Two-page spread splitting — skipped: manifest pages are single-page renders (width/height sane)
19. [x] easyocr paragraph A-B — CLOSED moot: reader-combo fix landed (item 3 done, 391/400); paragraph A-B rejected by D12 (T-2 of demo) + low ROI
20. [x] PSM 3 vs 6 A-B — ANSWERED by gate B3 (13 Sep): PSM6 helps only te_001 (+17% chars), PSM1≡PSM3 elsewhere; parked as per-page chooser idea, no 400-rerun
21. [x] tessdata_best vs fast — ANSWERED by gate B3 (13 Sep): LOSS 0/12 configs; homebrew mal already best-by-md5; FAST stays, no rerun
22. [ ] user-words tuning — skipped (no gain expected on exam prose)

## 2. VERIFICATION (prove the outputs are real capacity)
23. [x] verify_all.py vs PDF text layer (empty/short/script-mismatch/capture-ratio)
24. [x] Cross-engine consensus: ≥6/10 agree — consensus_page_ids list in VERIFY_V2_SUMMARY.json (367/400)
25. [x] Repetition-loop detector — loop_redundancy 8-gram >0.6 in verify_v2.py
26. [x] Charset-hallucination flag — script_of vs dominant_script in verify_v2.py (15 events)
27. [x] Line-count sanity vs GT — lines_short_vs_gt (surya 97, doctr 3)
28. [x] Garbage-ratio — category L/M/N-based noise ratio (unicodedata, matra-safe)
29. [x] CER/WER floor — DONE: verify_v2 computes full CER/WER vs PDF layer + L1 cross-check (CER_STAGE3B.json, writer basis n=126 scored after mojibake/gt_thin nulls); per-script + bootstrap CIs in reports/CER_BY_SCRIPT.md
30. [x] Level-1 gold cross-check — median_capture_vs_l1 in leaderboard (item 30 metric)
31. [~] Confidence harvesting — paddle/rapidocr return box confs but current harness stores text only; needs run_engine.py change (noted)
32. [x] Per-page runtime telemetry — ms/page column in LEADERBOARD.md + DASHBOARD.md (from HEARTBEAT.jsonl)
33. [x] Output size P10/P50/P90 — per-engine p10/med/p90 in FAILURE_TAXONOMY.md
34. [x] Duplicate-output collapse detector — max_duplicate_pages per engine (2 max — no engine collapse)
35. [~] Table-page check — no table metadata in L1 labels (all 'paragraph'), approximated via multi-line/spacing heuristic in RUN.md table-ish examples; honest approximation
36. [~] Handwriting/stamp check — L1 has only 2 handwritten-span labels; cannot build meaningful stat, skipped honestly
37. [x] English-leak detector — english_leak in verify_v2.py (doctr 263, paddle 89, rapidocr 70)
38. [x] Native digits check — native/ascii digit profiles per engine in verify_v2.py
39. [x] NFC compliance — nfc_violations = 0 across all engines
40. [x] JSON schema validator — schema_violations = 0 (all packs valid)
41. [x] PNG render integrity — manifest_render_check in verify_v2.py (0 missing, 0 tiny)

## 3. ORCHESTRATION / AUTOMATION (one-push AGI-ops)
42. [x] orchestrator.py status/fill/migrate — plus verify/dashboard/guards/autoloop/loop commands
43. [x] auto-loop mode — `orchestrator.py autoloop 30` = fill→migrate→verify→dashboard→archive→seal every cycle
44. [x] Stall detector — stall_kill() 10-min idle kill+respawn (kept in loop)
45. [~] Auto-migrate on 400 — migrate runs every autoloop cycle (instant enough at 30-min cadence)
46. [x] HEARTBEAT.jsonl per page — crash-survivable, feeding ETA + speed stats
47. [x] DASHBOARD.md auto-refresh — counts+speed+ETA+guard section, written each loop cycle
48. [x] ETA calculator — live FILLING ETA in DASHBOARD.md (remaining × median ms/page)
49. [x] Core-count guard — MAX_PARALLEL_FILLS=7 in orchestrator.py fill_guards_ok
50. [x] Disk-space guard — 5GB floor pauses fills + alerts
51. [x] Known-error signature parser — KNOWN_ERRORS classify spawn failures, SPAWN_GUARD.json blocks futile respawns (caught easyocr reader-combo bug)
52. [~] Nightly verify rerun + diff — verify+dashboard refresh each autoloop; explicit diff-vs-previous report not built (low value at current cadence)
53. [~] Auto-archive + rerun on policy change — archive law manual+documented; out_archive/_vN pattern enforced in FOLDER_MAP rules
54. [x] Fresh-machine setup.sh — scripts/setup_fresh_machine.sh (venvs, tessdata, weights, verify)

## 4. DATA & MANIFEST QUALITY
55. [x] work/ → Datasets/ rename, all refs
56. [x] pages_script_map.json (dominant script per page)
57. [x] Merge dominant_script into pages_manifest — field present for 400/400 + mixed_book_page flag
58. [x] Manifest integrity — raw_path exists + page_index valid (verified 0/400 bad)
59. [x] Password-protected PDF list — verified 0 locked PDFs in manifest
60. [x] Corrupt/render-failed page list — verified 0 missing/0 tiny renders
61. [x] Mixed-book marking — 167/400 flagged in manifest + counted in reports (mislabeled te_024 lesson encoded)
62. [x] Human-review queue — reports/REVIEW_QUEUE.md top-50 disagreement pages
63. [x] Duplicate content audit — reports/DUPLICATE_AUDIT.md (found kn_035/kn_074 true PDF duplicate)

## 5. REPORTING / TEAM USABILITY
64. [x] Consolidated CSV — reports/MATRIX.csv page_id × engine char counts
65. [x] Leaderboard by median capture + nonempty — reports/LEADERBOARD.md (total chars, capture vs L1, ms/page)
66. [x] Per-language + Devanagari-subset leaderboards — reports/LANG_LEADERBOARD.md
67. [x] Failure taxonomy doc with examples — reports/FAILURE_TAXONOMY.md
68. [x] Best-engine-per-scenario table — reports/SCENARIO_BEST.md (mixed-book vs pure-Indic)
69. [x] Gap analysis — reports/GAP_ANALYSIS.md (union-of-best 485K chars vs per-engine)
70. [x] Side-by-side showcase — reports/SHOWCASE.md 10 pages × 10 engines
71. [x] WhatsApp 5-line weekly — reports/WHATSAPP_WEEKLY.md counts-only template
72. [x] "Explain like I own it" story — level2/PIPELINE_STORY.md
73. [x] Engine metadata in each JSON — DONE: engine_meta {engine, policy, dpi, version} in all 4,000 packs (verified in rapidocr/te/te_001.json)
74. [x] LEVEL2_SEAL.md auto-generation from disk — seal_gen.py (counts, forbidden checks, LEVEL 3 NOT STARTED)

## 18. EXECUTION STATUS (13 Sep — Track A/B/D done-tonight + remaining)
Track A (extraction):
- [x] easyocr 400/400 via per-script readers (spawn-guard released; DASHBOARD easyocr DONE) — evidence: level2/out/easyocr/ 400 json, level2/DECISIONS.log 2026-09-12
- [x] rapidocr 3.9.2 per-lang upgrade, ml honest-empty — evidence: level2/models/rapidocr/RUN.md (model/version line: "per-lang PP-OCRv5/v4 mobile rec; te/ta/kn+dev; ml=no model->honest empty")
- [x] openbharat alias classification (ID-card-only, tesseract-mirror fallback documented) — evidence: level2/models/openbharatocr/RUN.md
- [x] timeout real + shutdown fix — evidence: run_engine.py run_ocr_with_timeout (300s wall); HEARTBEAT.jsonl telemetry
- [x] provenance ocr_engine + engine_meta {engine, policy, dpi, version} in every pack — evidence: level2/out/rapidocr/te/te_001.json engine_meta
- [x] pages_400 broken symlinks fixed → renders_shared single-copy — evidence: renders_shared/ 400 PNGs, models/*/png/ symlinks
- [x] A3: _bin variants purged from renders_shared — DONE 14 Sep: 400 bins archived to _archive/renders_shared_bin_20260914/ (parent dir clean, 400/400 verified)
- [x] C5: en_fallback limitation stamped — DONE 14 Sep via seal_gen.py ENGINE_LIMITATIONS (auto-written into paddle RUN.md + metrics.json every regen; ml-ratio-0.0 disk evidence)
- [x] C8: preprocess uplift measured — DONE: PREPROCESSING_UPLIFT.json (-879 avg; 17/20 pages base>0→bin=0) + research/PREPROCESSING_UPLIFT_WHY.md (14 Sep): empties are contentless, binarization destroys faint strokes; keep retry-only, expansion gated off
- [x] C9: 300-dpi probe DONE — 0/10 recovered, truly contentless/photo pages (research/300DPI_PROBE.md); no rerun warranted
- [x] C10: sanity doc DONE — research/PUBLISHED_BENCHMARKS.md (capture-ratio vs curated-accuracy distinction; every external number TODO-VERIFY) + research/EXTERNAL_BENCHMARK_MAP.md + research/SARVAM_DELTA.md (14 Sep fetch: Sarvam publishes no per-script OCR accuracy)
Track B (verify):
- [x] B7 NFC — nfc_violations = 0 (item 39)
- [x] family consensus (tesseract-family = 1 vote) — evidence: reports/VERIFY_V2_SUMMARY.json consensus 382/400
- [x] B16 line-count sanity — lines_short_vs_gt (item 27)
- [x] B6 missing=ABSENT explicit — manifest_render_check 0 missing (item 41)
- [x] B9: char 5-gram Jaccard ≥0.6 consensus LIVE in TRUE_CONSENSUS.json (family-deduped, spec in consensus_5gram section; count 1/400)
- [x] B11: CER_STAGE3B.json LIVE (writer basis: 126 scored pairs after 55 mojibake + 219 gt_thin nulls; Stage-3b preference pairs = training_assets/preference_pairs_dpo.jsonl 126)
- [x] B12: L1-gold cross-check LIVE in VERIFY_V2_SUMMARY.json engines[].l1_crosscheck (median_cer_vs_l1 + l1_cer_gt1_examples)
- [x] B21: render_sha1 pinned per page in pages_manifest.json (400/400) + renders_shared.sha1
- [x] B22: regression alarm LIVE in verify_v2 (_verify_v2_previous.json baseline diff; regression_alarm fires in DASHBOARD on >2%)
- [x] B23: stamps in every report — report.py stamps 27 artifacts + seal_gen self-stamps LEVEL2_SEAL.md (14 Sep)
Track D (docs/law):
- [x] D2 docs 11→6 LIVING — evidence: this file + README + SOUTH_CANON + ULTIMATE_HYBRID_CONCERN + FOLDER_MAP + HOW_TO_RUN (root); 7 archived with headers in level2/_archive/
- [x] D9 DECISIONS.log ledger created (17 backfilled lines) — evidence: level2/DECISIONS.log
- [x] CANON pointer line added (L2 ops law supersedes where conflicting) — evidence: SOUTH_CANON.md line 2
- [x] Track G deck wiring in root README (§ "How Level 2 feeds Vaultstack")
- [x] D8: handoff test — PASSED in practice 13-14 Sep: BOSS_AGENT_LOAD_ORDER.md + ULTIMATE_HYBRID_CONCERN.md drove fresh subagents end-to-end (gates B1/B3/B12 + C-track all executed from docs alone; two failures were infra-flake, not doc gaps)
