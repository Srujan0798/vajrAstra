# NOTE_QUANT_INDIC — Quantization × Indic scripts: threat model + law

## Threat model (C1-041, C1-042, C1-044)
Quantization error is language-anisotropic. English-calibrated sub-4B GPTQ shows
1.35× (English) → 4.37× (Arabic) perplexity gaps (C1-041); non-Latin low-resource
scripts are hit hardest (C1-043 foundation). Our tail — Ol Chiki (Santali 53.91),
Nastaliq (Kashmiri 54.82), Mayek (mni), Odia (80.01) — sits exactly in the
maximum-harm zone. AWQ with English-only calibration is the sharpest knife:
it under-protects non-English embedding channels (−27.5pp translation, C1-004).

## Law (non-negotiable for W6)
1. Every PTQ/AWQ/GPTQ calibration corpus MUST include Ol Chiki + Nastaliq +
   Mayek + Odia samples (C1-042: +3.52 ppl win, ~zero cost).
2. FP8-first (lossless at all scales, C1-025); SmoothQuant preferred for spiky
   tail-script outlier distributions (C1-044 mechanism + C1-001 empirical win).
3. Vision side: quantize LLM decoder cautiously, ViT per C1-026 (LLM is the
   fragile part: 3% vs 1% under W4A4) and C1-024 (selective quant for vision);
   keep attention/KV high-precision (C1-002, C1-023, C1-039 — three votes).
4. Post-hoc rescue exists: language-conditional dequant adapters recover
   70–83% of the non-Latin gap without re-quantization (C1-041) — fallback if a
   deployed engine underperforms on a tail script.
5. Escalation ladder: multilingual-PTQ → QAT on rec head (C1-052) → LCD adapters.
   Never INT3-class on tail scripts.

## Scoreboard anchors (DocVQA-flavored, English — discount before promotion)
- Qwen2-VL-2B official: BF16 88.34 → GPTQ-Int8 88.28 → GPTQ-Int4 87.21 (C1-030).
- VLM compressor quants: >99% @8-bit, ~98% @4-bit (C1-027).
- NVFP4: ≤1% vs FP8 @R1 with micro-scaling (C1-019/020); 4/6+AWQ best PTQ (C1-021).
- PaddleOCR-VL-0.9B servable via vLLM/SGLang; <10GB dense-decoder note (C1-049/050).
