# ts_ai_sdks_detailed (converted from ts_ai_sdks_detailed.jsonl - all records, fields verbatim)

## Record 1 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://sdk.vercel.ai/docs
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Vercel AI SDK Core: generateText, streamText, generateObject, streamObject for text/structured generation. Tool calling via tools parameter with execute function. Multi-step tools: streamText handles multiple tool steps automatically. Providers: OpenAI, Anthropic, Google, Azure, Amazon Bedrock, Cohere, Mistral, etc. AI SDK UI: useChat, useCompletion, useObject hooks for React/Vue/Svelte/Solid. AI SDK Harnesses: HarnessAgent for Claude Code, Codex, Pi. AI Gateway: 100+ models, single API key. Vercel Sandbox: secure code execution.
- **decision_it_changes**: W6 architecture: AI SDK Core for OCR validation agent tool calling
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://github.com/vercel/ai/blob/main/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Vercel AI SDK packages: ai (main), provider (interfaces), provider-utils (shared), openai, anthropic, google, azure, amazon-bedrock, etc. Framework integrations: react, vue, svelte, angular, rsc. Codemod for migrations. Examples: ai-functions, next-openai. Documentation in content/. Unified provider architecture. Default AI Gateway for 100+ models. MIT license. 26k stars, 5k forks.
- **decision_it_changes**: W6 architecture: provider abstraction for multi-model OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://cursor.com/docs/sdk/typescript
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Cursor SDK (@cursor/sdk): Agent.create({apiKey, model, local: {cwd}}). Model: composer-2.5 or other. Local: cwd for working directory. Cloud: runs on dedicated VM. Agent.run() returns stream. Agent.resume() for continuation. agent.getUsage() for cost tracking (TypeScript). Cursor.auth.login() browser login, mints API key to ~/.cursor/sdk/auth.json. Bundled single file: @cursor/sdk/bundled, @cursor/sdk/bundled/sqlite. Cookbook examples: quickstart, app-builder, kanban, coding-agent CLI.
- **decision_it_changes**: W6 architecture: Cursor SDK for programmatic OCR validation (needs API key)
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://cursor.com/blog/typescript-sdk
- **date**: 2026-04-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Cursor SDK use cases: CI/CD auto-fix bots, bug triage workers, code-review passes, embedded in-product agents, orchestrators. Public beta, token-based pricing. Same runtime/harness/models as Cursor IDE. Teams invoke from CI/CD, automate end-to-end workflows, embed in products. Native /sdk skill for guidance. Cloud agents run on empty VM with no repository.
- **decision_it_changes**: W6 architecture: Cursor cloud for OCR validation (paid, online)
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langchain/overview
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  LangChain v1.0: createAgent replaces createReactAgent. Middleware: summarizationMiddleware (condense history), humanInTheLoopMiddleware (approval for sensitive tools), piiRedactionMiddleware (redact PII). Agent = Model + Harness. Harness = prompt, tools, middleware. Deep Agents: automatic context compression, virtual filesystem, subagent spawning. LangGraph: low-level orchestration, durable runtime, checkpointing, human-in-loop. LangSmith: tracing, evaluation, debugging.
- **decision_it_changes**: W6 architecture: LangChain createAgent + middleware for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langgraph/quickstart
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  LangGraph Graph API: define tools/model, state (MessagesValue reducer, ReducedValue for counters), model node, tool node, edges, compile. Functional API: @entrypoint, @task decorators. State persists throughout execution. LangChain Docs MCP server for agent access to docs. LangChain Skills for performance. Checkpointing built-in. Human-in-loop via interrupts.
- **decision_it_changes**: W6 architecture: LangGraph for OCR validation multi-agent workflow with checkpointing
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://docs.langchain.com/oss/javascript/langchain/frontend/overview.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  LangChain Frontend SDKs: React, Vue, Svelte, Angular v1 packages. Hook exposes: durable thread state, tool-call lifecycle, interrupts, checkpoint history, custom state values. UI becomes control plane for long-running agents. Backend createAgent -> compiled LangGraph graph -> streaming API. Frontend stream handle -> reactive state. Migration guides for v0 to v1.
- **decision_it_changes**: W6 architecture: frontend SDK for OCR validation monitoring dashboard
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 8 (from ts_ai_sdks_detailed.jsonl)
- **source_url**: https://www.langchain.com/resources/ai-agent-frameworks
- **date**: 2026-06-09
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Framework comparison 2026: LangChain + LangGraph + Deep Agents + LangSmith. OpenAI Agents SDK: tightly scoped assistants, clean multi-agent delegation. Mastra: TypeScript teams, workflows, memory, Studio. CrewAI: role-based agents. Microsoft Agent Framework: enterprise. LlamaIndex Workflows: RAG-focused. Google ADK: Google ecosystem. LangChain recommended for production with LangGraph orchestration.
- **decision_it_changes**: W6 architecture: framework selection - LangChain/LangGraph for OCR validation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
