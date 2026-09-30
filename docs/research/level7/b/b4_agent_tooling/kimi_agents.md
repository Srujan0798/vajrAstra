# kimi_agents (converted from kimi_agents.jsonl - all records, fields verbatim)

## Record 1 (from kimi_agents.jsonl)
- **source_url**: https://www.kimi.com/en/blog/kimi-k2
- **date**: 2026-09-05
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Kimi K2: Mixture-of-Experts model with 32B activated params, 1T total params. Open-sourced with agentic capabilities. Optimized for agentic tasks: does not just answer, acts. Supports 20+ tools including file system, browser, terminal, code generation, image/audio generation. End-to-end RL training as native agent. 256K context window (updated weight).
- **decision_it_changes**: W6 architecture: Kimi K2 as alternative OCR validation engine for weak cells (Santali 53.91, Kashmiri 54.82)
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from kimi_agents.jsonl)
- **source_url**: https://platform.moonshot.ai/docs/guide/kimi-k2-quickstart
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Kimi K2 Quickstart: 1T total params, 32B active MoE. Leading coding abilities in China. Full stack support: frontend to backend, code generation, DevOps, debugging, optimization. 12+ built-in tools: web search, precise tool calls. Agent-building: complex task decomposition, Enforcer & JSON mode for stable tool calls, multitool collaboration. API compatible with Anthropic/OpenAI formats.
- **decision_it_changes**: W6 architecture: Kimi API for offline OCR validation (needs API key = paid key risk)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from kimi_agents.jsonl)
- **source_url**: https://platform.kimi.ai/docs/guide/use-kimi-k3-to-setup-agent
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Kimi K3 agent setup: reasoning, coding, tool-calling for complex tasks. Combines official web-search tool with custom tools. Task breakdown: Retrieve (scope, current data), Analyze (compare, identify conflicts), Deliver (structured report). Official tools: web-search, fetch, code-runner, excel. Formula API flow for tool integration.
- **decision_it_changes**: W6 architecture: Kimi K3 for research agent in validation pipeline
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from kimi_agents.jsonl)
- **source_url**: https://github.com/MoonshotAI/Kimi-K3
- **date**: 2026-07-20
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Kimi K3: open-weight, native multimodal agentic model, 2.8T params, Kimi Delta Attention (KDA) + Attention Residuals (AttnRes). Stable LatentMoE: 16 of 896 experts active, 2.5x scaling efficiency over K2. 1M token context. Long-horizon coding: GPU kernel optimization, compiler dev, vision-in-loop game dev, CAD, chip design. Agentic knowledge work: deep research with visualizations, widgets, dashboards, motion design, video editing. Native multimodality: text, images, video.
- **decision_it_changes**: W6 architecture: Kimi K3 open-weight for offline OCR engine (2.8T params too large for offline)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from kimi_agents.jsonl)
- **source_url**: https://platform.moonshot.ai/docs/guide/agent-support
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Using Kimi K2 in software agents: VS Code + Cline/RooCode integration. Anthropic API compatible endpoint: https://api.moonshot.ai/anthropic. OpenAI compatible: https://api.moonshot.ai/v1 with model kimi-k2-0711-preview. Requires API key from platform.moonshot.ai. Disable browser tool usage in Cline settings.
- **decision_it_changes**: W6 architecture: Kimi integration via Cline (requires paid API key)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from kimi_agents.jsonl)
- **source_url**: https://www.kimi.com/en/help/agent/agent-overview
- **date**: 2025-09-05
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Kimi Agent overview: Kimi K2 (Sept 5 2025) - 32B activated, 1T total, MoE. Kimi K2.5 (Jan 27 2026). Kimi K2.6 (Apr 20 2026) - open-sourced, state-of-the-art coding, long-horizon, Agent Swarm. Native agent via end-to-end RL. Works with 20+ tools: filesystem, browser, terminal, code gen, image/audio gen. Principle: 'the model is the product'.
- **decision_it_changes**: W6 architecture: Kimi K2.6 open-source for offline use (but 1T params)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
