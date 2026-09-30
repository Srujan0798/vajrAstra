# artifact_210_langgraph_crewai_autogen_openai (converted from artifact_210_langgraph_crewai_autogen_openai.jsonl - all records, fields verbatim)

## Record 1 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://www.langchain.com/langgraph
- **date**: 2025-01-15
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 3
- **actionability**: 4
- **extraction**:

  LangGraph: low-level orchestration framework with StateGraph primitives. Nodes = computation steps, edges = control flow transitions. Supports single, multi-agent, hierarchical control flows in one framework. Built-in memory stores conversation histories across sessions. First-class streaming for token-by-token UX. Human-in-the-loop moderation and quality controls. Trusted by production companies. Maps to our PPT_SPEC architecture: StateGraph matches our DAG-based Phase 6 engine pipeline; memory = unified-memory vault; human-in-the-loop = validation call at H44-48; streaming = terminal-ops evidence display.
- **decision_it_changes**: W6 architecture choice: LangGraph as orchestration backbone for Phase 6 engine pipeline DAG
- **transfer**: SURVIVES
- **transfer_harness_fact**: PPT_SPEC designed for DAG execution; unified-memory provides persistent state; offline pipeline compatible with LangGraph local execution

## Record 2 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://www.langchain.com/blog/langgraph-multi-agent-workflows
- **date**: 2024-01-23
- **status**: DERIVED
- **relevance**: 3
- **recency**: 2
- **actionability**: 3
- **extraction**:

  LangGraph multi-agent workflows: three examples — Agent Supervisor (orchestrator routes to specialists), Multi-Agent Collaboration (independent agents with own scratchpads, final responses appended to global scratchpad), and Handoff patterns. Agent Supervisor: orchestrator LLM decides which specialist to call. Multi-Agent Collaboration: agents have independent prompts, LLMs, tools; connected via shared global scratchpad. Handoffs: control moves to specialist. Maps to our 3-agent model: Engine as supervisor routing to per-language OCR engines; Verdict/Miss as collaborators with shared unified-memory scratchpad.
- **decision_it_changes**: W6 architecture choice: supervisor vs collaboration pattern for Engine routing to 18 language engines
- **transfer**: SURVIVES
- **transfer_harness_fact**: unified-memory provides shared scratchpad; 18 engines need supervisor routing; dmux-workflows supports parallel collaboration

## Record 3 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://github.com/crewAIInc/crewAI
- **date**: 2025-06-01
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  CrewAI: role-based autonomous teams with Crews (high-level) and Flows (event-driven control). Agents have role, backstory, goal; communicate naturally, delegate work. Memory enabled with embedder config. v1.0 late 2025. 100k+ certified developers. Maps to our specialist squads: each language could be a 'crew' with role-specialized agents (preprocess, OCR, postprocess). But requires training data for embedder — conflicts with no training until W6 freeze. Event-driven Flows could model Engine→Verdict→Miss handoffs.
- **decision_it_changes**: W6 architecture choice: CrewAI role-based crews per language vs custom orchestrator; memory embedder needs training data (blocked until W6)
- **transfer**: DIES
- **transfer_harness_fact**: no training until W6 freeze blocks CrewAI memory embedder; 18 Indic langs need custom roles not pre-built; offline pipeline prefers explicit control over natural delegation

## Record 4 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://www.meta-intelligence.tech/en/insight-ai-agent-frameworks
- **date**: 2025-08-09
- **status**: DERIVED
- **relevance**: 3
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Framework comparison: LangGraph best for stateful workflows (graph-based state machines, durable execution, human-in-the-loop). CrewAI best for role-based teams (intuitive roles, fastest setup, A2A support). AutoGen best for conversational agents (diverse chat patterns, no-code Studio, .NET support). AutoGen group chat: centralized Group Chat Manager (LLM) orchestrates speaker selection. Maps to our needs: LangGraph matches PPT_SPEC DAG + verification-loop; CrewAI roles map to Engine/Verdict/Miss but memory blocked; AutoGen conversation-driven not suited for deterministic OCR pipeline.
- **decision_it_changes**: W6 architecture choice: LangGraph selected over CrewAI/AutoGen for deterministic offline OCR pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: LangGraph state machines match PPT_SPEC; human-in-the-loop = validation call; durable execution = unified-memory; no paid keys needed

## Record 5 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://developers.openai.com/api/docs/guides/agents/orchestration
- **date**: 2025-05-01
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  OpenAI Agents SDK orchestration: two patterns — Handoffs (specialist takes over conversation, control moves) and Agents as Tools (manager stays in control, calls specialists as bounded capabilities). Handoffs for delegated ownership; Agents as Tools for manager-owned final answer combining specialist outputs. Built-in handoff() function. Triage agent with handoffs to billing/refund agents. Maps to our Engine/Verdict/Miss: Engine as manager using Verdict/Miss as tools (Agents as Tools pattern) keeps ownership of final OCR result; or Handoffs for Engine→Verdict→Miss sequential chain. Agents as Tools fits our orchestrator model better.
- **decision_it_changes**: W6 architecture choice: Agents-as-Tools pattern for Engine calling Verdict/Miss vs Handoffs chain
- **transfer**: SURVIVES
- **transfer_harness_fact**: OpenAI Agents SDK requires paid API keys (blocked: no paid keys); but pattern transfers to our custom orchestrator; offline pipeline implements Agents-as-Tools natively

