---
name: proto-89-plan-v3-bodhan-base
description: "Added 2026-09-30 (Opus, \"new brain\") — PLAN V3 supersedes Plan v2's recogniser choice: build on Bodhan IndicOCR (84.94 on Sarvam's bench, open weights, commercial + fine-tune allowed with attribution, MLX 4-bit port runs on this Mac) instead of surya (69.96); fine-tune its 0.8B block recogniser locally where it trails Sarvam; strict no-leakage; command-level steps and gates"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T09:25:30.422Z
---

# PROTO-89 — PLAN V3: STAND ON THE STRONGEST OPEN MODEL, THEN SHARPEN IT WHERE IT LOSES

## Why v3 (verified 2026-09-30 — sources opened this day)
- **Market, same benchmark, run by Sarvam:** Sarvam 87.39 · **Bodhan Indic-OCR 84.94** · Gemini 3.6 Flash 79.35 · Google Cloud Vision 71.76 · surya 69.96 (https://www.sarvam.ai/blogs/sarvam-vision-2-1). Plan v2 was built on surya → a ~15-point handicap nobody had to accept.
- **Bodhan per language vs Sarvam (same page):** Kashmiri 48.04 vs 54.82 · Odia 75.45 vs 80.01 · Gujarati 83.26 vs 88.87 · Bengali 90.87 vs 93.47 · Hindi 90.99 vs 93.52 · Punjabi 86.51 vs 89.16 ·
  Manipuri 82.85 vs 85.12 · Konkani 95.99 vs 97.41 · **Santali 68.30 vs 53.91 (Bodhan ahead)**. Bodhan's own bench: 86.2 printed, 66.7 handwriting (https://huggingface.co/bodhan-ai/indic-ocr).
- **Model:** IndicDocLayout 33M (PP-DocLayoutV3/RT-DETR, blocks + reading order) + IndicBlockOCR 0.8B (Qwen3.5-0.8B, Sarvam-30B tokenizer); input = page images; output Markdown + block JSON; printed: English + all 22; handwriting: English + 12.
- **Licence (official card):** Indic Open Model License v1.0 — research, government, commercial use OK; fine-tuning and self-hosting OK; attribution "Built with [Model Name] from Bodhan AI / AI4Bharat"; derivatives under the same licence;
  **hosted APIs need written approval** (nonprofit/academic exempt); commercial licence only above 500M MAU or $250M revenue; prohibited-use list. → far safer than surya's $5M cap.
- **Runs here:** MLX ports of the block recogniser — 4-bit 636 MB, ~391 ms/crop; 8-bit 1.0 GB; bf16 1.6 GB (https://huggingface.co/hari31416/indic-ocr-mlx-4bit); port-reported CER 4.83% on its own test crops (not our data).
- **Trainable here:** mlx-vlm LoRA/QLoRA supports Qwen2/3/3.5-VL on Apple Silicon (`mlx_vlm` `lora.py`; dataset = HF dataset with `images` + `messages`; needs `mlx-vlm[train]`).
- **Already on disk but never used:** `docs/research/DEEP_RESEARCH_STRATEGY_2026-09-29.md` proposed "Bodhan base + targeted per-script SFT + RLVR". Keep its idea; REJECT its errors: licence stated as "Apache 2.0" (wrong), cloud budget $50–150 (breaks $0),
  "P(beat) ≈ 0.65" and "88.5–90.0 projected" (unsourced), and **RL on Sarvam's `small_representative` split** (evaluation leakage — never train or tune on any split of the benchmark we report on).

## The five days (Day 1 starts when the approvals below land). Each gate must pass before the next day.
| Day | Commands / work | Gate |
|---|---|---|
| 0 (today) | Boss/Vinay approve U23–U27 (proto-92): Bodhan weights, benchmark download, Bodhan written approval if the submission is a hosted API, optional Kashmiri data, optional HF MCP | approvals recorded |
| 1 · Bodhan baseline | §A below: run Bodhan on (a) our 300 human gold pairs (bn/hi/sa), (b) all 1,227 scored probe items, (c) Sarvam's `small_representative` (1,173) with the official `metrics.py`; 4-bit vs bf16 **per script, Perso-Arabic separately**; raw + Arabic-normalized CER for ur/ks/sd; Bodhan's handwriting languages ([[proto-100-research-to-build]] B-01, B-02, B-12) | Bodhan reproduces ~84.9 (±2) on (c) AND beats surya on (a) → Bodhan becomes the base; else fall back to Plan v2 (proto-87) |
| 2 · Training data | §B: mine block-level pairs — human pairs (bn/hi/sa/en) + official-PDF text blocks via PyMuPDF — split by source document, test items and near-duplicates removed | split manifest passes the Verdict leakage audit (mandela patterns 6/3/4/5) |
| 2.5 · Vinay's gates (Sep 29 D4 + D5) | Multi-LLM evaluation of Plan v3: the [[proto-17-w1f-multi-llm-eval]] method on `docs/PLAN.md` (OpenCode + a fresh Sonnet reviewer + a ChatGPT paste; judged "by the process, not by the AI"). Then the boss holds a 15–20 min cross-question session with Vinay on the DRAFT plan + flowchart (proto-100 B-16/B-17) | **no training before both** (Sep 29 red line: "No training before research validation"); outcome recorded as U-rows |
| 3 · Sharpen | §C: LoRA on IndicBlockOCR (mlx-vlm; base precision per proto-100 B-01 — bf16/8-bit for ks/ur/sd unless Day 1 proves 4-bit parity; Vinay's GPUs if U33) for the languages where Bodhan trails Sarvam most and we hold data; 5-item smoke test first | held-out-document CER drops on target languages; no language regresses > 1 point on our probe |
| 4 · Coverage + submission | Routing: Bodhan first; fallback engine — licence-cleared for shipping only (surya is evaluation-only, U14) — when a block fails the bad-output check; script read from Bodhan's output text by Unicode range (the IndicPhotoOCR script-ID has no sat/mni classes, RF-09); fixes from proto-82; timed dry run on 50 of the 5,344 test images (proto-78); test-set profile (proto-81); the official product outputs (proto-100 B-11: layout JSON, searchable PDF, per-block language detection, offline package — U35) | seconds/page fits the confirmed deadline |
| 5 · Proof | Re-score everything from scripts; full 6,909 test split with the official scorer (never trained on); attribution notice in outputs; write-up for Vinay | every number reproduces; licence notice present |

## §A — Bodhan baseline (Engine subagent) — writes `level2/unified/run_bodhan.py`, `docs/campaign/BODHAN_BASELINE.md`
> 1. Download (approved only): `bodhan-ai/indic-ocr` (layout + block recogniser; note any gating form) or, for speed, the MLX 4-bit block recogniser `hari31416/indic-ocr-mlx-4bit` + the 33M layout model; record revisions + sha256.
> 2. Load `sarvamai/indic-ocr-bench` `small_representative` (then `test` later); vendor `metrics.py` unchanged (hash it).
> 3. Run the page pipeline on our probe images and on bench blocks (bench items are already block crops → recogniser only). Time every item (s/page, s/crop).
> 4. Score: our items with `level2/probe22/metrics.py` (CER) per GT tier (proto-62); bench items with the official scorer (word accuracy macro over 22, English excluded).
> 5. Report beside surya and the published 84.94/87.39; per-language table; empty-output rate; speed. Label anything not reproduced.

## §B — Leak-free block-level training data (Engine builds, Verdict audits) — writes `level2/w6/split_manifest.json`, `docs/campaign/TRAIN_DATA_V3.md`
> Sources: official image–text pairs (bn ~2.9k, hi 3.5k, sa ~0.5k, en 3.5k) and official PDFs whose text layer passes our honesty gates (`extract_gt.py` gates; `candidates/<code>.json` pools), cut into blocks with
> PyMuPDF (`page.get_text("blocks")` → bbox + text; render the page at 200 dpi; crop each block) — block-level pairs match what the recogniser expects.
> Exclusions: every probe item and its source document; near-duplicates (perceptual hash + text overlap); anything from Sarvam's benchmark; the 5,344 test images; barred GT (§6.4) unless the boss reopens it (U6).
> Split by source document: train / val / held-out test per language. Report counts per language and the exclusion list.

## §C — Sharpen (Engine trains; Verdict verifies) — writes adapter + `docs/campaign/FINETUNE_V3.md`
> Target order (largest Bodhan-vs-Sarvam gap × data we hold): Bengali, Hindi (human pairs), then PDF-layer languages among Gujarati, Odia, Punjabi, Konkani where §B yields enough clean blocks;
> Kashmiri only if the boss approves the 600K-KS-OCR download (CC-BY-4.0, 10.6 GB, word images). LoRA on the base chosen by proto-100 B-01 (never 4-bit for ks/ur/sd without Day-1 parity): rank 16, alpha 32, lr 2e-4, 1–2 epochs, grad checkpointing; smoke test 5 items first; watch memory.
> Evaluate on held-out documents + our probe; paired bootstrap on CER. RL (GRPO, reward = 1 − CER on OUR training pool) only if SFT passes Gate 3 and time remains.

## What this does NOT do
No cloud GPUs, no Sarvam calls, no training on any benchmark split or test image, no novel backbone (Bodhan is an existing model — this is the boss's hybrid-integration approach (proto-103 S5), which the lead accepted), no claim before Day 5 numbers exist.

Related: [[proto-100-research-to-build]], [[proto-87-plan-v2-execution]], [[proto-94-tool-integration]], [[proto-92-boss-decisions]], [[proto-83-licence-verification]], [[proto-62-gt-tier-stratified-reporting]]
