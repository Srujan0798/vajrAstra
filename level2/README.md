# level2/ — folder map (cleaned 2026-09-25; post-cleanup snapshot 2026-09-29)

Hierarchy of all project docs: `docs/INDEX.md`. level2 cross-reference index: `UNIFIED_INDEX.md`.

## ACTIVE
- `pages_manifest.json` — 400-page frozen set
- `pages_script_map.json` — per-page dominant script
- `renders_shared/` — the 400 PNG renders (single copy); sha1 in `renders_shared.sha1`
- `pages_400/` — symlinks → `renders_shared/` (seal G8)
- `engines_config.py` — engine roster + versions
- `run_engine.py` — harness
- `orchestrator.py` — one-push ops
- `verify_all.py` / `verify_v2.py` / `deep_verify.py` — verification
- `report.py` / `report_gen.py` / `seal_gen.py` — one writer
- `out/` — **SEALED (L10)** — 4001 files (4000 JSON + 1 README.md). Live engine write target; agents NEVER edit.
- `models/<engine>/` — **4035 files** (4000 JSON + 10 PROMPT.md + 10 RUN.md + 10 metrics.json + 5 quality_20.json + 4000 png symlinks → `renders_shared/`). Documentation view, SHA256-identical to `out/` (see `MODELS_VS_OUT.md`).
- `reports/` — generated scores (LEADERBOARD, CER_BY_SCRIPT, …)
- `research/` — `*_gen.py`, `gates/`, anuvaad tessdata (runtime). No essays.
- `engines/` — plugin socket
- `training_assets/` — Stage 3/3b exports
- `probe22/` — **1227 items × 11 engines** (18 langs, 100/lang where data allows; 54 sarvam subset at 3/lang). `level2/probe22/out/` is **SEALED** — 13289 packs (11 engines × ~1200 packs each).
- `HEARTBEAT.jsonl` — run telemetry
- `DECISIONS.log` — append-only ledger
- `ULTIMATE_HYBRID_CONCERN.md` — L2 bench law

## ARCHIVE
Cleared 2026-09-25 at operator request (synth-leak PNGs, superseded essays, old logs). Live law is `docs/INDEX.md`. Gate ledger stays in `research/gates/`. Anuvaad weights stay in `research/smoke/anuvaad_tesseract/tessdata` (runtime).

## DOCS (amended 2026-09-25 — hierarchy is `docs/INDEX.md`)

Living law (root): `README.md` · `AGENTS.md` · `OCR_AGENT_MEMORY_FEED.md` · `SOUTH_CANON.md` · `HOW_TO_RUN.txt`
Living law (level2): `ULTIMATE_HYBRID_CONCERN.md` (L2 bench law) · `FOLDER_MAP.md` (this file)
Current work: `docs/architecture/` · `docs/research/` · `docs/probe/`
Numbers: `reports/` only (one writer). Engine docs: `engines/README.md` + `models/<eng>/{PROMPT,RUN}.md`.

## models/<engine>/ contents (all 10 engines)
- `PROMPT.md` — ENGINE CONTRACT (invoke config, engine+version, policy, known limits). NOT a prompt sent to engines — L2 engines are programs (no prompting, per ULTIMATE_HYBRID_CONCERN §11)
- `RUN.md` — run facts (identity, counts, examples, rerun history) from seal_gen.py
- `json/`, `png/` (symlinks → renders_shared), `metrics.json`

## Root (repo)
- `docs/INDEX.md` — hierarchy
- `scripts/` — **3 active shell scripts**: `setup_fresh_machine.sh`, `install_mlx_stack.sh` (user-gated), `reclaim_memory.sh` (user-gated)
- `.audit/` — 19 files (cleanup sub-agent reports + `safety_backup/`). Last cleanup 2026-09-28. DO NOT add new files unless requested.
- `graphify-out/` — knowledge graph of the law corpus. Current: **3990 nodes / 4681 edges / 420 communities / 50 hyperedges** (rebuilt 2026-09-29 18:24 from commit `8fec177d`, full corpus = 18239 files; pre-rebuild backup at `.pre-rebuild-2026-09-29`). Canonical: `GRAPH_REPORT.md`.
- `HOW_TO_RUN.txt` — Level-2 ops card

## Rules
- Numbers live in `reports/` (one writer)
- New markdown goes in `docs/`, not here
- `__pycache__` is disposable
# level2/models/ vs level2/out/ — Consolidation Decision

**Date:** 2026-09-29
**Phase:** 6 (disk consolidation per audit-2)
**Decision:** KEEP BOTH (documented dual storage)

---

## TL;DR

`level2/models/` and `level2/out/` contain the SAME 4,000 per-engine JSON
outputs stored in two different on-disk layouts. SHA256-verified identical.
Different *purposes*, not different *truth*.

