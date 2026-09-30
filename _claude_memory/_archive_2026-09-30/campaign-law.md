---
name: campaign-law
description: The 3-agent architecture (Engine/Verdict/Miss), their lanes, file-based interfaces, and the cross-check law governing the South OCR campaign
metadata:
  type: project
---

The campaign runs as exactly **three top-level agents**, simultaneous. No fourth. Each may spawn subagents freely.

**AGENT 1 — Engine.** Owns OCR engines, model execution, probe runs, scoring pipelines, downloads (only with explicit boss approval), GPU/compute, engine queues, kill/restart of stuck processes. Must not edit protocol docs owned by others, or call a result final without Verdict sign-off.

**AGENT 2 — Verdict.** Owns GT verification, forensics, scorer rules, hostile audits, fix-specs, leaderboards, and the TRUTH-status of every other agent's output. Must counter-check every Engine and Miss output. Has standing authority — and obligation — to counter the boss with evidence.

**AGENT 3 — Miss (Miscellaneous).** Owns everything else: file hygiene, doc merges, protocol edits, dispatch logistics, integration glue, `BOSS_CONCERNS.md`, `DISPATCH_LOG.md`, cleanup execution via fix-specs. Must not overwrite Engine/Verdict work or apply fix-specs touching truth-bearing artifacts without Verdict verification.

**Interfaces — file-based, append-only:**
- `level2/probe22/engine_health_log.jsonl` — Engine writes, all read
- `level2/probe22/fix_specs/` — anyone proposes, Miss applies, Verdict verifies
- `DISPATCH_LOG.md` — Miss maintains, all obey
- `BOSS_CONCERNS.md` — Miss maintains, every agent reads at every turn
- `PROTOCOL_UPGRADES.md` — Verdict drafts, boss approves

**CROSS-CHECK LAW:** every agent's output is checked by at least one other agent before it counts as truth. Nothing reaches the boss unverified.

**Orchestration, not labor.** Top-level agents dispatch and monitor; labor goes to subagents. Work belonging to an existing lane joins that lane's queue — new agents only for genuinely unowned work. Anything the lead cannot cover goes into `DISPATCH_LOG.md` for the boss to assign; the lead does the *higher* work, subagents do the *broad* work.

**Cycle-graph workflow:** dispatch → subagent reports → monitors verify → lead implements → re-audit → next cycle. A subagent's report is evidence, not a verdict. Monitors re-open a random sample of every subagent's verdicts and link-check every MERGE/DELETE before it executes.

**Council deliberation:** load-bearing md/audit decisions get a structured multi-reviewer pass. No single-agent fiat on documents the campaign depends on.

**Why:** The boss watched agents stall, duplicate each other, and silently drop work. Lane ownership plus file-based interfaces means state survives any individual agent dying, and no two agents can silently disagree about the same artifact.

**How to apply:** Before dispatching, ask which lane owns the work. Before writing to a shared file, check the owner above. Never let a subagent's self-report stand as truth — it needs a second pass.

Related: [[boss-standard]], [[campaign-state]], [[open-front]]
