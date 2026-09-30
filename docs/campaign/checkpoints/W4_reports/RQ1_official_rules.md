# RQ-1 — Official AksharDrishti Rules & Deadline · live re-verification

**Verdict agent · date opened: 2026-09-30 (all URLs in this report opened on this date)**
**Mode: read-only research. No downloads, no training, no Sarvam. No repo file written except this report.**

## Method and the harvest-first payoff

`docs/research/level7/c/c2/LEDGER.md` §A rows A01–A09 (2026-09-26 snapshot) were read first and **hold**. This
report does not redo the harvest; it re-verifies it against live primary sources and answers the five sub-questions.

**The single most important technical discovery of this pass:** the AksharDrishti page is a client-rendered SPA.
A plain HTTP fetch of the page returns only the **Timeline** table — the `Evaluation Process`, `Eligibility Criteria`
and `Contact Us` tab bodies, and the entire **full problem statement** (behind a "View Full Details →" modal), are
absent from the static HTML. The four candidate sub-routes
(`/…-hackathon/evaluation-process`, `/prize`, `/problem-statement`, and the UAT mirror) all return the **global
nav/footer chrome only**. Therefore the 2026-09-26 evaluation-parameter quote (A02) **cannot be re-verified by
static fetch**; it was obtained by a rendered browser read. This report renders the page (Playwright) and clicks
the tabs. Any future agent re-verifying A02 must render, not fetch.

**Machine-checked absence test (the strongest form of "no rule published").** I enumerated the full text of the
rendered page (all four tabs + the full problem-statement modal) and searched for every plausible metric token.
Result — **zero occurrences** of: `CER`, `WER`, `metric`, `substitution`, `deletion`, `insertion`, `edit distance`,
`seconds`, `latency`, `score`, `weight`, `percentage`, `third-party`, `dataset`, `test set`, `license`.
This is a reproducible negative, not an impression.

---

## 1. Metric — is any CER/WER/accuracy/S-D-I/seconds-per-page rule published now?

**ANSWER: UNKNOWN — no metric, formula, threshold, or weighting is published. "Accuracy" appears only as an
undefined evaluation dimension. A02 CONFIRMED and sharpened: the table has exactly 2 columns (Parameter |
Description), 6 rows, and no weight column.**

The Evaluation Process tab, verbatim, in full:

> "Parameter	Description
> Approach Towards Problem Solving	Product Idea, Degree of Innovation, Simplicity of Final Solution, Uniqueness & Scalability of Idea, Novelty of Approach
> Business Use Case	Business Case, USP and Vision
> Solution Technical Feasibility	Product features, Scalability, Interoperability, Enhancement & Expansion, Underlying Technology Components & Stack, and Futuristic Orientation
> Product Roadmap	Productization Potential, Cost to Build Product, Go to Market Strategy, Time to Market
> Team Ability & Culture	Team Leader's Effectiveness (Ability to guide, Ability to present idea), Ability to Market Product, Growth Potential of Organization
> Addressable Market	Channel, Deployment Cost, Customization and Enhancement Cost (Per Person Per Month Basis), and Resource Rate Evaluation for 4 years"

The **only** official statement anywhere on the page that names an evaluation target — from the problem
statement's Objectives, verbatim (note: "or" is **as published**; almost certainly a typo for "for"):

> "Establishing Standardized Evaluation Pipelines or accuracy, layout detection, and multilingual text handling."

So three evaluation dimensions are named — **accuracy, layout detection, multilingual text handling** — with
**no metric, no formula, no threshold, no weighting, and no CER-vs-WER rule**.

- URL: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (tab "Evaluation Process"; full text via the "View Full Details →" modal)
- Date opened: 2026-09-30 · **PRIMARY** (for the six parameters and the three dimensions) · **UNKNOWN** (for any metric)

### 1a. HIGH-RISK CONFLATION ALERT — a seconds-per-page rule DOES exist officially, but for a *different* challenge

An official Government of India page publishes numeric OCR thresholds:

