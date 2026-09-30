---
name: proto-79-council-briefing-prompts
description: "Added 2026-09-30 — uni T7.2(e) briefing format DECISIONS|DELIVERED|BLOCKERS|RISKS|NEXT, T7.4 prompt maintenance (rewrite a prompt when an agent re-asks), T7.5 council deliberation for load-bearing docs, CO-026/027/028/037 — how agents report and how prompts self-correct"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:53.865Z
---

# PROTO-79 — COUNCIL, BRIEFING FORMAT, PROMPT MAINTENANCE (all agents, standing)

## 1. Briefing format (uni T7.2e; CO-026 Verdict must stop asking "what next")
Every report to the boss or the lead: a table with exactly these rows — **DECISIONS** (made, with reason) · **DELIVERED** (files, with verification) · **BLOCKERS** (only boss-level, each with a
recommendation) · **RISKS** · **NEXT** (what the agent does next without asking). ≤2,000 tokens, file:line refs. The ≤10-line boss report in [[proto-90-templates]] §7 is this table compressed.
Never end with "what should I do?" — end with NEXT (uni R0.10, CO-063).

## 2. Prompt maintenance (uni T7.4; CO-037 "fix the flow so improvement requests stop coming back as our fault")
If a subagent re-asks, misreads, or returns off-scope work twice: the lead rewrites that step's protocol file (memory + `docs/campaign/protocols/` mirror) with the missing instruction,
records `PROMPT-FIX: <step> — <what was missing>` in the checkpoint, and re-dispatches. Relaying the confusion upward unchanged is a failure.

## 3. Council deliberation (uni T7.5; CO-081 "deliberate like a council")
For load-bearing documents — `DRAFT_RESEARCH_PLAN.md`, `EDGE_THESIS.md`, `ARCHITECTURE_FREEZE.md`, `BOSS_CONCERNS.md` rebuild, level2 `MOVE_PLAN.md`, any §6.4 reopening:
three independent Sonnet reviewers (lenses: evidence/truth · feasibility/time · boss-concern coverage), each blind to the others; the lead writes a synthesis listing agreements, disagreements and
the resolution with reasons, appended to the document's checkpoint report. A disagreement the lead cannot resolve by evidence goes to the boss with a recommendation.

## 4. Verdict autonomy (CO-027/028)
Verdict acts within scope without asking, counters the boss with evidence when a directive is wrong, and its recommendations are adopted by default unless they need boss authority (uni T7.3).

Related: [[proto-91-verdict-cross-check]], [[proto-90-templates]], [[proto-60-monitor-and-checkpoint-discipline]]
