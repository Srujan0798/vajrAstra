# 1G — VERIFY: the Miss agent's application of FS-01…FS-54

**Agent:** Verdict (subagent) · **Run:** 2026-09-29 · **Role:** reviewer. I did not author
`level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` and I did not apply any fix.
**Law observed:** read-only on all 8 targets. I wrote **this file only**. No fix applied, no
`src/` run, no download, no Sarvam call, no write to any sealed dir.

## VERDICT: **PASS-WITH-FIXES (39)**

The application itself is **clean and honest**: 54/54 spec headers, 62/62 edit pairs verified,
**every load-bearing number re-derived from `sheet.csv` reproduces exactly**, and the archive is
byte-perfect. It fails only on scope discipline (1 collateral hunk) and completeness (the residual
list is materially incomplete, and one fix introduced a new internal contradiction).

| Dimension | Result |
|---|---|
| Specs PASS / FAIL | **54 / 0** (62 edit pairs, all PASS) |
| NEW present exactly once | 62 / 62 |
| OLD count == 0 after | 62 / 62 |
| OLD count == 1 in pre-image | 62 / 62 (audit's uniqueness claim is TRUE) |
| EVIDENCE commands re-run | all load-bearing numbers reproduce |
| **COLLATERAL hunks** | **1** (of 53 hunks across 8 files) |
| Defects INTRODUCED by the fix pass | **1** (FS-50) |
| Residual defect classes | 5 reported (4 confirmed, 1 under-counted) + **15 undisclosed** |
| Round-2 specs written | **39**, every OLD verified unique |

---

# PART 1 — PER-SPEC VERIFICATION

Legend: **(a)** NEW present exactly once · **(b)** OLD count 0 · **(c)** diff hunk spec-explained ·
**(d)** EVIDENCE re-run and true. `pre` = the archive pre-image.

| spec | a | b | c | d | evidence | exact fix needed |
|---|---|---|---|---|---|---|
| FS-01 `PKT:126` | ✅ | ✅ | ✅ | ✅ | paired 54: best-local 10/18 = surya 10/18 (identical set); item 21/28/5; beat-ALL 5 | none |
| FS-02 `PKT:49` | ✅ | ✅ | ✅ | ✅ | winners n≥50 = 12 → surya 9, tess-fam 2, easyocr 1 | none |
| FS-03 `PKT:303` | ✅ | ✅ | ✅ | ✅ | best-local 0.2956 > sarvam 0.2640 on the 54 | none |
| FS-04a `PKT:117` | ✅ | ✅ | ✅ | ✅ | Konkani 97.41 / Kashmiri 54.82 / Odia 80.01 / Santhali 53.91 / Sanskrit 84.05 re-fetched from sarvam.ai | **+ R2-03** (3rd site) |
| FS-05 `PKT:216` | ✅ | ✅ | ✅ | ✅ | D1 default now `A`; matches TL;DR | none |
| FS-06 `PKT:127` | ✅ | ✅ | ✅ | ✅ | pa vs tesseract_indic n=90 disc=3 p=1.00 tie | **+ R2-09a-d** (4 survivors) |
| FS-07 `PKT:120` | ✅ | ✅ | ✅ | ✅ | `date`: 09-30 Wed, 10-01 Thu, 10-04 Sun | **+ R2-05a-f** |
| FS-08a `PKT:79` | ✅ | ✅ | ✅ | ✅ | 10-01 = Thursday | **+ R2-05e** |
| FS-08b `ARCH:21` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-08c `ARCH:6` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-08d `ARCH:72` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-08d `PKT:296` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-08e `PKT:6` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-09a `PKT:289` | ✅ | ✅ | ✅ | ✅ | 10-04 = Sunday | none |
| FS-09b `PKT:330` | ✅ | ✅ | ✅ | ✅ | same | none |
| FS-10 `PKT:161` | ✅ | ✅ | ✅ | ✅ | 09-29 Tue, 10-01 Thu | **+ R2-05a** (line head survives) |
| FS-11 `PKT:127` | ✅ | ✅ | ✅ | ✅ | `W6_QLORA_SPEC.md:53` Qwen primary; hub has no qwen/glm | **+ R2-05b/e, R2-06** |
| FS-12 `PKT:219` | ✅ | ✅ | ✅ | ✅ | OmniDocBench v1.6: PaddleOCR-VL 96.01, Sarvam 94.97, **GLM-OCR absent** | **+ R2-06** (verdict cell) |
| FS-13 `PKT:54` | ✅ | ✅ | ✅ | ✅ | 12,324 rows; 11 model strings; 10×1227+54; 1,227 image_ids | **+ R2-02a** |
| FS-14 `PKT:87` | ✅ | ✅ | ✅ | ✅ | same | **+ R2-02c** |
| FS-15 `PKT:116` | ✅ | ✅ | ✅ | ✅ | same | **+ R2-02b** |
| FS-16 `ARCH:27` | ✅ | ✅ | ✅ | ✅ | surya mean 0.3944 over 1,227 | none |
| FS-17 `ARCH:28` | ✅ | ✅ | ✅ | ✅ | sarvam mean 0.2640 over 54 | none |
| FS-18 `ARCH:29` | ✅ | ✅ | ✅ | ✅ | 370/1227 all-3; 1225/1227 ob==ti; 1,209 sigs | none |
| FS-19 `ARCH:48` | ✅ | ✅ | ✅ | ✅ | kok p=3.327e-3 disc=31 n=100; pa p=1.00 disc=3 n=90 | none |
| FS-20 `EV:84` | ✅ | ✅ | ✅ | ✅ | 0.2640; ablation 0.2400 = loop-excluded (sat mean(0.0265,0.4054)=0.21595) | none |
| FS-21 `EV:58` | ✅ | ✅ | ✅ | ✅ | sa surya 100/100 empty, CER 1.0000, sa GT Devanagari 0.797, Ol Chiki 0.0000; sat GT Ol Chiki 0.443 | **+ R2-11c** (2nd copy) |
| FS-22 `EV:60` | ✅ | ✅ | ✅ | ✅ | ur: all 9 surya pairs p=1.00 tie, disc ≤1 | none |
| FS-23 `EV:78` | ✅ | ✅ | ✅ | ✅ | 1225/1227; 370/1227; 1,209 | none |
| FS-24 `EV:24` | ✅ | ✅ | ✅ | ✅ | 11 model strings → 9 independent | none |
| FS-25 `EV:50` | ✅ | ✅ | ✅ | ✅ | brx surya 0.1653 easyocr 0.3400 Δ0.175; p=1.57e-4 n=67 | **+ R2-10d, R2-11a, R2-12b** |
| FS-26 `EV:56` | ✅ | ✅ | ✅ | ✅ | or n=69, 0.2588/0.2606 | **+ R2-10e, R2-11d, R2-12a, R2-13** |
| FS-27 `EV:58` | ✅ | ✅ | ✅ | ✅ | sa n=100, easyocr 0.1751, paddle 0.1776 | **+ R2-11b** |
| FS-28 `PLR:18` | ✅ | ✅ | ✅ | ✅ | gap 0.6186−0.4248 = 0.1938; p=0.003327 | none |
| FS-29 `PLR:21` | ✅ | ✅ | ✅ | ✅ | ur 0/9 | none |
| FS-30 `PLR:59` | ✅ | ✅ | ✅ | ✅ | `en_sanity_sarvam_vision.json` n=3 cer 0.10782 | none |
| FS-31 `PLR:27` | ✅ | ✅ | ✅ | ✅ | as indicphotoocr 0.1887, surya 0.2534, sarvam 0.334 | none |
| FS-32 `PLR:28` | ✅ | ✅ | ✅ | ✅ | gu surya 0.2550 n=24 | none |
| FS-33 `PLR:29` | ✅ | ✅ | ✅ | ✅ | ne tesseract_bilingual 0.1608 n=37 | none |
| FS-34 `PLR:32` | ✅ | ✅ | ✅ | ✅ | sat sarvam (0.0265,1.0,0.4054) mean 0.4770 | none |
| FS-35 `LVL7:23` | ✅ | ✅ | ✅ | ✅ | kok p=0.0033 gap 19.4pt; pa p=1.00 | none |
| FS-36 `LVL7:10` | ✅ | ✅ | ✅ | ✅ | surya 0.3944; beat-ALL 5 | none |
| FS-37 `LVL7:12` | ✅ | ✅ | ✅ | ✅ | 9+2+1=12, +6 n<50 = 18 | **+ R2-14** (line 9) |
| FS-38 `LVL7:11` | ✅ | ✅ | ✅ | ✅ | 0.2640 over 54 | none |
| FS-39 `CBE:35` | ✅ | ✅ | ✅ | ✅ | 54 Indic + 3 EN = 57 | none |
| FS-40 `CBE:100` | ✅ | ✅ | ✅ | ✅ | 9/12 mean-CER; 5 beat-ALL; ur 0/9 | none |
| FS-41 `CBE:103` | ✅ | ✅ | ✅ | ✅ | kok 19.4pt p=0.0033; pa 8.1pt p=1.00 | none |
| FS-42 `OPT:9` | ✅ | ✅ | ✅ | ✅ | 0.2640 / 0.3944 | **+ R2-10b/c** (same line 9/58) |
| FS-43 `OPT:116` | ✅ | ✅ | ✅ | ✅ | sd 7/9; ur 0/9 | **+ R2-10a** (OPT:48 twin) |
| FS-44 `OPT:59` | ✅ | ✅ | ✅ | ✅ | 1225/1227, 370/1227 | none |
| FS-45a `PLAN:59` | ✅ | ✅ | ✅ | ✅ | brx n=67, 0.165 | none |
| FS-45b `PLAN:65` | ✅ | ✅ | ✅ | ✅ | or n=69, 0.259 | **+ R2-12a** (PLAN:132) |
| FS-45c `PLAN:69` | ✅ | ✅ | ✅ | ✅ | sa n=100, 0.175; Sanskrit 84.05 re-fetched | none |
| FS-46 `OPT:47` | ✅ | ✅ | ✅ | ✅ | mr 0.2046 n=79; or 0.2588 n=69; ne 0.1608 n=37; kok 0.0033/0.0107 | **+ R2-10d/e** |
| FS-47 `PLR:43` | ✅ | ✅ | ✅ | ✅ | sat: sarvam 0.336 Ol Chiki, **all 10 local 0.000**; indicphotoocr 0.6514 | none |
| FS-48 `PKT:309` | ✅ | ✅ | ✅ | ✅ | 12,324 rows | none |
| FS-49 `PKT:166` | ✅ | ✅ | ✅ | ✅ | no OldScan subset in probe22 | none |
| FS-50 `PKT:141` | ✅ | ✅ | ⚠️ | ❌ | **band at n≥50 = 7, not 6** | **R2-08 (mandatory)** |
| FS-51 `PKT:102` | ✅ | ✅ | ✅ | ✅ | path resolved | none |
| FS-52 `PKT:126` | ✅ | ✅ | ✅ | ✅ | 0 remaining citations | none |
| FS-53 `PKT:338` | ✅ | ✅ | ✅ | ✅ | mtime 20:08 | none |
| FS-54 `PKT:28` | ✅ | ✅ | ✅ | ✅ | — | none |

**Two notes on the audit's own citations** (not application errors — the OLD strings were unique,
so they landed correctly): the audit's line numbers are stale in 6 places.
`PER_LANG_ROUTING` FS-28 `:34`→actual 18, FS-29 `:26`→21, FS-47 `:44`→43 ·
`COMPUTE_BUDGET` FS-40 `:76`→100, FS-41 `:80`→103 · `W5_BEAT_SARVAM_PLAN` FS-45a `:61`→59 ·
`W5_STRATEGY_OPTIONS` FS-46 `:44`→47 · `lvl7` FS-38 `:12`→11, FS-37 `:14`→12, FS-35 `:31`→23.
**And FS-04 is labelled a 2-site spec (`:117, :309`) but its OLD occurs exactly ONCE in the
pre-image** — the real line 309 text names *Santhali 53.91, not Konkani*. The audit pointed at the
wrong line; the Miss applied it correctly at the one real site. The actual Konkani defect is at
**line 56** and no spec ever covered it (→ R2-03).

