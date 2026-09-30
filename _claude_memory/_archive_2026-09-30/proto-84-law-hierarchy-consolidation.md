---
name: proto-84-law-hierarchy-consolidation
description: "Added 2026-09-30 — law is spread over 6+ documents (two different \"12 standing laws\", feed §9 hard rules, AGENTS.md, directive Part C, proto-01) and the declared \"Master doc\" FULL TECHNICAL BRIEFING Part II is 2 days stale; build one layered law index with no contradictions and refresh or banner the stale master"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T22:12:34.042Z
---

# PROTO-84 — ONE LAW HIERARCHY (Verdict maps conflicts, Miss applies after the boss sees the map)

**Found 2026-09-30:** law documents — `docs/campaign/CAMPAIGN_DIRECTIVE.md` (Part B/C), `AGENTS.md` (load order + identity), `OCR_AGENT_MEMORY_FEED.md` §9 (hard rules) + §10–§19 locks,
`FULL TECHNICAL BRIEFING.md` Part II §3 ("the 12 standing laws"), `level2/ULTIMATE_HYBRID_CONCERN.md` Part II §4 ("THE 12 STANDING LAWS", L1–L12 incl. L6 "never claim 10 independent", L11
"one fact one file", L12 D12 "new scope auto-rejected inside T-4 of a demo") + Parts VIII–IX amendments, `level2/probe22/AGENT_PROTOCOL.md` §0, `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §7/§9/§10,
`SOUTH_CANON.md` §N, memory `proto-01`. Two "12 laws" lists differ in wording and scope. `FULL TECHNICAL BRIEFING.md` Part II (the doc AGENTS.md calls "Master doc") still shows 2026-09-27
evening state ("surya queued", "W5 freeze Oct 1", "LEVEL7_INTEGRATED_ARCHITECTURE.md" — check it exists). Agents obeyed some laws and broke others (e.g. L6 engine count, L11 duplicates).

## Verdict subagent — TASK (paste after the shared context block)
> 1. Extract every rule from each law document above into one table: rule text (verbatim) · source file:line · scope (campaign / process / probe / South bench / agent behaviour) · status
>    (in force / superseded by X / contradicted by Y). Deduplicate identical rules; list CONTRADICTIONS explicitly (e.g. seals vs the boss's U10 approval; "10 independent" vs L6; W5 dates).
> 2. Propose a layered hierarchy: Layer 0 boss decisions (U-table) → Layer 1 campaign directive → Layer 2 process law (feed §9) → Layer 3 domain law (probe AGENT_PROTOCOL; South bench
>    ULTIMATE_HYBRID_CONCERN) → Layer 4 agent execution protocols (memory proto files). "Higher layer wins; later dated amendment wins within a layer."
> 3. Staleness check of every "current state" section in these docs (FULL TECHNICAL BRIEFING Part II §6–§9, README "State", docs/INDEX.md, SOUTH_CANON §L, PROJECT_COMPLETE) against disk.
> Write `docs/campaign/LAW_MAP.md` (≤2,000 words + the rule table as an appendix).

## Miss applies (after Verdict review; append-only law files get errata lines, not rewrites)
- `AGENTS.md` load order points to `LAW_MAP.md` as step 0.5.
- Stale "current state" sections get a dated banner "SUPERSEDED — current state: docs/campaign/CAMPAIGN_DIRECTIVE.md Part A" or a refresh generated from disk (no hand-typed numbers).
- Duplicated laws: the lower-layer copy becomes a pointer to the owning layer.

Related: [[proto-73-md-fact-consolidation]], [[proto-66-concern-register-rebuild]], [[proto-01-law-and-guardrails]]
