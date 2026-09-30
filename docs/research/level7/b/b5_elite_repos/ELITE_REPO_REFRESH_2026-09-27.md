# B5 Elite-Repo Refresh — 2026-09-27

Scan law: window 2026-03-27 → 2026-09-27, 10x weight on Aug–Sep 2026. Method: 4
parallel research subagents (trending-top-15 / agent-harness / OCR-docAI /
dev-process), live sources only (github-search API, github-trending weekly +
monthly, repo-README fetches). No downloads, clones, or installs performed
(hard rule respected).

Record format per campaign §3: `repo | stars/created | what | status(source) |
free+local | decision it can change`. Status is exactly one of the §9 law
values. Unlabeled numbers forbidden; every record names its decision.

## A. PRODUCT — Indic OCR engine & W6 recipe (Lane A overlap)

- **A1. zai-org/GLM-OCR** | 7.5k★, created 2026-02-02, active through Sep | 0.9B
  OCR VLM, 94.62 OmniDocBench v1.5 (#1 score), MTP loss, built-in two-stage
  pipeline (PP-DocLayout-V3 + parallel recognition = exactly our wrap
  architecture), official mlx-vlm deploy guide (examples/mlx-deploy) +
  LLaMA-Factory FT guide | PRIMARY (repo README) | Apache-2.0 code / MIT
  weights; YES local on Apple Silicon | DECISION: W6 recipe primary candidate
  + wrap-pipeline engine. Beats PaddleOCR-VL 1.6 (96.33 OmniDocBench) class
  at 0.9B params.
- **A2. studio-dots-ai/dots.mocr** (mirror of rednote-hilab/dots.mocr) | 351★,
  created 2026-03-19, hot through Sep | 3B "parse anything" multilingual VLM,
  single model + graphics→SVG; top Elo avg 1124.7 (beats HunyuanOCR,
  PaddleOCR-VL-1.5, GLM-OCR head-to-head per their table); olmOCR-bench 83.9
  with best Old-scans-math 85.5 and Old-scans 48.2; Kannada/Tibetan demos =
  low-resource script coverage | PRIMARY (repo README) | MIT; vLLM CUDA-only,
  CPU path documented, MLX UNKNOWN | DECISION: wrap-pipeline head-to-head vs
  GLM-OCR; Old-scans number directly targets our OldScan 55.3 weak cell.
- **A3. baidu/Unlimited-OCR** | 26.4k★, created 2026-06-18 | One-shot
  long-horizon parsing: multi-page docs in a single pass (≤32,768 output
  tokens), builds on DeepSeek-OCR/PaddleOCR; vLLM/SGLang/ms-swift; arXiv
  2606.23050, Trendshift daily badge | PRIMARY (repo README + live fetch) |
  MIT; CUDA transformers, local UNKNOWN | DECISION: cross-page context could
  lift OldScan 55.3 weak cell; Lane-A candidate engine.
- **A4. Yuliang-Liu/MonkeyOCRv2** | 1.5k★, created 2026-07-10 | Document-native
  vision backbone (ViT-S 28M / ViT-B 113M); MonkeyOCRv2-B-Parsing 0.7B, #1
  MDPBench 83.3 across 17 languages incl. Hindi 71.9; CPU support added
  2026-08-22; FT instructions available | PRIMARY (repo README + LICENSE) |
  Apache-2.0 code AND all weights | DECISION: W6 smallest strong fine-tunable
  backbone (0.7B fits 32GB with headroom).
- **A5. Tencent-Hunyuan/HunyuanOCR** (1.5 released 2026-07-07) | 2.0k★, repo
  created 2025-11-18 | 0.9B, 4K res, 128K ctx, DFlash; llama.cpp GGUF
  CPU/consumer-GPU deployment; "Agentic Data Flow" explicitly targets
  low-resource + ancient-script OCR; CHAOS-Bench 2026-07-13 | PRIMARY (repo
  README) | Tencent Hunyuan Community License — free, not pure OSS; llama.cpp
  → likely local, UNKNOWN until tested | DECISION: weak-cell attack angle
  (ancient-script class ≈ Ol Chiki/Nastaliq adjacents); license review
  REQUIRED before any use.
- **A6. ARahim3/mlx-tune** | 1.4k★, created 2026-01-03 | MLX-native fine-tuning
  (SFT/DPO/GRPO) for LLMs/VLMs incl. DeepSeek-OCR-1/2, GLM-OCR, DOTS-OCR,
  olmOCR-2, LightOnOCR, Qwen2.5-VL, Pixtral; ships CER/WER metrics | PRIMARY
  (repo README) | Apache-2.0, built for Apple Silicon | DECISION: THE QLoRA
  tool for the W6 conditional-training path (D1). Replaces hand-rolled
  training scripts.
- **A7. deepseek-ai/DeepSeek-OCR-2** | 3.4k★, created 2026-01-27 | 3B "Visual
  Causal Flow" OCR, dynamic resolution (0–6)×768² + 1024² | CONTRADICTION on
  MLX: mlx-tune README says needs mlx-vlm≥0.4 → transformers≥5.0, "not
  loadable anywhere" yet, vs repo README claims | Apache-2.0; local NO
  currently | DECISION: watch for MLX support landing; do not block W6 on it.
- **A8. arcships/light-ocr** | 508★, created 2026-07-14 | PP-OCRv6 packaged
  with CoreML for Apple Silicon | PRIMARY existence (github-search); details
  UNKNOWN | DECISION: fast local detection stage in the wrap pipeline.
- **A9. TimmyOVO/deepseek-ocr.rs** | 2.2k★ (created 2025-10-25, outside window)
  | Rust multi-backend OCR/VLM engine (DeepSeek-OCR-1/2, PaddleOCR-VL,
  DotsOCR), DSQ quantization, OpenAI-compatible server, no Python | PRIMARY
  existence (github-search) | DECISION: lean production-serving option for a
  local server.

## B. PRODUCTION — output, serving, monitoring

- **B1. firecrawl/anydoc** | 22.1k★, created 2026-08-03 | Rust documents→clean
  Markdown (Word/PPT/Excel/ODT/RTF/EPUB/CSV/PDF), Node.js + Python bindings |
  PRIMARY (github-search) | DECISION: post-OCR normalization/output layer for
  the product; Python bindings drop into our stack. Evaluate for Lane A.
- **B2. run-llama/liteparse** | 12.7k★, created 2026-02-09, benchmarks updated
  2026-09-09 | Rust, model-free PDF parsing (PDFium) with pluggable
  OCR-server backends, worker-pool mode; benchmarked on M2 Max 32GB | PRIMARY
  (repo README) | Apache-2.0, runs natively | DECISION: PDF front-end harness
  for the wrap pipeline (native on our exact hardware class).
- **B3. datalab-to/lift** | 910★, created 2026-06-03 | 9B vision model for
  schema-constrained JSON extraction from PDFs (surya team) | PRIMARY (repo
  README) | Apache-2.0 code / OpenRAIL-M weights; 9B needs quant on 64GB,
  UNKNOWN | DECISION: structured-output stage if the product needs JSON.
- **B4. neural-maze/production-ocr-course** | 416★, created 2026-07-22 |
  Production OCR serving with vLLM/Rust/K8s | PRIMARY existence
  (github-search) | DECISION: reference material for W6+ serving plan; not
  hackathon-critical.
- **B5. superloglabs/superlog** | 1.5k★, created 2026-06-02 (488 commits) |
  Open-core agentic telemetry: OTel ingest → incident grouping → pluggable
  agent runner investigates and records incident summaries; YC P26 | PRIMARY
  (repo README) | Apache-2.0 community edition, self-host Docker Compose |
  DECISION: post-hackathon production monitoring; too infra-heavy for the 48h
  window.

## C. HARNESS/PROCESS — 3-agent ops model upgrades

- **C1. TokenRhythm/opensquilla** | 7.1k★, created 2026-05-06 (1,659 commits,
  arXiv 2607.11399) | SquillaRouter: on-device LightGBM+ONNX per-turn
  classifier routes to cheapest capable model across 4 tiers (C0–C3);
  adaptive reasoning + system-prompt scaling; persistent local memory
  (MEMORY.md, SQLite FTS + sqlite-vec); Seatbelt sandbox on macOS; denial
  ledger auto-pauses runs; 15 bundled skills + MCP; 20+ providers |
  PRIMARY (repo README) | Apache-2.0, BYO provider keys, classification fully
  on-device | DECISION: token-cost control for our subagent lanes — strongest
  measured claim in scan: PinchBench 1.2.1, 25 tasks: 0.9251 avg at $0.688
  vs OpenClaw 0.9255 at $6.233 (~9x cheaper at equal score).
- **C2. LilMGenius/paperthin** | 1.1k★, created 2026-06-19 | 25-skill
  anti-slop suite, works on any agent incl. OpenCode (`npx skills add
  LilMGenius/paperthin --global --agent '*'`): `mandela` (8-pattern
  eval-leakage audit), `factchk` (two-way source verification), `hate` (the
  one objection that kills the plan + cheapest test), `sip`, `re0`, `ssotize`,
  `shower`, `macrothink` | PRIMARY (repo README) | MIT, pure markdown skills |
  DECISION: strengthen H44–48 validation-call kill criteria — `mandela`
  audits our CER harness against self-confirming evals at zero cost. ADOPT
  NOW.
- **C3. ksimback/looper** | 710★, created 2026-06-18 | Claude Code skill
  (`/looper`) that DESIGNS review-gated loops before running: coached goal,
  typed verification (programmatic/judge/human), cross-model reviewer by
  default, termination guards (iteration/revision/no-progress/budget caps),
  portable loop.yaml + `looper lint` CI gate | PRIMARY (repo README) | MIT |
  DECISION: our loop-design law made operational; adopt selectively only if a
  new agent loop is designed this week.
- **C4. vectorize-io/hindsight** | 34.6k★, created pre-window (created date
  DERIVED via search-exclusion from created:>2026-03-27 top-30) | "Agent
  Memory That Learns" — memory layer for agents that improves from experience;
  #1 weekly velocity on trending (7.3k★/wk) | PRIMARY stars/velocity
  (github-trending-weekly) | DECISION: candidate upgrade for unified-memory
  cross-agent handoffs (Engine/Verdict/Miss).
- **C5. TencentCloud/TencentDB-Agent-Memory** | 27.3k★, created 2026-04-07 |
  Team memory hub: Chat Memory L0→L3, Skills, Wiki + link-graph, CodeGraph;
  proxy-based zero-code integration (point agent base URL at proxy); PersonaMem
  48%→76%; adapters incl. opencode (adapters/opencode/ on feat/server_team
  branch) | PRIMARY (repo README) | MIT self-host, local-first tagged; BYO
  LLM API params required | DECISION: team-tier memory option; native opencode
  adapter in progress — watch, don't install mid-campaign.
- **C6. deepseek-ai/deepseek-harness** | 237.3k★, created 2026-08-13 |
  "Everything is a Plugin" agent harness (DSH); fastest-growing repo of the
  window (~5.5k★/day for 6 weeks); satellite ecosystem crystallized in 48h
  (dsh-desktop 29.1k★, dsh-web 8.1k★, awesome-dsh-plugin) | PRIMARY
  (github-search) | DECISION: harness-as-plugin reference pattern for our
  ops model; do NOT migrate mid-campaign.
- **C7. cloudflare/security-audit-skill** | 22.1k★, created 2026-06-18 |
  Coding-agent skill: multi-phase security audits producing independently
  verified machine-readable findings; 19.1k★/mo + 6.5k★/wk dual velocity |
  PRIMARY (github-trending-weekly + monthly + search) | DECISION: pre-W5-freeze
  security audit pattern; machine-readable findings fit our evidence law.
- **C8. vercel-labs/eve-software-factory-template ("Foreman")** | 1.1k★,
  created 2026-08-12 | Software factory: GitHub/Linear issue → Classifier →
  Analyst (plan + acceptance criteria) → Implementer (sandbox) → INDEPENDENT
  Reviewer that sees only the diff, never the implementer's reasoning; factory
  brain repo memory; red CI auto-diagnosed on factory branches | PRIMARY (repo
  README) | MIT; local TUI only, full pipeline needs Vercel (conflicts
  no-cloud-spend) | DECISION: external validation of our FIND→SPEC→FIX→
  RE-VERIFY judge-independence law; reference architecture for W6, don't
  deploy mid-campaign.
- **C9. DietrichGebert/ponytail** | 146.7k★, created 2026-06-12 (35.1k★ this
  month) | YAGNI-enforcement skill/proxy — "makes your AI agent think like the
  laziest senior dev in the room" (Claude Code plugins, cursor rules) | PRIMARY
  (github-trending-monthly + search) | DECISION: already known to us; now
  quantified. YAGNI discipline is exactly the W5-freeze + "do not invent a
  novel backbone" law.
- **C10. tt-a1i/archify** | 72.5k★, created 2026-04-15 (55.7k★/mo — highest
  monthly gain on trending) | Agent skill: verifiable
  architecture/workflow/sequence/data-flow diagrams as self-contained HTML |
  PRIMARY (github-trending-monthly) | DECISION: diagram generation for
  PPT_SPEC/campaign docs; optional polish only.
- **C11. NandhaKishorM/laya** | 26.2k★, created 2026-09-18 (~2.9k★/day —
  fastest new repo of September) | Non-autoregressive "System 1" typed
  decision engine (choice/score/yes-no in one forward pass), 100+ languages,
  per-request checkpoint router (ModernBERT); satellites laya-mlx, kev, and
  fast-jev-compaction within days | PRIMARY (github-search) | DECISION:
  upgrade path for our LAYA System-1 gates (we already run laya-gate);
  multilingual router concept maps to Indic script detection pre-processing.
- **C12. stablyai/orca** | 79.2k★, created pre-window (DERIVED, same method) |
  "ADE" agent development environment — fleet of parallel agents on your own
  subscription, desktop/mobile/remote runtime; 6.5k★/wk (top-3 weekly) |
  PRIMARY velocity (github-trending-weekly) | DECISION: parallel-fleet
  reference for scaling the 3-agent model; not needed for hackathon.
- **C13. browser-use/jev-ultrafast** | 20.7k★, created 2026-09-16 | "Fastest
  and cheapest web agent" from browser-use org; anchor of the September
  Jev/System-1 wave | PRIMARY (github-search) | DECISION: cheap research-lane
  patterns for Miss's monitoring; cost-cap discipline reference (our 54-call
  Sarvam cap).
