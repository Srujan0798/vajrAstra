# LEVEL 7 — 48-Hour Continuous Multi-Agent Research Campaign

Locked 2026-09-26 (evening). This is the tier above everything done so far.
What exists on disk today is 100% gold — never redo, never re-litigate. Level 7
is the next 10X: a research base so dense that no individual or team could
reconstruct it in under a decade. A single agent doing this work would need
~2 months; we compress it into 48 hours via 3 agents × parallel subagents.

---

## 1. THREE-AGENT PARALLEL OPERATIONS MODEL (always-on, simultaneous)

| Agent | Owns | Never does |
|---|---|---|
| **Engine Agent** | the main build work: probe22 engines end-to-end (indicphotoocr → surya → easyocr → paddleocr_indic), retry passes, EN sanity columns, Phase 6 scoring, final report + leaderboard; Lane A research | research writing outside `docs/research/level7/a/`; parallel heavy engines |
| **Verdict Agent** | verification of everything: §6.4 GT verification, hostile audits, lane verification, rankings, verdict ledger. **Specifies improvement fixes** (exact file, exact change, evidence id) — applies them only to its OWN artifacts (gt_verification.json, verify_visual.py, verdict ledger); shared docs get a fix spec for Miss | re-litigating reconciled audits (§10 of AGENT_PROTOCOL.md is closed); applying fixes it specified to shared docs |
| **Miss Agent** (equal tier) | **applies every fix Verdict specifies** (shared docs, tooling, artifacts); Lane C research; monitoring both agents' output health; data-collection strategy for remaining languages; tooling/logging; validation-call coordination | running heavy engines; touching `level2/out/` or `level2/reports/`; editing files Engine is actively writing |

**Fix-loop law (locked 2026-09-27):** FIND (Verdict) → SPEC (Verdict writes exact fix: file, change, evidence) → FIX (Miss applies) → RE-VERIFY (Verdict checks). Max 2 rounds per issue, then escalate to the user. The orchestrator (main session) plans, pre-researches, writes agent prompts, monitors, manages — it does not apply fixes itself.

All three run simultaneously. Each may spawn subagents (research lanes run as
parallel subagent task forces; engines stay sequential on the main process).
Every agent re-reads `level2/probe22/AGENT_PROTOCOL.md` + this file before
starting, and re-checks disk state before every report.

## 2. LANES (parallel; each lane = one subagent task force)

### LANE A — OCR / Document-AI SOTA (Engine Agent's subagents)
- A1 Current-generation OCR models (2025–2026 only): PaddleOCR-VL 1.6, Qwen-VL,
  Sarvam Vision 2.1, GOT-OCR2.5, olmOCR2, dots.ocr, DeepSeek-OCR, Granite-Docling,
  Nougat, Gemini/GPT vision OCR. Per model: architecture, training data scale,
  Indic CER/WER where published, inference cost, license, fine-tune openness.
- A2 Indic-script-specific problems: Nastaliq segmentation (Kashmiri/Urdu),
  Ol Chiki (Santali), Meitei Mayek, PDF-layer GT corruption (legacy fonts,
  control chars, ZWJ/ZWNJ), code-mixed text, akshara-level modeling for abugidas.
- A3 Degraded-document restoration: binarization, deshadow, dewarping, text
  super-resolution, synthetic degradation pipelines (OldScan cell 55.3).
- A4 Benchmarks & metrics: CER/WER/akshara metrics, AksharDrishti eval protocol,
  Indic handwriting datasets, ranking models over benchmarks.

### LANE B — Agentic-AI-era methods (Verdict Agent's subagents)
- B1 RLVR: RL with verifiable rewards for OCR/document models — GRPO/PPO recipes,
  reward shaping on CER, reward-hacking guards, synthetic gold generation.
- B2 Self-improving agent systems: Hermes-style self-improvement loops, memory
  (instincts/skills), continuous verification, regression gates.
- B3 Multi-agent orchestration: parallel subagent patterns, eval-first execution,
  loop design checks, adversarial review (santa-method), quality gates.
