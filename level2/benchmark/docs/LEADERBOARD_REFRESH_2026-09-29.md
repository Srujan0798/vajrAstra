<!--
🟡 W6 PAUSE BANNER (Miss agent, 2026-09-29 IST, per user directive)

All W6 fine-tuning prep is PAUSED. Not started.
Vinay meeting TOMORROW (2026-09-30) = gating step.
Vinay → W5 freeze after Wed 2026-10-01 → W6 training decision.

DO NOT execute training, mlx-tune, mlx_vlm, or QLoRA scripts from this file.
This file is preserved as W5-strategy evidence + post-meeting W6 reactivation reference.
After Vinay meeting: if Option A approved → resume scaffold per this file.
If Option B → wrap-only ships; this file remains archival.
If Option C → backbone swap; this file is superseded; new spec required.

Refs: VINAY_MEETING_PACKET.md · STRATEGY_VINAY_TOMORROW.md · VINAY_CTA.md ·
      W5_STRATEGY_OPTIONS.md · W5_BEAT_SARVAM_PLAN.md ·
      OCR_AGENT_MEMORY_FEED.md §15-§16 · BOSS_CONCERNS.md items 53+

Hard law: §9 no downloads + §8 no training until W5 freeze + Vinay gate ahead of W5 freeze.
-->

> 🟡 **STATUS: PAUSED** — Created 2026-09-29 BEFORE W5 freeze. NOT AUTHORIZED.
> Per OCR_AGENT_MEMORY_FEED.md §8: "Training" is forbidden until W5 freeze.
> This file is a DRAFT for review at W5 freeze (after Wed 2026-10-01), not executable.
> Vinay meeting tomorrow is the gating step.

# Probe22 Final Leaderboard — 2026-09-29 (Engine refresh, W6 freeze prep)

**Disk-locked, this is the engine agent's wrap-up view.** Counts from `level2/probe22/sheet.csv` (12,324 rows, 0 error packs, fill excluded per AGENT_PROTOCOL.md §6.2).

---

## K1–K3 Kill-Criteria Thresholds (defaults from Verdict, user-set at call)

| ID | Trigger | Default | User-set at call? | Source |
|---|---|---|---|---|
| **K1 (QLoRA)** | Kill QLoRA if no SAFE-lang McNemar-significant gap; QLoRA must close > T2 absolute CER points | T1 = **0.05** (McNemar exact p), T2 = **3 pp** | YES — confirm or change at freeze call | campaign §11 K1 |
| **K2 (micro-repair)** | sat/ks micro-repair (D4) kill threshold | **6 h** remaining before freeze + pages pass purge-era gates | YES — confirm | campaign §11 K2 |
| **K3 (routing drop)** | Wilson 95% CI upper bound > next-best engine's point estimate → drop engine from final routing | (always on); Wilson α = 0.05 | YES — confirm | campaign §11 K3 |
| **n<50 power rule** | No per-language winner claims for n<50 cells (as 19, gu 24, doi 27, mni 20, sat 20, ne 37) | (always on) | YES — confirm | AGENT_PROTOCOL.md §6.7 |

**Status:** defaults in place; user has not yet set at the freeze call. Wrap-only ships regardless. QLoRA scaffold waits for these to be set + install approval.

---

## W6 Path Block — FEASIBLE NOW / FEASIBLE IF / INFEASIBLE

### FEASIBLE NOW (zero user gate after freeze)

| Item | Disk evidence | Owner |
|---|---|---|
| **Wrap-only pipeline** (D1 stage-1 baseline) | 12,324 sheet rows / 11 engines / 0 errors / per-script routing table (§3) | Engine |
| Per-engine kill from final routing via K3 Wilson CI | Wilson 95% CI computed per (engine × language); always on | Verdict (decision) |
| Sarvam API baseline reference (54 calls + EN column restored) | Already executed; 3/lang Indic + 30 EN items | Engine (run done) |

### FEASIBLE IF (gated on user approval)

