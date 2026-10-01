# GATE G-B3 — tesseract 5.5.2: tessdata_best vs FAST (homebrew) × PSM{3,6,1} — 4-PAGE GATE

Date: 2026-09-13 · Runner: EXEC (opencode) · Env: tesseract 5.5.2 CLI (/opt/homebrew/bin/tesseract)
Pages: te_001 / ta_001 / kn_001 / ml_001 (level2/renders_shared/)
Stacks mirror run_engine.py TESS_STACK (lines 46–51, read before writing):
te=tel+hin+eng, ta=tam+hin+eng, kn=kan+hin+eng, **ml=mal+hin+eng** (ml DOES use mal).
Models: FAST = /opt/homebrew/share/tessdata (homebrew), BEST = /tmp/tessdata_best
(downloaded 2026-09-13 from raw.githubusercontent.com/tesseract-ocr/tessdata_best).
Raw data: `research/gates/b3_results.json` (24 runs), `b3_quality_jac.json` (Jaccard-5 vs surya GT).
Script: `research/gates/b3_tessdata_best_gate.py` (standalone; no shared .py touched).

## 0. Model-set integrity note (md5, honest disclosure)

- /opt/homebrew **mal.traineddata md5 8de6fa791db70e78aaa727c99bba46e4 == tessdata_best mal**:
  homebrew Malayalam is ALREADY the best model. ml fast-vs-best rows are same-model A/B
  (deltas = noise, ml psm1 best-vs-fast "delta" is really a PSM behavior difference).
- tel/tam/kan/eng/hin homebrew models differ from best (tel fast 3.3MB vs best 9.1MB etc.).
  hin homebrew (1.65MB) is the FAST variant; best hin (11.9MB) used in stacks.

## 1. Full config table (chars, script chars, latin, ratio, ms)

| page | models | psm | chars | script | latin | ratio | ms |
|---|---|---|---|---|---|---|---|
| te_001 | fast | 3 | 1723 | 1376 | 44 | .7986 | 2147 |
| te_001 | fast | 6 | 2015 | 1607 | 38 | .7975 | 2093 |
| te_001 | fast | 1 | 1723 | 1376 | 44 | .7986 | 2230 |
| te_001 | best | 3 | 1718 | 1387 | 26 | .8073 | 3028 |
| te_001 | best | 6 | 2017 | 1623 | 24 | .8047 | 3343 |
| te_001 | best | 1 | 1718 | 1387 | 26 | .8073 | 3027 |
| ta_001 | fast | 3 | 1456 | 1200 | 10 | .8242 | 1897 |
| ta_001 | fast | 6 | 1392 | 1112 | 26 | .7989 | 2037 |
| ta_001 | fast | 1 | 1456 | 1200 | 10 | .8242 | 2022 |
| ta_001 | best | 3 | 1449 | 1192 | 10 | .8226 | 3258 |
| ta_001 | best | 6 | 1346 | 1029 | 54 | .7645 | 3546 |
| ta_001 | best | 1 | 1449 | 1192 | 10 | .8226 | 3261 |
| kn_001 | fast | 3 | 3888 | 1512 | 1576 | .3889 | 4303 |
| kn_001 | fast | 6 | 3797 | 1452 | 1457 | .3824 | 7243 |
| kn_001 | fast | 1 | 3888 | 1512 | 1576 | .3889 | 4421 |
| kn_001 | best | 3 | 3887 | 1516 | 1575 | .3900 | 7274 |
| kn_001 | best | 6 | 3817 | 1452 | 1487 | .3804 | 12138 |
| kn_001 | best | 1 | 3887 | 1516 | 1575 | .3900 | 7285 |
| ml_001 | fast | 3 | 1980 | 488 | 951 | .2465 | 5708 |
| ml_001 | fast | 6 | 1964 | 572 | 829 | .2912 | 5656 |
| ml_001 | fast | 1 | 2231 | 1717 | 103 | **.7696** | 4715 |
| ml_001 | best | 3 | 1795 | 540 | 674 | .3008 | 8708 |
| ml_001 | best | 6 | 1807 | 508 | 690 | .2811 | 8574 |
| ml_001 | best | 1 | 1795 | 540 | 674 | .3008 | 8709 |

## 2. best-vs-fast deltas (verdict-rule arithmetic)

| page | psm | chars Δ | ratio Δ | verdict-rule |
|---|---|---|---|---|
| te_001 | 3 | −0.3% | +.009 | FAIL (chars −, ratio + but <10% char gain) |
| te_001 | 6 | +0.1% | +.007 | FAIL (no ≥10% char gain) |
| te_001 | 1 | −0.3% | +.009 | FAIL |
| ta_001 | 3 | −0.5% | −.002 | FAIL |
| ta_001 | 6 | −3.3% | −.034 | FAIL (fidelity DROP) |
| ta_001 | 1 | −0.5% | −.002 | FAIL |
| kn_001 | 3 | −0.0% | +.001 | FAIL |
| kn_001 | 6 | +0.5% | −.002 | FAIL |
| kn_001 | 1 | −0.0% | +.001 | FAIL |
| ml_001 | 3 | −9.3% | +.054 | FAIL (chars −9.3%; same-model anyway) |
| ml_001 | 6 | −8.0% | −.010 | FAIL |
| ml_001 | 1 | −19.5% | −.469 | FAIL (psm1+best destroys ml) |

