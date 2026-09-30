---
name: proto-74-root-hidden-hygiene
description: "Added 2026-09-30 — repo root and hidden folders: misleading root files (PROJECT_COMPLETE.md etc.), stray root script, .env secret handling, .kilo worktrees, .deps, src/tests/scripts/configs ownership, duplicate root docs — verdicts, boss gates, safe execution"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T21:54:00.426Z
---

# PROTO-74 — REPO ROOT + HIDDEN FOLDERS HYGIENE (Verdict rules, Miss executes after gates)
> **2026-09-30 evening:** where this protocol differs from [[proto-98-clean-repo-master]] (official tree, `docs/sources/`, topic finals, WORTH score), proto-98 wins.

**Boss:** CO-002 keep only the new, merged · CO-008/015 unnecessary/waste files · CO-010 misleading names · AGENTS.md "no new markdown essays at repo root".

## Measured state (2026-09-30)
Root: 20 md + `AksharDrishti_Hackathon_Proposal.pptx`, `HOW_TO_RUN.txt` (09-25, may cite moved paths), `W5_W6_W7_LOOP.yaml`, `requirements.txt`, `sarvam_smoke.py` (stray script at root), `.env` (Sarvam key; gitignored).
Hidden/support: `.deps/IndicPhotoOCR` 4.4 GB (engine dependency — `level2/run_engine.py:31`; KEEP, document) · `.kilo/worktrees` 31 MB (another agent tool's git worktrees — stale? see proto-76) ·
`.claude/` (2 files) · `configs/evaluation/default.yaml` + `scripts/evaluation/{k1_verdict.py,verify_w6_kill.sh,mcnemar_test.py}` + `scripts/{setup_fresh_machine,install_mlx_stack,reclaim_memory}.sh` ·
untracked `src/` (49 files) + `tests/test_basic.py` (W6 build — U3).

## Items needing a verdict (Verdict subagent reads each, then rules)
| Item | Issue | Proposed |
|---|---|---|
| `PROJECT_COMPLETE.md` | name says complete; project is not | rename → `docs/campaign/history/W5_READY_STATE_2026-09-29.md` + banner, or archive |
| `W5_FREEZE_PLAN.md`, `LOOP_SPEC_W5_W6_W7.md`, `W5_W6_W7_LOOP.yaml`, `W5_BEAT_SARVAM_PLAN.md` (root copy) | W5/W6 plans at root; several copies elsewhere | one home `docs/architecture/w5_w6/`; duplicates per proto-63 |
| `LIVE_LATEST_2026-09-29.md` (root) | duplicate of `docs/research/` copy | pointer/archive (proto-63) |
| `PAPERTHIN_AUDIT.md`, `SAMPLE_PLAN_18_LANGS.md`, `AUDIT_REPORT.md`, `CLEANUP_EXECUTION_LOG.md`, `PROTOCOL_UPGRADES.md`, `HIERARCHY_MAP.md` | root docs; some superseded | keep the 5 directive deliverables (D01–D06 per C5) at root; others move to `docs/` with pointers |
| `sarvam_smoke.py` | stray root script; Sarvam cap is spent | move to `scripts/` with a "do not run — cap spent" header, or archive |
| `HOW_TO_RUN.txt` | 09-25; cites paths that moved | refresh after proto-70, or merge into `README.md` |
| `.env` | secret in repo folder (gitignored) | keep gitignored; verify `git log --all -- .env` shows it was never committed; boss decides moving it outside the repo (U12) |
| `.kilo/worktrees` | possibly stale worktrees of another agent tool | proto-76 decides (active? → keep; stale → `git worktree list`, archive) |
| `scripts/evaluation/*`, `configs/evaluation/*` | appear tied to the `src/` W6 build | follow U3 |
| `src/`, `tests/` | untracked W6 build | U3 |

## Execution rules
Pre-image + sha256 for everything moved; pointers left at old paths for any doc referenced elsewhere; `git mv` where tracked; never touch `.env` content; never delete `.deps`.
After execution: root md count and list recorded; `README.md` at root states the reading order in ≤15 lines.

Related: [[proto-72-per-file-audit]], [[proto-63-single-canonical-files]], [[proto-76-workstreams-and-agent-health]], [[proto-92-boss-decisions]]
