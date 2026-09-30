# BODHAN_BASELINE — Plan v3 Day 1 (proto-104 D1)

**Status: PARTIAL-BLOCKED (gated downloads)** · **Updated:** 2026-09-30

## Downloads

| Repo | Revision | Size | Status |
|---|---|---|---|
| `hari31416/indic-ocr-mlx-4bit` | `6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e` | TBD | **GATED — 403** · boss must click "Agree" on HF |
| `hari31416/indic-ocr-mlx-bf16` | `bb091d3a6366a0defe79f0f252c16a790fc8d74b` | TBD | **GATED — 403** · boss must click "Agree" on HF |
| `bodhan-ai/indic-ocr` | `cd50d301d0e17e8ecb32fc49c8ccbd7914dcfc25` | TBD | **GATED — 403** · boss must click "Agree" on HF |
| `sarvamai/indic-ocr-bench` | `84ce7ce447456a92bcbf25f3c0a55d6a5a44a24b` | 714 MB | **DOWNLOADED** ✓ (29 files: README, metrics.py, small_representative, test/) |

**HF access** (proto-104 R-5 / U23): `hf auth whoami` → user=Maya0769, token works for metadata (`repo_info` / `hf_hub_download` succeed for `sarvamai/indic-ocr-bench`). **The 3 Bodhan repos return 403 Forbidden on actual file downloads** — the Maya0769 account lacks gating acceptance. **Boss action: click "Agree and access repository" on each of the 3 HF pages, OR provide a token with gating permissions.**

## Installs (R-5)

| Package | Version | Status |
|---|---|---|
| `mlx` | 0.32.3 | ✓ installed |
| `mlx-vlm` | 0.7.4 | ✓ installed |
| `huggingface_hub` | 1.33.0 | ✓ installed |

## Sarvam bench parity (Agent 2's job, prep)

| File | SHA256 |
|---|---|
| `level2/models_bodhan/indic-ocr-bench/metrics.py` (Sarvam's official) | `944335edc4dbed7588b0d9ef1924018c782d8f914319a15f7551943b3db55aaa` |
| `level2/benchmark/pipeline/metrics.py` (ours) | `de3c8ad1c5eae6946d9af1438f0ea56ad8fdd21ee01062af2caa9736434559e4` |

**Byte-identity NOT proven** (DISPATCH_LOG §23). Agent 2 compares on next transcript pass.

## Output paths (created)

- `level2/benchmark/scores/bodhan_4bit/` (empty, ready)
- `level2/benchmark/scores/bodhan_bf16/` (empty, ready)
- `level2/unified/out/preds_bodhan_4bit.*` (run_bodhan.py writes here)

## Tonight's plan (proto-104 D1)

```bash
# After boss clicks "Agree" on the 3 HF repos:
export HF_TOKEN=$(cat ~/.cache/huggingface/token)

# Download 3 Bodhan repos
python3 -c "
from huggingface_hub import snapshot_download
for repo, rev, local in [
    ('hari31416/indic-ocr-mlx-4bit', '6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e', 'level2/models_bodhan/indic-ocr-mlx-4bit'),
    ('hari31416/indic-ocr-mlx-bf16', 'bb091d3a6366a0defe79f0f252c16a790fc8d74b', 'level2/models_bodhan/indic-ocr-mlx-bf16'),
    ('bodhan-ai/indic-ocr', 'cd50d301d0e17e8ecb32fc49c8ccbd7914dcfc25', 'level2/models_bodhan/indic-ocr'),
]:
    snapshot_download(repo_id=repo, revision=rev, local_dir=f'/Users/srujansai/Desktop/South/{local}', token='$HF_TOKEN')
"

# Run --sample 100 (stratified probe sample, fast)
python3 level2/unified/run_bodhan.py --port 4bit --mode probe --sample 100
python3 level2/unified/run_bodhan.py --port bf16 --mode probe --sample 100

# Run --pair-only 300 gold pairs
python3 level2/unified/run_bodhan.py --port 4bit --mode probe --pair-only
python3 level2/unified/run_bodhan.py --port bf16 --mode probe --pair-only

# Full 1,227
python3 level2/unified/run_bodhan.py --port 4bit --mode probe
python3 level2/unified/run_bodhan.py --port bf16 --mode probe

# Sarvam bench small_representative (official metrics.py for parity)
python3 level2/unified/run_bodhan.py --port 4bit --mode bench
python3 level2/unified/run_bodhan.py --port bf16 --mode bench

# Per-script table (B-01) + B-02 Arabic normalization → fills this doc
```

## Gate 1 (proto-89 §A)

**Threshold (reproduced from proto-89):** Bodhan reproduces ~84.9 ±2 on Sarvam's bench AND beats surya on 300 gold pairs.

**Current status:** cannot evaluate (weights blocked).

## Deliverables for tomorrow's Vinay call

1. Per-script CER table (B-01: 4-bit vs bf16, Perso-Arabic separately)
2. Bodhan vs surya on 300 gold pairs (pair-only)
3. Bodhan on FULL 6,909 Sarvam bench (eval only)
4. Bodhan vs Sarvam headline: published 84.94 vs 87.39 beside our numbers
5. Seconds per page/crop (per precision)
6. RQ-3 + RQ-7 answers inside this doc
7. Gate 1 PASS / FAIL verdict

**Status**: pre-implementation; all preparation done (D0, installs, paths, Sarvam bench). Execution pending HF access.

## Reference baseline (surya, 1,227 probe22 items) — ready for comparison

**Source**: `level2/benchmark/scores/sheet_v2.csv` (recomputed_CER column).

| Lang | n | surya CER | Notes |
|---|---|---|---|
| as | 19 | 0.2532 | |
| bn | 100 | 0.4765 | |
| brx | 67 | 0.1660 | |
| doi | 27 | 0.3366 | |
| gu | 24 | 0.2582 | |
| hi | 100 | 0.2217 | |
| kok | 100 | 0.4284 | Day-1 QLoRA scope (was) |
| ks | 100 | 0.5889 | Perso-Arabic |
| mai | 100 | 0.0320 | K1 KILLED (p=1.00 vs runner-up) |
| mni | 20 | 0.9773 | Meetei Mayek — near-total failure |
| mr | 79 | 0.2159 | |
| ne | 37 | 0.2289 | |
| or | 69 | 0.2831 | |
| pa | 90 | 0.1459 | Day-1 QLoRA scope — was |
| sa | 100 | **1.0000** | empty predictions (known bug) |
| sat | 20 | 0.7603 | Ol Chiki — near-total failure |
| sd | 75 | 0.3156 | Perso-Arabic |
| ur | 100 | 0.6279 | Perso-Arabic |
| **Weighted** | **1227** | **0.3956** | |

**Key comparisons for Gate 1** (when Bodhan lands):
- Gate 1: Bodhan reproduces ~84.9 ±2 on Sarvam bench AND beats surya on 300 gold pairs.
- Weighted surya CER 0.3956 over 1,227 = baseline to beat.
