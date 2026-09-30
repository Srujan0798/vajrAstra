# vajrAstra docs — the hierarchy

One topic, one file. Scores come from disk.

```
South/
├── README.md
├── FULL TECHNICAL BRIEFING.md  ← master doc (Part I briefing, Part II current state)
├── docs/INDEX.md                  ← this file
│
├── LAW
│   ├── AGENTS.md
│   ├── OCR_AGENT_MEMORY_FEED.md   process (W0–W6) + era addendum
│   ├── SOUTH_CANON.md             history + disk (§P refreshed 2026-09-27)
│   ├── HOW_TO_RUN.txt             Level-2 ops
│   ├── level2/ULTIMATE_HYBRID_CONCERN.md   South bench law (+2026-09-27 amendment)
│   └── level2/FOLDER_MAP.md
│
├── ARCHITECTURE
│   ├── AksharDrishti_Hackathon_Proposal final.pptx
│   ├── docs/architecture/PPT_SPEC.md
│   └── docs/architecture/W2_HYBRID.md     DRAFT until W5
│
├── CURRENT WORK
│   ├── docs/research/LEVEL7_RESEARCH_CAMPAIGN.md   ACTIVE campaign law (ops model, lanes, evidence law, D1–D4, call prep)
│   ├── docs/research/level7/            3-agent campaign workspace (prompts, lanes a/b/c, CALL_PACKET.md, W5_BEAT_SARVAM_PLAN.md, W5_STRATEGY_OPTIONS.md, W5_FREEZE_AGENDA.md, W6_QLORA_SPEC.md, KILL_CRITERIA.md)
│   ├── docs/PLAN.md                       next work
│   ├── docs/research/W1_RECIPE_REFRESH.md
│   ├── docs/research/SOURCES.md
│   ├── docs/probe/W3_PROBE_SCHEMA.md
│   ├── docs/probe/schema.json
│   └── level2/probe22/            18-lang probe: manifest 1,227; 11 engines; §6.4 verdicts LOCKED
│
├── SOUTH SCORES
│   ├── level2/reports/LEADERBOARD.md
│   ├── level2/reports/CER_BY_SCRIPT.md
│   ├── level2/reports/LANG_LEADERBOARD.md
│   ├── docs/south/EXTERNAL_BENCHMARK_MAP.md
│   └── docs/south/EMPTY_PAGES.md           empty = engine vs our dump
│
├── LEGAL
│   └── docs/legal/LICENSE_AUDIT.md
│
└── MACHINE
    ├── Datasets/akshardrishti_official/   official all-language dataset (34,871 files)
    ├── arc_level_1/labeled/       Level-1 frozen
    ├── level2/out/                South bench: 10 engines × 400 JSON (sealed)
    ├── level2/probe22/out/        probe runs: 11 engines × up to 1,227 JSON (writing)
    ├── level2/renders_shared/     the 400 page images
    ├── level2/models/<engine>/    PROMPT.md + RUN.md
    ├── level2/research/           generators + gates + anuvaad tessdata
    ├── graphify-out/              law-corpus knowledge graph — **3990 nodes / 4681 edges / 420 communities / 50 hyperedges** (graph.html, GRAPH_REPORT.md, graph.json; rebuilt 2026-09-29 18:24 IST over 18,239-file full corpus, +2666 nodes / +3016 edges / +249 communities vs Sep 27; pre-rebuild backup at .pre-rebuild-2026-09-29)
    └── scripts/

INTEGRATED-ELITE-STACK.md        canonical reference for the integrated elite repo stack (paperthin, looper, graphify, ECC, GLM-OCR, mlx-tune, liteparse, etc.) — install/keep/watch status, where each plugs in, how Engine/Verdict/Miss prompts use it
```

Current (2026-09-29 18:24 IST): Level 7 48h research campaign complete (ended ~04:23 Tue Sep 29) — 3-agent ops model (Engine/Verdict/Miss), lanes A/B/C closed, evidence law §9, decisions D1–D4 locked. probe22: 11 engines × 1,227 items; ALL 11 scored, §6.4 GT verdicts LOCKED (ks/mni/ur/sat/mr + ne-PDF BARRED from W6), W6 QLoRA scaffold K1-locked to kok+pa only. Validation call H44–48 held 2026-09-29; W5 freeze after Wed 2026-10-01; W6 training decision AT the call. Graph: 3990 nodes / 4681 edges / 420 communities (rebuilt this turn from 18,239 files). Do not train before the call.

Do not add markdown at repo root or under `level2/research/`. Edit the file in this tree that already owns the fact.

## Campaign law

- `docs/campaign/CAMPAIGN_DIRECTIVE.md` — **ACTIVE LAW (v4).** Supersedes `uni` v3. Verified disk state, 5 settled conflicts, the wave plan with ready-to-dispatch prompts, and the canonical CO-001…CO-096 register. Original v3 preserved at `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt`.
