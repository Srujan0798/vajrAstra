# 1H — VERDICT round 2: `docs/campaign/DRAFT_RESEARCH_PLAN.md`

**Agent:** VERDICT (subagent) · **Run:** 2026-09-30 · **Round:** fix-loop 2, re-check only.
**Law observed:** read-only on every target. I wrote **this file only**. No `src/` run, no download, no
Sarvam call, no write to `level2/out/`, `level2/reports/`, `level2/probe22/out/`, `arc_level_1/`,
`Datasets/`. No existing repo file edited. `DRAFT_RESEARCH_PLAN.md` mtime unchanged by me.
**Scope:** the 7 BLOCKERs from `1H_verify.md`, the smaller corrections, and anything the fixes broke.

## VERDICT: **PASS-WITH-FIXES (4) — 2 of 7 BLOCKERs fully clear, 4 clear with one residual fix each, 1 still FAILing.**

BLOCKER 1 and BLOCKER 4 are fully cleared. BLOCKERs 2, 3, 6, 7 are substantively fixed but each
leaves one checkable defect. **BLOCKER 5 is still FAIL** — the two numbers are right, the *citation
attached to them is wrong*, and the correction is still smuggled rather than stated. Separately,
**one NEW false numeric claim was introduced by the fixes** ("111 exact", which is both wrong and
self-contradictory), and the "6,609 valid" gloss now gives the right number for the wrong reason.
The load-bearing honesty core is intact and unharmed.

---

## 1. The 7 BLOCKERs

| # | item | result | evidence | remaining fix |
|---|---|---|---|---|
| 1 | §3 "weakest / biggest gap / worst at" | **PASS** | all four sub-checks reproduce; see §2.1 | none load-bearing (2 cosmetic notes) |
| 2 | §5 options A/D | **PASS-WITH-FIX** | columns genuinely differ; recommendation names the right column; hazard note accurate on content — but the cited path does not exist | repoint the citation (§2.2) |
| 3 | §3 "labelled only" | **PASS-WITH-FIX** | min scored n = 19 (as) ✓; "no language is labelled-only" ✓; ml n=5 below floor ✓; all 8 list values ✓ | the count "8 of 22" (§2.3) |
| 4 | §5 GLM-OCR / OmniDocBench | **PASS** | no absence assertion survives; CONTRADICTION / UNKNOWN disclosed | none |
| 5 | §2 K1/K2 kill criteria | **FAIL** | values all correct; **the citation says the opposite**; correction not disclosed; "K2" still the wrong label | §2.5 — three edits |
| 6 | §4 GlotOCR | **PASS-WITH-FIX** | reversal fixed, hedge present, §6 no longer leans on it | tag the "1 font per family" figure (§2.6) |
| 7 | §6 download ask | **PASS-WITH-FIX** | Q5 scoping is correct and verified; §6 itself not updated | carry the scoping line into §6 (§2.7) |

### 2.1 BLOCKER 1 — PASS (all four sub-checks)

Re-derived from `level2/probe22/sheet.csv` × `manifest.json` `language`, local engines only,
per-language **mean** CER, per-language winner = argmin engine mean at n ≥ 50:

```bash
python3 - <<'EOF'
import csv, json
from collections import defaultdict
rows=list(csv.DictReader(open('level2/probe22/sheet.csv')))
lang={i['image_id']:i['language'] for i in json.load(open('level2/probe22/manifest.json'))['items']}
by=defaultdict(lambda: defaultdict(list))
for r in rows:
    if r['model']!='sarvam_vision': by[lang[r['image_id']]][r['model']].append(float(r['CER']))
mean=lambda v: sum(v)/len(v)
Q=[]
for l in by:
    s=sorted((mean(v),e) for e,v in by[l].items())
    if len(next(iter(by[l].values())))>=50: Q.append((l,s[0][0],s[1][0]))
for l,w,r in sorted(Q,key=lambda x:-x[1]): print(l,round(w,4),round(r,4),round((r-w)*100,1))
EOF
```

