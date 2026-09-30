# A4 — stale path rewrite to the post-move tree (executor report)

- Date: 2026-09-30 (executor subagent, proto-102 Part A step A4)
- Scope grep (binding): `grep -rn "probe22\|level2/unified\|renders_shared\|pages_400\|level2/models/\|level2/reports" --include='*.py' --include='*.sh' level2 scripts | grep -v 'level2/unified/run_bodhan.py'` → **134 lines** at start.
- Mapping applied by meaning per file (not blind sed). Forbidden files untouched: `run_probe.py`, `AGENT_PROTOCOL.md`, `manifest_v1.json`, `sheet_v1.csv`, `run_bodhan.py`, `scores/`, `probe22/out/`, sealed dirs. No commit, no delete, no train, no Sarvam, no download.
- Disk truth used (measured 2026-09-30): `level2/benchmark/{manifest_v1.json,manifest_additions.json,manifest_22.json,pages/<lang>/,packs/<eng>/<lang>/,pipeline/{candidates,manifest_fragments,tessdata,en_sanity,metrics.py},scores/{sheet_v1.csv,sheet_v2.csv,metrics_80.csv,gt_*.json,self_audit_report.json,preds_*.json},logs/{engine_health_log.jsonl,engine_readiness.json},docs/{AGENT_PROTOCOL.md,MLX_INSTALL_RESULT.md,MEMORY_RECLAIM_RESULT.md}}` all exist. `level2/probe22/` absent. `level2/renders_shared`, `level2/pages_400`, `level2/models/`, `level2/reports/CER_STAGE3B.json`, `level2/benchmark/scores/LEADERBOARD.md` all **absent** (`[ -e ]` tested). `level2/out/` exists (South v1, retired).

## 1. Per-file table (19 files edited, 103 scope lines rewritten)

