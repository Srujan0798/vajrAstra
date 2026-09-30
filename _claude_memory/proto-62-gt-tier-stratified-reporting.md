---
name: proto-62-gt-tier-stratified-reporting
description: "Added 2026-09-30 — every engine comparison must be split by GT tier; monitor measured that local engines lead Sarvam only on PDF-text-layer GT (0.229 vs 0.311, n=36) while Sarvam leads on human gold pairs (0.064 vs 0.243, n=9) and bench items (0.278 vs 0.617, n=9)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:14.115Z
---

# PROTO-62 — GT-TIER-STRATIFIED REPORTING (rule for every agent + one Engine task)

**Monitor measurement (2026-09-30, `sheet.csv` × `manifest.json` `gt_source`, the 54 Sarvam-paired items):**
| GT tier | n | Sarvam mean CER | surya | best local (per item) |
|---|---|---|---|---|
| official_pair_txt — human gold (bn/hi/sa) | 9 | **0.064** | 0.535 | 0.243 |
| official_pdf_layer — PDF text layer | 36 | 0.311 | 0.229 | **0.229** |
| sarvam_bench — human-reviewed twice (per 1D) | 9 | **0.278** | 0.730 | 0.617 |

**Meaning:** the "our best local engine is ahead of Sarvam in 10/18 languages" signal comes entirely from PDF-text-layer GT. PDF text layers can encode reading order,
hyphenation, headers and legacy-font artefacts that line up with Tesseract-style output and penalise a VLM that reads the page naturally. On both human-verified tiers
Sarvam is 2–4× better. Hypothesis to test, not conclusion: PDF-layer GT favours layout-literal engines.

## Rule (all agents, all deliverables, effective now)
1. Never report an engine-vs-engine or us-vs-Sarvam comparison pooled across GT tiers. Show per tier with n.
2. The honest one-liner for Vinay: "On the 18 human-verified items where Sarvam ran, Sarvam's CER is 2–4× lower than our best local engine; our engines only lead on
   PDF-text-layer ground truth (n=36), which may favour layout-literal output. n is small (3 per language)."
3. Any "winner" claim at n≥50 (D4) must state its tier mix; winners decided mostly on PDF-layer GT are labelled "PDF-layer GT".

## Engine subagent — TASK (paste after the shared context block)
> Using `sheet.csv` (and `level2/unified/sheet_v2.csv` if [[proto-61-sheet-provenance-forensics]] produced it — report both):
> 1. Reproduce the table above. 2. For all 1,227 items: per language × tier × model mean CER and n; per-language winner per tier. 3. PDF-layer GT bias test:
> for 30 PDF-layer items where surya beats Sarvam by > 0.2 CER, show GT snippet vs both predictions (first 200 chars each) and classify the cause
> (reading order / hyphenation / header-footer / legacy font / true Sarvam error). 4. Write `docs/campaign/GT_TIER_ANALYSIS.md` with the tables, the 30-item
> classification counts, and the corrected one-liner. Writes only that file.

## Verdict check
Re-derive the 3-row table; confirm the 30 examples are quoted exactly; confirm the one-liner matches the data. Then Miss propagates the one-liner into
`DRAFT_RESEARCH_PLAN.md` §3 and the root packet (fix-spec, not free editing).

Related: [[proto-61-sheet-provenance-forensics]], [[proto-19-w1h-draft-research-plan]], [[proto-64-meeting-day-finish]]
