---
name: proto-15-w1e-edge-hunt
description: "Step 1E part 1 (research subagent) — the hidden-frontier hunt for Indic OCR edges 2025–2026: what counts as a find, what is rejected as well-known, the search-direction map across 10 families, per-find record format"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:13:10.662Z
---

# STEP 1E-HUNT — HIDDEN FRONTIER (research subagent) → report saved to `docs/campaign/checkpoints/W1_reports/1E_hunt.md` by the lead

**Why:** the boss (CO-086/087/088): "merging best strategies and assuming we beat them is nonsense; there is some edge/tactic to CRACK — the only way to beat
or compete". Hunt what is "beneath the ground — submerged, misleading, fallen-down, understated latest work; the basic integrations that are overlooked;
the crossings that emerged quietly from frontier models". A solo operator with agents cannot win on compute or data volume; only on what the field overlooked.

## TASK block (paste)
You are the frontier-research agent. This is NOT a literature survey. Eight genuinely non-obvious finds beat forty known ones. Three substantiated finds
and an honest "only three" is a good result. Do not pad.

**Scope:** Indic / multilingual OCR and document understanding, published 2025–2026. Load WebSearch/WebFetch via ToolSearch. Record every query you run.

**Our constraints (each find must be buildable within them):** 22 languages; ~1,683 labelled items (probe22 1,283 + South 400, but South has only ~126 scored pages);
10 independent local engines already run (surya, easyocr, paddleocr_indic, indicphotoocr, doctr, rapidocr, anuvaad_tesseract, tesseract family ×3 identical);
Santali (Ol Chiki) and Meetei Mayek have almost no engine support; Urdu/Kashmiri Nastaliq is cursive; no novel backbone (lead's rule); no downloads without the boss's
approval; no Sarvam calls left; ~5 development days; training not started and paused; Apple M2 Max, MLX stack installed, ~9–12 GB usable for training.

**Counts as a find:** a technique published without fanfare that nobody has combined with OCR; a result buried in an ablation table that is more interesting than the
headline; a method crossing over from an adjacent field not yet applied to Indic script recognition; an open dataset/tool/checkpoint competitors are not using;
**a structural flaw in how the field evaluates Indic OCR** (a flaw in the benchmark is an edge).
**REJECTED-AS-WELL-KNOWN (list them, don't count them):** LayoutLM/Donut/TrOCR/Surya/PaddleOCR coverage; "use a VLM"; "fine-tune on more data"; generic LoRA;
"ensemble engines" without a mechanism; anything a competent engineer already knows.

**Search-direction map — cover each family with ≥2 queries (examples; write your own too):**
1. *Evaluation flaws:* Unicode normalisation pitfalls in Indic CER (NFC vs NFKC, ZWJ/ZWNJ, nukta, chillu in Malayalam, virama/halant, visually identical
   code-point sequences); grapheme/akshara-level vs code-point CER; benchmark contamination in OCR; self-built vendor benchmarks.
2. *Multi-engine fusion with a mechanism:* ROVER-style character alignment and voting across OCR engines (speech-recognition origin); confidence-calibrated routing;
   disagreement as an error detector; minimum-Bayes-risk decoding across engines.
3. *Post-OCR correction:* LLM post-correction for Indic scripts; script-aware language-model rescoring; lexicon/akshara-grammar constraints (valid syllable structure as a verifier).
4. *Verifiable rewards:* RLVR/GRPO with CER or akshara-validity rewards for OCR; rule-based verifiers for Indic orthography.
5. *Low-resource scripts:* synthetic rendering with font/degradation diversity for Ol Chiki and Meetei Mayek; transliteration bridges; cross-script transfer
   between Brahmic scripts (shared structure); few-shot VLM prompting with script exemplars.
6. *Degraded documents:* restoration pre-passes (diffusion/document enhancement) measured on non-Latin scripts; binarisation for Indic.
7. *Test-time compute:* multi-crop/multi-scale inference, self-consistency over VLM transcriptions, iterative re-reading of low-confidence lines.
8. *Layout/reading order:* line segmentation failures specific to Indic (matras/diacritics crossing lines), Nastaliq baseline problems.
9. *Data leverage:* PDF text-layer mining with honesty gates (what we already do) — who else does it; weak supervision from multiple engines' agreement.
10. *Quiet releases:* small 2026 OCR models/checkpoints, Indic datasets (e.g. 600k-ks-ocr for Kashmiri, already noted), tools on GitHub with little attention.

**Per-find record:** `ID · title · URL (opened) · date · what it does (2 lines) · evidence of the key result (quote or table ref) · why the field overlooked it ·
what WE could build from it in ~5 days that competitors have not (concrete: which languages, which of our engines/data, what output) · cost in dev days ·
risks · novelty PRIMARY/DERIVED/UNKNOWN`.

**Output:** (1) finds ranked by (impact on our weak cells × buildability); (2) REJECTED-AS-WELL-KNOWN list with one line each; (3) all queries run;
(4) UNRESOLVED. Under 2,000 words.

## Lead's handling
Save the report to `docs/campaign/checkpoints/W1_reports/1E_hunt.md`. Verify 3 random URLs open and say what the record claims. Then go to [[proto-16-w1e-edge-refutation]].

Related: [[proto-16-w1e-edge-refutation]], [[proto-14-w1d-competitor-intel]], [[proto-10-w1-overview]]
