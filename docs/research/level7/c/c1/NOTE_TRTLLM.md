# NOTE_TRTLLM — TensorRT-LLM serving for the 2B OCR VLM

## Recommendation (1 paragraph)
Serve the fine-tuned Qwen2-VL-2B via TensorRT-LLM SmoothQuant W8A8 (C1-001:
2.0× TTFT / 2.13× decode, accuracy-neutral) behind Triton
inflight_batcher_llm (C1-012) with per-script LoRA adapters hot-swapped
(C1-012 + C1-088). Keep KV-cache in BF16 — FP8 KV destroys VLM accuracy
(C1-002). vLLM dynamic-FP8 (C1-028) is the zero-friction dev fallback
(no engine build); ModelOpt checkpoints run on both (C1-031).

## Tier list (measured on Qwen2-VL-2B, C1-001/003)
1. SmoothQuant W8A8 — lossless, best TTFT. DEFAULT.
2. INT8 weight-only — lossless, no calibration needed. SAFE DEFAULT.
3. FP8 W8A8 (BF16 KV) — lossless, 2.0×, +0.6GB dyn VRAM. APPROVED with guard.
4. INT4 / NVFP4 — fastest + smallest; −1pp avg, reasoning tails suffer (C1-004).
   NVFP4 for bulk OldScan transcription only, never for QA/reasoning heads.
5. INT4-AWQ — BARRED for script-heavy workloads until multilingual-calibrated
   (OCR 24→21/40, translation −27.5pp, C1-003/004).

## Hard guards
- G1: `--kv_cache_dtype fp8` FORBIDDEN on VLMs without per-tier CER proof (C1-002).
- G2: every tier gated by trtllm-bench (C1-016) on Santali/Kashmiri/Odia slices,
  not English MMLU (C1-025's numbers are English-only).
- G3: engines are arch-locked — build separately per serve GPU (C1-010).
- G4: rotation-based PTQ barred under MXFP4 (C1-026); start FP8 block-scaling (C1-008).
- G5: disaggregation NOT needed for single-2B single-page OCR (C1-065); revisit
  only for multi-GPU bulk backlogs (Dynamo pattern, C1-064).
