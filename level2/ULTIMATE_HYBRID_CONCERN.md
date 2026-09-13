# ULTIMATE HYBRID CONCERN — vajrAstra South, Level 2 (merged from ALL operator inputs)
# Merged: Grok session 01a08cbf (105 prompts, 9–12 Sep 2026) + opencode continuation 12 Sep 2026.
# Old/duplicated concerns cut; latest preference kept. Nothing operator-meaningful dropped.

## 0. WHO / WHAT
- Operator: Srujan Sai (IITGN) — Vaultstack AI, BHASHINI AksharDrishti hackathon, South track.
- Lead: Vinay Gahlot (data, GitHub, language sheet, Saturday David call). Krishna = North. Aryan = VLM pipeline (DO NOT TOUCH/STEAL). David = advisor (do not wait for him).
- Srujan languages LOCKED: te (Telu), ta (Taml), kn (Knda), ml (Mlym). No other languages, no 22-lang expansion.
- Repo: /Users/srujansai/Desktop/South. GitHub code-only: https://github.com/Srujan0798/vajrAstra (no zips/images/data dumps — Vinay rule).

## 1. LEVEL 1 — DONE, FROZEN
- 400 label packs (100/lang, B0–B4 × 5 model slots) in labeled/{te,ta,kn,ml}/ — L0+L1+L2, mostly T2 distilled_vlm.
- Labeled folder already uploaded to the team Drive. Message to Vinay already sent. DO NOT redo, DO NOT contradict.
- Law: gold = glyphs on page; no invented Indic; no spell-fix; born-digital PDF text layer = free GT; empty+T3 is honest, fabricated text is the worst FAIL.

## 2. LEVEL 2 — CURRENT (free Indian/local OCR engines as benchmarks)
- Same 400 pages (level2/pages_400/ + pages_manifest.json) run through free OCR engines → Level-1-style JSON packs = benchmarks.
- CORE 5: tesseract_indic, openbharatocr, easyocr, paddleocr_indic, indicphotoocr.
- +3 NEW (latest directive: FULL 400-page engines, NOT smoke-only): rapidocr, tesseract_bilingual, + one of {surya | doctr}. Target after core: 400×8 = 3200 packs.
- Success metric: MAX RAW OUTPUT. Useful = dense script text, errors allowed. Useless = empty / 1-line on full page / English essay on Indic page / repeat-loop.
- Useless ⇒ engine/prompt is wrong ⇒ fix ⇒ RE-RUN full 400 for that engine. Keep old run in json_vN/. Never fake counts — always from disk (find/ls).

## 3. SEAL STRUCTURE (disk truth only)
```
level2/
  pages_400/                       # shared 400 page set (INDEX.json + PNGs)
  models/<engine_id>/{PROMPT.md, RUN.md, json/, png/, logs/, metrics.json, quality_20.json}
  reports/LEVEL2_SEAL.md            # with line: LEVEL 3 NOT STARTED; counted N from find
  research/PLUS3_INDIAN_MODELS.md   # +3 notes (now full engines, research file still tracks)
```
- Same page_id set across ALL engines. RUN.md per engine: exact name+version, invoke cmd, paths, n_json/n_png/n_missing, collapse_rate, 5 example page_ids (best/worst/empty/english-leak/table), strengths/weaknesses, rerun history.

## 4. QUALITY LOOP (repeat until sealed)
- Page coverage per engine = ALL 400 (4 langs × 100). Operator confirmed: per-model 100/lang split is correct — the earlier "20 pages only per model" concern is REMOVED.
- 20-page sample check is ONLY a quality gate/audit probe (mixed pages: printed, table, handwriting, stamp, bad scan), never the coverage target.
- FAIL = empty/collapse/English-on-Indic/loop. WEAK = too short/skipped table or handwriting. OK = lots of script text (errors allowed).
- FAIL+WEAK >30% ⇒ bump PROMPT vN+1 (force lang+script, no translate, [UNREAD] not English, keep native digits, max tokens) ⇒ full 400 rerun for that engine only, old json kept.
- OK ≥70% ⇒ accept engine, log leftovers, move on.

