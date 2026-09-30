# NOTE_EDGE — Jetson/edge deployment map

## Platform → precision routing (C1-095)
- Orin Nano 8GB (Ampere SM87, 40 TOPS / Super 67 TOPS): NO FP8 compute →
  INT4-AWQ/GPTQ weight-only (≈1.2GB for 2B-VLM, C1-075). PROVEN: 2B-VLM-class
  (Cosmos-Reason2-2B INT4) serves on Nano 8GB across llama.cpp/vLLM/TRT-Edge-LLM
  (C1-098). Pin JetPack ≥6.2.2 (NvMap allocator trap) + vision-profile cap.
- Thor (Blackwell, 2070 FP4-TFLOPS, 128GB): full FP8/NVFP4; W4A16-first + spec
  decode measured (C1-097). Memory-bound box (270GB/s LPDDR) — weight bits are
  the lever (C1-099: π₀-2.7B @19Hz E2E, VLM step 20ms).
- Orin Nano 2 (78 TOPS, H1 2027): do NOT plan 2026 pilots on it (C1-102).

## Edge optimization stack (orthogonal, multiply)
1. Quantize: INT4 (Nano) / SmoothQuant-FP8 or NVFP4 (Thor) — NOTE_TRTLLM tier list.
2. Token-prune: LiteVLM-style visual-token importance pruning → 2.5× same-accuracy
   + FP8 further (C1-100). Highest value for 4250×6500-class OldScan pages.
3. Runtime: TRT-Edge-LLM (C-state) or vLLM container (monthly Thor builds, C1-097);
   bench via Jetson AI Lab procedure (C1-104) on CER slices, not tok/s alone.
4. Service pattern: Jetson Platform Services VLM microservice (REST + Prometheus,
   C1-105) with page-in/transcription-out swapped for stream-alerts.

## Fit matrix pointer
Living engine×hardware matrix: Jetson AI Lab board (C1-103). Qwen3-VL-2B is a
size-compatible future base swap (C1-110).
