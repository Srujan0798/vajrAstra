# ULTIMATE HYBRID CONCERN — vajrAstra South, Level 2
# FINAL CONSOLIDATED VERSION 14 Sep 2026 — merges ALL operator concerns from day 1 (Grok 105 prompts, 9-12 Sep)
# through opencode sessions 12-14 Sep (interrogation cycles 1-3) + every law, gate verdict, incident, and lesson.
# Supersedes: all prior versions (v1 archived at _archive/ULTIMATE_HYBRID_CONCERN_v2_20260914.md). Nothing dropped.
# RULE: this file is LAW. Conflicts resolve: latest § wins, disk truth wins, archive never deleted.

## PART I — WHO / WHAT / LANE (immutable core)

### 1. PEOPLE & CHANNELS
- Operator: Srujan Sai (IITGN) — Vaultstack AI, BHASHINI AksharDrishti hackathon, South track.
- Vinay Gahlot (lead — data, GitHub, language sheet, Saturday David call): WhatsApp = five lines, counts only.
- David = advisor (methodology receipts; do not wait for him).
- Krishna = North track. Aryan = VLM pipeline. DO NOT TOUCH/STEAL either lane.
- Srujan languages LOCKED: te, ta, kn, ml. No expansion, no 22-lang.
- Repo: /Users/srujansai/Desktop/South. GitHub code-only: https://github.com/Srujan0798/vajrAstra (no zips/images/data dumps — Vinay rule). Counts always from disk (4000 packs, never 20000).

### 2. THE DECK REALITY (Kimi K3 master plan — why this repo exists)
- Vaultstack = 4-trainable-stage company: Stage 0 OpenCV preprocess → 1 DocLayout-YOLO LoRA → 2 parallel SFT TrOCR + Qwen3-VL-8B + PaddleOCR-VL (akshara-boundary aux loss) → 2b SCCT RL on CER → 3 small-LLM SFT noisy→JSON → 3b SimPO/DPO on CER-tagged pairs.
- L2 repo = THE DATA ENGINE: out/ JSONs = Stage-3 noisy corpus; capture ratios = gap slide; per-page CER = Stage-3b preference labels; dominant_script/mixed flags = bench stratification; disagreement pages = Stage-1 layout queue; L1 gold = audit layer. FIREWALL: bench data never fine-tuned on.
- DEADLINES: BHASHINI initial results ~Sep 16 (Vinay, on tape); David call Saturday (numbers must survive him); Srujan exams 18–22 → heavy-work window closes Sep 17.

### 3. LEVELS
- LEVEL 1 — DONE, FROZEN: 400 label packs in labeled/{te,ta,kn,ml}/, uploaded to Drive, message to Vinay sent. DO NOT redo, DO NOT contradict. Gold = glyphs on page; no invented Indic; no spell-fix; born-digital PDF layer = free GT; empty+T3 honest, fabricated = worst FAIL.
- LEVEL 2 — CURRENT: same 400 pages through 10 free/OSS OCR engines → 4000 packs. Engine truth from disk: 10/10 × 400/400, seal G1-G11 machine-green (14 Sep).
- LEVEL 3 — LOCKED OUT: paid Indian APIs (Sarvam, Bhashini/ULCA, Bodhan) do NOT start until L2 sealed and budget approved. No paid keys in L2 ever. Plugin socket ready (level2/engines/, stubs LOCKED); cost worksheet research/LEVEL3_COST_ESTIMATE.md (prices TODO-VERIFY at kickoff).

## PART II — LAWS (absolute, permanent; violating = P0 incident)

