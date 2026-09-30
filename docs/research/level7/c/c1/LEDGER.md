# Lane C1 — NVIDIA stack for OCR/document VLMs: MASTER LEDGER

Lane: C1 (Miss Agent task force). Scope: TensorRT-LLM, NIM, NeMo Customizer,
quantization FP8/FP4 (Indic-script impact), Jetson/edge, serving $/1M pages,
LoRA VRAM math for 2B VLMs. Sources 2025–2026 only.

Format (campaign-mandatory):
`ID | source_url | date | VERIFIED/INFERENCE | rel(1-5) | rec(1-5) | act(1-5) |
Score=product | 3–10 line extraction (mechanism → result → maps to weak cells)`

Weak cells: Santali 53.91 / Kashmiri 54.82 / OldScan 55.3 / Odia 80.01.
Flag rule: Score ≥ 30/125 → candidate for integrated architecture (§INTEG).
VERIFIED = read the source content directly (fetch or full excerpt).
INFERENCE = claim inferred beyond what the excerpt strictly shows; marked inline.

Topic-note companions: NOTE_TRTLLM.md, NOTE_QUANT_INDIC.md, NOTE_SERVE_COST.md,
NOTE_EDGE.md, NOTE_LORA_VRAM.md. Record IDs cross-referenced there.

---

## S1 — TensorRT-LLM serving stack for small VLMs (S1-001…S1-018)

C1-001 | https://github.com/Kevinma0215/Qwen2-VL-TRT-Quantization/blob/main/results/reports/final_report.md | 2026 (repo, fetched full text 2026-09-26) | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
Seven TRT-LLM configs benchmarked on Qwen2-VL-2B-Instruct (our exact model class) on RTX 5060 Ti 16GB: TRT BF16/INT8/INT4/SmoothQuant/FP8/INT4-AWQ/NVFP4.
Mechanism: weight-bitwidth cut halves decode bandwidth → 4-bit tiers hit 2.39–2.42× decode speedup over PyTorch BF16; TTFT gains (1.63–2.12×) come from graph fusion regardless of precision.
Result: SmoothQuant W8A8 is Pareto-optimal — 2.00× TTFT / 2.13× decode while MATCHING baseline (VQAv2 82.8 vs 82.3, MME 1973 vs 1952).
Maps: single most actionable serving recipe for a fine-tuned Qwen2-VL-2B Santali/Kashmiri specialist — no accuracy cost, halves latency.

C1-002 | https://github.com/Kevinma0215/Qwen2-VL-TRT-Quantization/blob/main/results/reports/final_report.md (§5.1) | 2026 | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
FP8 KV-cache on Qwen2-VL caused VQAv2 −8.8pp / MME −189; ablation isolated `--kv_cache_dtype fp8` (removing FP8 FMHA changed nothing; removing FP8 KV fully restored 82.0/MME 1946).
Mechanism: visual-token KV from BF16 ViT has wider dynamic range than text KV; FP8-E4M3 (±448) clips it, error compounds across layers; landmark +10.5pp / posters +13.6pp recovered on fix.
Maps: hard deployment guard for OUR pipeline — any FP8 serve of the 2B VLM keeps KV in BF16 (cost: dyn VRAM 0.8→1.4GB, decode 2.3→2.0×). Directly protects OldScan 55.3 pages where visual-token variance is largest.

C1-003 | https://github.com/Kevinma0215/Qwen2-VL-TRT-Quantization/blob/main/results/reports/final_report.md (§4.5 MME detail) | 2026 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
MME-OCR subtask (closest to our CER goal): BF16 24/40 → INT8 24/40 (lossless), SmoothQuant 24/40, NVFP4 23/40, INT4-AWQ 21/40, FP8 22/40.
Mechanism: 8-bit tiers preserve glyph discrimination; AWQ per-group weight quant hurts most on OCR + text_translation (25/40 vs 37/40 baseline).
Maps: if we quantize the production OCR VLM, INT8-weight-only or SmoothQuant are CER-safe; AWQ is barred for script-heavy workloads (Santali Ol Chiki / Kashmiri Nastaliq unseen glyphs behave like the translation tail).

C1-004 | https://github.com/Kevinma0215/Qwen2-VL-TRT-Quantization/blob/main/results/reports/final_report.md (§5.2) | 2026 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
INT4-AWQ collapses text_translation 90.0→62.5% (−27.5pp) while plain INT4 scores 85.0%; NVFP4 collapses commonsense_reasoning 71.4→57.9% and code_reasoning 65→52.5% but perception tasks only −1–3pp.
Mechanism: AWQ protects channels salient in its calibration corpus — INFERENCE: English-only calibration under-protects non-English embedding channels, exactly our Kashmiri/Santali risk. NVFP4 error accumulates over multi-hop generation, not single-step recognition.
Maps: (a) any AWQ/GPTQ calibration MUST include Ol Chiki + Nastaliq + Mayek samples (links to C1-061/062 multilingual-calibration law); (b) NVFP4 acceptable for single-pass OCR transcription, barred for reasoning-heavy layout/QA heads.

C1-005 | https://nvidia.github.io/TensorRT-Edge-LLM/0.4.0/developer_guide/02_Supported_Models.html | 2026 (v0.4.0 docs) | VERIFIED | 5 | 4 | 5 | **100** | §INTEG
TensorRT Edge-LLM support matrix lists Qwen2-VL-2B-Instruct and Qwen2.5-VL-3B-Instruct with FP16/FP8/INT4-AWQ/INT4-GPTQ/NVFP4 ALL green; FP8 vision-encoder supported on SM89+; NVFP4 recommended on Thor (SM100+).
Mechanism: whole 2B-VLM stack (ViT + LM head + decoder) has a vendor-supported quant path, including FP8 ViT — no custom kernels needed.
Maps: de-risks the entire quantize-and-ship plan for Santali/Kashmiri specialists onto Jetson/edge; FP8-ViT support means the C1-002 visual-KV caveat is the only known trap.

C1-006 | https://nvidia.github.io/TensorRT-LLM/1.2.1/overview.html + https://developer.nvidia.com/tensorrt-llm | 2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
TRT-LLM supports Qwen2-VL / LLaVA-NeXT / VILA / Llama-3.2-Vision multimodal; headline features: FP8 + NVFP4 quant, disaggregated serving, EAGLE-3/MTP speculative decoding, paged KV + chunked prefill; v1.0 claimed 8× inference-perf uplift.
Mechanism: in-flight batching + paged attention raise sustained page-throughput; disagg prefill/decode lets long-context scans scale independently.
Maps: for 200-dpi full-page OldScan batch jobs, disagg serving + chunked prefill is the throughput lever; speculative decode is INFERENCE-likely neutral for OCR (short deterministic outputs) — do not budget gains there.

C1-007 | https://nvidia.github.io/TensorRT-LLM/1.1.0rc2/blogs/quantization-in-TRT-LLM.html | 2025–2026 (current docs) | VERIFIED | 4 | 4 | 4 | **64**
Official TRT-LLM quant guidance with measured tables: FP8 MMLU loss ≤0.9% (Falcon-180B 70.4→70.3, LLaMA-2-70B 69.1→68.5) vs INT8-SQ 2.5–2.75%; LLaMA-2-7B FP8 1.4–1.5× speedup @bs≤8, 2.3× @bs16/latency-cap.
Mechanism: at batch ≥16 BOTH bandwidth and compute density matter → FP8 (W+A quant) wins; at batch ≤4 weight-only is preferred.
Maps: rule of thumb for our batch OCR fleet — bulk reprocessing (large batch) → FP8/SmoothQuant; single-page interactive → INT4 weight-only suffices.

C1-008 | https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/features/quantization.md | 2026 (main) | VERIFIED | 4 | 4 | 4 | **64**
Quant recipe catalog: FP4, FP8 per-tensor / block-scaling / rowwise, FP8 KV cache, NVFP4 KV cache, W4A16/W4A8 GPTQ + AWQ; pre-quantized ModelOpt checkpoints load in 2 lines (`LLM(model='nvidia/Llama-3.1-8B-Instruct-FP8')`); NVFP4-KV requires offline ModelOpt quant.
Mechanism: block-scaling FP8 and W4A8-GPTQ give finer-grained error control than per-tensor — the knobs that matter for script-tail glyphs.
Maps: when quantizing our Indic VLM, start from FP8-block-scaling (not per-tensor) per the multilingual-calibration findings (C1-062).

C1-009 | https://nvidia.github.io/TensorRT-LLM/0.20.0rc2/performance/performance-tuning-guide/fp8-quantization.html | 2025–2026 | VERIFIED | 3 | 4 | 4 | **48**
FP8 tuning guide: QuantConfig(quant_algo=FP8) + optional FP8 KV (`kv_cache_quant_algo`, CLI `--kv_cache_dtype fp8`); warns explicitly "quantization aims to preserve accuracy — NOT guaranteed, must verify outputs."
Mechanism: KV-cache FP8 is an independent switch from weight/activation FP8.
Maps: vendor itself blesses the C1-002 fix pattern (KV stays BF16); our runbook keeps the two switches decoupled and verifies on Santali/Kashmiri slices, not English MMLU.

C1-010 | https://github.com/shifan3/TensorRT-LLM-qwen2-vl/blob/main/README.md | 2024–2025 | VERIFIED | 3 | 3 | 3 | **27**
Community TRT-LLM Qwen2-VL recipe (convert_checkpoint → build engine → serialize per-GPU-arch). Confirms TRT engines are arch-locked (rebuild per GPU).
Mechanism: AoT compilation trades portability for speed.
Maps: ops note — engine artifacts for H100-train vs L4-serve vs Jetson must be built separately; INFERENCE: minor, standard practice.

C1-011 | https://github.com/NVIDIA/TensorRT-LLM/issues/2658 | 2025-01-05 | VERIFIED | 2 | 3 | 2 | **12**
Early-2025 issue: Qwen2-VL checkpoint conversion failing on TRT-LLM. Dated evidence of immature VLM support at that time.
Mechanism: VLM multimodal graph (ViT + projector + LLM) lagged text-LLM support.
Maps: historical context only — C1-001/C1-005 (2026) supersede it; do not cite as current blocker.

C1-012 | https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html | 2026 (current) | VERIFIED | 4 | 4 | 5 | **80** | §INTEG
Triton TensorRT-LLM backend: C++ inflight_batcher_llm (in-flight batching + paged attention), MPI leader/orchestrator multi-GPU modes, LoRA support (lora.md), multimodal examples (BLIP2/LLaVA/VILA), LLM-API PyTorch backend serves any HF model with NO engine compile.
Mechanism: Triton = production wrapper (batching, multi-model, metrics) around TRT-LLM engines; LLM-API path removes the AoT friction for iteration.
Maps: recommended production topology for our OCR API — Triton + inflight_batcher_llm + one engine per script-specialist, LoRA adapters hot-swapped per language (Santali/Kashmiri/Odia).

C1-013 | https://github.com/triton-inference-server/tensorrtllm_backend | 2023–2026 (941★/142 forks) | VERIFIED | 3 | 3 | 3 | **27**
Backend repo health: 941 stars, Apache-2.0, source now lives under TensorRT-LLM/triton_backend.
Mechanism: maintained, mainstream path.
Maps: low integration risk; INFERENCE: star count is popularity, not correctness.

C1-014 | https://cerebrium.ai/docs/v4/examples/deploy-an-llm-with-tensorrtllm-tritonserver.md | 2025–2026 | VERIFIED | 3 | 3 | 4 | **36** | §INTEG
Serverless Triton+TRT-LLM deploy pattern (TritonPythonModel initialize/execute/finalize; Triton auto-batches to max_batch_size).
Mechanism: batching at the server layer multiplies the C1-007 large-batch FP8 win.
Maps: if hackathon demo needs a hosted endpoint, this is the copy-paste pattern; keep max_batch_size tuned for page images (memory-heavy prefill).

C1-015 | https://developer.nvidia.com/blog/scaling-llms-with-nvidia-triton-and-nvidia-tensorrt--llm-using-kubernetes | 2025 | VERIFIED | 3 | 3 | 3 | **27**
K8s scaling recipe for Triton + TRT-LLM.
Mechanism: horizontal scale-out for batch backlogs.
Maps: relevant only if post-hackathon scale-up; not W6.

C1-016 | https://nvidia.github.io/TensorRT-LLM/performance/perf-benchmarking.html | 2026 | VERIFIED | 3 | 4 | 3 | **36**
trtllm-bench supports FP8/NVFP4 build+bench flows with pre-quantized checkpoints (nvidia/Llama-3.1-*-FP8).
Mechanism: standardized before/after harness for our own quant-gating measurements.
Maps: adopt trtllm-bench as THE quant acceptance harness — CER on Santali/Kashmiri/Odia slices per tier before promoting any quantized engine.

C1-017 | https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1 | 2025-05-28 | VERIFIED | 4 | 4 | 3 | **48**
Llama-3.1-Nemotron-Nano-VL-8B: document-intelligence VLM (OCR/tables/charts), runtime engine TensorRT-LLM on H100, NIM container, 12-tile 512px layout (up to 2048×1536), 16K ctx. Language: English only.
Mechanism: NVIDIA's own doc-VLM ships ON TRT-LLM + NIM — proof the stack serves OCR VLMs in production.
Maps: architectural precedent for our serving choice; English-only flag is exactly why OUR Indic specialists have headroom (weak cells are non-English scripts).

C1-018 | https://github.com/NVIDIA-NeMo/Nemotron | 2025–2026 | VERIFIED | 3 | 4 | 3 | **36**
Nemotron asset hub: SFT→RL recipes, TensorRT-LLM/vLLM/SGLang/NIM deploy paths, Nemotron-Parse doc-parsing cookbooks, CC-BY VLM datasets (8M OCR/reasoning samples v2).
Mechanism: single hub for recipe + data + deploy.
Maps: cookbook source for W6 SFT→RLVR sequence; dataset licenses are clean (CC-BY) — candidate calibration/fine-tune data provenance.

---

## S2 — FP8 / FP4 / NVFP4 quantization: accuracy + speed (S2-019…S2-040)

C1-019 | https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference | 2026-01-08 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
NVFP4 = E2M1 FP4 + per-16-value FP8 micro-block scale + per-tensor FP32 scale; ≤1% degradation vs FP8 on DeepSeek-R1-0528 (MMLU-PRO/GPQA/HLE within 1%, scicode/math same, AIME −2%); 3.5× memory cut vs FP16, 1.8× vs FP8; up to 25×/50× energy eff. vs H100 for Blackwell/Ultra.
Mechanism: two-level micro-scaling preserves outliers that naive FP4 destroys — the same outlier problem that kills tail-script glyphs.
Maps: NVFP4 is viable for our 2B VLM ONLY with multilingual calibration + reasoning-head caution (C1-004); quantize via ModelOpt, serve via TRT-LLM/vLLM.

C1-020 | https://developer.nvidia.com/blog/3-ways-nvfp4-accelerates-ai-training-and-inference | 2026-08-21 | VERIFIED | 4 | 5 | 3 | **60** | §INTEG
NVFP4 peak 15 PFLOPS dense on Blackwell-Ultra (3× FP8); MLPerf Training Llama-3.1-405B in 64.6 min on 512×GB300 (1.9× prior FP8); closed-division accuracy met on DeepSeek-R1, Llama-3.1-8B/405B, Llama-2-70B.
Mechanism: NVFP4 throughput is real at 405B scale with strict accuracy gates.
Maps: validates NVFP4 as production-grade (not experimental) — but all gates are English-centric; our gate must be CER on Ol Chiki/Nastaliq/Mayek.

C1-021 | https://arxiv.org/pdf/2512.02010v2 (+v3/html) [Four Over Six: More Accurate NVFP4 Quantization] | 2026-01-22 (v3) | VERIFIED | 4 | 5 | 3 | **60**
4/6 adaptive block scaling: scaling some NVFP4 blocks to max 4 instead of 6 cuts worst-case error on near-max values; AWQ+4/6 best PTQ (WikiText-2 11.58, C4 32.36); combines with AWQ/SmoothQuant, HURTS GPTQ (−34.6% gap widening in v2; v3 notes GPTQ mostly improved — version skew flagged).
Mechanism: FP4's 16 values (±0,.5,1,1.5,2,3,4,6) misrepresent near-maxima; adaptive range fixes it; PTX-cvt implementable on Blackwell.
Maps: if NVFP4 PTQ underperforms on Indic slices, 4/6+AWQ is the first fix to try; kernels on GitHub. INFERENCE: v2-vs-v3 GPTQ discrepancy — verify against the repo before relying.

C1-022 | https://developer.nvidia.com/blog/using-nvfp4-low-precision-model-training-for-higher-throughput-without-losing-accuracy | 2026-02-23 | VERIFIED | 3 | 5 | 2 | **30** | §INTEG
NVFP4 pre-training matches BF16 downstream with recipe (AdamW eps 1e-8, LR 6e-4→6e-6, GBS 768) + last-4-layers in BF16 (else diverges); 1.59× throughput.
Mechanism: selective-BF16 tail stabilizes ultra-low-precision training.
Maps: we do NOT pre-train (law), but the principle transfers to QAT/RLVR: keep script-critical late layers (LM head, projector) high-precision. Borderline flag (score exactly 30).

C1-023 | https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell | 2026-08-05 | VERIFIED | 2 | 5 | 2 | **20**
NVFP4 MaxText recipe: 1.73× vs FP8, attention kept high-precision (softmax noise amplification), GEMMs in NVFP4.
Mechanism: attention-outlier guard mirrors the C1-002 visual-KV lesson.
Maps: reinforces keep-attention/KV-high-precision rule; training-only otherwise.

C1-024 | https://pytorch.org/blog/faster-diffusion-on-blackwell-mxfp8-and-nvfp4-with-diffusers-and-torchao | 2025–2026 | VERIFIED | 3 | 4 | 3 | **36**
NVFP4 selective-quant on FLUX/LTX: 1.55–1.68× speedup, LPIPS 0.44 vs MXFP8 0.11 — NVFP4 visibly lossier on pixels; selective layer exclusion required.
Mechanism: vision-path activations are quant-fragile (same family as C1-002 visual-KV finding, independent confirmation).
Maps: second vote for vision-encoder caution: quantize LLM decoder aggressively, ViT conservatively — matches Kevinma's BF16-ViT build choice.

C1-025 | https://aclanthology.org/2025.acl-long.1304 ["Give Me BF16 or Give Me Death?", Kurtic et al., ACL 2025] | 2025-07-01 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
500K+ evals across Llama-3.1 family: W8A8-FP8 effectively LOSSLESS at all scales; tuned W8A8-INT only 1–3% degrad (vs 10%+ in prior work); W4A16-INT (GPTQ+MSE-clip, 128-groups) rivals 8-bit; naive random-token calibration HURTS INT4 (needs OpenPlatypus-like data).
Mechanism: dynamic per-token acts + symmetric RTN weights + proper calibration = the accuracy recipe; calibration DATA is the load-bearing variable.
Maps: foundational citation for FP8-first policy + calibration-in-Indic-scripts requirement; cost tables (H100 sync inference $/query) feed S5 cost model.

C1-026 | https://aclanthology.org/anthology-files/pdf/acl/2026.acl-long.1854.pdf [MXFP PTQ benchmark, Huawei] | 2026 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
MXFP8 near-lossless across tasks/modalities; MXFP4 = substantial degradation (open challenge); W4A8 transition is the inflection point; rotation methods (QuaRot/SpinQuant) WORSEN MXFP4 (RTN ppl 8.27 beats QuaRot 10.34); KEY: same W4A4 on Qwen2.5-VL-7B LLM → 3% recovery-rate drop, on ViT → only ~1%.
Mechanism: LLM decoder is the quant-fragile part of a VLM, not the ViT — complements C1-024 (which tested generative vision, not VLM encoders).
Maps: quantize the 2B VLM's ViT freely-ish, spend the error budget protecting the Qwen decoder + projector — precise guidance for our quant plan. Rotation-based PTQ barred for MXFP4.