## 5. LEVEL 3 — LOCKED OUT
- Paid/top Indian APIs (Sarvam, Bodhan, etc. — keys/logins) = Level 3. DOES NOT START until Level 2 sealed. No paid keys ever in Level 2.

## 6. PARALLEL + AGENTS (operator style)
- Never stack work. Run all engine fills, audits, migrations, research in PARALLEL. Use subagents (max ~7).
- Operator must be able to EXPLAIN everything to the team as if he owns it — every agent answer must include clear "what/why/how" when asked.
- 7-day loop: D0 inventory → D1 audit+patch+rerun → D2 confirm 400 json+png each → D3 +3 → D4 collapse leftovers → D5 second bump if needed → D6 SEAL.md → D7 freeze prompts.

## 7. CLEANUP (recurring concern)
- No unnecessary MD files / clutter. No preview dumps, no regenerable JSON clutter, no __pycache__ in repo root.
- When deleting anything: check content first, merge anything important, THEN delete. Never fast-delete unreviewed.
- Workspace must be navigable by a stranger: every folder's purpose discoverable (RUN.md/README).

## 8. ENGINE STATE (disk at merge time — always re-verify)
- tesseract_indic: 400/400 ✅ (quality gate passed 25% FAIL — accepted)
- openbharatocr: 400/400 ✅ (mirrors tesseract path — honestly documented)
- paddleocr_indic: ~317/400 filling (ta/te/ml gaps) — RUN IN BACKGROUND
- easyocr: ~156/400 filling — RUN IN BACKGROUND
- indicphotoocr: 0/400 — BROKEN (torch.hub trust prompt EOFError + earlier checkpoint download) — FIX
- rapidocr: 400/400 in out/ ✅ but NOT yet migrated to models/ structure — MIGRATE
- tesseract_bilingual: 400/400 in out/ ✅ but NOT migrated — MIGRATE
- surya: 0/400 — BROKEN import (No module named 'surya.ocr' in installed surya version) — FIX or DROP for doctr
- doctr: 0/400 — never run — SET UP + RUN
- Old out/ dirs are the live run target; models/<eng>/json/ is the seal structure — sync/migrate after completion.

## 10. DONE-LINE (seal)
ALL engines (core 5 + agreed +3) have 400 matching page_ids in models/<eng>/json/ + RUN.md + metrics + quality20 recorded + reports/LEVEL2_SEAL.md regenerated from disk with LEVEL 3 NOT STARTED. Until then: parallel fills + quality reruns, max output, no stopping.

## 9. FORBIDDEN (never changes)
- No training/fine-tuning/SimPO/DPO. No Aryan pipeline. No Krishna sample-cutting.
- No paid APIs (Gemini/Claude/GPT/Sarvam/Bhashini keys) in Level 2. No Level 3 start.
- No invented Indic gold. No spell-correction of OCR output (raw is the benchmark).
- No git-add of zips/images/data dumps. No other languages. No new taxonomy.
- Do not contradict messages already sent to Vinay (L1 done, 400 packs, uploaded).

## 11. LEVEL 2 = NO PROMPTS TO ENGINES (operator clarified 12 Sep)
- OCR engines are programs, not AI agents: PNG in → raw text out → script wraps as JSON. No prompting involved.
- The 20 prompt files were for Level 1 AI models ONLY (forcing diverse page picks). In Level 2 they are NOT sent anywhere.
- Prompts remain useful only as instructions to CODING AGENTS (Grok/opencode) to write/update run_engine.py and orchestration.
- Operator's page-coverage preference confirmed: engine × 4 langs × 100 pages = 400 packs/engine; target 10 engines = 4000 packs (simple math).
- Level 2 top-10 target = FREE OPEN-SOURCE Indian-relevant OCR only. Real top-10 paid Indian APIs = Level 3 (after seal).
- Engine lineup (9 live + 1 candidate): tesseract_indic, openbharatocr, easyocr, paddleocr_indic, indicphotoocr, rapidocr, tesseract_bilingual, doctr, surya, + anuvaad_tesseract (bodhan smoke empty).

