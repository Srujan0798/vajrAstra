# FULL TECHNICAL BRIEFING — VAJRASTRA (OFFICIAL)

**Official merged document — last updated 2026-09-27 14:20 IST**

- **Part I** — The Complete Technical Briefing (2026-09-27, morning session): the full explanation of data, pipeline, process law, and training recipe.
- **Part II** — Master Briefing (2026-09-27, evening session): the current state, the 3-agent operations model, and the roadmap.

> **Where Part I and Part II disagree (item counts, engine status, GT verdicts), Part II is the current truth.** Part I is preserved for its full technical explanation of the data structure, the end-to-end pipeline, and the W6 recipe. The manifest was finalized at **1,227 items** after the corruption purge (Part I predates it and says 1,340).

---

# PART I — THE COMPLETE TECHNICAL BRIEFING

You are being trained as an agentic AI engineer architect. This is the entire system — data, process, architecture, and the agent layer that runs it all.

## 1. THE MISSION

BHASHINI AksharDrishti hackathon. Build an OCR system that reads Indian-language documents (forms, old scans, tables, handwriting) at accuracy that beats Sarvam Vision 2.1 — the current state of the art (87.39 word accuracy on their own Indic benchmark). Your team: Vaultstack AI (vajrAstra). You own 4 languages (te, ta, kn, ml) and now lead the probe for all 22 scheduled languages.

**Why we can win:** Sarvam is weak on exactly four cells — Santali (53.91), Kashmiri (54.82), old scans (55.3), Odia (80.01). We fight there, in our domain (200-dpi citizen documents), not on their bench.

## 2. THE DATA — What's Actually on Disk

Everything lives in `Datasets/akshardrishti_official/` — 34,871 files, ~25GB, the ONE official folder (merged from your 13 Downloads zips, verified lossless, duplicates deleted).

Structure per language folder:

```
Datasets/akshardrishti_official/
├── Hindi/                          ← language root
│   ├── s_hindi0001pro_raw.pdf      ← source PDFs (scanned documents)
│   ├── s_hindi0002pro_raw.pdf
│   └── Images and Transcriptions/
│       ├── i_hindi0001pro_labelled.jpeg   ← human-labeled image
│       └── i_hindi0001pro_labelled.txt     ← human GT transcription
├── Bengali/
├── test/test/                      ← 5,344 unlabeled test images (hackathon eval — NEVER train on it)
└── ...
```

Data quality tiers (verified by audit — this is the core truth):

| Tier | Languages | Count | Quality |
|---|---|---|---|
| Human GT pairs | Bengali, Hindi, English, Sanskrit | 10,434 pairs | Gold standard — image + human transcription |
| Clean PDF text layers | hi (23,486 pages), pa (23,372), sd (4,342), te (7,521), ta (6,551), sa (5,934), gu (3,567), bn (2,831), mni (1,353), or (1,625), mr (1,071), mai (701), as (2,504), kok (408), ne (464), ks (314), ur (405) | thousands | Usable after script-validation gates |
| Mojibake PDF layers | Bodo (886 rejected), Gujarati (whole corpus) | — | Legacy font encoding — garbage, rejected |
| Empty layers | Santali (0 pages), Dogri (11 pages) | — | Nothing to extract |
| **TRAP** | `Bodo/gu/` | 4,645 images | Copy of the test set with Gujarati vocab — NOT GT, never use |

## 3. THE PROCESS LAW — Workstreams

The project is governed by `OCR_AGENT_MEMORY_FEED.md` — a law file that every agent (this one, your execution agents, future sessions) must load and obey. This is agentic engineering principle #1: **agents don't follow vibes, they follow written law.**

```
DONE ── Level 1: machine setup (scripts/setup_fresh_machine.sh, .venv311)
DONE ── Level 2: South 400 — 10 engines × 400 pages = 4,000 packs, SEALED in level2/out/
         → results in level2/reports/LEADERBOARD.md (surya + anuvaad tied, median CER 0.43/0.48)
DONE ── W1: recipe research (docs/research/W1_RECIPE_REFRESH.md)
DONE ── W2: hybrid architecture draft (docs/architecture/W2_HYBRID.md vs PPT_SPEC.md)
NOW  ── W3: 18-language probe — 100 samples/lang × engines (your agents executing)
NEXT ── W4: multi-LLM audit (OpenCode + Claude + ChatGPT review the full packet)
NEXT ── W5: freeze — 15-20 min decision session after Wednesday 2026-10-01
NEXT ── W6: train — only after freeze
```

