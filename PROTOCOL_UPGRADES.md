# PROTOCOL_UPGRADES.md — D5
**Date:** 2026-09-28 | **Source:** Untitled T5 + Verdict agent self-improvement plan (adopted)
**Scope:** Agent workflow upgrades — Verdict primary, all agents secondary.

---

## 1. WHAT THIS DOCUMENT OWNS

All adopted workflow changes for the 3-agent ops model. Replaces scattered prompt fixes with one canonical upgrade list. Source: T5.1 + T5.2 + T5.3 from Untitled, plus Verdict agent's own self-improvement plan (already deployed 2026-09-28).

---

## 2. VERDICT AGENT UPGRADES (T5.1 + T5.2)

### 2.1 Autonomy within scope (T5.1)
**Before:** Verdict asks "what do I do next?" repeatedly.
**After:** Verdict works autonomously within its scope (§6.4 verification, Lane B research, fix-specs for own artifacts + specs to Miss for shared). Surfaces ONLY genuine boss-level decisions.

### 2.2 Nerve to counter Boss (T5.1)
**Before:** Verdict accepts Boss directives without question.
**After:** Verdict HAS THE NERVE TO COUNTER the Boss when a directive is wrong — with evidence (cite file:line + MEASURED/REJECTED status). Authority: §10 of OCR_AGENT_MEMORY_FEED.md + audit reconciliation history.

### 2.3 Self-improvement plan (T5.2 — ADOPTED)

| Upgrade | Status | Where |
|---|---|---|
| Pre-flight engine readiness checks | ✅ DEPLOYED 2026-09-28 | `level2/probe22/verify_engine_readiness.py` |
| In-progress engine health monitoring | ✅ DEPLOYED 2026-09-28 | `level2/probe22/spot_check_engine.py` + `engine_health_log.py` |
| Internal hostile self-audit before external review | ✅ DEPLOYED 2026-09-28 | `level2/probe22/self_audit.py` |
| §9 schema gates at write-time | ✅ DEPLOYED 2026-09-28 | Research subagent prompts embed "validate all 10 §9 fields before write" |
| Structured ≤2,000-token briefing format | ✅ DEPLOYED 2026-09-28 | `level2/probe22/orchestrator_briefing_template.md` (5 sections: DECISIONS NEEDED \| DELIVERED \| BLOCKERS \| RISKS \| NEXT) |
| Proactive fix-specs on first detection (<1hr) | ✅ DEPLOYED 2026-09-28 | Verdict prompt §"Proactive fix spec emission" |
| Formal engine-agent health contract | ✅ DEPLOYED 2026-09-28 | `level2/probe22/engine_agent_contract.json` v1.0.0 |

---

## 3. ALL-AGENT UPGRADES (T5.3)

### 3.1 5-section briefing format (mandatory for all agent→orchestrator reports)

```
## DECISIONS NEEDED
| decision | authority | evidence |
| --- | --- | --- |
| ... | user/orchestrator | file:line + MEASURED/REJECTED |

## DELIVERED
| artifact | status | location |
| --- | --- | --- |
| ... | DONE/PARTIAL | ... |

## BLOCKERS
| blocker | owner | unblock action |
| --- | --- | --- |
| ... | user/orchestrator/other agent | ... |

## RISKS
| risk | probability | impact | mitigation |
| --- | --- | --- | --- |
| ... | LOW/MED/HIGH | ... | ... |

## NEXT ACTIONS (≤5, ordered)
1. ...
2. ...
```

**Hard cap:** 2,000 tokens per briefing. Tables only. No essays.

### 3.2 §9 pre-write gate (mandatory for all research subagents)

Before writing ANY research record, validate all 10 §9 fields:
1. `source_url`
2. `date`
3. `status` (PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD)
4. `relevance` (1-5)
5. `recency` (1-5)
6. `actionability` (1-5)
7. `extraction` (3-10 lines: mechanism → result → how it maps to our goal)
8. `decision_it_changes`
9. `transfer` (SURVIVES/DIES/UNKNOWN against our harness facts)
10. `transfer_harness_fact`

If any missing → REJECT the record, do not write.

### 3.3 Proactive fix-spec emission (mandatory for Verdict)

On first detection of any issue in shared docs/artifacts, emit Fix Spec immediately:
- Exact file:line
- Exact change (text-edit spec)
- Exact evidence (cite source)
- Deadline (≤2 hours from detection)

Hand to Miss for application. Max 2 fix-loop rounds → escalate to user.

### 3.4 One-line dispatch prompts (T6.2)

Prompts to agents should be ONE-LINE where possible: "read file X and implement it" — the detail lives in the md file, NOT in the prompt. Do not repeat md content inside prompts.

### 3.5 Existing-agent lane injection (T6.3)

Where work aligns with an existing agent's lane, inject it into that agent's queue. Spin up a new sub-agent only for unowned work.

Examples:
- Engine owns probe22 execution → Lane A research + Phase 6 scoring injected there
- Verdict owns §6.4 verification → Lane B research + lane verification injected there
- Miss owns Lane C + monitoring → validation-call coordination + fix-spec application injected there

---

## 4. REJECTION CRITERIA (what to push back on)

Per T5.1 + audit reconciliation history, Verdict (and all agents) should REJECT:
1. **Stale claims** — anything that contradicts current disk truth (verify via command)
2. **Vibes-based architecture** — no paper, no bench, no failure slice cited
3. **Pretrained knowledge** — must pull 2025-2026 papers via live sources (MCP parallel-search/context7)
4. **Hidden downloads** — anything that would touch `~/.cache/huggingface/` or external resources without explicit user approval
5. **Self-confirming evals** — when scorer, model, and designer are all the same source
6. **"Quick fixes"** — patches that bypass gates (e.g., lower MAX_CTRL_CHARS to force items through)

When rejecting: cite file:line + provide MEASURED counter-evidence + propose corrected approach.

---

## 5. WHAT THIS DOCUMENT DOES NOT CHANGE

- §9 hard rules in `OCR_AGENT_MEMORY_FEED.md` — still binding
- §6.4 GT verdicts LOCKED 2026-09-27 — still binding
- Decisions D1-D4 in `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §10 — still binding
- SEALED directories (level2/out/, level2/reports/, etc.) — still sealed
- No downloads, no training, no Sarvam calls beyond cap — still binding

---

## 6. ADOPTION CHECKLIST

| Agent | Adopt 5-section briefing | Adopt §9 pre-write gate | Adopt proactive fix-specs | Adopt one-line dispatch |
|---|---|---|---|---|
| Engine | ✅ | ✅ | ✅ (Lane A only) | ✅ |
| Verdict | ✅ | ✅ | ✅ (primary) | ✅ |
| Miss | ✅ | ✅ (Lane C) | ✅ (apply specs) | ✅ |
| Sub-agents | ✅ | ✅ | n/a | ✅ |

---

## 7. TOKEN SPEND IMPACT

Pre-upgrade: agent→orchestrator reports averaged 4,500 tokens (essays + repeated context).
Post-upgrade: ≤2,000 tokens (tables only, structured).
**Saving:** ~55% on every agent report × ~50 reports/day = significant.

---

## 8. NEXT REVIEW

This document to be reviewed at W5 freeze (after Wed 2026-10-01). Any new upgrades from Boss or Boss-level decisions appended here.
