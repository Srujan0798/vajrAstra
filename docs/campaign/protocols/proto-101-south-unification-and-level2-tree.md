---
name: proto-101-south-unification-and-level2-tree
description: "Added 2026-09-30 evening (boss: 'why am I seeing South outputs in a separate place and other languages in other folders… delete them and do newly for South and merge/store them along with other languages') — EXECUTION protocol, no deferrals, owner per phase: all 22 languages become ONE benchmark tree (level2/benchmark/, ONE manifest/pipeline/scorer/table); South re-drawn from the official dataset (+ old South pages re-gated to the same standard); South v1 island retired (4,000 duplicate packs in models/, 21,689 symlinks, reports, renders) to git history + one bundle; weights and third-party assets out of level2; whole-repo folder verdicts; supersedes the timing of proto-70/71 (U10/U11 now)"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T11:02:18.820Z
---

# PROTO-101 — ONE BENCHMARK FOR ALL 22 LANGUAGES + THE FINAL LEVEL2 TREE (execute now, owner per phase)

**Boss, 2026-09-30 evening:** "why am I seeing South out [in a] separate place and other languages in other folders? If they are separate, delete them and do newly for those South and merge or store them relevantly along with other languages. Why are you keeping them separate? This is just a simple concern." Earlier the same concern appeared as CO-001, CO-003, CO-004, CO-025, CO-068, M8, H10 and H13 ([[proto-99-concern-crosswalk]]).

**Why this file exists:**
- [[proto-70-level2-restructure]] (the tree) and [[proto-71-south-rerun-same-standard]] (South under the probe standard) were written this morning with good inventories. **No session was ever assigned them.**
- This file merges them into one ordered execution with an owner per phase and removes the "after the meeting" hedge. U10 and U11 are now DECIDED-NOW, by the boss's order above.
- proto-70/71 stay as the reference for the dependency lists and details; this file decides the order, the owners and the end state.