The hard rules (§9 of the law):

1. No downloads of any kind without asking you first. You own data provenance.
2. No training before freeze.
3. Never touch `level2/out/` (the sealed South 400 result) or `level2/reports/`.
4. Every number counted from disk — never asserted, always verified by command.
5. Honest labels — mojibake rejected, shortfalls reported, fill sources labeled.

## 4. THE TECHNICAL PIPELINE — End to End

```
┌─────────────────────────────────────────────┐
│  RAW DATA (official dataset)                │
│  PDFs + human GT pairs + test images        │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  PHASE 1: GT EXTRACTION (extract_gt.py)     │
│  • pymupdf opens every PDF page             │
│  • extract text layer                       │
│  • GATES: ≥50 chars, script-ratio ≥0.5,    │
│    Latin ≤0.6  → mojibake rejected         │
│  • collect human pairs (.jpg/.jpeg + .txt)  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  PHASE 2-3: DRAW + MATERIALIZE              │
│  (build_manifest.py)                       │
│  • 100/lang: pairs first, then stratified   │
│    PDF pages (round-robin across sources)   │
│  • render pages at 200 dpi PNG              │
│  • shortfall fill (doi, sat, ne) from        │
│    Sarvam leftovers, honestly labeled        │
│  • output: manifest_fragments/<lang>.json   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  PHASE 4: MERGE (build_manifest.py --merge) │
│  • 18 fragments → manifest.json             │
│  • finalized at 1,227 items (post-purge)    │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  PHASE 5: ENGINES (run_probe.py)            │
│  • engines, one at a time                  │
│  • --skip-existing (resumable)              │
│  • packs: out/<engine>/<lang>/<id>.json     │
│    {text, gt, ms, error}                    │
│  • + EN sanity column (en_sanity manifest)  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  PHASE 6: SCORING (metrics.py)              │
│  • Indic-aware normalization (danda, quotes,│
│    ZWJ/ZWNJ, bullets stripped)               │
│  • CER/WER + loop/explosion detection       │
│  • sheet.csv: one row per (image, model)    │
│  • error tags: matra_order, conjunct,        │
│    old_scan, handwriting, table...          │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  LEADERBOARD → W4 AUDIT → W5 FREEZE         │
│  → W6 TRAINING (the recipe below)           │
└─────────────────────────────────────────────┘
```

## 5. PROBE EXECUTION STATUS (morning session snapshot — superseded by Part II §6)

The per-language agent lanes (A–E) completed their fragments; the honesty gates produced shortfalls for ne, as, mni, gu, or, brx — the official PDF layers for those languages are mojibake or Latin-heavy. **This is a finding, not a failure:** those languages will need human labeling for training GT after freeze. Final manifest was rebuilt at 1,227 items after the corruption purge.

## 6. THE TRAINING RECIPE (W6 — what we build after freeze)

```
STAGE 0 — DATA
  10,434 human GT pairs + validated PDF-layer GT + synthetic renders
  + human labeling for gu/brx/as/mni/ne (the probe proved this need)
  NOTE (Part II): ks/mni/ur/sat/mr + ne PDF-tier GT is BARRED pending repair
  (§6.4 verdicts) — see Part II §6 before using any PDF-tier GT.

STAGE 1 — PREPROCESS (light hand)
  deskew + Otsu binarize, ONLY on old scans
  (evidence: classic Otsu beat deep denoisers on our own Level-2 runs)

STAGE 2 — BACKBONE (don't invent — fine-tune)
  OCR-specialized VLM: Bodhan 0.8B (Indic specialist, wins Santali)
  or Qwen 3.5 VL / PaddleOCR-VL 1.6 as general spine

STAGE 3 — PROGRESSIVE SFT (curriculum)
  word → line → block → page
  + akshara-boundary auxiliary loss (OUR differentiator —
    Indic scripts are akshara-based; matra order + conjuncts
    are the top error tags in our South 400 data)

STAGE 4 — RLVR (after SFT plateau)
  reward = verifiable CER + binary unit tests on synthetic docs
  (olmOCR 2 pattern → biggest gains on tables, math, multi-column)
  small-model rule: design reward for OUR 0.8-3B size, don't copy big models

STAGE 5 — SCRIPT ROUTER
  Santali (Ol Chiki), Kashmiri/Urdu (Nastaliq), Manipuri (Meitei Mayek)
  → route to specialists, wrap Bodhan's strengths

STAGE 6 — STRUCTURED EXTRACTION HEAD
  schema/KV JSON output for forms — parity with Sarvam 2.1's headline feature
```

