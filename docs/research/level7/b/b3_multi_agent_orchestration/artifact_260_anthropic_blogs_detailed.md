# artifact_260_anthropic_blogs_detailed (converted from artifact_260_anthropic_blogs_detailed.jsonl - all records, fields verbatim)

## Record 1 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/building-c-compiler
- **date**: 2026-02-05
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Building a C Compiler with a Team of Parallel Claudes (Anthropic Engineering): parallel agent team built a C compiler. Multiple Claude instances worked in parallel on different compiler passes (lexer, parser, type checker, codegen). Coordination via shared spec and interfaces. Maps to our Lane A: Engine builds 18 OCR engines in parallel (one per language) with shared PPT_SPEC interface. Each language engine = compiler pass. Parallel-execution-optimizer coordinates. Validation call = integration test.
- **decision_it_changes**: W6 architecture choice: parallel engine builds per language (like parallel compiler passes) with shared PPT_SPEC interface
- **transfer**: SURVIVES
- **transfer_harness_fact**: parallel-execution-optimizer skill; shared PPT_SPEC = shared spec; 18 langs = 18 parallel passes; validation call = integration test

## Record 2 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **date**: 2025-11-26
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Effective Harnesses for Long-Running Agents (Anthropic): harness design for agents running continuously. Key principles: stateless harness, durable session log outside harness, containers as cattle, crash recovery via session replay. p50 TTFT 60% drop, p95 >90% drop. Maps to our campaign: autonomous-agent-harness + unified-memory = stateless harness + durable session log. Engine/Verdict/Miss as stateless harnesses; unified-memory = session log. Containers as cattle = isolated worktrees per language. Crash recovery = replay from unified-memory.
- **decision_it_changes**: W6 architecture choice: stateless agent harnesses + unified-memory session log for 48h campaign durability
- **transfer**: SURVIVES
- **transfer_harness_fact**: autonomous-agent-harness + unified-memory implements this; isolated worktrees = cattle containers; crash recovery via memory replay

## Record 3 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/harness-design-long-running-apps
- **date**: 2026-03-24
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Harness Design for Long-Running Application Development (Anthropic): harness must manage context, tool calls, error recovery, deployment. Context engineering is #1 job. Rainbow deployments for zero-downtime updates. Async execution bottlenecks: lead waits for subagents. Maps to our campaign: context engineering = unified-memory context management. Rainbow deployments = validation call gates (no mid-campaign deploy). Async bottleneck: Engine→Verdict→Miss currently synchronous; could async for speed but adds coordination complexity. Campaign law: fix-loop max 2 rounds synchronous for determinism.
- **decision_it_changes**: W6 architecture choice: synchronous Engine→Verdict→Miss for determinism (fix-loop max 2 rounds); async rejected for coordination complexity
- **transfer**: SURVIVES
- **transfer_harness_fact**: sync loop for determinism; fix-loop max 2 rounds; validation call = deployment gate; context engineering via unified-memory

## Record 4 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **date**: 2026-01-09
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Demystifying Evals for AI Agents (Anthropic): eval-driven development for agents. Eval = task + scorer + threshold. Continuous eval in CI. Infrastructure noise quantification. Maps to our campaign: verification-loop = eval-driven development. CER per language = scorer. Threshold = weak cell targets (Santali >55, Kashmiri >55, OldScan >55, Odia >80). Continuous eval = per-engine verification-loop. Infrastructure noise = terminal-ops evidence capture.
- **decision_it_changes**: W6 architecture choice: CER per language as eval scorer with weak-cell thresholds; verification-loop as continuous eval
- **transfer**: SURVIVES
- **transfer_harness_fact**: verification-loop skill = eval-driven; CER scorer per language; weak cell thresholds as pass criteria; terminal-ops captures infrastructure noise

## Record 5 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/quantifying-infrastructure-noise
- **date**: 2026-02-05
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Quantifying Infrastructure Noise in Agentic Coding Evals (Anthropic): infrastructure variability affects eval results. Need controlled environments, repeated runs, noise quantification. Maps to our campaign: 18 langs × 100 samples lock = controlled evaluation. Probe22 18×100 lock is controlled baseline. Engine builds must run in controlled isolated worktrees. terminal-ops captures execution evidence for noise analysis. Campaign law: honest-empty for UNKNOWN noise.
- **decision_it_changes**: W6 architecture choice: controlled isolated worktrees per language for noise-controlled evals; probe22 baseline as reference
- **transfer**: SURVIVES
- **transfer_harness_fact**: probe22 18×100 lock = controlled baseline; isolated worktrees control noise; terminal-ops captures evidence; honest-empty for UNKNOWN

