# obsidian_detailed (converted from obsidian_detailed.jsonl - all records, fields verbatim)

## Record 1 (from obsidian_detailed.jsonl)
- **source_url**: https://github.com/RAIT-09/obsidian-agent-client/blob/master/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Obsidian Agent Client: React 19, TypeScript, Obsidian API, ACP. AgentConfig for Claude/Codex/Gemini/Custom. ACP layer: acp-client.ts (AcpClient class, process lifecycle), acp-handler.ts (SDK event handler + sessionId filter + listener broadcast), type-converter.ts (ACP SDK types <-> internal), permission-handler.ts (permission queue, auto-approve, Promise resolution), terminal-handler.ts (terminal process create/output/kill). Data flow single path: Agent Process -> ACP SDK -> AcpHandler -> listeners -> useAgentSession -> useAgentMessages -> useAgent facade.
- **decision_it_changes**: W6 architecture: ACP client for OCR validation agent connectivity
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from obsidian_detailed.jsonl)
- **source_url**: https://github.com/RAIT-09/obsidian-agent-client/blob/master/ARCHITECTURE.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Services injected via React Context: session-storage.ts (session metadata + message file I/O, sessions/*.json), settings-normalizer.ts (validation helpers), session-helpers.ts (agent config building, API key injection), view-registry.ts (multi-view management, focus, broadcast), update-checker.ts (agent/plugin version check). ChatPanel orchestrates hooks, renders children. ACP protocol isolated in acp/ layer. Multi-session support via view registry.
- **decision_it_changes**: W6 architecture: session storage for OCR validation history
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from obsidian_detailed.jsonl)
- **source_url**: https://github.com/UltimateAI-org/aitoolsforobsidian
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  AI Tools for Obsidian features: parallel sessions (4 max), message queueing (type while agent responds), quick prompts with @[[wikilinks]], direct agent integration, image attachments, slash commands, multi-agent support, floating chat, mode/model switching, session history, chat export as Markdown, terminal integration, MCP support (agents use their MCP servers). Install via BRAT. Apache-2.0.
- **decision_it_changes**: W6 architecture: Obsidian as OCR validation dashboard with multi-agent
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from obsidian_detailed.jsonl)
- **source_url**: https://community.obsidian.md/plugins/openagent-canvas
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  OpenAgent Canvas: runs local AI agent workflows from vault and Canvas. Connects to local OpenAgent daemon. Starts Codex tasks from Canvas nodes/notes. Tracks active threads. Writes results back to Canvas. Requirements: Obsidian desktop, community plugins, local OpenAgent daemon, Codex Desktop. Desktop-only (local filesystem access). Version 0.1.4, 163 downloads.
- **decision_it_changes**: W6 architecture: Canvas for OCR validation workflow visualization
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from obsidian_detailed.jsonl)
- **source_url**: https://github.com/testy-cool/obsidian-ai-canvas
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Obsidian AI Canvas: Gemini-powered, supports OpenAI, Claude, Ollama, 15+ providers. Features: Ask AI (right-click note), conversation threads (note links = history), MCP tools (web scraping, APIs, custom tools), any provider, image generation (NanoBanana), flashcards for Spaced Repetition. URL context, YouTube videos, image inputs. Install via community plugins or manual.
- **decision_it_changes**: W6 architecture: AI Canvas with MCP tools for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from obsidian_detailed.jsonl)
- **source_url**: https://zed.dev/acp/editor/obsidian
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Zed ACP Client for Obsidian: side panel for agents (Claude Agent, Gemini CLI). Direct agent integration, note mentions, slash commands, multi-agent, terminal integration, permission management. ACP enables editors to support any ACP-compatible agent without custom integrations. Metrics: weekly sessions for Zed Agent, Claude Agent, Codex CLI. Install via BRAT or manual.
- **decision_it_changes**: W6 architecture: ACP protocol standardization for OCR agent connectivity
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from obsidian_detailed.jsonl)
- **source_url**: https://obsidian.md/help/plugins
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Obsidian core plugins: Canvas (infinite visual space), Graph view (relationships), Note composer, Daily notes, File explorer, etc. Community plugins extend via BRAT or manual install. Canvas core plugin enables visual workflow layout for AI Canvas plugins.
- **decision_it_changes**: W6 architecture: Obsidian Canvas as OCR validation workflow canvas
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
