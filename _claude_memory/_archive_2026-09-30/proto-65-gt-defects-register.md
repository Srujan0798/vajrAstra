---
name: proto-65-gt-defects-register
description: "Added 2026-09-30 — build docs/campaign/GT_DEFECTS.md, one register of every known ground-truth defect (Marathi Ol Chiki injection, gt_thin 179 vs 200, te script contradiction, ne R5, sarvam_bench now known human-reviewed, PDF-layer bias) with measured scope and the decision each needs"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:44:30.000Z
---

# PROTO-65 — GROUND-TRUTH DEFECTS REGISTER (Verdict builds; decisions go to the boss) → `docs/campaign/GT_DEFECTS.md`

**Why:** GT defects are scattered across 1A, 1B, EDGE_THESIS, gt_forensics.json, gt_verification.json and the feed. Every score is only as good as its GT; the boss needs
one list with scope and decisions. §6.4 stays LOCKED — this register proposes, the boss decides.

## Known entries to verify and measure (starting list)
| ID | Defect | Source | Scope to measure |
|---|---|---|---|
| G1 | Marathi PDF-layer GT with injected Ol Chiki code points; the 18 items are table pages (7.4× Latin, 7.9× digits) | EDGE_THESIS C4, lens reports | count items; CER with/without them per engine |
| G2 | `gt_thin` threshold: 179 chars (CER_BY_SCRIPT.md, docs) vs 200 (code, 3 places) | BENCHMARK_22 UNRESOLVED #2 | which value ran; how many South pages change basis |
| G3 | te_024 / te_065 dominant script: `pages_script_map.json` vs `pages_manifest.json` disagree | BENCHMARK_22 UNRESOLVED #3 | Telugu scored n = 6 or 4 |
| G4 | ne PDF-tier BARRED (R5: ctrl chars, trust 26.6) | gt_forensics.json | unchanged — confirm |
| G5 | `sarvam_bench` fill GT is human-reviewed twice (HF card) — contradicts protocol's "machine GT"; §6.4 BARRED mni/sat partly on an LLM-vision verifier that cannot read Ol Chiki/Meetei Mayek | COMPETITOR_INTEL §0.1; gt_verification.json | which §6.4 verdicts depend on the "machine GT" premise → U6 |
| G6 | PDF-text-layer GT may favour layout-literal engines | [[proto-62-gt-tier-stratified-reporting]] | result of the 30-item classification |
| G7 | `sheet.csv` gt column vs manifest gt byte equality | [[proto-61-sheet-provenance-forensics]] step 2 | mismatch count |
| G8 | South 274/400 pages without CER (219 thin GT, 55 mojibake) | CER_BY_SCRIPT.md | per language |
| G9 | Items whose GT came from the same source Sarvam built its bench on (sarvam_bench) — potential home-turf for Sarvam | manifest `gt_source` | count per language; exclude-or-flag rule for comparisons |

## Verdict subagent — TASK (paste after the shared context block)
> For each entry: reproduce the defect with a command, measure its scope (items, languages, engines affected, effect on mean CER with/without), classify
> SEVERITY (changes a winner / changes a number / cosmetic), and write the decision it needs (boss / Verdict / none). Add any new defect you find while measuring.
> Write only `docs/campaign/GT_DEFECTS.md`: summary (≤10 lines) → register table → per-entry evidence → decisions list.

Related: [[proto-61-sheet-provenance-forensics]], [[proto-62-gt-tier-stratified-reporting]], [[proto-92-boss-decisions]]
