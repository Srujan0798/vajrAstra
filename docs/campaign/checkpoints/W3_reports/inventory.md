# W3 · PART 1 — TOOL INVENTORY WITH EVIDENCE OF USE (proto-30, Miss agent, 2026-09-30 Wed)

Basis: enumerated on disk 2026-09-30 16:05 IST. Evidence law: every claim cites a command run or file:line. Precursor check first: `ECC_VERIFICATION.md` and `LAYA_GATE_DECISIONS.md` — **listed as precursors by proto-30 but absent from the repo** (`find` at depth ≤2 returned nothing) — stale precursor note, not a finding against any tool.

## 1. Enumeration (commands run)

- **Claude user skills (59):** `ls ~/.claude/skills` → aim, autobahn, automate, autopilot, canvas, catchup, create-hook/rule/skill/subagent, debloat, dedash, detool, **factchk**, feynman, goal, **graphify**, hate, laya-gate, learned, loop, looper, macrothink, **mandela**, migrate-to-skills, modelchk, nba, new-repo, omi, onboard, origin, prism, re0* (10), readchk, rename-chat, reorder, review, review-bugbot, review-security, sdk, share, shell, shower, sip, split-to-prs, ssotize, statusline, synced, update-cli-config, update-cursor-settings.
- **Claude plugins (15 enabled, `~/.claude/settings.json` → `enabledPlugins`):** context7, superpowers, feature-dev, security-guidance, skill-creator, pr-review-toolkit, session-report, pydantic-ai, data-engineering, semgrep, frontend-design, playwright, ralph-loop, vercel, ecc@ecc. Cache: `ls ~/.claude/plugins/cache/` → claude-plugins-official (14 plugins) + ecc/2.2.2. Plugin skills also live under `~/.claude/plugins/synced/...` (documentation, incident-response, code-review, tech-debt, standup, architecture, testing-strategy, deploy-checklist, system-design, debug; data-engineering: write-query, validate-data, sql-queries, build-dashboard, explore-data, statistical-analysis; searchfit-seo ×10; UX set: user-research, research-synthesis, ux-copy, design-handoff, design-critique, accessibility-review, design-system; desktop-commander ×6).
  Note: the protocol's `find ~/.claude/plugins/cache -maxdepth 5 -name SKILL.md` returned **empty** (skills sit deeper / under synced) — enumeration done by directory instead.
- **MCP servers (50 entries, `claude mcp list` 2026-09-30 16:05):**
  - ✔ Connected (14 usable): Claude Docs, Google Drive, Gmail, Google Calendar, Notion, context7, semgrep-guardian (hook), playwright, vercel, chrome-devtools, omi-memory, opencode, github (`~/.local/bin/github-mcp-bridge`), ecc-memory (fixed path `.../ecc/2.2.2/scripts/memory-mcp.mjs`).
  - ! Needs auth (14): PostHog, Linear ×2, engineering-slack, engineering-atlassian, engineering-notion, datadog, monday, clickup, figma, intercom, hex, amplitude ×2, **hf-mcp-server**.
  - ✘ Failed (7): engineering-asana, engineering-github, engineering-pagerduty, desktop-commander (CONNECTION_CLOSED), bigquery, definite, (plugin:design/productivity google cal/gmail "Not configured" ×6).
- **OpenCode:** 217 skills (`ls ~/.config/opencode/skills | wc -l` = 217), 2 agents (local.md, notools.md), ~100 commands (aside.md … verify.md, incl. checkpoint.md, build-fix.md, code-review.md, epic-*, orch-*, prp-*, multi-*).
- **Elite repos (`INTEGRATED-ELITE-STACK.md`):** 11 INSTALLED/keep (paperthin, looper, graphify, ECC, ralph-wiggum ref, claude-mem, rtk, browser-use, hermes-agent, awesome-claude-skills, deepseek-harness); 11 keep-for-W6 (GLM-OCR, mlx-tune, liteparse, dots.mocr, MonkeyOCRv2, HunyuanOCR-1.5, Unlimited-OCR, light-ocr, anydoc, lift, TencentDB-Agent-Memory); ~15 watch-only.

## 2. Evidence of use — spot checks

