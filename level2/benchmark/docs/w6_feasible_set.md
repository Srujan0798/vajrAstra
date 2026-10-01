# W6 feasible set — three columns per §6.7 + §9 locks

For each of the 18 probe22 languages + 4 South-400 carryover langs, mark as:
- **FEASIBLE NOW**: gold + PDF GT verified, falsification test OK, ≥50 samples, engine CER <0.30 average
- **FEASIBLE IF <missing>**: needs a specific primary evidence to unlock
- **INFEASIBLE UNDER CURRENT RULES**: §6.4 barred, R5 lock, n<50, or engine-only agreement cell

Locked decisions D1–D4 (referenced below):
- **D1**: sarvam_fill GT is NEVER for training (probe-scoring only)
- **D2**: SFT/RLVR against unverified PDF GT is forbidden (§6.4 + §9)
- **D3**: GT<10 char items are purged (already done)
- **D4**: n<50 cells (as, gu, ne, doi, mni, sat) carry no winner claims

---

## Per-language feasible status

| code | lang | n | GT tier mix | status | missing primary |
|---|---|---|---|---|---|
| bn | Bengali | 100 | 100 pair / 0 pdf / 0 fill | **FEASIBLE NOW** | — |
| hi | Hindi | 100 | 100 pair / 0 pdf / 0 fill | **FEASIBLE NOW** | — |
| sa | Sanskrit | 100 | 100 pair / 0 pdf / 0 fill | **FEASIBLE NOW (gold only)** | surya broken; use tesseract_indic / easyocr / sarvam for sa |
| or | Odia | 69 | 0 pair / 50 pdf / 19 fill | **FEASIBLE NOW** (after §6.4 verify-first passes; verification record 91.7% OK) | — |
| pa | Punjabi | 90 | 0 pair / 90 pdf / 0 fill | **FEASIBLE NOW** (after §6.4 verify-first passes; 100% pass) | — |
| brx | Bodo | 67 | 0 pair / 47 pdf / 20 fill | **FEASIBLE IF §6.4 verify-first confirm** (95.8% pass on visual sample; full PDF-tier verify pending) | full §6.4 PDF-tier visual verification |
| kok | Konkani | 100 | 0 pair / 100 pdf / 0 fill | **FEASIBLE IF §6.4 verify-first confirm** (100% pass on visual sample; full PDF-tier verify pending) | full §6.4 PDF-tier visual verification |
| mai | Maithili | 100 | 0 pair / 100 pdf / 0 fill | **FEASIBLE IF §6.4 verify-first confirm** (90.0% pass on visual sample) | full §6.4 PDF-tier visual verification |
| gu | Gujarati | 24 | 0 pair / 4 pdf / 20 fill | **FEASIBLE IF (n=24 boost to n>=50) + §6.4 verify-first confirm** (85.7% visual sample) | either: draw more gu PDF items from upstream pool (gates previously rejected 3,567 layers; cannot re-draw without unlocking gates per §1) OR remove n<50 status |
| sd | Sindhi | 75 | 0 pair / 75 pdf / 0 fill | **FEASIBLE IF §6.4 verify-first confirm** (85.7% visual sample) | full §6.4 PDF-tier visual verification |
| as | Assamese | 19 | 0 pair / 0 pdf / 19 fill | **INFEASIBLE UNDER CURRENT RULES** | n<50 (D4) + 100% fill (D1); cannot satisfy both even with more draw because upstream as PDF layers were control-char corrupt (§1) |
| mni | Manipuri | 20 | 0 pair / 0 pdf / 20 fill | **INFEASIBLE UNDER CURRENT RULES** | n<50 (D4) + 100% fill (D1) + 0% §6.4 pass (BARRED per §6.4) |
| sat | Santali | 20 | 0 pair / 0 pdf / 20 fill | **INFEASIBLE UNDER CURRENT RULES** | n<50 (D4) + 100% fill (D1) + 15% §6.4 pass (BARRED per §6.4); Ol Chiki layers from upstream are broken |
| ne | Nepali | 37 | 0 pair / 17 pdf / 20 fill | **INFEASIBLE UNDER CURRENT RULES** (PDF-tier); FEASIBLE IF (R5 lock override + n>=50 boost) | R5 lock (trust 26.6, 32 control chars) — locked 2026-09-26, cannot override; n<50 also (D4) |
| mr | Marathi | 79 | 0 pair / 79 pdf / 0 fill | **INFEASIBLE UNDER CURRENT RULES** (PDF-tier) | §6.4 BARRED (42.9% pass); cannot use mr PDF-tier GT for SFT/RLVR |
| ks | Kashmiri | 100 | 0 pair / 100 pdf / 0 fill | **INFEASIBLE UNDER CURRENT RULES** (PDF-tier) | §6.4 BARRED (0% pass); Nastaliq fragmentation + pipe/danda issues |
| ur | Urdu | 100 | 0 pair / 100 pdf / 0 fill | **INFEASIBLE UNDER CURRENT RULES** (PDF-tier) | §6.4 BARRED (10% pass); Syriac contamination |
| doi | Dogri | 27 | 0 pair / 7 pdf / 20 fill | **INFEASIBLE UNDER CURRENT RULES** | n<50 (D4); 100% visual-sample §6.4 pass but cell too small to rank |

