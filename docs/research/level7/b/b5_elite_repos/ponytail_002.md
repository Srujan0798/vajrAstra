# ponytail_002 (converted from ponytail_002.jsonl - all records, fields verbatim)

## Record 1 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Ponytail commands for Verdict agent: /ponytail-review (review current diff for over-engineering, hands back delete-list), /ponytail-audit (audit whole repo for over-engineering), /ponytail-debt (harvest deferred 'ponytail:' shortcuts into ledger), /ponytail-gain (show measured impact scoreboard). These are perfect for Verdict's verification gate — review Engine's output for over-engineering before commit.
- **decision_it_changes**: Integrate /ponytail-review into Verdict agent's mandatory review step. /ponytail-audit for periodic whole-repo sweeps before W5 freeze.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Commands are skill invocations — local.

## Record 2 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail intensity levels: 'lite' (minimal enforcement), 'full' (default, balanced), 'ultra' (maximum YAGNI, for when codebase has wronged you personally), 'off' (disabled). Set default with PONYTAIL_DEFAULT_MODE env var or ~/.config/ponytail/config.json. Subagent injection controlled by PONYTAIL_SUBAGENT_MATCHER regex (e.g., 'explore|general' to exclude search agents). Startup/mode-change text shows current mode.
- **decision_it_changes**: Use 'full' for Engine agent, 'ultra' for Verdict's review pass, 'off' for Miss's monitoring (where verbosity is OK). Exclude Verdict's verification subagents from Ponytail via SUBAGENT_MATCHER.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Config is local file/env var.
- **actionality**: 3

## Record 3 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail Cursor install: 'git clone && node ponytail/scripts/cursor-hooks.js install' merges two native hooks into ~/.cursor/hooks.json (add --project for project-level). Keeps existing hooks. Cursor reloads on save; ruleset arrives through sessionStart. Send '/ponytail lite|full|ultra|off' as plain message to switch level. Limitations: subagentStart cannot inject context (subagents run without ruleset), cloud agents never fire sessionStart. Rule-only alternative: copy .cursor/rules/ponytail.mdc (alwaysApply: true).
- **decision_it_changes**: Not directly relevant (we use Claude Code), but shows Ponytail's hook architecture for subagent injection control.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Hook behavior is platform-specific.
- **actionality**: 3

## Record 4 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail instruction-only adapters (no plugin): Cursor (.cursor/rules/ponytail.mdc), Windsurf (.windsurf/rules/), Cline (.clinerules/), GitHub Copilot Chat (.github/copilot-instructions.md), Kiro (.kiro/steering/), Qoder (.qoder/rules/), Aider, Zed, CodeWhale, Swival. These load always-on ruleset without commands/hooks. Amp (Sourcegraph) reads AGENTS.md from working directory and parents up to $HOME. Jules (Google) reads AGENTS.md from repo root. JetBrains Junie: point to AGENTS.md in settings.
- **decision_it_changes**: If any of our agents use these platforms, copy the matching rules file. For our Claude Code + ECC setup, use the native plugin.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Rule files are local markdown.
- **actionality**: 3

## Record 5 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/examples/
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Ponytail examples/ directory: More survivors showing before/after. Date picker: 404 lines → 23 lines (native <input type=date>). Color picker: 287 lines → 23 lines (native <input type=color>). These demonstrate the ladder rungs 3-4 (stdlib/native platform feature) in action. The examples are the best documentation of the ladder's real-world impact.
- **decision_it_changes**: Study examples/ for patterns applicable to our OCR pipeline UI (if any) — native HTML elements over custom components.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Examples are static code.
- **actionality**: 3

## Record 6 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/scripts/check-rule-copies.js
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Ponytail check-rule-copies.js: Keeps agent rule copies aligned when changing compact rule text. Run 'node scripts/check-rule-copies.js' and 'npm test' after rule changes. OpenClaw skill package generated from skills/ via 'node scripts/build-openclaw-skills.js'. Test suite fails if stale. This ensures consistency across 20+ platform adapters.
- **decision_it_changes**: If we customize Ponytail rules for our campaign, run check-rule-copies.js to propagate to any instruction-only adapters we use (e.g., AGENTS.md for Codex).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Local Node.js script.
- **actionality**: 2

## Record 7 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Ponytail FAQ: 'Can I use it with caveman?' Yes — caveman shrinks what agent SAYS; ponytail shrinks what it BUILDS. Different halves, no overlap. 'Terse talk about minimal code.' 'Does it need a config file?' No — optional ~/.config/ponytail/config.json or PONYTAIL_DEFAULT_MODE. 'What if I really need the 120-line cache class?' You don't. Insist anyway and he'll build it. Slowly. Correctly. While looking at you. 'Does it scale?' The code you never wrote scales infinitely. Zero bugs, zero CVEs, 100% uptime since forever.
- **decision_it_changes**: Philosophy alignment: Ponytail's 'code you never wrote' = our 'do not invent a novel backbone'. The cache class example = our weak cell temptation (custom Ol Chiki/Nastaliq models).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Philosophy match is exact.
- **actionality**: 2

## Record 8 (from ponytail_002.jsonl)
- **source_url**: https://github.com/DietrichGebert/ponytail/blob/main/README.md
- **date**: 2026-08-30
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Ponytail sponsor: GreenPT. MIT license ('shortest license that works'). Star history: #1 monthly gain on GitHub trending July 2026 (35.1k stars/month), 146.7k total stars. Trendshift daily/weekly/monthly badges show sustained velocity. The Retriever (theretriever.app) built with Ponytail — production proof.
- **decision_it_changes**: High velocity + production use (The Retriever) = low abandonment risk. MIT license = no legal friction. Sponsor (GreenPT) doesn't affect local usage.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Sponsorship is passive.
- **actionality**: 2
