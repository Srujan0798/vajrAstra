# R7 — W6 Training Decision Tree (parameterized; scores pending)

Status: plan only. No training. No backbone invention. No 400-page collection.
Binding guards: `level2/probe22/AGENT_PROTOCOL.md` §9 (SFT gold+synthetic always allowed; PDF-layer GT per-language ONLY if §6.4 pass AND §6.2 no pair-vs-pdf gap; RLVR on human-verified gold ONLY, waits for §6.6 no-inversion; sarvam_fill never training; akshara-aux Indic-abugida only, undefined ur/ks/sd/sat/mni; Otsu cheap baseline until old-scan ablation; router only after §6.4+CIs; extraction head parked until forms slice).
Inputs pending: `out/<engine>` packs, `gt_forensics.json` (R5 trust), `gt_verification.json` (§6.4). Probe: n=1227 (pair 300 gold bn/hi/sa; pdf 769 silver; fill 158 agreement-only); Layer-1 pairs 10,432 (bn 2938 / hi 3500 / sa 494 / en 3500). Power §6.7: n=100→~8pp, n<50 no winner claims. WER primary ur/sd/ks, else CER (§6.3).
R5 signal (binding): ks official_pdf trust ~29/100 (short-token 0.71, intra-word splits = extractor artifacts) → ks PDF tier BARRED from SFT until §6.4 verification; mr ~92, brx ~82 (eligible subject to §6.4+§6.2).

Notation: `IF <condition on artifact> THEN <action> ELSE <fallback> [cite | artifact]`.

---

## N0 — Entry gates (evaluate first; all must pass before any SFT)

| # | Gate | Condition | Fail action |
|---|---|---|---|
| N0.1 | EN harness sanity | `out/<engine>` on `en_sanity/manifest.json`: EN CER ≤0.05, else harness broken not models [artifact: `en_sanity/manifest.json` + `out/<engine>/en/*`] | Fix harness; no training |
| N0.2 | Scorer integrity | `metrics.py` §6.5 enforced: empty=1.0 counted, no space-forgery, `cer_uncapped`+`cer_100_count` logged, single denominator [artifact: `preds_<engine>.json` + metrics summary] | Re-score; no stage transition until fixed |
| N0.3 | RLVR scorer gate | §6.6 raw-vs-normalized: no engine rank inversion [artifact: raw vs `--normalize` tables] | RLVR OFF → SFT-only (see N4) |
| N0.4 | Per-language train eligibility | `gt_verification.json` fail-rate ≤20% AND §6.2 pair-vs-pdf gap ≤10pp [artifact: `gt_verification.json` + per-tier CER] | Language's PDF tier barred from SFT (N2) |

---

## N1 — BASE (≤100 GPU-h QLoRA; weights-open check mandatory)

Candidates:
- A: **Qwen2-VL-2B-Instruct** — open weights; QARI-proven backbone; native dynamic resolution + M-RoPE; pretrain 24.8M OCR pairs EN+ZH only, no Urdu → knows OCR-as-task, not Nastaliq-as-script. https://arxiv.org/html/2409.12191v1 · https://arxiv.org/pdf/2308.12966v3 · https://arxiv.org/html/2506.02295
- B: **InternVL2-2B** — open weights; OCRBench-v2 class comparable to Qwen2-VL (InternVL3-8B 49.0 vs Qwen2-VL-7B 51.4 vs Qwen2.5-VL-7B 46.7; neither pre-tuned Nastaliq, both need SFT). https://ling99-ocrbench-v2-leaderboard.hf.space/
- C: **PaddleOCR-VL-0.9B** — open (verify checkpoint before W6); 109-lang incl. Urdu/Sindhi cluster; Nastaliq-vs-Naskh NOT disclosed; two-stage detect+order→crop→VLM (§2+docs). https://huggingface.co/PaddlePaddle/PaddleOCR-VL · https://arxiv.org/abs/2606.03264v1 · https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html