| file | scope lines rewritten | check | RETIRED-SOURCE flags in this file |
|---|---|---|---|
| level2/benchmark/pipeline/gt_forensics.py | 1 (const block L16–20: PROBE→BENCH, manifest→manifest_v1.json, images→pages/, out→scores/gt_forensics.json) | py_compile OK | — |
| level2/benchmark/pipeline/build_manifest.py | 9 (docstring L6–15 + consts L33–37: protocol→benchmark/docs, candidates/fragments→pipeline/, images→pages/, manifest→manifest_v1.json) | py_compile OK | — |
| level2/benchmark/pipeline/en_harness_gate.py | 3 (L3 prose, L12 cd→pipeline, L24–25 + L93 sys.path→pipeline/en_sanity + pipeline/) | py_compile OK | — |
| level2/benchmark/pipeline/build_benchmark_22.py | 33 (L6–7,15,33–34 constants+docstring; 26 generated-md strings L440–917: probe22 paths→benchmark counterparts, prose "probe22"→"benchmark", `basis="probe22"`→`"benchmark"`) | py_compile OK | L8, L35, L451 read sealed `level2/reports/CER_STAGE3B.json` — left, file ABSENT on disk |
| level2/benchmark/pipeline/reconcile_22.py | 13 (L4–5,18–19,26 packs,53 sheet,134–135 pages,140 origin,142 gt pointer,183–184 generator+sources,197 writer→benchmark/manifest_22.json) | py_compile OK | L20 + L185 read sealed `level2/reports/CER_STAGE3B.json` — left, ABSENT; L26 `level2/out` half — left, retired South-v1 tree (EXISTS, read-only fallback) |
| level2/benchmark/pipeline/variance_22.py | 6 (L5–6,9,13,22–23,239: manifest_22→benchmark root, candidates→pipeline/, gates ref→pipeline/extract_gt.py, run cmd→pipeline/) | py_compile OK | — |
| level2/benchmark/pipeline/build_metrics_80.py | 7 (L4,11,22,25,58–59,66,92,96: metrics.py→pipeline, sheet→scores/sheet_v1.csv, out-dir→packs, writers→scores/metrics_80.csv) | py_compile OK | — |
| level2/benchmark/pipeline/build_sheet_v2.py | 9 (L6–7,23,56,58,81–82,99–100,126: manifest→manifest_v1.json, preds→packs/, sheet→scores/sheet_v1.csv, out→scores/sheet_v2.csv) | py_compile OK | — |
| level2/benchmark/pipeline/extract_gt.py | 3 (L5 protocol→benchmark/docs, L9 candidates→pipeline/, L30–31 PROBE→benchmark + CAND→pipeline/candidates) | py_compile OK | — |
| level2/benchmark/pipeline/visual_verify.py | 1 (const block L14–17 → manifest_v1.json, scores/gt_verification.json, pages/) | py_compile OK | — |
| level2/benchmark/pipeline/verify_visual.py | 1 (const block L15–19 → manifest_v1.json, scores/gt_verification.json, scores/gt_forensics.json, pages/) | py_compile OK | — |
| level2/benchmark/pipeline/resource_shortfall.py | 1 (const block L28–32 → pipeline/candidates, pipeline/manifest_fragments, pages/, manifest_v1.json) | py_compile OK | — |
| level2/benchmark/pipeline/spot_check_engine.py | 1 (L12–14 → ROOT=benchmark, scores/, manifest_v1.json; preds_*.json verified present in scores/) | py_compile OK | — |
| level2/benchmark/pipeline/engine_health_log.py | 1 (L5 LOG→benchmark/logs/engine_health_log.jsonl; file exists) | py_compile OK | — |
| level2/benchmark/pipeline/self_audit.py | 5 (L19–22 → scores/gt_verification.json, scores/gt_forensics.json, manifest_v1.json, logs/engine_readiness.json; L97 out→scores/self_audit_report.json; all targets exist) | py_compile OK | — |
| level2/benchmark/pipeline/verify_engine_readiness.py | 6 (L12–13 manifest→manifest_v1.json + logs/; L20–21,25 tessdata→pipeline/tessdata, exists; L92 law string probe22→benchmark) | py_compile OK | — |
| level2/benchmark/pipeline/build_en_sanity.py | 1 (L5 writes→benchmark/pipeline/en_sanity/; DEST already resolves there) | py_compile OK | — |
| scripts/install_mlx_stack.sh | 1 (L13 LOG→benchmark/docs/MLX_INSTALL_RESULT.md; file exists) | bash -n OK | — |
| scripts/reclaim_memory.sh | 1 (L9 LOG→benchmark/docs/MEMORY_RECLAIM_RESULT.md; file exists) | bash -n OK | — |

Deliberate deviations from the task's Part-C mapping (disk truth wins, invent nothing):
- D1: task maps `manifest_22.json` output → `scores/`; the file lives at `level2/benchmark/manifest_22.json` (749,957 B, 2026-09-30 14:50) and `scores/manifest_22.json` is absent. `reconcile_22.py:197` and `variance_22.py:22` point at the real location. Moving the pointer to a nonexistent path would be a fake fix.
- D2: `reconcile_22.py:140 "origin": "probe22"` → `"benchmark"` (data value; grep-0 requires it; old `manifest_22.json` on disk still carries the old value — regenerating it is out of scope).
- D3: `build_benchmark_22.py:746` path rewritten to `level2/benchmark/scores/LEADERBOARD.md` per mapping although the target file is ABSENT (incident loss); it is a historical citation of what EVIDENCE_SUMMARY claimed, not a read this script performs (script reads only manifest_v1/sheet_v1/CER_STAGE3B/script-maps/labeled-counts).
- D4: out-of-scope tokens on edited lines left intact: `reconcile_22.py:136 sc="sheet.csv"` (label, no pattern token), uppercase `PROBE22`/`PROBE22_CODES` (grep is case-sensitive; renaming code identifiers would exceed the path-rewrite mandate).
- D5: `py_compile` wrote `level2/benchmark/pipeline/__pycache__/*.pyc`; left in place (no deletes in this step).

## 2. Untouched scope lines — RETIRED-SOURCE survivors (13) + locked-file errata (4)

