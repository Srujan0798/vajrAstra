# VAJRASTRA 100/10 MASTER SPEC
# The ultimate specification for beating Sarvam AI and reaching #1 in India.
# Authored by the ETERNAL VALIDATOR after full-disk audit — 2026-09-14.
# Scope: every item verified against disk, DECISIONS.log, and gates before being listed.

---

## 0. HOW TO USE THIS FILE (read first — agents MUST obey)

This is the single, ordered, verified execution register. Laws:

1. **Anti-phantom law** — before executing ANY item, re-verify it exists on disk
   (the prior validator's "P0 bugs" were 70% contamination phantoms —
   DECISIONS.log 2026-09-14). Command for each item is included — run it first.
2. **4-page gate** — no engine/model change beyond 4 pages without surviving 4.
3. **One-writer truth** — never hand-edit `level2/reports/` or `models/`.
   Fix the writer (`verify_v2.py`, `report.py`, `seal_gen.py`, `report_gen.py`,
   `deep_verify.py`, `research/gap_report_gen.py`), never the output.
4. **No shared-pipeline edits by sub-agents** — agents work only in
   `research/` + `research/gates/` + new standalone generators. The executor
   (main agent) merges. (Hard-learned: contamination incident 14 Sep.)
5. **Completion law** — nothing is ever "done." 100/10 = Sarvam #2, Vaultstack #1.
6. **Completion order** — execute P0 → P1 → P2 in order; each item lists its
   verification command AND its acceptance gate.

Verified basis at spec time (disk-recounted, this cycle):
- 10/10 engines × 400 pages = **4,000/4,000 packs**; schema 0 violations
- LEVEL2_SEALED = true (11/11 gates GREEN; verify with `seal_gen.py`)
- True consensus 38/400 (word-Jaccard ≥0.5, family-dedup); family 21/400; 5-gram 1/400
- Gap (lower bound, 177-page GT≥200 basis): **7.1%** (GAP.md)
- Median CER vs PDF-layer (writer basis): surya 0.430 · anuvaad 0.475 ·
  tess-fam 0.493 · IPO 0.655 · paddle 0.707 · rapidocr 0.712 · doctr 0.853 · easyocr 0.903
- Sarvam published (sarvam.ai, cited STALE until re-fetched by main agent):
  te 87.7% · ta 93.4% · kn 89.9% · ml 91.6% accuracy (≈ CER 0.123/0.066/0.101/0.084)

---

## 1. THE 100/10 DEFINITION (22 Pillars — current status audited)

| # | Pillar | Status | Verification |
|---|--------|--------|--------------|
| P1 | Benchmark 4,000/4,000 sealed | ✅ DONE | `seal_gen.py` → 11/11 GREEN |
| P2 | One-writer report chain | ✅ DONE | `report.py` runs verify→deep→gap→gen→seal in one pass |
| P3 | True consensus (family-deduped) | ✅ DONE | `TRUE_CONSENSUS.json` 38/21/1 counts |
| P4 | Script-sliced leaderboards | ✅ DONE | `LEADERBOARD_BY_SCRIPT.md` 6 strata |
| P5 | Engine honesty (alias/wash/limitation disclosed) | ✅ DONE | `seal_gen.py` QUALITY_STATUS + ENGINE_LIMITATIONS → RUN.md |
| P6 | Engine provenance stamped in packs | ✅ DONE | `engine_meta` + `provenance=ocr_engine` in all packs |
| P7 | Manifest integrity + tag corrections | ✅ DONE | 400/400; te_024/te_065 → Devanagari |
| P8 | Reproducibility (setup.sh smoke) | ✅ DONE | `.setup_smoke_proven` flag + script |
| P9 | Decision ledger | ✅ DONE | `DECISIONS.log` 22+ entries, append-only |
| P10 | Regression harness (auto-baseline) | ✅ DONE | `_verify_v2_previous.json` diff in verify_v2 |
| P11 | CER vs PDF-layer per engine | ✅ DONE | `CER_STAGE3B.json` writer-basis, mojibake-null gate |
| P12 | Level-3 socket (stubs that refuse to run) | ✅ DONE | `engines/level3_stub.py` + sarvam/bhashini adapters dry-run |
| P13 | Training-data exports (SFT/DPO/disagreement) | ✅ DONE | `training_assets/` (SFT 1760, DPO 126, queue 50) |
| P14 | Gap slide with rigorous lower bound | ✅ DONE | `GAP.md` 7.1% |
| P15 | Sep-16 package | ✅ DONE | `SEP16_ONE_SCREEN.md`, `WHATSAPP_*.md`, `SHOWCASE.md` |
| **P16** | **Accuracy ≥ Sarvam per-language** | ❌ **GAP-3.5x** | See §2 Delta Table |
| **P17** | **Akshara-boundary aux loss (Stage 2)** | ❌ MISSING | No annotation schema, no trainer |
| **P18** | **SCST RL on CER (Stage 2b)** | ❌ MISSING | Rewards export exists; RL trainer absent |
| **P19** | **SimPO/DPO at scale (Stage 3b)** | ⚠️ PARTIAL | 126 pairs exist; need ≥50K + trainer |
| **P20** | **Learned preprocessing (Stage 0)** | ❌ MISSING | OpenCV binarize-only; deskew NOT implemented |
| **P21** | **Layout model (Stage 1, DocLayout-YOLO)** | ❌ MISSING | L1 boxes exist (400 gold) — no training harness |
| **P22** | **Production serving (API, latency, SLOs)** | ❌ MISSING | No Triton/K8s; no paid-API runs |

