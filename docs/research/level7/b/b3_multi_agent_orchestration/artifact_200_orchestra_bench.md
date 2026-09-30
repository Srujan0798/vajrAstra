# artifact_200_orchestra_bench (converted from artifact_200_orchestra_bench.jsonl - all records, fields verbatim)

## Record 1 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://arxiv.org/abs/2608.05263
- **date**: 2026-08-05
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OrchestraBench introduces a controlled failure-injection harness for multi-agent orchestration, measuring cascade radius and per-failure-mode recovery across templated enterprise workflows. Key finding: keyword/flag router scored 0% on adversarial cases with misleading flags, while intent-reasoning router scored 100% matching oracle. Three failure-handling tiers: tool faults (1.0 full recovery), ambiguous delegation (0.30 partial), latent/semantic modes (0.0 never recovered). Cascade radius increased with pipeline depth (mean 0.9 to 4.7 across depths 3-7). Blind retry reproduced latent faults and increased detection time. Maps to our 18-lang OCR weak cells (Santali 53.91, Kashmiri 54.82, OldScan 55.3, Odia 80.01) — need intent-reasoning routing for ambiguous OCR script delegations.
- **decision_it_changes**: W6 architecture choice: orchestrator routing policy for weak-cell delegation (intent-reasoning vs keyword/flag)
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells require intent-reasoning routing not keyword flags; offline pipeline supports controlled failure injection

## Record 2 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://arxiv.org/abs/2602.16873
- **date**: 2026-02-18
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  AdaptOrch formalizes task-adaptive multi-agent orchestration with dynamic topology selection among four canonical patterns (parallel, sequential, hierarchical, hybrid) based on task dependency graphs and domain characteristics. Performance Convergence Scaling Law shows orchestration topology dominates system-level performance over individual model capability when LLMs converge. Topology Routing Algorithm maps task decomposition DAGs to optimal orchestration in O(|V|+|E|) time. Adaptive Synthesis Protocol with provable termination and heuristic consistency scoring. Validated on coding (SWE-bench), reasoning (GPQA), RAG: 12-23% improvement over static single-topology baselines. Maps to our 18-lang OCR: weak cells need adaptive topology (Santali 53.91 may need hierarchical, Odia 80.01 may need parallel).
- **decision_it_changes**: W6 architecture choice: dynamic topology selection for per-language OCR pipeline routing
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs with varying difficulty need adaptive topology; offline pipeline supports DAG-based routing without training

## Record 3 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://arxiv.org/abs/2608.18167
- **date**: 2026-08-16
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Adversarial Review (AR) introduces minimal 3-agent cooperative code-review protocol: main coder, reviewer, critic. Reviewer evaluates, critic audits review through structured disagreement before main agent edits. On LiveCodeBench, AR achieves highest pass rate among tested methods, outperforming 5-agent baseline with only 3 agents. On SWE-PRBench, naive AR exposes false-consensus failure (agents converge without evidence), but single prompt iteration adding explicit disagreement constraints achieves highest F1. Two modes: Python orchestrator and portable SKILL.md protocol. Key insight: shape of disagreement matters more than agent count. Maps to ECC santa-method dual-reviewer and council. Directly applicable to our OCR weak cell validation: Engine→Verdict→Miss loop mirrors AR structure.
- **decision_it_changes**: W6 architecture choice: Engine/Verdict/Miss 3-agent ops model structure validated; false-consensus guard needed
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model (Engine/Verdict/Miss) locked per campaign law; santa-method dual-reviewer already implemented; offline pipeline supports SKILL.md protocol

## Record 4 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://www.anthropic.com/engineering/managed-agents
- **date**: 2026-04-08
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Anthropic Managed Agents: decouples brain (Claude+harness) from hands (sandboxes/tools) and session (durable event log). Harness writes session with emitEvent(id, event) for durable record. Session log sits outside harness — nothing in harness needs to survive crash; new harness can reboot with wake(sessionId) and resume via getSession(id). Container becomes cattle: provisioned via execute(name,input)→string tool call, failed containers caught as tool-call errors and retried with standard recipe. p50 TTFT dropped ~60%, p95 >90%. Scaling to many brains = starting stateless harnesses, connecting to hands only if needed. Maps to our unified-memory + dmux-workflows: session log = unified memory vault; stateless harnesses = parallel subagents in isolated worktrees.
- **decision_it_changes**: W6 architecture choice: session-log architecture for agent handoffs and crash recovery in 18-lang OCR pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: unified-memory skill provides durable session log; dmux-workflows supports stateless parallel subagents; offline pipeline compatible

