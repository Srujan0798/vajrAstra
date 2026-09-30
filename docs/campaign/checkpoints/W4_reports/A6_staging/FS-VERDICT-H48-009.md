<!-- RECOVERED 2026-09-30 from db part prt_0eabfab2600194r2nAq2rKWRrW (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #9 — LEADERBOARD.md "19/18 langs" Labeling Bug

**File**: `level2/probe22/scores/LEADERBOARD.md`
**Lines**: 15-24 (coverage summary table)
**Status**: READY FOR ENGINE AGENT APPLICATION

---

## Issue
LEADERBOARD.md coverage summary table shows **"19/18"** for multiple engines:
- doctr: "19/18"
- indicphotoocr: "19/18"  
- openbharatocr: "19/18"
- tesseract_bilingual: "19/18"
- tesseract_indic: "19/18"

## Reality
- Probe has **18 languages** + 1 EN sanity column = 19 total columns
- But the 18 probe languages + EN sanity = 19 total, not "19/18"
- The "19/18" is a labeling bug: should be "18/18" for probe languages, with EN sanity as separate column

---

## Required Change
**Replace all "19/18" with "18/18" in coverage table (lines 14-24):**

| Engine | Current | Corrected |
|--------|---------|-----------|
| doctr | 19/18 | 18/18 |
| indicphotoocr | 19/18 | 18/18 |
| openbharatocr | 19/18 | 18/18 |
| tesseract_bilingual | 19/18 | 18/18 |
| tesseract_indic | 19/18 | 18/18 |

**Note**: Keep the total packs correct (e.g., doctr 1257, indicphotoocr 1257, etc.)

---

## Evidence
- Probe manifest: 18 languages exactly
- EN sanity is separate manifest (`en_sanity/manifest.json`, 30 items)
- LEADERBOARD line 26-51 per-lang table correctly shows 18 langs
- Only the coverage summary table has the bug

---

## Owner
**Engine Agent** — owns LEADERBOARD.md artifact

---

## Law
§9 evidence law: labels must be accurate. "19/18" misrepresents the probe scope (18 languages, not 19).