# W2 · Variance evidence, candidate pools, re-source plan (proto-21)

**Agent:** ENGINE · **Closes:** CO-022, CO-023, CO-024 · **Date:** 2026-09-30
**Input:** `level2/unified/manifest_22.json` (1,683 items, 22 languages, locked — read-only),
`level2/probe22/candidates/<code>.json` (read-only), `arc_level_1/labeled/<lang>/*.json` (read-only).
**Script:** `level2/unified/variance_22.py` (reproduces every number below; run `python3 level2/unified/variance_22.py`).
**Gates:** `level2/probe22/extract_gt.py:66-69` — MIN_CHARS=50, MIN_SCRIPT_RATIO=0.5, MAX_LATIN_RATIO=0.6, MAX_CTRL_CHARS=3. Never relaxed.

## Summary (≤10 lines)

1. Labelled 1,683/2,200 (22 langs); deficit **517**, all in 8 short languages (as 19 · mni 20 · sat 20 · gu 24 · doi 27 · ne 37 · brx 67 · or 69).
2. **Pair tier (bn/hi/sa): CO-022/023/024 all DISPROVEN** — 100 distinct images, top-1 share 1%, ids spread pool-wide (bn 32→3088, hi 18→3461, sa 22→506).
3. **First-page-only (CO-022): CONFIRMED** for ur (34/100 = 34%) and doi (6/7 = 86%); **PARTIAL** ks (15%), mai/mr/pa/brx/or (1–11%); DISPROVEN gu/kok/ne/sd (0%).
4. **Clustered (CO-024): CONFIRMED** as/kn/ml/ta/te (single source), mni/sat (single benchmark), doi (74%), gu (83%), ne (54%), or (72%), pa (90%); **kok exactly 50/50 = PARTIAL** (structural: 2 PDFs).
5. **One-paper/single-source (CO-023): CONFIRMED** fill tier (as/mni/sat = sarvam_bench) and **South (kn/ml/ta/te = S5_govt, all 100/100)** — new measured fact.
6. **Closable from PDFs alone: +17 items** (as +11, gu +6); mni/sat/doi/ne/brx/or have 0 remaining clean candidates. 517 not closable — structural.
7. **Official pairs: 0 usable.** Nepali's 193 "pairs" carry NO transcription text (Pascal-VOC bbox-only XMLs, 0/193 with `<Unicode>`, 0 `.txt` files) — option (b) is dead for every short language.
8. Why short: honesty gates reject PDF text layers (mojibake/short-Latin) — not page offsets. sat has NO text layer at all (0/207 pages); mni 1,353/1,353 rejected; gu 3,486/3,567 rejected.
9. Re-draw proposals (kok, pa, ur, ks) — see table; **proposals only, executing changes the locked manifest (boss decision U5).**
10. Locked files untouched; verdict check passed (brx + ur rows recomputed independently, all "remaining" numbers re-confirmed from JSON).

## 1. Variance table (all 22 languages)

Measured by `variance_22.py` from manifest_22.json. "Distinct docs" spans tiers (PDFs + fill source / South GT `source` field). Page offsets exist only for pdf_layer. Pair id = numeric id from the symlink target (`os.readlink`).

