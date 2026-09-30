# vajrAstra docs — the hierarchy

One topic, one file. Scores come from disk.

```
South/
├── README.md
├── docs/INDEX.md                  ← this file
│
├── LAW
│   ├── AGENTS.md
│   ├── OCR_AGENT_MEMORY_FEED.md   process (W0–W6)
│   ├── SOUTH_CANON.md             history + disk
│   ├── HOW_TO_RUN.txt             Level-2 ops
│   ├── level2/ULTIMATE_HYBRID_CONCERN.md   South bench law
│   └── level2/FOLDER_MAP.md
│
├── ARCHITECTURE
│   ├── AksharDrishti_Hackathon_Proposal final.pptx
│   └── docs/architecture/PPT_SPEC.md
│
├── CURRENT WORK
│   ├── docs/research/W1_RECIPE_REFRESH.md
│   ├── docs/probe/W3_PROBE_SCHEMA.md
│   ├── docs/probe/schema.json
│   └── level2/probe22/            outputs land here when drawn
│
├── SOUTH SCORES
│   ├── level2/reports/LEADERBOARD.md
│   ├── level2/reports/CER_BY_SCRIPT.md
│   ├── level2/reports/LANG_LEADERBOARD.md
│   └── docs/south/EXTERNAL_BENCHMARK_MAP.md
│
├── LEGAL
│   └── docs/legal/LICENSE_AUDIT.md
│
└── MACHINE
    ├── Datasets/{te,ta,kn,ml}/
    ├── arc_level_1/labeled/       Level-1 frozen
    ├── level2/out/                10 engines × 400 JSON
    ├── level2/renders_shared/     the 400 page images
    ├── level2/models/<engine>/    PROMPT.md + RUN.md
    ├── level2/research/           generators + gates + anuvaad tessdata
    └── scripts/
```

Current: South 400 is scored. PPT exists. No new model trained. Next is W1 → 20-sample probe of the other 18 languages → hybrid vs the PPT → freeze after Wednesday 2026-10-01 → train.

Do not add markdown at repo root or under `level2/research/`. Edit the file in this tree that already owns the fact.
