# B21 — SYNTHETIC LINES SPECIFICATION (proto-100 B-21)

**Status:** DRAFT — proto-100 B-21
**Owner:** Agent 3 (Miss)
**Date:** 2026-09-30
**Scope:** Licensed Unicode text, fonts, and degradations for ks (Kashmiri), sat (Santali), mni (Manipuri). **No bench text may be reused.**

---

## 1. Purpose

Generate synthetic line-level training/evaluation data for the three Indic scripts where real data is structurally absent or legally encumbered:

| Script | Language | Code | Gap |
|--------|----------|------|-----|
| Ol Chiki | Santali | sat | Zero real pages in probe22 (0/100 clean under gates) |
| Nastaliq | Kashmiri | ks | Severe fragmentation; surrogate Sarvam fails |
| Meitei Mayek | Manipuri | mni | Zero real pages in probe22 (0/100 clean) |

**Constraint:** No text from Sarvam bench, Indic OCR Bench, or any public benchmark may be reused. All text must be freshly generated from licensed Unicode sources.

---

## 2. Licensed Unicode Text Sources

| Script | Source | License | Notes |
|--------|--------|---------|-------|
| Ol Chiki | Unicode CLDR (Santali), OLPC Santali corpus | Unicode License / MIT | ~2k sentences |
| Nastaliq | URDU-KB, Rekhta corpus (public domain subset) | CC-BY-4.0 / PD | Filtered for Kashmiri lexicon |
| Meitei Mayek | Manipuri Wikipedia (hi/mni), Unicode CLDR | CC-BY-SA / Unicode License | ~1.5k sentences |

**Forbidden:** Sarvam bench text, Indic OCR Bench text, IIIT-HW, IIIT-HW-words, BSTD, any public benchmark corpus.

---

## 3. Font Matrix (Licensed, Redistributable)

| Script | Font Family | Source | License | Glyph Coverage |
|--------|-------------|--------|---------|----------------|
| Ol Chiki | Noto Sans Ol Chiki | Google Fonts | OFL-1.1 | 100% |
| Nastaliq | Noto Nastaliq Urdu | Google Fonts | OFL-1.1 | 95% (Kashmiri subset) |
| Meitei Mayek | Noto Sans Meetei Mayek | Google Fonts | OFL-1.1 | 100% |
| Fallback | Noto Sans | Google Fonts | OFL-1.1 | All scripts |

**Rendering:** Use `pymupdf` (PyMuPDF) with embedded subsetting. No external font downloads at runtime.

---

## 4. Degradation Pipeline (Configurable, Deterministic)

Each synthetic line passes through a **reproducible** degradation pipeline (seed = 20260926 + line_id):

| Stage | Parameter | Range | Notes |
|-------|-----------|-------|-------|
| 1. Font render | Font size | 12–24 pt | Uniform |
| | DPI | 150, 200, 300 | Weighted: 0.5 / 0.3 / 0.2 |
| 2. Optical blur | Gaussian σ | 0.0–1.5 px | Gamma(2, 0.5) |
| 3. Noise | Gaussian σ | 0–15 (0–255) | |
| | Salt-pepper | 0–2% | |
| 3. Photometric | Contrast | 0.5–1.5× | Log-uniform |
| | Brightness | ±30% | |
| 4. Geometric | Rotation | ±3° | Uniform |
| | Skew | ±5% | Affine |
| 4. Aging | Coffee stains | 0–3 blobs/page | Poisson(λ=0.5) |
| | Fold lines | 0–2 / page | Horizontal |
| 5. Compression | JPEG Q | 40–95 | |
| 6. Binarization | Otsu / Sauvola | Random choice | Post-render |

**Seed policy:** `seed = 20260926 + line_id` (deterministic, reproducible).

---

## 5. Output Format

Each synthetic line item:

```json
{
  "line_id": "syn_ks_00042",
  "script": "Kashmiri",
  "language": "ks",
  "text": "کٔشِیر بॅنٛوٛ یۂ تہٕ وپرٕ",
  "font": "Noto Nastaliq Urdu",
  "font_size_pt": 18,
  "dpi": 200,
  "degradation": {
    "blur_sigma": 0.73,
    "noise_sigma": 8.2,
    "contrast": 0.87,
    "rotation_deg": -1.2,
    "jpeg_quality": 78
  },
  "image_path": "syn/ks/line_00042.png",
  "gt_text": "کٔشِیر بॅنٛوٛ یۂ تہٕ وپرٕ",
  "license": "synthetic_pd_unicode",
  "seed": 202609260042
}
```

---

## 6. Generator CLI (proto-104 §P)

```bash
python -m product.tools.gen_synthetic_lines \
  --scripts ks,sat,mni \
  --count 5000 \
  --seed 20260926 \
  --out product/synthetic/lines/
```

**Outputs:**
- `product/synthetic/lines/ks/line_*.png` + `.json` sidecar
- `product/synthetic/lines/manifest.jsonl` (JSONL, one per line)
- `product/synthetic/lines/LICENSE` (aggregate license statement)

---

## 7. License & Provenance

| Asset | License | Attribution |
|-------|---------|-------------|
| Unicode text (CLDR, Wikipedia) | Unicode License / CC-BY-SA / PD | Per source |
| Fonts (Noto family) | SIL OFL-1.1 | Google Fonts |
| Degradation code | MIT | This project |

**No benchmark text reused.** All text freshly sampled from licensed Unicode sources.

---

## 7. Validation Gates (proto-104 §P)

| Gate | Criterion | Check |
|------|-----------|-------|
| G1 | License audit | `python -m product.tools.audit_licenses` → PASS |
| G2 | No bench text | `grep -r "sarvam\|indic-ocr-bench" product/synthetic/` → empty |
| G3 | Determinism | Re-run with seed → byte-identical PNGs + JSONL |
| G4 | Coverage | ≥5,000 lines per script (ks, sat, mni) |
| G4 | Visual sanity | 100 random samples human-reviewed |

---

## 8. Integration

- Output dir: `product/synthetic/lines/{ks,sat,mni}/`
- Manifest: `product/synthetic/lines/manifest.jsonl` (JSONL)
- License file: `product/synthetic/lines/LICENSE`

---

*End of B21_SYNTHETIC_LINES_SPEC.md*
