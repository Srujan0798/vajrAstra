# claude_mem_001 (converted from claude_mem_001.jsonl - all records, fields verbatim)

## Record 1 (from claude_mem_001.jsonl)
- **source_url**: https://github.com/thedotmack/claude-mem
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  claude-mem (thedotmack/claude-mem) v13.28.0: Persistent memory compression system for Claude Code. Auto-captures tool usage observations, generates semantic summaries, makes them available to future sessions. Core: 5 lifecycle hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd), smart install, worker service (local HTTP API + web viewer UI + search endpoints, managed by Bun), SQLite database (sessions, observations, summaries), mem-search skill (natural language queries with progressive disclosure), Chroma vector database (hybrid semantic + keyword search). Install: 'npx claude-mem install' (auto-sign-in for free 30-day observer trial), or '/plugin marketplace add thedotmack/claude-mem' then '/plugin install claude-mem'. Apache-2.0 license. Works with OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode.
- **decision_it_changes**:

  Whether to adopt claude-mem as our cross-session memory layer for the 3-agent ops model (Engine/Verdict/Miss), replacing or augmenting ECC's unified-memory. The worker service + Chroma + SQLite stack is more feature-complete.
- **transfer**: SURVIVES
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Local SQLite + Chroma + Bun worker — fully local. Observer trial is optional; can use --provider host for local-only.

## Record 2 (from claude_mem_001.jsonl)
- **source_url**: https://docs.claude-mem.ai/architecture/search-architecture
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  claude-mem MCP search tools (3-layer workflow, ~10x token savings): 1) 'search' — compact index with IDs (~50-100 tokens/result), 2) 'timeline' — chronological context around results, 3) 'get_observations' — full details ONLY for filtered IDs (~500-1000 tokens/result). Available MCP tools: search (full-text queries, filters by type/date/project), timeline (context around observation), get_observations (batch fetch by IDs). Example: search(query='authentication bug', type='bugfix', limit=10) → get_observations(ids=[123,456]).
- **decision_it_changes**: Whether to use claude-mem's MCP search tools as the canonical memory query interface for all three agents, enabling token-efficient cross-session context retrieval.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. MCP tools served by local worker — zero cloud.

## Record 3 (from claude_mem_001.jsonl)
- **source_url**: https://github.com/thedotmack/claude-mem/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  claude-mem modes: 'code' (default English), 'code--zh' (Simplified Chinese), 'code--ja' (Japanese). Configured via CLAUDE_MEM_MODE in ~/.claude-mem/settings.json. Language-specific modes follow pattern 'code--[lang]' (ISO 639-1). Restart Claude Code to apply. This enables multilingual observation generation — relevant for our 18 Indic languages.
- **decision_it_changes**: Whether to configure claude-mem with Indic language modes for agents working on language-specific OCR tasks (e.g., code--hi for Hindi, code--bn for Bengali).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Mode config is local settings.json.

## Record 4 (from claude_mem_001.jsonl)
- **source_url**: https://docs.claude-mem.ai/architecture/hooks-architecture
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  claude-mem hooks architecture: 7 hook scripts explained. SessionStart (loads context), UserPromptSubmit (captures intent), PostToolUse (captures observations), Stop (generates summaries), SessionEnd (finalizes), plus pre-hook (smart install) and worker management. Hooks write to SQLite + Chroma. Worker service runs on localhost:37777 (configurable), provides web viewer UI at worker URL printed on startup.
- **decision_it_changes**: Understanding the hook lifecycle for integration with ECC's hook system — potential conflict if both manage hooks.
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Hook conflict with ECC needs testing — both use Claude Code hooks.

## Record 5 (from claude_mem_001.jsonl)
- **source_url**: https://github.com/thedotmack/claude-mem/blob/main/README.md
- **date**: 2026-08-31
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  claude-mem release branches: 'main' (stable, published to npm), 'core-dev' (early reliability fixes), 'community-edge' (community integrations). Only 'main' published to npm; others run from source. Version 13.28.0 current. CMEM token (BASE CA: 0x76b1967eec0ccaeb001bbbb2b40dc4badba31ba3) embraced by creator as community catalyst — not required for functionality.
- **decision_it_changes**: Branch strategy for our use — stick to 'main' stable branch. CMEM token is irrelevant to functionality.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Branch choice is local git decision.

## Record 6 (from claude_mem_001.jsonl)
- **source_url**: https://docs.claude-mem.ai/cloud-sync
- **date**: 2026-08-31
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: 2
- **extraction**:

  claude-mem Cloud Sync: Back up memories to cmem.ai — no daemon, worker syncs on write. Free 30-day observer trial, then falls back to Anthropic plan unless subscribed. This is the 'observer' memory that runs off-plan. Privacy: use '<private>' tags to exclude sensitive content from storage.
- **decision_it_changes**: Whether to enable cloud sync for our campaign — DECISION: NO. Our law: no paid keys, no cloud spend. Use --provider host for local-only, or skip sign-in with CLAUDE_MEM_ONLINE_OPTIN=false.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Cloud sync requires paid subscription after trial — violates no-paid-keys law.

## Record 7 (from claude_mem_001.jsonl)
- **source_url**: https://github.com/thedotmack/claude-mem/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  claude-mem OpenClaw Gateway: 'curl -fsSL https://install.cmem.ai/openclaw.sh | bash' installs as persistent memory plugin on OpenClaw gateways. Handles dependencies, plugin setup, AI provider config, worker startup, optional real-time observation feeds to Telegram, Discord, Slack. This is a separate integration path from Claude Code.
- **decision_it_changes**: Not directly relevant — we use Claude Code, not OpenClaw. But shows claude-mem's multi-platform architecture.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. OpenClaw integration is separate; our path is Claude Code plugin.

## Record 8 (from claude_mem_001.jsonl)
- **source_url**: https://github.com/Vvkmnn/claude-historian-mcp/blob/main/README.md
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Comparison: claude-mem vs historian (Vvkmnn/claude-historian-mcp). claude-mem: Plugin captures observations via lifecycle hooks, compresses into SQLite + Chroma, loads context every session. Requires Bun, Python, background worker on port 37777. Real-world testing (270+ sessions): 95% of sessions never query history — always-on tools pay 5-8k tokens/session regardless. historian: Pays 0 tokens idle, 500-2k per query, saving ~475k tokens over 100 sessions. Known issues with claude-mem: stub session files break --continue, worker daemon version conflicts, security hooks blocking valid edits.
- **decision_it_changes**:

  Critical data point: claude-mem's always-on context injection costs 5-8k tokens/session even when unused (95% of sessions). historian's on-demand query is 10x cheaper. For our campaign with 3 agents running many sessions, this token tax is significant.
- **transfer**: CONTRADICTION
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Token cost matters under our no-paid-keys law — historian's on-demand model may be better.
- **actionality**: 3