> "Based on open source technology
> Word Level Accuracy > 95%
> Low latency < 1 sec/page"

> "Government of India offices receive multiple communications on paper in regional languages.
> These documents (both printed and handwritten) to be digitized using OCR and then translate then worked upon and then needs to be translated back and responded in original regional language."

- URL: https://innovateindia.mygov.in/bhashini-challenge/ (section "Objective", problem statement **02**)
- Date opened: 2026-09-30 · **PRIMARY for the 2023 Bhashini Grand Innovation Challenge · NOT the AksharDrishti rule**

**This page's own timeline is 2023** ("Launch of Innovation Challenge | Monday, 12 June 2023" … "Declaration of
Results | Thursday, 16 November 2023"). It is the **Bhashini Grand Innovation Challenge (2023)**, not
AksharDrishti 2026. **NEVER cite "Word Level Accuracy > 95%" or "1 sec/page" as the AksharDrishti rubric.**

**Why this matters now (INFERENCE, clearly marked):** a "seconds per page" shape exists in genuine Bhashini
material. That is the most likely provenance of the student-repo "seconds per page" claim already withdrawn in
`proto-80`, and of any future re-introduction of it. It remains **not-official for AksharDrishti**. Anyone who
wants to use a speed target must cite the 2023 page **and label it 2023**, or drop it.

---

## 2. Submission format — files or hosted API? Is JSON / searchable PDF specified? What must be submitted?

**ANSWER: UNKNOWN — no files-vs-API statement, no upload mechanics, no templates or size limits published.
JSON + searchable PDF appear only as a technical focus area, not as a submission requirement.**

JSON and searchable PDF, verbatim, under **Focus Area 5 of 6**:

> "Post-OCR Pipeline Innovations
> Layout-preserving output formats (JSON, searchable PDF)
> Automatic transliteration and language detection
> Context-based correction and formatting"

- URL: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (full problem statement modal)
- Date opened: 2026-09-30 · **PRIMARY** that JSON/searchable PDF are named as a focus area · **UNKNOWN** that they are required deliverables

