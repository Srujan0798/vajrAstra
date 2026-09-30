---
name: agent-automation-setup
description: How the South repo makes every agent start from the plan and use skills without the boss pasting prompts (set 2026-09-30) — AGENTS.md START HERE block, SessionStart/Stop hooks running scripts/agent_bootstrap.sh, NEXT.md, ECC plugin enabled, global rules for OpenCode and Claude
metadata:
  type: reference
---

Set 2026-09-30 after the boss said: "I can't push every time… set it so all agents use all skills and plugins every time."

- **Anchor every tool loads:** repo `AGENTS.md` starts with a "START HERE" block (Claude Code, OpenCode and Cursor all auto-load AGENTS.md; OpenCode v2 ignores the `instructions` config key — context7, 2026-09-30).
- **Claude Code hooks** in `.claude/settings.local.json`: SessionStart (startup|resume|clear|compact) runs `bash scripts/agent_bootstrap.sh` → prints NEXT step, checkpoint STATUS, open U-decisions, live agent count, graph staleness, rules, skill hints; Stop runs `--sync-only` → copies memory `proto-*.md` into `docs/campaign/protocols/` (memory is the source of truth).
- **NEXT.md** at `docs/campaign/checkpoints/NEXT.md` = the one next step; whoever finishes a step rewrites it ([[proto-60-monitor-and-checkpoint-discipline]] Rule 1b).
- **Skills:** [[proto-88-skill-routing]] maps each kind of work to a Claude skill and an OpenCode skill. The ECC plugin (`ecc@ecc`, 292 skills) was installed but DISABLED in Claude Code; enabled 2026-09-30 (user scope) — takes effect in new sessions.
- **Laptop-wide:** `~/.config/opencode/AGENTS.md` (new, generic skill discipline) and a "Skill discipline (all projects)" block appended to `~/.claude/CLAUDE.md` (backup of the old file in that session's scratchpad).
- **To change the next step** edit NEXT.md; to change the automation edit the script or run `/hooks`.

Related: [[proto-00-runbook]], [[proto-88-skill-routing]], [[sonnet-handoff]]