## 12. CLEANUP / ARCHIVE LAW (operator clarified 12 Sep)
- Completed / Level-1-only / unused artifacts must move to an archive area (arc_level_1/ or level2/_archive/), NEVER silently deleted.
- Before moving: verify content, note what it is, confirm not referenced by active scripts. If unsure — keep, don't move.
- Repo must stay simple, clean, navigable: active work visible; finished work archived with a one-line README.

## 13. EVOLVE THE PROJECT 360° (operator directive 12 Sep)
- Not just fast execution — continuous improvement of: process, scripts, engine calls, logging, clarity, research, statistics.
- Automation target: ONE-PUSH execution — a single orchestrator command (status/monitor/fill/audit/seal) so the pipeline runs itself with minimal manual steps.
- Keep evolving toward "AGI-level agentic" operation: parallel lanes, self-healing runs (restart on stall), disk-truth status dashboards, quality-gate automation.
- Every improvement should make the NEXT benchmark round easier: reuse engine harness for Level 3 (paid APIs) with plug-in engine definitions.
- Think like a top startup: crash the competition — more research, statistics, tactics, diverse improvements each cycle.

## 14. OUTPUT VERIFICATION IS THE MAIN LABOR (operator directive 12 Sep — STRONG)
- Operator demands: verify EVERY output JSON of EVERY engine (10 × 400) against the actual page. Not sampling — all.
- Verification method (this opencode route has NO image vision): cross-check each page's OCR text against (a) PDF text layer (free GT), (b) Level-1 gold labels, (c) cross-engine agreement. Flag mismatches.
- Known trap found (te_024): work/te books are Maharashtra Telugu-medium — many pages are Hindi/Marathi/English. Engines invoked with single-lang models (e.g. tesseract `tel`) output EMPTY on Devanagari pages. Operator confirmed: engines must output whatever glyphs are on the page — NO language restriction was ever intended. page_id lang tag is just an ID label, not a content constraint.
- Fix direction: (1) auto-script detection per page (PDF text layer script histogram) BEFORE OCR; (2) invoke engines with the detected script's models (e.g. tesseract tel+hin+eng stacked, or multi-lang model sets); (3) treat empty-on-visible-text as a FAIL to be re-run, not accepted.
- Goal restated: engines must be tested at 100% CAPACITY (raw output volume), not 100% accuracy. Wrong/empty outputs = wasted training signal for Vaultstack's future model.
- Do verification in PARALLEL with fills/research — never serial. Find 1 problem → assume 1000 like it → fix pattern-wide.

## 15. FINAL STRUCTURE DIRECTIVES (operator, 12 Sep evening)
- Improvement work split into TWO files: IMPROVEMENTS_CURRENT_WORK.md (pipeline/extraction now) vs IMPROVEMENTS_VAJRASTRA_FUTURE.md (product — LATER, do not touch now).
- CURRENT priority: execute ALL current-work improvements — every one that helps today's benchmark extraction, verification, orchestration, reporting. Startup product items are NOT now-work.
- Dataset folder renamed: work/ → Datasets/ (all refs updated). It holds the source PDFs for all future rounds.
- OPEN POLICY locked: engines read ANY script on ANY page (any Indian language + English). No language boundaries anywhere. page_id lang tag = ID label only, never a constraint. Future languages drop in freely.
- Use ONLY real/latest/top named models (validated 12 Sep: tess 5.5.2, paddle 3.7.0, doctr 1.1.0, surya 0.22.1, rapidocr 1.4.4, easyocr 1.7.2, anuvaad official, IPO IIIT-H). Never waste time on fake/old versions.
- ALL PRE-BENCH BASE WORK must complete before product development starts: manifest integrity, script map (done: 167/400 mixed-book pages flagged), engine hardening (timeout/retry/preprocess), orchestrator automation (stall detect/heartbeat/dashboard/auto-loop), verification suite v2 (consensus/loops/CER/schema), reporting pack (CSV/leaderboard/taxonomy/seal), archive cleanup.
- Operator style: work in parallel lanes, keep everything verified from disk, no claims without counts.

