# A7-JURY — Jury-criteria audit and exact pitch package (READ-ONLY audit of /home/user/boss)

Scope note: RULES.md asks ~1,500 words; this task also demands a full pitch package, so it runs longer. Paths are repo-relative to /home/user/boss. CLAIMED = someone wrote it; VERIFIED = file/output exists in the snapshot. The snapshot has text only: no weights, no data, no images.

## 0. Headline findings
- The six criteria are verbatim at docs/campaign/checkpoints/W4_reports/RQ1_official_rules.md:36-42. Two further facts matter. Only two dates are published: launch 12/02/2026 and pitch screening 23/07/2026 (RQ1:114-128). No metric, weights, test set or submission format is published (RQ1:30, 82, 237-292).
- Of the six criteria, only the Approach criterion has a real artifact. Business case, roadmap, team and market exist only as narrative bullets or as a four-line stub (proto-108 §5, lines 255-263).
- No deck exists. The only deck is the Aug-2026 4-slide Vaultstack PPT, which lives on the Mac at /Users/srujansai/Desktop/South/ and is not in the repo (docs/architecture/PPT_SPEC.md:3). Plan v4 changed the architecture since then.
- No cost/TCO sheet, no 4-year costing, no IPR/NOC document and no market sizing exist anywhere. Verified by find/grep: there are no files named *tco*, *costing*, *ipr*, *pitch* or *deck*. The only IPR/NOC mentions are rule restatements in c2/LEDGER A06, R115, R116 and the "company gets no IPR" line.
- Any Vaultstack product package, CLI or Docker image is CLAIMED only. artifact_showcase.md:128 says "product/ in the repo", but product/ holds a single file, product/docs/B21_SYNTHETIC_LINES_SPEC.md. There is no Dockerfile, pyproject or CLI anywhere (find returned nothing). A "50-image timed dry run" is likewise only a planned gate (proto-108:517-523, G-SHIP).
- The measured handwriting expert does not exist yet. All "92-96%" figures are third-party ICDAR 2023 numbers (artifact_showcase.md:13-14). Our own Bengali handwriting WRR is unmeasured, and the plan is gated on Vinay's OK (artifact_showcase.md:145-147).

## 1. Per-criterion audit

### C1. Approach / innovation
- **Artifacts:**
  - docs/campaign/handoff_2026-10-01_v4_integration/artifact_showcase.md §5-6 (two-expert router).
  - docs/campaign/protocols/proto-108-plan-v4-final.md §2-5.
  - docs/campaign/COMPETITOR_INTEL.md §2 (the comparability table) and §4 (what competitors overlooked).
  - docs/architecture/PPT_SPEC.md (original pipeline).
- **Quality (strong):**
  - The thesis is evidence-based. The official test set is handwritten Bengali words (DISPATCH_LOG.md:583, 13/13 viewed). Vendor handwriting scores are low: Bengali Sarvam 58.3, Bodhan 71.3, Gemini 74.8 (showcase:41-43). The ICDAR specialist best is 96.10 (showcase:100-110).
  - The honesty layer is a real differentiator: CIs, abstention, GT tiers, "never compare across benches" (COMPETITOR_INTEL:62-80).
- **Gaps:**
  - The showcase says "16/16 viewed" (artifact_showcase.md:7) but DISPATCH_LOG.md:583 says 13/13, and TEST_SET_PROFILE.md:47 says 3. Reconcile to a single counted number before pitching.
  - No "simplicity" story. The jury lists simplicity explicitly (RQ1:37), and the 7-stage router plus experts looks complex.
  - The showcase omits the novelty claim "benchmark leakage / hash-gate / independent-writer eval", which exists only in plan text.

### C2. Business use case
- **Artifacts:**
  - c2/LEDGER A04 and R126 (heritage/governance framing).
  - proto-108:258 (lead with governance/archive handwriting).
  - showcase §7 (two bullets).
