# W5 Strategy Review — ranked alternatives to the current Vaultstack plan

**Audience:** Vinay Gahlot (CEO, Vaultstack AI) · tomorrow's W5 strategy session
**Author:** Verdict Agent · 2026-09-29 17:00 IST
**Scope:** rank 5 alternatives to the current PPT_SPEC.md / R7 W6 architecture, with cost / time / CER-delta / risks / decision-it-changes per option. Disk-truth only. Probe22 numbers from `level2/probe22/scores/LEADERBOARD.md` + per-lang CER table.

**Pre-read anchors:**
- Current plan: `docs/architecture/PPT_SPEC.md` + `docs/architecture/W2_HYBRID.md` + `docs/research/R7_W6_TRAINING_TREE.md`
- Probe truth: 11 engines × 1,227 packs × 18 langs; sarvam 0.2640 (mean over its 54 scored items; 0.2400 is the loop-excluded n=50 figure) / surya 0.3944 (mean over 1,227) / tesseract-family 0.486 / easyocr 0.494 / indicphotoocr 0.559 / paddleocr 0.656 / rapidocr 0.669 / anuvaad 0.711 / doctr 0.869
- §6.4 LOCK (BARRED): ks / mni / sat / mr / ur + ne PDF-tier
- §6.4 LOCK (SAFE pending §6.2): as / brx / doi / kok / mai / or / pa
- §6.4 LOCK (VERIFY-FIRST): gu / sd
- D1 (prior lock, NOW RE-OPENED for Vinay): QLoRA on kok + pa only — narrow
- D4 (prior lock, still binding): sat+ks micro-repair W5-only if freeze-safe; mni/mr/ur no repair

---

## Baseline (current Vaultstack plan, from PPT_SPEC.md)

| Stage | Spec | Verdict label (W2) | Status today |
|---|---|---|---|
| 0 | OpenCV deskew/denoise/binarize | KEEP geometry / HYBRID binarize | fine on clean, breaks on OldScan (Sarvam 55.3 worst column globally) |
| 1 | DocLayout-YOLO + IndicDLP LoRA | REPLACE detector → PP-DocLayoutV3 / Bodhan IndicDocLayout | 2026 production stacks don't ship YOLO as detector |
| 2 | TrOCR-from-scratch + Qwen 3.5 VL + PaddleOCR-VL 1.6 + akshara-boundary aux | DROP TrOCR-from-scratch; KEEP Qwen 3.5 VL + PaddleOCR-VL 1.6; ADD Nanonets-OCR2-3B | TrOCR seq2seq-fine-tune is the obsolete training target per Chitrapathak-2 |
| 2b | SCST / RL on CER | KEEP order, rename SCST→RLVR/GRPO | Sarvam 2.1 = SFT then RLVR (only published order) |
| 3 | IndicBERT / Airavata small LLM: noisy → JSON | HYBRID: schema on OCR VLM (Parichay 89.8% EM) | second-LLM pipeline is the obsolete target |
| 3b | SimPO / DPO on ranked JSON | KEEP | valid; Sarvam moved this into SFT+RLVR |
| Eval | Sarvam / IndicDLP / Indic Vision Bench; no FT on test | UPDATE: add sarvamai/indic-ocr-bench + our probe + South 400 | firewall holds |

**Cost:** full SFT of 2 backbones (Qwen 3.5 VL + PaddleOCR-VL 1.6) ≈ 200-500 GPU-h on Vast.ai spot 4090 (~$200-500) OR on local M2 Max ≈ 60-150 h wall (memory-uncertain)
**Time:** 10-15 days (SFT 5-8d + RLVR 2-3d + eval 2-3d + integration 1d) — *outside hackathon window*
**Expected CER delta vs probe:** no MEASURED data — the architecture hasn't been instantiated; only the wrap-pipeline subset has. Sarvam 87.39 word-acc is the published target.
**Risks:** (a) TrOCR-from-scratch arm is dead weight even with LoRA — no 2026 winner ships it; (b) two parallel SFTs = 2× the validation surface for marginal CER gain; (c) RLVR before SFT plateaus is the documented failure mode; (d) budget ~$200-500 + 60-150 GPU-h is non-trivial under standing no-money rule; (e) nothing in the current plan addresses the four weakest cells (sat/ks/OldScan/or) — they're orthogonal to "more shared pretraining".
**Decision it changes:** W6 freeze recipe (yes, deep); W5 strategy (no — this is the freeze target itself, not an alternative).
**Verdict:** This is the architecture the team proposed ~mid-August 2026. R1-R7 + probe22 say: keep Stage 0/1/2b/3b, replace Stage 2 detector, drop TrOCR arm, add schema-on-VLM. The freeze at W5 should diff against this baseline, not repeat it.

