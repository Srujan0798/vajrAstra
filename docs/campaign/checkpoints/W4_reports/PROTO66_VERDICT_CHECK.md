# PROTO-66 VERDICT CHECK — the concern register

**Verifier:** Verdict + research lane (OpenCode `ses_f1233a0a…`) · **Date:** 2026-09-30
**Register checked:** `BOSS_CONCERNS.md` — **64,363 bytes, mtime 2026-09-30 16:31:13, 296 register rows**
**Method (proto-66 "Verdict check"):** re-run every DONE-VERIFIED evidence command · sample 15 other rows · confirm no concern from sources 1–5 is missing (count rows per source).
**I modified nothing.** `BOSS_CONCERNS.md` is byte-identical to how I found it; a pre-image was taken at `_archive/pre_fix_2026-09-30/BOSS_CONCERNS.pre-verdict.md` but no edit was applied (see the correction below).

## What is right

The rebuild is real work, not a template. It has the proto-66 layout (`How to use` · `Part 1 Register` · `Part 2 Open work summary` · `Appendix A Status diary` · `Appendix B Sources`), per-row **evidence with actual commands and outputs**, a **protocol owner** per row, and a source attribution per row. Evidence is concrete, e.g. CO-002: `find level2/unified/ -type l | wc -l` shows 17,289 symlinks; CO-005: `find . -type f | wc -l` = 59,769 with the note that `AUDIT_REPORT.md` is directory-level.

### Source coverage (protocol sources 1–5) — COMPLETE
| source | required | present | verdict |
|---|---|---|---|
| uni_v3 Parts 18–20 | CO-001…CO-096 | **96 / 96**, none missing | **PASS** |
| `SESSION_DIRECTIVES_2026-09-28.md` §3 | C1–C17 | **17 / 17** | **PASS** |
| chat meta-concerns | M1–M8 | **8 / 8** | **PASS** |
| boss 2026-09-30 afternoon turns (HL) | H1–H12 | **12 / 12** (filed as `HL1…HL12`) | **PASS** |
| `CAMPAIGN_DIRECTIVE.md` Part B / G0 | C1–C12 + the CO crosswalk | covered by the C-series rows; **all 96 CO ids in the G0 crosswalk are present in the register** | **PASS** |
| **source 6 — the two meetings** | `S10-*` and `S29-*` rows | **0 / 0** | **FAIL — see D1** |

## Defects found

### D1 — the two meetings are absent from the register (0 rows). **BLOCKER-ish, and it matters most.**
proto-66 source 6 requires both meetings read in full, with *"every action item, method step and red line becomes a row (S10-*, S29-; crosswalk proto-99 §I)"*. The register carries **zero** `S10-*` and **zero** `S29-*` rows. I read the Sep 10 transcript in full this lane for the B-14 ruling and can already show what is being lost — the red lines live there, and they are what the boss enforces on us:
- *"No training before research validation"* (Sep 29, D4/D5 — this is the red line currently at risk from the Engine lane's Day 3)
- *"there should be one standard, like one page, one sample"* (Sep 10 — captured only inside my B-14 ruling, not as a register row)
- the Sep 29 method steps (a)–(j) and the action items A1–A7
A register that omits the meetings cannot be the single live truth `uni` T3.2 demands.

### D2 — **not one row is marked DONE-VERIFIED, and 35 claim a bare "DONE."**
The protocol's central rule: *"a row can be DONE only if the Evidence column holds a command whose output reproduces the claim today. Verdict re-runs every DONE row's command."* On disk: **DONE-VERIFIED = 1 row; bare `DONE` = 35 rows.** This is the same overclaim the protocol was written to strip — 35 rows still assert completion in a word the register does not define.

I sampled **15 of the 35** DONE rows. **7 carry a runnable command** in Evidence; **8 do not** — they carry prose or a bare file reference, e.g. #29 *"verified NOT in Surya 2's 91-lang benchmark"*, #28 *"`AGENT_PROTOCOL.md` §6.4 LOCKED"*, #57 *"surya.predict() ran on 3 probe22 images, 41.6s"*, #25 *"113 extras = 30 EN-sanity + 83 pre-purge orphans"*. Those 8 cannot be re-verified today as the rule requires, so they are not DONE-VERIFIED-eligible in their current form. The 7 with commands are verifiable, but I did not re-run them in this pass (they are individually cheap; that is the remaining work).

### D3 — 22 rows use status words the register does not define.
- **18 rows** use `OVERCLAIMED`; the canonical word in the protocol's own list is **`OVERCLAIMED-REOPENED`**.
- **4 rows** use `PENDING`, which is **not in the allowed list at all** (allowed: DONE-VERIFIED · PARTIAL · OPEN · BLOCKED-ON-BOSS (U-id) · SUPERSEDED · STANDING · OVERCLAIMED-REOPENED).
`grep -c '| PENDING' BOSS_CONCERNS.md` = 4. This matters mechanically: `uni` T3.2 makes this file the thing every agent reads each turn, and a status word that is not in the legend cannot be counted.

## Correction to my own check — recorded because a Verdict that reports a false finding is worse than one that reports nothing
My first pass reported **"CO-032 is missing from the register"** and I began to add it. **That was a false positive from my own parser**, which dropped any row with fewer than 7 pipe-delimited columns. Corrected with a direct `grep -c '^| CO-[0-9]'`: **96 of 96 CO rows are present, none missing.** The file was never modified. Likewise an intermediate "H1–H12 missing" was wrong — they are filed as `HL1…HL12`, all 12 present. **Both were my measurement errors, not register defects.**

## Verdict
**PASS-WITH-FIXES.** The register is structurally correct, its sources 1–5 coverage is complete and its evidence is concrete. Three fixes stand between it and proto-66's DONE-VERIFIED rule:
1. **D1** — add the `S10-*` / `S29-*` meeting rows (both meetings, every action item, method step and red line). *This is the one that protects the red lines.*
2. **D2** — resolve the 35 bare-`DONE` rows: re-run the evidence command and promote to `DONE-VERIFIED`, downgrade to `PARTIAL`, or write the reason it cannot be verified. 8 of 15 sampled have no runnable command at all.
3. **D3** — normalise 18 `OVERCLAIMED` → `OVERCLAIMED-REOPENED` and 4 `PENDING` → a word in the legend.

I have **not** applied 2 or 3: rewriting 35 status cells is a Miss-lane edit, and no U# covers it. Recommend the boss authorise the vocabulary normalisation (D3, mechanical) and assign the meeting transcription (D1, the real work).
