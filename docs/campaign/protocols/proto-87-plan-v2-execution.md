---
name: proto-87-plan-v2-execution
description: "Added 2026-09-30 — Plan v2 (the better plan the boss gives Vinay): PPT core recipe cut to one fine-tune, built in proof order — fix engines, get ONE comparable number on Sarvam's public benchmark, then LoRA one VLM on ~10k human pairs split by document; 5 days, 5 gates; mandela independence fixes; maps each step to existing protocols"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T09:08:11.263Z
---

# PROTO-87 — PLAN V2 EXECUTION (after the Vinay meeting; supersedes the W6 "QLoRA kok+pa" scope)

**Shared doc for Vinay:** https://claude.ai/code/artifact/77a91224-033e-49d7-96dc-7233776a8575 ("AksharDrishti — Plan v2 vs the current PPT plan", 2026-09-30).
**Status of the plan itself:** a proposal until Vinay/the boss approve decisions V1–V7 below. Nothing trains before Gate 2.

## Why Plan v2 (evidence, opened/measured 2026-09-30)
- Market (Sarvam blog, Indic OCR Bench, word accuracy, macro over 22 languages, all systems run by Sarvam): Sarvam Vision 2.1 87.39 · Bodhan 84.94 · Gemini 3.6 Flash 79.35 · Google Cloud Vision 71.76 ·
  **Surya OCR 2 69.96** · Mistral OCR4 69.16 · Opus 5 68.81 · Gemma 4 65.53 · Chandra-OCR2 64.56 · GPT 6 Astra 63.69 · Infinity-Parser2 Pro 49.83 · Azure Vision 4.0 41.29 · AWS Textract 4.64.
  Surya vs Sarvam per language: Bengali 81.79 vs 93.47 · Hindi 86.12 vs 93.52 · Konkani 90.81 vs 97.41 · Punjabi 83.06 vs 89.16.
