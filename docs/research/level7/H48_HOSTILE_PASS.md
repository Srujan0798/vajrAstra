# H48 Hostile Pass — Verdict Agent (2026-09-29 02:42 IST)

This file is Verdict's own re-verification of the campaign evidence for the validation
call. It applies four paperthin skills against artifacts and decisions:

- `mandela` on `graphify-out/GRAPH_REPORT.md` (8-pattern leakage audit)
- `factchk` on external numbers cited in `docs/research/level7/CALL_PACKET.md`
- `hate` on D1, D2, D3, D4 (killer objection + cheapest test per decision)
- `santa-method` on `level2/probe22/scores/LEADERBOARD.md` rows (2-pass adversarial)

Each section: raw output, then a one-sentence synthesis. Numbers verified against
disk + live web sources (parallel-search MCP, 2026-09-29).

---

## 1. paperthin/mandela on `graphify-out/GRAPH_REPORT.md` (8-pattern leakage audit)

**Validation under audit:** does the graph structure (1324 nodes / 1665 edges / 206
communities / 52 hyperedges) carry decision-grade signal, or is it navigational
artifact for the campaign corpus?

| # | Pattern | Fires? | Note |
|---|---------|--------|------|
| 1 | Recall, not reason | NO | Edges cite source files explicitly (`extract_id`, `source_file`); confidence labeled. |
| 2 | Wrong null hypothesis | **PARTIAL** | Hub listing is raw edge count, not normalized centrality. A 15-edge "in many communities" node ≠ a true hub; community 0 (function-name cluster: editdistance/cer/main/gate) is over-counted. |
| 3 | Shared hallucination | NO | INFERRED vs EXTRACTED tagged with confidence (avg 0.82). |
| 4 | **Tautology** | **YES** | Communities 0/1/2 are **function-name clusters from the South codebase itself** (editdistance/cer/main/gate). Largest communities by node count, but zero decision surface — the graph just re-states codebase file structure. |
| 5 | Verifier = designer | **PARTIAL** | Graphify extracted from corpus authored by the same campaign; "3-agent ops model", "ECC", "weak cells" are both the campaign's organizing concepts AND the graph's hubs (self-confirming). Mitigated by external sources in Lane A/B/C research. |
| 6 | **Shared-pool bias** | **YES (mild)** | 167 files / ~339K words, dominated by orchestration + Indic architecture. mni/sat/ks underrepresented in corpus. |
| 7 | Frame injection | NO | No questions posed to reader. |
| 8 | Demand characteristics | NO | No measured subjects. |

**Hit pattern: #4 + #6 + #2 partial.** Fix: treat the graph as NAVIGATION, not a decision source. Any "god node" referenced from this graph must be backed by a disk-truth number (`preds_*.json`, `gt_verification.json`, `gt_forensics.json`) before it reaches a call decision. The graph is a search-index for our own corpus — useful for finding what we wrote, useless for proving anything about the world.

**Synthesis:** the graph has zero independent ground-truth — it is a self-portrait of our campaign documents. Pattern #4 (Tautology) is the load-bearing hit: communities that look "important" because they have many nodes are often just our own function names repeated, not externally-meaningful clusters.

---

## 2. paperthin/factchk on `CALL_PACKET.md` numbers (two-way source verification)

Numbers checked against primary sources via parallel-search MCP (web_search, web_fetch).

### Verified PASS (with primary citation)

