---
name: handoff-2026-10-01-v4-integration
description: "Planner handoff 2026-10-01 ~17:45 IST — boss says Plan v4 + both docs are thin (\"false words\"); the REAL plan must come from a full read of ~320 research/concern/decision files. Ready-to-run Sonnet workflow + what is already read + next steps."
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-10-01T11:37:37.351Z
---

# HANDOFF — make the REAL Plan v4 from ALL research (2026-10-01 ~17:45 IST)

**Durable work folder:** `docs/campaign/handoff_2026-10-01_v4_integration/`. Scratchpad copies under /private/tmp may be evicted; use this folder.

## 1. What the boss wants (his words, condensed)
- "where the hell is the real plan, real architecture… we have done such high-level research… read all those research md files (200+) and the finalisation txt files."
- The boss's verdict on Plan v4 ([[proto-108-plan-v4-final]]) and the 2 Claude Docs: they look like "trash / false words". They under-use the research.
- Deliverables:
  1. a REAL integrated Plan v4 + architecture, where every box traces to research file:line;
  2. update both docs:
     - showcase for Vinay: https://claude.ai/artifact/Fn257YXfs4RD5htjZMUR3i
     - pure Plan v4: https://claude.ai/artifact/X3Bg1Mg58pPzrB6AcGEan9 (the boss attached this one; re-read it before editing).
- Ultracode is ON (workflows allowed and expected).
- **HARD rule: every subagent runs on Sonnet, never Opus.** The boss: "i will kill u if u use opus for sub agent".

## 2. Done so far (verified)
- **Read fully by the planner**, with notes in `corpus_extract.md`:
  - OCR_AGENT_MEMORY_FEED.md (all 1,621 lines);
  - PPT_FULL_DUMP and PPT_VS_SPEC_DIFF;
  - docs/architecture: W2_HYBRID, W5_BEAT_SARVAM_PLAN, W5_STRATEGY_OPTIONS;
  - R-series: R1, R2, R3, R4, R6, R7;
  - W1_RECIPE_REFRESH, W6_STRATEGY_UNIFIED, DEEP_RESEARCH_STRATEGY, PROBE22_EDGE_ANALYSIS, DEEPER_LIVE_RESEARCH (all);
  - MEETING_2026-09-29_STRUCTURED, LEVEL7_RESEARCH_CAMPAIGN;
  - ACTUAL_PROBE22_RESULTS, SURYA_LIVE, TEST_STATUS_NOTE, SOURCES;
  - the 5 W4 blind_verify reports.
- **Factchk correction, measured 17:10.** `Datasets/akshardrishti_official/Bodo/gu` is NOT a copy of the official test.
  - sha256 content overlap with test/test = 0. The old "4,645/5,344 overlap" matched filenames only.
  - Image 1.jpg is a real Gujarati handwritten word, "વાગડોદ", and matches its label (vocab[8831]).
  - So the H2 Gujarati slice has valid ground truth for the ≤4,645 images on disk. The images sit at `test/test/N.jpg`, so the manifest paths need that prefix.
- **Loop tick 1 (16:42 → 17:00).**
  - Agent 2's S5, H2 and Gold W0 work, blind-verified: all PASS.
  - Collision: Agent 2 copied two ECC notes into `docs/campaign/protocols/` as proto-107-gate1-and-s5-ssot.md and proto-108-md-consolidation.md. These clash with the planner's proto-107/108 numbers.
  - The sync (rsync without --delete) is safe. Nothing has been renamed yet. Fix: have Agent 3 archive or rename them with sha + log line, and add an alias line to proto-00.
  - Agent 1 is IDLE (DISPATCH §40) and needs the HW1 paste line, which is in proto-108 §12.

## 3. Next step: run the workflow (ready)
- **Run:** Workflow with `scriptPath: docs/campaign/handoff_2026-10-01_v4_integration/wf_corpus_to_plan_v4.js`. Every agent is set to `model:'sonnet'`.
- **What it covers:**
  - 50 partitions, 320 files, 4.65 MB, all paths validated (`partitions.json`; rebuild with `make_parts.py`, then `gen_wf.py`).
  - Per partition: Extract (every line read), then Verify (every number re-checked at path:line; hallucinations dropped).
  - Then 7 theme digests: handwriting / printed_architecture / weak_cells / training_compute / eval_gt_leakage / product_jury_competition / decisions_ops.
  - Then a completeness critic.
