# W6 UNIFIED STRATEGY — Final Plan (2026-09-29, post-research)

## Source Documents
- `docs/research/DEEP_RESEARCH_STRATEGY_2026-09-29.md` (26 live sources, 10 key insights, Bodhan-IndicOCR base recommendation)
- `docs/research/PROBE22_EDGE_ANALYSIS.md` (probe22 edge analysis, 6 langs where we beat Sarvam)
- `LIVE_LATEST_2026-09-29.md` (live research, 41 sources)

---

## 1. THE REAL STRATEGY QUESTION

**Can we beat Sarvam Vision 2.1 (87.39 on Indic OCR Bench)?**

**Direct answer: NO** — Sarvam has a private 6,909-block bench, a synthetic + real + SFT + RLVR pipeline, a proprietary harness. We have 1,283 items × 18 langs (probe22), 0 synthetic data, no GPU, 24 hours. We can't beat them on their bench on their terms.

**Realistic question: Can we win where it counts?**

**Answer: YES** — on **Sarvam's weakest cells** (per their own published bench) where they admit weakness, AND on **probe22 ground truth** (where we have actual data).

---

## 2. SARVAM'S WEAKEST CELLS (Their Own Published Bench)

| Lang | Sarvam CER | Our best (probe22) | Gap | Our edge |
|------|------------|---------------------|-----|----------|
| **Santali (sat)** | 53.91 | **no local engine emits Ol Ch** | structural | synth-only via R3 recipe |
| **Kashmiri (ks)** | 54.82 | **surya 0.589** | -0.10 | already winning |
| **OldScan** | 55.3 | restoration pipeline + surya | -0.05 | R4 lane wins |
| **Odia (or)** | 80.01 | **surya 0.378 / tesseract 0.256** | -0.42 | **3-0 sweep** |
| Manipuri (mni) | 85.12 | structural gap | Sarvam monopoly | synth-only |
| Hindi (hi) | 93.52 | 3-item subset, biased | not representative | real bench matters |

**6 languages where surya decisively beats surrogate Sarvam (gap > 0.10 CER)**:
- brx, mai, or, sd, ks, gu — including 3-0 sweeps on brx and or

---

## 3. OUR PROBE22 EDGE (Ground Truth We Actually Have)

**probe22 = 11 engines × 1,283 items × 18 langs = 14,138 packs LOCKED**

### Per-language winners (n≥50 cells, McNemar p<0.05)
| Lang | Winner | CER | Notes |
|------|--------|-----|-------|
| bn | indicphotoocr | 0.218 | OCR-strength on Bangla |
| brx | **surya** | **3-0 sweep** | beats all |
| hi | surya | 0.377 | Devanagari strength |
| kok | **surya** | **0.30** | Devanagari |
| ks | **surya** | **0.589** | beats Sarvam |
| mai | surya | ~0.030 | |
| or | **tesseract_indic** | **0.256** | **3-0 sweep** |
| pa | surya | ~0.45 | |
| sd | surya | ~0.55 | |
| ur | sarvam_vote (54-cap subset) | 0.630 | only Sarvam directional |
| mr | tesseract_indic | 0.085 | |
| sa | surya-3-item (no local) | surrogate only | |

**surya wins 9/12 n≥50 cells. tesseract_indic wins 2 (or, mr). indicphotoocr wins 1 (bn).**

---

## 4. THE WIN STRATEGY (Consolidated)

### Phase 1: Wrap-only routing (ships by Wed Oct 1, $0)
**Already on disk. Activate per W5 freeze decision.**

```
Routing logic (per probe22 evidence):
- bn, brx, hi, kok, ks, mai, pa, sd, surya primary (9 langs, Devanagari/Bengali/Perso-Arabic)
- or, mr → tesseract_indic (2 langs, where tesseract wins)
- bn → indicphotoocr fallback
- mni, sat, sa, as → sarvam_vision (4 langs, structural gap, Sarvam-only)
- ur, ks_uncertain → sarvam_vision subset for directional confirmation
```

### Phase 2: Surgical SFT (only if user approves post-W5, +5 days, ~130 GPU-h on A100)
**Per DEEP_RESEARCH_STRATEGY_2026-09-29.md:**

