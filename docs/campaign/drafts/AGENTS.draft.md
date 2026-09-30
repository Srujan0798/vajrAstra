# AGENTS.md — standing law for every agent (Claude Code, OpenCode, Cursor)

Level 1 of the hierarchy: [README.md](README.md) → **AGENTS.md** → [docs/INDEX.md](docs/INDEX.md) → the files it lists.

## START HERE, every session
1. Run `bash scripts/agent_bootstrap.sh`. Claude Code runs it at session start. It prints the NEXT step, checkpoint status and graph freshness, and it syncs memory into `docs/campaign/protocols/`.
2. Read these in order, full reads:
   1. `docs/campaign/checkpoints/NEXT.md` — your lane and your step.
   2. `docs/campaign/protocols/proto-104-project-first-critical-path.md` — THE PLAN (rev 4; Appendix A = merged protocols 65/71/75/76/78/80/81/82 + step Q).
   3. `docs/campaign/protocols/proto-01-law-and-guardrails.md` — the law (LAW ORDER, §A never-list).
   4. `docs/campaign/protocols/boss-rules.md` — the boss's current rules.
   5. `docs/campaign/protocols/proto-88-skill-routing.md` — which skill or tool to use for each step, and its STATUS.
   6. `BOSS_CONCERNS.md` Part 0 — concern themes K-01…K-30.
   7. `docs/campaign/protocols/proto-103-…md` §0 — every meeting and lead message.
3. Before editing any file, open `graphify-out/GRAPH_REPORT.md`. If the graph is older than the last layout change, run `graphify update .`.

## LAW ORDER (a higher line wins)
1. The boss, in chat.
2. proto-104 rev 4.
3. proto-01.
4. boss-rules.
5. proto-92 (decisions + settled conflicts C1–C15).
6. `level2/ULTIMATE_HYBRID_CONCERN.md` HL1–HL12.
7. `SOUTH_CANON.md`.
8. The history docs listed in `docs/INDEX.md` § History. They are never executed from.

## Hard rules (full text: proto-01 §A)
- No subagents on Opus.
- No team-mate lanes.
- No git commit or push without the boss.
- No downloads, no training and no Sarvam calls without the boss. Only ₹67 of Sarvam credit is left; never resubmit a job.
- Sealed paths are read-only: `level2/out/` (until S6), `Datasets/`, `arc_level_1/`, `_archive/bundles/`. `level2/benchmark/packs/` is append-only.
- Locked files:
  - `level2/benchmark/docs/AGENT_PROTOCOL.md`
  - `manifest_v1.json`
  - `scores/sheet_v1.csv`
  - `pipeline/run_probe.py`
  - the default in `pipeline/metrics.py`
- Moves need a sha manifest, a verified bundle and a log line. Never delete. Never use `2>/dev/null` on mv, rm, cp or tar.
- A step is done only when its check output is in `W4.md`. Never say "done" without a reproducing command.
- GT tiers (official_pair / official_pdf / sarvam_bench) are never pooled. South bench items also sit inside step X's 6,909, so never count them twice.
- The product is portable. MLX is never assumed.
- Update `W4.md` and `DISPATCH_LOG.md` after every step. `NEXT.md` is written only by the planner or the boss.

## Agents
- **Agent 1 — Engine:** runs and scores.
- **Agent 2 — Verdict + repair:** verification, incident repair, docs and graph.
- **Agent 3 — Miss / builder:** benchmark packs and `product/`.
