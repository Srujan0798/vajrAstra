---
name: proto-76-workstreams-and-agent-health
description: "Added 2026-09-30 — uni T8.1/T8.5 + C15 (\"check both parallel tracks\", \"silence from a stream = flagged event\"): discover every agent/workstream touching the repo (OpenCode sessions, Claude sessions, Kilo worktrees, background jobs), what each is doing, stalled or conflicting, and register them in WORKSTREAMS.md"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:23.931Z
---

# PROTO-76 — WORKSTREAMS AND AGENT HEALTH (Miss, read-only) → `docs/campaign/WORKSTREAMS.md`

**Boss:** uni T8.1 "Every stream checked every cycle. Silence from a stream = flagged event, not peace." T8.5 "Find the boss's other parallel workstreams, read their concern docs, confirm none
stalled." C15 "you have 2 parallel works — see one you have done, what about the other." Monitor 2026-09-30: 3 OpenCode processes (since 07:29, 18:56, 21:02 on 09-29), Claude daemon sessions,
`.kilo/worktrees` (31 MB), untracked `src/`+`tests/` written by an unknown agent, a cleanup agent that moved 27 docs, and duplicates created "for discoverability".

## Miss subagent — TASK (paste after the shared context block)
> 1. Processes: `ps aux | grep -E 'claude|opencode|kilo|python' | grep -v grep` (start time, command, cwd via `lsof -p <pid> | grep cwd`).
> 2. OpenCode sessions (read-only MCP): ToolSearch `select:mcp__opencode__opencode_sessions_overview,mcp__opencode__opencode_session_list,mcp__opencode__opencode_session_get`;
>    list sessions for this repo, their titles/last activity; summarise what each is doing (do not send them messages).
> 3. Claude sessions: `ls -t ~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl | head` → title (ai-title rows) + last timestamp (small python, never cat).
> 4. Kilo: `git worktree list`; for each `.kilo/worktrees/*` branch, last commit date and whether it has unmerged changes.
> 5. Attribution: for files created/modified in the last 48 h outside `docs/campaign/`, attribute to a workstream (timestamps vs session activity; DISPATCH_LOG entries).
> 6. Write `docs/campaign/WORKSTREAMS.md`: table `workstream · tool · started · last activity · task (from its own log/title) · files it writes · status ACTIVE / IDLE / STALLED / CONFLICTING ·
>    owner lane (Engine/Verdict/Miss/boss) · action needed`. Flag every CONFLICTING pair (two streams writing the same files) and every STALLED stream.

## Standing rule (add to every wave's pre-flight)
Every workstream registers in `DISPATCH_LOG.md` before it writes (who, what files, until when). Unregistered writers are reported to the boss the same turn.

Related: [[proto-60-monitor-and-checkpoint-discipline]], [[proto-74-root-hidden-hygiene]], [[proto-02-preflight-and-checkpoints]]