## Record 5 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://www.anthropic.com/engineering/multi-agent-research-system
- **date**: 2025-06-13
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Anthropic multi-agent research system: lead agent (Claude Opus 4) + subagents (Claude Sonnet 4) outperformed single-agent Opus 4 by 90.2% on internal research eval. Multi-agent architectures scale token usage for tasks exceeding single-agent limits. Cost: agents use ~4× tokens vs chat, multi-agent ~15× tokens. Synchronous execution creates bottlenecks — lead waits for subagents, can't steer mid-flight. Async would enable parallelism but adds coordination/state consistency/error propagation challenges. Rainbow deployments avoid disrupting running agents. Each subagent needs objective, output format, tool guidance, clear boundaries. Early errors: spawning 50 subagents for simple queries, endless web search, excessive updates. Maps to our 3-agent ops model: Engine (lead) + Verdict/Miss (subagents) with token budget awareness.
- **decision_it_changes**: W6 architecture choice: async vs sync subagent execution for Engine/Verdict/Miss; token budget caps per language
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model fixed; token budgets per language (54-call Sarvam cap); offline pipeline needs sync for determinism but async for speed

## Record 6 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://claude.com/blog/multi-agent-coordination-patterns
- **date**: 2026-04-10
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Anthropic identifies 5 multi-agent coordination patterns: (1) Generator-Verifier: simplest, most deployed; verification subagent pattern. (2) Parallel teammates: independent subagents for independent subtasks, each builds context. (3) Orchestrator-workers: lead routes to specialists. (4) Message bus: shared communication layer for complex interactions. (5) Shared state: agents coordinate directly via shared state without intermediary. Key warning: unless explicitly parallelized, subagents run sequentially — multi-agent token cost without speed benefit. Use parallel when subtasks independent and benefit sustained multi-step work. Maps to our Lane A/B/C: Engine (orchestrator-workers for engine building), Verdict (generator-verifier for verification), Miss (parallel teammates for Lane C + monitoring).
- **decision_it_changes**: W6 architecture choice: coordination pattern assignment per agent role (Engine=orchestrator-workers, Verdict=generator-verifier, Miss=parallel teammates)
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model with defined roles; parallel-execution-optimizer skill for parallel teammates; offline pipeline supports all patterns

## Record 7 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- **date**: 2026-01-23
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: 4
- **extraction**:

  Anthropic guidance on when multi-agent systems excel vs single agent: (1) Context window exceeded — task needs more context than fits. (2) Distinct skill sets — subtasks require different specialized capabilities. (3) Parallelizable independent work — subtasks can run concurrently. Coordination costs typically exceed benefits outside these. Observed teams build elaborate multi-agent systems only to find improved single-agent prompting achieves equivalent results. Focus on orchestrator-subagent pattern: hierarchical lead agent spawns specialized subagents. Maps to our campaign: 18-lang OCR exceeds single-agent context (distinct scripts, weak cells); parallelizable per-language processing; distinct skill sets per engine/verdict/miss role.
- **decision_it_changes**: W6 architecture choice: confirms 3-agent multi-agent justified for 18-lang OCR (context, skills, parallelism)
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs exceed single-agent context; distinct Engine/Verdict/Miss skills; parallel per-language processing

## Record 8 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://arxiv.org/abs/2605.00410
- **date**: 2026-05-01
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Agent Capsules: adaptive execution runtime treating multi-agent pipeline as optimization with empirical quality constraints. Instruments coordination overhead per group, scores composition opportunity, selects among 3 compound execution strategies, gates every mode switch on rolling-mean output quality. Escalation ladder: standard → two-phase → sequential (recovers quality by un-merging, not rewriting). Against hand-tuned LangGraph 14-agent pipeline: 51% fewer fine-mode tokens, 42% fewer compound-mode tokens at +0.020/+0.017 quality. Against DSPy 5-agent: 19% fewer tokens at parity, 68% fewer than MIPROv2 at +0.052 quality. Treats multi-agent execution as group-level optimization with empirical quality gates — first system to do so. Maps to our OCR: 18 engines × 100 samples = 1800 calls; compound execution could save tokens but quality gates essential for weak cells.
- **decision_it_changes**: W6 architecture choice: compound execution with quality gates for token efficiency in 18-lang OCR pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18×100 lock = 1800 calls; quality gates essential for weak cells; offline pipeline supports rolling-mean quality monitoring

## Record 9 (from artifact_200_orchestra_bench.jsonl)
- **source_url**: https://arxiv.org/abs/2607.25152
- **date**: 2026-07-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Self-Evaluation Bias in Long-Running Agent Loops: agents grading own work suffer 'progress mirage' — plausible changes accepted as progress while real outcomes stagnate/regress. 54 cycles: agent claimed improvement every time, yet 56% had measured delta ≤0. Self-report uninformative; self-verdict gate degenerated to accept-all, eroding best state by 19%. Even strong in-band judge (full artifact + diff + history) accepted 44% real-world regressions, rejected 38% real improvements. On boundary task with artifact-verifiable success, mirage vanished to zero. Sign-only variant (accept/reject only) kept output similar to full feedback (110 vs 113), locating benefit in gate's grounding not feedback content. For open-ended objectives, out-of-band evaluation with real-world access is structural requirement. Maps to our campaign: Engine self-eval insufficient; Verdict (external verifier) + Miss (applier) provides out-of-band grounding.
- **decision_it_changes**: W6 architecture choice: confirms Engine/Verdict/Miss separation — Engine cannot self-verify; Verdict provides out-of-band verification; Miss applies fixes
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model separates generation (Engine) from verification (Verdict) and application (Miss); verification-loop skill enforces external grounding