### South-400 carryover languages (probe18 baseline)

| code | lang | status | notes |
|---|---|---|---|
| te | Telugu | **FEASIBLE NOW** (from South-400 baseline; not re-probed at n=100 here) | South-400 result: 0.06 CER (tesseract_indic te pack) |
| ta | Tamil | **FEASIBLE NOW** | South-400 baseline, 0.05 CER |
| kn | Kannada | **FEASIBLE NOW** | South-400 baseline |
| ml | Malayalam | **FEASIBLE IF no ml corruption purge resolved** | 1 corrupt PDF purged per §1; baseline South-400 result |

---

## Per-status totals

| status | langs | usable packs (SFT/RLVR) |
|---|---|---|
| FEASIBLE NOW | bn 100, hi 100, sa 100 (gold only), or 69, pa 90, te/ta/kn/ml baseline) | 459 + baseline carryover |
| FEASIBLE IF §6.4 verify-first | brx 67, kok 100, mai 100, sd 75 | 342 (gated on visual verification) |
| FEASIBLE IF (n boost + verify) | gu 24 | 24 (or 0 if no nboost possible) |
| INFEASIBLE | as 19, mni 20, sat 20, ne 37, mr 79, ks 100, ur 100, doi 27 | 0 (gated) |
| **TOTAL probe22** | **1,227** | **FEASIBLE 459–801 (37–65%)** |

---

## W6 training set construction (per §9)

For **SFT (synthetic-render + gold-pair + verified-PDF)**:
- 459 items unconditionally available (bn, hi, sa, or, pa, te, ta, kn, ml) — plus all sarvam-bench synthetic renders
- + up to 342 items conditionally available (brx, kok, mai, sd) after §6.4 visual verification confirms PDF-tier GT quality
- + up to 24 items for gu IF additional clean gu PDF layers can be sourced (per §1, gates previously rejected all 3,567; cannot re-draw without unlocking gates)

For **RLVR (gold-verified GT only)**:
- 300 items (bn 100 + hi 100 + sa 100 pairs)
- + any §6.4-verified langs (brx/kok/mai/sd after verify)
- **NEVER on PDF-tier or sarvam-fill** per D1 + D2

For **abstention training (silence = fail)**:
- 1,227 items, every language. CER 1.0 is the correct label for empty predictions. This is the entire probe22 regardless of GT quality.

---

## Hard guards (re-confirmed from §9, do not relax)

- **D1**: sarvam_fill GT NEVER for training
- **D2**: SFT/RLVR against unverified PDF GT forbidden
- **D3**: GT<10 char items purged (already done)
- **D4**: n<50 cells no winner claims (as, gu, ne, doi, mni, sat)
- **D5 (implicit)**: §6.6 ablation must show no rank inversion before RLVR (PASS — max delta = 0.5pp, 0 inversions)
- **D6 (implicit)**: Akshara-boundary aux loss scoped to Indic-abugida only (Devanagari + Bengali-Assamese family); NOT for ur/ks/sd (Perso-Arabic), sat (Ol Chiki), mni (Meitei Mayek)
- **D7 (implicit)**: §6.4 visual verification must be machine-confirmed by verdict agent; 20-item human spot-check by user pending

Generated 2026-09-28 20:31 IST by Engine Agent. Locked decisions D1–D4 as defined in `OCR_AGENT_MEMORY_FEED.md §9`.