## Measured state (planner, 2026-09-30 ~17:00 IST, disk + graphify)
| What | Where | Size | Fact |
|---|---|---|---|
| South v1 packs | `level2/out/<engine>/{kn,ml,ta,te}/*.json` | 4,000 files, git-tracked, newest 09-14 | 10 engines × 400 pages; made by `level2/orchestrator.py` + `run_engine.py` + `level2/engines/`; GT = PDF text layer of Level-1 sources (`arc_level_1/`), ~45% legacy-font mojibake → only **126/400** pages carry a CER |
| **Duplicate** South packs | `level2/models/<engine>/json/*.json` | **4,000 real files** | byte-identical copies of `level2/out` (sample `te_029` IDENTICAL; the old "KEEP BOTH" #71 kept duplicates) |
| South views | `level2/models/<engine>/png` (4,000 links), `level2/pages_400` (400 links), `level2/unified` (17,289 links) | 21,689 symlinks | views, zero data |
| South pages | `level2/renders_shared/*.png` | 400 PNG, 570 MB | 200-dpi renders |
| South scores | `level2/reports/` | 48 files, 34 MB | LEADERBOARD, CER_BY_SCRIPT (sealed) |
| Probe (18 langs + en) | `level2/probe22/{manifest.json, images/ (1,194: 158 jpg + 1,036 png), out/<engine>/<lang>/ (13,289 packs, 11 engines), scores/, sheet.csv}` + 98 loose root items | 1.1 GB | from the OFFICIAL dataset via `extract_gt.py` → `build_manifest.py` → `run_probe.py` → `metrics.py` |
| New today 16:20 | `level2/models_bodhan/{indic-ocr, indic-ocr-mlx-bf16, indic-ocr-mlx-4bit}/.cache/huggingface` | downloading | the Engine subagent is writing Bodhan **weights** into level2, next to `level2/models/` (which holds outputs) — a fourth confusing name |
| Model assets scattered | `.deps/IndicPhotoOCR` (4.7 GB, hidden), `level2/probe22/tessdata` (133 MB), `level2/research/smoke/anuvaad_tesseract/tessdata` (read by `run_probe.py:218`), `~/.cache/huggingface` (surya), `level2/models_bodhan` | 5 places | nobody can see why they exist |
| Official South sources | `Datasets/akshardrishti_official/{Tamil 38, Telugu 84, Kannada 41, Malayalam 29}` files | — | PDFs + PNGs; mojibake risk (B12: 52/115 "clean" South pages had legacy-font GT) |

## The end state (one sentence)
Every language — 18 probe languages + ta/te/kn/ml + en — lives in ONE tree, drawn by ONE pipeline from the official dataset, scored by ONE scorer, reported in ONE table. Nothing else in level2 pretends to be a benchmark.
```
level2/
├── README.md                     the ONE level2 map (FOLDER_MAP.md + UNIFIED_INDEX.md + MODELS_VS_OUT.md merged in, then bundled)
├── benchmark/                    ← level2/probe22/ renamed (it IS the 22-language benchmark; "probe22" misled — 18 langs + en)
│   ├── manifest_v1.json          the locked 1,283-item manifest, unchanged (lock = content never edited)
│   ├── manifest_v2.json          v1 items + the South items (same schema, origin: official | south_v1_regated)
│   ├── pages/<lang>/<id>.<ext>   probe22/images + the new South pages
│   ├── packs/<engine>/<lang>/<id>.json   probe22/out + ALL new runs (South, Bodhan, …) — ONE physical tree
│   ├── scores/                   sheet_v1.csv (locked) · sheet_v2.csv (all langs) · preds_* · metrics_* · mcnemar · tables
│   ├── pipeline/                 extract_gt.py · build_manifest.py · run_probe.py · metrics.py · candidates/ · manifest_fragments/ · en_sanity/ · slices/ · snapshots/
│   └── docs/                     AGENT_PROTOCOL.md (locked; path errata only) · README · FINAL_REPORT · …
├── engine_docs/<engine>/         PROMPT.md · RUN.md · metrics.json (the 35 real files from models/)
├── research/                     gate experiments, after the proto-95 harvest
└── logs/                         HEARTBEAT.jsonl · DECISIONS.log · run logs · engine_health_log.jsonl
third_party/  (repo root, gitignored)   IndicPhotoOCR (from .deps) · tessdata (both copies merged, sha-checked) · README: source · licence · revision · sha256 · used-by
model weights (Bodhan, surya, …)         OUTSIDE the repo, in the standard HF cache (~/.cache/huggingface); revision + sha256 recorded in DISPATCH_LOG + docs/legal/LICENSE_AUDIT.md
RETIRED: level2/out · level2/models/*/json|png · level2/unified · level2/pages_400 · level2/renders_shared · level2/reports · level2/engines · the South v1 scripts
         → git history (tracked files: `git rm`) + `_archive/bundles/2026-10-01_south_v1.tar.gz` (untracked) + one "History: South v1" section in BENCHMARK_22.md
```

## Phases (each ends with its check. Owners are lanes: see "Who" at the bottom)

**P0 — Freeze + pre-image (Agent 3, 20 min)**
1. Post `P0 START` in DISPATCH_LOG; the Engine lane confirms which engine, if any, is running.
2. sha256 manifest of every file under level2 except `.venv*` → `docs/campaign/audit/level2_pre_move.sha256`.
3. Bundle the UNTRACKED sealed data about to move: `tar -czf _archive/bundles/2026-09-30_level2_untracked_pre_move.tar.gz level2/probe22/out level2/reports level2/probe22/scores level2/probe22/sheet.csv level2/probe22/manifest.json`. `level2/out` is in git, so git is its pre-image.
4. Verify the bundle: extract to scratch, compare sha256 = 100%.

**Check:** bundle entries = file count; sha sample of 200 = 100%.

**P1 — South feasibility on the official data (Agent 3, read-only except a scratch dir, ~1–2 h)**
Run [[proto-71-south-rerun-same-standard]] Phase A as written:
- **Language tables:** do `extract_gt.py` and `build_manifest.py` cover ta/te/kn/ml? Write the exact additions as fix-specs.
- **Extraction:** extract to `docs/campaign/checkpoints/W_south_reports/candidates_<code>.json`, never overwriting `probe22/candidates/`.
- **Engine support per script:** system tessdata has tam/tel/kan/mal; the `run_probe.py` language maps (PADDLE_LANG etc.) need entries. Record them as fix-specs; U10/U11 cover edits to locked files.

**Plus:** re-gate the 400 South v1 pages with the SAME `extract_gt.py` gates (MIN_CHARS 50, MIN_SCRIPT_RATIO 0.5, MAX_LATIN_RATIO 0.6, MAX_CTRL_CHARS 3). Pages that pass may enter the benchmark as `origin: south_v1_regated`, in the same tree and to the same standard; pages that fail are retired.

**Output:** `docs/campaign/SOUTH_RERUN_FEASIBILITY.md`, one row per language: official clean candidates · distinct PDFs · re-gated v1 pages · total available vs 100 · engine coverage · fix-specs.

**Check (Verdict):** gate statistics reproduce; 10 random candidates per language eyeballed (GT vs image).

**P2 — Build the ONE tree (Agent 3, the only mover; ~1 h + path fixes)**
1. Post `P2 MOVE WINDOW START`. No engine starts a run until `END` is posted.
2. `mv level2/probe22 level2/benchmark`, then reorganise inside it to the tree above: `images/` → `pages/<lang>/` (per-language subfolders), `out/` → `packs/`, loose root items → `scores/` · `pipeline/` · `docs/` · `logs/`. Copy `manifest.json` → `manifest_v1.json` and `sheet.csv` → `sheet_v1.csv`, content untouched.
3. Fix every path constant. Start from proto-70's "Path dependencies" list, then re-grep the live code and docs for `probe22`, `level2/out`, `renders_shared`, `pages_400`, `unified`.
   - `run_probe.py` and `AGENT_PROTOCOL.md` get path errata only (U10).
   - Absolute paths in `engine_health_log.py`, `spot_check_engine.py` and `verify_engine_readiness.py` are fixed too.
4. `graphify`: query the graph for every doc that cites a moved path and update those referrers. Historical logs are left alone.
5. Smoke test: one item per engine through `run_probe.py` from the new paths; outputs land in `benchmark/packs/`.
6. Post `P2 MOVE WINDOW END`.

**Check (Verdict):**
- sha manifest after = before for every moved file, with paths remapped;
- the smoke test passes for all 11 engines;
- `grep -rn "probe22/" --include=*.py level2` = 0 outside the history docs.

**P3 — South draw + runs (Agent 3 prepares; Engine lane runs)**
1. **Draw.** `manifest_v2.json` = v1 items + South items: 100 per language where the P1 feasibility table allows, seed 20260926, same stratification. Where fewer exist, take the honest n and record why (the same rule as the 8 short languages; no gate relaxation, no fabrication).
2. **Pages.** Render South pages to `benchmark/pages/<lang>/` in the same format and dpi as the probe images (check `image_meta.json`).
3. **Run list.** Hand it to the Engine lane via DISPATCH_LOG. Order:
   1. Bodhan (after Plan v3 Day 1, from the HF cache);
   2. surya;
   3. tesseract_indic;
   4. rapidocr;
   5. doctr;
   6. easyocr;
   7. indicphotoocr;
   8. paddleocr_indic;
   9. anuvaad_tesseract.

   openbharatocr is recorded as an alias of tesseract_indic (1,225/1,227 identical), and sarvam_vision is marked "not run — cap spent".
4. **Engine discipline.** One engine at a time (AGENT_PROTOCOL). Outputs go straight into `benchmark/packs/<engine>/<lang>/`.
5. **Score.** Use the same `metrics.py`, producing `sheet_v2.csv` for all 22 languages + en, per GT tier ([[proto-62-gt-tier-stratified-reporting]]).

**Check (Verdict):** every engine × South language cell has its count; 10 drawn pages per language spot-checked; no South number is compared with a v1 number.

**P4 — Retire South v1 (Agent 3, after the P3 draw and at least the first 3 engines have landed)**
1. Run `git rm -r level2/out` and `git rm` for the 35 tracked `models/` docs. Git keeps the history, and the 35 docs are moved to `engine_docs/` first.
2. The 4,000 duplicate `models/*/json`: re-verify sha256 against the git blobs, then delete them (U29: twins).
3. Delete the symlink views: `models/*/png`, `pages_400/`, `unified/`. The `unified/` scripts and data (`build_*.py`, `manifest_22.json`, `sheet_v2.csv`, `metrics_80.csv`) move to `benchmark/` first.
4. Bundle the untracked South v1 files into `_archive/bundles/2026-10-01_south_v1.tar.gz` (sha-verified), then remove them: `level2/reports`, `level2/renders_shared`, `level2/engines`, the South v1 root scripts (`orchestrator.py`, `run_engine.py`, `report.py`, `report_gen.py`, `seal_gen.py`, `verify_v2.py`, `deep_verify.py`, `engines_config.py`, `pages_manifest.json`, `pages_script_map.json`, `renders_shared.sha1`).
5. `BENCHMARK_22.md` gets ONE history section: "South v1 (Sep 11–14, Level-1 own-labelled sources, 126/400 scorable) — archived, not comparable". Every current table is built from `benchmark/` only.

**Check:** `ls level2` shows exactly the target entries; `_archive/INDEX.md` has a line per retired file.

**P5 — Assets out of level2 (Engine lane; after its Bodhan download finishes)**
- Move `level2/models_bodhan/*` into the standard HF cache layout (`~/.cache/huggingface/hub/models--<org>--<name>`), or re-download into it. Record revision + sha256. Delete `level2/models_bodhan/`, and fix `run_bodhan.py` to load by repo id and revision.
- `.deps/IndicPhotoOCR` → `third_party/IndicPhotoOCR`; both tessdata copies → `third_party/tessdata` (sha-dedupe); fix the paths.
- Write `third_party/README.md`: one row per asset — source, licence, revision, sha256, used-by (file:line).

**Check:** each engine's smoke test passes from the new paths; `du -sh level2` falls by at least the weights size.

**P6 — level2 root + repo-root hidden debris (Agent 3)**
- **level2 root:**
  - `README.md` = the one map;
  - FOLDER_MAP / UNIFIED_INDEX / MODELS_VS_OUT → merged into it, then bundled;
  - `HEARTBEAT.jsonl` + `DECISIONS.log` → `logs/`;
  - delete every `__pycache__`.
- **`.kilo/`** (Kilo Code worktrees; both at `8fec177` = main, one already "prunable"):
  - for each worktree, check `git -C <path> status --porcelain`;
  - if clean: `git worktree remove`, then `git worktree prune`; then delete `.kilo/`;
  - if dirty: report to the boss, don't delete.
- **`.playwright-mcp/`** (browser-tool logs from today) → delete; add to `.gitignore`.
- **`.venv` vs `.venv311`:** don't delete. Find which scripts and engines use each (shebangs, docs, run logs); the root `README.md` states it in one line each; drop one only if nothing uses it (boss gate).

**P7 — Verify + show the boss (Verdict)**
- **Counts:** before = after + retired, exactly.
- **Engine coverage:** every language has packs from the same engines, or an honest "not run".
- **Stale references:** 0 live references to retired paths.
- **graphify:** `/graphify … --update`, then islands and not-in-graph counts before → after.
- **Table:** `BENCHMARK_22.md` regenerated from `benchmark/` only.
- **The boss gets 10 lines:** the new `ls level2`, languages × engines coverage, what was retired and where it can be recovered (git commit + bundle).

## Whole-repo folder verdicts (the boss asked why each folder exists)
| Folder | What it is | Verdict | Where |
|---|---|---|---|
| `Datasets/` (27 GB, sealed) | official hackathon data + `test/test` (5,344 unlabelled) | KEEP, sealed | — |
| `arc_level_1/` (413, sealed) | Level-1 labelled pages (the South v1 source) | KEEP, sealed; one README line | P6 |
| `level2/` | benchmark work | RESTRUCTURE into the tree above | P2–P6 |
| `docs/` (675) | campaign docs + research | proto-95 harvest + proto-98 finals | proto-95/98 |
| `_archive/` (521) · `_reports/` (58) | old archives + reports about cleanups | COMPACT → INDEX + bundles; `_reports/` gone | proto-96 |
| `scripts/` (7) | bootstrap / setup | KEEP | — |
| `src/` (46) · `tests/` (1) · `configs/` (1) | untracked OpenCode-built trainer/pipeline (routes on ground truth; broken Laya router, F63) | recommend ARCHIVE (bundle); Plan v3 does not use it | **U3 — boss** |
| `graphify-out/` (567) | knowledge graph | KEEP (gitignored); rebuild after P7 | P7 |
| `.deps/` (4.7 GB) | IndicPhotoOCR engine | MOVE → `third_party/` (visible, documented) | P5 |
| `.venv/` (1.2 GB) · `.venv311/` (2.8 GB) | two Python envs | KEEP; README says which runs what | P6 |
| `.kilo/` (4,117) | Kilo Code worktrees of this repo (stale) | REMOVE via `git worktree remove` / `prune` | P6 |
| `.playwright-mcp/` (6) | browser-tool logs | DELETE + gitignore | P6 |
| `.claude/` (2) | Claude Code settings + hooks | KEEP | — |

## Who (lanes; one-line assignments in NEXT.md)
- **Agent 3** (`ses_f16bc20e…`): P0, P1, P2, P3 prep, P4, P6. This is the structure/Miss lane, with subagents.
- **Agent 1 Engine lane** (`ses_f12a7b89…`): P3 runs (after Plan v3 Day 1) and P5. Until P2 creates `benchmark/packs/`, new Bodhan outputs go to `level2/probe22/out/bodhan*/`, which P2 then moves along.
- **Agent 2 Verdict** (`ses_f1233a0a…`): the checks after P1, P2, P3 and P7.

Every phase posts START/END in DISPATCH_LOG and a STATUS line in `docs/campaign/checkpoints/W4.md`.

**Skills:**
- **graphify:** referrer queries in P2; `--update` in P7.
- **ECC** (loaded in the OpenCode agents; for Claude sessions it loads in NEW sessions only): `living-docs-governance` (README / map merge) · `verification-loop` (every check) · `architecture-decision-records` (only if the tree decision needs an ADR — put it inside `level2/README.md`, no new essay).
- **Others:** `ssotize` (map merge) · `superpowers:verification-before-completion`.

**Honesty rules:**
- No phase says DONE without its check command output pasted into W4.md.
- A language short of 100 is reported with its honest n.
- No v1 number is ever mixed into v2 tables.

Related: [[proto-70-level2-restructure]], [[proto-71-south-rerun-same-standard]], [[proto-98-clean-repo-master]], [[proto-96-archive-reports-compaction]], [[proto-62-gt-tier-stratified-reporting]], [[proto-92-boss-decisions]], [[proto-74-root-hidden-hygiene]]
