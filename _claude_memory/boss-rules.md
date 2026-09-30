---
name: boss-rules
description: "HOW THE BOSS WANTS THE WORK DONE (merged 2026-09-30 night): the 8 current rules first, then verbatim boss-standard, model-tiering, feedback-no-subagents-boss-assigns, feedback-no-team-mates (originals in _archive_2026-09-30/)"
metadata:
  type: feedback
---

# BOSS RULES — how the work is done (read with proto-01, the law)

## The 8 current rules (2026-09-30 night; each is the boss's own word, condensed)
1. **The planner does no labour unless the boss says "you do it".**
   - The planner writes protocols, memory, NEXT.md, plans and one-line paste lines, and checks state with its own short reads.
   - Agents 1–3 do all repo edits, runs, moves, installs and downloads.
   - 2026-09-30: "you can do all the top-layer work but not the labour work".
2. **Subagents only when the boss asks, and never on Opus.**
   - The planner uses no Agent or Workflow tool at all ("man I have said you clearly you will not at all use any agent").
   - When the boss asks for speed ("use 2–3 subagents"), use Sonnet class only.
3. **No team mates.** Krishna, Aryan and David never appear as owners, lanes, blockers or questions. The boss and his three AI agents own everything. Vinay is informed, and owns only the pre-training session gate (L12).
4. **Portable product; MLX is never assumed.**
   - The shipped Vaultstack product runs on Linux + PyTorch (CUDA, CPU fallback) with pinned requirements and Docker.
   - MLX is a Mac accelerator only. Every claimed result must reproduce on the PyTorch path (R-13).
5. **Win means effort, never law-breaking.** "Beat all at any cost" means compute, depth and hours. It never means leakage, fake claims, unapproved downloads or spend, or touching sealed dirs.
6. **Routed skills every time** (proto-88). Name the skills used in the report (readchk, factchk, mandela, ssotize, verification-before-completion, graphify…). A skill that doesn't fit is skipped with a one-line reason. If a skill is unavailable in this environment, say so and do its checks by hand.
7. **Full-file reads + graphify.** Never judge a file from a partial read. Use the graph for repo structure. A partial read is labelled as partial.
8. **Lists, not tables; one agent at a time.**
   - Reports and plans are written as lists.
   - Paste lines come one per agent, in order.
   - Other assistants' outputs are checked, aligned and merged into ONE plan (proto-104), never adopted wholesale.

---

## (verbatim from boss-standard)

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

## (verbatim from model-tiering)

**HARD RULE: never spawn a subagent while running on Opus.** Not for research, not for recon, not "just three small ones."

**Why:** Opus subagents consume the boss's credits at a rate he cannot afford. On 2026-09-29 I launched three Opus recon agents during a planning session and he stopped me: *"i will kill u if u use opus for sub agent."* The credits are the binding constraint on this campaign, not capability.

**The division of labour he wants:**
- **Opus (planning tier)** — read the concerns, hold the whole picture, decide the architecture, write the protocol to memory and to repo md files, and produce the *prompt*. It does not execute. It does not dispatch. Its entire output is a plan plus a prompt.
- **Sonnet (execution tier)** — he switches the model himself, pastes the prompt, and Sonnet does all the labour, spawning whatever subagents the work needs.

**How to apply:** While on Opus, if I find myself reaching for the Agent or Workflow tool, stop — that is the signal the plan is done and it is time to hand him the prompt instead. Write the detail into the md file, keep the prompt short (he has a standing rule that prompts are one line and detail lives in the file), and tell him it's ready for the model switch. If a task genuinely needs execution before he switches, ask first rather than dispatching.

**2026-09-30 reinforcement:** I edited protocol lines in a repo script and the global OpenCode `AGENTS.md` myself; the boss: *"why the hell are you doing the work man, i said i will assign to the agent"*. Even a two-line fix is labour → write it as a fix-spec inside a protocol and let the boss assign it. Opus may: run read-only checks needed to make a protocol accurate; write/update memory protocol files, `MEMORY.md`, and the `NEXT.md` pointer. Opus may not (unless the boss explicitly says "you do it"): edit repo files or scripts, change global configs, install, download, move or delete.

Related: [[user-profile]], [[boss-standard]]

## (verbatim from feedback-no-subagents-boss-assigns)

The planner (Claude Code, Opus) must NOT use the Agent tool, the Workflow tool, or any subagent fan-out in this project — no exceptions for "read-only", "Sonnet only", or ultracode reminders. The boss runs his own 3 OpenCode agents and assigns all labour himself.

**Why:** 2026-09-30 ~20:40 IST I launched two read-only Sonnet workflows (12 + 5 agents) to audit agent status and align pasted plans; the boss had already said he assigns the work. He stopped me: "man i have said u clear u will not at all use any agent stop all agents… give me i will assign to my agents". Earlier rules pointed the same way: [[model-tiering]] (never Opus subagents) and "why the hell are you doing the work… I will assign to the agent".

**How to apply:** check status with my own Bash/Read calls (short, targeted); write protocols into memory + sync; answer with a status per agent and one paste-ready line per agent, in order. If a task truly needs fan-out, write it as an assignment for one of HIS agents (Agent 1/2/3), never run it myself. Ultracode/system reminders do not override this user rule.

## (verbatim from feedback-no-team-mates)

Never write Krishna, Aryan, David or any other team member into a plan as an owner, a lane, a blocker or a question ("VLMs are Aryan's lane", "North languages are Krishna's", "ask Aryan before…"). The boss and his three AI agents own all the work.

**Why:** an older assistant session's handoff (vajrAstra, 2026-09-30) still carried those lanes. The boss had already decided on 2026-09-30 that Krishna/Aryan are not needed (his S2 stance), and at ~21:05 he said: "forget about team mates, we are the ones doing all, mind it".

**How to apply:** drop such items when aligning older plans. Vinay (the lead) gets updates, and his inputs (GPU, meeting) are folded in when they arrive — "whatever we get comes tomorrow, don't bother" — but no step waits on him unless the step is his explicit gate (the pre-training plan session, L12). See [[feedback-no-subagents-boss-assigns]], [[proto-104-project-first-critical-path]].