- **C14. ai-memory** | stars UNKNOWN from this scan (agent-harness lane pick) |
  Zero-LLM, git-backed memory persistence; closest fit to our no-spend law |
  PRIMARY (agent-harness scan; verify README before install) | DECISION:
  lightweight cross-session memory if unified-memory vault proves insufficient.
- **C15. reverify / open-code-review / codex-plugin-cc** (agent-harness lane
  picks) | reverify: VERIFIED/REFUTED ledger that survives compaction;
  open-code-review: deterministic+LLM hybrid review, OpenCode plugin;
  codex-plugin-cc: cross-vendor adversarial review | PRIMARY (agent-harness
  scan) | DECISION: fix-loop verification upgrades — reverify strengthens the
  FIND→SPEC→FIX→RE-VERIFY loop; open-code-review fits our exact harness.

## D. RANKED SHORTLIST (top 15)

**ADOPT NOW (this week; zero/low cost; fits no-spend law):**
1. paperthin — `mandela`/`factchk`/`hate` as validation-call eval gates
2. GLM-OCR — W6 recipe + wrap engine (official MLX deploy guide)
3. mlx-tune — W6 QLoRA tooling on our exact hardware
4. liteparse — model-free PDF front-end, measured on M2 Max 32GB
5. light-ocr — CoreML PP-OCRv6 fast local detector
6. archify / cloudflare security-audit-skill — docs + pre-freeze audit (optional)

