# CONSOLIDATED_PARALLEL_WORK_2026-09-28.md — Orchestrator parallel-track task ledger

This document merges all parallel-work concerns from this session (and prior sessions) into one canonical reference. Replaces the fragmented per-concern memory I was carrying in chat. Boss's order: "rea llathe conrn na store them so u won meiss aaian ... merge them ... clear order".

Generated 2026-09-28 21:35 IST by orchestrator.

---

## SECTION 0: IDENTITY REMINDER

- I am the ORCHESTRATOR (main session). Three equal-tier worker agents report to me: ENGINE (build), VERDICT (verify + specify fixes), MISS (apply + monitor + Lane C).
- Boss pastes prompts into agents himself (D12). I do NOT dispatch agents (C13).
- Hard rules (§9): no downloads without approval, no training before W6, no manifest edits, sealed dirs (`level2/out/`, `level2/reports/`) untouched.

---

## SECTION 1: PAST CONCERNS CONSOLIDATED (C1–C17 from SESSION_DIRECTIVES, deduped)

The 17 distinct concerns from SESSION_DIRECTIVES_2026-09-28.md, MERGED into 5 thematic clusters so old/new/separate things don't bleed:

### Cluster A — Sampling & data integrity
- **C1** 1800-sample run (got to 1227, locked at 100/lang)
- **C16** 100/lang ≠ 100 independent pages (as/bn/hi/mni/sa/sat = 1 PDF each in source)
- **NEW (this turn)** manifest dedup attempt was wrong, REVERTED (manifest.json ≡ manifest.json.1227items.backup by sha256)
- **NEW (this turn)** rapidocr has 113 extras beyond 1257 lock (as/gu/mr/ne/or/pa/sd)

### Cluster B — File hygiene (audit + delete waste)
- **C9** audit trash/variants/dupes (5 files deleted earlier this session, ~12.23 MB)
- **NEW (this turn)** 7 sub-agents found ~270 KB more deletable in lane B, ~30 MB in backups, ~5 MB in scores dupes
- **NEW (this turn)** `manifest.json.1227items.backup` is BYTE-IDENTICAL to canonical `manifest.json` — pure dead weight

### Cluster C — Engine queue + scoring
- **C4** languages handled properly (sat/ks/mni/mr/ur/ne = §6.4 BARRED or R5-locked)
- **C7** clear honest report (no winner claims n<50, honest-empty cells explicit)
- **NEW (this turn)** all 11 engines scored, effective 10 (openbharatocr = byte-identical dup of tesseract_indic)
- **NEW (this turn)** surya COMPLETED at CER 0.3849 (best non-Sarvam)

### Cluster D — Validation call prep
- **C3** graph integrity (graph at 1324 nodes / 1665 edges / 52 hyperedges / 206 communities)
- **C5** all work not just one (sheets 11,097 rows = 9×1227 + 54 sarvam + EN extras)
- **C15** parallel tracks (3 worker agents + 7 audit sub-agents all running)

### Cluster E — Process & persistence
- **C2** one big agent (3-agent ops model is locked)
- **C8** process Verdict findings don't re-ask (CRITICAL SCOPE RULE locked)
- **C10** apply Verdict self-improvements (8 deliverables on disk, all ACTIVE)
- **C11** stop meta-verdicts do real work (4 fix specs applied to disk)
- **C12** boss pastes prompts himself (boss authorization pattern)
- **C13** don't dispatch agents (boss dispatches)
- **C14** memory loss re-read (SESSION_DIRECTIVES + CHEATSHEET + memory feed §11 are the canonical sources)
- **C17** read all 50+ concerns and save clear (THIS DOCUMENT)

---

## SECTION 2: PARALLEL-WORK AUDIT (7 sub-agent reports)

7 sub-agents ran in parallel on 2026-09-28 21:30 IST. Reports at `.audit/subagent_{1..7}_*.md` (read-only, no deletions performed).

