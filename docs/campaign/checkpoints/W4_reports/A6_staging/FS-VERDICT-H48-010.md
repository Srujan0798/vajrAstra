<!-- RECOVERED 2026-09-30 from db part prt_0eabf872e0013CEHhoqgGw2fTu (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #10 — LEADERBOARD.md Add Wilson 95% CI Column

**File**: `level2/probe22/scores/LEADERBOARD.md`
**Status**: READY FOR ENGINE AGENT APPLICATION

---

## Issue
LEADERBOARD.md presents point-estimate CERs without Wilson 95% CIs, violating §6.7 power statement requirement.

## Required Change
**Add Wilson 95% CI column to per-lang CER table (lines 33-51) and overall CER table (lines 55-67).**

### Per-lang CER Table — Add CI Column
**Current (line 33):**
```markdown
| Lang | tesseract_indic | tesseract_bilingual | indicphotoocr | surya | paddleocr_indic | easyocr | sarvam_vision | rapidocr | anuvaad_tesseract | doctr | openbharatocr |
```

**Add after each CER value:** ` (CI: lower–upper)`

**Example for sarvam_vision (n=3/lang):**
- CER = 0.2400, n=3 per lang
- Wilson 95% CI: [0.151, 0.329] (half-width ~0.089)
- Display: `0.001 (n=2) [0.000–0.054]`

**Example for surya (n=1227):**
- CER = 0.3849, n=1227
- Wilson 95% CI: ±0.013 → [0.372, 0.398]

### Overall CER Table — Add CI Column
**Current (line 55):**
```markdown
| Engine | overall CER | overall WER | n_packs | missing | valid |
```

**Add:** `| Wilson 95% CI |`

---

## Wilson 95% CI Formula
For proportion p = CER, n = valid samples:
```
z = 1.96
p̂ = p + z²/(2n)
denom = 1 + z²/n
lower = (p̂ - z * sqrt(p*(1-p)/n + z²/(4n²))) / denom
upper = (p̂ + z * sqrt(p*(1-p)/n + z²/(4n²))) / denom
```

---

## Required Output Format
**Per-lang table:** `CER (n=X) [lower–upper]`
**Overall table:** `CER [lower–upper]`

**Example for sarvam_vision as (n=2):**
`0.001 (n=2) [0.000–0.054]`

**Example for surya overall:**
`0.3849 [0.372–0.398]`

---

## Evidence
- §6.7: "Wilson 95% intervals on every per-language engine CER"
- §6.7: "abstention (empty predictions) is reported as coverage + conditional CER separately"
- Campaign estimator law (campaign §9.3): Wilson 95% intervals mandatory

---

## Owner
**Engine Agent** — owns LEADERBOARD.md artifact

---

## Law
§6.7: "Wilson 95% intervals on every per-language engine CER; paired engine comparisons on the SAME items use McNemar exact, never point-estimate deltas"
§9 evidence law: uncertainty must be quantified, not hidden.