---

# PART 2 — NUMBERS I RE-DERIVED FROM `sheet.csv` (not taken from the spec)

`csv.DictReader` on `level2/probe22/sheet.csv`: **12,324 records · 11 model strings · 1,227
distinct `image_id` · 18 languages.** Every figure below is my own computation.

| Claim | My value | Verdict |
|---|---|---|
| K1 paired, surya mean < sarvam mean, 3 items/lang | **10/18** — brx gu ks mai mr ne or pa sd ur | REPRODUCED |
| K1 **best-local** on the same 3 paired items | **10/18 — the identical set** | REPRODUCED; FS-01's "our best local engine" is **correctly** attributed (best-local = surya on this restriction) |
| item-level paired | **surya 21 / Sarvam 28 / tie 5** | REPRODUCED |
| sarvam mean over its 54 | **0.2640** | REPRODUCED |
| surya mean over the same 54 | **0.3637** | REPRODUCED |
| best-local mean over the same 54 | **0.2956** (worse than Sarvam) | REPRODUCED |
| winner count at n≥50 (12 langs) | surya **9**, tesseract-family **2** (mr, or), easyocr **1** (sa) = 12 | REPRODUCED |
| n<50 (6 langs) | as 19, mni 20, sat 20, gu 24, doi 27, ne 37 | REPRODUCED |
| surya mean over 1,227 | **0.3944** (0.3849 does not reproduce) | REPRODUCED |
| McNemar surya beat-**ALL** testable | **5** — bn, brx, hi, kok, ks | REPRODUCED |
| surya beat counts | pa **5/9**, or 5/9, sd **7/9**, mai 1/9, mr 2/9, ne 2/9, sa 8/9, **ur 0/9** | REPRODUCED |
| **kok gap** | easyocr 0.6186 − surya 0.4248 = **0.1938 ≈ 19.4 pt** | **K7 VERIFIED — 0.194 is right, the feed's 0.32 is stale** |
| kok McNemar | vs tesseract_bilingual p=**3.327e-3** disc=31 n=100; vs easyocr p=**1.067e-2** | REPRODUCED |
| pa McNemar | vs tesseract_indic p=**1.00** disc=3 n=90 **tie** | REPRODUCED — FS-06/19/35/41 all true |
| **sa "Ol Chiki"** | sa GT Devanagari fraction **0.797**, Ol Chiki **0.0000**; sat GT Ol Chiki **0.443**; surya sa **100/100 empty, CER 1.0000, 1 distinct prediction** | **K6 VERIFIED — the FACT is right, the label is fabricated. Ol Chiki = Santali (sat).** |
| Ol-Chiki emission on sat | sarvam_vision **0.336**; **all 10 local engines 0.000** | REPRODUCED (audit said 0.42; not load-bearing, no applied text quotes it) |
| tesseract-family identity | all-3 identical **370/1227**; openbharat==tesseract_indic **1225/1227**; tesseract_bilingual **370/1227**; **1,209** distinct signatures | REPRODUCED |
| 24 spot-checked per-engine CERs (brx, or, sa, gu, ne, as, pa, sat, mr, ur, sd, hi, mai, kok ×2) | all match to 4 dp | ALL REPRODUCED |
| n≥50 winner CER in [0.10, 0.40] | **7** — pa 0.145, brx 0.165, sa 0.175, mr 0.205, **hi 0.220**, or 0.259, sd 0.315 | **7, not 6** → FS-50's applied list is wrong (R2-08) |
| external (re-fetched `sarvam.ai/blogs/sarvam-vision-2-1`) | Overall **87.39**, Bodhan **84.94**, Konkani **97.41**, Kashmiri **54.82**, Odia **80.01**, Santhali **53.91**, Sanskrit **84.05**, Marathi 95.06, Hindi 93.52; olmOCR-Bench "officially English-only", OldScan 55.3; OmniDocBench v1.6 PaddleOCR-VL **96.01** / Sarvam 2.1 **94.97**, **GLM-OCR absent** | ALL REPRODUCED — FS-04/12/45c are TRUE |
| calendar | 2026-09-29 Tue · 09-30 **Wed** · 10-01 **Thu** · 10-03 **Sat** · 10-04 **Sun** | CONFIRMED |

