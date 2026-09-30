# SAMPLING_PLAN — Wave 2 (D04) · 2026-09-30

**Lead:** orchestrator (composes from subagent reports) · **Method:** CAMPAIGN_DIRECTIVE v5 Part F Wave 2 + protocols proto-20/21
**Reproduces from:** `level2/unified/reconcile_22.py` + `level2/unified/variance_22.py` (run either — both print their numbers) · `docs/campaign/checkpoints/W2_reports/variance.md`
**Supersedes:** `SAMPLE_PLAN_18_LANGS.md` (stale at 1,227). Every claim carries a file/command. No fake claims. Gates NEVER lowered (extract_gt.py:66-69; AGENT_PROTOCOL forbids relaxing).

---

## 1. Summary (≤10 lines)

1. Labelled **1,683 / 2,200** (22 languages: 1,283 probe22 + 400 South); deficit **517**, all in 8 short languages (as 19 · mni 20 · sat 20 · gu 24 · doi 27 · ne 37 · brx 67 · or 69).
2. **Pair tier (bn/hi/sa): the three forbidden shortcuts are all DISPROVEN** — 100 distinct images each, top-1 document share 1%, ids spread pool-wide (bn 32→3088, hi 18→3461, sa 22→506; seeded shuffle SEED 20260926).
3. **First-page-only bias CONFIRMED**: ur 34/100 (34%), doi 6/7 (86%); PARTIAL: ks 15%, mai/mr/pa/brx/or 1–11%; DISPROVEN: gu/kok/ne/sd (0%).
4. **Clustered CONFIRMED**: as/kn/ml/ta/te + mni/sat (single source), doi 74%, gu 83%, ne 54%, or 72%, pa 90%; kok exactly 50/50 = PARTIAL (structural: 2 PDFs, cannot improve without a re-draw).
5. **Single-source CONFIRMED**: fill tier (as, mni, sat + parts of 5 others) = sarvam_bench; **South = S5_govt 100/100 in all 4 languages** (new measured fact).
6. **Closable within the gates: +17 items** (as +11, gu +6). mni/sat/doi/ne/brx/or have **0 remaining** clean candidates — structural, not ceremony-gated.
7. **Official image+transcription pairs: 0 usable** — Nepali's 193 pairs carry NO transcription text (0/193 XMLs with `<Unicode>`, 0 `.txt` files) → option (b) is dead for every short language.
8. Why short: the honesty gates reject the PDF text layers (mojibake legacy fonts, short/Latin) — gu 3,486/3,567 pages rejected; mni 1,353/1,353 rejected; sat has NO text layer (0/207).
9. **Scoring covers 1,227 of 1,283** — the 56 un-scored items are mr 21, pa 10, sd 25 (they are a SUBSET of the manifest, not additions — see §2).
10. Re-draw proposals are **U5 only** (executing changes the locked manifest): pa 41, ur 34, ks 21 — all proposals, none executed tonight.

---

## 2. Reconciliation (18 probe languages — `reconcile_22.py` output)

| lang | man | scored | tiers |
|---|---|---|---|
| as | 19 | 19 | sarvam_bench 19 |
| bn | 100 | 100 | official_pair_txt 100 |
| brx | 67 | 67 | official_pdf_layer 47, sarvam_bench 20 |
| doi | 27 | 27 | official_pdf_layer 7, sarvam_bench 20 |
| gu | 24 | 24 | official_pdf_layer 4, sarvam_bench 20 |
| hi | 100 | 100 | official_pair_txt 100 |
| kok | 100 | 100 | official_pdf_layer 100 |
| ks | 100 | 100 | official_pdf_layer 100 |
| mai | 100 | 100 | official_pdf_layer 100 |
| mni | 20 | 20 | sarvam_bench 20 |
| mr | 100 | 79 | official_pdf_layer 100 |
| ne | 37 | 37 | official_pdf_layer 17, sarvam_bench 20 |
| or | 69 | 69 | official_pdf_layer 50, sarvam_bench 19 |
| pa | 100 | 90 | official_pdf_layer 100 |
| sa | 100 | 100 | official_pair_txt 100 |
| sat | 20 | 20 | sarvam_bench 20 |
| sd | 100 | 75 | official_pdf_layer 100 |
| ur | 100 | 100 | official_pdf_layer 100 |

**Checks (all PASS):** n_total == 1,283 probe + 400 South = 1,683 · every uid unique (1,683/1,683) · every image_path exists (0 missing) · local engines agree on scored n per language.

