# VAJRASTRA INTERROGATION PROTOCOL v1.0
**Purpose:** Evolve the project 360° — not by doing more of the same, but by attacking our own
benchmark with real debate, real evidence, and researched best practice. Feed sections to
mini-boss agents; every answer lands in DECISIONS.log or IMPROVEMENTS_CURRENT_WORK.md.
**Grounded in:** disk state (4000 packs sealed), ULTIMATE_HYBRID_CONCERN law, published
research (Sarvam Indic OCR Bench, IndicDLP, IIIT-ILST, PaddleOCR-VL papers, open-model surveys).
**Owner:** Srujan · **Date:** 2026-09-13 · **Mode:** 7-day loop, red/blue teams, parallel.

---

## PART 0 — DIRECT ANSWERS (disk truth, the questions you already asked)

### 0.1 "If anyone doubts, can we re-run everything live, and how long does it take?"
YES. This is the strongest property of the repo. Exact numbers from HEARTBEAT medians
(DASHBOARD 2026-09-13 11:48):

| engine | ms/page | 400 pages sequential |
|---|---|---|
| rapidocr | 967 | 6.5 min |
| doctr | 3,166 | 21 min |
| anuvaad_tesseract | 3,680 | 25 min |
| tesseract_indic | 4,871 | 32 min |
| tesseract_bilingual | 4,874 | 32 min |
| openbharatocr | 5,026 | 34 min |
| indicphotoocr | 15,700 | 1.7 h |
| surya | 16,925 | 1.9 h |
| easyocr | 30,741 | 3.4 h |
| paddleocr_indic | 95,568 | 10.6 h |
| **TOTAL** | | **20.2 h sequential** |

Parallel as orchestrator fill runs it (7-way, CPU contention): **~2–4 h wall clock, unattended**
(`orchestrator.py autoloop 30` is resume-safe, so a crash costs nothing). Correct procedure
per archive law: `mv level2/out level2/out_archive/full_regen_$(date +%F)` THEN re-run —
never delete first. So: "delete out/ and regenerate everything" = ~4 hours of machine time,
zero human time. That is a valid, provable claim to make to David or Vinay.

### 0.2 "Is the OCR model really being used to its full potential?"
HONEST VERDICT: **No — and we know exactly where.** The seal proves coverage, not maximization.
Known headroom (from IMPROVEMENTS_CURRENT_WORK.md, most decided as "low ROI" = assumption,
not measurement):
- doctr: CRNN backend in use; PARSeq backend available in doctr 1.1.0 — never A/B'd.
- rapidocr: mobile rec models in use; PP-OCRv5 server rec never tried.
- tesseract: tessdata fast in use; tessdata_best + PSM grid never A/B'd (only "low ROI" note).
- paddle: server det replaced by mobile under timeout pressure; textline_orientation off.
- surya: no language hints possible in 0.22.1 (verified) — but guided-layout flag and
  block-mode html extraction paths interact; only partially explored.
- 200 DPI renders: 300-DPI probe was 0/10 on 10 pages — which 10? Was the probe big enough
  to conclude? (C9 item — still open.)
- 31 historically-empty pages: proven GT-blank or unproven? (C9 open.)
Every "low ROI" line needs either a 4-page-gate measurement or an explicit accept-with-reason
entry in DECISIONS.log. That is what Category B forces.

### 0.3 "Are we really making the real full flesh of OCR from the target?"
Level 2 = capacity benchmark of free OSS engines at v1 configs on 400 real pages, verified
against PDF-layer GT, L1 gold, and family-deduped consensus. That is real. What it is NOT:
an accuracy-certified gold standard (L1 is T2-heavy), a handwriting/form/stress benchmark
(data is book-heavy), or a max-config bake-off (see 0.2). The interrogation below closes
each gap with evidence or an honest written limitation.

### 0.4 Pack-count correction for all messaging
400 pages × 10 engines = **4,000 packs**. Never 20,000 (law P103). In any slide/message.

---

## PART 1 — HOW TO RUN THE INTERROGATION (mini-boss protocol)

**Roles (run in parallel, max ~7 agents):**
- **RED** — attacks validity; must cite disk files or published sources for every attack.
- **BLUE** — defends with disk evidence only (counts, sha1s, report mtimes). No vibes.
- **EXEC** — runs 4-page-gate experiments; writes results to research/gates/.
- **SCRIBE** — every concluded question = one line in DECISIONS.log
  (`date | area | decision | why | evidence_path | owner`).

