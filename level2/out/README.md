# Level 2 — Free-OCR Benchmark Outputs (out/)

**Owner:** Srujan Sai (IITGN)  
**Lead:** Vinay Gahlot — Vaultstack AI / BHASHINI AksharDrishti  
**Languages:** Telugu (`te`), Tamil (`ta`), Kannada (`kn`), Malayalam (`ml`)  
**Status:** COMPLETE — 10 engines x 400 pages = **4,000 JSON packs**

This file explains the `out/` folder the same way the Level-1 README explains `labeled/`.
**1 page = 1 sample = 1 JSON file per engine.** The text in each JSON is the **raw OCR
output** — never corrected, never translated; the raw output IS the benchmark.

**There are no source documents in this folder — only the engine outputs.** The source
pages are the SAME files the team already has on Drive in `Dataset/` (4 language
folders). Every source page was rendered to PNG at 200 dpi before the engines read it.

---

## 1. What this folder is

- **Goal (Sep-10 sync):** benchmark free OCR engines on our own data — a reality check
  against published numbers.
- Level 1 (`labeled/`) = AI-assisted page labels. Level 2 (`out/`) = the SAME 400 pages
  run through **10 free OCR engines**.
- Same page_ids as Level 1: `te_001`–`te_100`, `ta_001`–`ta_100`, `kn_001`–`kn_100`,
  `ml_001`–`ml_100`.

---

## 2. Folder layout

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
Opening the same `te_001.json` across all 10 engine folders shows the same page read
by 10 different engines — the benchmark in one click.

**Totals: 400 JSONs per engine · 4,000 JSONs in the whole folder.**

---

## 3. The 10 engine folders

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

The four tesseract folders share one binary, so the honest count is **10 engine runs =
9 distinct engines = 7 independent families**.

---

## 4. Source documents (where the 400 pages come from)

Same sources as Level 1 — the team Drive `Dataset/` folder. The 400 benchmark pages
came from **190 source files: 177 PDFs + 13 PNGs** (Telugu 84 PDF · Tamil 34 PDF + 4 PNG ·
Kannada 40 PDF · Malayalam 19 PDF + 9 PNG).

**How to open a source:**
- **PDF** → open the page at `page_index` (each pack JSON says which page, 0-based).
- **PNG** → the file itself is the page (`page_index` = 0).

In every pack JSON, `image.raw_path` = the source file and `image.page_index` = which
page of that file.

### Telugu (`te`) — under `Dataset/Telugu/` (or equivalent)

- Total source files: **84**
- PDFs: **84**
- PNG images: **0**

**PDF files (84):** multi-page documents. One PDF can contain many
pages; the benchmark picks specific `page_index` values into separate JSONs.

<details><summary>Click to list all PDF filenames</summary>

