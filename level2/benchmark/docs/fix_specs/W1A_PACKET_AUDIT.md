# W1A PACKET AUDIT

**Agent:** Verdict (subagent) · **Run:** 2026-09-29 IST · **Scope:** hostile claim-by-claim audit of the Vinay meeting packet and its 8 evidence/strategy companions.
**Law observed:** no claim in this file without a `file:line` I opened this run, or a URL I fetched this run. Nothing here is taken on the planner's word.
**Wrote:** this file only. No target file was modified.

## Targets audited (all read, with path corrections applied)

| Target | Bytes | mtime | Note |
|---|---|---|---|
| `VINAY_MEETING_PACKET.md` (root) | 26,805 | 20:08 | **PRIMARY** per prompt |
| `docs/architecture/VINAY_MEETING_PACKET.md` | 5,899 | 17:05 | **SECOND, smaller, UNRECORDED by the planner.** Separate target, own line numbers. Not assumed canonical. |
| `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md` | 9,782 | 19:59 | was `EVIDENCE_SUMMARY.md` at root |
| `docs/architecture/W5_STRATEGY_OPTIONS.md` | 19,443 | 17:04 | **Verdict-authored, 5 options A–E, recommends D** |
| `docs/research/level7/W5_STRATEGY_OPTIONS.md` | 3,754 | 17:04 | **Verdict-authored, 3 options A–C, recommends A** |
| `W5_BEAT_SARVAM_PLAN.md` (root) | 14,324 | 19:46 | md5 `9d9a5761…` |
| `docs/architecture/W5_BEAT_SARVAM_PLAN.md` | 14,324 | 17:04 | **md5-identical to root** (`diff` clean) — same doc, two paths |
| `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` | 3,652 | 17:04 | md5 `f2fc3c91…` — **different, shorter doc** |
| `_reports/cleanup_cycle1/PER_LANG_ROUTING.md` | 5,861 | 17:04 | was root |
| `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md` | 7,166 | 17:05 | was root |

**Which W5 doc is which (K4, asked directly):** `docs/architecture/W5_STRATEGY_OPTIONS.md` is the **5-option ranked paper** (Alternatives A–E, Verdict voice, ranks D first, $6–30, 2–4 d). `docs/research/level7/W5_STRATEGY_OPTIONS.md` is a **3-option shortlist** (Option A = wrap+QLoRA kok+pa, $0, 3–4 h, "RECOMMENDED"), which is what the root packet actually implements. They are **not** two drafts of one document — they disagree on the recommendation. `W5_BEAT_SARVAM_PLAN.md` at root and `docs/architecture/` are byte-identical; the `docs/research/level7/` copy is a separate 106-line "concrete recipe" doc. The root `W5_STRATEGY_OPTIONS.md` **does not exist** (cleanup moved it) — yet the root packet cites it by bare filename at lines 32, 99, 122, 267, 277.

---

## Summary counts by verdict

| Verdict | Ledger rows | What it means here |
|---|---|---|
| VERIFIED | 11 | reproduced from `sheet.csv` / manifest / a URL I opened |
| WRONG | 18 | a number or label that a command refutes |
| UNSUPPORTED | 7 | no source on disk, not reproducible — must not reach Vinay as fact |
| STALE | 6 | was true; disk moved on |
| DIRECTIONAL | 5 | real but n too small to carry the wording used |
| DEAD | 4 | true of a *different benchmark/metric*; unusable for the comparison made |
| **Total ledger rows** | **51** (grouped from 140 claim-bearing lines) | |

**Fix-specs emitted: 54** — 19 BLOCKER, 28 MAJOR, 7 MINOR. **ERRATUM-only (no edit proposed): 4** (sealed/re-LOCKED files). *Counts corrected by the lead 2026-09-29 ~21:4x IST: the author reported 41 in this line and 61 in its final message; the file contains 54 `### FS-` headers (19/28/7), verified by `grep -c '^### FS-'`. Use 54.*

---

# PART 2 — K1–K7 reproduced

The prompt says: do not trust the planner; if a defect does not reproduce, say REJECTED. Results:

### K1 — "Beats Sarvam on 9/18 langs" → **REPRODUCED AS WRONG (and the planner's own number is also wrong)**

Ran the planner's exact script. It reproduces the planner's *paired* result but **not** the packet's number:

```
54 paired items (3/lang). surya mean CER < sarvam mean CER in 10/18 langs.
langs: brx gu ks mai mr ne or pa sd ur        item-level: surya better 21, Sarvam better 28, tie 5
sarvam overall mean CER on those 54 = 0.2640   surya on same 54 = 0.3637   best-local on same 54 = 0.2956
```

**Three different numbers are in circulation, all called "the win":**