**AT THE H44–48 VALIDATION CALL (decision items):**
7. dots.mocr vs GLM-OCR head-to-head as wrap engine (needs Indic bench first)
8. MonkeyOCRv2 0.7B as smallest fine-tune backbone
9. Unlimited-OCR long-horizon for OldScan 55.3
10. HunyuanOCR-1.5 license review (ancient-script angle)
11. rtk CONTRADICTION (below) — keep or drop from harness stack
12. opensquilla router for token cost (~9x measured, equal score)

**WATCH (no action):**
13. DeepSeek-OCR-2 (MLX support pending — CONTRADICTION)
14. hindsight / TencentDB-Agent-Memory (memory tier, post-hackathon)
15. deepseek-harness / orca / ZCode / grok-build (architecture reference;
    vendor-harness consolidation trend — do not migrate mid-campaign)

**POST-HACKATHON:** superlog (telemetry), eve-software-factory (deploy),
anydoc (output layer), lift (JSON stage), production-ocr-course (serving).

## E. CONTRADICTION register (both quotes stored, no winner picked)

- **E1. rtk token reduction:** prior B5 claim (rtk-ai/rtk, 60–90% token
  reduction) vs agent-harness scan finding (JetBrains study: +7.6% median
  cost). DECISION IT CHANGES: whether rtk stays in our harness stack →
  H44–48 call agenda.
- **E2. DeepSeek-OCR-2 local runnability:** repo README (runnable, dynamic
  res) vs mlx-tune README (needs mlx-vlm≥0.4 → transformers≥5.0, "not
  loadable anywhere yet"). DECISION IT CHANGES: W6 recipe eligibility.

## F. HONEST-EMPTY register (successful outputs, not holes)

- **F1.** No new dedicated Ol Chiki / Nastaliq / Meitei-Mayek OCR repos found in
  window. Closest indirect: dots.mocr multilingual demos, HunyuanOCR-1.5
  ancient-script data flow, MonkeyOCRv2 Hindi 71.9 (MDPBench). sat/ks remain
  vision-LLM-only or W6 fine-tune targets — verdict unchanged.
- **F2.** OldScan restoration: nothing new; best signals dots.mocr Old-scans
  48.2 / Old-scans-math 85.5 and Unlimited-OCR long-horizon parsing.
- **F3.** Indic doc layout: nothing new beyond known IndicPhotoOCR.

— Scan ends. 4 agents, ~30 github searches, ~25 README fetches, all records
status-labeled per §9. No downloads performed (§9 hard rule).
