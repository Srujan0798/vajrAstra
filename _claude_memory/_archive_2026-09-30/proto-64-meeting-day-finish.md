---
name: proto-64-meeting-day-finish
description: "Added 2026-09-30 — time-boxed finish plan for the Vinay meeting TODAY: exact order (reconcile checkpoint → single packet → GT-tier line → 1G round-2 verify → 1F → 1H with the new findings → boss brief), what goes into the draft plan now, what is cut"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:24.659Z
---

# PROTO-64 — MEETING-DAY FINISH (Wed 2026-09-30; supersedes the ordering of proto-10 for the remaining steps)

## ADDED 2026-09-30 ~05:00 — first do [[proto-86-draft-plan-fixes]] (13 defects in DRAFT_RESEARCH_PLAN.md incl. the Punjabi K1 correction and the GT-tier table). Deadline guard (law L12/D12): no new scope within 4 h of the meeting — Wave 2 work started at 03:30 (manifest_22.json) is paused until after the meeting; do not delete it.

## Order (do not reorder; each ≤ the stated time)
1. **Reconcile `W1.md`** from disk ([[proto-60-monitor-and-checkpoint-discipline]] Rule 2) — 10 min.
2. **One packet** ([[proto-63-single-canonical-files]] row 1) — 10 min.
3. **1G round 2:** apply the 39 round-2 specs if not yet applied (the packet was re-edited 09-30 01:33 — first check which R2 specs are already in: count OLD/NEW occurrences),
   then a fresh Verdict re-verify per [[proto-18-w1g-apply-verify]]; include the FS-50 self-contradiction and the ur/“10 independent”/0.2400/1,257 corrections — 40 min.
4. **GT-tier line** ([[proto-62-gt-tier-stratified-reporting]] rule 2) into the packet via fix-spec — 10 min. (The full Engine task of proto-62 runs after the meeting unless time allows.)
5. **1F** finish: OpenCode evaluator + fresh Sonnet reviewer; ChatGPT leg = ask the boss now, mark PENDING if not back — 30 min.
6. **1H `DRAFT_RESEARCH_PLAN.md`** per [[proto-19-w1h-draft-research-plan]], with these mandatory additions:
   - §3 uses the GT-tier table, not the pooled 10/18.
   - §3 states South scored n (126/400; kn/ml ≈4) and that "22 languages" holds for labelled data only.
   - §3 carries the sheet.csv note from [[proto-61-sheet-provenance-forensics]] ("CER as stored; independent re-derivation in progress").
   - §6 says plainly: 4 edge candidates tested, 0 survived; the one measured fact is a coverage gap (no local engine emits Ol Chiki / Meetei Mayek); the fix is a small
     Tesseract model download awaiting approval (U7).
   - §4/§1 use 1D's comparability table: 87.39 = word accuracy 100×(1−WER), macro over 22 languages, n=6,609, English excluded, Sarvam's own human-reviewed bench;
     Bodhan's bench flips 8/22 per-language winners → vendor benches disagree; no CER of ours is comparable to 87.39.
   - §8 questions add U6 (reopen §6.4 for mni/sat now that bench GT is human-reviewed), U7 (download), U8 (the `src/`+`tests/` build), U9 (adopt sheet_v2 if proto-61 changes numbers).
   — 60 min.
7. **Verdict cross-check** of the draft plan ([[proto-91-verdict-cross-check]]) — 20 min.
8. **Boss brief** (≤10 lines, [[proto-90-templates]] §7) + the U-questions ([[proto-92-boss-decisions]]) + ChatGPT paste request.

## Cut-order if time runs out
Keep 1, 2, 3, 4, 6, 8. Cut 5 to "OpenCode leg only" before cutting anything else. Never cut the GT-tier line or the sheet.csv note.

## After the meeting (queue)
proto-61 forensic rebuild → proto-62 full analysis → proto-65 GT-defects register → Wave 2 (proto-20/21) → proto-63 remaining rows → Waves 3–5.

Related: [[proto-10-w1-overview]], [[proto-19-w1h-draft-research-plan]], [[proto-61-sheet-provenance-forensics]], [[proto-62-gt-tier-stratified-reporting]]
