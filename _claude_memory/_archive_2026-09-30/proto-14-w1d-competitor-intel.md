---
name: proto-14-w1d-competitor-intel
description: "Step 1D (research subagent) — consolidate existing competitor research, then live re-verify only the numbers the meeting packet uses (Sarvam 87.39 and its denominator, per-language scores, indic-ocr-bench GT process, Bodhan, Gnani, Consensus.app), with a WHAT-THEY-OVERLOOKED field per competitor"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:12:48.858Z
---

# STEP 1D — COMPETITOR INTEL (research subagent) → `docs/campaign/COMPETITOR_INTEL.md`

**Why:** the boss will be cross-examined on these numbers. A fabricated or mis-scoped figure is worse than a blank. Also resolves the directive's C12
(is sarvam_fill GT machine-made or human-reviewed?).
**Writes only:** `docs/campaign/COMPETITOR_INTEL.md`.

## TASK block (paste)
You are the research agent for competitor intelligence. **Consolidate first, fetch second.** Much of this was researched on 2026-09-29 already; your job is to
merge it, correct it against live sources, and scope every number.

**Step 1 — read the precursors (slices, `cut -c1-800`):** `docs/research/R6_COMPETITION_INTEL.md` · `docs/research/LIVE_LATEST_2026-09-29.md` (a second copy
exists at root — note whether they differ: `diff -q LIVE_LATEST_2026-09-29.md docs/research/LIVE_LATEST_2026-09-29.md`) · `docs/research/DEEPER_LIVE_RESEARCH_2026-09-29.md` ·
`docs/south/EXTERNAL_BENCHMARK_MAP.md` · `PAPERTHIN_VINAY_AUDIT.md` · `EVIDENCE_SUMMARY.md` §0 · `OCR_AGENT_MEMORY_FEED.md` §18 (line ~997). Build a list of every
competitor number these files cite, with file:line.

**Step 2 — live re-verification** (ToolSearch `select:WebSearch,WebFetch`). Only the numbers that the meeting packet uses or that change a decision:
1. **Sarvam Vision 2.1** — https://www.sarvam.ai/blogs/sarvam-vision-2-1 : what exactly is 87.39 (metric name; is it word accuracy, 1−CER, a composite?), averaged over what
   (languages? blocks? which subset?), per-language table (sat 53.91? ks 54.82? or 80.01? mni 85.12? "OldScan 55.3" — is OldScan a language or a condition?),
   comparison baselines they show, model size/architecture/training data statements.
2. **indic-ocr-bench** — https://huggingface.co/datasets/sarvamai/indic-ocr-bench : languages (22 + EN?), per-language sizes, total (6,909 blocks?), block vs page unit,
   splits, licence, **how GT was produced** (quote the card: human-reviewed? twice? machine?), who built it (Sarvam itself → self-built benchmark), evaluation code link.
3. **Dataset-overlap concern** — the packet cites a LinkedIn comment (Krrish Agarwalla) alleging Sarvam's bench overlaps its training data. Try the boss's links
   https://lnkd.in/p/eFzz2Dtb and https://lnkd.in/p/ewsNXkTs (LinkedIn often blocks fetches → UNKNOWN is fine). Do not restate an allegation as fact.
4. **Bodhan Indic-OCR** — find the primary source for "84.94" headline and "82.85 mni", open weights? price "₹0.20/image"? architecture.
5. **Gnani** — https://www.gnani.ai/ and https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B : confirm modality (text-only LLM vs OCR/vision), languages, size (30B-A3B MoE),
   licence, any OCR/document product. If it is not OCR, say so plainly: it is a funding/market competitor, not a benchmark competitor.
6. **Consensus.app** — https://consensus.app/ : what it indexes, free-tier limits (the lead says 10 searches/day), whether it is usable for this campaign. Do not create accounts.
7. Anything a precursor marked CONTRADICTION about these competitors — resolve if a primary source settles it.

**Step 3 — per competitor block (Sarvam Vision 2.1 · indic-ocr-bench as an evaluation instrument · Bodhan · Gnani · others found in precursors, e.g. Chitrapathak-2,
LightOnOCR-2-1B, PaddleOCR-VL 1.6 — only if a precursor cites them as competitors):**
`Architecture · Training approach · Data strategy · Published numbers (value · metric · subset · n · URL · PRIMARY/DERIVED) · Known weaknesses · WHAT THEY OVERLOOKED · Confidence`.
WHAT THEY OVERLOOKED = concrete: languages/scripts they report low or not at all; document conditions they skip (handwriting, degraded scans, tables, mixed script);
evaluation they built themselves; missing per-language n or confidence intervals; normalisation choices that flatter them; anything their own text admits as a limitation (quote it).

**Step 4 — the comparability section (critical for tomorrow):** a table "Can we compare our number X to their number Y?" for every pairing the packet makes
(e.g. our probe22 CER vs Sarvam 87.39; our per-language CER vs Sarvam per-language scores). Answer YES / NO / ONLY-DIRECTIONAL with the reason (different metric,
different items, different normalisation, different n).

**Step 5 — contradictions with precursors:** where live sources disagree with R6/LIVE_LATEST/DEEPER/packet, list both, file:line + URL.

**Step 6 — UNRESOLVED:** every URL that failed, every number you could not confirm.

Under 1,800 words. Final message: the comparability table + top 5 overlooked gaps + path.

## Lead's acceptance check
Open 3 random URLs from the file and confirm the quoted number appears. Every number carries metric + subset + n or is marked UNKNOWN.
Feed the GT-process finding into the checkpoint as the resolution (or not) of directive C12.

Related: [[proto-10-w1-overview]], [[proto-15-w1e-edge-hunt]], [[proto-19-w1h-draft-research-plan]]
