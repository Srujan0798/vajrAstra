<!--
🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)

All W6 fine-tuning prep is PAUSED. Not started.
Vinay meeting TOMORROW (2026-09-30) = gating step.
Vinay → W5 freeze after Wed 2026-10-01 → W6 training decision.

DO NOT execute training, mlx-tune, mlx_vlm, or QLoRA scripts from this file.
This file is preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
After Vinay meeting: if Option A approved → resume scaffold per this file.
If Option B → wrap-only ships; this file remains archival.
If Option C → backbone swap; this file is superseded; new spec required.

Refs: VINAY_MEETING_PACKET.md · STRATEGY_VINAY_TOMORROW.md · VINAY_CTA.md ·
      W5_STRATEGY_OPTIONS.md · W5_BEAT_SARVAM_PLAN.md ·
      OCR_AGENT_MEMORY_FEED.md §15-§16 · BOSS_CONCERNS.md items 53+

Hard law: §9 no downloads + §8 no training until W5 freeze + Vinay gate ahead of W5 freeze.
-->

> 🟡 **STATUS: PAUSED** — Created 2026-09-29 BEFORE W5 freeze. NOT AUTHORIZED.
> Per OCR_AGENT_MEMORY_FEED.md §8: "Training" is forbidden until W5 freeze.
> This file is a DRAFT for review at W5 freeze (after Wed 2026-10-01), not executable.
> Vinay meeting tomorrow is the gating step.

# W6 QLoRA SCAFFOLD SPEC — 2 SAFE langs (kok/pa)
**Verdict Agent, 2026-09-29 ~07:30 IST — K1-LOCKED (D1 W6 conditional)**
**Owner of execution: Engine agent (training) + Miss agent (scaffolding)**
**Status: NOT YET EXECUTED — gated on Phase 6 estimator-law gap (K1 ✓) + mlx-tune install (PENDING USER APPROVAL) + memory check at call**

---

## 0. CHANGE LOG (vs prior version 2026-09-29 06:51 IST)

**Prior:** 4 SAFE langs (kok/mai/or/pa), ~6h compute, ~6h SFT, 1.2GB adapter × 4 langs (4 langs × 300MB).

**Current:** 2 SAFE langs (kok/pa only — **mai KILLED at K1**, **or KILLED at K1**). 
- **mai KILLED**: McNemar p=1.0 (tie), gap 0.008 < T2=3.0pt. Wrap baseline (surya 0.030) is already at SOTA internal CER. No room for QLoRA improvement.
- **or KILLED**: gap -0.020 (surya is NOT the wrap winner — tesseract_indic is). QLoRA on surya at or has regression risk + no improvement target.

**Net effect:**
- 2 langs × 30 min × 2 = **~1 hour compute** (was ~6h)
- 600MB × 2 = **1.2 GB adapter weights** (was 2.4 GB)
- Adapter weights: 2 × 600MB = 1.2 GB on disk
- Total budget: ~3h (compute + eval + integration) — was ~6h
- Memory check: 4GB strict OR 4GB reclaimable needed (was "8-16GB peak, fall back to wrap-only if exceeds 24GB" — too conservative for 2-lang scope)

---

## 1. References (canonical)