- **Quality (thin):**
  - The framing is sourced: the launch call names Sanskrit manuscripts, Tamil records, Gujarati archives and so on (LEDGER:10, 298).
  - There is no named customer, no workflow, no pain quantification, no USP statement, no vision statement. The criterion asks for "Business Case, USP and Vision" (RQ1:38).
- **Missing:**
  - A one-page business case with a concrete document class: exam answer scripts, forms, land records.
  - A USP line: offline, ₹0 per page, handwriting-first, honest evaluation.
  - A vision line.

### C3. Technical feasibility
- **Artifacts:**
  - proto-108 §2-6 (gates, kill table).
  - BODHAN_BASELINE.md. The measured figures live in the planner notes: Bodhan reproduces ≈86.4 vs 84.94 published; CER 0.4034 vs surya 0.5660 on 300 gold pairs; 0.69 CER on sample-100 pages (v4_notes.md:20-21). The 24.3 s/page surya and 0.40 s/page rapidocr latencies come from BOSS_EXPLAINER.md:14.
  - Showcase §5, §8 (risks).
  - docs/legal/LICENSE_AUDIT.md.
- **Quality:**
  - Measurement discipline is good.
  - But no shipped system exists: no router code, no handwriting expert, no JSON/PDF writer demonstrably produced in this snapshot.
  - Bodhan's own page-level CER of 0.69 is unexplained (showcase:177).
  - Bodhan inference on a CUDA box has not run: the 24 GB SSH GPU is still pending (VINAY_CALL_AND_GPU_DAY1.md:28, proto-108:352 "O-3").
- **Missing for the jury:**
  - A working end-to-end demo with timing.
  - Interoperability evidence: the Udyat/dhruva-api serviceIds (c2/LEDGER P103, R120, R121) are cited but no adapter exists.
  - A components-and-licence table (see section 5).

### C4. Product roadmap
- **Artifacts:** two bullet lists (showcase §7 "Roadmap"; proto-108:257).
- **Quality (thin):**
  - No dated milestones. Bhashini's own funnel is Screening → Prototype → Product (LEDGER A07, A09; cadence ≈6 weeks, R119). It is not mapped.
  - Cost to build, go-to-market and time to market are all unquantified.
- **Missing:**
  - A 4-quarter roadmap tied to Bhashini stages.
  - A GTM channel plan.
  - A build-cost number.

### C5. Team ability and culture
- **Artifacts:**
  - PPT_SPEC.md:5 (team: Vinay Gahlot CEO, Akshay Gahlot CTO, David Babu advisor).
  - VINAY_MEETING_PACKET.md:46 (Vinay Gahlot, IIM-A).
  - OCR_AGENT_MEMORY_FEED.md:1187 (Srujan Sai, IITGN, operator).
  - proto-108:259 ("solo operator plus agent workforce with audit trail").
- **Quality:** an inconsistent story. The deck lists three named people; the plan says solo operator; the showcase says "one lead plus three AI agents" (showcase:34). There are no bios and no track record. The only proof is the audit trail (DISPATCH_LOG.md, W4.md). The team memory also holds "no team mates" and "boss assigns" rules.
- **Missing:** a single, true team slide: named humans and roles, relevant credentials, how AI agents are governed, and who presents ("Team Leader's... ability to present", RQ1:41).

### C6. Addressable market (channel, deployment cost, customisation cost per person per month, 4-year resource rate)
- **Artifacts:** only cost anchors in proto-108:260-262 and c2/LEDGER C30, D35, P104, R123, Q106. There is no market sizing at all (grep for TAM/market-size found none).
- **Quality (weakest criterion):**
  - The jury asks for four specific figures (RQ1:42). None is computed.
  - proto-108:262 lists "IPR, O&M" but leaves them unwritten.
- **Missing:** the whole cost sheet (section 3), the 4-year table (section 4) and a bottom-up market estimate.