**Count: 15/22 pillars standing. 7 missing. Progress toward 100/10: 68%.**

---

## 2. SARVAM DELTA TABLE (the only scoreboard that matters)

Per-script best CER (writer basis, VERIFY_V2_SUMMARY.json) vs Sarvam published accuracy.
Accuracy = 1 − CER. **Metric parity caveat:** Sarvam's numbers are on their curated
benchmarks; ours on our hard 177-page GT≥200 basis. Honest comparison needs THEIR
pages on disk (§5 P16-1).

| Script | Our best (engine) | Our CER | Our Acc | Sarvam Acc | Gap (pp) |
|--------|-------------------|---------|---------|------------|----------|
| Telugu | surya | 0.430 | 57.0% | 87.7% | **−30.7** |
| Tamil | surya | 0.633 | 36.7% | 93.4% | **−56.7** |
| Kannada | surya | 0.810* | 19.0% | 89.9% | **−70.8** |
| Malayalam | surya (IPO-cap) | 0.655 | 34.5% | 91.6% | **−57.1** |

*Kannada median across all engines is weak; basis has only 19 GT≥200 pages (small-n).
Malayalam basis only 9 pages (tiny-n) — directionally bad, statistically loud.

**The honest sentence:** on our hardest verifiable pages, the best free engine is
~30–70pp behind Sarvam's published accuracy. This is the reason Vaultstack exists.

---

## 3. P0 — IMMEDIATE FIXES (execute first; each ≤1h; all blocker-class)

### P0-1. PURGE 14,600 SYNTHETIC RENDERS POLLUTING renders_shared (RED)
- **Evidence (disk, this cycle):** `ls level2/renders_shared | wc -l` → **15,000**;
  `ls level2/renders_shared | grep -c '^synth_'` → **14,600 synthetic junk**;
  real renders = 400. verify_v2's manifest check already flagged
  `"n_renders": 15000` and nobody acted.
- **Why:** renders_shared is law-protected as "the 400 shared PNG renders."
  14,600 foreign files break the checksum discipline, every audit count,
  the render_once race contract, and any future diff/reproduce workflow.
- **Fix (archive law safe — move, not delete):**
  ```bash
  mkdir -p level2/_archive/synth_renders_leak_20260914
  mv level2/renders_shared/synth_* level2/_archive/synth_renders_leak_20260914/
  ls level2/renders_shared | wc -l   # must equal 400
  shasum level2/renders_shared/*.png > level2/renders_shared.sha1
  python level2/verify_v2.py          # n_renders must print 400
  ```
  Plus one DECISIONS.log line recording the leak.
- **Acceptance:** 400 files; `verify_v2` manifest render check reports
  n_renders=400, missing_render=0, tiny_render=0.
- **Rating lift:** Data truth 9.5→10; Reporting truth +0.5 (kills the
  "n_renders=15000" red flag everyone has been skimming past).

### P0-2. Kill GAP_ANALYSIS.md properly (archive, not delete)
- **Evidence:** `level2/reports/GAP_ANALYSIS.md` exists alongside `GAP.md`.
  FOLDER_MAP lists GAP_ANALYSIS as the item-69 artifact; DECISIONS 2026-09-14
  calls it "legit one-writer artifact" — BUT two gap files answering one question
  invites exactly the quoting-error David will ask about (9.9% vs 7.1%).
- **Fix decision needed (H-queue):** keep both as complementary views (rename
  ANALYSIS → "GAP_RAW_VOLUME.md" with banner "volume ≠ correctness — cite GAP.md")
  OR archive it. This is a human call (brand surface).