**STRUCTURAL CORRECTION (new fact, changes the "56 additions" framing):** `manifest_additions.json` is a **SUBSET** of `level2/probe22/manifest.json` (set arithmetic on image_ids — NOT on `manifest_22.json`, whose keys are `uid`), equal to the **56 manifest items that are NOT scored** (mr 21, pa 10, sd 25). `len(manifest) + len(additions) = 1,339` is WRONG; the true total is 1,283 scored + un-scored inside one manifest. Every doc that says "1,283 = 1,227 + 56 additions" must say "1,283 items, of which 1,227 scored; the 56 un-scored are listed in manifest_additions.json" — the items were never added to the manifest, only left un-scored.

**Engine coverage of the 56 un-scored:** all 10 local engines have 21/21 (mr), 10/10 (pa), 25/25 (sd) outputs on disk — EXCEPT **surya 12/25 on sd** and **sarvam_vision 0/56** (cap spent). The outputs exist; scoring them (writing them into the LOCKED `sheet.csv`) is **U5**.

**Orphan outputs explained:** rapidocr holds files for ids NOT in the manifest — as 12, gu 6, mr 21, ne 29, or 10, pa 10, sd 25 (= the un-scored items + pre-purge orphans, protocol §5 documented behavior); en 303 (EN sanity 30×10 + 3 sarvam).

**South 400:** labelled 100/100/100/100 (ta/te/kn/ml); **scored: ta 70, te 26, kn 25, ml 5 = 126 of 400** (nulls: gt_thin 24/49/55/91, legacy_mojibake_layer 6/25/20/4; `CER_STAGE3B.json`); all 10 engines have 100/100 outputs per lang. By lang-tag: kn 25 and ml 5 are at or below the lead's 5–10 floor at the scored level; the v5 Part A5 "Tamil 53, Telugu 6, Kannada 4, Malayalam 4" figures are the by-dominant-SCRIPT basis, not the by-language basis — both are true of different groupings and must not be mixed.

---

## 3. Variance table + shortcut verdicts (22 languages — `variance_22.py` output)

| flag | languages |
|---|---|
| **clustered (top-1 share >50%)** | as, kn, ml, ta, te, mni, sat (100% single-source), doi 74%, gu 83%, ne 54%, or 72%, **pa 90%** |
| **first-page bias (page≤1 share >20%)** | **ur 34%**, **doi 86%** |
| **clean pair tier** | bn, hi, sa — top-1 1%, 100 distinct docs |
| kok | 50/50 across 2 PDFs — PARTIAL (structural floor) |

**Verdict per language on the three forbidden shortcuts (CO-022/023/024):**

| Shortcut | Verdict | Evidence |
|---|---|---|
| (a) First-page-only | **CONFIRMED for ur (34%), doi (86%)**; PARTIAL: ks 15%, mai/mr/pa/brx/or 1–11%; DISPROVEN: gu/kok/ne/sd (0%) | `variance_22.py` page-offset distribution |
| (b) One-paper-per-file | **CONFIRMED for fill tier (sarvam_bench single source)** and South (S5_govt 100/100); kok/pa 2 PDFs each = PARTIAL; DISPROVEN for pair tier + ur (38 PDFs) | manifest `source_pdf` |
| (c) Clustered/unrepresentative | **CONFIRMED for as/kn/ml/ta/te/mni/sat/doi/gu/ne/or/pa** (top-1 >50%); kok PARTIAL (exactly 50/50) | `variance_22.py` top-1 share |

CO-023/024 are **DISPROVEN for the pair tier** (bn/hi/sa): 100 distinct images, spread pool-wide, seeded shuffle.

---

## 4. Candidate pools (8 short languages — `candidates/<code>.json`)

