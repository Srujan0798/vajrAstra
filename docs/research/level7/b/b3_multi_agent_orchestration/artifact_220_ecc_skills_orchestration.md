# artifact_220_ecc_skills_orchestration (converted from artifact_220_ecc_skills_orchestration.jsonl - all records, fields verbatim)

## Record 1 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/team-agent-orchestration/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Team-Agent Orchestration skill: runs agent squads with work items, ownership, agent Kanban, merge gates, control pane handoffs. Coordinates agent squads using work items with clear ownership. Kanban board tracks work item state. Merge gates enforce quality before integration. Control pane enables handoffs between agents. Maps directly to our 3-agent ops model: Engine/Verdict/Miss as squad with work items (per-language OCR tasks), ownership (Engine owns build, Verdict owns verify, Miss owns fix+apply), Kanban (lane A/B/C boards), merge gates (verification-loop), control pane (unified-memory handoffs).
- **decision_it_changes**: W6 architecture choice: team-agent-orchestration skill as backbone for 3-agent ops model execution
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists in ECC; 3-agent ops model locked per campaign law; unified-memory enables control pane handoffs; Kanban maps to lane A/B/C tracking

## Record 2 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/ralphinho-rfc-pipeline/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Ralphinho RFC Pipeline: RFC-driven multi-agent DAG execution with quality gates, merge queues, work unit orchestration. RFCs define work units; DAG defines dependencies; quality gates at each node; merge queue sequences integration. Maps to our PPT_SPEC Phase 6: each engine build = RFC work unit; DAG = engine dependency graph; quality gates = verification-loop at each stage; merge queue = sequential integration into main pipeline. Campaign law: probe22 execution law §6.4 GT verdicts LOCKED; §10 closed — RFC pipeline must respect locked verdicts.
- **decision_it_changes**: W6 architecture choice: RFC-driven DAG for Phase 6 engine builds with quality gates respecting locked probe22 verdicts
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; probe22 verdicts locked; verification-loop provides quality gates; unified-memory enables merge queue state

## Record 3 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/santa-method/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Santa Method: multi-agent adversarial verification with convergence loop. Two independent review agents must both pass before output ships. Adversarial reviewers challenge each other's findings. Convergence loop iterates until agreement. Maps to our Verdict agent: dual-reviewer pattern ( santa-method) for OCR output verification. Engine produces, Verdict runs two independent verifiers (e.g., different models or prompts), both must pass. Convergence loop = fix-loop max 2 rounds (campaign law). Directly implements Adversarial Review paper's critic role.
- **decision_it_changes**: W6 architecture choice: santa-method dual-verifier for Verdict agent; convergence loop = fix-loop max 2 rounds
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign law fix-loop max 2 rounds matches convergence loop; Adversarial Review paper validates approach; offline pipeline supports dual verification

## Record 4 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/council/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Council skill: four-voice council for ambiguous decisions, tradeoffs, go/no-go calls. Structured disagreement before choosing. Use when multiple valid paths exist. Maps to our validation call at H44-48: W6 training decision happens AT THE CALL. Council provides structured disagreement framework for the call. Four voices could be: Engine lead, Verdict lead, Miss lead, Orchestrator. Campaign law: I (Orchestrator) hold the law, batch user decisions. Council formalizes this.
- **decision_it_changes**: W6 architecture choice: council framework for validation call decision-making (W6 training go/no-go)
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; validation call at H44-48 is decision point; Orchestrator batches decisions; no training until call

## Record 5 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/council-multi-model/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Council Multi-Model: adds optional external Codex critique after council produces decision draft. Sends compact draft + disagreement to OpenAI for attempt to break synthesis. Labels same-provider reviews honestly. Marks review absent when adapter unavailable. Requires explicit consent. Maps to our validation call: could add external model critique but campaign law says no paid keys. Would need local model alternative. Marks review absent if unavailable — honest-empty is correct per campaign law.
- **decision_it_changes**: W6 architecture choice: external critique at validation call — blocked by no paid keys; local model alternative needed
- **transfer**: DIES
- **transfer_harness_fact**: no paid keys blocks external Codex critique; local model alternative not specified; honest-empty correct per campaign law