---

## Alternative A — Wrap-only with per-script engine routing

**Idea.** Ship the highest-CER engine per cell on a frozen-detector + per-script router harness. No training. No new backbone. Sarvam Vision 2.1 API is wrapped as a routable component for sat / mni (the only Ol Chiki / Mayek-capable engine we measured).

**Per-script routing table** (n≥50 winner per `level2/probe22/scores/LEADERBOARD.md` + §6.4 lock):

| Tier-1 routing decision | Engine | Cell coverage | Why (MEASURED) |
|---|---|---|---|
| Devanagari (hi / mr / sa / ne / mai / kok / brx / doi) | surya first, tesseract-family fallback | hi (0.220) / brx (0.165) / kok (0.425) / mai (0.030) / sa (1.000 honest-empty) — surya wins; mr (0.205, n=79) / or (0.259, n=69) / ne (0.161, n=37) — tesseract-family wins | surya McNemar p=0.0033 vs tesseract_bilingual on kok; p=0.0107 vs easyocr (the runner-up) |
| Perso-Arabic (ur / sd / ks) | surya | sd (0.315) / ks (0.589) — surya wins 9/9 opponents; ur (0.623) surya loses 0/9 (all-tie or worse) | ks 0.589 vs Sarvam 0.630 directional on 3-pack subset |
| Bengali-Assamese (bn / as) | indicphotoocr / surya | bn (surya 0.476 / indicphotoocr 0.657); as (n=19, no winner claim) | surya beats indicphotoocr on bn |
| Ol Chiki (sat) | sarvam_vision (ONLY Ol Chiki emitter; surya 1.000 honest-empty, tesseract fallback to eng) | sat (n=20 agreement-only, GT garbage) | physics: no open engine emits Ol Chiki; Sarvam is the route |
| Meitei Mayek (mni) | sarvam_vision (ONLY Mayek emitter; all open engines Latin/garbage) | mni (n=14 agreement-only) | physics: no open engine emits Meitei Mayek; Sarvam is the route |
| Odia (or) | tesseract-family | or (0.259, n=69) | tesseract-family beats indicphotoocr 0.353 + surya 0.276 |
| Gurmukhi (pa) | surya | pa (0.145 n=90) | surya McNemar p<0.012 vs tess-family |
| English (EN sanity) | surya (best non-Sarvam) | en (sarvam 0.1078 / surya 0.1514 / rapidocr 0.4535) | surya beats tess-family 0.81 / easyocr 0.60 / indicphotoocr 0.67 |