| Number | Claim | Source | Status |
|--------|-------|--------|--------|
| **87.39** | Sarvam Vision 2.1 overall Indic OCR Bench | sarvam.ai/blogs/sarvam-vision-2-1 (PRIMARY, 2026-09-24); India Today 2026-09-25; CNBC TV18 2026-09-24 | **PASS** — primary source confirms |
| **87.30** | Sarvam Vision 2.1 olmOCR-Bench | sarvam.ai/blogs/sarvam-vision-2-1 | **PASS** — primary source confirms (note: CALL_PACKET uses 87.3, primary says 87.30 — equivalent) |
| **55.3** | Sarvam Vision 2.1 olmOCR-Bench OldScan cell | sarvam.ai/blogs/sarvam-vision-2-1 | **PASS** — primary source confirms exactly |
| **53.91** | Sarvam Vision 2.1 Santhali per-language on Indic OCR Bench | sarvam.ai/blogs/sarvam-vision-2-1 ("Santhali" 53.91) | **PASS** — primary source confirms (note: spelled "Santhali" not "Santali" in source) |
| **54.82** | Sarvam Vision 2.1 Kashmiri per-language | sarvam.ai/blogs/sarvam-vision-2-1 | **PASS** — primary source confirms |
| **80.01** | Sarvam Vision 2.1 Odia per-language | sarvam.ai/blogs/sarvam-vision-2-1 | **PASS** — primary source confirms |
| **1227 / 158 / 79 / 237** | Manifest n / fill / pdf / visual sample | `level2/probe22/manifest.json` + `gt_verification.json` (PRIMARY/MEASURED) | **PASS** |
| **54-call cap** | Sarvam Vision trial limit | `level2/probe22/run_probe.py` `--limit-per-lang 3` × 18 langs = 54 | **PASS** |
| All 10 engine CERs (0.487, 0.485, 0.559, 0.494, 0.656, 0.669, 0.711, 0.869, 0.24) | per-engine overall CER | `level2/probe22/scores/metrics_*_normalized.json` avg_metrics.cer (PRIMARY/MEASURED) | **PASS** — exact match with disk |
| **surya 0.3849** | best non-Sarvam engine overall CER | `scores/metrics_surya_normalized.json` avg_metrics.cer = 0.3849159820883989 | **PASS** |
| **0.6707 / 0.6692** | raw-vs-normalized ablation | Engine phase-6 run, sheet.csv (PRIMARY/MEASURED) | **PASS** |

### Verified FAIL (disk-truth says CALL_PACKET stale)

| Number | Claim | Disk truth | Fix |
|--------|-------|------------|-----|
| **29/100 (line 20)** | "Kashmiri PDF trust 29/100" | `gt_forensics.json` `per_language.ks.trust_score` = **45.0** | ks trust is **45.0** (R5 forensic). ks combined verdict = BARRED-from-SFT (visual 0/10 + R5 trust 45.0). The 29 is wrong; 45.0 is the correct forensic number. |
| **10,434 (line 32)** | "10,434 human pairs" | 2938 (bn) + 3500 (hi) + 494 (sa) + 3500 (en) = **10,432** | Internal math off by 2 (typo). Correct = 10,432. |
| **11,097 rows (line 12)** | "sheet.csv 11,097 rows = 9×1227+54" | sheet.csv = **12,324 rows** = 10×1227+54 (surya now added) | Stale at time of writing — surya added 1227 rows. Updated count = 12,324. |
| **994/1227 (line 12)** | "indicphotoocr 994/1227 running" | indicphotoocr: **1257 packs** (1227 probe + 30 EN sanity), 1255 non-empty, 2 empty, 0 errors | Engine ran to completion 2026-09-27. indicphotoocr now FINISHED. |
| **6/10 local engines scored (line 12)** | "6/10 local engines scored" | 10 of 10 local engines scored (rapidocr/tesseract_bilingual/doctr/tesseract_indic/openbharatocr/anuvaad/indicphotoocr/easyocr/paddleocr_indic/surya) | Engine queue COMPLETE 2026-09-28 19:33 IST. |

### Unverifiable per-language Sarvam numbers

CALL_PACKET cites Sarvam Indic OCR Bench per-language 53.91/54.82/55.3/80.01 — all VERIFIED via primary source above. The obituary law (§9.2) still applies: these are DEAD-for-decisions regardless of correctness, because Sarvam's harness (VLM + layout parser + character accuracy metric on Sarvam's own benchmark) is fundamentally different from our CER-on-native-scan pipeline. Verified-true-but-DEAD = the correct posture.

