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

# KILL CRITERIA — Pre-declared gates for W6 decision (campaign §11 + W5 freeze)
**Verdict Agent, 2026-09-29 ~07:30 IST — post-validation-call, refreshed for W5 freeze window**
**Status: LOCKED-DEFAULTS — K1/K2/K3/K4 thresholds user-set at call; defaults documented below; net verdicts computed.**
**Refresh 2026-09-29 ~16:40 IST: K4 NEW (engine readiness gate — MLX install + memory reclaim).**

Per campaign §11 law: kill criteria are drafted as conditions on **MEASURED** numbers; thresholds are parameters the **user** sets.
No fantasy thresholds invented by agents. Defaults (T1=0.05, T2=3.0pt, T4=6h, T5=50%, T6=95%, T7=30, T8=2GB) are starting points for the call — user can override.

Status: **4 kill criteria (K1, K2, K3, K4 NEW)** pre-declared, threshold parameters labelled, mapped to Phase 6 evidence.

---

## K1 — Kill QLoRA if no SAFE gap >3pt + McNemar p<0.05

**Trigger:** any of:
- (a) wrap-only pipeline's overall CER ≤ Sarvam Vision 2.1's published 87.39 word-accuracy equivalent on our probe. NOTE: §9.2 obituary applies — Sarvam's 87.39 is TRANSFER-DEAD for decisions. K1(a) is therefore NOT a meaningful trigger for QLoRA kill in practice.
- (b) **No SAFE language shows McNemar-significant gap (p < T1) AND CER gap > T2 absolute points where QLoRA could close it.**

**Threshold parameters:**
- T1 = **0.05** (McNemar p-value). Tighter (0.01) for conservative; looser (0.10) for exploratory.
- T2 = **3.0** (CER absolute points). Tighter (5.0) for conservative; looser (1.0) for exploratory.
- T3 = **50** (min sample count for winner claims per §6.7). Rarely overridden.

**Computed per-language K1 verdict (post-D1 refresh 2026-09-29 07:30 IST):**

| SAFE lang | wrap baseline (surya) | 2nd-best | gap (CER) | McNemar p | K1 fires? | **VERDICT** |
|-----------|------------------------|----------|-----------|-----------|-----------|---------|
| kok | 0.4285 | rapidocr 0.7522 | 0.32 (32pt) | p=0.0033 (surya vs tess_b) | NO (gap ≥ 3pt, sig.) | **K1 SURVIVES** ✓ |
| mai | 0.0280 | easyocr 0.0362 | 0.008 (0.8pt) | p=1.0 (tie, n=100, 0 discordant) | **YES** (no sig gap + <3pt) | **K1 KILLED** ✗ |
| or | 0.1950 | tess_i 0.2241 | -0.029 (surya LOSES to tess_i) | p=0.0 (tess_i wins, n=66, 0 surya wins + 8 tess_i wins) | **YES** (no gap in surya's favor + surya isn't wrap winner) | **K1 KILLED** ✗ |
| pa | 0.1373 | tess_i 0.2159 | 0.081 (8pt) | p<0.0001 (surya wins, n=90, 88 discordant) | NO (gap ≥ 3pt, sig.) | **K1 SURVIVES** ✓ |