## Record 6 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/claude-code-best-practices
- **date**: 2025-04-18
- **status**: DERIVED
- **relevance**: 3
- **recency**: 3
- **actionability**: 3
- **extraction**:

  Claude Code Best Practices (Anthropic): agentic coding patterns. Use subagents for independent tasks. Keep context focused. Batch tool calls. Maps to our campaign: Engine uses subagents per language (independent). Verdict uses subagents per language verification. Miss uses subagents per language fixes. Batched unified-memory reads/writes. Context focused per language = isolated worktree context.
- **decision_it_changes**: W6 architecture choice: subagents per language for all 3 roles; batched unified-memory ops; focused context per worktree
- **transfer**: SURVIVES
- **transfer_harness_fact**: subagents per language via dmux-workflows; batched unified-memory; isolated worktree context focus

## Record 7 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/advanced-tool-use
- **date**: 2025-11-24
- **status**: DERIVED
- **relevance**: 3
- **recency**: 3
- **actionability**: 2
- **extraction**:

  Advanced Tool Use (Anthropic): tool design for agents. Tools as discrete capabilities. Tool descriptions critical — bad descriptions send agents wrong paths. Maps to our campaign: Engine tools = OCR engine build commands; Verdict tools = CER verification commands; Miss tools = patch application commands. Tool descriptions in unified-memory must be precise. Campaign law: no paid keys — all tools local/offline.
- **decision_it_changes**: W6 architecture choice: precise local tool definitions for Engine/Verdict/Miss; no external API tools
- **transfer**: SURVIVES
- **transfer_harness_fact**: all tools local (indicphotoocr, sarvam_vision, CER scorer); no paid keys; tool descriptions in unified-memory

## Record 8 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/code-execution-with-mcp
- **date**: 2025-11-04
- **status**: DERIVED
- **relevance**: 3
- **recency**: 3
- **actionability**: 2
- **extraction**:

  Code Execution with MCP (Anthropic): MCP for code execution in agents. Secure sandboxed execution. Maps to our campaign: terminal-ops executes engine build/verify/fix commands. MCP could provide sandboxed execution but campaign uses local execution in isolated worktrees. MCP adds complexity; local worktrees sufficient for offline pipeline.
- **decision_it_changes**: W6 architecture choice: local isolated worktree execution over MCP sandbox (simpler, offline-compatible)
- **transfer**: DIES
- **transfer_harness_fact**: local worktrees sufficient; MCP adds complexity; offline pipeline requires no external services; terminal-ops executes locally

## Record 9 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://www.anthropic.com/engineering/effective-context-engineering
- **date**: 2025-09-29
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Effective Context Engineering for AI Agents (Anthropic): context engineering is effectively the #1 job of engineers building AI agents. Communicating context to models automatically in dynamic systems. Multi-agent makes it harder to ensure each sub-agent has appropriate context. Maps to our campaign: unified-memory solves context engineering — each agent (Engine/Verdict/Miss) reads/writes precise context per language. Context = PPT_SPEC slice + engine config + CER history + fix patches. No context confusion because unified-memory enforces structure.
- **decision_it_changes**: W6 architecture choice: unified-memory as context engineering backbone — structured per-language context for each agent
- **transfer**: SURVIVES
- **transfer_harness_fact**: unified-memory enforces structured context; per-language context slices; Engine/Verdict/Miss read/write defined schema; honest-empty prevents context pollution

## Record 10 (from artifact_260_anthropic_blogs_detailed.jsonl)
- **source_url**: https://claude.com/blog/when-to-use-multi-agent-systems
- **date**: 2026-01-23
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 3
- **extraction**:

  When to Use Multi-Agent Systems (Anthropic Blog): three scenarios where multi-agent excels: (1) context window exceeded, (2) distinct skill sets, (3) parallelizable independent work. Coordination costs exceed benefits otherwise. Maps to our campaign: all three apply — 18 langs × 100 samples exceeds context; Engine/Verdict/Miss distinct skills; 18 languages parallelizable. Campaign law confirms multi-agent justified. But warns: teams build elaborate systems only to find single agent with better prompting works. Our 3-agent ops model is minimal (not elaborate).
- **decision_it_changes**: W6 architecture choice: confirms 3-agent minimal multi-agent justified (not elaborate); all 3 scenarios apply
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model minimal (not elaborate); all 3 scenarios apply; campaign law locks this
