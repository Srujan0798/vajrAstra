# artifact_270_ecc_final_batch (converted from artifact_270_ecc_final_batch.jsonl - all records, fields verbatim)

## Record 1 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/agent-harness-construction/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Agent Harness Construction: designs and optimizes AI agent action spaces, tool definitions, observation formatting for higher completion rates. Maps to our campaign: Engine action space = engine build commands (indicphotoocr, sarvam_vision, config); Verdict action space = CER verification commands; Miss action space = patch application commands. Observation formatting = unified-memory structured reads. Completion rate = CER target per language. Tool definitions must be precise per campaign law.
- **decision_it_changes**: W6 architecture choice: precise action spaces and tool definitions per agent role via agent-harness-construction
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; action spaces defined per role; tools local/offline; observation formatting via unified-memory schema

## Record 2 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/agent-eval/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Agent Eval: head-to-head comparison of coding agents (Claude Code, Aider, Codex) on custom tasks with pass rate, cost, time, consistency metrics. Maps to our campaign: could eval Engine vs other agents for engine building. But campaign law: Engine role locked per 3-agent ops model. No agent comparison needed — role assignment fixed. Eval metrics (pass rate, cost, time) map to our CER, token budget, campaign timeline.
- **decision_it_changes**: W6 architecture choice: agent-eval not needed for role assignment (locked); metrics map to CER/token/time
- **transfer**: DIES
- **transfer_harness_fact**: 3-agent ops model roles locked; no agent comparison; eval metrics survive as CER/token budget/timeline

## Record 3 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/agentic-engineering/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Agentic Engineering: eval-first execution, decomposition, cost-aware model routing. Use when planning engineering work agents carry out end-to-end. Maps to our campaign: Orchestrator does eval-first planning (PPT_SPEC → blueprint → plan-orchestrate). Decomposition = 18 engine builds. Cost-aware routing = local models only (no paid keys), token budgets per language (54-call Sarvam cap). Campaign law: no training until W6 freeze.
- **decision_it_changes**: W6 architecture choice: eval-first planning via blueprint/plan-orchestrate; cost-aware routing = local models only
- **transfer**: SURVIVES
- **transfer_harness_fact**: eval-first via blueprint/plan-orchestrate; local models only; token budgets per language; no training until W6

## Record 4 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/ai-first-engineering/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 2
- **recency**: 5
- **actionability**: 1
- **extraction**:

  AI-First Engineering: operating model for teams where AI agents generate large share of implementation. Team process, review gates, ownership rules. Maps to our campaign: Orchestrator is human, Engine/Verdict/Miss are agents. Review gates = verification-loop, santa-method. Ownership = Engine owns build, Verdict owns verify, Miss owns fix. But this skill is for human teams using agents, not pure agent orchestration.
- **decision_it_changes**: W6 architecture choice: ai-first-engineering not directly applicable (human+agent team model); review gates and ownership map
- **transfer**: PARTIAL
- **transfer_harness_fact**: review gates (verification-loop, santa-method) and ownership (per role) survive; human team process doesn't apply

## Record 5 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/ai-regression-testing/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  AI Regression Testing: sandbox-mode API testing without DB dependencies, automated bug-check workflows, patterns to catch AI blind spots where same model writes and reviews code. Maps to our campaign: Verdict verifies Engine output (different agents — catches blind spots). Miss applies fixes, Verdict re-verifies (different agent re-reviews). Sandbox mode = isolated worktrees per language. No DB dependencies = offline pipeline. Campaign law: Verdict specifies, Miss applies, Verdict re-verifies — different agents for write/review.
- **decision_it_changes**: W6 architecture choice: Verdict (different agent) verifies Engine; Verdict re-verifies Miss fixes — catches AI blind spots
- **transfer**: SURVIVES
- **transfer_harness_fact**: different agents for write (Engine) and review (Verdict); sandbox = isolated worktrees; no DB deps; fix-loop max 2 rounds

## Record 6 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/automation-audit-ops/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: 1
- **extraction**:

  Automation Audit Ops: evidence-first automation inventory and overlap audit for ECC. Jobs, hooks, connectors, MCP servers, wrappers — live, broken, redundant, missing. Maps to our campaign: could audit Engine/Verdict/Miss automation stack before validation call. But campaign timeline tight — audit adds overhead. Campaign law: honest-empty — only audit if evidence shows need.
- **decision_it_changes**: W6 architecture choice: automation-audit-ops only if evidence shows need (honest-empty); not default pre-call
- **transfer**: UNKNOWN
- **transfer_harness_fact**: honest-empty principle; audit only if evidence shows gap; campaign timeline tight; not default

