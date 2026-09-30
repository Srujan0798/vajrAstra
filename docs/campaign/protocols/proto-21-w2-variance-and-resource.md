---
name: proto-21-w2-variance-and-resource
description: "Wave 2 part 2 (Engine + Verdict) — per-language variance evidence disproving or confirming first-page/one-paper/clustered shortcuts, candidate-pool measurement for the 8 short languages from candidates/<code>.json, re-source plan within the honesty gates, and the SAMPLING_PLAN.md layout"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:15:36.356Z
---

# WAVE 2 · PART 2 — VARIANCE, CANDIDATE POOLS, RE-SOURCE PLAN → `docs/campaign/SAMPLING_PLAN.md` (D04)

**Closes:** CO-022, CO-023, CO-024 (evidence per language, not assumption). **Never:** fabricate samples, lower the gates, collect 400-page sets, download.
**Writes only:** `level2/unified/variance_22.py`, `docs/campaign/SAMPLING_PLAN.md` (lead composes), reports in `docs/campaign/checkpoints/W2_reports/`.

## Facts to start from (planner-measured; re-verify)
- Gates in `level2/probe22/extract_gt.py:66-69`: `MIN_CHARS = 50`, `MIN_SCRIPT_RATIO = 0.5`, `MAX_LATIN_RATIO = 0.6`, `MAX_CTRL_CHARS = 3`. AGENT_PROTOCOL forbids relaxing them.
- `level2/probe22/candidates/<code>.json` keys: language, language_name, scripts, pdfs, pages_scanned, pages_with_text, candidates, rejected_mojibake_or_wrong_script,
  rejected_short_or_latin, pdf_errors, pdf_error_list, pairs, items, pair_items. Example gu: 220 PDFs, 13,406 pages scanned, 3,567 with text,
  **3,486 rejected as mojibake/wrong script**, 71 short/Latin, **10 clean candidates** (4 drawn). → Gujarati PDFs use legacy font encodings; more pages cannot fix it.
- Variance already measured from the manifest (distinct PDFs / distinct pages / page≤1 count): pair tier bn/hi/sa 100 distinct images spread across the pool
  (bn ids 32→3088, hi 18→3461, sa 22→506); kok 2 PDFs/100 pages; pa 2/100; mr 7; mai 8; ks 10 (15 on page≤1); sd 16; **ur 38 PDFs but 34 items on page≤1**;
  brx 7/48; or 2/51; ne 2/18; gu 2/5; doi 4/8; fill tier (as, mni, sat and parts of others) = sarvam_bench, single source.
- Short languages (manifest level): as 19 · mni 20 · sat 20 · gu 24 · doi 27 · ne 37 · brx 67 · or 69 → deficit 517 to 100 each.

## TASK block (paste after the shared context block)
> You are the Engine agent. Produce per-language sampling evidence and a re-source plan that stays inside the gates.
> 1. **Variance table (all 22 languages)** from `level2/unified/manifest_22.json` (or `manifest.json` + South labels): n · distinct source documents · top-1 document share ·
>    distinct pages · page-offset distribution (min / q25 / median / q75 / max of `source_page`) · share on page ≤1 · for pair tier: id spread (min/median/max of the numeric
>    id parsed from the symlink target: `os.readlink`) · for South: sources (`source` field e.g. S5_govt) distribution. Flag: top-1 share > 50% (clustered), page≤1 share > 20%
>    (first-page bias), single source (one-paper).
> 2. **Verdict per language on the three forbidden shortcuts** — first-page-only, one-paper-per-file, clustered/unrepresentative — each DISPROVEN / CONFIRMED / PARTIAL with the numbers.
> 3. **Candidate pools for the 8 short languages** from `candidates/<code>.json`: pdfs, pages_scanned, pages_with_text, rejected by reason, clean candidates, already drawn,
>    **clean candidates remaining**. Also check other official sources for each language under `Datasets/akshardrishti_official/<Language>/` (read-only listing: are there
>    image+transcription pairs not yet used? count them). Explain in one line per language WHY it is short (mojibake fonts, no text layer, no source at all).
> 4. **Re-source options per short language, within the gates only:** (a) remaining clean candidates → how many more can be drawn; (b) unused official image+transcription
>    pairs → how many; (c) nothing available → "accept low-n with permanent caveat". For concentrated languages (kok, pa, ur, ks) propose a stratified re-draw
>    (max share per document, page≤1 excluded) and how many items it would replace. **Proposals only — executing a re-draw changes the locked manifest (boss decision U5).**
> 5. Report with tables and a ≤10-line summary. Under 1,500 words.

## `docs/campaign/SAMPLING_PLAN.md` layout (lead composes)
1. Summary (≤10 lines): where we stand vs 100 × 22; which gaps are closable within the gates and by how much; which are structural (and why); what needs U5.
2. Reconciliation (from [[proto-20-w2-sampling-reconcile]]). 3. Variance table + shortcut verdicts. 4. Candidate pools. 5. Re-source plan per language (source, method, count, gate status).
6. Low-n caveats (exact wording for leaderboards: "n=19, fill-tier GT, no winner claim (D4)"). 7. What this plan does NOT do. 8. Decisions for the boss (U5).
Supersedes `SAMPLE_PLAN_18_LANGS.md` — add a one-line pointer at the top of that file (Miss), do not delete it.

## Verdict check
Recompute two languages' variance rows independently; confirm every "remaining candidates" number from the JSON; confirm no locked file changed.

Related: [[proto-20-w2-sampling-reconcile]], [[proto-92-boss-decisions]], [[proto-93-measured-facts]]
