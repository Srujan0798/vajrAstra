<!-- RECOVERED 2026-09-30 from db part prt_0eabfab24001ui2ztFv7aoajD6 (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #2 — CALL_PACKET.md Surya Completion Status

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 26
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 26 states: **"surya... DONE 19:33"**

## Reality
Per FINAL_VERDICT_2026-09-27.md line 120: **surya RUNNING** (PID 15941, started 18:10 IST) at time of FINAL_VERDICT writing.

**Evidence**: FINAL_VERDICT line 120: "surya RUNNING (PID 15941, started 18:10 IST, ~3.5h elapsed, will finish before 04:23 Sep 29)"

---

## Required Change
**Replace line 26:**
```markdown
| **surya** | **1227 + 30 EN = 1257** | **0.3849** | **DONE 19:33** ← best non-Sarvam engine |
```

**With:**
```markdown
| **surya** | **1227 + 30 EN = 1257** | **0.3849** | **RUNNING (PID 15941)** ← best non-Sarvam engine; completes before 04:23 Sep 29 |
```

---

## Evidence
- FINAL_VERDICT_2026-09-27.md line 120: "surya RUNNING (PID 15941, started 18:10 IST, ~3.5h elapsed, will finish before 04:23 Sep 29)"
- LEADERBOARD.md line 85-90 confirms surya completed later (auto-restarted at 5:45PM)

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)
**Verdict** — specifies fix, verifies after application

---

## Law
§9 evidence law: engine status must match disk truth. "DONE 19:33" contradicts disk truth at time of CALL_PACKET assembly.