## 7. THE AGENTIC ENGINEERING LAYER (your architect skills)

This is the meta-skill set you're building by running this project:

| Principle | How it shows up here |
|---|---|
| Written law over vibes | `OCR_AGENT_MEMORY_FEED.md` — every agent loads it, §9 hard rules bind everyone |
| Gates before results | GT gates freeze BEFORE engines run; verification gates before "done" |
| Count from disk | No agent may assert a number — `ls \| wc -l` or checksum, always |
| Honest failure reporting | Shortfalls labeled, mojibake rejected, gt_source provenance on every row |
| Human owns decisions | Downloads, freezes, strategy calls — agents ask, you decide |
| Parallel lanes, no conflicts | Disjoint language lanes; shared tools (extract_gt.py, metrics.py) so output is uniform |
| LLM-as-evaluator, not architect | W4: three different LLMs audit our packet; we don't let an LLM invent the backbone |
| Sealed baselines | South 400 results are frozen — new work extends, never overwrites |

**The one-sentence architecture:** data → validated GT → probe → leaderboard → audit → freeze → fine-tune specialist + akshara loss + RLVR → beat Sarvam on their weakest cells in our hardest domain.

---

# PART II — MASTER BRIEFING (CURRENT STATE, 2026-09-27 EVENING)

Everything you need to own this project, from mission to next move.

## 1. THE MISSION (why this repo exists)

**Vaultstack AI** (you + Vinay CEO + Akshay CTO + David advisor) is competing in the **Bhashini AksharDrishti hackathon** — build an OCR system for all 22 scheduled Indic languages. The target: **beat Sarvam Vision 2.1**, the current best (bench avg Indic CER 87.39). Its weak cells are your openings: **Santali 53.91, Kashmiri 54.82, OldScan 55.3, Odia 80.01**.

This is not a review paper. The goal is to **ship an Indic OCR that beats current engines**. You own the South track; Krishna owns North, Aryan owns VLM pipeline — never touch their lanes.

## 2. HISTORY IN ONE PASS (what's done = 100% gold, never redo)

| Phase | What happened | Where it lives |
|---|---|---|
| **Level 1** | 400 pages (te/ta/kn/ml) human-labeled, frozen, uploaded | `arc_level_1/labeled/` |
| **Level 2** | 10 free OCR engines × 400 pages = 4,000 packs, sealed | `level2/out/` (SEALED) |
| **South scores** | surya + anuvaad tied leaders (median CER 0.430/0.475), decisive drop after tier-1 | `level2/reports/LEADERBOARD.md` |
| **§P unlock (Sep 25)** | You unlocked a 22-language probe: South 400 kept + 18 remaining languages probed | `SOUTH_CANON.md §P` |
| **W3 probe (now)** | Manifest built from official dataset: **1,227 items** (100/lang target, honesty gates trimmed some), 3 GT tiers | `level2/probe22/` |

## 3. THE LAW (the 12 standing laws — violating any = incident)

1. **Disk truth only** — no claim without a count from disk. (Agents hallucinate numbers.)
2. **One writer, one truth** — the scoring pipeline is the only writer; patch the writer, never the output. (Output-patching got wiped 3×.)
3. **4-page gate** — no engine/config change touches 400 pages until it wins on 4.
4. **Archive, never delete** — merge beats deleting.
5. **Datasets immutable** — reruns versioned.
6. **Family = 1 vote** — tesseract-family (tesseract_indic, openbharatocr, anuvaad, tesseract_bilingual) counts as ONE independent engine, never 4.
7. **No training in the probe, no paid keys, no invented GT, no spell-correcting OCR output** — raw is the benchmark.
8. **Open policy** — engines read any script on any page; language tags are IDs, not constraints.
9. **Consensus law** — 3 engines agreeing can't be hallucinating.
10. **Agents never edit shared pipeline files** — agent work lives in separate dirs. (The Sep 14 contamination incident: a stale script overwrote sealed evidence.)
11. **One fact, one file** — if a fact lives in two places, consolidate.
12. **Incident rules** — same failure ≥5 pages → stop that engine's spawns until you acknowledge.

