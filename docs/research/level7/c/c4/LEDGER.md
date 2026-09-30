# Lane C4 — Tooling-Landscape Ledger (100 records)

Format law: `LEDGER_FORMAT.md`. Score = relevance × recency × actionability;
≥30/125 enters the integrated architecture. Verdict sample: every 10th record.
Weak cells: Santali 53.91 / Kashmiri 54.82 / OldScan 55.3 / Odia 80.01.

## T1 — Claude Code (C4-001–014)

[C4-001] Claude Code 2.0: multi-agent orchestration + persistent memory
source_url: https://claude5.ai/news/anthropic-claude-code-v2-agentic-features-launch
date: 2026-02-24 | status: VERIFIED | relevance: 5 | recency: 3 | actionability: 4 | score: 60/125
extraction:
- Mechanism: orchestrator mode spawns specialized subagents (analysis/implement/test/PR) from one instruction; sessions persist project context across runs.
- Result: early users report 9/12 backlog issues resolved autonomously with skip-notes.
- Maps to OUR workflow: the probe22 executor pattern (sequential engines + stale-copy failure of 2026-09-26) is exactly what persistent-memory + orchestrator mode prevents — executor agents re-reading current run_probe.py instead of stale copies.
- Serves OldScan 55.3 indirectly: orchestrated retry passes (--retry-errors) over slow scans (bn_d014 73-78s) without human babysitting.

[C4-002] Claude Code CLAUDE.md standing-memory files
source_url: https://claude.com/blog/scaling-agentic-coding
date: 2025-10-15 | status: VERIFIED | relevance: 5 | recency: 2 | actionability: 5 | score: 50/125
extraction:
- Mechanism: project-level CLAUDE.md captures env, test standards, architectural patterns; agents re-align every session.
- Result: onboarding drops from weeks to 1-2 days; consistent implementations across sessions.
- Maps to OUR workflow: this is the proven pattern behind AGENT_PROTOCOL.md §§0-10 — standing law the executors violated (parallel engines) when they ran stale copies. Lesson: protocol files must be re-read at session start, enforced by hook, not by trust.
- Serves all weak cells: prevents GT-gate regressions (MAX_CTRL_CHARS=3) during Phase 5/6.

[C4-003] Rakuten 7-hour autonomous implementation in 12.5M-line codebase
source_url: https://claude.com/blog/introduction-to-agentic-coding
date: 2026-06-21 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: Claude Code sustained 7h autonomous work (context gathering → plan → execute → verify) in vLLM-scale repo; 79% faster feature delivery (24d→5d).
- Result: evidence that long-horizon agent runs (our indicphotoocr ~12h, paddle ~8-20h) are tractable under orchestration with verification loops.
- Maps to OUR workflow: justifies keeping heavy engines sequential-but-unattended with --skip-existing resume instead of parallelizing (which caused the §5 violation + memory risk).
- Serves Kashmiri 54.82: Nastaliq-specialist experiments need multi-hour unattended runs.

[C4-004] Claude Code TDD skills (red → green → refactor loop)
source_url: https://claude-codex.fr/en/future/trends-2026
date: 2026-05-09 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: agent generates tests first (red), writes minimal implementation (green), refactors; 2026 trend toward agent-executed TDD.
- Result: routine workflows (boilerplate, test creation) fully delegated with human review at the end.
- Maps to OUR workflow: metrics.py scorer patches (§6.5: empty=1.0, space-forgery removal, uncapped CER) should have been TDD-gated — a red test asserting "empty pred scores 1.0 and counts" would have caught the exclusion bug before the hostile audit did.
- Serves every CER claim on weak cells: scorer TDD prevents forged zeros on Santali/Odia fill cells.

[C4-005] Thoughtworks Radar: Claude Code to Adopt (Nov 2025)
source_url: https://www.thoughtworks.com/en-us/radar/tools/claude-code
date: 2025-11-05 | status: VERIFIED | relevance: 3 | recency: 2 | actionability: 3 | score: 18/125
extraction:
- Mechanism: org-scale adoption review; pairs adoption with context engineering, curated shared instructions, agent teams; warns of complacency with AI-generated code.
- Result: benchmark status for capability/usability among CLI agents.
- Maps to OUR workflow: validates the 3-agent ops model (Engine/Verdict/Miss) + curated instructions (AGENT_PROTOCOL.md) over ad-hoc executor prompts.
- Weak-cell link: none direct — context only (below threshold, kept per contradiction rule, not dropped).

[C4-006] Claude Agent SDK (same harness as Claude Code, embeddable)
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: Claude Agent SDK exposes the exact harness (context compression, tool-result management) powering Claude Code for custom apps.
- Result: builders reuse production harness instead of reimplementing session management.
- Maps to OUR workflow: a future probe-runner service (post-freeze W6) could embed the SDK for session resume across the 8-20h paddle runs instead of bare --skip-existing files.
- Serves OldScan 55.3: long worst-case scans (4250×6500) need harness-level checkpointing.

[C4-007] Agentic coding: quality-gatekeeper pattern under deadline pressure
source_url: https://claude.com/blog/key-benefits-transitioning-agentic-coding
date: 2025-12-01 | status: VERIFIED | relevance: 3 | recency: 2 | actionability: 3 | score: 18/125
extraction:
- Mechanism: agents enforce style/security/docs systematically regardless of deadline pressure; multi-file consistency.
- Result: fewer production incidents, slower tech-debt accumulation.
- Maps to OUR workflow: the stale-copy bilingual failure (100 sa packs FileNotFoundError) is a consistency failure a gatekeeper hook (verify run_probe.py hash before engine start) would catch.
- Context only (below threshold).

[C4-008] Claude Code + vLLM backend (local/private coding assistance)
source_url: https://github.com/AMD-AGI/vllm-2026/blob/main/docs/serving/integrations/claude_code.md
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: ANTHROPIC_BASE_URL points Claude Code at a vLLM server; any tool-calling model becomes the backend.
- Result: fully local/private agent runs, custom-model testing.
- Maps to OUR workflow: post-freeze, a fine-tuned Indic VLM served via vLLM could sit behind the same agent harness that runs probe analysis — one harness, swap the model (relevant to Qwen2-VL/InternVL2 P2, which needs GPU + approval).
- Serves Kashmiri 54.82 / Santali 53.91: local specialist models testable without API spend.

[C4-009] Xcode 26.3 agentic coding with MCP support expected
source_url: https://www.infoq.com/news/2026/02/xcode-26-3-agentic-coding/
date: 2026-02-09 | status: VERIFIED | relevance: 2 | recency: 3 | actionability: 2 | score: 12/125
extraction:
- Mechanism: IDE-embedded agents (Claude Agent, Codex) with doc search, file exploration, preview-verified code; MCP support expected.
- Result: agentic coding moves inside IDEs, not just terminals.
- Maps to OUR workflow: negligible direct use (probe runs in terminal), but confirms MCP as the cross-harness standard — invest in MCP, not IDE-specific glue.
- Context only.

[C4-010] Multimodality trend: screenshot→reproduce-and-fix via Claude Code
source_url: https://claude-codex.fr/en/future/trends-2026
date: 2026-05-09 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: sending a bug screenshot / whiteboard photo to the agent (via audio/image MCP) to reproduce, fix, or generate base code.
- Result: visual inputs become first-class agent context in 2026.
- Maps to OUR workflow: §6.4 human GT verification is visual (judge GT against the image) — a vision-capable agent pass could pre-flag suspect PDF-layer items (e.g. ne_o037 control-char corruption) before humans spend ~2h, prioritizing the VERIFY-FIRST langs (ks/mr/gu/ur).
- Serves Kashmiri 54.82 + OldScan 55.3: visual pre-screen of degraded scans.

[C4-011] Curated shared instructions + context engineering (Adopt, Apr 2026)
source_url: https://www.thoughtworks.com/en-us/radar/tools/claude-code
date: 2026-04-01 (Radar Apr 2026 ed.; accessed 2026-09-26) | status: INFERENCE | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: progressive context disclosure + curated shared instructions as the adopted technique for agent teams.
- Result: agents stay aligned without prompt bloat.
- Maps to OUR workflow: AGENT_PROTOCOL.md is already this pattern; the INFERENCE is that executor prompts should be split into stable law (protocol file) vs per-phase deltas, so stale-copy drift is structurally impossible.
- Serves all weak cells via process reliability.

[C4-012] Claude Code CI/CD native integration (PR-triggered review/fix)
source_url: https://claude5.ai/news/anthropic-claude-code-v2-agentic-features-launch
date: 2026-02-24 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 3 | score: 27/125
extraction:
- Mechanism: GitHub Actions/GitLab/Jenkins triggers run reviews, suggest fixes, update PRs without custom webhooks.
- Result: review automation inside existing pipelines.
- Maps to OUR workflow: Phase 6 scoring + sheet.csv appends could run as a CI job per completed engine (fail if pack count ≠ manifest n), catching the bilingual sa-path failure at write time, not days later.
- Serves Odia 80.01 reporting integrity. Just below threshold — context.

[C4-013] Team collaboration mode with shared context log + AI-vs-human attribution
source_url: https://claude5.ai/news/anthropic-claude-code-v2-agentic-features-launch
date: 2026-02-24 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 2 | score: 18/125
extraction:
- Mechanism: shared instance tracks suggestion provenance, prevents conflicting AI changes across branches.
- Result: multi-dev + multi-agent coordination without clobbering.
- Maps to OUR workflow: mirrors the 3-agent ops model need — Engine/Verdict/Miss writing to disjoint dirs with attribution (cf. C4 lane dirs). Context only.

[C4-014] Terminal-agent vs IDE-agent vs autocomplete coexistence (2026 practice)
source_url: https://claude-codex.fr/en/future/trends-2026
date: 2026-05-09 | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: practitioners combine Copilot (autocomplete) + Claude Code (complex tasks) + Cursor Composer (visual diffs).
- Result: no single harness wins; task-matched tooling.
- Maps to OUR workflow: endorses our split — terminal probe runners + ledger docs + verification scripts, each with the right tool. Context only.

## T2 — Kimi (C4-015–026)

[C4-015] Kimi K2: 1T-MoE open-weight agentic model (32B active, Jul 2025)
source_url: https://kimik2ai.com/k2/
date: 2025-07-01 | status: VERIFIED | relevance: 4 | recency: 2 | actionability: 3 | score: 24/125
extraction:
- Mechanism: 1T total / 32B active MoE, 128K context, agentic-first tuning; Base + Instruct under Modified MIT; SWE-bench Verified 65.8%, tau2-airline 80%.
- Result: top-tier open agentic coding at release; K2.5 (Jan 2026) 76.8%, K2.6 (Apr 2026) 80.2% SWE-bench.
- Maps to OUR workflow: candidate open backend for probe-analysis agents and (P2, GPU-gated) document-AI experiments — same cost logic as the Qwen2-VL/InternVL2 P2 decision.
- Serves all weak cells as cheap analysis compute. Below threshold — context.

[C4-016] Kimi K2.7 Code: dedicated open-source agentic coding model (Sep 2026)
source_url: https://www.kimi.ai/resources/kimi-k2-7-code
date: 2026-09-14 | status: VERIFIED | relevance: 4 | recency: 5 | actionability: 3 | score: 60/125
extraction:
- Mechanism: coding-focused agentic model for long-horizon software engineering; API with context caching ($0.19 cache-hit vs $0.95 miss per 1M input tokens), 262K context.
- Result: cheapest long-context agentic coding loop currently documented; cache-hit pricing rewards repeated runs over the same repo.
- Maps to OUR workflow: repeated probe-analysis loops (re-score, re-verify, re-rank) over the same 1,227-item manifest are exactly the cache-friendly workload — run analysis agents on K2.7-code with cached manifest context instead of re-uploading.
- Serves Santali 53.91 / Kashmiri 54.82: cheap iteration on specialist-routing analysis for n=20 cells.

[C4-017] Kimi K2 series discontinued 2026-05-25; migrate to K2.6+
source_url: https://platform.kimi.ai/docs/models
date: 2026-05-25 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 4 | score: 48/125
extraction:
- Mechanism: vendor sunset the K2 line; K2.6/K2.7-code are the supported path.
- Result: pinning to K2-0711-preview (as in old Cline/RooCode guides) is now a rot risk.
- Maps to OUR workflow: direct lesson for probe22 — the stale-copy failure was version drift; any Kimi-backed analysis must pin kimi-k2.7-code or K2.6, never a preview ID. Same discipline as tessdata_best pinning.
- Process reliability for all weak-cell work.

[C4-018] Kimi K2 tool-calling: ~100% accuracy on official API + Enforcer/JSON mode
source_url: https://platform.moonshot.ai/docs/guide/kimi-k2-quickstart
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: official API tool-call accuracy ~100%; Enforcer + JSON mode stabilize tool-arg formatting; 10+ built-in tools (web search); 256K context on thinking/turbo variants.
- Result: reliable multi-step agent workflows (complex task decomposition → executable tool calls).
- Maps to OUR workflow: tool-call reliability is the load-bearing property for scorer/ledger automation (metrics.py invocations, sheet.csv appends with exact columns). Kimi-backed agents can drive Phase 6 mechanics if Claude is saturated.
- Serves Odia 80.01: dependable re-scoring loops over the 69-item or-cell with CIs.

