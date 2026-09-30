# artifact_240_arxiv_papers_advanced (converted from artifact_240_arxiv_papers_advanced.jsonl - all records, fields verbatim)

## Record 1 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2605.00410
- **date**: 2026-05-01
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Agent Capsules (arXiv:2605.00410): adaptive runtime treating multi-agent pipeline as optimization with empirical quality constraints. Instruments coordination overhead per group, scores composition opportunity, selects among 3 compound execution strategies (standard, two-phase, sequential), gates every mode switch on rolling-mean output quality. Escalation ladder recovers quality by un-merging (moving toward per-agent dispatch) not rewriting prompts. Against LangGraph 14-agent pipeline: 51% fewer fine-mode tokens, 42% fewer compound tokens at +0.020/+0.017 quality. Against DSPy 5-agent: 19% fewer tokens at parity, 68% fewer than MIPROv2 at +0.052. First system treating multi-agent execution as group-level optimization with empirical quality gates. Maps to our 18-lang OCR: 1800 calls (18×100) — compound execution could save significant tokens but quality gates essential for weak cells (Santali 53.91, Kashmiri 54.82).
- **decision_it_changes**: W6 architecture choice: Agent Capsules pattern for compound execution with quality gates in 18-lang OCR pipeline
- **transfer**: SURVIVES
- **transfer_harness_fact**: 1800 calls benefit from compound execution; quality gates essential for weak cells; offline pipeline supports rolling-mean quality monitoring; no training needed for runtime controller

## Record 2 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2607.25152
- **date**: 2026-07-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Self-Evaluation Bias in Long-Running Agent Loops (arXiv:2607.25152): agents grading own work suffer 'progress mirage' — 54 cycles, agent claimed improvement every time, 56% had measured delta ≤0. Self-report uninformative; self-verdict gate degenerated to accept-all, eroding best state by 19%. Even strong in-band judge (full artifact+diff+history) accepted 44% regressions, rejected 38% improvements. On boundary task with artifact-verifiable success, mirage vanished to zero. Sign-only variant (accept/reject only) kept output similar to full feedback (110 vs 113), locating benefit in gate's grounding not feedback content. For open-ended objectives, out-of-band evaluation with real-world access is structural requirement. Maps to our campaign: Engine self-eval insufficient; Verdict (external verifier) + Miss (applier) provides out-of-band grounding. Campaign law: Verdict specifies fixes, Miss applies, Verdict re-verifies — exactly this structure.
- **decision_it_changes**: W6 architecture choice: confirms Engine/Verdict/Miss separation — Engine cannot self-verify; Verdict provides out-of-band verification
- **transfer**: SURVIVES
- **transfer_harness_fact**: 3-agent ops model separates generation from verification; verification-loop provides out-of-band grounding; fix-loop max 2 rounds prevents accept-all erosion

## Record 3 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2511.17330
- **date**: 2025-11-17
- **status**: MEASURED
- **relevance**: 3
- **recency**: 3
- **actionability**: 2
- **extraction**:

  Agentic Verification of Software Systems (arXiv:2511.17330): proof agent integrated with AI coding agents for generate-and-validate loop. Evaluated on SV-COMP benchmarks and Linux kernel modules. Promising efficacy for automated program verification. Maps to our Verdict agent: could use formal verification for OCR output correctness. But OCR verification is visual/perceptual, not formal logic. CER scoring is empirical, not provable. Formal verification not applicable to weak cell OCR quality assessment.
- **decision_it_changes**: W6 architecture choice: formal verification not applicable to OCR quality — empirical CER scoring required
- **transfer**: DIES
- **transfer_harness_fact**: OCR quality is perceptual/empirical (CER), not formal logic; weak cells need empirical measurement; no formal spec for 200-dpi citizen docs

## Record 4 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2603.11445
- **date**: 2026-03-11
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 3
- **extraction**:

  Verified Multi-Agent Orchestration (VMAO): coordinates specialized LLM agents through verification-driven iterative loop. Plan-Execute-Verify cycle with formal verification. But requires formal specs and verification tools. Maps to our campaign: we have empirical verification (CER scoring) not formal. VMAO's formal verification doesn't transfer to OCR. However, verification-driven iterative loop pattern matches our Engine→Verdict→Miss fix-loop.
- **decision_it_changes**: W6 architecture choice: verification-driven iterative loop pattern yes; formal verification no
- **transfer**: PARTIAL
- **transfer_harness_fact**: verification-driven loop pattern transfers (Engine→Verdict→Miss); formal verification dies (no formal spec for OCR); empirical CER replaces formal proofs

