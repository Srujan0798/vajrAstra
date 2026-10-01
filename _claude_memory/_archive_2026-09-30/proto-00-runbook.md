---
name: proto-00-runbook
description: "READ FIRST (rewritten 2026-09-30 ~22:15 IST after the memory consolidation) — the read order for every agent and the planner, and where every old protocol number now lives (74 memory files merged into ~18); the old runbook is archived"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
---

# PROTO-00 — READ ORDER + WHERE EVERYTHING LIVES (rewritten 2026-09-30 night)

## Read order (every agent, every session)
1. `AGENTS.md` start block, then run `bash scripts/agent_bootstrap.sh` (it prints NEXT.md and syncs these files into `docs/campaign/protocols/`).
2. **proto-104 — THE PLAN** (rev 4 section at the top): goal, measured facts, rulings R-1…R-15, the steps with owners, the paste lines. Appendix A holds the step details.
3. **proto-01 — the law**: forbidden actions, evidence tags, rules 17–21, checkpoints, the 3-agent model, templates, the cross-check.
4. **proto-88 — tools**: which skill/plugin/MCP for which work; what is installed and in use; Python envs.
5. **Concerns**: `BOSS_CONCERNS.md` Part 0 (repo) = proto-99 §0 — the merged, verified concern themes.
6. **Meetings**: proto-103 §0 — every meeting and lead message in one place, then the Sep 29 verbatim table.
7. Only for your step: proto-89 (Plan v3 technical: Bodhan §A–§C), proto-100 (build queue B-01…B-21), proto-105 (Consensus → decisions), proto-97 (research questions + status), proto-102 (incident repair R), proto-92 (boss decisions + settled conflicts), proto-93 (measured facts with commands).

Where two documents disagree, the later-dated boss ruling in proto-104 wins. The planner fixes the loser.

## Where every old protocol now lives
- **proto-01 (law):** proto-01, 02, 60, 62, 79, 90, 91, campaign-law
- **proto-88 (tools):** proto-88, agent-automation-setup; the Laya ruling (formerly proto-31) is summarised there
- **proto-92 (decisions):** proto-92, conflicts-register
- **proto-104 (THE plan):** Appendix A holds proto-65 (step Q), 71 (S), 75 (G), 76 (planner monitoring), 78 (D4), 80 (S5/X scoring), 81 (§H), 82 (X coverage matrix)
- **proto-98 (the cleanup master, PARKED until the boss says "resume cleanup"):** proto-50, 63, 70, 72, 73, 74, 77, 84, 95, 96, 98, 101
- **history-completed-protocols (done, superseded or stale, each with a verified status):** proto-10…19, 20, 21, 30, 31, 40, 51, 61, 64, 66, 83, 86, 87, 94, campaign-state, open-front, sonnet-handoff
- **boss-rules (how the boss wants the work done):** boss-standard, model-tiering, feedback-no-subagents-boss-assigns, feedback-no-team-mates
- **Unchanged homes:** proto-89, 93, 97, 99, 100, 102, 103, 104, 105, user-profile

Originals are moved (never deleted) to the memory folder `_archive_2026-09-30/`. The repo mirror's stale copies go to `docs/campaign/protocols/_archive_2026-09-30/`.

## Who does what
- **The boss** assigns every task. His three OpenCode agents do the labour:
  - Agent 1 = Engine (`ses_f12a7b89…`)
  - Agent 2 = Verdict + repair lead (`ses_f1233a0a…`)
  - Agent 3 = Miss/builder (`ses_f16bc20e…`)
- **The planner** (Claude Code, Opus) writes the protocols, checks state from disk, and gives one-line paste lines. It uses subagents only when the boss explicitly asks (Sonnet only) — see boss-rules.
