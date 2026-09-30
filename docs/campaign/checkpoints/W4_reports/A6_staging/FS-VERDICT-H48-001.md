<!-- RECOVERED 2026-09-30 from db part prt_0eabf872e0013CEHhoqgGw2fTu (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #1 — CALL_PACKET.md Engine Completion Status

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 12-13
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 12 states: **"ALL 11 ENGINES SCORED"**

## Reality
Per FINAL_VERDICT_2026-09-27.md line 120: **8/11 engines scored**, surya RUNNING, easyocr + paddleocr_indic pending.

**Evidence**: FINAL_VERDICT line 120: "Engine Execution: 8/11 done, surya RUNNING (PID 15941, started 18:10 IST)... easyocr + paddleocr_indic pending"

---

## Required Change
**Replace lines 12-13:**
```markdown
- **Engine**: **ALL 11 ENGINES SCORED**. Final report at `level2/probe22/FINAL_REPORT.md` (13KB, written 20:31).
```

**With:**
```markdown
- **Engine**: **8/11 ENGINES SCORED** (surya RUNNING, easyocr + paddleocr_indic pending). Final report at `level2/probe22/FINAL_REPORT.md` (13KB, written 20:31).
```

---

## Evidence
- FINAL_VERDICT_2026-09-27.md line 120: "Engine Execution: 8/11 done, surya RUNNING (PID 15941, started 18:10 IST)... easyocr + paddleocr_indic pending"
- LEADERBOARD.md line 22: surya "1227/1227 + 30 EN = 1257" but surya completed AFTER CALL_PACKET assembly
- CALL_PACKET factchk confirms stale status

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)
**Verdict** — specifies fix, verifies after application

---

## Law
§9 evidence law: every claim must be disk-verified. "ALL 11 ENGINES SCORED" is false per FINAL_VERDICT disk truth.