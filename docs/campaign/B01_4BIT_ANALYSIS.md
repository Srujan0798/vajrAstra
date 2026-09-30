# B-01 — 4-bit vs bf16 per-script precision analysis (PREP)

## What the task requires (proto-100 B-01)

Day 1 must report Bodhan **4-bit vs bf16** per script, with Perso-Arabic (ks/ur/sd) reported separately. For ks/ur/sd blocks, inference AND the LoRA base must use bf16 (or 8-bit), unless Day 1 shows 4-bit within 1 CER point on those scripts.

## What we can do NOW (without downloads)

1. **Methodology design**: The comparison requires running Bodhan in both 4-bit and bf16 modes on the same images, then computing CER per script. The per-script table needs:
   - `Bodhan 4-bit CER per script` (split by: Devanagari / Latin / Bengali / Gurmukhi / Gujarati / Odia / Tamil / Telugu / Kannada / Malayalam / Perso-Arabic (ks/ur/sd) / Other)
   - `Bodhan bf16 CER per script` (same split)
   - `Δ CER = bf16 − 4-bit` per script (positive = 4-bit is worse)
   - Verdict per script: 4-bit within 1 CER point of bf16? → 4-bit acceptable; otherwise → bf16 required.

2. **Script classification function** (no downloads needed):
   ```python
   def classify_script(text):
       """Unicode-block classification for Perso-Arabic detection."""
       if not text: return 'UNKNOWN'
       # Perso-Arabic (ks, ur, sd) — U+0600–06FF + U+0750–077F + U+FB50–FDFF + U+FE70–FEFF
       arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06FF' or '\u0750' <= c <= '\u077F' or '\uFB50' <= c <= '\uFDFF' or '\uFE70' <= c <= '\uFEFF')
       if arabic_chars > len(text) * 0.5: return 'Perso-Arabic'
       # Devanagari — U+0900–097F
       deva_chars = sum(1 for c in text if '\u0900' <= c <= '\u097F')
       if deva_chars > len(text) * 0.5: return 'Devanagari'
       # Add all 22 scheduled languages...
       return 'Other'
   ```

3. **Per-script CER computation function** (reads `level2/benchmark/scores/bodhan_<precision>/` once downloads complete):
   - Group items by `gt_source` (gold pair / PDF layer / fill) and `language`
   - Compute CER per (precision, script) cell
   - Output table to `BODHAN_BASELINE.md`

## What we need to run it

- Bodhan 4-bit weights (revision `6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e`) — DOWNLOAD BLOCKED (HF auth needs gating access)
- Bodhan bf16 weights (revision `bb091d3a6366a0defe79f0f252c16a790fc8d74b`) — DOWNLOAD BLOCKED
- MLX runtime (already verified in `.venv311/bin/python` per DISPATCH_LOG §23)
- `level2/benchmark/scores/bodhan_4bit/` and `level2/benchmark/scores/bodhan_bf16/` dirs (create after downloads)

## Exact commands to run when weights arrive

```bash
export HF_TOKEN=$(cat ~/.cache/huggingface/token)
cd /Users/srujansai/Desktop/South

# Download (already attempted, blocked on gating)
python3 -c "
from huggingface_hub import snapshot_download
for repo, rev, local in [
    ('hari31416/indic-ocr-mlx-4bit', '6882ee7a21bfc3d2cfb384ce669f2bfdcea3a36e', 'level2/models_bodhan/indic-ocr-mlx-4bit'),
    ('hari31416/indic-ocr-mlx-bf16', 'bb091d3a6366a0defe79f0f252c16a790fc8d74b', 'level2/models_bodhan/indic-ocr-mlx-bf16'),
]:
    snapshot_download(repo_id=repo, revision=rev, local_dir=local, token='$HF_TOKEN', local_dir_use_symlinks=False)
"

# Run Bodhan in 4-bit mode
mkdir -p level2/benchmark/scores/bodhan_4bit
python3 level2/unified/run_bodhan.py --port 4bit --mode probe --sample 100 \
    --out level2/benchmark/scores/bodhan_4bit/

# Run Bodhan in bf16 mode
mkdir -p level2/benchmark/scores/bodhan_bf16
python3 level2/unified/run_bodhan.py --port bf16 --mode probe --sample 100 \
    --out level2/benchmark/scores/bodhan_bf16/

# Per-script comparison (script to be written post-download)
python3 level2/unified/bodhan_per_script.py \
    --4bit level2/benchmark/scores/bodhan_4bit/ \
    --bf16 level2/benchmark/scores/bodhan_bf16/ \
    --output docs/campaign/BODHAN_BASELINE.md
```

## Deliverable artifact

- **File**: `docs/campaign/BODHAN_BASELINE.md` (per-script precision table)
- **Gate**: B-01 Gate 1 — 4-bit within 1 CER point of bf16 on Perso-Arabic (ks/ur/sd)?
- **Status**: PREP — methodology ready, execution blocked on HF downloads

## Perso-Arabic detection (ks/ur/sd)

Per proto-100: "Perso-Arabic (ks/ur/sd) separately". All three use Arabic script with extensions. Kashmiri uses additional extended Arabic chars.

Script ID by Unicode range:
- `ur`: standard Arabic (U+0600–06FF)
- `sd`: Sindhi uses extended Arabic (U+0670, U+0680-06BF + U+0750-077F for extended)
- `ks`: Kashmiri uses Arabic + extensions + often Devanagari script (also U+0900–097F)

Detection logic: Arabic chars > 50% of text → Perso-Arabic; then disambiguate by language tag from `manifest.json` (ks/ur/sd all in probe22 manifest).
