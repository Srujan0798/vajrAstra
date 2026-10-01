---
name: proto-110-knowledge-canon
description: "2026-10-01 (boss: 'all research md files, concerns, meetings, consensus txt, memory files … make all into one organised flow hierarchy, so an agent reads only the live ones; the others are variants: merge, link, or archive; no file randomly gone; clear checking, reading, compacting, merging') — the KNOWLEDGE CANON task for the Vigilante agent: every authored knowledge file classified LIVE / MERGED / LINKED / HISTORY with a no-loss proof, one numbered tree docs/knowledge/, one CANON_MAP an agent reads first. Specialises proto-107 W1–W8 for knowledge files; code/data/envs stay with proto-107."
metadata:
  node_type: memory
  type: project
---

# PROTO-110 — KNOWLEDGE CANON: one organised hierarchy, nothing lost

## 0. Goal (the boss's words, condensed)
- Every research, concern, meeting, decision, consensus, plan and memory file ends in ONE organised hierarchy.
- An agent arriving later reads ONLY the live files, in a fixed order.
- Everything else is a variant. Each variant is **merged** into its live file (facts carried, sources cited), **linked** (kept as evidence, pointed to), or **archived** (moved, with a verified bundle).
- No file disappears without a checked trail. Never delete: archive only. A deletion needs the boss's GO-D under proto-107.
- Do it slowly: read every line, compact, merge. No skimming, no summarising away facts.

## 1. Scope (what counts as "knowledge")
- **In scope:** authored text (md, txt, tex, json reports, yaml plans) under:
  - `docs/` (incl. `research/`, `campaign/`, `architecture/`, `sources/consensus/`, `south/`, `legal/`, `probe/`, `benchmark_docs/`)
  - `level2/**/*.md` and `level2/research/`
  - `_reports/`, `_archive/` (harvest only)
  - root `*.md`, `.ecc/memory/`, `~/.claude/projects/*South*/memory/` (= repo `_claude_memory/`)
  - the meeting docx/txt (read via textutil)
- **Out of scope** (proto-107 handles these, or they are data):
  - envs (`.venv*`), `Datasets/`, `level2/benchmark/{pages,packs,scores}`, `level2/out/`
  - weights, `graphify-out/` (regenerate), `.opencode/`, `.kilo/`, `.claude/` worktrees, caches, symlinks
- **Measured** (proto-107 §0): 203,380 files exist, but only about 2,000 are authored. The 200k are mostly envs and data and are NOT junk to delete.

## 2. Inputs already done — reuse them, don't redo them
- `docs/campaign/handoff_2026-10-01_v4_integration/digests/`:
  - 50 partition extracts + verifies (2,654 findings, each with path:line);
  - 7 theme digests;
  - `gaps_misc.txt`, `critic.json` (lists the 71 files no partition covered).