## Record 6 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/verification-loop/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Verification Loop skill: comprehensive verification system for Claude Code sessions. Verifies work before claiming complete. Multi-stage: syntax, types, tests, security, performance, docs. Gates: each stage must pass before next. Maps to our campaign: Phase 6 engine build → verification-loop at each engine; Verdict agent runs verification-loop; Miss applies fixes; re-verification loop max 2 rounds. Campaign law: Verdict specifies fixes, Miss applies, Verdict re-verifies (fix-loop max 2 rounds).
- **decision_it_changes**: W6 architecture choice: verification-loop as mandatory gate for each engine build; fix-loop max 2 rounds enforced
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign law mandates fix-loop max 2 rounds; Verdict specifies, Miss applies, Verdict re-verifies; offline pipeline supports all stages

## Record 7 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/loop-design-check/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Loop Design Check: designs goal-oriented agent loops, reviews for 5 failure modes — spinning/burning tokens, Goodhart-gaming verifier, running wrong answer to completion, plus decidability, boundaries, fallback, judge independence, keep-judgment-with-human red lines. Two actions: WRITE loop (gate whether to build, define machine-decidable goal, pick loop type, pick skeleton) and REVIEW loop. Maps to our Engine/Verdict/Miss loop: must have machine-decidable goal (CER score per language), judge independence (Verdict independent from Engine), human judgment at validation call. Campaign law: validation call at H44-48 is human judgment gate.
- **decision_it_changes**: W6 architecture choice: loop-design-check applied to Engine→Verdict→Miss loop; CER score as machine-decidable goal; validation call as human judgment gate
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; CER per language is machine-decidable metric; validation call is human gate; fix-loop max 2 rounds prevents spinning

## Record 8 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/blueprint/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Blueprint skill: turns one-line objective into step-by-step construction plan for multi-session, multi-agent projects. Each step has self-contained context brief for fresh agent execution. Includes adversarial review gate, dependency graph, parallel step detection, anti-pattern catalog, plan mutation protocol. TRIGGER: user requests plan/blueprint/roadmap for complex multi-PR task. Maps to our campaign: PPT_SPEC is our blueprint; each engine build is a step with context brief; adversarial review gate = santa-method; dependency graph = engine DAG; parallel steps = Lane A/B/C; plan mutation = campaign law updates.
- **decision_it_changes**: W6 architecture choice: blueprint skill used to decompose PPT_SPEC into per-engine work units with context briefs
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; PPT_SPEC is blueprint; per-engine context briefs in unified-memory; adversarial review = santa-method

## Record 9 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/plan-orchestrate/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Plan-Orchestrate skill: reads plan document, decomposes into steps, designs per-step agent chain from ECC catalogue, emits ready-to-paste /orchestrate custom prompts. Generative only — never invokes /orchestrate itself. Maps to our campaign: reads PPT_SPEC, decomposes into 18 engine builds, designs agent chains (Engine build → Verdict verify → Miss fix), emits orchestrate prompts for each. Campaign uses this for Lane A/B/C orchestration.
- **decision_it_changes**: W6 architecture choice: plan-orchestrate drives per-engine agent chain generation for 18 languages
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; PPT_SPEC is plan; ECC agent catalogue has Engine/Verdict/Miss roles; offline pipeline executes chains

## Record 10 (from artifact_220_ecc_skills_orchestration.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/dmux-workflows/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  DMux Workflows: multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode. Runs multiple agent sessions in parallel, coordinates multi-agent development. Maps to our campaign: dmux manages parallel Engine subagents (one per language), parallel Verdict verifiers, parallel Miss fixers. tmux panes = isolated worktrees per language. Coordination via unified-memory session log. Campaign uses this for Lane A/B/C parallel execution.
- **decision_it_changes**: W6 architecture choice: dmux-workflows for parallel 18-lang execution across Engine/Verdict/Miss lanes
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; tmux panes map to isolated worktrees; unified-memory coordinates; parallel-execution-optimizer uses this
