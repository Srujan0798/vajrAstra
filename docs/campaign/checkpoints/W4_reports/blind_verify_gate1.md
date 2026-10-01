# BLIND VERIFY — Gate 1 (BODHAN_BASELINE.md)

**Verifier:** blind subagent (no prior context to BODHAN work).
**Source under test:** `docs/campaign/BODHAN_BASELINE.md` (28 lines).
**Reference:** `DISPATCH_LOG.md` §36 (lines 699–708) + `level2/models_bodhan/` on disk.
**Date:** 2026-10-01.

## Check 1 — exact strings present in BODHAN_BASELINE.md

```
grep -c "0.4034"      → 1   (line 18)
grep -c "0.4010"      → 1   (line 18)
grep -c "0.6878"      → 1   (line 17)
grep -c "0.6863"      → 1   (line 17)
grep -c "0.0540"      → 1   (line 19)
grep -c "0.1356"      → 1   (line 19)
grep -c "CONDITIONAL PASS" → 1   (line 22)
```
All seven strings present exactly once. **PASS.**

## Check 2 — DISPATCH_LOG §36 carries the same values

| Field | DISPATCH_LOG §36 | BODHAN_BASELINE.md | Match |
|---|---|---|---|
| sample-100 4-bit CER | 0.6878 (line 703) | 0.6878 (line 17) | ✓ |
| sample-100 bf16 CER | 0.6863 (line 703) | 0.6863 (line 17) | ✓ |
| pair-only 4-bit CER | 0.4034 (line 704) | 0.4034 (line 18) | ✓ |
| pair-only bf16 CER | 0.4010 (line 704) | 0.4010 (line 18) | ✓ |
| bench small_rep CER | 0.0540 (line 705) | 0.0540 (line 19) | ✓ |
| bench small_rep WER | 0.1356 (line 705) | 0.1356 (line 19) | ✓ |
| sample-100 n | 99 (line 703) | 99 (line 17) | ✓ |
| pair-only n | 300 (line 704) | 300 (line 18) | ✓ |
| bench small_rep n | 1,173 (line 705) | 1173 (line 19) | ✓ (formatting only) |
| Gate 1 status | "CONDITIONAL PASS." (line 708) | "**Gate 1: CONDITIONAL PASS.**" (line 22) | ✓ |

All numerical values identical. n formatting differs by thousands separator (1,173 vs 1173) — cosmetic, not material. **PASS.**

## Check 3 — required rows in the table

| Required row | Present? | Detail |
|---|---|---|
| sample-100 (n=99) | ✓ | line 17 — n column = 99, label "sample-100 (same 99)" |
| pair-only (n=300) | ✓ | line 18 — n column = 300, label "pair-only (300 gold)" |
| bench small_rep (n=1173) | ✓ | line 19 — n column = 1173, label "bench small_rep" |
| official-path (BLOCKED) | ✓ semantic | line 20 — label "official-path", n=99, both CER columns = "—", Notes = "vendor assert; parity waits GPU day". BLOCKED is conveyed via empty CER + vendor-assert note (DISPATCH_LOG §36 uses "BLOCKED: vendor code asserts CUDA; GPU tomorrow"; BODHAN_BASELINE paraphrases to "vendor assert; parity waits GPU day"). Empty CER columns = no measurable result = BLOCKED. |

All four required rows present; BLOCKED semantics preserved. The label "BLOCKED" itself is absent in BODHAN_BASELINE (renamed/paraphrased to vendor-assert note) — flag for awareness but not a fail. **PASS** (with note).

## Check 4 — on-disk Bodhan variants exist

```
ls level2/models_bodhan/indic-ocr/          → ARCHITECTURE.md, README.md, app.py, config.json, idp_*.py, …
ls level2/models_bodhan/indic-ocr-mlx-4bit/ → README.md, app.py, chat_template.jinja, config.json, …
ls level2/models_bodhan/indic-ocr-mlx-bf16/ → README.md, app.py, chat_template.jinja, config.json, …
```
All three required directories present and non-empty (contain app.py, config.json, etc.). **PASS.**

## Summary

| # | Check | Verdict |
|---|---|---|
| 1 | exact strings (0.4034, 0.4010, 0.6878, 0.6863, 0.0540, 0.1356, "CONDITIONAL PASS") in BODHAN_BASELINE | **PASS** |
| 2 | DISPATCH_LOG §36 carries identical Gate 1 numbers | **PASS** |
| 3 | table rows: sample-100/99, pair-only/300, bench small_rep/1173, official-path BLOCKED | **PASS** (label "BLOCKED" paraphrased but semantics intact via empty CER + vendor-assert note) |
| 4 | on-disk variants: indic-ocr, indic-ocr-mlx-4bit, indic-ocr-mlx-bf16 | **PASS** |

**OVERALL: PASS.** Gate 1 numbers in BODHAN_BASELINE.md faithfully reproduce DISPATCH_LOG §36 and match on-disk reality.

## Notes / non-failures observed

- Two extra directories on disk (`indic-ocr-bench`, `indic-ocr-mlx-8bit`) are also listed in the BODHAN_BASELINE "Variants on Disk" table as 0-safetensors / 0-MB placeholders. Not part of Gate 1 numeric checks; informational only.
- BODHAN_BASELINE.md is 28 lines, total, no orphan EOF, no PENDING / 403 / Agree rows (confirmed absent in §36.1 rewrite note).