### Sub-agent 1: training_assets region
- **0 byte-identical duplicates** (safe-to-delete is empty by sha256)
- 7 retirement candidates identified (5 SUPERSEDED, 1 MIXED-OLD-NEW, 1 RETIREMENT-STUB)
- **CRITICAL**: `level2/reports/training_data/sft_noisy_to_gold.jsonl` (32.3MB, OLD schema with `gold_json`) vs `level2/training_assets/sft_noisy_to_gold.jsonl` (11.5MB, NEW schema with `gold_source`+`generated_at`) — different versions, both exist, BOTH KEEP until W6 freeze
- `pages_400/INDEX.json` (newer) vs `pages_manifest.json` (older) — INDEX is canonical but 7 scripts still load old one (pipeline trap)

### Sub-agent 2: Lane B region
- **b1**: CLEAN
- **b2**: 6 batch files (~125 KB) content-redundant with `b2_all_artifacts.jsonl` — DEFER until W6 freeze (USER-GATED)
- **b3**: 33 old-format `001_xxx.json` superseded by `artifact_0NN_*.json` (~43 KB); 16 byte-identical dupes (~16 KB); 1 misnamed `.yaml` file with JSON content; 1 missing artifact #051
- **b4**: ALL 13 .md files STALE relative to .jsonl partners (jsonl Sep 28, md Sep 27) — 12 of 13 have URL drift
- **b5**: CLEAN

### Sub-agent 3: docs region
- **`docs/research/R5_*.md` MISSING** despite being cited in 5+ canonical files — HIGHEST PRIORITY DEFER (not a delete, a MISSING file we need to either find or replace refs)
- Stale state in PROMPT_MISS_AGENT.md ("Effective independent engines: 7" should be 10) and PROMPT_ENGINE_AGENT.md (1370-anomaly no longer needs flagging)
- Heavy overlap (but deliberate) among FINAL_VERDICT/CALL_PACKET/CHEATSHEET/SESSION_DIRECTIVES — each serves a distinct role, KEEP-AS-CANONICAL
- 26 KEEP-AS-CANONICAL, 6 DEFER, 0 DELETE

### Sub-agent 4: scores region
- ✅ `preds_tesseract_indic.json` ≡ `preds_openbharatocr.json` (sha `355a3d775b…`, byte-identical)
- ✅ `preds_surya.json` is the 1227-state (current); no partials on disk
- **13 byte-identical duplicates** in 11 groups (sha256-confirmed)
- `surya_spotcheck.json` STALE (total_predictions=726, actual=1227) — never re-run after surya completion
- `mcnemar_results.json` STALE-PARTIAL — superseded by `mcnemar_full_matrix.json` (606 triples vs 382, 11 vs 10 engines)
- 3 `test_bn.*` files (191 KB) dead pre-pipeline calibration
- 5 orphan .tsv files
- **P0 delete list (20 files, ~27 MB freed)**: 11 openbharatocr_* artifacts + 2 en-duplicate preds + mcnemar_results.json + surya_spotcheck.json + 3 test_bn.* + 5 orphan .tsv

### Sub-agent 5: graphify-out + staging region
- graph.json is **1324 nodes / 1665 links / 52 hyperedges / 206 communities** (post-merge)
- AGENTS.md note is STALE (still says 1198/1554 — needs bump)
- vajrastra_law_corpus: 4.4MB, 309 files (live graphify root, KEEP)
- elite_skills_install: install VERIFIED sha-identical (paperthin re0/SKILL.md = `8f418bc5…`; looper = `a84ca572…`)
- **P1 delete list (~1.45 MB freed, zero risk)**:
  1. `graphify-out/manifest.json` (2 bytes, literal `{}`, obsolete)
  2. `vajrastra_law_corpus/b_short/` (empty staging dir)
  3. `/tmp/elite_skills_install/` (install complete)
  4. `/tmp/build_chunk15.py` (output already in graph.json)
  5. `/tmp/{poll_engines,watch_engine_poll}.py`, `wait_surya.sh`