| sub-check | doc | re-derived | result |
|---|---|---|---|
| (a) kok is not the worst | "Konkani is **fourth-worst, not the worst**" | ur 0.6232 > ks 0.5894 > bn 0.4763 > **kok 0.4248** | **PASS** |
| (b) worst-first ranking | ur .623, ks .589, bn .476, kok .425, sd .316, or .259, hi .220, mr .205, sa .175, brx .165, pa .145, mai .030 | .6232 .5894 .4763 .4248 .3155 .2588 .2198 .2046 .1751 .1653 .1447 .0298 — **all 12 values and the order** | **PASS** |
| (c) Hindi lead is the largest | "largest gap to the runner-up is **Hindi, 0.220 vs 0.504 — a 28.4-point lead**" | surya 0.2198 vs **paddleocr_indic 0.5037** = 0.2839 = **28.4pt**; next is kok 19.4pt | **PASS** |
| (d) Konkani 19.4pt decomposition | "surya 0.4248 vs easyocr 0.6186" | 0.6186 − 0.4248 = 0.1938 = **19.4pt** | **PASS** |

Also verified in the same sentence: `surya 9, tesseract-family 2, easyocr 1` → 9+1+1+1 = 12 ✓;
**7 of 12** in the 0.10–0.40 band ✓ (`0.10<=w<=0.40` → sd or hi mr sa brx pa = 7).

**Hedge reads correctly** (`DRAFT_RESEARCH_PLAN.md:83`): "it is the one where Sarvam is **strongest**
(97.41 on their own bench; our rank of that cell among their 22 is **UNKNOWN** — their table and
Bodhan's disagree, a FLIP)". "Strongest" is the correct rank (Konkani 97.41 is **rank 1 of 22**:
97.41 > ne 97.00 > mai 96.70) and the UNKNOWN + FLIP disclosure is present.

**No "third-best" survives.** `grep -n -i -E "third.best|biggest gap|worst at" DRAFT_RESEARCH_PLAN.md`
→ 0 hits for all three. The only "weakest" hits are §3:104 "**Weakest cells:**" (a different, correct
list) and §4:114 "this is the **weakest link** in §6" (the new hedge, intended).

*Cosmetic, non-blocking:* §3:79 says n ≥ 50 is "**13 of 22**" while §3:83 says "**12 languages
qualify**". Both are right — the 13th is South `ta` (n=70) and §3:83's set is probe22-only — but the
document never says so, and a reader sees 13 and 12 in adjacent lines. Also `22.0pt` re-derives as
**21.9pt** (0.6442 − 0.4248 = 0.2194). Immaterial; not worth a fix round.

### 2.2 BLOCKER 2 — PASS-WITH-FIX (the columns are fixed; the citation is dead)

**A and D now genuinely differ.** Verified cell by cell at `DRAFT_RESEARCH_PLAN.md:123-129`:
A = ships only the on-disk routing table, **no QLoRA**, no restoration, no API → $0, 0.1d-class.
D = wrap **+ learned script-router + R4 restoration pre-pass + sat/mni API subsidy** → $0–30, a day+.
The prior "both columns describe the same option" defect is gone. ✓

**The recommendation names the right column**: line 131 recommends "**Option A as redefined in the
first column (wrap-only, $0, no downloads)**" and justifies it with the router's **negative** measured
gain (−0.0351 CER). The prior round's objection — that the recommendation rested on the *other*
column's risk profile — no longer applies. ✓

**The naming-hazard note is accurate on content.** Two genuinely different "A"s exist:
- `VINAY_MEETING_PACKET.md:44` — "**Option A** (wrap-only + Konkani + Punjabi QLoRA, ~4h wall, $0
  compute + optional ₹1005 (~$12) Sarvam subsidy for sat/mni cells)" ✓ = wrap + QLoRA kok+pa.
- the level-7 W5 options file — Option A "**W6 QLoRA on kok+pa + wrap-only baseline**", Cost
  "**$0**", "**Wall-budget: ~3-4 hours**" ✓ — exactly what the plan states.

