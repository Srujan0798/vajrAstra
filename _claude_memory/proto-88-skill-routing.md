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

## STATUS 2026-09-30 (planner, night) — what is installed and in use
- **graphify: USED, but stale.**
  - The package and skills are 0.9.65 for Claude, OpenCode and agents.
  - `graphify-out/graph.json` is still the 14:34 build (6,796 nodes; backup `graph.pre-update.json` in the planner scratchpad). `graphify update .` was started and stopped.
  - Owner: Agent 2 runs `graphify update .` once, after LAYOUT FROZEN and after AGENTS.md/INDEX/README are applied. Then `graphify query "<question>"` for navigation, and GRAPH_REPORT islands/orphans for the hierarchy.
- **ECC: USED**, with one skill per step:
  - OpenCode (217 skills): `verification-loop` before every PASS/"done"; `council-multi-model` for Gate 2.5; `deep-research` for the proto-105 papers; `benchmark-methodology` + `eval-harness` for steps X, S5 and H2; `gateguard` before any move/delete; `unified-memory` for handoffs; `paperthin` on the Plan v3 draft; `looper` for night runs.
  - Claude: the ECC plugin + the `ecc-memory` MCP.
- **Laya: NOT used** in the OCR pipeline (text-only classifier, cannot read images; U30, formerly proto-31). The file-triage trial (U31) is parked with the cleanup.
- **Consensus.app: USED**, 3 Deep Searches per day. Results are stored in `docs/sources/consensus/` → proto-105 (Agent 2, not yet processed).
- **Python environments** (R-14):
  - `.venv311` (Python 3.11.10: torch, transformers, surya, paddleocr, easyocr, pytesseract, datasets, jiwer, pandas, pyarrow, fitz, mlx 0.32.3, mlx-vlm 0.7.4) = THE env for engines, scoring, bench and data prep.
  - `.venv` (Python 3.14.3) = only what already runs there. It is never mixed into a result without saying so.
  - `product/` gets its own pinned requirements + a Linux/CUDA Dockerfile (D4).
- **MCPs:** `hf-mcp-server` (U26; the HF account is Maya0769; Bodhan repos 403 until the access forms are submitted), `context7`, `github` (read-only use), `opencode`, `ecc-memory`.
- **Cloud planner sessions** (claude.ai/code, e.g. the vajrAstra session):
  - They cannot see the Mac or its local skills (readchk/factchk/mandela/ssotize/graphify), so they do those checks by hand and say so.
  - They read the repo only through a branch the boss pushes (`boss/campaign-docs`, one-off, docs only).


## (verbatim from agent-automation-setup, merged 2026-09-30 night)

Set 2026-09-30 after the boss said: "I can't push every time… set it so all agents use all skills and plugins every time."

- **Anchor every tool loads:** repo `AGENTS.md` starts with a "START HERE" block (Claude Code, OpenCode and Cursor all auto-load AGENTS.md; OpenCode v2 ignores the `instructions` config key — context7, 2026-09-30).
- **Claude Code hooks** in `.claude/settings.local.json`: SessionStart (startup|resume|clear|compact) runs `bash scripts/agent_bootstrap.sh` → prints NEXT step, checkpoint STATUS, open U-decisions, live agent count, graph staleness, rules, skill hints; Stop runs `--sync-only` → copies memory `proto-*.md` into `docs/campaign/protocols/` (memory is the source of truth).
- **NEXT.md** at `docs/campaign/checkpoints/NEXT.md` = the one next step; whoever finishes a step rewrites it ([[proto-60-monitor-and-checkpoint-discipline]] Rule 1b).
- **Skills:** [[proto-88-skill-routing]] maps each kind of work to a Claude skill and an OpenCode skill. The ECC plugin (`ecc@ecc`, 292 skills) was installed but DISABLED in Claude Code; enabled 2026-09-30 (user scope) — takes effect in new sessions.
- **Laptop-wide:** `~/.config/opencode/AGENTS.md` (new, generic skill discipline) and a "Skill discipline (all projects)" block appended to `~/.claude/CLAUDE.md` (backup of the old file in that session's scratchpad).
- **To change the next step** edit NEXT.md; to change the automation edit the script or run `/hooks`.

Related: [[proto-00-runbook]], [[proto-88-skill-routing]], [[sonnet-handoff]]
