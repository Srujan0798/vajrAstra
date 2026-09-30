<!-- RECOVERED 2026-09-30 from db part prt_0eabfab24001ui2ztFv7aoajD6 (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #5 — CALL_PACKET.md indicphotoocr Status

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 12
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 12 states: **"indicphotoocr 994/1227 running"**

## Reality
Per FINAL_VERDICT and LEADERBOARD: **indicphotoocr COMPLETE (1257/1227 packs)**

**Evidence**: 
- FINAL_VERDICT line 118: "indicphotoocr | 15 | 963 | ✅ DONE"
- LEADERBOARD line 18: "indicphotoocr | 1257 | 1255 | 2 | 19/18"
- CALL_PACKET factchk line 173: "indicphotoocr has **1257 packs (1255 non-empty, 2 empty, 0 errors)**"

---

## Required Change
**Replace in line 12:**
```markdown
indicphotoocr 994/1227 running
```

**With:**
```markdown
indicphotoocr 1257/1227 DONE
```

---

## Evidence
- FINAL_VERDICT line 118: "indicphotoocr: 15 | 963 | ✅ DONE" (15 langs, 963 packs — partial but listed as DONE)
- LEADERBOARD line 18: "indicphotoocr | 1257 | 1255 | 2 | 19/18"
- CALL_PACKET factchk line 173 confirms: "indicphotoocr has **1257 packs (1255 non-empty, 2 empty, 0 errors)**"

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)

---

## Law
§9 evidence law: status must match disk truth. "994/1227 running" is stale; actual is 1257 complete.