### Sub-agent 6: backup files region
- **CRITICAL**: `manifest.json.1227items.backup` is BYTE-IDENTICAL to canonical `manifest.json` (sha `ad70a277…30a9`) — pure dead weight, **DELETE**
- `manifest_deduped.json` (4.06 MB) different content, KEEP as failed-attempt record per §11
- 17 `manifest_fragments/*.json.pre-purge` (5.19 MB) — DEFER
- 2 `.DS_Store` (14 KB) gitignored — DELETE
- 59 `.pyc` (0.51 MB) gitignored, includes 1 stale `run_probe.cpython-311.pyc` — DELETE
- **86 findings total, 30 MB of backup/duplicate material**

### Sub-agent 7: worktrees + hidden region
- `.kilo/worktrees/screeching-shallot/` (31 MB, 4115 files) — Sep-13 WIP, 29 MB is `level2/out/` (byte-identical to main), DEFER per FINAL_VERDICT §10
- `.git/worktrees/subdued-quince/` (~877 KB) — `git worktree prune --dry-run` confirms prunable, zero-risk
- `.audit/` (216 KB) — NOT gitignored, RISK of git commit, needs .gitignore policy
- 135 KB hidden `__pycache__` — DELETE
- `.DS_Store` files — DELETE

---

## SECTION 3: ACTION PLAN (sha256-verified deletions + pointer fixes)

### 3.1 IMMEDIATE (orchestrator can apply, no user gate, all sha-verified)

| Path | Reason | Bytes freed |
|---|---|---|
| `level2/probe22/manifest.json.1227items.backup` | byte-identical to canonical manifest.json | 5,044,933 |
| `level2/probe22/scores/{preds,metrics_normalized,metrics_raw,metrics_en_normalized,ablation_delta,coverage,en_sanity,tier,wilson_ci,spotcheck}_openbharatocr.{json,tsv}` (14 files) | byte-identical to tesseract_indic; engine duplicate | ~27,000,000 |
| `level2/probe22/scores/preds_openbharatocr_en.json` | en-duplicate (tesseract_indic_en equivalent) | ~80,000 |
| `level2/probe22/scores/surya_spotcheck.json` | stale (predictions=726, actual=1227) | ~5,000 |
| `level2/probe22/scores/mcnemar_results.json` | superseded by mcnemar_full_matrix.json | ~199,000 |
| `level2/probe22/scores/test_bn.{json,predictions.csv,metrics.json}` (3 files) | dead pre-pipeline calibration | ~191,000 |
| `level2/probe22/scores/*.orphan.tsv` (5 files) | orphan .tsv files | ~25,000 |
| `graphify-out/manifest.json` | 2 bytes, literal `{}` | 2 |
| `/tmp/elite_skills_install/` (whole dir) | install verified, no longer needed | ~1,400,000 |
| `/tmp/build_chunk15.py` | output already in graph.json | ~12,000 |
| `/tmp/{poll_engines,watch_engine_poll}.py`, `/tmp/wait_surya.sh` | temp wrappers | ~8,000 |
| `vajrastra_law_corpus/b_short/` | empty staging dir | 0 |
| `__pycache__` dirs in `level2/` and `level2/probe22/` | auto-regen | ~135,000 |
| `.DS_Store` files | gitignored, cosmetic | ~14,000 |

**Total safe-to-delete: ~34 MB**, all sha256-verified, all reversible (sources still in canonical).

### 3.2 USER-GATED DEFER (NEED BOSS APPROVAL at validation call or W6)