## Record 7 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/benchmark/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Benchmark: measure performance baselines, detect regressions before/after PRs, compare stack alternatives. Maps to our campaign: CER per language = performance baseline. Probe22 18×100 lock = baseline. Engine builds must not regress CER. Benchmark skill could run pre/post engine build comparison. But campaign uses CER as primary metric, not latency/throughput.
- **decision_it_changes**: W6 architecture choice: CER as primary benchmark metric; probe22 baseline; regression detection via verification-loop
- **transfer**: SURVIVES
- **transfer_harness_fact**: CER per language = benchmark metric; probe22 baseline exists; verification-loop detects regression; latency/throughput secondary

## Record 8 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/benchmark-optimization-loop/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Benchmark Optimization Loop: make something faster, try many variants, run recursive optimization, benchmark latency/throughput/cost, choose best by repeated measured tests. Maps to our campaign: Engine could try engine config variants for each language, benchmark CER, choose best. But campaign law: probe22 GT verdicts LOCKED (§6.4); engine configs fixed per language. No recursive optimization — fixed configs from locked verdicts. Optimization loop dies.
- **decision_it_changes**: W6 architecture choice: benchmark optimization loop rejected — probe22 GT verdicts LOCKED fix engine configs
- **transfer**: DIES
- **transfer_harness_fact**: probe22 GT verdicts LOCKED (§6.4); engine configs fixed; no variant testing; fixed configs from locked verdicts

## Record 9 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/cost-aware-llm-pipeline/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Cost-Aware LLM Pipeline: model routing by task complexity, budget tracking, retry logic, prompt caching. Maps to our campaign: token budgets per language (18×100 = 1800 calls budget). Sarvam_vision at 54-call cap. Model routing: Engine uses local indicphotoocr (no API cost); Verdict uses local CER scorer; Miss uses local patcher. Budget tracking = terminal-ops evidence + unified-memory. Retry logic = fix-loop max 2 rounds. Prompt caching = unified-memory context reuse.
- **decision_it_changes**: W6 architecture choice: cost-aware pipeline with local models only; token budgets per language; Sarvam 54-call cap; fix-loop max 2 retries
- **transfer**: SURVIVES
- **transfer_harness_fact**: local models only (no paid keys); token budgets per language; Sarvam 54-call cap hard limit; fix-loop max 2 rounds = retry logic; unified-memory = prompt cache

## Record 10 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/cost-tracking/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Cost Tracking: track and report Claude Code token usage, spending, budgets from local ECC cost-tracker metrics log. Maps to our campaign: token usage tracking per language per agent (Engine/Verdict/Miss). Budgets: 1800 total calls, Sarvam 54-call cap. Cost-tracking skill monitors spend. Campaign law: no paid keys — only local token counting. Validation call needs cost report.
- **decision_it_changes**: W6 architecture choice: cost-tracking skill monitors per-language per-agent token usage; validation call includes cost report
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; local token counting only; per-language per-agent budgets; Sarvam 54-cap; validation call cost report

## Record 11 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/context-budget/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Context Budget: audits Claude Code context window consumption across agents, skills, MCP servers, rules. Identifies bloat, redundant components, token-savings recommendations. Maps to our campaign: 3-agent ops model must fit context windows. Engine context = PPT_SPEC slice + engine config. Verdict context = CER criteria + engine output. Miss context = fix spec + verification report. Unified-memory keeps context minimal per agent. Context-budget skill audits before validation call.
- **decision_it_changes**: W6 architecture choice: context-budget audit pre-validation-call; unified-memory minimizes per-agent context
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; unified-memory minimizes context; per-agent context slices; pre-call audit fits timeline

## Record 12 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/continuous-learning-v2/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 2
- **recency**: 5
- **actionability**: 1
- **extraction**:

  Continuous Learning v2: instinct-based learning from sessions via hooks, creates atomic instincts with confidence scoring, evolves into skills/commands/agents. Project-scoped to prevent cross-project contamination. Maps to our campaign: could capture lessons from 48h campaign. But campaign law: no training until W6 freeze; learning captures patterns not model updates. Instincts from campaign could inform W6 training decision. But W6 decision AT THE CALL — learning captured for call evidence.
- **decision_it_changes**: W6 architecture choice: continuous-learning-v2 captures campaign instincts for W6 call evidence; no model updates until W6
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; project-scoped instincts; captures patterns for W6 call; no model updates until W6 freeze; honest-empty for UNKNOWN

## Record 13 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/delivery-gate/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Delivery Gate (revisited): stop hook blocking finish until quality checks pass. Detects rationalization (surface text heuristics), stale learning logs (mtime), low disk space. Maps to our campaign: blocks Engine done until verification-loop passes; blocks Verdict done until santa-method dual-review passes; blocks Miss done until re-verification passes. Rationalization detection catches 'engine looks good' without CER evidence. Stale logs detection catches missing unified-memory updates. Campaign law: fix-loop max 2 rounds.
- **decision_it_changes**: W6 architecture choice: delivery-gate hooks on all 3 agents enforcing verification-loop, santa-method, fix-loop max 2
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; hooks on all 3 agents; rationalization detection needs CER evidence; stale logs = missing unified-memory updates

