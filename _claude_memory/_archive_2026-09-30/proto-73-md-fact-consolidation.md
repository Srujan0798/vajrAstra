---
name: proto-73-md-fact-consolidation
description: "Added 2026-09-30 — uni T2.4 \"no two md files state different facts about the same thing\": scan every live md for conflicting statements of the same fact (counts, engine numbers, dates, CERs, statuses), pick one authoritative md per topic, fix or pointer the rest; covers CO-012/013/070"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:53:45.986Z
---

# PROTO-73 — MD FACT CONSOLIDATION (Verdict finds conflicts, Miss applies fixes)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Boss:** uni T2.4 "every topic gets exactly ONE authoritative md … After merging, verify: no two md files state different facts about the same thing … at EVERY level of the project."
CO-012 (clean all hybrid-concern md), CO-013 (merge duplicate md), CO-070 (md cleanup level by level). Today the same facts are stated differently across ~300 live md files.

## Fact families to scan (starting list — extend as found)
| Fact | Known variants on disk (2026-09-30) | Truth source |
|---|---|---|
| probe size | 1,227 · 1,283 · "1,800" · "18 × 100 lock" · 12,324 "packs" | proto-93 F1–F3 (1,283 manifest / 1,227 scored / 12,324 sheet rows) |
| independent engines | 11 · 10 · 9 | 1A audit (openbharatocr ≈ tesseract_indic 1,225/1,227; tesseract_bilingual differs 857/1,227) |
| Sarvam numbers | 87.39 (word accuracy, macro-22, n=6,609) vs our CER; "0.2400 n=54" | COMPETITOR_INTEL §0.2; 1A |
| kok gap | 0.32 / 32pt / 19.4pt / 0.194 | 1A K7 |
| dates | "Wed 2026-10-01", "Tue 2026-09-30", "Oct 4 (Sat)", qualifier 30/09 vs 10-15 | U1/U2 answers |
| W6 path / backbone | Option A vs D; Qwen2.5-VL-3B vs GLM-OCR 0.9B | U4 answer |
| South scored n | "100/lang", "400 pages", 126/400 | CER_BY_SCRIPT.md |
| graph size | 1,324 / 3,990 nodes | graphify-out current |
| status words | "COMPLETE", "DONE", "READY", "LOCKED", "FINAL" on unfinished work | proto-66 register |
| md count | 211 / 240 / 303 / 309 / 379 | recount |

## Skills (load first)
`ssotize` (find the canonical source and plan the merge) · ECC `living-docs-governance` · `graphify` duplicate-label/community queries · `factchk` on every fact family's truth source.

## Verdict subagent — TASK (paste after the shared context block)
> 1. List live md files (exclude `_archive/`, `.venv*`, `Datasets/`, `graphify-out/cache/`). For each fact family above, grep all files for its patterns (write the regex list in the report)
>    and build a table: fact · file:line · stated value · matches truth? (MEASURED against the truth source) · live or historical (append-only log lines are historical — never rewrite them;
>    note them as HISTORICAL).
> 2. Find topics with more than one "authoritative" md (e.g. two meeting packets, three W5 plans, two sampling plans, two leaderboards, several INDEX/MAP docs:
>    `docs/INDEX.md`, `HIERARCHY_MAP.md`, `level2/FOLDER_MAP.md`, `level2/UNIFIED_INDEX.md`, `FULL TECHNICAL BRIEFING.md`, `README.md`, `SOUTH_CANON.md`). Propose ONE authority per topic
>    and what each other file becomes (merge / pointer / historical banner).
> 3. Output `docs/campaign/audit/MD_FACT_CONFLICTS.md`: per family the conflict table + the exact fix-specs (old → new) for live statements; per topic the authority decision.
> Use graphify (`graphify-out/GRAPH_REPORT.md` communities; `graph.json` nodes with the same label in several files) to find topic clusters faster.

## Miss applies (after Verdict review)
Fix-specs per [[proto-18-w1g-apply-verify]] method (pre-images, exact strings, re-verify). Historical log lines get no edits — instead a single dated erratum line where the log allows appends.
Topic losers get a pointer or a banner `> SUPERSEDED by <path> on <date> — kept for history.` Then re-run the scan: every live conflict count must be 0.

Related: [[proto-72-per-file-audit]], [[proto-63-single-canonical-files]], [[proto-66-concern-register-rebuild]]
