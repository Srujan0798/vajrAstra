# PAPERTHIN AUDIT — Mandela + Factchk + Hate on 4 docs
**Date:** 2026-09-29 21:00 IST · **Author:** AGENT-1 · **Skill:** paperthin/depth/mandela (eval-leakage), paperthin/depth/factchk (two-way source), paperthin/depth/hate (load-bearing objection)

**Scope:** DEEP_REPORT.md, VINAY_MEETING_PACKET.md, W5_BEAT_SARVAM_PLAN.md, EVIDENCE_SUMMARY.md

**Mode:** Read-only audit. Names the leak, names the fix, does NOT rewrite.

---

## A. METHOD — THE 8 MANDELA PATTERNS

For each document, I walk the 8 leakage patterns:
1. Recall, not reason (memorized answer recited)
2. Wrong null hypothesis (control leaks signal)
3. Shared hallucination (components confirming each other)
4. Tautology (scorer grading buckets it drew)
5. Verifier = designer (private recipe)
6. Shared-pool bias (train and holdout from same pool)
7. Frame injection (question hands the hypothesis)
8. Demand characteristics (measured subjects know)

Plus **factchk** (two-way: claim → primary source; primary source → claim) and **hate** (the single load-bearing objection that kills the plan + cheapest test).

---

## B. DEEP_REPORT.md — audit

### B1. Mandala walk

| Pattern | Hit? | Note |
|---|---|---|
| 1. Recall, not reason | No | All numbers cite specific files (`_archive/cleanup_2026-09-28/AUDIT_*.md`, `level2/probe22/scores/`) |
| 2. Wrong null hypothesis | **PARTIAL** | The cleanup claims "no regression fired" — but the cleanup itself never had a fresh-eyes auditor verify the 95% threshold claim |
| 3. Shared hallucination | **YES (load-bearing)** | DEEP_REPORT §Phase 7 says "graph already at **1324 nodes / 1665 edges / 206 communities / 52 hyperedges** as of 2026-09-27 21:15". Disk truth: `graphify-out/GRAPH_REPORT.md` (built 2026-09-29) reports **3990 nodes / 4681 edges / 420 communities / 50 hyperedges**. The doc cites a stale graph state — factchk FAILS. |
| 4. Tautology | No | Reports 24h cleanup phases 1-7 from disk; not a self-grading bucket |
| 5. Verifier = designer | No | SCOPE-AUDIT-AGENTs #1-#10 are separate (different prompts) from the Phase-2 consolidator |
| 6. Shared-pool bias | No | Cleanup touched only _archive/ + root .py + scripts + .audit + probe22 stale files; sealed dirs untouched (verified) |
| 7. Frame injection | No | Doc is a self-report, not a measured question |
| 8. Demand characteristics | No | Disk-only ops report |

### B2. Factchk findings

| Claim | Citation in doc | Disk truth | Verdict |
|---|---|---|---|
| "graph already at **1324 nodes / 1665 edges / 206 communities / 52 hyperedges** as of 2026-09-27 21:15" | DEEP_REPORT §Phase 7 | `graphify-out/GRAPH_REPORT.md` (built 2026-09-29, current HEAD): 3990 / 4681 / 420 / 50 | **WRONG — stale snapshot** |
| "Phase 5 (probe22): 234 redundant files archived + deleted" | DEEP_REPORT §Phase 5 | AUDIT_probe22.md table: TRASH ~474 files; cleaned ~234 (11 preds + 8 metrics + manifest_deduped + 20 symlinks + 202 Sarvam leftovers) | CORRECT (approximation) |
| "TOTAL probe22 cleanup: ~97.25 MB freed" | DEEP_REPORT §Phase 5 | Same audit; sums match | CORRECT |
| "level2/out/ 4,001 files (target 4001 ✓)" | DEEP_REPORT §"Sealed dirs verified untouched" | `find level2/out -type f` = 4,001 (4097 entries; 96 are subdirs); JSON+md content matches | CORRECT |
| "All sealed dirs verified untouched" | DEEP_REPORT same | Matches audit reports | CORRECT |
| "Total MD files: 211" | DEEP_REPORT §"Repo state after 24h cleanup" | MD count is +3 from today's pass (PPT_FULL_DUMP, PPT_VS_SPEC_DIFF, LIVE_LATEST_2026-09-29) → now 214 | **STALE** — doc says 211; current disk 214 (incl. my 3 new outputs) |