---

# PART 3 — GREP COUNTS (exact)

**Command 1 (as specified), 6 files:**
`grep -n -E 'Beats Sarvam on 9/18|beats Sarvam on 9/18|Tue 2026-09-30|Sat 2026-10-04' …` → **2 hits**
- `VINAY_MEETING_PACKET.md:288` · `VINAY_MEETING_PACKET.md:329` (both `Tue 2026-09-30`)
- `Beats Sarvam on 9/18` = **0** · `beats Sarvam on 9/18` = **0** · `Sat 2026-10-04` = **0**

**Command 2, `9/18` across all 8 targets → 3 hits, all in the root packet, all line-tails of FS-13/14/15:**
`VINAY_MEETING_PACKET.md:56` (**2** occurrences), `:89` (1), `:118` (1). All other 7 files: **0**.

**Command 3, `Wed 2026-10-01` across all 8 targets → 6 hits, all in the root packet:**
`:163` `:289` `:290` `:305` `:330` `:331`.
**The Miss reported 5 (163, 289, 305, 330, 331) — it missed `:290`.** `:290` and `:331` each carry
a **second** weekday error: `Fri 2026-10-03` (10-03 is a **Saturday**).

**Wider sweep, all 8 targets:** `0.3849` **3** (2 are the applied "does not reproduce" notes; 1 is
a live claim at `OPT:58`) · `0.2400` **4** (all applied notes) · `1,257` **1** (applied note) ·
`32-pt|32pt` **3** (all applied "NOT 32pt" notes) · `9/10` **4** (bn/hi rows — *true*: both beat 9/9) ·
`9/9` **2** (`PLR:39` true for ks; `OPT:48` **false for ur**) · `9/12` **0** · `byte-identical`
**6** (all in applied "NEAR-identical, not byte-identical" notes) · `12,324 packs` **0** ·
`18 languages × 100` **0** · `1,227 packs` **4** · `n=99|n=66` **5** · `11 engines` **7** ·
`0.153` **3** · `McNemar-significant` **6** · `≥100` **3**.