Session-jsonl grep (`~/.claude/projects/-Users-srujansai-Desktop-South/*.jsonl`, pattern `"skill":"<name>"`): **mandela: 2 · factchk: 2 · graphify: 2** · verification-loop: 0 · ssotize: 0 · unified-memory: 0 · council: 0 · loop-design-check: 0 · living-docs-governance: 0 · terminal-ops: 0 · research-ops: 0 · market-research: 0 · sip: 0.
Repo grep (`DISPATCH_LOG.md`): graphify rebuild DONE `DISPATCH_LOG.md:115` (3,990 nodes / 4,681 edges / 420 communities; `graphify-out/graph.json` exists, 6.6 MB); factchk named as Verdict's checker `DISPATCH_LOG.md:312`; audit/archive row `DISPATCH_LOG.md:24`; corpus row referencing LIVE_LATEST + graphify-out `DISPATCH_LOG.md:168`. No DISPATCH_LOG hits for hate, catchup, santa-method, scholar-evaluation, omi, `npx skills`, ecc-memory. `PAPERTHIN_AUDIT.md` exists at root (8 mandela findings per AGENTS.md). Live research used web tools: `LIVE_LATEST_2026-09-29.md` "(41 sources)" (AGENTS.md).

## 3. Step map (IDs from CAMPAIGN_DIRECTIVE.md:219–292: 1A audit · 1B benchmark table · 1C mentor playbook · 1D competitor intel · 1E edge thesis · 1F multi-LLM eval · 1G apply+re-verify · 1H draft plan · W2 manifest · W3 this + Laya/JEV · W4 corpus · W5 freeze)

## 4. Inventory table