**Evidence standard (law-compatible):** A claim is TRUE only if (a) a file on disk shows it,
(b) a 4-page gate measured it, or (c) it is marked ASSUMPTION with a reason. Anything else
is a question, not a fact.

**Cadence:** 10 questions/day across categories · evening: SCRIBE consolidates · nightly
autoloop keeps dashboards fresh while agents argue.

---

## PART 2 — THE QUESTION BANK (~150)

### CATEGORY A — BENCHMARK VALIDITY & SELF-DECEPTION (the "are we fooling ourselves" set)
A1. Our primary GT is the PDF text layer. What fraction of the 400 pages actually HAS a text
    layer, and are all conclusions biased toward born-digital pages? (compute, don't estimate)
A2. PDF text layers can be wrong (bad font encoding, extraction artifacts). Did we ever
    sample 10 pages where layer text disagrees with the visible render — and check by eye
    which is right?
A3. L1 gold is mostly T2 distilled_vlm. We audit T2 engines partly against T2 gold. Where is
    the circularity, and which conclusions are immune vs contaminated?
A4. Family-dedup gives 7 independent votes; consensus needs ≥6. Is 6-of-7 near-unanimity
    actually "independence"? OSS engines share training corpora (same book scans, same
    IIIT data). What shared-data collapse could fake consensus?
A5. The 92 hallucination events (verify_v2): per-engine breakdown, base rate, and did a human
    eyeball at least 20 of them? Which verdicts changed after eyeballing?
A6. Empty outputs: for each engine's empties, how many are GT-blank pages vs engine failure?
    The 31 GT-empty list — is it pageset truth or pageset accident?
A7. English-leak detector (90% ASCII words on ≥5 words): on genuinely-mixed pages, could it
    flag correct behavior? List the flagged pages; how many are mixed-book true positives?
A8. Are we benchmarking engines or our harness? The easyocr reader-combo bug capped output
    for hours. What other wrapper-level caps exist that we haven't noticed (timeouts killing
    slow-but-good configs, binarized-retry path overwriting good outputs)?
A9. Capture-ratio denominators: PDF layer char counts include headers/footers/page numbers
    that engines may skip. Is "capture" under-measured by design? Quantify on 5 pages.
A10. LOOP detector threshold 0.6 8-gram redundancy: calibrated or guessed? What happens at 0.4?
A11. GARBAGE ratio uses Unicode categories — Devanagari matras are category M (kept), but
    what about legitimate symbols (₹, °, §)? False-positive rate on 20 sampled pages?
A12. The manifest's dominant_script came from L1 gold's script histogram. The 15
    manifest_tag_suspects — resolved or just listed? kn pages tagged dominant=Telugu: data
    truth or mis-tag? (kn_002–kn_013 are all Telugu-dominant — a Kannada benchmark where
    12% of 'kn' pages are Telugu is a finding, not a footnote.)
A13. Duplicate content: kn_035/kn_074 same render (same sha1). How many other cross-page
    duplicate renders exist in the 400? What does that do to per-language stats?
A14. Statistical power: 400 pages, per-script strata as small as ~40 (Devanagari-dominant).
    Are leaderboard deltas between engines within noise? Compute a confidence interval for
    the top-3 engines' median capture difference.
A15. Survivorship: pages that froze into the manifest are the openable, renderable ones.
    What failed to enter (password PDFs — 0 found; corrupt; OOR page_index) and does the
    freeze bias toward easy pages?
A16. Time-of-run bias: engines ran at different times under different CPU contention.
    HEARTBEAT medians mix engine speed with machine load. Does any latency conclusion
    survive a normalized re-measurement of 20 pages?
A17. Binarized-retry path: when the retry fires, does it ever produce WORSE text than the
    failed original would have? (C8 telemetry — open.)
A18. The seal gates G1–G11 are machine-checked, but who checks the checkers? When did
    seal_gen.py itself last get reviewed for a bug that would green-light a false seal?
A19. If David asks "how do you know your CER is real," what is the one-page demonstrable
    answer? Build it before Saturday.
A20. What would make us DECLARE Level 2 invalid? Pre-register 3 falsification conditions
    now, so we can't move goalposts later.

