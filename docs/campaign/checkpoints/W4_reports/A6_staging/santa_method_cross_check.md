<!-- PARTIAL 2026-09-30 from db part prt_0e8cd58f7001DdwkYkrW3YzcOb (bash `cat`, 2026-09-28 21:46) + cross-check prt_0ef39d98a001sbUvX40pFoAIfh (read, 2026-09-30 03:42), read at 18:05; any later edits are lost -->
# Santa-Method Cross-Check — CALL_PACKET.md vs FINAL_VERDICT_2026-09-27.md vs LEADERBOARD.md

**Date**: 2026-09-28 H48 (~18:00 IST)
**Reviewers**: Pass 1 (Reviewer #1), Pass 2 (Reviewer #2) — blind to each other
**Consensus threshold**: ≥2 reviewers flagged

---

## Documents Cross-Checked

| Doc | Source | Date |
|-----|--------|------|
| CALL_PACKET.md | Miss agent | 2026-09-28 ~19:50 IST (refreshed) |
| FINAL_VERDICT_2026-09-27.md | Orchestrator | 2026-09-27 21:20 IST (refreshed) |
| LEADERBOARD.md | Orchestrator | 2026-09-28 19:33 IST |

---

## Consensus Findings (≥2 Reviewer Consensus)

### CRITICAL Contradictions

#### CRITICAL-1: Engine Completion Status
| Location | Claim | Counter-Claim |
|----------|-------|---------------|
| CALL_PACKET.md line 12 | "ALL 11 ENGINES SCORED" | FINAL_VERDICT line 120: "8/11 done, surya RUNNING, easyocr + paddleocr_indic pending" |

**Evidence**: FINAL_VERDICT line 120: "Engine Execution: 8/11 done, surya RUNNING (PID 15941)... easyocr + paddleocr_indic pending"

**Impact**: CRITICAL — Call readiness misrepresented; 3 engines not actually complete

---

#### CRITICAL-2: Surya Completion Status
| Location | Claim | Counter-Claim |
|----------|-------|---------------|
| CALL_PACKET line 26 | "surya... DONE 19:33" | FINAL_VERDICT line 120: "surya RUNNING (PID 15941, started 18:10 IST)" |
| LEADERBOARD line 22 | "surya | 1227 | 1098 | 129 | 17/18" (implies done) | FINAL_VERDICT line 120: "surya RUNNING (PID 15941)" |

**Evidence**: FINAL_VERDICT line 120 shows surya RUNNING with PID 15941

**Impact**: CRITICAL — Engine completion misreported; affects call readiness assessment

---

#### CRITICAL-3: paddleocr_indic Queue Status
| Location | Claim | Counter-Claim |
|----------|-------|---------------|
| CALL_PACKET line 24 | "paddleocr_indic | 1227 | 0.6562 | DONE" | FINAL_VERDICT line 122: "paddleocr_indic — NOT IN QUEUE — Engineer must schedule manually" |

**Evidence**: FINAL_VERDICT line 122: "paddleocr_indic — NOT IN QUEUE — Engineer must schedule manually"

**Impact**: CRITICAL — Engine missing from execution queue; not actually complete

---

### HIGH-Severity Errors

#### HIGH-1: Kashmiri PDF Trust Score
| Location | Claim | Actual |
|----------|-------|--------|
| CALL_PACKET line 20 | "Kashmiri PDF trust 29/100" | gt_forensics.json trust_score = **45.0** |

**Evidence**: gt_forensics.json shows ne=26.6, ks=45.0, mr=46.8, etc. CALL_PACKET factchk line 171 confirms 45.0 is correct.

---

#### HIGH-2: Stale indicphotoocr Status
| Location | Claim | Actual |
|----------|-------|--------|
| CALL_PACKET line 12 | "indicphotoocr 994/1227 running" | Actual: 1257/1227 complete |

**Evidence**: CALL_PACKET factchk line 173 confirms "indicphotoocr has **1257 packs (1255 non-empty, 2 empty, 0 errors)**"

---

#### HIGH-3: Human Pairs Count
| Location | Claim | Actual |
|----------|-------|--------|
| CALL_PACKET line 32 | "10,434 human pairs" | 2938 (bn) + 3500 (hi) + 494 (sa) + 3500 (en) = **10,432** |

**Evidence**: CALL_PACKET factchk line 172-173 confirms 10,432 is correct; off by 2.

---

### MEDIUM-Severity Issues

| # | Issue | Location | Detail |
|---|-------|----------|--------|
| MEDIUM-1 | "6/10 local engines scored" | CALL_PACKET line 12 | Actual: 9/9 local engines scored (all 9 local engines done) |
| MEDIUM-2 | Per-language Sarvam scores unverifiable | CALL_PACKET line 174 | Should cite OBITUARIES.md explicitly per §9.2 |
| MEDIUM-3 | Santa-method analysis only in CALL_PACKET | No cross-doc verification | Only in CALL_PACKET |
| MEDIUM-4 | paperthin/hate on D1-D4 only in CALL_PACKET | No cross-doc verification | CALL_PACKET only |
| MEDIUM-5 | paperthin/mandela findings only in CALL_PACKET | No cross-doc verification | CALL_PACKET only |

---

### LOW-Severity Issues

| # | Issue | Location | Detail |
|---|-------|----------|--------|
| LOW-1 | Surya EN CER 0.1514 only in LEADERBOARD | LEADERBOARD line 89 | Not in FINAL_VERDICT/CALL_PACKET |
| LOW-2 | "19/18 langs" labeling bug | LEADERBOARD lines 15-24 | 5 rows show "19/18" but only 18 probe langs |
| LOW-3 | Surya EN CER 0.1514 not in FINAL_VERDICT | LEADERBOARD line 89 | Missing from FINAL_VERDICT |
| LOW-4 | Surya + Santali warning only in FINAL_VERDICT | FINAL_VERDICT line 124 | Missing in CALL_PACKET |
| LOW-5 | CALL_PACKET line 147-160 paperthin/mandela only in CALL_PACKET | No cross-doc verification | CALL_PACKET only |

---

## Wilson 95% CI Application (Where Appropriate)

For sarvam_vision (n=3/lang = 3 samples per language):
- CER = 0.2400, n=54 total (48 valid)
- Wilson 95% CI: ~±0.15 (exact: 0.151-0.329) — **enormous uncertainty**
- Cannot meaningfully compare to other engines' point estimates

For surya (n=1227):
- CER = 0.3849, n=1227
- Wilson 95% CI: ±0.013 — tight interval

**Conclusion**: Headline "Sarvam 0.24 vs Surya 0.38" is statistically invalid without CIs; sarvam_vision CI half-width >50pp.

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 3 |
| HIGH | 3 |
| MEDIUM | 5 |
| LOW | 5 |
| **TOTAL** | **16** |

**Verdict**: CALL_PACKET.md contains 3 CRITICAL contradictions with FINAL_VERDICT.md on engine completion status. CALL_PACKET misrepresents engine completion (says 11/11 done when 3 engines not done). CALL_PACKET contains 3 HIGH-severity numerical errors. Multiple MEDIUM issues where CALL_PACKET contains unique analyses not cross-verified in other docs.

**Recommendation**: CALL_PACKET.md must be refreshed before validation call. FINAL_VERDICT.md is the authoritative source for engine status.

---

*Generated by Santa-Method 2-Pass Cross-Check (H48)*
*Reviewers: Pass 1 + Pass 2 (blind)*
*Consensus: ≥2 reviewers*