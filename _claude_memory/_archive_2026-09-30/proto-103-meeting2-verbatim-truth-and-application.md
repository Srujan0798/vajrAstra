---
name: proto-103-meeting2-verbatim-truth-and-application
description: "Added 2026-09-30 ~17:15 IST (boss: 'check meeting 2 details, sort this relevantly and apply… to not mislead') — the Sep 29 meeting re-read from the RAW transcript: every statement attributed to its speaker (Lead Vinay = L1–L14, the boss Srujan = S1–S5, unattributed = U1) with verbatim quotes; 10 misleading items in our docs and memory (D6 'hybrid/no novel backbone' and D7 'AI-only team' were the BOSS's words, not the lead's; H44–48 timing and red lines invented or mixed); how each lead request is applied (plan, gate, status, owner)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T11:35:51.963Z
---

# PROTO-103 — MEETING 2 (2026-09-29): VERBATIM TRUTH TABLE, CORRECTIONS, APPLICATION

**Why:** the boss: "check this, meeting 2 details, sort this relevantly and apply… to not mislead". Our derived docs put words in Vinay's mouth. Presenting him with "as you said…" when he did not say it costs the trust the D5 session depends on.

**Source of truth:** the RAW block of `docs/research/MEETING_2026-09-29_STRUCTURED.md` (lines 3–10). The boss pasted the same text into chat on 2026-09-30.
- The transcript has **no speaker labels**. Attribution below comes from content and turn-taking.
- Items that stay ambiguous are marked **U** (unattributed).
- Everything outside the RAW block — the D1–D7 / A1–A7 tables, timeline and red lines — is **DERIVED** by an agent and is not evidence.

## 1. What was said — verbatim, by speaker
**Lead (Vinay Gahlot):**
| ID | Verbatim (shortened with …, never reworded) | Meaning |
|---|---|---|
| L1 | "whatever process I would be doing, I'll just walk you through the process. You need to do that, and then based on it… we can, like, discuss those things and then start executing" | his method: research → discuss → execute |
| L2 | "This Consensus dot app… ten searches free daily. So in two, three searches, you'll get all the gist… this is how we presented our strategy also" | use Consensus.app (2–3 searches) |
| L3 | "first you need to determine, like, how to train an OCR problem… flowchart, like what's the process, how to start, what to do then" | an OCR-training flowchart first |
| L4 | "check what are the recent advancements… any new breakthroughs… any research group or any company find something really interesting?" | scan recent advances |
| L5 | "these steps we designed, and we felt that it was good enough… I'm asking you to do this again… a month, one and a half month back… Every week new techniques are coming up… compare that methodology you come up with what we have already built" | redo the research; diff it against his recipe |
| L6 | "I'll ask open code… cross-checking with Claude and one time ChatGPT… use multiple LLMs as an evaluator… By the process mentioned, not by the AI mentioned… from the process, that also we should be also convinced" | multi-LLM evaluation, judged by the reasoning |
| L7 | "No, no, benchmarking for the existing ones… At least one for each language, all the 22 languages… five or ten samples, that's enough" | benchmark existing engines on all 22, 5–10 each |
| L8 | "give it to… multiple LLMs. And maybe the research papers of the lab who created good OCR… these are the current state, and I want to reach at this state. What's the best way forward? And then we'll perform the training accordingly" | current state + target + papers → LLMs → then train |
| L9 | "I'll join after next Wednesday… I'll ask Krishna to support you. I'll ask Aryan also… how many people do you feel like you need more… we'll add more people" | availability; offers people |
| L10 | "before, like jumping into training the OCR… very good recipe was developed. Because of that recipe only we got selected into the top five… if you got something better, we will go for that… not what we have already decided… spend one hour on the research part only" | his recipe stands unless something better is shown; 1 hour of research |
| L11 | "I think I have already prepared that architecture. This PPT I have shared with you… it's full architecture" | the PPT = the full architecture |
| L12 | "not directly add, we will have one session… a 15-20 minute session… You present the plan, we can cross question each other, brainstorm… and then we execute the plan" | a cross-question session before execution |
| L13 | "you have done for South Indian languages only, no? So just cover the other languages also before giving your final" | cover all languages first |
| L14 | "you first do some, like, this initial draft research plan. I'll discuss it with you, and then we will finalize" | deliverable = a DRAFT research plan |

