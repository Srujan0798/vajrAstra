# Level 2 — Free-OCR Benchmark Outputs (`out/`) README

**Owner:** Srujan Sai (IITGN)
**Lead:** Vinay Gahlot — Vaultstack AI / BHASHINI AksharDrishti
**Languages:** Telugu (`te`), Tamil (`ta`), Kannada (`kn`), Malayalam (`ml`)
**Status:** COMPLETE — 10 engines × 400 pages = **4,000 JSON packs**

This file explains the `out/` folder the same way the Level-1 README explains
`labeled/`. **1 page = 1 sample = 1 JSON file per engine.** The text in each
JSON is the **raw OCR output** — never corrected, never translated.

**Source documents are NOT in this folder.** They are the SAME files the team
already has on Drive in **`Dataset/`** (Telugu / Tamil / Kannada / Malayalam
folders). All 400 pages were rendered to PNG at 200 dpi (in the repo at
`level2/renders_shared/`) before the engines read them.

---

## 1. What this folder is

- **Goal (Sep-10 sync):** benchmark free OCR engines on OUR data — reality
  check vs published numbers. This is exactly that.
- Level 1 (`labeled/`) = AI-assisted page labels. Level 2 (`out/`) = the same
  400 pages run through **10 free OCR engines**.
- Same page_ids as Level 1: `te_001`–`te_100`, `ta_001`–`ta_100`,
  `kn_001`–`kn_100`, `ml_001`–`ml_100`.

---

## 2. Folder layout

```
out/
├── README.md              ← this file
├── tesseract_indic/       ← 10 engine folders, each identical in shape:
│   ├── te/                te_001.json … te_100.json   (100 packs)
│   ├── ta/                ta_001.json … ta_100.json   (100 packs)
│   ├── kn/                kn_001.json … kn_100.json   (100 packs)
│   └── ml/                ml_001.json … ml_100.json   (100 packs)
├── tesseract_bilingual/   (same 4×100 shape)
├── anuvaad_tesseract/     (same)
├── openbharatocr/         (same)
├── easyocr/               (same)
├── paddleocr_indic/       (same)
├── indicphotoocr/         (same)
├── rapidocr/              (same)
├── doctr/                 (same)
└── surya/                 (same)
```

Full path example: `out/surya/te/te_001.json` = engine **surya**, page **te_001**.
To see the benchmark in one click: open `te_001.json` in all 10 engine
folders — same page, 10 different OCR readings.

**Totals per engine: 400 JSONs. Whole folder: 4,000 JSONs.**

---

## 3. The 10 engine folders

| folder | engine / setup | honest note |
|---|---|---|
| `tesseract_indic/` | tesseract 5.5.2, open script stack (`tel+hin+eng` etc.) | solid all-rounder |
| `tesseract_bilingual/` | tesseract 5.5.2, eng-led stack | fastest timed (probe 0.7 s/page) |
| `anuvaad_tesseract/` | Anuvaad-tuned tesseract weights | **tier-1 accuracy (CER 0.48)** |
| `openbharatocr/` | **mirror of tesseract_indic** — byte-identical | documented alias, same family |
| `easyocr/` | easyocr 1.7.2, all-Indic open reader | 391/400 pages nonempty |
| `paddleocr_indic/` | PaddleOCR 3.7.0, per-language models | **no Malayalam model** — ml pages use English stack (disclosed) |
| `indicphotoocr/` | IndicPhotoOCR (IIIT-H) | solid mid tier |
| `rapidocr/` | RapidOCR 3.9.2, PP-OCR mobile rec | **fastest engine timed (0.44 s/page)** |
| `doctr/` | python-doctr 1.1.0 (CRNN) | Latin-only on our pages — honest weakness, kept for record |
| `surya/` | surya-ocr 0.22.1 | **tier-1 accuracy leader (CER 0.43)** |

The four tesseract folders share one binary (same engine, different model
stacks), so the count is **10 engine runs = 9 distinct engines = 7
independent families**.

---

## 4. Where the source pages are (PDFs vs PNGs — open these directly)

**Same sources as Level 1 — the team Drive `Dataset/` folder.** 400 pages
came from **190 source files: 177 PDFs + 13 PNGs** (Telugu 84 PDF · Tamil
34 PDF + 4 PNG · Kannada 40 PDF · Malayalam 19 PDF + 9 PNG).

**PDF → open page `page_index`** (the pack JSON says which page, 0-based).
**PNG → the file itself is the page** (`page_index` = 0). In every pack:
`image.raw_path` = source file, `image.page_index` = which page of it.

### JSON packs that come from PNG images (each PNG = 1 page sample)

**Tamil (4 pages):** `ta_001`, `ta_002`, `ta_003`, `ta_004`
→ `Dataset/Tamil/s_tamil0001pro_raw.png` … `s_tamil0004pro_raw.png`

**Malayalam (9 pages):** `ml_004` … `ml_012`
→ `Dataset/Malayalam/s_malayalam0004pro_raw.png` … `s_malayalam0012pro_raw.png`

### JSON packs that come from PDF pages (per language)

| lang | pages | from PDFs | from PNGs |
|------|-------|-----------|-----------|
| `te` Telugu | 100 | 100 | 0 |
| `ta` Tamil | 100 | 96 | 4 |
| `kn` Kannada | 100 | 100 | 0 |
| `ml` Malayalam | 100 | 91 | 9 |

Telugu PDFs: `s_telugu0001…0084pro_raw.pdf` (84 files) — Kannada PDFs:
`s_kannada0001…0040pro_raw.pdf` (40) — Tamil PDFs: `s_tamil0005…0038pro_raw.pdf`
(34) — Malayalam PDFs: `s_malayalam0013…0031pro_raw.pdf` (19).

---

## 5. What each JSON pack contains

| field | meaning |
|---|---|
| `page_id` | e.g. `te_001` — language + page number (001–100) |
| `ocr_engine` | which engine produced this text |
| `engine_meta` | `{engine, version, policy: open_any_script, dpi: 200}` |
| `image.raw_path` | source file in `Dataset/` (PDF or PNG — see §4) |
| `image.page_index` | 0-based page number inside that file |
| `image.width / height` | page pixel size |
| `regions[].bbox_xyxy` | text-region box on the page |
| `regions[].text` | **the raw OCR text** — never corrected (raw IS the benchmark) |
| `missing` / `unreadable_reason` | engine read nothing — honest empties, never fabricated |

---

## 6. Quick checks anyone can do

- Count: any engine folder → 4 language subfolders × 100 JSONs = 400.
- Cross-engine compare: open `out/surya/te/te_001.json` vs
  `out/easyocr/te/te_001.json` — same page, different readings.
- Analysis built from these packs: `level2/upload_sept16/` (gap %, accuracy
  tiers, per-script winners — all machine-generated).

---

## 7. GitHub copies

- outputs: https://github.com/Srujan0798/vajrAstra/tree/main/level2/out
- summary: https://github.com/Srujan0798/vajrAstra/tree/main/level2/upload_sept16