| Item | Trigger |
|---|---|
| **Local QLoRA on SAFE langs** (kok + pa priority, or/mai marginal) | (a) Phase 6 McNemar p < T1 on at least one SAFE lang; (b) user approves `pip install mlx mlx-vlm` + `git clone https://github.com/ARahim3/mlx-tune.git && pip install -e .`; (c) `vm_stat` Pages free × page_size ≥ 3 GB after inactive reclamation at launch time. Tool plan: `level2/probe22/MLX_INSTALL_PLAN.md` |
| **W6 backbone download** (GLM-OCR 0.9B primary, Qwen2.5-VL-3B alt) | Separate explicit user yes (model weights = download too) |
| **sat/ks micro-repair** (D4, 5–10 curated pages each) | W5 time permits after freeze; pages pass purge-era gates (K2) |
| **20-item human spot-check** (D3) | Verdict runs packet; user reviews at call (gu_o005 first) |
| **Optional memory headroom increase** | User quits Chrome / Brave / WhatsApp manually (PIDs in `MEMORY_AUDIT.md` §3) — ~3.5 GB active freed |

### INFEASIBLE UNDER CURRENT RULES

| Item | Law | Reason |
|---|---|---|
| Cloud GPU rental | §0 hard rule 1 + standing no-money law | No budget, no approval |
| New backbone invention | §9 hard rule | Architecture research is locked |
| Fine-tune on barred langs (ks, mni, ur, sat, mr, ne PDF-tier) | §6.4 LOCKED + D4 | Garbage-GT or no signal |
| sarvam_fill GT in SFT/RLVR | §9 hard rule | Machine GT, never training data |
| Paid API runs beyond 54-call cap + EN column | D2 + §6.8 | Already at cap; EN column restored from disk (see §1) |

---

## QLoRA Top-2 (D1 priority, post-gate)

### **#1 — kok (HIGH)** — QLoRA primary target

| Metric | Value | Source |
|---|---|---|
| Script | Devanagari | §3.1 |
| n | 100 | manifest |
| surya CER (best local) | **0.4285** | §4 |
| Best non-surya CER | 0.7522 (rapidocr) | §4 |
| Gap | **0.32 (32 pp)** | derived |
| QLoRA engine target | tesseract-family or rapidocr (NOT surya — already strong) | §4 |
| Verdict at K1 (T1=0.05, T2=3pp) | needs Phase 6 McNemar p < 0.05 to advance | campaign §11 |
| Status | scaffold ready; install pending user approval | this session |

### **#2 — pa (HIGH)** — QLoRA second target

| Metric | Value | Source |
|---|---|---|
| Script | Gurmukhi | §3.4 |
| n | 100 | manifest |
| surya CER (best local) | **0.1373** | §4 |
| Best non-surya CER | 0.2159 (tesseract-family) | §4 |
| Gap | **0.079 (8 pp)** | derived |
| QLoRA engine target | tesseract-family | §4 |
| Verdict at K1 (T1=0.05, T2=3pp) | needs Phase 6 McNemar p < 0.05 to advance | campaign §11 |
| Status | scaffold ready; install pending user approval | this session |

### KILLED at K1 (D1 default)

- **mai (LOW)** — gap 0.008 (below T2=3pp); no QLoRA needed
- **or (MARGINAL)** — gap 0.029 (near T2=3pp); defer unless kok/pa advance

---

**DECISION ANCHORS — this file is the source of truth for these decisions:**
- **D1 (QLoRA on SAFE langs):** QLoRA top-2 above + K1 thresholds; mai + or KILLED by K1 default.
- **D5 (Sarvam full-run for "Beat 87.39"):** headline ranking §1 row `sarvam_vision` (3/lang cap = 54 packs; OBITUARY-DEAD per §9.2; directional only — do not present as head-to-head).
- **D2/D4 (EN sanity):** §1 EN sanity column (surya 0.1514 / **sarvam 0.1078** / rapidocr 1.0 / paddleocr_indic 0.2495 / anuvaad 1.0 / openbharatocr NOT_PRESENT family-overlap).

**Standing warning at the top of every future use:**