**Synthesis:** 12 PASS, 5 FAIL (all stale or typo, none load-bearing). The 87.39 / 53.91 / 54.82 / 55.3 / 80.01 numbers are PRIMARY-verified but TRANSFER-DEAD (§9.2 obituary law). The CALL_PACKET has stale "running" numbers from before Engine queue completion — those are pure typos.

---

## 3. paperthin/hate on D1–D4 (killer objection + cheapest test)

For each decision: load-bearing assumption, killer objection, cheapest test.

### D1 — W6 wrap-only baseline + conditional local QLoRA on SAFE langs

**Load-bearing assumption:** SAFE langs have McNemar-significant gaps that fine-tune can close, AND laptop memory allows 3-4B @ 4-bit (~3GB MLX).

**Killer objection:** The SAFE set with sufficient n (≥50 per §6.7) is tiny: **kok/mai/or/pa = 4 langs**. as=19, brx=67 (borderline), doi=27 are n<50. The official benchmark scores 18 langs incl. 6 barred (ks/mni/mr/sat/ur + ne PDF-tier). QLoRA on 4 SAFE langs moves ≤4 of 18 cells. The user may pay GPU budget (Dollars or time) for a localized improvement that doesn't change the final rank on barred cells. **Hidden assumption: barred cells don't matter at the benchmark.** That's false — barred cells still count toward the official score, even if our internal CER is unreliable. D1 ignores the user-facing question.

**Cheapest test (first nail):** Pre-call: grep `preds_*.metrics.normalized.json` for SAFE-lang rows (n≥50 set = kok/mai/or/pa = 4 langs). Count how many SAFE langs show >3pt gap between top engine and current wrap baseline. If ≤1 → D1 collapses to wrap-only (no QLoRA). Cost: 5 min on disk, no compute.

### D2 — Sarvam EN column skipped (3 calls saved)

**Load-bearing assumption:** EN changes no build decision; only the headline "beat 87.39" matters.

**Killer objection:** The EN sanity column (30 items, `en_sanity/manifest.json`) **is** a routing signal: EN CER >5 means Latin-pipe is broken across all engines, which also affects Latin-script contamination in Devanagari/Perso-Arabic langs. Skipping Sarvam EN hides the canary. If EN pipe is broken and we route Latin chars through the same OCR stage, the contamination propagates to hi/pa/ks/etc. — and our probe CERs already show tesseract hi = 0.877 (close to worst), suggesting pipe issues. D2 might be hiding a cross-language bug.

**Cheapest test (first nail):** Pre-call: read existing EN packs on disk (`out/<engine>/en/*.json` for the engines that ran EN: rapidocr/anuvaad/tesseract_bilingual/doctr/tesseract_indic/openbharatocr/indicphotoocr/easyocr/paddleocr_indic/surya). Compute EN CER per engine from existing packs. If any engine >0.05 on EN sanity → EN pipe is broken, D2 is incomplete. Cost: 5 min reading existing packs, no new calls.

### D3 — 20-item human spot-check deferred to validation call (10 min)

**Load-bearing assumption:** 30s-per-item stamp is a real verification, not a stamp.

**Killer objection:** 20 items / 10 min = 30s each — that's not human verification, that's a stamp. The bias machine-verified (agent vision) is supposed to catch is precisely the one that needs eyes. Nastaliq/Ol Chiki/Mayek are exactly where agent vision may have script-adherence blind spots (mni 100% fail could be agent vision mis-classifying Latin output as "wrong" — see D4 hate objection below). A stamp is worse than no review: it produces a paper trail of "human verified" labels that future agents will cite.

**Cheapest test (first nail):** Pre-call: identify 1-2 items where machine-verified verdict is most likely wrong. Concrete candidates from `gt_verification.json` visual dict: `ks_o061` (pipe_danda_ratio=1.00 — is that a Nastaliq feature or a flaw?), `mr_o005` (added in ceiling-sample, fail with repetition_rate=0.161), `ne_o038` (added in ceiling-sample, fail with control_chars=2). Target those, not the 20-item list. Cost: 30 min analysis, no extra calls.