### CATEGORY B — ENGINE MAX-POTENTIAL (the "full flesh" set; each needs a 4-page gate or a DECISIONS.log waiver)
B1. doctr: PARseq vs CRNN backend — gate it (te/ta/kn/ml one page each). If PARseq wins,
    is a doctr_v2 rerun justified by expected yield?
B2. rapidocr: PP-OCRv5 server rec + Cls module on vs off — gate it. Server weights cost
    download time; measure gain first.
B3. tesseract_indic: tessdata_best vs fast — gate on the densest Telugu page. PSM 3 vs 6
    vs 4 — same gate. Any win ≥10% chars → config bump + targeted rerun of weak pages only.
B4. paddleocr_indic: was the server-det→mobile fallback ever re-tested after the timeout fix?
    Retry server det at 300s budget on 4 pages. Also textline_orientation=True on rotated pages.
B5. surya: SURYA_GUIDED_LAYOUT=false is set for the grammar-400 fix — does guided layout ON
    change output quality (not just crash)? Gate it.
B6. easyocr: per-script readers chosen; was paragraph=True vs False compared? allowlist
    for digits? decoder beam width?
B7. indicphotoocr: identifier_lang="auto" confirmed from disk (te_041–44) — but is auto the
    BEST mode? Gate identifier_lang=te on pure Telugu pages vs auto.
B8. anuvaad_tesseract: stack order anuvaad+hin+eng — does dropping hin (anuvaad+eng) change
    anything on pure Dravidian pages? Does adding the system's tam/kan/mal models to the
    anuvaad dir help mixed pages?
B9. openbharatocr: it is an honest alias of tesseract path. Should it be REMOVED from the
    leaderboard (double-counting tesseract) or kept with a bigger alias warning? Decide once.
B10. For each engine: what does its OWN documentation claim as best-practice invocation for
    Indic scripts, and where do we deviate? (Documented deviations = decisions, not accidents.)
B11. Cross-engine cascade: tesseract layout + surya recognition, or rapidocr det + paddle rec —
    is any 2-engine combo yield > best single engine? Gate on 4 pages; if yes, that's a
    research paper mini-result for the deck.
B12. Ensemble voting: where ≥3 independent families agree on a page's text, is agreement-text
    cleaner than any single engine (measured vs PDF layer CER)? If yes — free pseudo-GT
    expansion for Stage 3 without any human.
B13. DPI: 300-DPI re-render of the 31 empty pages (C9) — run it before claiming "engines
    at max."
B14. Per-engine timeouts: 300s wall — which engines ever hit it, and did the timeout (not the
    engine) create any empty? List them.
B15. Region structure: every pack is ONE full-page region. Do any engines natively give
    line/block boxes we threw away (paddle, rapidocr, surya all have them)? Storing them
    costs nothing and upgrades packs to layout-capable. Why is this still open (item 31)?
B16. Confidence harvesting (item 31): paddle/rapidocr return per-box confidence. Even if
    unused for scoring now, un-harvested confidence = discarded signal. Decide: harvest or
    formally waive.
B17. Native digits: engines that transliterate to ASCII digits — which ones, how often?
    For citizen-facing digitization this is an accuracy bug, not a style choice.
B18. Script confusion matrix: build engine-output-script × page-dominant-script counts from
    existing packs (pure disk work). Which engine confuses Telugu↔Kannada most? That's a
    pitch-slide exhibit.
B19. If we re-ran the single best config change per engine (from B1–B8), what's the
    projected yield delta and total machine time? If <2h machine time for >5% yield —
    do it before Sep 16; if not, write the waiver.
B20. What's the NEXT engine rung beyond configs — fine-tuned community checkpoints
    (HuggingFace "telugu ocr" fine-tunes of TrOCR/PARSeq)? 2h research task; if a credible
    checkpoint exists, it's a legitimate free L2.5 engine.

### CATEGORY C — METRICS & VERIFICATION SCIENCE
C1. CER normalization lowercases everything. Indic scripts have no case; Latin does. Our mixed
    pages lose case signal in CER. Harmless or real loss? Quantify on 5 Latin-heavy pages.
C2. WER on whitespace tokens is linguistically wrong for agglutinative Dravidian scripts
    (word = many morphemes). Indic OCR literature prefers akshara error rate. Should we add
    AKER (akshara error rate) as a third metric? Implementation: split on Unicode grapheme
    clusters; ~30 lines on top of existing edit distance.
