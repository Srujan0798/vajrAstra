---
name: proto-02-preflight-and-checkpoints
description: "Pre-flight checks the lead runs before every wave (concurrent agents, dispatch log, git state, sealed-dir counts) and the checkpoint-file scheme that lets any fresh session resume mid-wave"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:09:20.692Z
---

# PRE-FLIGHT AND CHECKPOINTS

## Pre-flight (run at the start of every session and every wave; paste outputs into the checkpoint)
```bash
cd /Users/srujansai/Desktop/South
date '+%Y-%m-%d %a %H:%M IST'
# 1. Who else is running? (two OpenCode agents were live on 2026-09-29)
ps aux | grep -E 'claude|opencode' | grep -v grep | awk '{print $2, $9, substr($0, index($0,$11), 110)}'
# 2. What did other agents just do?
tail -30 DISPATCH_LOG.md | cut -c1-300
# 3. Working tree
git status --short | head -40
# 4. Sealed-dir counts (must match; any change = stop and report)
for d in level2/out level2/reports level2/probe22/out arc_level_1; do printf "%-24s %s\n" $d "$(find $d -type f | wc -l | tr -d ' ')"; done
# 5. Locked files unchanged since the planner's read
stat -f '%Sm %N' -t '%Y-%m-%d %H:%M' level2/probe22/manifest.json level2/probe22/sheet.csv level2/probe22/AGENT_PROTOCOL.md
```
Reference values at planning time (2026-09-29): manifest.json mtime 2026-09-29 02:45; sealed counts per feed §17: `level2/out/` 4,001 · `level2/reports/` 48 ·
`level2/probe22/out/` 13,289 · `arc_level_1/` 413. If a sealed count differs from the previous checkpoint, STOP and report — do not "fix" it.

**Concurrency rule:** if `ps` shows OpenCode or another Claude session and `DISPATCH_LOG.md`/`git status` shows them editing a file your step will edit
(e.g. `VINAY_MEETING_PACKET.md`), do not edit it. Tell the boss in one line and continue with steps that touch other files.

## Checkpoint scheme
- Folder: `docs/campaign/checkpoints/` (create on first use: `mkdir -p docs/campaign/checkpoints`).
- One file per wave: `W1.md`, `W2.md`, … Template in [[proto-90-templates]].
- Each step has one line: `- [ ] 1A packet audit` → `- [x] 1A DONE 2026-09-29 23:10 — fix_specs/W1A_PACKET_AUDIT.md (42 specs) — verified by <subagent id>`.
- A step in progress records its last completed sub-step, so a fresh session resumes mid-step: `1E-refute: candidates C1,C2 refuted; C3 in progress (lens b done)`.
- Subagent raw reports that the lead needs later go into `docs/campaign/checkpoints/W<n>_reports/<step>.md` (evidence trail; not deliverables).
- The wave file ends with `STATUS: COMPLETE` only when every step is DONE and verified.

## Resume logic for a fresh session
1. `ls docs/campaign/checkpoints/` → first `W<n>.md` without `STATUS: COMPLETE` is the current wave; if none exist, current = W1.
2. Inside it, the first unchecked step is next. If a step shows partial progress, resume from its last sub-step; do not redo finished sub-steps.
3. Re-run pre-flight before continuing.

Related: [[proto-00-runbook]], [[proto-90-templates]], [[proto-01-law-and-guardrails]]