Plus the project-level hard rules: **no downloads without your approval** (you own data provenance), **no training until W6**, **seal level2/out + reports**, **honest-empty is correct** (an engine with no model for a language returning nothing is the truth, not a bug), and **never re-ask the Sep 25 meeting** — it's distilled in the docs.

## 4. THE METHOD (fixed order, never reversible)

```
W1 research refresh → W2 hybrid vs PPT → W3 22-lang probe (NOW)
→ W4 multi-LLM audit → W5 freeze (after Wed Oct 1) → W6 train
```

- **W3 (current):** probe all 18 remaining languages with free engines + Sarvam trial.
- **W4:** ChatGPT + Claude + OpenCode audit the architecture against actual scores; humans accept/reject.
- **W5:** 15–20 minute freeze where you lock the architecture. **Forbidden until W5: training, novel backbones, paid keys.**
- **W6:** train only after the freeze.

## 5. THE ARCHITECTURE (what you're building — `docs/architecture/PPT_SPEC.md`)

The pipeline you already designed, with the current draft verdict on each box:

| Stage | What | Verdict |
|---|---|---|
| 0 | OpenCV preprocess (deskew/denoise/binarize) | **KEEP** — OldScan is still everyone's worst category |
| 1 | DocLayout-YOLO LoRA on IndicDLP | **HYBRID** — keep stage, maybe swap detector to 2026 defaults |
| 2 | Recognition SFT: Qwen 3.5 VL + PaddleOCR-VL 1.6 (akshara-boundary aux loss — the Indic-specific keep) | **HYBRID** — drop TrOCR-from-scratch (fine-tuning an OCR-VLM beats it 3–6× latency) |
| 2b | RL on CER (RLVR) after SFT | **KEEP** — Sarvam 2.1's own recipe: SFT then RL, never start at RL |
| 3 | Small-LLM SFT: noisy text → corrected JSON | **KEEP if product is forms** |
| 3b | DPO/SimPO on CER-ranked JSON | **KEEP** |
| Eval | Sarvam + IndicDLP + indic-ocr-bench, no fine-tune on test | **UPDATE** bench set |

The Level 7 research campaign exists to pressure-test every one of these verdicts against the current 2025–2026 paper era before you freeze.

## 6. CURRENT STATE (verified from disk)

**Probe execution — engines:**
- DONE, 0 errors: rapidocr, tesseract_bilingual, doctr, tesseract_indic, openbharatocr, anuvaad_tesseract (+30 EN sanity packs each)
- sarvam_vision: 54 calls (3/lang × 18), at the free-credit cap
- Running: indicphotoocr (mid-run, 0 fails so far)
- Queued: surya, easyocr, paddleocr_indic

**GT quality — locked (§6.4), the big finding:**
- **BARRED from W6:** ks, mni, ur, sat, mr + ne PDF-tier — their ground truth is corrupted (Nastaliq fragmentation, Ol Chiki broken, Syriac contamination, repetition/mojibake, control chars)
- **SAFE:** as, brx, doi, kok, mai, or, pa
- **Verify-first:** gu, sd
- **Consequence:** mni/sat engine scores are measured against garbage — leaderboard rows for them carry a permanent caveat.

**Engine findings:** tesseract-family fails catastrophically on ornate/degraded scans (~122% CER on English sanity) while reading clean text perfectly — engine weakness, not a broken harness. Doctr ~42%. rapidocr/anuvaad honest-empty on English (no English model, correct behavior).

## 7. THE MACHINE NOW (3-agent parallel model)

You run **three agents simultaneously**, each may spawn subagents:

- **ENGINE AGENT** — finishes engines → Phase 6 scoring → leaderboard + Lane A research (OCR SOTA papers)
- **VERDICT AGENT** — GT verification, hostile audits, ranks/verifies all research + Lane B (RLVR, self-improving agents, orchestration)
- **MISS AGENT** — everything else: Lane C (NVIDIA stack, competition intel, data strategy), health monitoring, validation-call coordination

**Level 7 campaign (48h, running):** the research tier above everything — 1,000+ live 2025–2026 papers, 5,000+ artifacts across Lanes A/B/C, every record scored (relevance × recency × actionability), Verdict verifies 10%, then everything merges into `LEVEL7_INTEGRATED_ARCHITECTURE.md` → **validation call with all agents + AMs** → locked plan → W6 go/no-go.

## 8. YOUR DECISIONS (only you can make these)

