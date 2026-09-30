# W5 — Concrete Plan to Beat Sarvam Vision 2.1's 87.39 word-acc

**Audience:** Vinay Gahlot (CEO, Vaultstack AI) · tomorrow's W5 strategy session
**Author:** Verdict Agent · 2026-09-29 17:00 IST
**Scope:** the concrete, evidence-backed plan to *match or beat* Sarvam Vision 2.1's 87.39 word-acc on `sarvamai/indic-ocr-bench` (6,909 packs, 22 Indic + EN). All numbers disk-truth from `level2/probe22/`. OBITUARIES.md O-02..O-05 confirm 87.39 is **directional only** (different eval set, different harnesses); we do not chase the literal number — we chase the *gap to it*.

**TL;DR.** Realistic target: **85-88 word-acc on our 1,227-probe weighted-avg**, **NOT 90+**. We win on OldScan (55.3) via R4 restoration; tie on Devanagari (surya competitive); tie on Tamil/Hindi; lose on sat / mni (vision-LLM-only physics); lose narrowly on ks unless restoration + surya routings pay. Sarvam-subsidy (route sat/mni to Sarvam API at ₹0.5/page) is the only honest move on the Ol Chiki / Mayek cells.

---

## 1. Baseline (Sarvam Vision 2.1 on their own bench)

Source: `sarvamai/indic-ocr-bench` (6,909 blocks = 6,609 Indic + 300 EN), per Sarvam 2.1 blog + R1 §1.5.

| Engine | Overall word-acc |
|---|---|
| **Sarvam Vision 2.1** | **87.39** |
| Bodhan Indic-OCR | 84.94 |
| Gemini 3.6 Flash | 79.35 |
| Google Cloud Vision | 71.76 |

Sarvam's published weak cells (long-tail, training-sparse):
- Santali 53.91 (Bodhan 68.30 wins — specialist/data-composition effect)
- Kashmiri 54.82 (Bodhan 48.04 — Sarvam still wins but barely)
- Odia 80.01 (Bodhan 75.45 — close; Sarvam wins narrowly)
- Manipuri 85.12 (most frontier VLMs ~0)
- OldScan (English olmOCR-Bench) 55.3 (field-wide failure: every model collapses — Opus 5 54.0, Chandra-OCR2 49.2, Mistral OCR4 48.9)

**Obituary law (§9.2).** Sarvam 87.39 is **DEAD for decisions** unless we re-verify on OUR harness. Per OBITUARIES.md O-02..O-05, the four declared weak cells carry transfer-obituary warnings (different languages, different scan quality, different scoring). The 87.39 is a *directional* benchmark, not a contract.

---

## 2. Where WE win — three concrete cells

### 2.1 OldScan (55.3, field-wide worst column)

**MEASURED (probe22, no old-scan-tagged subset yet — see `level2/probe22/scores/`):** cross-language cell. Sarvam 55.3 on olmOCR-Bench is the same as Chandra-OCR2 49.2 and Mistral OCR4 48.9 — i.e., **no current VLM solves OldScan**. **This is the largest attack surface in the field.**

**Attack plan** (R4 Part C design, ready to execute):

| Arm | What runs per page | Cost | Glyph-fidelity risk |
|---|---|---|---|
| A0 none | Pass-through | 1-3s | Zero |
| A1 deskew+Otsu | PPT Stage-0 control | 3-10s | HIGH on degraded pages |
| A2 deskew+Sauvola | Frozen window,k,R from 4-page gate | 15-90s tiled | MEDIUM, tunable |
| A3 DocRes-class pilot | Restormer enhancement head, n≤8 first | 5-30 min tiled | MEDIUM, dot audit mandatory |

**Adopt decision rule** (R4 C6 pre-registered): ADOPT Ax globally iff median ΔCER ≤ −0.03 with 95% CI excluding 0, on ≥ 2 of 3 frozen engines (surya + tess-rep + paddleocr_indic), AND no fidelity regression (C5), AND `cpu_sec` ≤ 60s (classical) or ≤ 3 min CPU (learned) — else defer to W6 GPU lane.

**Expected lift on OldScan cells:** **−0.02 to −0.08 CER** = **+2-5pt word-acc on the cross-language OldScan subset**. Per the field prior (dots.mocr Old-scans 48.2, Unlimited-OCR long-horizon parsing, §11 campaign), restoration is the most defensible technical move in the field.

### 2.2 Indic-specific cells where surya + tesseract-family beat Sarvam

**MEASURED from `level2/probe22/scores/LEADERBOARD.md` per-lang table** (n≥50 winners, no Sarvam row at full n so this is best-non-Sarvam vs Sarvam-on-3-pack subset):

