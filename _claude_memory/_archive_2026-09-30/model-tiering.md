---
name: model-tiering
description: NEVER spawn subagents on Opus — it burns the boss's credits. Opus plans and writes prompts only; Sonnet executes with subagents.
metadata:
  type: feedback
---

**HARD RULE: never spawn a subagent while running on Opus.** Not for research, not for recon, not "just three small ones."

**Why:** Opus subagents consume the boss's credits at a rate he cannot afford. On 2026-09-29 I launched three Opus recon agents during a planning session and he stopped me: *"i will kill u if u use opus for sub agent."* The credits are the binding constraint on this campaign, not capability.

**The division of labour he wants:**
- **Opus (planning tier)** — read the concerns, hold the whole picture, decide the architecture, write the protocol to memory and to repo md files, and produce the *prompt*. It does not execute. It does not dispatch. Its entire output is a plan plus a prompt.
- **Sonnet (execution tier)** — he switches the model himself, pastes the prompt, and Sonnet does all the labour, spawning whatever subagents the work needs.

**How to apply:** While on Opus, if I find myself reaching for the Agent or Workflow tool, stop — that is the signal the plan is done and it is time to hand him the prompt instead. Write the detail into the md file, keep the prompt short (he has a standing rule that prompts are one line and detail lives in the file), and tell him it's ready for the model switch. If a task genuinely needs execution before he switches, ask first rather than dispatching.

**2026-09-30 reinforcement:** I edited protocol lines in a repo script and the global OpenCode `AGENTS.md` myself; the boss: *"why the hell are you doing the work man, i said i will assign to the agent"*. Even a two-line fix is labour → write it as a fix-spec inside a protocol and let the boss assign it. Opus may: run read-only checks needed to make a protocol accurate; write/update memory protocol files, `MEMORY.md`, and the `NEXT.md` pointer. Opus may not (unless the boss explicitly says "you do it"): edit repo files or scripts, change global configs, install, download, move or delete.

Related: [[user-profile]], [[boss-standard]]
