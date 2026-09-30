# laya_gates (converted from laya_gates.jsonl - all records, fields verbatim)

## Record 1 (from laya_gates.jsonl)
- **source_url**: https://github.com/NandhaKishorM/laya
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Laya: Non-autoregressive System 1 decision engine. Typed choice, score, yes/no decisions over any text in single forward pass. 100+ languages. Router picks right checkpoint per request. ~33ms inference. convaiinnovations/laya model. Open-source showcase.
- **decision_it_changes**: W6 architecture: Laya System-1 gate for OCR validation decision boundaries
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from laya_gates.jsonl)
- **source_url**: https://raw.githubusercontent.com/NandhaKishorM/laya/6a5819129eb220570792e417e49723d697efd76f/laya/__init__.py
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Laya Python package exports: Agent, RLAgent, load, Router, RouteDecision, DEFAULT_MODELS, detect_language, detect_script, is_english, clean_email_body, email_questions, guard_questions, moderation_questions, router_questions, triage_questions, confidence_from_probs, ece_score, proper_reward, render_options, td_lambda_targets. Version 0.3.3. System-1 decision types: classification, routing, scoring.
- **decision_it_changes**: W6 architecture: Laya Router for language-specific OCR engine routing
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from laya_gates.jsonl)
- **source_url**: https://laya.aay.sh/
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Laya AI Notification Command Center: Three scope toggles - Read, Write, Egress - gate what clients can call. Bearer-token auth or loopback-only mode. Full surface: search cards, semantic search, mutate, trigger outbound actions across 9 connected platforms. Same transport powers in-app coding agents. Open-source, local-first.
- **decision_it_changes**: W6 architecture: Laya scope gates for OCR validation tool access control
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from laya_gates.jsonl)
- **source_url**: https://github.com/PapaKoftes/Layla/blob/master/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Layla (different from Laya): self-hosted AI companion, local GGUF model via llama-cpp-python. No cloud, no API keys. Approval gate: file writes and code execution gated by allow_write/allow_run + approval flow. Personalities loaded from personalities/*.json. Decision schema via Pydantic. Coordinator runs agent_loop.autonomous_run. Tool dispatch implemented but agent executed zero tools for 16 days - dispatch discarded model's args.
- **decision_it_changes**: W6 architecture: approval gate pattern for OCR validation human-in-loop
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from laya_gates.jsonl)
- **source_url**: https://raw.githubusercontent.com/ThinkFlowLab/system1-agents/main/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  System1-agents: MCP server serving list_agents, run_agent, decide tools. Agents are modules under s1a/agents/ ending in frozen SPEC. Builder skill runs in Claude Code, probes task with 8-12 hand-written decisions before writing code, stops when task needs deduction/arithmetic. Injection guard: rail answering one question at hook of running agent, fails closed. Runs on jev, laya, or cua.
- **decision_it_changes**: W6 architecture: System-1 agent pattern for OCR validation gates
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from laya_gates.jsonl)
- **source_url**: https://arxiv.org/abs/2606.04306
- **date**: 2026-06-03
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Organizational Control Layer: Governance Infrastructure at Execution Boundary of LLM Agent Systems. Deployment-grade LLM agent systems require explicit governance at boundary between language generation and executable action. Governance layer mediates access to authority.
- **decision_it_changes**: W6 architecture: governance layer for OCR validation execution boundary
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from laya_gates.jsonl)
- **source_url**: https://arxiv.org/html/2606.28679v1
- **date**: 2026-06-28
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks. Capability gating (static: which tools exist) vs per-call authorization (dynamic: whether this call allowed). Safe design: prevent model from being authorization boundary. ScopeGate operationalizes at LLM tool-call boundary. Agentic payment protocols. LangChain/LangGraph, LlamaIndex, Stripe Agent Toolkit leave authorization to integrator.
- **decision_it_changes**: W6 architecture: ScopeGate pattern for OCR validation tool authorization
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