- B4 Agent tooling landscape: Claude Code, Kimi, OpenCode/ECC, LAYA gates,
  Obsidian/knowledge-graph workflows, TypeScript AI SDKs, MCP servers.
- B5 Elite harness & productivity repos (the "elite builder" stack, verified
  current 2026-09-27): affaan-m/ECC (agent harness performance system —
  ALREADY INSTALLED on this laptop at ~/.config/opencode/, full profile since
  2026-09-21; study its own patterns AND use its skills), Graphify-Labs/graphify
  (codebase→knowledge graph, tree-sitter AST, embedded MCP — INSTALLED at
  ~/.local/bin/graphify; use /graphify query on probe22 instead of grepping),
  anthropics/claude-code ralph-wiggum plugin (Geoffrey Huntley's continuous
  agent loop — the technique behind our own loop-design-check discipline),
  claude-mem (persistent cross-session context), rtk-ai/rtk (token-reduction
  proxy), ponytail (minimal-code philosophy), ComposioHQ/awesome-claude-skills,
  NousResearch/hermes-agent, deepseek-ai/deepseek-harness, browser-use.
  For each: what elite operators run, the measurable gain claimed, what we
  adopt vs reject for an 18-language OCR build under hackathon constraints.

### LANE C — Infrastructure & competition (Miss Agent's subagents)
- C1 NVIDIA stack: TensorRT-LLM, NIM, NeMo, quantization (FP8/FP4), edge/Jetson
  deployment, serving costs for OCR models.
- C2 Competition intel refresh (extends R6): rules, evaluation, prizes, competitor
  scan — VERIFIED vs INFERENCE discipline mandatory.
- C3 Data collection for remaining languages: quality-first strategy (the law:
  NO 400-page sets), licensing, GT-quality gates learned from the purge.
- C4 Tooling & logging: research ledger format, verification verdicts, rankings.

## 3. DENSITY TARGETS (how dense)

- **1,000+ live research papers** (2025–2026 agentic-AI era only — no dummy
  listicles, no stale surveys), plus **5,000+ total artifacts** counting case
  studies, method PDFs, concept notes, repos, benchmark cards.
- Per lane minimum: A ≥ 400, B ≥ 400, C ≥ 400 artifacts, spread across sublanes.
- Every artifact record (mandatory fields, no exceptions):
  `source_url | date | status | relevance(1-5) | recency(1-5) |
  actionability(1-5) | 3–10 line extraction: mechanism → result → how it maps
  to our 18-language goal or weak cells`.
  Status is exactly one of: `PRIMARY` (opened the source and copied the span),
  `MEASURED` (computed from disk with command + n), `DERIVED` (arithmetic
  from PRIMARY/MEASURED, formula shown), `CONTRADICTION` (two primaries
  disagree; both quotes stored; no winner picked), `UNKNOWN` (required for a
  decision, not established — a successful output, not a hole), `REJECTED`
  (secondary source failed primary check), `DEAD` (true but cannot change
  any decision — record and cut). Unlabeled numbers are forbidden. Every
  record ends with: **decision it can change** (which W6/architecture choice
  this row moves). A record that names no decision is DEAD by definition.
- Weak cells steer ranking: Santali 53.91, Kashmiri 54.82, OldScan 55.3,
  Odia 80.01. Score = relevance × recency × actionability; only ≥ 30/125 enters
  the integrated architecture.
- Output location: `docs/research/level7/` (lane subdirs a/, b/, c/) — this is
  the ONLY sanctioned location. Never repo root, never `level2/research/`.

## 4. VERIFICATION (Verdict Agent)

- Sample-check 10% of every lane's records against the live source.
- Rank all artifacts; produce the verdict ledger (`level7/verdicts.json`-style,
  same evidence rules as the probe audits — disk-verified or it did not happen).
- Flag contradictions with W1, R1–R7 docs; contradictions are first-class
  artifacts: store both quotes, never pick a winner silently, resolve only in
  the integration pass with an explicit note.
