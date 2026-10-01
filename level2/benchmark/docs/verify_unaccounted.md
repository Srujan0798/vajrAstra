# Unaccounted Visual Items — Resolved 2026-09-28 (Verdict re-verification 2026-09-29)

## Definition
"4 unaccounted visual items" = the 4 ceiling-sample additions that bring the visual verification total from 233 → 237. They were missing from the original stratified sample because the floor-vs-ceiling sampling bug (`len // 10` vs `-(-len // 10)`) dropped 1 item per affected language.

## The 4 Items (cross-checked against manifest.json)

| Item ID | Language | Set / gt_source | In manifest | Visual verdict | Auto precheck | Human spot-check |
|---------|----------|-----------------|-------------|----------------|---------------|------------------|
| brx_o045 | Bodo | official_pdf / official_pdf_layer | ✓ | pass [machine-verified (agent vision)] | pass | NOT in list |
| mr_o005 | Marathi | official_pdf / official_pdf_layer | ✓ | fail: script_adherence_low=0.921; repetition_rate=0.161; pipe_danda_ratio=1.00 [machine-verified (agent vision)] | pass | NOT in list |
| ne_o038 | Nepali | official_pdf / official_pdf_layer | ✓ | fail: control_chars=2; script_adherence_low=0.950 [machine-verified (agent vision)] | pass | NOT in list |
| sd_o002 | Sindhi | official_pdf / official_pdf_layer | ✓ | pass [machine-verified (agent vision)] | pass | NOT in list |

All 4 are present in manifest.json (n=1227), in `gt_verification.json` visual dict (n=237), and in auto_precheck dict (n=237). None are in the 20-item human_spot_check list.

## Root cause (mechanically verified)
Original stratified sampling used floor division `max(1, len(items) // 10)`:
- brx (47 PDF items) → floor=4, ceil=5 → lost 1 (brx_o045)
- mr (79 items) → floor=7, ceil=8 → lost 1 (mr_o005)
- ne (17 items) → floor=1, ceil=2 → lost 1 (ne_o038)
- sd (75 items) → floor=7, ceil=8 → lost 1 (sd_o002)

Replacement: ceiling division `-(-len(items) // 10)` recovers all 4. The 4 ceiling items are all from `official_pdf_layer` GT tier (none are sarvam_fill, so the GT quality is silver-tier at best; they go through the same `verify_visual.py` metric gates as the stratified sample).

## GT-tier integrity check (Verdict, 2026-09-29)
- brx_o045 GT starts with "7\nBodo\nHindi\nEnglish..." — multi-script header with Devanagari content. Visual pass holds (script_adherence above 0.95 gate).
- mr_o005 GT has repetition_rate=0.161 (above 0.05 threshold) and pipe_danda_ratio=1.00 (above 0.5 threshold). Visual FAIL recorded. mr_o005 contributes to mr's 37.5% pass rate → mr already BARRED via R5 + ceiling.
- ne_o038 GT contains control chars (n=2, above 0 threshold) and script_adherence=0.950 (above 0.85 but below 0.95). Visual FAIL recorded. ne stays BARRED via R5 full-set forensics (trust 26.6).
- sd_o002 GT starts with Arabic-script content — passes all gates.

## 18-lang code coverage check
Manifest languages (18): as, bn, brx, doi, gu, hi, kok, ks, mai, mni, mr, ne, or, pa, sa, sat, sd, ur. All 18 present.
Visual verification sample (15): as, brx, doi, gu, kok, ks, mai, mni, mr, ne, or, pa, sat, sd, ur. Missing: bn, hi, sa (these are the 3 official_pair languages with 300 human-verified gold pairs — they bypass visual verification because their GT is human-verified already; this is by design, not a gap).

## Resolution (locked)
- All 4 items added to visual dict with machine-verified pass/fail status.
- All 4 added to auto_precheck dict.
- sample_pdf_n updated 75 → 79.
- summary refreshed to: 233 machine-verified, 20-item human spot-check pending user, 4 unaccounted.
- The 4 ceiling items are NOT separate from the 233 — they are the 4 ADDITIONAL items that bring 233 → 237.

## Final state (canonical)
- visual dict: 237 keys (165 pass + 72 fail)
- auto_precheck: 237 keys (all pass — this is the lighter precheck)
- human_spot_check: 20 keys (suspicious subset, pending user)
- per_language_summary: 15 languages × varying n = 237 items

## STATUS: RESOLVED. No further Verdict action on this item.