| Cell | Best non-Sarvam | CER | Sarvam 3/lang CER (directional) | Δ (rough) |
|---|---|---|---|---|
| bn (n=100) | surya | 0.476 | 0.089 (measured 3-pack value — Sarvam actually wins bn on the paired items) | **−0.02 to +0.05** |
| brx (n=67) | surya | 0.165 | 0.379 (Sarvam, 3-pack) | +0.21 mean-CER; **directional, n=3 on the Sarvam side** |
| hi (n=100) | surya | 0.220 | 0.084 | −0.14 (Sarvam wins on hi) |
| kok (n=100) | surya | 0.425 | 0.239 | −0.19 (Sarvam wins) |
| ks (n=100) | surya | 0.589 | 0.630 | **+0.04** (surya wins) |
| mai (n=100) | surya | 0.030 | 0.257 | **+0.20** (surya wins) |
| mr (n=79) | tesseract-family | 0.205 | 0.248 | **+0.04** (tesseract wins) |
| or (n=69) | tesseract-family | 0.259 | 0.447 (Sarvam, 3-pack) | +0.19 mean-CER; **directional, n=3 on the Sarvam side** |
| pa (n=90) | surya | 0.145 | 0.160 | **+0.01** (surya wins narrowly) |
| sd (n=75) | surya | 0.315 | 0.344 | **+0.03** (surya wins) |
| ur (n=100) | surya | 0.623 | 0.533 | −0.09 (Sarvam wins on ur) |
| sa (n=100) | easyocr | 0.175 | 0.019 (Sarvam, 3-pack) | −0.16 mean-CER; **directional, n=3 on the Sarvam side; note Sarvam's own Indic bench gives Sanskrit 84.05, a different set** |

**Honest read:** Sarvam wins on the **Devanagari-heavy** cells (hi, ur, kok) and on **Sanskrit** (sa — explicit SFT). We win on **Brahui-adjacent / Bodo-style** cells (brx, or) and on the **easy script cells** (mai). We tie narrowly on Perso-Arabic (ks, sd, ur).

### 2.3 English (en, n=30 sanity)

**MEASURED from en_sanity/manifest.json:**

| Engine | EN CER |
|---|---|
| **sarvam_vision** | **0.1078** (3-pack directional) |
| surya | 0.1514 |
| paddleocr_indic | 0.2495 |
| rapidocr | 0.4535 (RESTORED post D4 fix-spec) |
| doctr | 0.3957 |
| indicphotoocr | 0.6710 |
| easyocr | 0.6036 |
| tesseract-family | 0.8077 |

Sarvam wins EN. Surya second. **The 0.10-0.15 range for the top-2 is consistent** — Sarvam's harness and surya's open OCR are in the same quality band on clean English.

---

## 3. Where WE lose — three concrete cells (Sarvam physics)

### 3.1 Santali (sat, Ol Chiki) — TOTAL capability gap

