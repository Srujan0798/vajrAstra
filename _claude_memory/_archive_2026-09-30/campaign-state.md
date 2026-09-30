---
name: campaign-state
description: "Verified disk state of the South OCR campaign as of 2026-09-29 ~20:45 IST — clock, what the lead actually asked for, meeting-packet defects, probe/sampling truth, other actors; read before re-running any directive task"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:19:09.344Z
---

**Snapshot 2026-09-29 ~20:45 IST, measured on disk by the Opus planner. Full detail with evidence: `docs/campaign/CAMPAIGN_DIRECTIVE.md` v5 Part A.** Numbers decay — re-verify in one command before acting.

**Clock.** Today Tue 2026-09-29. **Vinay meeting Wed 2026-09-30** (nearest gate). 2026-10-01 is a **Thursday** — 43+ docs wrongly say "Wed 2026-10-01"; source is the lead's ambiguous "I'll join after next Wednesday". Real submission deadline UNKNOWN (Oct 4 vs Oct 15 vs "qualifiers 30/09" conflict). Training has NOT started; W6 is PAUSED (feed §15).

**Who is who.** Vinay Gahlot = CEO of the boss's own team (Vaultstack AI); his 4-slide PPT = "Vinay's plan" = the architecture baseline. The meeting-transcript "Lead" is very likely Vinay (inferred). Team: Akshay Gahlot CTO, David Babu advisor, Aryan, Krishna, Srujan = the boss.

**What the lead asked for** (raw transcript): an *initial draft research plan* to cross-question in a 15–20 min session; hybrid integration of existing models (no novel backbone); benchmarks for **all 22 languages** at 5–10 samples; multi-LLM evaluation (OpenCode + Claude + ChatGPT). Status: data for 22 langs exists (min 19/lang) but **no single 22-lang table**; **multi-LLM evaluation never done**; no training flowchart doc.

**Meeting packet.** `VINAY_MEETING_PACKET.md` exists ("READY") but: "beats Sarvam 9/18" is unsupported (paired n=3/lang: surya mean lower in 10/18 langs, item-level Sarvam 28 vs surya 21, 5 ties); 1,227 vs 1,283 mixed; wrong weekdays; Option A (Miss) vs Option D (Verdict) conflict hidden; backbone Qwen2.5-VL-3B (§12.2) vs GLM-OCR 0.9B (packet).

**probe22.** manifest 1,283 = 1,227 + 56 additions (sd 25, mr 21, pa 10; 2026-09-29). `sheet.csv` 12,324 rows scores only the 1,227. Additions' engine outputs partial. `AGENT_PROTOCOL.md` still says 1,227 (CANNOT-apply file). 10 effective engines, not 11. Sarvam cap spent (57).

**South scored n is tiny.** 400 South pages are labelled (100/lang) but only 126 carry a CER (55 mojibake + 219 thin-GT nulled): Tamil 53, Telugu 6, Kannada 4, Malayalam 4 (+ Devanagari 16, Latin 43 by dominant script). kn/ml are below the lead's 5–10 floor at scored level.

**Sampling.** 22 langs / 1,683 manifest-level; target 2,200, deficit 517 (as 19, mni 20, sat 20, gu 24, doi 27, ne 37, brx 67, or 69) — caused by the honesty gates rejecting PDF text layers, so "varied pages from existing PDFs" cannot close it alone. Pair tier (bn/hi/sa) passes the variance test; PDF tier concentrated (kok and pa: 100 pages from 2 PDFs each; ur 34% page≤1).

**Other actors.** Two OpenCode agents write to the repo (DISPATCH_LOG "AGENT-1 integration pass" ~20:20). They created an untracked `src/` QLoRA/GRPO training tree 19:53–20:07 — conflicts with the W6 pause; boss decision U3.

**Already DONE:** 24h cleanup, `Untitled` ingested + deleted, no `old` folder, graph rebuilt (3,990 nodes), LAYA vs JEV researched (DEEPER_LIVE_RESEARCH §B6: JEV more accurate but closed/hosted; Laya open, local, fast; both routing heads, not OCR).

**Past-agent failure patterns** (why "done = reproduced by a command"): a dedup without hostile pass destroyed 447 items; 6/10 fix-specs hallucinated from stale text; 5/9 claimed winners false; BOSS_CONCERNS overclaimed a per-file audit.

**How to apply:** treat directive Part A as truth over any older doc; re-verify a number before building on it; never re-run the DONE list.

Related: [[sonnet-handoff]], [[open-front]], [[conflicts-register]], [[campaign-law]]