### 4. THE 12 STANDING LAWS
L1. Disk truth only — no claims without counts; re-verify any cited number from disk.
L2. ONE WRITER ONE TRUTH — report.py is the ONLY report pipeline; no hand-written numbers under reports/ or models/; patch the WRITER, never the output (learned 3× the hard way: output-patching gets wiped by regen).
L3. 4-page gate law — no engine/config change touches 400 pages until it wins on 4 (one per language). Saved rapidocr from a wasted rerun.
L4. Archive never delete — move to _archive/ with context; check content first; merging beats deleting.
L5. Datasets immutable — archives append-only, reruns versioned (out_archive/<eng>_vN/).
L6. Family = 1 vote — tesseract-family (tesseract_indic, openbharatocr=byte-alias, anuvaad_tesseract, tesseract_bilingual) pools as ONE independent family; "10 engine runs, 9 engines, 7 independent families" (never claim 10 independent).
L7. No training in L2, no paid keys, no Aryan/Krishna lanes, no new languages, no invented GT, no spell-correction of OCR output (raw is the benchmark).
L8. Open policy locked — engines read ANY script on ANY page; lang tag = ID label, never a content constraint.
L9. Tags can be wrong, but 3 engines agreeing can't be hallucinating (consensus law).
L9b. Freshness stamped (generated_at) or it's fiction; seal is a machine state, not a feeling.
L10. Agents NEVER edit shared pipeline files (verify_v2.py, report.py, run_engine.py, seal_gen.py, report_gen.py) — agent work lives in research/gates/ + standalone generators only (contamination incident law, 14 Sep).
L10b. External improvement plans are AUDITED against disk before execution — ~70% of "P0 bugs" in the 14 Sep plan were contamination phantoms or already-done items.
L11. One fact one file — if a fact lives in two files, delete one (consolidate, don't duplicate).
L11b. Group = counts. David = receipts. Vinay = five lines.
L12. D11 incidents: same-signature FAIL ≥5 pages → auto-line in IMPROVEMENTS + stop that engine's spawns until human ack. D12 deadline guard: new scope auto-rejected inside T-4 of a demo.

### 5. THE CONTAMINATION INCIDENT (14 Sep — case law)
- WHAT: stale pre-v2 verify_v2.py/report.py overwrote sealed HEAD post-commit; partial metrics re-run dirtied 10 engines' RUN.md; 4 scaffold .py appeared (1 with syntax error). External audit plans then read the contamination as "P0 bugs."
- WHY IT MATTERS: unverified agent edits to shared files can silently corrupt the seal and then GHOST-write the evidence trail.
- THE FIX: git restore; audit every claim against disk before acting; quarantine uninvited scaffolds (_quarantine/); log incident in DECISIONS.log.
- THE LAW (now L10): agents work in research/gates/ + standalone generators ONLY. Never shared files.

## PART III — HOW THE MACHINE RUNS (interrogation protocol)

### 6. INTERROGATION PROTOCOL V2 (active — research/INTERROGATION_PROTOCOL_V2.md)
- Roles: RED (attacks, cites disk/papers), BLUE (defends, disk evidence only), EXEC (4-page gates → research/gates/ + INDEX.md), SCRIBE (DECISIONS.log append-only).
- Question fission: every answered P0/P1 spawns 1–3 successors (deeper/broader/inverted); lineages tracked; cycles forbidden; depth caps.
- Hybrid human-genius loop: agent-decidable vs human-decidable split; H1–H5 batched to operator ONCE daily (team promises, money, legal, scope bets, exam week); nothing human-decidable proceeds without Srujan.
- Debate engine: stalemates auto-become motions; ≥2 cross-category hybrid questions daily (B×E, D×F, C×G); verdicts must land in DECISIONS.log/gate/new question or FAILED.
- Self-mutation: nightly meta-review; comfort audit — a day with zero conflicts exposed = FAILED day; a week = protocol is being gamed → RED attacks the protocol itself.
- Question bank v1.0 (~150 questions A–H) = canonical question pool; V2 file wins conflicts.

### 7. GATE LEDGER (all closed — one-line verdicts, full docs in research/gates/)
| gate | verdict | one-line truth |
|---|---|---|
| rapidocr v1 Chinese config | WASH | 400/400 zero Indic chars — fixed to per-lang v5 |
| rapidocr 4-page law (post-fix) | PASS | te/ta/kn real script, ml honest-empty (no ml model) |
| 300-dpi empty rescue (10p) | NO-RECOVER | 0/10 — truly contentless/photo pages |
| G-B1 doctr PARSeq | NO | no Indic weights in 1.1.0; mojibake 0/4; fake-fidelity probe documented |
| G-B3 tessdata_best × PSM | LOSS 0/12 | homebrew FAST stays; mal already best-by-md5; PSM6 helps only te_001 |
| G-B2 rapidocr server-rec | NO-SERVER-INDIC | every _rec_server weight is ch_* — disk-proven from default_models.yaml |
| G-B4 paddle server-det | NO-GAIN | full mode byte-identical to shipped 4/4; timeouts were load-transients; light fallback = insurance |
| G-B12 ensemble voting | NO | 0/115 beat best single; union 3.92 = worse than worst single on 115/115 (line-granularity mismatch); agreement = precision marker only (prec 0.60 vs 0.36, 34% coverage); 6/115 pseudo-GT-grade |

## PART IV — WHAT THE BENCH ACTUALLY SAYS (writer basis, 14 Sep)

### 8. HONEST RANKING & METRICS VERDICTS
- Median CER (clean GT basis, n=126 scored pairs): surya 0.430 [CI 0.369-0.500] > anuvaad 0.475 [0.373-0.534] > tess-family 0.493 > IPO 0.655 > paddle 0.707 > rapidocr 0.751 > doctr 0.841 > easyocr 0.884.
- Bootstrap (1000 paired resamples): {surya, anuvaad} TIED leaders (Δ −0.045, CI [−0.086,+0.020]); both SEPARABLY better than IPO (CIs exclude 0). DECK LINE: "tied leaders surya+anuvaad, decisive drop after tier-1."
- AKER (full basis n=83): does NOT reorder top-2 (surya 0.670 < anuvaad 0.741, same order as CER; probe reorder was small-n noise). Deck keeps CER; AKER disclosed as phonetic-fairness check.
- Per-script: surya wins Tamil + Devanagari decisively; te/kn hard for everyone (0.85–0.92); ml small-n (4 pages clean).
- GAP: 7.1% lower bound (177 GT≥200 pages; 63 legacy + 43 broken layers; 106/177 must-OCR). Per-script: Devanagari 5.21% gap. Uncapped 0.2% never quoted.
- Volume truth: coverage_ge6 382/400; consensus word 38 / family 21 / 5-gram 1 (of 400) — engines disagree a lot (that's the training signal).
- GT-quality gate IN WRITER: 55 legacy-mojibake pages + 219 gt_thin auto-nulled (reason flags in CER_STAGE3B.json) — can never contaminate rankings through any regen. doctr #1-by-wins was a mojibake-GT artifact (fell to 8th-9th).
- Training assets: SFT 1760 / DPO 126 / disagreement queue 50 (read nulls automatically).
- Difficulty honesty: our 400-page corpus is old-scan-class 200-dpi renders = surya's own worst olmOCR-bench category (OldScan 41.8% pass-rate vs Base 99.7 — cite-only, EXTERNAL_BENCHMARK_MAP.md); our EASY split is their worst category; never claim comparability with MLITS/IIIT-IndicHW-Word/IndicDLP (different task, curated GT) — TODO-VERIFY until side-by-side run.
- Fission survivors (parked): paddle↔rapidocr AKER 7/8 swap (cosmetic); B12.1 agreement-text triage flag on 6 pseudo-GT pages; B4.1 load-stress threshold (LOW).

### 9. ENGINE DISCLOSURES (auto-written into every RUN.md via seal_gen ENGINE_LIMITATIONS)
- paddle ml: NO ml model in paddle 3.7.0 — all 100 ml pages run en stack (ml ratio 0.0 on disk — coverage hole, not failure).
- surya 0.22.1: no language-hint param (open-script by design); upstream tracked.
- easyocr: combos te+en/ta+en/kn+en + hi+mr+ne+en pairwise-validated (391/400 nonempty).
- doctr 1.1.0: crnn/parseq Latin-only on our pages — mojibake honestly disclosed.
- tesseract: anuvaad homebrew FAST models stay (B3 proved best loses); open stack tel+hin+eng / mal+hin+eng etc.
- Preprocessing truth: binarize-only retry path (NO deskew — docstring lie fixed 14 Sep); -879 avg uplift explained (17/20 pages base>0→bin=0; empties are contentless; research/PREPROCESSING_UPLIFT_WHY.md); do NOT expand preprocessing without a gate proving a contrast-failure cohort exists.

## PART V — STATE, DOCS, DELIVERABLES

### 10. PIPELINE & CODE (one-writer chain)
- verify_v2.py → deep_verify ×10 → report_gen → seal_gen → stamp (report.py orchestrates; all 27 artifacts stamped every tick).
- engines_config.py = single source of truth for ENGINES + ENGINE_VERSIONS (7 duplicate sites consolidated 14 Sep).
- Research generators (idempotent, .venv/bin/python): gap_report_gen / showcase_gen / latency_gen / one_screen_gen / whatsapp_gen / training_assets_gen / metrics_rigor_gen — outputs to reports/, DECISIONS-only log lines.
- Orchestrator: status/monitor/fill/audit/seal/autoloop; stall detect + heartbeat + dashboard; nightly verify diff = regression alarm (>2% → DASHBOARD red).
- Verify spec V1–V23: coverage, true/family/5-gram consensus, hallucination flip + tag correction, schema missing=ABSENT rows, manifest integrity + render_sha1 400/400, NFC, loops, garbage, eng-leak, digits, L1 cross-check, line-count sanity, per-engine telemetry, script-sliced leaderboard, MATRIX.csv.

### 11. SEP-16 PACKAGE (all disk-generated, stamped)
- GAP.md (money slide: 7.1% lower bound + per-script) · SHOWCASE.md (6 scenarios × 6 engines) · LATENCY.md (ms/page + p/h) · SEP16_ONE_SCREEN.md (methodology, one page) · WHATSAPP_SEPT16.md (Vinay 5-liner) · FAILURE_TAXONOMY.md · CER_BY_SCRIPT.md (writer basis + CIs + AKER) · LEADERBOARD_BY_SCRIPT.md.
- Five-liner core: 10/10 engines × 400 pages · 4000 packs verified fresh · free-OSS gap 7.1% (lower bound) · tied leaders surya+anuvaad · next: Level-3 budget approval.

### 12. LIVING DOCS (≤6) + GOVERNANCE
- Six living: README, SOUTH_CANON (history/law-zero pointer), ULTIMATE_HYBRID_CONCERN (this file — L2 operational law), FOLDER_MAP, IMPROVEMENTS_CURRENT_WORK, HOW_TO_RUN. Everything else → _archive/ with headers.
- DECISIONS.log: append-only ledger (~34 entries; every gate/verdict/incident/law).
- Folder law: no clutter, no regenerable JSON, no __pycache__ in repo (purged), stranger-navigable (README/RUN.md everywhere).
- _quarantine/: uninvited scaffolds (level3_readiness, preprocessing_uplift, regression_test .py) — operator keep/kill pending (H-queue).

## PART VI — OPEN CONCERNS (live queue)

### 13. H-QUEUE (Srujan-decidable — nothing proceeds without you)
H1. _quarantine/ scaffolds: keep or kill? (compile-clean, uninvited)
H2. Deck accuracy line confirm: "tied leaders surya+anuvaad (CER 0.43/0.48, statistically tied), tier-1 clear of indicphotoocr by ≥0.18 CER" — OK to send?
H3. Level-3 budget: Sarvam ₹0.5/page est → 400 pages = ₹200 (worksheet LEVEL3_COST_ESTIMATE.md; prices TODO-VERIFY) — approve or defer?
H4. P4 elite items (cascade router, distillation, Triton serving, active-learning UI, CI/CD per-PR CER delta) = post-Sep-16 by design — confirm parking.
H5. Exam week 18–22: machine runs itself (autoloop + regression alarm); only H-queue items wait on you.

### 14. WHAT I (opencode) STILL CONCERN ABOUT — from my side, complete
1. GT ceiling: only 177/400 pages have usable layers; 224 gt_thin + 55 mojibake → CER basis n=126. The accuracy story rests on 31% of the bench. If David asks "how do you know engines are right on the other 69%?", the only answer is cross-engine agreement + L1 gold (107 pages) — both partial. L1-gold expansion is human labor = post-exam or Vinay-side.
2. ml (Malayalam) is the weakest measured script (4 clean pages; paddle hole; 0.29 rapidocr capture): deck must carry small-n caveat or someone will quote it wrong.
3. Latency table asymmetry: tesseract-family 1 timed page (heartbeat thin) — indicative only; a full timing sweep is cheap (paddle 95s/page × 400 = 10h) — worth it only if David asks cost-per-page.
4. Seal G10 runs pre-commit in report.py chain → transient RED; re-run seal after commit always (known sequence quirk, documented).
5. Regression alarm is armed but unproven: no real regression has fired it yet — first fire will be the true test (D11 wiring exists, untested-in-anger).
6. Bootstrap CIs are page-level, not page×engine paired across scripts: a stratified (script × density) bootstrap could still move tier boundaries — parked as question, not a defect.
7. The deck's "10 engines" must always be said with "9 engines, 7 independent families" — one wrong WhatsApp line to Vinay creates a retractable fact.
8. External plans will keep arriving (Nemotron "elite plans" etc.): L10b audit-first is now muscle memory, but every new operator-facing plan should pass through the same disk-audit gate before any command runs.
9. Archive is getting deep (_archive/ now holds 40+ items): worth a one-line-per-item INDEX before Sep-16 so strangers can navigate it (cheap, 10 min).
10. Question bank v1.0 (~150 questions) has categories E-H (product/deck/level-3) that interrogation hasn't touched yet — they're the next fission frontier post-Sep-16; don't let them rot unasked.
11. My own failure modes this session: (a) output-patching instead of writer-fixing (3×, now law), (b) panicking at dirty RUN.md that was legit rotation, (c) two empty subagent returns before switching to inline execution — if a subagent returns empty twice, run the gate yourself, inline.
12. The concern file itself: if it grows past ~200 lines again, consolidate (this merge) rather than append — FOLDER_MAP + DECISIONS.log carry the details; this file carries the LAW.

### 15. NEXT ACTIONS (machine continues)
1. CER_BY_SCRIPT regen is done (writer basis); bootstrap verdicts sealed into deck line.
2. SEPT16 package refreshed; five-liner mirrors seal state.
3. Evening summaries daily: conflicts exposed / questions born/killed / gates run / H-queue / comfort audit / DECISIONS delta.
4. Post-seal + post-Sep-16: Level-3 kickoff (Sarvam first, ₹200 estimate), P4 elite items, E-H question categories, L1-gold expansion, archive INDEX, stratified bootstrap.

## PART VII — VERBATIM OPERATOR CONCERNS (never to be lost, mixed into the above)
- "Max raw output" = the L2 success metric; useful = dense script text (errors allowed), useless = empty/1-line/English-on-Indic/loop.
- "Useless ⇒ engine is wrong ⇒ fix ⇒ re-run full 400; keep old in json_vN; never fake counts."
- "No hand-written reports; one writer; freshness or fiction."
- "7-day loop; parallel lanes; max ~7 subagents; never stack work."
- "Operator must be able to explain everything as if he owns it — what/why/how on demand."
- "Work like a top startup — crash the competition: more research, statistics, tactics each cycle; AGI-level agentic operation; one-push execution."
- "Verify EVERY output of EVERY engine against the page — not sampling; cross-check PDF layer + L1 gold + engine agreement; find 1 problem → assume 1000 like it → fix pattern-wide."
- "400 × 10 = 4000 packs. Don't write 20000. Counts from disk."
- "If a fact lives in two files, delete one."
- "Your testicles are safe. The system is elite." (Boss-agent verdict, 13 Sep — morale law, kept verbatim.)