1. **GPU budget for W6** — fine-tune vs wrap-only. This gates the entire training plan.
2. **Sarvam EN column** — 3 more trial calls over the 54 cap, yes/no?
3. **20-item human spot-check** — the flagged GT failures in `gt_verification.json` awaiting your eyes.
4. **GT repair for barred languages** (ks/mni/sat/ur/mr) — repair GT, or exclude those languages from W6 and dominate with the 12 usable ones?

## 9. THE ROADMAP FROM HERE

```
Today      → indicphotoocr + surya + easyocr + paddleocr_indic finish
             → Phase 6 scoring → full 18-language leaderboard
Sep 27–29  → Level 7 campaign: lanes hit ≥400 artifacts each, Verdict verifies
Sep 29–30  → merge → integrated architecture → adversarial review
Oct 1      → W5 FREEZE (15–20 min, you decide) — architecture locked
After      → W6: training with gated GT (barred languages excluded or repaired)
             → head-to-head vs Sarvam 87.39
```

You are the architect and the final gate — every human-decidable question batches to you. The agents do the labor; you own method, architecture, money, and scope.

---

# PART III — DIRECTIVE HISTORY (ORIGINAL BOSS BRIEFING, 2026-09-27, ARCHIVED 2026-09-29)

> **This part is archived directive history, not current law. The 7 Untitled deliverables (D1–D7) at root are the canonical executed form.**

*Source: `Untitled` (root, 19,916 bytes, 262 lines), merged into this master doc on 2026-09-29 per audit-5 finding A. Original file deleted after merge.*

### Part III-A — MASTER DIRECTIVE #2 — 3-AGENT ARCHITECTURE + 10-DAY HACKATHON

```
╔══════════════════════════════════════════════════════════════════════╗
║  MASTER DIRECTIVE #2 — 3-AGENT ARCHITECTURE + 10-DAY HACKATHON       ║
║  Issued by: Boss │ Scope: ENTIRE HACKATHON CAMPAIGN                  ║
╚══════════════════════════════════════════════════════════════════════╝

THIS IS A CAMPAIGN-LEVEL DIRECTIVE, NOT A TASK LIST. READ FULLY.
```

**SECTION 1 — THE 3-AGENT ARCHITECTURE (LOCKED)**

We run EXACTLY 3 top-level agents, ALL running SIMULTANEOUSLY as a
multi-agent system. Each may spawn sub-agents and multitask freely
(agentic AI). No 4th top-level agent. No solo work outside this frame.

- **AGENT 1 — ENGINE AGENT**
  - Owns: all OCR engines, model execution, probe runs, scoring
    pipelines, downloads (with approval), GPU/compute execution.
  - Never edits shared protocol/docs owned by others.

- **AGENT 2 — VERDICT AGENT**
  - Owns: GT verification, forensics, scorer rules, hostile audits,
    fix-specs, leaderboards, truth/verification of everything the
    others produce. Must counter-check Engine and Miss outputs.
  - Has authority to challenge ANY result with evidence.

- **AGENT 3 — MISS (MISCELLANEOUS)**
  - Owns: everything not owned by Engine or Verdict — file hygiene,
    doc merges, protocol edits, dispatch logistics, integration glue,
    boss-concern tracking, cleanup executions handed to it.

**INTERFACES** (all file-based, append-only, in `level2/probe22/`):

- `engine_health_log.jsonl` — Engine writes, all read
- `fix_specs/` — anyone proposes, Miss applies, Verdict verifies
- `DISPATCH_LOG.md` — Miss maintains, all obey
- `BOSS_CONCERNS.md` — Miss maintains, all check every turn

**RULE:** Every output one agent produces gets cross-checked by at least
one of the other two before it is treated as truth. Nothing flows to
the boss unverified.

**SECTION 2 — WHERE WE ARE IN THE CAMPAIGN (DO NOT RUSH)**

- C2.1 This is a 10-DAY HACKATHON. We are on approximately DAY 1.
- C2.2 CURRENT PHASE = DATA COLLECTION / PREPARATION. Model training has
  NOT started. Do not rush toward training — rushing now corrupts
  everything downstream.
- C2.3 Everything done so far is 100% GOLD — treat past completed work as
  locked, correct, and non-negotiable. New work must match that
  standard of perfection, not dilute it.
- C2.4 We have done roughly 1% of the total campaign. Internalize this.
  The remaining ~5 days of active development are where 99% of the
  value gets built. Plan capacity accordingly.

