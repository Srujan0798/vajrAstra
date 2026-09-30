# composio_awesome_skills_001 (converted from composio_awesome_skills_001.jsonl - all records, fields verbatim)

## Record 1 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  ComposioHQ/awesome-claude-skills: Curated list of 1000+ production-ready Claude Skills and Plugins. 34.9k stars (per Wechat-ggGitHub/Awesome-GitHub-Repo). Covers: Document Processing (docx, pdf, pptx, xlsx, epub, legal), Development & Code Tools (artifacts-builder, aws-skills, changelog-generator, chrome-relay, connect, d3js, ffuf, finishing-branch, full-page-screenshot, great_cto, iOS simulator, jules, langsmith-fetch, lean-ctx, mcp-builder, move-code-quality, openweb, overkill, playwright, prompt-engineering, pypict, reddit-fetch, septim-agents, skill-creator, skill-seekers, software-architecture, subagent-driven-development, TDD, git-worktrees, webapp-testing), Data & Analysis, Business & Marketing, Communication & Writing, Creative & Media, Productivity & Organization, Collaboration & PM, Security & Systems, Assistive Tech, App Automation via Composio (78 SaaS apps). Apache-2.0 license.
- **decision_it_changes**:

  Whether to use this as our canonical skill discovery catalog for the campaign — finding relevant skills for OCR pipeline (pdf, docx, xlsx for doc processing; playwright for browser testing; TDD, git-worktrees for workflow; lean-ctx for token optimization).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Catalog is static markdown — zero deps. Individual skills install separately.
- **actionality**: 4

## Record 2 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Key skills for our campaign: 1) pdf/docx/pptx/xlsx (anthropics/skills) — document processing for research papers, specs. 2) playwright-skill (lackeyjb/playwright-skill) — browser automation for testing. 3) TDD (obra/superpowers) — test-driven development enforcement. 4) git-worktrees (obra/superpowers) — isolated worktrees for parallel agents. 5) lean-ctx (yvgude/lean-ctx) — MCP server + context runtime: session caching, AST-aware compression, 90+ shell patterns to reduce token usage. Supports Claude Code, Cursor, Copilot. 6) subagent-driven-development (NeoLabHQ/context-engineering-kit) — dispatch independent subagents with code review checkpoints. 7) root-cause-tracing (obra/superpowers) — trace errors to original trigger. 8) great_cto (avelikiy/great_cto) — 7 specialised subagents orchestrating full SDLC.
- **decision_it_changes**:

  Which specific skills to install from this catalog for our 3-agent ops model. lean-ctx directly competes with RTK (token reduction). great_cto's 7-subagent SDLC mirrors our Engine/Verdict/Miss but more granular.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Skills are local markdown — install only what we need.
- **actionality**: 5

## Record 3 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Composio MCP Gateway: Single MCP endpoint for 1000+ integrations with built-in auth, team access controls, audit logs, production reliability. 'connect-apps' plugin lets Claude perform real actions (send emails, create issues, post to Slack) across Gmail, Slack, GitHub, Notion, 1000+ services. Install: 'claude --plugin-dir ./connect-apps-plugin' then '/connect-apps:setup' with API key from dashboard.composio.dev. This is a CLOUD service — requires Composio account.
- **decision_it_changes**:

  DECISION: REJECT Composio MCP Gateway for our campaign. Cloud service requiring API key and paid tiers violates no-paid-keys, no-cloud-spend law. We use only local skills from the catalog, not the gateway.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Gateway is cloud SaaS — incompatible.
- **actionality**: 4

## Record 4 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- **date**: 2026-08-29
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Skill structure: Each skill is a folder with SKILL.md (YAML frontmatter: name, description) + optional scripts/, templates/, resources/. Skills load progressively: at session start, agent sees only name+description (~100 tokens/skill). Full SKILL.md body (~5000 tokens) loads only when agent decides relevant. Auxiliary files load on demand. This enables hosting hundreds of skills without context bloat. Skills ≠ MCP servers ≠ tools. MCP = access, tools = actions, skills = behavior. All three layers run together in production.
- **decision_it_changes**: Confirms skill loading is lazy — we can install many skills from this catalog without context penalty. Only relevant skills load fully.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Lazy loading is client-side behavior.
- **actionality**: 3

## Record 5 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Install methods: Claude.ai (click skill icon), Claude Code (cp to ~/.config/claude-code/skills/), API (skills parameter in messages.create). For Claude Code, skills also work via the plugin system. The catalog includes both official Anthropic skills (anthropics/skills) and community skills. Official skills repo: github.com/anthropics/skills (50+ verified).
- **decision_it_changes**: Install path for our campaign — use ECC's skill installation (which manages ~/.claude/skills/) or manual cp. ECC already manages 292 skills; we should prefer ECC's curated set over raw catalog.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Local file copy only.
- **actionality**: 3

## Record 6 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/EmbraceAGI/awesome-chatgpt-zh/blob/main/docs/Claude_Skills.md
- **date**: 2026-08-23
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Chinese community ranking: ComposioHQ/awesome-claude-skills listed as '由 Composio 维护的精选 Claude Skills 列表，涵盖技能、资源与工具'. Karanb192/awesome-claude-skills called '权威合集, 50+ 已验证技能, 覆盖 TDD、调试、Git 工作流、文档处理等, 持续维护'. VoltAgent/awesome-agent-skills: '1000+ 官方与社区 agent 技能合集, 兼容 Claude Code、Codex、Gemini CLI、Cursor 等'. Multiple competing catalogs exist.
- **decision_it_changes**: Catalog choice — ComposioHQ is largest (1000+) but Karanb192 has verified subset. For our campaign, prefer ECC's 292 curated skills (already installed) over external catalogs.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Catalog comparison is informational only.
- **actionality**: 2

## Record 7 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/CONTRIBUTING.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Contributing guidelines: Skills must be based on real use case, check for duplicates, follow structure template, test across platforms (Claude.ai, Claude Code, API), document prerequisites/dependencies, include error handling. PR process with quality standards. This ensures catalog quality but doesn't guarantee every skill works for our specific use case.
- **decision_it_changes**: Quality bar for catalog submissions — but we still need to test any skill we adopt on our 18-lang OCR workload.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Contribution process is external.
- **actionality**: 2

## Record 8 (from composio_awesome_skills_001.jsonl)
- **source_url**: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- **date**: 2026-08-29
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Community: 20,000+ developers (per README). Discord, Twitter/X, support@composio.dev. 'Join 20,000+ developers building agents that ship.' Composio platform (dashboard.composio.dev) is the commercial backend. The catalog is a lead gen funnel for Composio MCP Gateway.
- **decision_it_changes**: Catalog is marketing for Composio's paid gateway. We extract the skill list (value) and ignore the gateway pitch (cost).
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Catalog usage is free; gateway is separate.
- **actionality**: 2
