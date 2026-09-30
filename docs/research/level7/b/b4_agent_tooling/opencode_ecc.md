# opencode_ecc (converted from opencode_ecc.jsonl - all records, fields verbatim)

## Record 1 (from opencode_ecc.jsonl)
- **source_url**: https://v2.opencode.ai/skills
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OpenCode Skills: Markdown instructions loaded on-demand via native skill tool. One directory per skill with SKILL.md. Sources: Global (~/.config/opencode/skills), Global compat (~/.claude/skills, ~/.agents/skills), Project (.opencode/skills), Project compat (.claude/skills, .agents/skills). Skills array in opencode.json adds local dirs or HTTP catalogs. Skill includes scripts/ and references/ subdirectories.
- **decision_it_changes**: W6 architecture: OpenCode skills for OCR engine wrappers (18 languages)
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from opencode_ecc.jsonl)
- **source_url**: https://www.opencode.asia/skills
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OpenCode skill discovery: walks up from CWD to git worktree, loads matching skills from .opencode/, .claude/skills/, .agents/skills/. Global from ~/.config/opencode/skills/, ~/.claude/skills/, ~/.agents/skills/. Skill metadata: name, description, license, compatibility, metadata (audience, workflow). Skills loaded on-demand via native skill tool - agents see available skills and load full content when needed.
- **decision_it_changes**: W6 architecture: skill discovery pattern for multi-language OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from opencode_ecc.jsonl)
- **source_url**: https://github.com/elmm-programing/opencode/blob/main/opencode-agent-skills/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  opencode-agent-skills plugin: dynamic skills plugin providing 4 tools - use_skill (load SKILL.md), read_skill_file (read supporting files), run_skill_script (execute scripts), get_available_skills. Requires OpenCode v1.0.110+. Skill discovery order: .opencode/skills/, .claude/skills/, ~/.config/opencode/skills/, ~/.claude/skills/, ~/.claude/plugins/cache/, ~/.claude/plugins/marketplaces/. Alternatives: opencode-skills, superpowers, skillz (MCP server).
- **decision_it_changes**: W6 architecture: plugin-based skill loading for OCR engines
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from opencode_ecc.jsonl)
- **source_url**: https://github.com/diegaccio/opencode-agent-skills/blob/main/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Production-grade engineering skills for OpenCode: DEFINE->PLAN->BUILD->VERIFY->REVIEW->SHIP lifecycle. Commands: /spec, /plan, /build, /test, /review, /ship. Repository layout: .opencode/commands/, .opencode/skills/, .opencode/agents/, .opencode/plugins/, .opencode/references/. Fork of addyosmani/agent-skills adapted for OpenCode. AGENTS.md for project instructions.
- **decision_it_changes**: W6 architecture: full SDLC command pipeline for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from opencode_ecc.jsonl)
- **source_url**: https://github.com/westcliff-resources/ECC-agent-skills/blob/main/.opencode/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  ECC for OpenCode: 26 agents (build, planner, architect, code-reviewer, security-reviewer, tdd-guide, build-error-resolver, e2e-runner, doc-updater, refactor-cleaner, go-reviewer, go-build-resolver, database-reviewer, docs-lookup, harness-optimizer, java-reviewer, java-build-resolver). 26 commands: /plan, /tdd, /code-review, /security, /build-fix, /e2e, /refactor-clean, /orchestrate, /learn, /checkpoint, /verify, /eval, /update-docs, /update-codemaps, /test-coverage, /setup-pm, /go-review, /go-test, /go-build, /skill-create, /instinct-status. Plugin hooks: Prettier on file.edited, TypeScript check.
- **decision_it_changes**: W6 architecture: ECC agent/command framework for OCR validation pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from opencode_ecc.jsonl)
- **source_url**: https://github.com/generalduel/ECC-claude-skills-and-agents-/blob/main/.opencode/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  ECC for OpenCode (variant): 12 agents (planner, architect, code-reviewer, security-reviewer, tdd-guide, build-error-resolver, e2e-runner, doc-updater, refactor-cleaner). 31 commands including /orchestrate, /learn, /checkpoint, /verify, /eval, /update-codemaps, /test-coverage, /skill-create, /instinct-status, /go-*. Plugin hooks: Prettier, TypeScript, ESLint, Ruff, Go fmt on file.edited. Hook events: file.edited, session.start, pre_tool_use, post_tool_use.
- **decision_it_changes**: W6 architecture: ECC variant with more commands/hooks for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from opencode_ecc.jsonl)
- **source_url**: https://opencode.ai/docs/agents
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  OpenCode Agents: specialized AI assistants with custom prompts, models, tool access. Plan agent analyzes code and reviews suggestions without making changes. Agents configured via .opencode/agents/ directories. Compatible with Claude Code agent definitions.
- **decision_it_changes**: W6 architecture: OpenCode plan agent for OCR validation orchestration
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
