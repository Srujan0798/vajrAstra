---
name: proto-77-graph-concerns
description: "Added 2026-09-30 — boss's C3 (\"50 concerns in the graph… I kept graphify\") and M4: make the knowledge graph show every concern as a node linked to its protocol, deliverable and evidence; use graphify for navigation, orphans and duplicates; rebuild after each structural wave"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:36.783Z
---

# PROTO-77 — GRAPH THE CONCERNS (Miss, graphify skill) — uses `graphify-out/`

**Boss:** C3 "if you were working you would have seen all 50, minimum 50 [concerns in the graph]… I have given you 100+"; M4 "I kept graphify". Current graph: 3,990 nodes / 4,681 edges /
420 communities (rebuilt 2026-09-29 18:24, before the 27-doc move and all Wave 1 outputs) — stale paths now.

## Steps
1. Load the graphify skill (`/graphify` instructions in `~/.claude/skills/graphify/SKILL.md`). Read its query/update modes first.
2. After [[proto-66-concern-register-rebuild]] exists: make each register row a first-class node — the register must be in the corpus and each row identifiable
   (ID + short title). Verify with a graph query that CO-001…096, C1–C17, M1–M8 each resolve to a node, and that each has edges to its protocol file and deliverable.
3. Incremental update (`--update`) after each structural wave (proto-70/72/73/74) so moved files are re-linked; full rebuild only if the skill says incremental cannot handle moves.
4. Use the graph as an audit tool: list orphan md nodes (degree 0–1), duplicate-label nodes across files (feeds proto-73), communities that mix superseded and live docs.
5. Report `docs/campaign/checkpoints/GRAPH_STATUS.md`: node/edge counts, concern-node coverage (n of N), orphans, duplicates, and the command used.

## Done when
Every concern ID in the register resolves to a graph node with ≥1 edge to its protocol and ≥1 edge to evidence or deliverable; the graph report is regenerated after the last structural wave.

Related: [[proto-66-concern-register-rebuild]], [[proto-72-per-file-audit]], [[proto-73-md-fact-consolidation]]
