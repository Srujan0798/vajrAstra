# graphify_002 (converted from graphify_002.jsonl - all records, fields verbatim)

## Record 1 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Graphify code-only extraction: 'graphify extract --code-only' indexes only code via tree-sitter AST, no API key needed, fully offline. On mixed repo, this skips docs/PDFs/images that would need LLM. This is our primary mode for campaign codebase (PPT_SPEC, AGENTS.md, skills, scripts) — zero cost, zero cloud.
- **decision_it_changes**: Use --code-only for initial campaign graph build. Add docs/pdf later with local Ollama backend if needed.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Code-only = fully local, zero credits.
- **actionality**: 5

## Record 2 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Graphify wiki export: '/graphify . --wiki' builds agent-crawlable markdown wiki from graph. Useful for creating searchable documentation from our campaign corpus. Obsidian export: '/graphify . --obsidian' generates Obsidian vault (never overwrites existing notes/.obsidian config). Can write into existing vault with --obsidian-dir.
- **decision_it_changes**: Generate wiki export for human-readable campaign documentation. Obsidian export for personal knowledge management.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Export is local file generation.
- **actionality**: 4

## Record 3 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Graphify PR dashboard: 'graphify prs' shows CI state, review status, worktree mapping. 'graphify prs 42' deep dive on PR #42 with graph impact. 'graphify prs --triage' AI ranks review queue (uses configured backend). 'graphify prs --conflicts' shows PRs sharing graph communities — merge-order risk. This is valuable for our Engine agent's PR workflow.
- **decision_it_changes**: Integrate graphify prs into Engine agent's commit/push workflow for automated PR impact analysis.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. PR analysis uses local graph + GitHub API (free tier).
- **actionality**: 4

## Record 4 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Graphify merge-graphs: 'graphify merge-graphs a.json b.json' combines two graphs. Useful for merging Engine's build graph with Verdict's verification graph + Miss's monitoring graph into unified campaign graph.
- **decision_it_changes**: Use merge-graphs to create unified campaign knowledge graph from three agent graphs.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Local JSON merge.
- **actionality**: 3

## Record 5 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Graphify callflow export: 'graphify export callflow-html' generates Mermaid architecture/call-flow HTML, auto-regenerates on every git commit if hook installed. This provides living architecture diagrams for our PPT_SPEC.
- **decision_it_changes**: Enable callflow export hook for living architecture diagrams in campaign docs.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Mermaid HTML is local.
- **actionality**: 3

## Record 6 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Graphify .graphifyignore: same syntax as .gitignore, merged with .gitignore (graphifyignore wins on conflicts). .gitignore respected automatically. Subdirectory scoping works like git. '--no-gitignore' disables gitignore for generated/transpiled code that belongs in graph. This prevents polluting graph with build artifacts.
- **decision_it_changes**: Add .graphifyignore for our campaign: ignore node_modules/, dist/, *.generated.py, level2/out/, level2/reports/ (sealed dirs per AGENTS.md).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Ignore file is local.
- **actionality**: 3

## Record 7 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Graphify privacy: Video/audio transcribed locally with faster-whisper (nothing leaves machine). Docs/PDFs/images sent to AI assistant for semantic extraction (via /graphify skill, using IDE session model). Headless extract needs API key. Data residency: auto-detects provider by key priority (Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). For code with data-residency requirements: --backend ollama (fully local) or explicit --backend. Kimi routes to China servers.
- **decision_it_changes**: Use --backend ollama for any semantic extraction to keep data local. Avoid Kimi backend (China routing). Our campaign uses local Ollama on M2 Max.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Ollama backend is fully local.
- **actionality**: 2

## Record 8 (from graphify_002.jsonl)
- **source_url**: https://github.com/Graphify-Labs/graphify/blob/main/README.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Graphify troubleshooting: 'graphify: command not found' → run 'uv tool update-shell' or 'pipx ensurepath'. 'uvx graphify' fails → use 'uvx --from graphifyy graphify'. 'python -m graphify' works but command doesn't → PATH issue. PowerShell: use 'graphify .' not '/graphify .'. Graph has fewer nodes after update → pass --force. Extract exits with 'extraction incomplete' → fix failure or --allow-partial. Ghost duplicates (pre-v0.8.33) → full re-extract. Ollama OOM → reduce GRAPHIFY_OLLAMA_NUM_CTX. LLM JSON truncated → raise GRAPHIFY_MAX_OUTPUT_TOKENS or lower --token-budget. HTML too large (>5000 nodes) → use --no-viz. Graph.json conflicts → hook install sets up merge driver.
- **decision_it_changes**: Operational knowledge for running Graphify reliably in campaign. Key: use uv tool install, --code-only for code, --no-viz for large graphs, hook install for auto-merge.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. All troubleshooting is local config.
- **actionality**: 2
