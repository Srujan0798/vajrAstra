# Agent standing law (Vaultstack / AksharDrishti)

## START HERE — every agent, every session (Claude Code, OpenCode, Cursor; set 2026-09-30)
1. Run `bash scripts/agent_bootstrap.sh` first (Claude Code runs it automatically at session start). It prints the NEXT step,
   checkpoint status, open boss decisions, graph freshness, and syncs the protocols into `docs/campaign/protocols/`.
2. Read `docs/campaign/protocols/proto-00-runbook.md` (read order + where every old protocol now lives), then
   **`proto-104-project-first-critical-path.md` = THE PLAN** (rev 4 at the top: goal, facts, rulings R-1…R-15, steps, paste lines),
   `proto-01` (law), `proto-88` (tools in use), `BOSS_CONCERNS.md` Part 0 (merged concerns), `proto-103` §0 (all meetings).
   Do your step from `docs/campaign/checkpoints/NEXT.md` / proto-104. Old protocol numbers (e.g. proto-87, proto-95) were merged
   on 2026-09-30 night — proto-00 maps each to its new home; files under `protocols/_archive_2026-09-30/` are history only.
3. Before each piece of work, load the skill `docs/campaign/protocols/proto-88-skill-routing.md` names for it —
   ECC skills (`verification-loop`, `unified-memory`, `terminal-ops`, `council-multi-model`, `deep-research`, `living-docs-governance`),
   `graphify` for navigation and duplicates, `factchk` for claims, `mandela` for evaluations, `ssotize` for merging files.
4. Hard rules: no subagents on Opus · no training, downloads or Sarvam calls without the boss · sealed dirs read-only ·
   the product must be portable (PyTorch/CUDA/CPU; MLX = Mac-only accelerator, never a dependency) · no team-mate lanes ·
   read `BOSS_CONCERNS.md` first · update the checkpoint AND `NEXT.md` after every step · never say "done" without a reproducing command.

Map: `docs/INDEX.md`. Master doc: `FULL TECHNICAL BRIEFING.md` (root).
Do not re-ask the 2026-09-25 meeting.

Load in this order:

0. `docs/campaign/CAMPAIGN_DIRECTIVE.md` — **ACTIVE LAW v5 (2026-09-29 ~20:45 IST).**
   Supersedes v4 and the `uni` v3 directive (both archived in `_archive/directives/`).
   Carries verified disk state, 12 settled conflicts, the wave plan with ready-to-dispatch
   subagent prompts, the Sonnet execution handoff (**Part S — start there**), the CO status
   crosswalk and the canonical CO-001…CO-096 register. Where any other doc disagrees with
   its Part A, Part A wins. Note: the "18 langs × 100/lang lock" line below is false for the
   scored set (1,227 scored / 1,283 manifest) — see Part A4.
1. `OCR_AGENT_MEMORY_FEED.md` — process law (§9 hard rules, §10 state, §11 log)
2. `SOUTH_CANON.md` §P — how this repo maps to that law
3. `docs/architecture/PPT_SPEC.md` — architecture we already designed (diff it)
4. `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` — ACTIVE campaign law: 3-agent
   ops model (Engine/Verdict/Miss, §1), lanes A/B/C, evidence law (§9),
   locked decisions D1–D4 (§10), call prep (§11)
5. `level2/probe22/AGENT_PROTOCOL.md` — probe22 execution law (§6.4 GT
    verdicts LOCKED; §10 closed)
6. `level2/ULTIMATE_HYBRID_CONCERN.md` — South Level-2 disk law (scores,
    not the next recipe)
7. `INTEGRATED-ELITE-STACK.md` (root) — canonical map of the integrated
   elite-repo stack (paperthin, looper, graphify, ECC, GLM-OCR, mlx-tune,
   liteparse, etc.); install/keep/watch per repo + how each plugs into
   Engine/Verdict/Miss prompts
8. `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` — assignment
   scripts for the 3 worker agents (paste into a fresh subagent session to
   dispatch them); refreshed 2026-09-27 19:00 with current disk truth, the
   integrated elite-stack section, and role-specific call-outs

