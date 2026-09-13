# SOUTH_CANON
# L2 operational law: level2/ULTIMATE_HYBRID_CONCERN.md supersedes where conflicting.
# Single keep-file for understanding (not a summary).
# Merged from: BHASHINI proposal, WhatsApp 9 Sep 2026, meeting 10 Sep 2026, Grok labeling thread 9–11 Sep 2026.
# Live disk: this file + work/ + labeled/ + prompts/ + scripts/. Evidence zips+meeting docx are in Downloads backup.

Last locked: 2026-09-11 (ops section N refreshed)
Operator: Srujan Sai (IITGN) — Vaultstack AI, AksharDrishti
Root on this machine: /Users/srujansai/Desktop/South  (this folder IS south/)

---

## A. Project

BHASHINI AksharDrishti hackathon.
Goal: OCR that actually works on Indian-language citizen documents — printed, handwritten, mixed, low-quality, structured fields — all 22 scheduled languages in the product vision.

Vaultstack pitch (from the 4-page proposal PDF Vinay circulated):
- Akshara-aware layout + recognition (conjuncts, matras, sandhi)
- Calibrated confidence, visual lookup, per-language morphology
- Structured fields; low-confidence spans always go to human review
- Pipeline stages in the deck:
  0 OpenCV deskew/denoise/binarize
  1 DocLayout-YOLO / IndicDLP LoRA for layout
  2 Parallel SFT: TrOCR + Qwen 3.5 VL + PaddleOCR VL 1.6, akshara-boundary auxiliary loss
  2b SCST / RL on CER
  3 small LLM SFT noisy-text → JSON
  3b SimPO or DPO on ranked JSON
  Bench: Sarvam, IndicDLP, Indic Vision Bench — no fine-tune on test

That pipeline is the team product. It is not Srujan’s job this week.

---

## B. People

| Person | Role | This week |
|--------|------|-----------|
| Vinay Gahlot | CEO, IIM-A | data, language sheet, GitHub, Saturday David call, free-tier API list |
| Akshay Gahlot | CTO, IITD | systems (not in the 10 Sep body-split) |
| David Babu | AI advisor | Saturday methodology. Do not wait for him to start labeling |
| Aryan (IITB) | pipeline | ingest samples → run VLM → dump outputs. GitHub setup. Exams soon; Srujan may take pipeline later |
| Krishna Jangid (IITJ) | North + samples | North langs (Punjabi, Gujarati, …). Create 20-sample sets in OCR_data/working_experiments |
| Srujan Sai (IITGN) | South labeling | start labeling directly on South languages |

Do not steal Aryan’s pipeline or Krishna’s sample-cutting.

---

## C. WhatsApp 9 Sep (Vinay ↔ Srujan)

Vinay: “first focus on how to label the dataset we already have” then “will share the data also.”
Shared Google Slides “overall strategy.”
Srujan asked group vs DM; Vinay dropped the slides link in that chat.

Srujan later sent:
labeling really lands on proprietary govt+exam scans; public sets already come labeled; the fork is born-digital PDF vs photographed image; PDF text layer is free GT; asked 20–30 sample pages before the call.

Vinay: “I will share the whole dataset.”

Then the 10 Sep call happened and replaced “wait for 20–30 pages” with: full dump + Krishna 20-sample working folder + language assignment sheet.

Do not re-send the five-layer essay into the group. Counts + files only.

---

## D. Meeting 10 Sep 2026 — Srujan’s part, as spoken

Source: Google doc “sync - ocr - September 10” + Fathom recording notes.
https://docs.google.com/document/d/1Nq0n01hgzyhoOEiAfTLjkz2JFJMtjH3C7bh2GMpwbdE/edit

Meeting docx backup: `~/Downloads/South_backup_evidence_2026-09-11/sync - ocr - September 10.docx`

Official action items:
- Share free-tier API sources in group
- Create GitHub repo; invite Srujan, Krishna, Vinay; set up benchmarking pipeline; share results
- Schedule Sat call with David re OCR/VLM pipeline
- Create language assignment sheet; share with Srujan, Krishna, Aryan
- Share OCR data with Srujan, Krishna, Aryan; create OCR_data/working_experiments; Krishna creates 20-sample sets
- Share meeting recording and notes

