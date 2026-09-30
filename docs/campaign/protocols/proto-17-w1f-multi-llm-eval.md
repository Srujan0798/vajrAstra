---
name: proto-17-w1f-multi-llm-eval
description: "Step 1F (lead) — the lead's A3 multi-LLM evaluation: compose a one-page plan summary, get independent critiques from OpenCode (via MCP), a fresh hostile Sonnet reviewer, and ChatGPT (boss pastes a prepared prompt), then accept/reject each critique by reasoning, not by source"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:14:01.674Z
---

# STEP 1F — MULTI-LLM EVALUATION → `docs/campaign/MULTI_LLM_EVAL.md` + `docs/campaign/CHATGPT_EVAL_PROMPT.md`

**Why:** the lead: "cross-checking with Claude and one time ChatGPT… use multiple LLMs as an evaluator, and then I'll fix, like, if it is making sense… by the process
mentioned, not by the AI mentioned." Planned as "W4" in `docs/PLAN.md:23`; never executed. It is one of the two things the lead asked for that do not exist.
**Needs:** 1B, 1D and the 1E result (survivors or "none") done; 1A's K4 analysis (Option A vs D).

## 1. Compose the one-pager (lead) — `docs/campaign/checkpoints/W1_reports/1F_onepager.md`, ≤700 words
Sections: goal (beat Sarvam Vision 2.1 honestly on Indic OCR; 22 languages) · current state with n (from 1B: scored n per language, best local engine, Sarvam paired
result at n=3/lang) · baseline architecture (the lead's PPT, 4 stages, from `docs/architecture/PPT_SPEC.md`) · proposed hybrid integration (Option A and Option D side by side,
from 1A K4) · edge thesis survivors (1E) · known risks (South scored n tiny, low-n languages, barred GT, no Santali engine, normalisation comparability from 1B) ·
the 5 questions we most want critiqued. Every number carries its n. No adjectives without numbers.

## 2. Evaluator 1 — OpenCode (via MCP)
1. ToolSearch `select:mcp__opencode__opencode_setup,mcp__opencode__opencode_provider_list,mcp__opencode__opencode_provider_models,mcp__opencode__opencode_ask`.
2. `opencode_setup`, then `opencode_provider_list` → pick a **non-Anthropic** model if one is configured (e.g. an OpenAI/Google/open model); record provider + model id.
   If only Anthropic models exist, use one and record "same model family as Claude — reduced independence".
3. `opencode_ask` with the evaluator prompt below + the one-pager text inline (do not rely on it reading repo files). Save the full answer to `W1_reports/1F_opencode.md`.

## 3. Evaluator 2 — fresh hostile Sonnet reviewer (subagent)
Shared context block + evaluator prompt + the one-pager + permission to open these evidence files only: `docs/campaign/BENCHMARK_22.md`, `docs/campaign/COMPETITOR_INTEL.md`,
`docs/campaign/EDGE_THESIS.md`, `docs/architecture/PPT_SPEC.md`. It must not see the lead's reasoning or 1A. Save to `W1_reports/1F_sonnet.md`.

## 4. Evaluator 3 — ChatGPT (the boss pastes)
Write `docs/campaign/CHATGPT_EVAL_PROMPT.md` = the evaluator prompt + the one-pager, fully self-contained, with a first line "Paste everything below into ChatGPT
(latest model) and paste its full answer back to Claude." In the wave report, ask the boss to paste and return the answer. When it returns, save to `W1_reports/1F_chatgpt.md`.
If it has not returned by the time 1H must be written, mark the ChatGPT leg "PENDING BOSS" — do not invent it.

## Evaluator prompt (identical for all three)
> You are an independent senior reviewer of an Indic OCR plan for a hackathon. The team's goal is to beat Sarvam Vision 2.1 on Indic OCR across 22 Indian languages
> using hybrid integration of existing open models (no new backbone), in about 5 development days, on one Apple M2 Max, with no paid API budget left.
> Read the plan below. Then: (1) list the 5 most serious weaknesses — technical, evaluation, or strategic — each with the concrete failure it would cause;
> (2) for each proposed method, say whether it is likely to work for Indic scripts specifically (conjuncts, matras, Nastaliq, Ol Chiki, Meetei Mayek) and why;
> (3) name any published 2025–2026 technique or open resource you believe the plan is missing (title + where it appeared; say "uncertain" if you are not sure it exists);
> (4) check the evaluation: are any comparisons unfair or statistically unsupported?; (5) rank Option A vs Option D and explain; (6) the single change that most
> increases the chance of beating Sarvam honestly. Be specific and blunt. Do not praise.

## 5. Disposition — `docs/campaign/MULTI_LLM_EVAL.md`
Header: evaluators (tool, model id, date), independence caveats. Then one table: `# · critique (≤30 words) · raised by (1/2/3) · verification (what we checked, file/URL) ·
ACCEPT / REJECT / NEEDS-DATA · reason · action (which deliverable changes)`. Rule from the lead: **accept by the reasoning, not by the source** — a critique raised by all
three is not automatically right; a critique from one is not automatically wrong. Any "missing technique" an evaluator names must be checked live before it is accepted
(LLMs invent paper titles) — mark INVENTED if it does not exist. End with "What changed in the plan because of this evaluation" (bullets). ≤1,200 words.

## Checks
Verdict cross-check ([[proto-91-verdict-cross-check]]): every ACCEPT has a verification; every accepted missing technique has an opened URL.

Related: [[proto-10-w1-overview]], [[proto-19-w1h-draft-research-plan]], [[proto-13-w1c-mentor-playbook]]