- Daily hostile pass (each campaign day): (1) unlabeled claims added today
  must be zero; (2) seed/inherited rows promoted or rejected; (3) name the
  single fact today that most changes the architecture, and one that does not.
  Prefer a sharp UNKNOWN over a soft guess — a guess becomes a landmine in the
  integration pass; an UNKNOWN becomes a post-call experiment.

## 9. EVIDENCE-LAW UPGRADES (adopted 2026-09-27 from PROTOCOL_1_RESEARCH.md,
## the Gemma-4 competition protocol — transferred only what changes our decisions)

1. **Transfer cards.** Every paper/method record in Lanes A/B/C carries a
   transfer verdict: `SURVIVES` / `DIES` / `UNKNOWN` against OUR harness
   facts — 18 Indic languages, weak cells (Santali/Kashmiri/OldScan/Odia),
   200-dpi citizen documents, no paid keys, no training until W6 freeze,
   offline-capable pipeline. The harness fact that kills or saves it is named.
   A method needing what we don't have (weights, GPUs, hidden tests) is DIES
   or UNKNOWN — never "inspiration".
2. **Transfer obituaries.** Any external number we are tempted to cite
   (Sarvam 87.39, OmniDocBench/HuggingFace leaderboard cells, vendor blog CERs)
   gets an obituary: why it does NOT transfer (different languages, scan
   quality, harness, metrics). The number is DEAD for decisions unless its
   obituary fails. This formalizes what we already do with 87.39.
3. **Estimator law for Phase 6.** Wilson 95% intervals on every per-language
   engine CER; paired engine comparisons on the SAME items use McNemar exact,
   never point-estimate deltas; pre-declare the test family before looking
   (per §6.7 power rules, no winner claims on n<50 cells). Abstention
   (empty predictions) is reported as coverage + conditional CER separately —
   never let honest-empty inflate or punish a story silently.
4. **W6 feasible set.** The validation call presents the training tree as
   three columns only: `FEASIBLE NOW` / `FEASIBLE IF <missing primary
   arrives>` (e.g. GPU budget answer) / `INFEASIBLE UNDER CURRENT RULES`.
5. **Pre-declared kill criteria.** Before results are read, kill criteria are
   drafted as conditions on MEASURED numbers; thresholds are parameters the
   operator (user) sets. No fantasy thresholds invented by agents.

## 10. DECISIONS LOCKED (2026-09-27 ~14:35, user-delegated to orchestrator)

**D1 — W6 training path.** Wrap-only is the locked baseline deliverable
(hybrid routing per §6.2 + restoration, zero GPU cost). Conditional second
stage: local QLoRA/LoRA on SAFE languages only, gated on Phase 6 gap
analysis under the estimator law (only if a real, McNemar-significant gap
exists that fine-tune can plausibly close, and laptop memory allows).
NO cloud GPU spend — standing no-money law stands; if the feasible-set
table at the call shows cloud would be decisive, present it with a cost
number for the user to approve explicitly. Final go/no-go at the validation
call (H44–48).

**D2 — Sarvam EN column.** SKIPPED. It changes no build decision: Sarvam is
the benchmark target, not a pipeline component we route to. The EN matrix
carries a permanent note: "sarvam EN: not run (capped 54; no decision
impact)". Follows the DEAD-weight law. Saves 3 calls.

**D3 — 20-item human spot-check.** Deferred to the validation call as a
10-minute agenda item, in this order: (1) gu_o005 — the only W6-relevant
item (gu is VERIFY-FIRST); (2) ks/mni/mr/ur items — already-barred
languages, confirmation only, no decision impact. If the user waives at the
call, log "human check waived" in gt_verification.json.

**D4 — Barred languages (ks, mni, ur, sat, mr + ne PDF-tier).** All stay
excluded from W6 fine-tuning — the bar stands. They still compete in the
final benchmark via the wrap pipeline (the official benchmark scores them
regardless of our internal GT). Engine routing for barred languages uses
Lane A published evidence + native-script support + visual inspection of
outputs — NEVER garbage-GT CERs. Micro-repair option, priority order: ONLY
sat and ks (the weak cells where beating Sarvam matters most) get 5–10
curated pages each, scheduled in W5 after the campaign, ONLY if it does not
threaten the Oct 1 freeze — a tiny clean sat/ks GT passes the
"decision it can change" test (it would re-rank engines for sat/ks
routing). mni/mr/ur: no repair. ne: fill-tier GT usable (90.5% visual
pass), PDF-tier stays BARRED.