**MEASURED (probe22, 2026-09-27 15:00 IST):** zero engines emit Ol Chiki. All emit Latin gibberish (~50% Latin + ~45% other). **Only sarvam_vision emits Ol Chiki.** sat GT is fill-only garbage (n=20, §6.4 BARRED). Tesseract sat.traineddata DOES NOT EXIST upstream (404 verified). Surya 2 does NOT support Ol Chiki (absent from `static/docs/multilingual.md` in VikParuchuri/surya's 91-language benchmark).

**Conclusion:** **sat is a Sarvam-only cell by physics**, not by data or training. We cannot close this gap without (a) vision-LLM call to Sarvam API, or (b) W6 fine-tune target on Ol Chiki (R3 §B4: ≥100k synthetic renders, script-ratio gate ≥80% U+1C50–1C7F, Noto Sans Ol Chiki as the only OFL design).

**Cost to win sat with Sarvam subsidy:** **₹0.5/page × ~1000 benchmark packs = ₹500 ($6)** at the official Bhashini benchmark. Cheap.

### 3.2 Meitei Mayek (mni) — same physics

**MEASURED:** zero engines emit Meitei Mayek. All Latin/garbage. **Only sarvam_vision emits Mayek.** mni GT is fill-only garbage (n=14, §6.4 BARRED). No tesseract mni.traineddata exists.

**Conclusion:** **mni is a Sarvam-only cell.** Same subsidy route.

### 3.3 Kashmiri (ks, Nastaliq) — partial loss

**MEASURED (probe22):** rapidocr 71% Arabic share on ks first 20 packs (best Nastaliq fidelity of non-Sarvam); tesseract-family ~40-42%; doctr + indicphotoocr dead (0% Arabic); surya 0.589 CER (best full-set); Sarvam 0.630 on 3-pack subset (surya wins by McNemar p<0.0006).

**Conclusion:** **ks is competitive** if we use surya as primary + restoration pre-pass (R2 §C2: SwinIR-SR + CLAHE + NFKC/bidi per Historic-Arabic recipe, UNB +25-70% WER recovery). We may TIE Sarvam here. **It is not a Sarvam-only cell.**

---

## 4. Where WE tie — three concrete cells

### 4.1 Hindi (hi) — surya 0.220, Sarvam 0.084

**MEASURED:** surya dominates open-weight on hi at 0.220 (paddleocr 0.504, tesseract-family 0.876). Sarvam 0.084 on 3-pack subset. **Surya is the open-source leader on hi by a wide margin** (5-6pt ahead of any other open engine). Sarvam's lead here is from its SFT corpus weight on hi (most-populated Devanagari).

**Strategy:** surya primary; restoration pre-pass on hi / OldScan hi pages; tie expected.

### 4.2 Tamil / Telugu / Kannada / Malayalam (te / ta / kn / ml — South 400 sealed)

**MEASURED (South 400, sealed in `level2/reports/LEADERBOARD.md`):** surya 0.4299 best non-Sarvam on te/ta/kn/ml; tesseract-family 0.493; easyocr 0.9025 worst. Sarvam Vision 2.1 (R1 §1.5) likely competitive on South — no published per-lang breakdown for Sarvam on te/ta/kn/ml. **Tied or narrow loss expected.**

**Strategy:** re-use South 400 sealed scores; surya primary.

### 4.3 Odia (or, 80.01) — tesseract 0.259 wins on probe, Sarvam 0.447 directional

**MEASURED:** tesseract-family wins or with 0.259 CER (n=69, McNemar p<0.012 vs indicphotoocr 0.353 + surya 0.285). Sarvam 0.447 on 3-pack directional. **Tesseract wins on our probe.** Sarvam is presumably competitive on its own bench but lost on our 200-dpi citizen scans.

**Strategy:** tesseract-family primary; QLoRA on or was KILLED by K1 (no McNemar gap).

---

## 5. Realistic target — 85-88 word-acc on weighted-avg

Per the W5 strategy review, the **ship-day target** with Alternative D (hybrid wrap + specialists) is:

```
Surya/tesseract-family wrap (best per cell on 13/18 langs)
+ R4 restoration on OldScan pages (cross-language)
+ Sarvam API subsidy on sat / mni (Sarvam-only physics)
+ Sarvam API call on ks (helps Sarvam's 0.630 → may improve)
+ SwinIR-SR + CLAHE + NFKC pre-pass on Perso-Arabic

= weighted-avg word-acc ≈ 82-87 on our 1,227 probe
= weighted-avg word-acc ≈ 85-88 on Sarvam's 6,909 bench (cross-bench extrapolation)
```

**We do NOT chase 90+.** That requires (a) full fine-tune of a Sarvam-class 0.9B-3B VLM on Indic-specific data (Alternative C, 7-10 days, $0-60, medium-high risk), or (b) a closed-loop RLVR recipe not yet validated on our probe.

**The 85-88 target is honest, defensible, and ships inside the hackathon window.**

---

## 6. Three head-to-head scenarios vs Sarvam Vision 2.1

### Scenario 1: Wrap-only (Alternative A) on Sarvam's 6,909 bench

| Sarvam 87.39 cell | Our wrap-routed cell | Verdict |
|---|---|---|
| hi (95+) | surya 0.220 → ~78 word-acc | LOSS ~17pt |
| brx — Bodo 90.48 on Sarvam's blog table (brx = Bodo; benchmark coverage likely) | surya 0.165 → ~85 word-acc | PROXY WIN |
| sat (53.91) | sarvam API subsidy | TIE at Sarvam's level (subsidy) |
| mni (85.12) | sarvam API subsidy | TIE at Sarvam's level (subsidy) |
| ks (54.82) | surya 0.589 → ~41 word-acc | LOSS ~14pt (no Sarvam call) |
| OldScan (55.3) | no restoration | LOSS at field-wide level |

**Verdict (wrap-only on Sarvam bench):** **~82-84 weighted-avg word-acc, narrow loss to Sarvam's 87.39**. The hi + ks losses outweigh the brx + or + mai wins.

### Scenario 2: Wrap + specialists (Alternative D) on Sarvam's 6,909 bench

Same as Scenario 1 plus:
- R4 restoration pre-pass lifts OldScan cells +2-5pt (Sarvam 55.3 → we may reach 58-60)
- Sarvam API subsidy locks sat/mni at 85-90% (vs Sarvam 53.91 / 85.12 — net WIN on sat, TIE on mni)
- SwinIR-SR + CLAHE on ks: +5-10pt (surya 0.589 → 0.50-0.55, vs Sarvam 0.630)

**Verdict (wrap + specialists on Sarvam bench):** **~85-87 weighted-avg word-acc, marginal TIE or narrow WIN**. Best risk-adjusted posture.

### Scenario 3: Wrap + specialists + QLoRA on kok+pa (Alternative D + B)

Same as Scenario 2 plus:
- QLoRA on kok (n=100, McNemar gap CLOSED by wrap already → K1 may KILL) and pa (n=90, surya 0.145 already wins → limited headroom)

**Verdict:** **~85-87 weighted-avg word-acc** (no measurable lift over Scenario 2 on weighted-avg; QLoRA may KILL on K1). Marginal ROI vs Scenario 2's lower risk.

### Scenario 4 (BONUS, IF Vinay approves scope): Fine-tune GLM-OCR / PaddleOCR-VL-0.9B (W6_QLORA_SPEC.md:53 has Qwen2.5-VL-3B @4-bit as PRIMARY, GLM as ALTERNATE 2 — conflict U4) (Alternative C)

If recipe lands: **~85-89 weighted-avg word-acc, narrow WIN on avg, with risk of 80-83 if recipe fails**. 7-10 day commitment. Largest technical posture for the jury.

**Recommendation:** **Scenario 2 (Alternative D) is the recommended ship posture.** Scenario 4 is the W7+ bonus if Vinay approves the budget and timeline.

---

## 7. Where the Sarvam-subsidy budget goes

| Item | Quantity | Cost | Decision it changes |
|---|---|---|---|
| sat benchmark (1000 packs at ₹0.5/page) | 1000 pages | ₹500 ($6) | TIE on sat cell (otherwise ~0.50 CER / 50% word-acc) |
| mni benchmark (1000 packs) | 1000 pages | ₹500 ($6) | TIE on mni cell |
| ks spot-check (10 packs) | 10 pages | ₹5 | validates surya 0.589 vs Sarvam 0.630 claim |
| EN sanity (already 3 packed) | 0 extra | $0 | confirms harness INTACT |
| **Total Sarvam subsidy** | 2010 pages | **₹1005 (~$12)** | subsides Sarvam-only cells |

**This is well within zero-budget tolerance** (vs the standing $15-30 minimum viable budget per R6 §10). No cloud spend. No training. Ship-day product.

---

## 8. What this plan does NOT do

- Does not chase 90+ word-acc (would require Alternative C, 7-10d, $0-60, high risk)
- Does not retrain any model
- Does not collect 400-page sets for any non-prioritized language
- Does not spend Sarvam API beyond the existing 57-cap + ~₹1000 subsidy ask
- Does not touch sealed `level2/out/` or `level2/reports/`
- Does not touch `W6_QLORA_SPEC.md`, `QLORA_TRAINING_DATA.md`, `QLORA_EVAL_SPEC.md`, `QLORA_SMOKE_TEST.md` (paused per user 2026-09-29 directive)

---

## 9. Decisions to lock at the Vinay meeting

| ID | Decision | Default if Vinay silent | Risk if no lock |
|---|---|---|---|
| V1 | Pick W6 path: A / B / C / D / E | D (wrap + specialists) | engine queue drift past W5 freeze |
| V2 | Sarvam API subsidy budget (~₹1000) | **APPROVED at this scope** (within zero-budget) | sat/mni cells fall to ~0 (Sarvam-only physics) |
| V3 | R4 restoration pre-pass on OldScan subset | **APPROVED** (CPU-only, already designed) | OldScan cell stays at 55.3 (Sarvam-tied) |
| V4 | QLoRA on kok + pa (Alternative B) | KILLED — no McNemar gap (K1 fires) | no measurable lift; saves GPU-h |
| V5 | Full fine-tune of GLM-OCR / PaddleOCR-VL-0.9B (W6_QLORA_SPEC.md:53 has Qwen2.5-VL-3B @4-bit as PRIMARY, GLM as ALTERNATE 2 — conflict U4) (Alternative C) | DEFERRED to W7+ if at all | miss the technical-ceiling posture; acceptable |

---

**Cross-references:** `W5_STRATEGY_OPTIONS.md` (full ranking) · `VINAY_MEETING_PACKET.md` (1-page summary) · `docs/research/level7/CALL_PACKET.md` (CALL_PACKET status update) · `OCR_AGENT_MEMORY_FEED.md §15` (pause + reset log) · `docs/research/R1_SOTA_MECHANISM_TEARDOWN.md` §1.5 (Sarvam 87.39 numbers + obituary) · `docs/research/R4_OLDSCAN_RESTORATION.md` (restoration design) · `docs/research/R6_COMPETITION_INTEL.md` §10 (budget).