| lang | n (labelled) | PDFs | pages scanned | pages w/ text | rej mojibake/wrong | rej short/Latin | clean candidates | drawn into manifest | **remaining** | why short |
|---|---|---|---|---|---|---|---|---|---|---|
| as | 19 | 40 | 4,241 | 2,504 | 898 | 1,600 | 11 | 0 | **+11** | fill tier single-source; clean candidates remain undrawn |
| gu | 24 | 220 | 13,406 | 3,567 | 3,486 | 71 | 10 | 4 | **+6** | legacy font encodings; pages cannot fix it |
| mni | 20 | 10 | 1,358 | 1,353 | 689 | 664 | 0 | — | **0** | no text layer survives the gates |
| sat | 20 | 3 | 207 | 0 | 0 | 0 | 0 | — | **0** | NO text layer at all |
| doi | 27 | 6 | 446 | 11 | 1 | 3 | 7 | 7 | **0** | tiny pool, fully drawn |
| ne | 37 | 30 | 4,146 | 464 | 411 | 36 | 17 | 17 | **0** | small pool, fully drawn |
| brx | 67 | 32 | 3,349 | 2,428 | 886 | 1,495 | 47 | 47 | **0** | pool fully drawn |
| or | 69 | 27 | 1,767 | 1,625 | 74 | 1,508 | 50 | 50 | **0** | pool fully drawn |

*Column basis: PDFs/pages/rejections from `candidates/<code>.json`; "drawn into manifest" = the `official_pdf_layer` count in `manifest_22.json` (fill-tier items are sarvam_bench, not drawn from candidates). The proto-21:23 "doi 4/8, ne 2/18, brx 48, or 51" figures are the MANIFEST distinct-docs/pages basis — a different grouping; both are true of their own basis and not mixed here.*

**Official image+transcription pairs: 0 usable** for any short language (Nepali 193 pairs carry NO transcription text — option (b) dead).

---

## 5. Re-source plan per language (within the gates ONLY)

| lang | source | method | count | gate status |
|---|---|---|---|---|
| as | remaining clean candidates (`candidates/as.json`) | draw 11, varied pages | +11 → 30 | gates intact; still <100 — permanent caveat |
| gu | remaining clean candidates (`candidates/gu.json`) | draw 6, varied pages | +6 → 30 | gates intact; structural (mojibake fonts) — permanent caveat |
| mni / sat / doi / ne / brx / or | none available | — | +0 | **accept low-n with permanent caveat** |
| kok / pa / ur / ks | stratified re-draw (PROPOSAL → U5) | max share per document, page≤1 excluded | pa 41, ur 34, ks 21 replaced; kok +0 (already 50/50) | **executing changes the locked manifest — U5 only** |

Outside sources (downloads, new datasets): **NOT in this plan** — §9 hard rule, boss approval required separately.

---

## 6. Low-n caveats (exact wording for leaderboards)

- `n=19, fill-tier GT (sarvam_bench), no winner claim (D4)` — as
- `n=20, fill-tier GT, no winner claim (D4)` — mni, sat
- `n=24/24/27/37, pdf_layer GT (4/4/7/17 scored) + fill, no winner claim (D4)` — gu, doi, ne
- `n=67/69, pdf_layer GT (47/50 scored) + fill` — brx, or (winner claim allowed at n≥50 scored)
- South: `labelled 100, scored 70/26/25/5 (gt_thin + legacy_mojibake_layer nulls) — kn/ml at/below the 5–10 floor at the scored level`

---

## 7. What this plan does NOT do

- Does not lower any gate (extract_gt.py:66-69 unchanged; AGENT_PROTOCOL forbids)
- Does not execute any re-draw (U5 only)
- Does not score the 56 un-scored items into the LOCKED `sheet.csv` (U5)
- Does not download anything (§9 hard rule)
- Does not fabricate samples or collect 400-page sets
- Does not touch sealed dirs (`level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`, `Datasets/akshardrishti_official/`)

---

## 8. Decisions for the boss (U5 + new)

| # | Decision | Recommendation |
|---|---|---|
| U5 | Score the 56 un-scored items (mr 21, pa 10, sd 25) into the LOCKED `sheet.csv` and regenerate it; re-draw pa 41 / ur 34 / ks 21 | Yes, after the meeting — the outputs already exist on disk for 9/10 engines; regenerating is the one fix that makes `sheet.csv` a citable evidence artefact (see EDGE_THESIS §4 CONTRADICTION) |
| U6 (new) | Draw as +11 / gu +6 within the gates (updates the manifest — a new `manifest` revision, not the locked file) | Yes, cheap and within the gates; brings as/gu to 30 labelled each |
| U7 (new) | The Ol Chiki / Meetei Mayek traineddata pack (~2–4 MB download) — the only fix for the 2 dead languages | Boss decision (download gate); verify the pack's file listing first (EDGE_THESIS §3 UNRESOLVED) |

Supersedes `SAMPLE_PLAN_18_LANGS.md` (pointer added at its top; file retained per L4).