C3. The Myers bit-vector edit distance silently truncates above 950 chars (swap). Which
    pages hit the cap, and did any CER get computed on a truncated string? (Bug audit.)
C4. gt_thin threshold: pages with <200 GT chars get null CER. What fraction of pages per
    script is excluded, and does the exclusion skew CER rankings?
C5. CER vs PDF layer on born-digital pages measures extraction-fidelity + engine error
    mixed. Can we separate: layer-vs-render fidelity (sample by eye) vs engine-vs-layer?
C6. Per-script CER slicing exists? CER_STAGE3B is per-page; do we have per-SCRIPT median
    CER per engine? That's the number David and BHASHINI will ask for first.
C7. Statistical rigor: bootstrap confidence intervals on per-engine median CER (resample
    pages, 1000 reps). Takes minutes; turns leaderboard into defensible ranking.
C8. Human spot-check protocol: we have no written protocol for human verification of
    engine output vs image. Write one (10 pages, 2 passes, disagreement adjudication,
    record CER-of-the-eye). Until it exists, every "verified" claim is partial.
C9. Inter-annotator agreement: when Srujan spot-checks, who checks Srujan? (Self-check
    bias is real; even a second pair of eyes on 10 pages changes credibility.)
C10. Regression alarm threshold: >2% relative on any scalar triggers. Was 2% ever
    calibrated? On a 400-page set, what natural run-to-run variance does the same engine
    show? (Re-run rapidocr on 20 pages to measure.)
C11. Consensus 5-gram Jaccard ≥0.6 — is 0.6 right for Indic? Calibrate: take 10 pages,
    compute the Jaccard between two KNOWN-good outputs of the same page (PDF layer vs L1
    gold) and see where truth sits on the scale.
C12. Capture-ratio vs l1_chars: l1 gold lengths are T2-draft lengths, not truth lengths.
    Is median_capture_vs_l1 systematically biased? Compare against PDF-layer capture on
    the subset with both.
C13. Are we reporting CER (lower better) and capture (higher better) without a combined
    score? A combined "usefulness index" (weighted) would simplify the leaderboard but
    hides tradeoffs. Decide: keep separate (honest) or combine (communicable)?
C14. Runtime as a first-class metric: pages/hour is in the leaderboard. For the hackathon
    story, cost-per-1000-pages per engine (electricity-only for local) is a compelling
    column. Compute from ms/page + a watts estimate?
C15. The hallucination flip decision (D11 INCIDENTS law): same-signature FAIL ≥5 → stop
    spawns. Has it ever fired? Dry-run it on historical HEARTBEAT fails to prove it works.
C16. verify_v2 and deep_verify disagree anywhere? (Two verifiers, two verdicts — cross-diff
    their per-page verdicts; any conflict is a verifier bug or a definition bug.)
C17. NFC: we require NFC everywhere. Some engines emit NFD (canonical decomposition).
    nfc_violations=0 — because outputs are clean or because text_nfc field hides them?
    Check the raw text field, not text_nfc.
C18. What metric will BHASHINI actually score us on? If it's CER on their held-out set,
    our entire internal metric stack should be checked for alignment with theirs — find
    their evaluation definition before Sep 16, not after.

### CATEGORY D — DATA & MANIFEST TRUTH
D1. Domain coverage: the 400 pages are overwhelmingly books/textbooks. BHASHINI's task is
    govt docs + exam scripts. How defensible is a books-only benchmark for a govt-doc
    pitch? What's the minimal govt-doc add-on (25 pages scraped from eGazette/Bhulekh)?
D2. Handwriting coverage: L1 had ~2 handwritten-span labels. Zero handwriting in the
    benchmark. The deck promises handwritten exam scripts. This is the biggest data-pitch
    gap — what's the plan (IIIT-HW crops as a parallel mini-bench)?
D3. Stamps/seals/tables: L2's single-region packs can't represent them. Do any of the 400
    pages even contain tables/stamps? (visual scan of 20 random renders — human task.)
D4. The kn Telugu-dominant cluster (12 pages): keep (mixed-reality honesty), re-tag to a
    "mixed" language, or exclude from kn stats? Decide with reasoning in DECISIONS.log.
