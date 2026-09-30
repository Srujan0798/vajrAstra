# laya_detailed (converted from laya_detailed.jsonl - all records, fields verbatim)

## Record 1 (from laya_detailed.jsonl)
- **source_url**: https://github.com/NandhaKishorM/laya
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Laya model checkpoints: router picks right checkpoint per request. Supports 100+ languages. Typed choice (classification), score (confidence), yes/no decisions. Single forward pass ~33ms. Non-autoregressive System 1. convaiinnovations/laya base model. Open-source, local-first.
- **decision_it_changes**: W6 architecture: Laya checkpoints for per-language OCR confidence scoring
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from laya_detailed.jsonl)
- **source_url**: https://raw.githubusercontent.com/NandhaKishorM/laya/6a5819129eb220570792e417e49723d697efd76f/laya/__init__.py
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Laya presets: email_questions, guard_questions, moderation_questions, router_questions, triage_questions. Functions: confidence_from_probs, ece_score (expected calibration error), proper_reward, render_options, td_lambda_targets. Language detection: detect_language, detect_script, is_english. Email cleaning: clean_email_body. Agent types: Agent, RLAgent, Router, RouteDecision, DEFAULT_MODELS.
- **decision_it_changes**: W6 architecture: Laya triage/guard questions for OCR validation gates
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from laya_detailed.jsonl)
- **source_url**: https://laya.aay.sh/
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Laya AI Command Center: 3 scope toggles - Read (read access), Write (write access), Egress (outbound actions). Gates what clients can call. Bearer-token auth or loopback-only mode. 9 connected platforms: Slack, Gmail, GitHub, Jira, etc. Search cards, semantic search, mutate, trigger outbound. Same transport for in-app coding agents. Open-source, local-first, privacy-focused.
- **decision_it_changes**: W6 architecture: scope toggles for OCR validation tool permissions
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from laya_detailed.jsonl)
- **source_url**: https://github.com/PapaKoftes/Layla/blob/master/AGENTS.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Layla (self-hosted companion): approval gate for file writes (write_file, apply_patch) and code execution (shell, run_python) via allow_write/allow_run + approval flow. Personalities from personalities/*.json, dynamic loading via _load_aspects(). Decision schema via Pydantic. Coordinator runs agent_loop.autonomous_run. Runtime safety loads config (TTL-cached, mtime-cached). Tool dispatch implemented but discarded model args for 16 days.
- **decision_it_changes**: W6 architecture: approval gate pattern for OCR validation human review
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from laya_detailed.jsonl)
- **source_url**: https://raw.githubusercontent.com/ThinkFlowLab/system1-agents/main/README.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  System1-agents as MCP server: tools list_agents, run_agent, decide. Agents under s1a/agents/ with frozen SPEC. Builder skill in Claude Code probes 8-12 hand-written decisions before coding. Stops when deduction/arithmetic needed. Injection guard: rail at hook of running agent, fails closed. Runs on jev, laya, or cua. Flags, run commands, extras in docs/agents.md.
- **decision_it_changes**: W6 architecture: System-1 agent builder for OCR validation gate agents
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from laya_detailed.jsonl)
- **source_url**: https://arxiv.org/abs/2606.04306
- **date**: 2026-06-03
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Organizational Control Layer: governance at execution boundary between language generation and executable action. Deployment-grade systems need explicit governance. Control layer mediates access to authority. Governance infrastructure for LLM agent systems.
- **decision_it_changes**: W6 architecture: governance layer for OCR validation execution control
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from laya_detailed.jsonl)
- **source_url**: https://arxiv.org/html/2606.28679v1
- **date**: 2026-06-28
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Capability Gates vs Authorization: capability gating (static tool menu) != per-call authorization (dynamic allow/deny). Confused deputy when authority and designation conflated. ScopeGate at LLM tool-call boundary. Safe design: model not authorization boundary. LangChain/LangGraph, LlamaIndex, Stripe Agent Toolkit leave authorization to integrator. Agentic payment protocols need explicit auth.
- **decision_it_changes**: W6 architecture: ScopeGate for OCR validation tool authorization
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
