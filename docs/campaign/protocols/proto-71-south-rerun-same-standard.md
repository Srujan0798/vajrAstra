---
name: proto-71-south-rerun-same-standard
description: "Added 2026-09-30 — CO-003/025 + uni T2.2/T6.4 (\"South meets the exact same 100-per-language standard, same verification, no leftovers from older standards\"): feasibility then execution of running ta/te/kn/ml through the probe pipeline from the official dataset, so all 22 languages share one standard; old South 400 becomes history"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:52:47.630Z
---

# PROTO-71 — SOUTH LANGUAGES UNDER THE SAME STANDARD (feasibility by Engine → boss gate U11 → execution)
> **2026-09-30 evening:** the execution order, owners and end state are in [[proto-101-south-unification-and-level2-tree]] (U10/U11 now). This file stays the reference for its inventory and path-dependency lists.

**Why:** the boss's own words: CO-003 "merge into new **or run them fresh in the same flow**"; CO-025 "rerun under the same standard — delete old versions";
uni T6.4 "THE SOUTH LANGUAGES meet this exact same bar — same 100-per-language standard, same verification, no leftovers from older standards."
Today South = 400 self-labelled pages from other sources (Level 1 `arc_level_1/labeled/`, sources like S5_govt), rendered at a different basis, scored by a different writer
(`verify_v2.py`), and **only 126/400 pages carry a CER** (kn ≈4, ml ≈4, te ≈6 scored). The 18 other languages come from the official hackathon dataset through
`level2/probe22/` (extract_gt gates → build_manifest → run_probe → metrics). A symlink view cannot fix a standards difference.

## Official-dataset sources for the 4 languages (monitor, 2026-09-30)
`Datasets/akshardrishti_official/`: Tamil 34 PDF + 4 PNG · Telugu 84 PDF · Kannada 41 PDF · Malayalam 20 PDF + 9 PNG. No image+transcription pairs.
Unknown: how many PDF pages pass the honesty gates (Gujarati: 3,567 text pages → 10 clean because of legacy font encodings — South PDFs may behave the same).

## Phase A — feasibility (Engine subagent, read-only except candidate files in a scratch folder)
> 1. Check `level2/probe22/extract_gt.py` and `build_manifest.py` language tables: do they support `ta`, `te`, `kn`, `ml` (script Unicode ranges, codes)? If not, list the exact
>    additions needed (do not edit yet).
> 2. Run the extract stage for the 4 languages writing ONLY to `docs/campaign/checkpoints/W_south_reports/candidates_<code>.json` (copy the script to a scratch path or pass an output
>    flag — never overwrite `level2/probe22/candidates/`). Report per language: PDFs, pages scanned, pages with text, rejected by reason, clean candidates, distinct PDFs among clean.
> 3. Engines: which of the 10 local engines support each script? Tesseract traineddata for `tam`, `tel`, `kan`, `mal` — `level2/probe22/tessdata/` has none; find what the South run used
>    (`level2/engines_config.py`, `run_engine.py`, system tessdata e.g. `/opt/homebrew/share/tessdata`, `level2/research/smoke/anuvaad_tesseract/tessdata`). `run_probe.py` (LOCKED) language map:
>    does it route ta/te/kn/ml? List exact edits needed. No downloads.
> 4. Time estimate: per engine ms/page from `level2/reports/LATENCY.md` and probe logs × 400 items.
> 5. Write `docs/campaign/SOUTH_RERUN_FEASIBILITY.md`: per language clean-candidate count vs 100, engine coverage, required code edits (with file:line), time, risks, recommendation.

## Boss gate U11 — APPROVED 2026-09-30 ("Yes, feasibility first"): run Phase A, then Phase B for every language the feasibility report marks feasible; report the rest
Present: feasible yes/partial/no per language; edits to LOCKED files needed (`run_probe.py`, possibly `AGENT_PROTOCOL.md` scope); compute hours; what happens to old South 400
(recommended: becomes `benchmark/scores/south400_v1/` history + `_archive/level2_south400_v1/`, cited as "Level 2 v1 (own-labelled, different standard)", never mixed into the 22-language table).

## Phase B — execution (only after U11 yes)
1. Add the 4 languages to extract/build/run tables (fix-specs, Verdict-verified). 2. Extract → draw 100/lang with the same seed and stratification (SEED 20260926), same gates.
3. Run all local engines one at a time (AGENT_PROTOCOL engine discipline), outputs into the probe output tree (or `benchmark/packs/` after proto-70). 4. Score with the same `metrics.py`.
5. Regenerate `BENCHMARK_22.md` so all 22 languages share one standard; old South numbers shown only in a clearly labelled history section.
6. Where a language cannot reach 100 clean pages: record the honest n and why (same rule as the 8 short languages; no gate relaxation, no fabrication).

## Verdict check
Visual spot-check of 10 drawn pages per language (GT vs image), gate statistics reproduce, engine outputs complete (counts per engine × lang), no sealed/locked file edited without the approved fix-spec.

Related: [[proto-70-level2-restructure]], [[proto-20-w2-sampling-reconcile]], [[proto-21-w2-variance-and-resource]], [[proto-92-boss-decisions]]