**The boss (Srujan):**
| ID | Verbatim | Meaning |
|---|---|---|
| S1 | "I have just got the results… how can we do benchmark? We should start the OCR model training, no?" | wanted to start training (then accepted L7) |
| S2 | "actually there is no need of people, just AI itself is enough. But we need the correct methods and correct architecture and correct person who can understand what is actually going on… For doing work I have AI" | AI-first team. **This is the boss's line, not the lead's** |
| S3 | "we have already got some benchmarks of other AIs. I have brought it from For South. Now we need to really develop the OCR model" | South benchmarks exist; wants to build |
| S4 | "we should plan some best architecture or new architecture, which will outcome or overlead the current existing architectures" | aim: beat existing architectures |
| S5 | "instead of directly doing the OCR model… research on existing models and what are the best hybrid way of integrations we can make… then we will add it to the current your plan" → lead: "Yes." | hybrid integration of existing models — **the boss's proposal, accepted by the lead** |

**Unattributed:**
| ID | Verbatim | Meaning |
|---|---|---|
| U1 | "If you send this data to OpenCode or any other AI tool to examine… that tool will have a greater picture… identify pinpoint things. Like for this language, this type of training, or this type of recognition is missing" | give the evaluators the data, not just conclusions |

**Not in the transcript at all:**
- "no novel backbone";
- "H44–H48";
- "~04:23 IST";
- an engine list;
- "Sarvam cap";
- a "deck";
- "decisions locked".

