---
name: proto-61-sheet-provenance-forensics
description: "Added 2026-09-30 — BLOCKER: sheet.csv (every leaderboard number) has no generator on disk, is not in git, and its CER column cannot be re-derived from its own gt/prediction columns (334/400 mismatch); forensic trace + reproducible rebuild as sheet_v2 without touching the locked file"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:09.243Z
---

# PROTO-61 — SHEET.CSV PROVENANCE FORENSICS (Engine builds, Verdict verifies) — BLOCKER

**Facts (monitor + EDGE_THESIS §4, 2026-09-30):**
- `level2/probe22/sheet.csv` (12,324 rows; mtime 2026-09-28 21:54) — **no script on disk or in `_archive/` writes it**; not in git.
- Seeded 400-row sample (`random.seed(20260926)`): `level2/probe22/metrics.py` `calculate_cer(gt, prediction)` matches stored `CER` in 66/400 (1e-9), 100/400 (5e-4);
  no normaliser variant (NFC, NFKC, raw edit distance, `calculate_cer_uncapped`) closes it; implied ref length median 1.336× stored GT; spread over all 11 models.
- Headline numbers are internally consistent because all are computed FROM the stored column. The question is whether the column measures what we say it measures.
- A second scorer exists at `src/utils/metrics.py` (untracked `src/` tree). Do not use it as truth.

**Law:** `sheet.csv` is LOCKED — never edit, never overwrite. Build `level2/unified/sheet_v2.csv` beside it. Nothing downstream switches to v2 without the boss's yes (U9).

## Engine subagent — TASK (paste after the shared context block)
> 1. **Trace provenance (read-only).** Search for any writer: `grep -rn "sheet" level2/probe22/*.py level2/*.py scripts/ 2>/dev/null`, the same in `_archive/`, and in
>    `OCR_AGENT_MEMORY_FEED.md` / `docs/research/level7/*.md` / `DISPATCH_LOG.md` for "sheet.csv" (who built it, when, with what). Check `level2/probe22/scores/` for per-item
>    metric files (`metrics_*_normalized.json`, `ablation_delta_*`) and whether their per-item CER equals `sheet.csv`'s. Report the most likely generator, with evidence.
> 2. **Find what the stored CER was computed against.** For 40 mismatching rows, open the pack JSON `level2/probe22/out/<model>/<lang>/<image_id>.json`; compute CER of
>    (a) `regions[].text` joined, (b) `regions[].text_nfc` joined, (c) with/without newline flattening, against (i) sheet `gt`, (ii) manifest `gt`. Which combination reproduces
>    the stored value? Also check whether sheet `gt` == manifest `gt` byte-for-byte for all 1,227 items (count mismatches).
> 3. **Rebuild reproducibly.** Write `level2/unified/build_sheet_v2.py` (stdlib + `level2/probe22/metrics.py` only): for every (item in the 1,227 scored set, local model),
>    GT from `manifest.json`, prediction from the pack JSON using ONE documented text field and ONE documented normalisation (the scorer's own), output
>    `level2/unified/sheet_v2.csv` with the same columns + `pred_source_field`, `scorer_version`. Sarvam rows: same method from its packs.
> 4. **Compare v1 vs v2:** per model × language mean CER in both; the per-language winner in both; the Sarvam paired result in both (by GT tier, see [[proto-62-gt-tier-stratified-reporting]]);
>    list every headline claim whose conclusion changes. Write `docs/campaign/SHEET_PROVENANCE.md`: provenance finding, the reproducing combination (or "none found"),
>    v1-vs-v2 table, changed conclusions, recommendation.
> Writes only: `level2/unified/build_sheet_v2.py`, `level2/unified/sheet_v2.csv`, `docs/campaign/SHEET_PROVENANCE.md`.

## Verdict check
Re-run `build_sheet_v2.py`, confirm deterministic (same sha256 twice); hand-compute 5 rows; confirm `sheet.csv` sha256 unchanged before/after.

## Meeting-day rule (until this step is DONE)
Any number shown to Vinay from `sheet.csv` carries the note: "CER as stored by the probe scoring pass; independent re-derivation is in progress". If proto-61 finishes before
the meeting and conclusions change, the draft plan uses v2 and says so.

Related: [[proto-62-gt-tier-stratified-reporting]], [[proto-92-boss-decisions]], [[proto-93-measured-facts]]
