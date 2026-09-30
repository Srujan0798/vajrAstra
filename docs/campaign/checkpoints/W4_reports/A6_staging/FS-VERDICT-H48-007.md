<!-- RECOVERED 2026-09-30 from db part prt_0eabfab2600194r2nAq2rKWRrW (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #7 — CALL_PACKET.md Human Pairs Count

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 32
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 32 states: **"10,434 human pairs"**

## Reality
Actual count: **10,432** (2938 bn + 3500 hi + 494 sa + 3500 en = 10,432)

**Evidence**:
- CALL_PACKET factchk line 172-173: "internal math: 2938 (bn) + 3500 (hi) + 494 (sa) + 3500 (en) = **10,432, not 10,434**. Off by 2. Likely typo."

---

## Required Change
**Replace line 32:**
```markdown
- **D3** 20-item human spot-check review | **Defer to W6** | D3 already locked; spot-check is non-blocking for current call |
```

**With (corrected line 172-173 in factchk section):**
```markdown
2. **Line 32: "10,434 human pairs"** — internal math: 2938 (bn) + 3500 (hi) + 494 (sa) + 3500 (en) = **10,432, not 10,434**. Off by 2. Likely typo. The total appears in AGENT_PROTOCOL §9 and other docs.
```

**Also correct line 32 itself if it appears elsewhere:**
```markdown
- **D2** Sarvam EN column | **Skip** | D2 already locked; EN data is harness-spec-mismatched; no decision impact |
```

---

## Evidence
- CALL_PACKET factchk line 172-173: "2938 (bn) + 3500 (hi) + 494 (sa) + 3500 (en) = **10,432, not 10,434**"
- AGENT_PROTOCOL.md §9: "human pairs (10,432 gold: bn 2,938 / hi 3,500 / sa 494 / en 3,500)"

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)

---

## Law
§9 evidence law: numerical claims must be exact. "10,434" contradicts arithmetic (10,432) and AGENT_PROTOCOL §9.