- **Acceptance:** exactly one headline gap figure is quotable; the other file
  carries a banner pointing at it.
- **Rating lift:** Reporting truth 8→9.

### P0-3. Commit the working tree (git clean state)
- **Evidence:** `git status --short` shows modified RUN.md/metrics + untracked
  agents' files (cascade/, training/, reliability/, governance/, engines/*,
  VAJRASTRA_ELITE_ARCHITECTURE.py, quarantine batch).
- **Fix:** operator decides keep/kill per quarantine law (§4 P4). Restore G10.
- **Acceptance:** `git status --porcelain` empty except auto-regen paths; seal
  G10 GREEN.
- **Rating lift:** Reproducibility 8→9.

### P0-4. Stamp `generated_at` freshness on LEVEL2_SEAL.md itself
- **Evidence:** seal file's stamp line comes from report.py pass; verify
  `tail -2 level2/reports/LEVEL2_SEAL.md`.
- **Fix:** already emits via report.py stamp; CONFIRM in-place, not create.
- **Acceptance:** stamp line present after every report run.

---

## 4. P1 — QUALITY HARDENING (this week)

### P1-1. Quarantine verdicts (H-queue, operator)
- `level2/_quarantine/{level3_readiness.py, preprocessing_uplift.py, regression_test.py}`
  — uninvited scaffolds. Decide: keep → wire into report.py formally, or kill.
- `VAJRASTRA_ELITE_ARCHITECTURE.py` (root) — mega-file scaffold with import errors
  (references `nn`, `torch` without imports in some functions). Kill or promote
  to `level2/elite/` package properly.

### P1-2. Wire `regression_test.py` into autoloop (if kept)
- Currently orphaned. If kept: add to `refresh_chain()` after `cmd_report()`;
  alarm triggers DASHBOARD banner on regression >2%.

### P1-3. engines/ socket formalization
- `engines/__init__.py` needs `BaseEngine` + `register` + `REGISTRY` exported
  cleanly (level3_stub imports them). Add `engines/README.md` contract.

### P1-4. B21 render sha1 spot-audit
- `renders_shared.sha1` exists; recompute + compare 20 random pages quarterly.

### P1-5. B22 regression alarm LIVE
- Verify_v2 writes `_verify_v2_previous.json`; add DASHBOARD.md banner when
  any engine's median CER regresses >2% vs previous. (Wiring was planned,
  confirm visible alert exists after next regen.)

### P1-6. Confidence harvest (V18)
- Install per-engine confidences for paddle/doctr/rapidocr into packs
  (fields exist in engine outputs; add `confidence_mean` per region in
  run_engine.py write_json — gated 4-page law first).

### P1-7. 300-DPI rescue — CLOSED as decided
- `research/300DPI_PROBE.md`: 0/10 recovered → pages are GT-empty.
  Propagate this verdict into `PROMPT.md` section of tesseract_indic RUN.md
  so no one re-proposes it.

### P1-8. Deskew — decided SKIPPED (documented)
- OpenCV deskew not implemented; binarize-only is current. Justification:
  7.1% gap mostly not skew-driven (PUBLISHED_BENCHMARKS + 300DPI probe).
  Keep as post-Sep-16 Track A item with measured-ROI gate [NO-SARVAM-DELTA now].

### P1-9. Latency trust fix
- HEARTBEAT median ms/page per engine on dashboard is fine for run engines,
  but tesseract-family heartbeat had only 4 samples; TIMING_PROBE.jsonl has
  21 fresh ones. Republish LATENCY.md from probe until heartbeat fills.

---

## 5. P2 — COMPETITIVE ENGINEERING (next 2 weeks, pre-L3)

### P2-1. Acquire Sarvam comparison pages (THE P16 precondition)
- Download Sarvam's published benchmark pages / IndicDLP test split (whatever is
  public), run OUR harness on them, produce apples-to-apples CER. Without this,
  our delta table is a parallax guess. [SARVAM-DELTA: CRITICAL]
- Gate: `research/gates/P16_sarvam_pages/` with protocol-before-run.

### P2-2. AKER vs CER verdict closure (C×G debate live)
- Full clean-basis AKER (grapheme-cluster error rate) recompute → DECISIONS.log
  verdict on deck metric claims. (grapheme-cluster = closest OSS proxy to
  akshara-level scoring before P17 exists.)

### P2-3. Bootstrap CIs on writer basis
- Recompute two-tier CIs over the 79-page v2-clean basis (1000 resamples);
  publish confidence intervals next to leaderboard ranks so "wins" are honest.