The word "submission" occurs on the whole page **only** in the eligibility sentence ("required to get registered
if they get selected for the final submission") and in the TBD timeline row names. There is **no** statement of
whether a prototype is delivered as files, a repo, a hosted endpoint, or a live demo.

- **DERIVED** (from the timeline row names only): the deliverable classes are *ideas* ("Last date of registration
  - submission of ideas"), an *initial prototype* ("Last date for initial prototype submission (for Stage 2)"), and
  a *final prototype* ("Last date for final prototype submission (Stage 3)"). The **format of each is unpublished**.
- **Adjacent, NOT AksharDrishti (2023 challenge):** "A: (a) Stage 1 - Registration form + PPT application
  (b) Stage 2 - HW shipment + prototype build out (c) Stage 3 - In person jury presentation" —
  https://bhashini.gov.in/sahyogi/hackathon/open-handheld-ai/FAQ, opened 2026-09-30. Do not transfer this to AksharDrishti.

---

## 3. Deadline — is ANY date published? Do the internal Oct 4 / Oct 15 / qualifiers-30-09 claims have an official basis?

**ANSWER: NO official deadline exists. Ten of twelve timeline rows are TBD, including every submission,
screening, qualifier and winner date. None of the three internal claims has an AksharDrishti basis. The
"qualifiers 30/09" claim is RESOLVED: it belongs to the Rajasthan Language Model Training Hackathon, a different track.**

The Timeline tab, verbatim, complete — 12 rows, 2 dated, 10 TBD:

> "Activity	Timeline
> Launch of Innovation Challenge	12/02/2026
> Query sessions for problem statements	TBD
> Last date of registration - submission of ideas	TBD
> Initial screening of applications (Stage 1)	TBD
> Declaration of results (Stage 1 qualifiers)	TBD
> Pitch Screening Session	23/07/2026
> Last date for initial prototype submission (for Stage 2)	TBD
> Evaluation of stage 2 initial prototypes	TBD
> Declaration of results (Stage 2 qualifiers)	TBD
> Last date for final prototype submission (Stage 3)	TBD
> Evaluation of stage 3 prototypes	TBD
> Declaration of winning teams	TBD"

- URL: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (tab "Timeline")
- Date opened: 2026-09-30 · **PRIMARY** · A05 CONFIRMED, unchanged.

### 3a. The "qualifiers close 30/09" claim — traced to the WRONG hackathon (decision-changing)

> "Launch of the Challenge (Registration Opens) | 23/07/2026
> Query sessions for problem statements | 30/07/2026
> Last date of registration - submission of ideas | 31/08/2026
> Declaration of results (Stage 1 qualifiers) | 09/09/2026
> Last date for Initial bench marking, Data collection and validation (for Stage 2 & Stage 3) | 22/09/2026
> Evaluation of stage 2 & 3 | 24/09/2026 - 29/09/2026
> **Declaration of results (Stage 2 & 3 qualifiers) | 30/09/2026**
> Last date for Model training and Optimization (Stage 4) | 05/10/2026
> Evaluation of stage 4 | 06/10/2026 - 09/10/2026
> Declaration of results (Stage 4 qualifiers) | 14/10/2026
> Last date for testing and iteration (Stage 5) | 16/10/2026
> Evaluation of stage 5 | 19/10/2026 - 21/10/2026
> Declaration of results (Stage 5 qualifiers) | 22/10/2026
> Publishing Results and Scalability Planning | 23/10/2026"

> "Rewards & Opportunities
> ₹90 lakhs
> Total Prize Pool"

- URL: https://bhashini.gov.in/sahyogi/hackathon/rajasthan-language-model-Training-Hackathon
- Date opened: 2026-09-30 · **PRIMARY** · **DIES as an AksharDrishti rule** (different hackathon)

**Verdict: the internal claim "qualifiers close 30/09" is a Rajasthan date.** It is a *Stage 2&3 qualifier
declaration*, not an AksharDrishti submission deadline. The on-disk record R132 already carried this warning
("TRANSFER: SURVIVES as timing context, DIES as rules (different hacka…"). **CONFIRMED today.** Rajasthan is
separately launched and separately branded — PIB release 2026-07-02, "BHASHINI Showcases Multilingual AI
Innovations at NCeG 2026; Launches Rajasthan Language Model Training Hackathon"
(https://www.pib.gov.in/PressReleasePage.aspx?PRID=2280490, opened 2026-09-30).

**INFERENCE (not fact):** AksharDrishti's only dated event, **Pitch Screening Session 23/07/2026**, is the *same
date* as Rajasthan's "Launch of the Challenge (Registration Opens) | 23/07/2026". A same-date collision on two
sibling Bhashini pages is the most plausible mechanism by which the two tracks' schedules got merged in internal
notes. Plausible, unproven.

**Oct 4 and Oct 15: no official basis found on any source.** UNKNOWN. (`INTEGRATION_REPORT.md:146`'s
"2026-10-15 Bhashini qualifier deadline" has **no primary source**; note 15 Oct sits near Rajasthan's Stage-4
qualifier date of 14/10/2026 — flagged as a hypothesis only, not a finding.)

### 3b. Positive control — the site CAN publish full dated timelines, so the TBDs are a real gap

Rajasthan 2026 publishes 15 dated rows; VYOMA 2026 publishes 16:

> "Registration portal opens | 30/04/2026 … Declaration of Stage 1 shortlisted teams (up to 20 teams) | 21/07/2026
> … Grand Finale – in-person prototype showcase | TBD
> Jury deliberation and final evaluation | TBD
> Declaration of winners – 4 teams selected | TBD"

- URL: https://bhashini.gov.in/sahyogi/hackathon/open-handheld-ai · opened 2026-09-30 · **PRIMARY** (for VYOMA) ·
  **DERIVED** (that AksharDrishti's TBDs are editorial absence, not a fetch artefact — the timeline *was* rendered
  in a live browser and still showed TBD)

---

## 4. Which external models and data are allowed? Is Bodhan/Surya/PaddleOCR-class open-weight usage sanctioned?

**ANSWER: Open-source OCR usage is explicitly PROMOTED and PaddleOCR is named. No restriction on downloaded
third-party weights is published. Third-party training data, hosted APIs and paid/closed models: nothing
published either way — UNKNOWN.**

Verbatim, from the problem statement's **Objectives**:

> "Promoting Fine-Tuning and Benchmarking of open-source OCR frameworks like Tesseract, EasyOCR, TrOCR, and PaddleOCR."

Verbatim, **Focus Area 5 of 6**:

> "Model Adaptation and Fine-Tuning
> Integration with LayoutLM, Donut, DocTR
> Use of GPU-based fine-tuning environments
> Optimization of open-source OCR engines"

And from **Objectives**:

> "Delivering Deployment-Ready Solutions compatible with Bhashini's document stack."

- URL: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (full problem statement modal)
- Date opened: 2026-09-30 · **PRIMARY**

**Reading for the campaign:** "Optimization of open-source OCR engines" is a *named focus area*, and fine-tuning
those engines is an *objective*. PaddleOCR is therefore sanctioned by name. **Bodhan and Surya are not named**,
but they sit in exactly the sanctioned category ("open-source OCR engines" / "open-source OCR frameworks"), so
they are **permitted by implication, not by name**. No clause forbids downloaded third-party model weights.

### 4a. Adjacent Bhashini restrictions that touch this — but are NOT AksharDrishti's rules

From https://innovateindia.mygov.in/bhashini-challenge/ (the **2023** Grand Innovation Challenge), opened 2026-09-30,
**PRIMARY for 2023 · NOT AksharDrishti**:

> "7. The teams shall not display any existing solution or collaborate with companies that have existing solutions. Such entries, if identified, shall be liable for disqualification."

> "14. The solution should not violate/breach/copy any idea/concept/product already copyrighted, patented or existing in this segment of the market."

> "Based on open source technology"

These are the **only** published Bhashini clauses bearing on third-party use. Rule 7 is aimed at *presenting an
existing solution as your own*, not at *using an open-weight model*. Do not present rule 7 or rule 14 as an
AksharDrishti rule; AksharDrishti publishes no equivalent.

Also adjacent, VYOMA only: "Solutions need not be limited to Bhashini APIs and models, but should feature them."
(https://bhashini.gov.in/sahyogi/hackathon/open-handheld-ai/FAQ, opened 2026-09-30.) VYOMA, not AksharDrishti.

---

## 5. Test-set description — what does the page say the data/domain is? Handwriting? Low-quality? Code-mixing? 22 languages? Held-out test set?

**ANSWER: Domain is described; handwriting, low-quality scans and code-mixing are all explicitly named.
"22 languages" appears NOWHERE on the page (zero occurrences of the token "22"). NO dataset, NO test set and
NO held-out split is published — teams must bring their own data.**

Verbatim, the domain sentence (problem-statement header):

> "Indian language documents—particularly government, legal, and citizen-service records—exist in highly diverse formats, scripts, and quality levels, including complex layouts, low-resolution scans, handwritten content, and multilingual text."

Verbatim, **Key Focus Areas** (all six, in full — this text is **not on disk anywhere** and is new to the campaign):

> "Improved OCR for Complex Layouts
> Multi-column and nested table structures
> Forms with fixed field alignments
> Complex government and legal templates
> Low-Quality and Noisy Scans
> Handling blur, fading, folds, stamps, and seals
> Correcting skewed or rotated pages
> Denoising and contrast enhancement
> Handwritten Text Recognition
> Full-page handwritten or cursive text
> Mixed typed and handwritten documents
> Regional handwriting styles in Indic scripts
> Multilingual and Code-Mixed Inputs
> Multi-script documents (e.g., Hindi–English–Tamil)
> Code-mixing and language-switching detection
> Model Adaptation and Fine-Tuning
> Integration with LayoutLM, Donut, DocTR
> Use of GPU-based fine-tuning environments
> Optimization of open-source OCR engines
> Post-OCR Pipeline Innovations
> Layout-preserving output formats (JSON, searchable PDF)
> Automatic transliteration and language detection
> Context-based correction and formatting"

- URL: https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon (full problem statement modal)
- Date opened: 2026-09-30 · **PRIMARY**

Item by item:

| Asked about | Published? | Verbatim basis |
|---|---|---|
| Handwriting | **YES** | "Full-page handwritten or cursive text" · "Regional handwriting styles in Indic scripts" |
| Low-quality scans | **YES** | "Handling blur, fading, folds, stamps, and seals" · "Denoising and contrast enhancement" |
| Code-mixing | **YES** | "Code-mixing and language-switching detection" · "Multi-script documents (e.g., Hindi–English–Tamil)" |
| 22 languages | **NO** | Regex-tested: `/22\s*(Indian\|Bhartiya\|languages)/i`, `/\b22\b/`, `/scheduled languages/i`, `/languages?\s*(covered\|included\|scoped)/i` → **all four false** |
| Held-out test set | **NO** | no `dataset`, no `test set`, no train/test split, no sample data anywhere on the page |
| Data provision | **NO** | nothing is supplied to entrants; no data link, no corpus, no sample set |

**Campaign consequence (DERIVED):** the campaign's **22-language scope is not a hackathon requirement** — it is a
self-imposed scope traceable to the lead's 2026-09-29 ask, not to any published rule. The only language signal is
generic "Indian languages" plus the single example "Hindi–English–Tamil" (which notably includes **English**).
And because **no official data or test set exists**, our `probe22` / `south_400` numbers are measurements against
*our own* held-out data — they are not comparable to any official figure, and no official figure exists to compare
against. This is a **sharp UNKNOWN and it is the correct, complete answer.**

---

## 6. New notice, extension, results or schedule change published since 2026-09-26?

**ANSWER: NONE. No change of any kind found. Every A01–A09 row survives. Three things are newly *captured*
(not changed) that were absent from the on-disk ledger.**

Not changed (byte-for-byte consistent with the 2026-09-26 snapshot): the 12-row timeline with the same 2 dates
and 10 TBDs; the 6 evaluation parameters (A02 paraphrase confirmed, now quoted verbatim); no published metric;
no published prize; the eligibility wording (A06, now quoted verbatim).

**Newly captured (additive, not contradictory):**

1. **The full problem-statement text** — Objectives + all six Key Focus Areas. This is **not in the on-disk
   ledger at all**. A01 captured only the short teaser. The full text is the single most decision-relevant
   addition of this pass, because it is the *only* official text that mentions JSON/searchable PDF,
   open-source fine-tuning, handwriting, low-quality scans and code-mixing.
2. **The organiser contact address**, from the Contact Us tab, verbatim:
   > "For any queries or concerns, please contact us at the following email address
   > gic.dibd@gmail.com"

   **This is the official channel to ask the metric question directly.** It is the highest-value actionable
   item in this report: RQ-1 §1 is answerable in one email. (The 2023 challenge's own contact is
   `ajay.rajawat@digitalindia.gov.in` — different, do not confuse.)
3. **The `LATEST UPDATES` block is a 3-slide rotating carousel, and no slide carries a date or a deadline.**
   All three slides, verbatim, captured by 30 s of polling:
   - "Launch date: 12th February 2026!"
   - "Interested participants can explore the exciting opportunity"
   - "Registration link is active"

   This explains why the 2026-09-26 snapshot (A05) and today's reads differ in this block: the rotator moves.
   **A05's "Registration link reported active in Latest Updates rotator" is CONFIRMED and is a stable fact, not a
   new notice.**

**Prize (A08) — still not published as text, with a new explanation.** Clicking the "Prize" nav item does not
navigate and renders no prize content. The prize is present only as an image,
`AksharDrishtiAward.37efd6d63d95449a443b.png`, with an **empty `alt` attribute**. Contrast: Rajasthan publishes
"₹90 lakhs / Total Prize Pool" as live **text**. So the platform *can* render prize text, and AksharDrishti's
absence is a real absence of published text. **I did not download or read the image, so any amount visible in it
is UNKNOWN and I will not guess one.**

**Residual unverified channel (flagged, not pursued):** the "Structured Journey / Stages of AksharDrishti
Hackathon" block is also an image, `AkasharDrishtiSatge.28f5018adcf49c339f1b.png`, with an **empty `alt`**. The
stage *definitions* may be visible on screen to a human but are not machine-readable text. If the boss needs the
stage structure, someone must open the page visually. I did not download images (forbidden), so this is a
deliberate honest gap, not an oversight.

---

## 7. Current stage status of the AksharDrishti track

**ANSWER: The page publishes NO stage status — UNKNOWN. All observable signals are consistent with an OPEN,
still-registered, featured track that has NOT published results.**

Official statement: **none exists.** The page never says "open", "screening complete", "results out", or
"closed".

Derived signals, all from https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon and
https://bhashini.gov.in/hackathon, opened 2026-09-30 (**DERIVED**):

- **Listed under the ACTIVE "Featured Hackathons" tab, not "Past Hackathons."** On bhashini.gov.in/hackathon the
  tab buttons carry `border-b-2 border-[#c25f3a] text-[#c25f3a]` on "Featured Hackathons" (active) versus
  `text-gray-600 hover:text-gray-900` on "Past Hackathons" (inactive). The AksharDrishti card sits with the
  active set {Rajasthan, VYOMA, AksharDrishti, VaniSangam, Khasi&Garo, Mizo}; the 2025 tracks
  {bsv2, bdic, sanrakshan, sansad} sit in a hidden container.
- **A "Register" button is present** in the page header.
- **No "Registration Closed!" banner**, whereas the 2025/finished tracks do carry one — bdic and bsv2 both show
  "Registration Closed!", and Rajasthan's live page shows "Registration Closed!" with the update slide
  "Registration link is Inactive". **AksharDrishti shows neither**, and one of its three rotator slides says
  "Registration link is active".
- **No results have been published anywhere.** No Stage-1 qualifier list, no winner announcement, on any primary
  channel. On-disk **R127's UNKNOWN re-verified and unchanged** on 2026-09-30.
- The last dated event remains **Pitch Screening Session 23/07/2026**, and the row immediately after it
  ("Last date for initial prototype submission (for Stage 2)") is still TBD.

**Therefore: cannot claim we are in, nor out. Cannot claim the field is strong or weak. Unknown stands.**

---

## 8. Official social posts — reachable? Any post-deadline or extension notice?

**ANSWER: LinkedIn was REACHABLE (not blocked) and confirms A03 verbatim. No post-deadline or extension notice
exists since the 2026-03-14 extension. Facebook corroborates the same post.**

Verbatim, official DIBD/Bhashini LinkedIn post:

> "We are pleased to announce that the registration deadline for BHASHINI's AksharDrishti Hackathon has been extended to 30 March, 2026.
> With the encouraging response from innovators, students, and technology enthusiasts, this extension provides additional time to register and develop impactful solutions that strengthen language technology, accessibility, and inclusive digital communication."

- URL: https://www.linkedin.com/posts/digiital-india-bhashini-division_importantupdate-akshardrishti-bhashini-activity-7438569655599865856-rnSZ
- Post date: **2026-03-14** · Date opened: 2026-09-30 · **PRIMARY** · **A03 CONFIRMED verbatim**

Corroboration on the official Bhashini Facebook page, dated Mar 14, 2026, same text
(https://www.facebook.com/100093281985246/posts/importantupdatewe-are-pleased-to-announce-that-the-registration-deadline-for-bha/821066227679436, opened 2026-09-30) · **PRIMARY** (official page) — A03 is now **dual-sourced**.

**No newer notice found.** Searches specifically for late-September-2026 AksharDrishti announcements, PIB
releases, stage-1 results and qualifier lists returned **nothing AksharDrishti-specific**. The only late-2026
Bhashini news item found was the **Rajasthan** launch (PIB, 2026-07-02). A03 remains the most recent dated
official communication about this track.

**Note on A03's derivation:** the original 30 March 2026 registration deadline is stated nowhere on the official
page (it is a TBD row); the "originally 12 March 2026" figure in A03 is likewise not on the official page. Both
come from the announcement post's own framing, not from a published rule.

---

## The withdrawn student-repo metric — status, and a live stale claim in our own repo

The campaign has **correctly withdrawn** "CER with bootstrap 95% CI, WER, S/D/I breakdown, seconds per page" as the
hackathon rubric (`docs/campaign/protocols/proto-80-hackathon-metric-alignment.md`, correction dated 2026-09-30;
also `proto-86-draft-plan-fixes.md` D8). I found **no official source** repeating it. Marked **not-official**:
its origin is a **student B.Tech project repo**, `github.com/Ayush-04-spec/akshardrishti` (K. K. Wagh Institute),
describing **its own** evaluation.

**Where it still circulates in our repo — a live defect I cannot fix (I may write only this report):**

> `docs/campaign/DRAFT_RESEARCH_PLAN.md:18` — "**The hackathon rubric is CER with bootstrap 95% CI, WER, S/D/I breakdown and seconds per page** — evaluation criteria itemised in `docs/campaign/protocols/proto-80-hackathon-metric-alignment.md`."

That line **still asserts the withdrawn claim as the hackathon's rubric** and points at the very protocol that
withdrew it. It directly contradicts `proto-80` and `proto-86` and contradicts this report. Also stale:
`docs/campaign/checkpoints/W1.md:145` ("hackathon rubric absent | APPLIED — CER + bootstrap 95% CI, WER, S/D/I,
sec/page") and `docs/campaign/protocols/proto-99-concern-crosswalk.md:194`.
**→ Boss/Miss action: rewrite `DRAFT_RESEARCH_PLAN.md:18` to "official scoring rules are not public; we report
CER with CIs, WER and error breakdown on our own terms."** Note that the plan is the artefact going into the
Vinay meeting; a cross-examiner who opens the official page will catch this.

**Second caution, newly established (see §1a):** "seconds per page" is not a pure invention — an official
Bhashini page publishes "Low latency < 1 sec/page" for the **2023** challenge. So the withdrawn claim has a
plausible genuine ancestor. It is **still not the AksharDrishti rule**, and any reintroduction must either cite
the 2023 page and label it 2023, or be dropped.

---

### Sources relied on

All opened **2026-09-30**. Every URL below was actually opened; none is cited from a search snippet alone.

| # | URL | Date published | Class | Used for |
|---|---|---|---|---|
| 1 | https://bhashini.gov.in/sahyogi/hackathon/akshardrishti-hackathon | live, undated | PRIMARY | §1–§8. Rendered; all 4 tabs + full problem-statement modal |
| 2 | https://bhashini.gov.in/hackathon | live, undated | PRIMARY | §6, §7 — Featured-vs-Past tab classification |
| 3 | https://www.linkedin.com/posts/digiital-india-bhashini-division_importantupdate-akshardrishti-bhashini-activity-7438569655599865856-rnSZ | **2026-03-14** | PRIMARY | §8, §3 — registration extension to 30 March 2026 |
| 4 | https://www.facebook.com/100093281985246/posts/importantupdatewe-are-pleased-to-announce-that-the-registration-deadline-for-bha/821066227679436 | **2026-03-14** | PRIMARY | §8 — corroborates #3 |
| 5 | https://bhashini.gov.in/sahyogi/hackathon/rajasthan-language-model-Training-Hackathon | live, undated | PRIMARY | §3a, §6, §7 — true owner of 30/09; "Registration Closed!" contrast; ₹90 lakhs |
| 6 | https://innovateindia.mygov.in/bhashini-challenge/ | **2023** | PRIMARY (2023 challenge only) | §1a, §4a — the real "1 sec/page" + ">95%" thresholds; open-source clauses; NOC rule |
| 7 | https://bhashini.gov.in/sahyogi/hackathon/open-handheld-ai | live, undated | PRIMARY (VYOMA only) | §2, §3b, §4a — dated-timeline positive control; FAQ |
| 8 | https://bhashini.gov.in/sahyogi/hackathon/open-handheld-ai/FAQ | live, undated | PRIMARY (VYOMA only) | §2, §4a |
| 9 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2280490 | **2026-07-02** | PRIMARY | §3a — Rajasthan launched as a separate track |
| 10 | https://uat-bhashini.bhashini.co.in/sahyogi/hackathon/akshardrishti-hackathon | live, undated | PRIMARY (mirror) | cross-check: same 10 TBDs, same 2 dates (confirms R131) |

Opened and found **empty of hackathon content** (recorded so the next agent does not re-walk them): the four
sub-routes `…/akshardrishti-hackathon/{evaluation-process,prize,problem-statement}` and the UAT `…/evaluation-process`
— all return global nav/footer chrome only, because the SPA does not server-render them.

**Explicitly NOT used as a source for any rule** (per instruction): student project repos, blogs, news articles.
The only news opened (PIB, #9) is used solely to confirm that Rajasthan is a separate track — never to establish
a rule.

---

### UNRESOLVED

1. **The metric itself — UNKNOWN, and it is the answer.** No CER/WER/threshold/weighting exists. Machine-verified
   zero hits across the whole rendered page. **Resolvable by one email to `gic.dibd@gmail.com`** (§6, new).
2. **Submission format — UNKNOWN.** Files vs hosted API, deliverable templates, size limits: nothing published.
   JSON/searchable PDF are a *focus area*, not a requirement.
3. **Every date except launch (12/02/2026) and pitch screening (23/07/2026) — UNKNOWN.** 10 of 12 rows TBD.
4. **Stage status — UNKNOWN.** Not past screening as far as any primary source shows; not provably still open either.
   "Featured tab + Register button + no closed banner" is DERIVED, not official.
5. **Third-party training data / hosted APIs / paid models — UNKNOWN.** AksharDrishti publishes no clause.
   Open-*source* OCR is promoted; whether *open-weights-downloaded-from-elsewhere* and *commercial APIs* are
   permitted is simply not addressed. The 2023 challenge's rules 7 and 14 are the nearest published text and are
   not AksharDrishti's.
6. **The prize — UNKNOWN.** Published only inside an image with an empty `alt`; I did not download it. The
   platform renders prize text for Rajasthan, so the absence is real, but I will not guess an amount.
7. **The stage structure — UNKNOWN.** Also image-only (`AkasharDrishtiSatge.*.png`, empty `alt`).
8. **"22 languages" has no official basis — UNKNOWN as a requirement.** The number appears nowhere on the page.
   It is our own scope, not a published rule. Same for any held-out-test-set assumption: no official data exists.
9. **Two residual image-only channels** (prize, stages) need one human eye on the live page to close.
10. **The original pre-extension registration deadline (12 March 2026, per A03) is not on the official page** —
    it survives only inside the 2026-03-14 announcement post. Treat as announcement context, not a published rule.
11. **Unfixed repo defect:** `DRAFT_RESEARCH_PLAN.md:18` still states the withdrawn metric as the official rubric.
    Needs a boss/Miss rewrite before the Vinay meeting.

**Bottom line for the campaign:** the official rules are *product-weighted and qualitative*; there is no metric to
target, no data to submit against, no test set, and no published deadline. Optimise the weak cells and the pitch,
report CER/CI/WER on our own explicitly-labelled terms, and stop treating any date as official. The single highest
value action available is **emailing `gic.dibd@gmail.com` and asking for the evaluation rubric and the Stage-2
submission date.**
