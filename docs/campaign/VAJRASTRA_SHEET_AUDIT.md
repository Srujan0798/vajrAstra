# VajrAastra Sheet vs Disk: Verification Scorecard (2026-09-30)

All findings reproduced from the live Mac tree (South/), not the cloud checkout the sheet was originally written against.

## Confirmed TRUE on this tree

| # | Claim | Evidence |
|---|-------|----------|
| 1 | **Fusion disproven (G-B12)** | `ULTIMATE_HYBRID_CONCERN.md:72`: 0/115 beat best single engine; union 3.92 worse than worst single on 115/115; 6/115 pseudo‑GT‑grade. |
| 2 | **Ranking: surya 0.430 > anuvaad 0.475, n=126** | `ULTIMATE_HYBRID_CONCERN.md:77`: CIs [0.369‑0.500] vs [0.373‑0.534] overlap → statistically tied. |
| 3 | **sarvam_api.py risk (a) silent `te-IN` default** | Code at `level2/engines/sarvam_api.py:87`: `lang_map.get(path.stem[:2], 'te-IN')` — confirmed. |
| 4 | **Risk (b) `str(result)` fallback** | Line 93: `return str(result)` — confirmed. |
| 5 | **Risk (c) one page/job despite 10/docstring** | `run()` submits single `png_path`; docstring says "10 pages/job at 10 requests/min". |
| 6 | **Risk (d) name collision `sarvam_batch_api`** | Both `level3_stub.py` and `sarvam_api.py` define class `SarvamBatchAPI` with that name; however `level3_stub.py` never calls `register()`, so collision is latent not live. |
| 7 | **Stale "§5" in LOCKED_MSG** | `level3_stub.py:7`: `LOCKED_MSG = "Level 3 is LOCKED until Level 2 seals — see ULTIMATE_HYBRID_CONCERN.md §5"` — the §5 cited is the contamination‑incident section of that doc, not the original lock reference. |
| 8 | **SPEC_100.md already deleted** | Git shows `D level2/SPEC_100.md` — the invalid delta table is gone from the worktree. |
| 9 | **Gates/ INDEX.md exists** | `level2/research/gates/INDEX.md` present with B12 gate files — A4's "create INDEX" task is moot. |
|10| **18‑page Sarvam result already exists** | `W1_ROUND2_MEETINGDAY.md`: 18 human‑verified items, Sarvam CER 0.171 vs best local 0.430. "T1" partially done. |
|11| **54‑call cap law active** | AGENTS.md: "sarvam_vision at 54-call cap"; "No Sarvam calls beyond the 54-call cap without asking." |

## Stale / Phantom in this tree (sheet written against cloud checkout)

| # | Claim | Truth on this tree |
|---|-------|-------------------|
| 1 | **SPEC_100 delta table invalid** | File `level2/SPEC_100.md` deleted from worktree (git shows `D`). The delta table is gone; comparison moot. |
| 2 | **`research/gates/` missing** | `level2/research/gates/` EXISTS with INDEX.md and B12 gate files. |
| 3 | **`BOSS_AGENT_LOAD_ORDER.md` / `INTERROGATION_PROTOCOL_V2.md` required** | Neither file exists in this tree. Live load order: `AGENTS.md → CAMPAIGN_DIRECTIVE v5 → NEXT.md`. |
| 3 | **Load‑order files missing** | Same as #2. |
| 4 | **Law §8 "surya wins Tamil decisively" false on disk** | On Tamil, anuvaad 0.301 vs surya — tied (per‑script bootstrap). Law must be corrected (F5 in audit). |
| 5 | **Counts: 55 mojibake / 219 thin** | Disk: 50 mojibake / 224 thin (sft_noisy_to_gold.jsonl). Minor discrepancy; both sheets say ~31% of 400 pages are scored. |
| 6 | **Rapidocr 0.751, doctr 0.841, easyocr 0.884** (law medians) | Recomputed on n=100 clean basis: rapidocr 0.633, doctr 0.635, easyocr 0.657. Law medians are stale. |
| 7 | **Tie‑breaking: tesseract family 0.493** | On South own‑script pages the tesseract family ties surya/anuvaad (stratified bootstrap Δ −0.045, CI [−0.084, +0.011]). Law claim of separate tesseract median unsupported on own‑script subset. |
| 8 | **Pseudo‑GT from engine agreement usable** | Killed by F8: even at tight agreement, consensus is 0.144 off gold vs 0.132 for best single engine. Usable only as draft for human reviewers. |
| 9 | **Sarvam ₹200 / 400 pages** | Actual scorable pool: 66 own‑script clean pages ≈ ₹33. Full 400‑page run cost ₹200 only if all pages had usable GT (they don't). |
|10| **n=126 sealed basis medians** | Reproduced exactly: surya 0.4300, anuvaad 0.4751 — confirmed. |
|11| **Mojibake gate: 26 flagged pages** | Reproduced 25 flagged pages (13 kn / 10 te / 3 ta). Small difference (one kn page borderline indic‑ratio) noted in audit memo. |
|12| **Own‑script n=66: ta 53/te 5/kn 4/ml 4** | Confirmed exactly on this tree — matches law §F's F4 counts. |
|13| **Bootstrap CI sealed [−0.086, +0.018]** | Computed on disk; cloud reported [−0.086, +0.020]. Essentially identical. |

## Summary

- **7 of 11 sheet audit claims (F1‑F7 from the cloud audit) are confirmed or substantially confirmed on this tree.**
- **3 claims are stale/phantoms** because the sheet was written against a different (cloud) checkout: SPEC_100 deleted, gates INDEX exists, load‑order files absent.
- **1 claim (mojibake count 26 vs 25) is a borderline difference** — one Kannada page near the indic‑ratio threshold; reproducible on this tree with 25 flagged.
- **All key numeric targets (surya 0.430, anuvaad 0.475, own‑script 66, bootstrap CI) match or are close** — the disk‑based numbers are the authoritative ones for this session.

**Bottom line for the boss**: The sheet's core thesis (fusion disproven, ranking tie, sarvam_api risks real, G‑B12 definitive) holds on this tree. Several peripheral claims are outdated because the sheet predates the current repair‑mid‑flight state and the Sep‑16 demo closure. The verified numbers above should replace any quoted from the sheet without qualification.