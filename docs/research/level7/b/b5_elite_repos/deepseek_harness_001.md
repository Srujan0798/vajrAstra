# deepseek_harness_001 (converted from deepseek_harness_001.jsonl - all records, fields verbatim)

## Record 1 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/deepseek-ai/deepseek-harness
- **date**: 2026-08-13
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: direct
- **extraction**:

  DeepSeek Harness (deepseek-ai/deepseek-harness, 'dsh'): Everything-is-a-plugin agent harness. Built on Cordis (spatiotemporal composability paradigm, arXiv:2608.25512). Developer preview — compatibility-breaking changes expected. 237.3k stars (as of ELITE_REPO_REFRESH), fastest-growing repo of window (~5.5k stars/day for 6 weeks). Satellite ecosystem crystallized in 48h: dsh-desktop 29.1k, dsh-web 8.1k, awesome-dsh-plugin. Run: 'npx @deepseek-ai/dsh web' (Web UI at localhost:3080) or from source: 'git clone && pnpm install && pnpm run build && pnpm dsh web'. Community: GitHub Discussions, Discord, dsh-plugin topic for discoverability. MIT license. Third-party deps in THIRD_PARTY_NOTICES.md.
- **decision_it_changes**:

  Whether to adopt dsh as our harness instead of ECC. dsh's 'everything is a plugin' architecture is compelling but it's in developer preview with breaking changes. Our campaign ends ~Sep 29 — too risky to migrate mid-campaign. ELITE_REPO_REFRESH decision: 'harness-as-plugin reference pattern for our ops model; do NOT migrate mid-campaign.'
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Developer preview + breaking changes = unacceptable risk for 48h campaign. ECC is stable.
- **actionality**: 4

## Record 2 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/deepseek-ai/deepseek-harness/blob/main/README.md
- **date**: 2026-08-13
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  dsh architecture: Cordis-based plugin system. Models, tools, sandboxes are all plugins. Follow AGENTS.md for agent integration. Development: 'pnpm run dev:web' builds/serves/rebuilds on edits. 'make help' lists Make targets. Plugin ecosystem: awesome-dsh-plugin (community plugins), dsh-desktop, dsh-web. The 48h ecosystem crystallization suggests strong plugin developer experience.
- **decision_it_changes**: Plugin architecture is a reference pattern for our ECC skill system — but ECC already has 292 skills with similar discoverability. No need to adopt dsh for this.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Architecture pattern is informational only.
- **actionality**: 3

## Record 3 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/Devin-AXIS/iPolloWork/blob/main/README.md
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  iPolloWork (Devin-AXIS/iPolloWork) integrates Codex, DeepSeek Harness, OpenCode, and future runtimes through explicit compatibility boundaries. OpenCode is default local execution runtime; dsh is optional peer runtime and subagent delegation target; Codex connects through ipollowork-ui-mcp. MCP is integration protocol, not another agent engine. This validates multi-harness orchestration pattern.
- **decision_it_changes**: Confirms dsh can be a peer runtime for subagent delegation — but our 3-agent model uses Claude Code subagents, not cross-harness delegation. Extra complexity not needed.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Multi-harness adds operational complexity without clear benefit for our use case.
- **actionality**: 3

## Record 4 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/TeleAI-UAGI/telemem/blob/main/docs/MCP.md
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  TeleMem ships opt-in Cordis patch for dsh: starts pinned TeleMem release with uvx, discovers all eight memory tools. dsh connects to external tools through @deepseek-ai/dsh-mcp-client plugin. This shows dsh's MCP integration pattern.
- **decision_it_changes**: MCP client plugin pattern — but ECC also has MCP support. No unique advantage for our campaign.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. MCP pattern is standard across harnesses.
- **actionality**: 3

## Record 5 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/nagisanzenin/engram/blob/main/INSTALL-DSH.md
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Engram on dsh: Runs through surfaces dsh ships natively: SKILL.md directory-bundle skills from ~/.agents/skills, AGENTS.md instructions, unmodified Claude Code hook bridge for session nudge, subagent delegation. dsh is in developer preview with compatibility-breaking changes warned in its own README.
- **decision_it_changes**: Confirms dsh supports Agent Skills standard (SKILL.md in ~/.agents/skills) and AGENTS.md — same as ECC, Claude Code, Codex. Interoperability exists but dsh's instability is the blocker.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Developer preview instability = DIES for campaign.
- **actionality**: 3

## Record 6 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/sandbaseai/sandbase-harness/blob/main/llms.txt
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Sandbase Harness showcase: Official DeepSeek Harness Showcase at github.com/deepseek-ai/deepseek-harness/discussions/1918. Verified dshbase listing at dshbase.com/plugins/sandbase-harness/. Independent self-hosting guide (SSD Nodes). This shows dsh has a plugin registry (dshbase.com) and community showcase.
- **decision_it_changes**: Plugin registry exists but is new. ECC's skill catalog (292 skills) is larger and battle-tested. No migration incentive.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. New registry vs established ECC catalog.
- **actionality**: 2

## Record 7 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/EmbraceAGI/Awesome-AGI/blob/main/README.md
- **date**: 2026-08-20
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Awesome-AGI: deepseek-harness (dsh) listed with star badge, description: 'DeepSeek's official open agent harness — everything is a plugin (models, tools, sandboxes)'. Plugin ecosystem: awesome-dsh-plugin. Aug 2026 launch. Compared to: Claude Code (skills, hooks, MCP, subagents), OpenAI Codex (codex-security), Grok Build (headless/CI, ACP), OpenHands (autonomous SE agents), Hermes Agent, OpenClaw, OpenWorker, MetaGPT.
- **decision_it_changes**:

  dsh is the newest major harness (Aug 2026) with fastest growth. But 'everything is a plugin' is also ECC's model (skills, agents, commands, hooks). ECC has 2.2.2 stable release; dsh is developer preview.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Preview vs stable = DIES for time-boxed campaign.
- **actionality**: 3

## Record 8 (from deepseek_harness_001.jsonl)
- **source_url**: https://github.com/liaohch3/claude-tap/blob/main/README.md
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Claude Tap (liaohch3/claude-tap) captures traffic from: Codex App, Gemini CLI, Grok Build CLI, DeepSeek Harness (dsh headless tasks and custom profiles using DeepSeek or compatible gateways), Kimi CLI, MiMo Code, OpenCode. This shows dsh can be monitored/tapped like other CLIs.
- **decision_it_changes**: Observability tooling exists for dsh — but not relevant to our campaign which uses Claude Code + ECC.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Tap tool is separate; doesn't affect harness choice.
- **actionality**: 2
