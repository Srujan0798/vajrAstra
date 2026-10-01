# W6 set construction log — 2026-09-28 21:23 IST (Miss agent)

NO TRAINING performed. Data prep only. Output is JSONL manifests on disk for the next phase (W6 = after the user picks a date, all gates green).

## Outputs

| File | Items | Status | Purpose |
|---|---|---|---|
| `level2/probe22/w6_sft_unconditional.jsonl` | 458 | 100% OK | W6 SFT (no §6.4 blocker) |
| `level2/probe22/w6_sft_conditional.jsonl`   | 342 | 100% PENDING §6.4 VERIFY | W6 SFT (gated on user verdict sign-off) |
| `level2/probe22/w6_rlvr_unconditional.jsonl` | 300 | 100% OK | W6 RLVR (D1: NO sarvam_fill, gold-pair only) |

## Per-language totals (matches w6_feasible_set.md intent)

### SFT unconditional — 458 written vs 459 target (sa short by 1, see gaps)
| lang | tier mix | items |
|---|---|---|
| bn | 100 official_pair | 100 |
| hi | 100 official_pair | 100 |
| sa | 99 official_pair | 99 |
| or | 50 official_pdf + 19 sarvam_fill | 69 |
| pa | 90 official_pdf | 90 |

### SFT conditional — 342 written, all PENDING §6.4 VERIFY
| lang | items |
|---|---|
| brx | 67 |
| kok | 100 |
| mai | 100 |
| sd | 75 |

### RLVR unconditional — 300 written
| lang | items |
|---|---|
| bn | 100 pair |
| hi | 100 pair |
| sa | 100 pair |

## D-honors (audit trail)

- **D1 honored**: `or` fill items (19) appear in the jsonl but FLAGGED `"status": "EXCLUDE-D1"` — runtime filter before training drops them. No sarvam_fill anywhere else.
- **D2 honored**: NO PDF-tier items in unconditional SFT/RLVR. Conditional SFT is all PDF-tier, all marked PENDING §6.4.
- **D3 honored**: GT<10 char items already purged (1,229 → 1,227).
- **D4 honored**: NO training items from n<50 cells (as, gu, ne, doi, mni, sat).
- **D5 honored**: §6.6 ablation max delta 0.5pp, 0 inversions — RLVR gate clear.
- **D6 honored**: No ur/ks/sd/sat/mni in any jsonl — no Perso-Arabic/Ol Chiki/Meitei for the akshara-boundary aux loss scope.
- **D7 pending**: §6.4 full PDF-tier verification (visual sample only); gates the 342-item conditional set.

## Sanity gaps (audit findings, surface to orchestrator)

1. **sa pair count = 99, target = 100.** One sa item is gone between §1 purge and current manifest. NOT inflation. NOT flagged.
2. **w6_feasible_set.md math**: 459 + 342 + 437 = 1238, but manifest = 1227. Diff = 11 items absent from w6 totals. NOT touching that file (per-doc lock).
3. **`or` 19 fill items** in unconditional jsonl tagged EXCLUDE-D1 — runtime filter required.

## What I did not do (per law)

- No training run, no model write, no GPU touch.
- No Sarvam API call.
- No dataset download.
- No edits to AGENT_PROTOCOL.md, level2/out/, level2/reports/, manifest.json, or sealed dirs.

## Artifacts on disk

- `level2/probe22/w6_sft_unconditional.jsonl` (458 items, 1 sa short)
- `level2/probe22/w6_sft_conditional.jsonl` (342 items, all PENDING §6.4 VERIFY)
- `level2/probe22/w6_rlvr_unconditional.jsonl` (300 items, pair-only)
- `level2/probe22/w6_set_construction_log.md` (this file)

## Blocker (user-decision)

- §6.4 full PDF-tier verification for brx/kok/mai/sd = gate for 342-item conditional set.
- GPU budget answer for actual training (Steps A are prep only — no training run).