| lang | n | tiers | distinct docs | top-1 share | distinct pages | offsets min/q25/med/q75/max | page≤1 | pair id min/med/max | flags |
|---|---|---|---|---|---|---|---|---|---|
| as | 19 | fill:19 | 1 | 100% | 19 | - | - | - | clustered, single-source |
| bn | 100 | gold_pair:100 | 100 | 1% | 100 | - | - | 32/905/1586/2376/3088 | none |
| brx | 67 | fill:20+pdf:47 | 7 (6 PDFs) | 39% | 67 | 0/5/16/24/36 | 5/47 (11%) | - | none |
| doi | 27 | fill:20+pdf:7 | 4 (3 PDFs) | 74% | 27 | 0/0/1/1/2 | 6/7 (86%) | - | clustered, first-page-bias |
| gu | 24 | fill:20+pdf:4 | 2 (1 PDF) | 83% | 24 | 3/5/6/6/10 | 0/4 (0%) | - | clustered |
| hi | 100 | gold_pair:100 | 100 | 1% | 100 | - | - | 18/1150/1988/2835/3461 | none |
| kn | 100 | south_label:100 | 1 (S5_govt) | 100% | 100 | - | - | - | clustered, single-source |
| kok | 100 | pdf_layer:100 | 2 | 50% | 100 | 2/31/75/133/225 | 0/100 (0%) | - | none |
| ks | 100 | pdf_layer:100 | 10 | 11% | 100 | 0/3/8/14/42 | 15/100 (15%) | - | none |
| mai | 100 | pdf_layer:100 | 8 | 13% | 100 | 0/16/33/55/94 | 2/100 (2%) | - | none |
| ml | 100 | south_label:100 | 1 (S5_govt) | 100% | 100 | - | - | - | clustered, single-source |
| mni | 20 | fill:20 | 1 | 100% | 20 | - | - | - | clustered, single-source |
| mr | 100 | pdf_layer:100 | 7 | 20% | 100 | 0/20/44/77/151 | 2/100 (2%) | - | none |
| ne | 37 | fill:20+pdf:17 | 2 (1 PDF) | 54% | 37 | 9/22/35/42/51 | 0/17 (0%) | - | clustered |
| or | 69 | fill:19+pdf:50 | 2 (1 PDF) | 72% | 69 | 0/12/41/55/67 | 2/50 (4%) | - | clustered |
| pa | 100 | pdf_layer:100 | 2 | 90% | 100 | 1/1433/3469/5862/7367 | 1/100 (1%) | - | clustered |
| sa | 100 | gold_pair:100 | 100 | 1% | 100 | - | - | 22/136/245/415/506 | none |
| sat | 20 | fill:20 | 1 | 100% | 20 | - | - | - | clustered, single-source |
| sd | 100 | pdf_layer:100 | 16 | 13% | 100 | 3/58/128/217/632 | 0/100 (0%) | - | none |
| ta | 100 | south_label:100 | 1 (S5_govt) | 100% | 100 | - | - | - | clustered, single-source |
| te | 100 | south_label:100 | 1 (S5_govt) | 100% | 100 | - | - | - | clustered, single-source |
| ur | 100 | pdf_layer:100 | 38 | 3% | 100 | 0/1/4/7/15 | 34/100 (34%) | - | first-page-bias |

South sources distribution (from GT json `source` field): **kn S5_govt=100 · ml S5_govt=100 · ta S5_govt=100 · te S5_govt=100** — every South page is one source.

## 2. Shortcut verdicts (CO-022 / CO-023 / CO-024)

| lang | first-page-only (CO-022) | one-paper/single-source (CO-023) | clustered (CO-024) |
|---|---|---|---|
| as | N/A (no page offsets) | CONFIRMED (1 source: sarvam_bench) | CONFIRMED (top-1 100%) |
| bn | N/A (no page offsets) | DISPROVEN (100 docs, top-1 1%) | DISPROVEN (100 docs, top-1 1%) |
| brx | PARTIAL (5/47 = 11%) | DISPROVEN (7 docs, top-1 39%) | DISPROVEN (7 docs, top-1 39%) |
| doi | CONFIRMED (6/7 = 86%) | PARTIAL (4 docs, top-1 74%) | CONFIRMED (top-1 74% > 50%) |
| gu | DISPROVEN (0/4) | PARTIAL (2 docs, top-1 83%) | CONFIRMED (top-1 83% > 50%) |
| hi | N/A (no page offsets) | DISPROVEN (100 docs, top-1 1%) | DISPROVEN (100 docs, top-1 1%) |
| kn | N/A (no page offsets) | CONFIRMED (1 source: S5_govt) | CONFIRMED (top-1 100%) |
| kok | DISPROVEN (0/100) | DISPROVEN (2 docs, top-1 50%) | PARTIAL (2 docs, top-1 exactly 50%) |
| ks | PARTIAL (15/100 = 15%) | DISPROVEN (10 docs, top-1 11%) | DISPROVEN (10 docs, top-1 11%) |
| mai | PARTIAL (2/100 = 2%) | DISPROVEN (8 docs, top-1 13%) | DISPROVEN (8 docs, top-1 13%) |
| ml | N/A (no page offsets) | CONFIRMED (1 source: S5_govt) | CONFIRMED (top-1 100%) |
| mni | N/A (no page offsets) | CONFIRMED (1 source: sarvam_bench) | CONFIRMED (top-1 100%) |
| mr | PARTIAL (2/100 = 2%) | DISPROVEN (7 docs, top-1 20%) | DISPROVEN (7 docs, top-1 20%) |
| ne | DISPROVEN (0/17) | PARTIAL (2 docs, top-1 54%) | CONFIRMED (top-1 54% > 50%) |
| or | PARTIAL (2/50 = 4%) | PARTIAL (2 docs, top-1 72%) | CONFIRMED (top-1 72% > 50%) |
| pa | PARTIAL (1/100 = 1%) | PARTIAL (2 docs, top-1 90%) | CONFIRMED (top-1 90% > 50%) |
| sa | N/A (no page offsets) | DISPROVEN (100 docs, top-1 1%) | DISPROVEN (100 docs, top-1 1%) |
| sat | N/A (no page offsets) | CONFIRMED (1 source: sarvam_bench) | CONFIRMED (top-1 100%) |
| sd | DISPROVEN (0/100) | DISPROVEN (16 docs, top-1 13%) | DISPROVEN (16 docs, top-1 13%) |
| ta | N/A (no page offsets) | CONFIRMED (1 source: S5_govt) | CONFIRMED (top-1 100%) |
| te | N/A (no page offsets) | CONFIRMED (1 source: S5_govt) | CONFIRMED (top-1 100%) |
| ur | CONFIRMED (34/100 = 34%) | DISPROVEN (38 docs, top-1 3%) | DISPROVEN (38 docs, top-1 3%) |

