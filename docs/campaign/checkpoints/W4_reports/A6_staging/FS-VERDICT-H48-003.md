<!-- RECOVERED 2026-09-30 from db part prt_0eabfab24001ui2ztFv7aoajD6 (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #3 — CALL_PACKET.md paddleocr_indic Queue Status

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 24
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 24 states: **"paddleocr_indic | 1227 | 0.6562 | DONE"**

## Reality
Per FINAL_VERDICT_2026-09-27.md line 122: **paddleocr_indic NOT IN QUEUE** — "Engineer must schedule manually"

**Evidence**: FINAL_VERDICT line 122: "**paddleocr_indic** | — | — | ⏳ **NOT IN QUEUE — Engineer must schedule manually**"

---

## Required Change
**Replace line 24:**
```markdown
| paddleocr_indic | 1227 | 0.6562 | DONE |
```

**With:**
```markdown
| paddleocr_indic | — | — | ⏳ NOT IN QUEUE — Engine must schedule manually after easyocr |
```

---

## Evidence
- FINAL_VERDICT_2026-09-27.md line 122: "paddleocr_indic — NOT IN QUEUE — Engineer must schedule manually"
- Engine queue: surya → easyocr → paddleocr_indic (sequential per §5)
- Engine Agent must manually schedule paddleocr_indic after easyocr completes

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)
**Verdict** — specifies fix, verifies after application

---

## Law
§9 evidence law: engine queue status must match disk truth. "DONE" is false when engine is not even in queue.