D5. mixed_book_page=167/400 flagged. Cross-check: does the PDF-layer script histogram
    AGREE with the L1-derived flag on a sample of 20? Flag drift = mis-stratified scenario tables.
D6. raw_path stability: manifest points into Datasets/. Vinay still holds master copies.
    What's the checksum-verification story if someone claims data drift? (sha1 of the 400
    source PDFs + renders — renders_shared.sha1 exists; source PDFs don't. Add it.)
D7. Page sampling method: how were the 400 chosen from the dumps? Documented anywhere?
    If it was "first N openable," that's a bias to disclose.
D8. Language purity: are there pages in the te set that are entirely English (l1_chars
    from English text)? How many? "Telugu benchmark with 40% Latin pages" must be a
    stated feature, not a surprise.
D9. Data licensing: the source dumps (textbook scans) — do we have redistribution rights?
    For the startup: training on them is one thing; shipping derived datasets is another.
    Flag for Vinay (legal), not for engineers.
D10. Text quality of GT: textbook pages are clean printed text — the easiest OCR regime.
    Where in the 400 are the HARD pages (low contrast, skew, bleed-through, old prints)?
    If <5% are hard, the benchmark says nothing about degradation robustness.
D11. Expansion path: next 400 pages — from where, chosen how, with what stratification?
    Write the sampling spec BEFORE the hackathon ends so scaling is mechanical.
D12. Cross-language contamination in out/: engine outputs for a te page that actually
    contains Marathi — the pack is stored under lang=te. Fine for open policy, but
    per-language leaderboards silently pool scripts. Should scenario tables be the
    PRIMARY leaderboard (SCENARIO_BEST exists — is anyone reading it)?
D13. Render pipeline: 200 DPI from PDF — for scanned-source PDFs (image-embedded), what
    is the effective native DPI? Upscaling a 100-DPI scan to 200 DPI adds nothing. Detect
    native DPI per render and record it.
D14. Password/corrupt audit says 0 locked — verify by actually attempting authentication
    on a sample rather than trusting pymupdf flags.
D15. If BHASHINI gives us their eval set (likely scenario), can our pipeline ingest it in
    <1 day? Write the intake adapter spec now (manifest schema → their format).

### CATEGORY E — LEVEL 3: PAID INDIAN APIs (research-grounded; seal is done, L3 prep is legal now)
Facts from research (2026): Sarvam Vision API ₹0.5/page (cut from ₹1.5 in June 2026;
35M+ pages digitized). Sarvam Document AI = doc_ai namespace, digitise()/extract(),
Vision 1.5, 23 languages, 10 pages max per request, 10 req/min all plans. Sarvam Indic
OCR Bench publishes per-language accuracy — Telugu 87.7, Tamil 93.4, Kannada 89.9,
Malayalam 91.6 (Sarvam Vision column). Bhashini APIs are PoC-only per their GitBook —
production use requires contacting Bhashini for paid plans. PaddleOCR-VL-1.6 (Apache-2.0,
0.9B, 100+ languages, OmniDocBench v1.6 96.33%) is free and self-hostable — it straddles
L2/L3: no API cost, but needs a GPU.
E1. L3 engine candidate list, ranked: Sarvam doc_ai, Bhashini OCR (if accessible),
   VisionBodhan, Gnani, + free-but-GPU PaddleOCR-VL-1.6 as "L2.5". What are the other two
   of Vinay's named five (NE-OCR status?)? Verify each exists and has an API today.
E2. Cost math for 400 pages: Sarvam at ₹0.5/page = ₹200 total. At 10 req/min, 400 pages
   = 40 min minimum wall clock. This is CHEAPER than the electricity for paddle's 10.6h
   CPU run. Does the five-liner to Vinay include "L3 costs less than a pizza"?
E3. Bhashini as hackathon organizer: we are their top-5 team. Is there a partner/hackathon
   API tier? Asking costs one email to the organizer — Vinay's job, draft it for him.
E4. Plugin socket readiness (engines/ stubs LOCKED): write the Sarvam adapter skeleton now
   (input: renders_shared PNG; output: L2 pack schema). Adapter exists = L3 starts the
   minute a key arrives.
