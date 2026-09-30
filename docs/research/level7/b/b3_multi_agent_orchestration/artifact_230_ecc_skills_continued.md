# artifact_230_ecc_skills_continued (converted from artifact_230_ecc_skills_continued.jsonl - all records, fields verbatim)

## Record 1 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/claude-devfleet/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Claude DevFleet: orchestrates multi-agent coding tasks via planning, dispatching parallel agents in isolated worktrees, monitoring progress, reading structured reports. Plans projects, dispatches parallel agents in isolated worktrees, monitors progress, reads structured reports. Maps to our campaign: Orchestrator plans 18 engine builds, dispatches Engine agents in isolated worktrees (one per language), monitors via structured reports, Verdict/Miss similarly dispatched. DevFleet reports map to our validation call evidence package.
- **decision_it_changes**: W6 architecture choice: claude-devfleet for dispatching 18 parallel Engine agents in isolated worktrees with structured reports
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; isolated worktrees per language; structured reports feed validation call; parallel-execution-optimizer uses this

## Record 2 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/unified-memory/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Unified Memory: shares durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other agents through local ECC Memory Vault. Agent saves work state, transfers context, resumes another agent's task, searches shared project knowledge. Maps to our campaign: Engine saves engine build state per language; Verdict reads Engine state, writes verification results; Miss reads both, applies fixes, writes fix state; all via unified-memory. Validation call reads full trace. Campaign law: honest-empty is correct — unified-memory stores only measured evidence.
- **decision_it_changes**: W6 architecture choice: unified-memory as backbone for Engine→Verdict→Miss handoffs and validation call evidence
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; local Memory Vault; honest-empty principle enforced; all 3 agents share vault; validation call reads vault

## Record 3 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/orch-pipeline/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Orchestrator Pipeline (shared engine for orch-* skills): classifies request size (trivial/small/standard/large). Five operation skills: orch-add-feature, orch-change-feature, orch-fix-defect, orch-refine-code, orch-build-mvp. Phases: 0 Intake, 1 Research & Reuse (gh search, Context7, vendor docs, package registries, Exa), 2 Plan (delegate to planner/architect, output task_list as thin vertical slices) -> GATE 1, 3 Scaffold (orch-build-mvp only), 4 Implement TDD (tdd-guide: red-green-refactor) -> GATE 2, 5 Review (code-reviewer + security-reviewer), 6 Commit. Two gates: Gate 1 after Plan (present task_list, no impl until user approves), Gate 2 before Commit (diff summary + messages, no commit until user confirms). Maps to our Phase 6: each engine build follows this pipeline; Gate 1 = validation call approval; Gate 2 = W6 freeze commit.
- **decision_it_changes**: W6 architecture choice: orch-pipeline governs each engine build; Gate 1 = validation call; Gate 2 = W6 freeze
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign law has validation call at H44-48 (Gate 1) and W6 freeze after Wed 2026-10-01 (Gate 2); TDD enforced

## Record 4 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/orch-add-feature/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Orch-Add-Feature: orchestrates building brand-new feature end-to-end — research, plan, TDD implementation, review, gated commit — delegating each phase to matching ECC agent. Maps to our engine builds: each new OCR engine for a language is a 'new feature' built via this pipeline. Engine agent handles research/plan/TDD, Verdict handles review, Miss handles gated commit. But campaign law: no training until W6 freeze — engine builds use existing backbones, not novel training.
- **decision_it_changes**: W6 architecture choice: orch-add-feature pipeline for each engine build using existing backbones (no novel training)
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; engine builds use existing indicphotoocr/sarvam backbones; no training until W6 freeze; TDD with existing models

## Record 5 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/orch-build-mvp/SKILL.md
- **date**: 2026-06-11
- **status**: DERIVED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Orch-Build-MVP: bootstraps working MVP from design/spec — ingest doc, plan thin vertical slices, scaffold first end-to-end slice, then TDD-implement, review, gated commit. Maps to our campaign: PPT_SPEC is design doc; first engine (e.g., indicphotoocr for Hindi) is MVP slice; then replicate pattern for 17 remaining languages. Phase 6 in progress (indicphotoocr in progress per campaign state).
- **decision_it_changes**: W6 architecture choice: orch-build-mvp for first engine slice; replication pattern for remaining 17 languages
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; PPT_SPEC is design; indicphotoocr in progress is MVP slice; replication pattern for 17 langs; no training