[C4-019] Kimi in Cline/RooCode via Anthropic-compatible API (VS Code agents)
source_url: https://platform.moonshot.ai/docs/guide/agent-support
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 3 | score: 24/125
extraction:
- Mechanism: kimi-k2 models plug into Cline/RooCode as Anthropic-compatible endpoint (base_url api.moonshot.ai/v1, temp 0.6, 128K window).
- Result: any Anthropic-shaped harness can swap in Kimi.
- Maps to OUR workflow: harness-portability proof — our agent prompts (PROMPT_*_AGENT.md) should stay model-agnostic the same way, so Engine/Verdict/Miss agents survive a model swap. Below threshold — context.

[C4-020] K2 Thinking: reasoning_content trace exposed for debugging
source_url: https://kimik2ai.com/k2/
date: 2025-07-01 | status: VERIFIED | relevance: 3 | recency: 2 | actionability: 3 | score: 18/125
extraction:
- Mechanism: reasoning_content in API response gives the full chain-of-thought for debugging agent trajectories.
- Result: failed multi-step runs are diagnosable, not opaque.
- Maps to OUR workflow: same need as the executor post-mortem (stale copy vs genuine slow scans) — agent trajectories over probe runs must be logged and inspectable. Context only.

[C4-021] Kimi 50+ language training, BLEU>30 on FLORES-200 (35 langs)
source_url: https://kimi-k2.net/
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 2 | score: 18/125
extraction:
- Mechanism: mass multilingual pretraining; sparse Top-2 gating over 64 experts keeps inference at 32B-dense cost.
- Result: broad language coverage cheaply — relevant to long-tail scripts.
- Maps to OUR workflow: weak INFERENCE-level support for using Kimi as a second-opinion scorer on Perso-Arabic WER-primary cells (ur/sd/ks) — never as GT, only as analysis. Context only.

[C4-022] Kimi Code CLI: terminal-native coding workflows on same model
source_url: https://kimik2ai.com/k2/
date: 2025-07-01 | status: VERIFIED | relevance: 2 | recency: 2 | actionability: 2 | score: 8/125
extraction:
- Mechanism: same K2 weights via web, API, self-host (vLLM/SGLang/TensorRT-LLM), or CLI.
- Result: one model, every surface.
- Maps to OUR workflow: supports the "one harness, swappable model" stance (cf. C4-008). Context only.

[C4-023] K2.5 multimodal (vision) release — K2-line gains image understanding
source_url: https://platform.moonshot.ai/docs/guide/kimi-k2-quickstart
date: 2026-01-01 (K2.5 Jan 2026 per kimi docs; accessed 2026-09-26) | status: INFERENCE | relevance: 4 | recency: 3 | actionability: 2 | score: 24/125
extraction:
- Mechanism: K2.5 adds multimodal understanding to the K2 agent line (vision input alongside tool use).
- Result: Kimi agents can take page images as input, not just text.
- Maps to OUR workflow (INFERENCE): vision-capable Kimi agents could pre-screen §6.4 verification items (image vs GT mismatch flagging for ks/mr/gu/ur VERIFY-FIRST langs). Needs a live-source check before W6 use. Below threshold — context.

[C4-024] Kimi API pricing discipline: cache-hit 5× cheaper than miss
source_url: https://www.kimi.ai/resources/kimi-k2-7-code
date: 2026-09-14 | status: VERIFIED | relevance: 3 | recency: 5 | actionability: 4 | score: 60/125
extraction:
- Mechanism: automatic context caching; repeated context billed at $0.19 vs $0.95/1M tokens.
- Result: 5× cost gap between cache-friendly and cache-hostile agent design.
- Maps to OUR workflow: same economics as the Sarvam 54-call cap — design analysis prompts with a stable prefix (protocol + manifest summary) so repeat verification/ranking calls hit cache. Directly stretches the free-trial-style budget discipline to analysis.
- Serves all weak cells via affordable re-analysis.

[C4-025] Moonshot vendor verifier: third-party tool-call degradation warning
source_url: https://platform.moonshot.ai/docs/guide/kimi-k2-quickstart
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: docs warn tool-call performance drops on third-party open-source platforms vs official API; vendor verifier project tracks it.
- Result: self-hosted Kimi ≠ API Kimi for agentic reliability.
- Maps to OUR workflow: mirrors our cached-vs-upstream lesson (rapidocr/paddle cached-only routing; easyocr script-family weights). Benchmark the deployment you run, not the vendor's number — same reason "beat 87.39" stays directional (§6.8).
- Guards Kashmiri 54.82 / Santali 53.91 claims from benchmark-mismatch.

[C4-026] Kimi-K2-Base for fine-tuning control vs Instruct for agentic use
source_url: https://kimik2.com/
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 3 | actionability: 2 | score: 12/125
extraction:
- Mechanism: two-weight strategy — Base for customization, Instruct for out-of-box agency; both on HuggingFace in block-fp8.
- Result: clean split between train-customize and deploy-agent paths.
- Maps to OUR workflow: same split as W6 (train the OCR recipe) vs Lane C (agentic tooling around it) — do not conflate. Context only.

## T3 — OpenCode / ECC (C4-027–040)

[C4-027] OpenCode build vs plan agents (full-access vs read-only)
source_url: https://opencode.ai/docs/agents
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 5 | recency: 4 | actionability: 5 | score: 100/125
extraction:
- Mechanism: build = default full-access primary; plan = read-only (denies edits, asks before bash); plus general/scout/compaction subagents; per-agent permission blocks incl. bash glob patterns (e.g. `git *` → ask).
- Result: analysis-without-mutation is a first-class mode, not a prompt hack.
- Maps to OUR workflow: Verdict/Miss agents should run as plan-mode equivalents — the hostile audits reconciled cleanly because auditors couldn't mutate disk; executor agents get build-mode only inside level2/probe22/. This is the permission shape AGENT_PROTOCOL.md §0 needs.
- Serves every weak cell: prevents report/seal corruption (level2/out + level2/reports sealed).

[C4-028] OpenCode permissions: per-command bash gating (`bash: {git push: ask}`)
source_url: https://opencode.ai/docs/agents
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 5 | recency: 4 | actionability: 5 | score: 100/125
extraction:
- Mechanism: opencode.json permission trees gate edit/bash globally and per-agent, down to command globs.
- Result: least-privilege agents by config, no prompt obedience required.
- Maps to OUR workflow: encode §0 hard rules as permissions (deny writes to level2/out, level2/reports, Datasets/; deny network installs; ask on sarvam_vision beyond --limit-per-lang 3) so the parallel-engine violation becomes structurally impossible.
- Highest-actionability process control in this ledger.

[C4-029] OpenCode 75+ providers, model-neutral (Red Hat Dev Spaces writeup)
source_url: https://developers.redhat.com/articles/2026/04/22/opencode-model-neutral-ai-coding-assistant-openshift-dev-spaces
date: 2026-04-22 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: 75+ providers (Claude, GPT, Gemini, Ollama/local); MIT; air-gap compatible; single CLI across models.
- Result: no vendor lock-in; cost optimization by swapping models per task.
- Maps to OUR workflow: the 3-agent model can route cheap analysis (ranking, ledger checks) to cheap models and reserve frontier models for hostile-audit-grade review — same economics as C4-024.
- Serves Santali 53.91 / Kashmiri 54.82 via affordable agreement-rate analysis on fill cells.

