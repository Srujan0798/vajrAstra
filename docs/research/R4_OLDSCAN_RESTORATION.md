# R4 — Old-scan restoration: SOTA, cost, and ablation spec

Status: research only. No training. No backbone invention. No GPU until W6 (CPU-only costing in Part B).
Date: 2026-09-26. Scope: the manual old-scan slice (200-dpi govt/textbook/exam pages; South 400 + W3 `old_scan` tags).
Protocol note: the repo holds an UNVERIFIED claim that deskew+Otsu beats deep denoisers on our data. That claim was
protocol-downgraded and stays downgraded until the Part C ablation runs. This doc settles the prior from published
evidence only; it does not settle our data.
Sources are primary only (papers, official repos/competition pages, model cards). Every numbered claim carries a URL.
Where nothing published exists (notably Indic-script binarization competitions), this file says so instead of inferring.

Terminology: "DocRes-class" = unified generalist restoration (DocRes + successors Uni-DocDiff, MMDIR, DocPure).
"Engines fixed" = OCR engines are frozen during the ablation; only the restoration arm varies.

---

## PART A — 2026 SOTA on document restoration/enhancement

### A0. SOTA table (numbers first, caveats inline)

| # | Method (class) | Representative result (published) | Params / weights | Glyph-fidelity risk on our scripts |
|---|---|---|---|---|
| 1 | Otsu global threshold (1979) | DIBCO09 FM 78.72, PSNR 15.34; DIBCO13 FM 83.9, PSNR 16.6; DIBCO14 FM 91.56 / DIBCO16 FM 73.79 (clean-vs-degraded swing) | No weights (algorithm). OpenCV `threshold+OTSU`. Classic refs via review https://arxiv.org/pdf/1901.09425 and tables in https://arxiv.org/pdf/1709.01782v1 , https://arxiv.org/pdf/2010.08764 , https://github.com/rezazad68/BCDUnet_DIBCO | HIGH on stained/uneven pages: one global threshold drowns faint strokes and light diacritics/dots while keeping blotches. Safe only on clean uniform pages. |
| 2 | Sauvola local (2000) / Niblack (1986) | DIBCO09 Sauvola FM 85.41 vs Otsu 78.72; DIBCO13 Sauvola FM 85.0 / Niblack 72.8; DIBCO14 Sauvola 77.08 / DIBCO16 Sauvola 82.00 | No weights. OpenCV ximgproc (`niBlackThreshold`). Tables: https://arxiv.org/pdf/1709.01782v1 , https://arxiv.org/pdf/2010.08764 , https://github.com/rezazad68/BCDUnet_DIBCO | MEDIUM: window-size sensitive. Too-small window eats isolated dots/nuqtas and thin vowel signs; too-large window leaves stain halos. Must freeze one window on a 4-page gate, then lock it. |
| 3 | SauvolaNet (learned Sauvola, 2021) | 40K params (~1% of MobileNetV2); SOTA-class across 13 binarization datasets; best on DIBCO19 in the 2024 fair evaluation (DE-GAN best 2013, DP-LinkNet best 2017, 2-StageGAN best 2018, SauvolaNet best 2019) | Tiny (40K). Code released per paper: https://arxiv.org/abs/2105.05521 ; fair-eval comparison: https://arxiv.org/abs/2401.11831 | LOW-MEDIUM: threshold-only output (no generative repaint), so it cannot invent strokes; residual risk is dot erosion at aggressive thresholds. Best cost/risk trade for CPU. |
| 4 | DP-LinkNet (CNN SOTA) | ~28.7M params; DIBCO09 FM 96.39 vs competition winner 91.24; H-DIBCO10 96.19; DIBCO11 96.27; consistent 4–8 pt lead over classical baselines | Weights per repo/dataset splits: https://exploreds.xyz/beargolden/DP-LinkNet | LOW-MEDIUM: discriminative (no diffusion sampling), but trained on Latin/Greek — thin Indic ligatures are out-of-distribution; validate dots before trusting. |
| 5 | DE-GAN / 2-StageGAN (GAN enhancement+binarization) | DE-GAN DIBCO13 PSNR 24.9 / FM 99.5 / pFM 99.7 / DRD 1.1 (author-reported; note inflation vs winner FM ~92 — treat as optimistic); DIBCO17 FM 97.91 vs winner 91.04; 2-StageGAN best on DIBCO18 per fair eval | Fragmented per-paper weights; formulation as image-to-image translation: https://arxiv.org/pdf/2010.08764 ; fair eval: https://arxiv.org/abs/2401.11831 ; efficient-GAN successor: https://arxiv.org/html/2407.04231 | MEDIUM-HIGH: GANs can drop or merge fine dots/strokes (mode-collapse artifacts) and "beautify" away nuqta distinctions. Never adopt on CER gain alone — require dot-audit. |
| 6 | DocRes (CVPR 2024, generalist, Restormer backbone + DTSPrompt) | Unifies 5 tasks (dewarp/deshadow/enhance/deblur/binarize). Reported: RealDAE enhance PSNR 24.65 / SSIM 0.9219; SD7K deshadow 33.13; H-DIBCO binarization PSNR ~18.5 (competitive, not leading — task-specific Restormer/GDB variants edge it) | OPEN, MIT. Repo: https://github.com/ZZZHANG-jx/DocRes ; paper: https://arxiv.org/abs/2405.04055 (see https://arxiv.org/abs/2405.04408v1) ; weights rehost: https://huggingface.co/DaVinciCode/doctra-docres-main | MEDIUM: enhancement/desmudge heads smooth paper texture — good for stains, risky for 1-px dots and thin conjunct hooks. Binarization head is its weakest of the five; prefer its enhancement head for OCR preprocessing, not its binarization head. |
| 7 | Uni-DocDiff (ACM MM 2025, first unified DIFFUSION restorer) | TDD deblur 28.77 dB / 0.9824; deshadow Kligler 28.56 / 0.9382, Jung 23.93 / 0.9156; appearance RealDAE 24.97 / 0.9485, DocUNet 18.22 / 0.7682 — matches or beats task-specific experts | Paper: https://arxiv.org/html/2508.04055v1 ; task collection it builds on: https://github.com/ZZZHANG-jx/Recommendations-Document-Image-Processing | MEDIUM-HIGH: diffusion sampling can hallucinate stroke detail on rare glyphs (Nastaliq secondaries, Ol Chiki small forms). Prior-Pool + frequency loss help, but no Indic glyph test exists. Gate on dot/matra audit. |
| 8 | DocDiff (MM 2023, residual diffusion enhance) / DvD (generative dewarp) / TextDoctor (2025 inpainting) / MMDIR (CVPR 2026) / DocPure (Aug 2026, prompt-free) | DocDiff: 5-step sampling beats MPRNet/HINet on perceptual metrics; DvD: coordinate-level (not pixel-level) diffusion for dewarp — architecturally the safest diffusion idea for OCR (moves pixels, doesn't repaint them) | DocDiff lineage via https://arxiv.org/pdf/2604.09367 survey; DvD: https://arxiv.org/html/2505.21975v2 ; TextDoctor: https://arxiv.org/abs/2503.04021 ; DocPure: https://arxiv.org/html/2608.09536v1 ; collection: https://github.com/ZZZHANG-jx/Recommendations-Document-Image-Processing | DvD-style coordinate dewarp: LOW repaint risk (preferred if skew/curl dominates). Pixel-repaint diffusion (inpainting/aesthetic): HIGH risk on glyphs — excluded from the ablation. |

How to read this table: classical methods sit ~78–85 FM on DIBCO09-class degraded pages; learned discriminative
methods sit ~92–97; GAN/diffusion add perceptual quality but their pixel-level FM lead over a good discriminative
baseline is small and dataset-dependent (the fair evaluation finds NO single winner — best method changes per DIBCO
year: https://arxiv.org/abs/2401.11831). For OCR preprocessing, that means: threshold quality matters more than
generative beauty, and the DocRes-group's own 2025 follow-up warns aesthetics ≠ text fidelity
("Aesthetics is Cheap, Show me the Text", noted in https://github.com/ZZZHANG-jx/DocRes news).

### A1. Diffusion-based restoration (DocRes-class + successors)

- DocRes (CVPR 2024, Zhang et al.): single Restormer-based generalist over dewarping, deshadowing, appearance
  enhancement, deblurring, binarization, steered by Dynamic Task-Specific Prompts (prior features per task, works at
  variable resolution). Competitive-or-better vs task experts except binarization, where it trails the best specialist.
  Paper: https://arxiv.org/abs/2405.04408v1 ; code+weights (MIT): https://github.com/ZZZHANG-jx/DocRes ; HF rehost
  of `docres.pkl`: https://huggingface.co/DaVinciCode/doctra-docres-main
- Uni-DocDiff (ACM MM 2025, Zhao et al.): first unified restorer built on diffusion, with learnable task prompts
  (scalability fix over handcrafted DTSPrompts), a Prior Pool (local high-freq + global low-freq features), and a
  coordinate branch for dewarping so geometry and pixel tasks stop interfering. Handles dewarp/deblur/deshadow/
  illumination/binarization/handwriting-removal in one model. Paper: https://arxiv.org/html/2508.04055v1 ;
  numbers consolidated in https://github.com/ZZZHANG-jx/Recommendations-Document-Image-Processing (SOTA sheets:
  appearance, deshadow tabs).
- Supporting line: DocDiff residual diffusion (perceptual quality at few steps), DvD coordinate-diffusion dewarp
  (generative control without repainting pixels — the diffusion idea most compatible with OCR), TextDoctor patch-pyramid
  diffusion for inpainting (relevant only as a warning: inpainting invents strokes), MMDIR multimodal-instruction
  mixed-degradation (CVPR 2026), DocPure prompt-free wavelet-modulated (Aug 2026). Links above.
- Load-bearing limitation: ALL diffusion-restoration training/eval is Latin/Chinese/English benchmarks (DocUNet,
  RealDAE, RDD, SD7K, TDD, DIBCO). Zero Indic-script glyph-fidelity tests found. Diffusion is therefore the
  highest-upside, highest-risk arm — and the least CPU-feasible (Part B).

### A2. GAN enhancement

- DE-GAN (Souibgui et al.): cGAN framing of denoising+binarization; strong author-reported DIBCO13/17 numbers
  (see table; treat the 99.5 FM on DIBCO13 as optimistic — winners sit ~92). Paper/table source:
  https://arxiv.org/pdf/2010.08764
- 2-StageGAN: best on DIBCO18 under the common-protocol fair eval; efficient multi-scale GAN variant cuts
  training/inference time vs SOTA GANs: https://arxiv.org/html/2407.04231 ; fair eval: https://arxiv.org/abs/2401.11831
- DocEnTr (ICPR 2022, transformer enhancer, included here as the non-GAN learned-enhancement reference): best
  PSNR/DRD on DIBCO17 in author tests: https://arxiv.org/pdf/2201.10252
- Verdict for us: GAN enhancement is a legitimate arm only with a dot-level fidelity audit. Its failure mode
  (dropped/merged dots, smoothed-away thin strokes) is exactly the Nastaliq/Ol Chiki danger zone, and weights are
  fragmented per paper rather than one maintained checkpoint. Not in the 4-arm ablation; first reserve if SauvolaNet
  fails.

### A3. Classical binarization + modern successors (Otsu / Niblack / Sauvola → SauvolaNet et al.)

- Classics: Otsu (global histogram threshold), Niblack (local mean/std window), Sauvola (Niblack refinement with
  range term; typical k=0.5, R=128). Technique survey: https://arxiv.org/pdf/1901.09425 ; DIBCO09 table
  (Otsu 78.72 / Sauvola 85.41): https://arxiv.org/pdf/1709.01782v1 ; DIBCO13 table
  (Otsu 83.9 / Niblack 72.8 / Sauvola 85.0): https://arxiv.org/pdf/2010.08764 ; DIBCO14/16 cross-table
  (Otsu 91.56→73.79 across clean→degraded years; Sauvola 77.08/82.00): https://github.com/rezazad68/BCDUnet_DIBCO
- Modern successors: SauvolaNet (multi-window Sauvola + per-pixel window attention + adaptive threshold, end-to-end,
  40K params): https://arxiv.org/abs/2105.05521 ; DP-LinkNet (large-margin CNN winner-beater):
  https://exploreds.xyz/beargolden/DP-LinkNet ; ColDBin (cold-diffusion binarization, DIBCO09–18 per-dataset table,
  e.g. 2013 FM 96.62 / 2014 FM 97.89): https://github.com/saifullah3396/coldbin ; critical review of the metric
  suite (FM/pFM/PSNR/DRD/NRM/MPM): https://repository.kaust.edu.sa/bitstreams/a9a3f75e-7694-4ab1-b5d9-7dd687dfb826/download
- "Self-supervised" honesty note: no pure self-supervised binarization SOTA was found in this pass. The closest
  published things to the label are (a) SauvolaNet-style learned thresholds (supervised, but tiny and adaptive),
  (b) test-time/adaptive thresholding variants, (c) GAN/cGAN enhancement trained without paired GT. Do not claim a
  self-supervised SOTA arm exists; the ablation uses supervised-light arms with frozen configs instead.
- 2026 freshness: a March-2026 structured-document study re-confirms Otsu-vs-Sauvola is still an active comparison
  (i.e., the field has not deleted the classical baseline): https://www.semanticscholar.org/paper/Performance-Evaluation-of-Otsu-and-Sauvola-for-Darpito-Firdausy/7778a962b9882f39c342d24952441005e32668a3/figure/0

### A4. Published benchmarks on HISTORICAL INDIC documents — the honest gap

1. DIBCO/H-DIBCO (2009–2019) are NOT Indic benchmarks. Their sets are Latin/Greek machine-print and handwriting
   (plus Bickley Diary English, SMADI multispectral). Competition pages: https://vc.ee.duth.gr/dibco2019 (series
   history back to DIBCO 2009 / H-DIBCO 2010: https://vc.ee.duth.gr/dibco2019) ; H-DIBCO 2018:
   https://www.computer.org/csdl/proceedings-article/icfhr/2018/587500a489/17D45WaTkoF ; DIBCO 2019 report
   (24 methods): https://www.semanticscholar.org/paper/ICDAR-2019-Competition-on-Document-Image-%28DIBCO-Pratikakis-Zagoris/ba478852219088c754dc5c97983c98c2652006cc
   No Indic-script edition found after targeted search. Any "DIBCO proves X on Indic" sentence is unsupported.
2. No Indic binarization competition found. The nearest non-Latin training inclusion is the Persian Heritage Image
   Binarisation Dataset (PHIBD, Persian script) inside multi-set GAN training pools (sets listed in
   https://arxiv.org/html/2407.04231). Persian ≠ Indic, but it is the closest published restoration-adjacent signal
   for Perso-Arabic scripts (Urdu/Sindhi/Kashmiri Nastaliq live in the same script family).
3. What DOES exist for Indic is OCR-level (not binarization-level) evidence, and it all points the same way —
   degraded/old-scan + Perso-Arabic/low-resource scripts are the failure cells: Sarvam Indic bench OldScan 55.3,
   Santali 53.91, Kashmiri 54.82 (W3 schema snapshot; bench: `sarvamai/indic-ocr-bench`); real-Hindi-scan collapse
   (synthetic chrF++ hides it) per https://arxiv.org (arXiv:2606.29213 per W1); VLM rewriting of imperfect text
   (FaithC4) per W1.
4. Nastaliq-specific mechanism (why binarization/thinning is dangerous there): multi-SVM Urdu work documents that
   thinning reduces strokes to 1-px skeletons with lost junction points and alphabet changes, plus diacritic
   mis-association on multi-dot ligatures: https://www.ijrte.org/wp-content/uploads/papers/v8i5/E6949018520.pdf ;
   Nastaliq's diagonal cascading baseline, stacking, and nuqta-critical distinctions are documented in R2 with
   primary sources (CRULP/Lehal/UTRNet). Implication: any binarizer tuned on Latin stroke widths will be
   over-aggressive on Nastaliq diagonals and dots.
5. Ol Chiki honesty note: no binarization/restoration study on Ol Chiki (Santali) found. Risk is inferred, not
   measured: small uniform glyph inventory with fine short strokes and dot-like elements at 200 dpi is precisely the
   profile classical windows and generative smoothers damage first. The ablation must include a Santali/Ol Chiki spot
   check (see C5) rather than a literature claim.

### A5. OTSU VERDICT — is Otsu dead on our data?

NO — as a baseline. YES — as the claim "deskew+Otsu beats deep denoisers."

- The published prior is unambiguous on degraded pages: Otsu trails Sauvola by ~2–7 FM points and trails learned
  methods by ~8–18 FM points on the same DIBCO sets (tables in A3). Otsu's DIBCO14→16 swing (91.56 → 73.79) shows
  exactly why: it is fine on clean uniform pages and collapses on bleed-through/stains/uneven light — which is the
  definition of our old-scan slice.
- The repo's "deskew+Otsu beats deep denoisers" sentence therefore stays UNVERIFIED and protocol-downgraded. Plausible
  only on the clean sub-slice (where every method ties near ceiling), not as a global statement.
- Disposition: KEEP deskew+Otsu as ablation arm A1 (cheap control, interpretable, matches PPT Stage-0 lineage), but
  promote deskew+Sauvola (A2) to the favored classical arm and DocRes-class (A3) to the pilot learned arm. Otsu wins
  a place in the recipe only if Part C shows a non-inferior CER delta with CIs — not by assertion.

---

## PART B — Cost accounting per method (per 4250×6500 scan, CPU-only, no GPU until W6)

Reference size: 4250×6500 ≈ 27.6 MP grayscale ≈ 27.6 MB/frame in uint8 (≈82.9 MB RGB). All learned methods must tile
at this size; classical methods should too for Sauvola windows. Estimates below are order-of-magnitude CPU
(Intel/Apple-Silicon-class, single process, OpenCV/PyTorch CPU) for budgeting, NOT vendor SLAs — the ablation logs
wall-clock per page (column `cpu_sec`) and replaces these with measured numbers.

| Arm | What runs per page | Weights open? | CPU estimate @27.6MP | Memory note | Glyph-fidelity risk (Nastaliq / Ol Chiki thin ligatures + diacritics) |
|---|---|---|---|---|---|
| A0 none | Pass-through (optional resize only) | N/A | ~1–3 s I/O | 1 frame | Zero added risk. Baseline that every arm must beat. |
| A1 deskew+Otsu | Deskew (Hough/projection) + 1 global threshold | N/A (algorithm; OpenCV) | ~3–10 s | 2–3 frames | HIGH on degraded pages (drowns faint strokes/dots); LOW on clean pages. Matches PPT Stage-0; cheapest interpretable control. |
| A2 deskew+Sauvola | Deskew + local window (integral-image impl, e.g. OpenCV ximgproc) + frozen (window, k, R) | N/A (algorithm) | ~15–90 s full-res single-thread; ~5–20 s tiled/threaded | Tiled streaming OK | MEDIUM, tunable: small windows kill isolated dots; large windows keep stain halos. Freeze on 4-page gate (L3), then lock. Favored classical arm. |
| SauvolaNet (reserve / A2b) | Deskew + 40K-param threshold net, tiled 256/512 px | Code per paper (verify checkpoint before W6): https://arxiv.org/abs/2105.05521 | ~30–120 s CPU tiled | Small net, tile-bound | LOW-MEDIUM: threshold-only, no repaint. Best learned option under CPU. Promote to full arm if checkpoint verifies in <1 h. |
| A3 DocRes-class pilot | Deskew + DocRes enhancement head (NOT binarization head), fixed prompt, tiled with overlap, fp32 CPU | YES, MIT: https://github.com/ZZZHANG-jx/DocRes + https://huggingface.co/DaVinciCode/doctra-docres-main (`docres.pkl`) | ~5–30 min/page CPU tiled (≈ Restormer backbone, hundreds of MB); infeasible full-speed without GPU | 8–16 GB RAM working; tile ≤1024 px with overlap | MEDIUM: stain/uneven-light cleanup helps Latin/Devanagari blocks; smoothing risk on 1-px dots, thin conjunct hooks, Nastaliq secondaries. Require dot audit (C5). Pilot on n≤8 before full slice. |
| Deferred: Uni-DocDiff / pixel-diffusion | Iterative sampling × N steps | Paper https://arxiv.org/html/2508.04055v1 ; confirm code release before costing | CPU-INFEASIBLE at 27.6 MP (hours/page class) | GPU-mem class | MEDIUM-HIGH hallucination on rare glyphs. W6-GPU lane only. NOT in this ablation. |
| Deferred: GAN (DE-GAN/2-StageGAN) | Single forward tiled | Fragmented per-paper; verify per checkpoint: https://arxiv.org/pdf/2010.08764 | ~1–10 min CPU tiled | Moderate | MEDIUM-HIGH dot dropout. First reserve. NOT in this ablation. |

Operational consequences of no-GPU-until-W6:

1. Full-slice arms now: A0, A1, A2 (+SauvolaNet if its checkpoint verifies fast). A3 runs as a capped pilot
   (n≤8 pages spanning clean/stained/uneven-light) with wall-clock logged; full A3 across the slice waits for W6 GPU
   unless the pilot shows a large CER win AND acceptable CPU (<~3 min/page tiled).
2. All arms deskew FIRST with the identical routine (log angle per page); never compare "Otsu without deskew" to
   "DocRes with deskew" — that confound is how the original unverified claim likely arose.
3. Downscale rule: no learned arm sees a different resolution than the classical arms on the same page. If A3 must
   run at ≤2048-px long-edge for memory, record it as a separate sub-arm (A3s) rather than silently comparing
   across resolutions.

---

## PART C — Ablation design for the manual old-scan slice (ready to run)

### C0. Locks and firewalls (do not negotiate)

- No training, no backbone invention, no paid APIs (L7). Engines read any script (L8). Family = 1 vote when
  counting engine agreement (L6). Agent work stays out of shared pipeline files (L10); reruns versioned (L5);
  4-page gate before any full-slice run (L3).

### C1. Slice definition

- Population: pages tagged `old_scan` in the South 400 (te/ta/kn/ml) + W3 probe `old_scan` tags as they land.
- Sample: n=40 (10 per South language, stratified clean / stained / uneven-light where tags permit). If fewer than
  40 `old_scan` pages exist, take ALL of them and record n; do not pad with born-digital pages.
- Exclusions: born-digital clean PDFs (different regime); pages with empty GT (log, don't score); handwriting- or
  table-dominated pages stay only if `old_scan` is also present, flagged in `notes`.
- GT: existing L1 gold / script-validated PDF layer (per W3 GT-audit rule); T3-unverified languages flagged, never
  silently treated as gold.

### C2. Arms (restoration varies, everything else frozen)

| Arm | Preprocessing (frozen) | Notes |
|---|---|---|
| A0 none | Raw ingest only | Baseline. |
| A1 deskew+Otsu | Fixed deskew routine → Otsu global | Control; PPT Stage-0 lineage. |
| A2 deskew+Sauvola | Same deskew → Sauvola, ONE frozen (window, k, R) from the 4-page gate | Favored classical arm. |
| A3 DocRes-class | Same deskew → DocRes enhancement head, ONE frozen checkpoint+prompt, tiled | Pilot n≤8 first; expand only on gate pass. |

- Tuning protocol (L3): choose Sauvola window/k and confirm DocRes head on 4 pages (one per language). Freeze.
  The 40-page run uses frozen configs — no per-page tweaking.
- Resolution lock: identical pixels into every arm per page (§B.3). Log `long_edge_px` per row.

### C3. Engines fixed

- Minimal set (cost-bounded): surya (Tier-1 leader) + one tess-family rep (family=1 vote) + paddleocr_indic
  (Tier-2 representative). If compute binds, drop to surya + tess rep and say so in the report.
- 40 pages × 4 arms × 3 engines = 480 inferences; pilot phase = 8 × 4 × 3 = 96. No engine config changes mid-run.

### C4. Metrics and statistics (primary: CER delta with bootstrap CIs)

- Primary endpoint: per-(page, engine) ΔCER = CER(arm) − CER(A0). Report median ΔCER per arm×engine with 95%
  bootstrap CI (1000 paired resamples over pages — same paired-bootstrap discipline as the L2 leaderboard, which
  reported e.g. surya 0.430 [0.369–0.500] and a tied-leader Δ −0.045 [−0.086, +0.020]).
- Reference bootstrap (paired pages, numpy):
  ```python
  import numpy as np
  rng = np.random.default_rng(0)
  d = np.asarray(delta_cer)          # one value per page for a fixed (arm, engine)
  boots = [np.median(rng.choice(d, size=len(d), replace=True)) for _ in range(1000)]
  lo, hi = np.percentile(boots, [2.5, 97.5])
  ```
- Secondary: ΔWER, `old_scan` error-tag rate shift, per-script (te/ta/kn/ml) ΔCER medians, `cpu_sec` median per arm.
- Glyph-fidelity audit (C5) is a co-endpoint, not an afterthought: an arm cannot win on CER while regressing dots.

### C5. Glyph-fidelity audit (Nastaliq / Ol Chiki / matra-conjunct)

1. South slice: count matra-order / conjunct / nukta-dot error tags per arm on the same pages (W3 tag set); arm
   must not increase dot/matra deletions vs A0 (McNemar or paired-rate CI; pre-register tolerance: ≤+1 pp).
2. Perso-Arabic spot check: 5 Urdu/Sindhi/Kashmiri Nastaliq pages (official hackathon set) through A1 vs A2 only —
   score nuqta/dot preservation qualitatively (dots kept / merged / dropped per line) since no binarization GT
   exists. Mechanism prior from https://www.ijrte.org/wp-content/uploads/papers/v8i5/E6949018520.pdf (thinning
   destroys junctions; diacritic mis-association).
3. Ol Chiki spot check: all available Santali pages through A1 vs A2, same dot/short-stroke audit. No literature
   claim is made (none found); this check CREATES the evidence.
4. A3 pilot pages get the same audit before any expansion: if enhancement smooths away ≥2 dots/matra-hooks per
   page vs A0 on average, A3 is rejected regardless of CER.

### C6. Decision rule for W6 (pre-registered)

1. ADOPT arm Ax globally iff: median ΔCER ≤ −0.03 with 95% CI excluding 0, on ≥2 of 3 fixed engines, AND no
   fidelity regression (C5), AND median `cpu_sec` within budget (classical: ≤60 s/page; learned: ≤3 min/page CPU
   or deferred to W6 GPU lane).
2. ENGINE-SPECIFIC flag (not global) iff the bar passes on exactly 1 engine — record as routing rule, not recipe.
3. DEFER iff only A3-pilot passes but CPU-infeasible → W6 GPU lane with identical frozen config.
4. KEEP LIGHT-PREPROCESS iff nothing passes (matches W1 challenger: light preprocess stays useful on OldScan even
   when heavy restoration doesn't pay).
5. REPORT "no evidence" (not "no effect") whenever CIs include 0 — with n=40, wide CIs are expected; the bar is
   exclusion of 0, not the point estimate.

### C7. Ready-to-run sheet and paths

- Sheet columns (extends W3 §columns):
  `image_id | language | script | print_or_hand | quality | old_scan | arm | engine | long_edge_px | cpu_sec | gt | prediction | CER | WER | error_tag | notes`
  One row = one (page, arm, engine) triple. `error_tag` reuses W3 tags
  (`matra_order | conjunct | old_scan | handwriting | table | reading_order | hallucination | repetition | charset | other`).
- Proposed paths (data, not essays): manifest `level2/restore_abla/manifest.json`, rows
  `level2/restore_abla/sheet.csv`, predictions `level2/restore_abla/out/<arm>/<engine>/<lang>/*.json`,
  timings `level2/restore_abla/timings.csv`. Keep South-400 seal tree untouched; version reruns per L5.
- Run order: (1) draw slice + manifest; (2) 4-page gate → freeze Sauvola + DocRes head; (3) A3 pilot n≤8 with
  fidelity audit — STOP/GO; (4) full A0/A1/A2 (+A3 iff GO); (5) bootstrap CIs + per-script splits; (6) apply C6 rule;
  (7) append verdict to DECISIONS-style log with n, CIs, cpu_sec, and frozen hashes.

---

## Bottom line

- SOTA table with numbers: §A0. Classical baselines (Otsu ~79–84, Sauvola ~77–85 FM on DIBCO09/13-class) trail
  learned discriminative methods (~92–97) by large margins; GAN/diffusion add perceptual quality with small,
  dataset-dependent pixel gains and real glyph risk; no Indic binarization benchmark exists — DIBCO/H-DIBCO are
  Latin/Greek and do not transfer silently.
- Costs: on CPU at 4250×6500, only A0/A1/A2 (+tiny SauvolaNet) run at full-slice speed; DocRes-class is a capped
  pilot now, full run at W6-GPU; diffusion sampling and GANs are deferred.
- Ablation: 4 arms × 3 frozen engines × 40 old-scan pages, ΔCER medians with paired-bootstrap CIs, dot/matra
  co-audit, pre-registered W6 adopt/defer/keep-light rule — executable as specified in C1–C7.