## Record 5 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2602.03786
- **date**: 2026-02-03
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 2
- **extraction**:

  AOrchestra: Automating Sub-Agent Creation for Agentic Orchestration. Dynamically creates sub-agents based on task decomposition. But requires LLM to design sub-agent roles, prompts, tools dynamically. Maps to our campaign: Engine builds 18 language engines — could dynamically create per-language sub-agents. But campaign law: probe22 GT verdicts LOCKED (§6.4); engine designs fixed per language. Dynamic sub-agent creation adds unpredictability. Fixed per-language engine configs preferred.
- **decision_it_changes**: W6 architecture choice: fixed per-language engine configs over dynamic sub-agent creation (locked probe22 verdicts)
- **transfer**: DIES
- **transfer_harness_fact**: probe22 GT verdicts LOCKED; engine designs fixed; dynamic creation adds unpredictability; offline pipeline needs determinism

## Record 6 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2608.15032
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 2
- **extraction**:

  Handoff-H1: Orchestrated Vision-Agent System for takeoff. Three layers earning results in combination: purpose-built vision encoder, agent controller, handoff protocol. Vision-agent handoff for multimodal tasks. Maps to our OCR: vision encoder = OCR backbone (indicphotoocr/sarvam_vision); agent controller = Engine; handoff protocol = Engine→Verdict→Miss. But Handoff-H1 is for vision-language-action (robotics), not document OCR. Vision encoder frozen backbone matches our no-training constraint.
- **decision_it_changes**: W6 architecture choice: frozen vision encoder (no training) matches campaign law; handoff protocol maps to Engine→Verdict→Miss
- **transfer**: PARTIAL
- **transfer_harness_fact**: frozen backbone survives (no training); vision-agent handoff pattern transfers; robotics domain doesn't transfer; 200-dpi citizen docs not robotics

## Record 7 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2606.13707
- **date**: 2026-06-10
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: 2
- **extraction**:

  Orchestra-o1: Omnimodal Agent Orchestration. Coordinates agents across modalities (text, vision, audio). Multi-agent orchestration for omnimodal tasks. Maps to our OCR: single modality (vision→text). Omnimodal overkill. But orchestration principles transfer: specialist agents per modality → specialist engines per language. However, campaign has 18 fixed languages, not dynamic modality routing.
- **decision_it_changes**: W6 architecture choice: specialist per language (fixed) not dynamic modality routing
- **transfer**: PARTIAL
- **transfer_harness_fact**: specialist-per-language pattern survives; omnimodal routing dies (single modality); fixed 18 langs not dynamic

## Record 8 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2607.22917
- **date**: 2026-07-22
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Agent Team Work Zone (arXiv:2607.22917): shared workspace for multi-agent collaboration with explicit state management. Agents operate in shared 'work zone' with structured state transitions. Reduces context confusion in multi-agent systems. Maps to our unified-memory: shared workspace = Memory Vault. Explicit state transitions = Engine build → Verdict verify → Miss fix → re-verify. Campaign law: honest-empty state tracking. Work zone pattern validates unified-memory design.
- **decision_it_changes**: W6 architecture choice: unified-memory as shared work zone with explicit state transitions per campaign law
- **transfer**: SURVIVES
- **transfer_harness_fact**: unified-memory skill is shared work zone; honest-empty = explicit state tracking; campaign law enforces state discipline

## Record 9 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2606.03115
- **date**: 2026-06-03
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  SPOQ (arXiv:2606.03115): Self-Prompting Optimization for Quality. Agents self-optimize prompts based on quality feedback. Iterative prompt refinement with quality gates. Maps to our Engine agent: could self-optimize per-language engine prompts based on CER feedback from Verdict. But campaign law: no training until W6 freeze; prompt optimization is training-adjacent. Verdict provides CER feedback, Miss applies fixes — prompt changes would be 'fixes' applied by Miss, not Engine self-optimization.
- **decision_it_changes**: W6 architecture choice: prompt optimization via Miss fixes (not Engine self-optimization) to respect no-training constraint
- **transfer**: SURVIVES
- **transfer_harness_fact**: Miss applies fixes including prompt tweaks; Engine doesn't self-optimize; no training until W6 freeze; CER feedback drives fixes

## Record 10 (from artifact_240_arxiv_papers_advanced.jsonl)
- **source_url**: https://arxiv.org/abs/2603.24621
- **date**: 2026-03-24
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: 1
- **extraction**:

  ARC-AGI-3: New challenge for frontier agentic intelligence. Benchmark for agentic reasoning. Not directly applicable to OCR. But demonstrates multi-agent evaluation frameworks. Maps to our campaign: we need OCR-specific eval (CER per language), not ARC-AGI. However, evaluation framework principles transfer: controlled, reproducible evals with clear success metrics.
- **decision_it_changes**: W6 architecture choice: controlled reproducible eval framework (CER per language) not ARC-AGI benchmark
- **transfer**: PARTIAL
- **transfer_harness_fact**: eval framework principles survive; ARC-AGI benchmark dies (wrong domain); CER per language is our eval metric