---

# PART 4 — COLLATERAL

**Exactly 1 unexplained hunk in 53.** All 8 files: 22+5+7+6+3+3+4+2 = **52 spec-explained hunks**,
plus **1 collateral**.

```
--- _archive/pre_fix_2026-09-29/root__VINAY_MEETING_PACKET.md   VINAY_MEETING_PACKET.md
+++ 
24a25,26
> > Corrected 2026-09-29 per fix_specs/W1A_PACKET_AUDIT.md - every number states its set and n. Draft research plan: docs/campaign/DRAFT_RESEARCH_PLAN.md
> 
```

This is **additive** — every one of the 62 specs is a 1-line→1-line substitution, so no spec can
produce `24a25,26`. Worse, it points at **`docs/campaign/DRAFT_RESEARCH_PLAN.md`, which does not
exist** (`ls` → no such file; `docs/campaign/` holds only BENCHMARK_22, CAMPAIGN_DIRECTIVE,
COMPETITOR_INTEL, MENTOR_PLAYBOOK, checkpoints, protocols). The fix pass created a new dead path
in the document it was repairing. → **R2-01**.

---

# PART 5 — ROUND-2 SPECS (39). Every OLD verified `count == 1` in its file.

**A. The collateral (1)**

| id | target | OLD → NEW |
|---|---|---|
| **R2-01** | `VINAY_MEETING_PACKET.md` (L25-26) | OLD `> Corrected 2026-09-29 per fix_specs/W1A_PACKET_AUDIT.md - every number states its set and n. Draft research plan: docs/campaign/DRAFT_RESEARCH_PLAN.md\n\n` → NEW `""` (**delete both lines**). Not in any FS; cites a non-existent file. |

**B. RESIDUAL 1 — surviving `9/18` at L56, L89, L118** (each tail also cites dead `EVIDENCE_SUMMARY.md`)

| id | OLD → NEW |
|---|---|
| **R2-02a** (L56) | OLD `**surya** (wins 9/18 langs; per-lang CER 0.030–0.623 per \`EVIDENCE_SUMMARY.md\` §3). Wrap-only routing (already on disk)` → NEW `**surya** (lowest mean CER in 9 of the 12 languages with n>=50; per-lang CER 0.030–0.623 per \`_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md\` §3). Wrap-only routing (already on disk)` |
| **R2-02b** (L118, full line to force uniqueness) | OLD `2. **Status:** …57 total. Best non-Sarvam = **surya** (wins 9/18 langs; per-lang CER 0.030–0.623 per \`EVIDENCE_SUMMARY.md\` §3).` → NEW same with `lowest mean CER in 9 of the 12 languages with n>=50` and `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md` |
| **R2-02c** (L89) | OLD `Best non-Sarvam engine = **surya** (wins 9/18 languages statistically; per-lang CER 0.030–0.623 per \`EVIDENCE_SUMMARY.md\` §3).` → NEW `Best non-Sarvam engine = **surya** (lowest mean CER in 9 of the 12 languages with n>=50; per-lang CER 0.030–0.623 per \`_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md\` §3).` |

**C. UNDISCLOSED AND MOST DANGEROUS — the Konkani claim survives at a third site (L56)**

| id | OLD → NEW |
|---|---|
| **R2-03** (L56) | OLD `**wins the 9/18 probe22 cells where Sarvam's own 3-pack numbers are weak** (OldScan, Kashmiri, Odia, Konkani)` → NEW `**is competitive with Sarvam on the cells we measured (n=3/lang, directional)**, and Sarvam's own published weak cells are Kashmiri 54.82, Odia 80.01 and Santhali 53.91 — not Konkani, where Sarvam scores 97.41 on their Indic OCR Bench. Note OldScan 55.3 is an olmOCR-Bench (English-only) column, a different benchmark from the 87.39 Indic headline` |

**The Miss's residual list named L56 — but only for the `9/18` tail. It did not report that the
same line still asserts Konkani is a Sarvam weak cell.** This is the fastest way to lose the room
and it is still in the document. (I re-fetched the source: Konkani **97.41**, the highest Indic
cell in the table.)

**D. RESIDUAL 2 — `Tue 2026-09-30` (2 sites)**