- `level2/out/` — **writer's output** (run_engine.py writes here, live)
- `level2/models/` — **documented view** (carries PROMPT.md, RUN.md, metrics.json, quality_20.json)

---

## Why both exist

| Aspect | `level2/out/` | `level2/models/` |
|---|---|---|
| **Role** | Harness write target | Documentation view |
| **Structure** | `out/<engine>/<lang>/<page>.json` (nested) | `models/<engine>/{PROMPT.md, RUN.md, metrics.json, quality_20.json, json/<page>.json, png/}` (flat + meta) |
| **Files** | 4,001 (4,000 JSON + 1 README.md) | 4,035 (4,000 JSON + 10 PROMPT.md + 10 RUN.md + 10 metrics.json + 5 quality_20.json + 4,000 png symlinks) |
| **Status** | SEALED (L10 — agents never edit) | KEEP (metadata is unique) |
| **Writer** | `run_engine.py` (live harness) | `migrate` subcommand in `orchestrator.py` |
| **Unique content** | nothing beyond the 4,000 JSON | PROMPT.md, RUN.md, metrics.json, quality_20.json (10+10+10+5 = 35 unique files) |

---

## SHA256 verification (30 samples, 100% match)

Tested by PHASE-6-AGENT on 2026-09-29. For each of 10 engines, picked 3
random JSON files from `models/<engine>/json/` and computed SHA256 of both
the models copy and the corresponding `out/<engine>/<lang>/<page>.json`.

```
TOTAL=30 MATCH=30 MISMATCH=0
```

This confirms the on-disk JSON content is byte-identical. The audit-2
report (see `_archive/cleanup_2026-09-28/AUDIT_level2_other.md` lines 60-75)
also did 8 manual spot-checks (surya × kn/ml/ta/te × 001) — all matched.

**Verdict:** same data, different structure, different purpose.

---

## Why NOT merge