## 2. Exact deck outline (10 slides + 2 backup; 10-minute slot assumed, source c2/LEDGER A10 which is INFERENCE only, so confirm with gic.dibd@gmail.com, RQ1:313-317)
1. **Title and one-line promise.** "Offline handwriting-first Indic document OCR, ₹0/page." Team name and logo. Source: showcase §1.
2. **The problem (governance/archive).** Handwritten and degraded records in Indian languages; the official problem statement text (RQ1:245). Quote the launch-call document classes (LEDGER A04). Needed: one real, de-identified sample image.
3. **What the test actually is.** 5,344 single handwritten Bengali words (TEST_SET_PROFILE.md:11; DISPATCH_LOG.md:583). Fix the 3/13/16 viewed-count discrepancy first.
4. **Evidence the field is weak here.** One chart, Bodhan HW bench, labelled "vendor-built, directional" (showcase:41-43). Next to it the ICDAR specialist results (showcase:100-110), labelled third-party. Never mix benches (COMPETITOR_INTEL.md:62).
5. **Our approach: two experts under one router.** The showcase §5 diagram. Slide note: "kept the original PPT stages, upgraded two" (showcase:119-121). Simplicity framing: the router is one decision, crop vs page.
6. **Proof (the only slide that needs fresh numbers).** WRR/CRR with 95% CI on an independent-writer set, ours vs Bodhan vs Sarvam vs Tesseract. Pre-registered targets are ≥92% IIIT val and ≥85% independent (showcase:130). If the run is not done, show the leak-control process and say "measured on X date", never a placeholder number.
7. **Live demo.** See section 6.
8. **Technical feasibility and stack.** Component table (name, licence, size, role), latency per page, CPU/GPU requirements, interoperability with Bhashini Udyat/dhruva-api serviceIds (LEDGER R120, R121), JSON/PDF/MD outputs (RQ1:85-90).
9. **Business, market and cost.** Customer, channel, pricing, 4-year TCO against Sarvam ₹0.5/page and Bodhan ₹0.20/image (LEDGER C30, D35). See sections 3-4.
10. **Roadmap, team, ask.** Quarters mapped to Bhashini's Screening → Prototype → Product funnel (LEDGER A07). Team with names and credentials. Ask: GPU, stage dates, submission format (showcase:145-151).
- **Backup A:** risk and licence slide (sections 5 and 7).
- **Backup B:** "What we did not claim": no beat-87.39 claim; no cross-bench head-to-head; no "10/18" (proto-108:269-276).

## 3. Cost / TCO sheet: required fields and sourced values
Use the official columns (RQ1:42): Channel · Deployment Cost · Customisation and Enhancement Cost per person per month · Resource Rate for 4 years.

Fields to build, with the value and its source or "NEEDS BOSS INPUT". Do not invent any number.
- **Per-page compute, ours (offline):** ₹0 licence fee. Needs a measured s/page and hardware amortisation. Measured now: surya 24.3 s/page, rapidocr 0.40 s/page (BOSS_EXPLAINER.md:14); the Bodhan and PARSeq latency is UNMEASURED.
- **Comparison per page:**
  - Sarvam ₹0.5/page, 5,344 pages ≈ ₹2,672 (c2/LEDGER C30).
  - Bodhan API ₹0.20/image (LEDGER D35; PRIMARY in COMPETITOR_INTEL.md:23).
  - Mistral $2/1,000 (cited at proto-108:262; underlying a/LEDGER not opened here).
  - Krutrim is token-priced (₹83.6 per 1M input tokens, ₹34.53 per 1M output; LEDGER G54), so convert before citing.
