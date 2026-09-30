# NOTE_SERVE_COST — $/1M pages model + NIM verdict

## Cost laws
1. Utilization dominates: $0.21–$15.25/M tokens on the SAME H100 by offered load
   alone (C1-069). Quote every $/page number WITH a utilization assumption.
2. API parity bar: 8B-class ~$0.20/M output tokens (C1-070); inference cost falls
   ~10×/year (C1-071) — rent, short terms, re-price quarterly.
3. 2B-VLM fits 8GB cards: BF16 4.9GB / FP8 2.5GB / INT4 1.2GB (C1-075) → serve on
   L4 ($0.33–0.70/hr) or A10G (~$1.00), never H100 (C1-074). GPU index anchor:
   H100 $3.38 / A100 $1.86 / L40S $1.54 / 4090 $0.43 (C1-073).

## Worked sketch (saturated batch, L4 $0.50/hr, SmoothQuant 2B-VLM)
Assume ~2K visual + 0.5K text in, ~0.5K transcription out per page (≈3K tokens),
sustained ~1.5K tok/s saturated (C1-001-class 2× over ~35 tok/s-A100-BF16 scaled
to L4-batch; VERIFY on our rig — INFERENCE placeholder).
→ ~1.8M pages/GPU-day theoretical → ~$7/day → **≈ $4–8 per 1M pages at
saturation** (order-of-magnitude; interactive-idle pays 10–30× per C1-069).
Full 1,227-page probe ≈ cents. Even at 10× pessimism, <$100/1M pages.

## NIM verdict (C1-055/056/059/060/061)
- Prototype on FREE dev NIMs (1K credits, 40 rpm) — zero budget validation.
- Production: NIM wrapper costs $4.5K/GPU/yr ($0.51/hr floor) before compute —
  for a single-GPU 2B service the LICENSE exceeds the GPU (L4 $0.33–0.70).
  RECOMMENDATION: ship Triton + TRT-LLM directly (C1-012), skip NIM wrapper
  unless enterprise support/CVE process is required.
- NIM-ON tuning itself is worth ~2× (1201 vs 613 tok/s, C1-056) — replicate via
  continuous batching + tuned kernels in our Triton config (free).
