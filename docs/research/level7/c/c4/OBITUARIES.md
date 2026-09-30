# Lane C4 — Transfer Obituaries (campaign §9.2, 2026-09-27)

Law: `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §9.2. Any external number any
lane cites gets a transfer obituary: the number, where cited, why it does NOT
transfer (languages / scan-quality / harness / metrics mismatch). Verdict:
**DEAD-for-decisions** unless its obituary fails (fail-condition stated per
obituary — the disk evidence that would revive it). No downloads. No training.

Scope note: our own probe CERs (O-09–O-13) are MEASURED on disk, not vendor
claims — but they die the same death the moment they are cited outside the
harness that produced them (manifest n, tier mix, normalization, GT-trust).
Hence obituaries for them too, per PROMPT_MISS_AGENT task 4.

## O-01 — Sarvam Vision 2.1 overall 87.39 (Indic OCR Bench)

- Number: **87.39** overall block-level accuracy, 6,909 samples (6,609 × 22
  langs + 300 EN), sources 1800–present.
- Where cited: R6_COMPETITION_INTEL.md:136; lane C2 C21/C27/C31/C32; lane A
  citation shelf (`docs/research/level7/a/LEDGER.md:24`); C4-025 ("beat 87.39"
  stays directional).
- Why it does NOT transfer: (a) languages — bench-wide mean hides the cells
  that ARE our decision surface (Santali 53.91, Kashmiri 54.82, Odia 80.01);
  (b) scan quality — vendor-curated bench, not our 200-dpi citizen-document
  manifest with old-scan skew/warp/illumination; (c) harness — measured inside
  Sarvam's layout-parser + reading-order-pointer harness around the VLM, not
  our offline probe harness; (d) metrics — block-level accuracy vs our
  uncapped CER/WER tier split (§6.2/§6.5), no Wilson CIs, no McNemar pairing.
- Verdict: **DEAD-for-decisions.** "Beat 87.39" stays directional per §6.8.
- Fail-condition: revive only if re-measured on OUR manifest (n=1,227, same
  gates, SEED=20260926) with tier CERs + CIs — i.e. it stops being external.

## O-02 — Santali 53.91 (Sarvam bench cell)

- Number: **53.91**, global minimum of Sarvam's bench; Bodhan hits 68.30 on
  the same cell.
- Where cited: LEDGER.md header weak cells; C4-025/034/060/069/076/091; R6:136;
  lane C2 C22/J67; R4_OLDSCAN_RESTORATION.md:105-106.
- Why it does NOT transfer: (a) languages — vendor's Santali slice (script
  mix Ol Chiki/Bengali undisclosed) ≠ our sat cell (n=20, 100% sarvam_fill,
  agreement-only §6.2); (b) scan quality — bench sources 1800–present, unknown
  degradation mix vs our manifest; (c) harness — vendor VLM+harness vs any
  engine we route; (d) metrics — single point estimate, no CI on a
  small-n cell; the 14.4-pt Bodhan gap is same-data but same-harness-unknown.
- Verdict: **DEAD-for-decisions.** Our sat routing uses Lane A evidence +
  native-script support + visual inspection (D4), never this cell.
- Fail-condition: §6.4 human verification of our own sat items passes AND a
  paired on-manifest comparison shows a McNemar-significant gap.

## O-03 — Kashmiri 54.82 (Sarvam bench cell)

- Number: **54.82**; prior generation 55.93 (flat across generations).
- Where cited: LEDGER.md header; C4-003/010/016/023/025/033/046/060/064/069/
  071/073/076/079/091/098; R6:136; lane C2 C22/C28/K73/K80; R1; lane A.
- Why it does NOT transfer: (a) languages — Nastaliq-Kashmiri-specific
  failure (Urdu 91.21 / Sindhi 91.44 strong on same bench); vendor slice's
  Nastaliq-vs-Naskh mix unknown vs our ks cell (PDF-tier VERIFY-FIRST, trust
  45.0, barred D4); (b) scan quality — unknown; (c) harness — vendor harness;
  (d) metrics — point estimate, n undisclosed per cell; flatness 55.93→54.82
  is a structural hint, not a measurement of OUR pipeline.
- Verdict: **DEAD-for-decisions.** ks stays barred from W6 (D4); Nastaliq
  diagnosis comes from Koshur-Pixel lane-A/C2 records, not this number.
- Fail-condition: same as O-02 (own-manifest paired significant gap on
  verified ks GT only).

## O-04 — OldScan 55.3 (Sarvam bench cell)

- Number: **55.3** (Sarvam 2.1 old-scan column; cf. olmOCR-bench framing R1:72:
  field-wide worst column, every model).
- Where cited: LEDGER.md header; C4-006/010/032/040/045/048/056/066/072/075/
  076/083/090/093/094; R6:141 (Surya old_scan 42.8); lane C2 D34/N93/N99; R4.
- Why it does NOT transfer: (a) languages — vendor OldScan slice language mix
  undisclosed; ours is Indic citizen docs; (b) scan quality — THE load-bearing
  mismatch: their degradation distribution ≠ our 200-dpi renders +
  skew/warp/illumination (R1:72 confirms it is the worst column for ALL
  models, i.e. nobody's number transfers); (c) harness — vendor harness;
  (d) metrics — column accuracy vs our tier CER + planned 5-axis distortion
  stratification (§6.8, Real5 template C4-093).
- Verdict: **DEAD-for-decisions.** OldScan decisions use our manifest slice +
  Otsu-baseline deltas (R4), never 55.3.
- Fail-condition: our own old-scan slice scored per-engine with CIs +
  distortion tags; then the vendor number is irrelevant anyway.

## O-05 — Odia 80.01 (Sarvam bench cell)

- Number: **80.01**; Gemini 3.6 Flash 81.01 beats it; Bodhan 75.45 trails.
- Where cited: LEDGER.md header; C4-012/018/031/033/047/058/064/068/072/073/
  076/081/089; R6:136,143; lane C2 C22/G52/L81/L87; lane A:97.
- Why it does NOT transfer: (a) languages — three-way race within ~5 pts on
  undisclosed or-slice composition (PDF-tier + fill mix unknown) vs our
  or-cell (PDF-tier + 19 fill, script-ratio gate); (b) scan quality —
  unknown; (c) harness — three different vendor harnesses, none ours;
  (d) metrics — sub-5-pt gaps with no CIs and no pairing are noise-shaped;
  citing 80.01 vs 81.01 as a ranking is a point-estimate delta (§9.3 forbids).
- Verdict: **DEAD-for-decisions.** or-cell is winnable by wrap/ensemble, but
  that call uses our paired on-manifest numbers, not vendor cells.
- Fail-condition: paired McNemar-significant or-cell gap on OUR manifest
  with Wilson CIs.

## O-06 — Bodhan Santali 68.30

- Number: **68.30** Santali (0.8B, vs Sarvam 53.91 → 14.4-pt gap, same bench).
- Where cited: R6:136; lane C2 C22/J67; lane A citation shelf; R7 sat rule
  (`THEN` clause cites Bodhan lead).
- Why it does NOT transfer: (a) languages — same vendor-bench slice, same
  undisclosed-composition problem as O-02; (b) scan quality — unknown;
  (c) harness — Bodhan's 33M-layout + 0.8B-Qwen3.5 block-OCR harness, not
  ours; the gap may be harness, data, or slice luck; (d) metrics — point
  estimate, no CI, no pairing; "14.4-pt headroom" is directional, not a W6
  budget input.
- Verdict: **DEAD-for-decisions.** sat specialist stays highest-ROI INFERENCE
  (J67), gated on our own §6.4 verification (D4), not on 68.30.
- Fail-condition: independent on-manifest measurement of a Bodhan-routed
  pipeline (needs download approval + GPU — P1/P2, not now).

## O-07 — Bodhan overall 84.94

- Number: **84.94** overall (vs Sarvam 87.39, Gemini 79.35, GCV 71.76).
- Where cited: R6:136; lane C2 C21; lane A competitive matrix (`a/LEDGER.md:267`).
- Why it does NOT transfer: same four mismatches as O-01 (bench-wide mean,
  curated sources, vendor harness, block-accuracy vs tier-CER). Ranking
  vendors against each other is competition intel (C2's job), not a probe
  decision input.
- Verdict: **DEAD-for-decisions.**
- Fail-condition: none within campaign scope — vendor-vs-vendor means never
  enter our W6 feasible set (§9.4).

## O-08 — PaddleOCR-VL-1.6 OmniDocBench 96.33

- Number: **96.33%** OmniDocBench v1.6 (0.9B VLM); CPT +0.69 / SFT +0.63 /
  RL +0.08 (94.93→96.33); Real5 93.19.
- Where cited: C4-045/093/094/095; lane C2 E41/E42/E44/D34; lane A:60-64,136;
  R6:140.
- Why it does NOT transfer: (a) languages — OmniDocBench is EN/CJK-heavy;
  Devanagari/Arabic coverage ≠ Ol Chiki/Nastaliq/Mayek (C4-096 precedent:
  no-script-claim means no transfer); (b) scan quality — Real5 distortions
  are physical-reconstruction classes, not our 200-dpi citizen scans;
  (c) harness — 0.9B VLM needing GPU + download approval (P2, §0 rule 1);
  not runnable in our offline probe harness today; (d) metrics — TEDS/
  composite doc-parsing accuracy vs our line CER; 96.33 is a parsing score,
  not a recognition CER.
- Verdict: **DEAD-for-decisions** as a model claim; **ALIVE as method**:
  Real5's five distortion axes (C4-093) and CPT→SFT→RL sequencing (E42) enter
  the architecture as design patterns — patterns transfer, numbers don't.
- Fail-condition (model number): P2 approval + GPU + on-manifest scoring
  with tier CERs; then it is our number, not theirs.

## O-09 — Our probe rapidocr CER 0.669

- Number: **0.6692** (`avg_metrics.cer`, `preds_rapidocr.metrics.normalized.json`;
  n=1,227 scored, 343 missing + 15 loop-failures + 347 CER-100 rows inside).
- Where cited (risk): any lane citing "rapidocr 0.67" as rapidocr's quality.
- Why it does NOT transfer outside its harness: (a) languages — 18-lang mean
  over a manifest with barred-GT langs (ks/mni/mr/ur/ne-pdf) whose GT is
  garbage by our own forensics; (b) scan quality — our 200-dpi citizen mix
  only; (c) harness — rapidocr build + our gates + normalization choice
  (raw-vs-normalized Δ0.0015 ablation not attached to the bare number);
  (d) metrics — mean over uncapped CERs incl. 347 CER=1.0 rows and 343
  missing counted per §6.5; valid-samples CER is 0.5417 — a DIFFERENT number
  from the same run. Quoting 0.669 without the counting rule is forgery-adjacent.
- Verdict: **DEAD-for-decisions outside probe22.** Inside: valid only with
  tier split + CIs + abstention split (§9.3).
- Fail-condition: cite with full §9.3 dress (Wilson CI, coverage +
  conditional CER, tier table) on the same manifest/gates — then it is
  evidence, not a slogan.

## O-10 — Our probe tesseract CER 0.487

- Number: **0.4870** tess_indic (0.4853 bilingual)
  (`preds_tesseract_indic.metrics.normalized.json`; valid-samples CER 0.4199,
  102 CER-100 rows).
- Where cited (risk): "tesseract 0.49" as the classical baseline to beat.
- Why it does NOT transfer: same four as O-09, plus (c2) engine-config
  specificity — tessdata pin + 300s-timeout runs (bn_d014 ~78s, hi_d066 ~82s)
  are part of the number; a stock-tesseract install elsewhere reproduces
  nothing; (d2) EN-sanity asymmetry — tesseract stacks ~122% CER on ornate
  EN scans (C4-099), so 0.487 already bundles genuine engine weakness on
  ornate pages with GT-noise inflation on barred langs.
- Verdict: **DEAD-for-decisions outside probe22**; inside, tier + CI dressed.
- Fail-condition: same §9.3 dress as O-09.

## O-11 — Our probe doctr CER 0.869

- Number: **0.8691** (`preds_doctr.metrics.normalized.json`; valid-samples
  CER 0.8638, only 47 CER-100 rows — honestly bad, not inflated).
- Where cited (risk): "doctr fails Indic (0.87)" as a general doctr claim.
- Why it does NOT transfer: (a) languages — our 18-Indic manifest; doctr's
  Latin strength is documented, not measured here; (b) scan quality — our
  mix; (c) harness — doctr build + predictor config pinned in probe22;
  (d) metrics — 0.869 bundles GT-noise langs with real weakness; the honest
  read needs the EN-sanity column (doctr ~42% on EN per C4-099) to separate
  harness-sound/engine-weak from GT-noise.
- Verdict: **DEAD-for-decisions outside probe22** (never "doctr is bad at
  OCR" — only "doctr scored 0.869 on our manifest under our gates").
- Fail-condition: §9.3 dress + EN-sanity pairing.

## O-12 — Our probe anuvaad CER 0.711

- Number: **0.7114** (`preds_anuvaad_tesseract.metrics.normalized.json`;
  valid-samples CER 0.3162 on only 503 valid of 1,227 — 672 CER-100 rows).
- Where cited (risk): "anuvaad 0.71" as an engine ranking input.
- Why it does NOT transfer: (d) metrics is the killer here — the 0.711 mean
  is dominated by 672 CER=1.0 rows (abstention/coverage story, §9.3), while
  valid-samples CER is 0.3162. Citing either number alone inverts the story:
  the engine either looks mid (0.71) or good (0.32); the truth is
  coverage 503/1227 + conditional 0.32. Any citation without BOTH numbers is
  a silent-abstention violation.
- Verdict: **DEAD-for-decisions as a scalar.** Alive only as the pair
  (coverage + conditional CER).
- Fail-condition: cite the pair with CIs; never the scalar.

## O-13 — Our probe sarvam-subset CER 0.24

- Number: **0.2400** (`preds_sarvam_vision.metrics.normalized.json`;
  n=54 = 3/lang × 18 langs, credit cap; valid-samples 0.2185, n=48).
- Where cited (risk): "sarvam 0.24 beats everything" as a routing argument.
- Why it does NOT transfer: (a) languages — 3 items/lang cannot represent any
  language (n<50 no-winner rule §9.3/§6.7 bites hardest here); (b) scan
  quality — 54-item convenience slice, not the manifest distribution;
  (c) harness — credit-capped API baseline, no EN column (D2: Sarvam EN
  SKIPPED — the baseline lacks the sanity reference every other engine
  carries); (d) metrics — no CIs possible at n=3/lang; comparing 0.24
  (n=54) against 0.487 (n=1,227) is a sample-size category error.
- Verdict: **DEAD-for-decisions.** Sarvam is the benchmark target, not a
  routable component (D2). The 54-call cap means this number can never grow
  into evidence without user approval.
- Fail-condition: user-approved full-manifest Sarvam run + EN column +
  §9.3 dress — explicitly deferred to the validation call, not this campaign.

---

Obituary count: **13** (O-01–O-13). Verdicts: 13 × DEAD-for-decisions (O-08
method-half alive as pattern). No obituary failed; no number revived.
