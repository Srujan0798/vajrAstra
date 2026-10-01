# Next work (after first work + stored research)

**First work is complete.** Level 1 frozen. Level 2 sealed: 10 engines × 400 = 4000 packs. Empty pages diagnosed (`docs/south/EMPTY_PAGES.md`). No second South flush. No training. No paid keys.

## Stored (do not redo)

| Work | File |
|---|---|
| Meeting / process law | `OCR_AGENT_MEMORY_FEED.md` |
| PPT dump | `docs/architecture/PPT_SPEC.md` |
| Recipe refresh | `docs/research/W1_RECIPE_REFRESH.md` |
| Sources | `docs/research/SOURCES.md` |
| Hybrid vs PPT (draft) | `docs/architecture/W2_HYBRID.md` |
| South scores | `level2/reports/` |
| Probe law + 20×18 list | `docs/probe/W3_PROBE_SCHEMA.md` · `level2/probe22/` |

## Do now (this phase)

1. **W3 probe — SOURCE SWITCHED 2026-09-26 (user decision); SIZE LOCKED 2026-09-26: 100/lang × 18 langs × 10 engines.** Probe draws from the official hackathon dataset `Datasets/akshardrishti_official/`. The 2026-09-25 Sarvam-bench run (tessdata downloads + tesseract/easyocr preds) was DISCARDED by user order; its 360 images are kept as shortfall fill (user approved).
2. **Execute via `level2/probe22/AGENT_PROTOCOL.md`** (verified tools: `extract_gt.py`, `build_manifest.py`, `run_probe.py`, `metrics.py`). GT audit done 2026-09-26: direct pairs bn 2,938 / hi 3,500 / sa 494 / en 3,500; validated PDF text layers cover 100/lang for 15/18 languages (e.g. hi 23,486; pa 23,372; sd 4,342; gu 3,567 pages). Shortfalls: Dogri 11, Santali 0 → Sarvam fill. Bodo layers are legacy-font mojibake → script-validation gate mandatory; `Bodo/gu/` is a main-test-set copy, NOT GT.
3. **Run free engines** on the merged manifest (no new downloads without asking). Keep South 400 scores. Sarvam 2.1 / Bodhan wait for W5 unless a free path exists. Tesseract-family engines need user-approved traineddata packs: asm, ben, guj, mar, nep, ori, pan, san, snd, urd.
4. **Fill `level2/probe22/sheet.csv`** — CER/WER vs GT.
5. **W4** — OpenCode + Claude + ChatGPT audit using PPT spec + W2 + this sheet. Humans accept/reject.
6. **W5** — 15–20 min freeze after Wednesday 2026-10-01.
7. **W6** — train only after freeze.

## Do not do

Rerun South 400 to chase empty%. Invent a backbone. Train. Collect 400-page remaining-language dumps. Paid Level-3 keys before W5.

## Plan v3 draft (current) → see `docs/campaign/DRAFT_RESEARCH_PLAN.md` (Gate 1 numbers + RF-21..37 pointers added). This file (`docs/PLAN.md`) is the stale 09-26 list of next-work; do not execute from it.
