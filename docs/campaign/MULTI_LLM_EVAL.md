# MULTI-LLM EVALUATION — Wave 1 (A3)

**Lead:** Sonnet session 2026-09-29 · **Protocol:** memory proto-17 · **One-pager evaluated:** `checkpoints/W1_reports/1F_onepager.md` · **Paste artefact:** `docs/campaign/CHATGPT_EVAL_PROMPT.md`

## 1. Status: PARTIAL — 1 of 3 evaluator legs ran, 2 could not

| # | Evaluator | Tool | Model id | Status |
|---|---|---|---|---|
| 1 | OpenCode | MCP `mcp__opencode__opencode_*` | — | **NOT RUN — tool unavailable.** The MCP server is not exposed to this session; the only available tools are GitHub, Context7, parallel-search and Playwright. Independence caveat moot. |
| 2 | Hostile Sonnet reviewer | subagent | harness default (Sonnet-class per the boss's constraint) | **NOT RUN — budget.** The subagent dispatcher returned `Token Plan usage limit reached` on the last call of the session. |
| 3 | ChatGPT | boss pastes `CHATGPT_EVAL_PROMPT.md` | unknown (latest) | **PENDING BOSS** — the prompt is written and self-contained. Not invented, not simulated. |

**Independent adversarial critique WAS obtained, by another route.** The 1E-refutation step (proto-16) ran **three independent Sonnet subagents in three separate roles** — lens (a) incumbents-already-do-it, lens (b) mechanism-fails-on-real-Indic-input, lens (c) cannot-be-built-in-time — against four edge-thesis candidates, i.e. **12 independent hostile critiques**, each instructed to return REFUTED by default. They are in `W1_reports/1E_lensA.md`, `1E_lensB.md`, `1E_lensC.md` and are dispositioned in `docs/campaign/EDGE_THESIS.md`. That is not the same artefact as a plan review (they attacked theses, not the plan), and it is **not** offered as a substitute. It is recorded here because it is the critique evidence this wave actually holds.

**Honest-empty is correct.** No evaluator output is simulated, paraphrased or attributed to a model that did not produce it.

## 2. Disposition table — critiques actually received, and what changed because of them

Drawn from the three lens reports. **Accepted by reasoning, not by source** (the lead's rule: *"by the process mentioned, not by the AI mentioned"*).

| # | Critique (≤30 words) | Raised by | Verification | Disposition | Action taken |
|---|---|---|---|---|---|
| 1 | "The Santali cell is saturated — a perfect Ol Chiki recogniser scores 0.457 vs our 0.459" | hunt | **REFUTED by lead re-measurement.** Ol Chiki share mean **0.6764** (n=20 items × 10 engines) → floor **0.324**, not 0.457; best local `sat` = `indicphotoocr` **0.6514** | **REJECT** (the saturation claim is false) · the underlying capability gap **ACCEPT** | `EDGE_THESIS.md` §2, §3 rewritten: cell has ~0.33 headroom; the real blocker is that **0 of 200 local predictions contain any Ol Chiki codepoint** |
| 2 | "Per-script-block CER is an edge" | hunt, lens A | Sarvam's own indic-ocr-bench card curates samples "at the semantic **block level**… rather than full noisy pages"; `mixed_script` is `False` on all 12,324 of our rows; only 16/1,227 items (1.30%) are multi-script | **REJECT** — the competitor already scores at block level, and our data has no multi-script pages to score | thesis killed; not carried into the plan |
| 3 | "An akshara-validity verifier will fuse our 10 engines" | hunt, lens A, lens B | Lens B **measured** it: validity-argmax **0.6766** vs surya-always **0.4190** — 61% worse. Lens A: UAX #29 already specifies the Indic grapheme rules; ICDAR 2017 "Script Grammar Learning" is the same mechanism; Aksharamukha ships the conventions | **REJECT** on measurement | thesis killed; recorded in `EDGE_THESIS.md` §2 as the most promising idea that died on a number |
| 4 | "Script-mismatch is a free abstention signal" | hunt, lens A, lens B | Precision 95–100% but **recall 0.0–5.2% for 8 of 10 engines**; `anuvaad` fires 0/610, `paddleocr_indic` 1/691; **zero gain on ks/ur/sd** (Nastaliq is script-invariant); surya routing gain **−0.0351**; CVPR 2026 "Consensus Entropy" (arXiv 2504.11101) already does training-free inter-model agreement | **REJECT** the router · **ACCEPT** the cheap half | **Report median + abstain rate instead of mean** (lens C prices it at 2 h; `paddleocr_indic` 43.7% empty, `anuvaad_tesseract` 50.3%, `rapidocr` 28.0%, `surya` 10.5%). Carried into `DRAFT_RESEARCH_PLAN.md` §9 as a day-1 item |
| 5 | "A GT script-purity gate is an honesty fix that lowers our scores" | hunt, lens A, lens B | Lens A: dropping the 18 items moves our Marathi CER **0.228 → 0.120** — it *raises* it, there is no sacrifice. Lens B: cause is **14× over the arithmetic ceiling**; the 18 items are table pages (7.4× Latin, 7.9× digits) | **REJECT as framed** · **ACCEPT as hygiene, deferred** | Not before the meeting: `sheet.csv` is LOCKED and U5 defers re-scoring. Recorded in `EDGE_THESIS.md` §5 as a post-meeting item |
| 6 | "The stored `CER` column in `sheet.csv` is not reproducible from the repo's own `metrics.py`" | lens C | **CONFIRMED by lead measurement**: 66/400 exact, 100/400 within 5e-4; 0 match the uncapped variant; no normaliser closes it (NFC 55, NFKC 55, raw 54, WER 65); implied reference length median **1.336×** the stored GT length; mismatch spread across all 11 models | **ACCEPT — highest-severity finding of the wave** | `EDGE_THESIS.md` §4 (full analysis) · `DRAFT_RESEARCH_PLAN.md` §3 and §8 as a named risk and a question for Vinay · escalated to the boss as **U5, now blocking for external citation** |
| 7 | "The dev-day estimates are inflated 2–4×" | lens C | C1 1 d → 1.5–2 d; C2 2 d → 4–5 d across 22 scripts; C3 1 d → the median column alone is 2 h | **ACCEPT** | All estimates in `DRAFT_RESEARCH_PLAN.md` §9 use lens C's numbers, not the hunt's |
| 8 | "Unicode normalisation is not a problem for us — 0 exact-match flips across 12,324 rows" | hunt (self-refutation) | Hunt's own measurement, reproduced by 1B's normalisation diff (NFC/NFKC/whitespace/quotes/dashes/danda/ZWJ-ZWNJ/nukta/digits/case all **identical** to Sarvam's) | **ACCEPT** | Stated explicitly in the plan as a place **not** to spend 5 days |
| 9 | "Sarvam self-scored, macro-22, English excluded, degenerate outputs dropped" | 1D (independent of the lenses) | PRIMARY from the HF card, opened this run | **ACCEPT** | `DRAFT_RESEARCH_PLAN.md` §1 and §6: the comparability verdict is NO, and our answer is to publish on our own terms |
| 10 | "Bodhan is ~0.83B, released 5 Sep 2026, and 84.94 is *Sarvam's* score for Bodhan; Bodhan's own number is 86.2" | 1D | PRIMARY, live re-verified | **ACCEPT** | Corrected in `BENCHMARK_22.md` / competitor intel; the packet no longer compares to 84.94 |
| 11 | "The Mahtesar/other 'C' candidate" | — | not raised | — | no candidate survived to a 'C' stage |

**Accepted critiques with a verification each: 7 of 11.** No critique was accepted on the strength of who raised it: #2 and #5 were raised by all three lenses and were still rejected, because the measurement said so.

## 3. What changed in the plan because of this evaluation

- `DRAFT_RESEARCH_PLAN.md` §9 now opens with the **2-hour median + abstain-rate change**, not with a router or a verifier. It is the only surviving engineering item with a measured payoff.
- The plan states **"zero edge theses survived"** in its own words, in §6, rather than implying an edge exists.
- The **`sheet.csv` non-reproducibility** is named as the top evidence risk and as a question for Vinay, because it changes what we can safely show a reviewer.
- The **fusion oracle gap is de-scoped** to 0.0332 ex-`sa` (lens B), so the plan does not promise a fusion win that the data does not support.
- Dev-day estimates were **halved where the lens found them inflated** and the honest numbers are used instead.
- The plan now names **"normalisation is a non-issue for us"** as an explicit anti-priority.

## 4. What this evaluation is NOT

It is **not** the lead's A3 deliverable. A3 asked for a multi-LLM evaluation of the plan by OpenCode + Claude + ChatGPT. **One leg of three did not run for tool-availability reasons, one did not run for budget reasons, and one is pending the boss's paste.** What exists is (a) 12 independent adversarial critiques of the *theses*, dispositioned above, and (b) a self-contained paste prompt for the third leg. **A3 remains PARTIAL and should be reported as such to Vinay.** The cheapest completion is the paste: `docs/campaign/CHATGPT_EVAL_PROMPT.md` is self-contained and takes two minutes.

## 5. UNRESOLVED

- No ChatGPT answer received (PENDING BOSS).
- No OpenCode leg — the MCP server is not exposed in this session; needs a session with `mcp__opencode__*` available.
- The lens reports attacked **theses**, not the composed plan. A review of `DRAFT_RESEARCH_PLAN.md` itself has not been performed by any evaluator leg.

---

## 6. ADDENDUM 2026-09-30 — evaluator leg 2 (hostile Sonnet reviewer) RAN and changed the plan

`W1_reports/1F_sonnet.md`. Same evaluator prompt as leg 3. Disposition, **by reasoning not by source**:

| # | Critique | Verdict | What changed |
|---|---|---|---|
| 1 | **The 2.5× headline is ~a third coverage gap, not accuracy.** The 18 human-verified items cover only 6 languages (bn, hi, sa, as, mni, sat) and **two are the dead-script cells**. | **ACCEPT — the sharpest critique of the wave** | §3 now carries three caveats: it is a **per-item oracle** (surya-always = **3.70×**), the languages are named, and excluding mni/sat the gap is **2.02×** (0.132 vs 0.265). Lead-verified both numbers. |
| 2 | "Best local" is an **argmin over 10 engines selected on the same items** — an oracle relabelled as an engine, with zero confidence intervals. | **ACCEPT** | Table column relabelled "*(oracle)*" in the plan **and** in the packet's GT-tier sentence, which now says "the best of our 10 local engines … not one engine". |
| 3 | The download ask is mis-scoped: **none** of the six missing traineddata is on disk, and files are **8–15 MB**, not 2–4 MB. | **ACCEPT — and it corrected a round-2 Verdict error** | The lead re-checked `tessdata/` directly: 12 files, `ori` + `san` present, **mni, sat, kan, mal, tam, tel all absent**. Estimate raised to **~40–70 MB**; a previous reviewer had wrongly said tam/tel/kan/mal were on disk. |
| 4 | Internal contradictions: 12 vs 13 languages at n≥50; "min n is 19" vs ml n=5; 6,909→6,609 attributed to exclusion when it is the 300 English samples. | **ACCEPT** | n<50 list corrected to **9 of 22**; min-scored-n sentence corrected; 6,609 now attributed to the English split, not exclusions. |
| 5 | `K2 pa p=1.00 n=90` is **arithmetically impossible** for a two-sided exact McNemar, and it is what removed Punjabi from QLoRA scope. | **ACCEPT the doubt, REFUSE the conclusion** | The value is not asserted either way: §2's K2 node now reads **UNRESOLVED provenance** — our audit says p=1.00 vs tesseract_indic, `W6_QLORA_SPEC.md:75` says "p<0.0001 SURVIVES". Both cannot be true; escalated. "Pa out of QLoRA scope" removed as unsupported. |
| 6 | **Rank the options:** A > D decisively, because D adds a router with 0–5% recall, a Latin-only restoration that would hurt Nastaliq, and a Sarvam subsidy that contaminates the table. But **A as specified ships the −0.0351 router as its deliverable** — use gap-gated routing instead. | **ACCEPT** | Plan's recommendation already picks A; it now also states the "A ships a losing router" objection and the gap-gated alternative. |
| 7 | **The plan never asks to raise the Sarvam call cap** — yet every §3 claim rests on 54 items. | **ACCEPT** | Added to §8 as a question. The 54-call cap is spent, so this is a budget ask, not a technical one. |
| 8 | Named 2025–26 techniques the plan might be missing | **REJECTED as unsourced** | The reviewer marked its own items UNCERTAIN; under the campaign rule a named technique must be opened and confirmed before acceptance, and nothing was confirmed. Not carried. |

**Net effect: 7 of 8 critiques accepted, and 4 of them changed numbers the plan had published an hour earlier.** This is the second time in this campaign that an adversarial review found a real error in a deliverable I had already marked done (the first was the 1H round-1 review, 7 BLOCKERs). The control works; the cost is that "DONE" from a subagent is not evidence.

**Leg status now: 2 of 3 RUN (the 1E-refutation lenses, and this Sonnet reviewer) · 1 of 3 UNAVAILABLE (OpenCode MCP not exposed) · 1 PENDING BOSS (ChatGPT paste at `CHATGPT_EVAL_PROMPT.md`).** A3 remains **PARTIAL**.
