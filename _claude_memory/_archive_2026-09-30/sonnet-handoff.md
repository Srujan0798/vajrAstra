---
name: sonnet-handoff
description: "START HERE when the boss says \"read your memory and continue\" — the Opus-written execution protocol is the proto-00…proto-93 files in this memory folder (entry proto-00-runbook), backed by docs/campaign/CAMPAIGN_DIRECTIVE.md v5; Sonnet executes wave by wave with Sonnet subagents"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:18:43.070Z
---

**If you are Sonnet and the boss said "read your memory and continue" (or similar): this is your task.**

The Opus planner (2026-09-29, max effort) read the repo, measured the state on disk and wrote every task as a detailed protocol file in this memory folder.
**Open [[proto-00-runbook]] now and follow it exactly.** It tells you what to read (proto-01 law, proto-02 pre-flight, proto-90 templates), how to find the next
step from `docs/campaign/checkpoints/`, and which protocol file each step uses. Each protocol file is self-contained: sources, commands, full subagent prompts,
output layout, acceptance checks.

Repo law summary: `docs/campaign/CAMPAIGN_DIRECTIVE.md` v5 (Part A = verified state; Part S = start point + boss decisions U1–U5).

**First run starts at Wave 1** (the gate for the boss's meeting with Vinay on Wed 2026-09-30): audit and correct `VINAY_MEETING_PACKET.md`, build the 22-language
benchmark table, mentor playbook, competitor intel, edge thesis, multi-LLM evaluation and the draft research plan the boss presents.

**Never:** spawn a subagent on Opus (every Agent call `model: "sonnet"`), train, download, call Sarvam (cap spent), touch sealed dirs or locked files,
run/delete the untracked `src/` tree, resume an old or backgrounded session (that caused the 2026-09-29 "exit code 1").

**Why:** the boss's division of labour — Opus plans deeply once, Sonnet executes cheaply and deeply ([[model-tiering]]).

**How to apply:** if a protocol and disk disagree, follow the evidence and log a PROTOCOL-DEVIATION in the checkpoint. If a U-decision blocks a step, ask it with the
recommendation ([[proto-92-boss-decisions]]) and continue other steps.

Related: [[proto-00-runbook]], [[campaign-state]], [[open-front]], [[conflicts-register]], [[model-tiering]]
