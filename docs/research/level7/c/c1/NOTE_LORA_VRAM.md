# NOTE_LORA_VRAM — LoRA VRAM math for 2B VLMs (W6 budget input)

## Answer first
Qwen2-VL-2B LoRA/QLoRA trains on a SINGLE 16GB card (T4/L4); QLoRA+Unsloth fits
6–8GB typical page configs. Full-FT is unnecessary (≈95% quality via QLoRA,
C1-091). W6 GPU budget: 1× L4/A10G rental ($0.33–1.00/hr, C1-074), NOT A100/H100.

## Triangulated VRAM table (2B VLM, page-image loads ≈1–2K visual + 0.5K text tok)
| Method | Weights | +Grad/Opt/Act (page ctx) | Peak | Source |
|---|---|---|---|---|
| Inference BF16 | 4.1GB | KV/act/frag | 4.9GB | C1-075 measured |
| Inference FP8 | 2.1GB | — | 2.5GB | C1-075 |
| Inference INT4 | 1.0GB | — | 1.2GB | C1-075 |
| LoRA (fp16 base) | 4.1 | +adapters+opt+acts | ~8–11GB | C1-081 interp (1B:16GB, 3B:24GB) + C1-087 curve |
| QLoRA NF4 + Unsloth | ~1.2 | +bf16 adapters/acts | ~5–8GB | C1-084 (T4-16GB free tier PROOF) + C1-086 (6–8GB) + C1-088 |
| Full-FT fp16 | 4.1 | +4.1 grad +8.2 Adam +acts | ~18–24GB | C1-089 formula + C1-091 ladder |

Cross-checks: 7B QLoRA 11.5–13.9GB @s512–2048 (C1-087) → 2B ≈ ¼ → 4–7GB ✓;
Llama-8B QLoRA 11.8GB bs4/s2048 (C1-080) → consistent ✓; 7B-floor 16GB (C1-092)
vs NeMo 40GB (C1-081) explained: NeMo = conservative fp16-LoRA, community =
QLoRA+Unsloth+ckpt — use community numbers for budgeting, NeMo for process.

## W6 recipe pointers
- Existence proof + quality jump: Qwen2-VL-2B QLoRA, Nougat pages, ROUGE
  0.18→0.41, 3ep/2.4K pairs, free Kaggle T4s (C1-084). Our analog: 2–5K
  gold pairs per weak script (bn/hi/sa pairs exist at 3–3.5K each), CER-gated.
- Starter hypers: LLaMA-Factory lora_target=all, bs2×acc4, ≥12GB (C1-085) +
  bf16+fp32 mixed precision val-loss trick (zhangfaen).
- Stack: Unsloth + QLoRA (2× faster, −70% mem, C1-086); NeMo Customizer process
  (SFT→NIM auto-deploy adapters, C1-081/082) IF VLM-LoRA support verified,
  else LLaMA-Factory/Unsloth path.
- Architecture fit: one frozen 2B base + per-script adapters (C1-088) served via
  Triton LoRA (C1-012) = the R7 script-router tree made concrete.