| Param | A (Qwen2-VL-2B) | B (InternVL2-2B) | C (PaddleOCR-VL-0.9B) |
|---|---|---|---|
| QLoRA VRAM (4-bit, r=32, eff-batch 8) | 12–16 GB → ≥16 GB card (T4 marginal, L4/A10/4090 comfortable) https://vast.ai/pricing · R6§9 | same class as A | 8–12 GB → T4 viable |
| 4250×6500 (sa_d004, `image_meta.json`) | TILE ≤1536px overlap (full-frame OOM ≤16GB) | TILE ≤1536px overlap | NATIVE crops via frozen PP-DocLayoutV3 (no full-frame VLM pass) https://github.com/PaddlePaddle/PaddleOCR |
| Indic prior | QARI-v0.2: 0.550→0.061 CER on 50k synth SFT (49-pt closure precedent) https://arxiv.org/html/2506.02295 | no Nastaliq SFT precedent found → inferred same-class as A, no citation | arabic rec 81.27% line-acc, Naskh-skewed; off-shelf Arabic CER 0.77–0.81 https://huggingface.co/PaddlePaddle/arabic_PP-OCRv5_mobile_rec/blob/main/README.md · https://huggingface.co/medyas/arabic_PP-OCRv6_small_rec/blob/main/README.md |

