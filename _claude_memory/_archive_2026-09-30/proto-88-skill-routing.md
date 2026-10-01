---
name: proto-88-skill-routing
description: "Added 2026-09-30 — which skill, plugin or MCP every agent (Claude Code and OpenCode) must use for each kind of campaign work; pick the skill BEFORE starting the work and name it in the checkpoint line (CO-075/094, uni T7.1–T7.4)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T09:14:21.843Z
---

# PROTO-88 — SKILL ROUTING (standing; loaded via AGENTS.md start block for every agent)

Rule: before a step starts, find its kind of work below and load the listed skill (Claude Code: the Skill tool; OpenCode: its skill of that name). Record `skills used: …` in the step's checkpoint line.
A skill that does not fit the moment may be skipped — say why in one line. Names below were verified on this laptop on 2026-09-30 (`~/.claude/skills`, plugin skill list, `~/.config/opencode/skills`).

| Kind of work | Claude Code | OpenCode |
|---|---|---|
| Session start / back after a gap | `catchup` + this runbook | `codebase-onboarding` |
| Not sure what is next | `nba` | `plan-orchestrate` |
| Long, bundled or ambiguous request | `readchk` | `search-first` |
| Any factual claim (number, paper, date, rule) | `factchk` + WebSearch/WebFetch; library docs via `context7` MCP | `deep-research`, `research-ops`, `documentation-lookup`, `exa-search` |
| Designing or trusting an evaluation, benchmark or split | `mandela` | `benchmark-methodology`, `eval-harness` |
| Duplicates, one source of truth, file consolidation | `ssotize` | `living-docs-governance` |
| Repo map, orphans, concerns graph | `graphify` | `graphify` |
| A bug (empty engine output, scorer mismatch, crash) | `superpowers:systematic-debugging` | `agent-introspection-debugging` |
| Writing a script or tool | `superpowers:test-driven-development`, then `code-review` / `simplify` | `tdd-workflow` |
| Before saying "done" | `superpowers:verification-before-completion` | `verification-loop`, `delivery-gate` |
| Parallel batches of subagents (Sonnet only) | `superpowers:dispatching-parallel-agents` | `parallel-execution-optimizer` |
| Multi-LLM review of a plan | `opencode` MCP + a fresh reviewer subagent | `council-multi-model`, `council` |
| Research: frontier, competitors, papers | WebSearch (standard, then extended) + `factchk` | `deep-research`, `scientific-thinking-literature-review`, `market-research` |
| Gated actions: move, delete, download, unseal | the boss's approval in proto-92 (U29 deletion rule) — never a classifier | `gateguard` |
| File triage suggestions (advisory only) | Laya trial per proto-98 §Laya (U31), run in swa-erp's `.venv-laya`; never decides a fate, never deletes | same |
| Repo structure, islands, variant clusters | `graphify` (`/graphify … --update`, then `graph_signals.tsv` per proto-98) | `graphify` |
| Recurring monitoring | `loop`, `schedule` | `looper`, `continuous-agent-loop` |
| Memory across sessions | Claude auto-memory + `ecc-memory` MCP | `unified-memory` |
| Charts, docs, deck for Vinay | `dataviz`, `anthropic-skills:docs`, `anthropic-skills:pptx` | `investor-materials`, `article-writing` |
| Killer-objection / anti-slop pass on a document | `hate`, `sip` | `paperthin` |
| Secrets, scripts, security | `security-review` | `security-review` |
| Model tier and cost | `modelchk` | `context-budget`, `cost-tracking` |

Never: spawn a subagent on Opus (model tiering); use a skill as an excuse to skip the protocol's own checks.

Related: [[proto-00-runbook]], [[proto-30-w3-skill-inventory]], [[proto-01-law-and-guardrails]]
