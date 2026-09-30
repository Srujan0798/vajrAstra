# graphify_001 (converted from graphify_001.jsonl - all records, fields verbatim)

## Record 1 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Graphify (Graphify-Labs/graphify) v8: Turn any folder of code, SQL schemas, docs, papers, images, videos into a queryable knowledge graph. Installed at ~/.local/bin/graphify on this laptop. Code parsed locally with tree-sitter AST (37 grammars) — deterministic, no LLM, nothing leaves machine. Docs/PDFs/images/video use assistant's model or configured API. Outputs: graph.html (interactive), GRAPH_REPORT.md, graph.json. Skills for 20+ platforms (Claude Code, Codex, Cursor, Gemini, etc.). LOCOMO recall@10: 0.497 (vs mem0 0.048, supermemory 0.149). LongMemEval-S QA accuracy: 76% (tied with dense RAG). Graph build: 0 LLM credits.
- **decision_it_changes**: Whether to adopt Graphify as our canonical knowledge graph for the Level-7 campaign corpus (PPT_SPEC, AGENTS.md, SOUTH_CANON, research docs). Replaces grep-based navigation with graph queries.
- **transfer**: SURVIVES
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Code parsing is fully local (tree-sitter). Semantic pass on docs needs LLM — can use local Ollama or our existing Claude session.

## Record 2 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/BENCHMARKS.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Graphify benchmarks: LOCOMO (n=300) recall@10 0.497 vs mem0 0.048, supermemory 0.149. LOCOMO QA accuracy 45.3% vs supermemory 49.7%, mem0 27.3%. LongMemEval-S (n=50) QA accuracy 76% tied with dense RAG. Graph build LLM credits: 0 (vs per-token for most systems). All systems ran on same harness with same model/budgets, judge blind-validated (90.6% agreement, Cohen's kappa 0.81).
- **decision_it_changes**: Validates Graphify's retrieval quality for our campaign knowledge base — 10x better recall than mem0, competitive QA accuracy with zero LLM credits for code graph building.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Benchmarks run on same hardware class; local tree-sitter parsing costs zero credits.

## Record 3 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  Graphify install: 'uv tool install graphifyy' then 'graphify install' registers skill with AI assistant. '/graphify .' builds graph. Commands: query, path, explain, add (papers/YouTube), hook install (auto-rebuild on commit), merge-graphs, prs (dashboard with CI state, review status, worktree mapping, merge-order risk via shared communities). MCP server: stdio or HTTP (shared team server). Privacy: code local, video/audio local (faster-whisper), docs/PDFs/images via configured backend.
- **decision_it_changes**: Whether to use Graphify's MCP server for shared team access to campaign knowledge graph, and hook install for auto-updates on git pull.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. MCP server can run local (stdio) or HTTP with API key. Hook install is local git hook.

## Record 4 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Graphify optional extras: pdf, office, google, video (faster-whisper + yt-dlp), mcp, neo4j, falkordb, svg, leiden (community detection), ollama (local inference), openai, gemini, anthropic, bedrock, azure, sql, postgres, dm, terraform, pascal, ocaml, commonlisp, robot, chinese. 'uv tool install graphifyy[all]' for everything. Our campaign needs: pdf, video (for research papers), mcp, leiden, ollama (local).
- **decision_it_changes**: Which Graphify extras to install for our campaign — pdf/video for research ingestion, mcp for agent access, leiden for community detection, ollama for fully local semantic extraction.
- **transfer**: SURVIVES
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. All extras install locally via uv; ollama backend enables fully offline semantic extraction.

## Record 5 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/docs/agent-portability.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Graphify supports 20+ platforms: Claude Code (hooks), Codex (AGENTS.md + hooks), OpenCode (plugin), Cursor (rules), Gemini CLI (extension), Hermes (plugin), Kimi, Pi, Factory Droid, Trae, Devin, OpenClaw, Aider, Copilot, VS Code Copilot, Kilo, Antigravity, CodeWhale, Swival, Qoder, Amp, Jules, Junie. Agent Skills cross-framework platform uses ~/.agents/skills/.
- **decision_it_changes**: Confirms Graphify skill works on our primary harness (Claude Code via hooks) and can be shared across Engine/Verdict/Miss if they use different platforms.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Platform adapters are local config files.

## Record 6 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Graphify team workflow: 'graphify-out/' gitignored by default. Share only queryable products: 'git add -f graphify-out/graph.json graphify-out/GRAPH_REPORT.md'. manifest.json portable (relative paths). Hook install sets up post-commit, post-checkout rebuilds, merge driver for graph.json. After git pull: 'graphify update .'. Alias: 'git config --global alias.gpull "!git pull && graphify update ."'.
- **decision_it_changes**: Whether to adopt Graphify's team workflow for our campaign — shared graph.json + GRAPH_REPORT.md in repo, auto-rebuild hooks, gpull alias.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Git hooks and graph sharing are fully local.

## Record 7 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Graphify YC S26 company. Early access to platform at app.graphify.com. CLI is 'graphifyy' on PyPI (double-y). Trendshift ranking shows consistent top-10 trending since July 2026. 59+ translations. Discord community active.
- **decision_it_changes**: Background context — Graphify is a funded startup (YC S26) with active development, not abandonware. Platform offers hosted graph but CLI is fully local.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. We use only the local CLI, not the hosted platform.

## Record 8 (from graphify_001.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Graphify strict mode (Claude Code): 'graphify install --project --strict' blocks first raw source read and redirects to graph, then reverts to nudge (fires at most once per session). Toggle with GRAPHIFY_HOOK_STRICT=1/0. Default install is soft nudge. This enforces graph-first querying discipline.
- **decision_it_changes**: Whether to enable Graphify strict mode for our campaign agents to enforce evidence-first querying over grep/file-read habits.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Strict mode is a local hook behavior.