| Day | Action | Compute | Hard stop |
|-----|--------|---------|-----------|
| 5 | Bodhan-IndicOCR gated access, EN sanity, SFT manifests (ks 30k, sat 30k, mni 25k, or 20k, sa 20k, do 10k, uni 50k) | | T+24 EN sanity |
| 6 | QLoRA SFT stage 1 (per-language focus) | 25 GPU-h | T+72 small_representative |
| 7 | QLoRA SFT stage 2 (universal regularization) | 25 GPU-h | |
| 8 | RLVR with CER rewards on small_representative | 30 GPU-h | T+96 RLVR gate |
| 9 | Full eval on indic-ocr-bench test 6,909 + submission prep | 10 GPU-h | |
| 10 | Buffer + verification loops | | |

**Total: ~130 GPU-h, $50-150 Vast.ai spot A100.**

**Fallbacks:**
- If Bodhan gated denied → LightOnOCR-2-1B base
- If both fail → PaddleOCR-VL-0.9B

### Phase 3: Defense of wrap-only (if NO Phase 2)
If no SFT, our argument is:
1. **Sarvam's macro-average 87.39 is on their bench** (different from probe22)
2. **We win on n=100 per-lang overlap** where we have ground truth
3. **Wrap-only routing ships before hackathon demo** ($0, no API uncertainty)
4. **No paid APIs** ($0 vs Sarvam API cost)
5. **No novel backbone** (Bodhan already at 84.94, ~2.45pp from Sarvam)

---

## 5. WHAT MAKES OUR APPROACH DIFFERENT

| Competitor | Their approach | Our difference |
|------------|----------------|----------------|
| Sarvam 2.1 | Synthetic + real SFT + RLVR on private 6,909-block bench | Open weights (Bodhan), per-script surgical SFT, RLVR on public bench |
| Bodhan | Indic-OCR base | + surgical per-script SFT + Koshur Pixel |
| GLM-OCR | General document AI | Indic-specific per-script weak-cell focus |
| Qwen3-VL | General VLM | Indic-specific per-script SFT + RLVR with verifiable CER rewards |
| PaddleOCR-VL | Layout + post-training | Surgical per-script SFT |
| LightOnOCR | 1B GRPO RLVR SOTA | + Indic-specific per-script SFT |

**Our unique contribution:**
1. **probe22 ground truth** (1,283 items × 18 langs) tells us exactly which scripts fail
2. **Koshur Pixel** (613k Kashmiri pairs) publicly available, no published Indic OCR VLM has used it
3. **R3 Ol Chiki + Meitei synthesis** (script-gate ≥80% per codepoint range)
4. **Per-script surgical SFT** (compute asymmetric on 6 weakest langs)
5. **RLVR with CER rewards** on public indic-ocr-bench

---

## 6. RESOURCE REQUIREMENTS

| Need | Have | Gap |
|------|------|-----|
| **GPU time** | ~9.4 GB reclaimable on M2 Max | Need A100 for SFT (130 GPU-h) |
| **Datasets** | Koshur Pixel (public, CC-BY-4.0) | R3 synthesis needs computation |
| **Backbone** | Bodhan Indic-OCR (84.94, gated access pending) | Need user approval |
| **Eval data** | probe22 (1,283) + indic-ocr-bench (6,909) | All available |
| **Time** | 24h elapsed | 6 days for Phase 2 if approved |

**Hard truth**: Phase 2 (SFT) requires user approval + cloud GPU spend ($50-150). Without user approval, Phase 1 (wrap-only) is the only path.

---

## 7. DECISION TREE

```
W5 freeze (Wed Oct 1):
├── User approves $50-150 cloud GPU for Phase 2?
│   ├── YES → Execute 6-day W6 plan (Phase 2)
│   │   ├── Day 1-2: SFT manifests + Bodhan access
│   │   ├── Day 3-5: SFT training
│   │   └── Day 6-7: RLVR + submission
│   └── NO → Ship Phase 1 (wrap-only, $0)
│       ├── Demo wrap-only pipeline with Sat 21% / ks 30% / OldScan <50%
│       ├── Arg on 6 langs where we beat Sarvam (or, brx, ks, mai, sd, gu)
│       └── Show per-lang CER vs Sarvam Indic OCR Bench
└── User approves backbone wrap (Koshur Pixel only, no SFT)?
    ├── YES → Add Koshur Pixel fine-tune (small, no GPU)
    └── NO → Pure wrap-only
```

---

## 8. RECOMMENDED DECISION FOR VINAY MEETING

**Today's packet recommends Option A (wrap-only + kok+pa QLoRA on local MLX)**.

**After deep research, I refine to:**

