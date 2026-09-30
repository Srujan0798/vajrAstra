# ponytail_001 (converted from ponytail_001.jsonl - all records, fields verbatim)

## Record 1 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Ponytail (DietrichGebert/ponytail): 'Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never written.' YAGNI-enforcement skill/proxy. Measured on real Claude Code sessions editing FastAPI + React repo (tiangolo/full-stack-fastapi-template), 12 feature tasks, Haiku 4.5, n=4: vs no-skill baseline: LOC -54%, tokens -22%, cost -20%, time -27%, safety 100%. Caveman (terse prose control): LOC -20%, tokens +7%, cost +3%, time +2%. 'YAGNI + one-liners' prompt: LOC -33%, tokens -14%, cost -21%, time -30%, safety 95%. Ponytail is ONLY arm that cuts every metric AND stays fully safe.
- **decision_it_changes**: Whether to adopt Ponytail as mandatory skill for all three agents (Engine, Verdict, Miss) to enforce minimal-code discipline — directly implements our W5 freeze + 'do not invent a novel backbone' law.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Pure skill (markdown + hooks) — zero deps, fully local.

## Record 2 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Ponytail's 7-rung ladder (runs AFTER understanding problem): 1) Does this need to exist? → no: skip (YAGNI). 2) Already in codebase? → reuse. 3) Stdlib does it? → use it. 4) Native platform feature? → use it. 5) Installed dependency? → use it. 6) One line? → one line. 7) Only then: minimum that works. Lazy about solution, never about reading. Trust-boundary validation, data-loss handling, security, accessibility NEVER on chopping block. Code ends up small because necessary, not golfed.
- **decision_it_changes**: Whether to adopt this exact 7-rung ladder as our code-generation policy for Engine agent — replaces ad-hoc 'write less code' instructions with deterministic decision procedure.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Ladder is pure prompt logic — no external deps.
- **actionality**: 5

## Record 3 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Ponytail install: 20+ agents supported. Claude Code: '/plugin marketplace add DietrichGebert/ponytail' then '/plugin install ponytail@ponytail' (two separate prompts). Codex: 'codex plugin marketplace add DietrichGebert/ponytail' then 'codex plugin add ponytail@ponytail'. Cursor: 'git clone ... && node ponytail/scripts/cursor-hooks.js install'. Gemini: 'gemini extensions install ...'. OpenCode: add '@dietrichgebert/ponytail' to opencode.json plugins. Hermes: 'hermes plugins install DietrichGebert/ponytail --enable'. Many more. Commands: /ponytail [lite|full|ultra|off], /ponytail-review, /ponytail-audit, /ponytail-debt, /ponytail-gain, /ponytail-help.
- **decision_it_changes**: Which install method for our Claude Code harness — use native plugin commands. The /ponytail-review command is valuable for Verdict agent's code review gate.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Plugin install is local; hooks run node from checkout.
- **actionality**: 4

## Record 4 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md
- **date**: 2026-06-18
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 4
- **actionability**: direct
- **extraction**:

  Ponytail agentic benchmark full writeup: 12 feature tasks on real FastAPI+React repo. Tasks: date picker (404→23 lines, native <input type=date>), color picker (287→23 lines, native <input type=color>), form validation, API client, error boundary, theme toggle, modal, table sort, search, pagination, toast, dropdown. Haiku 4.5, n=4. Ponytail mean: 46% LOC, 78% tokens, 80% cost, 73% time vs baseline. Safety: adversarial tier (separate) — baseline, caveman, ponytail 100%, yagni-oneliner 95%. Cut biggest where over-build trap exists (native HTML elements), near zero on already-minimal code.
- **decision_it_changes**:

  Benchmark validates Ponytail for our Engine agent's build tasks — especially relevant for UI/frontend work in our OCR pipeline (if any). The date/color picker examples show native platform feature detection working.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Benchmark ran on same model class (Haiku 4.5) — reproducible.
- **actionality**: 4

## Record 5 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail compatibility: Works with caveman (JuliusBrussee/caveman) — caveman shrinks what agent SAYS; ponytail shrinks what it BUILDS. Different halves, no overlap. 'Terse talk about minimal code.' Does not need config file (optional ~/.config/ponytail/config.json or PONYTAIL_DEFAULT_MODE env var). Default mode: 'full'. Subagent injection: ruleset injected into every subagent via Agent tool; scope with PONYTAIL_SUBAGENT_MATCHER regex (e.g., 'explore|general' to exclude search agents).
- **decision_it_changes**: Whether to combine Ponytail + caveman for maximum token+code reduction. Subagent injection control is useful — we may want to exclude Verdict's verification subagents from Ponytail's rules.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Both skills are local markdown/hooks.
- **actionality**: 3

## Record 6 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail development: 'node scripts/check-rule-copies.js' keeps agent copies aligned. 'npm test' runs correctness benchmark (spawns Python for email/CSV checks; needs pandas). OpenClaw skill package generated from skills/ via 'node scripts/build-openclaw-skills.js'. Publish to ClawHub: 'clawhub login' then 'node scripts/publish-openclaw-skills.js'. Agent portability map: .cursor/rules/, .windsurf/rules/, .clinerules/, .github/copilot-instructions.md, AGENTS.md, .kiro/steering/, .qoder/rules/ — copy matching file for instruction-only adapters.
- **decision_it_changes**: If we adopt Ponytail, we must keep rule copies aligned across any instruction-only adapters we use (e.g., AGENTS.md for Codex). The check-rule-copies.js script automates this.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Dev tooling is local Node.js scripts.
- **actionality**: 3

## Record 7 (from ponytail_001.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail sponsors: GreenPT. MIT license ('shortest license that works'). Star history: #1 monthly gain on GitHub trending July 2026 (35.1k stars/month), 146.7k total stars (as of ELITE_REPO_REFRESH). Trendshift daily/weekly/monthly badges show sustained velocity. The Retriever (theretriever.app) built with Ponytail.
- **decision_it_changes**: Confirms Ponytail is actively maintained, funded, and used in production (The Retriever). High velocity suggests ongoing improvements.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Sponsorship doesn't affect local usage.
- **actionality**: 3

## Record 8 (from ponytail_001.jsonl)
- **source_url**: https://x.com/GeoffreyHuntley/status/1944614322107564194
- **date**: 2025-07-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 2
- **actionability**: indirect
- **extraction**:

  Geoffrey Huntley references Ponytail in context of Ralph Wiggum loops: 'Ponytail makes your AI agent think like the laziest senior dev.' The two are complementary — Ralph provides loop orchestration, Ponytail provides code-generation discipline.
- **decision_it_changes**: Validates the combination: Ralph (loop orchestration) + Ponytail (code discipline) for Engine agent. This is our intended stack.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Social validation only.
- **actionality**: 2
