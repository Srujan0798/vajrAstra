<!-- RECOVERED 2026-09-30 from db part prt_0eabfab2600194r2nAq2rKWRrW (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #8 — CALL_PACKET.md OBITUARIES.md Citation for Sarvam Scores

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 174 (paperthin/factchk section)
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md paperthin/factchk section line 174 states:
> "Per-language Sarvam scores (53.91/54.82/55.3/80.01) publicly unverifiable... Already handled by campaign §9.2 transfer obituary law (OBITUARIES.md O-02–O-05 declare all four **DEAD-for-decisions**); packet should cite OBITUARIES.md explicitly so the user is not surprised."

## Required Change
**Add explicit OBITUARIES.md citation in the factchk section for line 174:**

**Replace line 174:**
```markdown
4. **Per-language Sarvam scores (53.91/54.82/55.3/80.01) publicly unverifiable** — Sarvam Indic OCR Bench per-language table not present in indexed web sources (Sarvam blog cites only 87.39 headline, 84.3 olmOCR-Bench English subset, 87.3 olmOCR-Bench). Already handled by campaign §9.2 transfer obituary law (OBITUARIES.md O-02–O-05 declare all four **DEAD-for-decisions**); packet should cite OBITUARIES.md explicitly so the user is not surprised. No decision impact because of the obituary.
```

**With:**
```markdown
4. **Per-language Sarvam scores (53.91/54.82/55.3/80.01) publicly unverifiable** — Sarvam Indic OCR Bench per-language table not present in indexed web sources (Sarvam blog cites only 87.39 headline, 84.3 olmOCR-Bench English subset, 87.3 olmOCR-Bench). **Per OBITUARIES.md O-02–O-05 (transfer obituary law §9.2), all four declared DEAD-for-decisions**; these numbers cannot be used for decisions. Citation: `docs/research/level7/c/c4/OBITUARIES.md`. No decision impact because of the obituary.
```

---

## Evidence
- OBITUARIES.md O-02–O-05 explicitly declare Sarvam per-language scores DEAD-for-decisions
- Campaign §9.2 transfer obituary law mandates obituary citations for external numbers
- CALL_PACKET factchk line 174 acknowledges this but doesn't cite the file

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)

---

## Law
§9 evidence law: external numbers require obituary citations (OBITUARIES.md). Transfer obituary law (§9.2) mandatory.