E5. L3 verification parity: Sarvam outputs must run through the SAME verify_v2/deep_verify
   chain. Any Sarvam-specific parsing (they return structured JSON with layout) needs a
   normalizer to pack schema. Build the normalizer against their docs before we have a key.
E6. L3 metric asymmetry: Sarvam returns layout + reading order; our packs are single-region.
   Comparing CER is fair; comparing capability isn't. Decide the comparison contract now.
E7. Firewall extension: bench data never fine-tuned on — does this cover PAID outputs?
   Write the extension explicitly (paid outputs are also referee-only).
E8. Data residency: govt-doc pages sent to Sarvam's API — any compliance issue for the
   hackathon? (These are public textbook scans, not personal docs — state it in writing.)
E9. Free-credit harvesting: Sarvam signup credit (₹1,000 per reports) covers 200k pages —
   the whole L3 could run on free credits. Who signs up, with which account, and is that
   within ToS? (Legitimate: yes for evaluation; document it.)
E10. Rate-limit reality: 10 req/min → 400 pages ≈ 40 min; but job-based doc_ai may batch.
    Read the actual API shape (jobs vs synchronous) before promising times to Vinay.
E11. Anchor pricing for the deck: our CPU pipeline cost per 1000 pages (paddle: 95.6s/page
    ≈ 26.5 h/1000 pages on this machine) vs Sarvam ₹500/1000 pages. The economic gap IS
    the pitch. Compute both honestly.
E12. Should PaddleOCR-VL-1.6 (free, Apache-2.0) be added as engine #11 on Vinay's own GPU
    resources (he said "we have our own GPUs")? 0.9B model, vLLM, ~45-60 pages/min on L40S
    per published figures — it would dominate every free engine and is the deck's Stage-2
    base model anyway. This is arguably higher-leverage than any paid API.

### CATEGORY F — SEP-16 COMPETITION PACKAGE
F1. What EXACTLY does "initial results by 16" mean — submission format, metrics, eval set?
    Has anyone on the team read the hackathon brief's evaluation section? (If no brief is
    accessible, list assumptions and send Vinay one question TODAY.)
F2. The gap slide's one number: "% of GT volume all free engines miss" — pooled AND
    per-script. Which denominator (PDF layer vs L1)? Publish the computation; David will
    ask for it live.
F3. Showcase 6×6: page selection criteria (book/bad-scan/form/stamp/handwriting/mixed —
    handwriting/stamp pages may not exist in the 400; see D2/D3). What replaces them honestly?
F4. What's our one-sentence story? Candidate: "Every free OCR engine misses X% of real
    South-Indian page text — here's the proof on 400 pages × 10 engines." Test it on
    someone outside the project (Aryan) — if they ask a question we can't answer, that's
    the next work item.
F5. David-call survival kit: 5 numbers, each with a disk path, that survive interrogation.
    Pre-brief them into a single screen (reports/SEP16_ONE_SCREEN.md exists — refresh it
    with the latest same-tick run).
F6. Demo risk: live demo vs screenshots? If live, what's the 60-second script (open
    DASHBOARD → open a pack → open its render → show CER row)? Rehearse it once.
F7. Failure honesty exhibit: the FAILURE_TAXONOMY is a differentiator — most teams hide
    failures. Should the slide LEAD with it? (Red-team this: does leading with failure
    read as weakness to a jury?)
F8. If BHASHINI's eval includes layout or structure, our single-region packs are
    structurally weak there — what's the 48-hour layout-upgrade path (surya/paddle boxes
    → COCO export → 50 pages)?
F9. Team split for the week: Srujan exams 18–22 — what MUST be human-done before 18, and
    what runs unattended (autoloop + nightly verify + research agents)? Write the handover
    note to self.
F10. The five-liner to Vinay (law: counts only) — current draft exists; update with
    final gap number + L3 ₹-figure + PaddleOCR-VL-1.6 GPU option. One message, no essays.
F11. What do we do if we DON'T place in the hackathon? (Vinay said the model gets built
    anyway with own GPUs.) Pre-write the pivot paragraph so a bad result doesn't stall
    the team emotionally.
F12. Competitor scan: what are the other 4 top-5 teams likely showing? 2h of public
    info (GitHub, LinkedIn, prior Bhashini events). Knowing their likely demo changes
    what we emphasize.