**But the path the plan cites does not exist.** The plan cites it twice — line 126
("the `docs/research/level7/W5_STRATEGY_OPTIONS.md` A **does** include QLoRA kok+pa") and line 131
("`docs/research/level7/W5_STRATEGY_OPTIONS.md`'s A (wrap + QLoRA kok+pa, $0, 3–4 h)"). A reader
following that path finds nothing:

```
$ ls docs/research/level7/W5_STRATEGY_OPTIONS.md
ls: docs/research/level7/W5_STRATEGY_OPTIONS.md: No such file or directory
$ find . -name "*W5_STRATEGY*" -not -path "*/.git/*"
./docs/architecture/W5_STRATEGY_OPTIONS.md
./_archive/cleanup_2026-09-30/dedup_topic_superseded/W5_STRATEGY_OPTIONS.md
./_archive/pre_fix_2026-09-29/lvl7__W5_STRATEGY_OPTIONS.md          <-- the content, archived
./_archive/pre_fix_2026-09-29/arch__W5_STRATEGY_OPTIONS.md
./_archive/pre_fix_2026-09-29/round2_meeting/W5_STRATEGY_OPTIONS__level7.md
```

`docs/architecture/W5_STRATEGY_OPTIONS.md` **does** exist and **does** say what the task describes:
five alternatives `## Alternative A` … `## Alternative E` (lines 39/64/84/106/128) and a
`## Ranking` table (line 152) putting **D first**, "**Recommended pick for Vinay meeting:
Alternative D**" (line 162) ✓.

*Remaining fix:* repoint both citations at
`_archive/pre_fix_2026-09-29/lvl7__W5_STRATEGY_OPTIONS.md` (or fold the claim into
`docs/architecture/W5_STRATEGY_OPTIONS.md`, whose A is a *third* definition — pure wrap, $6, 0–1d,
rank 3). Note the "three documents … two different options" count is if anything an undercount: the
plan's own column A is now a third definition of A. This is a **new dead-path citation introduced by
the fix** — the previous draft did not cite this file, and round 1 explicitly recorded that it "does
not exist on disk".

### 2.3 BLOCKER 3 — PASS-WITH-FIX (statement and list now correct; the count is not)

`DRAFT_RESEARCH_PLAN.md:72` now reads: "So **no** language is labelled-only — the smallest scored n
of all 22 is **19 (Assamese)** — but the four South languages are the thinnest, and **Malayalam
(n=5) is below your 5–10 floor**." All three claims re-derive from `BENCHMARK_22.md` Table 1
(lines 37–58) and from the raw sources:

| claim | source | result |
|---|---|---|
| min scored n of all 22 = 19, Assamese | `BENCHMARK_22.md:37` `as \| probe22 \| 19 \| **19** \| 0` | **PASS** |
| no language is labelled-only | every row has scored n ≥ 1; min is `ml 5` | **PASS** (was "four … labelled-only" — false) |
| Malayalam n=5 below the 5–10 floor | `BENCHMARK_22.md:58` `ml … **5**`; only `ml` < 10 | **PASS** |
| the 8 listed n<50 values | as 19, mni 20, sat 20, gu 24, **te 26, kn 25**, doi 27, ne 37 | **PASS** — all 8 correct; `kn 25` is now present (it was missing in round 1) and the 8 named languages are exactly the n<50 set minus `ml` |

*Remaining fix:* the row label still reads "**No winner claim (n<50) \| 8 of 22**", but
**13 of 22** (the row above) + **8 of 22** = 21, and **9** languages are in fact n<50 — `ml 5` is the
ninth. `BENCHMARK_22.md` flags 9 (`no winner claim (D4)` on rows 37, 41, 42, 45, 48, 51, 56, 57, 58).
Change the label to "8 of 22 (plus `ml`, above)" or "9 of 22" so the section is self-consistent.

### 2.4 BLOCKER 4 — PASS

`DRAFT_RESEARCH_PLAN.md:133`: "On GLM-OCR's OmniDocBench v1.6 presence our two reviewers **disagree**
(one says the table omits it, one found it at 94.71, rank 3) — tagged **CONTRADICTION / UNKNOWN**
pending a source check. Either way the GLM-OCR recommendation is not evidence-backed yet."