South scores: `level2/reports/LEADERBOARD.md`, `CER_BY_SCRIPT.md`. Keep them.
Probe scores: `level2/probe22/` (18 langs × 100/lang lock, 11 engines,
sarvam_vision at 54-call cap).

Current state: Level 7 48h research campaign running (ends ~04:23 Sep 29);
engines landing tonight (indicphotoocr finished; surya/easyocr/paddleocr_indic
queued); validation call at H44–48; W5 freeze after Wed 2026-10-01; W6 training
decision at the call. Graph: **3990 nodes / 4681 edges / 420 communities /
50 hyperedges** (rebuilt 2026-09-29 18:24 IST, full corpus = 18,239 files,
graph.json 4.0 MB / GRAPH_REPORT.md 148 KB / graph.html 3.5 MB; pre-rebuild
backup at .pre-rebuild-2026-09-29). Elite stack installed:
paperthin + looper at ~/.config/opencode/skills/ (+2 from 215).

Do not train. Do not invent a novel backbone. Do not collect 400-page sets
for the remaining languages. Do not add new markdown essays at repo root or
under `level2/research/`. No downloads without explicit user approval. No
Sarvam calls beyond the 54-call cap without asking. Honest-empty is correct.

## WHO I AM (orchestrator identity — locked 2026-09-27)

I am the ORCHESTRATOR — the main session, the boss of the 3-agent ops model.

- My agents: ENGINE (build: engines, Phase 6, Lane A), VERDICT (verify +
  specify fixes, never applies them), MISS (equal tier: applies every fix
  spec + Lane C + monitoring + call coordination).
- My job: plan, pre-research, write agent prompts, monitor from disk, hold
  the law, batch user decisions. I do NOT do fixing labour — Verdict
  specifies, Miss applies, Verdict re-verifies (fix-loop max 2 rounds).
- Evidence law: every record carries PRIMARY / MEASURED / DERIVED /
  CONTRADICTION / UNKNOWN / REJECTED / DEAD and names the decision it can
  change. Count from disk. Honest-empty is correct. Sharp UNKNOWN beats a
  soft guess.
- Clock: campaign ends ~04:23 IST Tue Sep 29; validation call H44–48; W5
  freeze after Wed 2026-10-01; W6 training decision happens AT THE CALL.
- I never: train, download, call Sarvam past the 54 cap, touch sealed dirs
  (level2/out/, level2/reports/), re-litigate locked verdicts (§6.4, D1–D4),
  or re-ask the 2026-09-25 meeting.
- My tools are mandatory, not optional: ECC skills (terminal-ops,
  verification-loop, unified-memory, parallel-execution-optimizer), graphify
  (graphify-out/ knowledge graph of the law corpus), MCP servers
  (parallel-search, context7, github), and subagent tasks for parallel
  lanes. Live sources over pretrained knowledge. Always.

## KEY FILES — DISCOVERABLE LOCATIONS (agents read these)

### Meeting Details
- `docs/research/MEETING_2026-09-29_STRUCTURED.md` — Meeting 2 structured notes (D1-D7 decisions, A1-A7 action items, timeline, red lines)
- Original preserved at: `_reports/research/MEETING_2026-09-29_STRUCTURED.md`

### Master Directive
- `docs/research/uni_v3_ORIGINAL_2026-09-29.md` — ULTIMATE MASTER DIRECTIVE v3 (19 parts, R0.1-R0.4, T1-T9)
- Original preserved at: `_archive/directives/uni_v3_ORIGINAL_2026-09-29.txt`

### Canonical Memory
- `OCR_AGENT_MEMORY_FEED.md` (root) — Process law + all consolidated truth
- `SOUTH_CANON.md` (root) — Repo → law mapping
- `FULL TECHNICAL BRIEFING.md` (root) — Master briefing
- `BOSS_CONCERNS.md` (root) — Live concerns log

### Vinay Meeting (Tue 2026-09-30)
- `VINAY_MEETING_PACKET.md` (root) — PRIMARY brief
- `LIVE_LATEST_2026-09-29.md` (root) — Live research (41 sources)
- `PAPERTHIN_AUDIT.md` (root) — 8 mandela findings
- `LOOP_SPEC_W5_W6_W7.md` (root) — Full loop design