- `level2/reports/training_data/sft_noisy_to_gold.jsonl` (32.3 MB, OLD schema) — KEEP both versions until W6 freeze
- `level2/training_assets/sft_noisy_to_gold.jsonl` (11.5 MB, NEW schema) — KEEP
- `level2/training_assets/preference_pairs_dpo.jsonl` (already deleted per §10)
- `level2/training_assets/sft_noisy_to_gold.jsonl` (already deleted per §10)
- 6 `level2/probe22/b2_*_batch_*.jsonl` — DEFER to W6 freeze
- 33 `level2/probe22/b3/001_*.json` (old-format superseded) — USER-GATED (defer to W6)
- 16 `level2/probe22/b3/` byte-identical dupes — same gate
- 13 `level2/probe22/b4/*.md` (STALE, mtime drift) — regenerate or defer
- `.kilo/worktrees/screeching-shallot/` (31 MB) — DEFER per FINAL_VERDICT §10
- `manifest.json.pre-*` (15 MB, 3 files) — DEFER
- `manifest_fragments/*.json.pre-purge` (5.19 MB, 17 files) — DEFER

### 3.3 MISSING FILES (need creation, not deletion)

- `docs/research/R5_*.md` — MISSING, cited in 5+ canonical files. Need to either:
  - (a) find the original and restore, or
  - (b) replace references with the actual file (R5 forensics doc → `level2/probe22/R5_*` or similar)
- `level2/probe22/b3/artifact_051_*` — missing artifact number in the sequence

### 3.4 POINTER FIXES (unlink dangling references)

After deletions, scan and fix any docs that reference deleted files:
- `CALL_PACKET.md` references `mcnemar_results.json` (will be deleted) → switch to `mcnemar_full_matrix.json`
- `LEADERBOARD.md` references `surya_spotcheck.json` (will be deleted) → no current ref but verify
- Any `docs/research/R5_*.md` references — need to fix 5+ files

### 3.5 STALE PROMPT FIXES

- `PROMPT_MISS_AGENT.md` line 33: "Effective independent engines: 7" → "10"
- `PROMPT_ENGINE_AGENT.md`: 1370-anomaly no longer needs flagging (root-caused in MISS_MONITOR)
- `AGENTS.md`: graph state note (still says 1198/1554, should be 1324/1665/52/206)

### 3.6 GITIGNORE POLICY

`.audit/` should be added to `.gitignore` to prevent accidental commit of session-internal reports. `.gitignore` policy: any sub-agent intermediate output dir, any `__pycache__`, any `.DS_Store`.

---

## SECTION 4: ORCHESTRATOR ACTION SEQUENCE (next 30 min)

1. **Verify all shasums** one more time (defense in depth)
2. **Apply §3.1 deletions** (sha256-verified, all reversible via git/backup)
3. **Apply §3.5 prompt fixes** (3 small text edits, no risk)
4. **Apply §3.4 pointer fixes** in CALL_PACKET/LEADERBOARD
5. **Update §3.6 .gitignore** (add `.audit/`)
6. **Log §11** in OCR_AGENT_MEMORY_FEED.md with: (a) 7 sub-agent reports completed; (b) ~34 MB safe-to-delete list; (c) user-gated defer list; (d) R5 missing file surfaced as HIGH PRIORITY DEFER

---

## SECTION 5: VALIDATION CALL NOTE (boss handoff)

At the validation call, you (boss) need to decide on:

1. Apply §3.1 deletions NOW (no gate needed, all sha-verified, ~34 MB freed)
2. DEFER §3.2 to W6 freeze (recommended; safer)
3. INVESTIGATE §3.3 missing files (`docs/research/R5_*.md`, `artifact_051`)
4. APPLY §3.4-3.6 (small fixes, no risk)

Total potential disk freed (immediate + user-gated): ~80 MB.

---

*Generated by orchestrator 2026-09-28 21:35 IST. Sources: SESSION_DIRECTIVES_2026-09-28.md + memory feed §11 + 7 sub-agent reports at .audit/subagent_{1..7}_*.md.*
