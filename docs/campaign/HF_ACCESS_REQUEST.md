# HF_ACCESS_REQUEST.md — Boss action needed

**Date:** 2026-09-30
**Status:** D1 downloads BLOCKED on HF gating acceptance
**Token:** Maya0769 (oauth, valid until 2026-10-30)

## Problem

Three gated repos are required for Plan v3 Day 1 (proto-104 D1). The Maya0769 HF token can read metadata (repo_info succeeds, returns sha + gated=auto) but **403 Forbidden on every file download**.

```
hari31416/indic-ocr-mlx-4bit  → 403 Forbidden (gated=auto)
hari31416/indic-ocr-mlx-bf16  → 403 Forbidden (gated=auto)
bodhan-ai/indic-ocr           → 403 Forbidden (gated=auto)
sarvamai/indic-ocr-bench       → ✓ DOWNLOADED (714 MB, 29 files) — was dataset not gated
```

The repos are publicly listed but gated (require explicit acceptance of the model's license/terms). `gated=auto` means HuggingFace requires the user account to click "Agree and access repository" on each repo's page before downloads are permitted.

## Boss action (1 minute per repo)

Visit each of the 3 URLs below, sign in as Maya0769 (or whichever HF account you used), and click the green **"Agree and access repository"** button:

1. https://huggingface.co/hari31416/indic-ocr-mlx-4bit
2. https://huggingface.co/hari31416/indic-ocr-mlx-bf16
3. https://huggingface.co/bodhan-ai/indic-ocr

After clicking, no further action needed — the access propagates within ~30 seconds. Then re-run D1.

## Verification

```bash
export HF_TOKEN=$(cat ~/.cache/huggingface/token)
python3 -c "
from huggingface_hub import hf_hub_download
p = hf_hub_download('hari31416/indic-ocr-mlx-4bit', 'config.json',
    revision='6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e',
    token='$HF_TOKEN',
    local_dir='/Users/srujansai/Desktop/South/level2/models_bodhan/indic-ocr-mlx-4bit')
print(f'OK: {p}')
"
```

## Alternative: provide a different token

If the Maya0769 account cannot get access (the model owners may have restricted), provide a token from an account that does have access. Set it via:

```bash
export HF_TOKEN=hf_xxxxx
```

(overwrite the OAuth token at `~/.cache/huggingface/token`).

## Alternative: use `hf` CLI with your own login

```bash
hf auth login  # paste a token with access
hf download hari31416/indic-ocr-mlx-4bit --revision 6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e --local-dir /Users/srujansai/Desktop/South/level2/models_bodhan/indic-ocr-mlx-4bit
```

## Status while waiting

- ✅ mlx 0.32.3 + mlx-vlm 0.7.4 installed (R-5)
- ✅ mlx-tune NOT installed (R-5: "Not covered")
- ✅ sarvamai/indic-ocr-bench downloaded (714 MB)
- ✅ Output dirs ready: `level2/benchmark/scores/bodhan_{4bit,bf16}/`
- ✅ run_bodhan.py paths already correct (uses `level2/benchmark/`)
- ✅ Reference baseline (surya) computed: weighted CER 0.3956 over 1,227 items
- ✅ BODHAN_BASELINE.md template ready, populated with reference
- ⏸  D1 execution: awaits Bodhan downloads
