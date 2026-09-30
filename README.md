# vajrAstra — Vaultstack / BHASHINI AksharDrishti (South track)

Private working repo. **Map of the tree: [`docs/INDEX.md`](docs/INDEX.md).**

## Read in this order

1. [`AGENTS.md`](AGENTS.md) — load order for any agent
2. [`OCR_AGENT_MEMORY_FEED.md`](OCR_AGENT_MEMORY_FEED.md) — process law (W0–W6)
3. [`SOUTH_CANON.md`](SOUTH_CANON.md) — history, labeling, disk
4. [`docs/architecture/PPT_SPEC.md`](docs/architecture/PPT_SPEC.md) — existing architecture (diff it)
5. [`docs/research/W1_RECIPE_REFRESH.md`](docs/research/W1_RECIPE_REFRESH.md) — what changed since mid-August 2026
6. [`docs/probe/W3_PROBE_SCHEMA.md`](docs/probe/W3_PROBE_SCHEMA.md) — 20 samples × remaining 18 languages
7. [`level2/ULTIMATE_HYBRID_CONCERN.md`](level2/ULTIMATE_HYBRID_CONCERN.md) — South Level-2 bench law

## Layout

```
docs/            law-adjacent current work (architecture, recipe, probe)
Datasets/        source pages te/ta/kn/ml
arc_level_1/     Level-1 labels, frozen
level2/          South 400 × 10 engines (sealed scores + harness)
  reports/       generated leaderboards (writer: report.py)
  out/           4000 JSON packs
scripts/
```

## State

South scores exist. Architecture PPT exists. No new model has been trained. Do not train until the freeze session after Wednesday 2026-10-01.

## Level-2 ops

See [`HOW_TO_RUN.txt`](HOW_TO_RUN.txt). GitHub is code-only: https://github.com/Srujan0798/vajrAstra