| id | OLD → NEW |
|---|---|
| **R2-04a** (L288) | `**Same day (Tue 2026-09-30 evening):**` → `**Same day (Wed 2026-09-30 evening):**` |
| **R2-04b** (L329) | `| **Tue 2026-09-30** | ~30 min | User + Vinay | Strategy decision. |` → `| **Wed 2026-09-30** | ~30 min | User + Vinay | Strategy decision. |` |

**E. RESIDUAL 3 — `Wed 2026-10-01` (6 sites, not 5) + the GLM-OCR contradiction FS-11 created**

| id | OLD → NEW |
|---|---|
| **R2-05a** (L163) | `Our W5 freeze window opens Wed 2026-10-01.` → `Our W5 freeze window opens 2026-10-01 (Thu) — date TBC (U1).` |
| **R2-05b** (L289) | `- **Wed 2026-10-01 evening:** W5 freeze window opens. Per-script routing locked. Backbone choice GLM-OCR 0.9B confirmed (or rejected if Vinay picked Option B).` → `- **2026-10-01 (Thu) evening, date TBC (U1):** W5 freeze window opens. Per-script routing locked. Backbone choice OPEN (Qwen2.5-VL-3B-Instruct @ 4-bit is PRIMARY per W6_QLORA_SPEC §1; GLM-OCR 0.9B is ALTERNATE 2) — to be set or rejected at this call.` |
| **R2-05c** (L290 — **missed by the Miss**) | `- **Wed 2026-10-01 → Fri 2026-10-03:** QLoRA execution on Kok + Pa subset (only if Option A).` → `- **2026-10-01 (Thu) → 2026-10-03 (Sat), dates TBC (U1):** QLoRA execution on Kok + Pa subset (only if Option A).` |
| **R2-05d** (L305) | `Next gate: **Vinay meeting → W5 freeze after Wed 2026-10-01 → W6 training decision**` → `Next gate: **Vinay meeting → W5 freeze after 2026-10-01 (Thu, TBC U1) → W6 training decision**` |
| **R2-05e** (L330) | `| **Wed 2026-10-01 evening** | W5 freeze opens | Orchestrator + Engine | Per-script routing locked. Backbone choice GLM-OCR 0.9B confirmed. |` → `| **2026-10-01 (Thu) evening, TBC (U1)** | W5 freeze opens | Orchestrator + Engine | Per-script routing locked. Backbone choice OPEN (Qwen2.5-VL-3B primary, GLM-OCR alternate 2). |` |
| **R2-05f** (L331) | `| **Wed 2026-10-01 → Fri 2026-10-03** | ~3-4h | Engine + Miss | QLoRA execution on kok + pa subset (only if Option A). Wrap-only ships regardless at W5 freeze. |` → `| **2026-10-01 (Thu) → 2026-10-03 (Sat), TBC (U1)** | ~3-4h | Engine + Miss | QLoRA execution on kok + pa subset (only if Option A). Wrap-only ships regardless at W5 freeze. |` |

**F. RESIDUAL 4 — `GLM-OCR 0.9B (OmniDocBench #1)` in the D4 verdict cell (FS-12 fixed only the options cell)**

| id | OLD → NEW |
|---|---|
| **R2-06** (L221) | OLD `| **GLM-OCR 0.9B** (OmniDocBench #1, official MLX deploy); LightOnOCR-2-1B is Alternate 3 in W6_QLORA_SPEC.md §9.1 (1B SFT→GRPO, olmOCR-Bench SOTA at 1B, Apache-2.0, MLX deploy unverified — Option C candidate) |` → NEW `| **OPEN — no lock.** PRIMARY backbone is Qwen2.5-VL-3B-Instruct @ 4-bit per W6_QLORA_SPEC.md §1; GLM-OCR 0.9B is ALTERNATE 2. "OmniDocBench #1" is a v1.5-era figure (94.62) and is not corroborated on v1.6, where the top Overall is PaddleOCR-VL 1.6 at 96.01. Neither backbone is on disk — a download approval, not a $0 item. LightOnOCR-2-1B is Alternate 3 (unverified this run). |` |

**This cell now contradicts FS-11's own applied text at L129** (which made Qwen PRIMARY). The
fix pass created the contradiction by fixing one cell and not the other.

**G. RESIDUAL 5 — dead paths (all verified non-existent; replacements located on disk)**

| id | OLD → NEW |
|---|---|
| **R2-07a** (anchor L103) | `` | `EVIDENCE_SUMMARY.md` | Disk-truth findings + McNemar gaps | — | `` → `_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md` |
| **R2-07b** (anchor L105) | `` | `LEVEL7_RESEARCH_FINDINGS.md` | … `` → `_reports/research/LEVEL7_RESEARCH_FINDINGS.md` |
| **R2-07c** (anchor L106) | `` | `COMPUTE_BUDGET_ESTIMATE.md` | … `` → `_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md` |
| **R2-07d** (anchor L101) | `` | `W5_STRATEGY_OPTIONS.md` | 3 ranked options + ranking rationale | — | `` → `` | `docs/research/level7/W5_STRATEGY_OPTIONS.md` (3-option menu this packet presents) + `docs/architecture/W5_STRATEGY_OPTIONS.md` (5-option paper, recommends D) | ranked options + rationale — the two disagree on the recommendation | `` |
| **R2-07e** (anchor L102) | `` | `W5_BEAT_SARVAM_PLAN.md` | Concrete beat-Sarvam recipe | — | `` → `docs/architecture/W5_BEAT_SARVAM_PLAN.md` |
| **R2-07f** (L288) | `` Updates `CALL_PACKET.md` §0 status `` → `docs/research/level7/CALL_PACKET.md` |
| **R2-07g** (L311) | `` per `OBITUARIES.md` O-02–O-05 `` → `docs/research/level7/c/c4/OBITUARIES.md` |