- `corpus_extract.md` and `v4_notes.md` (the planner's own full-read notes).
- Already-merged homes:
  - concerns → `BOSS_CONCERNS.md` Part 0 + proto-99 §0;
  - meetings → proto-103 §0;
  - law → proto-01;
  - decisions → proto-92;
  - facts → proto-93;
  - research → proto-97/100/105;
  - plan → proto-108 rev 2;
  - history → `history-completed-protocols.md`.
- proto-107 waves and hazards. Read §0, §1 (the NO-LOSS LAW) and the H-1…H-6 hazards first.

## 3. Target tree (the live hierarchy; numbered = reading order)
```
docs/knowledge/
  00_CANON_MAP.md          ← the ONE file an agent reads first: every live file, why, its order; every variant → where it went
  01_PLAN/                 ← proto-108 rev 2 (strategy) + proto-104 (execution order) + NEXT.md pointer
  02_LAW/                  ← proto-01, boss-rules, proto-92 decisions, ULTIMATE_HYBRID_CONCERN (HL1–HL12), SOUTH_CANON §P
  03_FACTS/                ← proto-93 measured facts + BENCHMARK_22 + LEADERBOARD (tiered) + BODHAN_BASELINE
  04_CONCERNS_MEETINGS/    ← BOSS_CONCERNS (Part 0 live, Part 1 register), meetings (proto-103 + MEETING_2026-09-29_STRUCTURED + Sep-10 sync)
  05_RESEARCH/             ← one final per topic (see §4), each citing its sources; consensus .tex kept as sources
  06_PRODUCT/              ← product docs, schema, B21, Dockerfile notes
  07_OPS/                  ← W4 / DISPATCH_LOG pointers, incident (proto-102), sync (proto-109), gold (proto-107)
  90_SOURCES/              ← LINKED evidence kept as-is (ledgers, raw reports, verify reports), indexed, never edited
  99_HISTORY/              ← ARCHIVED variants (moved, sha-verified), each with a one-line "superseded by" header
```
- Memory (`_claude_memory/`) stays where Claude reads it. `00_CANON_MAP.md` links each memory file to its tree slot. MEMORY.md stays the memory index.
- Do NOT move live files that agents or scripts read by path: W4.md, DISPATCH_LOG, NEXT.md, AGENTS.md, README, `level2/benchmark/docs/AGENT_PROTOCOL.md`, locked files, `docs/campaign/protocols/*` (the sync target).
  - These get a canon entry and stay in place, or get a stub pointer.
  - The tree may hold symlink-free copies only if the map names the original as authoritative. Prefer pointers over copies.

## 4. Research finals (one per topic; each = merged facts + sources)
Draft list; Vigilante confirms it from the digests:
- R-HANDWRITING
- R-PRINTED-ENGINES (probe22 leaderboard, tiers, empties, speed)
- R-WEAK-CELLS (sat/mni/ks/ur/or/sa/kok/OldScan)
- R-TRAINING-COMPUTE (R7 tree, QLoRA spec, kill criteria K1–K4, GPU/costs)
- R-EVAL-GT-LEAKAGE (scorer, tiers, GT lock, transfer obituaries)
- R-COMPETITION-PRODUCT (official rules RQ1, competitor intel, pricing, jury)
- R-LICENCES (RQ9 + licence ledger)
- R-RECIPES (R2 Nastaliq, R3 Ol Chiki/Mayek, R4 OldScan, B21 synthetic, post-correction)
- R-TOOLS-AGENTS (level7 lane B tooling, ECC, graphify, skills; low priority)

**Each final has:**
- a header: sources list, last-verified date, status;
- body sections: CURRENT facts (newest dated wins, errata applied); SUPERSEDED (old → new, with reason); CONTRADICTIONS (both sides + ruling or OPEN); OPEN QUESTIONS;
- every bullet ending with `(path:line)`.

## 5. The per-file verdict (every in-scope file gets exactly one; recorded in `docs/knowledge/_ledger/FILE_LEDGER.csv`)
- **LIVE:** it is the canonical home of its topic. Stays (or moves into the tree with a stub at the old path).
- **MERGED → <final>:** every fact line was carried into the final; the file then goes to 99_HISTORY.
  - Proof per file: a `facts_carried` count and a `facts_dropped` count. Each dropped fact gets a reason: superseded-by `path:line`, or a duplicate of `path:line`.
  - facts_dropped without a reason = FAIL.
- **LINKED:** raw evidence (ledgers, verify reports, consensus .tex, logs). Kept unchanged in 90_SOURCES or in place; cited by finals.
- **HISTORY:** stale but nothing to carry (pure duplicate, sha-twin, superseded draft). Moves to 99_HISTORY with a header naming the live file.
- **Ledger columns:** path, sha256, bytes, lines, verdict, target, facts_carried, facts_dropped, reason, verifier, date.

## 6. Waves (gated; post each check in W4.md; Agent 2 blind-verifies)
- **K0 — Freeze and manifest** (no edits):
  - sha256 manifest of every in-scope file → `docs/knowledge/_ledger/K0_manifest.sha256`, with its count;
  - a verified bundle (`tar` + sha) of all in-scope files into `_archive/bundles/knowledge_K0_<date>.tar` (write-once);
  - check: the bundle lists the same count as the manifest.
- **K1 — Inventory:** one ledger row per manifest file (verdict blank).
  - Mark sha-twins and near-duplicates (same basename, ≥90% line overlap) as clusters.
  - Check: rows = manifest count.
- **K2 — Read and classify:** Sonnet-only readers, ≤ 40 in parallel, read-only, every line.
  - Reuse the 50 partition extracts. Read only what they did not cover: the critic's 71 files plus anything new since.
  - Propose a verdict and target per file.
- **K3 — Write the finals to STAGING** (`docs/knowledge/_staging/`): the §4 finals, `00_CANON_MAP.md`, and the stub texts.
  - Check: every MERGED file has facts_carried + facts_dropped(with reason) = its fact count from the extract.
- **K4 — Blind verify** (Agent 2, own subagents that did not write the finals):
  - sample ≥ 15% of MERGED files: every sampled fact must be found in a final or justified as dropped;
  - re-derive ≥ 20 numbers in the finals from their cited lines;
  - FAIL on any unexplained loss.
- **K5 — The boss reviews** `00_CANON_MAP.md` + the ledger summary (counts per verdict). Then GO-A (moves) yes/no.
- **K6 — Execute moves** (Vigilante, the ONLY mutator for knowledge files, inside a window ACKed by Agents 1–3):
  - `git mv` for tracked files, `mv` for untracked; never `rm`, never `2>/dev/null`;
  - one DISPATCH_LOG line per move;
  - stubs at old paths that scripts or docs reference: `MOVED → <new path> (proto-110 K6, <date>)`.
- **K7 — Links and entry points:**
  - fix every in-repo link to a moved file (grep before and after: 0 dangling);
  - AGENTS.md "START HERE" and docs/INDEX.md point to `docs/knowledge/00_CANON_MAP.md`;
  - MEMORY.md gets one line;
  - `graphify update .`;
  - `bash scripts/agent_bootstrap.sh --sync-only`;
  - sync A (proto-109).
- **K8 — Final check:**
  - manifest count = LIVE + MERGED + LINKED + HISTORY (every file accounted for);
  - every sha in K0 is findable either in the tree or in the bundle;
  - a fresh agent given only `00_CANON_MAP.md` answers 10 boss questions correctly from live files alone (Agent 2 runs it).

## 7. Hard rules
- Never delete. Never edit LINKED sources. Never edit live agent files (W4, DISPATCH_LOG, NEXT.md) except to add a log line.
- Never touch: `Datasets/`, `level2/benchmark/{pages,packs,scores}`, `level2/out/`, weights, locked files (proto-01 §A), `.env`.
- Sonnet subagents only, never Opus. Read-only subagents. One mutator.
- No commit or push except proto-109 sync A to `boss/campaign-docs`. `main` is never touched.
- Coordination with proto-107:
  - knowledge files are owned by proto-110 (Vigilante);
  - proto-107 keeps code, data, envs, worktrees and the dead symlinks;
  - Agent 3 must not run proto-107 W6 on knowledge paths.
- Facts never change meaning in a merge. Numbers are copied, not retyped; every bullet keeps its `(path:line)`.
- If unsure whether a file is live, it is LINKED (kept) and the question goes to the boss.

## 8. Done when
- `docs/knowledge/00_CANON_MAP.md` exists and is linked from AGENTS.md / INDEX / MEMORY.
- Every in-scope file has a ledger row with a verdict; the counts add up to the K0 manifest.
- K4 and K8 are PASS in W4.md, and the boss says the hierarchy is right.

## 9. Paste line — Vigilante agent
`You are the Vigilante for proto-110 (knowledge canon). First sync: git fetch origin boss/campaign-docs and run proto-109 section B. Then read in full: _claude_memory/proto-110-knowledge-canon.md, proto-107-gold-repo-consolidation.md §0–§1, proto-108 rev 2 §0, and docs/campaign/handoff_2026-10-01_v4_integration/digests/critic.json. Do K0 → K4 now (manifest + verified bundle, inventory ledger, classify with Sonnet-only read-only subagents ≤40 reusing the 50 partition extracts, write finals + 00_CANON_MAP to docs/knowledge/_staging/ only). Never delete, never move anything before K5 GO-A, never touch data/weights/locked files/.env, no commits except proto-109 sync A. Post each wave's check in W4.md and stop at K5 with the review pack.`

Related: [[proto-107-gold-repo-consolidation]], [[proto-108-plan-v4-final]], [[proto-109-github-mac-sync]], [[proto-99-concern-crosswalk]], [[proto-103-meeting2-verbatim-truth-and-application]], [[history-completed-protocols]]
