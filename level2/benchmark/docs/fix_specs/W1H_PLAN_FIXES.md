# W1H PLAN FIX-SPECS — proto-86 (13 verified defects in the plan the boss presents)

**Author:** Sonnet lead, 2026-09-30 · **Method:** proto-18 (pre-image, exact-string, verify) · **Target:** `docs/campaign/DRAFT_RESEARCH_PLAN.md`
**Pre-image:** `_archive/pre_fix_2026-09-30/DRAFT_RESEARCH_PLAN.md` (sha256 recorded in the apply log)
**Deadline guard (ULTIMATE_HYBRID_CONCERN L12/D12):** fixes only, no new scope. Keep ≤4 pages — replace, do not pile on.
**Lead-verified vs monitor-sourced is marked per item. Nothing here is taken on the monitor's word.**

| # | Status | Lead verification |
|---|---|---|
| D1 GT-tier table in §3 | **ALREADY DONE** in the proto-64 pass (this protocol's snapshot predates it) | re-derived from `sheet.csv` × `manifest.json` `gt_source` |
| D2 Option A/D columns | **ALREADY DONE** in the proto-64 pass | both columns verified distinct; naming hazard disclosed |
| D3 Punjabi K1 | **VERIFIED BY LEAD** | `mcnemar_full_matrix.json` → `tesseract_indic_vs_surya [pa]`: n_common 90, **n_ties 87, n_discordant 3, p_two_sided 1.0, winner "tie"**. `kok`: n_discordant **31**, p **0.003327**, winner b. The "88 discordant" belongs to **rapidocr** pairs. **QLoRA scope = Konkani only.** `KILL_CRITERIA.md:56` and feed §12.2 are wrong → ERRATUM. |
| D4 McNemar definition | **VERIFIED** | `mcnemar_full_matrix.json` `meta.cer_threshold = 0.5` |
| D5 already-answered questions | boss decisions supplied by the monitor | recorded as DECIDED, not asked |
| D6 Indic-OCR pack contents | **VERIFIED** | project README states the pack includes Ol Chiki + Meetei Mayek; **licence still UNVERIFIED** |
| D7 traineddata / fonts | **VERIFIED — and the monitor CORRECTS my earlier claim** | `level2/probe22/tessdata/` lacks mni/sat/kan/mal/tam/tel, but `/opt/homebrew/share/tessdata/` **has** kan, mal, tam, tel and `level2/research/smoke/anuvaad_tesseract/tessdata/` has anuvaad_kan/mal/tam/tel. So **only `mni` and `sat` are genuinely missing**, and the ask shrinks from 6 languages to 2. Fonts: `fc-list` → **10 Meetei Mayek, 1 Ol Chiki** (macOS Supplemental has NotoSansMeeteiMayek + October Meetei Mayek, and NotoSansOlChiki). **"One typeface each" was wrong.** |
| D8 hackathon rubric | monitor-sourced | one sentence + pointer to proto-80 |
| D9 coverage gap | **VERIFIED** | all 1,283 items `print_or_hand=printed`, `has_table=False`, `mixed_script=False`; `quality` = 983 unknown / 300 clean |
| D10 surya licence | **VERIFIED** | `docs/legal/LICENSE_AUDIT.md:21` — dist-info METADATA says Apache-2.0, the LICENSE text says **modified AI Pubs OpenRAIL-M "free for research, personal use, and startups under $5M funding/revenue"**. The package contradicts itself; a CEO decision, not an engineering one. |
| D11 submission path | **PARTIALLY verified** | IndicPhotoOCR's CLIP script identifier **exists**: `.deps/IndicPhotoOCR/IndicPhotoOCR/script_identification/CLIP_identifier.py` (weights licence TODO). The monitor's "5,344 unlabelled test images" did **not** reproduce — `find Datasets/akshardrishti_official -name '*.png' -o -name '*.jpg' -o -name '*.jpeg'` returns **20,656** files. Both numbers are reported; neither is asserted as the test-set size. |
| D12 Kok/Sarvam 97.41 | lead | mixes their word accuracy with our CER → demoted to a labelled footnote |
| D13 OpenCode leg | lead | the leg needs a session with the `opencode` MCP, or the boss pastes the prompt into OpenCode |

## ERRATUM (append-only, no edit to the files themselves)
- **ERRATUM-K1** — `docs/research/level7/KILL_CRITERIA.md:56` states Punjabi "SURVIVES K1, p<0.0001, 88 discordant". The 88 belongs to rapidocr pairs; the surya-vs-tesseract_indic comparison on `pa` is a **tie (87/90 items tied, 3 discordant, p=1.0)**. Konkani is the only language that passes K1 (31 discordant, p=0.0033). **Erratum only — the file is not edited here.**
- **ERRATUM-F1** — `OCR_AGENT_MEMORY_FEED.md` §12.2 carries the same superseded pa claim. Appended to the §11 log, never rewritten (feed law).

---

## APPLY LOG (proto-86, 2026-09-30)

Pre-images: `_archive/pre_fix_2026-09-30/DRAFT_RESEARCH_PLAN.md` (sha256 `1a5bed37475bfcc0a9b6c45d8717a54067804d14413bf2982c8d7cae0784a2a2`, 23,526 B) and `_archive/pre_fix_2026-09-30/VINAY_MEETING_PACKET.precondense.md`.

| item | result |
|---|---|
| D1, D2 | **already closed** before this protocol's snapshot (proto-64 pass) — re-verified, no action |
| D3 | APPLIED to the plan (§2 K1/K2 nodes, §5 plain statement) **and to the packet** (6 sites). Q1 statement added to the packet TL;DR. **ERRATUM-K1 + ERRATUM-F1 filed.** |
| D4 | APPLIED — McNemar pass = CER < 0.5, `meta.cer_threshold = 0.5`, added to §3 |
| D5 | APPLIED — U7/U6/U10/U11 recorded as DECIDED; U1, U2, U4, U5, U8 kept open; U13 and U14 added |
| D6 | APPLIED — pack contents stated, licence flagged unverified |
| D7 | APPLIED and **it corrects this lead's own earlier claim** — only mni + sat missing; 10 Meetei fonts, 1 Ol Chiki |
| D8 | APPLIED — rubric sentence (bootstrap 95% CI, WER, S/D/I, sec/page) + proto-80 pointer |
| D9 | APPLIED — 1,283 printed, 0 tables, 0 mixed-script, 983 quality unknown; U13 added |
| D10 | APPLIED — surya licence conflict (metadata Apache-2.0 vs LICENSE modified OpenRAIL-M $5M cap); U14 added |
| D11 | APPLIED — submission-path row with the on-disk CLIP identifier; **5,344 not reproduced, 20,656 measured, both reported** |
| D12 | APPLIED as an inline labelled parenthetical by a concurrent editor; my redundant footnote definition was **removed** so no orphaned `[^…]` marker remains |
| D13 | APPLIED — the OpenCode leg needs a session with the `opencode` MCP, or the boss pastes the prompt into OpenCode |

**CONCURRENCY (proto-60 Rule 3/4 breach, recorded):** another agent was editing `DRAFT_RESEARCH_PLAN.md` and `VINAY_MEETING_PACKET.md` **during this pass** — the plan grew 19,398 → 23,526 B before my edits and the packet had already received the Punjabi fix. Two of my replacements failed for that reason (D3-T1, D13) and seven packet mirrors failed for the same reason. **Consequence: two editors wrote the same file in the same window, so ownership of these two documents is now ambiguous.** The lead's condensation pass then replaced a 140-character parenthetical that the other editor had pasted **12–15 times** across the packet, with a short form plus one authoritative "Q1" statement — this is the one place where this pass overwrote another editor's wording, and it was done because 15 repetitions of the same caveat is not presentable to a CEO.

**Post-apply integrity:** false-pattern greps on the packet all 0 (`Beats Sarvam on 9/18`, `9/18`, `Tue 2026-09-30`, `Sat 2026-10-04`, `Wed 2026-10-01`, `Konkani + Punjabi`, `both SAFE, both`). Plan 27,346 B, packet 32,113 B. All 13 proto-86 items verified present by grep.
