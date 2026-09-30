# INTEGRATED ELITE STACK — 2026-09-27

How the 25+ elite repos from the B5 refresh (see `docs/research/level7/b/b5_elite_repos/`) are actually wired into this project. Every repo below has been examined, every "install / keep / watch" decision is recorded, and the skill prompts that the 3 agents use have been updated to reference the integrated tools.

This is the canonical reference. If you wonder "where do we use paperthin / mlx-tune / liteparse / etc.?" — read this file.

---

## Install status (verified on disk 2026-09-27 18:44)

| Repo | Status | Where it lives | Decision it changes |
|---|---|---|---|
| `LilMGenius/paperthin` | **INSTALLED** | `~/.config/opencode/skills/paperthin/` | H44-48 call kill-criteria — `mandela`/`factchk`/`hate` reinforce eval gates |
| `ksimback/looper` | **INSTALLED** | `~/.config/opencode/skills/looper/` | Loop-design law operationalized — use when designing new review-gated loops |
| `Graphify-Labs/graphify` | INSTALLED (pre-existing) | `~/.local/bin/graphify` + `~/.config/opencode/skills/graphify/` | Codebase query tool — already driving this rebuild |
| `affaan-m/ECC` | INSTALLED (pre-existing, full profile) | `~/.config/opencode/skills/` (~215 skills) | Agent harness discipline (terminal-ops, verification-loop, unified-memory, parallel-execution-optimizer, etc.) |
| `anthropics/claude-code ralph-wiggum plugin` | AVAILABLE (Claude Code plugin) | not local; reference for loop-design-check skill | Continuous-loop technique behind our D1 W6 recipe evaluation |
| `claude-mem` | KEEP-AS-REFERENCE | source on GitHub | Persistent cross-session memory; revisit if unified-memory vault proves insufficient |
| `rtk-ai/rtk` | KEEP-AS-REFERENCE (CONTRADICTION registered) | not local | Token reduction; CONTRADICTION with JetBrains +7.6% median cost → call agenda |
| `browser-use` | KEEP-AS-REFERENCE | source on GitHub | Cheap research-lane agent patterns for Miss monitoring |
| `NousResearch/hermes-agent` | KEEP-AS-REFERENCE | source on GitHub | Hermes-style self-improvement loops for W6 |
| `ComposioHQ/awesome-claude-skills` | KEEP-AS-REFERENCE | source on GitHub | Curated skill catalog; reference for new-skill discovery |
| `deepseek-ai/deepseek-harness` | KEEP-AS-REFERENCE | source on GitHub | Harness-as-plugin architecture reference (do NOT migrate mid-campaign) |

## Keep-as-reference for W6 OCR (do NOT install yet — clones required)