- `Dataset/Telugu/s_telugu0001pro_raw.pdf`
- `Dataset/Telugu/s_telugu0002pro_raw.pdf`
- `Dataset/Telugu/s_telugu0003pro_raw.pdf`
- `Dataset/Telugu/s_telugu0004pro_raw.pdf`
- `Dataset/Telugu/s_telugu0005pro_raw.pdf`
- `Dataset/Telugu/s_telugu0006pro_raw.pdf`
- `Dataset/Telugu/s_telugu0007pro_raw.pdf`
- `Dataset/Telugu/s_telugu0008pro_raw.pdf`
- `Dataset/Telugu/s_telugu0009pro_raw.pdf`
- `Dataset/Telugu/s_telugu0010pro_raw.pdf`
- `Dataset/Telugu/s_telugu0011pro_raw.pdf`
- `Dataset/Telugu/s_telugu0012pro_raw.pdf`
- `Dataset/Telugu/s_telugu0013pro_raw.pdf`
- `Dataset/Telugu/s_telugu0014pro_raw.pdf`
- `Dataset/Telugu/s_telugu0015pro_raw.pdf`
- `Dataset/Telugu/s_telugu0016pro_raw.pdf`
- `Dataset/Telugu/s_telugu0017pro_raw.pdf`
- `Dataset/Telugu/s_telugu0018pro_raw.pdf`
- `Dataset/Telugu/s_telugu0019pro_raw.pdf`
- `Dataset/Telugu/s_telugu0020pro_raw.pdf`
- `Dataset/Telugu/s_telugu0021pro_raw.pdf`
- `Dataset/Telugu/s_telugu0022pro_raw.pdf`
- `Dataset/Telugu/s_telugu0023pro_raw.pdf`
- `Dataset/Telugu/s_telugu0024pro_raw.pdf`
- `Dataset/Telugu/s_telugu0025pro_raw.pdf`
- `Dataset/Telugu/s_telugu0026pro_raw.pdf`
- `Dataset/Telugu/s_telugu0027pro_raw.pdf`
- `Dataset/Telugu/s_telugu0028pro_raw.pdf`
- `Dataset/Telugu/s_telugu0029pro_raw.pdf`
- `Dataset/Telugu/s_telugu0030pro_raw.pdf`
- `Dataset/Telugu/s_telugu0031pro_raw.pdf`
- `Dataset/Telugu/s_telugu0032pro_raw.pdf`
- `Dataset/Telugu/s_telugu0033pro_raw.pdf`
- `Dataset/Telugu/s_telugu0034pro_raw.pdf`
- `Dataset/Telugu/s_telugu0035pro_raw.pdf`
- `Dataset/Telugu/s_telugu0036pro_raw.pdf`
- `Dataset/Telugu/s_telugu0037pro_raw.pdf`
- `Dataset/Telugu/s_telugu0038pro_raw.pdf`
- `Dataset/Telugu/s_telugu0039pro_raw.pdf`
- `Dataset/Telugu/s_telugu0040pro_raw.pdf`
- `Dataset/Telugu/s_telugu0041pro_raw.pdf`
- `Dataset/Telugu/s_telugu0042pro_raw.pdf`
- `Dataset/Telugu/s_telugu0043pro_raw.pdf`
- `Dataset/Telugu/s_telugu0044pro_raw.pdf`
- `Dataset/Telugu/s_telugu0045pro_raw.pdf`
- `Dataset/Telugu/s_telugu0046pro_raw.pdf`
- `Dataset/Telugu/s_telugu0047pro_raw.pdf`
- `Dataset/Telugu/s_telugu0048pro_raw.pdf`
- `Dataset/Telugu/s_telugu0049pro_raw.pdf`
- `Dataset/Telugu/s_telugu0050pro_raw.pdf`
- `Dataset/Telugu/s_telugu0051pro_raw.pdf`
- `Dataset/Telugu/s_telugu0052pro_raw.pdf`
- `Dataset/Telugu/s_telugu0053pro_raw.pdf`
- `Dataset/Telugu/s_telugu0054pro_raw.pdf`
- `Dataset/Telugu/s_telugu0055pro_raw.pdf`
- `Dataset/Telugu/s_telugu0056pro_raw.pdf`
- `Dataset/Telugu/s_telugu0057pro_raw.pdf`
- `Dataset/Telugu/s_telugu0058pro_raw.pdf`
- `Dataset/Telugu/s_telugu0059pro_raw.pdf`
- `Dataset/Telugu/s_telugu0060pro_raw.pdf`
- `Dataset/Telugu/s_telugu0061pro_raw.pdf`
- `Dataset/Telugu/s_telugu0062pro_raw.pdf`
- `Dataset/Telugu/s_telugu0063pro_raw.pdf`
- `Dataset/Telugu/s_telugu0064pro_raw.pdf`
- `Dataset/Telugu/s_telugu0065pro_raw.pdf`
- `Dataset/Telugu/s_telugu0066pro_raw.pdf`
- `Dataset/Telugu/s_telugu0067pro_raw.pdf`
- `Dataset/Telugu/s_telugu0068pro_raw.pdf`
- `Dataset/Telugu/s_telugu0069pro_raw.pdf`
- `Dataset/Telugu/s_telugu0070pro_raw.pdf`
- `Dataset/Telugu/s_telugu0071pro_raw.pdf`
- `Dataset/Telugu/s_telugu0072pro_raw.pdf`
- `Dataset/Telugu/s_telugu0073pro_raw.pdf`
- `Dataset/Telugu/s_telugu0074pro_raw.pdf`
- `Dataset/Telugu/s_telugu0075pro_raw.pdf`
- `Dataset/Telugu/s_telugu0076pro_raw.pdf`
- `Dataset/Telugu/s_telugu0077pro_raw.pdf`
- `Dataset/Telugu/s_telugu0078pro_raw.pdf`
- `Dataset/Telugu/s_telugu0079pro_raw.pdf`
- `Dataset/Telugu/s_telugu0080pro_raw.pdf`
- `Dataset/Telugu/s_telugu0081pro_raw.pdf`
- `Dataset/Telugu/s_telugu0082pro_raw.pdf`
- `Dataset/Telugu/s_telugu0083pro_raw.pdf`
- `Dataset/Telugu/s_telugu0084pro_raw.pdf`

</details>

### Tamil (`ta`) — under `Dataset/Tamil/` (or equivalent)

- Total source files: **38**
- PDFs: **34**
- PNG images: **4**

**PNG files (each PNG = 1 page sample):**