- Our routing picks surya in 9 of 12 languages with n≥50 → our system today would likely sit near 69.96 (ESTIMATE until step 1 runs) → ~6th of 14, 17.4 points behind Sarvam.
- indic-ocr-bench (HF card): Apache-2.0, 6,909 test + 1,173 small_representative, 22 languages + English, GT "reviewed twice by human language experts", semantic text blocks, `metrics.py` scorer, freely downloadable.
- Human-labelled pairs already on disk (`Datasets/akshardrishti_official/`): ~2,900 bn, 3,500 hi, ~500 sa, 3,500 en image–text pairs; 100 per language (30 en) are our test items → ~10,000 usable for training after removal.
- Speed (level2/reports/LATENCY.md, this Mac): surya 16.3 s/page · tesseract 0.7–3.5 s · easyocr 30.7 s · paddle 95.2 s → surya-only on 5,344 test images ≈ 24 h.
- Punjabi fails K1 (tie, p=1.0); Konkani passes (p=0.0033, n=100).
- Official hackathon scoring rules and deadline: UNKNOWN (the "CER+CI/WER/S-D-I/sec-per-page" description is a student project's — factchk).

## Decisions needed (from the doc §8) — record answers in proto-92 as U16–U22
V1 download Sarvam's public benchmark (recommend yes) · V2 fine-tune scope = one VLM on bn/hi/sa/en human pairs + kok, pa dropped (recommend yes) · V3 backbone Qwen2.5-VL-3B vs GLM-OCR 0.9B ·
V4 ship surya under the $5M cap or fallbacks · V5 Ol Chiki/Meetei models have no stated licence — benchmark-only use? · V6 who confirms deadline + scoring rules · V7 handwriting in scope after the test-set profile.

## The five days (Day 1 = the day approvals land). Each gate must pass before the next day starts.
| Day | Work (protocol) | Gate |
|---|---|---|
| 1 | Paddle brx/doi mapping + surya Sanskrit diagnosis ([[proto-82-engine-empty-output-patterns]]); median + empty-output + CI columns ([[proto-80-hackathon-metric-alignment]]); rebuild the score sheet from a script ([[proto-61-sheet-provenance-forensics]]); GT-tier tables ([[proto-62-gt-tier-stratified-reporting]]) | every fix wins on 4 pages before any full re-run |
| 2 | **Comparable number (NEW, §A below)** + script-detection accuracy on our 1,283 labelled items ([[proto-78-submission-readiness]]) | no score, no training — if the number is not produced, stop and report why |
| 3 | **One fine-tune (NEW, §B below)**: 5-item smoke test, then LoRA on bn/hi/sa/en pairs + kok, split by source document | held-out error must drop below the untrained baseline, or training is abandoned |
| 4 | Ol Chiki/Meetei models if licensed ([[proto-83-licence-verification]]); routing with empty-output fallback; timed dry run on 50 test images ([[proto-78-submission-readiness]]); test-set profile ([[proto-81-handwriting-degraded-coverage]]) | seconds per page fits the confirmed deadline |
| 5 | Regenerate every table from scripts; re-score on Sarvam's benchmark; ChatGPT review + human spot check | every number in the write-up reproduces from its script |

## §A — Comparable number on Sarvam's public benchmark (Engine subagent; gated on V1)
> 1. Download `sarvamai/indic-ocr-bench` (record revision hash + sha256), `small_representative` split first (1,173 samples); keep the official `metrics.py` UNCHANGED (vendored copy + hash).
> 2. Run our current routing (per-language primary engine, fallback on empty output) on each block crop; the language label comes from the dataset row (we are measuring recognition, not script ID — report that assumption).
> 3. Score with the official scorer; report overall macro-22 exactly as Sarvam defines it (English excluded), per-language rows, loop-flagged exclusions, and our number beside the 13 published systems.
> 4. Then the full 6,909 test split if time allows (≈ ≤31 h at surya's full-page speed; blocks are smaller — measure).
> Writes: `level2/unified/run_indic_ocr_bench.py`, `docs/campaign/BENCH_SARVAM_RESULT.md`. Never fine-tune on this benchmark (it is evaluation only).

## §B — One fine-tune without leakage (Engine builds data + trains; Verdict audits the split first) — gated on V2, V3 and Gate 2
Mandela fixes built in (shared-pool bias, verifier = designer, tautology, shared hallucination):
> 1. **Split by source document, not by image:** derive a document/group id per pair (file-name stem families, source PDF, capture batch) — never let two crops of one page or document sit on both sides.
> 2. **Remove our test items and their near-duplicates** (the 100 probe items per language + perceptual-hash/text-overlap neighbours) from training; write the exclusion list with counts.
> 3. **Hold out 10% of documents per language** as the Gate-3 test; plus Sarvam's bn/hi/sa/kok rows from §A as an external test the training never saw.
> 4. Smoke test on 5 items (memory ≤ the budget in `COMPUTE_BUDGET_ESTIMATE.md`), then LoRA SFT at 4-bit; log loss curves; no RL until SFT passes Gate 3.
> 5. Significance by **paired bootstrap on CER difference** (seed 20260926, 1,000 resamples) — not the CER<0.5 McNemar bucket.
> Writes: `level2/w6/split_manifest.json` (train/val/test by document), `docs/campaign/FINETUNE_RESULT.md`. The untracked `src/` tree may be reused only after U3 is answered and Verdict reviews it.

## Reporting rules for anything that reaches Vinay
Every number states set, n, metric and GT tier; "our system ≈ 70 on Sarvam's bench" stays labelled ESTIMATE until §A runs; targets (pass 71.76 in five days; 79.35 stretch; 87.39 not this week) are targets, never predictions.

Related: [[proto-00-runbook]], [[proto-86-draft-plan-fixes]], [[proto-92-boss-decisions]], [[proto-99-concern-crosswalk]]