- **GPU training and dev cost:** RTX 4090 spot ≈ $0.13-0.14/hr (Vast), Runpod ≈ $0.34/hr; a 30 h LoRA ≈ $5-15; total budget ask $15-30 (c2/LEDGER Q106; R6 §9). Caveat: the current plan uses the boss's 24 GB SSH box, so the effective cost is probably ₹0 (VINAY_CALL_AND_GPU_DAY1.md:45).
- **Hosting/API tier:** Bhashini PoC APIs are free, production/charging needs the paid version (LEDGER R122). bhashini.ai tiers: Individual ₹250/mo, Creator ₹2,500, Professional ₹7,500, Scale ₹35K, Enterprise ₹1L per month (LEDGER P104, R123).
- **O&M benchmark from analogous contracts:**
  - Bhashini Challenge 2023: ₹10L/year O&M, 1-year deployment + 4-year support (LEDGER B19).
  - LEAP: winner ₹10L plus 4-year deployment contract plus ₹10L innovation/O&M (LEDGER B18, R118).
  - AksharDrishti's purse is UNKNOWN (RQ1:467). Never present an analogy as the AksharDrishti purse.
- **Resource rate (people):** NO source in the repo. NEEDS BOSS INPUT: monthly cost per engineer, annotator, DevOps and support person. "Per Person Per Month" is the unit the jury asks for.
- **Customisation per language/script:** NEEDS BOSS INPUT (person-months per new script). Anchor effort: ~30 GPU-hour class LoRA (LEDGER L82) plus annotation.
- **Licence cost lines:** Bodhan IOML has an "ask before hosting for others" clause plus 500M MAU/$250M revenue thresholds (COMPETITOR_INTEL.md:23; proto-108:126). Cost = ₹0 only as an internal component. A hosted Bodhan endpoint needs written approval. surya must not ship (LICENSE_AUDIT.md; proto-108:269).

## 4. 4-year costing structure (build as a sheet; fill from section 3)
- **Rows (per year Y0-Y3 or Y1-Y4):**
  - Engineering (FTE-months × rate).
  - Annotation/HITL (words × rate).
  - Compute (training + inference).
  - Hosting/support (Bhashini tier or own).
  - Licence/legal (DPIIT, IPR filing, Bodhan permission).
  - Customisation per added script.
  - Maintenance/O&M.
- **Scenarios:**
  - (a) offline/on-prem for a government office;
  - (b) Bhashini API-hosted;
  - (c) competitor-API baseline (Sarvam ₹0.5/page × volume; Bodhan ₹0.20/image × volume).
- **Break-even:** page volume at which the 4-year own cost undercuts Sarvam/Bodhan. This needs a customer volume assumption, flagged NEEDS BOSS INPUT.
- **Rule:** every cell carries a source tag (PRIMARY/DERIVED/ASSUMPTION), per the repo's own evidence law (proto-108 §6).

## 5. IPR and licences (what we can actually state)
- **Hackathon IPR terms (2023 challenge; AksharDrishti publishes none, RQ1:228):**
  - New IPR belongs to the final winner/organisation with government public-interest usage terms (c2/LEDGER R115).
  - Employer NOC must state the company has no right on prize money/IPR (R116, A06).
  - Do not cite as AksharDrishti rules (RQ1:228-230).
- **Registration:** Indian company or DPIIT startup needed; unregistered teams must register if selected for the final (A06). Vaultstack's registration status is NOT in the repo. DPIIT definition (≤10 yrs, ≤₹200 Cr turnover) is at LEDGER R114.
- **Component licences (stated in the repo):**
  - Bodhan: Indic Open Model License v1.0, attribution, internal component, hosting needs written approval, outputs used for training become Derivatives (proto-108:126, 310). The licence reading itself is marked OPEN (proto-108:337).
  - PARSeq code Apache-2.0, IndicPhotoOCR repo MIT; **weights licence unverified** (v4_notes.md:44, LICENSE_AUDIT.md TODO-VERIFY 6). The showcase's "licences are clean for a product" (showcase:162-168) overstates this.
  - IIIT-INDIC-HW-WORDS CC BY 4.0, train OK (v4_notes.md). IHTR 2022/2023 sets are eval-only (v4_notes.md:45).
  - Tesseract/tessdata Apache-2.0 expected, one verify outstanding. surya weights evaluation-only, never ship.
