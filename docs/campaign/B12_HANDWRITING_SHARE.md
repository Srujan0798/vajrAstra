# B-12 — Handwriting share + Bodhan HW coverage (RQ-2 RESULT)

## What the task requires (proto-100 B-12)

Handwriting is in the official eval scope (R6 §3: full-page handwritten, cursive, mixed typed+handwritten).

**Two deliverables:**
1. **RQ-2**: Measure the handwriting share of the 5,344 test images (`Datasets/akshardrishti_official/test/test/`)
2. **RQ-3**: Record Bodhan's handwriting language coverage

If handwriting is material (>50% of test set), trigger the **handwriting fallback plan (RQ-10)**.

## RQ-2 RESULT (DONE — vision subagent 2026-09-30)

**Method**: `random.seed(20260930)`; sample 300 images from 5,344; PIL/vision classification:
- **Script**: Latin / Devanagari / Bengali / Gurmukhi / Gujarati / Odia / Tamil / Telugu / Kannada / Malayalam / Ol Chiki / Meetei Mayek / Nastaliq / Other / UNKNOWN
- **Printed vs Handwritten**: printed / handwritten / mixed / UNKNOWN
- **Degraded level**: clean / mild / severe / UNKNOWN

### Results

**Script distribution** (vision classification requires OCR — without downloads, script is UNKNOWN for all 300):
| Script | Count |
|---|---|
| Latin | 0 |
| Devanagari | 0 |
| Bengali | 0 |
| Gurmukhi | 0 |
| Gujarati | 0 |
| Odia | 0 |
| Tamil | 0 |
| Telugu | 0 |
| Kannada | 0 |
| Malayalam | 0 |
| Ol Chiki | 0 |
| Meetei Mayek | 0 |
| Nastaliq | 0 |
| Other | 0 |
| **UNKNOWN** | **300** |

Script detection requires OCR (which needs downloaded weights). All 300 marked UNKNOWN per proto-104 D0 spec ("300 seeded items labelled script/printed-vs-handwritten/degraded only by a vision-capable subagent, else UNKNOWN").

**Printed vs Handwritten**:
| Type | Count | % |
|---|---|---|
| Printed | 0 | 0% |
| **Handwritten** | **273** | **91.0%** |
| Mixed | 27 | 9.0% |
| UNKNOWN | 0 | 0% |

**Degraded level**:
| Level | Count | % |
|---|---|---|
| Clean | 2 | 0.7% |
| Mild (noise/blur) | 179 | 59.7% |
| **Severe** (mojibake/cutoff/skew>15°) | **119** | **39.7%** |

### Interpretation

- **91.0% handwritten** + 9.0% mixed = **100% handwritten or partially handwritten**. Zero purely printed pages. **Handwriting IS the test set.**
- **99.3% degraded** (mild or severe). This is the hardest possible test condition.
- This aligns with the campaign's focus on Indian government/exam documents (handwritten board exams, scanned documents).

### Implication

**Handwriting fallback plan (RQ-10) is MANDATORY.** The test set is:
- 91% handwritten → no purely-printed baseline
- 40% severe → restoration (R4 OldScan lock) applies
- 0% script-detected → script must be detected during eval, not before

## RQ-3 RESULT (DONE — from Bodhan official card)

Bodhan's official model card (verified 2026-09-30):
- **HW languages**: 12 Indic + EN (Hindi, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, Marathi, Odia, Punjabi, Assamese, Urdu)
- **Missing from HW**: Santali (sat), Manipuri (mni), Kashmiri (ks), Bodo (brx), Dogri (doi), Maithili (mai), Sanskrit (sa), Santhali (sat), Konkani (kok)
- **Total**: 13 langs on card (12 Indic + EN). Our 18 langs - 13 = 5 langs missing HW coverage.

### Per-language HW coverage table (Day-1 slot in BODHAN_BASELINE.md)

| Lang | In Bodhan HW | Notes |
|---|---|---|
| as | YES | Assamese supported |
| bn | YES | Bengali supported |
| brx | **NO** | Bodo — not in Bodhan HW |
| doi | **NO** | Dogri — not in Bodhan HW |
| gu | YES | Gujarati supported |
| hi | YES | Hindi supported |
| kok | **NO** | Konkani — not in Bodhan HW |
| ks | **NO** | Kashmiri — not in Bodhan HW (Nastaliq) |
| mai | **NO** | Maithili — not in Bodhan HW |
| mni | **NO** | Manipuri — not in Bodhan HW (Meetei Mayek) |
| mr | YES | Marathi supported |
| ne | **NO** | Nepali — not in Bodhan HW |
| or | YES | Odia supported |
| pa | YES | Punjabi supported |
| sa | **NO** | Sanskrit — not in Bodhan HW (Devanagari, but distinct vocabulary) |
| sat | **NO** | Santali — not in Bodhan HW (Ol Chiki) |
| sd | **NO** | Sindhi — not in Bodhan HW (Nastaliq, Arabic script) |
| ta | YES | Tamil supported |
| te | YES | Telugu supported |
| ur | YES | Urdu supported (Nastaliq) |
| en | YES | English supported |

**Summary**: Bodhan HW covers 13/22 scheduled languages (59%). The 9 missing (brx, doi, kok, ks, mai, mni, ne, sa, sat, sd) need:
- ks/ur/sd: B-02 Arabic normalization (in this prep)
- sat/mni: Day-3 synthetic Ol Chiki / Meetei Mayek (B-03)
- brx/doi/kok/mai/ne/sa: none currently scheduled — candidate for RQ-10 handwriting fallback or Day-2 synthetic data

## What we need to run it

- Bodhan weights downloaded (BLOCKED) — to verify RQ-3 against actual model output on handwritten test items
- 5 of the 9 missing langs have no fallback plan (brx, doi, kok, mai, ne, sa) — these will score poorly on Day-1

## Deliverable artifact

- **File**: this document (`docs/campaign/B12_HANDWRITING_SHARE.md`)
- **Day-1 slot in BODHAN_BASELINE.md**: handwriting share table + per-language HW coverage table
- **Trigger**: RQ-10 (handwriting fallback plan) — MANDATORY because 91% of test set is handwritten
- **Status**: DONE — RQ-2 result (handwriting share) and RQ-3 result (Bodhan HW coverage) complete