- `Dataset/Tamil/s_tamil0001pro_raw.png`  → page `ta_001`
- `Dataset/Tamil/s_tamil0002pro_raw.png`  → page `ta_002`
- `Dataset/Tamil/s_tamil0003pro_raw.png`  → page `ta_003`
- `Dataset/Tamil/s_tamil0004pro_raw.png`  → page `ta_004`

**PDF files (34):** multi-page documents. One PDF can contain many
pages; the benchmark picks specific `page_index` values into separate JSONs.

<details><summary>Click to list all PDF filenames</summary>

- `Dataset/Tamil/s_tamil0005pro_raw.pdf`
- `Dataset/Tamil/s_tamil0006pro_raw.pdf`
- `Dataset/Tamil/s_tamil0007pro_raw.pdf`
- `Dataset/Tamil/s_tamil0008pro_raw.pdf`
- `Dataset/Tamil/s_tamil0009pro_raw.pdf`
- `Dataset/Tamil/s_tamil0010pro_raw.pdf`
- `Dataset/Tamil/s_tamil0011pro_raw.pdf`
- `Dataset/Tamil/s_tamil0012pro_raw.pdf`
- `Dataset/Tamil/s_tamil0013pro_raw.pdf`
- `Dataset/Tamil/s_tamil0014pro_raw.pdf`
- `Dataset/Tamil/s_tamil0015pro_raw.pdf`
- `Dataset/Tamil/s_tamil0016pro_raw.pdf`
- `Dataset/Tamil/s_tamil0017pro_raw.pdf`
- `Dataset/Tamil/s_tamil0018pro_raw.pdf`
- `Dataset/Tamil/s_tamil0019pro_raw.pdf`
- `Dataset/Tamil/s_tamil0020pro_raw.pdf`
- `Dataset/Tamil/s_tamil0021pro_raw.pdf`
- `Dataset/Tamil/s_tamil0022pro_raw.pdf`
- `Dataset/Tamil/s_tamil0023pro_raw.pdf`
- `Dataset/Tamil/s_tamil0024pro_raw.pdf`
- `Dataset/Tamil/s_tamil0025pro_raw.pdf`
- `Dataset/Tamil/s_tamil0026pro_raw.pdf`
- `Dataset/Tamil/s_tamil0027pro_raw.pdf`
- `Dataset/Tamil/s_tamil0028pro_raw.pdf`
- `Dataset/Tamil/s_tamil0029pro_raw.pdf`
- `Dataset/Tamil/s_tamil0030pro_raw.pdf`
- `Dataset/Tamil/s_tamil0031pro_raw.pdf`
- `Dataset/Tamil/s_tamil0032pro_raw.pdf`
- `Dataset/Tamil/s_tamil0033pro_raw.pdf`
- `Dataset/Tamil/s_tamil0034pro_raw.pdf`
- `Dataset/Tamil/s_tamil0035pro_raw.pdf`
- `Dataset/Tamil/s_tamil0036pro_raw.pdf`
- `Dataset/Tamil/s_tamil0037pro_raw.pdf`
- `Dataset/Tamil/s_tamil0038pro_raw.pdf`

</details>

### Kannada (`kn`) — under `Dataset/Kannada/` (or equivalent)

- Total source files: **40**
- PDFs: **40**
- PNG images: **0**

**PDF files (40):** multi-page documents. One PDF can contain many
pages; the benchmark picks specific `page_index` values into separate JSONs.

<details><summary>Click to list all PDF filenames</summary>