Quotes that lock Srujan:
- Srujan: showed “one I have made from Grok” — five labeling parts, layer zero page meta first.
- Vinay: “I got it… the pipeline… I think it’s in the right direction.”
- Vinay: “Srujan, maybe can you start with the labeling part directly? … you take some South languages.”
- Vinay: “Krishna, you take like all the north-end languages… Punjabi, Gujarati also… I’ll put up a sheet.”
- Aryan offered English or Hindi, or Assamese/Bangla.
- Vinay to Aryan: lead setup / build the ingest-VLM pipeline; Srujan takes over later because Aryan will be in exams.
- Vinay: “I’ll share the full data with all of you… you will be not using the whole data at a time… first hundred samples… Krishna will put out samples for each data, like 20 samples… working experiments.”
- GitHub for code. Data does not go on GitHub. LFS was mentioned; still do not commit zips/images unless Vinay says so.
- David has more depth on “what exactly needs to be done.” Saturday. Labeling still starts now.

Ignore any auto-summary that assigned Assamese/Bengali to Srujan. That mixed names. Spoken South = Dravidian four until the sheet says otherwise.

Until the language sheet arrives, Srujan languages are only:
- te Telugu script Telu
- ta Tamil script Taml
- kn Kannada script Knda
- ml Malayalam script Mlym

Srujan can personally gold-check Telugu. ta/kn/ml text is T3 until a native reader accepts it.

---

## E. What “the dataset we already have” was in the proposal

| Code | Source | Already gold? | What to do |
|------|--------|---------------|------------|
| S1 | BSTD scene text | yes polygons+text+script | remap meta, audit, do not redraw |
| S2 | IIIT-HW / INDIC-HW-WORDS | yes crop+text | add script/lang/tier |
| S3 | Sangraha / IndicCorp | text only | do not OCR-label; render later |
| S4 | Bhashadaan | dirty | re-verify later |
| S5 | govt / exam scans | usually raw | full L0+L1+L2 — the real new gold |
| S6 | synthetic | gold by construction | never put in eval |

If a zip is clearly S1/S2/IndicDLP for these four languages: inventory, mark inherited_public / T4, do not redraw tonight.
If a zip is raw pages/PDFs: treat as S5.

Born-digital PDF text layer under a box is free ground truth. That was the one technical point Vinay absorbed from Srujan’s WhatsApp.

---

## F. Label definition (the system produced in the Grok thread)

A page is not labeled because someone ran OCR on it.
A page is labeled when a JSON answers five questions:
1. kind — source, modality, domain, lang, script
2. where — boxes, class, reading order
3. glyphs — NFC string as on the page
4. proof — tier + provenance
5. object — structure JSON (can lag; not required for first 10 pages)

Layers ↔ pipeline:
- L0 meta → sampling, loss weights
- L1 layout → Stage 1 YOLO
- L2 transcript → Stage 2 SFT
- L2A akshara list → aux loss (lag ok)
- L3 JSON object → Stage 3 (lag ok)
- L4 tier + ranked hyps → 2b/3b (no extra collection; lag ok)

This run: L0+L1+L2 only.

### L1 classes for this run
paragraph, header, footer, page-number, section-title, table, table-caption, figure, figure-caption, form-field-label, form-field-value, handwritten-span, stamp-or-seal, signature, ordered-list, unordered-list

Full IndicDLP-42 exists if needed later (advertisement, answer, author, chapter-title, contact-info, dateline, first-level-question, flag, folio, footnote, formula, headline, index, jumpline, options, placeholder-text, quote, reference, second-level-question, sidebar, sub-* title/list/headline, table-of-contents, third-level-question, website-link, unordered-list, …). Do not explode the class list on night one.

Handwritten name in a printed form = form-field-value + region.modality handwritten.

### L2 trust order
1. PDF text layer under the box → born_digital_pdf
2. Type what is visible → human
3. VLM/OCR draft → distilled_vlm

VLM gates (fail ⇒ T3): length plausible vs box; do not dump unrelated English on a non-English stamp when the stamp itself is non-English.
Note: many real pages are mixed (English + South script). Mixed English on the page must still be transcribed (see §N). Do not use “English present” as a reason to blank the label.

### Tiers
- T0 two humans, or PDF-extract + second check
- T1 one verified pass
- T2 VLM + gates — low-weight train only, never eval
- T3 unread / failed / missing L2 / truly blank or unopenable after attempt
- T4 inherited public, unaudited

Telugu verified against page → T1.
For draft AI labeling runs: write visible text even for ta/kn/ml (tier T2 is fine). Native-reader acceptance is required before calling those strings training-gold / T0.
Empty L2 + T3 only if page is truly blank/illegible/unopenable after open — not as a shortcut.
Do not invent glyphs that are not on the page.
Do not “fix” spelling. Gold is the glyphs on the page.