| Item | Source | What it does | Step | Evidence of use | Status |
|---|---|---|---|---|---|
| graphify | Claude skill + `~/.local/bin/graphify` | codebase→knowledge-graph, query/path/explain | W3, W4, W5 | DISPATCH_LOG.md:115; graph.json 6.6 MB; jsonl 2 | **USED** — but graph STALE (bootstrap: 35 md changed since build) |
| factchk | Claude skill (paperthin) | two-way source verification | 1A, 1D, 1E, 1G | jsonl 2; DISPATCH_LOG.md:312; INTEGRATED-ELITE-STACK.md:64 | **USED** |
| mandela | Claude skill (paperthin) | 8-pattern eval-leakage audit | 1A, W3 (proto-31 JEV), W5 call | jsonl 2; PAPERTHIN_AUDIT.md; INTEGRATED-ELITE-STACK.md | **USED** |
| paperthin suite (catchup, nba, hate, sip) | Claude skill | context recovery, next action, kill-objection, self-check | every step re-entry; 1E, 1F | INTEGRATED-ELITE-STACK.md "Where each INSTALLED tool plugs in"; 0 jsonl/DISPATCH hits | **SHOULD-USE** (1E hate before backbone pick; catchup+nba before each dispatch) |
| verification-loop | OpenCode (ECC) | verify-before-claiming loop | 1G, every close-out | jsonl 0; named as mandatory in AGENTS.md standing law | **SHOULD-USE** (1G re-verify of 1A fixes) |
| unified-memory | OpenCode (ECC) | cross-agent handoffs via Memory Vault | W3, W4 | jsonl 0; INTEGRATED-ELITE-STACK.md ECC section | **SHOULD-USE** (Engine→Verdict→Miss handoffs) |
| council | OpenCode (ECC) | multi-voice tradeoff deliberation | 1F, U4 decision | jsonl 0; INTEGRATED-ELITE-STACK.md | **SHOULD-USE** (U4: Option A vs D, Qwen2.5-VL-3B vs GLM-OCR) |
| loop-design-check | OpenCode (ECC) | design-review for new agent loops | W3 (proto-98 memory phases), W6 | jsonl 0; AGENTS.md names it | **SHOULD-USE** |
| living-docs-governance | OpenCode (ECC) | anti-doc-rot governance | W3, W5 | jsonl 0; 43-file weekday error sweep (CAMPAIGN_DIRECTIVE.md A1) | **SHOULD-USE** |
| ssotize | Claude skill (paperthin) | consolidate scattered facts into one SSOT | 1G, 1H | jsonl 0; K1–K7 conflicts scattered (CAMPAIGN_DIRECTIVE.md A3) | **SHOULD-USE** |
| santa-method / scholar-evaluation | OpenCode (ECC) | adversarial two-pass review; evidence-quality rubric | 1A, 1G | INTEGRATED-ELITE-STACK.md; 0 jsonl hits | **SHOULD-USE** |
| context7 MCP | Claude plugin | current library docs | 1D, 1E, W6 (mlx-tune/GLM-OCR docs) | connected (claude mcp list); prompts reference it | **USED** |
| parallel-search MCP | OpenCode MCP | multi-query web search | 1D, 1E, W4 | LIVE_LATEST_2026-09-29.md (41 sources, AGENTS.md) | **USED** |
| github MCP | Claude (`github-mcp-bridge`) | repo/issue/PR ops | 1D, W6 (weight sha256 verification) | connected (claude mcp list) | **USED** |
| ecc-memory MCP | Claude plugin | persistent memory store | all steps | connected (claude mcp list, fixed path per proto-30:23); 0 DISPATCH mentions | **SHOULD-USE** (persist boss approvals U1–U32) |
| omi-memory MCP + omi skill | Claude | boss's live history/commitments | 1F, call prep | connected (claude mcp list) | **SHOULD-USE** (meeting-prep context) |
| hf-mcp-server | Claude (remote) | HF hub MCP: model/dataset lookup | W6, Bodhan downloads | "Needs authentication" (claude mcp list); U26 approved HF MCP (bootstrap NEXT.md) | **SHOULD-USE** — authenticate, then U26 downloads with sha256 into DISPATCH_LOG.md |
| Gmail / Calendar / Drive / Notion MCPs | Claude | email, schedule, docs | 1F (call scheduling), 1C | connected (claude mcp list) | **SHOULD-USE** (Vinay meeting scheduling only; never in the OCR model — U31) |
| semgrep-guardian MCP | Claude plugin | code security scanning | W5 (pre-freeze audit) | connected (claude mcp list) | **SHOULD-USE** (W5 security audit) |
| playwright MCP | Claude plugin | browser automation | 1D (competitor recon), ui-demo | connected (claude mcp list) | **SHOULD-USE** (1D recon) |
| opencode MCP | Claude | drive OpenCode from Claude | all waves | connected (claude mcp list) | **USED** (agent processes logged, DISPATCH_LOG.md:168 context) |
| claude-mem, rtk, browser-use, hermes-agent, awesome-claude-skills, deepseek-harness, ralph-wiggum | INTEGRATED-ELITE-STACK.md keep-as-reference | reference repos, not installed | none (watch) | INTEGRATED-ELITE-STACK.md install table | **IRRELEVANT** — reference-only by design (rtk has a registered CONTRADICTION) |
| GLM-OCR, mlx-tune, liteparse, dots.mocr, MonkeyOCRv2, HunyuanOCR-1.5, Unlimited-OCR, light-ocr, anydoc, lift | INTEGRATED-ELITE-STACK.md keep-for-W6 | W6 OCR stack, clone required | none until W6 freeze (~Oct 1) | INTEGRATED-ELITE-STACK.md "When to install: At W6 freeze"; PART A7/§A8 | **IRRELEVANT (now)** — W6 targets; clone only at freeze with boss yes |
| Failed MCPs (asana, engineering-github, pagerduty, desktop-commander, bigquery, definite) | Claude plugins | various | none | "✘ Failed to connect" (claude mcp list) | **BROKEN** (6) — auth incompatible / connection closed; not campaign-relevant |
| Auth-pending MCPs (PostHog, Linear ×2, slack, atlassian, engineering-notion, datadog, monday, clickup, figma, intercom, hex, amplitude ×2) | Claude plugins | SaaS integrations | none | "! Needs authentication" (claude mcp list) | **IRRELEVANT** — no campaign step; auth only if boss asks |
| searchfit-seo ×10, UX set ×7, engineering plugins (feature-dev, pr-review-toolkit, frontend-design, data-engineering, pydantic-ai, session-report, superpowers, ralph-loop, skill-creator, security-guidance) | Claude plugins | web/UX/app-dev skills | none | INTEGRATED-ELITE-STACK.md; campaign scope is OCR research | **IRRELEVANT** — out of campaign scope |
| OpenCode bulk (217 skills): brand/marketing family (brand-discovery, brand-voice, content-engine, crosspost, lead-intelligence, seo, social-*), homelab family (7), healthcare family (6), finance family (5), supply-chain family (5), security-language family (django/laravel/springboot/quarkus/perl/jpa/mysql/postgres/redis/prisma/k8s/docker/clickhouse…), frontend/backend framework family (react/vue/vue-review commands, nextjs, swift/ios family ×8), video family (remotion, manim, taste, fal-ai-media, video-editing, videodb), prediction-market family (4), ito family (4), persona/ops novelty (openclaw-persona-forge, nasiko, nanoclaw-repl), scientific family (pubmed, uspto, gget, literature-review, scholar-evaluation) | OpenCode | domain codifications | none (scholar-evaluation excepted) | family enumeration from `ls ~/.config/opencode/skills` | **IRRELEVANT** — outside OCR-campaign scope (scholar-evaluation → SHOULD-USE, 1A/1E) |
| OpenCode commands (~100) | OpenCode | workflow entry points | W3+ | checkpoint.md, build-fix.md, code-review.md, verify.md match campaign verbs | **SHOULD-USE** (checkpoint.md for wave close-outs) |
| ECC group (remaining ~120: config-gc, configure-ecc, ecc-guide, ecc-recipes, skill-* family, cost/eval/agent-ops family, orch-* family, blueprint, continuous-*, delivery-gate, gateguard, knowledge-ops…) | OpenCode (ECC) | agent-harness discipline | W3–W6 as named | AGENTS.md standing law names a subset | **SHOULD-USE** where named (skill-stocktake for this inventory class, gateguard for write discipline) |