`level2/probe22/PER_LANG_ROUTING.md` is **fully cleared** by FS-52 — 0 remaining citations.

**H. DEFECT INTRODUCED BY THE FIX PASS — FS-50's applied text contradicts itself**

The applied sentence reads: "…in the 0.10-0.40 band on **7 of the 12** languages with n>=50
(pa 0.145, brx 0.165, sa 0.175, mr 0.205, or 0.259, sd 0.315, kok 0.425 is outside — **6 in band**)…"
Headline **7** is correct; the list has 6 entries and omits **hi 0.220**; the text then concludes
"6 in band". The audit's own EVIDENCE line said "**6** in [0.10,0.40]" while its NEW said 7 — the
Miss copied the contradiction verbatim instead of reconciling it.

| id | OLD → NEW |
|---|---|
| **R2-08** (L141) | OLD `Per-lang best-engine CER in the 0.10-0.40 band on **7 of the 12** languages with n>=50 (pa 0.145, brx 0.165, sa 0.175, mr 0.205, or 0.259, sd 0.315, kok 0.425 is outside — 6 in band); the other 6 languages have n<50 and no winner claim.` → NEW `Per-lang best-engine CER in the 0.10-0.40 band on **7 of the 12** languages with n>=50 (pa 0.145, brx 0.165, sa 0.175, mr 0.205, **hi 0.220**, or 0.259, sd 0.315 — 7 in band); the other 5 at n>=50 (mai 0.030, kok 0.425, bn 0.476, ks 0.589, ur 0.623) are outside the band, and the 6 languages with n<50 carry no winner claim.` |

**I. UNDISCLOSED — "pa is McNemar-significant" survives in 4 places (FS-06 fixed only L127)**

| id | target | OLD → NEW |
|---|---|---|
| **R2-09a** | PKT L46 | `**Konkani + Punjabi only** (both SAFE, both ≥100/lang, both McNemar-significant gaps)` → `**Konkani + Punjabi only** (kok VERIFIED: McNemar p=0.0033, n=100, gap 19.4pt; pa CONDITIONAL: gap 8.1pt but McNemar vs runner-up tesseract_indic is p=1.00 tie, and pa n=90, not >=100)` |
| **R2-09b** | PKT L120 | `QLoRA on Konkani + Punjabi (the 2 SAFE langs where McNemar gaps survive the K1 gate).` → `QLoRA on Konkani (McNemar gap survives K1: p=0.0033) + Punjabi (gap does NOT survive: p=1.00 tie, n=90 — conditional).` |
| **R2-09c** | PKT L144 | `Adds McNemar-significant gap on 2 SAFE langs.` → `Adds a McNemar-significant gap on kok (19.4pt, p=0.0033) and a mean-CER-only gap on pa (8.1pt, p=1.00 tie).` |
| **R2-09d** | PKT L228 | `(Both SAFE per §6.4, both ≥100 samples, both McNemar-significant gaps.)` → `(kok: SAFE, n=100, McNemar p=0.0033 VERIFIED. pa: SAFE, n=90 — McNemar p=1.00 tie, so CONDITIONAL, not verified.)` |

**L228 is the question Vinay is asked to approve. It is currently false.**

**J. UNDISCLOSED — `docs/architecture/W5_STRATEGY_OPTIONS.md`: 5 live defects FS-42…46 never reached**

| id | line | OLD → NEW |
|---|---|---|
| **R2-10a** | 48 | `sd (0.315) / ur (0.623) / ks (0.589) — surya wins 9/9 opponents |` → `sd (0.315) / ur (0.623) / ks (0.589) — mean-CER leader on all three, but significance differs: ks 9/9 at p<=0.00049, sd 7/9, **ur 0/9 (every pair p=1.00 tie)** |` — *the exact claim FS-43 fixed at L116, unfixed in its twin at L48* |
| **R2-10b** | 58 | `e.g., surya 0.3849 → ensemble 0.25-0.30` → `e.g., surya 0.3944 → ensemble 0.25-0.30` — *ERRATUM-2 listed 4 sites; only 3 were fixed* |
| **R2-10c** | 9 | `- Probe truth: 11 engines × 1,227 packs × 18 langs;` → `- Probe truth: 11 model strings (10 x 1,227 items + Sarvam on 54) = 12,324 sheet.csv rows; **9 independent engines, not 11**; scored n 19-100, not 100;` |
| **R2-10d** | 47 | `hi (0.220) / brx (0.153) / kok (0.425)` → `hi (0.220) / brx (0.165) / kok (0.425)` |
| **R2-10e** | 52 | `| Odia (or) | tesseract-family | or (0.256 n=66) |` → `| Odia (or) | tesseract-family | or (0.259 n=69) |` |

**K. UNDISCLOSED — `PER_LANG_ROUTING.md`'s MAIN routing table still has the numbers FS-25…34 fixed in the *secondary* table**

| id | line | OLD → NEW |
|---|---|---|
| **R2-11a** | 13 | `| 3 | **brx** | Devanagari (Bodo) | 67 | surya (0.153) | easyocr (0.330) |` → `… surya (0.165) | easyocr (0.340) |` |
| **R2-11b** | 14 | `| 4 | **sa** | Devanagari (Sanskrit) | 99 | easyocr (0.168) | paddleocr_indic (0.171) |` → `… | 100 | easyocr (0.175) | paddleocr_indic (0.178) |` |
| **R2-11c** | 14 | `surya ALL-EMPTY (Ol Chiki bug); sa on PaddleOCR/Easy` → `surya ALL-EMPTY on sa (mean CER 1.000, 100/100) — sa is Sanskrit/Devanagari; the 'Ol Chiki bug' label belongs to sat (Santali) and is wrong here; sa on PaddleOCR/Easy` — *FS-21 fixed the EVIDENCE_SUMMARY copy of the K6 mislabel; this copy survives* |
| **R2-11d** | 16 | `| 6 | **or** | Odia | 66 | tesseract_indic (0.256) | tesseract_bilingual (0.258) |` → `… | 69 | tesseract_indic (0.259) | tesseract_bilingual (0.261) |` |