### Script ≠ language
Always store both. Devanagari is not automatically Hindi. These four are Telu/Taml/Knda/Mlym.

---

## G. JSON every page must become

```json
{
  "page_id": "te_001",
  "source": "S5_govt",
  "lang": "te",
  "script": "Telu",
  "modality": "printed",
  "domain": "unknown",
  "quality_tier": "T1",
  "missing": [],
  "unreadable_reason": null,
  "image": { "raw_path": "work/te/<file>", "page_index": 0, "width": 1654, "height": 2339 },
  "regions": [
    {
      "region_id": "r1",
      "cls": "paragraph",
      "bbox_xyxy": [x1, y1, x2, y2],
      "reading_order": 1,
      "modality": "printed",
      "text": "exact glyphs on the page",
      "text_nfc": "NFC of text",
      "provenance": "human"
    }
  ]
}
```

If tier is T3: `missing` must include `"L2"`, `text` empty, and `unreadable_reason` nonempty.
provenance enum: born_digital_pdf | human | distilled_vlm | inherited_public
modality page enum: printed | handwritten | scene | mixed
source enum if known: S1_bstd | S2_hw | S3_text | S4_bhashadaan | S5_govt | S6_synth

Boxes: layout model or OpenCV if present. Else one honest full-page paragraph box beats fake precise boxes.
`image.width` / `height` must be real (never 0). `page_index` required for multi-page PDFs.

---

## H. Disk contract after you delete `agents/`

Live project folder (`/Users/srujansai/Desktop/South`):
```
SOUTH_CANON.md
work/{te,ta,kn,ml}/          # live extracted pages (source of truth for labeling)
labeled/{te,ta,kn,ml}/       # JSON labels (real output)
prompts/                     # agent paste prompts + page_list_freeze.json
scripts/ .venv/ requirements.txt .gitignore
```

Evidence backup (moved out to declutter — do not delete):
```
~/Downloads/South_backup_evidence_2026-09-11/
  Telugu-….zip  Tamil-….zip  Kannada-….zip  Malayalam-….zip
  sync - ocr - September 10.docx
```

Meeting understanding lives in this SOUTH_CANON.md.  
Page bytes live in `work/`. Zips/docx are only offline evidence copies now.  
Never modify/delete `work/` casually. Re-unzip from Downloads backup only if `work/` is damaged.

---

## I. What agents must do now (no architecture talk)

Setup phases A–B are already done (`work/` exists).

Labeling:
- Use `prompts/*_B*_slot*.md` (FINAL-3b) for batch runs, or `prompts/PATH_A_GAP_COMPLETION.md` for leftover gaps only.
- 1 JSON = 1 page. Write L0+L1+L2. Full visible text including English/mixed.
- PDF text layer first when present; else read the page image. Do not invent glyphs.
- Password/unopenable/truly blank → substitute next sequential openable freeze pair; do not keep useless empty JSON.
- Halt with counts. Orchestrator reviews only — does not rewrite labels while testing AI.

Forbidden:
Aryan pipeline; training; Qwen/Paddle/YOLO fine-tune; SimPO; git-add of zips/images; 22 languages; new taxonomy; spell-correction into “proper” language; empty stubs when glyphs are visible.

---

## J. Messages already sent — do not contradict

To Vinay: labeling focus on proprietary scans; PDF text layer matters; asked samples; he promised whole dataset.
In meeting: showed 5-layer Grok structure; accepted South + start now.
Do not paste this canon into WhatsApp. If anything goes to the group: inventory counts and example JSON paths only (e.g. South labeling: N te / N ta / N kn / N ml draft pages).

---

## K. Open blockers (facts, not tasks for inventing)

- Language assignment sheet from Vinay not confirmed in this workspace
- Krishna 20-sample folder was not inside the 4 language zips (those are language dumps)
- GitHub invite may still be pending
- David Saturday may still be pending
- ta/kn/ml native reviewers not named
- Some `work/te` and `work/ta` PDFs are English/Hindi books despite folder names (mixed dump)

---

## L. Done / current state

This file replaces the agent-conversation folder.
Extract is done. B0-style draft labeling has started under `labeled/` (many nonempty JSONs).
Path A: keep drafts, stop prompt churn, optional gap prompt only, review-only for orchestrator.
Everything else waits on the operator.

---

## M. Compact operator card (same law)