### CATEGORY G — STARTUP & DECK WIRING (beyond the hackathon)
G1. Stage-3 corpus legality: our noisy corpus = engine outputs. Engine licenses (Apache/MIT/
    GPL — easyocr is GPL-3? VERIFY) matter for shipping derived training data. License
    audit of all 10 engines, one table.
G2. The moat question: "we benchmarked 10 free engines" is replicable in a weekend. The
    non-replicable parts: L1 gold, the verify stack, the consensus pseudo-GT, the gap
    analysis. Which of these do we double down on?
G3. North-language replication (Krishna's lane): the entire L2 pipeline is language-agnostic
    by design (open policy). Hand Krishna a one-page "how to run this for pa/gu" — does
    anyone owe him that doc? Write it.
G4. Aryan's pipeline + our packs: his ingest-VLM pipeline and our JSON schema — same schema?
    If not, we're building two incompatible ecosystems. Diff them; write the bridge.
G5. The deck's Stage-2 models include Qwen 3.5 VL + PaddleOCR-VL — our L2 just proved
    PaddleOCR-VL-1.6 is the strongest open parser. Does the deck still say 1.6? If the deck
    cites old versions anywhere, it undermines technical credibility. Version-audit the deck.
G6. Synthetic data route (Sangraha/IndicCorp rendering) is in the proposal but untouched.
    What's the 1-week MVP (render 1000 synthetic degraded pages from te/ta/kn/ml corpus
    text, add as engine-stress set)?
G7. GPU utilization: Vinay claims GPU resources. Zero GPU work has happened (all CPU).
    What's the first GPU job worth doing (PaddleOCR-VL-1.6 self-host vs fine-tuning a small
    TrOCR on our packs)? Order them by leverage.
G8. Pricing the product: per-page price must beat Sarvam's ₹0.5 at scale OR win on
    private-deployment. Which axis is Vaultstack on? One paragraph, founder-level.
G9. Publication strategy: the benchmark itself (400×10, open policy, consensus pseudo-GT)
    is a workshop paper (IndicNLP/ICON). Worth 2 days of writing post-hackathon? Decide.
G10. Dataset as product: could the verified packs + consensus labels be sold/shared as an
    Indic OCR eval set? Check demand signals (Bhashini, AI4Bharat gaps) before building.
G11. Team bus factor: everything above lives in Srujan's head + 6 law docs. If Srujan is
    hit by exam-week flu, what stops? The D8 handoff test answers this — run it for real:
    give a fresh agent ONLY the docs, one task, no help.
G12. 22-language roadmap realism: South-4 done, North with Krishna starting. What's the
    honest 90-day language count given one-machine throughput? Model it from measured
    ms/page × pages, not ambition.

### CATEGORY H — PROCESS, AGENTS & OPERATIONS
H1. DECISIONS.log has 17 entries; the interrogation will add ~50 more. Format still
    one-line? Any entry lacking an evidence_path is invalid — audit existing 17.
H2. Prompt-churn law (Path A) stopped label redo theater. Has prompt-churn moved to
    config-churn (endless engine-config fiddling)? Set a rule: a config change needs a
    gate result BEFORE touching the 400.
H3. Research folder hygiene: research/ holds smoke tests, probes, PUBLISHED_BENCHMARKS,
    cost worksheet. Is anything there load-bearing but undocumented? One README per
    subfolder, 10 minutes.
H4. Autoloop during exams 18–22: what happens on a regression alarm with nobody watching?
    Define the safe-default behavior (pause fills, keep verifying, alert via file).
H5. Agent-ops meta: every agent answer that changed disk should say what it changed.
    Is that enforced anywhere, or do we discover drift by accident? (Add a CHANGELOG.jsonl
    convention for agent sessions — 5 lines of code.)
H6. One-writer law (report.py) vs manual edits: grep reports/ for hand-edits weekly.
    Any hand number found = process violation, traceable how?
H7. Nightly diff report: regression alarm exists but does anyone READ the alarm? Define
    the morning 2-minute check ritual (DASHBOARD → alarm section → DECISIONS entry if red).
H8. Experiment ledger: 4-page gates produce scattered files in research/gates/. One
    gates/INDEX.md with verdicts prevents re-running the same gate twice.
H9. Time accounting: where did the last 7 days actually go (fills vs verification vs
    docs vs rework)? HEARTBEAT gives engine time; human time is unlogged. One-line
    end-of-day log = enough for a retro.