Selection rule (keyed to probe evidence):
- `IF` weights-open check fails for a candidate `THEN` drop it (no API weights train; Sarvam API-only https://www.sarvam.ai/blogs/sarvam-vision-2-1). [artifact: checkpoint hash log]
- `IF` Perso-Arabic WER gap (ur/ks/sd, `out/*` WER primary §6.3) is the binding lag AND QARI-port recipe applies `THEN` A default. [artifact: `out/<engine>/ur|ks|sd/*.json` + https://arxiv.org/html/2506.02295]
- `IF` A ks-CER after stage 2 >0.30 (capacity signal, R2§C5) `THEN` fall back to C hedge (30–50h) in parallel. [artifact: stage-2 checkpoint CER]
- `IF` doc-structure (table/reading-order) dominates error tags `THEN` prefer C harness (frozen detector + pointer order) https://arxiv.org/abs/2606.03264v1 · https://www.sarvam.ai/blogs/sarvam-vision-2-1. [artifact: `sheet.csv error_tag`]
- `DEFAULT: A (Qwen2-VL-2B-Instruct).` Hedge: C in parallel if GPU-h allows. B only if A+C both fail open-check.

---

## N2 — DATA (3 layers; per-language entry)

| Layer | Content | Entry condition | Cap |
|---|---|---|---|
| L1 | 10,432 human pairs (bn 2938 / hi 3500 / sa 494 / en 3500) | ALWAYS allowed (§9) | full |
| L2 | official_pdf 769 silver, PER-LANGUAGE | N0.4 pass for that language AND R5 trust ≥70 AND `gt_verification.json` pass AND §6.2 gap ≤10pp. ks: BARRED at trust ~29 until §6.4 re-verify [artifact: `gt_forensics.json` + `gt_verification.json` + per-tier CER] | only passing languages; mr (~92), brx (~82) eligible-first; gu/ne/doi (n<50) pooled by family only (§6.7) |
| L3 | R2/R3 synthetic, WEAK-CELLS-ONLY | Always allowed as SFT (S6 gold-by-construction, never eval). Mayek RAQM mandatory; Ol Chiki script-ratio gate ≥80% U+1C50–1C7F; Mayek gate ≥80% U+ABC0–ABFF [cites: https://pillow.readthedocs.io/en/stable/reference/ImageFont.html · https://harfbuzz.github.io/harfbuzz-hb-shape.html · R3§B1] | ks/ur/sd 40–60k lines (R2§C2); sat/mni ≥100k renders/script (R3§B4) |

Mixing ratios + token budget (LoRA r=32, 8-bit AdamW, eff-batch 8, seq 2048; total ≤100 GPU-h):
- S1 (pairs-only): L1 100% × 2 epochs ≈ ~25 GPU-h (2B) / ~15h (0.9B).
- S2 (+gated PDF): L1:L2 = 70:30 (upsample L1) × 1 epoch ≈ ~25 GPU-h / ~12h.
- S3 (+synthetic weak-cells): L1:L2:L3 = 50:20:30 × 1 epoch ≈ ~30 GPU-h / ~15h.
- RLVR (N4): ≤20 GPU-h on verified gold only. S1+S2+S3+RLVR ≤100h; any overrun → cut RLVR first, then S3 epochs.
- `IF` L2 language fails N0.4 `THEN` its 20–30% share reverts to L1 (never to fill; sarvam_fill NEVER trains). [artifact: `gt_verification.json`]

---

## N3 — CURRICULUM (official_pair → official_pdf → synthetic degraded)

- C1 pair (crop/word-ish; `set`=pair encodes granularity §9): S1 L1-only. Words 1–3 tok 50% / lines 5–15 tok 35% / blocks 3–6 lines 15% (R3§B1 ladder; challenger word→line→block per W1).
- C2 pdf (page, 200-dpi renders): S2 adds L2-passing languages only. NO layout-mix inside line-CER stage (QARI-v0.3 regressed 0.061→0.300 on layout mix https://arxiv.org/html/2506.02295).
- C3 synthetic degraded (pixel-only; GT frozen at sampling; geometry→ink→optical→compression order, ~15% clean anchors; JPEG q{30,50,70,90}+95; SR/CLAHE-gated inference https://arxiv.org/html/2505.13943v2): S3 adds L3 weak-cell flood.
- Transitions: `IF` S1 EN CER ≤0.05 AND pair-tier CER stable (CI excludes regression, §6.7 n≥50 cells only) `THEN` S1→S2 `ELSE` extend S1 ≤1 epoch. [artifact: checkpoint CER + `cer_uncapped` + CIs] `IF` S2 gated languages show no §6.2 gap reopen `THEN` S2→S3 `ELSE` hold S2, quarantine failing language to L1-only.
- Checkpoints per scorer rules: log capped CER means + `cer_100_count` + raw AND normalized tables every epoch; abort stage `IF` empty-pred rate rises (silence=1.0 counted §6.5). No 4-bit quant of recognizer (QARI 4-bit CER 3.45 vs 8-bit 0.091 https://arxiv.org/html/2506.02295).

---

## N4 — RLVR (verified gold only; OFF fallback)

- `IF` N0.3 inverts (rank flips raw↔normalized) `THEN` RLVR OFF → SFT-only. No override. [artifact: §6.6 ablation tables]
- `IF` ON: reward `R_t = Valid_t · Struct_t · Sim_t` https://arxiv.org/abs/2606.03264v1 (§4.3.2):
  - Valid: binary 0 on degeneration/truncation/malformed (anti-hacking arm).
  - Sim: OCR `1 − clip(cer_uncapped,0,1)` (uncapped visible §6.5, means capped); tables via TEDS only through frozen harness (extraction head PARKED §9).
  - Struct: soft penalty (rectangularity/LaTeX-validity analogue; for OCR lines = charset/shape conformity).
- Rollouts: 16/sample, T 0.85, top-p 0.9, top-k 32; keep r_max−r_mean high, variance non-flat; per-task top-8K; mining weight α=1 β=2 https://arxiv.org/abs/2606.03264v1 (§4.3.1). KL β 0.05–0.1 (0.9–2B policy sensitive to noisy/flat samples, R1§2b). Group size 16.
- Anti-GT-noise shaping: rollouts ONLY on human-verified gold (L1 + §6.4-passed L2 lines); never pdf-unverified, never fill (RLVR on extractor noise optimizes mimicry §9). Normalize NFKC + bidi-isolate BEFORE reward on ur/ks/sd (else 3–8pp scoring artifact) https://arxiv.org/html/2606.07167v1 · https://learnpunjabi.org/pdf/lehal.11.pdf.
- Success: median ΔCER ≤−0.03 with 95% paired-bootstrap CI excluding 0 on ≥2 engines (same bar as R4§C6). Else keep SFT checkpoint.

---

## N5 — WEAK-CELL subtrees

**N5a. ks/ur/sd Nastaliq flood (+router, router gated):**
- Physics: diagonal stacking, kashida, ligature explosion (9,262 ligatures https://dl.acm.org/doi/10.1145/2505377.2505379), CTC independence violation → autoregressive VLM decoder required (R2§A6; EasyOCR/Tesseract Nastaliq collapse WER 0.90–1.57 https://arxiv.org/html/2505.13943v2).
- Flood (R2§C2): 40–60k lines — 10k ks (Awami ≥3.300 https://software.sil.org/awami/release-3-300 + Gulzar + Mehr; Kashmiri Yeh U+0620 https://www.unicode.org/wg2/docs/n3673.pdf) + 20k ur (Jameel Noori Regular+Kasheeda https://urdufonts.net/fonts/jameel-noori-nastaleeq-regular?jmlVVPJ8=fc3MoVSPW + Noto v4 https://github.com/notofonts/nastaliq/releases + Alvi/Pak/Alqalam) + 10k OpenITI/UPTI-mix https://arxiv.org/html/2505.13943v2 + 5–10k degraded duplicates; QARI-v0.2 plain→diacritized/10-font order https://arxiv.org/html/2506.02295. Naskh distractor included for style separation https://arxiv.org/pdf/2205.02543.
- Bar: ks CER 0.55→≤0.20; `IF` ks >0.30 after stage 2 `THEN` abort A→C hedge (capacity signal R2§C5). [artifact: held-out 1k ks lines + 329-line real split]
- Preprocess first (week-1, independent): SwinIR-SR + CLAHE + NFKC/bidi (UNB +25–70% WER recovery https://arxiv.org/html/2505.13943v2). Path-5 CTC rec head NO-GO as primary (Naskh-skewed https://huggingface.co/PaddlePaddle/arabic_PP-OCRv5_mobile_rec/blob/main/README.md).
- Router: `IF` §6.4 pass AND CIs exist AND Bodhan-vs-Sarvam-class split (Santali precedent +14pt Bodhan https://huggingface.co/bodhan-ai/indic-ocr · https://www.sarvam.ai/blogs/sarvam-vision-2-1) replicates on ks/ur/sd `THEN` route weak Nastaliq blocks to specialist `ELSE` single model. Never route on fill cells (as/mni/sat agreement-only §6.2). [artifact: `gt_verification.json` + per-lang CIs + `out/*/ks|ur|sd/*.json`]

**N5b. sat (Ol Chiki) synthetic-only:**
- Inventory: single OFL design (Noto Sans Ol Chiki 4 weights https://fonts.google.com/noto/specimen/Noto+Sans+Ol+Chiki); corpora sat.wiki ~15.9k arts https://en.wikipedia.org/wiki/Santali_Wikipedia + FLORES sat_Olck 3,001 sents https://github.com/facebookresearch/flores/blob/main/flores200/README.md?plain=1; zero native labeled lines (R3§A4). BASIC layout acceptable, RAQM preferred https://pillow.readthedocs.io/en/stable/reference/ImageFont.html.
- `IF` probe sat cell (n=20, agreement-only §6.2/§6.7) shows charset errors `THEN` ≥100k renders, script-gate ≥80%, rare-char booster N≥500/char, val = held weight 700 + held seed (R3§B4) `ELSE` hold (router question dominates; Bodhan leads sat 68.30 https://huggingface.co/bodhan-ai/indic-ocr). Chassis TRDG https://github.com/Belval/TextRecognitionDataGenerator / SynthTIGER https://arxiv.org/abs/2107.09313. Never eval on synthetic (§B0).

**N5c. mni (Meitei Mayek) synthetic-only:**
- Inventory: two OFL designs (Noto 9 weights https://fonts.google.com/noto/specimen/Noto+Sans+Meetei+Mayek + Eeyek https://github.com/silnrsi/font-eeyek); RAQM/HarfBuzz MANDATORY (ABE3–ABEA + ABED misplace under BASIC) https://pillow.readthedocs.io/en/stable/reference/ImageFont.html · https://harfbuzz.github.io/harfbuzz-hb-shape.html.
- `IF` mni agreement cell warrants SFT `THEN` ≥100k renders, train Noto / val Eeyek-only (font-disjoint), historic U+AAE0–AAFF ≤2% (R3§B1–B4) `ELSE` hold for real-gold verification first.

**N5d. OldScan ablation (per R4§C, binding):**
- Arms A0 none / A1 deskew+Otsu / A2 deskew+Sauvola (frozen window,k,R from 4-page gate) / A3 DocRes-enhancement-head pilot n≤8 (NOT binarization head) https://github.com/ZZZHANG-jx/DocRes · https://arxiv.org/abs/2405.04408v1 · SauvolaNet reserve https://arxiv.org/abs/2105.05521. Otsu prior trails Sauvola ~2–7 FM, learned ~8–18 FM https://arxiv.org/pdf/1709.01782v1; DIBCO Latin/Greek only, no Indic transfer https://vc.ee.duth.gr/dibco2019.
- `IF` pilot passes C5 dot audit (Nastaliq thinning risk https://www.ijrte.org/wp-content/uploads/papers/v8i5/E6949018520.pdf; A3 rejected if ≥2 dots/matra-hooks smoothed/page) AND CPU ≤3 min/page `THEN` expand to 40-page run `ELSE` A0/A1/A2 only; diffusion/GAN deferred (CPU-infeasible, glyph risk).
- ADOPT Ax globally `IF` median ΔCER ≤−0.03, 95% paired-bootstrap CI excludes 0, on ≥2/3 frozen engines (surya + tess-rep + paddleocr_indic), no C5 regression, cpu within budget `ELSE IF` 1 engine → engine-specific routing flag `ELSE` KEEP LIGHT-PREPROCESS. [artifact: `level2/restore_abla/sheet.csv` + timings]

---

## N6 — INFERENCE (CPU / limited-GPU)

- Tile 4250×6500 inputs (≤1024px, overlap; identical pixels per arm; log `long_edge_px`; downscaled variant = separate sub-arm A3s per R4§B.3).
- Det-cap analog: frozen detector (PP-DocLayoutV3 / Bodhan-IndicDocLayout / DocLayout-YOLO) + VLM-on-crops + pointer-order merge; end-to-end VLM only for dense spotting regions https://www.paddleocr.ai/latest/en/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL.html. paddleocr_indic precedent: det-cap required for 8–20h feasibility (protocol §5).
- Latency/page (protocol §5 worst-case 4250×6500): rapidocr ~10m/slice; tesseract-family 1.5–3h/slice; doctr ~2h; surya ~4h; easyocr ~6h; indicphotoocr ~12h; paddle ~8–20h; sarvam API 5–8s/call (credit-capped, trial only). Log `cpu_sec` per (page, arm, engine); learned arms must clear R4§C6 cpu bar or defer to W6-GPU lane.
- Accuracy/latency knob: `IF` page clean (A0≈A1≈A2 per ablation) `THEN` A1-deskew+Otsu fast path `ELSE IF` stained/uneven-light AND A2/A3 adopted `THEN` slow path `ELSE` light-preprocess default (W1 challenger rule, R4§C6.4). Deterministic greedy decode + CLAHE/SR gate for ks/ur/sd (Historic-Arabic CER-0.10 recipe).
- akshara-aux: Indic-abugida only; OFF for ur/ks/sd/sat/mni (§9). Extraction head: PARKED (no forms slice §9; Sarvam KV/forms + Paddle TEDS/Valid·Struct·Sim cited as metric only https://www.sarvam.ai/blogs/sarvam-vision-2-1 · https://arxiv.org/abs/2606.03264v1).

---

## Artifact index (every deferred branch resolves here)

`out/<engine>/<lang>/<image_id>.json` · `preds_<engine>.json` · `sheet.csv` · `gt_forensics.json` (R5 trust) · `gt_verification.json` (§6.4) · `image_meta.json` · `en_sanity/manifest.json` · `level2/restore_abla/{manifest.json,sheet.csv,timings.csv}` · checkpoint CER/CI logs.

*Default pick: Qwen2-VL-2B-Instruct (QARI 0.550→0.061 precedent at identical scale/backbone https://arxiv.org/html/2506.02295); PaddleOCR-VL-0.9B parallel hedge.*
