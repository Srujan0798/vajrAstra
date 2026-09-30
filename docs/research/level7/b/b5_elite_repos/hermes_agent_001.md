# hermes_agent_001 (converted from hermes_agent_001.jsonl - all records, fields verbatim)

## Record 1 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/NousResearch/hermes-agent
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Hermes Agent (NousResearch/hermes-agent): Self-improving AI agent with built-in learning loop. Creates skills from experience, improves them during use, nudges itself to persist knowledge, searches past conversations, builds user model across sessions. Runs on $5 VPS, GPU cluster, or serverless (Daytona, Modal — hibernates when idle, costs nearly nothing). Model-agnostic: Nous Portal, OpenRouter, OpenAI, custom endpoint. Switch with 'hermes model'. Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, streaming tool output. Lives on Telegram, Discord, Slack, WhatsApp, Signal, CLI — single gateway process. Voice memo transcription, cross-platform continuity. Closed learning loop: agent-curated memory, periodic nudges, autonomous skill creation, skill self-improvement, FTS5 session search with LLM summarization, Honcho dialectic user modeling. Compatible with agentskills.io open standard. Scheduled automations (cron). Delegates and parallelizes (subagents, Python scripts via RPC). 7 terminal backends: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox. Research-ready: batch trajectory generation, trajectory compression for training next-gen tool-calling models. MIT license.
- **decision_it_changes**:

  Whether to adopt Hermes as an alternative harness for our 3-agent ops model — especially the built-in learning loop (autonomous skill creation + self-improvement) which matches our continuous-learning-v2 law. But Hermes is a full agent runtime, not a skill/plugin for Claude Code.
- **transfer**: UNKNOWN
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Hermes requires its own runtime (Python/Node) and model API keys. Can run local models but needs GPU for meaningful throughput. Serverless (Daytona/Modal) costs money — violates no-paid-keys.
- **actionality**: 4

## Record 2 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/NousResearch/hermes-agent/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Hermes install: Linux/macOS/WSL2: 'curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash'. Windows native (PowerShell): 'iex (irm https://hermes-agent.nousresearch.com/install.ps1)'. Delegates Python 3.14, Node.js, npm, ripgrep, FFmpeg, Python deps to PM (package manager). Android/Termux: signed APT repo (stable/canary). After install: 'source ~/.bashrc' then 'hermes'. Troubleshooting: Windows Defender may flag uv.exe (Astral's Rust pkg manager) — false positive, verify with gh attestation.
- **decision_it_changes**: Install complexity — Hermes is a separate CLI tool with its own dependency chain (Python 3.14, Node, uv). Not a drop-in for our Claude Code-based campaign.
- **transfer**: DIES
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Heavy install footprint; requires model API keys (Nous Portal, OpenRouter, etc.) — violates no-paid-keys.
- **actionality**: 4

## Record 3 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/NousResearch/hermes-agent/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Hermes Nous Portal: 300+ models under one subscription, Tool Gateway (web search, FAL image gen, OpenAI TTS, Browser Use cloud browser) all routed through sub. 'hermes setup --portal' logs in via OAuth, sets Nous as provider, turns on Tool Gateway. Can still bring own keys per-tool. This is a PAID subscription service.
- **decision_it_changes**: DECISION: REJECT Nous Portal. Paid subscription with cloud tool gateway violates no-paid-keys, no-cloud-spend law.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Portal is cloud SaaS.
- **actionality**: 3

## Record 4 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/NousResearch/hermes-agent/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Hermes OpenClaw migration: 'hermes claw migrate' imports SOUL.md, memories, skills, command allowlist, messaging settings, API keys, TTS assets, AGENTS.md. Interactive or --dry-run. Skills imported to ~/.hermes/skills/openclaw-imports/. This shows Hermes treats OpenClaw as a peer, not a dependency.
- **decision_it_changes**: Not directly relevant — we don't use OpenClaw. But shows Hermes's skill/memory portability.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Migration is local file copy.
- **actionality**: 3

## Record 5 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/Yonkoo11/hermes-dojo
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 3
- **recency**: 4
- **actionability**: theoretical
- **extraction**:

  Hermes Dojo (Yonkoo11/hermes-dojo): Self-improvement system for Hermes Agent that watches performance, finds weakest skills, fixes them with self-evolution, shows results. Requires Hermes Agent v0.2.0+, Python 3.10+. This is a meta-learning layer ON TOP of Hermes's built-in learning loop.
- **decision_it_changes**: Interesting pattern: external self-improvement system for an already self-improving agent. But adds another moving part. Our ECC continuous-learning-v2 is simpler (hook-based instinct extraction).
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Dojo requires Hermes + Python — extra complexity.
- **actionality**: 3

## Record 6 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/SebastianElvis/clawpier
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  ClawPier (SebastianElvis/clawpier): Native desktop app for managing OpenClaw and Hermes Agent instances inside Docker containers — sandboxed from host. Cites CVE-2026-25253 (CVSS 8.8): prompt injection gives attacker your machine. Runs on macOS, Linux, Windows. This validates the sandbox requirement Ralph/Hermes both emphasize.
- **decision_it_changes**: Confirms sandbox-isolated execution is critical for agent runtimes with system access. Our Engine agent runs in Docker/Fly/E2B sandboxes per Ralph's protection principle.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Sandbox is local Docker — no cloud cost.
- **actionality**: 2

## Record 7 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/lout33/symbiotic-ai
- **date**: 2026-08-15
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Symbiotic AI (lout33/symbiotic-ai): Compares Hermes Agent vs OpenClaw. Hermes: put AGENTS.md, USER.md, NOW.md in workspace; optionally copy SOUL.md to ~/.hermes/SOUL.md; run 'hermes' from workspace root. Full agent runtime: tools, memory, web, code execution, automation. OpenClaw: set workspace in ~/.openclaw/openclaw.json; HEARTBEAT, Telegram, scheduled check-ins.
- **decision_it_changes**: Hermes workspace model (AGENTS.md + USER.md + NOW.md) is similar to our ECC memory files. But Hermes is a separate runtime, not a Claude Code plugin.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Hermes replaces Claude Code; we're committed to Claude Code + ECC.
- **actionality**: 2

## Record 8 (from hermes_agent_001.jsonl)
- **source_url**: https://github.com/EmbraceAGI/Awesome-AGI/blob/main/README.md
- **date**: 2026-08-20
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Awesome-AGI ranking: Hermes Agent listed alongside Claude Code, OpenAI Codex, deepseek-harness (dsh), Grok Build, OpenHands, OpenClaw, OpenWorker, MetaGPT. No star count shown for Hermes (badgen.net badge). deepseek-harness has explicit plugin ecosystem (awesome-dsh-plugin). Hermes appears to be smaller ecosystem.
- **decision_it_changes**: Ecosystem size matters for skill/tool availability. Hermes has smaller plugin ecosystem than deepseek-harness or ECC. Not a primary candidate for our harness.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Smaller ecosystem = fewer ready-made skills for our OCR tasks.
- **actionality**: 2