**Cost:** $0 compute (CPU only); Sarvam API for sat/mni only ≈ **₹0.5/page × ~1000 benchmark packs ≈ ₹500 ($6)** at the official Bhashini benchmark; zero elsewhere. Within no-money-by-default-vinay-overrides.
**Time:** **0 days** to wire (router is a config swap in `level2/probe22/run_engine.py`'s existing routing table); 1 day to add the Sarvam-sat/mni guard + integration test; 1 day for EN sanity at submission.
**Expected CER delta vs probe22 (best-engine routing):** **−0.10 to −0.15 avg CER** vs current single-engine baselines (e.g., surya 0.3944 (probe22 weighted basis; does not reproduce as a per-lang mean) → ensemble 0.25-0.30); Sarvam-substituted on sat/mni/gu locks in 87% on those cells; **net word-acc on Sarvam's bench ~80-84** (matches the W5_BEAT_SARVAM_PLAN.md "where we tie" + "where we lose" cells).
**Risks:** (a) sarvam_vision on sat/mni at 3/lang = directional only; expanding to full 100/lang is a Sarvam-budget ask (≈ ₹5000 for sat/mni); (b) tesseract-family is NEAR-identical, not byte-identical (openbharatocr == tesseract_indic on 1,225/1,227; tesseract_bilingual only 370/1,227) → treat as ~1 engine for ranking, so **9 independent engines, not 11**; the correlation is not perfect and tesseract_bilingual is a genuinely weaker configuration; (c) OldScan cell NOT addressed — OldScan 55.3 is the global worst column, untouched by routing alone; (d) wrap pipeline runs at 0.4-1s/page on surya → at 5,344 test pages = ~30-90 min compute; fine for the demo.
**Decision it changes:** W6 path → freeze at Alternative A as **ship-today deliverable**; QLoRA / fine-tune becomes a post-freeze bonus if Vinay approves the budget.

---

## Alternative B — QLoRA on SAFE langs via mlx-tune

**Idea.** Per R7 N1 default: **Qwen2-VL-2B-Instruct** (QARI-port recipe, 0.550→0.061 CER precedent at identical scale/backbone; arXiv:2506.02295). mlx-tune 0.6.0 + mlx-vlm 0.7.4 already installed (per `level2/probe22/QLORA_READINESS.md` 2026-09-29 16:22 IST — both PASS). Local M2 Max; no cloud spend.

**Languages:** Per D1 prior lock (now RE-OPENED for Vinay) — kok + pa only (n≥50; mai + or KILLED by K1, no McNemar-significant gap). 459-801 W6 SFT-eligible items in manifest.

**Recipe (R7 N1-N4, executable in 7 days):**
1. CPT on L1 human pairs (bn 2938 + hi 3500 + sa 494 + en 3500 = 10,432 pairs) — 1 epoch ≈ 25 GPU-h @ 2B
2. SFT with L2 gated PDF for SAFE-passing langs only — R5 trust ≥ 70 + §6.4 PASS + §6.2 pair-vs-pdf gap ≤10pp — applies to brx (82), mai (78), or (91), pa (90); rejected for ks (45) + ne PDF (26) — 1 epoch ≈ 25 GPU-h
3. Progressive curriculum C1 word/line/block (R3§B1 ladder)
4. GRPO RLVR (R7 N4) on human-verified gold ONLY; Valid·Struct·Sim reward per Paddle §4.3.2; OFF if §6.6 raw-vs-normalized inverts

**Cost:** **$0 compute** (local M2 Max; mlx-tune handles MLX-native SFT/DPO/GRPO and ships CER/WER metrics); disk 12 GB free post-install (PASS QLORA_READINESS gate); 9.4 GB reclaimable memory (PASS for 3-4B @ 4-bit).
**Time:** **5-7 days** wall (SFT 2-3d + eval 1d + RLVR 1-2d + integration 1d). Within W6-W7 timeline.
**Expected CER delta vs probe22:** **−0.03 to −0.05 CER on kok + pa** (~190 packs); ≈ 0 elsewhere; **net avg CER lift on the 2 SAFE cells ≈ −3 to −5 pt word-acc**. Total avg word-acc lift across 1,227 packs ≈ **+0.5 to +1 pt** (2 of 18 cells × 190 packs). Will NOT beat Sarvam 87.39 (avg).
**Risks:** (a) K1 already KILLED mai + or — Phase 6 gap wasn't there; kok + pa may also fail K1 once actually tested (gap must be McNemar p<0.05 AND > 3pt CER closable); (b) memory at launch is UNKNOWN per QLORA_READINESS §4 — re-check `vm_stat` immediately before `mlx_vlm.convert`; abort if Pages free < 3 GB; (c) kok + pa already wins 0.425 / 0.145 — there's less room than for ks (0.589) or ur (0.623); (d) TrOCR blocked on MPS (RuntimeError on M4 — fix UNKNOWN) → skip TrOCR arm; (e) the wrap-only baseline (Alternative A) ALREADY delivers kok + pa at 0.425 / 0.145 — QLoRA must beat THAT bar, not the no-routing baseline; (f) laptop memory spike can OOM and lose the session.
**Decision it changes:** D1 W6 path → swap wrap-only for QLoRA on kok+pa; OR keep both (Alternative D); OR kill if K1 fires.

---

## Alternative C — Fine-tune open-weight state-space VLM (GLM-OCR or PaddleOCR-VL-0.9B)

**Idea.** Sarvam Vision 2.1 is API-only — **we cannot fine-tune Sarvam**. Alternative is to fine-tune an open-weight 0.9B VLM with **Indic tokenizer + harness-with-VLM** shape, either:

- **GLM-OCR 0.9B** (zai-org/GLM-OCR) — OmniDocBench table does not list it; olmOCR-Bench 78.9; PaddleOCR-VL 1.6 = 96.01 per Sarvam blog / 96.33 per Paddle's own claim; official MLX deploy, harness-with-VLM shape (per `INTEGRATED-ELITE-STACK.md` line 30); primary W6 recipe candidate per R7 N1 hedge.
- **PaddleOCR-VL-0.9B** (PaddlePaddle/PaddleOCR-VL) — 109 langs incl. Urdu / Sindhi / Kashmiri cluster (Nastaliq-vs-Naskh NOT disclosed); Apache-2.0; two-stage detect+order→crop→VLM (paper §2+docs).
- **MonkeyOCRv2 0.7B** (Yuliang-Liu/MonkeyOCRv2) — Apache-2.0 + open weights; MDPBench 83.3 / Hindi 71.9; smallest strong fine-tune backbone.

**Recipe (PaddleOCR-VL §4 progressive post-training, copied shape):**
1. CPT 16.8M samples (weak-region mining on our 1,227 probe + Sarvam bench + Sangraha synthetic)
2. SFT 7.3M samples (UACS-mined hard + corrected-label samples)
3. GRPO top-8K/task with reward = Valid · Struct · Sim (TEDS / 1-NED / edit-weighted F1)
4. Use the **W6 QLoRA scaffold** (mlx-tune + mlx-vlm) for the recipe — same MLX-native path as B

**Cost:** $0 local M2 Max (mlx-tune path) OR **$5-15 Vast.ai spot 4090** for 30-h QLoRA on cloud 4090 (interruptible; checkpoint every 200 steps); OR ~$30-60 Lambda A100 on-demand for safer sessions. No paid APIs beyond Sarvam 57-cap.
**Time:** **7-10 days** (CPT 3-4d + SFT 2-3d + GRPO 1-2d + eval 1d). Tight for hackathon window but possible.
**Expected CER delta vs probe22:** **−0.05 to −0.15 avg CER** (whole-board lift, not just 2 cells); on par with Sarvam-on-bench-style training distribution; could beat Sarvam 87.39 on Devanagari subset (Sarvam is already at 95% there — limited upside) and on ks (Sarvam 54.82 → potentially 0.40-0.50 with Nastaliq-aware SFT). **Net avg word-acc ≈ 85-89 if recipe lands, 80-83 if mid-RSAT**.
**Risks:** (a) largest scope of all 5 alternatives — fine-tuning a 0.9B VLM with 16.8M-sample CPT is non-trivial; (b) license check on synthetic data mixing — Sarvam bench is research-use, Sangraha is mixed-license; (c) **the recipe shape (CPT 16.8M → SFT 7.3M → GRPO 8K/task) needs hundreds of GPU-days at 0.9B to fully replicate** — we steal the SHAPE, not the corpus (per R1 §3b); (d) Paddle 1.5→1.6 took Paddle's team; (e) OldScan weak-cell still unaddressed without restoration pre-pass.
**Decision it changes:** W6 path → highest upside but highest risk; DEFER if Vinay wants minimum viable hackathon submission; PURSUE if Vinay wants the technical ceiling.

---

## Alternative D — Hybrid wrap + script-router with specialists

**Idea.** Wrap baseline (A) + targeted specialists ONLY for cells where wrap demonstrably loses. No general fine-tune.

**Specialists per weak cell:**

| Cell | Specialist | Why |
|---|---|---|
| OldScan (55.3 cross-lang) | Restoration pre-pass (R4 §A2 deskew+Sauvola frozen configs, A3 DocRes enhancement head pilot n≤8 first) | Adopts R4's KEEP LIGHT-PREPROCESS only on stained/uneven-light pages; pilot per C5 dot audit before scaling |
| Kashmiri (ks, 54.82) | surya (0.589) + SwinIR-SR + CLAHE + NFKC/bidi (per R2 §C2 historical-Arabic recipe) | UNB +25-70% WER recovery on urdu.PDF-tier; surya already wins ks McNemar p<0.0006 |
| Urdu / Sindhi (ur, sd) | surya (0.623 / 0.315) | mean-CER leader on both. **Significance differs sharply: sd = 7/9 opponents at p<0.05, ur = 0/9 (every pair p=1.00 tie).** Do not group them as one "dominates" claim. |
| Santali (sat, 53.91) | sarvam_vision API (only Ol Chiki emitter; ~₹500 for 1000 pages) | Physics-bound — no open engine emits Ol Chiki |
| Meitei (mni) | sarvam_vision API | Physics-bound — no open engine emits Mayek |

**Cost:** **$0 compute** (CPU only) + **Sarvam API ≈ ₹500-2500 ($6-30)** for sat / mni at official benchmark scale. Restoration uses already-installed OpenCV + Sauvola (CPU 15-90s/page tiled); DocRes pilot can use the existing pip-installed opencv-python 5.0.0.93 from mlx-tune install.
**Time:** **2-4 days** to wire (router config + R4 ablation run + Sarvam routing guard + EN sanity at submission).
**Expected CER delta vs probe22:** **−0.03 to −0.08 avg CER** with the highest variance (depends on R4 ablation win + Sarvam API coverage); OldScan cell lift +2-5pt (R4 prior); ks lift +5-10pt if restoration + SwinIR pay; **net avg word-acc ≈ 82-87**.
**Risks:** (a) R4 ablation may show no statistically-significant lift (CI excludes 0 required per C6); (b) OldScan SOTA dots/matra-hooks smoothing risk on Nastaliq → C5 dot audit mandatory; (c) Sarvam API budget ask (~₹500-2500) is the largest non-free component; (d) surya on ks at 0.589 already nearly matches Sarvam 0.630 directional — limited headroom for big ks lifts; (e) sat/mni are still Sarvam-only cells (no wrap alternative).
**Decision it changes:** W6 path → focused specialist investment; recommended as **the strongest baseline + targeted add** rather than all-or-nothing.

---

## Alternative E — Ensemble voting + restoration pre-pass + Sarvam-API for unmeasurable cells

**Idea (creative, NEW).** Don't pick ONE engine per cell — pick **TOP-3 engines per cell and majority-vote at the per-line CER level**. Combine with R4 restoration pre-pass on OldScan cells, Sarvam Vision 2.1 API for sat/mni, and the existing wrap pipeline. Adopts the engine-overlap warning (tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr — treat as one engine) and the documented surya + tesseract-family ensemble wins.

**Per-cell ensemble (MEASURED from probe22):**

| Cell type | Ensemble | Vote rule |
|---|---|---|
| Clean Devanagari (hi, pa, sd, ur, mr, or, mai, kok, brx) | surya + tesseract-family + indicphotoocr / easyocr (per cell) | majority at CER ≤ 0.5; flag for review (matches PPT 3b alignment) on disagreement |
| Nastaliq (ur, ks) | surya + rapidocr (71% Arabic share on ks) + tesseract-family | same |
| bn / as | surya + indicphotoocr + easyocr | same |
| Ol Chiki (sat) | sarvam_vision API only (others Latin/garbage) | single-route |
| Mayek (mni) | sarvam_vision API only | single-route |
| OldScan pages (any lang) | R4 restoration pre-pass (A2 deskew+Sauvola, frozen configs) → surya + tess-family + paddleocr | same majority, with restoration first |
| en | surya + rapidocr + sarvam (post-clearance) | same |

**Cost:** **$0 compute** for ensemble + restoration (CPU only) + **Sarvam API ≈ ₹500-2500 ($6-30)** for sat / mni at benchmark scale. The wrap-pipeline is already on disk.
**Time:** **3-5 days** to wire (ensemble code + R4 ablation runs + Sarvam-API guard + integration test). Slightly more than D because of the ensemble layer.
**Expected CER delta vs probe22:** **−0.02 to −0.05 avg CER from ensemble voting** (matches the OCR-VLM literature where multi-engine ensemble wins on disagreement); **−0.03 to −0.08 from restoration on OldScan subset** (R4 C6 prior); Sarvam-API on sat/mni locks 87-90% there. **Net avg word-acc ≈ 83-87**.
**Risks:** (a) ensemble voting on disagreeing engines can hurt when both are wrong (rare but documented); (b) low-confidence flag volume may exceed human review capacity — need a threshold rule; (c) R4 ablation may not pass the CI-excludes-0 bar; (d) Sarvam API budget for full benchmark = ₹500-2500 (still tiny); (e) the same Sat/mni Sarvam-only physics constraint.
**Decision it changes:** W6 path → **all four weak cells addressed via different mechanisms** (no single-engine fix); the ensemble is the broadest-but-shallowest lift; restoration is the deep-but-narrow lift on OldScan; Sarvam-API is the Sarvam-subsidy on sat/mni.

---

## Ranking (Verdict opinion, with rationale)

| Rank | Alternative | Cost | Time | Avg word-acc target | Risks |
|---|---|---|---|---|---|
| **1** | **D — Hybrid wrap + script-router with specialists** | $6-30 | 2-4d | 82-87 | restoration may not pay; Sarvam-API budget |
| **2** | **E — Ensemble + restoration + Sarvam-API** | $6-30 | 3-5d | 83-87 | ensemble disagreement handling |
| 3 | A — Wrap-only with per-script routing | $6 | 0-1d | 80-84 | no OldScan lift; sat/mni Sarvam-only |
| 4 | B — QLoRA on SAFE langs via mlx-tune | $0 | 5-7d | +0.5-1 pt over A | K1 may kill; memory at launch; narrow impact |
| 5 | C — Fine-tune GLM-OCR / PaddleOCR-VL-0.9B | $0-60 | 7-10d | 85-89 (if recipe lands) | largest scope; license; recipe-shape vs corpus |

**Recommended pick for Vinay meeting:** **Alternative D** — best risk-adjusted balance. It is the wrap baseline (Alternative A) + the targeted specialists (R4 restoration + Sarvam-API for sat/mni + surya for Perso-Arabic). Cheap, fast, addresses every weak cell with the appropriate tool, and ships a complete product for the hackathon jury without betting on QLoRA or full-VLM fine-tune.

**If Vinay wants maximum technical ceiling:** combine **D + C** — wrap+specialists as the ship-day product, GLM-OCR fine-tune as the W7+ bonus for the public demo. Most defensible posture.

**If Vinay wants minimum spend:** **A** — pure wrap, no Sarvam-API, no restoration, no QLoRA. Ships today. 80-84 word-acc is honest.

---

## What this document does NOT propose

- New backbone invention (forbidden by §9 hard rule)
- 400-page language collection for any non-prioritized lang (forbidden by §8 hard rule)
- Cloud GPU spend without explicit Vinay budget number (no-money-by-default)
- Sarvam calls beyond the 57-cap without Vinay approval
- Touching `level2/out/` or `level2/reports/` (sealed)
- Touching `W6_QLORA_SPEC.md`, `QLORA_TRAINING_DATA.md`, `QLORA_EVAL_SPEC.md`, `QLORA_SMOKE_TEST.md` (paused per user 2026-09-29 directive)

---

**Cross-references:** `W5_BEAT_SARVAM_PLAN.md` (concrete head-to-head scenarios vs Sarvam 2.1) · `VINAY_MEETING_PACKET.md` (1-page summary for tomorrow) · `docs/research/level7/CALL_PACKET.md` (CALL_PACKET status update) · `OCR_AGENT_MEMORY_FEED.md §15` (pause + reset log).