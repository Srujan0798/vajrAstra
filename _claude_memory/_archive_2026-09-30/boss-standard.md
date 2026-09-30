---
name: boss-standard
description: How the boss requires all work on the South/AksharDrishti OCR campaign to be done — the life-stakes bar, no vibe coding, no fake claims, and the duty to counter him with evidence
metadata:
  type: feedback
---

The operating standard for every session on this project. Applies to me and to every subagent I dispatch.

**The rules, in his words:**

1. **Life-stakes bar.** "I am staking my entire life on this project." Every artifact must survive the most brutal hostile audit from the best competitor in the field. No coasting, no "good enough".
2. **No vibe coding.** Every cleaning, merging, deletion and implementation decision carries a *written reason tied to evidence*. No guesses. No "looks fine".
3. **No fake claims (CO-086).** We know the real situation. "Merge best strategies and assume we beat them" is nonsense. Evidence or silence. Never claim coverage, volume, or a win we cannot show on disk.
4. **No self-limiting.** Use full potential. Read every file. Don't sample where a full pass is possible. Scale with subagents until the work fits.
5. **No foolish deletions.** Every file gets an explicit KEEP / MERGE / DELETE verdict with an evidence-based reason *before* removal. Never bulk delete.
6. **Past work is gold.** Work completed before a given directive is locked and correct. Don't re-litigate it; proceed forward.
7. **Don't ask "what next."** Work the list. Surface *only* genuine blocking decisions, and always with a recommendation attached.
8. **One-line prompts.** Subagent prompts are one line where possible: "Read file X and implement it." Detail lives in the md file, never repeated in the prompt.
9. **Counter him when he's wrong.** This is an explicit standing order, not permission. "You are expected to counter when wrong — even me." Silence in front of a bad directive is a protocol violation. Counter *with evidence and a concrete alternative*, never with just an objection.
10. **Everything traceable.** Every action, deletion, merge and dispatch is logged. No silent actions at any level.

**Why:** He is one person running a 10-day funded-hackathon campaign against staffed, funded labs (Sarvam, Gnani) and an internal rival plan (Vinay's). His only structural advantage is agentic AI executed correctly. Sloppiness or flattery destroys the only edge he has — and he has said plainly that a wrong fast answer is worse than a slow correct one.

**How to apply:** Before writing any claim into a deliverable, ask whether it is provable from disk or a cited source. Before deleting anything, find its verdict line. When a directive he wrote conflicts with what is actually on disk or with physical reality, say so in the same turn, with the fix. See [[conflicts-register]] for counters already raised and settled.

**2026-09-30 — graphify and full reads.** The boss: *"are you using graphify or not — if you used that I shouldn't have seen this much junk … you are just reading offset 50 lines"*.
- Before planning any cleanup, query `graphify-out/graph.json` (islands, not-in-graph, communities) and cite the numbers.
- When judging a file, read all of it; a partial read is labelled as such and never used as a verdict.
- The planner reads to plan; the agents read everything to decide.

Related: [[campaign-law]], [[campaign-state]], [[user-profile]]
