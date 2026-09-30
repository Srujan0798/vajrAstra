# ts_ai_sdks (converted from ts_ai_sdks.jsonl - all records, fields verbatim)

## Record 1 (from ts_ai_sdks.jsonl)
- **source_url**: https://sdk.vercel.ai/docs
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Vercel AI SDK: TypeScript toolkit for AI-powered apps/agents with React, Next.js, Vue, Svelte, Node.js. AI SDK Core: unified API for text generation, structured objects, tool calls, building agents. AI SDK UI: framework-agnostic hooks for chat/generative UI. AI SDK Harnesses: uniform API for running agent harnesses (Claude Code, Codex, Pi) via HarnessAgent. Model providers: OpenAI, Anthropic, Google, Azure, Amazon Bedrock, etc. Multi-step tools via streamText. AI Gateway: 100+ models, no markup, no multiple API keys. Vercel Sandbox: run agent code securely at scale.
- **decision_it_changes**: W6 architecture: Vercel AI SDK for OCR validation agent harness abstraction
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from ts_ai_sdks.jsonl)
- **source_url**: https://github.com/vercel/ai/blob/main/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Vercel AI SDK repo structure: packages/ai (main SDK), packages/provider (provider interfaces), packages/provider-utils (shared utilities), packages/<provider> (provider implementations: openai, anthropic, google, azure, amazon-bedrock), packages/<framework> (UI integrations: react, vue, svelte, angular, rsc), packages/codemod (migrations), examples/, content/ (docs). Unified provider architecture. Default uses Vercel AI Gateway for 100+ models. MIT license.
- **decision_it_changes**: W6 architecture: provider abstraction for multi-model OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from ts_ai_sdks.jsonl)
- **source_url**: https://cursor.com/docs/sdk/typescript
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Cursor TypeScript SDK (@cursor/sdk): calls Cursor's agent from code. Same agent as Cursor IDE, CLI, web. npm install @cursor/sdk. Requires Node.js 22.13+. Per-platform binaries for sandboxing and ripgrep. Lazy loads local executor. Bundled single file. Entry points: @cursor/sdk/bundled, @cursor/sdk/bundled/sqlite. Cookbook: SDK quickstart, app-builder, kanban board for cloud agents, coding-agent CLI. Use cases: CI auto-fix bots, bug triage, code review, embedded agents, orchestrators.
- **decision_it_changes**: W6 architecture: Cursor SDK for programmatic OCR validation agents
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from ts_ai_sdks.jsonl)
- **source_url**: https://cursor.com/blog/typescript-sdk
- **date**: 2026-04-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Cursor SDK announcement: build programmatic agents with same runtime, harness, models as Cursor. Run locally or on Cursor cloud (dedicated VM). Public beta, token-based pricing. Agent.create() with apiKey, model (composer-2.5), local cwd. Teams invoking agents from CI/CD, automations for end-to-end workflows, embedding agents in products. Native /sdk skill for guidance.
- **decision_it_changes**: W6 architecture: Cursor cloud agents for OCR validation (requires paid cloud)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from ts_ai_sdks.jsonl)
- **source_url**: https://github.com/langchain-ai/langchainjs/blob/main/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  LangChain.js: TypeScript framework for LLM-powered applications. Standard interfaces for agents, models, embeddings, vector stores. Packages: langchain (main), @langchain/core (core abstractions, runnables), @langchain/textsplitters, @langchain/openai, @langchain/anthropic, other providers. Corridor security analysis via analyzePlan tool. LangSmith for observability, LangGraph for orchestration, Deep Agents for sophisticated agents.
- **decision_it_changes**: W6 architecture: LangChain.js for OCR validation agent framework
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from ts_ai_sdks.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langchain/overview
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  LangChain overview: create_agent minimal configurable harness. Agent = Model + Harness. Harness = prompt, tools, middleware. Supports OpenAI, Anthropic, Google. LangChain vs LangGraph vs Deep Agents: Deep Agents for batteries-included (context compression, virtual filesystem, subagent spawning). LangChain for customizable harness. LangGraph for low-level orchestration (deterministic + agentic). LangSmith for tracing/debugging/evaluation. createAgent in v1.0 replaces createReactAgent. Middleware: summarization, human-in-the-loop, PII redaction.
- **decision_it_changes**: W6 architecture: LangChain create_agent for OCR validation with middleware
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from ts_ai_sdks.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langgraph/quickstart
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  LangGraph quickstart: calculator agent via Graph API or Functional API. State persists throughout execution. MessagesValue reducer for appending messages. ReducedValue for accumulating LLM call count. Install LangChain Docs MCP server for agent access to docs. LangChain Skills to improve performance. Graph API: define tools/model, state, model node, tool node, edges, compile. Functional API: @entrypoint, @task decorators.
- **decision_it_changes**: W6 architecture: LangGraph for OCR validation multi-agent workflow
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 8 (from ts_ai_sdks.jsonl)
- **source_url**: https://www.langchain.com/resources/ai-agent-frameworks
- **date**: 2026-06-09
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  AI agent frameworks comparison (2026): LangChain, CrewAI, Microsoft Agent Framework, LlamaIndex Workflows, Google ADK, OpenAI Agents SDK, Mastra. LangChain pairs with LangGraph for stateful cyclic multi-agent, Deep Agents for long-running, LangSmith for observability. LangSmith works with any framework. OpenAI Agents SDK for tightly scoped assistants and clean multi-agent delegation. Mastra for TypeScript teams wanting workflows, memory, Studio in one package.
- **decision_it_changes**: W6 architecture: framework selection for OCR validation (LangChain + LangGraph)
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 9 (from ts_ai_sdks.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langchain/frontend/overview.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  LangChain frontend SDKs: built for agent applications, not just chatbots. Hook exposes agent's durable thread state, tool-call lifecycle, interrupts, checkpoint history, custom state values. UI becomes control plane for long-running agent work. v1 frontend packages: React, Vue, Svelte, Angular. Backend createAgent produces compiled LangGraph graph with streaming API. Frontend stream handle connects to API, provides reactive state.
- **decision_it_changes**: W6 architecture: frontend SDK for OCR validation monitoring dashboard
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