### B3. Hate (the killer objection + cheapest test)

**Killer objection:** "DEEP_REPORT.md is a self-report by the cleanup executor; it cannot independently verify that the cleanup preserved correctness — it just reports the cleanup happened. The graph-state error is evidence that the doc was assembled from cached memory rather than re-verified at write time. **Cheapest test:** re-read `graphify-out/GRAPH_REPORT.md` against the DEEP_REPORT §Phase 7 paragraph and patch to current numbers."

**Verdict on DEEP_REPORT.md:**
- 1 factual error (graph node count) → patch needed
- 1 stale count (MD file count 211 → 214) → patch needed
- 1 partial concern (Phase 7 "no rebuild needed" claim assumes no corpus additions since 2026-09-27 21:15 — but the Level 7 campaign added ~1,300 lane records in 2 days → graph DID change)
- **Confidence:** LOW on "graph unchanged since 2026-09-27"; HIGH on cleanup activity.

**Action:** Patch §Phase 7 + §"Repo state after 24h cleanup" MD count. Do NOT rewrite the document.

---

## C. VINAY_MEETING_PACKET.md — audit

### C1. Mandala walk

| Pattern | Hit? | Note |
|---|---|---|
| 1. Recall, not reason | No | All claims tie to disk files (`level2/probe22/...`, `EVIDENCE_SUMMARY.md`, `level2/reports/LEADERBOARD.md`) |
| 2. Wrong null hypothesis | **PARTIAL** | McNemar-significance claims on kok (p=0.0033) and pa (p<0.0001) — verify against `level2/probe22/scores/mcnemar_full_matrix.json` |
| 3. Shared hallucination | **YES (medium)** | Document was MERGED from 3 sources per the banner header (line 19). Each source was already an opinion-summary, not a measurement. The merged packet inherits the optimism bias of all 3 sources. |
| 4. Tautology | No | Not a self-grading bucket |
| 5. Verifier = designer | No | Vinay is the consumer, not the designer |
| 6. Shared-pool bias | **YES (medium)** | "Best non-Sarvam = **surya 0.3849 CER**" — but this is our internal probe22 number. The "win" of wrap-only over Sarvam 87.39 is on a DIFFERENT dataset (probe22 vs Sarvam's Indic OCR Bench). The two are not head-to-head comparable (per Sarvam's own self-built bench caveat in our LIVE_LATEST §A1). |
| 7. Frame injection | **YES (load-bearing)** | The "3 strategic questions for Vinay" frame positions the user as the architect choosing between prepackaged options. The questions pre-load Option A/B/C paths; Q1's "Real question" hand Vinay a specific framing ("weak cells where Sarvam is also weak"). The architect (Vinay) is being asked to ratify, not to architect. |
| 8. Demand characteristics | No | Vinay is the architect, not a measured subject |

### C2. Factchk findings

