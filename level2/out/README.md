# Level 2 — Free-OCR Benchmark Outputs (out/)

**Owner:** Srujan Sai (IITGN)  
**Lead:** Vinay Gahlot — Vaultstack AI / BHASHINI AksharDrishti  
**Languages:** Telugu (`te`), Tamil (`ta`), Kannada (`kn`), Malayalam (`ml`)  
**Status:** COMPLETE — 10 engines × 400 pages = **4,000 JSON packs**

This file explains the `out/` folder. **1 page = 1 sample = 1 JSON file per
engine.** The text in each JSON is the **raw OCR output** — never corrected,
never translated; the raw output IS the benchmark.

The 400 pages are the same pages used for Level 1 labeling — the source
documents are the ones already in the team Drive `Dataset/` folders. Only
the engine outputs live here.

---

## 1. Folder layout

```
out/
├── README.md            ← this file
├── <engine>/            ← 10 engine folders, ALL identical in shape:
│   ├── te/              te_001.json … te_100.json   (100 packs)
│   ├── ta/              ta_001.json … ta_100.json   (100 packs)
│   ├── kn/              kn_001.json … kn_100.json   (100 packs)
│   └── ml/              ml_001.json … ml_100.json   (100 packs)
```

Engine folders: `tesseract_indic`, `tesseract_bilingual`, `anuvaad_tesseract`,
`openbharatocr`, `easyocr`, `paddleocr_indic`, `indicphotoocr`, `rapidocr`, `doctr`, `surya`.

Full path example: `out/surya/te/te_001.json` = engine **surya**, page **te_001**.

**Totals: 400 JSONs per engine · 4,000 JSONs in the whole folder.**

---

## 2. The 10 engine folders

| folder | engine / setup | honest note |
|---|---|---|
| `tesseract_indic/` | tesseract 5.5.2, open script stack (`tel+hin+eng` etc.) | solid all-rounder |
| `tesseract_bilingual/` | tesseract 5.5.2, eng-led stack | fastest tesseract (probe 0.7 s/page) |
| `anuvaad_tesseract/` | Anuvaad-tuned tesseract weights | tier-1 accuracy (CER 0.48) |
| `openbharatocr/` | mirror of tesseract_indic — byte-identical | documented alias, same family |
| `easyocr/` | easyocr 1.7.2, all-Indic open reader | 391/400 pages nonempty |
| `paddleocr_indic/` | PaddleOCR 3.7.0, per-language models | no Malayalam model — ml pages use the English stack (disclosed) |
| `indicphotoocr/` | IndicPhotoOCR (IIIT-H) | solid mid tier |
| `rapidocr/` | RapidOCR 3.9.2, PP-OCR mobile rec | fastest engine timed (0.44 s/page) |
| `doctr/` | python-doctr 1.1.0 (CRNN) | Latin-only on our pages — honest weakness, kept for record |
| `surya/` | surya-ocr 0.22.1 | tier-1 accuracy leader (CER 0.43) |

The four tesseract folders share one binary, so the honest count is **10 engine
runs = 9 distinct engines = 7 independent families**.

---

## 3. Source pages — PDFs vs PNGs (which JSONs came from which)

Every JSON pack points back to its source page in `image.raw_path` +
`image.page_index`. Sources are of two kinds:

- **PDF pages** — most pages. The JSON's `page_index` says which page of that
  PDF (0-based).
- **PNG scans** — a small number of pages are single-page PNG scans. For
  these, the PNG file itself is the page (`page_index` = 0).

### JSON serial numbers that come from PNG scans

These page_ids exist **in every engine folder** (same 100 pages for all
engines) — open them directly to compare engines on the scan pages:

**Tamil (`ta/`) — 4 pages from PNGs:**
- `ta_001`, `ta_002`, `ta_003`, `ta_004`

**Malayalam (`ml/`) — 9 pages from PNGs:**
- `ml_004`, `ml_005`, `ml_006`, `ml_007`, `ml_008`, `ml_009`, `ml_010`, `ml_011`, `ml_012`

**Telugu (`te/`) and Kannada (`kn/`) — no PNG pages** (all 100 + 100 from PDFs).

### Per-language summary

| lang | JSON files | serial numbers | from PDFs | from PNGs |
|---|---|---|---|---|
| `te` Telugu | 100 | `te_001`–`te_100` | 100 | 0 |
| `ta` Tamil | 100 | `ta_001`–`ta_100` | 96 | **4** (`ta_001`–`ta_004`) |
| `kn` Kannada | 100 | `kn_001`–`kn_100` | 100 | 0 |
| `ml` Malayalam | 100 | `ml_001`–`ml_100` | 91 | **9** (`ml_004`–`ml_012`) |

In any engine folder, per language: `out/<engine>/ta/` holds 100 JSONs, of
which `ta_001.json … ta_004.json` came from single-page PNG scans and the
rest from PDF pages; `out/<engine>/ml/` holds 100 JSONs, of which
`ml_004.json … ml_012.json` came from PNG scans.

---

## 4. What each JSON pack contains

| field | meaning |
|---|---|
| `page_id` | e.g. `te_001` — language + page number (001–100) |
| `ocr_engine` | which engine produced this text |
| `engine_meta` | `{engine, version, policy: open_any_script, dpi: 200}` |
| `image.raw_path` | source file (PDF or PNG) |
| `image.page_index` | 0-based page number inside that file |
| `image.width / height` | page pixel size |
| `regions[].bbox_xyxy` | text-region box on the page |
| `regions[].text` | the raw OCR text — never corrected (raw IS the benchmark) |
| `missing` / `unreadable_reason` | engine read nothing — honest empties, never fabricated |

---

## 5. Where the numbers come from

Every headline number about Level 2 (gap %, accuracy, per-script winners,
latency) is computed from these 4,000 packs by machine — nothing hand-written.
Key results: best-engine volume gap 7.1% (lower bound, on the 177 pages with
a usable text layer); accuracy leaders surya and anuvaad_tesseract (median
character error rate 0.43 / 0.48). Full analysis is generated from these
packs in the vajrAstra repo.

<!-- generated 2026-09-14, disk census: 10 engines x 400 packs; 13 PNG-source pages (ta 4, ml 9) -->
