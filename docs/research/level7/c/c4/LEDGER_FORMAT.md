# Lane C4 — Research Ledger Format (ENFORCEMENT DOC)

Lane: C4 Tooling & logging (Miss Agent). Scope: the agent-tooling landscape —
Claude Code, Kimi, OpenCode/ECC, MCP servers, knowledge-graph/Obsidian
workflows, eval harnesses, TypeScript AI SDKs — **as applied to OUR OCR
probe/training workflow** (probe22 execution, Phase 6 scoring, §6.4 GT
verification, W6 recipe freeze). This doc is normative: any C4 record that
violates it is rejected from ranking.

## 1. Mandatory record fields (no exceptions)

Every record carries exactly:

```
[C4-NNN] title
source_url: <https URL, live at collection time>
date: <publication/release date; "n.d. (accessed 2026-09-26)" if undated>
status: VERIFIED | INFERENCE
relevance: 1-5 | recency: 1-5 | actionability: 1-5 | score: <product>/125
extraction: 3-10 lines, mechanism → result → mapping to OUR workflow
```

- `source_url` must be a real URL returned by web search or present on disk.
  No invented URLs. No listicles without a primary source behind them.
- `date` is the source's date, not the collection date. Stale (>12 months)
  sources cap recency at 2.
- `status: VERIFIED` = the claim was confirmed against the live source excerpt
  at collection time. `INFERENCE` = our extrapolation to the probe/training
  workflow (e.g. "this pattern would fix X in run_probe.py"). INFERENCE
  records are legal but never gate W6 decisions alone.

## 2. Weak-cell mapping (mandatory in every extraction)

Each extraction MUST name at least one weak cell it serves:

- Santali 53.91 (Ol Chiki / Bengali-script fill; 100% sarvam_fill, n=20)
- Kashmiri 54.82 (Nastaliq segmentation; PDF-tier VERIFY-FIRST, trust 45.0)
- OldScan 55.3 (200-dpi renders, skew/warp/illumination; Otsu-vs-denoiser open)
- Odia 80.01 (PDF-tier + 19 fill; script-ratio gate rejects)

Or one probe-workflow load-bearing point: scorer integrity (§6.5), tier
scoring/falsification (§6.2), human GT verification (§6.4), power/CIs (§6.7),
EN sanity column, credit-capped Sarvam API baseline, sequential-engine rule.

Records with no mapping are dropped at ranking.

## 3. Score rule

```
score = relevance × recency × actionability   (max 125)
```

- relevance: does it touch OUR workflow (probe tooling, scoring, verification,
  W6 training recipe)? 5 = directly pluggable this week.
- recency: 5 = 2026-08/09; 4 = 2026-05..07; 3 = 2026-01..04; 2 = 2025; 1 = older.
- actionability: 5 = concrete command/config/pattern we can run; 1 = background.
- **score ≥ 30/125 enters the integrated architecture** (LEVEL7_INTEGRATED_
  ARCHITECTURE.md). Below 30 stays as context only.

## 4. Verdict sampling rule (10% live-source check)

The Verdict Agent re-opens 10% of C4 records against the live source
(every 10th record: C4-010, C4-020, …). A sampled record fails if the URL is
dead, the date is wrong by >3 months, or the extraction misstates the source.
>20% sampled-failure rate voids the whole C4 ledger and triggers re-collection.

## 5. Contradiction rule

Contradictions with W1, R1–R7, SOUTH_CANON §P, PPT_SPEC, or the probe protocol
are **resolved in the integration pass, never by silently dropping a source**.
Procedure: log the contradiction in the record (`CONTRADICTS: <doc> §<x> —
<one line>`), keep both, and let the integration pass adjudicate with disk
evidence. Silent drops are a campaign violation.

## 6. Lane accounting

- Records target: ≥100 including this format doc (i.e. LEDGER.md holds ≥100
  C4-NNN records; this file is the +1 enforcement record).
- Sublanes: T1 Claude Code (C4-001–014), T2 Kimi (C4-015–026), T3 OpenCode/ECC
  (C4-027–040), T4 MCP servers (C4-041–054), T5 knowledge-graph/Obsidian
  (C4-055–066), T6 eval harnesses (C4-067–080), T7 TypeScript AI SDKs
  (C4-081–092), T8 ledger/logging/verification practice (C4-093–100).
- No downloads. No training. Nothing at root, nothing under level2/research/.

## 7. ADDENDUM — §9 evidence-law fields (2026-09-27; additive, §§1-6 unchanged)

Per `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §9 + PROMPT_MISS_AGENT tasks
1/4. Existing C4-001–100 rows keep their VERIFIED/INFERENCE status untouched
(never rewritten); the §9 upgrade lives as the appended `§9 UPGRADE` table in
LEDGER.md (one `§9-status | decision | TRANSFER` line per record) plus
§9-native records (C4-101+, T9). New records use this section's fields.

- `§9-status` set (replaces VERIFIED/INFERENCE for §9-native records only):
  PRIMARY (disk/spec first-party: probe22 files, protocol, campaign doc) |
  MEASURED (vendor-measured numbers, re-cited ledger URLs) |
  DERIVED (claim + our harness mapping) | UNKNOWN (single-source) |
  CONTRADICTION (logged per §5, kept not dropped). REJECTED/DEAD unused —
  nothing rejected; DIES lives in TRANSFER, not status.
- `decision:` line (mandatory, one line): the decision the record can change,
  or `none (context)`. A record naming no decision is DEAD (Miss law).
- `TRANSFER: SURVIVES / DIES / UNKNOWN` (mandatory): judged against OUR
  harness facts — 18 Indic langs, weak cells (Santali 53.91 / Kashmiri 54.82 /
  OldScan 55.3 / Odia 80.01), 200-dpi citizen docs, no paid keys, no training
  until W6 freeze, offline pipeline. Name the killing/saving fact. Needs
  weights/GPU/hidden-tests/keys → DIES or UNKNOWN, never "inspiration".
- `source_url` for §9-native records: disk-law paths allowed (C4-098/099/100
  precedent) or re-cites of URLs already in this ledger — no new downloads.
- `score` rule (§3) and `weak-cell mapping` (§2) apply unchanged; verdict
  sampling (§4) extends every 10th (C4-110, C4-120, …).
- Obituaries: external numbers cited anywhere in C4 live in OBITUARIES.md per
  campaign §9.2 (number + where-cited + four-mismatch kill + verdict +
  fail-condition); DEAD-for-decisions unless the obituary fails.

## 8. PROPOSAL — qualitative-to-numeric label mapping (Miss, 2026-09-27; for Verdict arbitration, NOT law until Verdict adopts)
Lane B records use qualitative labels (relevance high/medium/low; actionability direct/indirect/context) instead of 1–5 numbers, which the ≥30/125 score rule cannot consume. Proposed mapping (Verdict may amend; one-column re-pass over B):
- relevance: high=5, medium=3, low=1.
- recency: 2026-09=5, 2026-H1=4, 2025=3, older=1.
- actionability: direct=5, indirect=3, context=1.
Score = product as usual; rows scoring <30 stay as context per the contradiction rule (kept, not dropped). If Verdict prefers re-labeling at source instead, this section is void.