**L. UNDISCLOSED — `W5_BEAT_SARVAM_PLAN.md`: FS-45 fixed the table, not the prose**

| id | line | OLD → NEW |
|---|---|---|
| **R2-12a** | 132 | `**MEASURED:** tesseract-family wins or with 0.256 CER (n=66,` → `… with 0.259 CER (n=69,` |
| **R2-12b** | 166 | `| brx (n/a in Sarvam bench) | surya 0.153 → ~85 word-acc |` → `… surya 0.165 → ~85 word-acc |` |

**M. UNDISCLOSED — `EVIDENCE_SUMMARY.md:73` restates the or row FS-26 corrected**

| id | OLD → NEW |
|---|---|
| **R2-13** | `| **or** (Odia) | n=66, tesseract-family wins (CER 0.256). D4 borderline (n<70). |` → `| **or** (Odia) | n=69, tesseract-family wins (CER 0.259). D4 borderline (n<70). |` |

**N. UNDISCLOSED — `docs/research/level7/W5_STRATEGY_OPTIONS.md:9`**

| id | OLD → NEW |
|---|---|
| **R2-14** | `- 11 engines SCORED on 18 langs × ~100 items = 12,324 sheet rows LOCKED.` → `- 11 model strings SCORED (10 x 1,227 items + Sarvam on 54) = 12,324 sheet.csv rows; scored n per language 19-100, not 100.` |

---

# PART 6 — SCOPE CONFIRMATION

`find _archive/pre_fix_2026-09-29 -type f | wc -l` → **8** ✔ (expected 8).
All 8 target mtimes fall in **21:38:12 → 21:40:29**; the archive directory was created at
**21:36:07** (before the first edit). Files touched in the 21:30–21:45 window:

| file | in scope? | verdict |
|---|---|---|
| the 8 targets | yes | in scope |
| `_archive/pre_fix_2026-09-29/` (8 files) | yes | in scope |
| `level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` 21:35:17 | no | the lead's declared correction — see below |
| `OCR_AGENT_MEMORY_FEED.md` 21:32:44 | no | **not a fix-pass write**: its worktree diff contains **0** lines stamped `2026-09-29 21:0x` or `21:2x`; the diff is the cumulative 2026-09-25→28 corpus. Touched 4 min before the archive existed. |
| `docs/campaign/checkpoints/W1_reports/1E_hunt.md` 21:33:34 | no | a **different** agent's report (frontier-research / 1E-hunt), not the fix pass |

`git status --short` shows the whole tree as untracked/modified from days of campaign work; no
`git`-visible change outside the 8 targets was made by the fix pass. **No sealed directory
(`level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`, `Datasets/`) was
touched.** The Miss correctly left the re-LOCKED `OCR_AGENT_MEMORY_FEED.md` §12.2 alone — it still
carries the stale `gap 0.32`, `kok 32pt → 5pt` and the false `pa SURVIVES K1 — McNemar p<0.0001
(surya vs tesseract_indic, n=90)` (I measured p=1.00), exactly as ERRATUM-1 required.

## HONESTY CHECK ON THE MISS AGENT — **PASS**

- **The fix-spec file was not tampered with beyond the two declared lead corrections.** I found
  exactly **2** correction markers, both matching the lead's description: a count correction
  (L38) and a path correction (FS-45, L577). I verified the count correction is *true*:
  `grep -c '^### FS-'` = **54**, and the severity split is **19 BLOCKER / 28 MAJOR / 7 MINOR**,
  matching the `## BLOCKER` / `## MAJOR` / `## MINOR` section boundaries. Nothing was weakened:
  **all 62 OLD strings occur exactly once in the pre-images** (so no spec was made
  un-appliable) and **all 62 NEW strings occur exactly once now**.
- **The 8 pre-images match the audit's own recorded target sizes exactly** — 26,805 / 5,899 /
  9,782 / 5,861 / 7,166 / 14,324 / 19,443 / 3,754. **8/8 MATCH.** The archive is trustworthy and
  the diffs above are valid baselines.
- **"54/54 APPLIED, 0 NOT-APPLIED" is TRUE.** I independently re-derived all 62 edit pairs.
- **The Miss flagged its own incomplete residual list correctly** (it declined to hand-fix rather
  than guess) — but it under-reported. Its 5 categories are all real; **one is under-counted
  (`Wed 2026-10-01` = 6 sites, not 5) and 15 further defect classes went unmentioned**, including
  the Konkani claim at L56, the false "pa is McNemar-significant" at the question Vinay is asked to
  approve (L228), and the GLM-OCR verdict cell that now contradicts FS-11.

---

# PART 7 — EVERY file:line I RELIED ON

