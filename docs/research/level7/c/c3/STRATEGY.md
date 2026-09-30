# Lane C3 — Data-Collection Strategy for Remaining Languages (quality-first)

Locked 2026-09-26. Standing law (C3-001/004/113/114): NO 400-page sets · no downloads without explicit user yes · no training before freeze · sealed dirs untouched · fill declared as fill.
Evidence: LEDGER.md, same dir (115 records C3-001…C3-115, mandatory format). This file holds verdicts; the ledger holds records. Verdict agent: 10% re-check ≈ 12 records (suggested: C3-009/010/030/047/053/061/067/069/076/087/090/098).

## 1. Decision logic (applies to every cell)

1. Probe/eval vs SFT-safe are disjoint roles. Only HUMAN gold (official pairs, hand-verified lines, human-validated benches) may eval. Synthetic (S6 gold-by-construction) may SFT, NEVER eval (C3-007, R3§B0).
2. Every real line inherits the purge gates verbatim: ≥50 chars, script-ratio ≥0.5, Latin ≤0.6, control chars ≤3, GT ≥10 chars (C3-001). PDF-layer GT trains per-language ONLY on §6.4 pass + §6.2 pair-vs-pdf gap ≤10pp + R5 trust ≥70 (C3-003).
3. Mixing (R7, C3-003): S1 L1 100% ×2ep → S2 L1:L2 70:30 ×1ep → S3 L1:L2:L3 50:20:30 ×1ep → RLVR ≤20 GPU-h on verified gold only. Failing language reverts to L1, never to fill. Curriculum word→line→block 50/35/15, NO layout-mix in line stage (QARI v0.3 regression C3-094).
4. License-hygiene is a selection criterion: prefer MIT/Apache/CC-0/CC-BY for lines that may survive to product; NC-lineage tagged in sidecars, hackathon-only; copyleft quarantined (C3-079…085).

## 2. Per-cell verdicts

### ks/ur/sd — Nastaliq (ks 54.82; R5 ks trust ~29–45, ur 59.0 VERIFY-FIRST)
- SFT-safe (no approval needed beyond standing gate): 600k-ks-ocr word renders CC-BY-4.0 (C3-009) + KS-LIT-3M render strings CC-BY-4.0 (C3-010) + SynthOCR-Gen pipeline (C3-011/089) → R2 40–60k line curriculum (10k ks Awami≥3.300/Gulzar/Mehr + 20k ur Jameel-class/Noto/Alvi + 10k OpenITI/UPTI-mix + 5–10k degraded dupes), Kashmiri-Yeh U+0620 booster (C3-031), QARI plain→diacritized order (C3-094). ur word-hedge: RAVI 99k (C3-018) → PARSeq path (C3-036).
- Real anchors (hundreds of lines, NOT a collection): 300–500 hand-corrected ks lines mined from probe ks_100 + UNB 829-block eval transfer (C3-017; confirm host/license at freeze) + CLE image corpora (C3-019; confirm Nastaliq split).
- Probe/eval: UNB + OpenITI 250+250 + IIITH-corrected + UTRSet-Real (NC, agreement-gated, C3-014/015). UPTI synth never evals.
- GT gates: NFKC+bidi scoring pipeline mandatory pre-CER (C3-035, else 3–8pp artifact); WER primary (protocol §6.3); §6.4 verify-first on ks/ur before ANY PDF-tier SFT.
- sd note: Naskh-distractor training (Nafees wordlists C3-027) for style separation; Paddle-Arabic off-shelf excluded as ks fix (C3-109); sd Sindhi-script gate (Perso-Arabic vs Devanagari) on Dootio-corpus strings (C3-026).

### sat — Ol Chiki (53.91; probe n=20, 100% fill, agreement-only)
- SFT-safe: FLORES sat_Olck 3,001 sents CC-BY-SA (C3-037/038) + sat.wiki ~15.9k articles (C3-040) + santali-nlp/Crúbadán/OLAC boosters (C3-041/042) → ≥100k renders in Noto Sans Ol Chiki OFL (C3-047), gate ≥80% U+1C50–1C7F (C3-048), rare-char N≥500, val = held weight-700 + held seed (single-design constraint).
- Probe/eval: Mozhi-LR real slice IF script-verified Ol Chiki per file (C3-043/044); EkStep-90k synth row is SFT-side only (C3-045); ICDAR-HW organizer-gated, handwriting-tagged (C3-046).
- Router dominates volume: Bodhan leads sat 68.30 — the R7-N5b IF/ELSE (router vs more synth) is decided post-§6.4, not by collecting more (C3-110).
- Contamination guard: Bengali-script Santali (probe sat_14 mode) routed to bn-renderer queue, never Ol-Chiki renderer; transliterated strings need the 95%-on-500 sample gate (C3-051).