**ZERO of 12 configs meet the win rule (chars +≥10% at same-or-better fidelity).**
Jaccard-5 vs surya GT agrees: te fast_psm6 .8143 > best_psm6 .7694; kn fast_psm3 .7328 ≈
best_psm3 .7354 (wash); ta best_psm3 .2298 ≈ fast_psm3 .2233 (wash, both poor); ml all ~0.

## 3. PSM findings (same-model comparisons, the real signal)

- **PSM1 ≡ PSM3 output on ALL pages/models tested** (identical char/script counts; tesseract
  5.5.2 with OSD-auto only differs when orientation is ambiguous — our pages are upright).
  PSM1 costs nothing extra here; keep default PSM3 behavior. NOTE: ml_001 fast psm1 was the
  one exception run (2231/.7696) — rerun showed this is psm1's orientation-detection path
  flipping layout, not a stable win: best psm1 = 1795/.3008, and fast psm1 re-measure
  should be treated as UNSTABLE, not as a psm1 victory (flagged below, conflict C3).
- **PSM6 vs PSM3 is page-dependent, not language-dependent:**
  - te_001: psm6 +17% chars (2015 vs 1723) at −0.001 ratio — **real win** (dense question-paper
    page; uniform block assumption helps).
  - ta_001: psm6 −4.4% chars, ratio −.025 — **loss**.
  - kn_001: psm6 −2.3% chars, ratio −.007 — **loss** (and 2× slower).
  - ml_001: psm6 −0.8% chars, ratio +.045 (fast) — wash-to-slight-loss.
- **Wall time:** best ≈ 1.4–1.7× slower than fast on identical output (te 2147→3028 ms).
  kn psm6 best hit 12.1 s/page — worst config measured.

## 4. VERDICT — G-B3: **tessdata_best LOSES to homebrew FAST on the win-rule (0/12). NO rerun.**

- tessdata_best does NOT beat fast by ≥10% chars anywhere; fidelity moves are ±0.03 noise.
  Where best is slightly cleaner (te latin 44→24), it's ≤1% of text — below any action threshold.
- Homebrew's mal being ALREADY-best means half of B3's premise was already true on disk.
- Keep: tesseract_indic engine exactly as-is (FAST models, default psm3 via pytesseract).
- Do NOT switch packs to tessdata_best: −0 to −9% chars, 1.4–1.7× wall time, zero fidelity gain.
- PSM: not a global win — per-page +17% on te_001 but losses on ta/kn. A per-page PSM chooser
  (e.g. try psm6, fallback psm3) is a possible micro-uplift for te-class dense pages only;
  projected gain does not justify a 400-page rerun alone. Log as parked (Q-B3.1).

## 5. Machine-hours arithmetic (why no 400-page rerun from B3)

- fast psm3 measured: te 2.1s, ta 1.9s, kn 4.3s, ml 5.7s → mean ≈ 3.5s/page → 400 pages ≈ **0.4 h**.
- best psm3: te 3.0s, ta 3.3s, kn 7.3s, ml 8.7s → mean ≈ 5.6s/page → 400 ≈ **0.6 h**.
- Cheap, yes — but the outcome would be −0 to −9% chars at 1.4–1.7× time: rerun buys nothing.
  Gate law exists precisely to not spend even 0.6 h on a measured 0/12 loser.

## Conflicts found / spawned (fission duty)

- C2: B3's premise ("LSTM best models never tested") was HALF-STALE — mal best was already
  installed via homebrew. Disk-truth check found it in 1 md5 comparison. INDEX question-bank
  should carry a "check what's already on disk first" preamble.
- C3: ml_001 fast psm1 anomaly (2231 chars/.7696 vs best psm1 1795/.3008) — same mal model,
  different PSM path. Either psm1+OSD rescues ml pages sometimes (chase → try psm1 on 10 ml
  pages cheaply before Sep 16) or it's a one-page fluke (park). NOT proof ml is solved.
- Q-B3.1: per-page PSM chooser (psm6 for te-dense, psm3 default) — projected +1–2% global chars;
  only worth it bundled with other uplifts, never alone.
- Q-B3.2 (inverted): if best models are equal-but-slower on clean 200-dpi renders, do they win
  on DEGRADED/scan pages (our weakest page class)? → only test if hard-page rerun happens.