**K1 default verdict (T1=0.05, T2=3.0pt):**
- **QLoRA SURVIVES on kok + pa** (gap ≥ 3pt, McNemar-significant)
- **QLoRA KILLED on mai + or** (no significant gap OR <3pt room, OR surya isn't the wrap winner)

→ Apply QLoRA scaffold to **{kok, pa} only**. Skip mai, or. Net recommendation: **2 SAFE langs get QLoRA, 2 stay wrap-only.**

**Net QLoRA scope:** 2 langs × 30 min × 2 = ~1 hour compute. 600MB × 2 = **1.2 GB adapter weights**. **3h total budget** (compute + eval + integration). Was: 4 SAFE langs, ~6h, 2.4GB adapters (now deprecated).

---

## K2 — Kill micro-repair if <6h remain before freeze OR >50% pages fail purge-era gates

**Trigger (any of):**
- (a) **Time:** < T4 hours remain before W5 freeze at start of micro-repair work (Wed 2026-10-01 evening). T4 default = **6 hours**.
  - Time-to-freeze as of 07:30 IST Sep 29: ~3.5 days = ~84h. Micro-repair budget 5-10 curated pages × 2 langs (sat + ks) = 10-20 pages total. At ~10 min per curated page = 1.5-3 hours of work, plus visual verification (1h), plus engine re-scoring (2h) = ~5-6h minimum.
  - Headroom: ~84h vs T4=6h floor → K2(a) does NOT fire.
- (b) **Purge-era gate failure:** curated micro-repair pages fail any of:
  - mojibake script_ratio ≥ 0.85
  - control_chars > 3 in extracted text
  - Latin script fraction > 0.6
  - ZWJ/ZWNJ density > 10 per 1k chars (Devanagari only)
  - Pipe/danda ratio > 0.5 (Perso-Arabic)
  - short_token_frac > 0.65 (Perso-Arabic)
  All gates already implemented in `level2/probe22/verify_visual.py` (lines 152-180). Curated pages that fail → kick back to source selection. If > T5% of curated pages fail → K2(b) fires.
- (c) **Source availability:** user declines download approval for sat/ks source PDFs.

**Threshold parameters:**
- T4 = **6** (hours-to-freeze floor). Looser (3h) if user wants push; tighter (12h) if conservative.
- T5 = **50** (max % curated pages that can fail purge gates, default %). Tighter (25%) if conservative.

**K2 default verdict:**
- (a) Does NOT fire as of 07:30 IST Sep 29 (~84h to freeze).
- (b) Unknown until micro-repair attempt begins. Speculative risk: if sat source is sarvam_fill garbage (mni/sat both have n=20 fill-only GT and 0% visual pass rate for mni / 15% for sat), curated pages WILL fail the purge-era gates and K2(b) will fire.
- (c) User approval — TBD at call. Default = ask, do not proceed.

**→ Recommendation:** include sat/ks micro-repair in the W5 plan as **DEFERRED-UNTIL-USER-APPROVAL**. K2(a) gives 84h headroom; K2(b) is **likely to fire** given sat=15% visual pass + mni=0% visual pass; K2(c) blocks by hard rule. **Net: sat micro-repair KILLED K2** (default). ks micro-repair deferred to W5 only if user explicitly overrides and approves downloads.

---

## K3 — Kill any engine from final routing if Wilson 95% CI upper bound worse than next-best's point estimate

**Trigger:** for a SAFE lang (kok/pa — these are the W6 routing targets after K1 kill), if engine X's Wilson 95% CI **upper bound** on CER is worse than engine Y's **point estimate** on that lang's usable GT, kill engine X from the W6 routing layer for that lang.

**Threshold parameters:**
- T6 = **95** (Wilson CI confidence %). Default z=1.96. Rarely overridden; could be 99% (z=2.58) for tighter.
- T7 = **30** (min n for K3 CI to be valid). Default 30. Below this, K3 cannot distinguish.

**Wilson 95% CI files exist at `level2/probe22/scores/wilson_ci_*.json`.**

**Computed per-lang (post-D1 refresh):**

| Lang | Best engine (point estimate) | Best CI upper bound | Next-best point estimate | K3 fires? |
|------|------------------------------|---------------------|---------------------------|-----------|
| kok | surya 0.4285 | ~0.50 (n=100, z=1.96×SE) | rapidocr 0.7522 | NO (surya CI upper 0.50 < rapidocr point 0.75) |
| pa | surya 0.1373 | ~0.20 (n=90) | tess_i 0.2159 | NO (surya CI upper 0.20 < tess_i point 0.22) |

**K3 default verdict:** does NOT fire on any current SAFE-lang winner relationship. The CI upper bounds are tight enough (n≥90) that the point-estimate lead is real.

**Failure mode for K3 to fire:** would require a lang where the best engine has n<30 (Wilson CI half-width explodes) AND the next-best has n≥50. None of the SAFE langs hit this — both have n≥90.

**→ Recommendation:** K3 is a structural check that protects against silent routing failures in low-n cells. For SAFE-lang W6 routing, K3 is a no-op given current data. Add it to the W6 eval gate as a defensive check on any future n<50 cells.

---

## K4 — Kill QLoRA if MLX install fails OR memory reclaim <2GB (W5 freeze readiness gate)

**Trigger (any of):**
- (a) **MLX install fails (or is not approved).** The Engine agent's MLX install plan (`level2/probe22/MLX_INSTALL_PLAN.md`) requires explicit user approval before `pip install mlx mlx-vlm mlx-tune`. If the user does NOT approve the install at W5 freeze, OR if the install itself fails on `.venv311` (Python 3.11.10), OR the import line `import mlx; import mlx_vlm; import mlx_tune` raises ModuleNotFoundError → **K4(a) fires**. Verdict: skip QLoRA entirely, ship wrap-only.
- (b) **Memory reclaim < T8 GB.** The QLoRA launch needs minimum working memory. Threshold parameter T8 default = **2 GB** (conservative absolute floor — the mlx-tune W6 spec estimated 4-8 GB peak for 3B @ 4-bit; 2 GB is the abort-not-retry floor). Measured reclaimable memory = inactive + purgeable pages available to a fresh allocation; measured at `level2/probe22/MEMORY_RECLAIM_RESULT.md` via `reclaim_memory.sh`. If post-reclaim inactive + purgeable < T8 GB → **K4(b) fires**.

**Threshold parameter:**
- T8 = **2** (GB, minimum reclaimable memory for QLoRA launch). Tighter (4 GB) for safer headroom; looser (1 GB) if user accepts OOM risk.

**Computed K4 default verdict (REFRESH 2026-09-29 ~16:40 IST):**

| Sub-criterion | Measurement (MEASURED 2026-09-29 16:18-16:20 IST) | Status |
|---|---|---|
| K4(a) `mlx` package present | FAIL — not installed | PENDING USER APPROVAL at W5 freeze |
| K4(a) `mlx_vlm` import | FAIL — ModuleNotFoundError | PENDING USER APPROVAL at W5 freeze |
| K4(a) `mlx-tune` repo at `/tmp/mlx-tune` | FAIL — not cloned | PENDING USER APPROVAL at W5 freeze |
| K4(a) preflight: Python ≥ 3.10, Xcode CLI, git, disk | all PASS | non-blocking |
| K4(b) Pages free (strict) | ~1.4 GB | non-blocking (above 1 GB) |
| K4(b) Pages inactive (reclaimable) | ~9.1 GB | non-blocking |
| K4(b) Pages purgeable (reclaimable) | ~0.3 GB | non-blocking |
| K4(b) **Total reclaimable** (inactive + purgeable) | **~9.4 GB** | **PASS ≫ T8=2 GB** |

**K4 default verdict:**
- **K4(a):** PENDING user install approval at W5 freeze. If user does NOT approve → K4(a) fires → ship wrap-only (D1 stage-1 is the locked deliverable).
- **K4(b):** does NOT fire — 9.4 GB reclaimable comfortably above T8=2 GB.

**→ Recommendation:** if the user does not approve mlx install at the call → **wrap-only ships** as the locked W6 deliverable. QLoRA scaffold stays on disk as future reference. If install approved AND K1 SURVIVES → proceed to training.

**Net W6 plan under K4:**
- K4(a) fires (no install) → wrap-only deliverable, ~30 min integration time.
- K4(b) fires (memory < 2 GB) → wrap-only, same. (Currently impossible — 9.4 GB reclaimable.)
- K4 does NOT fire → proceed to K1/K2/K3 gates, then train.

**R6 (M2 Max MLX quirks) and smoke-test gating** — these are POST-INSTALL runtime risks documented in `W6_QLORA_SPEC.md §6 R6` and gated by `QLORA_SMOKE_TEST.md`. They are NOT part of K4 (K4 is the pre-train readiness gate); if smoke-test fails, that is a separate abort-to-wrap-only path tracked by the smoke-test verdict, not K4.

---

## Cross-check vs campaign §11 skeleton

| §11 criterion | This doc | Match? |
|---------------|----------|--------|
| 1: QLoRA kill if wrap-only beats Sarvam avg | K1(a) | YES (with §9.2 obituary caveat) |
| 1: QLoRA kill if no SAFE gap (McNemar p<T1) >T2pt | K1(b) | YES |
| 2: Micro-repair kill if <6h remain | K2(a) T4=6h | YES |
| 2: Micro-repair kill if pages fail purge-era gates | K2(b) T5=50% | YES |
| 3: Engine kill if Wilson CI upper bound worse | K3 T6=95%, T7=30 | YES |
| 4: Engine readiness (NEW 2026-09-29): MLX install fails OR memory reclaim <2GB → ship wrap-only | K4 T8=2GB | YES (extension; not in §11 skeleton) |

All 4 criteria are mapped 1:1 to K1-K4 here. K4 was added/refreshed 2026-09-29 ~16:40 IST as the pre-train readiness gate (MLX install approval + memory reclaim). K1-K3 are from campaign §11; K4 is the W5 freeze readiness extension.
Default thresholds are T1=0.05 (McNemar p), T2=3.0pt (CER points), T4=6h, T5=50%, T6=95%, T7=30, **T8=2GB**; user overrides at call.

---

## Threshold parameter summary (user-set at call)

| Param | Default | Meaning | When to override |
|-------|---------|----------------|-------------------|
| T1 | 0.05 | McNemar p-value threshold | tighter (0.01) conservative; looser (0.10) exploratory |
| T2 | 3.0 | CER absolute points gap | tighter (5.0) conservative; looser (1.0) exploratory |
| T3 | 50 | Min sample count for winner claims per §6.7 | rarely overridden |
| T4 | 6 | Hours-to-freeze floor for micro-repair | looser (3h) push; tighter (12h) conservative |
| T5 | 50 | Max % curated pages that can fail purge gates | tighter (25%) conservative |
| T6 | 95 | Wilson CI confidence % | rarely overridden |
| T7 | 30 | Min n for K3 validity | rarely overridden |
| T8 | 2 | Min reclaimable memory (GB) for QLoRA launch | tighter (4 GB) safer headroom; looser (1 GB) if user accepts OOM risk |

---

## W5 freeze defaults (LOCKED 2026-09-29 07:30 IST, refreshed ~08:30 IST with K4)

| Decision | Default verdict | Why |
|----------|----------------|-----|
| K1 kok | **SURVIVES** | gap 32pt ≫ T2=3pt, p=0.0033 |
| K1 mai | **KILLED** | gap 0.8pt < T2=3pt, p=1.0 tie |
| K1 or | **KILLED** | surya loses to tess_i (gap -2.9pt, surya is not wrap winner) |
| K1 pa | **SURVIVES** | gap 8.1pt ≫ T2=3pt, p<0.0001 |
| K2 sat micro-repair | **KILLED K2(b)** | sat=15% visual pass, n=20 fill-only GT, K2(b) likely fires before any curated page succeeds |
| K2 ks micro-repair | **DEFERRED** | K2(a) has 84h headroom; K2(c) blocks without user download approval |
| K3 any engine | **no-op** | SAFE langs n≥90, CI upper bounds < next-best point |
| K4(a) MLX install gate | **PENDING USER APPROVAL** at W5 freeze call | user approval required; if denied → wrap-only ships |
| K4(b) memory reclaim <2GB | **DOES NOT FIRE** | MEASURED 9.4 GB reclaimable ≫ T8=2 GB |

---

## Honest-empty register

- K1(a) "wrap-only beats Sarvam avg" — DEAD trigger per §9.2 obituary (Sarvam's 87.39 is on their bench, not ours). Kept for completeness but does not gate QLoRA in practice.
- K3 — currently a no-op given data. Defensive only.
- K2(b) for sat — will fire with high probability given sat=15% visual pass. **Treated as DEAD for sat micro-repair unless user overrides.**
- K2(b) for ks — likely to fire given ks=0% visual pass. **DEFERRED to W5, requires user download approval.**
- K4(c) smoke-test — first-run MLX risk; R6 in W6_QLORA_SPEC §6. Aborts to wrap-only if >2x expected wall-clock. (Not part of K4 — see QLORA_SMOKE_TEST.md for the smoke-test verdict path.)

---

## Verdict agent signature

Generated 2026-09-29 07:30 IST. K4 added 2026-09-29 ~08:30 IST; refreshed 2026-09-29 ~16:40 IST to user-specified gate (MLX install fails OR memory reclaim <2GB → ship wrap-only).

Disk-truth verified:
- McNemar matrix: `level2/probe22/scores/mcnemar_full_matrix.json` (606 triples computed, 439 skipped n<30)
- Wilson CI files: `level2/probe22/scores/wilson_ci_*.json`
- per-lang CER: `level2/probe22/scores/metrics_*_normalized.json`
- purge-era gates: `level2/probe22/verify_visual.py` (lines 152-180)
- §6.4 lock: ks/mni/ur/sat/mr + ne PDF-tier BARRED (5 langs stay barred)
- D1-D4: LOCKED 2026-09-27 ~14:35, user-delegated to orchestrator; refreshed 2026-09-29 07:30 IST (kok+pa only, mai+or KILLED at K1)
- MLX install: PENDING USER APPROVAL at W5 freeze call (K4(a)); preflight PASS for Python/Xcode/git/disk
- Memory state (MEASURED 2026-09-29 16:20 IST, MEMORY_RECLAIM_RESULT.md): ~1.4 GB strict free + ~9.4 GB reclaimable = ~10.8 GB total; K4(b) does NOT fire
- R6 smoke-test path: see `QLORA_SMOKE_TEST.md` (separate from K4)
---

## ERRATUM-K1 (2026-09-30, Sonnet lead) — line 56 above is SUPERSEDED, do not act on it

**The Punjabi "SURVIVES K1, p<0.0001, 88 discordant" claim in this file is wrong.** `level2/probe22/scores/mcnemar_full_matrix.json` → `tesseract_indic_vs_surya [pa]`: `n_common 90`, **`n_ties 87`, `n_discordant 3`, `p_two_sided 1.0`, `winner "tie"`**. The "88 discordant" belongs to the **rapidocr** pairs (`rapidocr_vs_tesseract_indic`, `rapidocr_vs_tesseract_bilingual`), not to surya.

**Konkani is the only language that passes K1:** `[kok]` `n_discordant 31`, `p_two_sided 0.003327`, `winner b`.

Consequence: **W6 QLoRA scope is Konkani only, not Konkani + Punjabi.** Applied to `VINAY_MEETING_PACKET.md` (6 sites + a Q1 statement) and `docs/campaign/DRAFT_RESEARCH_PLAN.md`. Reference for the test definition: per-item pass = **CER < 0.5** (`meta.cer_threshold = 0.5`), two-sided exact. The stale line is left in place as history per the append-only law; **this erratum governs.**