**Targets (current):** `VINAY_MEETING_PACKET.md` 6, 25-26, 28, 30, 44, 46, 49, 51, 56, 59, 77, 81,
89, 96, 99-110, 116-120, 122, 128-129, 141, 143, 163, 168, 195, 218, 221, 228, 288-291, 297-298,
305, 311, 320, 329-331, 340 · `docs/architecture/VINAY_MEETING_PACKET.md` 6, 17, 21, 27-29, 48, 72 ·
`_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md` 9, 24, 49-51, 55, 56, 58, 60, 64, 73, 78, 84, 101 ·
`_reports/cleanup_cycle1/PER_LANG_ROUTING.md` 13-19, 18, 21, 27-29, 32, 37-40, 43, 59 ·
`_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md` 35, 100, 103 ·
`docs/architecture/W5_BEAT_SARVAM_PLAN.md` 9, 37, 59, 65, 69, 132, 166 ·
`docs/architecture/W5_STRATEGY_OPTIONS.md` 9, 47, 48, 52, 59, 68, 78, 116 ·
`docs/research/level7/W5_STRATEGY_OPTIONS.md` 9, 10-12, 23, 87

**Pre-images:** all 8 in `_archive/pre_fix_2026-09-29/` (full-file diffs; root packet lines
6, 24-29, 49, 54, 79, 87, 102, 116-117, 120, 126-127, 141, 161, 166, 216, 219, 289, 296, 303, 309,
330, 338; arch packet 6, 21, 27-29, 48, 72; EV 24, 50, 56, 58, 60, 78, 84; PLR 18, 21, 27-29, 32,
43, 59; CBE 35, 100, 103; PLAN 59, 65, 69; OPT 9, 47, 59, 116; LVL7 10-12, 23)

**Data:** `level2/probe22/sheet.csv` (header + 12,324 records; per-language × per-model means,
paired-3 comparisons, prediction-identity hashing, Ol-Chiki / Devanagari codepoint fractions) ·
`level2/probe22/scores/mcnemar_full_matrix.json` (`meta`, 55 `pairs`, 19 languages) ·
`level2/probe22/fix_specs/W1A_PACKET_AUDIT.md` 1-691 (all 54 `### FS-` headers at 255-636; the
62 OLD/NEW pairs; L38 count correction; L577 path correction) ·
`level2/probe22/scores/en_sanity_sarvam_vision.json` ·
`docs/campaign/CAMPAIGN_DIRECTIVE.md` 19-117 (Part A) · `OCR_AGENT_MEMORY_FEED.md` 458-470 (§12.2)

**URL opened:** `https://sarvam.ai/blogs/sarvam-vision-2-1` (pub. 2026-09-24), fetched twice this
run — Indic OCR Bench language table, olmOCR-Bench table + "officially English-only" note,
OmniDocBench v1.6 table.

---

# PART 8 — UNRESOLVED

1. **The Konkani claim at L56 is the one thing that can sink the meeting in the room, and the
   fix pass left it in.** R2-03 is written and verified; it is not applied. Until it is, the
   packet's "What works" bullet still tells a CEO that Konkani is a Sarvam weak cell when
   Sarvam's own number there is **97.41 — the highest Indic cell in their table**.
2. **The `pa` question is still false as written.** L228 asks Vinay to approve
   "Konkani + Punjabi … both McNemar-significant gaps". pa is p=1.00 tie, disc=3, n=90. R2-09a-d
   are written and verified; not applied.
3. **FS-11 vs the D4 verdict cell (L221) and the two timeline rows (L289, L330) is a live
   contradiction created by the fix pass**: L129 now says Qwen2.5-VL-3B PRIMARY, three other lines
   still say "Backbone choice GLM-OCR 0.9B confirmed". R2-05b/e and R2-06 are written; not applied.
4. **I could not verify the provenance of the `24a25,26` insertion.** I can prove it is
   collateral (no spec is additive) and that its cited path does not exist, but not which actor
   wrote it. The write window (21:38:12–21:40:29) is the Miss's, so the working assumption is
   that the Miss added it — but the feed (21:32:44) and 1E_hunt (21:33:34) were also touched that
   minute-range by other actors, and directive A6 warns two OpenCode processes are live. **Ask the
   lead before attributing.**
5. **`docs/research/level7/W5_BEAT_SARVAM_PLAN.md` (the 3,652-byte copy) is still unread.** It is
   NOT one of the 8 targets, was not in the Miss's scope, and the audit listed it as UNRESOLVED #10
   warning it "may repeat the 32pt gap". I grepped it only for the false patterns. **A 5-minute
   read before the meeting is still outstanding** — it is the only packet-family doc nobody has read.
6. **Sealed files stay sealed.** `level2/reports/LEADERBOARD.md` and `CER_BY_SCRIPT.md` were not
   opened; the packet's "Level 1+2 DONE" row and "1,300+ lane records" remain unverified by me.
7. **The audit's `0.42` Ol-Chiki emission figure for sarvam_vision on sat does not reproduce** — I
   measure **0.336** on the same 3 rows. No applied text quotes 0.42 (FS-47 states only "only
   emitter" and "all 10 local = 0.00", both true), so nothing shipped is wrong. Flagging it so
   nobody re-cites 0.42.
8. **I did not open any of the six arXiv IDs in the packet's live-research block**, so the
   "NEW 2026-09-29" bullets (L58-63) remain UNSUPPORTED. That is the audit's UNRESOLVED #2 and it
   is untouched by this fix pass — it is a live exposure for a research-plan meeting.
9. **U1 (does "after next Wednesday" mean Sep 30 or Oct 7?) and U2 (the real submission deadline)
   are boss decisions and remain open.** Every round-2 spec above writes the Oct-1/Oct-4 dates as
   `TBC (U1)` / `TBC (U2)` rather than inventing a weekday, per directive A1. If the boss answers
   U1 with Oct 7, R2-05a/b/c/d/e/f need a second pass.
10. **`docs/architecture/W5_STRATEGY_OPTIONS.md` vs `docs/research/level7/W5_STRATEGY_OPTIONS.md`
    still recommend opposite options (D vs A).** R2-07d names both in the anchor row but does not
    decide which is canonical — that is a boss call, and the packet still presents only A.