## Record 14 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/eval-harness/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Eval Harness: formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD). Use when workflow needs formal eval before trusted or changed. Maps to our campaign: verification-loop IS the eval harness for each engine build. CER per language = eval metric. Threshold = weak cell targets. Formal eval before engine trusted = verification-loop gate. Campaign law: Verdict specifies fixes, Miss applies, Verdict re-verifies — eval harness at each stage.
- **decision_it_changes**: W6 architecture choice: eval-harness = verification-loop at each engine build stage; CER metric with weak cell thresholds
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; verification-loop is eval harness; CER metric; weak cell thresholds; formal eval at each stage per campaign law

## Record 15 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/intent-driven-development/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Intent-Driven Development: turns ambiguous changes into scoped, verifiable acceptance criteria before implementation. Use for de-risking security/data/migration/integration changes. Maps to our campaign: PPT_SPEC is intent; blueprint decomposes into acceptance criteria per engine (CER target per language). Orchestrator writes acceptance criteria before Engine builds. Campaign law: honest-empty — criteria must be measurable (CER).
- **decision_it_changes**: W6 architecture choice: intent-driven development via PPT_SPEC → blueprint → per-engine CER acceptance criteria
- **transfer**: SURVIVES
- **transfer_harness_fact**: PPT_SPEC = intent; blueprint decomposes; CER = measurable acceptance criteria; honest-empty enforced

## Record 16 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/loop-design-check/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Loop Design Check (revisited): WRITE loop (gate whether to build, define machine-decidable goal, pick loop type, pick skeleton) and REVIEW loop (5 failure modes + decidability, boundaries, fallback, judge independence, keep-judgment-human). Our Engine→Verdict→Miss loop: machine-decidable goal = CER per language; loop type = fix-loop max 2 rounds; judge independence = Verdict independent from Engine; human judgment = validation call at H44-48. REVIEW must pass before campaign runs.
- **decision_it_changes**: W6 architecture choice: loop-design-check REVIEW passed for Engine→Verdict→Miss loop; CER goal; fix-loop max 2; validation call human gate
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; CER machine-decidable goal; fix-loop max 2 rounds; Verdict independent; validation call human judgment gate

## Record 17 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/orch-refine-code/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 2
- **recency**: 5
- **actionability**: 1
- **extraction**:

  Orch-Refine-Code: behavior-preserving refactor — confirm tests green, restructure without behavior change, keep tests green, review, gated commit. Maps to our campaign: Engine builds are new features (not refactors). Miss applies fixes — could be refactors but must preserve behavior (CER not regress). Orch-refine-code pattern for Miss fix application: verify CER before/after fix. But campaign uses orch-fix-defect for Miss, not orch-refine-code.
- **decision_it_changes**: W6 architecture choice: Miss uses orch-fix-defect pattern (not orch-refine-code); CER regression check before/after fix
- **transfer**: DIES
- **transfer_harness_fact**: Miss uses orch-fix-defect for fixes; orch-refine-code for refactors only; CER regression check survives

## Record 18 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/parallel-execution-optimizer/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Parallel Execution Optimizer (revisited): concurrent agents, batched tool calls, isolated worktrees, independent verification lanes. Lane A: 18 Engine agents parallel (one per language). Lane B: 18 Verdict agents parallel. Lane C: 18 Miss agents parallel + monitoring. Batched unified-memory reads/writes per lane. Campaign target: engines landing tonight; validation call H44-48. Isolated worktrees prevent cross-language contamination.
- **decision_it_changes**: W6 architecture choice: parallel-execution-optimizer config for 3 lanes × 18 langs with isolated worktrees and batched memory ops
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; 3 lanes × 18 langs = 54 parallel agents max; isolated worktrees; batched unified-memory; engines landing tonight

## Record 19 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/skill-comply/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: 1
- **extraction**:

  Skill Comply: visualizes whether skills/rules/agent definitions are actually followed. Auto-generates scenarios at 3 prompt strictness levels, runs agents, classifies behavioral sequences, reports compliance rates. Maps to our campaign: could verify Engine/Verdict/Miss follow their skill definitions. But campaign timeline tight — compliance check adds overhead. Campaign law: honest-empty — only run if evidence shows non-compliance.