## 5. Top 10 tools we should be using and are not

1. **verification-loop** (OpenCode/ECC) → **1G** (and every close-out). How: run it before a wave is declared done; re-verify Miss-applied 1A fixes with a reproducing command. Evidence of non-use: jsonl count 0; AGENTS.md makes it mandatory.
2. **unified-memory** (OpenCode/ECC) → **W3/W4**. How: persist Engine→Verdict→Miss handoffs and boss approvals U1–U32 to the Memory Vault instead of re-pasting context blocks. jsonl 0.
3. **council** (OpenCode/ECC) → **1F**. How: multi-voice deliberation on U4 (Option A vs D; Qwen2.5-VL-3B vs GLM-OCR 0.9B) before the Vinay packet presents only Option A (CAMPAIGN_DIRECTIVE.md A3-K4/K5). jsonl 0.
4. **ssotize** (Claude/paperthin) → **1G/1H**. How: consolidate the K1–K7 scattered conflicts (dates, backbone, kok gap 0.32 vs 0.194, 1,227 vs 1,283) into one canonical statement, then replace the rest with references. Read-only first; mutates only with boss approval. jsonl 0.
5. **living-docs-governance** (OpenCode/ECC) → **W3/W5**. How: assign campaign docs clear roles and sweep the 43-file weekday-date error (CAMPAIGN_DIRECTIVE.md A1) under one rule. jsonl 0.
6. **graphify --update** → **W3 Phase 1 (now)**. How: bootstrap says the graph is STALE (35 md changed since build); run `graphify --update` before using graphify-out for navigation. (graphify itself is USED — the update is the gap.)
7. **hf-mcp-server** → **W6 Day 1 / Bodhan**. How: authenticate (currently "! Needs authentication"), then the U26-approved HF downloads with revisions + sha256 into DISPATCH_LOG.md. Cannot download without the boss's yes — U26 is in.
8. **santa-method** (OpenCode/ECC) → **1A/1G**. How: two independent adversarial passes on the packet fix-specs before they ship (Verdict re-verify round). 0 jsonl hits.
9. **catchup + nba** (Claude/paperthin) → **every dispatch re-entry**. How: before each wave, rebuild the owner's map and return the single next action; INTEGRATED-ELITE-STACK.md explicitly recommends both. 0 jsonl/DISPATCH hits.
10. **ecc-memory MCP** → **all steps**. How: connected and fixed (proto-30:23) but 0 DISPATCH_LOG mentions — persist decisions, checkpoints, and open boss approvals so no session re-asks settled questions.

## Verdict check note

Sampled rows above carry citations that exist: DISPATCH_LOG.md:24,115,168,312; graphify-out/graph.json (6.6 MB, `du -sh`); jsonl counts via the grep loop; claude mcp list statuses quoted verbatim; CAMPAIGN_DIRECTIVE.md:219–292 step IDs; INTEGRATED-ELITE-STACK.md:3,64 and its install tables. `ECC_VERIFICATION.md` / `LAYA_GATE_DECISIONS.md` / `docs/campaign/SKILL_STACK.md` are absent (`ls` errors reproduced) — SKILL_STACK.md is the lead's compose target.