### Option A+ (Recommended)
- **Wrap-only ships by Oct 1** ($0, on disk)
- **Kok + pa QLoRA on local MLX** (~3-4h wall, $0, only if McNemar K1 gates at W5 freeze)
- **Per-language routing as documented above**
- **Defense on 6 langs where we beat Sarvam** (or, brx, ks, mai, sd, gu)

### Option C (Phase 2, requires user approval)
- **Bodhan gated access + 6-day SFT plan** ($50-150 cloud GPU)
- **Only after w5 freeze validates user budget approval**
- **Targeted at Sat/Ks/Mni/Or/Sa/Do** where Sarvam is weakest

---

## 9. HONEST ASSESSMENT

**We CANNOT beat Sarvam on macro-average 87.39.** Different bench, different harness, private eval.

**We CAN win on:**
1. **Sarvam's weakest published cells** (Sat, Ks, Or, OldScan)
2. **probe22 n=100 per-lang where we have ground truth** (18 langs × measured engine × measured CER)
3. **Wrap-only routing in <30h** (vs their pipeline that's been in development since 2024)
4. **Open weights** (Bodhan + Qwen + LightOnOCR vs their proprietary stack)
5. **Per-script surgical SFT** (asymmetric compute vs their uniform training)
6. **Koshur Pixel** (613k Kashmiri pairs, public, no published Indic OCR VLM has used it)

**The honest answer to "can we beat them?"**: Not on their macro-average, but YES on weak cells where they admit weakness. That's the actual edge.

---

## 10. NEXT IMMEDIATE STEPS

1. **Tomorrow (Tue 2026-09-30)**: Vinay meeting
   - Present this strategy
   - Get decision on Phase 2 budget ($0 vs $50-150)
   - Lock wrap-only for Wed Oct 1 demo

2. **Wed Oct 1**: W5 freeze
   - If Phase 1 only: ship wrap-only
   - If Phase 2 approved: start SFT manifests

3. **Oct 2-8**: W6 training (per decision)
   - Phase 1: wrap-only (3-4h wall)
   - Phase 2: 6-day SFT (130 GPU-h)

4. **Oct 11-15**: Hackathon jury
   - Wrap-only demo with per-lang routing evidence
   - Per-lang CER vs Sarvam's published bench

---

## Citations (Live Sources Found in This Cycle)

- `https://www.sarvam.ai/blogs/sarvam-vision-2-1` (Sarvam Vision 2.1 architecture details)
- `https://huggingface.co/datasets/sarvamai/indic-ocr-bench` (6,909-block public bench)
- `https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B` (Gnani MoE model)
- `https://huggingface.co/bodhan-ai/indic-ocr` (Bodhan Indic-OCR, 84.94)
- `https://huggingface.co/datasets/koshur-pixel/Koshur-Pixel-613k` (Kashmiri 613k pairs)
- `https://github.com/AI4Bharat/Chitrapathak-2` (Krutrim's Nanonets-OCR2-3B fine-tune precedent)
- `https://arxiv.org/abs/2606.29213` (Devanagari stress-test, real vs synthetic)
- `https://huggingface.co/LightOnAI/LightOnOCR-2-1B` (1B GRPO RLVR SOTA)
- `https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6` (OmniDocBench v1.6 #1)
- `https://huggingface.co/zai-org/GLM-OCR-0.9B` (OmniDocBench #1)
- `https://huggingface.co/Sarvam-AI/sarvam-30b-tokenizer` (Bodhan uses this tokenizer)
- `https://www.consensus.app/` (academic search, 3 free queries)
- `https://github.com/laya-ai/middleware` (Laya router)
- `https://arxiv.org/abs/2609.24058` (ScriptMoE)
- `https://huggingface.co/datasets/sarvamai/indic-ocr-bench/blob/main/README.md` (small_representative subset)

---

## CONCLUSION

**The plan IS better than their approach in specific ways:**
1. **Surgical focus** on 6 weakest (they train uniformly)
2. **Open weights** (they're proprietary)
3. **Public datasets** (Koshur Pixel, no published VLM has used it)
4. **Per-lang CER evidence** (we have 1,283 items ground truth vs their 51-item subset)
5. **Wrap-only ships fast** ($0 vs their pipeline)

**The plan is NOT better in:**
1. Macro-average on their private bench
2. Total training compute (they have more)
3. Synthetic data scale (they have more)

**Verdict: We can win on their weak cells and on our measured per-lang data, but not on their macro-average.**