Notes: fill-tier "single-source" = one benchmark pool (sarvam_bench) with distinct images — not literally one paper's pages. kok's clustered verdict is PARTIAL because it sits exactly on the 50% line with 2 docs (structural, not a sampling fault). South single-source = one GT provenance (S5_govt), not one paper.

## 3. Candidate pools — 8 short languages

From `candidates/<code>.json` + official-dir listing (read-only). "drawn" = manifest pdf_layer (pdf,page) pairs matched against the candidate list.

| lang | n | PDFs | pages scanned | pages with text | rej moji | rej short/Latin | clean cands | cand PDFs | drawn | remaining | official pairs (usable) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| as | 19 | 40 | 4,241 | 2,504 | 898 | 1,600 | 11 | 1 | 0 | **11** | 0 |
| mni | 20 | 10 | 1,358 | 1,353 | 689 | 664 | 0 | 0 | 0 | 0 | 0 |
| sat | 20 | 3 | 207 | **0** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gu | 24 | 220 | 13,406 | 3,567 | 3,486 | 71 | 10 | 1 | 4 | **6** | 0 |
| doi | 27 | 6 | 446 | 11 | 1 | 3 | 7 | 3 | 7 | 0 | 0 |
| ne | 37 | 30 | 4,146 | 464 | 411 | 36 | 17 | 1 | 17 | 0 | 0 (of 193 images) |
| brx | 67 | 32 | 3,349 | 2,428 | 886 | 1,495 | 47 | 6 | 47 | 0 | 0 |
| or | 69 | 27 | 1,767 | 1,625 | 74 | 1,508 | 50 | 1 | 50 | 0 | 0 |

**Why short (one line each):**
- **as**: PDF text layers fail the gates (898 mojibake + 1,600 short/Latin rejections); the 11 clean pages all come from one PDF (s_assamese0006pro_raw.pdf).
- **mni**: PDF text layers fail the gates — all 1,353 pages with text rejected (689 mojibake + 664 short/Latin); 0 clean.
- **sat**: NO text layer at all — 0 of 207 pages carry any text; 3 image-only PDFs; nothing for the gates to pass.
- **gu**: legacy font encodings — 3,486 of 3,567 text pages rejected as mojibake; the 10 clean pages all come from one PDF (s_gujarati0005pro_raw.pdf).
- **doi**: only 11 of 446 pages carry any text layer; the 7 clean pages (3 PDFs) are all drawn.
- **ne**: only 464 of 4,146 pages have text (411 mojibake rejections); the 17 clean pages all come from one PDF (s_nepali0010pro_raw.pdf), all drawn, and ne PDF-tier GT is BARRED (R5).
- **brx**: text layers fail the gates (886 mojibake + 1,495 short/Latin); the 47 clean pages (6 PDFs) are all drawn.
- **or**: text layers fail the gates (74 mojibake + 1,508 short/Latin); the 50 clean pages all come from one PDF (s_odia0026pro_raw.pdf), all drawn.