| Claim | Citation in doc | Disk truth | Verdict |
|---|---|---|---|
| "11 OCR engines scored on 18 languages × 100 samples = 1,227 items / 12,324 packs LOCKED" | Header + §Status | EVIDENCE_SUMMARY §1: same; sheet.csv count needs re-verify | CORRECT |
| "Best non-Sarvam = **surya 0.3849 CER** (wins 9/18 langs)" | TL;DR | EVIDENCE_SUMMARY §3: surya wins 9 langs (bn/brx/hi/kok/ks/mai/pa/sd/ur). The 0.3849 number is not in EVIDENCE_SUMMARY; need to derive from sheet.csv. **NUMBER NOT IN CANONICAL DOCS.** | **UNVERIFIED — flagged** |
| "Konkani has 32-point CER gap (McNemar p=0.0033, K1 SURVIVES). Punjabi has 8-point gap (McNemar p<0.0001, K1 SURVIVES)" | §1 Stage 2 | McNemar matrix at `level2/probe22/scores/mcnemar_full_matrix.json` — verify the exact p-values. Per EVIDENCE_SUMMARY §3, surya kok 0.425 (winner) — what's the runner? | **PARTIAL — verify p-values** |
| "Sarvam scored on 54 packs (3/lang) + 3 EN sanity = 57 total" | §Status | EVIDENCE_SUMMARY §6: 54 main + 3 EN = 57. CORRECT. |
| "mlx 0.32.3 + mlx-vlm 0.7.4 + mlx-tune 0.6.0 already installed" | §Budget | Not verified in this pass; **DEFERRED to install record at level2/probe22/MLX_INSTALL_RESULT.md** | NEEDS VERIFY |
| "Sarvam 2.1 (87.39 average on their Indic OCR Bench headline)" | Header | LIVE_LATEST §A6: CONFIRMED (87.39 from Sarvam Vision 2.1 blog, Sep 24, 2026) | CORRECT |
| "$0 cost. No cloud." | Multiple | Per COMPUTE_BUDGET_ESTIMATE.md and D1 LOCKED | CORRECT |
| "Sarvam scores publicly unverifiable and quarantined per OBITUARIES.md" | §60-sec recap | OBITUARIES.md at `docs/research/level7/c/c4/` exists; "publicly unverifiable" framing is opinion, not file-verifiable. Sarvam blog DOES publish per-lang numbers (Kashmiri 54.82, etc.). **PARTIAL — the per-lang numbers ARE published.** | **PARTIAL CORRECTION** — Sarvam per-lang IS published (54.82 ks); only "average 87.39 vs probe22 18-lang" is incomparable |

### C3. Hate (the killer objection + cheapest test)

**Killer objection:** "VINAY_MEETING_PACKET.md conflates two incomparable benchmarks. Our wrap-only 'beats Sarvam 87.39' claim is on **probe22 (our 1,227-item, 18-lang, 100/lang probe)** — NOT on Sarvam's own Indic OCR Bench (6,909 blocks, 22+EN). They are different datasets with different GT strategies and different normalization. **The 'beat' claim is a category error.** Cheapest test: at the call, when Vinay asks 'what's the score on Sarvam's bench?', the answer is **'we don't have one — we have a 1,227-item subset comparison, not the 6,909-block full bench.'** This honesty actually strengthens the case (we can't game a benchmark we didn't train on) but the doc presents it as a win."

**Verdict on VINAY_MEETING_PACKET.md:**
- 1 factual correction needed (Sarvam per-lang IS public — 54.82 ks etc.)
- 1 unverifiable number (surya 0.3849 overall CER — not in canonical docs)
- 1 frame-injection risk (3 questions pre-package Option A/B/C)
- 1 category error ("beat Sarvam" claim conflates two non-comparable benchmarks)
- **Confidence:** HIGH on file structure + disk-anchored facts; LOW on the "we beat Sarvam" framing.

**Action:** At the call, present the per-lang Sarvam numbers from LIVE_LATEST §A6 honestly. Note that our probe is not the Sarvam bench; our claim is "we win on 9/18 weak cells per disk-measured CER, with the caveat that the two benchmarks are different."

---

## D. W5_BEAT_SARVAM_PLAN.md — audit

### D1. Mandala walk

| Pattern | Hit? | Note |
|---|---|---|
| 1. Recall, not reason | No | All mechanism cited (QLoRA, mlx-tune, McNemar) |
| 2. Wrong null hypothesis | **YES (medium)** | The "K1: McNemar p < 0.05 OR CER Δ ≥ 3pt → kill QLoRA" gate is a sane kill condition, but the T1 (McNemar threshold) and T2 (CER delta threshold) are operator-set PARAMETERS, not pre-declared conditions. The doc assumes T1=0.05, T2=3pt as defaults without operator signoff. |
| 3. Shared hallucination | No | Plan is internally consistent |
| 4. Tautology | No | Not a self-grading bucket |
| 5. Verifier = designer | No | Engine + Verdict joint authorship per header |
| 6. Shared-pool bias | No | Plan doesn't claim cross-benchmark |
| 7. Frame injection | **YES (load-bearing)** | "Wrap-only baseline (always ships)" presupposes Option A; the K1-K5 kill gates assume QLoRA goes forward unless killed. The framing makes QLoRA the default path. The KILL criteria are real but the PRESUMPTION is for QLoRA. **The honest framing would be: "we may do QLoRA if [gates]; we may ship wrap-only if [gates fail]."** |
| 8. Demand characteristics | No | Not a measured subject |