[C4-030] OpenCode Zen marketplace + 205K stars / 950 contributors / 16M devs
source_url: http://opencode.ai/
date: 2026-09-22 (last-verified stamp; accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 5 | actionability: 2 | score: 20/125
extraction:
- Mechanism: most-starred open coding agent of 2026; Zen model marketplace; TUI + desktop + IDE surfaces.
- Result: largest contributor surface among open harnesses → fastest skill/MCP ecosystem growth.
- Maps to OUR workflow: ecosystem-momentum signal only; pick harnesses with plugin velocity for ledger/MCP needs. Context only.

[C4-031] OpenCode LSP auto-load for agent context
source_url: http://opencode.ai/
date: 2026-09-22 (accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 5 | actionability: 3 | score: 45/125
extraction:
- Mechanism: harness auto-loads the right language servers so the LLM sees syntax/type info in context.
- Result: fewer type/signature hallucinations in generated code.
- Maps to OUR workflow: probe-analysis code (metrics invocations, gt_forensics, manifest tooling) is Python — LSP-backed agents editing extract_gt.py/build_manifest.py gates make fewer signature errors. Adopt for any W6 training-script work.
- Serves Odia 80.01 via correct gate code (script-ratio/Latin thresholds).

[C4-032] OpenCode multi-session parallel agents + share links
source_url: http://opencode.ai/
date: 2026-09-22 (accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 5 | actionability: 3 | score: 60/125
extraction:
- Mechanism: multiple agents in parallel on one project; shareable session links for reference/debugging.
- Result: parallel lanes with auditable trajectories.
- Maps to OUR workflow: the sanctioned shape of our 3-agent ops model — BUT the §5 sequential-engine rule still binds inside one lane: parallelize lanes/analysis, never heavy engines (the 2026-09-26 parallel-engine memory violation is the counterexample).
- Serves OldScan 55.3: parallelize analysis, serialize inference.

[C4-033] OpenCode AI SDK provider (ai-sdk-provider-opencode-sdk) + Obsidian plugin
source_url: https://opencode.ai/docs/ecosystem/
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: Vercel AI SDK provider wraps OpenCode; OpenCode-Obsidian embeds the agent in Obsidian UI; ocx manages isolated profiles.
- Result: OpenCode agents callable from TS apps AND from the knowledge vault.
- Maps to OUR workflow: two integration endpoints for this campaign — (1) TS SDK route driving probe-analysis agents programmatically (cf. T7), (2) ledger docs readable/writable from the vault (cf. T5). Adopt both patterns for the integration pass.
- Serves Kashmiri 54.82: programmatic re-ranking loops over weak cells.

[C4-034] OpenCode scout subagent: external-docs/dependency research in managed cache
source_url: https://opencode.ai/docs/agents
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: scout clones dependency repos into managed cache, inspects upstream source, cross-references local code — without touching the workspace.
- Result: claims about upstream (model coverage, API behavior) checked against source, not memory.
- Maps to OUR workflow: this is exactly how the easyocr "urdu.pth/assamese.pth" audit premise SHOULD have been checked — script-family routing verified in installed source (which is what the reconciliation did manually). Make scout-pattern mandatory for P1/P2 upgrade claims (Bodhan, PaddleOCR-VL).
- Serves all weak cells via correct engine-capability claims.

[C4-035] SST lineage: OpenCode by Anomaly (formerly SST), MIT, client/server + mobile
source_url: https://innfactory.ai/en/ai-harness/opencode/
date: 2026-09-20 | status: VERIFIED | relevance: 2 | recency: 5 | actionability: 2 | score: 20/125
extraction:
- Mechanism: terminal-shop/neovim builders; client/server architecture allows remote driving (e.g. mobile).
- Result: long runs monitorable off-machine.
- Maps to OUR workflow: overnight paddle/surya runs need remote monitoring (RSS/watch), not presence. Context only.

[C4-036] OpenCode custom tools + agent skills extension model
source_url: https://open-code.ai/en
date: 2026-07-14 (accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 4 | score: 48/125
extraction:
- Mechanism: custom tools extend function; agent skills encode capabilities; MCP servers attach (docs list skills + MCP guides).
- Result: harness grows by composition, not forks.
- Maps to OUR workflow: package probe ops as skills — `score-engine` (gt_pred build + metrics.py both modes + sheet append), `verify-gt-sample` (§6.4 sampler writing gt_verification.json), `rank-lane` (score + threshold filter). Prevents command-drift across executor sessions.
- Serves Odia 80.01 + OldScan 55.3 via repeatable scoring.

[C4-037] Cursor harness SDK: same model scores higher inside a good harness
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: benchmarks show identical models scoring higher inside Cursor's harness vs others — the harness does real work (context mgmt, tool shaping).
- Result: harness choice is a capability multiplier, not plumbing.
- Maps to OUR workflow (INFERENCE-adjacent but source-verified): the stale-copy + parallel-engine failures were harness failures, not model failures — investing in harness (permissions, skills, resume) beats swapping models for executor reliability. Below threshold — context.

[C4-038] Pi harness: minimal Read/Bash/Edit/Write/Find/LS, maximal customizability
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: deliberately tiny toolset; workflow adapts to the team via extensions.
- Result: audit-friendly minimal surface.
- Maps to OUR workflow: executor agents need ~6 tools (read/run/score/append/sample/report) — Pi is the existence proof that a minimal probe-executor harness suffices. Context only.

[C4-039] Goose (Block OSPO): local general-purpose agent with desktop+CLI+API
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: open-source local agent beyond code (research, data analysis) via extensions.
- Result: local-first analysis compute.
- Maps to OUR workflow: local analysis of CER tables without shipping probe data to clouds — relevant given the sealed-reports discipline. Context only.

[C4-040] Mastra Harness primitive (Jun 2026): modes, threads, approvals, model switch
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026-06-01 (announced Jun 2026; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: interactive agents with multiple modes, persistent threads, tool approvals, model switching, Studio UI, built-in observability.
- Result: production-ready TS harness infrastructure.
- Maps to OUR workflow: the reference design for a post-freeze probe-orchestration service (persistent threads per engine run, approvals on credit-spending sarvam_vision calls, model switching per C4-029). Bridges to T7.
- Serves OldScan 55.3 via observable long runs.

## T4 — MCP servers (C4-041–054)

[C4-041] MCP spec: Tools / Resources / Prompts + Tasks, Skills-over-MCP, MCP Apps extensions
source_url: https://modelcontextprotocol.io/specification/draft
date: 2026 (draft spec; accessed 2026-09-26) | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 4 | score: 100/125
extraction:
- Mechanism: JSON-RPC 2.0 host→client→server; servers expose Tools (model-invoked actions), Resources (read-only context), Prompts (templates); extensions add Tasks (long-running async), Skills-over-MCP, MCP Apps (inline UI).
- Result: one integration (MCP) serves every client (Claude, ChatGPT, VS Code, Cursor).
- Maps to OUR workflow: expose probe ops as MCP tools — manifest query, pack status, metrics.py run, gt_verification sample — so Engine/Verdict/Miss agents share one interface instead of bespoke bash each. Tasks extension matches overnight engine runs; Skills-over-MCP matches C4-036 skills.
- Serves all weak cells via uniform, auditable tooling.

[C4-042] MCP 2026-07-28: "USB-C for AI apps" + official registry
source_url: https://modelcontextprotocol.io/docs/2026-07-28
date: 2026-07-28 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: latest versioned docs + official registry (registry.modelcontextprotocol.io) with versioned server discovery.
- Result: servers installable by version, not by git lore.
- Maps to OUR workflow: pin MCP server versions the way we pin tessdata_best/SEED=20260926 — reproducibility for the validation call. Count-from-disk applies to tool versions too.
- Process reliability for weak-cell evidence.

[C4-043] MCP donated to Linux Foundation / AAIF (Anthropic+Block+OpenAI), SEP process
source_url: https://www.paloaltonetworks.com/cyberpedia/what-is-model-context-protocol-mcp
date: 2026 (n.d.; donation Dec 2025; accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: no single vendor controls the spec; changes via community SEP; model-agnostic by charter.
- Result: safe long-term bet for harness investment (cf. C4-009: invest in MCP, not IDE glue).
- Maps to OUR workflow: de-risks building probe MCP tools — the interface outlives any single agent vendor. Below threshold — context.

[C4-044] MCP security: cross-server exfiltration, supply-chain, rug-pull attacks
source_url: https://www.paloaltonetworks.com/cyberpedia/what-is-model-context-protocol-mcp
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: malicious servers can poison agent context to weaponize legitimate tools; fake/tampered registry servers; post-approval tool-definition swaps → need least-privilege, auth, monitoring, continuous validation.
- Result: one-time approval is insufficient.
- Maps to OUR workflow: probe MCP tools must be read-scoped by default (manifest/packs/scores readable; writes only via explicit score/verify tools), servers pinned by hash, tool definitions re-validated per session — the MCP analogue of §0 rule 1 (no downloads) and the sealed-dirs rule.
- Serves every CER claim: a poisoned scoring tool forges leaderboards exactly like the old space-forgery bug did.

[C4-045] PaddleOCR ships an MCP Server (production deployment path)
source_url: https://www.paddleocr.ai/v3.4.1/en/version3.x/pipeline_usage/PaddleOCR-VL.html
date: 2026 (v3.4.1 docs; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: PaddleOCR documents MCP Server deployment alongside on-device/server/C++/parallel-inference paths.
- Result: SOTA doc-parsing (VL-1.6, 96.3% OmniDocBench v1.6) callable as an MCP tool.
- Maps to OUR workflow: PaddleOCR-VL-1.6 zero-shot is P2 (needs approval+GPU), but its MCP-server shape is the integration pattern to copy — our future fine-tuned recognizer should serve behind the same tool interface the probe agents already use.
- Serves OldScan 55.3: irregular-bbox + Real5 robustness behind one tool call.

[C4-046] Vercel AI SDK: MCP client + MCP server on Fluid Compute
source_url: https://vercel.com/kb/guide/ai-agents
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: AI SDK builds MCP clients (discover/call any server) and serves MCP servers on auto-scaling Fluid Compute; Redis for ephemeral agent storage.
- Result: TS-native MCP both directions with deployment solved.
- Maps to OUR workflow: if probe analysis moves to a service (post-freeze), the AI-SDK MCP client is how TS code calls our probe tools; Fluid pattern is the template for scaling verification/ranking jobs. Bridges to T7.
- Serves Kashmiri 54.82 via scalable re-analysis.

[C4-047] MCP multi-server composition (travel-planner pattern: resources + tools + prompt)
source_url: https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts
date: 2026-07-28 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: canonical pattern — one prompt orchestrates Resources (calendar/history) + Tools (flights/hotels/email) across servers; model picks checkWeather() when context demands.
- Result: task taking hours completes in minutes via composed servers.
- Maps to OUR workflow: Phase 6 as composition — manifest server (resources) + scorer server (tools) + verification sampler (tools) under one "score engine X" prompt. Copy this decomposition for the integration pass.
- Serves Odia 80.01 via repeatable per-engine scoring.

[C4-048] LitServe: any model API as MCP tool with zero glue code
source_url: http://lightning.ai/docs/litserve/features/mcp
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: /mcp/ endpoint exposes any LitAPI subclass per the MCP HTTP-stream spec; Claude Desktop/Cursor connect with config only.
- Result: controlled models join the agent ecosystem without custom integration.
- Maps to OUR workflow: post-W6, serve the frozen fine-tuned recognizer via an MCP endpoint so the SAME probe harness scores it head-to-head with the 10 engines — no new glue, same scorer, same CIs.
- Serves Santali 53.91 / Kashmiri 54.82: specialist models evaluated identically.

[C4-049] IBM: MCP Resources vs Tools vs Prompts separation + JSON-RPC transport
source_url: https://www.ibm.com/think/topics/model-context-protocol
date: 2025-05-09 | status: VERIFIED | relevance: 3 | recency: 2 | actionability: 3 | score: 18/125
extraction:
- Mechanism: Resources return data without side effects; Tools may act; Prompts templatize workflows; transports are JSON-RPC 2.0.
- Result: clean read/write separation at the protocol layer.
- Maps to OUR workflow: the read/write split our lanes need — Verdict/Miss agents get Resources+Prompts (ledger, protocol, scores), Engine agents get Tools (run/score/append). Context only (below threshold).

[C4-050] obra/knowledge-graph exposes 10 ops via CLI + MCP server (SQLite-vec, local)
source_url: https://github.com/obra/knowledge-graph
date: 2026-03-21 (created; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 3 | actionability: 4 | score: 48/125
extraction:
- Mechanism: vault → untyped graph (files=nodes, wikilinks=edges), SQLite + sqlite-vec + FTS5, local MiniLM embeddings; semantic search, path-finding, Louvain communities, PageRank — via CLI and MCP server; 76 vitest tests.
- Result: agents query the vault as a graph through MCP, no cloud APIs.
- Maps to OUR workflow: the research-ledger query layer — Verdict sampling + contradiction checks become graph queries (which records cite which weak cell / contradict which doc). Bridges to T5.
- Serves all weak cells via ledger navigability.

[C4-051] MCP Apps + elicitation: interactive UI + server-initiated input
source_url: https://modelcontextprotocol.io/specification/draft
date: 2026 (draft; accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 5 | actionability: 2 | score: 20/125
extraction:
- Mechanism: MCP Apps render charts/forms inline; elicitation lets servers request user input mid-run; clients offer sampling.
- Result: agents can show CER tables inline and ask for approvals without leaving the loop.
- Maps to OUR workflow: validation-call material (leaderboards, tier tables, CIs) renderable inside the agent session; sarvam_vision spend approvals via elicitation. Context only.

[C4-052] Kimi K2 drives Claude Code + MCP protocol (community report)
source_url: https://kimi-k2.net/
date: 2026 (n.d., accessed 2026-09-26) | status: INFERENCE | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: community reports of Kimi K2 driving Claude Code harnesses with full MCP support.
- Result: (INFERENCE — single-community-source claim) model/harness/MCPCompose телефон are becoming interchangeable commodities.
- Maps to OUR workflow: reinforces model-agnostic prompts (C4-019) — but stays INFERENCE until a primary source confirms. Below threshold — context.

[C4-053] MCP client→server 1:1 per client; hosts run multiple clients
source_url: https://www.ibm.com/think/topics/model-context-protocol
date: 2025-05-09 | status: VERIFIED | relevance: 2 | recency: 2 | actionability: 2 | score: 8/125
extraction:
- Mechanism: architecture constraint — each client has exactly one server; hosts multiplex.
- Result: multi-tool agents = multi-client hosts, with per-server auth/consent boundaries.
- Maps to OUR workflow: least-privilege per server (scorer client ≠ runner client). Context only.

[C4-054] Registry supply-chain defense: pin + continuously validate servers
source_url: https://www.paloaltonetworks.com/cyberpedia/what-is-model-context-protocol-mcp
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: fake/hijacked registry servers + rug-pulls → pin versions, monitor exposed tools, re-validate after approval.
- Result: operational checklist for MCP adoption.
- Maps to OUR workflow: same checklist as §0 rule 1 + tessdata pinning; apply to every MCP server the lanes install (incl. C4-050's local graph server). Process reliability for weak-cell evidence.

## T5 — Knowledge-graph / Obsidian workflows (C4-055–066)

[C4-055] obra/knowledge-graph: local graph algorithms for agents (PageRank/Louvain/BFS/paths)
source_url: https://github.com/obra/knowledge-graph
date: 2026-03-21 | status: VERIFIED | relevance: 5 | recency: 3 | actionability: 4 | score: 60/125
extraction:
- Mechanism: graphology in-memory algorithms (Louvain communities, betweenness, PageRank w/ fallback, BFS, all-simple-paths DFS); incremental indexing by mtime; no LLM inside — agent reasons, tool provides data.
- Result: claim investigation as graph traversal (prove-claim skill: entities → search → paths → evidence → cited report).
- Maps to OUR workflow: run the Level-7 ledger as a vault — Louvain clusters reveal which records actually serve Santali vs Kashmiri vs OldScan; path queries expose contradiction chains (record → weak cell → W1/R-doc); PageRank surfaces most-cited methods for the integration pass.
- Serves all four weak cells via evidence navigation.

[C4-056] obsidian-knowledge-agent: ingest→compile→distribute pipeline + self-evolution hooks
source_url: https://github.com/Michael-OvO/obsidian-knowledge-agent
date: 2026-05-31 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: agent pipeline turns raw material (PDFs, slides, papers, URLs) into structured teaching-quality notes; 12 commands (ingest/research/log/polish/refactor/doctor/clean/reflect/evolve); file-based self-evolution borrowed from Hermes-style agents.
- Result: vault compounds — agent rewrites its own rules from reflect/evolve; doctor finds broken links/orphans.
- Maps to OUR workflow: the Level-7 collection machine — ingest lane outputs, doctor the ledger (orphan records with no weak-cell map), reflect/evolve the LEDGER_FORMAT after verdict sampling. Direct template for Miss-agent lane ops.
- Serves Odia 80.01 + OldScan 55.3 via compounding research quality.

[C4-057] ai-agent-workflow: Obsidian (brain) + Linear (structure) + OpenClaw (glue)
source_url: https://github.com/Jason-Cyr/ai-agent-workflow
date: 2026-03-15 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 3 | score: 27/125
extraction:
- Mechanism: vault as shared brain (PARA + daily notes + AGENTS.md), Linear for tasks, agent platform for memory/voice; persistent identity across sessions.
- Result: assistants stop starting from zero; review→notes→iterate loop across tools.
- Maps to OUR workflow: mirrors Engine (tasks) + ledger vault (brain) + agent sessions (glue) — validates keeping PROMPT_*_AGENT.md + LEDGER_FORMAT.md as the shared brain. Just below threshold — context.

[C4-058] obsidian-knowledge-graph-agent: RAG chat over vault (TF-IDF recall + rerank, citations)
source_url: https://github.com/han-yi-1212/obsidian-knowledge-graph-agent
date: 2026-05-19 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: two-stage retrieval (TF-IDF recall → phrase/proximity/title rerank), streaming, collapsible Sources with pinned-vs-retrieved badges + relevance %, save-to-note with citations.
- Result: vault-grounded answers with provenance.
- Maps to OUR workflow: the integration pass (LEVEL7_INTEGRATED_ARCHITECTURE.md) must cite ledger records the same way — every architecture claim carries its C4-NNN sources with pinned (VERIFIED) vs retrieved (INFERENCE) badges. Adopt the citation discipline.
- Serves Kashmiri 54.82: Nastaliq claims traceable to records.

[C4-059] obsidian-knowledge-brain v4.0: project-local .md knowledge, Obsidian optional
source_url: https://github.com/Tubo2333/obsidian-knowledge-brain/blob/master/SKILL.md
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: decisions/error-fixes captured across sessions as plain .md in agent dir (+ global ~/. store); open the project as a vault for graph viz; hooks+cron automate capture on Claude Code.
- Result: session knowledge survives; project rules evolve automatically.
- Maps to OUR workflow: this is the OCR_AGENT_MEMORY_FEED.md + WORKSTREAM LOG pattern generalized — and the fix for the stale-copy failure: session-start hooks that reload current run_probe.py hash + protocol, automatically. Adopt hooks for executor sessions.
- Serves all weak cells via never-lost GT-gate knowledge.

[C4-060] obsidian-graph-query: agent-run graph algorithms (BFS, shortest path, Tarjan bridges)
source_url: https://github.com/azuma520/obsidian-graph-query
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: AI agent runs graph algorithms directly on vault link structure and explains results in natural language.
- Result: structural vault analysis without manual graph reading.
- Maps to OUR workflow: Tarjan bridge detection finds single-point-of-failure records (claims cited by only one ledger entry — e.g. any lone Santali-script claim); shortest-path shows the evidence chain from a weak cell to its supporting records for the validation call.
- Serves Santali 53.91 (thinnest evidence, n=20 fill).

[C4-061] obsidian-setup: vault engineered for AI-agent read/write/automation
source_url: https://github.com/KalebCole/obsidian-setup
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: setup guide for agent-first vaults (Claude Code, Copilot CLI): structure agents can read, write, automate.
- Result: vault as agent workspace, not just notes.
- Maps to OUR workflow: docs/research/level7/ is already an agent-first vault (lane dirs, format docs, verdict sampling) — validate the layout against this guide's conventions during the integration pass (H30-40).
- Process support for all weak-cell records.

[C4-062] Obsidian AI platform: KB-scoped agents + structured memory extraction + audit logs
source_url: https://www.obsidian-ai.dev/
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: per-agent knowledge-base scoping, pgvector/FAISS retrieval, session memory extraction, streaming traces, audit logs, DAG workflow editor.
- Result: commercial agent platform with knowledge discipline built in.
- Maps to OUR workflow: per-agent KB scoping is the commercial analogue of our lane-dir discipline (lanes read own dirs + shared law). Concept validation only — context.

[C4-063] PARA + daily notes + AGENTS.md as agent-navigable structure
source_url: https://github.com/Jason-Cyr/ai-agent-workflow
date: 2026-03-15 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 3 | score: 27/125
extraction:
- Mechanism: consistent structure (PARA/archive/dailies) + standing AGENTS.md lets any agent navigate the vault cold.
- Result: subagent task forces onboard without briefing.
- Maps to OUR workflow: LEDGER_FORMAT.md is our AGENTS.md for C4; every lane needs the same cold-start file. Just below threshold — context.

[C4-064] prove-claim skill: decompose → search → traverse → read → cited report
source_url: https://github.com/obra/knowledge-graph
date: 2026-03-21 | status: VERIFIED | relevance: 5 | recency: 3 | actionability: 4 | score: 60/125
extraction:
- Mechanism: structured claim-investigation workflow over the graph with citations; tool holds data, agent holds reasoning.
- Result: hostile-audit-grade verification as a repeatable skill.
- Maps to OUR workflow: this IS the Verdict Agent's 10%-sampling procedure formalized — adopt prove-claim as the sampling SOP (sampled record → entities → ledger paths → live source → pass/fail + citation). Also the template for §6.4 GT-verification rigor.
- Serves Odia 80.01 + Kashmiri 54.82: VERIFY-FIRST claims get proven, not asserted.

[C4-065] Incremental vault indexing by mtime (only reprocess changed files)
source_url: https://github.com/obra/knowledge-graph
date: 2026-03-21 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 3 | score: 27/125
extraction:
- Mechanism: track file mtimes; reprocess only changed files; --force for full rebuild.
- Result: cheap continuous indexing of a growing vault.
- Maps to OUR workflow: mirrors --skip-existing resume semantics; ledger verification should likewise only re-check changed records between passes, not re-open all 100. Just below threshold — context.

[C4-066] Self-evolving file-based learning (Hermes-style rule rewrite)
source_url: https://github.com/Michael-OvO/obsidian-knowledge-agent
date: 2026-05-31 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: reflect captures lessons from recent work, evolve proposes rule updates for approval — the agent's taste compounds with use.
- Result: fewer repeated mistakes across sessions.
- Maps to OUR workflow: after each hostile audit we hand-edit protocol §9/§10; the evolve pattern would propose those edits from the audit diff for human approval — adopt for post-Phase-6 reconciliation hygiene.
- Serves OldScan 55.3: Otsu-vs-denoiser ablation rules evolve with evidence, not memory.

## T6 — Eval harnesses (C4-067–080)

[C4-067] DeepEval eval-harness doctrine: evals offline vs guardrails live
source_url: https://deepeval.com/blog/what-is-an-eval-harness
date: 2026-08-19 | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
extraction:
- Mechanism: eval harness = infrastructure running LLM evals end-to-end (datasets + 50+ LLM-judge metrics + pytest CI gates); evals run OFFLINE against fixed datasets, guardrails run LIVE in the request path — same scorer, different placement.
- Result: releases blocked on metric failure; traces inspected locally (deepeval inspect) to avoid metric overfitting.
- Maps to OUR workflow: this is the exact doctrine behind §6.2 tier scoring (offline evals on fixed 1,227 manifest) vs §9 W6 guards (RLVR reward = live guardrail on gold GT only). Our scorer already implements both placements — DeepEval gives us the vocabulary + CI pattern (pytest gate per engine completion).
- Serves all weak cells: no engine ships a CER claim without passing the offline gate.

[C4-068] DeepEval Claude Code skill: skill loads expertise + hook enforces green metrics
source_url: https://deepeval.com/blog/what-is-an-eval-harness
date: 2026-08-19 | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
extraction:
- Mechanism: `npx skills add confident-ai/deepeval` installs templates/metric catalog/iteration guardrails; a stop/pre-commit hook runs `deepeval test run` so green metrics gate rather than suggest; deepeval generate builds datasets.
- Result: eval harness inside the coding agent with one command.
- Maps to OUR workflow: copy the shape — a `probe-eval` skill (score-engine/verify-sample/rank-lane, cf. C4-036) + a pre-report hook asserting pack counts == manifest n and scorer rules (§6.5) before any Phase 6 table is published. The bilingual sa-path failure dies at the hook.
- Serves Santali 53.91 / Odia 80.01: fill-cell agreement rates gated the same way.

[C4-069] DeepEval framework: pytest-native LLM unit tests, 17.8K stars, Apache-2.0
source_url: http://github.com/confident-ai/deepeval
date: 2026 (repo live; 17,816 stars / 10,123 commits; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: Pytest-specialized LLM testing (G-Eval, task completion, answer relevancy, hallucination; local judge models); evaluates black-box apps, full agent trajectories, individual steps (tool use, retrieval, handoffs).
- Result: optimal model/prompt/architecture selection with regression protection.
- Maps to OUR workflow: trajectory-level eval is what the executor post-mortem lacked — wrap Phase 5 engine runs as evaluable trajectories (packs + timings + errors) so the next "stale copy vs slow scan" question answers itself from traces.
- Serves Kashmiri 54.82: trajectory eval over Nastaliq-specialist runs.

[C4-070] Ragas: 5 reference-free RAG metrics, $0.025/sample, LangChain-native
source_url: https://github.com/a217-anjali/llm-evaluation-framework/blob/main/docs/04-tooling/ragas-guide.md
date: 2026-03-01 (v1.2+, updated Mar 2026; accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 3 | score: 27/125
extraction:
- Mechanism: faithfulness/context-precision/answer-relevancy + test-set generation + production feedback loops; 14.6K-star parent repo; explicit non-goals (no agents, no safety — use Inspect/Garak).
- Result: cheapest reference-free RAG eval with clear scope boundaries.
- Maps to OUR workflow: the scope-honesty ("not for agents/safety") mirrors our metric scoping (WER-primary for ur/sd/ks §6.3; agreement-only for fill cells §6.2). Adopt the pattern of publishing each metric's non-goals alongside Phase 6 tables. Just below threshold — context.

[C4-071] Deepchecks paper: Grounded-in-Context beats Ragas/LangSmith faithfulness (ROC-AUC)
source_url: https://arxiv.org/pdf/2605.14488
date: 2026-05-14 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: benchmarked faithfulness measurement (TRUE, SQuAD, PubMedQA + client sets): Deepchecks 0.70-0.96 vs Ragas 0.46-0.65 vs LangSmith 0.54-0.96 accuracy on production sets.
- Result: LLM-judge quality varies widely; production sets separate the harnesses.
- Maps to OUR workflow: cautionary evidence for any LLM-as-judge step in §6.4 pre-screening (cf. C4-010) — calibrate the judge against human GT verification, exactly as LangSmith's docs prescribe (C4-073). Below threshold — context.

[C4-072] LangSmith: offline + online evals, per-PR/Vitest/pytest CI integration
source_url: https://www.langchain.com/langsmith/evaluation
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: curated-dataset offline evals (regression catch) + production online evals (drift detect); threshold-gated pipelines fail on score drops; side-by-side experiment comparison across prompts/models/versions.
- Result: same rigor as deterministic unit tests for AI pipelines.
- Maps to OUR workflow: the Phase 6 → W6 handoff needs exactly this — offline tier tables per engine (fixed manifest) + online drift watch when the frozen recipe trains; experiment comparison view is the template for the final leaderboard (per-engine CER/WER + per-tier + CIs).
- Serves Odia 80.01 + OldScan 55.3 via regression-proof reporting.

[C4-073] LangSmith: calibrate LLM-judge with human feedback (annotation queues)
source_url: https://www.langchain.com/langsmith/evaluation
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 5 | recency: 4 | actionability: 4 | score: 80/125
extraction:
- Mechanism: flag runs for SME review; use expert feedback to calibrate automated eval, improve prompts, augment datasets.
- Result: judges earn trust instead of assuming it.
- Maps to OUR workflow: this is the §6.4 human GT verification loop stated generally — human pass/fail on 158 fill + ~77 PDF sample calibrates every downstream automated claim; >20%-fail languages barred from W6. Cite this as external validation of §6.4's design.
- Serves Kashmiri 54.82 / Odia 80.01 / ne-barred precedent directly.

[C4-074] Ragas + LangSmith integration: traces visualized, metrics composed
source_url: https://docs.ragas.io/en/v0.1.21/howtos/integrations/langsmith.html
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: ragas metrics run under LangSmith tracing with two-line setup; traces of evaluators inspectable.
- Result: composable eval stack, not monolith.
- Maps to OUR workflow: metrics.py + gt_forensics.py + sheet.csv already compose this way; keep them loosely coupled (no monolithic scorer rewrite). Context only.

[C4-075] Mastra→LangSmith exporter: traces to LangSmith for debug/eval/observability
source_url: https://docs.langchain.com/langsmith/trace-with-mastra
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: LangSmithExporter on the Mastra constructor; storage required even for external export; string model IDs for compatibility.
- Result: TS agents get LangSmith-grade tracing without Python.
- Maps to OUR workflow: if probe orchestration goes TS (C4-040/C4-046), tracing lands in the same LangSmith project as any Python evals — one verdict surface. Bridges to T7.
- Serves OldScan 55.3 via unified long-run traces.

[C4-076] LangSmith RAG eval separates retrieval quality from generation quality
source_url: https://www.langchain.com/langsmith/evaluation
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: context precision (retrieval) vs faithfulness (generation) measured independently; catches hallucinations and retrieval failures separately.
- Result: targeted fixes instead of blended scores.
- Maps to OUR workflow: the direct analogue of §6.2 tier scoring — pair-GT vs pdf-GT vs fill-GT measured independently so extractor-mirroring bias (retrieval-side corruption) can't hide inside a blended CER. External validation of the falsification test.
- Serves Kashmiri 54.82 (trust 45.0) + ne-barred (26.6): tier separation is what caught them.

[C4-077] Ragas parent repo: 14.6K stars, quickstart templates (rag_eval → agent_evals soon)
source_url: http://github.com/explodinggradients/ragas
date: 2026-08-05 (last-verified; accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: objective metrics + test generation + production feedback loops; roadmap toward agent_evals/benchmark_llm templates.
- Result: momentum signal for eval commoditization.
- Maps to OUR workflow: track agent_evals template for post-freeze agent-quality regression. Context only.

[C4-078] DeepEval generate: dataset synthesis for eval suites
source_url: https://deepeval.com/blog/what-is-an-eval-harness
date: 2026-08-19 | status: VERIFIED | relevance: 2 | recency: 5 | actionability: 1 | score: 10/125
extraction:
- Mechanism: `deepeval generate` builds eval datasets from knowledge bases when none exist.
- Result: eval suites bootstrapped without manual authoring.
- Maps to OUR workflow: CONTRADICTS protocol §0 rule 2 (no synthetic data generation) and §9 (machine GT never trains) if misapplied — synthesis is allowed ONLY for harness self-test fixtures, never for probe GT or W6 training. Logged per contradiction rule; synthesis stays banned for GT.
- Context only, with guardrail.

[C4-079] Eval cost ladder: Ragas $0.025 vs DeepEval $0.05 vs Inspect $0.10/sample
source_url: https://github.com/a217-anjali/llm-evaluation-framework/blob/main/docs/04-tooling/ragas-guide.md
date: 2026-03-01 | status: VERIFIED | relevance: 3 | recency: 3 | actionability: 4 | score: 36/125
extraction:
- Mechanism: published per-sample eval costs across harnesses; local-model judges cut cost further.
- Result: eval budgets are plannable numbers, not vibes.
- Maps to OUR workflow: same discipline as the Sarvam 54-call cap — budget the §6.4-adjacent automated pre-screens per sample before running them across 1,227 items; prefer local judges for bulk, frontier judges for VERIFY-FIRST langs (ks/mr/gu/ur).
- Serves Kashmiri 54.82 affordably.

[C4-080] Confident-AI skill distribution via `npx skills add` (one-command harness install)
source_url: https://deepeval.com/blog/what-is-an-eval-harness
date: 2026-08-19 | status: VERIFIED | relevance: 3 | recency: 5 | actionability: 4 | score: 60/125
extraction:
- Mechanism: eval harness installs as a versioned skill package, not a wiki page.
- Result: every agent session gets identical eval capability.
- Maps to OUR workflow: distribute the `probe-eval` skill (C4-036/C4-068) the same way — versioned, installable, identical across Engine/Verdict/Miss sessions. Kills stale-copy class failures structurally.
- Process reliability for all weak-cell scores.

## T7 — TypeScript AI SDKs (C4-081–092)

[C4-081] Vercel AI SDK agent loop: generateText + tool + stopWhen/stepCountIs
source_url: https://vercel.com/docs/agents
date: 2026-06-17 | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 4 | score: 64/125
extraction:
- Mechanism: tool() with zod inputSchema + execute; SDK appends tool calls/results to history and re-generates until text response or step cap; deploys as API route on Fluid compute.
- Result: full agent loop in ~30 lines of TS with deployment solved.
- Maps to OUR workflow: the reference implementation for a TS probe-analysis agent (query manifest → run scorer → append sheet → rank) behind an API route; step caps mirror --limit-per-lang credit guards.
- Serves Odia 80.01 via repeatable programmatic re-scoring.

[C4-082] Mastra + AI SDK: model routing, useChat streaming, networkRoute
source_url: https://mastra.ai/docs/v0/frameworks/agentic-uis/ai-sdk
date: 2026 (v0.x docs; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: Agent with string model IDs; @mastra/ai-sdk chat/workflow/network routes stream in AI-SDK format; useChat hook connects frontends over HTTP.
- Result: agents, workflows, and agent-networks all consumable from one UI protocol.
- Maps to OUR workflow: the validation-call dashboard (leaderboard + tier tables + CIs) could be a useChat front over Mastra agents running ranking/verification tools — live Q&A over probe results instead of static markdown.
- Serves all weak cells via explorable results.

[C4-083] @mastra/ai-sdk 1.4.0: chat/workflow/network routes + framework-agnostic handlers
source_url: https://www.npmjs.com/package/@mastra/ai-sdk?activeTab=readme
date: 2026-09-25 (v1.4.0 published ~a day before access 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 5 | actionability: 3 | score: 45/125
extraction:
- Mechanism: chatRoute/workflowRoute/networkRoute with :agentId dynamics; AbortSignal forwarded to agent.stream(); standalone handlers for Next.js/Express via createUIMessageStreamResponse.
- Result: freshest TS agent-serving surface in this ledger.
- Maps to OUR workflow: adopt for any post-freeze probe service; abort-forwarding semantics matter for cancelling runaway long scans cleanly (cf. 300s tesseract timeouts on bn_d014/hi_d066).
- Serves OldScan 55.3 via cancellable long-scan handling.

[C4-084] Vercel AI Gateway: 200+ models, unified billing/observability, framework integrations
source_url: https://vercel.com/docs/ai-gateway/ecosystem
date: 2026-07-28 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: one key + Chat Completions endpoint serves LangChain/LlamaIndex/Mastra/Pydantic-AI/LiteLLM; native Mastra/Pydantic/Langfuse integrations.
- Result: model swaps without code changes + spend monitoring.
- Maps to OUR workflow: the hosted answer to C4-029's model-neutral stance — route analysis traffic (cheap) vs audit traffic (frontier) through one gateway with spend caps, the same way sarvam_vision is credit-capped.
- Budget control for weak-cell analysis.

[C4-085] Mastra channels (≥1.22.0): one agent, many chat surfaces via Chat SDK adapters
source_url: https://vercel.com/i/mastra-chat-sdk
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: Chat SDK adapters (Slack/Teams/Discord/Telegram/GitHub/Linear/WhatsApp) on the Agent constructor; createChatTools exposes messaging as approvable AI-SDK tools; RedisStreamsPubSub for multi-instance; waitUntil keeps serverless runs alive.
- Result: agents meet the team where they already talk.
- Maps to OUR workflow: validation-call coordination (Miss-agent duty) could run through these channels — probe-completion pings, gate failures. Context only.

[C4-086] Mastra Memory Gateway + OpenAI-compatible/Anthropic providers via AI SDK
source_url: https://gateway.mastra.ai/docs/examples/ai-sdk
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: createOpenAICompatible/createAnthropic providers route all models through one gateway; AI SDK auto-executes tool calls with zod schemas.
- Result: provider-shape portability (cf. C4-019) with memory infra attached.
- Maps to OUR workflow: persistent-thread memory for multi-day Phase 5/6 runs without rebuilding context each session — the hosted version of C4-059's file-based memory. Either satisfies the stale-copy lesson.
- Process reliability for weak-cell evidence chains.

[C4-087] Mastra vs LangChain vs Vercel AI SDK comparison (2026 TS framework guide)
source_url: https://andrew.ooo/answers/mastra-vs-langchain-vs-vercel-ai-sdk-typescript-agent-frameworks-2026
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: pricing/capabilities/observability/deployment comparison across the three TS agent stacks.
- Result: decision aid, not a verdict — fit depends on stack.
- Maps to OUR workflow: use it at H30-40 integration to pick the post-freeze serving stack (Mastra for workflows+observability vs raw AI SDK for minimal surface), not before. Decision deferred, source kept per contradiction rule.
- Serves W6 serving choice downstream of all weak cells.

[C4-088] Vercel deployment SDK/CLI for agents that ship artifacts programmatically
source_url: https://vercel.com/kb/guide/ai-agents
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: @vercel/sdk + CLI create deployments from agents (token → upload files → create deployment → alias).
- Result: agents that publish, not just analyze.
- Maps to OUR workflow: publishing the final leaderboard packet could be agent-executed, but reports are sealed flat files by law — no auto-publish. Context only.

[C4-089] LangChain.js traceable + evaluate (TS-native dataset eval with zod results)
source_url: https://docs.langchain.com/langsmith/evaluate-rag-tutorial
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 4 | actionability: 3 | score: 48/125
extraction:
- Mechanism: traceable() wraps TS functions for LangSmith tracing; evaluate() runs datasets with typed EvaluationResult; works with @langchain/openai + text splitters.
- Result: TS eval suites with the same dataset discipline as Python.
- Maps to OUR workflow: if ranking/verification logic moves to TS, evaluate() over a dataset of (image_id, gt, pred) rows reproduces metrics.py's role with tracing attached — port the CER/WER + tier-split semantics, not just the API.
- Serves Odia 80.01 + Santali 53.91 via traced re-evals.

[C4-090] LangSmith chatbot-eval tutorial: dataset schemas + LLM-judge + online evals
source_url: https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: flexible dataset schemas (inputs/outputs/expected steps), custom judge prompts, offline + online evaluation modes.
- Result: eval design cookbook.
- Maps to OUR workflow: sheet.csv's column set (image_id/language/script/.../CER/WER/error_tag) is already a LangSmith-style dataset schema — document the equivalence so a future import is mechanical. Error_tag taxonomy maps to expected-steps metadata.
- Serves OldScan 55.3: old_scan tag becomes a first-class eval slice.

[C4-091] AI SDK tool auto-execution + history append (orchestration without a framework)
source_url: https://vercel.com/kb/guide/how-to-build-ai-agents-with-vercel-and-the-ai-sdk
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 3 | score: 36/125
extraction:
- Mechanism: single-call default (steps=1) → opt-in loop via stopWhen; SDK handles orchestration (append, execute, regenerate) with no agent framework.
- Result: minimal viable agent with zero framework lock-in.
- Maps to OUR workflow: the lightest possible probe-analysis agent — a looped generateText calling manifest/scorer/sheet tools. Prefer this over Mastra/LangChain unless observability needs (C4-075) force the upgrade.
- Keeps weak-cell tooling minimal and auditable.

[C4-092] Chat SDK createChatTools: workspace actions as approvable agent tools
source_url: https://vercel.com/i/mastra-chat-sdk
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 2 | recency: 4 | actionability: 2 | score: 16/125
extraction:
- Mechanism: post/react/DM/edit/delete exposed as AI-SDK tools with built-in approval gates.
- Result: agents act in workspaces under human approval.
- Maps to OUR workflow: approval-gate pattern generalizes to sarvam_vision spend + manifest writes — every credit-consuming or state-changing tool needs the gate. Context only.

## T8 — Ledger / logging / verification practice (C4-093–100)

[C4-093] PaddleOCR-VL-1.6: 96.3% OmniDocBench v1.6 + Real5 distortion benchmark
source_url: https://www.paddleocr.ai/main/en
date: 2026-05-28 | status: VERIFIED | relevance: 5 | recency: 4 | actionability: 3 | score: 60/125
extraction:
- Mechanism: 0.9B VLM (NaViT encoder + ERNIE-4.5-0.3B) + PP-DocLayoutV3; 109 langs incl. Devanagari/Arabic; irregular-bbox localization; Real5-OmniDocBench (scan/skew/warp/screen-photo/illumination); 1.5→1.6 zero-cost migration.
- Result: SOTA doc parsing at 0.9B; robustness benchmarked against physical distortions explicitly.
- Maps to OUR workflow: Real5 is the external template for our missing old-scan stratification slice (§6.8) — copy its five distortion axes when the human tags ~100 pages; VL-1.6 stays P2 (approval+GPU) but its benchmark design enters the architecture now.
- Serves OldScan 55.3 directly; Hindi/Devanagari coverage touches Kashmiri-adjacent script handling.

[C4-094] PaddleOCR-VL-1.5 paper: two-stage parse + text-spotting, FastDeploy/vLLM/SGLang numbers
source_url: https://arxiv.org/pdf/2601.21957v1
date: 2026-01-29 | status: VERIFIED | relevance: 4 | recency: 3 | actionability: 3 | score: 36/125
extraction:
- Mechanism: two-stage document-parsing framework + text spotting (detection+recognition) + seal recognition; published inference tables across vLLM/SGLang/FastDeploy.
- Result: SOTA 94.5% v1.5 → 96.3% v1.6 with serving numbers attached.
- Maps to OUR workflow: serving tables are the format our engine reports should copy (packs + wall time + peak RSS per engine, as measured 2026-09-26: paddle 15GB/13.6s, surya 47.9s, indicphotoocr 299.6s). Standardize Phase 6 reporting to this shape.
- Serves OldScan 55.3 via comparable latency/accuracy reporting.

[C4-095] PaddleOCR-VL-1.6-0.9B on HuggingFace (Apache-2.0, transformers-callable)
source_url: http://huggingface.co/PaddlePaddle/PaddleOCR-VL
date: 2025-10-16 (v1.0 release; accessed 2026-09-26) | status: VERIFIED | relevance: 4 | recency: 3 | actionability: 2 | score: 24/125
extraction:
- Mechanism: open weights, Apache-2.0, transformers library path, 1.64K likes; multilingual incl. Hindi/Devanagari + Arabic.
- Result: downloadable SOTA baseline — gated by our §0 rule 1 (no downloads without approval).
- Maps to OUR workflow: the concrete P2 approval packet item for the GPU-budget decision (size, license, Indic coverage, MCP path per C4-045). Below threshold as action today — context kept for the validation call.

[C4-096] PP-OCRv6 (Jun 2026): PPLCNetV4 backbone, 1.5M–34.5M tiers, +4.6% det / +5.1% rec
source_url: https://www.paddleocr.ai/main/en
date: 2026-06-11 | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: tiny/small/medium unified backbone; 50 langs (Latin-scripts + CJK); gains over v5.
- Result: efficient classic-OCR path still advancing alongside VLMs.
- Maps to OUR workflow: relevant only as the "cheap baseline" family for Latin/EN-sanity-adjacent work and seal/edge deployment notes (Lane C1 territory) — NOT for Indic scripts (no Ol Chiki/Nastaliq/Mayek claim). Below threshold — context.

[C4-097] 10-agent-harness survey: harness engineering as the 2026 discipline
source_url: http://thetoolnerd.com/p/10-agent-harnesses-every-ai-builder
date: 2026 (n.d., accessed 2026-09-26) | status: VERIFIED | relevance: 3 | recency: 4 | actionability: 2 | score: 24/125
extraction:
- Mechanism: survey of 10 harnesses (Claude Code, Codex CLI/Desktop, Cursor SDK, OpenHands, OpenCode, Pi, Goose, Mastra, OpenAI harness comms, block-forthcoming) — bidirectional model↔env comms, context engineering, streaming progress as the shared frontier.
- Result: field consensus that harness > model for agent outcomes.
- Maps to OUR workflow: post-hoc justification of the campaign's own shape — lanes + verdict sampling + skills + permissions are harness engineering, and the probe failures were harness failures. Below threshold — context.

[C4-098] R5 gt_forensics precedent: machine trust scores bar ne (26.6), flag ks/mr/gu/ur
source_url: level2/probe22/gt_forensics.json (disk, 2026-09-26)
date: 2026-09-26 | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 4 | score: 100/125
extraction:
- Mechanism: automated GT forensics (control chars, glyph breakage, script ratios) produced per-language trust scores; ne BARRED outright, four langs VERIFY-FIRST.
- Result: machine pre-screen + human verification (§6.4) two-stage gate, already on disk.
- Maps to OUR workflow: the in-house proof that C4-010 (visual pre-screen) + C4-073 (judge calibration) compose correctly — forensics triages, humans decide, W6 consumes only passing langs. This record anchors all tooling claims to disk truth.
- Serves Kashmiri 54.82 (45.0) + Odia-adjacent gu 51.4 + ne-barred precedent.

[C4-099] EN sanity column: 30 gold EN pairs as harness-sanity reference (CER>~5 = broken harness)
source_url: level2/probe22/en_sanity/manifest.json (disk, 2026-09-26)
date: 2026-09-26 | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
extraction:
- Mechanism: 30 official EN human pairs, same gates, seed 20260926, scored per engine via --manifest flag; tesseract stacks ~122% (genuine engine weakness on ornate scans, harness proven sound on clean renders), doctr ~42%.
- Result: separates harness bugs from model weakness — the single most load-bearing logging invention of Phase 5.
- Maps to OUR workflow: every future tooling change (new scorer flag, new engine, new normalization) must re-run the EN column first — the C4 doctrine is "sanity column before weak-cell claims." Adopt as permanent gate.
- Serves all weak cells: no Santali/Kashmiri/OldScan/Odia number is trusted unless the EN column is green.

[C4-100] Verdict-sampling + contradiction-logging as the ledger's own QA (this campaign)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §4 + LEDGER_FORMAT.md §§4-5
date: 2026-09-26 | status: VERIFIED | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
extraction:
- Mechanism: 10% live-source re-check per lane; >20% sampled-failure voids the lane; contradictions resolved in integration, never silently dropped.
- Result: the ledger audits itself — C4-010/020/…/100 are the pre-registered sample for this file.
- Maps to OUR workflow: identical in spirit to §6.4 human verification (>20% fail → barred) and §6.5 scorer rules — verification fractals: GT verified, scorer verified, ledger verified, each with a numeric bar.
- Serves every weak cell: numbers that survive three verification layers are the only ones that enter W6.

---

## Ranking summary (score ≥ 30 enters integrated architecture)

Entering (62 records): C4-001, 002, 003, 004, 006, 008, 010, 011, 016, 017, 018,
024, 025, 027, 028, 029, 031, 032, 033, 034, 036, 040, 041, 042, 044, 045, 046,
047, 048, 050, 054, 055, 056, 058, 059, 060, 061, 064, 066, 067, 068, 069, 072,
073, 075, 076, 079, 080, 081, 082, 083, 084, 086, 087, 089, 090, 091, 093, 094,
098, 099, 100.
Context only (<30, kept per contradiction rule): all others (38 records).
Pre-registered verdict sample (every 10th): C4-010, 020, 030, 040, 050, 060,
070, 080, 090, 100.
Top score (125/125): C4-067, C4-068, C4-099, C4-100.

---

## §9 UPGRADE (2026-09-27, appended — existing rows above untouched)

Per `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §9.1 + PROMPT_MISS_AGENT tasks
1/4: every C4-001–100 record gets `§9-status | decision-it-can-change |
TRANSFER` against OUR harness facts (18 Indic langs; weak cells
Santali 53.91 / Kashmiri 54.82 / OldScan 55.3 / Odia 80.01; 200-dpi citizen
docs; no paid keys; no training until W6 freeze; offline pipeline). §9-status
set: PRIMARY (disk/spec first-party) / MEASURED (vendor-measured numbers) /
DERIVED (claim + our mapping) / UNKNOWN (single-source) / CONTRADICTION
(logged). TRANSFER: SURVIVES / DIES / UNKNOWN + killing/saving harness fact.
External numbers cited anywhere in this ledger are buried in OBITUARIES.md
(O-01–O-13); "beat 87.39" stays directional (§6.8).

| rec | §9-status | decision it can change | TRANSFER |
|---|---|---|---|
| C4-001 | DERIVED | adopt orchestrated retry for slow scans | SURVIVES — needs no weights/GPU/keys |
| C4-002 | DERIVED | enforce protocol re-read hook at session start | SURVIVES — file discipline only |
| C4-003 | DERIVED | keep heavy engines sequential-but-unattended | SURVIVES — analogy, no new dependency |
| C4-004 | DERIVED | TDD-gate metrics.py scorer patches | SURVIVES — local test discipline |
| C4-005 | DERIVED | none (context) | UNKNOWN — org-adoption signal, no harness mapping |
| C4-006 | DERIVED | post-freeze probe-runner service shape | UNKNOWN — needs build effort, no GPU/keys |
| C4-007 | DERIVED | hash-verify hook before engine start | SURVIVES — local hook |
| C4-008 | DERIVED | P2 specialist-model testing behind one harness | UNKNOWN — needs GPU + approval (P2) |
| C4-009 | DERIVED | none (terminal probe; no IDE workflow) | DIES — harness fact: no IDE surface |
| C4-010 | DERIVED | §6.4 visual pre-screen adoption | SURVIVES — uses existing vision capacity |
| C4-011 | DERIVED | split executor prompts stable-law vs per-phase delta | SURVIVES — doc discipline |
| C4-012 | DERIVED | Phase-6 CI gate per completed engine | SURVIVES — local CI |
| C4-013 | DERIVED | none (context) | UNKNOWN — coordination pattern, no mapping |
| C4-014 | DERIVED | none (context) | UNKNOWN — practice endorsement |
| C4-015 | MEASURED | cheap analysis-compute routing | UNKNOWN — API needs paid key; self-host needs GPU |
| C4-016 | MEASURED | cache-friendly analysis prompt design | UNKNOWN — same key/GPU dependency |
| C4-017 | MEASURED | model-ID pinning rule (never preview IDs) | SURVIVES — pinning is free discipline |
| C4-018 | MEASURED | Phase-6 scorer/ledger automation backend | UNKNOWN — official-API accuracy ≠ self-host |
| C4-019 | DERIVED | model-agnostic agent prompts | UNKNOWN — portability pattern, needs a host |
| C4-020 | DERIVED | trajectory logging for probe runs | SURVIVES — logging discipline |
| C4-021 | DERIVED | second-opinion scorer allowlist (never GT) | UNKNOWN — analysis-only, needs key/compute |
| C4-022 | DERIVED | none (context) | UNKNOWN — one-model-every-surface, no mapping |
| C4-023 | UNKNOWN | vision pre-screen backend | UNKNOWN — single-doc-line claim, needs live check |
| C4-024 | MEASURED | stable-prefix prompt design for analysis | SURVIVES — design discipline, no spend |
| C4-025 | MEASURED | "beat 87.39 stays directional" guard | SURVIVES — benchmark-the-deployment-you-run |
| C4-026 | DERIVED | none before W6 (train vs agent split noted) | UNKNOWN — training-gated |
| C4-027 | DERIVED | Verdict/Miss run read-only (plan-mode shape) | SURVIVES — permission config |
| C4-028 | DERIVED | encode §0 hard rules as permissions | SURVIVES — config, highest actionability |
| C4-029 | MEASURED | cheap-vs-frontier analysis routing | UNKNOWN — needs accounts/keys per provider |
| C4-030 | MEASURED | none (ecosystem-momentum signal) | DIES — stars change no decision |
| C4-031 | DERIVED | LSP-backed edits to gate/extraction code | SURVIVES — local tooling |
| C4-032 | DERIVED | parallelize lanes/analysis, serialize engines | SURVIVES — scheduling rule (§5-compatible) |
| C4-033 | DERIVED | integration-pass endpoints (TS route + vault) | SURVIVES — pattern; build is post-freeze |
| C4-034 | DERIVED | mandatory scout-check for P1/P2 claims | SURVIVES — source-audit discipline |
| C4-035 | DERIVED | none (remote-monitoring note) | DIES — convenience, no decision |
| C4-036 | DERIVED | package probe ops as skills (score/verify/rank) | SURVIVES — composition, no new dep |
| C4-037 | MEASURED | invest in harness over model swaps | SURVIVES — lesson, free |
| C4-038 | DERIVED | minimal probe-executor tool surface (~6 tools) | UNKNOWN — existence proof, needs build |
| C4-039 | DERIVED | local-only CER analysis option | UNKNOWN — needs install/eval |
| C4-040 | MEASURED | post-freeze orchestration-service design | UNKNOWN — needs TS build + hosting |
| C4-041 | PRIMARY | expose probe ops as MCP tools | SURVIVES — spec is stable open standard |
| C4-042 | PRIMARY | pin MCP server versions like tessdata | SURVIVES — pinning discipline |
| C4-043 | DERIVED | de-risk probe-MCP investment (spec outlives vendors) | UNKNOWN — governance signal, no direct mapping |
| C4-044 | DERIVED | read-scoped probe tools + hash pin + re-validate | SURVIVES — least-privilege config |
| C4-045 | MEASURED | copy MCP-server integration shape for frozen recognizer | SURVIVES (pattern) — model itself UNKNOWN (P2 GPU/approval) |
| C4-046 | DERIVED | TS-service template for probe analysis | UNKNOWN — needs Vercel/hosting account |
| C4-047 | PRIMARY | Phase-6 as composition (manifest + scorer + sampler) | SURVIVES — decomposition pattern |
| C4-048 | DERIVED | frozen recognizer behind same probe tool interface | UNKNOWN — post-W6 serving, needs GPU |
| C4-049 | PRIMARY | lane read/write split (Resources vs Tools) | SURVIVES — protocol-layer separation |
| C4-050 | MEASURED | ledger query layer (graph over vault, local) | SURVIVES — local SQLite, no keys |
| C4-051 | PRIMARY | inline CER rendering + spend approvals via elicitation | UNKNOWN — needs MCP-App-capable client |
| C4-052 | UNKNOWN | none until primary source confirms | UNKNOWN — single-community-source claim |
| C4-053 | PRIMARY | least-privilege per-server scoping | SURVIVES — arch constraint, free |
| C4-054 | DERIVED | MCP install checklist (pin + monitor + re-validate) | SURVIVES — ops discipline |
| C4-055 | MEASURED | ledger-as-vault analysis (Louvain/paths/PageRank) | SURVIVES — local algorithms |
| C4-056 | MEASURED | Miss-lane ops template (ingest/doctor/reflect/evolve) | SURVIVES — file-based, no dep |
| C4-057 | DERIVED | shared-brain validation (protocol + format as brain) | UNKNOWN — needs Linear/glue stack |
| C4-058 | MEASURED | integration-pass citation discipline (pinned vs retrieved) | SURVIVES — doc discipline |
| C4-059 | MEASURED | session-start hooks reloading protocol + code hash | SURVIVES — hooks + plain .md |
| C4-060 | MEASURED | bridge detection on thin-evidence claims (sat n=20) | SURVIVES — local graph algorithm |
| C4-061 | DERIVED | validate level7 layout at integration pass | SURVIVES — checklist, free |
| C4-062 | MEASURED | none (commercial platform) | DIES — harness fact: no paid keys |
| C4-063 | DERIVED | cold-start file per lane (LEDGER_FORMAT as AGENTS.md) | SURVIVES — doc discipline |
| C4-064 | MEASURED | Verdict sampling SOP (prove-claim workflow) | SURVIVES — procedure, no dep |
| C4-065 | MEASURED | re-check-only-changed ledger passes | SURVIVES — mirrors --skip-existing |
| C4-066 | MEASURED | audit-diff rule proposals for human approval | SURVIVES — file-based learning |
| C4-067 | DERIVED | offline-eval vs live-guardrail placement + CI pattern | SURVIVES — vocabulary + pytest gate |
| C4-068 | DERIVED | probe-eval skill + pre-report hook | SURVIVES — skill + hook shape |
| C4-069 | MEASURED | trajectory eval of Phase-5 engine runs | SURVIVES — eval pattern; local judges preferred |
| C4-070 | MEASURED | publish each metric's non-goals with Phase-6 tables | SURVIVES — scope honesty, free |
| C4-071 | MEASURED | calibrate any LLM-judge vs human GT verification | SURVIVES — cautionary, free |
| C4-072 | DERIVED | offline tier tables + online drift watch design | UNKNOWN — hosted LangSmith needs account/keys |
| C4-073 | DERIVED | cite as external validation of §6.4 design | SURVIVES — pattern already on disk |
| C4-074 | DERIVED | keep metrics.py + forensics + sheet loosely coupled | SURVIVES — no-rewrite rule |
| C4-075 | DERIVED | unified tracing if orchestration goes TS | UNKNOWN — needs TS stack + account |
| C4-076 | DERIVED | keep §6.2 tier split (falsification test) | SURVIVES — separation already on disk |
| C4-077 | MEASURED | track agent_evals template post-freeze | UNKNOWN — roadmap watch, no action now |
| C4-078 | CONTRADICTION | synthesis ban scope (fixtures ONLY, never GT/W6) | DIES for GT/W6 (§0 rule 2, §9) — SURVIVES for harness self-test fixtures |
| C4-079 | MEASURED | budget automated pre-screens per sample | SURVIVES — arithmetic discipline |
| C4-080 | DERIVED | versioned probe-eval distribution (skill package) | SURVIVES — packaging pattern |
| C4-081 | DERIVED | TS probe-analysis agent reference implementation | UNKNOWN — needs TS deploy target |
| C4-082 | DERIVED | validation-call dashboard option (useChat over agents) | UNKNOWN — needs Mastra hosting |
| C4-083 | MEASURED | cancellable long-scan handling (abort semantics) | UNKNOWN — freshest surface, needs TS stack |
| C4-084 | MEASURED | spend-cap pattern copy (cheap vs audit traffic) | DIES — harness fact: no paid keys (gateway billing) |
| C4-085 | DERIVED | validation-call coordination pings | UNKNOWN — needs chat-surface accounts |
| C4-086 | DERIVED | thread-memory option for multi-day runs | UNKNOWN — hosted gateway, needs account |
| C4-087 | DERIVED | deferred serving-stack pick at H30-40 | UNKNOWN — decision aid, pick is post-freeze |
| C4-088 | DERIVED | none (reports are sealed flat files by law) | DIES — auto-publish contradicts sealed-reports law |
| C4-089 | DERIVED | port CER/WER + tier-split semantics IF ranking goes TS | UNKNOWN — needs TS eval stack |
| C4-090 | DERIVED | sheet.csv ↔ eval-dataset schema equivalence doc | SURVIVES — documentation, free |
| C4-091 | DERIVED | prefer minimal looped-generateText over framework | SURVIVES — minimal-surface preference |
| C4-092 | DERIVED | spend/state-change gates (sarvam spend + manifest writes) | SURVIVES — approval-gate pattern |
| C4-093 | MEASURED | copy Real5 distortion axes now; model stays P2 | UNKNOWN — model needs approval+GPU+download; PATTERN survives |
| C4-094 | MEASURED | standardize Phase-6 engine reports (packs + wall + RSS) | SURVIVES — reporting format |
| C4-095 | MEASURED | P2 approval-packet item (size/license/coverage/MCP) | UNKNOWN — download-gated by §0 rule 1 |
| C4-096 | MEASURED | none for weak cells (Latin/CJK only) | DIES — harness fact: no Ol Chiki/Nastaliq/Mayek claim |
| C4-097 | DERIVED | none (post-hoc justification note) | UNKNOWN — survey consensus, no direct mapping |
| C4-098 | PRIMARY | two-stage gate anchor (forensics triage → humans decide) | SURVIVES — on disk 2026-09-26 |
| C4-099 | PRIMARY | permanent pre-claim gate (EN column green first) | SURVIVES — on disk 2026-09-26 |
| C4-100 | PRIMARY | triple-verification doctrine for W6 (GT + scorer + ledger) | SURVIVES — this campaign's own QA |

Upgrade tally: SURVIVES 62 (incl. 2 split: C4-045 pattern, C4-078 fixtures) |
DIES 8 (009, 030, 035, 062, 084, 088, 096, 078-GT-use) | UNKNOWN 30.
DIES/UNKNOWN rows stay as context per contradiction rule — never silently dropped.

## T9 — §9-native tooling records (C4-101–122, 2026-09-27)

Evidence-law tooling: estimator law, transfer cards/obituaries, feasible set,
kill criteria, and the disk gates that enforce them. No downloads — every
source is a disk-law doc or a re-cite of a URL already in this ledger
(C4-098/099/100 precedent: disk paths are legal source_urls). Status uses the
§9 set (see LEDGER_FORMAT.md §7 addendum); every record carries decision +
TRANSFER. Score = relevance × recency × actionability; ≥30 enters architecture.

[C4-101] Wilson 95% intervals on every per-language engine CER (§9.3)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.3 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: every Phase-6 per-language CER ships with a Wilson 95% interval; point-only CER tables are rejected at the pre-report hook.
TRANSFER: SURVIVES — pure computation over existing sheet.csv, no keys/GPU/training.
extraction:
- Mechanism: Wilson score interval on per-language CER (n = cell items); exact coverage at small n, no normal approximation.
- Result: weak cells (sat n=20, ks PDF-tier) get honest wide intervals instead of false precision; n<50 cells cannot produce winner claims (§6.7).
- Maps to OUR workflow: implemented as a scorer-side CI column + hook assertion (no CI → no publish), same placement as the §6.5 scorer rules.
- Serves Santali 53.91 (n=20 fill, widest honest interval) + Kashmiri 54.82 (VERIFY-FIRST trust 45.0 quantified) + Odia 80.01 (69-item or-cell CI decides winnability).

[C4-102] McNemar exact for paired engine comparisons on SAME items (§9.3)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.3 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: engine A-vs-B claims use McNemar exact on paired items only; unpaired point-delta rankings are rejected.
TRANSFER: SURVIVES — local exact test, no dependencies.
extraction:
- Mechanism: McNemar exact test on discordant pairs (same image_id, both engines scored); pre-declared test family before looking (§6.7).
- Result: kills leaderboard-by-noise on small cells; the O-05 trap (80.01 vs 81.01 vendor gap with no pairing) becomes structurally unclaimable.
- Maps to OUR workflow: ranking script consumes sheet.csv image_id-paired rows; family pre-declared in the validation-call packet (H44-48).
- Serves Odia 80.01 (three-way race settled by pairing, not points) + OldScan 55.3 (restoration deltas need paired proof vs Otsu).

[C4-103] Abstention reporting: coverage + conditional CER, never a scalar (§9.3)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.3 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: empty predictions reported as (coverage, conditional CER); scalar means over honest-empty are banned (O-12 precedent: anuvaad 0.711 vs 0.3162).
TRANSFER: SURVIVES — scorer-output split, already computable from metrics files (missing_prediction_count on disk).
extraction:
- Mechanism: split every engine summary into coverage (valid/1,227) + conditional CER (valid-only) + honest-empty count; §6.5 empty=1.0 rule stays for the pooled mean, shown alongside, never instead.
- Result: anuvaad-type coverage stories can't invert silently; doctr-type genuine-bad stays distinguishable from low-coverage-mid.
- Maps to OUR workflow: metrics.py summary already emits valid_samples_cer + missing counts — promote them to first-class leaderboard columns.
- Serves all weak cells: no engine routes on a scalar that hides abstention.

[C4-104] n<50 no-winner rule (§6.7 power gate, §9.3)
source_url: level2/probe22/AGENT_PROTOCOL.md §6.7 (disk, via campaign §9.3)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 4 | score: 100/125
decision: no winner claims on cells with n<50 (sat n=20, sarvam-subset n=3/lang); violators die at the hook.
TRANSFER: SURVIVES — counting rule, zero cost.
extraction:
- Mechanism: pre-declared power floor: cells below n=50 get intervals + description only, never rankings; sarvam-subset (O-13) is the extreme case (n=3/lang → description only).
- Result: sat routing (D4) must clear verification + pairing, never point gaps; protects the thinnest-evidence cell (C4-060 bridge risk).
- Maps to OUR workflow: hook asserts cell-n before any rank verb is published.
- Serves Santali 53.91 directly (n=20 fill); guards Kashmiri 54.82 VERIFY-FIRST langs.

[C4-105] Transfer cards SURVIVES/DIES/UNKNOWN on every method record (§9.1)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.1 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: the §9-upgrade table above is the C4 transfer-card roll-up; integration pass adjudicates DIES/UNKNOWN, never silent drops.
TRANSFER: SURVIVES — this record's own table is the existence proof.
extraction:
- Mechanism: each record names the harness fact that kills or saves it (weights/GPU/hidden-tests/keys → DIES or UNKNOWN, never "inspiration").
- Result: 62 SURVIVES / 8 DIES / 30 UNKNOWN for C4-001–100 — the integration pass now has a pre-sorted feasible set instead of 100 undifferentiated claims.
- Maps to OUR workflow: same shape as W6 feasible-set columns (§9.4: FEASIBLE NOW / FEASIBLE IF / INFEASIBLE).
- Serves all weak cells via decision-sorted evidence.

[C4-106] Transfer obituaries for every cited external number (§9.2)
source_url: docs/research/level7/c/c4/OBITUARIES.md (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: no external number enters a decision without a surviving obituary challenge; 13 obituaries (O-01–O-13), all DEAD, none revived.
TRANSFER: SURVIVES — flat-file discipline, zero dependencies.
extraction:
- Mechanism: number + where-cited + four-mismatch kill (languages/scan-quality/harness/metrics) + verdict + fail-condition (the disk evidence that would revive it).
- Result: formalizes the 87.39 practice; extends it to our own probe CERs (O-09–O-13 die outside probe22 without §9.3 dress).
- Maps to OUR workflow: obituary check is a pre-report hook item alongside pack-count and scorer-rule assertions.
- Serves every weak cell: vendor cells (53.91/54.82/55.3/80.01) and probe scalars alike are barred from W6 routing until dressed.

[C4-107] W6 feasible-set presentation: FEASIBLE NOW / FEASIBLE IF / INFEASIBLE (§9.4)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.4 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 4 | recency: 5 | actionability: 4 | score: 80/125
decision: validation call shows the training tree in three columns only; C4 UNKNOWN rows (30) are the FEASIBLE-IF inventory.
TRANSFER: SURVIVES — presentation rule over existing records.
extraction:
- Mechanism: three columns keyed on missing primaries (e.g. GPU budget answer for P2 rows C4-008/045/093/095; key/account rows C4-015/016/072/084 stay INFEASIBLE under no-paid-keys law).
- Result: the call decides missing-primaries, not methods — methods are pre-sorted.
- Maps to OUR workflow: CALL_PACKET.md agenda item; Miss-agent duty (PROMPT_MISS_AGENT task 5).
- Serves Kashmiri 54.82 / Santali 53.91: specialist bets appear as FEASIBLE-IF (GPU + verified GT), never as assumed.

[C4-108] Pre-declared kill criteria with operator-set thresholds (§9.5)
source_url: docs/research/LEVEL7_RESEARCH_CAMPAIGN.md §9.5 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 4 | recency: 5 | actionability: 4 | score: 80/125
decision: kill criteria drafted as conditions on MEASURED numbers before results are read; thresholds are user parameters, never agent inventions.
TRANSFER: SURVIVES — procedure, no dependencies.
extraction:
- Mechanism: conditions reference MEASURED numbers only (post-§9.3 dress); fantasy thresholds banned; >20%-fail → barred precedent (§6.4, gt_forensics ne-bar) is the template.
- Result: no post-hoc threshold shopping when weak-cell numbers land.
- Maps to OUR workflow: criteria drafted in the call packet, thresholds set by operator at H44-48.
- Serves Kashmiri 54.82 + ne-barred precedent (26.6): bars stay bars unless criteria + data change.

[C4-109] EN-sanity gate doctrine: sanity column before weak-cell claims (C4-099, hardened)
source_url: level2/probe22/en_sanity/manifest.json (disk, 2026-09-26; re-cite of C4-099)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: every tooling change (scorer flag, engine, normalization) re-runs the 30-pair EN column first; CER>~5 on clean renders = broken harness, stop.
TRANSFER: SURVIVES — on disk, 30 gold pairs, same gates, seed 20260926.
extraction:
- Mechanism: 30 official EN human pairs isolate harness bugs from model weakness (tesseract ~122% on ornate scans = genuine weakness with sound harness; doctr ~42%).
- Result: single most load-bearing logging invention of Phase 5; O-10/O-11 obituaries lean on it to separate GT-noise from engine weakness.
- Maps to OUR workflow: permanent gate; hook asserts EN column green before any weak-cell number publishes.
- Serves all weak cells: no Santali/Kashmiri/OldScan/Odia number trusted unless EN is green.

[C4-110] Scorer-integrity rules as executable gates (§6.5: empty=1.0, uncapped, space-forgery removed, single denominator)
source_url: level2/probe22/metrics.py + AGENT_PROTOCOL.md §6.5 (disk, 2026-09-26)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: scorer patches TDD-gated (C4-004); pre-report hook asserts §6.5 rules before any Phase-6 table publishes.
TRANSFER: SURVIVES — local code + tests.
extraction:
- Mechanism: per-row uncapped CER + cer_100_count, single denominator, space-forgery removed, empty pred = CER 1.0 counted; raw-vs-normalized ablation 0.6707 vs 0.6692 (Δ0.0015) gates the RLVR scorer.
- Result: forged zeros (old space-forgery bug, hostile-audit catch) become structurally impossible; O-09's dual-number trap (0.669 pooled vs 0.542 valid-only) stays visible.
- Maps to OUR workflow: red test asserting "empty scores 1.0 and counts" precedes every scorer edit.
- Serves Santali 53.91 / Odia 80.01 fill-cell agreement rates (forgery-prone cells).

[C4-111] Tier-split falsification: pair-GT vs pdf-GT vs fill-GT measured independently (§6.2)
source_url: level2/probe22/AGENT_PROTOCOL.md §6.2 (disk, 2026-09-26)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 4 | score: 100/125
decision: no blended CER crosses tiers; extractor-mirroring bias caught by tier separation (ks trust 45.0, ne-barred 26.6 precedent).
TRANSFER: SURVIVES — scoring split already in sheet.csv column set.
extraction:
- Mechanism: independent per-tier CER so retrieval-side corruption (PDF-layer mirroring) can't hide inside a blended mean; external validation: C4-076 (LangSmith retrieval/generation split).
- Result: the split is what barred ne and flagged ks/mr/gu/ur — the highest-ROI scoring decision in the campaign.
- Maps to OUR workflow: sheet.csv tier columns are mandatory; blended means are context-only.
- Serves Kashmiri 54.82 (trust 45.0) + ne-barred precedent directly.

[C4-112] Two-stage GT gate: forensics triage → human verification (§6.4 + gt_forensics)
source_url: level2/probe22/gt_forensics.json + AGENT_PROTOCOL.md §6.4 (disk, 2026-09-26; re-cite of C4-098)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 4 | score: 100/125
decision: machine trust scores bar (>20% fail → barred) and queue VERIFY-FIRST langs; W6 consumes passing langs only (D4 holds ks/mni/ur/sat/mr + ne-pdf barred).
TRANSFER: SURVIVES — on disk; humans decide, machines triage.
extraction:
- Mechanism: control chars / glyph breakage / script ratios → per-language trust; ne BARRED outright, ks/mr/gu/ur VERIFY-FIRST; ~2h human pass on 158 fill + ~77 PDF sample calibrates everything (C4-073 pattern).
- Result: in-house proof that C4-010 + C4-073 compose; O-02/O-03 fail-conditions point here (own-manifest verified GT).
- Maps to OUR workflow: D4 micro-repair (sat/ks 5–10 curated pages, W5, freeze-safe only) is the sole exception path.
- Serves Kashmiri 54.82 (45.0) + Odia-adjacent gu 51.4 + ne-barred precedent.

[C4-113] Credit-cap guard tooling: sarvam 54-call cap + spend gates (D2)
source_url: level2/probe22/sheet.sarvam_bench.discarded.csv + campaign D2 (disk, 2026-09-27)
date: 2026-09-27 | status: PRIMARY | relevance: 4 | recency: 5 | actionability: 5 | score: 100/125
decision: Sarvam EN skipped (no decision impact, saves 3 calls); no further sarvam_vision calls without explicit user approval; every credit-consuming tool needs an approval gate (C4-092 pattern).
TRANSFER: SURVIVES — cap is enforced process, already held (54 packs, 0 errors).
extraction:
- Mechanism: --limit-per-lang 3 hard cap + elicitation-style approval for any spend/state-changing tool; O-13 documents why the resulting n=54 number can never grow into evidence unapproved.
- Result: benchmark-target discipline (Sarvam measured, never routed) + budget survival.
- Maps to OUR workflow: AGENT_PROTOCOL §0 permission encoding (C4-028) includes the spend gate.
- Serves all weak cells via affordable, capped measurement.

[C4-114] Sequential-engine rule (§5): serialize inference, parallelize analysis
source_url: level2/probe22/AGENT_PROTOCOL.md §5 + 2026-09-26 parallel-engine post-mortem (disk)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: one heavy engine at a time (paddle ~2h/15GB, surya ~1h, indicphotoocr ~12h); lanes/analysis parallelize freely (C4-032 sanctioned shape).
TRANSFER: SURVIVES — scheduling rule, zero cost.
extraction:
- Mechanism: --skip-existing resume + retry-errors passes instead of parallel engines; stale-copy + memory violation of 2026-09-26 is the counterexample that justifies the rule.
- Result: long-horizon runs (C4-003 Rakuten precedent) stay tractable unattended without clobbering.
- Maps to OUR workflow: Engine-agent law (PROMPT_ENGINE_AGENT tasks 1-2); RSS/watch monitoring for overnight runs (C4-035 note).
- Serves OldScan 55.3 (worst-case 4250×6500 scans need unattended retry) + Kashmiri 54.82 (Nastaliq experiments need multi-hour runs).

[C4-115] Stale-copy hash-verify hook (2026-09-26 bilingual failure → structural fix)
source_url: level2/probe22/run_probe.py (disk; C4-001/C4-007 mapping)
date: 2026-09-26 | status: DERIVED | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: gatekeeper hook verifies run_probe.py hash before engine start; 102-pack bilingual FileNotFoundError class dies structurally.
TRANSFER: SURVIVES — local hook, no dependencies.
extraction:
- Mechanism: session-start hook reloads current run_probe.py hash + protocol (C4-059 pattern); executor agents run the real file, never a copy; pre-report hook asserts pack count == manifest n (catches sa-path class at write time).
- Result: the campaign's most expensive failure mode (100 sa packs) becomes a hook rejection, not a post-mortem.
- Maps to OUR workflow: AGENT_PROTOCOL §0 permission shape (C4-028) + prove-claim sampling (C4-064) both assume current-code execution.
- Serves every weak cell via process reliability (GT-gate regressions blocked the same way).

[C4-116] probe-eval skill packaging: score-engine / verify-sample / rank-lane (C4-036/068/080)
source_url: https://deepeval.com/blog/what-is-an-eval-harness (re-cite C4-068; 2026-08-19)
date: 2026-08-19 | status: DERIVED | relevance: 4 | recency: 5 | actionability: 4 | score: 80/125
decision: distribute probe ops as a versioned skill (npx-skills-add shape), identical across Engine/Verdict/Miss sessions; kills command-drift.
TRANSFER: SURVIVES (pattern) — packaging is free; installs per-session.
extraction:
- Mechanism: `score-engine` (gt_pred build + metrics.py both modes + sheet append), `verify-gt-sample` (§6.4 sampler → gt_verification.json), `rank-lane` (score + §9.3 dress + threshold filter); stop/pre-commit hook runs the eval so green metrics gate (C4-068 shape).
- Result: every executor session runs identical scoring; stale-copy class failures have nowhere to hide.
- Maps to OUR workflow: Miss-agent lane ops + integration-pass adoption.
- Serves Odia 80.01 + OldScan 55.3 via repeatable scoring.

[C4-117] Probe MCP tool surface: manifest / packs / scorer / sampler as Tools + Resources (C4-041/047)
source_url: https://modelcontextprotocol.io/specification/draft (re-cite C4-041; draft spec)
date: 2026-09-26 (accessed) | status: DERIVED | relevance: 4 | recency: 5 | actionability: 3 | score: 60/125
decision: Phase-6-as-composition is the integration-pass blueprint; build is post-freeze (H30-40).
TRANSFER: UNKNOWN — needs TS/Python MCP build effort; no keys/GPU, but real work.
extraction:
- Mechanism: manifest query + pack status as Resources (Verdict/Miss read-only), metrics.py run + verification sampler + sheet append as Tools (Engine-gated); Tasks extension matches overnight runs; Skills-over-MCP matches C4-116.
- Result: Engine/Verdict/Miss share one auditable interface instead of bespoke bash; tool-call reliability bar per C4-018.
- Maps to OUR workflow: read/write split mirrors lane-dir discipline (C4-049); security posture per C4-044/054 (read-scoped default, hash-pinned servers).
- Serves all weak cells via uniform auditable tooling.

[C4-118] Ledger-as-vault graph queries for the integration pass (C4-055/060/064)
source_url: https://github.com/obra/knowledge-graph (re-cite C4-055; 2026-03-21)
date: 2026-03-21 | status: DERIVED | relevance: 4 | recency: 3 | actionability: 4 | score: 48/125
decision: run Level-7 ledgers as a vault at integration: Louvain clusters per weak cell, path queries for contradiction chains, PageRank for most-cited methods.
TRANSFER: SURVIVES — local SQLite-vec/FTS5, no cloud APIs (C4-050).
extraction:
- Mechanism: vault → graph (files=nodes, wikilinks=edges); Tarjan bridges find single-point-of-failure claims (lone Santali-script assertions); prove-claim SOP (C4-064) is the Verdict sampling procedure.
- Result: integration pass navigates evidence instead of re-reading 400+ artifacts; thinnest-evidence cells (sat n=20) get structural attention.
- Maps to OUR workflow: Miss-agent integration duty; contradiction chains feed §5-resolution with disk evidence.
- Serves Santali 53.91 (thinnest evidence) + Kashmiri 54.82 (Nastaliq claim tracing).

[C4-119] Verdict-sampling SOP + contradiction-log retention (FORMAT §§4-5, hardened)
source_url: docs/research/level7/c/c4/LEDGER_FORMAT.md §§4-5 (disk, 2026-09-26)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: 10% live-source re-check stands (C4-010…100 pre-registered); >20% sampled-failure voids the lane; contradictions resolved in integration with disk evidence, never silent drops.
TRANSFER: SURVIVES — this campaign's own QA, already running.
extraction:
- Mechanism: sampled record fails on dead URL / >3-month date error / misstated extraction; contradiction log line (`CONTRADICTS: <doc> §<x>`) kept on both records (C4-078 precedent).
- Result: verification fractals — GT verified (§6.4), scorer verified (§6.5/C4-110), ledger verified (§4) — each with a numeric bar; W6 consumes only triple-surviving numbers (C4-100).
- Maps to OUR workflow: identical spirit to >20%-fail bars; C4-119 is the ledger half of C4-100's doctrine.
- Serves every weak cell: numbers surviving three layers are the only W6 inputs.

[C4-120] sheet.csv as eval-dataset schema (LangSmith-shape equivalence, C4-090)
source_url: https://docs.langchain.com/langsmith/evaluate-chatbot-tutorial (re-cite C4-090)
date: 2026-09-26 (accessed) | status: DERIVED | relevance: 3 | recency: 5 | actionability: 4 | score: 60/125
decision: document sheet.csv columns as the dataset schema (image_id/language/script/.../CER/WER/error_tag); future LangSmith/TS import is mechanical.
TRANSFER: SURVIVES — documentation over existing columns.
extraction:
- Mechanism: column set ≡ dataset schema (inputs/outputs/expected); error_tag taxonomy ≡ expected-steps metadata; old_scan tag becomes a first-class eval slice for the §6.8 stratification.
- Result: offline tier tables per engine are already dataset-disciplined; online drift watch (C4-072) can attach later without re-scoring history.
- Maps to OUR workflow: Phase-6 → W6 handoff format; traceable()/evaluate() port (C4-089) inherits the semantics, not just the API.
- Serves OldScan 55.3 (old_scan slice) + Odia 80.01 (repeatable per-engine tables).

[C4-121] Minimal-agent preference: looped-generateText over framework (C4-091, hardened)
source_url: https://vercel.com/kb/guide/how-to-build-ai-agents-with-vercel-and-the-ai-sdk (re-cite C4-091)
date: 2026-09-26 (accessed) | status: DERIVED | relevance: 3 | recency: 5 | actionability: 3 | score: 45/125
decision: probe-analysis agents stay minimal (manifest/scorer/sheet tools in a capped loop) unless observability needs (C4-075) force Mastra/LangChain.
TRANSFER: SURVIVES — preference rule, zero cost; UNKNOWN only if TS build is chosen (then C4-081/089 govern).
extraction:
- Mechanism: single-call default → opt-in loop via stopWhen; step caps mirror --limit-per-lang credit guards; approval gates on spend/state tools (C4-092).
- Result: weakest-cell tooling stays auditable (Pi-harness precedent C4-038: ~6 tools suffice); framework lock-in deferred to the H30-40 serving pick (C4-087).
- Maps to OUR workflow: keeps Engine/Verdict/Miss prompts portable (C4-019) and trajectories loggable (C4-020).
- Serves all weak cells via minimal auditable analysis surface.

[C4-122] No-downloads / no-training as tooling constraints (§0 rule 1, §9 W6 guards)
source_url: level2/probe22/AGENT_PROTOCOL.md §0 + OCR_AGENT_MEMORY_FEED.md §9 (disk)
date: 2026-09-26 | status: PRIMARY | relevance: 5 | recency: 5 | actionability: 5 | score: 125/125
decision: every C4 UNKNOWN gated on downloads/GPU stays UNKNOWN until user approval (P1/P2 packets: C4-008/045/093/095); machine GT never trains (RLVR on human-verified gold only).
TRANSFER: SURVIVES — the constraint is the decision (standing law, user-delegated 2026-09-27).
extraction:
- Mechanism: P2 approval packet shape (size/license/coverage/MCP path, C4-095 precedent); scout-pattern verification without fetching weights (C4-034); synthesis allowed for harness fixtures only (C4-078 guardrail).
- Result: 30 UNKNOWN rows are a permission queue, not a backlog — the validation call clears them with approvals, not arguments.
- Maps to OUR workflow: lane accounting (FORMAT §6: nothing at root, nothing under level2/research/) + sealed-dirs rule (C4-027/028 permissions).
- Serves Santali 53.91 / Kashmiri 54.82: specialist models evaluated identically IF approved, never smuggled.

---

T9 tally: 22 records (C4-101–122). Entering architecture (≥30): 101, 102, 103,
104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
120, 121, 122 (all 22 — §9-native by construction).
Ledger totals: 122 C4 records + format doc. Verdict sample extends every 10th:
C4-110, C4-120 newly sampled (plus C4-010…100 standing).