- `Dataset/Kannada/s_kannada0001pro_raw.pdf`
- `Dataset/Kannada/s_kannada0002pro_raw.pdf`
- `Dataset/Kannada/s_kannada0003pro_raw.pdf`
- `Dataset/Kannada/s_kannada0004pro_raw.pdf`
- `Dataset/Kannada/s_kannada0005pro_raw.pdf`
- `Dataset/Kannada/s_kannada0006pro_raw.pdf`
- `Dataset/Kannada/s_kannada0007pro_raw.pdf`
- `Dataset/Kannada/s_kannada0009pro_raw.pdf`
- `Dataset/Kannada/s_kannada0010pro_raw.pdf`
- `Dataset/Kannada/s_kannada0011pro_raw.pdf`
- `Dataset/Kannada/s_kannada0012pro_raw.pdf`
- `Dataset/Kannada/s_kannada0013pro_raw.pdf`
- `Dataset/Kannada/s_kannada0014pro_raw.pdf`
- `Dataset/Kannada/s_kannada0015pro_raw.pdf`
- `Dataset/Kannada/s_kannada0016pro_raw.pdf`
- `Dataset/Kannada/s_kannada0017pro_raw.pdf`
- `Dataset/Kannada/s_kannada0018pro_raw.pdf`
- `Dataset/Kannada/s_kannada0019pro_raw.pdf`
- `Dataset/Kannada/s_kannada0020pro_raw.pdf`
- `Dataset/Kannada/s_kannada0021pro_raw.pdf`
- `Dataset/Kannada/s_kannada0022pro_raw.pdf`
- `Dataset/Kannada/s_kannada0023pro_raw.pdf`
- `Dataset/Kannada/s_kannada0024pro_raw.pdf`
- `Dataset/Kannada/s_kannada0025pro_raw.pdf`
- `Dataset/Kannada/s_kannada0026pro_raw.pdf`
- `Dataset/Kannada/s_kannada0027pro_raw.pdf`
- `Dataset/Kannada/s_kannada0028pro_raw.pdf`
- `Dataset/Kannada/s_kannada0029pro_raw.pdf`
- `Dataset/Kannada/s_kannada0030pro_raw.pdf`
- `Dataset/Kannada/s_kannada0031pro_raw.pdf`
- `Dataset/Kannada/s_kannada0032pro_raw.pdf`
- `Dataset/Kannada/s_kannada0033pro_raw.pdf`
- `Dataset/Kannada/s_kannada0034pro_raw.pdf`
- `Dataset/Kannada/s_kannada0035pro_raw.pdf`
- `Dataset/Kannada/s_kannada0036pro_raw.pdf`
- `Dataset/Kannada/s_kannada0037pro_raw.pdf`
- `Dataset/Kannada/s_kannada0038pro_raw.pdf`
- `Dataset/Kannada/s_kannada0039pro_raw.pdf`
- `Dataset/Kannada/s_kannada0040pro_raw.pdf`
- `Dataset/Kannada/s_kannada0041pro_raw.pdf`

</details>

### Malayalam (`ml`) — under `Dataset/Malayalam/` (or equivalent)

- Total source files: **28**
- PDFs: **19**
- PNG images: **9**

**PNG files (each PNG = 1 page sample):**

- `Dataset/Malayalam/s_malayalam0005pro_raw.png`  → page `ml_004`
- `Dataset/Malayalam/s_malayalam0006pro_raw.png`  → page `ml_005`
- `Dataset/Malayalam/s_malayalam0007pro_raw.png`  → page `ml_006`
- `Dataset/Malayalam/s_malayalam0008pro_raw.png`  → page `ml_007`
- `Dataset/Malayalam/s_malayalam0009pro_raw.png`  → page `ml_008`
- `Dataset/Malayalam/s_malayalam0010pro_raw.png`  → page `ml_009`
- `Dataset/Malayalam/s_malayalam0011pro_raw.png`  → page `ml_010`
- `Dataset/Malayalam/s_malayalam0012pro_raw.png`  → page `ml_011`
- `Dataset/Malayalam/s_malayalam0013pro_raw.png`  → page `ml_012`

**PDF files (19):** multi-page documents. One PDF can contain many
pages; the benchmark picks specific `page_index` values into separate JSONs.

<details><summary>Click to list all PDF filenames</summary>

- `Dataset/Malayalam/s_malayalam0001pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0002pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0004pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0014pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0015pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0016pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0017pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0018pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0019pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0020pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0021pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0022pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0023pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0024pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0025pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0026pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0027pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0028pro_raw.pdf`
- `Dataset/Malayalam/s_malayalam0029pro_raw.pdf`

</details>

### PNG vs PDF summary (which JSON packs come from which kind)

| lang | pages | from PDFs | from PNGs |
|---|---|---|---|
| `te` Telugu | 100 | 100 | 0 |
| `ta` Tamil | 100 | 96 | 4 |
| `kn` Kannada | 100 | 100 | 0 |
| `ml` Malayalam | 100 | 91 | 9 |

### JSON packs that come from PNG images (open these directly)

**Tamil (4 JSON packs per engine):** `ta_001`, `ta_002`, `ta_003`, `ta_004`

**Malayalam (9 JSON packs per engine):** `ml_004`, `ml_005`, `ml_006`, `ml_007`,
`ml_008`, `ml_009`, `ml_010`, `ml_011`, `ml_012`

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
| `regions[].text` | the raw OCR text — never corrected (raw IS the benchmark) |
| `missing` / `unreadable_reason` | engine read nothing — honest empties, never fabricated |

---

## 6. Where the numbers come from

Every headline number about Level 2 (gap %, accuracy tiers, per-script winners, latency)
is computed from these 4,000 packs by machine — nothing hand-written. The analysis
reports live alongside this folder in the summary package (`SEP16_ONE_SCREEN.md`,
`GAP.md`, `LEADERBOARD_BY_SCRIPT.md`, `CER_BY_SCRIPT.md`).

<!-- generated 2026-09-14, from pages_manifest.json disk census | engines: 10 | packs: 4,000 -->