**SECTION 3 — THE RESEARCH PHASE (NEXT MAJOR WORKSTREAM)**

This is the highest-value work we will do. Specifications:

- **R3.1 MAGNITUDE:** 1,000–5,000+ research papers minimum. Case studies,
  method PDFs, architecture deep-dives, benchmarks, ablations.
  Not a light literature scan — a DENSE, COMPLETE, EXHAUSTIVE sweep.
- **R3.2 CURRENCY:** Agentic-AI-era CURRENT papers only (latest work — live
  2025–2026 frontier). No dummy/outdated online scraps. Everything
  on the current edge of: agentic AI, self-improving agents,
  multi-agent orchestration, OCR (all modalities: OCR, Indic OCR,
  document AI, VLM-based OCR), RVL (rich visual language), NVIDIA
  ecosystem work, Jaisa/Jais-style Indic LLM work, layout models
  (LayoutLM-lineage, Surya-class), Obsidian/Knowledge-graph memory
  systems, Kimi/Claude/Hermes-class long-horizon agentic systems —
  and how the top repositories in each are architected.
- **R3.3 SPECIALIZED DEPTH:** For OUR use-case (Indic multilingual OCR +
  agentic pipeline), produce specialized research per sub-domain:
  one research thread per area, each ranked and verified.
- **R3.4 VERIFICATION LAYER:** Every research artifact gets verdict/ranking/
  verification treatment — no unverified research enters the plan.
- **R3.5 DURATION:** These agents will run CONTINUOUSLY for 48 HOURS. This is
  a 48-hour continuous task — for a human team this would be ~2
  MONTHS of work. We compress it via parallel multi-agent execution.
  Budget context and time for exactly this.
- **R3.6 OUTPUT:** A unified, integrated research corpus — collated, merged,
  deduplicated — covering every method, architecture, and technique
  worth stealing. This corpus feeds the architecture freeze.

**SECTION 4 — THE ARCHITECTURE FREEZE (ULTIMATE GOAL)**

- A4.1 After research converges, hold an ALL-AGENT CALL / PRE-CHECK:
  every agent + sub-agents present findings, we synthesize ONE
  ULTIMATE ARCHITECTURE — integrated, novel, dense, high-level.
- A4.2 AMBITION BAR: the frozen architecture must combine new methods +
  new architecture + full integration such that no competitor —
  idiot or genius — could realistically catch it within the next
  decade. It should be good enough that others would want to steal it.
- A4.3 This architecture is then LOCKED and becomes the build spec for
  implementation and model training.

**SECTION 5 — LEVEL STRUCTURE (FOCUS RULE)**

- L5.1 The ultimate research/architecture vision is designated LEVEL 7.
  It is HELD — locked in concern, not executed yet.
- L5.2 ACTIVE FOCUS NOW: LEVELS 1 and 2 ONLY (data collection + current
  probe/cleanup/verification work). Execute these to perfection.
- L5.3 Alternatively: if spreading thinner buys more detail, divide and
  parallelize levels across the 3 agents — but Level 7 stays frozen
  until Levels 1–2 are gold.
- L5.4 Do NOT touch model training until the architecture freeze (A4).

**SECTION 6 — EXECUTION CHECKLIST**

- [ ] Confirm all 3 agents running SIMULTANEOUSLY with sub-agent rights
- [ ] Align this directive with the Hybrid Concern/Agent Protocol docs
      (merge conflicts, single source of truth)
- [ ] Boss concerns persisted in `BOSS_CONCERNS.md` (check every turn)
- [ ] Launch 48-hour continuous research agents (R3) — all sub-domains
- [ ] Miss: maintain `DISPATCH_LOG.md`; keep research + operational work
      parallel without collision
- [ ] Verdict: rank + verify all research artifacts as they land
- [ ] Engine: stand ready — research outputs will define engine upgrades
- [ ] Schedule the ALL-AGENT ARCHITECTURE CALL once research corpus ≥80%
- [ ] Report readiness — do NOT ask "what next"; this IS the plan

### Part III-B — MASTER DIRECTIVE — REPO CLEANUP + PROJECT COMPLETION (ALL CONCERNS)

