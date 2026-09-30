# ralph_wiggum_002 (converted from ralph_wiggum_002.jsonl - all records, fields verbatim)

## Record 1 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/files/PROMPT_plan_work.md
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: direct
- **extraction**:

  Ralph plan-work mode (from playbook enhancements): Creates scoped IMPLEMENTATION_PLAN.md on work branch. User creates branch, runs './loop.sh plan-work "work description"', LLM uses description to scope plan. Post-planning, Ralph builds from already-scoped plan with zero semantic filtering — just picks 'most important'. Solves the 'filter at runtime' unreliability (70-80%) by scoping at plan creation (deterministic). Work description is natural language, unconstrained by git naming rules.
- **decision_it_changes**: Adopt plan-work mode for our campaign's feature branches — each Engine agent task gets a scoped plan on its branch, eliminating runtime filtering ambiguity.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Workflow pattern — no deps.
- **actionality**: 4

## Record 2 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: direct
- **extraction**:

  Ralph Non-Deterministic Backpressure (playbook enhancement): LLM-as-judge for subjective criteria (tone, aesthetics, UX) with binary pass/fail. Creates src/lib/llm-review.ts (createReview function: criteria + artifact → ReviewResult {pass, feedback}) and llm-review.test.ts (examples: text eval, vision eval with screenshots, smart intelligence for complex judgment). Ralph discovers pattern from test examples during src/lib exploration. Intelligence levels: 'fast' (Gemini 3.0 Flash, multimodal, cheap) and 'smart' (GPT 5.1, better judgment, higher cost). Converges through iteration — reviews run until pass.
- **decision_it_changes**: Adopt for Verdict agent's subjective quality gates (e.g., 'CER output is readable', 'visual layout matches spec'). Binary pass/fail fits our evidence law (PRIMARY/MEASURED/UNKNOWN).
- **transfer**: SURVIVES
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. LLM review needs model API — use local Ollama for 'fast', or our Claude session for 'smart' (already paid).
- **actionality**: 5

## Record 3 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: direct
- **extraction**:

  Ralph Acceptance-Driven Backpressure (playbook enhancement): Derive test requirements from acceptance criteria in specs during planning. Prevents 'cheating' — can't claim done without required tests passing. Test requirements = WHAT to verify (outcomes), not HOW to implement. Architecture: Phase 1 specs + acceptance criteria → Phase 2 planning derives required tests → Phase 3 building implements with tests. Modifies PROMPT_plan.md to include test derivation, PROMPT_build.md to require all required tests exist and pass before commit. Adds guardrail: 'Required tests derived from acceptance criteria must exist and pass before committing. TDD approach: tests can be written first or alongside.'
- **decision_it_changes**: Mandatory for our campaign: Every Engine task spec must include acceptance criteria → Verdict derives required tests → Engine implements with tests. This IS our FIND→SPEC→FIX→RE-VERIFY loop.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Test derivation is prompt logic.
- **actionality**: 4

## Record 4 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Ralph AskUserQuestionTool for Planning (playbook enhancement): During Phase 1 (Define Requirements), use Claude's built-in AskUserQuestionTool to systematically explore JTBD, topics, edge cases, acceptance criteria through structured interview before writing specs. Flow: Start with known info → Claude interviews via AskUserQuestion → Iterate until clear → Claude writes specs with acceptance criteria → Proceed to planning/building. No code/prompt changes needed — uses existing Claude Code capability.
- **decision_it_changes**: Use AskUserQuestionTool for our campaign's requirements clarification phase (pre-research) before Engine starts building.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Built-in Claude Code tool.
- **actionality**: 3

## Record 5 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook
- **date**: 2026-01-15
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Ralph Specs Audit (playbook enhancement): Dedicated mode for generating/maintaining specs with quality rules: behavioral outcomes only, topic scoping (one sentence without 'and'), consistent naming. Reverse Engineering Brownfield Projects to Specs: Bring brownfield codebases into Ralph's workflow by reverse-engineering existing code into specs before planning new work. JTBD → Story Map → SLC Release: Connect JTBD's audience/activities to Simple/Lovable/Complete releases.
- **decision_it_changes**: Apply Specs Audit rules to our campaign specs (PPT_SPEC, AGENTS.md, SOUTH_CANON) — ensure behavioral outcomes, proper scoping.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Spec quality rules are prompt logic.
- **actionality**: 3

## Record 6 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/references/sandbox-environments.md
- **date**: 2026-01-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Ralph sandbox environments (referenced in playbook): Docker sandboxes (local), Fly Sprites/E2B (remote/production). Philosophy: 'It's not if it gets popped, it's when. And what is the blast radius?' Running without sandbox exposes credentials, cookies, SSH keys, access tokens. Options: isolate with minimum viable access (only API keys/deploy keys needed, no private data, restrict network). Escape hatches: Ctrl+C stops loop, git reset --hard reverts uncommitted, regenerate plan if trajectory wrong.
- **decision_it_changes**: Use Docker sandboxes for Engine agent's build loops. Our campaign already assumes containerized execution.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Docker is local.
- **actionality**: 3

## Record 7 (from ralph_wiggum_002.jsonl)
- **source_url**: https://github.com/ClaytonFarr/ralph-playbook/blob/main/references/nah.png
- **date**: 2026-01-15
- **status**: MEASURED
- **relevance**: 1
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Geoffrey Huntley's 'nah' response to Matt Pocock and Ryan Carson's Ralph overviews — indicating the playbook captures nuances the summaries missed. The playbook author (ClaytonFarr) dug into recent videos and Geoff's original post to 'untangle what works best.'
- **decision_it_changes**: Primary source (Geoff's post + videos) > secondary summaries. We use the playbook as our Ralph reference because it's based on primary sources.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Source hierarchy is methodological.
- **actionality**: 1

## Record 8 (from ralph_wiggum_002.jsonl)
- **source_url**: https://x.com/GeoffreyHuntley/status/1944614322107564194
- **date**: 2025-07-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 2
- **actionability**: indirect
- **extraction**: Geoffrey Huntley tweet: Ralph Wiggum built CURSED programming language over 3 months (complete language). Boris Cherny's 30 days: 259 PRs using Ralph. Real production validation at scale.
- **decision_it_changes**: Confirms Ralph scales to multi-month, 259-PR projects. Our 48h campaign with Engine agent is well within proven scope.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Social proof at scale.
- **actionality**: 2
