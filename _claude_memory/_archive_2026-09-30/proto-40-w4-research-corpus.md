---
name: proto-40-w4-research-corpus
description: "SUPERSEDED 2026-09-30 by proto-95 (harvest) + proto-97 (new research); keep only the S1–S12 tag list — was: Wave 4 (Miss + Verdict) — build RESEARCH_CORPUS.md as an index of the research already on disk mapped to threads S1–S12, with top-5 per thread and a \"what WE build\" line, filling gaps live only where a thread is thin; no paper quota (C3)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:16:27.097Z
---

# WAVE 4 — RESEARCH CORPUS INDEX → `docs/campaign/RESEARCH_CORPUS.md` (D08)

> **SUPERSEDED 2026-09-30** by [[proto-95-research-harvest-decisions]] (every research file → decisions → one fate) and [[proto-97-research-still-to-do]] (new research only where it changes a decision). Do not build `RESEARCH_CORPUS.md`. Keep the S1–S12 thread list below only as the tag vocabulary.

**Rule C3:** no paper quota. A corpus claiming 1,000–5,000 papers would be the fake claim CO-086 forbids. Every entry: real URL/title/date + "what WE build from this".
**This is an index of what exists, not new research**, except targeted gap-filling.

## Where the research lives (planner-verified 2026-09-29)
- `docs/research/level7/` — Level-7 campaign (2026-09-27/28): lane folders `a/` (1 LEDGER.md), `b/` (no LEDGER.md — discover its record files), `c/` (c1–c4 LEDGER.md);
  plus CALL_PACKET, H48_HOSTILE_PASS, FINAL_VERDICT_2026-09-27, SANTA_METHOD_FINAL, KILL_CRITERIA, W6_QLORA_SPEC. Claimed ~1,300+ records — count them yourself.
- `docs/research/`: R1_SOTA_MECHANISM_TEARDOWN, R6_COMPETITION_INTEL, other R*/W* files, `LIVE_LATEST_2026-09-29.md` (copy also at root), `DEEPER_LIVE_RESEARCH_2026-09-29.md`,
  `LEVEL7_RESEARCH_CAMPAIGN.md` (law). Root: `LEVEL7_RESEARCH_FINDINGS.md`. Wave 1 outputs: `COMPETITOR_INTEL.md`, `EDGE_THESIS.md`, hunt report.
- Knowledge graph: `graphify-out/GRAPH_REPORT.md` (communities help locate clusters).

## Threads
S1 agentic / multi-agent SOTA · S2 self-improving agents · S3 OCR classical → VLM · S4 Indic OCR & document AI · S5 RVL / document intelligence · S6 NVIDIA ecosystem ·
S7 Jais-class Indic LLMs · S8 layout analysis · S9 knowledge graphs / persistent agent memory · S10 long-horizon agentic systems · S11 LAYA & JEV integration patterns ·
S12 Gnani-class Indic MoE.

## TASK block — subagent A (Miss, indexer)
> 1. Find every research record file: `find docs/research -name '*.md' | xargs grep -l -E 'https?://' | head -200`; for each LEDGER, learn its record format from the first 60 lines.
> 2. Count records per file (by its record delimiter) and extract per record: title, URL, date, tag (PRIMARY/…), one-line claim. Write them to
>    `docs/campaign/checkpoints/W4_reports/records.jsonl` (one JSON per line) — this file is the machine index.
> 3. Assign each record to 1–2 threads by keyword rules you write down (e.g. S4: Indic|Devanagari|Bengali|Tamil|Nastaliq|Ol Chiki|Meetei|AI4Bharat|Sarvam|Bhashini…),
>    then hand-check 30 random assignments and report the error rate.
> 4. Per thread: record count; URL-less records count (they cannot be cited); duplicates (same URL); date range.
> Report counts and the rules. Under 1,000 words.

## TASK block — subagent B (Verdict, ranker), after A
> For each thread pick the top 5 records by decision relevance to THIS campaign (does it change a W5/W6 decision, a weak cell, the edge thesis?). For each: open the URL and confirm
> title/date/claim (mark DEAD links); write "what WE build from this" in one concrete line (component, languages, cost) or "nothing — context only".
> Flag threads with < 3 decision-relevant records as THIN.

## Gap filling (≤5 research subagents, only for THIN threads)
Use the hunt method of [[proto-15-w1e-edge-hunt]] restricted to the thread; 2025–2026; each new entry needs an opened URL and a "what WE build" line; stop at 5 good entries per thread.

## `RESEARCH_CORPUS.md` layout (lead composes, ≤2,500 words + tables)
1. Summary: real record counts (not claims), per-thread coverage, THIN threads and what was added. 2. Per thread S1–S12: count, top 5 with "what WE build", gaps.
3. Method (keyword rules, error rate, dedup). 4. Pointer to `records.jsonl`. Verdict cross-check on 10 random entries.

Related: [[proto-15-w1e-edge-hunt]], [[proto-91-verdict-cross-check]]