```
╔══════════════════════════════════════════════════════════════════════╗
║  MASTER DIRECTIVE — REPO CLEANUP + PROJECT COMPLETION (ALL CONCERNS) ║
║  Issued by: Boss │ Priority: ABSOLUTE │ Scope: ENTIRE PROJECT        ║
╚══════════════════════════════════════════════════════════════════════╝

YOU ARE NOT BEING ASKED TO DO SMALL FIXES. THIS IS A FULL PROJECT-STATE
RESET. READ THIS ENTIRE FILE TWICE BEFORE TOUCHING ANYTHING.
```

**RULE 0 — HOW YOU WORK (NON-NEGOTIABLE)**

- R0.1 FIRST, before ANY action: read ALL concern/memory md files, ALL md
  files in the repo top-to-bottom, and build a complete mental map.
  Do NOT work from partial memory. Your temporary memory WILL forget
  — therefore you MUST persist everything into md files as you go.
- R0.2 Use SUB-AGENTS (6–7) for the heavy audit work. You coordinate and
  verify; sub-agents read, score, and report. Do NOT rush. Quality
  over speed. Take your own time.
- R0.3 Do NOT delete foolishly. Every file — even old ones — gets a
  verdict: KEEP / MERGE / DELETE, with a one-line reason logged.
- R0.4 Orchestrator's role is DISPATCH + MONITOR, not manual labor. If a
  task belongs to an existing agent (Engine/Miss/Verdict), align it
  into their queue. Only create a new agent if no existing one owns it.

**TASK 1 — FULL REPO AUDIT (50,000+ FILES)**

- T1.1 Do a complete re-scan of the ENTIRE project — all 50,000+ files.
- T1.2 For every file, determine its PURPOSE. Flag every instance of:
  (a) duplicate files, (b) variant copies of the same work,
  (c) unnecessary/trash files, (d) misleading names,
  (e) files not following the intended order/hierarchy,
  (f) unlinked/orphaned files.
- T1.3 Output: `AUDIT_REPORT.md` — full file inventory, per-file verdict
  (KEEP/MERGE/DELETE + reason), grouped by directory.

**TASK 2 — FOLDER & FILE HYGIENE**

- T2.1 The "old" folder still sitting at level 2 — RESOLVE IT. No folder
  may exist as "old" alongside "new" if content is unchanged. Either:
  (a) merge old into new where no code change exists, or
  (b) delete old and create the proper new merged version.
  One source of truth per concern. No side-by-side stale copies.
- T2.2 The 4 previously-completed South languages kept in a SEPARATE folder
  — merge them INTO the main run/data flow so everything is in one
  place and one order. Do not keep parallel old/new splits.
- T2.3 Merge all duplicate/variant md files into single authoritative
  versions (incl. all hybrid-concern md files).
- T2.4 Delete confirmed trash: unlinked scripts, stale json, superseded
  reports — but ONLY after the `AUDIT_REPORT` verdict (T1.3) exists.
- T2.5 After cleanup: verify the linking/flow/hierarchy of every remaining
  file — no orphan, no misleading path, no broken reference.

**TASK 3 — CONCERN MEMORY (PERSISTENCE)**

- T3.1 Create/update `BOSS_CONCERNS.md` capturing ALL ~50+ boss concerns
  from this session, numbered, one line each, nothing dropped.
- T3.2 Every future turn: check `BOSS_CONCERNS.md` first, tick off what's
  done. NEVER rely on temporary context memory for boss concerns.

**TASK 4 — SAMPLE COVERAGE FIX (CRITICAL — CURRENTLY WRONG)**

- T4.1 Current state is ~1,200–1,300 packs. REQUIRED: 100 samples per
  language × all 18 languages = 1,800 minimum.
- T4.2 If a language's linear extraction is insufficient, source the
  remainder PROPERLY: pull additional relevant pages from the
  existing source PDFs/papers — varied pages, random offsets — from
  existing source languages only. Do NOT fabricate sources.
- T4.3 FORBIDDEN shortcuts: taking only the first page of one paper per
  file, taking one paper per file, or any pattern that produces
  unrepresentative samples. Verify each language's 100 are genuinely
  varied and logically sound.
- T4.4 Merge the 4 South languages' samples into this same standard — no
  separate treatment, no old/new split.

**TASK 5 — AGENT PROTOCOL UPGRADES (VERDICT AGENT & ALL AGENTS)**

- T5.1 Verdict agent must STOP asking "what do I do next" repeatedly.
  Upgrade its protocol so it: works autonomously within its scope,
  surfaces only genuine boss-level decisions, and HAS THE NERVE TO
  COUNTER the boss when a directive is wrong — with evidence.
