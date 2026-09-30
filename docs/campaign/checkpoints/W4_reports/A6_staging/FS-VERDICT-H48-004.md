<!-- RECOVERED 2026-09-30 from db part prt_0eabfab24001ui2ztFv7aoajD6 (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #4 — CALL_PACKET.md Local Engines Scored Count

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 12
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 12 states: **"6/10 local engines scored"**

## Reality
Per FINAL_VERDICT and LEADERBOARD: **9/9 local engines scored** (all 9 local engines completed)

**Evidence**: 
- LEADERBOARD line 15-24 shows 11 engines total, 10 independent (openbharatocr = tesseract_indic duplicate)
- Local engines (excluding sarvam_vision): 9 engines, ALL scored
- CALL_PACKET factchk line 173 confirms: "9 local engines are scored"

---

## Required Change
**Replace in line 12:**
```markdown
- **Engine**: **ALL 11 ENGINES SCORED**... (6/10 local engines scored)
```

**With:**
```markdown
- **Engine**: **8/11 ENGINES SCORED** (surya RUNNING, easyocr + paddleocr_indic pending)... (9/9 local engines scored)
```

---

## Evidence
- CALL_PACKET factchk line 173: "all 9 local engines are scored"
- LEADERBOARD shows 9 local engines + sarvam_vision = 10 independent
- All 9 local engines have scores in LEADERBOARD

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)

---

## Law
§9 evidence law: counts must be exact. "6/10" is factually incorrect; actual is 9/9 local engines scored.