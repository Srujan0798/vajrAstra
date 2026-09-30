# FIX SPECS — Verdict → Miss (H48 hostile pass, 2026-09-29 02:42 IST)

Per the fix-loop law (campaign §1): Verdict specifies; Miss applies.
These specs are for **shared artifacts only** (CALL_PACKET.md, FINAL_REPORT.md, MISS_MONITOR.md).
**Already applied by Verdict:** `gt_verification.json` (summary refresh), `verify_unaccounted.md` (re-verification), B3/B4 §9 field repairs (281 records).

---

## FS-V1 — CALL_PACKET.md line 12 stale engine-run status

**Current (stale):**
```
- **Engine**: **ALL 11 ENGINES SCORED**. Final report at `level2/probe22/FINAL_REPORT.md` (13KB, written 20:31). Sheet.csv 11,097 rows = 9×1227+54 (sarvam). All engine queue COMPLETE.
```

**Refresh to:**
```
- **Engine**: **ALL 11 ENGINES SCORED**. Final report at `level2/probe22/FINAL_REPORT.md` (13KB, written 2026-09-28 20:31). Sheet.csv 12,324 rows = 10×1227+54 (10 local engines + 1 Sarvam API). All engine queue COMPLETE 2026-09-28 19:33 IST (surya added 2026-09-28 19:33).
```

**Justification:** `sheet.csv` = 12,324 rows (counted via `awk -F, '{print $9}' sheet.csv | sort | uniq -c`). The 11,097 figure predates surya completion. Engine queue is COMPLETE (no in-flight engines as of 2026-09-28 19:33 IST).

---

## FS-V2 — CALL_PACKET.md line 20 wrong Kashmiri trust number

**Current:**
```
- R5: Kashmiri PDF trust 29/100
```

**Refresh to:**
```
- R5: Kashmiri PDF trust 45.0/100 (gt_forensics.json per_language.ks.trust_score). VERIFY-FIRST (visual 0/10 + R5 45.0 fails >20% gate → BARRED from W6 SFT).
```

**Justification:** `gt_forensics.json` `per_language.ks.trust_score` = **45.0** (PRIMARY/MEASURED). The 29 number has no source on disk. R5 trust 45.0 + visual 0/10 = ks BARRED-from-W6-SFT (combined verdict).

---

## FS-V3 — CALL_PACKET.md line 32 wrong human pairs total

**Current (line 32 / §4 / §5 / any reference):**
```
- 10,434 human pairs (bn 2,938 / hi 3,500 / sa 494 / en 3,500)
```

**Refresh to:**
```
- 10,432 human pairs (bn 2,938 / hi 3,500 / sa 494 / en 3,500)
```

**Justification:** Internal arithmetic: 2938 + 3500 + 494 + 3500 = **10,432** (verified). The 10,434 is off by 2 (likely typo from earlier doc revision). This number appears in AGENT_PROTOCOL.md §9 and elsewhere — fix at the source.

---

## FS-V4 — CALL_PACKET.md line 32 LEADERBOARD reference

**Current:** (implicit, points to `scores/LEADERBOARD.md`)

**Refresh to:**
```
- Source of truth: `level2/probe22/scores/LEADERBOARD.md` (refreshed 2026-09-28 19:33 IST after surya completion; 12,324 sheet rows; 10 effective engines).
```

**Justification:** LEADERBOARD was generated 2026-09-28 19:33 by orchestrator; should be Engine's artifact post-surya-completion. Source-of-truth reference date should be explicit.

---

## FS-V5 — LEADERBOARD.md "19/18 langs" labeling bug

**Current:** Coverage table cells like `doctr | 1257 | 1256 | 1 | 18/18 + EN`.

**Refresh to:** Either drop the `+ EN` suffix and report `18/18` (probe-only), OR explicitly footnote that the 30 EN-sanity items are separate from n=1227 probe. Choose consistent format across all 11 rows.

**Justification:** 5× rows show "19/18 + EN" labeling. EN-sanity is a separate manifest (`en_sanity/manifest.json`) — comparing 18 probe langs + 1 EN sanity as "19/18" is misleading. Either treat EN as part of probe (and bump denominator) or as separate (and don't show "19").

**Suggested:** all 11 rows show "X/18 + EN" where X is the number of probe langs with non-empty output, and "+ EN" is the explicit EN-sanity column.

---

## FS-V6 — LEADERBOARD.md missing Wilson CI column

**Current:** Headline rankings show point estimate only (e.g., "sarvam_vision 0.2400").

**Refresh to:** Add Wilson 95% CI per cell. CI files exist on disk (`scores/wilson_ci_*.json`) — surface them in the table.

**Justification:** §6.7 power statement requires CIs everywhere. n=3 cell (sarvam_vision) has CI half-width >50pp; the table presents the point estimate as if comparable to n=1227 cells.

---

## FS-V7 — LEADERBOARD.md script-correct column (sat/ks/mni)

**Current:** Coverage table uses "Non-empty" / "Honest-empty" columns.

**Refresh to:** Add a third column "Script-correct" for sat/ks/mni only — count predictions where script_adherence ≥ 0.95 (using the same threshold as `verify_visual.py`).

**Justification:** An engine emitting Latin gibberish on sat counts as "non-empty". The honest-empty column doesn't separate "I produced the right script" from "I produced text". For weak-cell languages (sat/ks/mni where Latin emission is the failure mode), the script-correct count is the meaningful signal.

---

## FS-V8 — LEADERBOARD.md bold the barred cells

**Current:** Barred-lang cells (ks/mni/ur/sat/mr + ne PDF-tier) are in the same table as safe cells, with a footnote at the bottom.

**Refresh to:** Bold the barred cells in the table itself, with a §6.4-lock footnote pointer at each cell.

**Justification:** A reader scanning the table without seeing the §6.4 lock footnote will draw conclusions from ks/sat/mni CERs as if comparable to safe-lang CERs. Bold + inline footnote forces the reader to acknowledge the lock.

---

## FS-V9 — Engine queue completion timestamp

**Apply to:** CALL_PACKET.md, FINAL_REPORT.md, MISS_MONITOR.md

**Add explicit "Engine queue complete: 2026-09-28 19:33 IST (surya added)" stamp** at the top of any document that asserts engine status. The 19:33 timestamp is when surya's last pack completed (`out/surya/<lang>/<id>.json` mtime + sheet.csv surya row count = 1227).

**Justification:** Future agents reviewing the docs need to know when the data was frozen. Missing timestamps make it ambiguous whether engine queue is complete or in-flight.

---

## STATUS: 9 FIX SPECS, READY FOR MISS.

Verdict has applied the 6 fix-specs for Verdict-owned artifacts (gt_verification.json, verify_unaccounted.md, B3/B4 §9 repair). Miss owns these 9 specs for shared artifacts.
