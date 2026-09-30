# claude_code_detailed (converted from claude_code_detailed.jsonl - all records, fields verbatim)

## Record 1 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/overview
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Claude Agent SDK capabilities: read files, run commands, search codebase, edit code. Key tools: Read, Glob, Grep, Edit, Write, Bash, Agent (for subagents). Subagents can be created programmatically (agents parameter), filesystem-based (.claude/agents/), or built-in general-purpose. AgentDefinition fields: description, prompt, tools, disallowedTools, model, skills, memory, mcpServers, maxTurns, background. Resume subagents retains full conversation history.
- **decision_it_changes**: W6 architecture: SDK tool set for OCR validation agents
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/subagents
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Subagent model selection: alias (fable, opus, sonnet, haiku, inherit) or full model ID. 'inherit' uses main model. Omitted = Claude Code picks from subagent model order. Skills array preloads skill content at startup; unlisted skills invocable via Skill tool. Memory source: user, project, local. mcpServers by name or inline config. maxTurns limits turns; partial output marked in v2.1.246+. background=true forces background execution.
- **decision_it_changes**: W6 architecture: subagent model/skill config for language-specific OCR engines
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/hooks
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Hook matcher patterns: exact tool names, glob patterns (mcp__.*__write.*), hyphens in exact-match need v2.1.195+. Common input fields: session_id, prompt_id, transcript_path, cwd, permission_mode, hook_event_name, tool_name, tool_input. Stop/SubagentStop hooks get last_assistant_message. SubagentStop gets stop_hook_active, agent_id, agent_type, agent_transcript_path. SubagentHandback tool (v2.1.271+) delivers report before stop. PreCompact/PostCompact: trigger manual/auto.
- **decision_it_changes**: W6 architecture: hook matchers for OCR engine validation triggers
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/hooks
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  SDK hooks: same events as CLI hooks. Hook types: command, http, mcp_tool, prompt, subagent. JSON output with decision, permissionDecision, additionalContext, retry. Async hooks (async: true) for command type only - run background, can't block. Timeout defaults per event. PermissionDenied hook: auto mode denies tool call. UserPromptExpansion: user-typed command or MCP prompt expands before reaching Claude. Notification hooks forward to external services (Slack). SubagentStop hooks track subagent completion.
- **decision_it_changes**: W6 architecture: SDK hook integration for OCR validation pipeline monitoring
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/skills
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Claude Code Skills: Markdown instructions in .claude/skills/<name>/SKILL.md. Auto-discovered from user (~/.claude/skills) and project (.claude/skills) directories. Additional directories via --add-dir. Skills loaded on-demand when Claude invokes Skill tool. Skill metadata: name, description, version, author. Can include scripts/ and references/. Plugin skills merge with user/project hooks when plugin enabled. Skill tool lets Claude read skill content.
- **decision_it_changes**: W6 architecture: skill-based OCR engine wrappers for 18 languages
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/agent-sdk/python
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Python SDK: async for message in query(prompt, options). Options: tools (preset or list), allowed_tools, system_prompt (string, preset, or file), mcp_servers (dict or path), strict_mcp_config, cli_path, settings, add_dirs, env. Methods: reconnect_mcp_server(server_name), toggle_mcp_server(server_name, enabled), stop_task(task_id). System message subtype 'init' yields skills array at stream start.
- **decision_it_changes**: W6 architecture: Python SDK for offline OCR validation orchestration
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from claude_code_detailed.jsonl)
- **source_url**: https://code.claude.com/docs/en/plugins
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Claude Code Plugins: extend functionality via .claude/plugins/<name>/. Components: commands, hooks, skills, agents, MCP servers. Plugin config: plugin.json with name, version, description, components. Hooks defined in hooks/hooks.json with optional description. When enabled, plugin hooks merge with user/project hooks. Example: auto-formatting plugin runs format.sh on PostToolUse Write/Edit. Plugin root available as ${CLAUDE_PLUGIN_ROOT} in commands.
- **decision_it_changes**: W6 architecture: plugin system for OCR validation tooling distribution
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