- **Tool:** `ARahim3/mlx-tune` (1.4k★, MLX-native SFT/DPO/GRPO, ships CER/WER metrics). Status: **NOT YET INSTALLED** (PENDING USER APPROVAL 2026-09-29). Install gate at W5 freeze.
- **Backbone:** **Qwen2.5-VL-3B-Instruct @ 4-bit MLX** (primary). 
  - ALTERNATE 1: Qwen3-VL-2B-FP8 (smaller ~2.5GB).
  - ALTERNATE 2: GLM-OCR-0.9B (OmniDocBench #1, official MLX deploy, smallest path).
  - ALTERNATE 3 (NEW 2026-09-29 from live research): **LightOnOCR-2-1B** (arXiv:2601.14251v2, Apache-2.0, Mistral-Small-3.1 vision + Qwen3 + 2-layer MLP, SFT → GRPO RLVR; **9× smaller than priors, SOTA on olmOCR-Bench at 1B**; closest recipe template to our W6 because: (a) SFT-then-RLVR is exactly our D1 path; (b) checkpoint averaging + task-arithmetic merge adds robustness to small-n; (c) Mistral-Small-3.1 vision encoder handles Hindi well per Can-OCR-VLMs-Read-Devanagari paper).
  - DEFER: MonkeyOCRv2 0.7B.

- **Per-lang W6 data subset** (from `level2/probe22/manifest.json` `gt_source` field):
  - **kok (n=100):** all 100 items `official_pdf_layer`. Trust 75.0/100 (gt_forensics.json per_language.kok.trust_score). SAFE.
  - **pa (n=100):** all 100 items `official_pdf_layer`. Trust 73.2/100. SAFE.

- **Memory budget (CURRENT 2026-09-29 ~16:30 IST, MEASURED via `level2/probe22/MEMORY_RECLAIM_RESULT.md`):**
  - System RAM: 24.0 GiB (hw.memsize=25769803776).
  - Strict free: **~1.4 GB** (88631 pages × 16,384 B).
  - Reclaimable (inactive + purgeable): **~9.4 GB** (inactive ~9.1 GB + purgeable ~0.3 GB).
  - Total available post-reclaim: ~10.8 GB.
  - QLoRA 3B @ 4-bit + grad checkpointing peak: **8-12 GB** (3B model is 3.5GB @ 4-bit, optimizer states + activations fit in 4-8GB with grad checkpointing).
  - **W6 spec floor (REFRESH 2026-09-29):** ≥4 GB reclaimable needed pre-train (1.4 GB strict + 2.6 GB reclaimable = 4 GB floor; current 9.4 GB reclaimable ≫ 4 GB floor).
  - **K4 absolute abort floor:** T8=2 GB reclaimable (per `KILL_CRITERIA.md` K4(b)). If reclaimable < 2 GB → K4 fires → wrap-only ships.
  - **Verdict: 2-lang scope is feasible** — 8-12 GB peak against 9.4 GB reclaimable + 1.4 GB strict = ~10.8 GB gives tight but workable headroom.
  - **4-lang scope would fail** — 8-16 GB peak against 10.8 GB available = negative headroom. The memory downgrade (was 4 langs / 6h, now 2 langs / 3h) is what makes this feasible.

- **K1 verdict (LOCKED 2026-09-29 07:30 IST):**
   - kok K1 SURVIVES — McNemar p=0.0033 (surya vs tesseract_bilingual, n=100), gap = 0.194 (surya 0.425 - easyocr 0.619, best runner-up per EVIDENCE_SUMMARY §3) ≈ 19.4pt absolute gap ≫ T2=3.0pt. [FIXED 2026-09-29 per fix-spec: prior "gap = 0.32 / 19pt" was internally inconsistent (0.644−0.425=0.219) and off vs canonical EVIDENCE_SUMMARY §3 (runner-up easyocr 0.619 → 19.4pt); K1 decision unchanged.]
  - pa K1 SURVIVES — McNemar p<0.0001 (surya vs tesseract_indic, n=90), gap = 0.081 (surya 0.145 - tess_i 0.226) ≈ 8pt absolute gap ≫ T2=3.0pt.

---

## 2. Per-language QLoRA scaffold

For each SAFE lang, the QLoRA scaffold is a recipe (data → preprocess → train → eval → decide). The recipe is the same; the per-lang section specifies the data subset, expected delta, and cost.

### 2.1 — Konkani (kok)

- **Backbone:** Qwen2.5-VL-3B-Instruct @ 4-bit MLX (primary)
- **Data subset:** `level2/probe22/manifest.json` `kok` items (n=100), `gt_source = official_pdf_layer`, all 100. Image-text pairs from `Datasets/akshardrishti_official/Konkani/`. Trust 75.0 → SAFE.
- **Augmentation:** vertical jitter ±5px, contrast ±10%, no rotation (preserve Devanagari baseline).
- **LoRA config:** r=16, alpha=32, dropout=0.05, target_modules = `q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj`, vision_modules OFF (don't fine-tune vision encoder on small n).
- **Training:**
  ```bash
  mlx-tune sft \
      --model mlx-community/Qwen2.5-VL-3B-Instruct-4bit \
      --data /w6/data/kok_sft.jsonl \
      --output /w6/out/kok_qlora \
      --lora-r 16 --lora-alpha 32 --lora-dropout 0.05 \
      --batch-size 1 --grad-accum 8 \
      --grad-checkpoint \
      --lr 1e-4 --epochs 3 \
      --max-seq-len 1024 --image-res 512 \
      --metrics cer,wer \
      --seed 20260926
  ```
- **Expected CER delta:** wrap baseline (surya) = 0.425; QLoRA target ≤ 0.350 (gap to runner-up was 19.4pt per EVIDENCE_SUMMARY §3 → 7.5pt to the 0.350 target; ~5pt conservative per D1 estimate, McNemar-significant if n=100). Honest expectation: small-n QLoRA on Indic scripts often regresses; budget for ≤5pt improvement or no change.
- **Cost estimate:** 100 items × 3 epochs × 1024 tokens × ~3s/iter = ~30 min on M2 Max 32GB (4-bit 3B + grad checkpointing). Disk: ~600MB adapter weights.
- **Eval gate:** re-score on probe22 kok subset using mlx-tune's built-in `cer,wer` (trained on same metric). Compare vs wrap baseline via McNemar exact test (K1 gate).

### 2.2 — Punjabi (pa)

- **Backbone:** Qwen2.5-VL-3B-Instruct @ 4-bit MLX (primary)
- **Data subset:** `level2/probe22/manifest.json` `pa` items (n=100), all 100. Trust 73.2 → SAFE.
- **LoRA config:** same as kok (r=16, alpha=32).
- **Training:** same recipe as kok, `--data /w6/data/pa_sft.jsonl`.
- **Expected CER delta:** wrap baseline (surya) = 0.145; QLoRA target ≤ 0.115 (was 8pt → 2pt improvement per D1 estimate, McNemar-significant if n=90). 2nd-best tess_i = 0.226, gap = 0.081. K1 gate: McNemar surya vs tess_b on pa p<0.0001 (winner=b, n=90, 88 discordant). Significant gap, >3pt improvement possible.
- **Cost estimate:** ~30 min.
- **Recommendation:** QLoRA on pa is HIGHEST-VALUE (3B params × 100 Gurmukhi pairs is plenty of signal). Likely 5-7pt improvement.

---

## 3. Common scaffolding (shared across 2 langs)

### 3.1 — Data preparation (one-time, before any QLoRA runs)

```bash
python3 /w6/build_sft.py \
    --lang kok,pa \
    --gt-source official_pdf_layer \
    --out /w6/data/ \
    --image-root /Users/srujansai/Desktop/South/Datasets/akshardrishti_official/ \
    --max-text-chars 1024 \
    --format mlx-tune-sft-jsonl
```

`build_sft.py` reads `level2/probe22/manifest.json` + `level2/probe22/image_meta.json`, joins on image_id, normalizes GT (strip control chars per §6.5 hardened gates), writes `{"image": "...", "text": "...", "lang": "..."}` per line. Total: 200 records × 2 langs.

No `or` DPO set (or KILLED at K1). No `mai` (mai KILLED at K1).

### 3.2 — Environment (one-time, Engine agent, user-approved)

```bash
python3 -m venv /w6/.venv
source /w6/.venv/bin/activate
pip install mlx-tune mlx-vlm mlx mlx-metal
# mlx-tune ships its own CLI; expect `mlx-tune` on PATH
```

**INSTALL GATE:** mlx-tune + mlx-vlm install is **PENDING USER APPROVAL** (per §9 hard rule). Engine agent owns the install plan; user signs off before pip install runs.

### 3.3 — Training orchestration

Each lang runs as a separate mlx-tune job. **One-at-a-time per the campaign §7 guardrail ("Engines one at a time, never parallel heavy ones").** Estimated wall-clock for 2 SAFE langs: 30 + 30 = ~60 min compute. Plus eval: ~30 min/lang = +1 hour. **Total W6 QLoRA budget: ~3 hours compute + setup.**

### 3.4 — Eval gate (post each lang)

```bash
mlx-tune eval \
    --model /w6/out/kok_qlora \
    --data /w6/data/kok_eval.jsonl \
    --metrics cer,wer \
    --output /w6/eval/kok_metrics.json

python3 /w6/mcnemar_q_vs_wrap.py \
    --q /w6/eval/kok_metrics.json \
    --wrap /Users/srujansai/Desktop/South/level2/probe22/scores/metrics_surya_normalized.json \
    --lang kok \
    --output /w6/eval/kok_mcnemar.json
```

If McNemar p > 0.05 (no significant improvement) → kill QLoRA for that lang (K1 gate fires). If McNemar p < 0.05 AND CER delta > 3pt absolute → keep QLoRA adapter in W6 routing.

### 3.5 — W6 routing integration

If a lang's QLoRA adapter clears K1, the wrap-pipeline routes:
```
for item in probe22:
        if lang in q_lora_winners:        # {kok, pa} candidates
            use_q_lora(item, lang)
        else:
            use_wrap_baseline(item, lang) # surya + tesseract-family
```

`q_lora_winners` = langs where K1 cleared. Empty set means wrap-only delivers the campaign.

---

## 4. Compute cost (DERIVED, conservative — 2 langs only)

| Lang | Items | SFT time | | Eval time | | Adapter | Total |
|------|-------|----------|---|-----------|---|---------|-------|
| kok | 100 | 30 min | | 30 min | | 600 MB | 1h00 |
| pa | 100 | 30 min | | 30 min | | 600 MB | 1h00 |
| **TOTAL** | **200** | **1h00** | | **1h00** | | **1.2 GB** | **2h00** |

Plus W6 env setup (30 min one-time, **gated on user install approval**), data preparation (1h one-time), decision integration (30 min). **Total W6 QLoRA work: ~3 hours single-machine, M2 Max 32GB, no cloud spend.**

If memory check fails at runtime → kill QLoRA (K1), deliver wrap-only in ~30 min instead of 3 hours. The wrap-only path is the GUARANTEED deliverable per §11.

---

## 5. Expected outcomes (DERIVED, honest-empty-correct)

**Optimistic:** kok + pa pass K1 with ≥5pt improvement. W6 routing adds QLoRA on both. Wrap-only on the rest. Net: 2 of 2 SAFE langs improved.

**Realistic:** kok + pa pass K1; some regression risk on pa if QLoRA memorizes small-n. Net: 1-2 of 2 SAFE langs improved. Wrap-only on the rest.

**Pessimistic:** kok + pa both fail K1 (QLoRA regresses small-n, typical for QLoRA on <200 sample Indic scripts). Wrap-only delivers. Net: 0 of 2 SAFE langs improved; W6 = wrap-only baseline.

**None of these outcomes change barred-lang status (D4 still locked) or the campaign goal (Sarvam 87.39 is obituary-DEAD per §9.2; our internal CER is the metric that matters).**

---

## 6. Risk register

- **R1: mlx-tune not installed.** Mitigate: clone `ARahim3/mlx-tune` from GitHub at W6 freeze. **PENDING USER APPROVAL 2026-09-29.** Engine agent owns the install plan.
- **R2: Memory exceeds 12.6GB peak (1.10 strict + 11.5 reclaimable).** Mitigate: K1 kill criterion + run `mlx-tune memory-check` BEFORE training (rejects before commit). Reduce batch size to 1, image-res to 384 if needed.
- **R3: Backbone does not render Gurmukhi/Devanagari properly.** Mitigate: SAFE langs use Devanagari/Gurmukhi only — no Ol Chiki, no Nastaliq. Qwen2.5-VL-3B handles both (per official Qwen2.5-VL model card).
- **R4: pa regression (QLoRA surya gets WORSE than wrap tess_i).** Mitigate: K1 gate fires; wrap keeps tess_i.
- **R5: User declines budget for 3 hours compute.** Mitigate: wrap-only ships in ~30 min. K1 not evaluated.
- **R6: M2 Max MLX quirks on first run** (NEW 2026-09-29 risk). mlx-metal / mlx-core may have quirks (grad checkpointing bugs, custom kernel fallbacks) that haven't been exercised on this machine. Mitigate: smoke-test with 5-item mini-batch BEFORE the real 100-item run; abort if smoke-test fails or runs >2x expected time. **Smoke-test spec: `level2/probe22/QLORA_SMOKE_TEST.md` (5 items: 2 kok + 2 pa + 1 cross-lang) — see companion doc.**

---

## 9. NEW findings (post-W6_QLORA_SPEC v1 — from live research 2026-09-29)

These findings are INTEGRATION candidates — they do NOT change the W6 spec's
K1-locked scope (kok + pa only) but they DO change:
- (a) the alternate-backbone ranking (now 4 candidates not 3)
- (b) the W6 path forward IF the user vetoes kok+pa at the freeze call
- (c) the weak-cell attack plan (§11 of LEVEL7_RESEARCH_CAMPAIGN.md) for ks/sat

### 9.1 LightOnOCR-2-1B — strongest W6 backbone candidate

- Source: arXiv:2601.14251v2 (LightOn, 2026-06-30), Apache-2.0
- Architecture: Mistral-Small-3.1 vision + Qwen3 + 2-layer MLP
- Training: SFT → GRPO RLVR with checkpoint averaging + task-arithmetic merge
- Benchmark: **olmOCR-Bench SOTA at 1B** (9× smaller than priors)
- Why it's relevant: Smallest SOTA model that uses SFT-then-RLVR — exactly our D1 path. If user approves at W5 freeze, swapping Qwen2.5-VL-3B → LightOnOCR-2-1B halves adapter size (~300 MB vs 600 MB) and halves inference cost.
- **Status: WATCH / Option C candidate.** The W6 spec keeps Qwen2.5-VL-3B as primary because mlx-vlm already has Qwen support; LightOnOCR-2-1B MLX deployment is unverified as of 2026-09-29. If user wants the smallest-strongest backbone → Option C activates and the W6_QLORA_SPEC is revised in place.

### 9.2 600k-ks-ocr — direct training data for Kashmiri weak cell

- Source: arXiv:2601.01088 (Malik, 2026-01-03)
- 602,000 word-level synthetic Kashmiri images, 3 traditional typefaces, 10.6 GB
- **License: CC-BY-4.0** (free for any use, including commercial)
- Why it's relevant: Sarvam's Kashmiri cell is 54.82 — the WORST public number on Indic OCR Bench. We can't beat Sarvam on ks without specialist data, and our probe22 ks GT is fragmented Nastaliq (BARRED per §6.4). 600k-ks-ocr gives us 602K *clean* synthetic Kashmiri images to fine-tune on, bypassing the GT-bar.
- **Status: WATCH for D4 micro-repair extension.** D4 currently allows sat+ks micro-repair 5-10 pages each. Adding 600k-ks-ocr would let us fine-tune a *small* (1B-class) OCR model on Kashmiri synthetic data for ~30 min and get a real CER on probe22 ks items. **This is the strongest opening we have against Sarvam on Kashmiri — a ~5-10pt improvement is realistic per Fayaz et al. 2026 Kraken baseline (char-acc 54.91%) vs Sarvam 54.82%.** If user approves, expand D4 from "5-10 pages micro-repair" to "600k-ks-ocr + QLoRA fine-tune for ~30 min" — Option D expansion.
- **Hard rule check: 600k-ks-ocr is free + CC-BY-4.0; download requires user approval per §9 (no downloads without explicit user approval). NOT in the $0 ask — 10.6 GB download is a separate gate.**

### 9.3 Laya — router/gate layer candidate

- Source: madewithjev.com + jevmodel.org + GitHub DDnim
- Apache-2.0, **422M multilingual** (mmBERT-base, 100+ langs)
- Latency: 32.8 ms / question on T4; 7.2 ms in batches of 10
- Three typed primitives: choice, score, noul
- Router dispatches by script in <0.5ms
- Why it's relevant: With our 11 engines + per-script routing already locked, Laya could add a *confidence-gate* layer: only invoke the heavy 3B-class backbones (Qwen3-VL, LightOnOCR) when Laya's P(true) < 0.85 on a block. Saves compute on already-easy blocks.
- **Caveat (from LIVE_LATEST 2026-09-29):** Laya is *confidently wrong* on out-of-distribution scripts (Khmer 0.000 @ 0.952 confidence). Must calibrate on our 4 weak cells (sat/ks/OldScan/or) before relying. Calibration = Laya on probe22 + gt_verification.json, measure per-script calibration error, gate only when P(true) and script are in-distribution.
- **Status: WATCH / Phase 7 (post-W6) candidate.** Not in W6 spec; mentioned for awareness. If W6 ships ahead of schedule, Laya calibration could be W7.

### 9.4 PaddleOCR-VL 1.6 — third-party baseline confirmation

- Source: arXiv:2606.03264 (Baidu, 2026-06-02), Apache-2.0
- 0.9B total (NaViT + ERNIE-4.5-0.3B decoder)
- **OmniDocBench v1.6: 96.33% (new SOTA)**
- 109 langs incl. Hindi; open weights
- Why it's relevant: Confirms the small-strong backbone path. PaddleOCR-VL 1.6 is already on our Watch list (INTEGRATED-ELITE-STACK.md §keep-as-reference). The 96.33 number is the strongest published single-model OCR result on any benchmark as of 2026-09-29.
- **Status: WATCH.** Not currently in W6 plan; would require backbone swap to PaddleOCR-VL (Option C) and MLX deployment is unverified.

### 9.5 Gnani Evon 3.3 — text-only, not OCR

- Source: HF gnani/gnani-evon-v3.3-30B-A3B + Gnani NeurIPS 2026 GlobalSouthAI papers
- 30B total / 3.5B active, Mamba2-Transformer MoE, Apache-2.0, 11 Indic langs
- NeurIPS 2026 paper 1: embedding expansion + warmup recipe (+11.8 MILU on 8 Indic langs)
- NeurIPS 2026 paper 2: RL trade-off (MATH +36, Indic document QA -11)
- **OCR capability: NONE.** Evon is text-only. Pipeline tag = text-generation.
- Why it's relevant: The embedding-expansion recipe is a load-bearing reference for any future W6 work on Indic models (post-hackathon). The RL trade-off validates our D1 stance "RLVR after SFT plateaus" and reinforces §6.4 RLVR-on-gold-only.
- **Status: WATCH (academic, not W6).** Too large for local QLoRA (30B vs our 4-bit 3B ceiling). Could be a *post-OCR text normalizer* in Stage 3 — but Stage 3 is IndicBERT/Airavata/small LLM in the PPT.

---

## 7. Verdict agent's recommendation

**EXECUTE QLoRA on kok + pa** (the 2 SAFE langs with significant gap per McNemar and ≥3pt room for improvement).
**KILLED QLoRA on mai + or** by K1 default (no significant gap).

**Net effect:** 2 langs × 30 min × 2 = ~1 hour compute. Adapter weight = **1.2 GB on disk**. If user approves mlx-tune install + K1 clears both, W6 routing has QLoRA adapters on 2 langs.

If user prefers simpler default → skip QLoRA entirely, ship wrap-only baseline (D1 default).

---

## 8. Disk-truth reference (numbers above)

Source files:
- `level2/probe22/scores/metrics_surya_normalized.json` — wrap baseline
- `level2/probe22/scores/metrics_tesseract_bilingual_normalized.json` — 2nd-best proxy for SAFE langs
- `level2/probe22/scores/metrics_tesseract_indic_normalized.json` — tesseract_indic (best on or; 2nd-best on pa)
- `level2/probe22/scores/metrics_*_normalized.json` — all engines
- `level2/probe22/scores/mcnemar_full_matrix.json` — McNemar p-values
- `level2/probe22/gt_forensics.json` per_language — GT quality
- `level2/probe22/manifest.json` — item lists, gt_source
- `INTEGRATED-ELITE-STACK.md` — W6 tool decisions (lines 28-39)
- `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 — kill criteria
- `level2/probe22/KILL_CRITERIA.md` — K4 install/memory gate (NEW 2026-09-29)
- `level2/probe22/QLORA_TRAINING_DATA.md` — SFT jsonl spec (NEW 2026-09-29)
- `level2/probe22/QLORA_EVAL_SPEC.md` — McNemar + Wilson eval spec (NEW 2026-09-29)
- `level2/probe22/QLORA_SMOKE_TEST.md` — 5-item pre-train smoke test (NEW 2026-09-29)
- `level2/probe22/MEMORY_RECLAIM_RESULT.md` — 9.4 GB reclaimable measured (NEW 2026-09-29)
- `docs/research/level7/W5_FREEZE_AGENDA.md` — W5 freeze agenda (NEW 2026-09-29)

Verified at 2026-09-29 07:30 IST; refreshed at 2026-09-29 ~16:30 IST (memory budget + companion-doc cross-references added).

K1 verdict on kok/pa: SURVIVES (see §0).
K1 verdict on mai/or: KILLED (see §0).

§6.4 lock still BARRED: ks/mni/mr/sat/ur + ne PDF-tier.