> **Engine overlap — treat as ONE engine for routing decisions:** tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on **340/1313 packs** (preds byte-identical; metrics differ ≤0.002 — rounding only). The trio collapses to a single "tesseract-family" recognizer where native-script coverage coincides (sat 20/20, mni 20/20, ur 58/100, pa 59/100, or 54/69, en 30/30). On the 11-engine leaderboard the nominal count is 11, the **effective engine count is 9**. This affects QLoRA feasibility math (a "fine-tune one engine" win is meaningless if the chosen engine is one of the three) and any ranking claim.

> **McNemar methodology (this file's §4 + §5 ranking):** all engine-comparison significance is from McNemar exact test on per-item CER vs wrap baseline at `cer_threshold = 0.5` (binary pass/fail per pack). Source: `level2/probe22/scores/mcnemar_full_matrix.json` `meta.cer_threshold`. Means a "winner" is a lang where the winning engine passes 0.5 on more packs than the loser — not a continuous CER-delta test.

> **OL CHIKI total capability gap (rerun of campaign §11):** surya 0.61 (worst than expected), indicphotoocr 0.50 (best local), sarvam_vision 0.41 (3/lang). Zero engines below 0.49. The Sat 53.91 weak cell has no good local answer. QLoRA on sat would need Ol Chiki-aware synth (R3_OLCHIKI_MAYEK_SYNTHETIC), not a vanilla mlx-tune run.

---

## 1. Per-engine CER (overall, fill excluded, sheet.csv)

| engine | n | mean CER | median CER | EN sanity CER | EN sanity WER | WER-rank-class | role |
|---|---|---|---|---|---|---|---|
| **sarvam_vision** | 54 | 0.2640 ±0.30pp | 0.1642 | **0.1078** | 0.2459 | — | bench target, NOT pipeline (capped 3/lang, Wilson 95% CI half-width >50pp on n=3 cells; directional only) |
| **surya** | 1,227 | 0.3944 | **0.3058** | 0.1514 | 0.2601 | tier-1 | primary local |
| tesseract_bilingual | 1,227 | 0.4907 | 0.4891 | 0.8077 | 0.9853 | tier-2 | family ≡ tesseract_indic |
| tesseract_indic | 1,227 | 0.4918 | 0.4779 | 0.8077 | 0.9853 | tier-2 | ≡ tesseract_bilingual ≡ openbharatocr (340/1313) |
| openbharatocr | 1,227 | 0.4918 | 0.4779 | n/a (family-overlap with tesseract; not separately scored) | n/a | tier-2 | ≡ tesseract_bilingual ≡ tesseract_indic |
| easyocr | 1,227 | 0.5013 | 0.5987 | 0.6036 | 0.9788 | tier-3 | script-family router |
| indicphotoocr | 1,227 | 0.5634 | 0.5558 | 0.6710 | 0.9433 | tier-3 | Sat / Bengali-assamese specialist |
| paddleocr_indic | 1,227 | 0.6629 | 0.9241 | 0.2495 | 0.4966 | tier-3 | Devanagari only — most honest-empties |
| rapidocr | 1,227 | 0.6753 | 0.7577 | 1.0000 | 1.0000 | tier-3 | fast Devanagari/Perso-Arabic only |
| anuvaad_tesseract | 1,227 | 0.7153 | 1.0000 | 1.0000 | 1.0000 | tier-4 | Devanagari-only — many honest-empties |
| doctr | 1,227 | 0.8704 | 0.8708 | 0.3957 | 0.8445 | tier-4 | Latin only, no Indic language models |

> **EN sanity column** is the harness-sanity reference (30 EN human pairs, separate manifest at `level2/probe22/en_sanity/manifest.json`). Source: `metrics_<engine>_en_normalized.json` `avg_metrics.cer`/`wer`. EN CER > 5% on these noisy old scans = expected (test images are 3120×4160 noisy, not clean synthetic; see `transfer_obituaries.md`). The ranking still holds: **sarvam 0.1078** wins on the cap-restored EN column; **surya 0.1514** is the best local English; rapidocr + anuvaad are honest-empty on EN (no English model cached).

> **Caveat:** sarvam 54 rows is the credit-capped subset (3/lang). Other engines' means/medians are the full 1,227 basis. Sarvam is the **benchmark target**, not a pipeline component — its lower number is structural (small sample, hand-picked subset) and not directly comparable. Per AGENT_PROTOCOL.md §6.8: "Without a user-funded full Sarvam API run, 'beat 87.39' stays directional — never present it as a head-to-head number."

---

## 2. W6 path feasibility (D1, campaign §11 FEASIBLE-NOW/FEASIBLE-IF/INFEASIBLE)

| Item | Verdict | Disk evidence | Decision it changes |
|---|---|---|---|
| Wrap-only pipeline (§6.2 tier routing + restoration) | **FEASIBLE NOW** | surya = 0.31 median across 1,227 items; DELIVERABLE before freeze; zero GPU cost | D1 baseline |
| Engine routing table (this file §3) | **FEASIBLE NOW** | per-script CER measured per language, locked | D1 routing default |
| Local QLoRA on SAFE langs (kok/mai/or/pa) | **FEASIBLE IF** | (a) Phase 6 McNemar-significant gap (T1=0.05 default); (b) **laptop memory VERIFIED at call time** via `mlx-tune memory-check` or `python -c "import mlx.core as mx; print(mx.metal.get_peak_memory())"` (peak budget ≤24GB on M2 Max 32GB unified RAM + swap); (c) user-approved install of mlx-tune + mlx-vlm. **mai has the biggest gap (surya 0.028 vs tesseract 0.057; 3-pt close unlikely from fine-tune alone — QLoRA marginal there)** | D1 stage-2 |
| sat/ks micro-repair (D4) | **FEASIBLE IF** | W5 time permits; only sat/ks get 5-10 curated pages; freeze safety first | D4 |
| Sarvam EN column | **INFEASIBLE / moot** | D2 SKIPPED (no decision impact) | D2 closed |
| Cloud GPU (cloud spend, new backbone) | **INFEASIBLE UNDER CURRENT RULES** | no budget, no user approval, no §9 hard-rule exemption | D1 stage-3 |
| Fine-tune on barred langs (ks/mni/ur/sat/mr + ne PDF-tier) | **INFEASIBLE UNDER CURRENT RULES** | §6.4 BARRED list stands; compete via wrap | D4 stands |
| Train on sarvam_fill GT | **INFEASIBLE UNDER CURRENT RULES** | machine GT, never training data | §9 hard rule |

> **Decision link:** QLoRA spec will live at `level2/probe22/W6_QLORA_SPEC.md` once the **Verdict agent** writes it (Engine prep-only, per the boss's task split). The link below is a placeholder until Verdict lands.
> → **Verdict will own:** W6_QLORA_SPEC.md (kill criteria T1=0.05 McNemar, T2=3pt CER, user-set thresholds).
> → **Engine prep-only:** `level2/probe22/QLORA_READINESS.md` (this session — DISK gates, mlx-tune/mlx-vlm install gates PENDING_USER_APPROVAL).

---

## 3. Per-script routing (DISK truth)

Median CER per (script × engine), fill excluded. Winner per script in **bold**. Boss's stated routing recommendation is given for comparison — where it disagrees with disk truth the disk wins (the boss's note was a draft; this is the verification pass). **Column / row order: each sub-table is sorted by median CER ascending (best engine first). All sub-tables use the same engine-row order for cross-script comparability (surya-led Devanagari family first; barred-cell script families last with bolded engine winner).**

### 3.1 Devanagari (hi, mr, ne, sa, kok, mai, brx, doi) — n_rows = 6,124

| engine | median CER | n |
|---|---|---|
| **sarvam_vision** | 0.108 | 24 |
| **surya** | **0.173** | 610 |
| easyocr | 0.200 | 610 |
| tesseract_bilingual | 0.235 | 610 |
| paddleocr_indic | 0.235 | 610 |
| tesseract_indic | 0.255 | 610 |
| openbharatocr | 0.255 | 610 |
| anuvaad_tesseract | 0.328 | 610 |
| indicphotoocr | 0.402 | 610 |
| rapidocr | 0.476 | 610 |
| doctr | 0.861 | 610 |

→ **Primary: surya (0.173).** Boss recommendation "Devanagari=surya" ✓.

### 3.2 Perso-Arabic (ur, sd, ks) — n_rows = 2,759 (WER-primary per §6.3)

| engine | median CER | n |
|---|---|---|
| sarvam_vision | 0.565 | 9 |
| **surya** | **0.581** | 275 |
| easyocr | 0.667 | 275 |
| tesseract_indic | 0.772 | 275 |
| openbharatocr | 0.772 | 275 |
| tesseract_bilingual | 0.773 | 275 |
| rapidocr | 0.877 | 275 |
| paddleocr_indic | 0.900 | 275 |
| doctr | 0.915 | 275 |
| indicphotoocr | 0.927 | 275 |
| anuvaad_tesseract | 1.000 | 275 |

→ **Primary: surya (0.581).** Boss recommendation "Perso-Arabic=surya" ✓. Caveat: this is the worst-performing script family; even sarvam 0.565 on the cap is not great. WER-primary for ur/sd/ks (campaign §11 weak-cell attack on ks uses WER, not CER, per protocol §6.3). **§6.4 BARRED note:** ks + ur are BARRED from W6 fine-tune per §6.4 lock (ks visual 0/10 pass; ur 90% PDF-tier fail). McNemar `surya-wins-ks p<0.0006` is an engine-only comparison against garbage GT — NOT a "surya is best at ks" benchmark claim. The wrap-pipeline uses surya on ks by routing default; W6 SFT barred.

### 3.3 Bengali-Assamese (bn, as) — n_rows = 1,206

| engine | median CER | n |
|---|---|---|
| sarvam_vision | 0.050 | 6 |
| **surya** | **0.410** | 120 |
| indicphotoocr | 0.646 | 120 |
| easyocr | 0.656 | 120 |
| tesseract_bilingual | 0.848 | 120 |
| tesseract_indic | 0.851 | 120 |
| openbharatocr | 0.851 | 120 |
| doctr | 0.900 | 120 |
| rapidocr | 1.000 | 120 |
| anuvaad_tesseract | 1.000 | 120 |
| paddleocr_indic | 1.000 | 120 |

→ **Primary: surya (0.410).** Boss recommendation "Bengali=indicphotoocr" ✗ — surya wins on disk. Indicphotoocr 0.646 is the local fallback only when surya unavailable. **Note: this is only bn+as — there are no other Bengali-script items in the probe (mni uses Meitei, sat uses Ol Chiki).**

### 3.4 Gurmukhi (pa) — n_rows = 903

| engine | median CER | n |
|---|---|---|
| **surya** | **0.137** | 90 |
| sarvam_vision | 0.163 | 3 |
| tesseract_indic | 0.216 | 90 |
| openbharatocr | 0.216 | 90 |
| tesseract_bilingual | 0.216 | 90 |
| indicphotoocr | 0.239 | 90 |
| doctr | 0.783 | 90 |
| easyocr | 0.820 | 90 |
| rapidocr | 1.000 | 90 |
| anuvaad_tesseract | 1.000 | 90 |
| paddleocr_indic | 1.000 | 90 |

→ **Primary: surya (0.137).** Boss recommendation "Gurmukhi=tesseract-family" ✗ — surya wins on disk by 8 pts. Tesseract-family is the fallback only.

### 3.5 Odia (or) — n_rows = 693

| engine | median CER | n |
|---|---|---|
| **surya** | **0.195** | 69 |
| tesseract_indic | 0.224 | 69 |
| tesseract_bilingual | 0.224 | 69 |
| openbharatocr | 0.224 | 69 |
| sarvam_vision | 0.310 | 3 |
| indicphotoocr | 0.337 | 69 |
| easyocr | 0.809 | 69 |
| doctr | 0.810 | 69 |
| rapidocr | 1.000 | 69 |
| anuvaad_tesseract | 1.000 | 69 |
| paddleocr_indic | 1.000 | 69 |

→ **Primary: surya (0.195).** Boss recommendation "Odia=tesseract-family" ✗ — surya wins by 3 pts. Tesseract-family is fallback only. QLoRA candidate (D1 SAFE).

### 3.6 Gujarati (gu) — n_rows = 243 (VERIFY-FIRST)

| engine | median CER | n |
|---|---|---|
| **surya** | **0.111** | 24 |
| tesseract_indic | 0.214 | 24 |
| tesseract_bilingual | 0.214 | 24 |
| openbharatocr | 0.214 | 24 |
| sarvam_vision | 0.222 | 3 |
| indicphotoocr | 0.226 | 24 |
| easyocr | 0.813 | 24 |
| doctr | 0.834 | 24 |
| rapidocr | 1.000 | 24 |
| anuvaad_tesseract | 1.000 | 24 |
| paddleocr_indic | 1.000 | 24 |

→ **Primary: surya (0.111).** VERIFY-FIRST pending §6.2 (D3 spot-check gu_o005 first at call).

### 3.7 Ol Chiki (sat) — n_rows = 193 (BARRED, weak cell 53.91)

| engine | median CER | n |
|---|---|---|
| sarvam_vision | 0.405 | 3 |
| **indicphotoocr** | **0.504** | 19 |
| surya | 0.613 | 19 |
| doctr | 0.840 | 19 |
| tesseract_indic | 0.840 | 19 |
| tesseract_bilingual | 0.840 | 19 |
| openbharatocr | 0.840 | 19 |
| easyocr | 0.856 | 19 |
| rapidocr | 1.000 | 19 |
| anuvaad_tesseract | 1.000 | 19 |
| paddleocr_indic | 1.000 | 19 |

→ **Primary: indicphotoocr (0.504).** BARRED — no W6 fine-tune on sat. D4 micro-repair option (5-10 pages) is the only local lever. Vision-LLM-only or W6 fine-tune target otherwise.

### 3.8 Meitei-Mayek (mni) — n_rows = 203 (BARRED)

| engine | median CER | n |
|---|---|---|
| sarvam_vision | 0.022 | 3 |
| tesseract_indic | 0.855 | 20 |
| tesseract_bilingual | 0.855 | 20 |
| openbharatocr | 0.855 | 20 |
| indicphotoocr | 0.915 | 20 |
| easyocr | 0.916 | 20 |
| doctr | 0.953 | 20 |
| rapidocr | 1.000 | 20 |
| anuvaad_tesseract | 1.000 | 20 |
| paddleocr_indic | 1.000 | 20 |
| surya | 1.000 | 20 |

→ **Primary: sarvam (0.022 on cap).** No local engine below 0.86. n=20 — small-cell, no winner claim (§6.7). BARRED — no W6 fine-tune on mni.

---

## 4. SAFE languages — QLoRA candidates (D1, n≥50)

| lang | script | n | surya CER | best non-surya CER | gap (best non-surya − surya) | QLoRA marginal? |
|---|---|---|---|---|---|---|
| **kok** | Devanagari | 100 | **0.4285** | 0.7522 (rapidocr) | 0.32 | **HIGH** — surya wins by 32 pts, fine-tune on a different engine COULD close; but surya itself would not benefit from QLoRA (it's already a strong general model). The right target is **fine-tuning tesseract-family or rapidocr** on kok to close the gap to surya. |
| **mai** | Devanagari | 100 | **0.0280** | 0.0362 (easyocr) | 0.008 | **LOW** — surya + all engines already below 0.10; 3-pt CER gain T2=0.03 default won't be hit. QLoRA not needed. |
| **or** | Odia | 69 | **0.1950** | 0.2241 (tesseract-family) | 0.029 | **MARGINAL** — gap near T2=0.03. Fine-tune tesseract-family on or might reach surya; but surya is the primary anyway. Marginal case for kill-criteria T1=0.05 McNemar (not yet computed). |
| **pa** | Gurmukhi | 100 | **0.1373** | 0.2159 (tesseract-family) | 0.079 | **HIGH** — surya beats tesseract-family by 8 pts; fine-tuning tesseract-family on pa could plausibly close. Realistic QLoRA candidate. |

→ **QLoRA priorities (D1, after Phase 6 McNemar + kill criteria T1=0.05):**
1. **kok (HIGH)** — biggest gap, strongest QLoRA leverage. Engine target: tesseract-family or rapidocr (NOT surya). mlx-tune + mlx-vlm pipeline.
2. **pa (HIGH)** — second-biggest gap, Gurmukhi-specific. Engine target: tesseract-family.
3. **or (MARGINAL)** — gap near threshold; defer unless Pa/Kok show promise.
4. **mai (LOW)** — kill at the McNemar gate; gap too small to justify QLoRA.

---

## 5. Routing recommendations (this session's verified version — supersedes boss's draft)

| script family | primary | fallback 1 | fallback 2 | barred/cap notes |
|---|---|---|---|---|
| Devanagari (hi/mr/ne/sa/kok/mai/brx/doi) | **surya** | easyocr (Devanagari subset) | tesseract-family (when surya down) | ne PDF-tier barred from SFT |
| Perso-Arabic (ur/sd/ks) | **surya** (WER-primary) | easyocr (Urdu charset cached) | rapidocr (ks Nastaliq partial) | all BARRED — no W6 fine-tune |
| Bengali-Assamese (bn/as) | **surya** | indicphotoocr | easyocr (bn.pth cached) | as is fill-only (19 items); no per-language winner claim |
| Gurmukhi (pa) | **surya** | tesseract-family | indicphotoocr | SAFE (QLoRA candidate per §4) |
| Odia (or) | **surya** | tesseract-family | indicphotoocr | SAFE (QLoRA candidate per §4) |
| Gujarati (gu) | **surya** | tesseract-family | indicphotoocr | VERIFY-FIRST (D3 spot-check) |
| Ol Chiki (sat) | **indicphotoocr** | surya | — | BARRED — D4 micro-repair only |
| Meitei-Mayek (mni) | sarvam (cap) | none local | — | BARRED — n=20 no winner claim |

> **Boss's draft routing was 3/5 wrong vs disk truth:** Bengali=indicphotoocr (surya wins), Gurmukhi=tesseract-family (surya wins by 8 pts), Odia=tesseract-family (surya wins by 3 pts). Devanagari=surya ✓, Perso-Arabic=surya ✓. The "primary engine" answer is **surya everywhere we have it** (surya is primary on 13/18 probe langs; of 13 langs with n≥50 power for winner claims per §6.7, surya wins 9 — bn/brx/hi/kok/ks/mai/pa/sd/ur; mr + or are tesseract-family winners; sat + mni are barred per §6.4), with tesseract-family as the fallback for the Devanagari/Odia/Gurmukhi cells where it comes within 8 pts of surya. Indicphotoocr's niche is **only Ol Chiki (sat)**.

---

## 6. Integrity check (locked)

- 11 engines, **0 error packs** each (verified pack-by-pack `error is null`)
- 1,227 scored items per engine (sarvam 54 by cap, correct)
- 12,324 total scored rows in sheet.csv ✓ matches boss prompt spec
- Manifest: **1,283 items** (mr/pa/sd re-sourced to 100); 56 new items not yet in any engine's packs (only 13 surya packs on sd reach past sd_o187)
- sheet.csv frozen at 12,324-row baseline; engine reruns on the 56 new items deferred to W6 freeze call
- Engine overlap warning: tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on **340/1313 packs** (38 sat, 60 mni, 58 ur, 59 pa, 54 or, 30 en) — preds byte-identical; metrics differ ≤0.002 (rounding only); not separate engines for routing purposes
- Sarvam Vision 2.1 = bench target, NOT pipeline. NEVER routed to.

---

## 7. What this file is NOT

- Not the **South-400** leaderboard (that lives at `level2/reports/LEADERBOARD.md`, SEALED, kn/ml/ta/te only).
- Not the **W6_QLORA_SPEC** (Verdict agent owns that file, kill criteria T1/T2 user-set; Engine prep-only at `level2/probe22/QLORA_READINESS.md`).
- Not the **gt_verification.json** lock (§6.4 visual verdicts — locked 2026-09-27 04:55, owned by Verdict).
- Not the **CALL_PACKET.md** (Miss agent's pre-call packet at `docs/research/level7/CALL_PACKET.md`).

This file is the **engine-side final view** for the validation call, frozen at this disk state. Anything that changes engines, manifest, or Phase 6 numbers must move through the standard fix-loop (Verdict → Miss) and re-emit.