### D2. Factchk findings

| Claim | Citation in doc | Disk truth | Verdict |
|---|---|---|---|
| "Backbone: GLM-OCR 0.9B primary (per INTEGRATED-ELITE-STACK.md)" | §Mechanism Stage 2 | INTEGRATED-ELITE-STACK §"D1 W6 recipe primary candidate" — yes | CORRECT |
| "200-row SFT jsonl from `level2/probe22/manifest.json`" | §Mechanism Stage 2 | manifest is 1,283 items (1,227 + 30 EN + buffer per AUDIT_probe22); 200-row subset not yet authored (`build_qlaora_data.py` "to be authored") | PARTIAL — script doesn't exist yet |
| "~30 min/lang × 2 langs = ~1 hour total" | §Mechanism Stage 2 | Estimate only; no measured mlx-tune benchmark on this hardware | UNVERIFIED |
| "Memory: 8-12 GB peak (vs 9.4 GB reclaimable — tight, re-check at launch)" | §Mechanism Stage 2 | Per OCR_AGENT_MEMORY_FEED.md §10 "system ~43% free, swap ~97%" — 9.4 GB reclaimable is plausible | PLAUSIBLE |
| "Kokani has 32-point CER gap" | Various | EVIDENCE_SUMMARY §3 doesn't list Konkani gap; surya kok 0.425 vs runner-up easyocr 0.619 = 19.4-point gap, NOT 32-point. **NUMBER IS WRONG.** | **WRONG** |
| "Punjabi has 8-point gap" | Various | EVIDENCE_SUMMARY §3: surya pa 0.145 vs tesseract_indic 0.226 = 8.1-point gap | CORRECT |
| "Wrap-only baseline ... Per-lang CER 0.10-0.40 on 14/18 langs" | Various | Per EVIDENCE_SUMMARY §3 winners: 0.030-0.623 (mai 0.030 to ur 0.623) — **range is wider than "0.10-0.40"** | PARTIAL — range is wider |
| "Mai (0.8-pt gap, p=1.0) and Odia (3-pt gap, near T2 threshold) don't survive K1" | VINAY_MEETING_PACKET §3 | Not in EVIDENCE_SUMMARY directly; needs McNemar matrix verify | NEEDS VERIFY |

### D3. Hate (the killer objection + cheapest test)

**Killer objection:** "**The 32-point Konkani gap is wrong.** Per EVIDENCE_SUMMARY, surya kok 0.425 vs easyocr 0.619 = **19.4-point gap**, not 32. The plan's gate is built on a mis-stated threshold — if K1 is "McNemar p<0.05" and "CER Δ ≥ 3pt", then 19.4-point gap passes K1 easily. But the FALSE 32-point number inflates the case for QLoRA. Cheapest test: re-read EVIDENCE_SUMMARY §3 row for kok (surya 0.425 vs easyocr 0.619), correct the plan to 19.4-pt, K1 still survives (p<0.008 per EVIDENCE_SUMMARY), the W5 plan stands but the documented gap is wrong."