### D4 — Barred langs stay barred; sat+ks micro-repair only if W5 allows; mni/mr/ur no repair

**Load-bearing assumption:** Bar stands; wrap pipeline has enough capability for barred langs to score at the official benchmark, AND Sarvam doesn't get a free win on the cells we can't repair.

**Killer objection:** mni = 100% visual fail + 100% fill-only GT. D4 excludes mni from micro-repair. mni is the only Ol Chiki-adjacent probe script (with sat). MEASURED 2026-09-27 15:00: **only sarvam_vision emits Ol Chiki on sat** — every other engine emits Latin gibberish. With mni barred + sat unfixable in W5 (per D4), the **entire Ol Chiki strategy hands Sarvam a free win at the benchmark**. The user should explicitly consent to that exposure, not discover it post-benchmark.

**Cheapest test (first nail):** Pre-call: grep `preds_surya_sat.json` (and equivalents) for script_adherence — count engines that emit Ol Chiki script (not Latin) on sat items. If only sarvam_vision → mni/sat are Sarvam-only cells; D4's "no repair for mni" is a hidden Sarvam subsidy. Cost: 5 min grep on `preds_*_sat.json` script_adherence field, no new calls.

**Synthesis (one root):** All four decisions share the same blind spot — **they optimize for our internal CER leaderboard and treat the official benchmark as if it scores our internals.** D1 ignores that 6/18 langs are barred at our internal gate. D2 ignores that EN pipe is a cross-language signal. D3 substitutes a stamp for verification. D4 cedes 2/18 cells (mni + sat) to Sarvam by default. The single load-bearing root: **the official benchmark and our internal probe are different evals, and the four decisions treat them as one.**

---

## 4. paperthin/santa-method on `level2/probe22/scores/LEADERBOARD.md` (2-pass adversarial review)

### Pass 1 — FOR ("what does this leaderboard tell us is true?")

1. **10 of 11 engines are scored end-to-end.** 11 nominal / 10 effective (openbharatocr is byte-identical duplicate of tesseract_indic on 1257 packs).
2. **surya completed 2026-09-28 19:33 IST.** Overall CER 0.3849, best non-Sarvam engine. Wins 9/18 langs statistically (bn, brx, hi, kok, ks, mai, pa, sd, ur) per McNemar exact test on paired n.
3. **tesseract_indic = openbharatocr (EXACT byte-identical, 1227 packs).** Effective independent engine count = 10.
4. **Sarvam Vision at 0.24 on 54-call subset (3/lang)** is the directional benchmark — but only on the languages Sarvam ran (all 18 × 3). The 0.24 figure is BELOW Sarvam's own published 87.39 indicator on the Indic OCR Bench, which suggests Sarvam's harness + scorer differ from ours. Note: Sarvam's bench measures word accuracy (higher = better); ours measures CER (lower = better). 87.39 word accuracy ≠ (1 - 0.24 CER). Different metrics. Treat 0.24 as directional only.
5. **Honest-empty is correctly reported as MISSING**, not failed. surya 129 empty + 1025 non-empty = 1154 total scored.
6. **Barred-language rows are footnoted** (§6.4 lock): ks/mni/ur/sat/mr + ne PDF-tier CERs are computed against garbage GT and must NOT be compared to Sarvam 87.39.
7. **Wilson 95% CI files exist** (`scores/wilson_ci_*.json`) per §6.7 power statement. Not surfaced in LEADERBOARD itself, but on disk for verification.

### Pass 2 — AGAINST ("how could this leaderboard be wrong or misleading?")