### P2-4. Distillation readiness (P21 prep)
- Export the aligned multi-teacher corpus (per-region best-engine text +
  confidence) as the distillation training set. No training yet (law).

### P2-5. Engine #11 candidate evaluation harness
- PaddleOCR-VL 1.6 free-Apache smoke via 4-page gate (published 96.33%
  OmniDocBench — strongest free claim). If it beats surya on our basis 4-page,
  it earns a 400 fill as engine #11. [SARVAM-DELTA: HIGH]

### P2-6. Surya lang-hint upstream watch
- 0.22.1 lacks lang hints (verified). Track surya releases; on release
  with hints, run 4-page gate → possible CER win without training.

---

## 6. P3 — THE 100/10 CLIMB (the Sarvam-beating program; Phase-plan)

### Phase α — Data (months 1–2)
- D1: akshara-boundary annotation schema (Syllable units for te/ta/kn/ml) +
  coding the segmenter (start rule-based on Unicode canonical decomp + postfixes,
  graduate to learned segmenter). Target: 10K pages Stage-2 loss-ready. [P17]
- D2: Layout gold expansion: extend L1 boxes to IndicDLP-42 classes on the 400
  pages (train-time gold for Stage 1). [P21]
- D3: Hard-case expansion: handwriting pages (IIIT-HW), old-scan pages
  (Surya OldScan 41.8% class — our missing failure mode), stamps/forms. [P16]

### Phase β — Training (months 2–4)
- T1: Stage-0 learned preprocessing (deskew/denoise/binarize as neural ops) —
  measured ROI gate: must beat OpenCV baseline by ≥2pp CER on 4-page gate.
- T2: Stage-2 SFT with akshara-boundary aux loss on 1 finetune of choice
  (TrOCR first) — success metric: median CER < tesseract-family (0.493) on
  our 79-page v2-clean basis. 4-page law applies. [P16, P17]
- T3: Stage-2b SCST on CER using cer_rewards as curriculum. [P18]
- T4: Stage-3 noisy→JSON SFT on 1760 pairs, then SimPO at scale on 50K pairs
  (grow from 126 via CER gap band 0.15/0.30). [P19]

### Phase γ — Product (months 4–6)
- S1: Distill ensemble → student (target ≥95% ensemble quality at ≤1/5 latency).
- S2: Triton serving + canary; SLOs from reliability/slo.py; error budgets.
- S3: Paid-API A/B: Sarvam digitise ₹0.5/page vs our student CER-delta →
  the Vinay pricing story. [P22]

### Phase δ — Win condition
- W1: Per-language CER < Sarvam published on OUR pages AND on THEIR pages
  (both directions — otherwise claims are cherry).
- W2: Same on at least 2 external public benchmarks (IndicDLP split + one more).
- W3: Reproduced by a stranger from setup.sh on a clean machine.

---

## 7. STANDING AGENT ORDERS (append to every agent brief)

1. Before executing ANY item here, run its Evidence command. If the finding is
   absent, mark CLOSED-NOT-A-BUG and move on. (Anti-phantom law.)
2. Agents never touch: `verify_v2.py`, `report.py`, `report_gen.py`,
   `seal_gen.py`, `deep_verify.py`, `run_engine.py` — propose in `research/gates/`
   via 4-page gates; the main agent merges.
3. Every completed item gets: (a) gate artifact in `research/gates/`, (b) one
   DECISIONS.log line, (c) IMPROVEMENTS_CURRENT_WORK.md checkbox flip.
4. Any new "improvements" from external reviews/quotes must be audited against
   disk BEFORE execution; log phantom-rate of that source in DECISIONS.log.
5. No completion claims, ever. The only acceptable sentence form is
   "at X/10 on the road to 100/10."

---

## 8. ACCEPTANCE AUDIT TRAIL (how the validator re-checks)

The validator wheel (read-only) will re-verify monthly by running, from disk:
- `python level2/seal_gen.py` — expect 11/11 GREEN (gates can add, never drop)
- `python level2/verify_v2.py` — schema 0; CER present on all engines
- recount packs: `find level2/models/*/json -name '*.json' | wc -l` == 4000
- `git log --oneline | head -1` age ≤ 24h while work continues
- `grep -c "TODO-VERIFY" level2/research/LEVEL3_COST_ESTIMATE.md` =
  declining month over month

This spec retires only when: Sarvam is #2, Vaultstack is #1, India's OCR is ours.

_End of SPEC. Execute in order. Verify before believing. Never claim done._
