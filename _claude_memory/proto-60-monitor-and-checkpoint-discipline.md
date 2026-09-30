---
name: proto-60-monitor-and-checkpoint-discipline
description: "Added 2026-09-30 by Opus monitor — mandatory checkpoint updates after every step (agents skipped them all night), how the lead reconciles a stale checkpoint from disk, and how the Opus monitor audits executing agents"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:04.218Z
---

# PROTO-60 — CHECKPOINT DISCIPLINE AND MONITORING (added 2026-09-30 03:25 IST)

**Why:** between 09-29 21:00 and 09-30 03:10 the executing agents produced 1A–1E and most of 1F/1G, but `docs/campaign/checkpoints/W1.md` was never updated
(last write 20:58, all steps unchecked, "STOPPED"). A fresh session following [[proto-02-preflight-and-checkpoints]] would redo finished work. Monitor report:
`docs/campaign/checkpoints/MONITOR_2026-09-30.md`.

## Rule 1 — the checkpoint is written after EVERY step, before the next dispatch
Tick the step line with output path, verdict (PASS / PASS-WITH-FIXES / FAIL), verifier, and one evidence line. No tick = the step did not happen.

## Rule 1b — NEXT.md (added 2026-09-30)
`docs/campaign/checkpoints/NEXT.md` holds the ONE next step for any agent; the SessionStart hook prints it. Whoever finishes a step rewrites NEXT.md (what is next, which protocol) in the same turn.

## Rule 2 — reconcile a stale checkpoint from disk (do this NOW for W1)
1. For each step, check its output file exists and its mtime (`stat -f '%Sm %z %N' -t '%m-%d %H:%M' <file>`).
2. Output exists + a verify report exists → tick as DONE with both paths. Output exists, no verify → tick as `DRAFT (unverified)` and run [[proto-91-verdict-cross-check]].
3. Replace the "STOPPED" footer with `RESUMED <time> by <agent>`; keep the history lines (append, don't erase).
State on 2026-09-30 03:25 (monitor-measured): 1A DONE · 1B DONE (7 UNRESOLVED) · 1C DONE · 1D DONE · 1E DONE (0 survivors) · 1F IN PROGRESS (no MULTI_LLM_EVAL.md) ·
1G PARTIAL (round 1 54/54 PASS, 1 defect introduced by FS-50, 39 round-2 specs; packet re-edited 09-30 01:33; round-2 verify NOT on disk) · 1H NOT STARTED.

## Rule 3 — one executing lead at a time per wave
Before dispatching, list running agents (`ps aux | grep -E 'claude|opencode' | grep -v grep`) and the last 10 DISPATCH_LOG lines. If another lead is working the same wave,
write `LEAD-CONFLICT` in the checkpoint and ask the boss which one continues.

## Rule 4 — no file moves, copies or duplicates during a wave
Cleanup/reorganisation is Wave 5 work ([[proto-63-single-canonical-files]]). Copies made "for discoverability" are duplicates; use a pointer line instead.

## How the Opus monitor audits (for future monitor passes)
Read-only: (1) mtimes of every deliverable vs checkpoint ticks; (2) grep deliverables for known-false patterns (proto-93); (3) re-derive 3 headline numbers per
deliverable; (4) check sealed counts + locked mtimes; (5) look for new untracked trees (`git status --short | grep '^??'`); (6) write `MONITOR_<date>.md` and new
protocols; never edit deliverables, never spawn subagents.

Related: [[proto-00-runbook]], [[proto-02-preflight-and-checkpoints]], [[proto-91-verdict-cross-check]]