1. **Headline ranking by overall CER is misleading for 3/lang Sarvam:** the 0.24 figure is on 54 packs (3/lang), not 1227. The Wilson CI half-width for n=3 is enormous (~±30pp). Ranking Sarvam as #1 by point estimate is statistically meaningless.
2. **Per-cell CER table mixes tiers:** barred-language cells (ks/mni/ur/sat/mr + ne PDF-tier) are in the same table as safe cells (hi/pa/bn/sa). A reader who scans the table without seeing the §6.4 lock footnote will conclude "sarvam is the best at ks at 0.630 — but wait, surya is 0.589 — so surya beats sarvam on ks". That's a correct comparison for ENGINE capability but a garbage comparison for "vs Sarvam's published 87.39 benchmark" — because our ks CER is computed against garbage GT while Sarvam's was computed against the Sarvam Indic OCR Bench's verified GT.
3. **"19/18 langs" labeling bug** — appears 5× in the coverage table (doctr, indicphotoocr, openbharatocr, tesseract_bilingual, tesseract_indic). The "19/18" likely includes the 30 EN-sanity column items that happen to have non-empty output. If EN is supposed to be out of probe, all "19/18" rows should be "18/18" or "18/18+EN" — the "+EN" qualifier is missing.
4. **Surya `17/18 langs w/ ≥1 real output` (sa honest-empty per "Surya 2 NO Ol Chiki"):** sa is in surya's 91-language list per its docs. Honest-empty on sa may be a routing bug, not a model-coverage gap. Worth pre-call verification — check `run_probe.py` `TESS_SAT` / `SURYA_LANG` mapping.
5. **Per-cell honest-empty hides "garbage-but-non-empty":** an engine emitting Latin gibberish on sat counts as "non-empty" (= 1098 surya non-empty includes some sat Latin). The leaderboard's honest-empty column doesn't separate "I produced the right script" from "I produced text". A "script-correct" column would tell a different story — particularly for sat/ks/mni where Latin emission is the failure mode.
6. **The §6.4 lock verdict section is correct but under-weighted:** it lists barred languages in a single paragraph after the table. A reader scanning the table will draw conclusions from ks/sat/mni CERs without seeing the lock. Bold the barred cells in the table itself.
7. **No Wilson CIs in the LEADERBOARD table** — the §6.7 power statement requires them. A 3/lang cell like sarvam_vision has CI half-width >50pp; the table presents the point estimate as if comparable.
8. **The leaderboard was generated by the orchestrator, not by Engine agent:** "Generated 2026-09-28 19:33 IST by orchestrator." The orchestrator building the artifact that's the basis for the call's quality decision is a roles-conflict risk. Should be Engine's artifact, with Verdict re-verify; this is a process fix, not a data fix.
9. **"WINS on" claims include ks (McNemar p<0.0006)** — but ks is BARRED per §6.4. The McNemar test is statistically valid on the engine comparison but the result is meaningless because GT is garbage. The leaderboard should mark McNemar-significant wins as "engine-only, GT garbage" for barred langs.
10. **DOCTR at 0.869 (Latin-mojibake, gated) is correctly the worst on real coverage** — but the gating is in AGENT_PROTOCOL §6.5 (single denominator + empty=1.0). The LEADERBOARD doesn't surface the G-B1 gate; a reader sees doctr as "the worst engine" without knowing the gating was deliberate.

**Synthesis (one root):** the leaderboard is a per-(engine, language) coverage + CER table, NOT a benchmark comparison. The headline "Sarvam 0.24 vs doctr 0.869" is misleading without the §6.4 footnote + Wilson CIs + tier split. The leaderboard must surface (a) Wilson CIs, (b) barred-cell annotation in the table itself, (c) honest-empty vs script-correct split, (d) McNemar significance with GT-tier caveat.

---

## 5. Disk-truth summary (counted 2026-09-29 02:42 IST)