- **No assertion of absence survives.** `grep -n -i "absent" DRAFT_RESEARCH_PLAN.md` → one hit, line
  171: "if either file is **absent from the pack**, abandon and report" — that is the Tesseract
  traineddata pack in the Day-2 kill criterion, not GLM-OCR. ✓
- **The contradiction is disclosed**, with both positions, the tag, and the consequence. ✓
- The stale source is correctly characterised: `W6_QLORA_SPEC.md:55` reads "ALTERNATE 2: GLM-OCR-0.9B
  (**OmniDocBench #1**, official MLX deploy…)" and the plan does not repeat "#1". ✓

Nothing to fix.

### 2.5 BLOCKER 5 — FAIL (values right, citation wrong, correction still unstated)

The **numbers in both nodes are correct** — I re-derived every one from
`level2/probe22/scores/mcnemar_full_matrix.json` (`pairs`, `p_two_sided`):

| node text | matrix entry | re-derived | value |
|---|---|---|---|
| K1 "19.4pt vs easyocr p=0.0107 n=100" | `surya_vs_easyocr · kok` → `n_common 100, p_two_sided 0.010674` | 0.0107, n=100 | ✓ |
| K1 "22.0pt vs tesseract-family p=0.0033" | `tesseract_bilingual_vs_surya · kok` → `p_two_sided 0.003327`; gap `0.6442−0.4248=0.2194` | 0.0033, 21.9pt | ✓ (0.1pt over) |
| K2 "pa: p=1.00 vs tesseract_indic n=90" | `tesseract_indic_vs_surya · pa` → `n_common 90, n_ties 87, n_discordant 3, p_two_sided 1.0` | 1.0, n=90 | ✓ |

**The round-1 arithmetic defect is genuinely fixed** — the two p-values are no longer welded to the
wrong comparison. But the fix failed on the three things round 1 actually required:

1. **The citation is misattributed — it points to a line that says the opposite.**
   `DRAFT_RESEARCH_PLAN.md:60` reads `K2["K2 pa: p=1.00 vs tesseract_indic n=90 NOT MET\n(W6_QLORA_SPEC.md:75) …"]`.
   `W6_QLORA_SPEC.md:75` actually reads:
   `pa K1 SURVIVES — McNemar p<0.0001 (surya vs tesseract_indic, n=90), gap = 0.081 …`
   So the document cites, as support for "p=1.00 NOT MET", the single line that asserts "p<0.0001
   SURVIVES". Same at `KILL_CRITERIA.md:56`: `pa | 0.1373 | tess_i 0.2159 | 0.081 (8pt) |
   p<0.0001 (surya wins, n=90, 88 discordant) | … **K1 SURVIVES** ✓`. This is a false source
   citation, which is the exact defect class BLOCKER 5 was raised for.
2. **The correction is still smuggled, not stated.** Round 1's fix was explicit: *"This corrects
   KILL_CRITERIA.md:56 and W6_QLORA_SPEC.md:75, which both say p<0.0001."* Neither line appears
   anywhere in the document. A reader cannot tell that the plan is overriding two cited sources —
   the document's own law (`§9` evidence tags, appendix "PRIMARY / MEASURED / … / CONTRADICTION")
   requires it.
3. **"K2" is still the wrong criterion label, and the node's conclusion overreaches.**
   `KILL_CRITERIA.md:68` — "**K2 — Kill micro-repair if <6h remain before freeze OR >50% pages fail
   purge-era gates**". K2 is the micro-repair time/purge gate; `pa` is a **K1** verdict in that file
   (row 56). The flowchart therefore shows a K1 criterion and a K2 criterion as if they were two
   peers of the same test. And "**pa out of QLoRA scope**" is not supported by the node's own
   evidence: `surya_vs_easyocr · pa` → `p 0.0, n 90, 89 discordant` and the same for
   `surya_vs_paddleocr_indic`; `pa` beats 5 of 10 local engines at p=0.0. The tie is against the
   tesseract-family **only**, which is a runner-up question, not a kill.
4. **K1 cites no source at all** — the task asked that K1/K2 "match them and cite the source". K2
   cites a line that contradicts it; K1 cites nothing.

*Remaining fix (all mechanical):* rewrite the two nodes as, e.g.
`K1["K1 kok SURVIVES: 19.4pt vs easyocr (McNemar p=0.0107, n=100); 22.0pt vs tesseract-family (p=0.0033, n=100) — mcnemar_full_matrix.json"]`
and
`K2["K1 (2nd lang) pa: vs tesseract_indic a TIE, p=1.00, n=90 (87 ties, 3 discordant) → does not meet K1 as written. THIS CORRECTS KILL_CRITERIA.md:56 and W6_QLORA_SPEC.md:75, which both read p<0.0001 SURVIVES. pa still beats easyocr/paddleocr/rapidocr/doctr/anuvaad at p=0.0 (n=90), so pa is a runner-up question, not a kill."]`

**Mermaid syntax: plausible.** Extracted lines 26–64: `[` 26 / `]` 26, `(` 3 / `)` 3, `{}` 0/0, double
quotes 52 (even), and **every one of the 20 node labels and 6 `subgraph` lines carries exactly 2
double-quotes** — no unbalanced label, no stray bracket, no unterminated node. Both KILL nodes are
well-formed. One cosmetic note: the two `\n` escapes inside `K1`/`K2` (lines 59–60) render as
literal `\n` in Mermaid; `<br/>` is the portable line break. Not a syntax break.

### 2.6 BLOCKER 6 — PASS-WITH-FIX

`DRAFT_RESEARCH_PLAN.md:114` now reads: "…reports a **font-coverage effect**: low-resource tiers carry
a median of **1 font per family**, and the paper attributes low-tier failure to *pretraining
coverage* of those scripts, **not** to font availability. Our machine has **1 Ol Chiki and 1
Meetei Mayek font**, so the font count is *our* constraint, not their conclusion — the analogy is
suggestive, not evidential. *Usable now, and this is the weakest link in §6.*"

- **The reversal is fixed.** The paper's claim (arXiv 2604.12978, per round 1) is "Performance broadly
  tracks **script-level pretraining coverage**"; the document now attributes exactly that, and
  explicitly negates "not font availability". ✓
- **The hedge is present** in both halves: "the font count is *our* constraint, not their conclusion"
  and "suggestive, not evidential", plus a self-flag as "the weakest link in §6". ✓
- **§6 no longer leans on GlotOCR.** `sed -n '135,146p' | grep -i glotocr` → 0 hits. §6:141's
  "The constraint is fonts — we have one typeface for each" is our own measured claim, and it is
  independently verified: `find /System/Library/Fonts … -iname '*OlChiki*' -o -iname '*Meetei*'`
  returns exactly `NotoSansOlChiki-Regular.ttf` and `NotoSansMeeteiMayek-Regular.ttf`. That is
  consistent with §4's "the font count is *our* constraint". ✓

*Remaining fix:* the "**median 1 font per family**" figure is still asserted as the paper's, with no
tag. Round 1 recorded it as UNRESOLVED: "not in the abstract. Needs the paper's low-tier table, or
the claim becomes ours-only." Either cite the table or tag it UNKNOWN.

### 2.7 BLOCKER 7 — PASS-WITH-FIX (Q5 is right; §6 was not updated with it)

`DRAFT_RESEARCH_PLAN.md:159` now reads: "**Scoped correctly: `tam`/`tel`/`kan`/`mal` traineddata is
already on disk, so the download is only `sat` and `mni`.**" Verified against all three tessdata
directories on the machine:

| dir | contents | sat / mni? |
|---|---|---|
| `level2/probe22/tessdata/` | asm ben eng guj hin mar nep ori pan san snd urd (12) | **neither** |
| `/opt/homebrew/share/tessdata/` | eng hin **kan mal tam tel** osd snum + configs | **neither** |
| `level2/research/smoke/anuvaad_tesseract/tessdata/` | **anuvaad_kan anuvaad_mal anuvaad_tam anuvaad_tel** eng hin osd | **neither** |

`kan`, `mal`, `tam`, `tel` are on disk; only `sat` and `mni` are absent everywhere. **The scoped
statement is factually correct.** ✓

*Remaining fix:* the correction landed **only in §8 Q5**, not where the ask is justified. §6:141
still reads "and `tessdata/` has none of `sat`, `mni`, `kan`, `mal`, `tam`, `tel`" and §6:143 still
reads "**The fix is one ~2–4 MB Tesseract model download**" — singular model, six languages, no
on-disk caveat. So the section that makes the ask still presents a 6-language gap while the questions
section says 2. Round 1's fix text said to put the scoping in both places. Add the one-line
correction to §6:141 and change §6:143 to "two" models.

---

## 2. The smaller corrections the author made

| claim (line) | re-derived | result |
|---|---|---|
| "**110 of 400** sampled rows within 1e-4 **(111 exact)**" (101) | `random.seed(20260926); random.sample(rows,400)` + `metrics.calculate_cer` → **exact 66 · ≤1e-4 110 · ≤5e-4 111** | **FAIL** — see below |
| "**~1,995 lines** of untracked QLoRA/GRPO" (161) | `find src -name '*.py' \| xargs wc -l` → **1,834**; `tests/test_basic.py` → **161**; total **1,995** | **PASS** |
| "**6,909 curated text-block samples** (6,609 valid after their own exclusion of ambiguous-GT and degenerate outputs)" (12) | 6,909 total ✓ (23 card rows); 6,609 ✓ — but see below | **FAIL on the gloss** |
| fusion "per-item oracle **0.3213** against **0.4190** … a **0.098 gap**" (145) | `random.seed(20260926)`, 300 `image_id`s, 10 local engines → surya **0.4190**, oracle **0.3213**, gap **0.0977** ≈ 0.098 | **PASS — fully reproduced** |
| "**67%** of it is the `sa` cell … Ex-`sa` the gap is **0.0332**" (145) | my decomposition → sa share **69.1%**, ex-sa gap **0.0328** | **PASS to rounding** (the exact share formula is not stated; two independent decompositions agree) |

**`110 of 400 … (111 exact)` is a new false claim.** The 110 is right, but the parenthetical is wrong
twice over: the **exact** count is **66**, and **111** is the count at **5e-4** tolerance — round 1's
instruction was "110 at 1e-4 / 111 at 5e-4, and **state the tolerance**". As printed the sentence is
also **self-contradictory**: you cannot have 111 exact matches inside a set of 110 that match within
1e-4. It is the same class of error round 1 raised (exact ⊆ within-tolerance). Fix: "…**110 of 400**
sampled rows within **1e-4** (**66 exact**; 111 at 5e-4)".

**`6,609 valid` gives the right number for the wrong reason.** `COMPETITOR_INTEL.md:10` and the
Sarvam blog both state the decomposition as **6,909 total = 6,609 across the 22 Indic languages +
300 English, English excluded from the macro**. The plan's parenthetical instead attributes 6,609 to
"their own exclusion of ambiguous-GT and degenerate outputs" — a *different* exclusion that applies
on top of both pools and yields a different denominator. Fix the mechanism, and attach n=6,609 to the
87.39 macro itself (line 14 names the 22 languages but not the n, which `proto-64` step 6 requires).

**Fusion numbers: the round-1 UNRESOLVED #1 is now closed.** The exact sampling
(`seed 20260926`, 300 `image_id`s) reproduces **0.4190 / 0.3213** to 4 dp, and
`EDGE_THESIS.md:56` carries the same pair with the withdrawn 0.4277/0.5229 explicitly retired
("*the hunt's original 0.4277/0.5229 pair did not reproduce and is withdrawn; lens B re-measured
it*"). Both files now agree — the impossible surya-below-oracle ordering is gone.

---

## 3. Protected items — all intact, nothing broken

| protected item | line | re-checked | result |
|---|---|---|---|
| §6 "Four edge theses were drafted. All four were killed by three adversarial reviewers each (12 critiques). **Zero survived.**" | 137 | verbatim present; matches `EDGE_THESIS.md` §1 | **INTACT** |
| §7 honest-empty: "**PARTIAL, and honestly so.** … one could not run … one could not run (budget), and one is waiting on your paste" | 149 | verbatim present | **INTACT** |
| §1 UNKNOWN tag on 87.39: "**UNKNOWN, do not assert:** the card defines word accuracy as 100 × (1 − WER) but never states that 87.39 *is* that figure" | 14 | verbatim present | **INTACT** |
| §3 GT-tier split, 3 tiers × 3 numbers | 91–93 | **all 9 re-derive exactly**: pair_txt 9/0.064/0.243 · pdf_layer 36/0.311/0.229 · sarvam_bench 9/0.278/0.617 | **INTACT** |
| "Sarvam's CER is 2.5× lower … (0.171 vs 0.430)" | 95 | 0.1711 / 0.4296, ratio **2.511**, n=18 | **INTACT** |
| "Every one of our **21 item-level wins** … sits in the PDF-layer tier" | 97 | surya-vs-sarvam by tier: pdf_layer **21 W**/13 L/2 T; pair_txt 0/9/0; sarvam_bench 0/6/3 | **INTACT** |
| "0 of 200 … Santali … single Ol Chiki character" | 141 | 200 sat local rows, **0** codepoints in 0x1C50–0x1C7F | **INTACT** |
| surya `sa` 100% empty | 145 | sa/surya: 100 rows, **100 empty**, mean CER 1.0000 | **INTACT** |
| verifier 0.6766 vs 0.4190, "61% worse" | 137 | `EDGE_THESIS.md:23`; 0.4190 independently re-derived; 0.2576/0.4190 = 61.5% | **INTACT** |
| 12,324 rows / 11 model strings / 1,227 scored / 126 of 400 | 72–78 | 12,324 · 11 · 12,270 local + 54 sarvam · 400 pages, 126 scored | **INTACT** |
| 43.7% / 50.3% abstention | 131 | 536/1227 = 43.68% · 617/1227 = 50.29% | **INTACT** |
| 564 NFC≠NFKC, 0 exact-match flips | 117 | 564 on `gt` | **INTACT** |
| 1 Ol Chiki + 1 Meetei Mayek font | 114 | exactly 2 font files | **INTACT** |

### New false claim found in the fixes (not one of the 7)

**"pooled 10/18" does not reproduce — I get 8/18.** The plan states `10/18` twice (lines 87 and 97),
both times only to refuse it ("A pooled 'we lead on 10/18 languages' is **not a result** …
the pooled 10/18 must not be presented as a win"). Per-language surya-vs-sarvam mean, 18 languages
with Sarvam rows (3 each):

```
as 0.2534<0.3339 YES   bn 0.4763>0.0891 no    brx 0.1653<0.3794 YES  doi 0.3350>0.0564 no
gu 0.2550>0.2223 no    hi 0.2198>0.0836 no    kok 0.4248>0.2387 no    ks 0.5894<0.6305 YES
mai 0.0298<0.2568 YES  mni 0.9769>0.0230 no   mr 0.2153<0.2477 YES    ne 0.2284>0.2099 no
or 0.2847<0.4475 YES   pa 0.1447<0.1597 YES   sa 1.0000>0.0195 no     sat 0.7621>0.4773 no
sd 0.3155<0.3441 YES   ur 0.6232>0.5332 no
=> 8/18  ['as','brx','ks','mai','mr','or','pa','sd']
   best-local-instead-of-surya: 9/18
```

`sheet.csv` is unchanged since round 1 (mtime **Sep 28 21:54**), so this is a **disagreement with
round 1's own finding** (which reported 10/18 with a list I cannot reproduce under any variant), not
a data drift. The load-bearing claim is unaffected — the plan's *point* is that the pooled number
must not be presented as a win, and refusing a number that is really 8/18 strengthens that. But a
number in the document is wrong, and it is a pooled n=3-per-language figure the document elsewhere
insists on tagging. Fix: change both to 8/18, or delete the figure and keep only the refusal.

### Carried over from round 1, not re-fixed (non-blocking, listing for completeness)

- Header date still **2026-09-29** (line 3) while §1:12 says the card was "**opened 2026-09-30**" —
  the document is dated the day before its own newest evidence.
- §4:112 venue "CVPR 2026" for arXiv 2504.11101 still unverified, and `2504.11101` is still **absent**
  from the appendix URL list (line 183) — the one claim that killed an edge thesis is still uncheckable.
- §4:113 "57 Maltese pages" still unsourced (abstract says a 422-paragraph dev set); and "(DocEng 2026
  winner)" is still there — the paper says the held-out result is "under organizer embargo and is not
  reported".
- §4:115 still "UNVERIFIED: we did not open its file listing" although round 1 confirmed the README
  states the pack includes Ol Chiki and Meetei Mayek.
- §3:102 still "219 nulled `gt_thin` at GT<200 chars" (observed max 178).

---

## 4. Overall verdict

**PASS-WITH-FIXES (4).**

- **2 of 7 BLOCKERs fully clear:** #1 (the CEO-facing paragraph — every value and the ranking now
  reproduce exactly, and the "third-best" falsehood is gone) and #4 (GLM-OCR).
- **4 of 7 substantively fixed with one residual defect each:** #2 (dead citation path),
  #3 (the "8 of 22" count), #6 (untagged GlotOCR font figure), #7 (§6 not updated with the scoping).
- **1 of 7 still FAILing: #5** — the K1/K2 values are right, but `W6_QLORA_SPEC.md:75` is cited as
  support for a claim it contradicts, the correction to two cited sources is never stated, "K2" is
  still the wrong criterion, and the "pa out of QLoRA scope" conclusion is not supported by the
  node's own evidence.
- **Plus 2 new numeric defects introduced by the fixes** ("111 exact", which is also
  self-contradictory; and the "6,609 valid" gloss), and **1 pre-existing number that does not
  reproduce** (pooled 10/18 → 8/18).
- **Nothing load-bearing was broken.** The GT-tier stratification, the 2.5× human-verified
  one-liner, "Zero survived", the honest-empty §7, the UNKNOWN on 87.39, the 0-of-200 Ol Chiki fact,
  the sheet.csv provenance note, and the fusion numbers all survive intact — and the fusion numbers,
  which round 1 could not reproduce at all, now reproduce to 4 dp on a seeded 300-item sample.

None of the residual items requires re-analysis. All are one-line edits. The document is
defensible in front of the CEO **once** #5 is corrected, because #5 is the one place where the
document currently asserts that a source says something it does not say.

### Law compliance (self-check)
Only `docs/campaign/checkpoints/W1_reports/1H_verify_round2.md` was created. `git status --short`
shows no new modification by me to any tracked file; `DRAFT_RESEARCH_PLAN.md` was read only. No
`src/` execution, no download, no Sarvam call, no write into `level2/out/`, `level2/reports/`,
`level2/probe22/out/`, `arc_level_1/` or `Datasets/`. I read `level2/probe22/metrics.py` by
importing `calculate_cer` only — no scoring pass, no write.

### UNRESOLVED after this round
1. **BLOCKER 5's citation** — needs a human decision on which is authoritative, the matrix or the two
   prose sources, before the node can be written honestly.
2. **"median 1 font per family"** — not in the GlotOCR abstract; needs the paper's low-tier table or an
   UNKNOWN tag.
3. **"pooled 10/18"** — round 1 and round 2 disagree on the same unchanged `sheet.csv`. One of the two
   derivations is wrong and the discrepancy is unresolved; I can only report that 8/18 is what the
   current file supports.
4. **§6's 6-language tessdata list** — needs the scoping line so §6 and §8 Q5 stop contradicting
   each other.
5. **Round 1's unresolved items 2–9** (57 Maltese pages, CVPR venue, pack licence, the 49-vs-43 file
   count, the missing `1D` report) are all still open and out of this round's scope.
