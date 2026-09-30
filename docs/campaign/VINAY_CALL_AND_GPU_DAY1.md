---
name: proto-106-vinay-call-and-gpu-day1
description: "Added 2026-09-30 ~23:40 by the planner — (1) the brief for the Vinay call on 2026-10-01 morning: agenda, Plan v3 in 5 lines, what we ask, what we must NOT claim; (2) the GPU day-1 plan for the 24 GB SSH box: order, portability, data rules, no training before Gate 2.5; (3) HF token handling"
metadata:
  node_type: memory
  type: project
---

# PROTO-106 — VINAY CALL (2026-10-01 morning) + GPU DAY-1 PLAN

Law above this file: proto-104 rev 4 → proto-01 → boss-rules. Quotes to Vinay only from PRIMARY rows (proto-103 §0) or W4.md lines with commands.

## 1. The call — 20 minutes, the boss speaks, lists only
### 1.1 Opening (1 min)
- "We followed your process: research → Consensus (3 searches) → a draft plan → multi-LLM review → this session → then execute." (L1, L2, L12)
- "No training has started." (red line L10/L12)

### 1.2 Plan v3 in five lines (5 min) — show the flowchart from `docs/campaign/DRAFT_RESEARCH_PLAN.md` (step G) if Agent 2 has it; else say these lines
1. **Base = Bodhan** (the strongest open Indic OCR, 84.94 on Sarvam's bench) — layout (IndicDocLayout) + block OCR (Qwen3.5-0.8B).
2. **Your PPT stages kept, each with a stronger part:** Stage 1 layout → Bodhan layout; Stage 2 VLM SFT → Bodhan + LoRA; Stage 2b RL on CER → GRPO, last and optional; Stage 3 LLM → JSON → post-correction (B-18) + our JSON/PDF writer.
3. **One fair benchmark, all 22 languages + English:** 1,683 items, South (ta/te/kn/ml) now merged; GT tiers reported separately, never pooled.
4. **Handwriting is the centre:** the official test set is 5,344 handwritten word crops (we viewed samples); a labelled handwriting slice + a handwriting LoRA (B-19) follow.
5. **Portable product:** PyTorch/CUDA/CPU, Docker; MLX only as a Mac speed-up.

### 1.3 Honest status (3 min) — only lines that have a W4.md command
- Benchmark v2 built (1,683 items); first South score: tesseract CER 0.145.
- Bodhan weights: access pending (HF gate), run starts the moment it opens.
- Sarvam: 12 South calls on free credit; outputs being retrieved; ₹67 credit left.
- NOT to say: any "we beat Sarvam" line (R-12 needs the independent set too); any number without a command; the other session's Sarvam South numbers (wrong, F78); the Sep-25 meeting date (contradiction open).

### 1.4 Questions for Vinay (8 min) — each one changes a decision
1. **GPU:** SSH user/host/port; how long we keep it; storage quota; may we copy the official data + benchmark onto it (data by rsync, never GitHub)? any data that must not leave your machine?
2. **Training gate:** after this session, may we start LoRA on Bodhan (train split only, leak-audited) — or do you want the multi-LLM review of the v3 draft first (Gate 2.5)?
3. **The official test set:** is it only handwritten words? which languages/scripts? is there a labelled dev split, or will one come? what is the submission format (per-image text? JSON? language tag)?
4. **Metric:** does the jury score accuracy at all, or only the product criteria (approach, feasibility, roadmap, market)? CER, WER or word accuracy?
5. **Bodhan licence:** Bodhan §3.1 needs approval to host its weights — can the registered company request it, or do we ship "download from the official repo"?
6. **"No clear communication… expect 10 days":** what is it about — Bhashini/ULCA data, or the hackathon organisers? What should we not wait for?
7. **Sep-16 package:** we owe a correction (26/126 CER pages had legacy-font GT; ₹100 was free credit, not price) — do you want it in writing? (only if Agent 2 has reproduced it)

### 1.5 Close (3 min)
- Book the 15–20 min cross-question session (L12) on the written v3 draft, with a date.
- Confirm: nothing trains before that session.
- Read back the decisions; the boss writes them to proto-92 as U-rows the same day.

## 2. GPU day-1 plan (24 GB VRAM, SSH) — Agent 1 runs, Agent 2 verifies
### 2.1 Before touching the box
- SSH key/password only in env vars on the server and in the Mac's `.env` (git-ignored). Never in chat logs, W4.md, the repo.
- Record in W4.md: `nvidia-smi` (GPU model, driver, CUDA), `df -h`, `free -g`, OS, Python.

### 2.2 Setup (≤ 1 h)
1. Code: `git clone` of the repo (code only).
2. Data: `rsync` from the Mac of exactly `level2/benchmark/` (manifest_v2 + pages + pipeline) and the Sarvam bench test split. Never `Datasets/` raw unless Vinay said yes (question 1). sha manifest checked on both sides.
3. Env: a `.venv311`-equivalent (Python 3.11) with CUDA builds of torch/transformers + `product/requirements.txt` (Agent 3's file). Log `pip freeze` to `level2/benchmark/logs/RUN_STATE/gpu-24gb_env.txt`.
4. HF token from env var `HF_TOKEN` (never in files).

### 2.3 Run order (each job resumable, R-15 rules, output tagged `device=gpu-24gb`)
1. **Continuity check:** 1 item per language per engine already run on the Mac → diff → W4.md. No other job before this passes.
2. **D1 on CUDA:** official `bodhan-ai/indic-ocr` on the PyTorch path — `--sample 100 --pair-only` → full manifest_v2 → `BODHAN_BASELINE.md` (tiered, R-12). MLX-vs-PyTorch parity number from the Mac run logged.
3. **H3:** Bodhan + surya + Tesseract on the handwriting slice (after H2).
4. **X:** Bodhan + paddle on the Sarvam bench test split (6,909), labelled "home bench"; never counted together with the 400 South items.
5. **Latency table:** one machine, s/page per engine, × 5,344 = the submission time budget.
6. **Downloads needing the boss's go:** dots.ocr, PaddleOCR-VL — list sizes first.
7. **NOT on day 1:** any LoRA/SFT/RL (Gate 2.5 + the Vinay session first), any Sarvam call.

### 2.4 Done-when (day 1)
- Continuity PASS + Bodhan 100-sample baseline on CUDA + env frozen — each with its command in W4.md.

## 3. HF token (boss, 2026-09-30 ~23:30)
- The boss gave the Maya0769 token in chat. Stored ONLY in the Mac `.env` (git-ignored) + `hf auth login` by Agent 2; never in memory files, the repo, W4.md or any branch.
- The gated-model access forms need the browser (no API); the token only works after the forms are accepted.
- Rotate the token after Bodhan downloads (it sits in a chat log).
- The cloud planner cannot reach huggingface.co (network policy: CONNECT rejected) — all HF work is on the Mac or the GPU box.
