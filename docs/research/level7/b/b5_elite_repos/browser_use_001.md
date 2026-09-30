# browser_use_001 (converted from browser_use_001.jsonl - all records, fields verbatim)

## Record 1 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/browser-use
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Browser Use (browser-use/browser-use): Open-source browser agent (Python and TypeScript). Three paths: 1) Fully Hosted Cloud (scale with hosted agent + stealth browsers + infrastructure), 2) CLI (give existing agent browser access — Claude Code, Codex, Hermes, OpenClaw, Pi, Cursor), 3) Python Library (run locally with custom tools, structured output, choice of model). $0.02 per browser-hour cloud browser with stealth, CAPTCHA solving, residential proxies. Hosted agent API. Quickstart CLI: 'Install/upgrade browser-use with uv using Python 3.12, run browser-use skill install, connect to browser.' Python: 'uv add browser-use', set OPENAI_API_KEY or BROWSER_USE_API_KEY, run agent.py with ChatOpenAI or ChatBrowserUse (BU2 model). BU2 is their model optimized for browser automation. MIT license. Made in Zurich and San Francisco.
- **decision_it_changes**:

  Whether to adopt Browser Use CLI for Miss agent's monitoring/research tasks that need web access (e.g., checking latest OCR papers, verifying engine outputs against live benchmarks). But cloud browser costs money — violates no-paid-keys. Local browser + local model (Ollama) is free option.
- **transfer**: UNKNOWN
- **transfer_harness_fact**:

  18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Cloud browser/API = paid. Local browser + Ollama = free but needs GPU for reasonable speed.
- **actionality**: 4

## Record 2 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/browser-use/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: direct
- **extraction**:

  Browser Use Benchmark v2: Very hard benchmark targeting hardest browser tasks. 60-task subset shown. Mean rubric score by model and cost per task. BU2 (their model) performance shown. On easier tasks, smaller models achieve high success rates. Best model recommendation: BU2 (ChatBrowserUse(model='bu-2-0')) using BROWSER_USE_API_KEY. Can also use Claude/GPT/Gemini through ChatBrowserUse with provider-prefixed model IDs (anthropic/claude-sonnet-4-6, google/gemini-3-pro) via Browser Use gateway. Custom tools supported via Tools registry.
- **decision_it_changes**:

  BU2 requires BROWSER_USE_API_KEY (paid). Provider-prefixed models through gateway also need Browser Use API key. Only free path: local browser + local model (Ollama) or own API keys (OpenAI/Anthropic/Google) — but those are paid keys we don't have.
- **transfer**: DIES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. All recommended models need paid API keys. Local Ollama path needs GPU we may not have.
- **actionality**: 3

## Record 3 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/browser-use/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Browser Use integrations: Browser Harness (CLI for AI agents), Browser Harness JS (JS agents), Browser Use Pi (TS agent on Pi), Cloud SDK (integrate Cloud API), Video Use (edit videos with coding agent), macOS Harness (control Mac apps/browsers/files), Benchmark (compare agent performance). Related repos show ecosystem breadth.
- **decision_it_changes**: Ecosystem exists but all cloud-dependent. The CLI path (giving our Claude Code browser access) is most relevant — but requires Browser Use skill install and browser connection.
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. CLI skill install is free but browser connection may need cloud for stealth/CAPTCHA.
- **actionality**: 3

## Record 4 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/browser-use/blob/main/README.md
- **date**: 2026-08-31
- **status**: PRIMARY
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  Browser Use FAQ: Local browser: use Browser.from_system_chrome() to reuse Chrome profile (cookies, SSO). Cloud browser: profile sync guide (transfers cookies, not localStorage/IndexedDB/extensions). CAPTCHA: Cloud provides stealth browsers/proxies to reduce bot detection; no config guarantees solving all CAPTCHAs. Production: keep agent code + connect to cloud browsers, or use fully hosted Cloud API. Auth: local browser reuse is free; cloud needs profile sync.
- **decision_it_changes**: Local browser reuse (Browser.from_system_chrome()) is free and uses existing Chrome profile. This could work for Miss agent's research tasks without cloud spend. But CAPTCHA-heavy sites may block.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Local browser reuse is fully local — zero cost.
- **actionality**: 3

## Record 5 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/jev-ultrafast
- **date**: 2026-09-16
- **status**: MEASURED
- **relevance**: 3
- **recency**: 5
- **actionability**: theoretical
- **extraction**:

  browser-use/jev-ultrafast (20.7k stars, created 2026-09-16): 'Fastest and cheapest web agent' from browser-use org. Anchor of September Jev/System-1 wave. This is a separate repo for a System-1 (fast, cheap) web agent variant.
- **decision_it_changes**: Jev-ultrafast is a cost-optimized variant — relevant to our cost-cap discipline (54-call Sarvam cap). But still needs browser infrastructure.
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. New repo (Sep 16), untested; likely still needs cloud browser for best results.
- **actionality**: 3

## Record 6 (from browser_use_001.jsonl)
- **source_url**: https://github.com/EmbraceAGI/Awesome-AGI/blob/main/README.md
- **date**: 2026-08-20
- **status**: MEASURED
- **relevance**: 2
- **recency**: 4
- **actionability**: indirect
- **extraction**:

  Awesome-AGI: Browser Use not explicitly listed but browser-use org repos (browser-harness, browser-use-pi, sdk, video-use, macos-harness, benchmark) form a complete browser automation stack. The cloud browser ($0.02/hr) is the commercial engine.
- **decision_it_changes**: Browser Use's business model is cloud browser + hosted agent. Open source library is the on-ramp. For our campaign, only the library + local browser is viable.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Library is MIT; cloud is separate product.
- **actionality**: 2

## Record 7 (from browser_use_001.jsonl)
- **source_url**: https://docs.browser-use.com/open-source/supported-models
- **date**: 2026-08-31
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**:

  Supported models: ChatBrowserUse (BU2, provider-prefixed via gateway), ChatOpenAI, ChatAnthropic, ChatGoogle, Ollama (local). Ollama path: local model, local browser — fully free but needs hardware. 'Subject to your hardware and model requirements.' This is our only no-paid-keys path.
- **decision_it_changes**: Ollama + local browser is the only free tier. Requires GPU for reasonable browser automation speed. Our campaign hardware (M2 Max 32GB) can run Ollama but browser automation is CPU-heavy.
- **transfer**: UNKNOWN
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. Hardware-dependent — UNKNOWN until tested on our M2 Max.
- **actionality**: 2

## Record 8 (from browser_use_001.jsonl)
- **source_url**: https://github.com/browser-use/browser-use/blob/main/README.md
- **date**: 2026-08-31
- **status**: MEASURED
- **relevance**: 2
- **recency**: 5
- **actionability**: indirect
- **extraction**: Citation: Browser Use by Müller, Magnus and Žunič, Gregor (2024). MIT license. The core team is two people. This is a small team project with commercial cloud backing.
- **decision_it_changes**: Small core team (2) + commercial cloud = sustainability risk if cloud revenue doesn't cover maintenance. But MIT license ensures forkability.
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline. MIT license protects us; cloud is optional.
- **actionality**: 2