## 16. MISSED-LINE AUDIT (re-read all 105 Grok prompts in FULL + this session — 12 Sep night)
- [covered] P80: Vinay WhatsApp exchange — L1 message sent (do not contradict). Vinay asked for 5 random sample images → DONE (arc_level_1/v_samples/ has 5 PNG + captions).
- [covered] P81/P82: L1 explaining MD file with folder/data details → arc_level_1/labeled/README_SOUTH_LABELING.md exists.
- [covered] P85: Drive upload naming — team has "Dataset" folder of 4 langs; we renamed ours Datasets/ to match. Do not re-upload source data.
- [covered] P86: 5-batch model documentation (B0 Copilot-auto, B1 Grok 4.5, B2 Muse Spark 1.3, B3 Nemotron 3 Ultra, B4 Poolside Laguna-S-2.1) → in README_SOUTH_LABELING.md §"How the 100 pages per language were batched".
- [covered] P87: Vinay's named engines {Sarvam Akshar, VisionBodhan AI, AI4Bharat OCR, OpenBharatOCR, IndicPhotoOCR, NE-OCR, Anuvaad OCR} — free/OSS ones used in L2: OpenBharatOCR ✅, IndicPhotoOCR ✅, Anuvaad ✅; Sarvam/Bodhan = paid → Level 3.
- [covered] P92: old outputs were NOT benchmarks — L1 archive (arc_level_1/) holds them; L2 is the fresh start (current work).
- [covered] P95/P96/P100: operator must understand engine invocation (tesseract -l flags, tessdata download) to answer team — explained in session; EXPLAIN_FOR_SRUJAN.txt exists.
- [covered] P99: GitHub link https://github.com/Srujan0798/vajrAstra — code-only rule (never data).
- [covered] P101: per-model md file + PNG organization → seal_gen.py writes RUN.md; models/<eng>/png/ now 400 symlinks → renders_shared (fixed broken _tmp_render links + _bin noise).
- [covered] P103: 7-day loop / parallel / organize-for-stranger / max-raw-output — all encoded in orchestrator + seal_gen.
- [LAW] P103 note: "400 × 5 = 2000 packs, do not write 20000" — counts always from disk.
- [covered] P104/P105: +3 engines in L2 as FULL engines (not smoke), done: rapidocr, tesseract_bilingual, doctr, surya, anuvaad → 10 engines total.
- REMAINING OPEN ITEMS from P101: (a) operator will later place Vaultstack main-strategy docs in Downloads — read when they appear; (b) Level 3 = top-5 paid Indian models with API keys/logins — starts only after seal.

## 17. FINAL MASTER PLAN (Kimi K3, 13 Sep — grounded in deck + sync transcript)
- DEADLINES: BHASHINI initial results ~Sep 16 (Vinay, on tape); David methodology call Saturday (numbers must survive him); Srujan exams 18–22 → heavy-work window closes Sep 17.
- THE DECK REALITY: Vaultstack = 4-trainable-stage company (Stage 0 OpenCV preprocess → 1 DocLayout-YOLO LoRA → 2 parallel SFT TrOCR + Qwen3-VL-8B + PaddleOCR-VL w/ akshara-boundary aux loss → 2b SCST RL on CER → 3 small-LLM SFT noisy→JSON → 3b SimPO/DPO on CER-tagged pairs). L2 repo = THE DATA ENGINE: out/ JSONs = Stage-3 noisy corpus; capture ratios = gap slide; per-page CER vs PDF layer = Stage-3b preference labels; dominant_script/mixed flags = bench stratification; L1 gold = audit layer. No fine-tuning on bench data. Bench vs Sarvam/IndicDLP.
- [LAW] 4-PAGE GATE: no engine change touches 400 pages until it survives 4 (one per language). Saved rapidocr from a wasted rerun.
- [LAW] ONE WRITER ONE TRUTH: level2/report.py is the ONLY report pipeline — DASHBOARD, LEADERBOARD (script-sliced), MATRIX, VERIFY_*.json, SEAL, CER, GAP — one pass, loop-wired. No hand-written numbers in reports/ ever.
- [LAW] Free-tier labeling APIs (Grok/NIM/Gemini, Vinay-sanctioned) are for LABELING only; "no paid keys in L2 benchmark" stands. Keep separated.
- Consensus spec (final): char 5-gram Jaccard ≥0.6, pairwise, ≥6 engines, tesseract-family = 1 vote. Word-token Jaccard kept as secondary.
- Sep-15 deliverables to Vinay: gap slide (one number: % of page text ALL free engines miss, pooled per script), showcase 6×6, failure taxonomy, latency column, five-liner (10/10 · 4000 packs · verified fresh · gap number · L3 budget ask).
- Post-seal: plugin socket built (level2/engines/, 12 registered, Sarvam/Bhashini stubs LOCKED); cost worksheet level2/research/LEVEL3_COST_ESTIMATE.md (all prices TODO-VERIFY at kickoff).
- Docs stay ≤6 living: README, SOUTH_CANON, ULTIMATE_HYBRID_CONCERN, FOLDER_MAP, IMPROVEMENTS_CURRENT_WORK, HOW_TO_RUN. Others fold/archive.
- Nightly verify diff = regression alarm; FAIL cluster ≥5 same signature → auto-open IMPROVEMENTS line.