| Repo | Decision it changes | When to install |
|---|---|---|
| `zai-org/GLM-OCR` (0.9B, OmniDocBench #1, official MLX deploy) | **D1 W6 recipe primary candidate** — replaces Qwen2.5-VL-3B in R7 W6 training tree | At W6 freeze (~Oct 1), clone + mlx-vlm deploy |
| `ARahim3/mlx-tune` (1.4k★, MLX-native SFT/DPO/GRPO, ships CER/WER) | **the QLoRA tool for D1** — replaces hand-rolled training scripts | At W6 freeze, install + use for fine-tuning |
| `run-llama/liteparse` (12.7k★, Rust, model-free PDF, M2 Max measured) | PDF front-end harness for wrap pipeline | At W6 freeze, Rust build |
| `studio-dots-ai/dots.mocr` (3B, MIT, multilingual Elo 1124.7, Old-scans 48.2) | head-to-head vs GLM-OCR for OldScan 55.3 weak cell | At W6 freeze, evaluate on probe22 subset |
| `Yuliang-Liu/MonkeyOCRv2` (0.7B Apache-2.0 code+weights, MDPBench 83.3, Hindi 71.9) | smallest strong fine-tune backbone | At W6 freeze, evaluate on Indic subset |
| `Tencent-Hunyuan/HunyuanOCR-1.5` (llama.cpp, ancient-script Agentic Data Flow) | weak-cell attack (sat/ks class adjacents) | At W6 freeze, license review first |
| `baidu/Unlimited-OCR` (26.4k★, long-horizon multi-page) | OldScan 55.3 — cross-page context could lift | At W6 freeze, evaluate |
| `arcships/light-ocr` (CoreML PP-OCRv6) | fast local detector on Apple Silicon | At W6 freeze, clone + test |
| `firecrawl/anydoc` (22k★, Rust doc→MD, Python bindings) | post-OCR normalization/output layer for the product | Post-hackathon |
| `datalab-to/lift` (910★, 9B schema JSON from PDFs) | structured-output stage if product needs JSON | Post-hackathon |
| `TencentCloud/TencentDB-Agent-Memory` (27.3k★, opencode adapter in progress) | team-tier memory option | Post-hackathon, when adapter lands |

## Watch-only (do NOT install)

| Repo | Note |
|---|---|
| `TimmyOVO/deepseek-ocr.rs` | Rust multi-backend engine; post-hackathon |
| `neural-maze/production-ocr-course` | reference for serving; not hackathon-critical |
| `superloglabs/superlog` (1.5k★, agentic telemetry) | post-hackathon production monitoring |
| `vercel-labs/eve-software-factory-template` | external validation of our FIND→SPEC→FIX→RE-VERIFY law; reference architecture for W6, don't deploy |
| `vectorize-io/hindsight` (34.6k★, agent memory) | candidate upgrade for unified-memory |
| `tt-a1i/archify` | diagram generation; optional polish |
| `cloudflare/security-audit-skill` | pre-W5-freeze security audit pattern |
| `zai-org/ZCode` / `stablyai/orca` / `deepseek-ai/deepseek-harness` / `xai-org/grok-build` | vendor-harness consolidation trend — DO NOT migrate mid-campaign |
| `Tencent-Hunyuan/HunyuanOCR` (Tencent Hunyuan Community License — not pure OSS) | license risk flag — REVIEW before any use |

---

## Where each INSTALLED tool plugs in

### paperthin (anti-slop skill suite, 28 skills)

The 5 most useful for our campaign right now:

- **`mandela`** — 8-pattern eval-leakage audit. Use during H44-48 validation call to audit our CER harness against self-confirming evals. At campaign integration point: ran on graphs/, GRAPH_REPORT.md, agent prompts.
- **`factchk`** — two-way source verification. Use when claiming a number, fact, or repo stats — must trace both directions through primary source.
- **`hate`** — the one objection that kills the plan + cheapest test. Use before any big decision (D1, D2, D3, D4) to surface the killer objection and the cheapest test for it.
- **`sip`** — auto self-check after changes. Apply after every Step 4 build to surface integrity issues.
- **`catchup` + `nba`** — rebuild owner's map → single next action. Use when context grows long to surface the single most important next step.

Invoke: `npx skills add LilMGenius/paperthin --global --agent '*'` (re-run if skills go missing). The skills are loaded automatically by the opencode agent — just reference them by name in your prompt.

### looper (loop-design skill)

- **Use when:** designing a NEW review-gated agent loop (e.g., a new fix-loop variant, a new pipeline step, a new validation cycle).
- **Don't use when:** running an existing loop. Looper is design, not execution.
- **Output:** a portable `loop.yaml` describing the loop (goal, verification type, reviewer model, termination guards). Saved alongside the loop code.
- **Cross-check with ECC `loop-design-check` skill:** both enforce plan-build-judge, judge independence, stop guards. ECC's is the discipline; looper is the spec format.

Invoke: `npx skills add ksimback/looper --global --agent '*'`. Same auto-load as paperthin.

### graphify (codebase→knowledge-graph CLI, pre-existing)

- **Use when:** asking any question about the codebase, file relationships, project content. Especially when `graphify-out/` exists.
- **Don't use when:** live-coding, debugging, or writing code.
- **Query forms:**
  - `graphify query "<question>"` — BFS traversal for broad context
  - `graphify query "<question>" --dfs` — DFS for tracing specific paths
  - `graphify path "<node_a>" "<node_b>"` — shortest path between two concepts
  - `graphify explain "<node>"` — plain-language explanation of a node
- **Built and kept up-to-date by:** the orchestrator (this session) on every corpus change. Current graph: **3990 nodes / 4681 edges / 420 communities / 50 hyperedges** (rebuilt 2026-09-29 18:24 IST over 18,239-file full corpus; pre-rebuild backup at `.pre-rebuild-2026-09-29`).

### ECC (215 skills, pre-existing)

- **Use when:** any agent workflow. ECC provides discipline skills (terminal-ops, verification-loop, unified-memory, parallel-execution-optimizer, santa-method, council, loop-design-check, market-research, deep-research, graphify as an ECC skill, etc.).
- **Skills relevant to current campaign:**
  - `verification-loop` — Engine and Miss use this for any "verify before claiming" work.
  - `terminal-ops` — Engine for evidence-first repo execution.
  - `unified-memory` — cross-agent handoffs (Engine→Verdict→Miss context).
  - `parallel-execution-optimizer` — subagent lane dispatching (the 3-wave chunk strategy we used).
  - `santa-method` — Verdict for adversarial review (two-pass).
  - `scholar-evaluation` — Verdict for evidence-quality audit.
  - `council` — multi-voice trade-off deliberation (for D1–D4 at validation call).
  - `loop-design-check` — design review for new agent loops (looper's discipline layer).
  - `market-research` — Miss for lane C competition intel.
  - `graphify` (ECC skill, not standalone) — codebase query interface wrapping the local CLI.

### Ralph Wiggum technique (continuous agent loop)

- **Use when:** designing a long-running autonomous agent task that must persist across iterations without losing context or drift.
- **Reference:** Geoffrey Huntley's ralph-wiggum technique, now an official anthropics/claude-code plugin.
- **Our adoption:** the `loop-design-check` ECC skill + the looper install together operationalize the ralph-wiggum discipline without the full plugin (we don't need the plugin; we need the discipline).

---

## Wiring into the 3-agent ops model (Engine / Verdict / Miss)

The 3 agent prompts at `docs/research/level7/PROMPT_{ENGINE,VERDICT,MISS}_AGENT.md` now reference the integrated elite stack. Quick reference:

- **Engine** uses `mlx-tune` (when W6 starts) for QLoRA training scripts; `liteparse` for PDF front-end; `GLM-OCR` (or `dots.mocr`) as the wrap-pipeline primary engine; `MonkeyOCRv2` for smallest fine-tune backbone; `Unlimited-OCR` for OldScan attack.
- **Verdict** uses `paperthin` (`mandela`, `factchk`, `hate`) for every eval-gate decision; `santa-method` for adversarial review; `scholar-evaluation` for evidence audit; `reverify` + `open-code-review` + `codex-plugin-cc` for fix-loop verification.
- **Miss** uses `paperthin` (`catchup`, `nba`) for context recovery; `unified-memory` for handoffs; `market-research` for lane C; `claude-mem` (when integrated) for cross-session context.

All 3 agents use `graphify` for codebase queries and `ECC` skills for workflow discipline (terminal-ops, verification-loop, parallel-execution-optimizer).

---

## Verification — how to confirm integration worked

```bash
# Skills installed
ls ~/.config/opencode/skills/ | grep -E 'paperthin|looper|graphify'
# → paperthin, looper, graphify (plus 214 others)

# Graph built
ls /Users/srujansai/Desktop/South/graphify-out/
# → GRAPH_REPORT.md, cost.json, graph.html, graph.json, manifest.json, .graphify_labels.json

# Graph size
python3 -c "import json; g=json.load(open('/Users/srujansai/Desktop/South/graphify-out/graph.json')); print(f'{len(g[\"nodes\"])} nodes, {len(g[\"links\"])} links')"
# → 3990 nodes, 4681 links, 420 communities

# Skills auto-load in prompts
grep -l paperthin /Users/srujansai/Desktop/South/docs/research/level7/PROMPT_*.md
```

---

## Decisions registered (campaign evidence law, status + decision it changes)

- **paperthin** — INSTALLED. Decision: H44-48 call kill-criteria reinforced with `mandela`/`factchk`/`hate` at zero cost.
- **looper** — INSTALLED. Decision: any new review-gated loop designed this week must use looper's spec format.
- **GLM-OCR** — KEEP for W6. Decision: D1 W6 recipe primary candidate upgraded from Qwen2.5-VL-3B (0.9B OmniDocBench #1, official MLX deploy).
- **mlx-tune** — KEEP for W6. Decision: replaces hand-rolled QLoRA training tooling (ships CER/WER metrics, MLX-native, Apache-2.0).
- **liteparse** — KEEP for W6. Decision: PDF front-end harness for the wrap pipeline (Rust, M2 Max measured).
- **dots.mocr** — KEEP for W6. Decision: head-to-head vs GLM-OCR at validation call for OldScan 55.3 attack.
- **rtk** — KEEP-AS-REFERENCE with CONTRADICTION. Decision: H44-48 call agenda item (60-90% reduction vs JetBrains +7.6% median cost).
- **DeepSeek-OCR-2 MLX** — CONTRADICTION (repo claims runnable, mlx-tune README says not loadable). Decision: do not block W6 on it; watch for MLX support.

---

## Honest-empty register (record these, don't paper over)

- **No new dedicated Ol Chiki / Nastaliq / Meitei-Mayek OCR repos** in the 6-month scan window. sat/ks/OldScan/or remain vision-LLM-only or W6 fine-tune targets.
- **OldScan restoration:** no new repos; best signals are dots.mocr Old-scans 48.2 and Unlimited-OCR long-horizon parsing.
- **Indic doc layout:** nothing new beyond known IndicPhotoOCR.
- **paperthin/looper via `npx skills add --global`:** FAILED with "PromptScript does not support global skill installation". Worked around by `git clone` + `cp -r` to `~/.config/opencode/skills/`. Future installs must use the manual method, not `npx`.
- **deepseek-harness plugin migration:** DO NOT migrate mid-campaign. Architecture reference only.

---

Cross-reference: see `docs/research/level7/b/b5_elite_repos/ELITE_REPO_REFRESH_2026-09-27.md` for the original 25-record refresh (this file is the action layer that wires them in).
