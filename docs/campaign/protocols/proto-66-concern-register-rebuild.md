---
name: proto-66-concern-register-rebuild
description: "Added 2026-09-30 — rebuild BOSS_CONCERNS.md into a true register: every boss concern verbatim (CO-001…096, C1–C17, uni Part items, chat meta-concerns M1–M8) with a disk-verified status; strip the overclaimed DONE marks; keep the old status diary as an appendix"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:51:49.376Z
---

# PROTO-66 — REBUILD THE CONCERN REGISTER (Miss builds, Verdict verifies every DONE)

**Why (monitor, 2026-09-30):** `BOSS_CONCERNS.md` (root, 517 lines) turned into a status diary. `uni` T3.1 required CO-001…CO-096 verbatim; they were never transcribed.
It marks as DONE things that are not done on disk. The boss: "many concerns are still left and not done", "I value all my concerns". A repeated concern = a memory-system
bug (uni T3.3). This protocol makes the register the single live truth every agent reads each turn (uni T3.2).

## Sources (all concerns, read fully)
1. `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt` Parts 1–17 (rule/task items T1.x, T2.x, T3.x, T6.x, T7.x, T8.x, C10.x, R11.x, P12.x, F13.x, E14.x, L15.x) and Parts 18–20 (CO-001…096).
2. `docs/research/level7/boss_directives/SESSION_DIRECTIVES_2026-09-28.md` §3 — C1–C17 (77 boss turns, verbatim quotes) and §11 lessons.
3. `BOSS_CONCERNS.md` items 1–81 (current).
4. The boss's chat meta-concerns (2026-09-29/30), recorded here as **M1–M8**:
   M1 Opus plans deeply, Sonnet executes; never Opus subagents · M2 protocols must be many, deep and stored in memory so any agent can execute them ·
   M3 read and understand all important files before planning · M4 graphify must be used · M5 plan to 100% completion, "I stake my life" ·
   M6 monitor the executing agents, find misleading/unfinished work, add protocols · M7 all concerns considered, none dropped ·
   M8 level2 still shows old/unwanted files, old South out vs new out separate, misleading hierarchy — sort it out (2026-09-30).
5. `docs/campaign/CAMPAIGN_DIRECTIVE.md` Part B (C1–C12 settled conflicts; C13–C15 in memory `conflicts-register`) and Part G0 crosswalk.
6. **The two meetings, read in full:**
   - `sync - ocr - September 10.docx` (302 lines; moves to `docs/sources/meetings/` in proto-98 Phase 1);
   - `docs/research/MEETING_2026-09-29_STRUCTURED.md` (raw transcript + D1–D7 / A1–A7).
   Every action item, method step and red line becomes a row (S10-*, S29-*; crosswalk `proto-99` §I).
7. The boss's 2026-09-30 afternoon turns H1–H12 (`proto-99` §H).

## Known overclaims to correct (verify each; do not trust this list either)
- #1 / #47 "54,000+ files inventoried, KEEP/MERGE/DELETE per file" — `AUDIT_REPORT.md` is directory-level (uni T1.3 unmet).
- #2 / CO-001 "old folder resolved" — no folder named old, but old-vs-new parallel structures remain (`level2/out` vs `level2/probe22/out`; `models/` vs `out/`; `unified/`).
- #3 / #12 / CO-003/025/068 South merged — only a symlink view exists; South is not at the same standard (126/400 scored; different sources/GT).
- #49 D4 "sample plan DONE" — 1,227 scored / 1,283 manifest vs 1,800 (now 2,200) target.
- #71 "models vs out KEEP BOTH" — contradicts CO-004 (content SHA256-identical per `level2/MODELS_VS_OUT.md`); it says "deferred … if user approves".
- #80 "R3 deferred" — the boss's 2026-09-30 message (M8) asks for exactly this.
- FINAL section "0 duplicates remain" — false (3× W5_BEAT_SARVAM_PLAN, 2× LIVE_LATEST, 2× meeting packet, 2× uni, 2× meeting file).
- #31 "effective independent engines = 10" — 1A: tesseract_bilingual differs from the other two on 857/1,227.
- C1 status "Already done" (1800) — not done; C16 "bn/hi/sa = 100 tiles of 1 page" — disproven (ids spread across the pool).
- "Council of Kang reviewed all 7 decisions", "Laya/paperthin/looper/ECC fully integrated" — find evidence or mark UNVERIFIED. Laya was never integrated: proto-31 / U30 rule it NOT used, and U31 allows only an advisory triage trial.
- The CORRECTION line "11 engines × 1,283 items × 18 langs = 14,138 packs (locked)":
  - the arithmetic is wrong (11 × 1,283 = 14,113);
  - it mixes the manifest (1,283) with the scored set (1,227) and with sealed `probe22/out` (13,289 packs).
- Item #45 is written twice.

## New file layout (edit `BOSS_CONCERNS.md` in place; the pre-image is the proto-98 Phase 0 snapshot — take it first if it doesn't exist; no per-file copies)
```
# BOSS_CONCERNS.md — the live register (read FIRST every turn — uni T3.2)
## How to use  (5 lines: statuses, evidence rule, append rule, who maintains)
## Part 1 — Register
| ID | Concern (verbatim or exact quote) | Source | Status | Evidence (command/file:line) | Protocol | Last verified |
Statuses: DONE-VERIFIED · PARTIAL · OPEN · BLOCKED-ON-BOSS (U-id) · SUPERSEDED (by C-id, with reason) · STANDING (a rule, never "done") · OVERCLAIMED-REOPENED
Order: CO-001…096, then C1–C17, then uni task items not covered by a CO, then M1–M8, then any BOSS_CONCERNS #1–82 item not covered above, then the meeting rows S10-* / S29-*, then H1–H12.
## Part 2 — Open work summary (auto-derived from Part 1: counts by status, top 10 open by leverage)
## Appendix A — Status diary (the old file body, preserved verbatim, marked historical)
```
**DONE-VERIFIED rule:** a row can be DONE only if the Evidence column holds a command whose output reproduces the claim today. Verdict re-runs every DONE row's command.

## Miss subagent — TASK (paste after the shared context block)
> Rebuild `BOSS_CONCERNS.md` exactly per memory proto-66 (layout, statuses, sources, overclaims list). Transcribe concerns verbatim. For every row, check disk and set
> status + evidence + the protocol that owns it (use memory `proto-99-concern-crosswalk` for the mapping). Never mark DONE without a reproducing command.
> Confirm the proto-98 Phase 0 snapshot exists (take it if not). Write only `BOSS_CONCERNS.md`.

## Verdict check
Re-run every DONE-VERIFIED evidence command; sample 15 other rows; confirm no concern from sources 1–5 is missing (count rows per source).

Related: [[proto-99-concern-crosswalk]], [[proto-91-verdict-cross-check]], [[boss-standard]]