**Official pairs check (read-only):** the only short-language directory with a pairs folder is `Datasets/akshardrishti_official/Nepali/Images and Transcriptions/` — 386 files (193 jpeg + 193 xml + 178 jpg variants). **0 usable image+transcription pairs**: all 193 XMLs are Pascal-VOC bbox annotations with no transcription text (0/193 carry `<Unicode>`; 0 `.txt` files exist anywhere in the Nepali tree — measured command: grep for `<Unicode>` across all 193 XMLs → 0). bn/hi/sa gold pairs use `.txt` transcription siblings; Nepali has none.

## 4. Re-source options per short language (within the gates only)

| lang | (a) remaining clean cands | (b) unused official pairs | (c) fallback | post-re-source n (max) |
|---|---|---|---|---|
| as | **+11** (1 PDF — clustered) | 0 | accept caveat | 30 |
| mni | 0 | 0 | accept low-n with permanent caveat | 20 |
| sat | 0 | 0 | accept low-n with permanent caveat | 20 |
| gu | **+6** (1 PDF — clustered) | 0 | accept caveat | 30 |
| doi | 0 | 0 | accept low-n with permanent caveat | 27 |
| ne | 0 (PDF-tier BARRED, R5) | **0 — pairs carry no transcription text** | accept low-n with permanent caveat | 37 |
| brx | 0 | 0 | accept low-n with permanent caveat | 67 |
| or | 0 | 0 | accept low-n with permanent caveat | 69 |

**Total closable within the gates: +17 items** → 1,700/2,200. The 517-item deficit is structural (mojibake fonts, no text layer, no transcribed source) and cannot be closed from the official PDFs or pairs without lowering the gates (forbidden) or new sources (download — forbidden).

## 5. Stratified re-draw proposals (kok, pa, ur, ks) — PROPOSALS ONLY, boss decision U5

| lang | strict 30%-cap re-draw replaces | achievable rebalance replaces | page≤1 excluded | candidate pool | caveat |
|---|---|---|---|---|---|
| kok | 80 | **0** (already 50/50; floor 50/doc) | 0 | 332 clean pages, 2 PDFs | 2 PDFs only — strict cap unachievable; balance already met |
| pa | 31 | **41** (90/10 → 50/50) | 1 | 7,462 clean pages, 2 PDFs | 2 PDFs only — rebalance possible, diversity not |
| ur | 34 | **34** (page≤1 items, max doc share 3%) | 34 | 335 clean pages, 38 PDFs | fully achievable within gates |
| ks | 15 | **21** (rebalance to 10/doc floor + 15 page≤1) | 15 | 198 clean pages, 10 PDFs | fully achievable within gates |

Executing any re-draw or candidate draw changes the LOCKED manifest (`level2/unified/manifest_22.json` + downstream `manifest.json`) — **boss decision U5**.

## 6. What this plan does NOT do

No downloads · no gate relaxation · no training · no Sarvam calls (cap reached, A8) · no writes to sealed dirs · no edits to `AGENT_PROTOCOL.md`, `manifest.json`, `sheet.csv`, `run_probe.py`, `src/` · does not execute the re-draw · does not write SAMPLING_PLAN.md (lead composes).

## 7. Verdict check

- brx and ur variance rows recomputed with an independent code path — identical (brx: 67 n, 6 PDFs + fill, 47 pages, page≤1 = 5; ur: 100 n, 38 docs, 100 pages, page≤1 = 34).
- Every "remaining candidates" number re-confirmed from the JSONs by (pdf,page) matching: as 11/0 → 11, gu 10/4 → 6, doi 7/7 → 0, ne 17/17 → 0, brx 47/47 → 0, or 50/50 → 0.
- No locked file changed (git status checked; `level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`, `Datasets/akshardrishti_official/`, `manifest_22.json` read-only).
