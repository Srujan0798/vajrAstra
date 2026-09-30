# SKILL_STACK — Wave 3 (D10) · 2026-09-30 Wed

**Lead:** orchestrator (composes from the W3 inventory + proto-31's DECIDED ruling) · **Protocol:** proto-30 (inventory) + proto-31 (Laya/JEV) · **Full inventory:** `docs/campaign/checkpoints/W3_reports/inventory.md` (~420 rows, evidence-cited)
**Evidence law:** every claim cites a command or file:line. No fake claims. Laya/JEV ruled per proto-31 — DECIDED, evidence-verified.

---

## 1. Summary — counts by status

| Status | Count | Notes |
|---|---|---|
| **USED** | 6 | graphify (graph STALE — 35 md changed since build, `--update` pending), factchk, mandela, context7 MCP, parallel-search MCP, github/opencode MCPs |
| **SHOULD-USE** | ~30 named | top-10 below, with the exact step and how |
| **IRRELEVANT** | bulk of ~380 | out-of-scope OpenCode/plugin families (brand/marketing, homelab, healthcare, finance, supply-chain, framework, video, prediction-market, ito, persona), SaaS MCPs pending auth (14), keep-as-reference repos, W6-future repos (clone only at W6 freeze with boss yes) |
| **BROKEN** | 6 | engineering-asana, engineering-github, pagerduty, desktop-commander, bigquery, definite — "✘ Failed to connect" (`claude mcp list`, 2026-09-30 16:05) |

**Enumeration basis (2026-09-30 16:05 IST):** 59 Claude user skills · 15 enabled Claude plugins (+cache claude-plugins-official ×14 + ecc/2.2.2; skills under `~/.claude/plugins/synced/...`) · 50 MCP entries (14 connected / 14 auth-pending / 7 failed) · 217 OpenCode skills · 2 OpenCode agents · ~100 OpenCode commands · 11+11+~15 elite repos (INSTALLED / keep-for-W6 / watch) per `INTEGRATED-ELITE-STACK.md`.

## 2. Top 10 tools we should be using and are not

1. **verification-loop** (ECC) → **1G + every close-out.** How: run before a wave is declared done; re-verify Miss-applied fixes with a reproducing command. Non-use evidence: session-jsonl count 0; AGENTS.md makes it mandatory.
2. **unified-memory** (ECC) → **W3/W4.** How: persist Engine→Verdict→Miss handoffs + boss approvals U1–U32 to the Memory Vault instead of re-pasting context blocks. jsonl 0.
3. **council** (ECC) → **1F/U4.** How: multi-voice deliberation on Option A vs D and Qwen2.5-VL-3B vs GLM-OCR before the packet presents only one. jsonl 0.
4. **ssotize** (paperthin) → **1G/1H.** How: consolidate the K1–K7 scattered conflicts (dates, backbone, kok gap, 1,227 vs 1,283) into one canonical statement; read-only first, mutates only with boss approval. jsonl 0.
5. **living-docs-governance** (ECC) → **W3/W5.** How: assign campaign docs clear roles; sweep the 43-file weekday error under one rule. jsonl 0.
6. **graphify --update** → **W3 Phase 1 (now).** How: bootstrap says the graph is STALE; run `graphify --update` before using graphify-out for navigation.
7. **hf-mcp-server** → **W6/Bodhan Day 1.** How: authenticate ("! Needs authentication"), then the U26-approved HF downloads with revisions + sha256 into DISPATCH_LOG.md. Currently AUTH-BLOCKED — the boss's HF token is the gate (NEXT.md §7).
8. **santa-method** (ECC) → **1A/1G.** How: two independent adversarial passes on fix-specs before they ship. 0 jsonl hits.
9. **catchup + nba** (paperthin) → **every dispatch re-entry.** How: before each wave, rebuild the owner's map + return the single next action. 0 jsonl/DISPATCH hits.
10. **ecc-memory MCP** → **all steps.** How: connected + fixed (proto-30:23) but 0 DISPATCH_LOG mentions — persist decisions, checkpoints, open approvals so no session re-asks settled questions.

## 3. Per-step tool map (only tools that exist in the inventory)

| Step | Tools |
|---|---|
| 1A audit / 1G apply+re-verify | factchk, mandela, verification-loop, santa-method, scholar-evaluation, ssotize |
| 1B benchmark | (W2 tools) + reconcile_22.py / variance_22.py |
| 1C mentor playbook | Gmail/Calendar MCP (scheduling only — never in the OCR model, U31), omi-memory |
| 1D competitor intel / 1E edge | parallel-search MCP, context7 MCP, playwright MCP, github MCP |
| 1F multi-LLM eval | council, opencode MCP, CHATGPT_EVAL_PROMPT.md (boss pastes) |
| W2 sampling | reconcile_22.py, variance_22.py, candidates/<code>.json |
| W3 this wave | skill-stocktake (this inventory class), checkpoint.md command |
| W4 clean repo / corpus | graphify (--update), living-docs-governance, unified-memory, ecc-memory |
| W5 freeze | semgrep-guardian MCP (pre-freeze audit), verification-loop, mandela |
| W6 (post-freeze, boss gates) | hf-mcp-server (downloads, sha256), mlx-tune/GLM-OCR/Bodhan clones at freeze, council (W6 decision) |
| Memory / handoffs | ecc-memory MCP, unified-memory, catchup + nba |

## 4. LAYA / JEV RULING — DECIDED 2026-09-30 (proto-31, evidence-verified)

**Answer: Laya is NOT used. JEV is NOT used.** The boss's prior (CO-076/077: "LAYA is almost better and free → LAYA is best; could serve as a classifier or some layer") was countered with evidence — this is the counter the boss ordered.

**Evidence (verified 2026-09-30 ~15:30 IST on disk + PyPI; facts F61/F63/F64 in proto-93):**
1. **Installed state:** `laya 0.3.5` sits in Homebrew Python 3.14's user site, installed 2026-09-22 — it **cannot import there** (`ModuleNotFoundError: numpy`; torch/transformers absent). A working copy lives in another project's venv (`~/Desktop/swa-erp/.venv-laya`) — South must not depend on it. Not installed in South's `.venv`/`.venv311`; no Laya weights in the HF cache. PyPI current: 0.3.22 (Apache-2.0, Convai Innovations).
2. **It reads text, not images.** It cannot do OCR and cannot tell a page's language from the page.
3. **Its own code says it fails on Indic text:** the `laya/lang.py` docstring (0.3.5) — English checkpoint "collapsing to near-random on non-Latin scripts (Hindi 0.100, Korean 0.103, Swahili 0.103, Tamil 0.113 at 20 options, where random is 0.050)". Multilingual checkpoint (mmBERT-base, 322M) reports MASSIVE 0.657 averaged over 51 languages; no per-language numbers for our scripts; Ol Chiki, Meetei Mayek, Nastaliq Kashmiri UNKNOWN. Base typed decisions 0.362 zero-shot.
4. **Its script detection is a Unicode-range lookup** ("Script detection is exact") — a 10-line function does the same; no model needed.
5. **The Claude `laya-gate` skill is not for this project:** it runs swa-erp packs through swa-erp's decision service; its own honesty note says base LAYA checkpoints are near-chance zero-shot; in South the BOSS gates moves/deletes/downloads (proto-92 U29), not a classifier.
6. **The untracked `src/` "LayaRouter" never imports laya (F63):** it routes on `gt_text` (the answer key — leakage), ignores the engine it picks, maps Meetei Mayek to `Mend` (Mende Kikakui) instead of `Mtei`. U3 matter — archived per the boss's decision; do not fix without the boss.
7. **JEV is out:** closed-source, hosted, paid, 236–276 ms p50 (§B6) — breaks local-first and $0. Its numbers come from vendor-affiliated pages (orcarouter.ai, jev-ai.pro) — treat as vendor claims. Measured comparison: JEV wins accuracy (Banking77 0.870 vs Laya 0.425; zero-shot typed decisions 0.727 vs 0.362) but is not deployable in this campaign.

**The only reopen path (measured, not argued):** reopen only if BOTH hold after Plan v3 Day 4 (proto-89): (a) the oracle gap (proto-97 RQ-11) ≥ 0.02 CER for some language; AND (b) a deterministic bad-output check (empty output; wrong-script share; invalid Unicode sequences; n-gram repetition loops; low mean token log-prob) misses enough recoverable errors to move that language's CER by ≥ 0.02. If both hold, a learned gate may be tested (Laya-multilingual fine-tuned RLCD, or a character n-gram LM) — that is TRAINING, so it needs the boss (the W6 decision) and a leak-free split by source document. **Until then: no install, no download, no code, no new md.**

**CO-088 (the crossing pattern, one sourced paragraph):** how Laya/JEV "crossed into relevance" — typed-decision classifiers distilled for speed (mmBERT-base 322M, 32.8 ms/question on T4, 7.2 ms batched) and used as ROUTING/GATE layers for larger LLM agents — the small model decides *when to invoke the big one*, not the task itself. The analogous OCR move is the Day-4 deterministic gate above: a cheap bad-output check deciding *when to invoke a learned gate or the heavy engine*. JEV shows the hosted/paid variant of the same pattern (236–276 ms p50); Laya shows the local/free variant. Neither is an OCR model — both fit only as routing/decision heads, and only after the Day-4 gate proves the deterministic check insufficient.

**ECC and graphify verdicts (proto-31 Verdict task):**
- **ECC:** keep — the standing law names its skills as mandatory (verification-loop, unified-memory, terminal-ops, parallel-execution-optimizer); the gap is USE, not existence (jsonl counts 0 for the named set). Hook overhead: not measured (no hook_success durationMs extracted) — UNKNOWN, measure on next transcript pass.
- **ecc-memory MCP:** connected (fixed path) — SHOULD-USE, 0 mentions in DISPATCH_LOG: adopt for decision/checkpoint persistence.
- **graphify:** keep — navigation use is real (DISPATCH_LOG.md:115 rebuild; graph.json 6.6 MB); graph STALE (35 md changed since build) → `--update` before W4/W5 navigation use. Freshness rule: the bootstrap reports STALE when md files are newer than graph.json.

---

## Law held this wave

- Laya/JEV ruled DECIDED per proto-31 — no install, no download, no code (U31 file-triage TRIAL is advisory; never in the OCR model — U30).
- U26 (HF MCP) approved but AUTH-BLOCKED — boss's HF token is the gate (NEXT.md §7).
- No training, no Sarvam calls, sealed dirs read-only, no new root md.
- **Rule for every future tool decision:** no tool sits idle without a written reason (CO-075); use is proven from session-jsonl or DISPATCH_LOG citations, not assumed.
