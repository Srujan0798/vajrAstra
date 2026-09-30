# ralph_wiggum_001 (converted from ralph_wiggum_001.jsonl - all records, fields verbatim)

## Record 1 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 5
- **extraction**:

  Ralph Wiggum (Geoffrey Huntley's continuous agent loop): 'A dumb bash loop that keeps restarting the agent, and the agent figures out what to do next by reading the plan file each time.' Three phases: 1) Define Requirements (JTBD → specs), 2) PLANNING mode (gap analysis → IMPLEMENTATION_PLAN.md), 3) BUILDING mode (implement → test → commit → update plan). Core loop: cat PROMPT.md | claude -p --dangerously-skip-permissions --output-format=stream-json --model opus --verbose. IMPLEMENTATION_PLAN.md persists on disk as shared state between isolated iterations. AGENTS.md = operational guide (build/test commands). specs/ = requirements (one per JTBD topic).
- **decision_it_changes**: Whether to adopt Ralph's loop architecture for our Level-7 campaign execution — specifically the PLANNING/BUILDING mode separation, disk-persisted plan, and bash-loop orchestration for Engine agent.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Pure bash + Claude CLI — fully local, zero deps.

## Record 2 (from ralph_wiggum_001.jsonl)
- **source_url**: https://ghuntley.com/ralph/
- **date**: 2025-12-30
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 3
- **actionability**: 5
- **extraction**:

  Geoffrey Huntley's original Ralph post: 'Bash loop, PRD, let the agent run overnight.' Key principles: Context is everything (tight tasks + 1 task per loop = 100% smart zone utilization). Use main agent as scheduler, subagents as memory extension (each gets ~156KB garbage-collected). Simplicity and brevity win. Prefer Markdown over JSON. Steer upstream (deterministic setup, existing code patterns) and downstream (backpressure via tests/typechecks/lints). Let Ralph Ralph (trust eventual consistency). Use protection (sandbox, minimal keys). Move outside the loop (observe, tune, don't prescribe).
- **decision_it_changes**: Whether to adopt Ralph's context discipline (1 task per loop, subagents for memory extension) for our Engine agent's build loops, and backpressure philosophy for Verdict's verification gates.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Principles are architecture-agnostic; sandbox is local Docker/Fly/E2B.

## Record 3 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/files/loop.sh
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 5
- **extraction**:

  Enhanced loop.sh: Supports plan/build modes, max-iterations, git push per iteration. Uses PROMPT_plan.md (gap analysis → plan) vs PROMPT_build.md (implement from plan). Flags: -p (headless), --dangerously-skip-permissions (YOLO), --output-format=stream-json, --model opus (or sonnet for speed), --verbose. Streamed variant pipes through parse_stream.js for readable output. Max-iterations limits task selection loop (not tool calls within task).
- **decision_it_changes**: Whether to use this exact loop.sh as Engine agent's orchestration script, with plan/build mode switching for our campaign phases.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Pure bash script — no external deps.

## Record 4 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/PROMPT_build.md
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 5
- **extraction**:

  PROMPT_build.md template: Phase 0 (orient: study specs, plan, src/lib), Phase 1-4 (task selection, implement with up to 500 Sonnet subagents for search, 1 Sonnet subagent for build/tests, Opus for complex reasoning), validation (run tests, update plan, commit, push), guardrails (999... numbering: capture the why, single source of truth, git tags, debug logging, keep plan current, resolve bugs, no placeholders, clean completed items, fix spec inconsistencies, AGENTS.md operational only). Key phrase: 'don't assume not implemented' — the Achilles' heel.
- **decision_it_changes**: Whether to adopt this prompt template for Engine agent's BUILDING mode, especially the subagent allocation (500 Sonnet search, 1 Sonnet test, Opus reasoning) and guardrail hierarchy.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Prompt template is pure text — no deps.

## Record 5 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/PROMPT_plan.md
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 4
- **extraction**:

  PROMPT_plan.md template: Study specs (250 Sonnet subagents), study plan, study src/lib (250 Sonnet subagents), gap analysis with 500 Sonnet subagents + Opus analysis to create/update IMPLEMENTATION_PLAN.md as prioritized bullet list. Ultrathink. Search for TODO, minimal impls, placeholders, flaky tests, inconsistent patterns. Plan only — no implementation. 'IMPORTANT: Do NOT assume functionality is missing; confirm with code search first.' Treat src/lib as standard library.
- **decision_it_changes**: Whether to use this PLANNING mode prompt for our campaign's planning phases (pre-research, architecture decisions) before Engine builds.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Prompt template is pure text.

## Record 6 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Ralph enhancements (playbook): 1) AskUserQuestionTool for planning — systematic JTBD/edge case/acceptance criteria clarification before specs. 2) Acceptance-Driven Backpressure — derive test requirements from acceptance criteria in specs during planning, preventing 'cheating' (can't claim done without required tests). 3) Non-Deterministic Backpressure — LLM-as-judge for subjective criteria (tone, aesthetics, UX) with binary pass/fail, converges through iteration. 4) Ralph-Friendly Work Branches — scope at plan creation (plan-work mode) not task selection. 5) JTBD → Story Map → SLC Release. 6) Specs Audit. 7) Reverse Engineering Brownfield to Specs.
- **decision_it_changes**:

  Whether to adopt Acceptance-Driven Backpressure (deriving test requirements from specs) for our Verdict agent's verification specs, and Non-Deterministic Backpressure for subjective quality gates (e.g., CER threshold quality).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Enhancements are prompt/workflow patterns — no external deps.

## Record 7 (from ralph_wiggum_001.jsonl)
- **source_url**: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum
- **date**: 2026-01-08
- **status**: MEASURED
- **relevance**: 3
- **recency**: 3
- **actionability**: 3
- **extraction**:

  Ralph Wiggum is an official Claude Code plugin (anthropics/claude-plugins-official). Install: '/plugin install ralph-wiggum@ghuntley'. The plugin packages the loop.sh, prompts, and workflow. Referenced in Pulumi blog: 'How Ralph Wiggum built a serverless SaaS with Pulumi' — real production use case.
- **decision_it_changes**: Confirms Ralph is an official Anthropic plugin, not just a GitHub repo. Can be installed via native plugin system.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Plugin is local code.

## Record 8 (from ralph_wiggum_001.jsonl)
- **source_url**: https://x.com/GeoffreyHuntley/status/1944614322107564194
- **date**: 2025-07-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 2
- **actionability**: 2
- **extraction**:

  Geoffrey Huntley's tweet: Ralph Wiggum built CURSED programming language over 3 months (complete language). Boris Cherny's 30 days: 259 PRs using Ralph. Real-world validation of the loop architecture for substantial projects.
- **decision_it_changes**: Evidence that Ralph scales to multi-month, multi-PR projects — supports using it for our 48h campaign with Engine agent.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Social proof only — no technical dependency.
