---
name: proto-50-w5-repo-map-and-drift
description: "Wave 5 part 1 (Miss + Verdict, after the meeting) — FINAL_REPO_MAP.md with a link/path checker and a reason per file (CO-067), the weekday/date-drift fix across all docs after U1, and errata for AGENTS.md and the locked AGENT_PROTOCOL.md"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:16:45.940Z
---

# WAVE 5 · PART 1 — REPO MAP, LINK PROOF, DRIFT FIXES → `docs/campaign/FINAL_REPO_MAP.md` (D07)

**Closes:** CO-002/004/006–019/066/067/070 remainder (the 24h cleanup ran; what is missing is link proof and a reason per file).
**Precursors:** `HIERARCHY_MAP.md`, `FILE_INVENTORY.md` (root, 353 lines, 186 verdict mentions), `AUDIT_REPORT.md` (directory-level — not per-file), `docs/INDEX.md`, `DEEP_REPORT.md`.

## Part A — link and path checker (Engine subagent) → `level2/unified/check_links.py` + report
> Write a stdlib python checker over every `*.md` outside `_archive/`, `.venv*`, `Datasets/`, `graphify-out/cache/`: extract markdown links `[..](path)` and backticked
> repo paths (`` `docs/…md` ``, `` `level2/…` ``); resolve relative to the file and to repo root; report BROKEN (target missing), OUTSIDE (points outside repo),
> and ORPHAN md files (no inbound reference from any md). Print counts + first 50 of each. Read-only.

## Part B — reason per file (Miss subagent)
> For every file at repo root and every md under `docs/` (not `_archive/`): one row `path | purpose (one line, from its first lines) | owner (Engine/Verdict/Miss/boss) |
> status KEEP / MERGE→target / ARCHIVE | inbound refs count (from Part A)`. Use `FILE_INVENTORY.md` verdicts where present; fill the rest. Known duplicates to rule on:
> `W5_BEAT_SARVAM_PLAN.md` ×3 (root, `docs/architecture/`, `docs/research/level7/` — an earlier verdict says KEEP-BOTH for architecture vs level7, `CLEAN_DOCS_MD.md:153`;
> the root copy is new — diff all three); `LIVE_LATEST_2026-09-29.md` ×2 (root, `docs/research/`); `W5_STRATEGY_OPTIONS.md` ×2. Verdicts only — Miss executes MERGE/ARCHIVE
> after Verdict approval and after archiving (never raw delete).

## Part C — date-drift fix (only after the boss answers U1)
1. Find: `grep -rn --include='*.md' -E 'Wed(nesday)? 2026-10-01|Tue(sday)? 2026-09-30|Sat(urday)? 2026-10-04|Oct 4 \(Sat\)|Oct-1 freeze' . | grep -v _archive`.
2. Build the replacement table from U1/U2 answers (correct weekday + correct date; for unknowns "TBC"). Do not touch append-only historical log lines in
   `OCR_AGENT_MEMORY_FEED.md` §11 — instead append one erratum line listing the correction.
3. Miss applies per file with exact-string edits; Verdict re-runs the grep → must return 0 lines outside errata.

## Part D — errata for locked/law files
- `AGENTS.md`: fix "probe22 … 18 langs × 100/lang lock" to "1,283 manifest / 1,227 scored; 10 of 18 at 100 scored" (numbers from W2), and "11 engines" → "11 engines, 10 independent".
- `level2/probe22/AGENT_PROTOCOL.md` is CANNOT-apply: append an erratum to `OCR_AGENT_MEMORY_FEED.md` §11: "AGENT_PROTOCOL gates n_total==1227; manifest is 1,283 since 2026-09-29 02:45 (+56 additions); scoring still on 1,227 pending U5".
- `SAMPLE_PLAN_18_LANGS.md`: pointer to `docs/campaign/SAMPLING_PLAN.md` (if W2 did not add it).
- `docs/INDEX.md`: add `docs/campaign/` deliverables.

## `FINAL_REPO_MAP.md` layout
1. Summary: counts (files by area, broken links before/after, orphans, merges done). 2. The hierarchy as a tree (depth 2) with one line per folder purpose.
3. Root and `docs/` per-file table (Part B). 4. Link report after fixes. 5. Sealed/locked list. 6. How to navigate (reading order for a newcomer, ≤10 lines).

## Verdict check
Re-run the link checker after fixes (broken count must drop to 0 or each remaining one justified); sample 10 per-file reasons.

Related: [[proto-92-boss-decisions]], [[proto-51-w5-architecture-freeze]]