## 11. CALL PREP (orchestrator work-stream — feeds Miss's CALL_PACKET.md)

### W6 feasible-set skeleton (to be filled with MEASURED Phase 6 numbers)

| Column | Items |
|---|---|
| FEASIBLE NOW | Wrap-only pipeline: §6.2 tier routing, per-script engine routing, restoration preprocessing, no training. Deliverable guaranteed before freeze. |
| FEASIBLE IF | (a) Local QLoRA on SAFE languages — IF Phase 6 shows a McNemar-significant gap AND laptop memory allows (system ~43% free, swap ~97%; 3–4B backbone at 4-bit is the realistic ceiling — VERIFY at call time, currently UNKNOWN). (b) sat/ks micro-repair — IF W5 time permits after freeze. (c) Sarvam EN column — moot (D2). |
| INFEASIBLE UNDER CURRENT RULES | Cloud GPU rental (no budget), new backbone invention (§9 hard rule), paid APIs, training on barred/GT-garbage languages, sarvam_fill in SFT/RLVR. |

### Kill criteria draft (thresholds = parameters, user sets at call)

1. Kill QLoRA if: wrap-only already beats Sarvam avg on official-style eval, OR no SAFE language shows a significant gap (McNemar p < T1, default 0.05) that > T2% CER improvement could close (default T2 = 3 absolute points).
2. Kill micro-repair if: < 6h remain before freeze at start of repair, OR curated pages fail the purge-era gates (mojibake, script-ratio, Latin ≤0.6).
3. Kill any engine from final routing if: Wilson 95% CI upper bound worse than the next-best engine's point estimate on that language's usable GT (or Lane A evidence for barred langs).

### Weak-cell attack plan (MEASURED 2026-09-27 14:55, orchestrator forensics)

