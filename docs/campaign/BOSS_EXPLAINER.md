# PROTO-85 — BOSS EXPLAINER + TOP-10 Q&A (for the Vinay meeting, 2026-09-30)

One page to hold. Every number carries its n, metric and GT tier. Sources at the foot.
**Status: the plan Vinay is asked to approve is Plan v2 (proto-87); this card is the honest state of the ground it stands on.**

## The 30-second version
We have **22 languages of labelled data, 1,683 items**, and **10 local OCR engines already run** over 1,227 of them. On our own probe our best engine is surya, which has the lowest mean CER in **9 of the 12** languages where n≥50. **On human-verified ground truth we are behind Sarvam 2.5×**; our apparent lead sits entirely on PDF-text-layer GT, which is not human-checked. **We have no edge thesis that survived adversarial review.** What we do have is a measured capability gap we can close cheaply, a benchmark we can now run for a directly comparable number, and a five-day plan with gates.

## The six numbers that matter
| # | Number | Why it matters |
|---|---|---|
| 1 | surya lowest mean CER in **9 of 12** languages at n≥50 | the wrap-only baseline, $0, already on disk |
| 2 | On the **18 human-verified** items where Sarvam ran: Sarvam **0.171** vs our best **0.430** = **2.51×** | the honest headline; our lead is a GT-tier artefact |
| 3 | **0 of 200** local predictions on Santali contain an Ol Chiki character | no local engine reads Ol Chiki or Meetei Mayek at all |
| 4 | Only **mni** and **sat** lack Tesseract traineddata; the indic-ocr pack **states it includes both** (licence unverified) | the one cheap, concrete unlock |
| 5 | surya **24.3 s/page** → **36 h** for 5,344 test images; rapidocr **0.40 s/page** → **0.6 h** | speed is now measured; the best engine is our slowest by ~60× |
| 6 | Abstention: anuvaad **59.4%** empty, paddleocr **56.1%**, rapidocr **39.7%**, surya **17.4%** | our leaderboard partly measures refusal, not recognition |

**Escalation worth knowing:** `sheet.csv` does not re-derive from its own inputs (**62.9% of 12,324 cells**) — but under a full independent recomputation **every headline number is unchanged** (same winner in all 12 n≥50 languages, same 10/18, Konkani 0.4248→0.4286). Use the numbers; do not call them independently checkable.

---

## TOP-10 QUESTIONS VINAY IS MOST LIKELY TO ASK

**Q1 — "So are we beating Sarvam or not?"**
**No, and we will not claim it.** Our only paired comparison is **54 items, 3 per language** — far too few for a win. Worse, when we split those 54 by how the ground truth was made, **all 21 of our item-level wins sit on PDF-text-layer ground truth and none on human-verified ground truth**, where Sarvam is 2.5× better. Either our lead is a measurement artefact, or we have a real problem on human-checked text. We are testing which, on Day 2.

**Q2 — "What is our actual number then?"**
**We do not have one yet, and that is the point of Day 2.** Sarvam's own benchmark is public, Apache-2.0 and downloadable. Running **their scorer on their data** gives the first figure of ours that can be set beside their 87.39. Until then our position is an **estimate** near Surya OCR 2's 69.96 — about 6th of 14, ~17 points back.

**Q3 — "What did you find that nobody else has?"**
**Honestly: no accuracy edge survived.** Four candidates were put to three adversarial reviewers each; all four died. What we did find is a **capability gap we can state as fact**: no local engine reads two of our 22 languages at all, and the fix is one traineddata file. That is not a research win — it is a coverage win, and we are calling it that.

**Q4 — "Why did the lead with 9 of 12, then say you're behind?"**
Both are true and they measure different things. 9 of 12 is *our* ranking among *our* engines on *our* GT. The 2.5× is *us versus Sarvam* on GT a human verified. The second is the one that would decide a hackathon.

**Q5 — "Why no training? The PPT is a training plan."**
Two reasons, both yours to overrule. Training is **paused by your own directive** until this review, and an untracked 2,000-line QLoRA/GRPO tree appeared on disk **before** you reviewed it. Plan v2 proposes **one** controlled fine-tune, not four stages, and only after Day 2 gives us a comparable number to improve on.

**Q6 — "Five days is not enough. What is realistic?"**
Being beaten by Sarvam on human-verified text, in five days, on one laptop, is not realistic. Getting an honest comparable number, closing two dead languages, and shipping a routed pipeline at **$0** is. Plan v2's gates are built so that each day can fail without wasting the next.

**Q7 — "What does surya cost us commercially?"**
Its package contradicts itself: the metadata says Apache-2.0, the licence text is a **modified OpenRAIL-M capped at $5M funding/revenue**. That is your call, not engineering. It is also our best engine in 9 of 12 languages, so it matters.

**Q8 — "Can we finish the submission in time?"**
Speed is now measured, not guessed. surya is **24.3 s/page ≈ 36 h** for the 5,344-image test set (p90 is 72 s → ~107 h). rapidocr is **0.6 h**, Tesseract-family **3.8 h**. So yes — but on a routing table, not on surya alone, unless the deadline allows two days of compute.

**Q9 — "Why is half our data unusable?"**
`gt_thin` and mojibake gates nulled 274 of 400 South pages; 8 probe22 languages sit at n 19–37; Malayalam has **5** scored pages. The gates are not negotiable, so low-n cells carry a permanent caveat instead.

**Q10 — "What do you need from me today?"**
**V1** download Sarvam's benchmark (the comparable number) · **V2** one fine-tune on bn/hi/sa/en + Konkani · **V3** backbone · **V4** surya's licence · **V5** Ol Chiki/Meetei licence · **V6** who confirms the deadline and the official scoring rules — **currently UNKNOWN**, the circulated metric set came from a student project · **V7** handwriting in scope. Plus: stop or authorise the `src/` build, and pick **one** editor for this repo.

---

## The five weakest parts of our own position (say these before he finds them)
1. **No comparable number exists yet.** Everything about our standing is an estimate.
2. **Our evidence sheet is not re-derivable**, even though its conclusions survive.
3. **n=3 per language** on the only head-to-head we have.
4. **Abstention is huge** on three engines, so "10 engines" overstates the depth of the comparison.
5. **Two editors have been writing this repo**; the campaign tree was archived once mid-day and the packet's own pointer dangled.

## Sources
`docs/campaign/BENCHMARK_22.md` · `SHEET_V2_FORENSICS.md` · `EDGE_THESIS.md` · `MULTI_LLM_EVAL.md` · `level2/unified/build_sheet_v2.py` · `level2/unified/build_metrics_80.py` · `level2/probe22/{sheet.csv,manifest.json,metrics.py}` · `level2/reports/LATENCY.md`
URLs opened 2026-09-30: `huggingface.co/datasets/sarvamai/indic-ocr-bench` (card, tree, `metrics.py`, `README.md`) · `sarvam.ai/blogs/sarvam-vision-2-1` · `github.com/indic-ocr/indic-ocr.github.io` · `arxiv.org/pdf/2604.12978v1` (GlotOCR Bench)