## Record 6 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://openai.github.io/openai-agents-python/multi_agent/
- **date**: 2025-06-01
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  OpenAI Agents SDK multi-agent: LLM-driven orchestration (LLM plans/reasons/decides steps) vs code-driven (determine flow via code). Mix-and-match allowed. Agents as Tools: manager calls specialists via Agent.as_tool(). Handoffs: specialist takes over. Best when: manager owns final answer, combines outputs, enforces shared constraints. Maps to our campaign: code-driven orchestration (PPT_SPEC pipeline fixed) with Engine as manager calling Verdict/Miss as tools. LLM-driven only for per-language engine selection within Engine agent.
- **decision_it_changes**: W6 architecture choice: code-driven main pipeline + LLM-driven per-language engine selection inside Engine agent
- **transfer**: SURVIVES
- **transfer_harness_fact**: code-driven pipeline matches PPT_SPEC; LLM-driven engine selection uses local models only; no paid keys needed for pattern transfer

## Record 7 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration
- **date**: 2025-05-28
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 3
- **extraction**:

  OpenAI Agents SDK multi-agent portfolio collaboration: combines deep specialization, parallel execution, robust orchestration. Demonstrates parallel subagent execution with result coordination. Maps to our Lane A/B/C parallelism: Engine builds 18 engines in parallel (Lane A), Verdict verifies in parallel (Lane B), Miss applies fixes + Lane C monitoring in parallel. Parallel execution optimizer skill directly implements this pattern.
- **decision_it_changes**: W6 architecture choice: parallel-execution-optimizer configuration for 18-lang parallel engine build/verify/fix
- **transfer**: SURVIVES
- **transfer_harness_fact**: parallel-execution-optimizer skill implements this; isolated worktrees for each language; offline pipeline supports batched parallel execution

## Record 8 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://dev.to/pockit_tools/langgraph-vs-crewai-vs-autogen-the-complete-multi-agent-ai-orchestration-guide-for-2026-2d63
- **date**: 2026-05-05
- **status**: DERIVED
- **relevance**: 3
- **recency**: 4
- **actionability**: 2
- **extraction**:

  2026 guide: shift from monolithic agents to multi-agent orchestration. LangGraph = control freak's dream (graph-based, exact step control). CrewAI = role-based teams with memory. AutoGen = conversation-driven with code execution. 'God Agent' anti-pattern: single agent doing everything. Multi-agent decomposes: orchestrator routes to specialists. CrewAI memory uses embeddings. AutoGen Group Chat Manager orchestrates speaker selection. Maps to our PPT_SPEC: LangGraph control matches our deterministic pipeline; God Agent anti-pattern warns against single agent for 18-lang OCR.
- **decision_it_changes**: W6 architecture choice: confirms LangGraph for control; rejects God Agent (single agent for all 18 langs)
- **transfer**: SURVIVES
- **transfer_harness_fact**: LangGraph deterministic control matches offline pipeline; no God Agent — 3-agent ops model distributes work

## Record 9 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://openagents.org/blog/posts/2026-02-23-open-source-ai-agent-frameworks-compared
- **date**: 2026-03-02
- **status**: DERIVED
- **relevance**: 3
- **recency**: 4
- **actionability**: 2
- **extraction**:

  Framework comparison 2026: CrewAI best for role-based teams (intuitive roles, fastest setup, A2A support). LangGraph best for stateful workflows (graph-based state machines, durable execution, human-in-the-loop). AutoGen best for conversational agents (diverse chat patterns, no-code Studio, .NET support). CrewAI v1.0 late 2025. LangGraph reached v1.0 late 2025, default runtime for LangChain agents, supports Python/JS. Production-grade agents needing fault tolerance and precise state management → LangGraph. Maps to our needs: fault tolerance + precise state = LangGraph; human-in-the-loop = validation call.
- **decision_it_changes**: W6 architecture choice: LangGraph for production-grade fault tolerance and state management in OCR pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: LangGraph v1.0 Python support; unified-memory provides durable state; verification-loop provides human-in-the-loop gate

## Record 10 (from artifact_210_langgraph_crewai_autogen_openai.jsonl)
- **source_url**: https://deepwiki.com/openai/openai-agents-python/13.2-multi-agent-orchestration-examples
- **date**: 2025-07-01
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 2
- **extraction**:

  OpenAI Agents SDK multi-agent orchestration examples: concrete implementations of delegation, handoffs, tool-based invocation. Coordinates specialized agents through delegation and handoffs. Maps to our Engine delegating per-language OCR to sub-engines, then handing off to Verdict for verification, then Miss for fixes. Tool-based invocation = Engine calling Verdict/Miss as tools (Agents-as-Tools pattern).
- **decision_it_changes**: W6 architecture choice: tool-based invocation pattern for Engine→Verdict→Miss handoffs
- **transfer**: SURVIVES
- **transfer_harness_fact**: pattern transfers without OpenAI SDK; orch-pipeline skill implements tool-based agent calls; offline pipeline compatible