### Split
Vinay: data, language sheet, GitHub, Sat David call
Aryan: VLM pipeline. Do not build this.
Krishna: North langs + 20-sample sets
Srujan: South labeling only — te ta kn ml
David: Saturday methodology. Do not wait.

### Do now
- Continue/scale labeling with existing FINAL-3b prompts or Path A gap prompt
- Prefer PDF text-layer pages for max yield; measure AI misses as benchmark
- Share counts + examples with Vinay; no pipeline/train; no zip uploads

### Setup status (machine)
- 2026-09-11: SOUTH_CANON locked; agent conversation folder deleted; zips+meeting docx moved to `~/Downloads/South_backup_evidence_2026-09-11/`.
- Phases A–B done: `work/{te,ta,kn,ml}/` extracted.
- Tooling ready: `.venv`, `scripts/`, `requirements.txt`, `.gitignore`.
- Agent paste prompts: `prompts/*_B*_slot*.md` only (one AI per batch, full 20 labels from scratch).
- Each prompt embeds its 20 page targets. Assign all 5 batches x 4 langs fresh.

---

## N. Operations lock (merged from deleted status notes — 2026-09-11)

### Cleanup note
- `graphify-out/` and `.vision_cache/` removed (not labeling inputs/outputs).
- Old labeled JSONs archived to `~/Downloads/South_backup_evidence_2026-09-11/labeled_old_archive_*.tar.gz`.
- Native images live in `work/ta/*.png` and `work/ml/*.png`; prompts require JSON for those too.


**Do not recreate extra status MD files.** Important facts live here only.

### Path A decision
- Stop endless prompt-version / redo theater.
- Keep good nonempty labels as draft fuel + AI-capability evidence.
- Orchestrator **reviews only** — must not rewrite model labels while testing AI.
- Assign all batch prompts fresh. After runs, optional check: `python scripts/verify_labels.py`.

### B0 inventory snapshot (at Path A lock)
- KEEP-ish nonempty (>=50 chars): majority of te/ta/kn/ml B0 (~73/80 class).
- Typical gaps seen: `te_011`, `te_013`, `kn_005` missing; `ta_005`, `ta_016`, `ml_014`, `ml_016` weak/short/empty (re-check disk before any gap run).
- Contaminated orchestrator rewrites (if any) belong in `labeled/_orchestrator_contaminated_do_not_score/` — **do not score as model output**.

### Root causes (not filename drama)
1. **Mixed dump:** some files under `work/te` / `work/ta` are English/Hindi books (names lie). AI often transcribed what was on the page.
2. **Hard pages:** blank last pages, handwriting, scans without text layer → short/empty/missing.
3. **Chat-agent limits:** not a perfect unattended Indic OCR factory; will cut corners unless rules + tooling are strict.
4. **Password PDFs:** cannot open → substitute next sequential openable page (do not keep useless empty JSON).

### How to use AI results (so we are not fooled)
- Nonempty rate / short rate / missing rate / wrong-script-dominant rate = **benchmark of today’s AI on OUR data**.
- Low or messy ≠ “project is fake”; it means AI drafts need review and hard pages need better OCR tooling or humans.
- Maximize yield: prefer PDF text-layer pages first; for scans prefer API vision OCR script over endless chat babysitting.

### Disk keep-set (live)
```
SOUTH_CANON.md          # this file only for understanding
work/{te,ta,kn,ml}/     # extracted masters
labeled/{te,ta,kn,ml}/  # JSON labels (the real output)
prompts/*_slot*.md      # one prompt = one batch = one AI
scripts/ .venv/ requirements.txt .gitignore
```
Evidence zips+docx: `~/Downloads/South_backup_evidence_2026-09-11/`


---

---

## O. Level 2 — Indian OCR model outputs (current)

Level 1 archived in `arc_level_1/` — leave it alone.

Level 2 goal (what Vinay wants):
- Same Dataset pages
- Run **Indian / Indic OCR systems**
- Save their outputs as Level-1-style JSON packs
- Those outputs can be kept as benchmarks

Working folder: `level2/`
- `prompts/` — 20 batch prompts (100 pages × 4 langs, 5 batches)
- `out/<engine>/{te,ta,kn,ml}/` — JSON outputs per engine
- `pages_manifest.json` — the 400 page targets
- `ENGINES.txt` — engine list

First 5 engines (OSS):
1. tesseract_indic
2. indicphotoocr
3. openbharatocr
4. paddleocr_indic
5. easyocr

Assign: for each engine, run all 20 prompts (or equivalent scripts), writing into `level2/out/<engine>/...`.
