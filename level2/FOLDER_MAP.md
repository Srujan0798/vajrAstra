# level2/ — folder map (organized 12 Sep 2026; doc triage 13 Sep 2026)

## ACTIVE (the work)
- `pages_manifest.json` — 400-page frozen set (with dominant_script + mixed_book_page fields)
- `pages_script_map.json` — per-page dominant script (from L1 gold)
- `renders_shared/` — the 400 shared PNG renders (single copy, all engines read these)
- `pages_400/` — legacy page-set folder (kept: INDEX.json + PNGs used by early runs)
- `run_engine.py` — the engine harness (open policy, timeout, retry, heartbeat)
- `orchestrator.py` — one-push ops (status/fill/migrate/verify/dashboard/guards/loop/autoloop)
- `verify_all.py` — mass verification vs PDF text layer
- `verify_v2.py` — suite v2 (consensus/loops/leak/NFC/schema/digits/manifest check)
- `deep_verify.py` — per-pack deep verify (every JSON vs original page: script mix, verdicts OK/EMPTY/THIN/SCRIPT_MISMATCH/ENGLISH_LEAK/LOOP → reports/DEEP_VERIFY_<engine>.json)
- `report_gen.py` — team reports (lang/scenario/gap/showcase/review-queue/duplicates/WhatsApp)
- `seal_gen.py` — RUN.md + metrics.json + LEVEL2_SEAL.md from disk counts
- `audit_engine_quality.py` — quality-20 gate + README writer (gate superseded by verify_v2; kept, .py law: no delete)
- `run_all_engines.py`, `continue_all_engines.sh` — batch runners (older, kept)
- `out/` — LIVE engine output JSONs (per engine)
- `out_archive/` — superseded policy runs (v0_singlelang etc.) — never delete
- `models/` — seal structure per engine (json/, png/, RUN.md, metrics.json, PROMPT.md = engine contract; json_v0_weak = archived weak runs)
- `reports/` — generated reports (VERIFY_*, DEEP_VERIFY_*, MATRIX.csv, LEADERBOARD, FAILURE_TAXONOMY, LANG_*, SCENARIO_BEST, GAP_ANALYSIS, SHOWCASE, REVIEW_QUEUE, DUPLICATE_AUDIT, WHATSAPP_WEEKLY, LEVEL2_SEAL)
- `research/` — +3 model research + smoke tests (incl. anuvaad tessdata) + rapidocr damage stats
- `prompts/` — Level-1 batch prompts (historical, frozen)
- `HEARTBEAT.jsonl` — per-page run telemetry (grows during fills)
- `DASHBOARD.md` — auto-refreshed status page (counts + speed + ETA + guards)
- `logs_active/` — live run logs + SPAWN_GUARD.json (orchestrator spawns here; root stays clean)
- `logs_archive/` — logs of completed engines (auto-moved by `orchestrator.py archive-logs`)

## DOCS (read-me-first order)
- `ULTIMATE_HYBRID_CONCERN.md` — ALL operator directives merged (the law; §10-11 = 10-engine seal contract)
- `PIPELINE_STORY.md` — "explain like I own it" story (what/why/how of the pipeline)
- `README_LEVEL2.md` — level overview
- `LEVEL2_MASTER_BRIEF.txt` — one-page ownership note
- `HOW_TO_RUN.txt`, `EXPLAIN_FOR_SRUJAN.txt`, `ENGINES.txt` — how/what
- `IMPROVEMENTS_CURRENT_WORK.md` — current pipeline improvements (status audited 12 Sep; supersedes archived ENHANCEMENTS_SPEC)
- `IMPROVEMENTS_VAJRASTRA_FUTURE.md` — product roadmap (NOT now)

## models/<engine>/ contents (all 10 engines)
- `PROMPT.md` — ENGINE CONTRACT (invoke config, engine+version, policy, known limits). NOT a prompt sent to engines — L2 engines are programs (no prompting, per ULTIMATE_HYBRID_CONCERN §11)
- `RUN.md` — run facts (identity, counts, examples, rerun history) from seal_gen.py
- `json/`, `png/` (symlinks → renders_shared), `metrics.json`
- `json_v0_weak/` — archived weak runs (archive law)
- `quality_20.json` (tesseract_indic, openbharatocr, easyocr, indicphotoocr, paddleocr_indic) — HISTORICAL: quality-20 gate was replaced by verify_v2 (12 Sep). Kept per archive law, not regenerated.

## Root (repo)
- `scripts/setup_fresh_machine.sh` — one-command fresh-machine setup (venvs, deps, checks)
- root README.md — repo overview (see it for layout)

## _archive/ (dead but kept)
- `ENHANCEMENTS_SPEC.md` — superseded by IMPROVEMENTS_CURRENT_WORK.md (~85% duplicate; archived 13 Sep with header)
- `LEVEL2_SEAL_AGENT_PROMPT.md` — 5-engine-era seal prompt; 10-engine contract lives in ULTIMATE_HYBRID_CONCERN.md §10-11 (archived 13 Sep with header)
- `logs/` — all run logs (incl. logs_cycle, orch_*)
- `reports/` — old audit snapshots (QUALITY_AUDIT etc.)
- `misc/` — weak-investigation artifacts, DISCOVERY.json, old research text

## Rules
- Run logs are born in logs_active/ and move to logs_archive/ when the engine completes
- Engine policy change ⇒ old out/ moves to out_archive/<eng>_vN_<reason>/ first
- Nothing here gets deleted without content-check + archive README note
- level2/__pycache__ deleted 13 Sep (regenerable bytecode — the only allowed delete); venvs' __pycache__ regenerate on import