- **decision_it_changes**: W6 architecture choice: skill-comply only if evidence shows non-compliance (honest-empty); not default
- **transfer**: UNKNOWN
- **transfer_harness_fact**: honest-empty; compliance check only if evidence shows gap; campaign timeline tight; not default pre-call

## Record 20 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/verification-loop/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Verification Loop (revisited): multi-stage verification (syntax, types, tests, security, performance, docs). Each stage gates next. Maps to our campaign: Engine build → syntax/types/tests (OCR runs); Verdict → security (no leaks), performance (CER), docs (evidence). Miss fix → re-verify all stages. Fix-loop max 2 rounds. Campaign law: Verdict specifies, Miss applies, Verdict re-verifies — verification-loop at each step.
- **decision_it_changes**: W6 architecture choice: verification-loop stages map to Engine build → Verdict verify → Miss fix → re-verify; fix-loop max 2 rounds
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; stages map to campaign phases; fix-loop max 2 rounds; Verdict independent verifier

## Record 21 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://arxiv.org/abs/2602.16873
- **date**: 2026-02-18
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  AdaptOrch (revisited): topology routing algorithm O(|V|+|E|) maps task DAGs to optimal orchestration. Our task DAG: 18 language nodes → Engine build → Verdict verify → Miss fix. Topology per language: weak cells (Santali, Kashmiri, OldScan) → hierarchical (more supervision); strong cells (Odia) → parallel. Routing algorithm assigns topology per language based on probe22 CER baseline. Adaptive synthesis protocol merges results with consistency scoring.
- **decision_it_changes**: W6 architecture choice: per-language topology routing via AdaptOrch algorithm; weak cells hierarchical, strong parallel
- **transfer**: SURVIVES
- **transfer_harness_fact**: probe22 CER baseline drives routing; weak cells get hierarchical; strong get parallel; O(|V|+|E|) routing; offline pipeline supports

## Record 22 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://arxiv.org/abs/2608.05263
- **date**: 2026-08-05
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  OrchestraBench (revisited): failure injection harness. Cascade radius 0.9-1.5 for depth-3 pipeline (Engine/Verdict/Miss). Intent-reasoning router 100% vs keyword 0% on adversarial. Trusted-state repair gains from trusted signal. Maps to our campaign: unified-memory checkpoint = trusted state. Engine→Verdict→Miss delegation uses intent-reasoning (CER-based) not keyword flags. Failure injection testing pre-validation-call could verify robustness. But campaign timeline tight.
- **decision_it_changes**: W6 architecture choice: intent-reasoning delegation (CER-based); unified-memory checkpoint = trusted state; failure injection test if time permits
- **transfer**: SURVIVES
- **transfer_harness_fact**: depth-3 pipeline = low cascade radius; intent-reasoning = CER-based delegation; unified-memory = trusted checkpoint

## Record 23 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/terminal-ops/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Terminal-Ops (revisited): evidence-first execution. Every command run, repo check, CI debug, fix push has exact proof. Maps to our campaign: Engine runs indicphotoocr/sarvam commands with terminal-ops proof. Verdict runs CER verification with proof. Miss runs patch commands with proof. All evidence in unified-memory with PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD status per §9 evidence law. Validation call reads evidence package.
- **decision_it_changes**: W6 architecture choice: terminal-ops mandatory for all agent commands; evidence package for validation call per §9 law
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; §9 evidence law enforced; all commands have proof; validation call reads evidence package

## Record 24 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/unified-memory/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Unified Memory (revisited): durable, inspectable context handoffs between agents via local ECC Memory Vault. Engine writes build artifacts + CER; Verdict reads, writes verification; Miss reads both, writes fixes; all agents read/write. Validation call reads full trace. Honest-empty: only measured evidence stored. Campaign law: every record names decision it can change. Transfer: SURVIVES — this IS the campaign backbone.
- **decision_it_changes**: W6 architecture choice: unified-memory IS the campaign backbone for all agent handoffs and validation evidence
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign backbone; honest-empty enforced; §9 evidence law; all 3 agents share vault; validation call reads trace

## Record 25 (from artifact_270_ecc_final_batch.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/santa-method/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Santa Method (revisited): dual independent reviewers must both pass. Adversarial reviewers challenge each other. Convergence loop iterates to agreement. Maps to Verdict agent: two independent verification passes (e.g., CER + visual inspection, or two different CER scorers). Both must pass. Convergence loop = fix-loop max 2 rounds. Adversarial Review paper (arXiv:2608.18167) validates: critic role catches false consensus. Campaign law: Verdict specifies fixes — santa-method ensures fix specs are robust.
- **decision_it_changes**: W6 architecture choice: santa-method dual verification for Verdict; convergence loop = fix-loop max 2 rounds
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; Adversarial Review paper validates; fix-loop max 2 rounds = convergence limit; Verdict specifies fixes after dual review