C1-027 | https://developers.redhat.com/articles/2025/04/01/enable-faster-vision-language-models-quantization | 2025-04-01 | VERIFIED | 5 | 4 | 5 | **100** | §INTEG
LLM-Compressor VLM quants (Pixtral, Qwen2-VL-72B, Qwen2.5-VL-3B/7B/72B): >99% accuracy @8-bit, ~98% @4-bit; up to 3.5× throughput (72B gains most; 3B only 1.1–1.5×); INT-W4A16 best for memory-bound Qwen-VL; low-latency favors W4A16 (1.3–1.7×), high-throughput favors W8A8; A6000 gains most.
Mechanism: small VLMs are less bandwidth-starved → modest quant speedups; format choice depends on latency-vs-throughput SLO.
Maps: temper expectations — our 2B VLM gets ~1.1–2× (matches C1-001's 2.0–2.4× on TRT), not 3.5×; for interactive single-page OCR pick W4A16, for bulk OldScan reprocessing pick W8A8. Off-the-shelf quantized Qwen-VL checkpoints exist for vLLM deploy.

C1-028 | https://docs.vllm.ai/en/v0.16.0/features/quantization/fp8 + https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/fp8.md | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
vLLM FP8 W8A8: 2× memory cut, up to 1.6× throughput, minimal accuracy loss; dynamic per-token (no calibration needed) via llm-compressor; static per-channel weights; W8A16 fallback on Ampere (Marlin); needs whole-model load before quant (memory caveat).
Mechanism: zero-calibration FP8 = fastest path to quantized serving.
Maps: vLLM is the low-friction alternative to TRT-LLM for our 2B VLM (no engine build); caveat — dynamic FP8 uses default calibration-free scales, so STILL gate on Indic CER (C1-030 shows why calibration-free can bite non-English).

C1-029 | https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community | 2025-03-25 | VERIFIED | 3 | 3 | 3 | **27**
vLLM FP8 (Neural Magic/Anyscale): up to 2× ITL (Llama-3-70B), 3× throughput via bigger batches, >99% accuracy preserved on Open LLM Leaderboard v1.
Mechanism: batch-size expansion from memory savings is the real throughput engine.
Maps: same lesson as C1-027; English-only accuracy evidence — discount one relevance point for our scripts.

C1-030 | https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct-AWQ | 2024–2026 (model card, live) | VERIFIED | 5 | 3 | 4 | **60** | §INTEG
Official Qwen2-VL-2B quant card: BF16 DocVQA 88.34 → GPTQ-Int8 88.28 (lossless) → GPTQ-Int4 87.21 (−1.1) → AWQ 86.96 (−1.4); MMMU 41.88→41.33/39.22; speed/memory table (A100: BF16 4.68GB/35tok-s rise to 31.6GB @30K ctx; INT4 2.91GB).
Mechanism: vendor-measured 8-bit-lossless / 4-bit-~1pp on DOCUMENT QA (DocVQA = our task family).
Maps: strongest direct evidence that INT8/GPTQ-Int8 serving of our 2B OCR VLM costs ~nothing on document QA; memory table sizes the L4/A10G serve tier (S5). DocVQA is English — apply Indic gate before promotion.

C1-031 | https://docs.vllm.ai/en/v0.9.0/features/quantization/modelopt.html + v0.9.2 API modelopt page | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64**
vLLM natively loads ModelOpt FP8/NVFP4 checkpoints (`quantization="modelopt"`; nvidia/Llama-3.1-8B-Instruct-FP8 example); FP8 KV-cache scales loadable; NVFP4 supported.
Mechanism: ModelOpt = single quantize-once, serve-anywhere (TRT-LLM AND vLLM) format.
Maps: quantize our fine-tuned 2B VLM once in ModelOpt (WITH Indic calibration, C1-062), deploy to TRT-LLM (prod) or vLLM (dev) interchangeably.

C1-032 | https://developer.nvidia.com/blog/model-quantization-turn-fp8-checkpoints-into-high-performance-inference-engines-with-nvidia-tensorrt | 2026-06-09 / 2026-07-09 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
ModelOpt→ONNX→TensorRT FP8 CLIP path: text-enc −34%, image-enc −50% size; engines −48%/−34%; RTX 6000 Ada 1.39×/1.45× speedup; `--stronglyTyped` preserves FP8 annotations through trtexec; notes LLM path differs (via TRT-LLM tutorial).
Mechanism: end-to-end vision-encoder FP8 recipe with measured vision (not LLM) numbers.
Maps: if we FP8 the ViT side of PaddleOCR-VL-0.9B or Qwen2-VL ViT via classic TensorRT (non-LLM path), this is the runbook; attention-scale FP32-roundtrip caveat documented.

C1-033 | https://docs.nvidia.com/nemo-framework/user-guide/25.09/model-optimization/quantization/quantization.html (+24.09/24.12/25.07) | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64**
NeMo PTQ: FP8 / INT8-SmoothQuant / INT4-AWQ via ModelOpt, lightweight calibration, qnemo checkpoint → TRT-LLM engine via nemo.export; `no_quant` export for baseline; families covered Llama/Mistral/GPT/Nemotron/Gemma/StarCoder.
Mechanism: framework-native quant→serve loop (calibrate → qnemo → engine) with built-in baseline comparison.
Maps: if W6 uses NeMo for SFT, PTQ is one CLI (`nemo llm ptq`) — adopt the `no_quant`-baseline-then-quant diff as mandatory gate procedure.

C1-034 | https://github.com/NVIDIA/Model-Optimizer/blob/main/modelopt/torch/quantization/config.py | 2026 (main) | VERIFIED | 3 | 4 | 3 | **36**
ModelOpt config surface: FP8_DEFAULT_CFG, INT4_AWQ_CFG, W4A8_AWQ_BETA_CFG; FPx (E,M) emulation; KV-cache amax hardcode note; NVFP4 FP8-scale-sweep option.
Mechanism: exposes exactly the block-scaling / sweep knobs C1-008 and C1-021 recommend.
Maps: implementer's reference for the quant configs in our runbook; no direct CER evidence.

C1-035 | https://huggingface.co/docs/diffusers/v0.36.0/en/quantization/modelopt | 2025–2026 | VERIFIED | 2 | 3 | 2 | **12**
ModelOpt dtype list (int8/fp8/int4/nf4/nvfp4) via diffusers docs.
Mechanism: corroborates format support.
Maps: marginal; kept for format inventory completeness.

C1-036 | https://www.spheron.network/blog/tensorrt-model-optimizer-modelopt-quantization-guide | 2026-05-28 | VERIFIED | 2 | 4 | 2 | **16**
Third-party ModelOpt guide (FP8 H100 ~47% figure cited; INFERENCE: estimated values, treat as directional).
Mechanism: tutorial-level.
Maps: backup tutorial pointer only; prefer primary docs C1-032/C1-033.

C1-037 | https://docs.clore.ai/guides/gpu-devops/tensorrt-llm.md | 2025–2026 | VERIFIED | 3 | 3 | 3 | **27**
Field report: TRT-LLM 2–4× vs HF transformers, +30–50% vs vLLM batch serving; VRAM table (8B: 16/8/4GB FP16/INT8/INT4); RTX4090 Llama-8B ~3.5K tok/s FP16 → 6.2K INT4-AWQ.
Mechanism: independent corroboration of C1-001/C1-007 magnitudes.
Maps: cross-check on speedup claims; VRAM table seeds S5 math. INFERENCE: vendor-adjacent hosting blog — discount precision.

C1-038 | https://arxiv.org/html/2505.08620v1 [Resource-Efficient LMs survey] | 2025-04+ | VERIFIED | 2 | 3 | 2 | **12**
Survey table: TRT-LLM/vLLM/SGLang quant-method coverage (AWQ/SmoothQuant/FP8/INT8/INT4); notes sub-3-bit degrades fast.
Mechanism: landscape confirmation.
Maps: background only.

C1-039 | https://docs.vllm.ai/projects/vllm-omni/en/v0.26.0/user_guide/quantization/fp8/ | 2026 | VERIFIED | 3 | 4 | 3 | **36**
vLLM-Omni FP8: per-tensor online scaling default (no calibration); static scales optional; quality-sensitive layers (img_mlp) stay BF16 via ignored_layers; Blackwell FlashInfer + quack fused bias kernel.
Mechanism: vendor pattern for "keep vision-sensitive layers high-precision" — third independent vote alongside C1-002/C1-024.
Maps: adopt ignored_layers for ViT projector + LM head when FP8-serving our VLM; Blackwell kernel notes matter if serving on B200/Thor.

C1-040 | https://docs.vllm.ai/en/v0.21.0/features/quantization/fp8 | 2026 | VERIFIED | 2 | 4 | 2 | **16**
vLLM FP8 latest-docs restatement (2× mem, 1.6× tput, minimal accuracy impact).
Mechanism: confirms C1-028 current.
Maps: version-freshness anchor only.

---

## S3 — Quantization × Indic / non-English scripts (S3-041…S3-054)

C1-041 | https://arxiv.org/pdf/2608.11786 [Language-Conditional Dequantization, Thomas/Prathama, Aug 2026] | 2026-08-12 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
English-calibrated INT3-GPTQ on Qwen2.5-3B/Llama-3.2-3B: per-language ppl degradation 1.35× (English) → 4.37× (Arabic); 2–4× larger non-English gaps sub-4B; LCD post-hoc adapters recover 70–83% ppl gap (non-Latin) + 17–28% GlobalMMLU gap, beating language-agnostic correction 3–9 pts on distant languages.
Mechanism: quantization error is language-anisotropic — English calibration bakes in Latin-centric scales; tiny language-conditional residuals fix it post-hoc WITHOUT re-quantization.
Maps: DIRECT threat model for Santali (Ol Chiki)/Kashmiri (Nastaliq): aggressive quant on our 2B VLM will hit them 2–4× harder than Hindi/English. Mitigations in order: (1) multilingual calibration (C1-042), (2) LCD-style adapters if already deployed, (3) never INT3-class on tail scripts.

C1-042 | https://arxiv.org/pdf/2601.18306 [Calibrating Beyond English, Jan 2026] | 2026-01-26 | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
Llama-3.1-8B AWQ-4bit: multilingual calibration beats English-only (ppl 14.64 vs 19.65 vs 15.82 FP16-pattern figure); non-English sets win up to +3.52 ppl on Llama-GPTQ; traces failures to activation-range differences across languages; Marchisio-2024 confirmed (low-resource non-Latin hit hardest).
Mechanism: calibration-set language sets the scale factors; English-only scales mismatch tail-script activation ranges.
Maps: HARDEST REQUIREMENT in this lane — every PTQ/AWQ/GPTQ calibration corpus for our VLM MUST contain Ol Chiki + Nastaliq + Mayek + Odia samples; cost ≈ zero (a few hundred pages), payoff = the entire tail-script CER. Actionable tomorrow.

C1-043 | https://aclanthology.org/2024.findings-emnlp.935.pdf [Marchisio et al., How Does Quantization Affect Multilingual LLMs?, EMNLP 2024] | 2024-11-09 | VERIFIED | 4 | 2 | 3 | **24**
Foundational result (cited by C1-041/C1-042): quantization disparately degrades non-English, worst at low-resource/non-Latin scales; W4 non-English worse on average.
Mechanism: established the disparate-harm phenomenon.
Maps: recency=2 (2024, outside 2025–26 window — kept as cited foundation, flagged); substance already superseded by C1-041/C1-042 for actionability.

C1-044 | https://aclanthology.org/2026.propor-1.108.pdf [Lost in Quantization: Activation Outliers, Silva 2026] | 2026 | VERIFIED | 4 | 5 | 3 | **60** | §INTEG
Llama-3-8B EN vs PT-BR: INT8-with-outlier-handling preserves both; NAIVE FP8 cast degrades English +18% vs PT-BR +3.9% — English's sparse extreme outliers (>35) break FP8 range while PT-BR's compact distribution survives.
Mechanism: outlier SHAPE is language-dependent; naive casting without outlier handling is the failure mode, not FP8 itself.
Maps: flips the naive assumption ("English is safe, tail scripts risky") — for OUR scripts the lesson is: profile per-script activation outliers BEFORE choosing FP8 vs INT8-SmoothQuant; SmoothQuant's outlier-migration (C1-001 winner) is theoretically the right tool for spiky tail-script distributions.

C1-045 | https://arxiv.org/pdf/2511.20478 [NVIDIA Nemotron-Parse 1.1, Nov 2025] | 2025-11-26 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
Nemotron-Parse-1.1: 885M encoder-decoder doc-parse/OCR (256M LM decoder), SOTA-class OmniDocBench (edit-dist 0.131 vs MinerU 0.133, GOT-OCR2 0.287, olmOCR 0.326), table TEDS tracked; ships optimized NIM container; Parse-TC tiny variant (833 output-tok) for production.
Mechanism: sub-1B specialist + layout-aware extraction + reading order beats 70B generalists on parse metrics.
Maps: sets the efficiency bar our PaddleOCR-VL-0.9B lane must clear; NIM-container precedent = our deploy template; table metrics relevant to mixed tables in OldScan pages.

C1-046 | https://build.nvidia.com/search/models?filters=publisher%3Anvidia&q=Nemotron (+https://build.nvidia.com/nvidia/nemotron-ocr-v1/modelcard) | 2026-03/2026-06 | VERIFIED | 4 | 5 | 3 | **60** | §INTEG
NVIDIA NIM model inventory: nemotron-ocr-v2 (SOTA multilingual OCR, 338K API calls/30d, downloadable, Jun 2026), nemotron-ocr-v1 (206K calls), page-elements/graphic-elements detectors, parse models.
Mechanism: NVIDIA treats OCR as first-class NIM microservices with real usage volume.
Maps: competitor/baseline reference for R6 refresh + proof that NVIDIA-stack OCR serving is production-trodden; INFERENCE: "multilingual" here likely Latin+CJK-heavy — verify Ol Chiki/Nastaliq coverage before citing as Indic evidence.

C1-047 | https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-nano-12b-v2-vl + https://build.nvidia.com/nvidia/nemotron-nano-12b-v2-vl + https://arxiv.org/html/2511.03929v1 | 2025-10-28 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
Nemotron Nano 12B v2 VL: hybrid Mamba-Transformer 12B VLM, 9.83M OCR training samples (5.3TB), DocVQA 94.39 / ChartQA 89.72 / OCRBench 85.6, +35% throughput on multi-page docs vs prior; checkpoints released in BF16 AND FP8 AND FP4.
Mechanism: hybrid architecture cuts long-doc cost; vendor pre-quantized FP8/FP4 checkpoints = existence proof of served quantized doc-VLMs.
Maps: (a) multi-page OldScan throughput technique to watch (token reduction); (b) FP8/FP4 official checkpoints validate our quant-serve plan; (c) 9.8M-sample OCR training scale contextualizes our fine-tune data needs (we need far less — adaptation, not pretraining).

C1-048 | https://arxiv.org/html/2409.12191v2 [Qwen2-VL paper] | 2024-09 (foundation) | VERIFIED | 4 | 2 | 3 | **24**
Qwen2-VL-2B: 675M ViT + 1.5B LLM, DocVQA 90.1, MTVQA 20.0 (multilingual text-VQA WEAK even at pretrain — 20.0 vs 72B's higher), M-ROPE, 3-stage training (ViT-freeze → all → LLM-only).
Mechanism: 2B's multilingual doc reading is its weakest axis out of the box — exactly our fine-tune target.
Maps: recency=2 (2024 foundation, flagged); justifies LoRA fine-tune on Indic doc pages (S6) rather than zero-shot hope; training-stage order informs our curriculum.

C1-049 | https://huggingface.co/TimmyOVO/PaddleOCR-VL-Quantization | 2025–2026 | VERIFIED | 4 | 3 | 4 | **48**
Community PaddleOCR-VL quant note: dense Ernie decoder (18 layers, hidden 1024) activates fewer params/token, <10GB memory, near-parity quality on most docs.
Mechanism: small dense decoder = quant-friendly (fewer active params → less error accumulation than MoE).
Maps: supports INT8/FP8 serving of PaddleOCR-VL-0.9B on 16GB cards for our pipeline; INFERENCE: community claim, gate on our CER before trusting "near-parity."

C1-050 | https://github.com/PaddlePaddle/PaddleOCR/blob/main/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md | 2026 (1.5 Jan 2026, 1.6 May 2026) | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
PaddleOCR-VL: 0.9B = NaViT-dynamic-res ViT + ERNIE-4.5-0.3B; v1.5 OmniDocBench-v1.5 94.5% + irregular-shape boxes + seal rec; v1.6 (May 2026) current; full pipeline ≠ raw VLM (layout/order modules matter); supports vLLM/SGLang/FastDeploy serving + local Transformers.
Mechanism: dynamic-res ViT handles our mixed scan sizes; pipeline (det→order→rec) is where degraded scans win or lose.
Maps: PaddleOCR-VL-0.9B is servable TODAY via vLLM (ties C1-027/028/031); vLLM FP8 path + Indic calibration (C1-042) = candidate OldScan/Odia workhorse. Version velocity (1.5→1.6 in 4 months) noted for R6.

C1-051 | https://www.paddleocr.ai/latest/en/version3.x/inference_deployment/local_inference/high_performance_inference.html (+v3.3.1, main EN) | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
PaddleOCR high-perf inference: one-flag `--enable_hpi` auto-selects backend (PaddleInference/OpenVINO/ONNX-RT/TensorRT) + FP16; needs matching TensorRT (8.6.1.6/CUDA11.8; CUDA12.6 lacks TRT backend); ONNX auto-convert.
Mechanism: backend autotune removes manual TRT plumbing for the classical (non-VLM) PP-OCR stack.
Maps: our paddleocr_indic probe engine could be re-run under HPI+TensorRT+FP16 for a like-for-like accelerated baseline; env constraint (CUDA11.8/TRT8.6) recorded for repro.

C1-052 | https://github.com/PaddlePaddle/PaddleOCR/blob/main/deploy/slim/quantization/README_en.md + https://www.paddleocr.ai/v2.10.0/en/ppocr/model_compress/quantization.html | 2025–2026 | VERIFIED | 3 | 3 | 4 | **36** | §INTEG
PaddleSlim QAT path for PP-OCR det/rec (offline + online QAT, export INT8-range model).
Mechanism: quantization-AWARE training recovers what PTQ loses — the escalation if PTQ fails our Indic gate.
Maps: fallback plan: if PTQ INT8 on Ol Chiki/Nastaliq fails CER gate, QAT the rec head (small, cheap) rather than abandoning quantization.

C1-053 | https://huggingface.co/PaddlePaddle (org: PP-OCRv6 50-lang 1.5M–34.5M params; PaddleOCR 3.5 Transformers backend; PaddleOCR-VL-1.6) | 2026-05/06 | VERIFIED | 3 | 5 | 2 | **30** | §INTEG
Paddle velocity: VL-1.6 (May 2026), PP-OCRv6 50-language tiny models (Jun 2026), 3.5 Transformers-backend release.
Mechanism: ecosystem moving to HF-Transformers compatibility (easier TRT/vLLM interop).
Maps: watch-item for Lane A/R6; Transformers backend simplifies any future TRT-LLM ingestion of Paddle models.

C1-054 | https://www.paddleocr.ai/v2.10.0/en/infer_deploy/benchmark.html | 2025 | VERIFIED | 2 | 3 | 2 | **12**
PP-OCRv2/v3 bench: mobile whole-system 8.1MB, server 155MB; T4 GPU 111–200ms end-to-end (Chinese/English).
Mechanism: classical-stack latency anchor.
Maps: order-of-magnitude comparison vs VLM serving (100× heavier); not Indic, dated — background only.

---

## S4 — NIM microservices: deploy + economics (S4-055…S4-068)

C1-055 | https://www.nvidia.com/en-sg/ai-data-science/products/nim-microservices + https://developer.nvidia.com/nim | 2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
NIM = containerized model + optimized engine (TRT-LLM/vLLM/SGLang/TensorRT) + OpenAI-compatible API + runtime deps; deploy-anywhere (cloud/DC/workstation/edge/RTX); 5-min deploy; supports community + fine-tuned models; free dev prototyping via build.nvidia.com.
Mechanism: removes engine-plumbing labor; fine-tuned-model support means OUR LoRA adapters can ship as NIMs.
Maps: recommended wrapper for any hackathon demo endpoint AND production handoff — standard API, NVIDIA-validated engines, no custom server code.

C1-056 | https://www.nvidia.com/en-gb/ai-data-science/products/nim-microservices (perf panel) | 2026 | VERIFIED | 4 | 4 | 3 | **48**
NIM perf panel: Llama-3.1-8B on 1×H100, 200 concurrent: NIM-ON FP8 1201 tok/s @32ms ITL vs NIM-OFF FP8 613 tok/s @37ms — ~2× throughput from NIM's tuned serving.
Mechanism: continuous batching + tuned kernels compound the raw FP8 win.
Maps: serving-stack choice ≈ model choice in $/page impact — budget the full 2× when costing NIM vs naive HF-serve.

C1-057 | https://docs.nvidia.com/nemo/microservices/25.8.0/run-inference/deployment-management/deploy-nim.html | 2025-08 | VERIFIED | 3 | 4 | 3 | **36**
NeMo Deployment Management API for NIM (Python SDK + cURL model-deployments; status polling).
Mechanism: programmatic fleet ops for per-language NIMs.
Maps: if we ship 3–4 script-specialist NIMs (Devanagari-shared, Nastaliq, Ol Chiki, Mayek), this is the deployment API; P1, not W6.

C1-058 | https://costbench.com/software/llm-api-providers/nvidia-nim | 2026-08-19 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
NIM pricing (Aug 2026, medium confidence): hosted $0.90–1.20/1M tokens blended (Llama-70B $0.90, Mixtral-8x22B $1.20); free dev credits; Enterprise = AI Enterprise license + DGX Cloud custom.
Mechanism: usage-based hosted vs license-based self-host.
Maps: input to S5 $/1M-pages model — hosted-NIM price anchor for 70B-class; our 2B self-hosted cost will sit far below (compute math in S5).

C1-059 | https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/pricing.html | 2026-09-02 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
AI Enterprise list: $4,500/GPU/yr subscription ($1,125 EDU/Inception), 5-yr $18K; cloud CSP pay-go $1/GPU-hr + instance; DGX Cloud H100 ~$37K/mo. NIM production self-host REQUIRES AI Enterprise (dev/test free).
Mechanism: the license is the fixed-cost floor for "official" NIM self-hosting.
Maps: CRITICAL cost-law input — $4.5K/GPU/yr amortizes to ~$0.51/GPU-hr floor before compute; for a single-GPU 2B-OCR service this dominates vs raw cloud GPU ($0.35–1.00/hr on T4/L4/A10G). Recommendation: prototype on free dev NIMs, produce on TRT-LLM/Triton WITHOUT the NIM wrapper unless enterprise support is needed.

C1-060 | https://www.spheron.network/blog/nvidia-nim-pricing-vs-self-hosted-vllm-cost-2026 + https://cloudai.pt/nvidia-nim-economics-where-self-host-beats-every-api | 2026-06 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
Third-party NIM-vs-vLLM economics: NIM priced $4.5K/GPU/yr under AI Enterprise; self-host NIM on RunPod H100 $2.69/hr ≈ $1,950/mo; crossover math favors self-host past sustained token volumes.
Mechanism: independent validation of C1-059's arithmetic + utilization-crossover framing.
Maps: corroborates the S5 recommendation; INFERENCE: vendor-adjacent blogs — treat exact crossover points as directional, recompute with our page-token profile.

C1-061 | https://apis.io/plans/nvidia-nim/nvidia-nim-plans-pricing + https://decodethefuture.org/en/nvidia-nim-api-pricing-limits-guide | 2026-05 | VERIFIED | 3 | 5 | 3 | **45**
NIM dev tier: free, 1,000 signup credits, 40 req/min, 100+ models via integrate.api.nvidia.com; production = $4.5K/GPU/yr or ~$1/GPU-hr cloud.
Mechanism: free prototyping envelope quantified.
Maps: we can prototype the OCR endpoint on free NIM credits TODAY (no budget) within 40rpm — enough for probe-scale validation, not bulk.

C1-062 | https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/nvidia-nim-for-nvidia-nemotron-cosmos--microsoft-trellis-now-available-in-azure-/4463262 | 2025-10-28 | VERIFIED | 3 | 4 | 3 | **36**
Llama-3.1-Nemotron-Nano-VL-8B as Azure NIM: compact doc-intel VLM (report-gen, Q&A, visual understanding, document intelligence), low-latency/high-efficiency/TCO positioning.
Mechanism: cloud-NIM path for doc VLMs exists on Azure AI Foundry.
Maps: alternative demo-hosting path (no GPU procurement); English/multilingual coverage TBD — same discount as C1-046.

C1-063 | https://www.nvidia.com/en-us/data-center/products/ai-enterprise/ | 2026 | VERIFIED | 2 | 4 | 2 | **16**
AI Enterprise positioning (5× utilization, 20× throughput claims).
Mechanism: marketing-level.
Maps: background; do not cite numbers without primary benchmark.

C1-064 | https://developer.nvidia.com/dynamo + https://www.nvidia.com/en-us/ai/dynamo/ | 2025–2026 | VERIFIED | 4 | 5 | 3 | **60** | §INTEG
Dynamo = open-source disaggregated serving (successor to Triton Inference Server for LLM scale): prefill/decode split pools, KV-aware router, NIXL transfer, KV block manager, Grove/K8s, backends SGLang/TRT-LLM/vLLM; claims 2× Llama-on-Hopper revenue, 30×+ R1 tokens/GPU on GB200, 7× disagg throughput (DeepSeek-R1/Blackwell), 50× MoE on GB300-vs-Hopper.
Mechanism: phase-disaggregation + cache-aware routing attack exactly the utilization waste C1-066 quantifies.
Maps: overkill for single-2B-VLM W6, but THE design pattern if OldScan bulk reprocessing scales to multi-GPU; KV-aware routing directly reusable for repeated-form inference (same govt-form layout across pages = prefix-cache hits).

C1-065 | https://docs.nvidia.com/dynamo/user-guides/disaggregated-serving.md | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
Disagg-serving docs: helps when prefill-heavy (long prompts/retrieval) vs decode-heavy diverge; NOT auto-better — "for small models, short prompts, low concurrency, aggregated may be simpler and faster"; needs RDMA-class KV transfer cross-node.
Mechanism: honest scope-limits from the vendor itself.
Maps: decision rule for us — our 2B single-page OCR (short prompt+image prefill, short transcription decode, low concurrency) likely does NOT need disaggregation; single-GPU aggregated TRT-LLM/Triton is the right complexity. Saves us from over-engineering.

C1-066 | https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Dynamo-Open-Source-Library-Accelerates-and-Scales-AI-Reasoning-Models/default.aspx | 2025-03-18 | VERIFIED | 3 | 3 | 2 | **18**
Dynamo launch claims (2× Hopper Llama, 30× R1/GB200).
Mechanism: press-release numbers.
Maps: background; superseded by C1-064/065 for decisions.

C1-067 | https://arxiv.org/abs/2606.17081v1 [Price of Anarchy in Disaggregated Inference, Dynamo case study] | 2026-06-11 | VERIFIED | 2 | 5 | 2 | **20**
Game-theoretic analysis of Dynamo disagg serving on 3×B200 (v0.9.0): prefill/decode resource games, caching games, routing games.
Mechanism: academic lens on disagg trade-offs.
Maps: background; supports C1-065's "not auto-better" with theory.

C1-068 | https://www.spheron.network/blog/nvidia-dynamo-disaggregated-inference-guide + https://www.infoq.com/news/2025/12/nvidia-dynamo-kubernetes | 2025-12/2026-03 | VERIFIED | 2 | 4 | 2 | **16**
Third-party Dynamo summaries (7× claim, K8s/Grove notes).
Mechanism: secondary.
Maps: pointers only.

---

## S5 — Serving cost models ($/1M pages) (S5-069…S5-080)

C1-069 | https://arxiv.org/pdf/2606.11690 [Beyond Per-Token Pricing, Patil, Jun 2026] | 2026-06-10 | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
42 vLLM runs on H100: effective $/M tokens spans $0.21–$15.25 (up to 36×) on IDENTICAL hardware driven by offered load λ (1→25 rps: Mixtral-8x7B $15.25→$0.87); under-utilization penalty 2.5–24× at enterprise 1–10 rps; formula Ceff = Pgpu×10⁶/(TPS×3600); vllm-cost-meter tool released.
Mechanism: cost is dominated by concurrency/utilization, NOT model size or GPU price — idle GPUs bill the same per hour while emitting few tokens.
Maps: THE cost-model law for our $/1M-pages estimate — batch OldScan backlogs to saturation (continuous batching, off-peak queues) or pay 10–30×. Our estimate MUST quote a utilization assumption; idle-interactive vs saturated-batch differ by an order of magnitude. Tool reusable for our own measurement.

C1-070 | https://arxiv.org/html/2506.04645v1 [Inference economics of LMs, Erdil-style] | 2025-06 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
Roofline cost theory: Fireworks serves Llama-3-8B @~400 tok/s for $0.20/M, 70B @~150 tok/s $0.90/M, within ~2× of raw GPU-rental cost; each NVIDIA GPU generation +~25% tok/s at fixed $/token.
Mechanism: competitive API pricing ≈ 1–2× raw compute — self-host must beat ~$0.20/M-output (8B-class) to be worth operating.
Maps: sets the beat-this bar: our 2B-VLM self-host $/M-pages must land well under API-parity; +25%/gen rule lets us project L4→H100→B200 serving costs.

C1-071 | https://a16z.com/llmflation-llm-inference-cost | 2025–2026 (verified 2026-09-01) | VERIFIED | 3 | 5 | 3 | **45**
LLMflation: inference $/equal-performance down 10×/year; 1000× in 3 years (GPT-3-era → Llama-3.2-3B @ $0.06/M via Together.ai).
Mechanism: algorithmic + hardware compounding.
Maps: timing insight — serving costs decay fast; do NOT over-commit to long GPU contracts for the OCR service; re-price quarterly.

C1-072 | http://jarvislabs.ai/blog/h100-price | 2026-03/04 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
H100 rental $2.00–9.98/hr (Jarvislabs $2.69, RunPod $2.99, Baseten $9.98 managed); worked inference example: Llama-70B @3.5–4K tok/s → 1M tok/day ≈ 2–3 GPU-hrs ≈ $269/mo; 13B-model ≈ $112/mo; cloud-vs-buy break-even ~10.4K GPU-hrs (~7 wks 8×H100) or 16 mo (24/7 inference).
Mechanism: concrete $/M-tok arithmetic with throughput anchors.
Maps: template for OUR $/1M-pages math (NOTE_SERVE_COST.md works it with 2B-VLM tok/s + page-token profile); break-even rule says rent, don't buy, for W6-scale.

C1-073 | https://aimultiple.com/gpu-index | 2026-08-25 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
69-provider GPU index (Aug 2026): H100 median $3.38/hr (was $7+ early 2024; neocloud down, hyperscalers $10+); A100 ~$1.86; L40S $1.54; RTX 4090 $0.43 (cheapest train-class); B200/B300 listings 2× up as hyperscalers list; 1-yr reserved −5–38%.
Mechanism: market-wide price discovery, monthly methodology.
Maps: PRIMARY GPU-price source for S5 model — L4/A10G-class for 2B serve (~$0.33–1.00/hr, C1-074), A100 for LoRA (~$1.10–1.86), H100 only if batch-throughput math demands it.

C1-074 | https://vibeengines.com/tools/gpu-rental-prices + https://www.nvidia.com/en-us/launchables/pricing/ (Brev) + https://cloudgpuprices.com/instances + https://gpuperhour.com/rent/h100-pcie-80gb | 2026-08/09 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
Convergent small-GPU prices: T4 $0.35–0.53, L4 $0.17–0.70 (Brev GCP $0.17!), A10G ~$1.00–1.12, A100-40GB $1.10 (Lambda) –2.50, H100 $2.50–5.95 (median $2.90); Baseten serverless per-minute (L4 $0.014/min, A100 $0.067/min).
Mechanism: 2B-VLM inference fits 8–16GB → T4/L4/A10G serve tier is 5–15× cheaper per hour than H100.
Maps: load-bearing for S5: serve the quantized 2B VLM on L4 ($0.33–0.70) or A10G ($1.00), NOT H100 — the single biggest $/page lever. Brev $0.17 L4 spot noted opportunistically.

C1-075 | https://www.aquanode.io/tools/gpu-recommender/qwen/qwen2-vl-2B-instruct | 2026 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
Qwen2-VL-2B VRAM ledger: BF16 4.1GB weights → 4.9GB required; FP8 2.1→2.5GB; INT4 1.0→1.2GB; cheapest fit RTX 3070 $0.05/hr; +50% memory note for LoRA fine-tune.
Mechanism: measured weight→VRAM map for OUR model (KV/act/fragmentation included).
Maps: anchors both S5 (serve fits ANY 8GB card; FP8 halves it) and S6 (LoRA ≈ 1.5× inference VRAM ≈ 7–8GB BF16 → single T4/L4 trains it).

C1-076 | https://arxiv.org/html/2606.11690v1 (companion HTML) | 2026-06 | VERIFIED | 2 | 5 | 2 | **20**
Same-paper HTML rendering (duplicate evidentiary value).
Mechanism: n/a.
Maps: kept as access-pointer only; all weight on C1-069.

C1-077 | https://www.lesswrong.com/posts/mRKd4ArA5fYhd2BPb/observations-about-llm-inference-pricing | 2025-03-03 | VERIFIED | 3 | 3 | 3 | **27**
Open-model inference is a commodity: 10× price spreads per model; $0.03 fixed + $0.02/10B-params variable fit; 405B @ $0.90/M cheapest.
Mechanism: market structure corroboration of C1-070.
Maps: buy-vs-build framing: if any API serves Indic-OCR-VLM at commodity spread, benchmark-buy before building — but no such Indic specialist exists (our gap).

C1-078 | https://ufal.mff.cuni.cz/~odusek/inlg2025/inlg2025-main/pdf/2025.inlg-main.32.pdf + https://arxiv.org/html/2506.21901v1 | 2025–2026 | VERIFIED | 2 | 4 | 2 | **16**
Efficient-serving surveys (paged attention, chunked prefill, disagg, Sarathi-Serve token-budgets).
Mechanism: technique inventory behind C1-064/069 numbers.
Maps: background; implementers' reading list.

C1-079 | https://www.giiresearch.com/report/fbs1954918-ai-inference-market-size-share-growth-global.html | 2026 | VERIFIED | 1 | 4 | 1 | **4**
Inference market $103.7B (2025) → $312.6B (2034), 13% CAGR.
Mechanism: market sizing.
Maps: no technical actionability; dropped from integration (score 4).

C1-080 | https://gigagpu.com/rtx-5060-ti-16gb-qlora-training-speed (memory rows) | 2026-04-23 | VERIFIED | 3 | 5 | 3 | **45**
Blackwell-16GB VRAM anchors: Llama-8B QLoRA bs4/s2048 = 11.8GB peak; bs2/s4096 = 13.2GB; 14B = 14.5GB; Unsloth ≈ half time.
Mechanism: measured QLoRA VRAM scaling (batch × seq).
Maps: cross-check for S6 2B-VLM math (2B ≈ ¼ of 8B → ~4–6GB typical configs); Unsloth pointer.

---

## S6 — NeMo Customizer + LoRA VRAM math for 2B VLMs (S6-081…S6-094)

C1-081 | https://docs.nvidia.com/nemo/microservices/26.3.1/customizer/tutorials/understand-configurations-and-models.html | 2026 (v26.3.1) | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
Official NeMo Customizer GPU-sizing table: 1B → LoRA 1×16GB / Full 1×24GB; 3B → LoRA 1×24GB / Full 2×24GB; 7–8B → LoRA 1×40GB / Full 2–4×80GB; 13B → LoRA 1×80GB; LoRA needs 1.5× model-size disk; LoRA auto-deploys adapters onto existing NIMs.
Mechanism: vendor-certified LoRA-vs-full VRAM ladder + adapter-as-artifact workflow.
Maps: interpolates our 2B VLM LoRA at 1×16–24GB (single L4/A10G/T4-16GB) — the W6 GPU-budget answer in one table; adapter→NIM auto-deploy = per-script specialists without re-shipping base weights (Santali/Kashmiri/Odia adapters on one frozen 2B base).

C1-082 | https://docs.nvidia.com/nemo/microservices/latest/fine-tune/models/index.html | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
NeMo Customizer catalog: Llama-3.1/3.2, Nemotron-Nano-8B/9B, Phi-4, gpt-oss-20B, Qwen2.5-1.5B, Qwen3-0.6B, Mistral/Ministral — all Full-SFT + LoRA, sequence packing, NIM inference; 120B-class LoRA-only.
Mechanism: catalog proves LoRA+SFT+pack+NIM-deploy is a supported commodity path (though VLM entries are thin — LLM-centric).
Maps: process template for W6 SFT; caveat: VLM/LoRA coverage is LLM-first — verify Qwen2-VL-2B LoRA support in Customizer before committing vs LLaMA-Factory/Unsloth path (C1-085/086).

C1-083 | https://developer.nvidia.com/blog/fine-tune-and-align-llms-easily-with-nvidia-nemo-customizer | 2024-03-27 | VERIFIED | 2 | 2 | 2 | **8**
NeMo Customizer intro blog (2024 — dated, predates window).
Mechanism: historical.
Maps: kept as provenance pointer only; substance superseded by C1-081/082. Score 8, excluded.

C1-084 | https://medium.com/@f223442/fine-tuning-a-vision-language-model-on-a-free-kaggle-gpu-qlora-meets-document-ai-7baa6469db15 | 2026-05-12 | VERIFIED | 5 | 5 | 5 | **125** | §INTEG
Qwen2-VL-2B-Instruct QLoRA (NF4 + PEFT-LoRA) on 2×T4-16GB Kaggle FREE tier, Nougat arXiv pages→Markdown: ROUGE-1 0.18 (zero-shot) → 0.41, ROUGE-L 0.37 after 3 epochs/2.4K pairs; Gradio deploy.
Mechanism: EXISTENCE PROOF that our exact model + document task fine-tunes on free 16GB hardware with 2.3× quality jump; full-FP32 would need ~16GB weights-alone, QLoRA collapses it.
Maps: STRONGEST W6 feasibility evidence — Santali/Kashmiri/Odia page-tuning needs ~2–5K pairs (we HAVE 100–10K gold pairs/lang in official data) and fits a T4/L4; replicate this recipe per weak-script cell with CER (not ROUGE) as the gate.

C1-085 | https://medium.com/ai-insights-cobet/fine-tuning-the-qwen2-vl-model-a-comprehensive-guide-75e86cdcfc2d + https://github.com/zhangfaen/finetune-Qwen2-VL | 2024-09/2025-02 | VERIFIED | 4 | 3 | 4 | **48**
LLaMA-Factory Qwen2-VL-2B LoRA recipe: ≥12GB GPU, lora_target=all, bs2 × accum4, Colab-able; zhangfaen repo adds bf16+fp32 MIXED precision improving val loss + Qwen2.5-VL-3B + video support.
Mechanism: concrete hyperparameter starter (rank/alpha/targets/precision) + mixed-precision trick.
Maps: W6 starter config for the 2B LoRA runs; 12GB floor corroborates C1-081 interpolation; mixed-precision note is a free quality lever.

C1-086 | https://huggingface.co/unsloth/Qwen2-VL-2B-Instruct (+https://medium.com/@matteo28/qlora-fine-tuning-with-unsloth-a-complete-guide-8652c9c7edb3, Dec 2025) | 2025–2026 | VERIFIED | 4 | 4 | 4 | **64** | §INTEG
Unsloth Qwen2-VL-2B: free T4 Colab notebooks (2B AND 7B), 1.8–2.4× faster / 40–70% less memory; 3B-class QLoRA peaks 6–8GB vs 20–24GB full; 1.28% trainable params typical.
Mechanism: kernel-level efficiency (manual backprop, fused LoRA) without accuracy cost.
Maps: default training stack recommendation for W6 2B-LoRA: Unsloth + QLoRA on single 16GB card; halves step-time vs HF+PEFT (matters on rented GPUs at $0.35–1.00/hr).

C1-087 | https://qwenlm-qwen.mintlify.app/finetuning/qlora | 2025–2026 | VERIFIED | 4 | 3 | 4 | **48**
Official Qwen Q-LoRA table (Qwen-7B: 11.5GB@s256 → 13.9GB@s2048 → 23.5GB@s8192; 1.8B fits 11–12GB cards; Int4-train peak 13–14GB for 7B).
Mechanism: vendor seq-length→VRAM curve.
Maps: scale-down anchor — 2B-VLM at page-image token loads (≈1–2K visual + 0.5K text tokens) sits ≈ s1024–2048 band → ~6–9GB with QLoRA (consistent with C1-075/080/086 triangulation in NOTE_LORA_VRAM.md).

C1-088 | https://medium.com/%40minahilmohsin908/fine-tuning-vision-language-models-vlms-with-qlora-from-document-images-to-clean-markdown-b4607db85e7c | 2025–2026 | VERIFIED | 3 | 4 | 3 | **36**
VLM-QLoRA doc summary: full-FT 2B ≈ 16GB FP16 vs QLoRA 6–8GB, 3–5× faster, instant adapter switching.
Mechanism: corroborates C1-084/086 magnitudes from a second practitioner source.
Maps: adapter-switching property is architecturally load-bearing — ONE base + N script adapters served via Triton LoRA (C1-012), matching the script-router design (R7 tree).

C1-089 | https://www.spheron.network/blog/gpu-vram-requirements-fine-tune-llm-2026 | 2026 | VERIFIED | 4 | 5 | 4 | **80** | §INTEG
2026 VRAM-math guide: full vs LoRA vs QLoRA ladder 7B→70B (16× spread by method); rule components (weights + grads + Adam states 2× + activations ×seq ×batch).
Mechanism: general formula to derive any (model, method, seq, batch) cell.
Maps: METHOD source for NOTE_LORA_VRAM.md's 2B-VLM table — lets W6 planners recompute VRAM for any rank/seq/batch without new research.

C1-090 | https://github.com/EdwardNguyen2854/qlora-starter-kit | 2026-03-15 | VERIFIED | 2 | 4 | 3 | **24**
QLoRA starter (7B: 6–8GB, r16/α32, paged-AdamW, grad-ckpt, bs1×acc4; 4-bit NF4 + double-quant).
Mechanism: canonical starter hyperparams.
Maps: corroborates C1-085 defaults; 7B-numbers scale down to 2B per C1-089 formula.

C1-091 | https://cloudinsight.cc/en/blog/gemma-4-fine-tuning | 2026-04-06 | VERIFIED | 3 | 5 | 3 | **45**
LoRA/QLoRA/Full ladder on Gemma-4 (31B: 250GB full / 40GB LoRA / 18GB QLoRA; E4B-4.3B: 35/12/6GB); LoRA ≈ 95–98% of full, QLoRA ≈ 93–97% of LoRA; Unsloth 2×/−70%.
Mechanism: quality-ladder + VRAM-ladder quantified on modern models.
Maps: justifies QLoRA (not full-FT) for W6 — ~95% quality at ~1/14 VRAM; 4.3B-class 6GB-QLoRA point triangulates our 2B estimate (~4–6GB).

C1-092 | https://www.adaptiverecall.com/llm-fine-tuning/qlora-on-single-gpu.php | 2026 | VERIFIED | 2 | 4 | 2 | **16**
Single-GPU QLoRA practical floors (7–8B: 16GB min, 24GB comfortable).
Mechanism: practitioner floor consistent with C1-081 (7–8B LoRA 1×40GB is NeMo-conservative; community 16–24GB with QLoRA+Unsloth).
Maps: explains the NeMo-vs-community gap (NeMo table is full-LoRA-fp16-conservative; QLoRA+Unsloth halves it) — recorded so W6 doesn't over-provision.

C1-093 | https://docs.clore.ai/guides/getting-started/model-compatibility | 2025–2026 | VERIFIED | 3 | 3 | 3 | **27**
VRAM fit tables: Qwen2.5-VL-7B OCR needs 16–24GB (RTX 4090); 3B-class fits 12GB; full-FT-7B needs A100-40GB; Unsloth-QLoRA-7B on 12–24GB.
Mechanism: VLM-specific inference+train fit data (7B OCR anchor).
Maps: 7B-OCR 16GB-inference point implies 2B-OCR ≈ 5–8GB (matches C1-075 exactly) — triangulation vote #3.

C1-094 | https://deepwiki.com/QwenLM/Qwen-VL/5.3-lora-fine-tuning | 2025–2026 | VERIFIED | 2 | 3 | 2 | **12**
DeepWiki Qwen-VL LoRA guide (community synthesis).
Mechanism: tutorial.
Maps: pointer only; primary recipes (C1-085/086) preferred.

---

## S7 — Jetson / edge deployment (S7-095…S7-110)

C1-095 | https://nvidia.github.io/TensorRT-Edge-LLM/0.4.0/developer_guide/02_Supported_Models.html (precision/platform rows) | 2026 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
Edge precision map: FP16 1× baseline; FP8 2× smaller (SM89+); INT4 4× (all platforms); NVFP4 4× (SM100+/Thor recommended); Orin Nano = Ampere SM87 → INT4-AWQ/GPTQ path (NO FP8 compute); Thor = Blackwell → full NVFP4.
Mechanism: platform→precision routing table.
Maps: hard constraint — Orin-Nano-class field devices serve our 2B VLM in INT4 (≈1.2GB, C1-075), Thor-class in NVFP4/FP8; W6 quant plan must produce BOTH artifacts (INT4-AWQ-multilingual-calib + FP8).

C1-096 | https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor | 2025–2026 | VERIFIED | 4 | 4 | 3 | **48**
Jetson Thor: 2070 FP4-TFLOPS sparse, 128GB LPDDR5X (273GB/s), 40–130W, MIG, Blackwell 5th-gen Tensor Cores; runs VLA/LLM/VLM + agentic frameworks (NemoClaw).
Mechanism: datacenter-class memory (128GB) at edge power.
Maps: Thor is the "field server" tier — could serve the FULL unquantized pipeline (VLM + router + post-corrector) on-device; memory-bound caveat per C1-099.

C1-097 | https://developer.nvidia.com/blog/unlock-faster-smarter-edge-models-with-7x-gen-ai-performance-on-nvidia-jetson-agx-thor | 2025-10-30 | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
Thor software stack: 7× genAI throughput since launch; vLLM container monthly; Llama-3.3-70B 41.5 tok/s (3.3× vs launch), R1-70B 40.29 (3.5×); guidance START WITH W4A16 (fastest + smallest); EAGLE-3 speculative decode 2.5× (6.27→16.19 tok/s); NVFP4 supported.
Mechanism: W4A16-first + spec-decode are the two edge levers, both measured.
Maps: edge recipe mirrors server (C1-027): W4A16 default on Thor; INFERENCE: spec-decode gains measured on 70B reasoning — expect LESS on 2B OCR (short outputs, C1-006 note); verify before budgeting.

C1-098 | https://github.com/hokwangchoi/jetson-orin-nano-benchmarks | 2025–2026 | VERIFIED | 5 | 5 | 4 | **100** | §INTEG
Orin Nano 8GB (Super, JetPack 6.2.2) REAL measurements: YOLOv8n TRT-FP16 4.43ms / INT8 3.49ms; VLM tier — Cosmos-Reason2-2B (Qwen3-VL-2B-based, INT4-w/FP16-act) across llama.cpp vs vLLM vs TRT-Edge-LLM; JetPack-6.2.1 NvMap contiguous-alloc ceiling BLOCKED vLLM+TRT-Edge-LLM (fixed in 6.2.2 with vision-profile cap).
Mechanism: 2B-VLM-class INT4 runs on 8GB Nano across THREE runtimes; OS-version-gated allocator trap documented with fix.
Maps: STRONGEST edge feasibility evidence — a 2B VLM (same class as ours) serves on the SMALLEST Jetson; runbook must pin JetPack ≥6.2.2 + vision-encoder profile cap. Direct template for a field Santali/Kashmiri kiosk demo.

C1-099 | https://arxiv.org/html/2602.18397v1 [VLA-Perf: How Fast Can I Run My VLA?] | 2026-02 | VERIFIED | 4 | 5 | 3 | **60** | §INTEG
Measured: Jetson Thor runs π₀-2.7B (SigLIP-So + Gemma-2B) at 19Hz E2E (vision 6.06ms / VLM 20.30ms / action 26.2ms) vs H100 162.5Hz; Thor is MEMORY-bound (LPDDR 270GB/s vs 4090 1TB/s vs B100 8TB/s) — even ViT+VLM compute-bound elsewhere become memory-bound on Thor.
Mechanism: edge bottleneck = bandwidth, not FLOPS → weight-bitwidth (INT4/NVFP4) is the highest-leverage knob.
Maps: justifies aggressive weight quant for edge (C1-095) with measured causality; 20ms VLM-step on 2B-class ≈ 50 pages/sec-class prefill rates — plenty for kiosk OCR.

C1-100 | https://arxiv.org/pdf/2506.07416v1+v2 [LiteVLM, NVIDIA, Jun 2025/Oct 2025] | 2025-06 (v2 Oct 2025) | VERIFIED | 5 | 4 | 4 | **80** | §INTEG
NVIDIA LiteVLM: 2B-VLM pipeline for DRIVE Thor/embedded — visual-token importance pruning (self-attention scores + critical-object preservation) → 2.5× latency cut at SAME accuracy + further FP8 speedup (ModelOpt PTQ); per-stage ViT/prefill/decode latency tables FP16-vs-FP8.
Mechanism: token-PRUNE (fewer visual tokens) multiplies with quantize (cheaper per token) — orthogonal gains; synthetic GT from attention-importance for the pruning policy.
Maps: highest-value edge optimization for OldScan pages — dense 200-dpi scans mint thousands of visual tokens; pruning background/blank-token regions before the LLM decoder cuts prefill linearly. P1 experiment: LiteVLM-style pruning + SmoothQuant on sa_d004-class 4250×6500 scans.

C1-101 | https://www.nvidia.com/en-au/autonomous-machines/embedded-systems/jetson-orin + https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/latest | 2025–2026 | VERIFIED | 3 | 4 | 3 | **36**
Orin family: Nano 40 TOPS (7–15W, 4/8GB) / Super 67 TOPS (7–25W, 102GB/s); 7 modules pin-compatible to AGX Orin 275 TOPS; JetPack + TAO + NGC stack.
Mechanism: power/cost ladder quantified.
Maps: positions Nano as the sub-15W field tier vs Thor (C1-096) lab/vehicle tier; TAO Toolkit = classical-model fine-tune path (not VLM — note scope).

C1-102 | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Jetson-Orin-Nano-2-Robotics-Computer-to-Redefine-Entry-Level-Edge-AI/default.aspx + chosunbiz/yahoo coverage | 2026-08-25 | VERIFIED | 3 | 5 | 2 | **30** | §INTEG
Orin Nano 2 (announced Aug 2026, availability H1 2027): 78 TOPS, 8GB, 8-core Arm, 2× Nano-Super inference, −40% power @15W; runs Cosmos/Nemotron/Gemma-4/Qwen-3 VLMs; Wing/Cognex/Bobcat/Matic early adopters.
Mechanism: next-gen entry edge doubles perf at same memory.
Maps: procurement timing note — do NOT design a 2026 field pilot around Nano 2 (ships H1 2027); current Nano 8GB (C1-098) is the shippable-now tier. Borderline flag.

C1-103 | https://www.jetson-ai-lab.com/models | 2026 | VERIFIED | 3 | 5 | 3 | **45**
Jetson AI Lab model board: Qwen3.8-27B VLM, Gemma-4-E2B, Cosmos3-Edge-4B omnimodal, Muse-Glimmer-30B with per-module (Thor/T5000/T4000/Orin-64/16/8GB/Nano-8GB) × engine (vLLM/Ollama/llama.cpp/TRT-Edge-LLM) fit matrix.
Mechanism: living compatibility matrix for edge VLM deploy.
Maps: standing reference for engine×hardware selection; confirms 2–4B VLMs span the whole Jetson range.

C1-104 | https://www.jetson-ai-lab.com/tutorials/genai-benchmarking | 2025–2026 | VERIFIED | 3 | 4 | 3 | **36**
Jetson vLLM benchmarking tutorial (random + vision-arena datasets; TTFT/TPOT/ITL/E2E; concurrency 1 vs 8; W4A16 Llama-8B example: 44 tok/s @conc1).
Mechanism: standard edge-bench procedure (shareGPT-style + vision sets).
Maps: adopt as edge acceptance procedure (run on our CER slices, not just tok/s).

C1-105 | https://docs.nvidia.com/jetson/jps/inference-services/vlm.html | 2025-01 | VERIFIED | 3 | 3 | 3 | **27**
Jetson Platform Services VLM service: REST alert/Q&A over video streams, Prometheus metrics (token count, decode rate), NanoLLM-backed.
Mechanism: edge VLM-as-microservice with observability built in.
Maps: pattern reference for a kiosk/file-drop OCR service (swap stream-alerts for page-in/transcription-out); metrics schema reusable.

C1-106 | https://developer.nvidia.com/embedded/jetson-benchmarks | 2026 (JetPack 7.0/CUDA 13/TRT 10.13) | VERIFIED | 2 | 4 | 2 | **16**
Official Jetson benchmark hub (VLLM ISL/OSL 2048/128 methodology note).
Mechanism: methodology anchor.
Maps: pointer; real numbers live in C1-097/098/099.

C1-107 | https://developer.nvidia.com/blog/solving-entry-level-edge-ai-challenges-with-nvidia-jetson-orin-nano | 2022-09-21 | VERIFIED | 1 | 1 | 1 | **1**
2022 Orin Nano launch blog (30× vs Nano, JetPack 5.0.2-era).
Mechanism: stale.
Maps: OUT-OF-WINDOW, kept as negative control; excluded from integration.

C1-108 | https://static6.arrow.com/aropdfconversion/2dc77d5a4e5edc55139d28cc7e4b8402dc2c87bf/jetson-orin-nano-datasheet-web.pdf | 2023 | VERIFIED | 2 | 1 | 2 | **4**
Orin Nano datasheet (40/20 TOPS, Ampere 1024-core, 8/4GB).
Mechanism: spec anchor.
Maps: OUT-OF-WINDOW specs; superseded by C1-101. Excluded.

C1-109 | https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models | 2025-03-18 | VERIFIED | 2 | 3 | 1 | **6**
Dynamo intro blog (launch).
Mechanism: duplicates C1-064.
Maps: pointer; weight on C1-064/065.

C1-110 | https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct/discussions/4 | 2025-11/12 | VERIFIED | 2 | 4 | 2 | **16**
Practitioner notes: Qwen3-VL-2B ≈ Qwen2-VL-2B size (~300M ViT + 1.7B LLM); runs on CPU/minimal GPU for chat, image slower.
Mechanism: size-continuity evidence across Qwen-VL generations.
Maps: upgrade-path note — Qwen3-VL-2B is a drop-in future base; no re-budget needed for the 2B envelope.

---

## TOP-10 RANKED RECORDS (by Score, ties → higher actionability first)

| Rank | ID | Score | One-line verdict |
|---|---|---|---|
| 1 | C1-001 | 125 | TRT SmoothQuant W8A8 on Qwen2-VL-2B: 2× faster, zero accuracy loss — the production quant tier |
| 2 | C1-002 | 125 | FP8-KV-cache breaks VLMs (−8.8pp); keep KV in BF16 — hard deploy guard |
| 3 | C1-042 | 125 | Multilingual calibration beats English-only (+3.52 ppl) — mandatory Ol Chiki/Nastaliq/Mayek calib |
| 4 | C1-069 | 125 | $/token spans 36× on same GPU by utilization — batch to saturation or pay 10–30× |
| 5 | C1-081 | 125 | NeMo LoRA ladder: 2B-VLM LoRA fits 1×16–24GB — the W6 GPU-budget answer |
| 6 | C1-084 | 125 | Qwen2-VL-2B QLoRA on FREE T4s: ROUGE 0.18→0.41 on doc pages — W6 feasibility proof |
| 7 | C1-003 | 100 | MME-OCR subtask: INT8/SmoothQuant lossless (24/40), AWQ worst — CER-safe tier list |
| 8 | C1-005 | 100 | TRT Edge-LLM: Qwen2-VL-2B all-precisions-green incl. FP8-ViT — no custom kernels needed |
| 9 | C1-019 | 100 | NVFP4 ≤1% vs FP8 on R1, 3.5× smaller — viable with Indic calibration + reasoning caution |
| 10 | C1-027 | 100 | LLM-Compressor VLMs: >99% @8-bit, 3.5× (72B) / 1.1–1.5× (3B) — temper 2B speedup hopes |

Next-in-line (all ≥80, §INTEG flagged): C1-004 (80), C1-012 (80), C1-025 (80),
C1-026 (80), C1-032 (80), C1-041 (100 — rank 11 by tiebreak), C1-045 (80),
C1-047 (80), C1-050 (100), C1-058 (80), C1-060 (80), C1-072 (80), C1-073 (100),
C1-074 (80), C1-075 (80), C1-089 (80), C1-095 (80), C1-097 (80), C1-098 (100),
C1-099 (60 — below line), C1-100 (80).

## LEDGER STATS

- Records: 110 witness rows (C1-001…C1-110), 107 in-window (2025–2026).
- Out-of-window / excluded from integration: C1-043, C1-048 (2024 foundations, kept cited), C1-083 (2024 blog), C1-107, C1-108 (stale).
- §INTEG flagged (≥30): 66 records. Top-line count for lane rollup: **110 records**.
- Verification: all rows VERIFIED from fetched excerpts or full-text fetch (C1-001/002/003/004).
- No downloads, no training, no level2/out or level2/reports contact. Research only.

---

## §9 UPGRADE (2026-09-27) — campaign §9 evidence law applied

Law: `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §9. Existing C1-001…C1-110 rows
above are UNTOUCHED (past work is gold). This section (a) re-grades every old ID
under the §9 status taxonomy + names the decision it moves + gives the TRANSFER
verdict, and (b) adds §9-native records C1-111…C1-137.

Status key (§9): PRIMARY (source opened, span copied) | MEASURED (disk-computed,
command+n) | DERIVED (arithmetic shown) | CONTRADICTION (two primaries disagree)
| UNKNOWN (needed for a decision, not established — a success, not a hole) |
REJECTED (secondary failed primary check) | DEAD (true but moves no decision).
No MEASURED rows in this upgrade (no disk compute; MEASURED arrives with Phase 6
under the estimator law). No REJECTED rows (no secondary failed a primary check
during the upgrade; C1-036's directional figure is cut as DEAD, not rejected).
Decision codes: W6-QUANT-TIER (which quant tier serves the 2B VLM) | W6-KV
(KV-cache precision) | W6-CALIB (calibration corpus law) | W6-SERVE (TRT-LLM /
Triton vs vLLM vs NIM) | W6-COST (self-host vs hosted $/1M pages; GPU tier) |
W6-LORA (LoRA/QLoRA budget + stack) | W6-EDGE (Orin vs Thor, JetPack pins) |
W6-DISAGG (aggregated vs Dynamo) | W6-TRAIN-PATH (D1 wrap-only vs conditional
QLoRA) | W6-VIT-SPLIT (ViT vs decoder quant split) | W6-QAT-FALLBACK (PaddleSlim
QAT / NVFP4-QAD escalation) | W6-BENCH (acceptance harness) |
W6-BARRED-ROUTE (D4 sat/ks routing on published evidence) | W6-PADDLE-BASE
(PaddleOCR-VL / PP-OCRv6 candidacy) | R6-COMP (competition-intel posture for C2).
Harness facts: H-18LANG (18 Indic langs) | H-SAT (Santali 53.91, Ol Chiki) |
H-KS (Kashmiri 54.82, Nastaliq) | H-SCAN (OldScan 55.3, 200-dpi degraded) |
H-ODIA (Odia 80.01) | H-200DPI (200-dpi citizen docs) | H-NOPAID (no paid keys,
licenses, or cloud spend) | H-NOTRAIN (no training until W6 freeze) |
H-OFFLINE (offline-capable pipeline) | H-FREEZE (Oct 1 freeze window).

### §9-A — TRANSFER CARD PER EXISTING RECORD (one line each, C1-001…C1-110)

C1-001 | PRIMARY | W6-QUANT-TIER (SmoothQuant W8A8 = default production tier) | TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (PTQ-only, serves frozen 2B VLM with TRT-LLM, zero training, zero license).
C1-002 | PRIMARY | W6-KV (KV stays BF16; FP8-KV breaks VLMs −8.8pp) | TRANSFER: SURVIVES — H-SCAN (visual-token variance largest on degraded scans; fix costs only VRAM 0.8→1.4GB).
C1-003 | PRIMARY | W6-QUANT-TIER (INT8/SmoothQuant CER-safe; AWQ barred for scripts) | TRANSFER: SURVIVES — H-SAT/H-KS (glyph-discrimination evidence; Indic CER gate per C1-042 still required).
C1-004 | PRIMARY | W6-CALIB + W6-QUANT-TIER (multilingual-calib mandate; NVFP4 single-pass-only) | TRANSFER: SURVIVES — H-SAT/H-KS (English-calib failure is exactly our tail-script risk).
C1-005 | PRIMARY | W6-QUANT-TIER/W6-EDGE (all-precisions-green, FP8-ViT, no custom kernels) | TRANSFER: SURVIVES — H-OFFLINE (vendor-supported path, no new infra).
C1-006 | PRIMARY | W6-SERVE/W6-DISAGG (disagg = bulk-OldScan lever; NO spec-decode budget for OCR) | TRANSFER: SURVIVES — H-SCAN (throughput lever); spec-decode half of the row DIES on H-200DPI (short deterministic outputs).
C1-007 | PRIMARY | W6-QUANT-TIER (batch≥16 → FP8/SQ; single-page → INT4 weight-only) | TRANSFER: SURVIVES — H-SCAN (bulk-reprocessing vs interactive routing rule).
C1-008 | PRIMARY | W6-QUANT-TIER (start from FP8-block-scaling, not per-tensor) | TRANSFER: SURVIVES — H-NOTRAIN (PTQ knobs only).
C1-009 | PRIMARY | W6-KV (KV-FP8 is an independent switch; vendor blesses BF16-KV) | TRANSFER: SURVIVES — H-SCAN (corroborates C1-002 fix pattern).
C1-010 | PRIMARY | W6-SERVE ops (engines arch-locked; build per GPU target) | TRANSFER: SURVIVES — H-OFFLINE (build-farm procedure, no cost; below 30-gate, ops note only).
C1-011 | DEAD | none (early-2025 immaturity note, superseded by C1-001/C1-005) | TRANSFER: n/a — record and cut.
C1-012 | PRIMARY | W6-SERVE (Triton + inflight batching + LoRA hot-swap, one engine per script-specialist) | TRANSFER: SURVIVES — H-18LANG/H-OFFLINE (adapter swap needs only Triton, offline).
C1-013 | DEAD | none (repo-health popularity, explicitly not correctness — ledger says so) | TRANSFER: n/a — record and cut.
C1-014 | PRIMARY | W6-SERVE (serverless Triton+TRT-LLM demo-endpoint pattern) | TRANSFER: SURVIVES — H-NOPAID (pattern needs no license; max_batch_size tuned for page images).
C1-015 | DEAD | none (post-hackathon K8s scale-up, explicitly not W6 — ledger says so) | TRANSFER: n/a — record and cut.
C1-016 | PRIMARY | W6-BENCH (trtllm-bench = THE quant acceptance harness on our slices) | TRANSFER: SURVIVES — H-SAT/H-KS/H-ODIA (gate runs offline on our CER slices, zero cost).
C1-017 | PRIMARY | W6-SERVE precedent + W6-BARRED-ROUTE headroom (English-only doc-VLM proves stack, flags our gap) | TRANSFER: SURVIVES — H-SAT/H-KS (non-English weakness is the opportunity; its English numbers carry an obituary, DEAD for decisions).
C1-018 | PRIMARY | W6-TRAIN-PATH/D1 (SFT→RLVR cookbook source; CC-BY data provenance) | TRANSFER: SURVIVES — H-NOTRAIN (reference now, execute only post-freeze; licenses clean).
C1-019 | PRIMARY | W6-QUANT-TIER (NVFP4 viable with Indic calib + reasoning-head caution) | TRANSFER: SURVIVES — H-NOTRAIN (PTQ via ModelOpt, offline); vendor English gates carry an obituary (≤1% claim DEAD until our CER gate passes).
C1-020 | PRIMARY | W6-QUANT-TIER (NVFP4 production-grade, not experimental) | TRANSFER: SURVIVES — same obituary condition as C1-019 (all gates English-centric).
C1-021 | CONTRADICTION | W6-QUANT-TIER (4/6+AWQ fix candidate, but v2-vs-v3 GPTQ skew unresolved) | TRANSFER: UNKNOWN — kills no decision until verified against the repo; both quotes stored in the row above.
C1-022 | PRIMARY | W6-QAT-FALLBACK principle (keep script-critical late layers high-precision) | TRANSFER: DIES as a training recipe — H-NOTRAIN (we do not pre-train); principle note survives for the QAT/RLVR escalation only.
C1-023 | PRIMARY | W6-KV (attention-kept-high-precision corroboration) | TRANSFER: SURVIVES — H-SCAN (below 30-gate; reinforces C1-002, training-only otherwise).
C1-024 | PRIMARY | W6-VIT-SPLIT (LLM decoder aggressive, ViT conservative) | TRANSFER: SURVIVES — H-SCAN/H-200DPI (vision-path fragility on scans; independent vote with C1-002).
C1-025 | PRIMARY | W6-QUANT-TIER (FP8-first policy) + W6-COST (H100 $/query tables) | TRANSFER: SURVIVES — H-SAT/H-KS/H-NOTRAIN (calibration-DATA law is load-bearing for Ol Chiki/Nastaliq).
C1-026 | PRIMARY | W6-VIT-SPLIT (protect Qwen decoder + projector; rotation-PTQ barred for MXFP4) | TRANSFER: SURVIVES — H-SAT/H-KS (decoder fragility directly threatens tail scripts).
C1-027 | PRIMARY | W6-QUANT-TIER/W6-SERVE (W4A16 interactive vs W8A8 bulk; temper 2B speedup hopes) | TRANSFER: SURVIVES — H-SCAN (bulk) + kiosk-interactive split.
C1-028 | PRIMARY | W6-SERVE (vLLM zero-calibration FP8 = fastest quantized-serve path) | TRANSFER: SURVIVES — H-OFFLINE/H-NOPAID (no license, offline); calibration-free-scale risk on non-English named, gate required.
C1-029 | PRIMARY | W6-COST (batch-expansion is the real throughput engine) | TRANSFER: SURVIVES — H-SCAN (batch-to-saturation law); English-only accuracy evidence discounted one point per the row.
C1-030 | UNKNOWN | W6-QUANT-TIER (INT8/GPTQ-Int8 ~lossless on DocVQA; L4/A10G sizing table) | TRANSFER: UNKNOWN — DocVQA is English-only; transfers to H-SAT/H-KS only after the Indic CER gate (C1-042 law). Unestablished proposition: English DocVQA delta predicts Ol Chiki/Nastaliq CER delta.
C1-031 | PRIMARY | W6-SERVE (ModelOpt quantize-once, serve TRT-LLM-prod or vLLM-dev) | TRANSFER: SURVIVES — H-OFFLINE (single artifact; WITH Indic calibration per the row's C1-062-note).
C1-032 | PRIMARY | W6-VIT-SPLIT (ViT-side FP8 runbook via classic TensorRT) | TRANSFER: SURVIVES — H-SCAN (vision-encoder quant path with measured numbers).
C1-033 | PRIMARY | W6-BENCH/W6-QUANT-TIER (NeMo PTQ one-CLI + mandatory no_quant-baseline diff) | TRANSFER: SURVIVES — H-NOTRAIN (PTQ half usable now; SFT half post-freeze).
C1-034 | PRIMARY | W6-QUANT-TIER implementer ref (block-scaling / sweep knobs) | TRANSFER: SURVIVES — H-OFFLINE (config-only reference, no evidence weight).
C1-035 | DEAD | none (format-inventory corroboration, explicitly marginal — ledger says so) | TRANSFER: n/a — record and cut.
C1-036 | DEAD | none (third-party tutorial pointer with estimated figures; prefer C1-032/C1-033) | TRANSFER: n/a — record and cut.
C1-037 | PRIMARY | W6-COST (VRAM table seeds S5 math; independent speedup cross-check) | TRANSFER: SURVIVES — rent-tier math (vendor-adjacent blog, directional precision only).
C1-038 | DEAD | none (survey landscape confirmation, explicitly background — ledger says so) | TRANSFER: n/a — record and cut.
C1-039 | PRIMARY | W6-VIT-SPLIT (ignored_layers for ViT projector + LM head under FP8) | TRANSFER: SURVIVES — H-SAT/H-KS (third independent vote for keep-vision-sensitive-layers-high-precision).
C1-040 | DEAD | none (latest-docs restatement, explicitly version-anchor only — ledger says so) | TRANSFER: n/a — record and cut.
C1-041 | PRIMARY | W6-QUANT-TIER (INT3-class barred on tail scripts; LCD adapters as deployed-fix) | TRANSFER: SURVIVES — H-SAT/H-KS (2–4× harder hit quantified for our exact risk profile).
C1-042 | PRIMARY | W6-CALIB (HARDEST requirement: Ol Chiki + Nastaliq + Mayek + Odia in every calib corpus, ~zero cost) | TRANSFER: SURVIVES — H-SAT/H-KS/H-ODIA/H-NOPAID (few hundred pages already on disk, no budget, no training).
C1-043 | DEAD | none (2024 foundation, substance superseded by C1-041/C1-042 — ledger flags recency 2) | TRANSFER: n/a — record and cut.
C1-044 | PRIMARY | W6-QUANT-TIER (profile per-script outlier shape first; SmoothQuant for spiky tails) | TRANSFER: SURVIVES — H-SAT/H-KS (outlier-shape law favors SQ on tail-script distributions).
C1-045 | PRIMARY | W6-PADDLE-BASE/R6-COMP (sub-1B efficiency bar our lane must clear; NIM-container precedent) | TRANSFER: SURVIVES — H-SCAN (table/layout metrics relevant); OmniDocBench numbers carry an obituary (bench ≠ our CER, languages differ).
C1-046 | UNKNOWN | R6-COMP baseline + W6-BASE-MODEL posture (NVIDIA OCR as production-trodden reference) | TRANSFER: UNKNOWN — "multilingual" likely Latin+CJK-heavy per the row's own INFERENCE; Ol Chiki/Nastaliq coverage unverified. Unestablished proposition: nemotron-ocr coverage of H-SAT/H-KS scripts.
C1-047 | PRIMARY | W6-SERVE/W6-TRAIN-PATH (vendor pre-quantized FP8/FP4 checkpoints validate plan; 9.8M-sample scale context) | TRANSFER: SURVIVES — H-NOTRAIN (we adapt, never pretrain); multi-page token-reduction watch for H-SCAN.
C1-048 | PRIMARY | W6-TRAIN-PATH/D1 rationale (2B multilingual doc-reading weakest out-of-box → fine-tune, not zero-shot hope) | TRANSFER: SURVIVES — H-SAT/H-KS (MTVQA-20.0 weakness is our fine-tune target; 2024 foundation, below-gate but load-bearing rationale).
C1-049 | PRIMARY | W6-QUANT-TIER (PaddleOCR-VL INT8/FP8 serves on 16GB cards) | TRANSFER: SURVIVES — 16GB serve tier (community claim, gate on our CER before trusting "near-parity").
C1-050 | PRIMARY | W6-PADDLE-BASE (PaddleOCR-VL-0.9B servable TODAY via vLLM; OldScan/Odia workhorse candidate) | TRANSFER: SURVIVES — H-SCAN/H-ODIA/H-OFFLINE (open weights, offline, dynamic-res ViT fits mixed scan sizes).
C1-051 | PRIMARY | W6-PADDLE-BASE (HPI+TensorRT+FP16 accelerated classical baseline for paddleocr_indic) | TRANSFER: SURVIVES — H-OFFLINE (env constraint CUDA11.8/TRT8.6 recorded; no new hardware).
C1-052 | UNKNOWN | W6-QAT-FALLBACK (PaddleSlim QAT-the-rec-head if PTQ fails the Indic gate) | TRANSFER: UNKNOWN — QAT is training, gated by H-NOTRAIN until the W6 freeze (FEASIBLE-IF column). Unestablished proposition: QAT cost/efficacy on Ol Chiki/Nastaliq rec heads.
C1-053 | PRIMARY | R6-COMP watch + W6-PADDLE-BASE ingest (Paddle velocity; Transformers backend eases TRT/vLLM ingest) | TRANSFER: SURVIVES — H-OFFLINE (backend-compat only; borderline 30-gate watch-item).
C1-054 | DEAD | none (dated non-Indic classical latency anchor, explicitly background — ledger says so) | TRANSFER: n/a — record and cut.
C1-055 | PRIMARY | W6-SERVE (NIM wrapper for demo endpoint; LoRA-adapters-ship-as-NIMs) | TRANSFER: DIES for production — H-NOPAID (self-host NIM requires AI Enterprise $4.5K/GPU/yr); SURVIVES for free-dev prototyping inside the C1-061 envelope.
C1-056 | PRIMARY | W6-SERVE/W6-COST (tuned serving ≈2× $/page impact; stack choice ≈ model choice) | TRANSFER: SURVIVES — H-SCAN (bulk costing must assume NIM-tuned-class serving, not naive HF-serve).
C1-057 | PRIMARY | W6-SERVE P1 (programmatic per-language-NIM fleet ops) | TRANSFER: DIES — H-NOPAID (fleet API serves licensed NIMs) + P1-not-W6 scope; procedure survives for Triton-fleet adaptation only.
C1-058 | PRIMARY | W6-COST (hosted-NIM $0.90–1.20/1M anchor for 70B-class) | TRANSFER: SURVIVES — H-NOPAID (anchor used to REJECT the hosted path for our 2B, not to buy it).
C1-059 | PRIMARY | W6-COST (license floor $4.5K/GPU/yr ≈ $0.51/GPU-hr kills official-NIM-self-host; Triton-without-NIM recommendation) | TRANSFER: SURVIVES — H-NOPAID (the floor IS the decision; prototype free-dev, produce on TRT-LLM/Triton).
C1-060 | PRIMARY | W6-COST (independent crossover-math corroboration) | TRANSFER: SURVIVES — directional crossover points only; recompute with our page-token profile.
C1-061 | PRIMARY | W6-SERVE (free-dev 40rpm probe-scale validation TODAY, zero budget) | TRANSFER: SURVIVES — H-NOPAID (1000-credit envelope covers probe-scale, not bulk).
C1-062 | UNKNOWN | R6-COMP alt demo-host path (Azure NIM for doc VLMs) | TRANSFER: UNKNOWN — multilingual coverage TBD per the row + Azure path tensions H-NOPAID (paid cloud). Unestablished propositions: Indic coverage; zero-budget usability.
C1-063 | DEAD | none (marketing-level positioning, explicitly do-not-cite — ledger says so) | TRANSFER: n/a — record and cut.
C1-064 | PRIMARY | W6-DISAGG P1 pattern (phase-disagg + KV-router for multi-GPU bulk; prefix-cache for repeated govt-form layouts) | TRANSFER: DIES for W6 — single-GPU scope (no multi-GPU/RDMA under H-NOPAID); SURVIVES as post-hackathon scale pattern.
C1-065 | PRIMARY | W6-DISAGG (aggregated single-GPU is the RIGHT complexity for 2B single-page OCR — saves over-engineering) | TRANSFER: SURVIVES — single-GPU W6 scope (vendor's own scope limits; a negative decision is still a decision).
C1-066 | DEAD | none (launch press-release numbers, superseded by C1-064/065 — ledger says so) | TRANSFER: n/a — record and cut.
C1-067 | DEAD | none (game-theoretic lens, explicitly background supporting C1-065 — no independent decision) | TRANSFER: n/a — record and cut.
C1-068 | DEAD | none (third-party summaries, explicitly pointers only — ledger says so) | TRANSFER: n/a — record and cut.
C1-069 | PRIMARY | W6-COST (utilization law: Ceff spans 36× on identical hardware; every estimate quotes utilization) | TRANSFER: SURVIVES — H-SCAN (saturated-batch vs idle-interactive differ 10–30×; vllm-cost-meter reusable offline).
C1-070 | PRIMARY | W6-COST (API-parity beat-this bar ≈$0.20/M-output 8B-class; +25%/gen projection rule) | TRANSFER: SURVIVES — self-host must beat commodity or buy wins.
C1-071 | PRIMARY | W6-COST procurement timing (10×/yr decay → NO long GPU contracts; re-price quarterly) | TRANSFER: SURVIVES — H-NOPAID (timing law costs nothing to obey).
C1-072 | PRIMARY | W6-COST ($/1M-pages arithmetic template; cloud-vs-buy break-even → rent for W6) | TRANSFER: SURVIVES — rent-don't-buy rule for W6 scale.
C1-073 | PRIMARY | W6-COST (PRIMARY GPU-price source: H100 median $3.38; L4/A10G serve tier) | TRANSFER: SURVIVES — market facts; refreshed by C1-133 below.
C1-074 | PRIMARY | W6-COST (single biggest $/page lever: 2B serves on L4/A10G 5–15× cheaper/hr than H100) | TRANSFER: SURVIVES — serve-tier selection, no spend (re-confirmed by C1-133).
C1-075 | PRIMARY | W6-COST + W6-LORA (Qwen2-VL-2B VRAM ledger: BF16 4.9GB → INT4 1.2GB; LoRA ≈1.5× inference) | TRANSFER: SURVIVES — any-8GB-card serve; single-T4/L4 train post-freeze per H-NOTRAIN.
C1-076 | DEAD | none (same-paper HTML duplicate, explicitly access-pointer only — all weight on C1-069) | TRANSFER: n/a — record and cut.
C1-077 | DEAD | none (commodity-spread framing; row itself concludes no Indic specialist exists — no live decision) | TRANSFER: n/a — record and cut.
C1-078 | DEAD | none (survey technique inventory, explicitly background/reading-list — ledger says so) | TRANSFER: n/a — record and cut.
C1-079 | DEAD | none (market sizing $103.7B→$312.6B, explicitly no actionability, dropped, score 4) | TRANSFER: n/a — record and cut.
C1-080 | PRIMARY | W6-LORA (Blackwell-16GB VRAM anchors → 2B ≈4–6GB triangulation; Unsloth pointer) | TRANSFER: SURVIVES — H-NOTRAIN (estimate now, execute post-freeze).
C1-081 | PRIMARY | W6-LORA (THE GPU-budget answer: 2B-VLM LoRA ≈1×16–24GB; adapters auto-deploy onto NIMs) | TRANSFER: SURVIVES — H-NOTRAIN (budget locked now, spend only post-freeze; adapter workflow needs no new infra).
C1-082 | UNKNOWN | W6-LORA (NeMo Customizer SFT+pack+NIM process template; commit gated on VLM support) | TRANSFER: UNKNOWN — catalog is LLM-first per the row's own caveat; Qwen2-VL-2B LoRA support in Customizer unverified. Unestablished proposition: Customizer path vs LLaMA-Factory/Unsloth (C1-085/086) for our 2B VLM.
C1-083 | DEAD | none (2024 intro blog, substance superseded by C1-081/082, score 8 — ledger says excluded) | TRANSFER: n/a — record and cut.
C1-084 | PRIMARY | W6-TRAIN-PATH/D1 (STRONGEST feasibility proof: Qwen2-VL-2B QLoRA on FREE T4s, ROUGE 0.18→0.41 on doc pages; 2–5K pairs/lang already on disk) | TRANSFER: SURVIVES — H-NOTRAIN (replicate post-freeze only) + honors the NO-400-page law (pairs exist, zero collection).
C1-085 | PRIMARY | W6-LORA (starter config: ≥12GB, lora_target=all, bs2×acc4; bf16+fp32 mixed-precision lever) | TRANSFER: SURVIVES — H-NOTRAIN (config locked now, run post-freeze); 12GB floor corroborates C1-081.
C1-086 | PRIMARY | W6-LORA (default stack: Unsloth+QLoRA single-16GB, 1.8–2.4× faster, 40–70% less memory) | TRANSFER: SURVIVES — H-NOTRAIN (halves rented step-time when the freeze lifts).
C1-087 | PRIMARY | W6-LORA (vendor seq→VRAM curve: page loads ≈ s1024–2048 band → ~6–9GB QLoRA) | TRANSFER: SURVIVES — H-200DPI (page-image token-load anchor consistent with C1-075/080/086 triangulation).
C1-088 | PRIMARY | W6-SERVE (adapter-switching: ONE frozen base + N script adapters via Triton LoRA = script-router architecture) | TRANSFER: SURVIVES — H-18LANG (architecturally load-bearing; designing it needs no training).
C1-089 | PRIMARY | W6-LORA (general VRAM formula for any rank/seq/batch — METHOD source for NOTE_LORA_VRAM.md) | TRANSFER: SURVIVES — H-NOTRAIN (planning method, zero cost, recompute freely).
C1-090 | DEAD | none (starter-hyperparam corroboration; 7B numbers scale via C1-089 — no independent decision) | TRANSFER: n/a — record and cut.
C1-091 | PRIMARY | W6-TRAIN-PATH (QLoRA-not-full justification: ~95% quality at ~1/14 VRAM; 4.3B-class 6GB point triangulates 2B) | TRANSFER: SURVIVES — H-NOTRAIN (method choice locked pre-freeze, spend post-freeze).
C1-092 | DEAD | none (NeMo-vs-community gap explanation absorbed into C1-081/086; no independent decision — score 16) | TRANSFER: n/a — record and cut.
C1-093 | PRIMARY | W6-LORA/W6-COST (7B-OCR 16GB-inference point → 2B ≈5–8GB, triangulation vote #3) | TRANSFER: SURVIVES — sizing vote for the serve tier.
C1-094 | DEAD | none (community tutorial pointer; primaries C1-085/086 preferred — ledger says so) | TRANSFER: n/a — record and cut.
C1-095 | PRIMARY | W6-EDGE/W6-QUANT-TIER (Orin-Nano-class → INT4-AWQ/GPTQ, NO FP8 compute on SM87; Thor → NVFP4/FP8; produce BOTH artifacts) | TRANSFER: SURVIVES — H-OFFLINE (two-quant-artifact plan, no new hardware).
C1-096 | PRIMARY | W6-EDGE (Thor 128GB = field-server tier; full unquantized pipeline on-device possible) | TRANSFER: SURVIVES — H-OFFLINE (on-device serves the offline kiosk); memory-bound caveat per C1-099 carried.
C1-097 | PRIMARY | W6-EDGE (W4A16-first + EAGLE-3 spec-decode levers, measured on Thor; vLLM monthly containers) | TRANSFER: SURVIVES — H-OFFLINE; spec-decode OCR gains unverified (70B-reasoning numbers carry an obituary for 2B-OCR use).
C1-098 | PRIMARY | W6-EDGE (STRONGEST edge feasibility: 2B-VLM-class INT4 on 8GB Nano across 3 runtimes; JetPack ≥6.2.2 + vision-profile-cap runbook) | TRANSFER: SURVIVES — H-OFFLINE (direct template for a field H-SAT/H-KS kiosk demo, zero cloud).
C1-099 | PRIMARY | W6-EDGE/W6-QUANT-TIER (Thor is MEMORY-bound → weight-bitwidth is the top lever; 20ms 2B-class VLM step) | TRANSFER: SURVIVES — H-SCAN (kiosk OCR rate far above need; justifies aggressive edge weight-quant).
C1-100 | PRIMARY | W6-EDGE P1 experiment (LiteVLM visual-token prune × quantize for dense 200-dpi scans) | TRANSFER: SURVIVES — H-SCAN/H-200DPI (background-token pruning is inference-time policy; P1 experiment, no training-law conflict).
C1-101 | PRIMARY | W6-EDGE procurement tier (Nano sub-15W field vs Thor lab/vehicle; TAO = classical-only scope note) | TRANSFER: SURVIVES — H-OFFLINE (power/cost ladder for field vs lab placement).
C1-102 | PRIMARY | W6-EDGE procurement TIMING VETO (Nano 2 ships H1-2027 → do NOT design the 2026 pilot around it) | TRANSFER: DIES as a hardware option — H-FREEZE (availability post-dates the Oct 1 freeze); the veto itself is the surviving decision.
C1-103 | PRIMARY | W6-EDGE (standing Jetson AI Lab engine×hardware fit matrix) | TRANSFER: SURVIVES — H-OFFLINE (selection procedure; 2–4B VLMs span the whole Jetson range).
C1-104 | PRIMARY | W6-BENCH (Jetson vLLM bench tutorial as edge acceptance procedure — on OUR CER slices) | TRANSFER: SURVIVES — H-SAT/H-KS/H-ODIA (procedure only; tok/s secondary to CER).
C1-105 | PRIMARY | W6-EDGE kiosk pattern (VLM-as-microservice + Prometheus token/decode metrics schema) | TRANSFER: SURVIVES — H-OFFLINE (swap stream-alerts for page-in/transcription-out; metrics reusable).
C1-106 | DEAD | none (methodology anchor; real numbers live in C1-097/098/099 — ledger says pointer) | TRANSFER: n/a — record and cut.
C1-107 | DEAD | none (2022 launch blog, out-of-window negative control — ledger says excluded) | TRANSFER: n/a — record and cut.
C1-108 | DEAD | none (2023 datasheet specs, superseded by C1-101 — ledger says excluded) | TRANSFER: n/a — record and cut.
C1-109 | DEAD | none (Dynamo launch-blog duplicate of C1-064 — ledger says pointer) | TRANSFER: n/a — record and cut.
C1-110 | DEAD | none (forum size-continuity trivia; Qwen3-VL upgrade path belongs to Lane A, no gated W6 decision — score 16) | TRANSFER: n/a — record and cut.

§9-A tally: 110 lines (PRIMARY 78 | CONTRADICTION 1 [C1-021] | UNKNOWN 5
[C1-030, C1-046, C1-052, C1-062, C1-082] | DEAD 26 | MEASURED 0 | REJECTED 0).
DEAD list: C1-011, 013, 015, 035, 036, 038, 040, 043, 054, 063, 066, 067, 068,
076, 077, 078, 079, 083, 090, 092, 094, 106, 107, 108, 109, 110.

### §9-B — NEW §9-NATIVE RECORDS (C1-111…, NVIDIA 2025–2026, full §9 format)

Provenance: live-source search excerpts read 2026-09-27 (campaign-sanctioned
parallel-search pull; NO downloads, NO fetches to disk, NO training). New rows
are PRIMARY-from-excerpt; full-fetch verification is Verdict's 10% sample
(C1-112, C1-118, C1-127 nominated). Format per record: ID | source_url | date |
status | rel | rec | act | Score | extraction, then Decision + TRANSFER lines.

C1-111 | https://nvidia.github.io/TensorRT-LLM/1.2.1/release-notes.html | 2026-04 (PyPI 1.2.1, Apr 20 2026) | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
TRT-LLM 1.2: broadened low-precision + MoE (FP8/NVFP4/MXFP4/INT4-AWQ incl. routing/kernels); MTP>1 for DeepSeek v3.2; disagg service-discovery + NIXL-LibFabric; FIXED KV-cache corruption (#12770); 1.1 fixed Qwen2.5-VL CUDA-graph-padding failure + Mistral-3.1 multi-image batching bug.
Mechanism: vendor release train keeps VLM serving current; the KV-corruption fix is a silent-accuracy landmine removed.
Maps: refreshes C1-006 — pin TRT-LLM ≥1.2 for any 2B-VLM serve (Qwen2.5-VL graph fix directly in our model family); KV fix retires a whole class of "mysterious CER regression" debugging.
Decision: W6-SERVE (floor version ≥1.2). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (upgrade is a version pin, no new hardware, no training).

C1-112 | https://nvidia.github.io/TensorRT-LLM/1.3.0rc13/features/quantization.html | 2026 (1.3.0rc13 docs) | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
TRT-LLM 1.3 quant matrix: Qwen-2/2.5 rows green across NVFP4 + FP8 + W4A8/W4A16 AWQ + W4A16 GPTQ; FP8-KV and NVFP4-KV columns explicit (Qwen-3 NVFP4-KV green); multimodal vision components (LLaVA/VILA/Nougat/BLIP2) default FP16; platform rows: Blackwell sm100/103 full-matrix, Hopper NVFP4-blank (no native FP4 kernels), sm120 (RTX Pro/Thor-class) NVFP4/MXFP4/FP8 green.
Mechanism: the single table that routes (model × precision × GPU) without guessing; vision-FP16-default corroborates C1-002/C1-024/C1-039 for the fourth time.
Maps: load-bearing router for W6-QUANT-TIER per GPU (L4/Hopper → FP8/SQ/AWQ, never NVFP4; Thor/sm120 → NVFP4 allowed) + fourth vote for keep-vision-high-precision.
Decision: W6-QUANT-TIER (per-GPU format routing table). TRANSFER: SURVIVES — H-OFFLINE (table-driven choice, zero cost; nominated for Verdict full-fetch).

C1-113 | https://nvidia.github.io/TensorRT-Edge-LLM/0.9.0/user_guide/examples/speculative-decoding.html | 2026 (Edge-LLM 0.9.0 docs) | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
Edge-LLM 0.9 spec-decoding: EAGLE3 draft table now lists Qwen2.5-VL-7B-Instruct (Rayzl draft) — first VLM EAGLE row on edge; draft quant supported (fp8/int4_awq/nvfp4/mxfp8/int8_sq) WITH explicit warning (draft quant drops acceptance rate); MTP path for Qwen3.5 (num_draft_layers>0, topK=1 linear chain); VLM recipe = quantize base LLM + export FP16 visual encoder + build visual-engine separately.
Mechanism: vision-FP16 + LLM-quant split is now the VENDOR-BLESSED edge VLM recipe (matches our W6-VIT-SPLIT exactly); draft-quant warning quantifies the spec-decode tax.
Maps: edge recipe for our 2B VLM (FP16 ViT engine + quantized LLM + optional EAGLE3); reinforces C1-006/C1-097 (do not budget spec-decode gains for short OCR outputs — acceptance math punishes small drafts).
Decision: W6-EDGE (vendor recipe alignment) + W6-VIT-SPLIT. TRANSFER: SURVIVES — H-OFFLINE (recipe runs on-device; no training, draft checkpoints are downloads-at-build-time only — no disk contact made in this research).

C1-114 | https://nvidia.github.io/TensorRT-LLM/1.2.1/release-notes.html (§1.1 / §0.21.0 / §0.19.0 rows) | 2025–2026 | PRIMARY (excerpt) | 4 | 4 | 4 | **64** | §INTEG
Release-train deltas: 0.19 added FP8 quant support FOR QWEN2-VL (our exact family); 0.21 enabled disagg serving for Qwen-3 + EAGLE3 for Qwen-3 + model-agnostic one-engine Eagle3; 1.1 added Llama-4 FP4 fixes + pipeline-parallel FP8/NVFP4 workaround flag (TRTLLM_LLAMA_EAGER_FUSION_DISABLED=1).
Mechanism: Qwen2-VL FP8 is vendor-supported since 0.19 (not a community hack); one-engine-Eagle3 removes the two-engine ops burden of C1-006-era spec-decode.
Maps: C1-030's GPTQ-Int8 card + this row = belt-and-braces that Qwen2-VL-2B quant serving is mainstream; EAGLE3-one-engine re-opens spec-decode ONLY as a P1 edge experiment (still not budgeted).
Decision: W6-SERVE (Qwen2-VL FP8 is vendor-supported; EAGLE3 P1-only). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (support facts, no new requirements).

C1-115 | https://docs.nvidia.com/deeplearning/tensorrt/10.x.x/index.html | 2026-05-23 (TRT 10.16.0 notes) | PRIMARY (excerpt) | 3 | 4 | 4 | **48** | §INTEG
TensorRT 10.13–10.16: NVFP4 fusions + FP4 build-time improvements; Blackwell perf fixes (up to 78% FP8 regression fixed on densenet121, 55% MHA regression for ViT models, 120MB FLUX memory regression); MoE IMoELayer with NVFP4/FP8 on SM110; KV-cache-reuse API; 10.12 added MXFP8 quant support.
Mechanism: the ViT-MHA-regression fix is directly in our vision-encoder path (classic-TensorRT ViT serving per C1-032); FP4 build-time fixes lower the quant-artifact iteration cost.
Maps: pin classic-TensorRT ≥10.14 for any ViT-side FP8 work (C1-032 runbook); NVFP4-fusion maturity supports the Thor-side plan (C1-095).
Decision: W6-VIT-SPLIT (TRT version floor ≥10.14 for ViT FP8). TRANSFER: SURVIVES — H-OFFLINE/H-SCAN (version pin only).

C1-116 | https://developer.nvidia.com/blog/recent-posts?products=TensorRT-LLM (DFlash 15× Blackwell post, 2026-07-31 listing) | 2026-07-31 | PRIMARY (excerpt listing only) | 3 | 5 | 2 | **30** | §INTEG
DFlash speculative decoding claims up to 15× interactive long-context inference on Blackwell (multi-agent-workflow latency framing, Jul 2026 post).
Mechanism: draft-model speculation pays off on long reasoning chains, not short deterministic transcriptions (same physics as C1-006/C1-113 notes).
Maps: NEGATIVE evidence — third vote that spec-decode stays OUT of the OCR latency budget; listing-only excerpt, numbers NOT cited (would need full-fetch + obituary: reasoning-workload numbers).
Decision: W6-SERVE (spec-decode excluded from OCR budget — borderline 30-gate negative decision). TRANSFER: DIES as a method for us — H-200DPI (short deterministic page transcriptions) + no Blackwell in W6 scope; survives only as "do-not-budget" law.

C1-117 | https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-ocr-v2/- + https://docs.nvidia.com/nim/ingestion/image-ocr/latest/api-reference.html | 2026-06 (NGC 05/27/2026; docs Aug 17 2026) | PRIMARY (excerpt) | 5 | 5 | 3 | **75** | §INTEG
Nemotron-OCR-v2 NIM: production OCR microservice (NeMo Retriever OCR), English + MULTILINGUAL runtime variants (multilingual = DEFAULT; NIM_ENGINE_MODEL_VARIANT=english switches); API returns per-detection text + confidence + float bbox + images_size_mb usage; container ~962MB, NGC Jun 2026, license = NVIDIA proprietary (container) + Open Model License (weights).
Mechanism: NVIDIA's OCR microservice is now versioned product surface (v2.0 docs, support matrix, OpenAPI) — the "buy" option in buy-vs-build is concrete, with a multilingual variant to interrogate.
Maps: sharpens C1-046's UNKNOWN: the exact variant flag + API shape to test Ol Chiki/Nastaliq coverage IF a free-dev probe is ever approved; proprietary-container license reinforces the C1-059 no-self-host-NIM law.
Decision: R6-COMP (concrete buy-option baseline) + W6-BARRED-ROUTE (coverage probe design, gated on user approval). TRANSFER: UNKNOWN — H-SAT/H-KS coverage still unverified (the proposition to test); license facts SURVIVE under H-NOPAID (proprietary container = cannot self-host free).

C1-118 | https://docs.nvidia.com/nim/ingestion/image-ocr/latest/support-matrix.html | 2026-08-17 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
OCR-NIM support matrix (measured startup GiB, FP16): L4 English 1.57 / multilingual 2.66; A10G 1.63/2.72; A100-80GB 1.79/2.88; H100 2.07/3.17; B200 2.17/3.26; GB200 2.23/3.33; GB10 unified-memory N/A; throughput mode (2 engines, bs16) needs MORE than latency-mode numbers; JPEG > PNG for batched decode.
Mechanism: vendor-measured VRAM map for a production OCR service: multilingual ≈ +1.1GiB over English; ENTIRE service fits L4 (2.66GiB) — the cheapest serve tier.
Maps: (a) VRAM anchor for OUR 2B-VLM serve math (if NVIDIA's OCR microservice fits L4-multilingual at 2.66GiB, our quantized 2B at 1.2–2.5GiB per C1-075 is consistent — triangulation vote #4 with C1-075/080/093); (b) multilingual:+1.1GiB prices the script-coverage tax in memory; (c) JPEG-input rule applies to our 200-dpi page pipeline.
Decision: W6-COST (serve-tier VRAM anchor) + W6-SERVE (JPEG ingestion rule). TRANSFER: SURVIVES — H-NOPAID-adjacent/H-SCAN (hardware facts need no license to learn from; nominated for Verdict full-fetch).

C1-119 | https://deepinfra.com/blog/nvidia-nemotron-api-pricing-guide-2026 | 2026-02-02 (updated Sep 2026 window) | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
Third-party Nemotron hosted pricing (DeepInfra, per 1M in/out): Nano-9B-v2 $0.04/$0.16; Nano-12B-v2-VL (128K ctx) $0.20/$0.60; Super-49B $0.10/$0.40 (NAS-pruned 70B→49B, 12× cheaper than 70B-Instruct $1.20/$1.20); Nano-12B-VL called "one of the most affordable VLMs" vs GPT-4o $2.50+ multimodal input.
Mechanism: 2026 VLM API market has a $0.20/M-input anchor (12B-VL) — the number our self-host $/page must beat; NAS-pruning (49B≈70B quality) is the efficiency technique to watch for future base-model swaps (Lane A territory).
Maps: refreshes C1-058/C1-070 beat-this bars with VLM-specific numbers; DERIVED use: at ~2K tokens/page all-in, $0.20/M-input ≈ $0.40–0.50/1K pages hosted-VLM — our L4 self-host target (C1-074 $0.33–0.70/hr at saturated batch) must land an order of magnitude under.
Decision: W6-COST (hosted-VLM beat-this bar $0.20/M input). TRANSFER: SURVIVES as price anchor — H-NOPAID (used to size the self-host win, never to buy; hosted path itself DIES under H-NOPAID/H-OFFLINE).

C1-120 | https://costbench.com/software/llm-api-providers/nvidia-nim | 2026 (pricing page, live) | PRIMARY (excerpt) | 3 | 5 | 3 | **45** | §INTEG
NIM pricing structure 2026: $0 dev tier (hosted endpoints + free credits) → pay-go hosted per-token ($0.04–1.20/M input across sizes on OpenRouter) → enterprise DGX Cloud / AI Enterprise self-host.
Mechanism: three-tier ladder corroborates C1-058/059/061 from an independent aggregator (dev-free / hosted-metered / license-self-host).
Maps: no new decision beyond corroboration; ladder shape confirms the campaign's prototype-free / produce-on-Triton split.
Decision: W6-COST (ladder corroboration; no independent move). TRANSFER: SURVIVES — H-NOPAID (structure facts).

C1-121 | https://docs.nvidia.com/nemo/microservices/26.3.1/customizer/tutorials/lora-customization-job.html | 2026 (v26.3.1 docs) | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG
NeMo Customizer 26.3.1 LoRA tutorial: prompt/completion JSONL (training/ + validation/ splits), FileSet→Model Entity→customization-job→adapter-attached-to-entity flow, Python SDK (nemo-platform), ≥1 GPU CUDA 12.8+, ~45-min SQuAD QA example on Qwen3-0.6B, adapters auto-deploy onto NIMs, MLFlow/W&B metrics, sequence-packing throughput tutorial.
Mechanism: the click-path for a LoRA job is now SDK-scripted (not click-ops) — scriptable inside our pipeline; prompt/completion JSONL maps 1:1 to page-image→transcription pairs.
Maps: SHARPENS C1-082's UNKNOWN (narrows it, does not resolve it): the flow is text-LLM-proven (Qwen3-0.6B QA); VLM (image+text prompt) LoRA via Customizer still unproven → the validation-call question is now precisely "does Customizer accept a VLM FileSet + image-text JSONL", answerable in one probe post-freeze.
Decision: W6-LORA (Customizer commit gated on one VLM probe). TRANSFER: UNKNOWN — H-NOTRAIN (entire flow gated to post-freeze) + VLM-support proposition still open (C1-082 carries it).

C1-122 | https://github.com/NVIDIA/Model-Optimizer/blob/main/README.md | 2026-05-13 / 2026-03-17 / 2026-03-11 entries | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG
ModelOpt 2026 changelog: Nemotron-3-Super FP8 + NVFP4 checkpoints on HF (quantize-for-deploy path documented); Puzzletron heterogeneous pruning/NAS for LLM+VLM (May 2026); customer proofs — Bielik Minitron 7B (33% smaller, 50% faster, 90% quality via pruning+distillation), Domyn 355B→260B.
Mechanism: ModelOpt is now quantize+prune+distill single-shop with vendor-shipped FP8/NVFP4 checkpoints as reference outputs; pruning+distillation proofs de-risk "smaller-than-2B" futures without our own training.
Maps: (a) ModelOpt = THE quantize-once tool (reinforces C1-031); (b) pruning/NAS watch for Lane A (a future 1B-class Indic doc-VLM would inherit our whole serve stack); (c) reference FP8/NVFP4 checkpoints = format-compat test vectors for our vLLM/TRT-LLM setup.
Decision: W6-SERVE (ModelOpt as quantize-once standard). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (quantize + load reference checkpoints needs no training, no license).

C1-123 | https://developer.nvidia.com/blog/nvfp4-trains-with-precision-of-16-bit-and-speed-and-efficiency-of-4-bit | 2025-08-25 | PRIMARY (excerpt) | 3 | 5 | 3 | **45** | §INTEG
NVFP4 pretraining recipe: micro-block 16 (vs MXFP4 32) + E4M3 scales + Hadamard + selective-2D-block-quant + stochastic rounding holds accuracy at trillion-token scale; GB200/GB300 = 7× GEMM vs Hopper; Blackwell first arch with native FP4.
Mechanism: the FORMAT facts (B=16 finer than MXFP4-32; E4M3 > E8M0 scales) are the same physics behind inference-time NVFP4 accuracy (C1-019/021) — training recipe and inference format share the micro-scaling core.
Maps: training half is out-of-scope (H-NOTRAIN, reinforces C1-022's DIES); format half upgrades C1-019/021 confidence: B=16-over-32 is now vendor-explained, and GB300-7× bounds any future "should we NVFP4-train" question (answer: no — H-NOPAID/H-NOTRAIN).
Decision: W6-QUANT-TIER (NVFP4-over-MXFP4 format choice, vendor-explained). TRANSFER: SPLIT — format facts SURVIVE (H-OFFLINE, no cost); training recipe DIES (H-NOTRAIN).

C1-124 | https://arxiv.org/pdf/2606.06527 (Characterizing NVFP4 for Low-Power Edge AI, Jun 2026) | 2026-06-10 (v3) | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
NVFP4 edge ablation (6 compact models): pure unscaled-FP4 collapses accuracy; NVFP4 two-level scaling recovers substantially WITH NO retraining; B=16 = practical accuracy/storage sweet spot (4.5078 bits/input @N=4096); weight-precision ablation: FP8/FP16 weights give only MODEST gains over FP4 weights under the same NVFP4 activation path (activation path dominates); +retraining = best, but no-retrain already recovers.
Mechanism: for edge deployment, ACTIVATION scaling (not weight bits) is the accuracy lever — quantize weights aggressively, spend care on activation scales; no-retrain recovery validates PTQ-only edge deploy.
Maps: DIRECT support for W6-EDGE INT4/NVFP4-on-Nano/Thor plans (C1-095/098): no-retrain NVFP4 works, B=16 confirmed independently of NVIDIA's own claims; activation-dominance says our Indic CER gate must stress long-tail activations (dense conjunct pages), not just weight tables.
Decision: W6-EDGE + W6-QUANT-TIER (no-retrain NVFP4 valid; B=16; gate on activations). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (PTQ-only, edge-relevant, zero training).

C1-125 | http://arxiv.org/html/2509.23202v1 (Bridging the Gap: Promise vs Performance of microscaling FP4, 2025–2026) | 2025–2026 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
Independent microscaling audit: BOTH NVFP4 and MXFP4 are lossy (MXFP4 ≈10% relative drops); existing PTQ tricks don't always beat RTN on these formats; GPTQ and MR-GPTQ give consistently good NVFP4 recovery (large models back to 98–99% FP16); MR-GPTQ lifts MXFP4 to within 1–2% of NVFP4; speedups measured: 3.6× layer-wise / 2.2× e2e on B200, 6×/4× on RTX 5090.
Mechanism: the recovery-method ranking for FP4 (MR-GPTQ > naive RTN; MXFP4 needs MR-GPTQ to approach NVFP4) — an incorporates-able PTQ ladder, all offline.
Maps: sets the W6 FP4 recovery order IF NVFP4-PTQ underperforms on Indic slices: (1) MR-GPTQ, (2) 4/6-scaling (C1-021), (3) QAT/QAD fallback (C1-126/C1-052); RTX-5090 6×/4× bounds Thor-class expectations; resolves C1-021's GPTQ doubt partially toward "GPTQ-family works for NVFP4" (C1-021 stays CONTRADICTION until repo-checked, this is a second primary in its favor).
Decision: W6-QUANT-TIER (FP4 recovery ladder: MR-GPTQ first). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (all-PTQ ladder, no training, no license).

C1-126 | http://arxiv.org/html/2601.20088v3 (Quantization-Aware Distillation for NVFP4 accuracy recovery, 2026) | 2026-01 | PRIMARY (excerpt) | 4 | 5 | 2 | **40** | §INTEG
NVFP4 accuracy-recovery ladder on Nemotron-Super-class: PTQ (MATH500 91.4 / AIME25 32.3) → QAT (94.3/41.5) → QAD distillation (94.6/45.6, near BF16 95.8/46.0; GPQA-D 64.5 vs 66.5; IFEval 87.8 vs 87.5).
Mechanism: distillation-with-quantization-awareness recovers the reasoning tail that PTQ loses (mirrors C1-004's NVFP4-reasoning caution) — the escalation path is proven, with numbers, on a Nemotron model.
Maps: prices the W6-QAT-FALLBACK: PTQ-first per C1-001/C1-003; IF Indic-gated PTQ fails on reasoning-heavy layout/QA heads, QAD (not blind QAT) is the named escalation — post-freeze, budgeted at the validation call, never before.
Decision: W6-QAT-FALLBACK (QAD = named escalation over blind QAT). TRANSFER: UNKNOWN — H-NOTRAIN (all recovery training gated to post-freeze FEASIBLE-IF; unestablished: QAD cost on a 2B VLM + Ol Chiki/Nastaliq distillation data).

C1-127 | https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/modelopt.md | 2026 (main-branch docs) | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
vLLM ModelOpt matrix 2026: FP8 (per-tensor + per-channel-per-token + block-scaled PB_WO 128×128) + NVFP4 + W4A16_NVFP4 (weight-only NVFP4, 16-bit acts) + MXFP8 via quantization="modelopt_fp4"/"modelopt_mxfp8"; NVFP4 GEMM auto-selects (CUTLASS/FlashInfer/Marlin); on GPUs WITHOUT native FP4 kernels vLLM FALLS BACK to W4A16 weight-only via Marlin (warning logged, throughput reduced for compute-heavy).
Mechanism: the Marlin-fallback row is the L4/Hopper story in one line — NVFP4 checkpoints still LOAD everywhere, they just execute weight-only where FP4 kernels are absent; block-scaled FP8-PB_WO gives the C1-008 granularity knob inside vLLM.
Maps: unlocks "quantize NVFP4 once, serve on L4 weight-only + Thor native" (single-artifact dual-target, extends C1-095's BOTH-artifacts plan to ONE artifact); W4A16_NVFP4 is the named L4 fallback format.
Decision: W6-SERVE (vLLM ModelOpt path; L4 = W4A16_NVFP4 fallback). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (config + checkpoint format only; nominated for Verdict full-fetch).

C1-128 | https://github.com/vllm-project/vllm/releases (v0.27.x Sep 2026 notes) + https://docs.vllm.ai/en/stable/features/quantization/ | 2026-09 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
vLLM late-2026 quant stack: NVFP4 in torch-linear backend + FlashInfer-CuTeDSL NVFP4-W4A16 default over Marlin on SM100/103; targeted online quantization (quantization_config.targets — quantize SELECTED layers); partially-pre-quantized checkpoints supported; FP8 ViT-encoder-attention support; W4A16 DSA with nvfp4_fp8_ds_mla KV cache; Qwen3.5 family landed (with EVS video-token pruning).
Mechanism: targeted/partial quantization = per-layer precision surgery (the automation of our W6-VIT-SPLIT: keep projector+head FP, quantize the rest); FP8-ViT-attention support re-opens the C1-032 path inside vLLM (no classic-TRT detour needed).
Maps: vLLM (not TRT-LLM) becomes the fastest route to a split-precision 2B-VLM serve: ignored_layers/targets for ViT-projector+head (C1-039 procedure, automated); Qwen3.5 landing keeps the upgrade path warm for Lane A.
Decision: W6-SERVE + W6-VIT-SPLIT (vLLM targeted-quant = split-precision automation). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (serve-config only).

C1-129 | https://docs.redhat.com/en/documentation/red_hat_ai/3/html/supported_product_and_hardware_configurations/rhaiis-gpu-quantization-support_supported-configurations | 2026 (RH AI 3 docs) | PRIMARY (excerpt) | 5 | 4 | 5 | **100** | §INTEG
Hardware×format hard-constraint table (vLLM kernels): Blackwell B200/B300 do NOT support INT8 in vLLM (use FP8/NVFP4); T4 has NO optimized INT4 kernels (use Ampere+ for INT4); T4/Ampere do NOT support FP8-W8A8 (W8A16-Marlin weight-only only); FP8-W8A8 needs Ada (L4/L40S) or Hopper+; NVFP4 = Blackwell-only (native).
Mechanism: third-party HARD constraints (not vendor marketing) that convert our format debate into a lookup: T4 → INT8-W8A8 or FP8-W8A16-only; L4 → FP8-W8A8/SQ/AWQ/GPTQ (no NVFP4-native); Thor/B200 → NVFP4/FP8 (no INT8-vLLM).
Maps: KILLS two live options cleanly: (a) NVFP4-serve on L4/Hopper (no kernels — weight-only fallback per C1-127 at best); (b) INT8-vLLM on any future Blackwell rental. Locks the per-GPU matrix: T4 INT8-SQ (C1-001 on Ampere), L4 FP8/SQ + W4A16_NVFP4-fallback, Thor NVFP4.
Decision: W6-QUANT-TIER (hard per-GPU format locks). TRANSFER: SURVIVES — hardware facts (no spend to learn; sharpest constraint table in the lane).

C1-130 | https://www.jetson-ai-lab.com/models/ (board snapshot) | 2026-09-10 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
Jetson AI Lab 2026-09 board rule: "all models utilize W4A16 for Orin and NVFP4 for Thor unless specified; NVFP4 and MXFP4 require Blackwell FP4 tensor cores, NOT available on Orin (Ampere)"; Edge-LLM generation-throughput benchmarks on AGX Thor dev kit; Qwen3.5-9B ships W4A16-Orin / NVFP4-Thor dual checkpoints.
Mechanism: living-board confirmation of C1-095/C1-129 from the deployment side (dual-checkpoint convention = the artifact pattern to copy); Thor Edge-LLM gen-throughput rows give the acceptance baseline.
Maps: adopt the dual-checkpoint convention (W4A16-Orin + NVFP4-Thor) as THE edge artifact standard for our 2B VLM; benchmark rows = edge acceptance numbers to beat with CER attached.
Decision: W6-EDGE (dual-checkpoint standard). TRANSFER: SURVIVES — H-OFFLINE (convention + public numbers, zero cost).

C1-131 | https://www.jetson-ai-lab.com/models/qwen3-5-9b + https://blogs.nvidia.com (embedded-AI 2026: Thor field notes) | 2026 (board + 2026 blog) | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG
Thor field evidence 2026: Qwen3 4B served LOCALLY via vLLM (no cloud link, CES/Cat-assistant demo); gpt-oss-20B on Thor via vLLM container = 52 tok/s @c1 → 273 tok/s @c8; Qwen3.5-9B VLM ships NVFP4-Thor / W4A16-Orin Jetson checkpoints with OpenAI-compatible serve commands; TRT Edge-LLM completed MLPerf Edge agentic bench 6.4× faster on AGX Thor (Sep 16 2026 forum); practitioner OpenAI-compat server recipe for Edge-LLM on Thor (May 2026, Qwen3.5-4B, bs1 most stable).
Mechanism: 9B-VLM-on-Thor and 20B@52-tok/s prove HEADROOM for our 2B (a 2B VLM is ~4–10× lighter than demonstrated loads); OpenAI-compat server recipes make the kiosk endpoint copy-paste.
Maps: retires "can Thor serve our VLM" risk (C1-096/098 Corde → field proofs); bs1-stability note + 52→273 scaling sets kiosk (interactive) vs batch expectations; MLPerf 6.4× dates Edge-LLM maturity to Sep 2026.
Decision: W6-EDGE (Thor headroom proven; kiosk topology copy-paste). TRANSFER: SURVIVES — H-OFFLINE (all evidence is local-serve; no cloud, no training).

C1-132 | https://github.com/ai-dynamo/dynamo (README, main) | 2026 (Dynamo 1.0 era: multimodal E/P/D, KVBM, NIXL, planner) | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG
Dynamo 1.0: disagg + KV-aware routing + KVBM offload (GPU→CPU→SSD→S3) + SLA planner + ModelExpress 7× cold-start, backends SGLang/TRT-LLM/vLLM; NEW multimodal E/P/D (disaggregated encode/prefill/decode + embedding cache, 30% faster TTFT on IMAGE workloads); repo's own rule: "If you're running a single model on a single GPU, your inference engine alone is probably sufficient."
Mechanism: the vendor's OWN single-GPU rule closes W6-DISAGG (C1-065 corroborated by the project README); E/P/D + embedding-cache is the one Dynamo idea relevant to image-heavy OCR (repeated form layouts = prefix/embedding hits).
Maps: W6 stays aggregated single-GPU (third corroboration: C1-065 + docs + README); E/P/D-embedding-cache becomes a P1 watch for OldScan bulk (same-form prefix hits via KV-aware routing WITHOUT full disagg).
Decision: W6-DISAGG (closed: aggregated; E/P/D watch P1). TRANSFER: DIES as a deploy for W6 — single-GPU scope (no multi-GPU/RDMA under H-NOPAID); the single-GPU quote + E/P/D pattern SURVIVE as law + watch.

C1-133 | https://getdeploying.com/gpus/nvidia-h100 + https://getdeploying.com/gpus/nvidia-a100-vs-nvidia-l4 | 2026-09-06 (live market snapshot) | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
Sep-2026 market medians: H100 on-demand $3.37/hr (cheapest in-stock $1.73 Vast.ai 4×SXM; spot floor $0.35 Vast.ai); Thunder A100-80GB $1.09; L4 typical $0.89 / cheapest on-demand $0.32 (A100 $0.56 cheapest / $1.79 typical); H100 90-day trend +11% (tightening at top, loosening via Vast/spot at bottom).
Mechanism: live two-sided market — top-tier tightens (+11%) while spot/floor stays deep; L4:A100 typical ≈ 1:2 ($0.89 vs $1.79) CONFIRMS the serve-tier economics of C1-074 with September numbers.
Maps: refreshes C1-073/C1-074 anchors (S5 model inputs): L4-typical $0.89 vs H100-median $3.37 = 3.8×/hr lever before quant-memory savings; spot floors ($0.20 L4 / $0.35 H100-spot) price opportunistic bulk-OldScan runs; +11% H100 trend reinforces C1-071 (no long contracts).
Decision: W6-COST (September price refresh; L4-typical vs H100-median lever). TRANSFER: SURVIVES — market facts (no spend; DERIVED $/page math in NOTE_SERVE_COST.md to be recomputed off these inputs).

C1-134 | https://jarvislabs.ai/blog/h100-vs-a100 (updated 2026-04-19) | 2026-04-19 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG
Per-JOB costing rule (measured Qwen3-8B 2.29× H100-vs-A100): 36h A100-80GB @ $1.49 = $53.64 vs ~16h H100 @ $2.69 = $43.04 — the 80%-pricier GPU costs ~20% LESS per job; A100-80GB settled $1.49 ($1.29 40GB), H100 $2.69–2.99; L4 line added (budget-inference GPU); guidance: H100 for training/FP8-serve/prod, A100 for budget fine-tune/dev/MIG-multi-tenant.
Mechanism: $/hr is a billing number, $/job is the decision number — the measured 2.29× flips naive "A100 is cheaper" for time-bound work.
Maps: W6-LORA GPU choice: a 2B-QLoRA run is hours-long, so the per-job rule SAYS evaluate H100-spot vs A100 vs L4 by measured 2B-step-rate (not $/hr) at the validation call — with H-NOPAID standing, the default stays L4/A100-cheapest until a timed trial proves otherwise; A100-$1.49 corroborates C1-073/133.
Decision: W6-COST/W6-LORA (per-job costing rule; timed-trial gate). TRANSFER: SURVIVES — H-NOPAID/H-NOTRAIN (rule costs nothing; spend gated to post-freeze timed trial).

C1-135 | https://arxiv.org/abs/2606.03264 (PaddleOCR-VL-1.6, Jun 2026) | 2026-06-02 | PRIMARY (excerpt) | 5 | 5 | 3 | **75** | §INTEG
PaddleOCR-VL-1.6: 0.9B compact doc-parse VLM, 96.33% OmniDocBench v1.6 SOTA (beats Qwen3-VL-235B-class giants on text/formula/table + seals/charts/ancient docs); method = region-aware data optimization (identify weak regions of v1.5 → targeted enhancement, NOT indiscriminate corpus growth) + progressive post-training (curated selection + RL).
Mechanism: the "fix weak regions, don't grow the corpus" doctrine is EXACTLY our weak-cell strategy (Santali/Kashmiri/Odia = under-optimized regions); RL post-training recipe is a Lane-B1 (RLVR) specimen from the doc-AI world.
Maps: (a) competitor bar for W6-PADDLE-BASE (0.9B @96.33% is the number our pipeline must contextualize with Indic CER, not chase on English bench); (b) region-aware doctrine independently validates the campaign's weak-cell steering; (c) RL-post-training recipe → Lane B1, gated by H-NOTRAIN.
Decision: W6-PADDLE-BASE (competitor bar) + weak-cell doctrine validation. TRANSFER: UNKNOWN — H-SAT/H-KS/H-ODIA coverage unverified (OmniDocBench ≠ our scripts; obituary required before any adoption claim). Unestablished proposition: 1.6 accuracy on Ol Chiki/Nastaliq/Odia pages.

C1-136 | https://github.com/PaddlePaddle/PaddleOCR/blob/main/README.md + https://paddleocr.dev/ | 2026-06-11 (v3.7.0) | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
PaddleOCR 3.7.0 (Jun 2026): PP-OCRv6 medium (34.5M) +4.6% det / +5.1% rec over v5-server, claimed past Qwen3-VL-235B/GPT-5.5 on OCR with 0.13s A100; tiers tiny 1.5M / small 7.7M / medium 34.5M; 50-lang unified model; PaddleOCR-VL supports 109 languages EXPLICITLY incl. Hindi (Devanagari); Apache-2.0; HF + ModelScope; Transformers backend (3.5.0+); official PaddleOCR-vs-Docling-vs-Surya-vs-Tesseract-vs-EasyOCR 2026 comparison page (96.3% vs Docling-complex ~92.8%).
Mechanism: classical stack now claims VLM-beating OCR at 34.5M params + explicit Devanagari coverage + Transformers-backend interop (our TRT/vLLM ingest) — the paddleocr_indic probe engine has a drop-in upgrade.
Maps: (a) PP-OCRv6-medium = candidate classical engine upgrade for Devanagari-shared languages (Hindi/Marathi/Nepali lanes of H-18LANG) — cheap to trial offline; (b) 109-lang claim needs the C1-042-style gate (Hindi ≠ Ol Chiki/Nastaliq); (c) comparison page = R6 baseline table material for C2.
Decision: W6-PADDLE-BASE (PP-OCRv6 trial for Devanagari-shared lanes) + R6-COMP (comparison table). TRANSFER: SURVIVES — H-OFFLINE/H-NOPAID (Apache-2.0, pip-installable, offline; trial needs no training).

C1-137 | https://arxiv.org/html/2601.21957 (PaddleOCR-VL-1.5 paper, Jan 2026) + http://www.paddleocr.ai/main/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html | 2026-01-29 / 2026 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG
PaddleOCR-VL-1.5: 94.5% OmniDocBench v1.5 (beats Qwen3-VL-235B 89.15% / Gemini-3-Pro 90.33%); Real5-OmniDocBench robustness = 92.05% overall across scanning/skew/warp/screen-photo/illumination (skew 91.66% = +14.19 over v1.0); seal NED 0.138 vs Qwen3-VL 0.382; vendor FAQ: fine-tuning NOT currently supported (high-priority, coming soon).
Mechanism: Real5's scanning/skew/illumination robustness is the closest published proxy to H-SCAN (200-dpi degraded citizen docs); the no-fine-tune FAQ is a HARD constraint that routes W6-LORA exclusively to Qwen2-VL (C1-084/085/086), killing any PaddleOCR-VL-LoRA plan without further debate.
Maps: (a) PaddleOCR-VL-1.5/1.6 = frozen-model OldScan/Odia workhorse candidates (serve, don't train); (b) Real5-skew numbers contextualize our OldScan 55.3 (different metric, obituary noted — NED/accuracy ≠ CER); (c) no-fine-tune FAQ closes the C1-082-style question for Paddle permanently (until vendor ships it).
Decision: W6-PADDLE-BASE (frozen workhorse; LoRA routed to Qwen2-VL only) + W6-LORA (Paddle-LoRA path KILLED by vendor FAQ). TRANSFER: SURVIVES as frozen-model evidence — H-OFFLINE/H-NOTRAIN (serve-only use needs neither training nor license); fine-tune path DIES by vendor statement.

§9-B tally: 27 new records (C1-111…C1-137), all PRIMARY-from-excerpt, all ≥30
(§INTEG: all 27). Transfer split: SURVIVES 19 (111, 112, 113, 114, 115, 118,
119, 120, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 136) | DIES-method
2 (116 spec-decode, 132 Dynamo-deploy) | UNKNOWN 4 (117 NIM-OCR coverage, 121
Customizer-VLM, 126 QAD-training, 135 VL-1.6-Indic) | SPLIT 2 (123 format
survives/training dies, 137 frozen-survives/fine-tune-dies). §9-A + §9-B
combined new decisions moved: W6-SERVE version floor ≥1.2 (111), per-GPU format
locks (112+129), vLLM split-precision automation (128), L4 NVFP4-fallback
single-artifact plan (127), September cost refresh (133), per-job costing rule
(134), Paddle-LoRA killed by vendor FAQ (137), spec-decode/Dynamo/NIM-self-host
kept dead with fresh 2026 evidence (116/132/117-120).

## §9 UPGRADE STATS (2026-09-27)

- §9-A upgrade lines: 110 (one per C1-001…C1-110). §9-B new records: 27
  (C1-111…C1-137). Lane rollup is now **137 records** (110 untouched + 27 new).
- Methods: search-excerpt pulls only. No downloads, no training, no disk compute
  (hence no MEASURED), nothing written outside `docs/research/level7/c/c1/`.
- Nominated for Verdict 10% full-fetch sample: C1-112 (quant matrix), C1-118
  (OCR-NIM VRAM table), C1-127 (vLLM ModelOpt fallback).

---

## §9 LATEST-REFRESH 2026-09-27 (LATEST OVER POPULAR)

Law: campaign §9 + lane directive. Enemy = stale famous docs. For each
ecosystem below the CURRENT live state (Sep 2026) was fetched and the existing
C1 record either CONFIRMed (old row stands) or SUPERSEDEd (old row ID + version
delta). Rows C1-001…C1-137 above are UNTOUCHED. New rows C1-138…C1-155.
Provenance: live-source search excerpts read 2026-09-27 (campaign-sanctioned
pull). No downloads, no training, nothing outside `docs/research/level7/c/c1/`.
New rows are PRIMARY-from-excerpt (same standing as §9-B); full-fetch
verification is Verdict's 10% sample (C1-140, C1-143, C1-151 nominated).
Decision codes / harness facts: same as §9 upgrade (§9 header above).

C1-138 | https://github.com/NVIDIA/TensorRT-LLM/releases (release list; v1.3.0rc21 notes 2026-07-15) + https://nvidia.github.io/TensorRT-LLM/release-notes.html (live 2026-09-21) | 2026-09 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG — **CONFIRM C1-111**: TRT-LLM 1.2.1 (PyPI Apr 20 2026) remains the latest STABLE; 1.3 is STILL pre-release in Sep 2026 (rc25 tops the release list; rc21 Jul 15 latest detailed notes). Fresh delta inside the confirm: rc21 brings Qwen3-VL preprocessing perf fix (#15598/#16353), Qwen2-VL Transformers-5 compat fix (#15997), MXFP4 Hopper swizzle mem cap (#16125), NT3 NVFP4 Blackwell perf fix (#16031).
Decision: W6-SERVE (floor ≥1.2 stands; track 1.3-stable, do not pin RC). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (version pin only).

C1-139 | https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc15 (notes 2026-05-21) | 2026-05-21 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG — **SUPERSEDE C1-112** (1.3.0rc13-era quant matrix): SM120-class (RTX Pro / Thor-adjacent) quant fixes have since landed — GPT-OSS MXFP4 weight fix (#13708), INT4-AWQ on SM120/121 fix (#11561), Qwen3 FP4 CUTLASS-MoE OOM fix (#13349); FP4/FP8 decode kernels + W4A8_MXFP4_FP8 MoE unit tests added. NVFP4/MXFP4 status Sep 2026: both live in the 1.3 train, Blackwell-native, Hopper still no native FP4 kernels (C1-112's platform rows stand).
Decision: W6-QUANT-TIER (SM120 quant path unblocked; per-GPU locks otherwise unchanged). TRANSFER: SURVIVES — H-OFFLINE (support facts, zero cost).

C1-140 | https://github.com/vllm-project/vllm/releases (v0.29.0, 2026-09-08) + https://github.com/vllm-project/vllm/pull/48538 (merged 2026-07-16) + https://github.com/vllm-project/vllm/pull/53724 (2026-08-25) | 2026-09-08 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG — **SUPERSEDE C1-128** (v0.27.x-era quant stack): vLLM v0.29.0 ships Qwen3.8-Flash-Next (BF16/FP8/NVFP4+MTP), Kimi-K3 NVFP4 checkpoints, `nvfp4_per_token` ONLINE MoE quantization (load-time NVFP4 from BF16, Qwen3-30B-A3B GSM8K 0.908 vs 0.912 bf16), online MXFP4 dense+MoE (#49347), compressed-tensors MXFP4-MoE fix with 2.07× throughput (4728→9793 tok/s, #53724). Mechanism shift: FP4 serving moved from "pre-quantized checkpoints only" to load-time/online quantization + kernel auto-select.
Decision: W6-SERVE + W6-QUANT-TIER (vLLM is now the fastest route to a served FP4 2B-VLM; targeted-quant split-precision story from C1-128 carries over). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (serve-config only; nominated for Verdict full-fetch).

C1-141 | https://github.com/PaddlePaddle/PaddleOCR/releases (list top = v3.7.0) + https://github.com/PaddlePaddle/PaddleOCR/releases/tag/v3.7.0 (2026-06-11) | 2026-09 | PRIMARY (excerpt) | 5 | 5 | 3 | **75** | §INTEG — **CONFIRM C1-136**: v3.7.0 (Jun 11 2026) is STILL the latest release Sep 2026 — no 3.8 on the release list; PP-OCRv6 stands as shipped (medium 34.5M +4.6% det / +5.1% rec, 50-lang unified incl. az/ku dict additions per the v3.6.0→v3.7.0 compare, 0.13s A100).
Decision: W6-PADDLE-BASE (PP-OCRv6 trial for Devanagari-shared lanes stands). TRANSFER: SURVIVES — H-OFFLINE/H-NOPAID (Apache-2.0, pip-installable, offline).

C1-142 | https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PaddleOCR-VL.html + https://paddlepaddle.github.io/PaddleX/3.7/en/pipeline_usage/tutorials/ocr_pipelines/PaddleOCR-VL.html (live) | 2026 | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG — **CONFIRM C1-135 + C1-137**: VL-1.6 (96.33% OmniDocBench v1.6) is STILL the current series tip — live docs list `pipeline_version` values `"v1"`, `"v1.5"`, `"v1.6"` only (NO VL-1.7 as of Sep 2026); arch identical to 1.5 (zero-cost migration); serve path under live maintenance (vLLM-server HPS pipeline fix #18129, Jun 2026).
Decision: W6-PADDLE-BASE (frozen workhorse; Paddle-LoRA stays KILLED per C1-137's vendor FAQ). TRANSFER: frozen-model evidence SURVIVES — H-OFFLINE/H-NOTRAIN; Indic coverage still UNKNOWN (C1-135's unestablished proposition carries).

C1-143 | https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct-FP8 (model card, live) + https://github.com/QwenLM/Qwen3-VL (release log: 2B 2025-10-21, FP8 collection 2025-10-04) | 2025-10 / live | PRIMARY (excerpt) | 5 | 5 | 5 | **125** | §INTEG — **SUPERSEDE C1-110** (forum size-trivia): official Qwen3-VL-2B-Instruct-FP8 EXISTS — fine-grained block-128 FP8, vendor states "nearly identical to BF16"; deploy via vLLM/SGLang (Transformers canNOT load it directly); Qwen3-VL-2B (Instruct+Thinking) released 2025-10-21; vLLM ≥0.11 required. Mechanism: vendor-shipped FP8 removes the quantize-it-ourselves step on the Qwen3-VL upgrade path (successor to C1-030's Qwen2-VL quant card).
Decision: W6-QUANT-TIER (Qwen3-VL-2B-FP8 = candidate frozen base) + Lane-A upgrade-path input. TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (weights-only, offline serve); Indic-CER gate still mandatory (C1-042 law); nominated for Verdict full-fetch.

C1-144 | https://huggingface.co/Qwen/Qwen3.5-2B-Base (model card, live) + https://llm-stats.com/models/compare/qwen3-vl-8b-instruct-vs-qwen3.5-2b (release 2026-03-02) | 2026-03-02 | PRIMARY (excerpt) | 4 | 5 | 2 | **40** | §INTEG — **NEW** (no prior row; extends C1-110's upgrade-path note): Qwen3.5-2B (Mar 2026) = native-multimodal foundation (early-fusion vision-language training, Gated-DeltaNet hybrid, 2B/24-layer) claiming cross-generational parity with Qwen3 and superiority over Qwen3-VL on reasoning/coding/agents/visual-understanding.
Decision: Lane-A watch only (no W6 move — zero OCR/CER evidence cited). TRANSFER: UNKNOWN — unestablished proposition: Qwen3.5-2B doc-OCR quality vs Qwen2/3-VL-2B on H-SAT/H-KS/H-ODIA scripts.

C1-145 | https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc21 (2026-07-15) + https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc14 (Qwen3.5 MoE/NVFP4 fixes) | 2026-07-15 | PRIMARY (excerpt) | 4 | 5 | 3 | **60** | §INTEG — **SUPERSEDE C1-114** (0.19/0.21/1.1-era deltas): Qwen-family support is now perf-fixed, not merely present — Qwen3-VL preprocessing + weight-mapping fixes (rc21), Qwen3.5 custom MoE routing + dense/NVFP4 weight-loading fixes (rc14); Qwen3-VL FP8 vendor path corroborates C1-143 from the engine side.
Decision: W6-SERVE (Qwen3-VL serve path is vendor-fixed on both engines). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (support facts).

C1-146 | https://github.com/NVIDIA/Model-Optimizer/releases (0.46.0 stable 2026-08-18; 0.47.0rc0 in flight) + https://pypi.org/project/nvidia-modelopt/ (v0.46.0) | 2026-08-18 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG — **SUPERSEDE C1-122** (May-2026 state): ModelOpt 0.46.0 stable adds NVFP4/FP8 PTQ recipes with projection-output quantizers (~halves TensorRT inter-layer activation memory vs plain `nvfp4` preset), YAML recipe configs (REPLACES the `mtq.*_CFG` module-constant table — runbook migration required), Megatron QAD export-all-iterations, experimental Qwen3.5-9B / Nemotron3-Nano pruning branch; minimum transformers 4.57.
Decision: W6-SERVE (quantize-once standard re-pinned to ModelOpt 0.46.0; recipe-YAML migration). TRANSFER: SURVIVES — H-OFFLINE/H-NOTRAIN (quantize + load reference checkpoints, no training, no license).

C1-147 | https://docs.nvidia.com/nemo/microservices/26.3.0/customizer/ (index/about/models/tutorials, live) + https://docs.nvidia.com/nemo-platform/documentation/customizer-reference/models/model-catalog (live) | 2026 (26.3.x docs) | PRIMARY (excerpt) | 4 | 5 | 2 | **40** | §INTEG — **CONFIRM C1-082 + C1-121 UNKNOWN**: NeMo Customizer catalog is STILL LLM-only (Llama-3.1/3.2, Nemotron-Nano-8B/9B, Nemotron-3, Phi-4, gpt-oss-20B, Qwen2.5-1.5B, Qwen3-0.6B, Mistral/Ministral — Full-SFT+LoRA, NIM inference) with NO VLM entries; the "known-good combos, not limits" disclaimer stands, so the VLM probe question stays open, not closed.
Decision: W6-LORA (Customizer commit still gated on one post-freeze VLM probe). TRANSFER: UNKNOWN — same unestablished proposition as C1-082 (Customizer vs LLaMA-Factory/Unsloth for our 2B VLM).

C1-148 | https://docs.vllm.ai/en/v0.20.0/features/quantization/fp8/ (W8A8 needs Ada/Hopper ≥8.9; Ampere/Turing W8A16-Marlin weight-only) | 2026 | PRIMARY (excerpt) | 4 | 4 | 4 | **64** | §INTEG — **CONFIRM C1-129** (RedHat hard-constraint table): vendor docs agree verbatim — FP8-W8A8 on Ada/Hopper only; T4/Ampere class runs FP8 weight-only (W8A16) via Marlin; dynamic per-token FP8 needs no calibration (llm-compressor RTN path). Per-GPU locks (T4→INT8-SQ, L4→FP8/SQ+W4A16_NVFP4-fallback, Thor→NVFP4) unchanged.
Decision: W6-QUANT-TIER (locks hold). TRANSFER: SURVIVES — hardware facts.

C1-149 | https://docs.api.nvidia.com/nim/re/docs/product (General FAQ, live Sep 2026) + https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/pricing.html (live) | 2026-09 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG — **CONFIRM C1-059**: NO 2026 price change — production self-host STILL $4,500/GPU/yr (EDU/Inception $1,125; 5-yr $18K; perpetual $22.5K) or ~$1/GPU-hr cloud, priced per-GPU (not per-NIM), same rate any GPU size; dev prototyping free (build.nvidia.com + downloadable NIMs ≤16 GPUs, research/dev/test only); 90-day AI Enterprise eval license for production-grade trial.
Decision: W6-COST (Triton-without-NIM production recommendation stands; prototype-free split stands). TRANSFER: SURVIVES — H-NOPAID (the floor IS the decision).

C1-150 | https://deepinfra.com/blog/nvidia-nemotron-api-pricing-guide-2026 (2026-02-02, Sep-2026 window) — no contradictory September evidence surfaced in this refresh | 2026-09 (refresh date) | PRIMARY (refresh-note) | 3 | 4 | 3 | **36** | §INTEG — **CONFIRM C1-119**: Nano-12B-v2-VL $0.20/$0.60 per 1M in/out remains the hosted-VLM beat-this anchor; Nano-9B-v2 $0.04/$0.16 floor stands; no newer hosted-VLM price found to displace it. Thin row by design (anchor maintenance, not new evidence).
Decision: W6-COST (beat-this bar unchanged). TRANSFER: SURVIVES as price anchor — H-NOPAID (sized to reject the hosted path, never to buy).

C1-151 | https://marketplace.nvidia.com/en-us/enterprise/robotics-edge/jetson-thor-developer-kit/ ($3,499 page) + https://magica.com/news/nvidia-jetson-price-increases (2026-07-22) + https://www.roboticscenter.ai/store/product/nvidia-jetson-thor-developer-kit ($5,500 in stock, Sep 2026) + https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics (GA Aug 2025, $3,499) | 2026-07-22 / 2026-09 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG — **SUPERSEDE C1-096** (spec-only row, no price): ADDS price + availability — Jul 2026 NVIDIA repriced the Thor dev kit $3,499 → $5,499 (+57%) with kits OUT OF STOCK on the official marketplace; Sep 2026 purchasable via partners (~$5,500, in stock, ~48h). NO spec/board change evidenced (2070 FP4-TFLOPS sparse, 128GB, 40–130W stand). Cause UNKNOWN (memory-cost inference only, NVIDIA silent).
Decision: W6-EDGE (Thor pilot BOM must use $5.5K + partner lead time, NOT $3.5K). TRANSFER: SURVIVES as field-server evidence — H-OFFLINE; procurement facts are market data (no spend); nominated for Verdict full-fetch.

C1-152 | https://magica.com/news/nvidia-jetson-price-increases (2026-07-22: Nano Super $249→$399 +60%, AGX Orin $1,999→$3,499 +75%, Nano module $99→$199, AGX Orin 32GB module $899→$1,799 at 1KU+) | 2026-07-22 | PRIMARY (excerpt) | 4 | 5 | 4 | **80** | §INTEG — **NEW** (extends C1-101's procurement ladder): the repricing hit the WHOLE Jetson line Jul 2026, not just Thor — kiosk-tier Nano Super now $399 (still the cheapest field tier), AGX Orin kit nearly doubled. Listings give no reason/effective-date/duration; treat as asking-price snapshot until partner quotes confirm.
Decision: W6-EDGE + W6-COST (kiosk BOM re-quoted at order time; current-Nano-8GB shippable-now guidance from C1-098 unaffected). TRANSFER: SURVIVES — market facts; cause UNKNOWN (unestablished: memory-cost explanation).

C1-153 | https://llmhosting.ai/gpus/h100-pcie (Sep 2026: floor $1.99 RunPod community; Vast median $3.07) + https://aliteq.com/cheapest-h100-rental-2026 (22 Sep 2026: Vast spot $1.73, RunPod on-demand $1.99, Hyperstack $1.95, neoclouds $3.85–6.16) | 2026-09-22 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG — **SUPERSEDE C1-133** (Aug-2026 medians): September floor DROPPED — cheapest RELIABLE on-demand H100 now <$2/hr (was $2.50–2.99); Vast median $3.07 ≈ old $3.37–3.38 (top still tight, consistent with the +11% tightening note); 2–3.5× provider spread for identical silicon persists. L4-typical-vs-H100-median $/page lever re-prices off a lower H100 floor.
Decision: W6-COST (S5 model inputs repriced; NOTE_SERVE_COST.md DERIVED math to be recomputed). TRANSFER: SURVIVES — market facts (no spend).

C1-154 | https://aliteq.com/cheapest-a100-rental-2026 (24 Sep 2026: Vast spot $0.47, RunPod on-demand $1.19 PCIe / $1.39 SXM) + https://computeprices.com/providers/runpod (25 Sep 2026 table: A100-SXM community $1.00) | 2026-09-24 | PRIMARY (excerpt) | 5 | 5 | 4 | **100** | §INTEG — **SUPERSEDE C1-134** (Apr-2026 $1.49/$2.69–2.99 inputs): A100-80GB on-demand now $1.00–1.19 (down ~25–30% vs the $1.49 anchor); spot floor $0.47. The per-JOB rule itself is CONFIRMED (mechanism unchanged — $/job flips naive $/hr ranking), ONLY the inputs are repriced; A100-budget-fine-tune guidance gets cheaper.
Decision: W6-COST / W6-LORA (timed-trial gate stands; default stays L4/A100-cheapest per H-NOPAID until a timed trial proves otherwise). TRANSFER: SURVIVES — H-NOPAID/H-NOTRAIN (rule costs nothing; spend gated post-freeze).

C1-155 | DERIVED from C1-153 + C1-154 vs C1-071 + C1-073 (arithmetic shown: H100 on-demand floor $2.50–2.99 → <$2.00; A100-80GB $1.49 → $1.00–1.19; decay direction uniform, no counter-example) | 2026-09-27 | DERIVED | 3 | 5 | 3 | **45** | — **CONFIRM C1-071** (LLMflation timing law): continued decay is now measured in our own two inputs — this refresh IS the quarterly re-price the row ordered; no-long-contracts rule re-validated.
Decision: W6-COST (procurement timing). TRANSFER: SURVIVES — H-NOPAID (timing law costs nothing to obey).

§9 LATEST-REFRESH tally: 18 new rows (C1-138…C1-155). Verdicts: CONFIRM 8
(138→C1-111, 141→C1-136, 142→C1-135/C1-137, 147→C1-082/C1-121,
148→C1-129, 149→C1-059, 150→C1-119, 155→C1-071) | SUPERSEDE 8
(139→C1-112 SM120/MXFP4 fixes; 140→C1-128 vLLM v0.29.0; 143→C1-110 official
Qwen3-VL-2B-FP8; 145→C1-114 Qwen3-VL perf fixes; 146→C1-122 ModelOpt 0.46.0;
151→C1-096 Thor $5.5K repricing; 153→C1-133 Sep GPU floor; 154→C1-134 A100
repriced) | NEW 2 (144 Qwen3.5-2B watch; 152 Jetson line-wide repricing).
Transfer split: SURVIVES 16 | UNKNOWN 2 (144 Qwen3.5-OCR quality; 147
Customizer-VLM — both carried, neither new). No contradiction surfaced that
moves a decision; the single sharpest decision-changer is C1-151 (Thor BOM
$3.5K→$5.5K). Lane rollup is now **155 records** (137 untouched + 18 new).

## §9 LATEST-REFRESH STATS (2026-09-27)

- §9 LATEST-REFRESH rows: 18 (C1-138…C1-155). Lane rollup: **155 records**.
- Methods: live search-excerpt pulls only. No downloads, no training, no disk
  compute (no MEASURED), nothing written outside `docs/research/level7/c/c1/`.
- Nominated for Verdict 10% full-fetch sample: C1-140 (vLLM v0.29.0 release),
  C1-143 (Qwen3-VL-2B-FP8 card), C1-151 (Thor repricing reports).

## §9 SELF-VERIFICATION (Miss, 2026-09-27 — live re-check of refresh rows)
- C1-140 AMENDED: vLLM v0.29.0 with online NVFP4/MXFP4 was claimed as Sep-8 stable. Live check: docs.vllm.ai/en/v0.29.0 exists BUT PyPI latest = 0.28.0 (2026-08-26) and GitHub Releases latest = v0.28.0. Status: v0.29.0 NOT confirmed stable — downgrade row to INFERENCE/UNKNOWN on the version number. NVFP4/MXFP4 quant support itself stays PRIMARY (vLLM docs quant list + NVIDIA 25.09 container notes). Decision it changes: none until 0.29.0 ships stable — do not pin serving stack to it.
- C1-143 CONFIRMED + CAVEAT: Qwen/Qwen3-VL-2B-Instruct-FP8 is official (huggingface.co, Apache-2.0, 3.48GB, vLLM+SGLang serve strings live). Caveat (UNKNOWN, needs Orc bench): HF discussion #1 (Dec 2025) reports answer-repetition degeneration on Blackwell vLLM deploys — FP8 VLM stability guard stands; test before serving claims.

## §9 INFERENCE-PRICING REFRESH (Miss, 2026-09-28 21:25 — live sources, on existing LEDGER per no-new-essays rule)
- C1-156 | https://www.runyard.dev/gpus/providers/vast | 2026-09-26 | VERIFIED | 5/5/5 = 125 | Vast.ai H100 (median own H100): $3.45/hr on 23 GPU samples, 2026-09-18 data. Decision it changes: zero-budget wrap-only becomes untenable if user picks Vast as the carrier; H100 spot/interruptible cheaper (see C1-157). TRANSFER: SURVIVES as Sept-2026 ground truth, DIES for specific carrier negotiation.
- C1-157 | https://aliteq.com/vast-ai-review-2026 | 2026-09-26 | VERIFIED | 5/5/5 = 125 | Vast.ai review 2026: H100 from $1.79/hr, RTX 4090 ~$0.14/hr, 24 Sep 2026 data. Spot/interruptible much cheaper than on-demand (reclaimable minutes' notice). Decision: H100 interruptible tier beats C1-153's <$2/hr claim — underbid floor. TRANSFER: SURVIVES for Vast.ai specifically, DIES for other carriers (different markets).
- C1-158 | https://www.spheron.network/blog/vastai-pricing-2026/ | 2026-09-26 | VERIFIED | 5/5/4 = 100 | Vast.ai 2026 ranges: H100 $0.90–$2.27/hr depending on host verification tier; H200/B200 higher; marketplace spread real. Decision: cross-checked against C1-153 SUPERSEDE; the $0.90 floor means 30 GPU-h × $0.90 = $27 for H100 SFT micro-run, OR $54–$68 at $1.79–2.27 mid-band. Replaces C1-153's single mid-band $1.50ish estimate. TRANSFER: SURVIVES as Vast floor-and-mid range.
- C1-159 | https://vast.ai/pricing/gpu/H100-PCIE | 2026-09-26 | VERIFIED | 4/5/4 = 80 | Vast.ai listed H100 PCIE rent: $1.87/hr (current outstanding offer; page says updates hourly). Decision: cheapest verified Sept-2026 single quote for H100 SFT/CS runs. TRANSFER: SURVIVES for H100 PCIE; DIES for H100 NVLink (different SKU, different price).
- C1-160 (NEW) | https://vast.ai/pricing | 2026-09-26 | VERIFIED | 3/5/3 = 45 | Vast.ai live platform overview: 40+ data centers, on-demand / interruptible / reserved tiers, marketplace-priced. Decision: confirms Vast as the budget carrier for H100. TRANSFER: SURVIVES as carrier choice; DIES for pricing floor (handled by C1-157/158).

FLOOR-AND-MID BAND LOCKED 2026-09-26: Vast.ai H100 interruptible floor $0.90/hr (C1-158, Spheron) → mid-band $1.79–2.27/hr (C1-157/158, Aliteq/Spheron) → PCIe outstanding offer $1.87/hr (C1-159, Vast direct). 30 GPU-h SFT micro-run = $27 floor / $54–68 mid. A100, Thor, BF16/FP4 quotes NOT refreshed in this pass (search returned H100-heavy only).

LAW NOTE: Tile-gate applied — all 5 records cite ≥1 source_url + a price number + a date stamp. No UNKNOWN rows filed for A100-80GB / Thor because no live quote captured this run (parallel-search returned H100-heavy only); those wait for next search cycle.