- **Size:** about 108 Sonnet agents.
- **Excluded on purpose** (older copies or process logs):
  - `_archive/pre_fix*`, `_archive/.audit*`, `_archive/cleanup*`;
  - `_reports/cleanup_cycle*`;
  - `_archive/campaign_drafts_2026-09-30`.

  The critic is told about these.
- **Then:**
  1. Write the integrated plan into proto-108 as a new top section, with history kept.
  2. Sync with `bash scripts/agent_bootstrap.sh --sync-only`.
  3. Update both docs: read each first, change only stale sections, never overwrite the boss's edits.

## 4. What the REAL plan must integrate (from what is already read)
- **The PPT already had a handwriting branch.** It used IIIT-HW-Dev / -Telugu / -INDIC-HW-WORDS (~872K words, 10 scripts). The v4 Handwriting Expert continues the original architecture; it is not a pivot (PPT_FULL_DUMP slide 2).
- **Two products in one system:**
  - (a) the handwriting word expert for the official test;
  - (b) printed 22-language page OCR, for the jury's "accuracy, layout detection, multilingual text handling".
  - (b) = Bodhan base + surgical per-script SFT on Sarvam's weak cells. Sarvam vs Bodhan on Sarvam's bench (DEEP_RESEARCH_STRATEGY lines 30–54):

    | Language | Sarvam | Bodhan |
    |---|---|---|
    | sat | 53.91 | 68.30 |
    | ks | 54.82 | 48.04 |
    | or | 80.01 | 75.45 |
    | sa | 84.05 | 78.11 |
    | mni | 85.12 | 82.85 |
    | doi | 89.46 | 85.51 |
    | brx | 90.48 | 90.69 |
- **Recipes:**
  - **R2 Nastaliq:** QARI-style 40–60k synthetic lines, then Qwen2-VL-2B / Bodhan LoRA, 8-bit not 4-bit, plus SR + CLAHE + NFKC/bidi first. Real data available: 600k-ks-ocr (CC-BY, 602K words) or Koshur Pixel 613k — verify which.
  - **R3 Ol Chiki / Mayek:** synthetic with HarfBuzz; fonts Noto + Eeyek; ≥100k renders.
  - **R4 OldScan:** A0–A3 ablation with a pre-registered adopt rule; never run.
  - **R7 tree:** N0 gates, data layers L1/L2/L3, curriculum word → line → block, RLVR on gold only.
  - **Kill criteria:** K1–K4.
- **Superseded beliefs:**
  - "sat/mni = Sarvam-only physics" is wrong now: Bodhan reads them (68.30 / 82.85).
  - The indic-ocr/tessdata community repo has sat and mni models (Apache-2.0).
  - IIIT-H printed results: Ol Chiki CRR 90.60, Kashmiri CRR 87.71.
  - The pa K1 "win" was a tie (ERRATUM-F1).
  - The tesseract trio is NOT byte-identical (ERRATUM-F2).
  - The "CER+CI rubric" came from a student repo (ERRATUM-F3).
  - The pooled "we lead 10/18" was a PDF-text-layer artefact.
- **mandela fires:**
  - DEEP_RESEARCH_STRATEGY and W6_STRATEGY_UNIFIED propose RLVR on indic-ocr-bench small_representative, then evaluating on the same bench. That is training on the test: forbidden.
  - surya's pair-vs-pdf gap (−0.25) shows PDF-tier ground truth flatters it.
- **Open:**
  - Bodhan licence: "Indic Open Model License" vs "Apache-2.0 with commercial threshold" (check RQ9_licences).
  - Normalisation parity of metrics.py with Sarvam's.
  - Bodhan page CER 0.69 (O-1).
  - The W4 H2 spec plans "B-19 Bodhan HW LoRA"; it must be reconciled with the PARSeq Handwriting Expert.

## 5. Standing rules
- No training, downloads or Sarvam calls without the boss.
- Sealed dirs are read-only.
- Never delete: archive with sha + log.
- NEXT.md is planner-owned.
- Lists, not tables, in the terminal.
- No commit without the boss.
- The boss assigns agents himself: give paste lines.
- Agents:
  - Agent 1 Engine: ses_f12a7b89cffet3Qff6UxLW7fYD
  - Agent 2 Verdict: ses_f1233a0a5ffeRSOBSwI87lmxxv
  - Agent 3 Miss: ses_f16bc20eaffe6J4emd9qVYK7CQ