- **Santali (Ol Chiki, 53.91 — Sarvam's weakest cell): TOTAL capability gap.**
  MEASURED: zero engines emit Ol Chiki on sat items — all emit Latin
  gibberish (~45–58% Latin + ~45–55% other); only sarvam_vision emits Ol
  Chiki. We currently have ZERO signal where our biggest win is.
  Engine-by-engine sat capability (MEASURED 2026-09-27 15:00):
  tesseract — NO sat.traineddata exists upstream (404 verified across
  tessdata, tessdata_best, tessdata_fast; `TESS_LANG` maps sat→eng) —
  DEAD path; easyocr — no sat model, falls back to en → gibberish
  expected; paddleocr_indic — sat not in `PADDLE_LANG` → honest-empty;
  surya — **NOT SUPPORTED (PRIMARY, verified 2026-09-27 15:05)**:
  Santali/Ol Chiki is absent from Surya 2's official 91-language
  benchmark table (static/docs/multilingual.md in VikParuchuri/surya,
  linked from README; 87.2% across 91 langs / 32,055 tests — sat not
  among them). Tonight's sat run is an out-of-support observation —
  expect low CER/garbage, treat as observation not benchmark;
  doctr/rapidocr — Latin/garbage (measured). Remaining
  sat attack options: (1) tonight's surya sat outputs; (2) D4 sat
  micro-repair (GT is fill-only garbage — without it even a good engine
  cannot be sanity-checked internally); (3) if surya fails too: sat is a
  vision-LLM-only cell (no money) or a W6 fine-tune target — flag for
  the validation call.
- **Kashmiri (Nastaliq, 54.82): partial capability.** MEASURED script
  fidelity (median Arabic share of output chars, first 20 ks packs):
  rapidocr 71%, tesseract_bilingual 41.7%, tesseract_indic/openbharatocr
  40.5%, doctr 0%, indicphotoocr 0% (dead on ks). GT is fragmented
  Nastaliq (short tokens, pipe artifacts) so internal CER is unreliable —
  routing decision needs a visual quality check + ks micro-repair (D4).
- **OldScan (55.3):** cross-language cell — restoration lane (A3)
  deliverables map directly here; measure best-engine × restoration delta
  on a small clean sample.
- **Odia (80.01):** GT usable (or 91.7% visual pass) — real CERs exist;
  routing by Phase 6 numbers directly; candidate for QLoRA if gap is
  significant.
- **Engine-overlap warning (MEASURED):** tesseract_bilingual ≡
  tesseract_indic ≡ openbharatocr on 322/1257 packs (sat 20/20, mni 20/20,
  en 30/30, ur 58/100, pa 52/90, or 54/69) — same fallback behavior where
  language configs coincide. The leaderboard must treat these as
  overlapping, not independent; effective engine count < nominal count.

## 5. INTEGRATION (after 48h) → THE ULTIMATE PLAN

- Merge all lanes into `docs/research/LEVEL7_INTEGRATED_ARCHITECTURE.md`:
  the current hackathon-selected architecture (SOUTH_CANON §P + PPT_SPEC,
  as-built) evolved with every new method worth ≥ 30/125, each mapped to the
  weak cells and the W6 training tree (R7 updated, not replaced).
- The validation call: all 3 agents + multiple AMs. Agenda: (1) architecture
  review, (2) weak-cell attack plan, (3) W6 go/no-go inputs + GPU budget
  decision, (4) lock the plan. Output: `docs/research/LEVEL7_FINAL_PLAN.md`,
  the single source of truth for the remaining hackathon days.

## 6. TIMELINE (48 hours continuous)

- **H0–2**: spawn lanes, seed collection, verification rules confirmed.
- **H2–24**: deep collection + extraction (subagents run continuously; engines
  finish in parallel on the Engine Agent's main process).
- **H24–30**: verification pass (Verdict), rankings published.
- **H30–40**: cross-lane merge (Miss), contradictions resolved.
- **H40–44**: adversarial review of the integrated architecture.
- **H44–48**: final packet, validation call scheduled and held, plan locked.

## 7. GUARDRAILS (unchanged law — violations end the campaign)

- No training. No new backbone invention. No 400-page datasets for remaining
  languages. No downloads without explicit user approval. No Sarvam calls beyond
  the 54-call cap without asking. Honest-empty is correct — never "fix" it.
  Engines one at a time, never parallel heavy ones. `level2/out/` +
  `level2/reports/` sealed. Count everything from disk. Past reconciled work
  is 100% gold — build forward only.

## 8. SKILL ASSIGNMENTS (locked 2026-09-27)

"Current era" means LIVE sources, not pretrained knowledge: every lane pulls
2025–2026 papers/docs through the parallel-search MCP (web_search/web_fetch)
and context7 MCP. Skills are workflow discipline on top of that.

| Skill | Assigned to | Used for |
|---|---|---|
| `terminal-ops` | Engine, Miss | evidence-logged command execution, disk-truth counts |
| `verification-loop` | Engine, Verdict | verify packs/results from disk before any "done" claim |
| `santa-method` | Verdict | H40–44 adversarial review — 2 independent reviewers must pass |
| `scholar-evaluation` | Verdict | rubric scoring of papers → ranking model (≥30/125 gate) |
| `loop-design-check` | Verdict | audit the 48h loop at H12/H24 — catch spin/Goodhart/wrong-run |
| `council` | Verdict | structured disagreement for ranking ties + validation call |
| `literature-review` | all 3 lanes | systematic search → screen → synthesize → cite |
| `research-ops` | all 3 lanes | evidence-first discipline on every record |
| `deep-research` | all 3 lanes | multi-source cited synthesis |
| `market-research` | Miss (C2) | competition intel |
| `unified-memory` | Verdict, Miss | cross-agent handoffs between Engine/Verdict/Miss |
| `parallel-execution-optimizer` | Miss | keep 3 agents + subagents collision-free |
| `strategic-compact` | Miss | context compaction at phase boundaries |
| `cost-tracking` | all 3 | report token burn in final messages |

If a skill is not installed in an agent's harness, the agent follows the
discipline as written in its prompt (the prompts embed the core rules).