H10. Tool sprawl: orchestrator + run_all_engines + continue_all_engines all exist.
    Which is canonical? (HOW_TO_RUN says orchestrator.) Archive the others per D2 law.
H11. Stranger test schedule: monthly, a fresh agent must reproduce the dashboard from docs
    alone. First run: this week, before Saturday.
H12. The law docs themselves: ULTIMATE_HYBRID_CONCERN is now 19 sections. When did it last
    get read end-to-end by someone who isn't its author? Schedule a 30-min self-review —
    contradictions between sections are accumulating risk.
H13. Alert fatigue: disk guard, core guard, spawn guard, regression alarm, D11 incidents —
    five alert systems. On call: nobody. Consolidate to one DASHBOARD alarm box.
H14. Backup reality: renders sha1'd, source PDFs not; out/ not backed up anywhere;
    Drive holds L1 only. What's the one-command backup (tar packs + manifest + reports to
    Drive/zip)? Write scripts/backup_daily.sh and wire to autoloop.
H15. What's the exit criteria for the 7-day loop itself? "Loop forever" burns attention.
    Define done: L3 keys in hand + Sep-16 package delivered + gates/INDEX full + D8 passed.

---

## PART 3 — TEN STRUCTURED DEBATE MOTIONS (assign RED vs BLUE, 20 min each)
1. "The PDF text layer is untrustworthy enough that capture-ratio should be dropped as a metric."
2. "L1 gold (T2-heavy) is a liability, not an asset, for verification."
3. "openbharatocr and the tesseract mirrors should be deleted from the benchmark, not just down-weighted."
4. "Single-region packs make Level 2 scientifically worthless for layout claims."
5. "Consensus pseudo-GT is strong enough to auto-label 100 new pages tonight."
6. "PaddleOCR-VL-1.6 self-hosted beats every paid Indian API for our demo purposes — L3 paid APIs are a distraction."
7. "200 DPI renders invalidate all low-capture conclusions."
8. "The 400-page set is too small and too clean to support any startup claim — we need the hard-page add-on before Sep 16."
9. "CER is the wrong primary metric for Indic OCR; we should switch the leaderboard to akshara error rate now."
10. "The hackathon is already won/lost on data, not models — stop all engine work, spend 48h on govt-doc data collection."
Rules: winner = side with more disk evidence, not better rhetoric. Verdict + best arguments
→ DECISIONS.log + research/debates/.

---

## PART 4 — LEVEL-3 RESEARCH BRIEF (verified facts, cite in deck/messages)
- **Sarvam Vision API**: ₹0.5/page (67% cut announced June 2026; 35M+ pages digitized on platform).
- **Sarvam Document AI** (doc_ai): digitise() + extract() with schema-based fields; Vision 1.5;
  23 languages (22 scheduled + English); tables→HTML/MD/JSON; max 10 pages/request, 200MB,
  10 req/min on all plans. Indic OCR Bench (published): Telugu 87.7 / Tamil 93.4 /
  Kannada 89.9 / Malayalam 91.6 for Sarvam Vision — our South-4 focus maps to their
  published weakest-and-strongest languages.
- **Bhashini APIs**: free tier is PoC-only per official GitBook; production/integrator use
  requires contacting Bhashini for paid plans. As organizer, a partner tier may exist — ask.
- **Free heavyweight**: PaddleOCR-VL-1.6 (Apache-2.0, 0.9B, 109+ languages, OmniDocBench
  v1.6 96.33% overall, seal/stamp/table capable, ~45–60 pages/min on an L40S per published
  figures) — self-hostable on Vinay's GPUs; strongest candidate for engine #11 and the
  deck's Stage-2 component.
- **Cost anchor for pitch**: 400 pages via Sarvam ≈ ₹200 + 40 min. Our paddle CPU run =
  10.6 machine-hours. Both numbers belong in the five-liner.

## PART 5 — TRACK MAPPING (where each category lands)
- A → Track B (verify spec) + DECISIONS.log · B → Track A (extraction) + gates/INDEX
- C → Track B11/B12 (CER_STAGE3B upgrade) + LEADERBOARD v2 · D → Track E + new data spec
- E → research/LEVEL3_* + plugin socket · F → Track E (Sep-16 package) · G → Track G deck wiring · H → D8/D9 laws
