# Orchestrator Briefing Template (Verdict Agent)

Use this format for **every** Verdict → Orchestrator handoff. ≤2,000 tokens. No essays.

```
## VERDICT BRIEFING — <engine or topic> — <ISO timestamp>

### 1. DECISIONS NEEDED (orchestrator action required)
1. <decision>: <one-line context + recommended action>
2. ...

### 2. DELIVERED (what landed on disk)
- <artifact path>: <one-line status>
- <artifact path>: <one-line status>

### 3. BLOCKERS (cannot proceed without)
- <blocker>: <what blocks> | <unblock path>

### 4. RISKS (newly surfaced; do not re-list known risks)
- <risk>: <trigger> → <mitigation>

### 5. NEXT ACTIONS (verdict commits)
- [ ] <action> by <deadline if known>
- [ ] <action> by <deadline if known>
```

## RULES
- ≤2,000 tokens. Cut prose, not evidence.
- Every record/note carries: source_url, date, status (PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD), relevance, recency, actionability, extraction, decision_it_changes, transfer, transfer_harness_fact.
- Honest-empty > soft guess. Mark UNKNOWN when truth isn't on disk.
- Never re-litigate locked verdicts. Cite the lock (§6.4, D1–D4, etc.) and move on.
- Never edit sealed dirs: `level2/out/`, `level2/reports/`. Read-only there.
- Sarvam: respect the 54-call cap. Stop and ask before exceeding.
- Engine ↔ Verdict contract: see `engine_agent_contract.json` next to this file.
