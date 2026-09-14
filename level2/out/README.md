# Level 2 — Free-OCR Benchmark Output Packs (out/) README

**Owner:** Srujan Sai (IITGN)
**Lead:** Vinay Gahlot — Vaultstack AI / BHASHINI AksharDrishti
**Languages:** Telugu (`te`), Tamil (`ta`), Kannada (`kn`), Malayalam (`ml`)
**Status:** COMPLETE — 10 engines × 400 pages = **4,000 packs**, machine-sealed (11/11 gates GREEN)

This file explains the `out/` folder so anyone can open it without confusion.
Same pack style as Level 1 (`labeled/`) — **1 page = 1 sample = 1 JSON file** —
but now the text comes from **10 free OCR engines** instead of AI labeling.

---

## 1. What this folder is

- **Goal (from the Sep-10 sync):** benchmark free OCR engines on OUR data — a
  reality check vs published numbers. This is exactly that, done.
- **Unit:** 1 page = 1 JSON pack per engine. 10 engine runs → 4,000 packs.
- **What's in a pack:** the raw OCR text the engine read from the page
  (never corrected, never translated — raw output IS the benchmark), the
  region boxes, and engine provenance (`ocr_engine`, `engine_meta`).

---

## 2. Folder layout

```
out/
├── <engine>/            ← 10 engine folders (below)
│   ├── te/              ← language (100 packs each)
│   │   ├── te_001.json
│   │   ├── ...
│   │   └── te_100.json
│   ├── ta/   kn/   ml/
└── README.md            ← this file
```

So a full path looks like: `out/surya/te/te_001.json` = engine `surya`,
Telugu page 1.

---

## 3. The 10 engine folders (what each one is)

| folder | engine | honest note |
|---|---|---|
| `tesseract_indic/` | tesseract 5.5.2, open script stack (tel+hin+eng etc.) | strong all-rounder |
| `tesseract_bilingual/` | tesseract 5.5.2, eng-led stack | fastest timed (0.7s/page probe) |
| `anuvaad_tesseract/` | Anuvaad-tuned tesseract models (project-anuvaad weights) | tier-1 accuracy (CER 0.48) |
| `openbharatocr/` | **mirror of tesseract_indic** (byte-identical outputs — documented alias) | counts as the SAME family, disclosed |
| `easyocr/` | easyocr 1.7.2, all-Indic open reader | 391/400 pages nonempty |
| `paddleocr_indic/` | PaddleOCR 3.7.0, per-language models | **no Malayalam model** — ml pages use the English stack (disclosed limitation) |
| `indicphotoocr/` | IndicPhotoOCR (IIIT-H) | solid 3rd tier |
| `rapidocr/` | RapidOCR 3.9.2, PP-OCRv5/v4 mobile rec | fastest engine timed (0.44s/page) |
| `doctr/` | python-doctr 1.1.0 (CRNN) | Latin-only rec on our pages — honest weakness, kept for the record |
| `surya/` | surya-ocr 0.22.1 | **tier-1 accuracy leader (CER 0.43)** |

**9 distinct engines, 7 independent families** — the four tesseract variants
share one binary, so the family count is 7 (never say "10 independent").

---

## 4. Where the source pages (PNGs) are

**There are NO image files in this folder** — `out/` contains JSON outputs only
(the packs). The images the engines read live in the repo at
`level2/renders_shared/` (400 PNGs, one per page, sha1-checksummed).

**Source documents** (where the 400 pages came from) are the SAME files the
team already has on Drive in **`Dataset/`** (4 language folders):

- **387 of 400 pages come from PDFs** (`s_<language>NNNNpro_raw.pdf`) —
  these pages were rendered to PNG at 200 dpi before OCR.
- **13 of 400 pages are born-PNG scans** (`s_<language>NNNNpro_raw.png`) —
  all in Tamil (ta_001–ta_005 + others) and Malayalam (ml_004 etc.) folders.
- 190 unique source files total; 308 pages are 2nd/3rd/4th pages of the same
  PDF (`page_index` in each pack JSON says which page of that file).

In every pack JSON, `image.raw_path` points to the source file and
`image.page_index` (0-based) says which page of it. Example:
`"raw_path": "Datasets/te/s_telugu0001pro_raw.pdf", "page_index": 0` =
page 1 of the Telugu 1st PDF.

Mapping (same as Level 1 packs):
`Datasets/<lang>/<file>` on our side = `Dataset/<LanguageFolder>/<file>` on the
shared Drive (Telugu / Tamil / Kannada / Malayalam).

---

## 5. Pack JSON fields (same schema family as Level 1)

| field | meaning |
|---|---|
| `page_id` | e.g. `te_001` — language + page number (1–100) |
| `ocr_engine` | which engine produced this text |
| `engine_meta` | engine name, model version, policy (`open_any_script`), dpi (200) |
| `image.raw_path` | source file (PDF or PNG) — see §4 |
| `image.page_index` | 0-based page number inside that file |
| `regions[]` | text regions; `bbox_xyxy` box + `text` = the raw OCR text |
| `missing` / `unreadable_reason` | engine produced nothing / page unreadable — honest empties, never fabricated |

**Important honesty rule:** empty or wrong text is NEVER corrected or
filled — it stays as-is because the benchmark measures what free engines
actually read. See `level2/upload_sept16/` for the analysis (gap %, accuracy
tiers, per-script winners) computed from these packs.

---

## 6. Quick verification anyone can do

- 10 folders × 4 languages × 100 JSONs = 4,000 packs (check: any folder →
  count files).
- Pick a page, e.g. `te_001` — open all 10 engines' `te/te_001.json` and
  compare what each read of the SAME page (that's the benchmark in one click).
- Compare with `level2/upload_sept16/GAP.md` (what % of text even the best
  engine misses) and `LEADERBOARD_BY_SCRIPT.md` (which engine wins per script).

---

## 7. What to upload where (Drive)

- ✅ upload this whole `out/` folder (29 MB, 4,000 JSONs) → Drive, next to
  Level 1's `labeled/` (suggested Drive name: `L2_benchmark_outputs/`)
- ✅ upload `level2/upload_sept16/` (the stamped summary folder + README)
- ❌ NOT the source documents (team already has them in `Dataset/`)
- ❌ NOT the 200-dpi renders (they regenerate from `Dataset/` via the repo code)

GitHub has both folders already:
- outputs: https://github.com/Srujan0798/vajrAstra/tree/main/level2/out
- summary: https://github.com/Srujan0798/vajrAstra/tree/main/level2/upload_sept16
