---
name: proto-30-w3-skill-inventory
description: "Wave 3 part 1 (Miss + Verdict) — inventory every skill, plugin, MCP server and elite repo across Claude and OpenCode, map each to a concrete campaign step, prove use or write an idle reason (CO-075/094), output SKILL_STACK.md"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:15:54.836Z
---

# WAVE 3 · PART 1 — SKILL / TOOL INVENTORY → `docs/campaign/SKILL_STACK.md` (D10, sections 1–3)

**Why:** CO-075 "boss unable to see why/where all skills are used — map every skill to its use"; CO-094 "use all skills, plugins, repos". No tool sits idle without a written reason.
**Precursors:** `INTEGRATED-ELITE-STACK.md` (root, canonical map of paperthin, looper, graphify, ECC, GLM-OCR, mlx-tune, liteparse…), `ECC_VERIFICATION.md`, `PAPERTHIN_AUDIT.md`,
`LAYA_GATE_DECISIONS.md`.
**Writes only:** `docs/campaign/checkpoints/W3_reports/inventory.md` (subagent); the lead composes `SKILL_STACK.md`.

## Where things live (planner-verified 2026-09-29)
- Claude user skills: `~/.claude/skills/` (includes graphify). Plugin skills: `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/skills/` (superpowers, ecc 2.2.2, context7,
  feature-dev, pr-review-toolkit, semgrep, playwright, vercel, skill-creator, session-report, pydantic-ai, data-engineering, frontend-design, ralph-loop…).
  Enabled plugins list: `~/.claude/settings.json` → `enabledPlugins`.
- MCP servers: `claude mcp list` (2026-09-29: Claude Docs, Google Drive, Gmail, Calendar, Notion, context7, semgrep, playwright, omi-memory, opencode, github, ecc-memory connected;
  PostHog, Linear, Vercel need auth). ecc-memory was fixed 2026-09-29 (repointed to the plugin's `scripts/memory-mcp.mjs`) — not a finding.
- OpenCode: `~/.config/opencode/` (config.json, agents/, commands/, hooks/, instructions/, skills/ — 217 entries in `skills/`, incl. paperthin + looper).

## TASK block (paste after the shared context block)
> You are the Miss agent. Build the complete tool inventory with evidence of use.
> 1. Enumerate: every Claude skill (user + each enabled plugin's skills), every Claude plugin (enabled or not), every MCP server (with status), every OpenCode skill/agent/command,
>    every repo named in `INTEGRATED-ELITE-STACK.md`. Commands: `ls ~/.claude/skills`, `find ~/.claude/plugins/cache -maxdepth 5 -name SKILL.md | sed 's|/SKILL.md||'`,
>    `claude mcp list`, `ls ~/.config/opencode/skills | head -300`, `ls ~/.config/opencode/agents ~/.config/opencode/commands`.
> 2. For each item: name · source (Claude skill / plugin / MCP / OpenCode / repo) · what it does (from its SKILL.md or README first lines) · **campaign step it belongs to**
>    (use the step IDs: 1A–1H, W2, W3, W4, W5, or "none") · **evidence of use** (grep the repo and `DISPATCH_LOG.md`/feed for its name; cite file:line; for Claude skills also
>    grep `~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl` for `"skill":"<name>"` counts) · status USED / SHOULD-USE (name the step) / IRRELEVANT (reason) / BROKEN (error).
> 3. Group the 217 OpenCode skills by family rather than one row each if most are irrelevant; list individually only those that map to a step.
> 4. Output a table + a short list "top 10 tools we should be using and are not, with the exact step and how".
> Under 2,000 words (tables excluded).

## `SKILL_STACK.md` sections 1–3 (lead composes; section 4 comes from [[proto-31-w3-laya-jev-verdict]])
1. Summary: counts by status; the 10 highest-leverage unused tools with the step they plug into.
2. Per-step tool map: for each campaign step, which tools to use (e.g. 1A → verification-loop / mandela / factchk skills; 1D/1E → WebSearch + parallel-search + context7;
   W5 → graphify link/orphan queries; memory → ecc-memory + unified-memory). Only tools that exist in the inventory.
3. Full inventory table (or grouped), each row with status and reason.

## Verdict check
Sample 10 rows; confirm the "evidence of use" citations exist and IRRELEVANT reasons are real.

Related: [[proto-31-w3-laya-jev-verdict]], [[proto-00-runbook]]
