# LEVEL 2 — Benchmark Results Package (Sep-16)

This folder is the shareable snapshot of vajrAstra South Level 2: our own-data
OCR benchmark of 10 free engines across 400 real government-textbook pages
(Telugu/Tamil/Kannada/Malayalam) — exactly what the Sep-10 sync asked for
("create our own benchmark with our own data — a reality check vs published
numbers").

## The one-screen summary
Open **SEP16_ONE_SCREEN.md** — everything on one page: 10/10 engines, 4,000
packs, coverage, consensus, per-script winners, gap headline, CER leaders,
latency, failure census.

## What's in this folder

| file | what it is |
|---|---|
| `SEP16_ONE_SCREEN.md` | the whole benchmark on one screen (start here) |
| `GAP.md` | the money number: 7.1% of GT text even the best free engine misses (lower bound) + per-script table |
| `LEADERBOARD_BY_SCRIPT.md` | per-script winners — no fake single-league averages |
| `CER_BY_SCRIPT.md` | accuracy table with confidence intervals + metric verdicts (CER vs AKER) |
| `SHOWCASE.md` | 6 rule-picked pages × 6 engines side-by-side with ground truth |
| `LATENCY.md` | ms/page + pages/hour per engine (probe-backed for tesseract family) |
| `FAILURE_TAXONOMY.md` | how engines fail: empty / loop / leak / thin |
| `LEVEL2_SEAL.md` | machine-checked seal: 11 gates green, 4,000/4,000 packs verified |
| `WHATSAPP_SEPT16.md` | the 5-line update for the group chat (paste-ready) |
| `DECISIONS.log` | every decision made, append-only ledger |
| `ULTIMATE_HYBRID_CONCERN.md` | the operating law file (how this was run) |
| `FOLDER_MAP.md` | what lives where in the repo |

## Headline numbers (all machine-verified, no hand numbers)

- **10 engine runs × 400 pages = 4,000 packs** (9 distinct engines; 7
  independent families — the 4 tesseract variants share one binary,
  disclosed).
- **Free-OSS volume gap: 7.1%** (lower bound; 177-page GT basis; 63
  legacy-font + 43 broken text layers in there = 60% of layered pages are
  extraction-hostile).
- **Accuracy: tied leaders surya + anuvaad** (median CER 0.43 / 0.48,
  statistically tied), tier-1 clear of 3rd place by ≥0.18 CER.
- **Consensus (independent engines agreeing): 38/400 word-level, 21/400
  family-deduped, 1/400 strict 5-gram** — disagreement is the training
  signal.
- **Seal: 11/11 machine gates GREEN** — schema, manifest, freshness,
  provenance, honesty disclosures.

## Method in one paragraph
400 real pages (200-dpi scans, government textbooks, 4 languages) rendered
once, run through 10 free/OSS engines under an open-script policy (engines
read whatever is on the page — no language restriction). Every output JSON is
verified against three truth layers: the PDF text layer, human gold labels
(Level 1), and cross-engine agreement. Ground-truth quality is gated: pages
with mojibake or thin text layers are nulled, never ranked on. Every report is
machine-generated with timestamps; nothing is hand-written.

## Reproduce
Repo (code only): https://github.com/Srujan0798/vajrAstra
```
git clone https://github.com/Srujan0798/vajrAstra
cd vajrAstra && bash setup.sh
.venv/bin/python level2/report.py     # regenerates every report from packs on disk
```

**Raw outputs:** all 4,000 engine packs live at `level2/out/` (see its README
for layout, engine notes, and where the PNG/PDF sources are) —
https://github.com/Srujan0798/vajrAstra/tree/main/level2/out

Generated 2026-09-14. Level 2 complete & sealed; Level 3 (paid-API
comparison, Sarvam ≈₹100 net for 400 pages) approved for post-demo.