## Record 6 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/parallel-execution-optimizer/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Parallel Execution Optimizer: does task much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, many independent verification lanes without losing correctness. Maps to our Lane A/B/C: Lane A (Engine) builds 18 engines in parallel across isolated worktrees; Lane B (Verdict) verifies 18 engines in parallel; Lane C (Miss) applies fixes + monitoring in parallel. Batched tool calls for unified-memory reads/writes. Campaign target: engines landing tonight, validation call H44-48.
- **decision_it_changes**: W6 architecture choice: parallel-execution-optimizer config for 18-lang parallel lanes A/B/C with isolated worktrees
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; 18 langs × 100 samples lock = 1800 independent units; isolated worktrees per lang; batched unified-memory ops

## Record 7 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/terminal-ops/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Terminal-Ops: evidence-first repo execution workflow. Runs commands, checks repo, debugs CI failures, pushes narrow fixes with exact proof of execution and verification. Maps to our campaign: Engine runs engine build commands with evidence; Verdict runs verification commands with evidence; Miss runs fix commands with evidence. All proof stored in unified-memory. Campaign law: every record carries PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD and names decision it can change.
- **decision_it_changes**: W6 architecture choice: terminal-ops for all agent command execution with evidence logging to unified-memory
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; evidence law enforced; unified-memory stores proof; 18 langs × 100 samples = 1800 evidence records

## Record 8 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/delivery-gate/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Delivery Gate: stop hook blocking Claude from finishing until quality checks pass. Detects rationalization patterns (surface text heuristics), stale learning logs (filesystem mtime), low disk space. Complements self-audit by mechanically enforcing learning capture. Maps to our campaign: blocks Engine from declaring engine build done until verification-loop passes; blocks Verdict from declaring verify done until santa-method dual-review passes; blocks Miss from declaring fix done until re-verification passes. Campaign law: fix-loop max 2 rounds.
- **decision_it_changes**: W6 architecture choice: delivery-gate hooks on each agent to enforce verification-loop, santa-method, fix-loop max 2 rounds
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign law fix-loop max 2 rounds; verification-loop mandatory; santa-method dual-review mandatory

## Record 9 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/agent-architecture-audit/SKILL.md
- **date**: 2026-06-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Agent Architecture Audit: full-stack diagnostic for agent/LLM apps. Audits 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures, hidden repair loops, rendering corruption. Produces severity-ranked findings with code-first fixes. Maps to our campaign: could audit Engine/Verdict/Miss agent stack before validation call. But campaign law: W5 freeze after Wed 2026-10-01; W6 training decision at call. Audit would be pre-call check.
- **decision_it_changes**: W6 architecture choice: agent-architecture-audit as pre-validation-call health check for 3-agent stack
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; pre-call audit fits timeline; W5 freeze after 2026-10-01; validation call H44-48

## Record 10 (from artifact_230_ecc_skills_continued.jsonl)
- **source_url**: https://github.com/affaan-m/ECC/blob/main/skills/continuous-agent-loop/SKILL.md
- **date**: 2026-06-11
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Continuous Agent Loop: patterns for continuous autonomous agent loops with quality gates, evals, recovery controls. Loop must self-check, gate on evals, recover from failures. Maps to our Engine→Verdict→Miss loop: continuous until CER targets met per language. Quality gates = verification-loop at each stage. Evals = CER measurement per language. Recovery = Miss applies fixes, Verdict re-verifies (max 2 rounds). Campaign ends ~04:23 IST Tue Sep 29; loop runs until then.
- **decision_it_changes**: W6 architecture choice: continuous-agent-loop pattern for Engine→Verdict→Miss until CER targets or campaign end
- **transfer**: SURVIVES
- **transfer_harness_fact**: skill exists; campaign end ~04:23 Sep 29; CER targets per language; fix-loop max 2 rounds recovery