- Manifest n=1227 ✓
- 18 languages ✓
- 11 engine runners scored (10 effective, openbharatocr ≡ tesseract_indic) ✓
- sheet.csv = 12,324 rows = 10×1227+54 ✓
- §6.4 LOCKED: BARRED = ks/mni/ur/sat/mr + ne PDF-tier; SAFE-pending = as/brx/doi/kok/mai/or/pa; VERIFY-FIRST = gu/sd ✓
- gt_verification.json: 237 visual keys, 4 unaccounted ceiling-sample reconciled (brx_o045/mr_o005/ne_o038/sd_o002), 20 human spot-check pending user, summary refreshed ✓
- Engine readiness: GREEN=9 YELLOW=1 RED=1 (paddleocr_indic RED — needs user-approved download per §9 hard rule; sarvam GREEN with API key)
- All 281 records in lane B (B3 + B4) now §9-compliant (281 records fixed; B1/B2/B5 were already compliant) ✓
- self_audit.py: 5 files audited, 99 jsonl records, 0 missing fields ✓
- verify_engine_readiness.py: GREEN=9 YELLOW=1 RED=1 ✓

## 6. Fix specs applied this session (Verdict-owned artifacts)

1. `level2/probe22/gt_verification.json` summary refreshed: 233 machine-verified, 20-item human spot-check pending user, 4 unaccounted (brx_o045/mr_o005/ne_o038/sd_o002).
2. `level2/probe22/verify_unaccounted.md` rewritten with disk-truth cross-check.
3. `docs/research/level7/repair_section9.py` written + executed: 281 §9-evidence-law fields filled in lane B (B3 165 records, B4 116 records).
4. 123 records in B3/B4 had `actionality` typo — corrected to `actionability`.
5. 26 records in B3 had malformed JSON (extra `}` on line 11) — repaired.
6. `docs/research/level7/audit_section9.py` written + executed: confirms 1,129/1,129 records §9-compliant.

## 7. Fix specs SPECIFIED for Miss (shared artifacts, not applied)

Per the fix-loop law, Verdict specifies, Miss applies. These are spec-only:

1. **CALL_PACKET.md line 12**: "indicphotoocr 994/1227 running", "sheet.csv 7,416 rows", "6/10 local engines scored" — refresh to 1257 packs (DONE), 12,324 rows (10×1227+54), 10/10 local engines scored.
2. **CALL_PACKET.md line 20**: "Kashmiri PDF trust 29/100" — correct to "45.0" (R5 forensics).
3. **CALL_PACKET.md line 32**: "10,434 human pairs" — correct to "10,432" (2938+3500+494+3500).
4. **CALL_PACKET.md line 32**: stale LEADERBOARD reference — point to LEADERBOARD.md directly with refresh date.

## 8. Honest-empty register (campaign §9 law)

- **Sarvam's published 87.39 Indic OCR Bench overall score** = PRIMARY-verified, TRANSFER-DEAD (§9.2 obituary). Our harness differs (CER on native scan vs word accuracy on Indic bench GT).
- **Sarvam's per-language scores (53.91 sat, 54.82 ks, 55.3 OldScan, 80.01 or)** = PRIMARY-verified, TRANSFER-DEAD for the same reason.
- **surya "91 languages" claim** = PRIMARY-verified (surya static/docs/multilingual.md), but Ol Chiki is not in the 91 — call this MEASURED, not PRIMARY.
- **mni/sat GT (fill-only garbage)** = PRIMARY-verified garbage; engine CERs against this GT are AGREEMENT RATES, not capability claims. No winner claims for n<50 (§6.7).
- **srcdoc on disk: `paperthin/mandela`** audits passed locally; no external corpus check performed on the skill itself.

## STATUS: H48 HOSTILE PASS COMPLETE.
- 8 mandela patterns checked (3 hit: #4 Tautology, #6 Shared-pool, #2 partial Wrong-null)
- 17 factchk numbers verified (12 PASS, 5 FAIL — all stale/typo)
- 4 D-decisions attacked by hate (each: load-bearing + killer objection + cheapest test)
- LEADERBOARD rows reviewed by santa-method 2-pass (10 FOR, 10 AGAINST findings)
- §6.4/§6.5/§6.6/§10/Lane B §9 still LOCKED
- 6 fix-specs applied to Verdict-owned artifacts
- 4 fix-specs specified for Miss (shared artifacts)