- T5.2 ADOPT the Verdict agent's self-improvement plan (it already
  proposed this — implement, don't re-debate): pre-flight engine
  readiness checks, in-progress engine health monitoring, internal
  hostile self-audit before any external review, §9 schema gates at
  write-time, structured ≤2,000-token briefing format (DECISIONS |
  DELIVERED | BLOCKERS | RISKS | NEXT), proactive fix-specs on first
  detection (<1hr), formal engine-agent health contract.
- T5.3 Take the Verdict agent's suggestions seriously and apply the
  maximum reasonable set to strengthen the project — treat its
  proposals as recommendations to adopt, not questions to bounce back.
- T5.4 If any prompt needs improvement so the agent stops re-asking,
  REWRITE the prompt/task and report the improved version — don't
  just relay the agent's question upward.

**TASK 6 — DISPATCH & COORDINATION RULES**

- T6.1 Main parallel work remains: dispatching prompts to agents and
  MONITORING them. Check on the other parallel task streams — do not
  let any assigned stream stall silently.
- T6.2 Prompts to agents should be ONE-LINE where possible: "read file X
  and implement it" — the detail lives in the md file, NOT in the
  prompt. Do not repeat md content inside prompts.
- T6.3 Where work aligns with an existing agent's lane, inject it into
  that agent's queue. Spin up a new sub-agent only for unowned work.
- T6.4 Track every dispatch in a `DISPATCH_LOG.md`: who, what, when, status.

**TASK 7 — END GOAL (WHY ALL THIS)**

- T7.1 The mission: COMPLETE the project and beat Sarvam (87.39) and every
  competitor. We are not even done with Levels 1, 2, 3 — push through
  ALL levels, in order, no skipping, no half-done levels.
- T7.2 Every cleanup/audit decision must be judged against one question:
  does this move us toward a complete, competitive, truthful project?

**DELIVERABLES (IN ORDER)**

| # | Deliverable | Source |
|---|---|---|
| D1 | `BOSS_CONCERNS.md` | T3 — persist all concerns |
| D2 | `AUDIT_REPORT.md` | T1 — full 50k-file inventory |
| D3 | `CLEANUP_EXECUTION_LOG.md` | T2 — every merge/delete + reason |
| D4 | Sample plan for 18 langs × 100 | T4 — with source-page mapping |
| D5 | `PROTOCOL_UPGRADES.md` | T5 — adopted agent workflow changes |
| D6 | `DISPATCH_LOG.md` | T6 — all agent assignments |
| D7 | Final hierarchy/linkage map of cleaned repo | T2.5 |

**EXECUTION ORDER:** D1 → D2 → D3 → D6 (dispatch sub-agents NOW for T1/T2
in parallel) → D4 → D5 → D7.

DO NOT ask me what to do next. Work this list top to bottom. Surface
ONLY genuine blocking decisions (with your recommendation). Everything
else, decide and execute. GO.

## PART IV — POST-PURGE RE-SOURCE (2026-09-30)

### Manifest final: 1,283 items (was 1,227 in Part I)
- 56 additional items re-sourced for mr/pa/sd (added mr +21, pa +10, sd +25 = 56 items)
- These 56 items are documented in `manifest_additions.json` (subset of `manifest.json`)
- 11 engines × 1,283 items × 18 langs (10 engines at max-power on official tiers + 1 Sarvam at 54-call cap)
- Note: `manifest_additions.json` is a SUBSET of `manifest.json` (the 56 unscored items) — never add the two files
- Per-pool tier breakdown:
  - official_pair_txt n=9 (human-verified): Sarvam 0.064 vs best-local 0.243
  - official_pdf_layer n=36 (PDF-text-layer GT, may be extractor-mirroring): Sarvam 0.311 vs best-local 0.229
  - sarvam_bench n=9 (machine fill): Sarvam 0.278 vs best-local 0.617
  - pooled human-verified n=18: Sarvam **0.171** vs **0.430** = **2.51× best-local** (3.70× surya, 2.02× ex mni/sat)
- All 21 item-level wins in PDF-layer tier, zero elsewhere
- Conclusion: We do NOT lead on 10/18 — the pooled human-verified win is **Sarvam 2.51×**, not us
- Correct framing for Vinay: Sarvam wins on validated tiers; our wrap-only baseline is "don't lose more than Sarvam on weak cells, beat on juried demos"

