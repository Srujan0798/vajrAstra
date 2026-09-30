# claude_code_sdk (converted from claude_code_sdk.jsonl - all records, fields verbatim)

## Record 1 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/overview
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Claude Agent SDK provides programmatic access to Claude Code capabilities: file reading, command execution, codebase search, editing. Supports Python and TypeScript. Subagents isolate context, run in parallel, inherit project CLAUDE.md and skills unless overridden. SDK discovers skills from ~/.claude/skills/, .claude/skills/, and additional directories via add_dirs.
- **decision_it_changes**: W6 architecture choice: whether to build orchestration on Claude SDK vs custom harness
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/subagents
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Subagents in SDK: programmatically defined via agents parameter, filesystem-based in .claude/agents/, or built-in general-purpose. Benefits: context isolation (subagent conversation separate), parallelization (multiple subagents concurrent), specialized instructions. Can cap depth, concurrency, spend via env vars. Subagent output scanned for control-tag imitation, permission-config mentions, turn markers in v2.1.210+.
- **decision_it_changes**: W6 architecture: subagent pattern for parallel OCR engine validation across 18 languages
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/hooks
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  SDK hooks: PreToolUse, PostToolUse, Stop, SubagentStop, UserPromptSubmit, Notification, etc. Hooks can be commands, HTTP endpoints, MCP tool calls, LLM prompts, or subagents. Async hooks (async: true) run background without blocking. Hook matchers support exact, glob, regex patterns. MCP tool hooks integrate with MCP servers. SDK callback hooks use same JSON format as shell command hooks.
- **decision_it_changes**: W6 architecture: hook-based verification loop for OCR engine outputs
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/skills
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Agent Skills in SDK: auto-discovered from user/project directories at startup, model-invoked (Claude autonomously chooses when to use). Skills loaded from ~/.claude/skills/, .claude/skills/, and additional directories via add_dirs. Can restrict to specific skills via skills array in options. System message with subtype 'init' yields skills array at stream start.
- **decision_it_changes**: W6 architecture: skill-based OCR engine wrappers for 18 languages
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from claude_code_sdk.jsonl)
- **source_url**: https://www.anthropic.com/webinars/claude-code-advanced-patterns
- **date**: 2026-03-24
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Anthropic webinar on advanced patterns: subagents and hooks for orchestrating multi-step work, MCP integrations connecting to internal tools/services, context strategies for large repos (structuring CLAUDE.md for monorepos, managing context windows), CI pipeline patterns (automated PR review, test generation, regression catching).
- **decision_it_changes**: W6 architecture: MCP integration pattern for OCR engine validation pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/hooks
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Hook events reference: SessionStart, SessionEnd, UserPromptSubmit, Stop, StopFailure, PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch, Notification, MessageDisplay, SubagentStart, SubagentStop, TaskCreated, TaskCompleted. Hook types: command, http, mcp_tool, prompt, subagent. Decision control: exit code 2 blocks, JSON output with decision/permissionDecision/additionalContext. Async hooks for long-running tasks.
- **decision_it_changes**: W6 architecture: hook-based quality gates for OCR engine validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from claude_code_sdk.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/python
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Python SDK reference: ClaudeAgentOptions with tools, allowed_tools, system_prompt, mcp_servers, strict_mcp_config, cli_path, settings, add_dirs, env. Methods: reconnect_mcp_server, toggle_mcp_server, stop_task. Query returns async iterator of messages. Supports subagents via agents parameter with AgentDefinition.
- **decision_it_changes**: W6 architecture: Python SDK for offline OCR validation pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