- **Missing:** a one-page IPR statement covering what Vaultstack owns (router, fine-tuned heads, post-corrector, tooling), what it licenses in (above), and the NOC for each person.

## 6. Demo script (5 minutes; source proto-108:519-523; every step must be rehearsed offline)
1. 0:00 Show a phone photo of a handwritten Bengali form (a real sample, de-identified).
2. 0:30 Run the CLI or UI with network off. Show the router's output: handwritten/printed, script, language per block.
3. 1:30 Show the layout-preserving JSON, the searchable PDF (select and copy text) and Markdown.
4. 2:30 Show confidence flags: low-confidence spans go to human review.
5. 3:15 Show the evaluation table: ours vs Bodhan vs Sarvam on the independent set, with CIs and abstention. If the number is not measured, drop the slide, do not substitute.
6. 4:15 Show cost: ₹0 per page against ₹0.5 and ₹0.20 (LEDGER C30, D35).
7. 4:45 Failure case, shown deliberately (full-page Bodhan CER 0.69 must be explained first).
- **Pre-flight (all UNPROVEN now):** a pinned environment, a CPU-only path, fallback screenshots, a pre-recorded video, and a timed 50-image dry run (proto-108 G-SHIP).

## 7. Risks (for the deck and the Q&A)
- **Rules unknown:** metric, deadline, format, test set, prize all unpublished (RQ1:30, 82, 467). Action: email gic.dibd@gmail.com (RQ1:313-317).
- **Overstated product:** the showcase asserts a built product and clean licences (showcase:128, 162). A jury demo will expose that. Fix the wording until code exists.
- **No measured number for our handwriting model.** This is the whole thesis. Pre-registered kill: independent writers <85% means no claim (proto-108 §6-7).
- **Leakage:** official test hashed against IIIT-HW sets before training (K-HW0). Bodo/gu labels are a separate set; sha256 overlap with the official test was 0 (HANDOFF.md §2).
- **Stale defect:** DRAFT_RESEARCH_PLAN.md:18 still states the withdrawn student-repo metric as the official rubric (RQ1:410). Fix before any share.
- **Licence:** Bodhan hosting restriction vs a product pitch; surya blocked; PARSeq weights unverified.
- **Vendor-bench weakness:** all vendor benches are self-built; any claim must be labelled directional (COMPETITOR_INTEL.md:62-80).
- **Team story inconsistent** (section C5).
- **Process risk:** two editors writing the repo, and the boss's complaint that Plan v4 and the showcase read as "false words" (HANDOFF.md §1).

## 8. Concrete next actions
1. Reconcile viewed-count (3/13/16) by viewing and logging N test images in DISPATCH_LOG.md; fix artifact_showcase.md:7. Done-when: one number across all docs.
2. Rewrite artifact_showcase.md:128 and :162-168 so product and licence claims match disk. Done-when: every claim has a path that exists.
3. Draft docs/campaign/pitch/DECK_OUTLINE.md from section 2 and docs/campaign/pitch/COST_4Y.csv from sections 3-4, each cell source-tagged. Done-when: no cell without a tag.
4. Obtain the people-rate, volume and registration inputs from the boss (listed NEEDS BOSS INPUT). Done-when: all blanks filled or struck.
5. Write docs/campaign/pitch/IPR_NOC.md (section 5). Done-when: DPIIT status and NOC status stated.
6. Email gic.dibd@gmail.com for the metric, format and dates, and view the prize and stage images by eye (RQ1:454-476). Done-when: replies logged.
7. Fix DRAFT_RESEARCH_PLAN.md:18 per RQ1:418.
8. Build the demo path and run the 50-image dry run. Done-when: JSON/PDF valid, s/page and memory logged in W4.md.
9. Run the proof table (E1) and put the one real WRR/CRR slide in the deck; if gates fail, ship the zero-shot with honest labelling.
10. Build the market-size slide bottom-up (document volumes by agency) from sourced Bhashini/government data. There is none in the repo today, so this needs new research.