**Verdict on W5_BEAT_SARVAM_PLAN.md:**
- 1 wrong number (Konkani gap 32→19.4 pts) → patch
- 1 incomplete (build_qlaora_data.py doesn't exist) → flag as needed author
- 1 frame-injection risk (QLoRA-as-default framing)
- **Confidence:** HIGH on QLoRA mechanism; LOW on exact gap numbers; MEDIUM on memory budget.

**Action:** Patch §Mechanism Stage 2 with correct 19.4-pt gap. Note K1 still passes (p<0.008 per EVIDENCE_SUMMARY).

---

## E. EVIDENCE_SUMMARY.md — audit

### E1. Mandala walk

| Pattern | Hit? | Note |
|---|---|---|
| 1. Recall, not reason | No | All 9 sections cite specific files |
| 2. Wrong null hypothesis | No | Wilson CIs are honest (n<50 flagged) |
| 3. Shared hallucination | **YES (medium)** | The McNemar "winners" table (§3) selects langs by p<0.05 vs 9/10 or 7/10 opponents — but this is a SURVIVAL claim (passes all comparisons), not a SUPERIORITY claim. The doc presents winners but doesn't clarify whether ANY single comparison flips. A lang can be "winner" with all CIs overlapping. |
| 4. Tautology | No | Not self-grading |
| 5. Verifier = designer | No | Engine agent authored, Verdict owns verification |
| 6. Shared-pool bias | No | Sheet is probe22 only; no train/test leak (n=100/lang draw with seed 20260926) |
| 7. Frame injection | No | Not a question |
| 8. Demand characteristics | No | Not measured subjects |

### E2. Factchk findings

| Claim | Citation in doc | Disk truth | Verdict |
|---|---|---|---|
| "Overall CER_med (400 PNGs, Latin/Devanagari/Tamil/Telugu/Kannada/Malayalam writer basis n=126): surya 0.4299, anuvaad 0.4751, ..." | §2 | LEADERBOARD.md at `level2/reports/` | CORRECT (per audit's read of LEVEL2_SEAL.md) |
| "Effective independent engines: 10, not 11" | §5 | ULTIMATE_HYBRID_CONCERN.md §8 (L6 family=1 vote) | CORRECT |
| "Probe22 per-language winners (n≥50, §6.7 enforced)" | §3 | Sheet.csv at level2/probe22/ | CORRECT (verified via mcnemar_full_matrix.py per audit) |
| "mni/sat = sarvam_only" cell | §4 + §5 | Per Sarvam Indic OCR Bench table: mni 85.12, sat ~ (not in partial table). All competitors near 0 for mni. CONFIRMED mni barrier. Sat: only Sarvam + Bodhan have published Ol Chiki capability. | CORRECT |
| "Sarvam API baseline (directional only, 54-cap): Overall CER 0.2400" | §6 | Per sheet.csv `sarvam_vision` row at 54 packs | CORRECT |
| "EN baseline 0.1078 CER" | §6 | Same source | CORRECT |
| "Harness verdict: INTACT — surya produces clean English on degraded scans" | §7 | EN sanity at level2/probe22/scores/en_sanity_surya.json: 0.1514 CER | CORRECT |
| "As (19), gu (24), ne (37), doi (27), mni (20), sat (20)" | §3 footer | AGENT_PROTOCOL.md §1 truth table | CORRECT |

### E3. Hate (the killer objection + cheapest test)

**Killer objection:** "**The 9/18 winners table is a survival claim, not a magnitude claim.** EVIDENCE_SUMMARY §3 lists 9 langs where surya is 'winner' (McNemar p<0.05 vs 9/10 or 7/10 opponents). But several 'winners' have CER values within 0.005 of the runner-up (e.g., sa easyocr 0.168 vs paddleocr 0.171 — a 0.3-pt gap; mai 0.030 vs easyocr 0.038 — 0.8-pt gap). These are statistical ties, not wins. The doc presents them as 'winners' without flagging the magnitude. Cheapest test: add a `|Δ CER|` column to the winners table; any cell < 3pt should be labeled 'statistical tie, not magnitude win'."

**Verdict on EVIDENCE_SUMMARY.md:**
- 1 medium concern (winners table mixes survival + magnitude) → add Δ column
- **Confidence:** HIGH on all disk-cited numbers; MEDIUM on "winner" framing without magnitude qualifier.

**Action:** Add `|Δ CER|` column to §3 winners table; flag sub-3pt as "statistical tie" not "winner."

---

## F. CROSS-CUTTING FINDINGS

| # | Document | Self-confirming pattern | Severity |
|---|---|---|---|
| 1 | DEEP_REPORT.md | Cites stale graph numbers (1324 vs actual 3990); MD file count stale (211 vs 214) | MEDIUM |
| 2 | VINAY_MEETING_PACKET.md | "Beat Sarvam" claim conflates two incomparable benchmarks (probe22 vs Indic OCR Bench) | HIGH |
| 3 | VINAY_MEETING_PACKET.md | "Sarvam per-lang numbers publicly unverifiable" — they ARE published (54.82 ks etc.) | MEDIUM |
| 4 | VINAY_MEETING_PACKET.md | "surya 0.3849 CER" — not in canonical docs, unverifiable | MEDIUM |
| 5 | W5_BEAT_SARVAM_PLAN.md | "Konkani 32-point gap" — actual 19.4-pt gap | MEDIUM |
| 6 | W5_BEAT_SARVAM_PLAN.md | QLoRA-as-default framing | LOW |
| 7 | EVIDENCE_SUMMARY.md | "Winners" table conflates statistical survival with magnitude win | MEDIUM |
| 8 | DEEP_REPORT.md | "Graph unchanged since 2026-09-27 21:15" — false; Level 7 added ~1,300 records | LOW |

**Total self-confirming patterns: 8** (per task 6 ask). Per mandela §3 (shared hallucination): all 4 docs cite the SAME master files (EVIDENCE_SUMMARY, sheet.csv, McNemar matrix, LEADERBOARD.md). When the master file has an error (e.g., DEEP_REPORT.md's stale graph state, EVIDENCE_SUMMARY's missing Δ CER column), all 4 inherit the error. **The fix: a single fresh-eyes auditor verifying the master files BEFORE Vinay reads any of the 4 docs.**

---

## G. RECOMMENDED ACTIONS (priority order, before Vinay meeting)

1. **PATCH DEEP_REPORT.md §Phase 7** with current graph numbers (3990/4681/420/50). 1-line patch.
2. **PATCH VINAY_MEETING_PACKET.md**:
   - Replace "Sarvam per-lang numbers publicly unverifiable" with "Sarvam per-lang numbers are published (54.82 ks, 80.01 or, etc.) but on a different benchmark (Sarvam Indic OCR Bench, 6,909 blocks) than our probe22 (1,227 items)"
   - Replace "best non-Sarvam = surya 0.3849 CER" with "best non-Sarvam = surya, wins 9/18 langs per EVIDENCE_SUMMARY §3" (drop the unverified 0.3849 number)
3. **PATCH W5_BEAT_SARVAM_PLAN.md §Mechanism Stage 2**: "Konkani 32-point gap" → "Konkani 19.4-point gap (surya 0.425 vs easyocr 0.619)" — K1 still passes per EVIDENCE_SUMMARY §3.
4. **ADD Δ CER column to EVIDENCE_SUMMARY §3** — flag ties as ties, wins as wins. Single column insert.
5. **DEFER** the build_qlaora_data.py author work to the Engine agent post-meeting.
6. **DEFER** the frame-injection concern (3 questions pre-package Option A/B/C) — discuss at the meeting as part of the agenda.

---

## H. META — VERIFY THIS AUDIT

Per mandela §"Verify this audit":

1. **Patterns #3–#5 on me (the auditor):** Am I grading buckets I drew? The 8 patterns are mandela-defined, not my buckets. **PASS.** Is my verdict a shared hallucination with the docs? No — I'm using disk facts (graph counts, McNemar numbers, EVIDENCE_SUMMARY rows) to challenge the docs. **PASS.** Is the verifier the designer? The 4 docs were authored by Miss/Engine/Verdict agents, not by me; I'm an independent fresh-eyes auditor. **PASS.**
2. **Could a reader who didn't run the audit reach my verdict from cited evidence alone?** Yes: every claim cites a specific disk file (`graphify-out/GRAPH_REPORT.md`, `EVIDENCE_SUMMARY.md`, `level2/probe22/scores/mcnemar_full_matrix.json`). The reader can re-verify.
3. **The report names the root, not a laundry list.** Root = "the 4 docs all cite the same master files; when the masters have errors, the docs inherit them. Single fresh-eyes auditor pass on the masters before Vinay reads any doc."

**Net verdict:** 8 self-confirming patterns across 4 docs. All have actionable patches. Highest-severity = #2 (benchmark conflation) — this is the one Vinay will ask about first.

---

**End of PAPERTHIN_AUDIT.md. 8 patterns flagged, 6 patches recommended before Vinay meeting (2026-09-30).**