RETIRED-SOURCE (code reads a retired tree as data; line left, never repointed):
- level2/research/gates/b1_doctr_parseq_gate.py:18,57,105 — reads `level2/renders_shared/` (ABSENT)
- level2/research/gates/b4_paddle_server_gate.py:60 — reads `level2/renders_shared/` (ABSENT)
- level2/research/gates/b1_parseq_telugu_vocab_gate.py:33 — reads `level2/renders_shared/` (ABSENT)
- level2/research/gates/b3_tessdata_best_gate.py:47 — reads `level2/renders_shared/` (ABSENT)
- level2/deep_verify.py:23 — `RENDERS = L2 / "renders_shared"` (ABSENT)
- level2/run_engine.py:753 — `tmp = L2 / "renders_shared"` (ABSENT)
- level2/engines/test_registry.py:54 — reads `level2/renders_shared/te_001.png` (ABSENT)
- level2/verify_v2.py:334 — `renders = L2 / "renders_shared"` (ABSENT)
- level2/seal_gen.py:198 — source via `level2/renders_shared/` (ABSENT)
- level2/seal_gen.py:279,285 — `pages_400` symlink gate (ABSENT)
- Plus scope-only (not in final grep) retired refs, left as-is: seal_gen.py:199 (`level2/out`, `level2/models` — models ABSENT, out EXISTS retired), seal_gen.py:289 (reports exclude — archive filter, not a data read), seal_gen.py:310 (models RUN.md display string), report.py:6, report_gen.py:4, research/*_gen.py outputs to `level2/reports/` (output declarations, not live inputs), training_assets_gen.py:266 + metrics_rigor_gen.py:13 read sealed `level2/reports/CER_STAGE3B.json` (ABSENT) — RETIRED-SOURCE.

## 3. Final grep output (quoted, 2026-09-30)

Command: `grep -rn "probe22\|level2/unified\|renders_shared\|pages_400" --include='*.py' --include='*.sh' level2 scripts | grep -v 'level2/unified/run_bodhan.py'`
Result (17 lines): 4× locked `run_probe.py` (errata below, file not editable) + 13× RETIRED-SOURCE survivors listed in §2.
`level2/benchmark/pipeline/run_probe.py:2:"""OCR the 20-per-lang probe (already on disk). Writes probe22/out only."""`
`level2/benchmark/pipeline/run_probe.py:17:PROBE = L2 / "probe22"`
`level2/benchmark/pipeline/run_probe.py:230:    """eng + native-language pack from probe22/tessdata (bilingual basis)."""`
`level2/benchmark/pipeline/run_probe.py:407:                    help="manifest to run against (default: probe22/manifest.json; e.g. en_sanity/manifest.json)")`
`level2/research/gates/b1_doctr_parseq_gate.py:18:Pages: te_001, ta_001, kn_001, ml_001 in level2/renders_shared/.`
`level2/research/gates/b1_doctr_parseq_gate.py:57:        img = f"{BASE}/level2/renders_shared/{pid}.png"`
`level2/research/gates/b1_doctr_parseq_gate.py:105:        doc = DocumentFile.from_images(f"{BASE}/level2/renders_shared/te_001.png")`
`level2/research/gates/b4_paddle_server_gate.py:60:        png = L2 / "renders_shared" / f"{pid}.png"`
`level2/research/gates/b1_parseq_telugu_vocab_gate.py:33:img = f"{BASE}/level2/renders_shared/te_001.png"`
`level2/research/gates/b3_tessdata_best_gate.py:47:    img = f"{BASE}/level2/renders_shared/{pid}.png"`
`level2/deep_verify.py:23:RENDERS = L2 / "renders_shared"`
`level2/run_engine.py:753:    tmp = L2 / "renders_shared"`
`level2/seal_gen.py:198:- **source:** level2/pages_manifest.json (400) via level2/renders_shared/`
`level2/seal_gen.py:279:            ["find", str(L2 / "pages_400"), "-type", "l", "!", "-exec",`
`level2/seal_gen.py:285:    gates.append(("G8", "pages_400 symlinks all resolve", g8))`
`level2/engines/test_registry.py:54:    png = ROOT / "level2" / "renders_shared" / "te_001.png"`
`level2/verify_v2.py:334:    renders = L2 / "renders_shared"`
Editable-file residual: **0 lines**.

## 4. Smoke gate — SMOKE-BLOCKED (run_probe.py locked, not touched)

Command (1 item, single engine; manifest load precedes engine dispatch so the block is engine-independent; no further engines attempted per STOP rule):
`python3 level2/benchmark/pipeline/run_probe.py --engine surya --limit-per-lang 1` → exit=1, full output:
`Traceback (most recent call last):`
`  File "/Users/srujansai/Desktop/South/level2/benchmark/pipeline/run_probe.py", line 448, in <module>`
`    main()`
`  File "/Users/srujansai/Desktop/South/level2/benchmark/pipeline/run_probe.py", line 411, in main`
`    items = json.loads(args.manifest.read_text())["items"]`
`  [pathlib frames elided]`
`FileNotFoundError: [Errno 2] No such file or directory: '/Users/srujansai/Desktop/South/level2/level2/probe22/manifest.json'`
Side effects: none — `level2/level2/` was not created; `level2/benchmark/packs/surya/en/` still 30 pre-existing files. No output landed in `packs/` from this run. No packs were modified.

## 5. Metrics parity — primary BLOCKED (no smoked item); supplementary PASS on a pre-existing pack

Primary parity (metrics.py on the one smoked item vs its sheet_v1.csv row) is not performable: SMOKE-BLOCKED, no smoked item exists. Not faked.
Supplementary (labelled as such): recomputed CER for pre-existing pack `level2/benchmark/packs/surya/as/as_01.json` (image_id `as_01`, surya) with `level2/benchmark/pipeline/metrics.py::normalize_for_scoring` + exact Levenshtein + `_bound_rate`, GT from `manifest_v1.json`:
- gt_len=233 pred_len=238 norm lengths 238/238; recomputed_CER=0.012605; stored `scores/sheet_v1.csv` CER='0.0126' (4-dp rounding), WER='0.0968'. Delta 5.04e-06 = rounding only. **MATCH.**

## 6. PATH ERRATUM (U10) — dated 2026-09-30, locked files NOT edited

run_probe.py (`level2/benchmark/pipeline/run_probe.py`):
- L2 docstring `Writes probe22/out only.` → should read `Writes level2/benchmark/packs/<engine>/<lang>/ only.`
- L15–21: `ROOT` resolves to `…/level2` (file moved one level deeper: `parents[2]` of `benchmark/pipeline/`), so `L2=…/level2/level2`, `PROBE=…/level2/level2/probe22` (nonexistent; observed in §4 traceback). Correct post-move constants: repo-root ROOT; `MANIFEST=level2/benchmark/manifest_v1.json`; `IMAGES=level2/benchmark/pages`; `OUT=level2/benchmark/packs`; `TESSDATA=level2/benchmark/pipeline/tessdata`.
- L230 docstring `probe22/tessdata` → `benchmark/pipeline/tessdata`.
- L407 help `probe22/manifest.json` → `benchmark/manifest_v1.json` (default), `en_sanity/manifest.json` → `benchmark/pipeline/en_sanity/manifest.json`.
AGENT_PROTOCOL.md (`level2/benchmark/docs/AGENT_PROTOCOL.md`, locked — U10 path errata only):
- L46 `Work only inside level2/probe22/` → `level2/benchmark/`; L96 `level2/probe22/images/<code>/` → `level2/benchmark/pages/<code>/`; L137,156,227,266 `cd …/level2/probe22` → `cd …/level2/benchmark/pipeline`; L171 `level2/probe22/images/...` listing → `level2/benchmark/pages/...` (also carries `2>/dev/null`, out of A4 scope); L191 `level2/probe22/tessdata/` → `level2/benchmark/pipeline/tessdata/`. L42 (`level2/reports/*`) and L396 (`level2/out/`, `level2/reports/`) are sealed-dir law, not stale paths — no change proposed.

## Verdict: CONDITIONAL-PASS
Edits: 19 files, 103 scope lines, all compile checks green, editable-file grep residual 0. Smoke: SMOKE-BLOCKED on locked run_probe.py (exact error above). Parity: primary blocked (no smoked item), supplementary pre-existing-pack check MATCH. Nothing committed, deleted, trained, downloaded, or Sarvam-called.