## 18. ULTIMATE 10/10 BLUEPRINT (13 Sep, final consolidation — supersedes scoring of §17 items already done)
- DONE TONIGHT (verified): easyocr 400 · timeout real · script-sliced leaderboard · family consensus · rapidocr 3.9.2 per-lang + ml honest-empty · openbharat alias · pages_400 fixed · PROMPT.md 10/10 · engine_meta stamps · plugin socket · cost worksheet · git 3 commits · pycache purge · hallucination flip · render_once · seal LEVEL2_SEALED=true.
- REMAINING (Track B verify spec): B7 NFC ✓done · B9 = char 5-GRAM Jaccard ≥0.6 consensus (word-token stays secondary) · B11 CER/WER floor vs PDF-layer → reports/CER_STAGE3B.json = Stage-3b preference pairs · B12 L1-gold edit-distance cross-check · B16 line-count sanity · B21 PNG sha1 checksums pinned at render · B22 nightly regression alarm (>2% → DASHBOARD alarm) · B23 generated_at stamp inside EVERY report · B6 missing=ABSENT explicit.
- Track A remainder: A3 purge _bin variants from renders_shared (400 files) · C5 stamp en_fallback limitation on paddle ml packs · C8 measure preprocess uplift from _bin retry telemetry · C9 one 300-dpi re-render probe on the 31 historically-empty pages (recover or prove blank) · C10 published-Indic-benchmark sanity doc (MLITS etc).
- Track D: D2 docs 11→6 LIVING (README, SOUTH_CANON, ULTIMATE_HYBRID_CONCERN, FOLDER_MAP, IMPROVEMENTS_CURRENT_WORK, HOW_TO_RUN) — fold ENGINES.txt/EXPLAIN_FOR_SRUJAN.txt/LEVEL2_MASTER_BRIEF.txt/PIPELINE_STORY into archive or the six · D9 DECISIONS.log append-only ledger · D8 handoff test = docs alone drive a fresh agent.
- Track E (Sep-15 deliverables): GAP_REPORT.md (ONE number: % of GT volume ALL free engines miss, pooled + per-script) · SHOWCASE 6 pages × 6 engines (book/bad-scan/form/stamp/handwriting/mixed) · failure taxonomy · latency table · best-per-scenario · explain-like-I-own-it one-pager · 5-liner to Vinay.
- Track G deck wiring documented in README: out/ packs = Stage-3 corpus · CER = 3b preference pairs · capture = gap slide · disagreement = Stage-1 layout queue · L1 = audit layer · firewall: no fine-tune on bench data.
- Scoreboard honesty: today 6.8/10 → 10/10 = all Track B + A-remainder + E green before Sep 16; seal-green by Sep 17; exams 18–22 automation runs itself.
