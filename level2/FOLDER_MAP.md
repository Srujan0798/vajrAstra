# level2/ — folder map (cleaned 2026-09-25)

Hierarchy of all project docs: `docs/INDEX.md`.

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
- `out/` — live engine JSON (10 × 400)
- `models/<engine>/` — PROMPT.md, RUN.md, metrics.json, json/, png/
- `reports/` — generated scores (LEADERBOARD, CER_BY_SCRIPT, …)
- `research/` — `*_gen.py`, `gates/`, anuvaad tessdata (runtime). No essays.
- `engines/` — plugin socket
- `training_assets/` — Stage 3/3b exports
- `probe22/` — remaining-language probe outputs (empty until drawn)
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
- `scripts/setup_fresh_machine.sh` — fresh-machine setup
- `HOW_TO_RUN.txt` — Level-2 ops card

## Rules
- Numbers live in `reports/` (one writer)
- New markdown goes in `docs/`, not here
- `__pycache__` is disposable
