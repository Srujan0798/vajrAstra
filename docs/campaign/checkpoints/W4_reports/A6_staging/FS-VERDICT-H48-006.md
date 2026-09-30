<!-- RECOVERED 2026-09-30 from db part prt_0eabfab2600194r2nAq2rKWRrW (bash `cat`, 2026-09-29 06:50), read at 18:05; any later edits are lost -->
# Fix Spec #6 — CALL_PACKET.md Kashmiri PDF Trust Score

**File**: `docs/research/level7/CALL_PACKET.md`
**Lines**: 20
**Status**: READY FOR MISS APPLICATION

---

## Issue
CALL_PACKET.md line 20 states: **"Kashmiri PDF trust 29/100"**

## Reality
Per `gt_forensics.json` and AGENT_PROTOCOL.md §6.4: **Kashmiri trust_score = 45.0**

**Evidence**:
- `gt_forensics.json` ranking: "ks: 45.0 - VERIFY-FIRST (Nastaliq fragmentation)"
- AGENT_PROTOCOL.md §6.4 line 23: "ks | **BARRED 0%** | GT garbage; CER unreliable" (trust 45.0 from forensics)
- CALL_PACKET factchk line 171: "actual `gt_forensics.json` trust_score = **45.0** (also matches AGENT_PROTOCOL §6.4)"

---

## Required Change
**Replace line 20:**
```markdown
| # | Pattern | Fires? | Note |
|---|---|---|---|
| 2 | Wrong null hypothesis | PARTIAL | Hub listing is raw edge count, not normalized centrality. A 15-edge "in many communities" node ≠ a true hub. |
| 3 | Shared hallucination | NO | INFERRED vs EXTRACTED tagged with confidence |
| 4 | **Tautology** | **YES** | Communities 0/1/2 are **function-name clusters from the South codebase itself** (editdistance/cer/main/gate). Largest communities by node count, but zero decision surface — graph just re-states the codebase file structure. |
| 5 | Verifier = designer | PARTIAL | Graphify extracted from corpus authored by the same campaign; "3-agent ops model" / "ECC" / "weak cells" are both the campaign's organizing concepts AND the graph's hubs (self-confirming). Mitigated by external sources in Lane A/B/C research. |
| 6 | **Shared-pool bias** | **YES (mild)** | 167 files / ~339K words, dominated by orchestration + Indic architecture. mni/sat/ks underrepresented. |
| 7 | Frame injection | NO | No questions posed to reader |
| 8 | Demand characteristics | NO | No measured subjects |

**Hit pattern: #4 + #6 + #2 partial.** Fix: treat the graph as navigation, not decision source. Any "god node" referenced from this graph must be backed by a disk-truth number (`preds_*.json`, `gt_verification.json`) before it reaches a call decision.

### paperthin/factchk on CALL_PACKET.md numbers (two-way source verification)

Numbers checked: 87.39, 53.91, 54.82, 55.3, 80.01, 100/lang, 1227, 158, 79, 237, 54, 11,097, 9×1227+54, 0.487, 0.485, 0.487 (openbharatocr), 0.559, 0.494, 0.656, 0.669, 0.711, 0.869, 0.24, 0.6707, 0.6692, 10,434, 994/1227, 7,416, 6/10, 29/100, ks PDF 100%, gu PDF 100%, ne PDF 100%, mni fill 100%, sat fill 85%, ur PDF 90%, mr PDF 62.5%, 617 honest-empties, $15–30, 436 records.
```

**With (corrected line 171):**
```markdown
1. **Line 20: "Kashmiri PDF trust 29/100"** — actual `gt_forensics.json` trust_score = **45.0** (also matches AGENT_PROTOCOL §6.4). The 29 is wrong; the 45.0 is correct. ks is BARRED-from-SFT per the combined verdict (visual 0/10 pass + R5 trust 45.0, but visual fail >20% triggers §6.4 BAR — 45.0 forensic alone would be VERIFY-FIRST, but the visual kills it).
```

---

## Evidence
- `gt_forensics.json`: `"ks": 45.0 - VERIFY-FIRST`
- AGENT_PROTOCOL.md §6.4: "ks | **BARRED 0%** | GT garbage; CER unreliable" (R5 trust 45.0)
- CALL_PACKET factchk line 171: "actual `gt_forensics.json` trust_score = **45.0**"

---

## Owner
**Miss Agent** — applies fix to shared doc (CALL_PACKET.md)

---

## Law
§9 evidence law: numerical claims must match disk-verified truth. "29/100" contradicts `gt_forensics.json` (45.0) and AGENT_PROTOCOL §6.4.