### mni — Meitei Mayek (probe n=20 fill; frontier VLMs ~0)
- SFT-safe: EN↔mni_Mtei 461k MIT (C3-053) + FLORES mni slice post-script-gate + CLDR seeds (C3-065) → ≥100k renders, train Noto-9-weight (C3-060) / val Eeyek-only font-disjoint (C3-061), RAQM-assert-or-abort + `language="mni"` (C3-064/112), historic block ≤2%, NFC order-sensitive.
- Probe/eval: printed-Mayek char bench (C3-056; confirm host/terms) as char-slice anchor; HW sets (TUMMHCD C3-054, IEEE-37 C3-055, Kaggle C3-058, Deena-55 C3-059) are future-handwriting pointers, excluded from printed budgets.
- Context: Bengali→Mayek switchover (C3-066) — re-check completion at freeze; expect Bengali-script contamination in crawls.

### or — Odia (80.01; weakest real-GT cell; probe or_69)
- SFT-safe strings: abhilash88 801MB CC-BY-4.0 DEFAULT base (C3-072) → IndicCorpV2-CC-0-overflow IF or-coverage confirmed (C3-075, TODO-verify) → IndicCorp-NC overflow tagged (C3-074); OdiEnCorp ≤20% share with extractor-noise gate (C3-073); Samanantar/Charles-EN-OR translationese-capped (C3-078).
- Probe/eval (pool to n≈350+ for CIs): or_69 probe tier + Odia-Lipi human-validated pages (C3-069, NC hackathon-only) + 223-row bench (C3-070) + Mozhi-Oriya slice IF CVIT terms clear (C3-104/105).
- Volume honesty: the 192k merge (C3-067/068) is ~95% char-level 32px — char-warm-up only, never line-SFT; the or gap is LINE/BLOCK data, filled by renders + the R7 S3 share, not by recounting chars.
- Precedent budget: Odia Qwen2.5-VL-3B FT, 58.7k pairs ×3ep ≈ 4 A100-h (C3-071) — our S3 ≤30 GPU-h is conservative.
- Layout harness: IndicDLP MIT incl. or (C3-076), role-separated (blocks/reading order, not OCR GT).

### OldScan (55.3)
- No restoration training set. Ablation only (R7-N5d, C3-108): A0/A1 Otsu / A2 frozen-Sauvola / A3 DocRes-pilot n≤8 with C5 dot-audit + CPU ≤3min/page; adopt bar median ΔCER ≤−0.03, 95% CI, ≥2/3 frozen engines.
- Degrader stack: Augraphy MIT default (C3-090) + TRDG/SynthTIGER MIT chassis (C3-087/088) + DocCreator as parameter-reference/binary-only (LGPL, C3-091) + SwinIR/CLAHE preprocess first (C3-017, +25–70% WER recovery).
- Only new collection: ~40-page manual old-scan EVAL slice (human-tagged, P1 §6.8); DIBCO/H-DIBCO are Latin/Greek method+cost references, never training data (C3-106/107).

## 3. GT-quality gates before any SFT use (summary)
Verify 100% of fill (158, blind) + 10% stratified PDF (~77, seed 20260926) with gold-seed checks per batch (C3-102/103); per-language >20% fail ⇒ tier barred; falsification gap >10pp ⇒ PDF GT suspect (C3-100); fail = image-vs-string semantic error, never normalization trivia (C3-100); dual-blind verify, never engine-majority vote (C3-099); triage low-confidence lines first (C3-101); report CIs on small cells, pool by family, no winners n<50 (protocol §6.7).

## 4. WHAT NOT TO COLLECT (closed list — C3-113/114/115)
400-page sets (any lang) · any download without user yes · training pre-freeze · sarvam_fill/Bodo-gu/test-test as GT · synthetic as eval · API-derived machine GT as GT · Rekhta/santals.in/Hueiyen bulk · Jameel-Noori redistribution · blogspot fonts · GPL-legacy-Eeyek · OpenSLR-GPL transcripts · Kaggle-provenance sets · SEACrowd-NC mirror · DocCreator in import chain · 4-bit recognizer quant · API at inference · novel backbone.
Allowed-but-capped: Grierson-1932, dictionary-register ≤10%, translationese ≤20%, OCR-extracted text (gated), transliterated strings (95%-sample gate).

## 5. Top-3 findings (return summary)
1. Kashmiri is SOLVED as a sourcing problem, not a collection problem: 600k CC-BY-4.0 synthetic words (C3-009) + 3.1M-word CC-BY-4.0 text base (C3-010) + OFL ks-capable fonts (C3-030/032) cover the R2 40–60k flood legally — the only real-data need is 300–500 hand-corrected lines (C3-006).
2. sat/mni need ZERO new collection: FLORES + sat.wiki + 461k-MIT-Mayek + two OFL Mayek designs with font-disjoint val (C3-037/040/053/060/061) already fund ≥100k-renders/script; sat's binding constraint is the router decision (Bodhan 68.30), not volume (C3-110).
3. Odia's 192k "merged dataset" is a granularity mirage (~95% 32px chars): the or cell needs line/block renders (CC-BY-4.0 801MB base, C3-072) + pooled human eval (probe + Lipi + 223-bench ≈ 350+, C3-069/070) — and the Qwen-3B precedent says the whole or-SFT fits in ~4 GPU-h (C3-071).

Record count: 115 (LEDGER.md C3-001…C3-115). Paths: `docs/research/level7/c/c3/STRATEGY.md` + `docs/research/level7/c/c3/LEDGER.md`.
