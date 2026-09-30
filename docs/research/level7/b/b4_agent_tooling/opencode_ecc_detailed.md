# opencode_ecc_detailed (converted from opencode_ecc_detailed.jsonl - all records, fields verbatim)

## Record 1 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://v2.opencode.ai/skills
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OpenCode skill structure: SKILL.md with frontmatter (name, description, license, compatibility, metadata). Supporting files in scripts/ and references/. Skills array in opencode.json/opencode.jsonc adds local dirs or HTTP catalogs. Global sources: ~/.config/opencode/skills, ~/.claude/skills, ~/.agents/skills. Project sources: .opencode/skills, .claude/skills, .agents/skills. Skills loaded on-demand via native skill tool.
- **decision_it_changes**: W6 architecture: OpenCode skill structure for 18 language OCR engines
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://opencode.ai/docs/commands
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OpenCode Custom Commands: defined in .opencode/commands/<name>.md or .opencode/commands/<name>/command.md. Frontmatter: name, description, argument (optional). Command body is prompt template. Variables: {{cwd}}, {{selection}}, {{file}}, {{args}}. Commands can call other commands. Global commands in ~/.config/opencode/commands/. Project commands in .opencode/commands/. Commands discoverable via /help.
- **decision_it_changes**: W6 architecture: custom commands for OCR validation workflow steps
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://opencode.ai/docs/plugins
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  OpenCode Plugins: TypeScript modules in .opencode/plugins/<name>.ts or ~/.config/opencode/plugins/. Plugin exports default object with name, version, description, and optional hooks, commands, skills, agents, mcpServers. Hooks: event handlers for session.start, session.end, pre_tool_use, post_tool_use, file.edited, etc. Plugins can register custom tools. Installed via opencode plugin install <url>. Plugin marketplace at opencode.ai/plugins.
- **decision_it_changes**: W6 architecture: plugin system for OCR validation tool extensions
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://github.com/westcliff-resources/ECC-agent-skills/blob/main/.opencode/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  ECC OpenCode agents (26): build (primary coding), planner, architect, code-reviewer, security-reviewer, tdd-guide, build-error-resolver, e2e-runner, doc-updater, refactor-cleaner, go-reviewer, go-build-resolver, database-reviewer, docs-lookup (Context7), harness-optimizer, java-reviewer, java-build-resolver. Each agent: custom prompt, model, tool access. Specialist agents for specific languages/domains.
- **decision_it_changes**: W6 architecture: specialist agents per OCR engine language
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://github.com/westcliff-resources/ECC-agent-skills/blob/main/.opencode/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  ECC OpenCode commands (26): /plan (implementation plan), /tdd (TDD workflow), /code-review, /security, /build-fix, /e2e, /refactor-clean, /orchestrate (multi-agent), /learn (extract patterns), /checkpoint (save progress), /verify (verification loop), /eval (evaluation), /update-docs, /update-codemaps, /test-coverage, /setup-pm, /go-review, /go-test, /go-build, /skill-create, /instinct-status. Commands chain agents and skills.
- **decision_it_changes**: W6 architecture: command pipeline for OCR validation SDLC
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://github.com/generalduel/ECC-claude-skills-and-agents-/blob/main/.opencode/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  ECC variant hooks: Prettier, TypeScript, ESLint, Ruff, Go fmt on file.edited. Hook events: file.edited, session.start, pre_tool_use, post_tool_use. More granular hook coverage than westcliff variant. 31 commands vs 26. Fewer agents (12 vs 26) but more commands. /update-codemaps, /test-coverage, /skill-create, /instinct-status unique to this variant.
- **decision_it_changes**: W6 architecture: hook-based quality gates for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from opencode_ecc_detailed.jsonl)
- **source_url**: https://opencode.ai/docs/agents
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  OpenCode Agents: specialized assistants with custom prompts, models, tool access. Defined in .opencode/agents/<name>.json or .opencode/agents/<name>/agent.json. Fields: prompt, model, tools, description. Plan agent: analyzes code, reviews suggestions, no changes. Compatible with Claude Code agent definitions. Agents can be invoked via Agent tool or commands.
- **decision_it_changes**: W6 architecture: plan agent for OCR validation orchestration
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
