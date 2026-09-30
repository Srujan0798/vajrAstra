---
name: proto-18-w1g-apply-verify
description: "Step 1G (Miss applies, Verdict verifies) — safe application of the 1A fix-specs to the meeting documents: concurrency check, pre-image archive, exact-string edits, per-spec verification, max 2 rounds, logs"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:14:18.213Z
---

# STEP 1G — APPLY FIX-SPECS AND RE-VERIFY (Miss subagent applies · Verdict subagent verifies)

**Input:** `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` (from [[proto-11-w1a-packet-audit]]), accepted by the lead.
**Law:** Verdict specifies, Miss applies, Verdict re-verifies (fix loop max 2 rounds, then escalate). Sealed/locked files never edited (errata only).

## Before applying (lead)
1. Concurrency: the OpenCode agents edited `VINAY_MEETING_PACKET.md` at 20:08 IST on 2026-09-29. Run pre-flight ([[proto-02-preflight-and-checkpoints]]) and
   `stat -f '%Sm' -t '%H:%M' VINAY_MEETING_PACKET.md EVIDENCE_SUMMARY.md`. If a file changed after 1A read it, send 1A's specs for that file back to Verdict for a
   re-check against the new text (round 1 of 2) before applying.
2. Pre-images (R0.6): `mkdir -p _archive/pre_fix_2026-09-29 && cp -p VINAY_MEETING_PACKET.md EVIDENCE_SUMMARY.md <every other target file> _archive/pre_fix_2026-09-29/`.
   Record sha256 of each pre-image in the checkpoint (`shasum -a 256`).

## Miss subagent — TASK block (paste after the shared context block)
> Apply the fix-specs in `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md`, BLOCKER first, then MAJOR, then MINOR. For each spec FS-nn:
> 1. Confirm the old text occurs exactly once in the target file (python `count`). If 0 or >1, do NOT improvise — mark `NOT-APPLIED: old text count=N` and move on.
> 2. Replace with the exact new text (Edit tool, exact string). Change nothing else. No reformatting, no "while I'm here" edits.
> 3. Log a row: `FS-nn | file | APPLIED / NOT-APPLIED | reason`.
> You may edit only the files named as targets in the fix-specs, and never: `AGENT_PROTOCOL.md`, `manifest.json`, `sheet.csv`, `run_probe.py`, sealed dirs.
> Additionally prepend to `VINAY_MEETING_PACKET.md` (below its title) one line: `> Corrected 2026-09-29 per fix_specs/W1A_PACKET_AUDIT.md — every number states its set and n. Draft research plan: docs/campaign/DRAFT_RESEARCH_PLAN.md`.
> Return the log table.

## Verdict subagent — TASK block (a different subagent from 1A's author)
> For each APPLIED spec: (1) the new text is present exactly once; (2) the old text is gone; (3) the diff against the pre-image in `_archive/pre_fix_2026-09-29/` touches only
> the spec's lines (`diff <(cat PRE) <(cat NEW)` — list any hunk not explained by a spec as COLLATERAL); (4) re-run the spec's evidence command — the new text is true.
> For NOT-APPLIED specs: propose a corrected old/new pair against the current text (this is round 2).
> Finally grep the corrected files for the known false patterns and report counts (all must be 0 unless the sentence now carries n and "directional"):
> `grep -n -E 'Beats Sarvam on 9/18|beats Sarvam on 9/18|Tue 2026-09-30|Sat 2026-10-04' VINAY_MEETING_PACKET.md EVIDENCE_SUMMARY.md`.
> Return PASS/FAIL per spec and the grep counts.

## Close-out (lead)
- Round 2 only for FAIL/NOT-APPLIED; after round 2, remaining items go to the boss in the wave report as "not fixed, here is why".
- Append the apply log + verify table to `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` under `## APPLY LOG (1G)`.
- Append one line to `OCR_AGENT_MEMORY_FEED.md` §11 log: date, "W1 packet audit applied: N specs, M verified, K open", pointer to the fix-spec file.
- Checkpoint: 1G DONE with counts.

Related: [[proto-11-w1a-packet-audit]], [[proto-91-verdict-cross-check]], [[proto-02-preflight-and-checkpoints]]