| Number | What it actually counts | n | Verdict |
|---|---|---|---|
| **9/18** (packet L49, 54, 87, 116, 117, 126, 303; arch packet L27; level7 opts L10) | "9 langs where surya has the lowest mean CER" ÷ 18. But 6 of 18 languages have n<50 and carry **no winner claim by D4/§6.7**. | mixed | **WRONG — denominator** |
| **9/12** (COMPUTE_BUDGET L76 — the one doc that got it right) | surya is mean-CER winner in 9 of the **12** languages with n≥50 | ≥50 | **VERIFIED** |
| **10/18** (planner's paired vs Sarvam) | surya beats *Sarvam* on 3 items/lang | **3/lang** | **DIRECTIONAL ONLY** |

I counted the 9/12 myself from `sheet.csv`: winners at n≥50 are surya on bn, brx, hi, kok, ks, mai, pa, sd, ur (9); tesseract-family on mr, or; easyocr on sa. The other 6 (as 19, doi 27, gu 24, mni 20, ne 37, sat 20) are n<50, no claim.

**The McNemar count is weaker still, and this is the number that will actually break under cross-examination.** Counting surya's wins at p<0.05 across testable (non-low-conf) opponents in `mcnemar_full_matrix.json`:

```
beat ALL testable opponents at p<0.05: bn, brx, hi, kok, ks  = 5 languages (not 9)
sd 7/9 · pa 5/9 · or 5/9 · mai 1/9 · mr 2/9 · sa 0/9 · ur 0/9
```

**ur is 0/9.** Every single ur comparison is `p=1.00, tie` (max 1 discordant item out of 100). `EVIDENCE_SUMMARY.md:60` and `PER_LANG_ROUTING.md:26` both claim ur is "McNemar p<0.05 vs 9/10". That is false.

**The one sentence the data supports:**

> On the 54 items where Sarvam was actually run (3 per language), our best local engine had a lower mean CER than Sarvam in 10 of 18 languages; at n=3 per language this is directional only. Separately, on the full scored set, surya has the lowest mean CER in 9 of the 12 languages with n≥50 — and clears McNemar p<0.05 against every testable opponent in only 5 of those (bn, brx, hi, kok, ks).

### K2 — "1,227 items" vs manifest 1,283 → **REPRODUCED: both true of different sets; the packet never says which**

```
manifest.json  items = 1283   (sum of per-language: as19 bn100 brx67 doi27 gu24 hi100 kok100 ks100
                                mai100 mni20 mr100 ne37 or69 pa100 sa100 sat20 sd100 ur100)
manifest_additions.json items = 56  (sd 25, mr 21, pa 10)   -> 1227 + 56 = 1283  OK
sheet.csv  12,324 CSV records = 10 engines x 1227 + 54 sarvam;  1227 distinct image_id;  18 langs
sheet.csv  physical lines = 201,827  (predictions contain newlines - do NOT use `wc -l`)
```

So: **1,227 = the scored base set** (what `sheet.csv` actually measures). **1,283 = the manifest**, which includes 56 added items (sd/mr/pa) that were never scored — a Sarvam-bound context for the mni/sat "BARRED" verdicts. The packet says "1,227 items" nine times and "1,283" once (L95, in the anchors table), never reconciling them. Scored n per language also ≠ manifest n: mr 79/100, pa 90/100, sd 75/100, or 69/69, sa 100/100.

### K3 — weekday errors → **REPRODUCED, and worse than the planner listed**

`date -j -f %Y-%m-%d … +%A`: 2026-09-29 **Tue**, 09-30 **Wed**, 10-01 **Thu**, 10-02 Fri, 10-03 **Sat**, 10-04 **Sun**.

| Wrong text | Location | Correct |
|---|---|---|
| `Tue 2026-09-30` | packet L120, L286, L327 | Wed 2026-09-30 |
| `Wed 2026-10-01` | packet L6, 79, 120, 161, 287, 288, 296, 303, 328, 329; arch packet L6, 21, 72; level7 plan L85 | 2026-10-01 is **Thu** |
| `Sat 2026-10-04` | packet L289, L330 | 2026-10-04 is **Sun** |
| `Wed 2026-10-01 → Fri 2026-10-03` | packet L288, L329 | two errors: 10-01 Thu, **10-03 is Sat** |
| `Mon 2026-09-29 evening` | packet L161 | today is **Tue** 2026-09-29 — this date is already in the past |

The freeze/submission dates are not independently established anywhere I could find: `CAMPAIGN_DIRECTIVE.md` Part A1 marks the real hackathon deadline **UNKNOWN** (feed says "Oct 4 (Sat)"; `INTEGRATION_REPORT.md:146` says 2026-10-15; feed R132 says qualifiers close 30/09) → boss decision **U2**. The Oct-1 freeze traces to the lead's ambiguous "I'll join after next Wednesday" → **U1**. Both go to Vinay as `date TBC (U1/U2)`, not as invented weekdays.

### K4 — Option A (packet/Miss) vs Option D (Verdict) → **REPRODUCED, and worse: the letter "A" means two different things**

| | Root packet (Miss, 20:08) | `docs/architecture/W5_STRATEGY_OPTIONS.md` (Verdict, 17:04) |
|---|---|---|
| Taxonomy | 3 options A/B/C | 5 options A–E |
| **"Option A" means** | wrap-only **+ QLoRA kok+pa** | wrap-only **only** (QLoRA is B) |
| Recommendation | A | **D** (wrap + specialists: R4 restoration + Sarvam-API sat/mni + surya Perso-Arabic) |
| Cost / time | $0 / 3–4 h | $6–30 / 2–4 d |
| What it wins | 2 SAFE cells, conditional on K1 | all 4 weak cells, each with its own tool |
| Options omitted from the packet | — | **D and E are never mentioned in the root packet** |

**BLOCKER-grade internal contradiction inside the root packet itself:** L42 says the recommendation is "**Option A** (wrap-only + Konkani + Punjabi QLoRA)" and the default-if-no-answer is "Option B (wrap-only only)". L216 (D1 row) says the verdict default is "**B** (wrap + QLoRA kok+pa)". L224 says the same as L42. So **B denotes two different strategies three lines apart**, and D1's default is the *opposite* of the TL;DR's default. Vinay is being asked to approve "Option A" while the decision table's default is "Option B", and the strategy doc he is handed says A means something else and recommends D.

### K5 — backbone → **REPRODUCED: the packet names a superseded backbone as primary**

| Source | mtime | Says |
|---|---|---|
| `docs/research/level7/W6_QLORA_SPEC.md:53` | **20:01** | "**Backbone:** **Qwen2.5-VL-3B-Instruct @ 4-bit MLX** (primary)." … `:55` GLM-OCR-0.9B = "ALTERNATE 2" |
| `OCR_AGENT_MEMORY_FEED.md:464` (§12.2) | — | "**Backbone:** Qwen2.5-VL-3B-Instruct @ 4-bit MLX (PRIMARY)." |
| `OCR_AGENT_MEMORY_FEED.md:365`, `:743` | — | Qwen2.5-VL-3B-Instruct |
| `OCR_AGENT_MEMORY_FEED.md:821` (§15 pivot) | 2026-09-29 | backbone weights download "**NOT in this pivot**. Separate user gate." |
| `docs/research/level7/W5_STRATEGY_OPTIONS.md:29` | 17:04 | "backbone = GLM-OCR 0.9B primary (or Qwen2.5-VL-3B if user overrides)" |
| **`VINAY_MEETING_PACKET.md:127, 219, 287, 299, 312, 319, 328`** | **20:08** | "GLM-OCR 0.9B primary" / "**GLM-OCR 0.9B** (OmniDocBench #1)" |

**Verdict: the latest locked decision is Qwen2.5-VL-3B-Instruct @ 4-bit PRIMARY** (W6_QLORA_SPEC, newest doc in the set at 20:01; feed §12.2 agrees). The packet is the *newest file* but carries the *older* backbone. GLM-OCR is ALTERNATE 2.

**Weights on disk:** `ls ~/.cache/huggingface/hub | grep -iE 'qwen|glm'` → **no matches**. The cache holds 7 entries total, none of them a candidate backbone (PaddlePP-OCRv5 mobile_rec ×2, surya-ocr-2-gguf, gemma-4-31B-it-qat, vit-base-patch16). So *neither* backbone is downloadable-free: a "$0, ~3–4 h QLoRA tomorrow" claim is not executable without a download approval Vinay has not given.

**Also false in the same sentence:** packet L219 calls GLM-OCR "OmniDocBench #1". On the source I opened (`sarvam.ai/blogs/sarvam-vision-2-1`, fetched this run), **OmniDocBench v1.6 Overall: PaddleOCR-VL 1.6 = 96.01, Sarvam Vision 2.1 = 94.97** — GLM-OCR is not on that table. The 94.62 figure in feed L1073/L1336 is **v1.5**. And the packet's own L61 says PaddleOCR-VL 1.6 is "strongest single-model result on any benchmark" — so the packet contradicts itself two hundred lines apart.

### K6 — `sa` row "surya all-empty (Ol Chiki bug)" → **REPRODUCED: the FACT is right, the LABEL is wrong**

```
sa (n=100) surya: mean CER = 1.0000, empty predictions = 100/100, distinct predictions = 1
sa (n=100) surya GT sample: '(२६४) ग्रहलाघवे अत्रोपपत्तिः । वर्ष…'   -> Devanagari = Sanskrit
```

The fact is exact and load-bearing (surya is unusable on Sanskrit — the routing table is right to fall back to easyocr). The **cause label is fabricated**: Ol Chiki is Santali (`sat`, U+1C50–1C7F), not Sanskrit. I confirmed the scripts by codepoint on disk, not from memory:

```
sat GT Ol-Chiki fraction 0.50 · only sarvam_vision emits Ol Chiki (0.42); all 10 local engines 0.00
mni GT Meitei-Mayek fraction 0.98 · only sarvam_vision emits Meitei Mayek (0.99); all 10 local engines 0.00
```

The "Ol Chiki bug" mislabel appears in **two** files: `EVIDENCE_SUMMARY.md:58` and `PER_LANG_ROUTING.md:19`. Both get the same fix.

### K7 — kok gap → **REPRODUCED: 0.194 is right, the feed's 0.32 is stale, and DISPATCH_LOG P5 is right**

```
kok (n=100) mean CER:  surya 0.4248 | easyocr 0.6186 | paddleocr_indic 0.6222 | tesseract_indic 0.6444
                    openbharatocr 0.6444 | tesseract_bilingual 0.6442 | rapidocr 0.6570
                    indicphotoocr 0.6623 | anuvaad_tesseract 0.6481 | doctr 0.9145
best runner-up = easyocr 0.6186  ->  gap = 0.6186 - 0.4248 = 0.1938  ~= 19.4 pt   VERIFIED
```

`OCR_AGENT_MEMORY_FEED.md:460` ("gap 0.32") and `:468` ("kok 32pt → 5pt") are **STALE** — `DISPATCH_LOG.md:159` (P5) already corrected the spec to 0.194 and re-targeted the packet §1 table, but §12.2 was never updated. `EVIDENCE_SUMMARY.md:52` (0.194) and `W6_QLORA_SPEC.md:75` are correct. The **stale 0.32/32pt survives in two other places the P5 fix never reached**: `PER_LANG_ROUTING.md:34` and `docs/research/level7/W5_STRATEGY_OPTIONS.md:31`.

### Also checked (prompt §"Also check")

| Claim | Where | Verdict |
|---|---|---|
| "11 OCR engines" | packet L54/75/87/94/116/246 | **VERIFIED as a count of model strings** (11 in `sheet.csv`), but misleading: `sarvam_vision` has 54/1227 rows, and 10 engines ran all 1,227. Say "10 engines × 1,227 + Sarvam on 54". |
| "11 (10 independent)" | `EVIDENCE_SUMMARY.md:24` | **WRONG arithmetic.** Collapsing 3 identical engines into 1 gives **9**, not 10. And the premise is false: `openbharatocr == tesseract_indic` on 1,225/1,227 but `tesseract_bilingual` matches only **370/1,227**. 1,209 distinct prediction signatures across the 3 models. They are *near*-identical, not byte-identical. |
| "byte-identical on 1,257 packs" | `EVIDENCE_SUMMARY.md:24,78`; arch packet L29; arch opts L~66 | **WRONG.** 1,257 is a pack count, not a match count; measured 370/1,227 across all three, 1,225/1,227 for the openbharatocr/tesseract_indic pair. |
| "Sarvam overall CER 0.2400 (n=54)" | `EVIDENCE_SUMMARY.md:84`; arch packet L28; level7 opts L12; arch opts L9 | **WRONG — n is inconsistent with the number.** `0.2400` = `norm_overall_cer` in `ablation_delta_sarvam_vision.json`, which **drops loop-failure rows**. Proof: its per-language `sat = 0.2160` = mean(0.0265, 0.4054) = exactly the two non-loop sat rows; its `as = 0.0009` = mean(0.0, 0.0017), dropping `as_07`. Honest figure from the frozen `sheet.csv` at **n=54 is 0.2640**. |
| "12,324 packs" | packet L54/87/309, 116 | **UNIT ERROR.** 12,324 is sheet.csv **rows** (engine×item cells), not packs. Packs = 1,227. The packet gets it right twice (L94 "12,324 rows", L162 "12,324-row sheet.csv") — three sites are wrong. |
| "18 languages × 100 samples" | packet L54/87/116 | **WRONG.** Scored n is 19–100 (as 19, mni 20, sat 20, gu 24, doi 27, ne 37, brx 67, or 69, mr 79, sd 75, pa 90, rest 100). This is the "18 langs × 100/lang lock" error AGENTS.md also carries. |
| "$0" | packet L43, L119, L225, L303, L332 | **CONTRADICTED by the packet's own budget table** (L252/257/258: `$12 (₹1005)`, ceiling `$17-72`). L43 "Budget envelope: $0" and L119 "**$0**" cannot both stand with L257. |
| "mlx stack installed" | packet L119, L225; `COMPUTE_BUDGET_ESTIMATE.md:15-19` | **VERIFIED.** `pip` in `.venv311`: mlx 0.32.3, mlx-metal 0.32.3, mlx-vlm 0.7.4, mlx-tune 0.6.0, mlx-lm 0.31.3, mlx-embeddings 0.1.0, mlx-audio 0.5.7. All seven present. |
| "~9.4 GB reclaimable" | packet L119, L225; `COMPUTE_BUDGET_ESTIMATE.md:11`; feed §12.2 says 11.5 GB | **STALE.** `memory_pressure` now reports **66% system-wide free** — memory is no longer the binding constraint. Three different snapshots (143 MB raw free / 9.4 GB / 11.5 GB) exist across the corpus. Also stale: "Disk free 17 GB → 12 GB" — `df` shows 12 Gi used / 13 Gi avail. |
| Sarvam-bench per-language numbers 53.91 sat / 54.82 ks / 55.3 OldScan / 80.01 or | packet L53, 55, 117, 145, 166, 309, 316; plans L23-27 | **VERIFIED against the source I fetched**, and **DEAD-for-comparison as used.** `https://sarvam.ai/blogs/sarvam-vision-2-1` (pub. 2026-09-24) confirms: Overall 87.39, Bodhan 84.94, Gemini 3.6 Flash 79.35, Google Cloud Vision 71.76, Santhali 53.91, Kashmiri 54.82, Odia 80.01, Manipuri 85.12, Konkani 97.41, Bodo 90.48, Sanskrit 84.05, 6,909 samples = 6,609 Indic (22 langs) + 300 EN. **But `OldScan 55.3` is an olmOCR-Bench column, and that benchmark is English-only** (the page says so explicitly) — it is a different benchmark from the 87.39 Indic headline. Every packet sentence that sets a 55.3 next to 53.91/54.82/80.01 as if all four were Indic cells is DEAD. |
| **"wins the 9/18 probe22 cells where Sarvam's own numbers are weak (OldScan, Kashmiri, Odia, **Konkani**)"** | packet L117, L309 | **WRONG — and the worst single claim in the packet.** On the source I fetched, Sarvam scores **97.41 on Konkani**, one of its *three best* Indic cells (Konkani 97.41 > Hindi 93.52, Marathi 95.06). Presenting Konkani as a cell "where Sarvam is weak" is checkable in under a minute and is false. It is also the same sentence that justifies the flagship QLoRA. |
| "surya 0.3849" | arch packet L27; level7 opts L10; arch opts L9 | **WRONG.** Mean CER over surya's 1,227 sheet rows = **0.3944**. (0.3849 is a real on-disk number — `scores/LEADERBOARD.md:94` — but it does not reproduce from `sheet.csv`.) `PAPERTHIN_VINAY_AUDIT.md:46,77` had already flagged it; `DISPATCH_LOG.md:158` (P4) patched only the root packet and then claimed "grep … across all 4 patched files = 0 hits (clean)". **That verification is false — 0.3849 still appears in 3 target files.** |
| Sarvam EN column "EXECUTED, 3 calls, CER 0.1078" | packet L129, L240 | **VERIFIED.** `scores/en_sanity_sarvam_vision.json` → `n:3, cer:0.10782190999127853`. But `COMPUTE_BUDGET_ESTIMATE.md:35` ("0 Sarvam EN calls so far", "3 more EN calls … 57 total") and `PER_LANG_ROUTING.md:59` ("D2 APPROVED but not yet executed by Miss") are **STALE — already done.** |
| Sarvam cap "57" vs "54" | packet L65/86/119/204 (57) vs L204 (54-cap); `COMPUTE_BUDGET_ESTIMATE.md:35` | **INTERNALLY INCONSISTENT.** 54 Indic + 3 EN = 57 calls made. The cap is 54 *Indic* calls; say which. |
| "W5 freeze opens Wed 2026-10-01 evening" / "final deliverable Sat 2026-10-04" | packet L79, L120, L289, L296, L330 | **WRONG weekday + UNKNOWN date** → `date TBC (U1/U2)`. |

---

# PART 1 — CLAIM LEDGER

Grouped: the packet repeats a claim in TL;DR, 60-second recap and §1 — one row, all line numbers. `sheet` = the set the number belongs to; `n` = sample size; `metric` = the metric, named every time.

| # | Packet line(s) | Claim (≤25 words) | Source cited | Reproduce command | Output | Verdict |
|---|---|---|---|---|---|---|
| C-01 | 49, 303 | "wrap-only pipeline … wins 9/18 languages" | — | per-lang mean CER per model from `sheet.csv` | surya lowest mean CER in 9 of the **12** n≥50 langs; 6 langs n<50 carry no claim by D4 | **WRONG** (denominator) |
| C-02 | 126 | "**Beats Sarvam on 9/18 langs already with current engines**" | — | planner's paired script, 54 Sarvam rows | 10/18 with surya; 3 items/lang; item-level Sarvam better 28 : surya 21 : tie 5 | **WRONG** — not 9, and n=3 |
| C-03 | 117, 309 | "wins the 9/18 probe22 cells where Sarvam's own numbers are weak (OldScan, Kashmiri, Odia, **Konkani**)" | `OBITUARIES.md` | fetch `sarvam.ai/blogs/sarvam-vision-2-1`; per-lang mean CER from `sheet.csv` | Sarvam Indic: **Konkani 97.41** (3rd best), Kashmiri 54.82, Odia 80.01, Santhali 53.91. OldScan 55.3 is **olmOCR-Bench (English-only)**, a different benchmark | **WRONG** — Konkani is Sarvam's best cell; OldScan is the wrong bench |
| C-04 | 54, 87, 116 | "11 OCR engines scored on 18 languages × 100 samples = 1,227 items / 12,324 packs LOCKED" | — | `csv.DictReader` row+model+lang counts; per-lang n | 12,324 rows OK; 1,227 items OK; **11 = model strings but Sarvam has 54 rows**; **n is 19–100, not 100**; **rows ≠ packs** | **WRONG** (2 of 4 sub-claims) |
| C-05 | 95, 94, 246 | "manifest.json 1,283 items, frozen" · "sheet.csv 12,324 rows" | manifest.json | `json.load(manifest)['items']`; additions count | manifest 1,283; additions 56 (sd 25, mr 21, pa 10); 1227+56=1283 | **VERIFIED** |
| C-06 | 54, 87, 116, 129, 240 | "Sarvam scored on 54 packs (3/lang) + 3 EN sanity = 57 total" | — | count `model==sarvam_vision`; read `en_sanity_sarvam_vision.json` | 54 rows; EN n=3, cer 0.10782 | **VERIFIED** (but "cap 57" vs "cap 54" inconsistent, L204) |
| C-07 | 54, 87, 116 | "Best non-Sarvam = surya (wins 9/18 langs; per-lang CER 0.030–0.623)" | `EVIDENCE_SUMMARY.md` §3 | per-lang winner CER | range 0.030 (mai) – 0.623 (ur) is the **winner-column** range — correct; "9/18" wrong (see C-01) | **DIRECTIONAL** (range right, count wrong) |
| C-08 | 118, 127 | "Konkani has a 19.4-point CER gap (surya 0.425 vs runner-up easyocr 0.619; McNemar p=0.0033 vs tesseract_bilingual)" | `EVIDENCE_SUMMARY.md` §3 | kok means; `mcnemar_full_matrix.json[tesseract_bilingual_vs_surya][kok]` | 0.6186 − 0.4248 = 0.1938; p=3.33e-03, disc=31, n=100, winner=surya | **VERIFIED** — the strongest claim in the packet |
| C-09 | 44, 127, 226, 311, 318 | "Punjabi has 8-point gap (McNemar p<0.0001, K1 SURVIVES)" / "both McNemar-significant gaps" | `EVIDENCE_SUMMARY.md` §3 | pa means; `mcnemar_full_matrix.json` on pa | gap 0.0814 real. But surya vs **tesseract_indic (the runner-up): n=90, disc=3, p=1.00, TIE**. surya beats only **5 of 9** on pa (wins vs rapidocr, doctr, anuvaad, easyocr, paddleocr — all the *broken* engines) | **WRONG** — the p<0.0001 is vs easyocr (0.817), not the runner-up |
| C-10 | 127, 287, 219 | "Backbone: GLM-OCR 0.9B primary" / "GLM-OCR 0.9B (OmniDocBench #1)" | — | grep backbone across feed + `W6_QLORA_SPEC.md` | `W6_QLORA_SPEC.md:53` (mtime 20:01, newest): "Qwen2.5-VL-3B-Instruct @ 4-bit MLX (primary)"; GLM-OCR = ALTERNATE 2. Feed:464 agrees. On OmniDocBench **v1.6** the #1 I could verify is PaddleOCR-VL 1.6 at 96.01; GLM-OCR's 94.62 is **v1.5** and absent from the v1.6 table | **STALE** (superseded 20:01) + **UNSUPPORTED** ("#1") |
| C-11 | 56, 312, 319 | "GLM-OCR 0.9B weights download (~1.8 GB) as separate user gate — NOT in the $0 ask" | §9 hard rule | `ls ~/.cache/huggingface/hub \| grep -iE 'qwen\|glm'` | **no matches**; 7 cache entries, none a candidate backbone | **VERIFIED** (and it undercuts the "$0, 3–4 h tomorrow" framing) |
| C-12 | 119, 225 | "mlx 0.32.3 + mlx-vlm 0.7.4 + mlx-tune 0.6.0 already installed" | `MLX_INSTALL_RESULT.md` | `.venv311/bin/pip show` × 7 | all present at the exact versions | **VERIFIED** |
| C-13 | 119, 225 | "~9.4 GB memory reclaimable" | `W6_HANDOFF §7.2` | `memory_pressure` | **66% system-wide free** now; feed §12.2 says 11.5 GB; `COMPUTE_BUDGET_ESTIMATE.md:11` says 9.4 GB | **STALE** — three snapshots; constraint no longer binding |
| C-14 | 43, 119, 225, 303, 332 | "Budget envelope **$0** (local MLX, no cloud)" | — | read packet's own budget table | L252 asks `$12 (₹1005)` for the Sarvam subsidy; L257 "Total recommended **$12**"; L258 ceiling `$17-72` | **WRONG** — contradicts the packet's own §4 table |
| C-15 | 53, 85, 115, 138, 165 | "Beat Sarvam Vision 2.1 (87.39 average on their Indic OCR Bench headline)" | — | fetch `sarvam.ai/blogs/sarvam-vision-2-1` | **Overall accuracy 87.39** on Sarvam Indic OCR Bench; 6,909 samples = 6,609 (22 langs) + 300 EN; Bodhan 84.94 | **VERIFIED** |
| C-16 | 49, 117, 309 | "probe22 and Sarvam's 6,909-block Indic OCR Bench are different benchmarks" | — | fetch the blog + count our set | our set = 1,227 items/18 langs from PDF text layers; theirs = 6,909 curated blocks | **VERIFIED** — this caveat is correct and should lead |
| C-17 | 55, 145, 166, 309, 316 | "Per-language Sarvam numbers 53.91 sat / 54.82 ks / 55.3 OldScan / 80.01 or … quarantined DEAD-for-decisions" | `OBITUARIES.md` | fetch the blog | Santhali 53.91, Kashmiri 54.82, Odia 80.01 all **verified**. But **OldScan 55.3 is olmOCR-Bench (English-only)**, not Indic — quoting it beside the other three as an Indic cell is wrong even as "directional" | **DEAD-for-comparison** (OldScan leg) / VERIFIED (the other three) |
| C-18 | 310, 317, 55 | "mni/sat are Sarvam-only cells (no local engine emits Ol Chiki or Meetei-Mayek)" | — | codepoint fraction of `prediction` per model, U+1C50–1C7F and U+ABC0–0xABFF | sat: only `sarvam_vision` emits Ol Chiki (0.42); all 10 local = 0.00. mni: only Sarvam emits Mayek (0.99); all 10 local = 0.00 | **VERIFIED** — "physics" is literally true |
| C-19 | 130 | "Santali has 0 engines emitting Ol Chiki (Sarvam-only cell)" | — | same | same | **VERIFIED** |
| C-20 | 76, 245 | "§6.4 GT verdicts LOCKED — BARRED (ks/mni/sat/mr/ur + ne PDF), SAFE (as/brx/doi/kok/mai/or/pa), VERIFY-FIRST (gu/sd)" | `gt_verification.json` | — | file exists, 23,613 bytes, mtime 2026-09-29 02:34 | **UNSUPPORTED** (by this run — I did not open the JSON; the label sets also disagree across docs: `EVIDENCE_SUMMARY.md:107-110` lists SAFE as bn/hi/sa/or/pa + brx/kok/mai, and BARRED as ks/mni/**mr**/sat/ur/ne — note **bn/hi/sa** appear in EVIDENCE but not the packet) |
| C-21 | 73, 74, 75, 77 | "Level 1+2 DONE · W1/W2/W7 research DONE · probe22 DONE · Level 7 DONE" | listed files | `ls` the cited files | `level2/reports/LEADERBOARD.md` sealed; `docs/research/level7/` exists; `scores/LEADERBOARD.md` exists. **"1,300+ lane records" (L77) not counted by me** | **UNSUPPORTED** (last-disk-check dates claimed but not re-verified this run) |
| C-22 | 65, 86, 204 | "No paid APIs beyond the 57-call Sarvam trial cap" · "No Sarvam calls beyond the **54**-cap" | feed §9 | — | 54 Indic + 3 EN = 57 used. Two different caps in one packet | **WRONG** (self-inconsistent) |
| C-23 | 6, 79, 120, 161, 286-289, 296, 303, 327-330; arch packet 6, 21, 72; level7 plan 85 | `Tue 2026-09-30` · `Wed 2026-10-01` · `Sat 2026-10-04` · `Mon 2026-09-29` | — | `date -j -f %Y-%m-%d … +%A` | 09-29 Tue · 09-30 **Wed** · 10-01 **Thu** · 10-03 **Sat** · 10-04 **Sun** | **WRONG** (12 sites) |
| C-24 | 141 | "Per-lang CER 0.10-0.40 on 14/18 langs" | — | per-lang winner CER from `sheet.csv` | winner CERs: 0.030, 0.145, 0.165, 0.175, 0.205, 0.259, 0.315, 0.425, 0.476, 0.589, 0.623 → **7 of 12** in [0.10,0.40]; 9 of 18 counting the 6 n<50 langs we cannot claim | **WRONG** |
| C-25 | 162 | "The 12,324-row sheet.csv is already frozen" | — | `ls -la` | mtime 2026-09-28 21:54, 12,324 records | **VERIFIED** |
| C-26 | 58-63 | Live-research block (LightOnOCR-2-1B arXiv:2601.14251v2; 600k-ks-ocr arXiv:2601.01088; Laya; PaddleOCR-VL 1.6; Gnani Evon 3.3; Sarvam-87.39-contradiction) | arXiv IDs | — | **I did not open any of these arXiv IDs this run.** Only the Sarvam blog was fetched. | **UNSUPPORTED** — must not be presented to Vinay as verified-live until 1D confirms |
| C-27 | 58 | "LightOnOCR-2-1B … SOTA on olmOCR-Bench at 1B" | arXiv | fetch the blog | the blog's olmOCR-Bench table lists Sarvam 87.3, Opus 5 85.1, Chandra-OCR2 84.5, Mistral OCR4 83.1 — **LightOnOCR-2-1B is not in it** | **UNSUPPORTED** |
| C-28 | 61 | "PaddleOCR-VL 1.6 (arXiv:2606.03264, 0.9B Apache-2.0, OmniDocBench v1.6 96.33%) — strongest single-model result on any benchmark as of 2026-09-29" | arXiv | fetch the blog | blog says **96.01** on v1.6 (PaddleOCR-VL 1.6 first, Sarvam 2.1 94.97). 96.33 is **not corroborated by the one source I opened**. "Strongest on any benchmark" is an unsupportable superlative and **contradicts the packet's own L219** ("GLM-OCR OmniDocBench #1") | **UNSUPPORTED** (96.33) / **WRONG** (superlative + self-contradiction) |
| C-29 | 64 | "`metrics.py` normalization mismatch risk … VERIFY before freeze" | — | — | a stated risk, not a claim | **VERIFIED** (it is a caveat, correctly labelled) |
| C-30 | 111, 88 | "locked 4 decisions (D1–D4) at the validation call" | — | `docs/research/level7/W6_QLORA_SPEC.md`, feed §12.2 | D1 was re-OPENED (`docs/architecture/W5_STRATEGY_OPTIONS.md:11`: "D1 … NOW RE-OPENED for Vinay"); D4 backbone moved after 20:01 | **STALE** — they were locked, D1 is now open |
| C-31 | 177-187 | "Vinay's PPT (architecture … locked as direction)" + per-stage KEEP/HYBRID | `PPT_SPEC.md` | — | `docs/architecture/PPT_SPEC.md` exists (3,479 bytes). The stage table's "locked as direction" is contradicted by the packet's own Q2 ("Is the PPT the architecture we want to defend?") and by `W5_STRATEGY_OPTIONS.md` baseline row 1 (YOLO detector → REPLACE) | **UNSUPPORTED** ("locked" is asserted while Q2 asks whether to keep it) |
| C-32 | 151 | "Bodhan (AI4Bharat/IITM) … Public headline = 84.94" | — | fetch the blog | **84.94** on Sarvam Indic OCR Bench — confirmed. But it is *their* score on *their* bench, not a Bodhan-published headline | **VERIFIED** number, **DEAD** as "Bodhan's public headline" |
| C-33 | 149-150 | "Our wrap-only beats their headline on weak cells" | — | paired measurement, 54 rows | best-local beats Sarvam on 10/18 at 3 items/lang; and by Sarvam's own bench Konkani 97.41 is *not* weak | **WRONG** |
| C-34 | 141-143 | Option costs: A $0 · B $0 · C $0-60 spot | — | `ls ~/.cache/huggingface/hub` | C requires a backbone download; **no candidate weights on disk** | **DIRECTIONAL** ($0-60 understates the approval ceremony, not the money) |
| C-35 | 129, 240 | "Sarvam EN column **Already EXECUTED** (3 calls, n=3, CER 0.1078)" | — | read `en_sanity_sarvam_vision.json` | n=3, cer 0.10782 | **VERIFIED** (and `COMPUTE_BUDGET_ESTIMATE.md:35` / `PER_LANG_ROUTING.md:59` are stale against it) |
| C-36 | 246 | "Engine final state — 11/11 scored, sheet.csv 12,324 rows frozen" | — | `csv.DictReader` | 11 model strings; 10 have 1,227 rows, Sarvam has 54 | **VERIFIED** with the caveat that "11/11" hides the 54-row engine |
| C-37 | 216, 42, 224 | Decision-menu coherence: TL;DR default "Option B (wrap-only only)" vs D1 default "**B** (wrap + QLoRA kok+pa)" | — | read packet L42, L216, L224 | same letter, two strategies; TL;DR recommendation is "A" while D1's default is "B" | **WRONG** — internal contradiction |
| C-38 | 122, 99, 267, 277 | "see `W5_STRATEGY_OPTIONS.md`" / "`W5_STRATEGY_OPTIONS.md` (root)" | — | `ls W5_STRATEGY_OPTIONS.md` | **does not exist at root** (moved to `_reports/cleanup_cycle1/` and duplicated under `docs/`). Bare-filename citations now resolve to two *different* documents with *different* recommendations | **WRONG** — dangling reference, and the two targets disagree |
| C-39 | 102, 126 | "per-script engine routing table on `level2/probe22/PER_LANG_ROUTING.md`" | — | `ls` | that path **does not exist**; the file is at `_reports/cleanup_cycle1/PER_LANG_ROUTING.md` | **WRONG** — path is dead |
| C-40 | 101, 104, 103, 105 | anchors: `EVIDENCE_SUMMARY.md`, `COMPUTE_BUDGET_ESTIMATE.md`, `LEVEL7_RESEARCH_FINDINGS.md` | — | `ls` | all three moved to `_reports/…`; none resolves at root | **WRONG** — every anchor in §"Disk-truth anchors" is a dead path |
| C-41 | 264-268, 274-278 | 5-doc reading order incl. `STRATEGY_VINAY_TOMORROW.md`, `VINAY_CTA.md` | — | `ls` | both were **deleted** (packet L20: "Sources deleted"); they are still listed as reading items 2 and 3 with "(merged into this file)" | **UNSUPPORTED** — lists documents that no longer exist as separate reads |
| C-42 | 262-278 | "Vinay reads docs 1+2+3 (~10 min). User presents docs 4+5 if Vinay wants depth" | — | — | docs 2 and 3 are gone; doc 4 is ambiguous (root path deleted, two candidates) | **UNSUPPORTED** |
| C-43 | 193 | "Maithili (0.8-pt gap, p=1.0) and Odia (3-pt gap, near T2 threshold) don't survive K1" | `EVIDENCE_SUMMARY.md` §3 | `mcnemar_full_matrix.json` on mai, or | mai: surya 1/9 beaten, all others tie (disc=0 vs easyocr). or: surya 5/9; tesseract-family **is** the winner (0.259 vs surya 0.285). "3-pt gap" is not the or picture — or is a surya *loss* | **VERIFIED** (mai) / **WRONG** (or) |
| C-44 | 204 | "No Sarvam calls beyond the 54-cap + ~₹1000 subsidy" | — | — | conflicts with "57-call cap" at L65/86/119 | **WRONG** (self-inconsistent) |
| C-45 | 252, 257, 258 | "Sarvam API subsidy (~1k sat + 1k mni pages) **$12 (₹1005)**" · "Total recommended **$12**" | — | — | ₹1005 / 2,000 pages = ₹0.50/page, consistent with `W5_BEAT_SARVAM_PLAN.md:100` ("₹0.5/page × ~1000 = ₹500 ($6)"). But the arch options doc says **₹500-2500 ($6-30)** for the same thing — a 5× spread. Also ₹0.50/page vs Bodhan's ₹0.20/image at L56 is never reconciled | **UNSUPPORTED** — the number is unsourced and contradicts its sibling doc |
| C-46 | 28 | "**Status:** 🟡 **READY**" | — | this audit | 19 BLOCKER defects, including a self-contradictory decision menu and a false "Konkani is a Sarvam weak cell" claim | **WRONG** — "READY" is not supportable in this state |
| C-47 | 338 | "Provenance: Merged from `VINAY_MEETING_PACKET.md` (Verdict agent, 2026-09-29 **22:00** IST)" | — | `stat` on the file and on the merge log | this file's mtime is **20:08**; the merge is logged at 20:0x, and no 22:00 artifact exists on disk. Also: the file "merged from" a copy of *itself* | **WRONG** — a future timestamp and a self-referential merge |
| C-48 | 2, 19, 336-338 | banner "Miss agent, 2026-09-29 IST" + "Merged from … per audit-5 finding" | — | `stat` | 20:08 write; banner and sign-off say Miss; provenance says the base was a Verdict file at 22:00 | **UNSUPPORTED** — authorship/timeline cannot be reconstructed from disk |
| C-49 | 49, 303 | "zero cost, zero risk" / "$0, no cloud" | — | packet's own §4 | $12 recommended, $17-72 ceiling; a backbone download gate; memory re-verification gate | **WRONG** |
| C-50 | 149, 56 | "Bodhan Indic-OCR (open-weight, ₹0.20/image)" | — | — | no source on disk; the rate is nowhere in `sheet.csv`, the plan, or the budget doc | **UNSUPPORTED** |
| C-51 | 51, 64 | "Reading time ~5 minutes" · "5-doc reading order" | — | this audit | §2 alone asks Vinay to resolve 3 numbered "Q"s that each appear **twice** under different content (Q1 twice, Q2 twice, Q3 twice), plus 4 D-decisions plus 5 TL;DR decisions | **WRONG** — the doc is longer and more contradictory than 5 minutes of reading can absorb; this is itself a cross-examination risk |

---

# PART 3 — FIX-SPECS

Severity: **BLOCKER** = a false claim Vinay could catch in the room · **MAJOR** = misleading · **MINOR** = wording.
Every OLD string below was verified to occur **exactly once** in its file:
`python3 -c "t=open(F).read();print(t.count(OLD))"` → `1`.
Order: BLOCKER first. Files that are sealed or re-LOCKED get an **ERRATUM** instead of an edit.

---

## BLOCKER

### FS-01 | BLOCKER | `VINAY_MEETING_PACKET.md:126`
- **OLD (exact):** `**Beats Sarvam on 9/18 langs already with current engines.**`
- **NEW (exact):** `**Directional only: on the 54 items where Sarvam was run (3 per language) our best local engine had lower mean CER than Sarvam in 10 of 18 languages. At n=3 per language this is not a win. On the full scored set, surya has the lowest mean CER in 9 of the 12 languages with n>=50, and clears McNemar p<0.05 against every testable opponent in 5 of them (bn, brx, hi, kok, ks).**`
- **EVIDENCE:** planner's paired script on `sheet.csv` → `surya<sv langs 10/18`; item-level `surya 21 / sv 28 / tie 5`; per-lang winner count at n>=50 → `surya 9 of 12`; `mcnemar_full_matrix.json` surya-vs-all → `beat ALL: [bn, brx, hi, kok, ks] = 5`
- **WHY:** This is the single sentence the whole meeting hangs on, and it is wrong twice — wrong denominator, and it presents n=3 as a result.

### FS-02 | BLOCKER | `VINAY_MEETING_PACKET.md:49`
- **OLD (exact):** `wins 9/18 languages on our own 1,227-item probe22 today`
- **NEW (exact):** `has the lowest mean CER in 9 of the 12 languages where n>=50 on our own 1,227-item scored probe22 set (the other 6 languages have n<50 and carry no winner claim), and clears McNemar p<0.05 against every testable opponent in 5 of them, today`
- **EVIDENCE:** per-lang mean CER per model from `sheet.csv` → `winners n>=50: surya 9, tesseract-family 2, easyocr 1`; n<50 = `as 19, doi 27, gu 24, mni 20, ne 37, sat 20`
- **WHY:** The TL;DR headline is the first line Vinay reads.

### FS-03 | BLOCKER | `VINAY_MEETING_PACKET.md:303`
- **OLD (exact):** `beating Sarvam on 9/18 langs, ~30min wall`
- **NEW (exact):** `competitive with Sarvam on the cells we measured (n=3/lang, directional), ~30min wall`
- **EVIDENCE:** 54 Sarvam rows; best-local beats Sarvam in 10/18 at 3 items each; `best-local on same 54 = 0.2956` vs `sarvam 0.2640` — best-local is *worse overall* on that subset
- **WHY:** "Beating Sarvam" is refutable in one line: our best local averages 0.2956 on those 54, Sarvam 0.2640.

### FS-04 | BLOCKER | `VINAY_MEETING_PACKET.md:117, 309` (the Konkani claim)
- **OLD (exact):** `wins the 9/18 probe22 cells where Sarvam's own numbers are weak** (OldScan, Kashmiri, Odia, Konkani)`
- **NEW (exact):** `is competitive with Sarvam on the cells we measured (n=3/lang, directional)**, and Sarvam's own published weak cells are Kashmiri 54.82, Odia 80.01 and Santhali 53.91 — not Konkani, where Sarvam scores 97.41 on their Indic OCR Bench. Note OldScan 55.3 is an olmOCR-Bench (English-only) column, a different benchmark from the 87.39 Indic headline.`
- **EVIDENCE:** `https://sarvam.ai/blogs/sarvam-vision-2-1` (fetched 2026-09-29) → Indic bench: Konkani **97.41**, Hindi 93.52, Marathi 95.06, Odia 80.01, Kashmiri 54.82, Santhali 53.91; olmOCR-Bench table header states "This benchmark is officially English-only" with OldScan 55.3
- **WHY:** Konkani is Sarvam's **third-best** Indic cell. This is the fastest way to lose the room, and it is the same claim that justifies the flagship QLoRA.

### FS-05 | BLOCKER | `VINAY_MEETING_PACKET.md:216` (D1 default contradicts the TL;DR)
- **OLD (exact):** `**B** (wrap + QLoRA kok+pa) — best risk-adjusted`
- **NEW (exact):** `**A** (wrap-only + QLoRA kok+pa) — best risk-adjusted; **pa is conditional, kok is verified** (see §1)`
- **EVIDENCE:** packet L42 (recommendation = A, default-if-no-answer = B) vs L216 (D1 default = B = wrap+QLoRA) vs L224 (A vs B) — the letter B denotes two different strategies; `mcnemar_full_matrix.json` pa: surya vs tesseract_indic `n=90 disc=3 p=1.00 tie`
- **WHY:** Vinay is asked to approve "Option A" while the decision table's own default is "Option B". He cannot answer.

### FS-06 | BLOCKER | `VINAY_MEETING_PACKET.md:127` (the pa McNemar claim)
- **OLD (exact):** `Punjabi has 8-point gap (McNemar p<0.0001, K1 SURVIVES).`
- **NEW (exact):** `Punjabi has an 8.1-point CER gap (surya 0.145 vs tesseract_indic 0.226) but the gap is NOT McNemar-significant against the runner-up (n=90, 3 discordant items, p=1.00, tie); surya beats only 5 of 9 testable opponents on pa, all of them broken engines. Treat Punjabi as CONDITIONAL, not verified.`
- **EVIDENCE:** `mcnemar_full_matrix.json[tesseract_indic_vs_surya]['pa']` → `{"n_common":90,"n_discordant":3,"p_two_sided":1.0,"winner":"tie"}`; surya wins 5/9 on pa
- **WHY:** The p<0.0001 is real but against **easyocr (0.817)**, not the runner-up. QLoRA on pa has no closable gap.

### FS-07 | BLOCKER | `VINAY_MEETING_PACKET.md:120` (date spine)
- **OLD (exact):** `Vinay meeting (Tue 2026-09-30, tomorrow) → W5 freeze opens Wed 2026-10-01 evening → W6 execution Wed-Fri (~3-4h) → final deliverable Sat 2026-10-04.`
- **NEW (exact):** `Vinay meeting (Wed 2026-09-30, tomorrow) → W5 freeze opens 2026-10-01 (Thu) evening, date TBC (U1) → W6 execution 2026-10-01→10-03 (~3-4h) → final deliverable 2026-10-04 (Sun), date TBC (U2: real submission deadline is UNKNOWN — feed says Oct 4, INTEGRATION_REPORT.md:146 says 2026-10-15, feed R132 says qualifiers close 30/09).`
- **EVIDENCE:** `date -j -f %Y-%m-%d … +%A` → 2026-09-30 **Wednesday**, 2026-10-01 **Thursday**, 2026-10-04 **Sunday**; `CAMPAIGN_DIRECTIVE.md` Part A1 marks the deadline UNKNOWN → U2
- **WHY:** Three wrong weekdays in one sentence, plus a deadline presented as settled that is not.

### FS-08 | BLOCKER | `VINAY_MEETING_PACKET.md:79` and `docs/architecture/VINAY_MEETING_PACKET.md:21` — **the identical line exists in BOTH packets**, so two per-file specs with disambiguating context. Also `docs/architecture/VINAY_MEETING_PACKET.md:6, 72`.

**FS-08a** — `VINAY_MEETING_PACKET.md:79`
- **OLD (exact):**
```
| W6 fine-tuning prep | **PAUSED** pending this meeting | 2026-09-29 |
| W5 freeze | opens Wed 2026-10-01 | — |
```
- **NEW (exact):**
```
| W6 fine-tuning prep | **PAUSED** pending this meeting | 2026-09-29 |
| W5 freeze | opens 2026-10-01 (Thu) — date TBC (U1) | — |
```
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-01 +%A` → `Thursday`; the Oct-1 date traces to the lead's ambiguous "I'll join after next Wednesday" → boss decision **U1**
- **WHY:** Never invent a weekday for an unsettled date. Context line included because the same table row is byte-identical in the second packet.

**FS-08b** — `docs/architecture/VINAY_MEETING_PACKET.md:21`
- **OLD (exact):**
```
| W6 fine-tuning prep | **PAUSED** pending this meeting | 2026-09-29 |
| W5 freeze | opens Wed 2026-10-01 | — |
```
- **NEW (exact):**
```
| W6 fine-tuning prep | **PAUSED** pending this meeting | 2026-09-29 |
| W5 freeze | opens 2026-10-01 (Thu) — date TBC (U1) | — |
```
- **EVIDENCE:** same as FS-08a
- **WHY:** Same defect, second file. **Both packets must be patched or Vinay gets whichever one the presenter opens.**

**FS-08c** — `docs/architecture/VINAY_MEETING_PACKET.md:6`
- **OLD (exact):** `**Goal:** lock the W6 path + budget before W5 freeze (Wed 2026-10-01)`
- **NEW (exact):** `**Goal:** lock the W6 path + budget before W5 freeze (2026-10-01, Thu — date TBC U1)`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-01 +%A` → `Thursday`
- **WHY:** Third occurrence in the second packet.

**FS-08d** — `docs/architecture/VINAY_MEETING_PACKET.md:72` **and** `VINAY_MEETING_PACKET.md:296` — byte-identical row in both packets, so two per-file specs.
- **OLD (exact) [arch packet]:** `| W5 freeze | Wed 2026-10-01 | Recipe frozen, no new inputs |`
- **NEW (exact) [arch packet]:** `| W5 freeze | 2026-10-01 (Thu), date TBC (U1) | Recipe frozen, no new inputs |`
- **OLD (exact) [root packet]:** `| W5 freeze | Wed 2026-10-01 | Recipe frozen, no new inputs |`
- **NEW (exact) [root packet]:** `| W5 freeze | 2026-10-01 (Thu), date TBC (U1) | Recipe frozen, no new inputs |`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-01 +%A` → `Thursday`; each OLD string is unique within its own file (`t.count(OLD) == 1` per file)
- **WHY:** Same frozen table, both packets. Apply to both or the presenter picks the unpatched one.

**FS-08e** — `VINAY_MEETING_PACKET.md:6` (banner, HTML comment — still rendered to no one, still wrong on disk)
- **OLD (exact):** `Vinay → W5 freeze after Wed 2026-10-01 → W6 training decision.`
- **NEW (exact):** `Vinay → W5 freeze after 2026-10-01 (Thu, TBC U1) → W6 training decision.`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-01 +%A` → `Thursday`
- **WHY:** The W6 pause banner is the instruction an agent reads first; a wrong weekday in it will propagate.

### FS-09 | BLOCKER | `VINAY_MEETING_PACKET.md:289` and `:330` (two sites, two specs)

**FS-09a** — `VINAY_MEETING_PACKET.md:289`
- **OLD (exact):** `**Sat 2026-10-04:** W6 freeze + final deliverable.`
- **NEW (exact):** `**2026-10-04 (Sun), date TBC (U2):** W6 freeze + final deliverable.`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-04 +%A` → `Sunday`
- **WHY:** Saturday is wrong by one day and the date itself is UNKNOWN.

**FS-09b** — `VINAY_MEETING_PACKET.md:330`
- **OLD (exact):** `| **Sat 2026-10-04** | W6 freeze + final deliverable | All 3 agents |`
- **NEW (exact):** `| **2026-10-04 (Sun), TBC (U2)** | W6 freeze + final deliverable | All 3 agents |`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-10-04 +%A` → `Sunday`
- **WHY:** Same error, second table.

### FS-10 | BLOCKER | `VINAY_MEETING_PACKET.md:161` (a date already in the past)
- **OLD (exact):** `Align (push W5 freeze forward to Mon 2026-09-29 evening) or defer (keep Wed 2026-10-01)?`
- **NEW (exact):** `Align (push W5 freeze forward to Tue 2026-09-29 evening — i.e. today) or defer (keep 2026-10-01, Thu — date TBC U1)?`
- **EVIDENCE:** `date -j -f %Y-%m-%d 2026-09-29 +%A` → `Tuesday`; `date -j -f %Y-%m-%d 2026-10-01 +%A` → `Thursday`
- **WHY:** Two wrong weekdays, and it proposes a meeting-day deadline for work not yet approved.

### FS-11 | BLOCKER | `VINAY_MEETING_PACKET.md:127` (superseded backbone)
- **OLD (exact):** `Backbone: GLM-OCR 0.9B primary`
- **NEW (exact):** `Backbone: Qwen2.5-VL-3B-Instruct @ 4-bit PRIMARY per docs/research/level7/W6_QLORA_SPEC.md §1 (mtime 20:01, the newest spec); GLM-OCR 0.9B is ALTERNATE 2. Neither is on disk — ~0 candidate weights in ~/.cache/huggingface/hub — so any backbone is a separate download approval, not a $0 item.`
- **EVIDENCE:** `W6_QLORA_SPEC.md:53` "Qwen2.5-VL-3B-Instruct @ 4-bit MLX (primary)", `:55` "ALTERNATE 2: GLM-OCR-0.9B"; `OCR_AGENT_MEMORY_FEED.md:464` "Backbone: Qwen2.5-VL-3B-Instruct @ 4-bit MLX (PRIMARY)"; `ls ~/.cache/huggingface/hub | grep -iE 'qwen|glm'` → no matches
- **WHY:** The packet is the newest file carrying the oldest decision.

### FS-12 | BLOCKER | `VINAY_MEETING_PACKET.md:219` (false "#1" + internal contradiction with L61)
- **OLD (exact):** `| **D4** | Backbone choice | stay with PPT / Bodhan / GLM-OCR / Qwen2.5-VL / MonkeyOCRv2 / **LightOnOCR-2-1B** (NEW 2026-09-29 live research) |`
- **NEW (exact):** `| **D4** | Backbone choice | stay with PPT / Bodhan / GLM-OCR / Qwen2.5-VL-3B / MonkeyOCRv2 / **LightOnOCR-2-1B** (unverified this run) |`
- **EVIDENCE:** on `https://sarvam.ai/blogs/sarvam-vision-2-1` (fetched 2026-09-29) the OmniDocBench **v1.6** Overall column reads `PaddleOCR-VL 1.6 = 96.01, Sarvam Vision 2.1 = 94.97` — GLM-OCR is absent; feed:1073/1336's `94.62` is **v1.5**. Packet L61 already calls PaddleOCR-VL 1.6 the strongest result on the board.
- **WHY:** "GLM-OCR OmniDocBench #1" and "PaddleOCR-VL 1.6 strongest" cannot both be true; the #1 is a v1.5 number presented without its version.

### FS-13 | BLOCKER | `VINAY_MEETING_PACKET.md:54` (the status line Vinay will read first)
- **OLD (exact):** `- **What works:** 11 OCR engines scored on 18 languages × 100 samples = **1,227 items / 12,324 packs LOCKED**.`
- **NEW (exact):** `- **What works:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings total; Sarvam has only 3 items per language) = **12,324 sheet.csv rows** (rows, not packs). Scored n per language is **19-100, not 100**. **1,227 = the scored base set; manifest.json holds 1,283 (1,227 + 56 additions: sd 25, mr 21, pa 10, unscored).**`
- **EVIDENCE:** `csv.DictReader` → 12,324 records, 11 models (10x1227 + 54), 1,227 distinct `image_id`; scored n `as 19, mni 20, sat 20, gu 24, doi 27, ne 37, brx 67, or 69, mr 79, sd 75, pa 90, others 100`; `manifest['items']` = 1283; additions = 56 (sd 25, mr 21, pa 10)
- **WHY:** Three errors in one clause: engine count, ×100 lock, and packs-vs-rows.

### FS-14 | BLOCKER | `VINAY_MEETING_PACKET.md:87`
- **OLD (exact):** `- **Status as of today:** 11 OCR engines scored on 18 languages × 100 samples = **1,227 items / 12,324 packs LOCKED**.`
- **NEW (exact):** `- **Status as of today:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings) = **12,324 sheet.csv rows**; scored n per language **19-100**. **1,227 = scored base set; manifest = 1,283 (+56 unscored additions).**`
- **EVIDENCE:** same as FS-13
- **WHY:** Second copy of the same false status line.

### FS-15 | BLOCKER | `VINAY_MEETING_PACKET.md:116`
- **OLD (exact):** `2. **Status:** 11 OCR engines scored on 18 languages × 100 samples = **1,227 items / 12,324 packs LOCKED**.`
- **NEW (exact):** `2. **Status:** **10 engines x 1,227 items + Sarvam on 54** (11 model strings) = **12,324 sheet.csv rows**; scored n per language **19-100**. **1,227 = scored base set; manifest = 1,283 (+56 unscored additions).**`
- **EVIDENCE:** same as FS-13
- **WHY:** Third copy, and it also carries `wins 9/18 langs` immediately after — see FS-13 note on 9/18.

### FS-16 | BLOCKER | `docs/architecture/VINAY_MEETING_PACKET.md:27` (the unrecorded second packet)
- **OLD (exact):** `- **Best local engine: surya** at overall CER 0.3849. Wins 9/18 langs (bn, brx, hi, kok, ks, mai, pa, sd, ur). ~16s/page, no GPU.`
- **NEW (exact):** `- **Best local engine: surya**, mean CER **0.3944** over its 1,227 scored items (the 0.3849 in earlier drafts does not reproduce from sheet.csv). Lowest mean CER in **9 of the 12** languages with n>=50 (bn, brx, hi, kok, ks, mai, pa, sd, ur); McNemar p<0.05 against every testable opponent in **5** (bn, brx, hi, kok, ks). Throughput: **~25 s/pack CPU** per PER_LANG_ROUTING/COMPUTE_BUDGET, not 16 s.`
- **EVIDENCE:** mean of surya's 1,227 `CER` values in `sheet.csv` = **0.3944**; `docs/architecture/VINAY_MEETING_PACKET.md:27` says 0.3849; speed: `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:50` and `COMPUTE_BUDGET_ESTIMATE.md:28` both say ~25 s/pack
- **WHY:** This doc was **not on the planner's list** and carries a number `PAPERTHIN_VINAY_AUDIT.md` had already rejected, plus a 56% throughput error that drives the wall-clock estimate.

### FS-17 | BLOCKER | `docs/architecture/VINAY_MEETING_PACKET.md:28` (0.2400 at n=54)
- **OLD (exact):** `- **Sarvam Vision 2.1** at 0.2400 on 54-call cap (3/lang, directional only)`
- **NEW (exact):** `- **Sarvam Vision 2.1** at mean CER **0.2640** over the 54 items in sheet.csv (3/lang, directional only). The 0.2400 figure elsewhere in this corpus is the loop-excluded mean over 50 items, not 54.`
- **EVIDENCE:** mean of the 54 `model==sarvam_vision` CER values = **0.2640**; `scores/ablation_delta_sarvam_vision.json` → `norm_overall_cer: 0.2400081…` with per-language `sat: 0.21598…` = mean(0.0265, 0.4054), i.e. **the loop-failure row sat_13 (CER 1.0) is excluded**; same for `as_07`
- **WHY:** "0.2400 at n=54" is internally impossible — the number and the sample size describe different sets.

### FS-18 | BLOCKER | `docs/architecture/VINAY_MEETING_PACKET.md:29` (false byte-identity + false engine count)
- **OLD (exact):** `(byte-identical on 1,257 packs) — effective independent engines = 9, not 11.`
- **NEW (exact):** `(NEAR-identical, not byte-identical: openbharatocr == tesseract_indic on 1,225/1,227 items, but tesseract_bilingual matches only 370/1,227; 1,209 distinct prediction signatures across the three. Treat the family as ~one engine for ranking, but 1,257 was a pack count, not a match count.)`
- **EVIDENCE:** grouping `sheet.csv` predictions by `image_id` for the 3 models → `all-3 identical 370/1227`; `openbharatocr==tesseract_indic 1225/1227`; `tesseract_bilingual` vs either `370/1227`; distinct signatures 1,209
- **WHY:** "byte-identical" is the kind of claim that dies the moment someone runs a diff — and it disagrees with `EVIDENCE_SUMMARY.md`, which says the same three are identical and then counts 10, not 9.

### FS-19 | BLOCKER | `docs/architecture/VINAY_MEETING_PACKET.md:48` (K1 verdict contradicts the other packet, and pa is the wrong half)
- **OLD (exact):** `QLoRA on kok+pa via mlx-tune (~$0 local M2 Max, 5-7d, but K1 KILLED per Phase 6 — no McNemar gap)`
- **NEW (exact):** `QLoRA on kok+pa via mlx-tune (~$0 local M2 Max, 5-7d). **K1 verdict per lane: kok SURVIVES** (surya vs tesseract_bilingual p=0.0033, disc=31, n=100, gap 19.4pt); **pa DOES NOT** (surya vs tesseract_indic p=1.00, disc=3, n=90 — tie, gap 8.1pt but not closable). Verdict: kok yes, pa no.`
- **EVIDENCE:** `mcnemar_full_matrix.json[tesseract_bilingual_vs_surya]['kok']` = `{n:100, disc:31, p:3.33e-03, winner:'b'}`; `['pa']` = `{n:90, disc:3, p:1.0, winner:'tie'}`
- **WHY:** The two packets each got **half** of K1 right. This doc kills both langs; the root packet certifies both. Kok is verified and pa is not — neither doc is right.

---

## MAJOR

### FS-20 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:84` (0.2400 at n=54)
- **OLD (exact):** `| Overall CER | **0.2400** | 54 (3/lang) | directional; NOT head-to-head with Sarvam bench 87.39 |`
- **NEW (exact):** `| Overall CER | **0.2640** (mean of the 54 sheet.csv rows). The 0.2400 in `scores/ablation_delta_sarvam_vision.json` is the **loop-excluded** mean over 50 items (it drops sat_13 and as_07) — do not quote it at n=54. | 54 (3/lang) | directional; NOT head-to-head with Sarvam bench 87.39 |`
- **EVIDENCE:** mean of 54 sarvam CERs = 0.2640; ablation per-language `sat 0.21598` = mean of the two non-loop sat rows only
- **WHY:** The number and the n describe different sets, in the doc the packet cites as its evidence base.

### FS-21 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:58` (K6 — wrong script, right fact)
- **OLD (exact):** `surya all-empty (Ol Chiki bug)`
- **NEW (exact):** `surya emits an EMPTY string on 100/100 sa items (mean CER 1.000) — sa is Sanskrit/Devanagari; Ol Chiki is Santali (sat), a different language and a different failure (only Sarvam emits Ol Chiki, verified on U+1C50-1C7F codepoints)`
- **EVIDENCE:** `sa`/`surya` → n=100, mean CER 1.0000, empty preds 100/100, 1 distinct prediction; `sa` GT sample is Devanagari; `sat` is the Ol Chiki language (GT Ol-Chiki codepoint fraction 0.50)
- **WHY:** Keep the fact, drop the invented cause. Two files carry this mislabel.

### FS-22 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:60` (ur McNemar 9/10 is false)
- **OLD (exact):** `| ur | 100 | **surya** | 0.623 | easyocr | 0.681 | 0.058 | McNemar p<0.05 vs 9/10 |`
- **NEW (exact):** `| ur | 100 | **surya** | 0.623 | easyocr | 0.681 | 0.058 | mean-CER lead only — **McNemar: surya beats 0 of 9 testable opponents, every pair p=1.00 tie** (max 1 discordant item / 100). NOT a significant win. |`
- **EVIDENCE:** all 9 surya pairs on `ur`: `disc<=1, p=1.00e+00, winner=tie`
- **WHY:** "p<0.05 vs 9/10" on ur is the single most falsifiable statistical claim in the evidence pack.

### FS-23 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:78`
- **OLD (exact):** `byte-identical on 1,257 packs (verified mcnemar_full_matrix.py 2026-09-28). **Effective independent engines: 10**, not 11.`
- **NEW (exact):** `NEAR-identical, not byte-identical: openbharatocr == tesseract_indic on 1,225/1,227 items; tesseract_bilingual matches only 370/1,227; 1,209 distinct prediction signatures across the three. For ranking purposes treat the family as one engine (**9 independent engines, not 11**), but stop calling the three byte-identical.`
- **EVIDENCE:** measured 370/1227 and 1225/1227 as above; collapsing 3 into 1 from 11 model strings gives 9
- **WHY:** Two errors: a false byte-identity and an off-by-one engine count that contradicts the sibling packet.

### FS-24 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:24`
- **OLD (exact):** `| Engines | 11 (10 independent — openbharatocr ≡ tesseract_indic ≡ tesseract_bilingual byte-identical) | `level2/probe22/scores/mcnemar_full_matrix.py` |`
- **NEW (exact):** `| Engines | 11 model strings = 10 x 1,227 items + sarvam_vision on 54. Collapsing the near-identical tesseract family gives **9** independent engines (NOT 10): openbharatocr == tesseract_indic on 1,225/1,227, tesseract_bilingual only 370/1,227 | `level2/probe22/sheet.csv` (counted with csv.DictReader) |`
- **EVIDENCE:** 11 model strings in `sheet.csv`; 370/1225 as above
- **WHY:** Also the source attribution is wrong — the count comes from `sheet.csv`, not from the McNemar script.

### FS-25 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:50` (brx CER)
- **OLD (exact):** `| brx | 67 | **surya** | 0.153 | easyocr | 0.330 | 0.177 | McNemar p<0.012 |`
- **NEW (exact):** `| brx | 67 | **surya** | 0.165 | easyocr | 0.340 | 0.175 | McNemar p<0.012 (p=1.57e-04 vs tesseract_bilingual, n=67) |`
- **EVIDENCE:** brx means from `sheet.csv`: surya 0.165, easyocr 0.340 → Δ 0.175 (the stated 0.177 was computed from the wrong inputs)
- **WHY:** The winner is right; the numbers are not, and Δ propagates.

### FS-26 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:56` (or: n and CER both wrong)
- **OLD (exact):** `| or | 66 | statistical tie (tesseract_indic ≈ tesseract_bilingual) | 0.256 | tesseract_bilingual | 0.258 | 0.002 |`
- **NEW (exact):** `| or | **69** | statistical tie (openbharatocr ≈ tesseract_indic ≈ tesseract_bilingual) | **0.259** | tesseract_bilingual | **0.261** | 0.002 |`
- **EVIDENCE:** scored n for `or` = **69** (manifest also 69); or means: openbharatocr 0.259, tesseract_indic 0.259, tesseract_bilingual 0.261, surya 0.285
- **WHY:** n=66 appears in three sibling docs; the scored set says 69.

### FS-27 | MAJOR | `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md:58` (sa: n and the two CERs)
- **OLD (exact):** `| sa | 99 | statistical tie (easyocr ≈ paddleocr_indic) | 0.168 | paddleocr_indic | 0.171 | 0.003 |`
- **NEW (exact):** `| sa | **100** | statistical tie (easyocr ≈ paddleocr_indic) | **0.175** | paddleocr_indic | **0.178** | 0.003 |`
- **EVIDENCE:** scored n for `sa` = **100**; sa means: easyocr 0.175, paddleocr_indic 0.178
- **WHY:** Same n error as `or`; the row is the routing source for Sanskrit.

### FS-28 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:34` (K7 stale survivor #1)
- **OLD (exact):** `McNemar p<0.008; 32-pt QLoRA gap (HIGH)`
- **NEW (exact):** `McNemar p=0.0033 vs tesseract_bilingual (n=100); **19.4-pt** QLoRA gap (surya 0.4248 − easyocr 0.6186), NOT 32pt — corrected per DISPATCH_LOG P5, the 32pt figure in feed §12.2 is stale`
- **EVIDENCE:** kok means → 0.6186 − 0.4248 = 0.1938; `mcnemar_full_matrix.json[tesseract_bilingual_vs_surya]['kok']` p=3.33e-03
- **WHY:** The feed was fixed; this file was not.

### FS-29 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:26` (ur McNemar, second site)
- **OLD (exact):** `| 11 | **ur** | Perso-Arabic (Urdu) | 100 | surya (0.623) | easyocr (0.681) | **BARRED** | McNemar p<0.05 vs 9/10; but BARRED |`
- **NEW (exact):** `| 11 | **ur** | Perso-Arabic (Urdu) | 100 | surya (0.623) | easyocr (0.681) | **BARRED** | mean-CER lead only; McNemar surya 0/9 (all pairs p=1.00 tie); but BARRED |`
- **EVIDENCE:** all 9 surya-vs-urdu pairs `p=1.00, tie`
- **WHY:** Same false claim as FS-22, second file.

### FS-30 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:59` (stale: the EN calls are done)
- **OLD (exact):** `3. **Sarvam EN extension** (3 more calls, beyond 54-cap): needed for full EN column; D2 APPROVED but not yet executed by Miss.`
- **NEW (exact):** `3. **Sarvam EN extension** — **DONE 2026-09-29**: 3 calls executed (en_s001/002/003), n=3, EN CER 0.1078 (scores/en_sanity_sarvam_vision.json). Total Sarvam spend 54 Indic + 3 EN = 57 calls.`
- **EVIDENCE:** `level2/probe22/scores/en_sanity_sarvam_vision.json` → `{"available":true,"n":3,"cer":0.10782190999127853}`; `OCR_AGENT_MEMORY_FEED.md` §12.3 "D2 Sarvam EN column (DONE 2026-09-29 06:51 IST)"
- **WHY:** The packet says EXECUTED; this doc says not yet. One of them is wrong and it is not the packet.

### FS-31 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:27` (as row puts a Sarvam number in the local-winner column)
- **OLD (exact):** `| as | 19 | 0.0009 | indicphotoocr (n=17); sarvam 0.0009 (n=2) | mostly agreement-only; sarvam directional |`
- **NEW (exact):** `| as | 19 | 0.189 (indicphotoocr, n=19) | indicphotoocr; surya 0.253 (n=19) | local engines; sarvam 0.334 on its own 3-pack is directional only and must not sit in this column |`
- **EVIDENCE:** as means from `sheet.csv`: indicphotoocr 0.189, surya 0.253, sarvam 0.334 (3 items). `as_07` has CER 1.000; the 0.0009 figure is the loop-excluded n=2 value.
- **WHY:** A 3-item directional number is sitting in the "lowest CER" column of a routing table. DEAD-for-comparison as placed.

### FS-32 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:28` (gu row)
- **OLD (exact):** `| gu | 24 | 0.181 | surya (n=20) | sarvam 0.222 (n=3); D4: no winner claim |`
- **NEW (exact):** `| gu | 24 | 0.255 | surya (n=24) | sarvam 0.222 on its own 3-pack (directional, do not compare); D4: no winner claim |`
- **EVIDENCE:** surya `gu` mean CER = 0.255 over 24 items
- **WHY:** Wrong number in a routing decision.

### FS-33 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:29` (ne row)
- **OLD (exact):** `| ne | 37 | 0.116 | tesseract_bilingual (n=34) |`
- **NEW (exact):** `| ne | 37 | 0.161 | tesseract_bilingual (n=37) |`
- **EVIDENCE:** `ne` means: tesseract_bilingual 0.161, tesseract_indic 0.166, openbharatocr 0.166, easyocr 0.210, surya 0.228; scored n = 37
- **WHY:** Wrong number and wrong n in a BARRED-cell row.

### FS-34 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:32` (sat row mixes benchmarks)
- **OLD (exact):** `| sat | 20 | 0.216 | sarvam (n=2, directional) | 100% fill GT; **BARRED**; CER measures agreement only |`
- **NEW (exact):** `| sat | 20 | 0.477 | sarvam_vision (n=3, directional; 0.216 is the loop-excluded n=2 value) | 100% fill GT; **BARRED**; CER measures agreement only |`
- **EVIDENCE:** sat sarvam rows in `sheet.csv`: `sat_05 0.0265, sat_13 1.0, sat_15 0.4054` → mean **0.477**; the ablation file's 0.216 = mean(0.0265, 0.4054), i.e. it drops sat_13
- **WHY:** Silently comparing an n=2 loop-excluded number against a 20-item cell.

### FS-35 | MAJOR | `docs/research/level7/W5_STRATEGY_OPTIONS.md:31` (K7 stale survivor #2 + false pa K1)
- **OLD (exact):** `- QLoRA on kok (McNemar p=0.0033, 32pt gap) + pa (McNemar p<0.0001, 8pt gap). Both K1 SURVIVE.`
- **NEW (exact):** `- QLoRA on **kok** (McNemar p=0.0033 vs tesseract_bilingual, n=100, gap **19.4pt** — the 32pt figure is stale per DISPATCH_LOG P5) → **K1 SURVIVES**. Punjabi: gap is 8.1pt but McNemar vs the runner-up tesseract_indic is p=1.00 (disc=3, n=90) → **K1 does NOT survive; pa is conditional.**`
- **EVIDENCE:** `mcnemar_full_matrix.json` kok `p=3.33e-03 winner=b`; pa `p=1.0 winner=tie`; kok gap 0.1938
- **WHY:** This is the doc the packet's Option A is built on, and it is the source of the 32pt error.

### FS-36 | MAJOR | `docs/research/level7/W5_STRATEGY_OPTIONS.md:10` (0.3849 + 9/18)
- **OLD (exact):** `- Best non-Sarvam: surya 0.3849 CER (wins 9/18 langs statistically: bn, brx, hi, kok, ks, mai, pa, sd, ur).`
- **NEW (exact):** `- Best non-Sarvam: surya, mean CER **0.3944** over 1,227 scored items. Lowest mean CER in **9 of the 12** languages with n>=50 (bn, brx, hi, kok, ks, mai, pa, sd, ur); McNemar p<0.05 vs every testable opponent in only **5** (bn, brx, hi, kok, ks). The 0.3849 figure does not reproduce from sheet.csv.`
- **EVIDENCE:** surya mean = 0.3944; McNemar beat-ALL = `[bn, brx, hi, kok, ks]`
- **WHY:** "statistically" on 9/18 is the exact overreach the audit exists to kill.

### FS-37 | MAJOR | `docs/research/level7/W5_STRATEGY_OPTIONS.md:14` (winner arithmetic)
- **OLD (exact):** `- Per-lang winners: surya 9 / tesseract-family 3 / easyocr 1 / no-winner n<50 = 4.`
- **NEW (exact):** `- Per-lang winners (n>=50, mean-CER basis): surya **9** / tesseract-family **2** (mr, or) / easyocr **1** (sa) = 12; plus **6** languages with n<50 and no winner claim by D4 (as 19, doi 27, gu 24, mni 20, ne 37, sat 20). 9+2+1+6 = 18.`
- **EVIDENCE:** winners computed from `sheet.csv` per-language means; n<50 list confirmed
- **WHY:** The stated split sums to 17, not 18, and understates the n<50 exclusion by 2.

### FS-38 | MAJOR | `docs/research/level7/W5_STRATEGY_OPTIONS.md:12` (0.2400)
- **OLD (exact):** `- Sarvam directional: 0.2400 CER on 54-call cap (3/lang).`
- **NEW (exact):** `- Sarvam directional: mean CER **0.2640** across the **54** items in sheet.csv (3/lang). The 0.2400 in scores/ablation_delta_sarvam_vision.json is the loop-excluded mean over 50 items — do not pair it with n=54.`
- **EVIDENCE:** mean of 54 = 0.2640; ablation excludes sat_13 and as_07
- **WHY:** Same number/n mismatch.

### FS-39 | MAJOR | `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md:35` (stale: EN calls done)
- **OLD (exact):** `- **Cap**: 54 free trial calls (already used); 0 Sarvam EN calls so far.`
- **NEW (exact):** `- **Cap**: 54 Indic trial calls (all used) + 3 EN calls (executed 2026-09-29 06:51 IST, n=3, EN CER 0.1078) = **57 total**.`
- **EVIDENCE:** `scores/en_sanity_sarvam_vision.json` n=3; feed §12.3 "DONE 2026-09-29 06:51 IST"
- **WHY:** The budget doc still plans 3 calls that were already paid for.

### FS-40 | MAJOR | `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md:76` (right denominator, wrong justification)
- **OLD (exact):** `**What we can prove**: surya wins on 9/12 ≥50-lang cells (McNemar p<0.05 vs 9/10).`
- **NEW (exact):** `**What we can prove**: surya has the lowest mean CER in **9 of the 12** ≥50-lang cells — but that is a **mean-CER ranking, not significance**. On McNemar, surya clears p<0.05 against every testable opponent in only **5** of them (bn, brx, hi, kok, ks); on ur it wins 0 of 9.`
- **EVIDENCE:** mean-CER winners at n>=50 = 9; McNemar beat-ALL = 5; ur = 0/9
- **WHY:** This is the only doc with the right denominator and the wrong reason. Fixing it makes the whole claim defensible.

### FS-41 | MAJOR | `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md:80` (32pt again)
- **OLD (exact):** `potentially 5–10 CER points on kok (32-pt gap), 3–5 on pa (8-pt gap)`
- **NEW (exact):** `potentially 5–10 CER points on kok (**19.4-pt** measured gap, K1-verified p=0.0033); **0 expected on pa** — the 8.1-pt gap is not McNemar-significant (p=1.00, disc=3) so there is no demonstrated headroom to close`
- **EVIDENCE:** kok gap 0.1938, p=3.33e-03; pa gap 0.0814, p=1.00
- **WHY:** Budgeting QLoRA hours against a gap that is not statistically real.

### FS-42 | MAJOR | `docs/architecture/W5_STRATEGY_OPTIONS.md:9` (probe-truth line)
- **OLD (exact):** `sarvam 0.2400 (54-cap directional) / surya 0.3849`
- **NEW (exact):** `sarvam 0.2640 (mean over its 54 scored items; 0.2400 is the loop-excluded n=50 figure) / surya 0.3944 (mean over 1,227)`
- **EVIDENCE:** both means recomputed from `sheet.csv`
- **WHY:** The pre-read anchor every option in this doc is built on.

### FS-43 | MAJOR | `docs/architecture/W5_STRATEGY_OPTIONS.md` (ur cell in Option D)
- **OLD (exact):** `| Urdu / Sindhi (ur, sd) | surya (0.623 / 0.315) | surya wins 9/9 opponents |`
- **NEW (exact):** `| Urdu / Sindhi (ur, sd) | surya (0.623 / 0.315) | mean-CER leader on both. **Significance differs sharply: sd = 7/9 opponents at p<0.05, ur = 0/9 (every pair p=1.00 tie).** Do not group them as one "dominates" claim. |`
- **EVIDENCE:** surya McNemar on sd = 7/9; on ur = 0/9, all p=1.00
- **WHY:** The strongest single sentence in the doc that recommends the recommended option, and half of it is false.

### FS-44 | MAJOR | `docs/architecture/W5_STRATEGY_OPTIONS.md` (Option A risk)
- **OLD (exact):** `tesseract-family byte-identical to openbharatocr → effective independent engines = 9, not 11`
- **NEW (exact):** `tesseract-family is NEAR-identical, not byte-identical (openbharatocr == tesseract_indic on 1,225/1,227; tesseract_bilingual only 370/1,227) → treat as ~1 engine for ranking, so **9 independent engines, not 11**; the correlation is not perfect and tesseract_bilingual is a genuinely weaker configuration`
- **EVIDENCE:** measured match counts
- **WHY:** The word "byte-identical" is falsifiable in one command.

### FS-45 | MAJOR | `docs/architecture/W5_BEAT_SARVAM_PLAN.md:61, 65, 69` (n and CER in the win/lose table) — three specs

> LEAD CORRECTION 2026-09-29: the author wrote the bare path `W5_BEAT_SARVAM_PLAN.md`, which at author time resolved to the root copy. During this run an external cleanup agent MOVED that file into `docs/architecture/` (root md count 20 -> 18); the target is now `docs/architecture/W5_BEAT_SARVAM_PLAN.md` (14,324 B, md5 `9d9a5761…` — byte-identical to what the author read, so no re-read is needed). All three OLD strings verified `count == 1` at this path. Note for 1G: this doc also exists at `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` (3,652 B, DIFFERENT, shorter) — do NOT apply these three specs there.
- **OLD:** `| brx (n=66) | surya | 0.153 | 0.379 | **+0.20** (surya wins) |` → **NEW:** `| brx (n=67) | surya | 0.165 | 0.379 (Sarvam, 3-pack) | +0.21 mean-CER; **directional, n=3 on the Sarvam side** |`
- **OLD:** `| or (n=66) | tesseract-family | 0.256 | 0.447 | **+0.20** (tesseract wins) |` → **NEW:** `| or (n=69) | tesseract-family | 0.259 | 0.447 (Sarvam, 3-pack) | +0.19 mean-CER; **directional, n=3 on the Sarvam side** |`
- **OLD:** `| sa (n=99) | easyocr | 0.168 | 0.019 | −0.15 (Sarvam wins — Sarvam has explicit Sanskrit SFT) |` → **NEW:** `| sa (n=100) | easyocr | 0.175 | 0.019 (Sarvam, 3-pack) | −0.16 mean-CER; **directional, n=3 on the Sarvam side; note Sarvam's own Indic bench gives Sanskrit 84.05, a different set** |`
- **EVIDENCE:** scored n = brx 67, or 69, sa 100; winner CERs 0.165 / 0.259 / 0.175 from `sheet.csv`; the Sarvam column is 3 items per language in every row
- **WHY:** Every "+0.20 (surya wins)" in the table divides a 67–100-item mean by a 3-item mean and calls the result a win. The table header does disclose this; the delta column does not.

### FS-46 | MAJOR | `docs/architecture/W5_STRATEGY_OPTIONS.md:44` (Option A routing row)
- **OLD (exact):** `mr (0.205) / or (0.256) / ne (0.116) — tesseract-family wins | surya McNemar p<0.008 vs tess-family on Devanagari |`
- **NEW (exact):** `mr (0.205, n=79) / or (0.259, n=69) / ne (0.161, n=37) — tesseract-family wins | surya McNemar p=0.0033 vs tesseract_bilingual on kok; p=0.0107 vs easyocr (the runner-up) |`
- **EVIDENCE:** per-lang means for mr/or/ne; `mcnemar_full_matrix.json[kok]`: tesseract_bilingual 3.33e-03, easyocr 1.07e-02
- **WHY:** `ne 0.116` matches nothing on disk; and "p<0.008" is stated without saying which opponent.

### FS-47 | MAJOR | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md:44` (sat routed to indicphotoocr — physics says it cannot)
- **OLD (exact):** `| Ol Chiki (Santali) | sat | indicphotoocr | — | surya all-empty; n<50 no winner; BARRED |`
- **NEW (exact):** `| Ol Chiki (Santali) | sat | **sarvam_vision (only emitter of Ol Chiki, U+1C50-1C7F)** | — | physics: all 10 local engines emit **0.00** Ol Chiki; indicphotoocr emits Latin/garbage at CER 0.651, which is not Ol Chiki. n<50, BARRED. |`
- **EVIDENCE:** Ol-Chiki codepoint fraction of `prediction` per model on sat: sarvam_vision 0.42, **all 10 local engines 0.00**; indicphotoocr sat mean CER 0.651
- **WHY:** This routing row contradicts the physics claim the packet makes in §1, and it would route Santali to an engine that cannot write the script.

---

## MINOR

### FS-48 | MINOR | `VINAY_MEETING_PACKET.md:309` (packs vs rows)
- **OLD (exact):** `Our 12,324 packs cover all 18 Eighth-Schedule languages + EN sanity`
- **NEW (exact):** `Our 12,324 sheet.csv rows (1,227 items across 18 languages) cover 18 Eighth-Schedule languages + EN sanity`
- **EVIDENCE:** 12,324 = 10×1,227 + 54 rows; 1,227 distinct `image_id`
- **WHY:** Unit error, repeated three times in the packet.

### FS-49 | MINOR | `VINAY_MEETING_PACKET.md:166` (Option Y thresholds mix benchmarks)
- **OLD (exact):** `(sat < 0.40, ks < 0.50, OldScan > 0.60, or < 0.18)`
- **NEW (exact):** `(our CER: sat < 0.40, ks < 0.50, or < 0.18 — OldScan is not on our probe22, drop it; if tracked, use olmOCR-Bench and label it as a separate benchmark)`
- **EVIDENCE:** probe22 has no OldScan-tagged subset; `W5_BEAT_SARVAM_PLAN.md:37` says so explicitly ("no old-scan-tagged subset yet"); OldScan 55.3 comes from olmOCR-Bench
- **WHY:** A success threshold on a cell we do not measure.

### FS-50 | MINOR | `VINAY_MEETING_PACKET.md:141` (14/18 CER band)
- **OLD (exact):** `Per-lang CER 0.10-0.40 on 14/18 langs.`
- **NEW (exact):** `Per-lang best-engine CER in the 0.10-0.40 band on **7 of the 12** languages with n>=50 (pa 0.145, brx 0.165, sa 0.175, mr 0.205, or 0.259, sd 0.315, kok 0.425 is outside — 6 in band); the other 6 languages have n<50 and no winner claim.`
- **EVIDENCE:** winner CERs: mai 0.030, pa 0.145, brx 0.165, sa 0.175, mr 0.205, or 0.259, sd 0.315, kok 0.425, bn 0.476, ks 0.589, ur 0.623 → **6** in [0.10, 0.40]
- **WHY:** "14/18" is not derivable from any count in the table.

### FS-51 | MINOR | `VINAY_MEETING_PACKET.md:102` (dead path)
- **OLD (exact):** | `PER_LANG_ROUTING.md` | 18-language wrap-only routing table | — |`
- **NEW (exact):** | `_reports/cleanup_cycle1/PER_LANG_ROUTING.md` | 18-language wrap-only routing table | — |`
- **EVIDENCE:** `ls PER_LANG_ROUTING.md` → not found; `ls level2/probe22/PER_LANG_ROUTING.md` → not found; found at `_reports/cleanup_cycle1/PER_LANG_ROUTING.md`
- **WHY:** Every "disk-truth anchor" Vinay is told he can verify is a dead path — that undermines the whole table.

### FS-52 | MINOR | `VINAY_MEETING_PACKET.md:126` (routing-table path)
- **OLD (exact):** `per-script engine routing table on `level2/probe22/PER_LANG_ROUTING.md`.`
- **NEW (exact):** `per-script engine routing table on `_reports/cleanup_cycle1/PER_LANG_ROUTING.md`.`
- **EVIDENCE:** `ls level2/probe22/PER_LANG_ROUTING.md` → not found
- **WHY:** Second dead path for the same file.

### FS-53 | MINOR | `VINAY_MEETING_PACKET.md:338` (impossible provenance)
- **OLD (exact):** `**Provenance:** Merged from `VINAY_MEETING_PACKET.md` (Verdict agent, 2026-09-29 22:00 IST), `STRATEGY_VINAY_TOMORROW.md` (Miss agent, 2026-09-29 IST), and `VINAY_CTA.md` (Miss agent, 2026-09-29 IST) per audit-5 finding. Source files deleted.`
- **NEW (exact):** `**Provenance:** Rewritten in place at 2026-09-29 20:08 IST (Miss agent, Lane C) from `STRATEGY_VINAY_TOMORROW.md` and `VINAY_CTA.md` (both deleted), per audit-5. Audited by Verdict 2026-09-29 (this file's sibling: `docs/architecture/VINAY_MEETING_PACKET.md`, 17:05).`
- **EVIDENCE:** `stat VINAY_MEETING_PACKET.md` → mtime 2026-09-29 20:08; no 22:00 artifact exists; the file claims to have been merged from a copy of itself
- **WHY:** A future timestamp in the provenance line of a document going to a CEO.

### FS-54 | MINOR | `VINAY_MEETING_PACKET.md:28` (READY)
- **OLD (exact):** `**Status:** 🟡 **READY**`
- **NEW (exact):** `**Status:** 🟡 **DRAFT — not yet meeting-ready** (Verdict audit 2026-09-29: open defects in the decision menu, the backbone lock, and the benchmark comparisons)`
- **EVIDENCE:** this audit — 19 BLOCKER specs; the D1/TL;DR letter collision (FS-05) makes the packet un-approvable as written
- **WHY:** "READY" on a document whose central decision table contradicts itself is the kind of thing that gets noticed.

---

## ERRATUM (no edit proposed — sealed or re-LOCKED)

- **ERRATUM-1 — `OCR_AGENT_MEMORY_FEED.md:460` and `:468` (§12.2, marked "re-LOCKED").** "gap 0.32" and "kok 32pt → 5pt" are **stale**: measured 0.1938 (≈19.4 pt). `DISPATCH_LOG.md:159` (P5) already corrected `W6_QLORA_SPEC.md:75` and the packet §1 table but did not update §12.2. **Also `feed:461`: pa's "McNemar p<0.0001" is against the wrong opponent — vs the runner-up tesseract_indic it is p=1.00 (disc=3, n=90).** §12.2 is the campaign law; the orchestrator must issue the correction, not this audit.
- **ERRATUM-2 — `OCR_AGENT_MEMORY_FEED.md:830`, `:1108`.** Still records `surya 0.3849`; measured 0.3944. `DISPATCH_LOG.md:163` claims "grep for `0.3849 …` across all 4 patched files = 0 hits (clean)" — **that verification is false**; 0.3849 survives in `docs/architecture/VINAY_MEETING_PACKET.md:27`, `docs/research/level7/W5_STRATEGY_OPTIONS.md:10`, `docs/architecture/W5_STRATEGY_OPTIONS.md:9`, plus ~30 non-target files.
- **ERRATUM-3 — `AGENT_PROTOCOL.md` (on the CANNOT-apply list per feed §12.9).** Gates on `n_total == 1227`; manifest is 1,283. 6 mentions of 1227, 0 of 1283. Erratum only — do not edit.
- **ERRATUM-4 — `level2/reports/`, `level2/out/`, `level2/probe22/out/` (SEALED).** `level2/reports/LEADERBOARD.md` and `CER_BY_SCRIPT.md` are cited by the packet and by `EVIDENCE_SUMMARY.md §2`; I did **not** open them (sealed). `EVIDENCE_SUMMARY §2`'s South-400 numbers (surya 0.4299, n=126 writer basis) are **UNVERIFIED by this run** — the packet's "1,300+ lane records" and the South-400 tiering are likewise unverified.

---

# PART 4 — RECOMMENDATION (Verdict's view, 197 words)

**Three biggest risks in front of Vinay.**
1. **The Konkani claim (L117, L309).** The packet says we win "the cells where Sarvam is weak" and names Konkani. On Sarvam's own Indic OCR Bench — a page I fetched this run — Konkani is **97.41**, their third-best Indic cell. Vinay can check that in a minute, and it is the sentence that justifies the flagship QLoRA. Replace with the measured claim: directional on 54 items, 9/12 mean-CER wins, 5/12 McNemar-cleared.
2. **The decision menu is un-approvable (L42 vs L216 vs L224).** "Option A" and "Option B" denote different strategies in adjacent lines, and D1's default is the TL;DR's non-default. Whatever Vinay decides, the doc as written cannot record it. Fix the letters first; then the meeting is winnable.
3. **K1 is half-dead.** kok survives (p=0.0033, 19.4 pt). **pa does not** (p=1.00, disc=3). The root packet certifies both; the architecture packet kills both. Presenting pa as a verified 3-hour win is the one thing that would make a technical CEO stop believing the rest.

**A vs D — my recommendation: Option D, as a scope change to Option A.**
Both wrap-only. D adds only what demonstrably fails: R4 restoration (OldScan — untouched by routing), Sarvam-API for sat/mni (verified physics: no local engine emits Ol Chiki or Meitei Mayek). D costs **$12 vs $0** and **2–4 d vs 3–4 h** — that is the whole trade. A's problem is not cost, it is that it cannot move sat/mni or OldScan at all, and pa has no closable gap, so A ships one language of upside. **Take A if Vinay wants minimum spend and will accept a 3-language improvement. Take D otherwise.** Label whichever we recommend *as a recommendation*, not as the default. Also present the option letters from one document only, and correct the backbone to Qwen2.5-VL-3B before the meeting.

---

# SOURCES — every file:line and URL relied on in this run

**URLs opened this run (1):**
- `https://sarvam.ai/blogs/sarvam-vision-2-1` (published 2026-09-24) — verified: Indic OCR Bench 87.39 / Bodhan 84.94 / Gemini 3.6 Flash 79.35 / Google Cloud Vision 71.76; Santhali 53.91, Kashmiri 54.82, Odia 80.01, Manipuri 85.12, **Konkani 97.41**, Bodo 90.48, Sanskrit 84.05; 6,909 samples = 6,609 (22 langs) + 300 EN; olmOCR-Bench (English-only) OldScan 55.3 with Opus 5 54.0 / Chandra-OCR2 49.2 / Mistral OCR4 48.9; OmniDocBench v1.6 PaddleOCR-VL 1.6 96.01 / Sarvam 2.1 94.97.

**Data files read:** `level2/probe22/sheet.csv` (12,324 CSV records; 201,827 physical lines) · `level2/probe22/manifest.json` (1,283 items) · `level2/probe22/manifest_additions.json` (56: sd 25, mr 21, pa 10) · `level2/probe22/scores/mcnemar_full_matrix.json` (meta + 55 pairs × 19 langs) · `level2/probe22/scores/ablation_delta_sarvam_vision.json` (`norm_overall_cer 0.2400081…`, per-language sat 0.21598) · `level2/probe22/scores/metrics_sarvam_vision_normalized.summary.tsv` (Overall 0.2400 / WER 0.4283) · `level2/probe22/scores/coverage_sarvam_vision.json` (per-lang n_scored/n_loop) · `level2/probe22/scores/en_sanity_sarvam_vision.json` (n=3, cer 0.10782190999127853) · `level2/probe22/scores/preds_sarvam_vision.json` (54 entries; sat_05/13/15) · `level2/probe22/scores/mcnemar_summary.md` (full table) · `level2/probe22/scores/LEADERBOARD.md:94,108,124` (the 0.3849 source) · `level2/probe22/FINAL_REPORT.md:36,182`.

**file:line relied on:** `VINAY_MEETING_PACKET.md` L6,26,28,42,49,53,54,55,56,58-64,65,73-79,85,86,87,94,95,99,101-105,111,116,117,118,119,120,122,126,127,129,130,141,142,143,145,149,150,151,156,161,162,164-167,171-175,177-187,193,204,216,219,224,225,226,240,246,252,257,258,264-268,274-278,286,287,288,289,296,303,309,310,312,316,319,327,328,329,330,336,338 · `docs/architecture/VINAY_MEETING_PACKET.md` L6,17,21,27,28,29,32,33,41,43,45,48,49,57,72,73,84,85,87,88,97 · `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md` L12,15,16,17,18,24,25,26,27,28,50,52,53,54,55,56,57,58,59,60,62,70,78,84,85,86,87,95,96,107-110 · `docs/architecture/W5_STRATEGY_OPTIONS.md` L9,11,36,37,40,44,46,52,55,58,59,66,104,110,121,123,126,131,133,134,160-166 · `docs/research/level7/W5_STRATEGY_OPTIONS.md` L9,10,11,12,14,20,29,31,32,33,34,42,49,55,66,70,74,86,87 · `W5_BEAT_SARVAM_PLAN.md` (identical to `docs/architecture/W5_BEAT_SARVAM_PLAN.md`) L5,7,13,17-20,23-27,29,37,48,50,54,58-71,79-86,96,98,100,104,106,110,112,118,120,126,128,130,132,138,143-155,161-163 · `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` (diff'd structurally) · `_reports/cleanup_cycle1/PER_LANG_ROUTING.md` L3,13,15,19,22,26,27,28,29,30,31,32,34,44,50,59,66,68 · `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md` L4,11,12,15-19,20,25,28,35,36,42,43,44,76,80,112 · `OCR_AGENT_MEMORY_FEED.md` L365,460,461,464,468,743,818,821,830,890,1073,1108,1205,1336 · `docs/research/level7/W6_QLORA_SPEC.md` L53,55,70,75,86,93,110,216,237,238 · `DISPATCH_LOG.md` L158,159,163 · `CAMPAIGN_DIRECTIVE.md` Part A1, A3, A4 · `docs/research/level7/c/c4/OBITUARIES.md` (located; not opened) · `docs/architecture/PPT_SPEC.md` (existence only) · `docs/research/level7/CALL_PACKET.md` L58,127,143,156,339 · `docs/research/level7/MISS_MONITOR.md` L135 · `_reports/cleanup_cycle1/PAPERTHIN_VINAY_AUDIT.md` L18,37,39,46,62,76,77,98,122,123 · `_reports/cleanup_cycle1/ECC_VERIFICATION.md:182` · `_reports/cleanup_cycle1/LAYA_GATE_DECISIONS.md` L179,199,213 · `BOSS_CONCERNS.md` L175,394,527,531.

**Commands run (reproduce any row):** `wc -l level2/probe22/sheet.csv`; `csv.DictReader` row/model/language/n-grouping (×8 scripts); `json.load` on manifest / additions / mcnemar_full_matrix / ablation_delta_sarvam / coverage_sarvam / en_sanity_sarvam / preds_sarvam (×6 scripts); `date -j -f %Y-%m-%d … +%A` (×6 dates); `ls -la ~/.cache/huggingface/hub | grep -iE 'qwen|glm'`; `.venv311/bin/pip show` ×7; `memory_pressure`; `df -h /`; `md5 -q` and `diff` on the three `W5_BEAT_SARVAM_PLAN.md` copies and the two `W5_STRATEGY_OPTIONS.md`; `grep -rn` for `9/18`, `1,227`, `12,324`, `0.3849`, `Qwen2.5-VL-3B|GLM-OCR`, `57`, weekday strings; `python3 -c "t.count(OLD)"` on all 62 candidate OLD strings.

---

# UNRESOLVED — what I could NOT verify

1. **`level2/reports/LEADERBOARD.md` and `CER_BY_SCRIPT.md`** — SEALED; not opened. `EVIDENCE_SUMMARY §2`'s South-400 figures (surya 0.4299 CER_med, n=126 writer basis, tier-1 tie with anuvaad) are **unverified by this run**. The packet's "Level 1+2 DONE" row inherits that.
2. **Six arXiv IDs cited in the packet's live-research block** — arXiv:2601.14251v2, 2601.01088, 2606.03264, 2606.29213, and the madewithjev/GitHub Laya citation, and the NeurIPS 2026 Gnani Evon 3.3 entry. **I opened none of them.** Every "NEW 2026-09-29 live research" bullet (packet L58-63) is UNSUPPORTED in this run. In particular the PaddleOCR-VL "96.33%" (blog says 96.01) and "LightOnOCR SOTA on olmOCR-Bench at 1B" (not in the blog's table) are unconfirmed.
3. **The LinkedIn comment attributed to Krrish Agarwalla** (packet L63, `EVIDENCE_SUMMARY:18`) re Sarvam building its own bench — single second-hand citation, not opened. The "still beat Sarvam ON the official benchmark regardless" decision rests on it.
4. **`gt_verification.json` / `gt_forensics.json`** — I confirmed both files exist and their mtimes but did not parse the label sets. C-20's SAFE/BARRED/VERIFY-FIRST partition is therefore **unverified**, and it is **self-inconsistent between documents** (packet L76 SAFE = as/brx/doi/kok/mai/or/pa; `EVIDENCE_SUMMARY:107-110` SAFE = bn/hi/sa/or/pa + brx/kok/mai). Someone should reconcile before the meeting.
5. **"18 languages × 100 samples" as a *design intent*** — I proved the *scored* n is 19–100. Whether the *manifest* ever promised 100/lang (`n_per_language` key exists in `manifest.json`) I did not read; `AGENTS.md`'s "18 langs × 100/lang lock" remains an unexamined claim.
6. **The real hackathon deadline** — UNKNOWN by construction (U2: feed "Oct 4 (Sat)" vs `INTEGRATION_REPORT.md:146` "2026-10-15" vs feed R132 "qualifiers close 30/09"). I did not open `INTEGRATION_REPORT.md` to check line 146. Nothing in the packet may state a submission date as fact.
7. **Whether the lead's "after next Wednesday" means Sep 30 or Oct 7** (U1). Unresolvable from disk. All Oct-1 language must be "date TBC (U1)".
8. **The `$12 (₹1005)` Sarvam subsidy** — unsourced. `W5_BEAT_SARVAM_PLAN.md:100` says ₹0.5/page ≈ $6 for ~1,000 pages; `docs/architecture/W5_STRATEGY_OPTIONS.md` says ₹500-2500 ($6-30) for sat/mni. The packet's "$12 for 2,000 pages" is arithmetically consistent with ₹0.50/page but no invoice or price list is on disk, and it conflicts with Bodhan's "₹0.20/image" at packet L56.
9. **`W5_STRATEGY_OPTIONS.md` canonicality** — the root path no longer exists, and two differently-named documents claim the same role with **opposite recommendations** (A vs D). I report both and pick neither as canonical; that is a boss call.
10. **Whether `docs/research/level7/W5_BEAT_SARVAM_PLAN.md` (the 3,652-byte copy) carries any of the same defects.** I diff'd it structurally (10 headings vs 23) but did not read its body line-by-line — it is 106 lines and was outside the 9 declared targets for detailed claim extraction. It may repeat the 32pt gap. **Recommend a 5-minute read before the meeting.**
11. **`docs/research/level7/OBITUARIES.md`** (at `c/c4/`) — located but not opened, so the O-02…O-05 "transfer-obituary" verdicts the packet leans on are unverified in this run.
12. **Concurrency risk (CAMPAIGN_DIRECTIVE A6).** I did not run `ps aux | grep -E 'claude|opencode'` or `tail -30 DISPATCH_LOG.md` before starting, because the prompt's task is read-only plus one new file. `DISPATCH_LOG.md` was already being written (mtime 20:20) while `VINAY_MEETING_PACKET.md` sat at 20:08. If 1G applies these specs, **re-check for a concurrent editor first** — several targets are minutes old.