1. **`level2/out/` is SEALED per AGENTS.md L10** ("agents NEVER edit shared
   pipeline files"). Touching it would breach the seal and invalidate every
   verification command anchored to it.

2. **`models/` carries UNIQUE metadata** (PROMPT.md, RUN.md, metrics.json,
   quality_20.json) that `out/` does not have. Deleting `models/<engine>/json/`
   to dedupe would lose nothing — but `models/` itself is the documentation
   layer and must remain.

3. **Symlinks are zero-cost.** The 4,000 PNG symlinks in `models/<engine>/png/`
   point to `renders_shared/` and occupy 0 bytes. Not a duplication concern.

4. **Two distinct consumers.**
   - `orchestrator.py:count()` reads `out/`
   - `orchestrator.py:model_count()` reads `models/`
   - `LEVEL2_SEAL.md` verification block reads both
   - `migrate` subcommand syncs `out/` → `models/`
   - Co-editing both paths to collapse to one is a coordinated 4-file
     change (run_engine.py, orchestrator.py, LEVEL2_SEAL.md, seal_gen.py)
     — too risky for the 24h cleanup window.

---

## Decision: KEEP BOTH

| Directory | Status | Reason |
|---|---|---|
| `level2/out/` | SEALED — never touched | Live engine write target; L10 + AGENTS.md |
| `level2/models/` | KEEP — documentation metadata | Unique PROMPT.md + RUN.md + metrics.json + quality_20.json per engine |

No file was created, modified, moved, or deleted in either directory
during Phase-6. The "consolidation" is purely documentary.

### File counts (verified unchanged)

```
level2/models/: 4035 files (4000 JSON + 10 PROMPT.md + 10 RUN.md + 4000 symlinks + 10 metrics.json + 5 quality_20.json)
level2/out/:    4001 files (4000 JSON + 1 README.md)
```

---

## Cross-references

- **Audit evidence:** `_archive/cleanup_2026-09-28/AUDIT_level2_other.md` §"level2/models/ vs level2/out/ — DEEP COMPARISON"
- **HIERARCHY_MAP.md:** dual-storage note added in §2 (level2/models/ line)
- **Consumer code:** `level2/orchestrator.py` (`count()`, `model_count()`, `migrate`)
- **Verification:** `level2/reports/LEVEL2_SEAL.md` (anchors both trees)

---

**Phase-6 complete. No files modified. Decision: KEEP BOTH.**# Unified OCR Output Index

Single browse point for **all OCR outputs** across both sealed dirs.

> **Path:** `level2/unified/<engine>/<lang>/<file>.json`
> **Sibling layout:** no — one tree, depth-4, same for everything
> **Reversible:** `rm -rf level2/unified/` (does not touch sealed dirs)
> **Created:** 2026-09-29 18:53 IST

## TL;DR

Both South 400 and probe22 outputs are reachable from one parent, with the same `<engine>/<lang>/<file>.json` shape. They are symlinks back to the **sealed** source dirs — nothing in `level2/out/` or `level2/probe22/out/` has been modified.

## What lives here

| Region | Files | Engines | Langs |
|---|---|---|---|
| `level2/unified/` (this index) | **17,289 symlinks** | 11 | 23 distinct |
| `level2/out/` (sealed, South 400) | 4,000 .json | 10 (no sarvam) | te, ta, kn, ml |
| `level2/probe22/out/` (sealed, probe22) | 13,289 .json | 11 | 19 (no te/ta/kn/ml) |

Total 17,289 = 4,000 + 13,289. All real files stay in their sealed dirs; this is a view.

## Why two naming conventions

| | South 400 | probe22 |
|---|---|---|
| Path | `level2/out/<engine>/<lang>/<file>` | `level2/probe22/out/<engine>/<lang>/<file>` |
| File name | `<lang>_<NNN>.json` (e.g., `te_001.json`) | `<lang>[d\|o\|s]<NNN>.json` (e.g., `hi_d001.json`) |
| Variant prefix | none | `d`=direct pair, `o`=official PDF render, `s`=synthetic, empty=sole variant |
| Lang coverage | 4 langs | 19 langs (disjoint from South) |

The asymmetry reflects a real semantic difference: South's 400 pages came from a single fixed provenance per language; probe22's 18-language probe included multiple page-image variants (direct pairs, official PDF renders, synthetic distortions) to stress engines more honestly. The d/o/s prefixes preserve that lineage.

Because the two sets cover **different languages**, files never collide in the unified tree. A south `te_001.json` lives next to nothing else under `te/`, while a probe22 `hi_d001.json` lives alongside its variant siblings `hi_o001.json`, `hi_s001.json` (or whatever variants exist for that lang).

## Engines present in `level2/unified/`

```
anuvaad_tesseract  doctr          easyocr       openbharatocr
indicphotoocr      paddleocr_indic rapidocr      sarvam_vision
surya              tesseract_bilingual tesseract_indic
```

(11 total — sarvam_vision is probe22-only; no south counterpart.)

## Langs present in `level2/unified/<any-engine>/`

```
as  bn  brx  doi  en  gu  hi  kn  kok  ks  mai  mni  mr  ne
or  pa  sa  sat  sd  ta  te  ur
```

(23 total. South contributes te/ta/kn/ml; probe22 contributes the other 19.)

## Browsing recipes

```bash
# All outputs for one engine, alphabetically sorted across both sealed sources
ls level2/unified/anuvaad_tesseract/

# South te pages through one engine
ls level2/unified/anuvaad_tesseract/te/   # → te_001.json ... te_100.json (south)

# probe22 hi pages through one engine
ls level2/unified/anuvaad_tesseract/hi/   # → hi_d001.json ... hi_d100.json (probe22)

# Read any output through the unified tree
cat level2/unified/easyocr/hi/hi_d042.json

# Count files per (engine,lang) under the unified view
for engine in level2/unified/*/; do
  for lang in "$engine"*/; do
    n=$(ls "$lang" 2>/dev/null | wc -l)
    echo "$(basename $engine)/$(basename $lang): $n"
  done
done

# Resolve any symlink back to its sealed source
realpath level2/unified/anuvaad_tesseract/te/te_001.json
# → /Users/srujansai/Desktop/South/level2/out/anuvaad_tesseract/te/te_001.json
```

## Verifying nothing in sealed dirs was touched

```bash
# Spot check south
cat level2/out/anuvaad_tesseract/te/te_001.json | head -3
# should show original south output (page_id, source=S5_govt, ...)

# Spot check probe22
cat level2/probe22/out/anuvaad_tesseract/hi/hi_d001.json | head -3
# should show original probe22 output (image_id, image_name, ...)

# Verify zero broken symlinks
find level2/unified -type l ! -exec test -e {} \; -print | wc -l
# should print 0
```

## To tear this down (no-op on sealed dirs)

```bash
rm -rf level2/unified/
```

The two sealed dirs (`level2/out/`, `level2/probe22/out/`) are never written to. Removal of `level2/unified/` reverses the entire change in one command and leaves both benches byte-identical.

## See also

- `UNIFIED_OUTPUT_PLAN.md` (repo root) — full decision record, option analysis, L10 compliance argument
- `level2/probe22/AGENT_PROTOCOL.md` §6.4 — GT verdicts on ks/mni/ur/sat/mr + ne PDF-tier (lock reasoning)
- `SOUTH_CANON.md` §P — sealed bench law