## 2. Misleading items to correct (owner: Agent 2's docs subagent; per-file pre-image per rule 17)
| # | Where | Wrong | Correct |
|---|---|---|---|
| M1 | `MEETING_2026-09-29_STRUCTURED.md` D6 | "Hybrid integration… not novel backbone", attributed to the Lead | S5 (the boss's approach), accepted by the lead ("Yes"). "No novel backbone" is campaign law (AGENTS.md), not the meeting |
| M2 | same, D7 | "No new hires… AI itself is enough", attributed to the Lead | S2 (the boss). The lead OFFERED more people (L9) |
| M3 | same: Participants + Timeline | "joins call at H44–48", "Review session H44–H48 (~04:23 IST Tue Sep 29)", "Campaign end ~04:23" | Not said. The lead said "I'll join after next Wednesday" (L9); which Wednesday = U1 (open) |
| M4 | same, A4 | "Prepare review deck: 15–20 min presentation" | L14 + L12: an **initial DRAFT research plan** to discuss and cross-question; not a deck or a decision menu (MENTOR_PLAYBOOK §5.1 already flagged the inversion) |
| M5 | same, A5 | engine list + "Sarvam cap = hard limit" | L7 names no engines. The list is DERIVED; the cap is campaign law |
| M6 | same: "Red Lines (From Lead / Campaign Law)" | sources mixed | Split them. **Lead:** don't jump into training before the research (L10); one session before execution (L12). **Campaign law:** the rest |
| M7 | same: "Decisions Locked (Do Not Re-Litigate)" | nothing was formally locked | Re-title "Agreed in the meeting (verbatim IDs L/S)" |
| M8 | `docs/campaign/MENTOR_PLAYBOOK.md` §1 (h), (j), §4.1, §4.8 | "hybrid of existing, no new one" and "AI-only team" listed as the lead's constraints | Re-attribute to S5 / S2; keep L-items only in "his method" and "his constraints" |
| M9 | memory proto-89, proto-99 §I (S29 rows) | "the lead's 'hybrid integration'", "j AI-only team" as the lead's method | planner fixes now (Part 4) |
| M10 | `VINAY_MEETING_PACKET.md`, `DRAFT_RESEARCH_PLAN.md`, BOSS_CONCERNS, `docs/PLAN.md` when written | any "as you said" built on M1–M7 | grep for "novel backbone", "AI itself", "H44", "hybrid", "Decisions Locked" and fix the attribution; each quote shown to Vinay must be an L-row |

## 3. How each lead request is applied (the plan must satisfy L1–L14)
| Lead item | Applied as | Status | Owner |
|---|---|---|---|
| L1 + L14 draft plan → discuss → finalize → execute | `docs/PLAN.md` (proto-98 T1) is the DRAFT research plan; it is final only after the L12 session | OPEN | Miss writer, Verdict check |
| L2 Consensus.app | Used at full strength (boss 2026-09-30): the 3 combined queries in proto-97 RQ-12; results → RESEARCH_DECISIONS via Agent 2 | OPEN | boss (U36-1) + Agent 2 |
| L3 training flowchart | Plan v3 flowchart heads `docs/PLAN.md` (proto-100 B-16) | OPEN | Miss |
| L4 recent advances | R1–R7, LIVE_LATEST, DEEPER_LIVE_RESEARCH → RESEARCH_DECISIONS | DONE (harvest ongoing, proto-95) | Verdict |
| L5 + L10 compare with his recipe; switch only if better | `docs/PLAN.md` carries a per-stage table: **PPT recipe stage → Plan v3 choice → why better (measured evidence)** (proto-75). The Bodhan-base switch is justified only by Day-1 numbers (Gate 1) | OPEN (needs Day 1) | Verdict + Engine |
| L6 + L8 + U1 multi-LLM evaluation by the process, with data | Gate 2.5 (proto-89, B-17). The input package = BENCHMARK_22 per-language tables (current state) + Sarvam/Bodhan numbers (target) + RESEARCH_DECISIONS + key papers + the draft plan. Each evaluator critique is accepted or rejected by its reasoning, one line each | OPEN | Verdict |
| L7 + L13 benchmark existing engines, all 22 languages | BENCHMARK_22 (18 + South 4). South v1 is 126/400 scorable; proto-101 re-runs South to the same standard. Per language n ≥ 5 is met everywhere | DONE / improving | Engine |
| L9 availability + people | DECIDED: "next Wednesday" = today (Wed 2026-09-30); the boss reaches him any time on WhatsApp (U1). Krishna/Aryan not needed — AI agents suffice (the boss's S2) | CLOSED | — |
| L11 PPT = full architecture | `docs/architecture/PPT_SPEC.md` + PPT dump (→ `docs/sources/proposal/`) | DONE | — |
| L12 15–20 min cross-question session before execution | After Gate 2.5, before any Day-3 training | OPEN | boss (U36-5) |

The boss's own positions (S2, S4, S5) stay as the campaign's approach, attributed to him: AI-first team; beat existing architectures through hybrid integration of existing models. Plan v3 builds on the strongest open model and sharpens it where it trails.

## 4. Planner corrections applied in memory with this file
- **proto-89:** "this IS the lead's 'hybrid integration of existing models'" → "this is the boss's hybrid-integration approach (S5), which the lead accepted".
- **proto-99 §I:** the S29 rows now cite L/S IDs.
  - Step "h hybrid" and "j AI-only team" are the boss's (S5, S2), not the lead's method.
  - D6/D7 re-attributed.

**Done when:**
- `grep -rn "novel backbone\|AI itself is enough\|H44\|Decisions Locked" docs/research/MEETING_2026-09-29_STRUCTURED.md docs/campaign/MENTOR_PLAYBOOK.md VINAY_MEETING_PACKET.md` shows only correctly attributed lines;
- every Vinay-facing quote is an L-row.

Related: [[proto-13-w1c-mentor-playbook]], [[proto-75-vinay-plan-baseline]], [[proto-89-plan-v3-bodhan-base]], [[proto-100-research-to-build]], [[proto-98-clean-repo-master]], [[proto-92-boss-decisions]], [[proto-99-concern-crosswalk]]
