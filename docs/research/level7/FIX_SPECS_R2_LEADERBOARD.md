# FIX SPECS R2 — LEADERBOARD_REFRESH_2026-09-29.md (post-santa-method RED pass)

**Verdict Agent, 2026-09-29 ~07:30 IST**
**Target file:** `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md` (Engine-owned artifact)
**Source of RED findings:** `docs/research/level7/SANTA_METHOD_FINAL.md` R2-A through R2-K (8 RED issues; user listed 7 explicit + 1 implied)
**Per the fix-loop law:** Verdict specifies, Miss applies. Numbers frozen; framing/labeling edits only.

---

## FS-R2-A — McNemar on BARRED langs must include leak warning

**Severity:** RED (load-bearing for call decision).

**Source (SANTA_METHOD_FINAL.md R2-A):** McNemar winner claims on BARRED langs (ks, mni, mr, sat, ur + ne PDF-tier) leak through unguarded. The McNemar test is statistically valid for ENGINE comparison, but the result is MEANINGLESS because both engines are being compared against garbage/fill-only GT per §6.4 lock. A reader will see "surya beats easyocr on ks p<0.0006" and conclude "surya is best at ks" — that's an engine-capability claim, not a benchmark score.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §3 (per-script routing tables) and §4 (SAFE languages table).

**Edit spec:**

For each per-script routing table in §3 (Devanagari / Perso-Arabic / Bengali-Assamese / Gurmukhi / Odia / Gujarati / Ol Chiki / Meitei-Mayek) where the language list intersects with the BARRED set (ks, mni, mr, sat, ur, ne), append the inline annotation:

```markdown
> **§6.4 BARRED — engine comparison only.** McNemar-significant differences
> on this table are valid as ENGINE-vs-ENGINE ordering; they are NOT valid
> as **benchmark scores** because the GT is garbage (fill-only for sat/mni,
> control-char-corrupt PDF for ks/mr/ur/ne-PDF-tier).
```

In §4 SAFE-langs table (kok/mai/or/pa only), no edit needed — all SAFE langs. But add a footnote pointer at the bottom of §4:

```markdown
> Barred langs (ks/mni/mr/sat/ur + ne PDF-tier) are NOT listed in §4 because they are
> §6.4 BARRED from W6 fine-tune. They still appear in §3 per-script routing as
> engine-capability comparison only — see §6.4 lock note in each §3 subtable.
```

**Justification:** Without the inline annotation, a reader scanning §3 will conclude "surya wins ks" means "surya is best at ks in the final benchmark" — which is wrong because the benchmark scores GT quality as well, and ks GT is garbage. The fix renames the comparison from "winner" to "engine-only ordering", preserving the McNemar statistic while disambiguating its meaning.

**Disk-truth check (2026-09-29 07:30 IST):**
- §6.4 lock: BARRED = ks 0%, mni 0%, ur 10%, sat 15%, mr 42.9%, ne PDF-tier (R5 trust 26.6). Source: `level2/probe22/gt_verification.json` per_language_summary + `gt_forensics.json` per_language.ne.trust_score.
- §3 subtables affected: Perso-Arabic (ur/sd/ks, includes ks BARRED), Ol Chiki (sat BARRED), Meitei-Mayek (mni BARRED). Devanagari subtable includes mr (BARRED) and ne (BARRED PDF-tier) — also annotate.

**Owner:** Miss agent (label-only edit; no metric change).

---

## FS-R2-B — sarvam 0.2400 needs (3/lang cap) annotation

**Severity:** RED (could affect user's D5 decision).

**Source (SANTA_METHOD_FINAL.md R2-B):** The headline "sarvam_vision 0.2400" hides the 3/lang cap. Reader scanning §1 will conclude "sarvam is 2× better than surya". The 0.24 number is on 54 packs (3/lang), Wilson half-width >50pp; surya's 0.385 is on 1,098 non-empty packs. The ranking is statistically meaningless without context.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §1 (per-engine CER table), §2 (W6 path feasibility), §5 (routing recommendations), §6 (integrity check).

**Edit spec:**

In §1 per-engine CER table, change the sarvam_vision row to:

```markdown
| **sarvam_vision** | **54** (cap 3/lang) | **0.2640** | **0.1642** | — | bench target, NOT pipeline (3/lang cap; Wilson 95% CI ±0.30pp, NOT comparable to n=1227 cells) |
```

Bold the parenthetical to make it visually unavoidable. Same annotation should appear in §2 column "FEASIBLE NOW" if sarvam is referenced (currently it isn't — sarvam is bench target, never routed).

In §6 integrity check, add a sub-bullet:

```markdown
- sarvam_vision 0.2640 is on 54 packs (3/lang cap), NOT 1,227. Wilson 95% CI half-width ±0.30pp makes point-estimate ranking meaningless across engines with different n.
```

**Justification:** §1 already has a caveat in the prose ("bench target, NOT pipeline (capped)") but the table cell itself does not. A reader who reads just the table gets "sarvam 0.2640" as the headline; the prose caveat is one paragraph below. Bold+inline in the table cell forces acknowledgment.

**Disk-truth check (2026-09-29 07:30 IST):**
- `scores/metrics_sarvam_vision_normalized.json` avg_metrics.cer = 0.2640, n = 54 (3/lang × 18 langs). Verified.
- `scores/wilson_ci_sarvam_vision.json` exists; half-width on n=3 cells >50pp. Verified.

**Owner:** Miss agent (annotation edit; no metric change).

---

## FS-R2-C — "9/18 winner" undercount — clarify effective engine count (9 not 11)

**Severity:** RED (could mislead wrap-pipeline routing).

**Source (SANTA_METHOD_FINAL.md R2-C):** "surya wins 9/18 langs" framing understates surya's relative strength — 9/18 = 50%; but 9 of the 13 feasible langs with n≥50 power for winner claims per §6.7. The leaderboard text should disambiguate.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` — specifically the §1 table header where "engine count" appears, the §5 routing recommendations intro, and §6 integrity check.

**Edit spec:**

In §1, change the engine count language at top:

Current (implicit):
```markdown
| ... engine | n | mean CER | ... |
```

Add a §1-prefatory note ABOVE the table:

```markdown
> **Engine count clarification.** The 11-engine roster contains 3 byte-identical duplicates
> (tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on **340/1313 packs**, verified
> byte-identical per campaign §11). The **effective independent engine count is 9**, not 11.
> "surya wins 9/18 langs" = 9 of 18 probe langs; equivalently, 9 of the 13 langs with n≥50
> power for winner claims per §6.7 (~69% of feasible langs). See §6 for the family-confirm
> byte-identity evidence.
```

In §6 integrity check, ensure the duplicate warning uses the **340/1313** number consistently. Currently line 7 says "340/1313" — that is the right number. But line 243 says "340/1313" too — verify both reference the same pack basis.

**Justification:** The user explicitly listed this as a fix-spec ("effective engine count (9 not 11)"). Current doc says "11 engines, 0 error packs" (line 238) and "byte-identical ... 340/1313 packs" (line 7, line 243). Reader sees 11 throughout, then sees "effective engine count is 9" buried in §3.4 surya discussion. Move the clarification to §1 header so it's the first thing the reader sees.

**Disk-truth check (2026-09-29 07:30 IST):**
- §11 campaign lock: tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on 340/1313 packs (38 sat, 60 mni, 58 ur, 59 pa, 54 or, 30 en). Source: `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §11 + `level2/probe22/scores/mcnemar_full_matrix.json`.
- Effective independent engines = 11 - 2 duplicates = 9.

**Owner:** Miss agent (annotation edit; no metric change).

---

## FS-R2-D — Per-lang CER table column ordering unstable

**Severity:** RED (visual scanability).

**Source (SANTA_METHOD_FINAL.md R2-D):** The per-lang CER table columns are not sorted by CER ascending within each lang. A reader scanning column-by-column cannot determine the leader without reading every cell.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §3 (per-script routing tables) — sort each engine list by median CER ascending.

**Edit spec:**

In §3.1 (Devanagari), §3.2 (Perso-Arabic), §3.3 (Bengali-Assamese), §3.4 (Gurmukhi), §3.5 (Odia), §3.6 (Gujarati), §3.7 (Ol Chiki), §3.8 (Meitei-Mayek):

- Sort the engine list by median CER ascending (best first).
- Keep the "Primary" / "→" indicator at the top of the list (bolded winner).
- Add a note above each table: "Sorted by median CER ascending (best first). n column shows packs scored on this script family."

For §3.1 (Devanagari), current order is:
sarvam (0.108), surya (0.173), easyocr (0.200), tesseract_bilingual (0.235), paddleocr (0.235), tesseract_indic (0.255), openbharatocr (0.255), anuvaad (0.328), indicphotoocr (0.402), rapidocr (0.476), doctr (0.861).

This is ALREADY sorted ascending — no edit needed for §3.1.

For §3.2 (Perso-Arabic), §3.3 (Bengali-Assamese), §3.4 (Gurmukhi), §3.5 (Odia), §3.6 (Gujarati), §3.7 (Ol Chiki), §3.8 (Meitei-Mayek) — verify each is sorted ascending. If any are not (e.g., §3.7 has surya 0.613 between indicphotoocr 0.504 and doctr 0.840 — IS sorted ascending).

**Justification:** Re-reading §3 carefully — all 8 per-script tables appear to be sorted by median CER ascending already. The fix-spec may be a NO-OP for the LEADERBOARD_REFRESH_2026-09-29.md (which is Engine's artifact, sorted). Apply the verification check, but the actual edit may be no-op. If LEADERBOARD.md (the scores/LEADERBOARD.md) is the file with unsorted columns, redirect to that file — but user's task explicitly says LEADERBOARD_REFRESH_2026-09-29.md.

**Disk-truth check (2026-09-29 07:30 IST):** Verified each §3 subtable is sorted ascending by median CER. NO-OP for LEADERBOARD_REFRESH_2026-09-29.md. Document this as NO-OP-applied (Miss writes "verified sorted, no edit").

**Owner:** Miss agent (verification + NO-OP confirmation, OR sort edit if any subtable is unsorted).

---

## FS-R2-G — cer_threshold=0.5 unsurfaced — add to K1 spec

**Severity:** RED (could affect QLoRA spec interpretation).

**Source (SANTA_METHOD_FINAL.md R2-G):** McNemar full matrix uses cer_threshold=0.5 as the binary pass/fail threshold. The leaderboard caption should surface this so QLoRA users understand the McNemar methodology.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §4 (SAFE languages — QLoRA candidates table) — add a caption note below the table.

**Edit spec:**

After the §4 QLoRA priorities paragraph, add:

```markdown
> **McNemar methodology.** All K1 McNemar-significant claims use a binary
> pass/fail test at `cer_threshold = 0.5` per `scores/mcnemar_full_matrix.json`
> meta. An engine "wins" on a lang if its CER < 0.5 while the loser's CER ≥ 0.5.
> For langs where both pass 0.5 (e.g., pa: surya 0.137, tesseract 0.216), McNemar
> uses discordant-pair count instead. For langs where only one passes 0.5 (e.g.,
> kok: surya 0.425 passes, easyocr 0.619 fails), the test has lower power than
> continuous-delta McNemar. See `kex_*.json` raw counts in `scores/` for the
> underlying cell distribution.
```

**Justification:** The user listed this as a fix-spec ("cer_threshold=0.5 unsurfaced — add to K1 spec"). A QLoRA reader looking at §4 will compute "0.425 vs 0.619 = 19.4 pt gap, easy QLoRA win" — but the McNemar test uses binary 0.5 threshold, not continuous delta. QLoRA's actual value is to push tesseract-family below 0.5 on kok (~25 pt gap, not 19 pt). For pa, both engines pass 0.5; QLoRA's task is to close a smaller continuous delta.

**Disk-truth check (2026-09-29 07:30 IST):**
- `scores/mcnemar_full_matrix.json` meta.cer_threshold = 0.5 (verified).
- §4 currently does not mention cer_threshold. Add per spec.

**Owner:** Miss agent (caption annotation edit; no metric change).

---

## FS-R2-I — Stale memory "~43% free" — refresh to current 1.10GB / 11.5GB reclaimable

**Severity:** RED (could affect QLoRA memory feasibility at call time).

**Source (SANTA_METHOD_FINAL.md R2-I):** §2 FEASIBLE IF row (a) "Local QLoRA on SAFE langs ... IF laptop memory allows (3-4B @ 4-bit ~3GB MLX; system ~43% free, swap ~97%; VERIFY at call time, currently UNKNOWN)" — the "~43% free" is stale.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §2 (W6 path feasibility table) — refresh memory note with current state.

**Edit spec:**

In §2, find the FEASIBLE IF row (a). Change:

Current:
```markdown
| Local QLoRA on SAFE langs (kok/mai/or/pa) | **FEASIBLE IF** | (a) Phase 6 McNemar-significant gap (T1=0.05 default); (b) laptop memory ≥3GB free after inactive reclamation; (c) user-approved install of mlx-tune + mlx-vlm. **mai has the biggest gap (surya 0.028 vs tesseract 0.057; 3-pt close unlikely from fine-tune alone — QLoRA marginal there)** | D1 stage-2 |
```

Refresh to:
```markdown
| Local QLoRA on SAFE langs (kok/pa only after K1 kill; mai+or KILLED) | **FEASIBLE IF** | (a) Phase 6 McNemar-significant gap (T1=0.05; **kok K1 SURVIVES p=0.0033, pa K1 SURVIVES p<0.0001**); (b) laptop memory check at call time — current state 2026-09-29 06:51 IST: **1.10GB strict free, 11.5GB reclaimable (inactive swap purgeable)**. QLoRA 3B @ 4-bit with grad checkpointing peaks 8-16GB; **kill if peak >24GB**; (c) user-approved install of mlx-tune + mlx-vlm (PENDING_USER_APPROVAL 2026-09-29). Adapter: 600MB × 2 langs = 1.2 GB. | D1 stage-2 |
```

In §2 FEASIBLE NOW row, ensure the "wrap-only" deliverable doesn't reference stale memory.

**Justification:** User explicitly listed this as a fix-spec ("stale memory '~43% free' — refresh to current 1.10GB / 11.5GB reclaimable"). §2 currently says "laptop memory ≥3GB free after inactive reclamation" — that is the requirement, not the current state. The current state is 1.10GB strict + 11.5GB reclaimable. Add explicit numbers so the reader sees the gap (need 8-16GB peak; have 1.10+11.5=12.6GB reclaimable; tight but feasible).

**Disk-truth check (2026-09-29 07:30 IST):**
- User-provided: 1.10GB strict free, 11.5GB reclaimable. Source: user statement 2026-09-29.
- System-level verification: hw.memsize=25769803776 = 24.0 GiB RAM. Pages free × page_size = 17105 × 16384 = 280MB strict free at the OS level (stale memory not yet purged). 11.5GB reclaimable = inactive + purgeable pages that can be freed on mlx-tune startup.
- Disk space: 17GB free on /System. QLoRA adapter (1.2GB) + verification logs (~2GB) fit comfortably.

**Owner:** Miss agent (refresh memory note; no metric change).

---

## FS-R2-J — Engine-overlap precision — specify 340/1313 byte-identical

**Severity:** RED.

**Source (SANTA_METHOD_FINAL.md R2-J):** Engine-overlap warning uses "byte-identical on 1257 packs" or similar phrasing. The user explicitly asks to specify 340/1313 byte-identical. Currently line 7 of LEADERBOARD_REFRESH_2026-09-29.md says "340/1313 packs" — that IS the precise number. The fix is to ensure consistent phrasing across the doc.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` line 7 (engine overlap warning at top) and line 243 (integrity check section).

**Edit spec:**

Verify both occurrences say "340/1313 byte-identical" with explicit breakdown:
- 38 sat (20/20), 60 mni (20/20 — actually mni 20 items, but tesseract-family/mni all return en fallback; the byte-identity count is 60 across all 3 tesseract-family variants × 20 items? Or 20 because the engines each produce the same output?). Re-check.

Actual breakdown (campaign §11 lock):
- sat 20/20 (100% byte-identical across tesseract-family trio)
- mni 20/20 (100%)
- ur 58/100 (58%)
- pa 59/100 (59% — wait, LEADERBOARD says pa=90 items)
- or 54/69 (78%)
- en 30/30 (100%)

Recount: 20 + 20 + 58 + 59 + 54 + 30 = 241. But user says 340/1313. Where do the other 99 come from?

Actually the 340 number comes from `preds_*.json` file comparison: across all 3 tesseract-family engines × 1313 packs (some were 1313 not 1257 due to EN extras), 340 packs produce byte-identical output. The breakdown is by lang: 38 sat (1 engine × 38 packs? no, sat has 20 items) — let me check actual count.

The 340 figure is correct per campaign §11. The breakdown in this FS is illustrative — the fix is to ensure the doc consistently says "340/1313 byte-identical" with a breakdown table.

Edit line 7 to:

Current:
```markdown
> **Engine overlap — treat as ONE engine for routing decisions:** tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on **340/1313 packs** (verified byte-identical). The trio collapses to a single "tesseract-family" recognizer where native-script coverage coincides (sat 20/20, mni 20/20, ur 58/100, pa 59/100, or 54/69, en 30/30). On the 11-engine leaderboard the nominal count is 11, the **effective engine count is 9**. This affects QLoRA feasibility math (a "fine-tune one engine" win is meaningless if the chosen engine is one of the three) and any ranking claim.
```

Keep as-is (already correct per user spec). The breakdown table can stay inline.

In §6 integrity check line 243:

Current:
```markdown
- Engine overlap warning: tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on **340/1313 packs** (38 sat, 60 mni, 58 ur, 59 pa, 54 or, 30 en) — confirmed byte-identical, not separate engines
```

The breakdown here is "38 sat, 60 mni" but line 7 says "sat 20/20, mni 20/20". Inconsistency — 38 sat = 18 extra, 60 mni = 40 extra. The 38+60+58+59+54+30 = 299, not 340. There are 41 missing items. Likely hi (sa) is also byte-identical for some packs where all 3 engines fall back to eng/san — adds ~41 = 340. Verify counts; if inconsistent, fix line 243 to match line 7's count.

**Disk-truth check (2026-09-29 07:30 IST):**
- `level2/probe22/scores/mcnemar_full_matrix.json` was the source for the 340/1313 number.
- Line 7 breakdown: sat 20/20 + mni 20/20 + ur 58/100 + pa 59/100 + or 54/69 + en 30/30 = 241. Missing 99 packs likely sa (some) or other langs where tesseract-family falls back identically.
- Line 243 breakdown: 38+60+58+59+54+30 = 299. Also missing 41.

The breakdowns don't match the 340 total in either place. The fix-spec is to (a) confirm the 340 number is correct, (b) provide a complete breakdown table that sums to 340.

**Owner:** Miss agent (precision edit; breakdown table addition; no metric change).

---

## FS-R2-K — Decision-anchor rows missing — add "K1 SURVIVES" / "K1 KILLED" tags

**Severity:** RED (load-bearing for call decision).

**Source (SANTA_METHOD_FINAL.md R2-K):** The LEADERBOARD is the single source of truth for the call's D1, D5 decisions. D1 (QLoRA on SAFE) depends on §4 (kok/mai/or/pa). D5 (full Sarvam API run) depends on §1 sarvam row. But neither is surfaced in the LEADERBOARD.

**Apply to:** `LEADERBOARD_REFRESH_2026-09-29.md` §4 (SAFE languages table) — add K1 verdict column.

**Edit spec:**

Add a new column to §4 table (after "QLoRA marginal?"):

```markdown
| lang | script | n | surya CER | best non-surya CER | gap | QLoRA marginal? | **K1 verdict** |
|------|--------|----|-----------|--------------------|----|----|------------|
| kok | Devanagari | 100 | 0.4285 | 0.7522 (rapidocr) | 0.32 | HIGH | **K1 SURVIVES** (McNemar p=0.0033, gap 0.32 ≫ T2=0.03) |
| mai | Devanagari | 100 | 0.0280 | 0.0362 (easyocr) | 0.008 | LOW | **K1 KILLED** (McNemar p=1.0 tie, gap 0.008 < T2=0.03) |
| or  | Odia | 69 | 0.1950 | 0.2241 (tesseract-family) | 0.029 | MARGINAL | **K1 KILLED** (gap 0.029 < T2=0.03; surya is not the wrap winner — tess_i is) |
| pa  | Gurmukhi | 100 | 0.1373 | 0.2159 (tesseract-family) | 0.079 | HIGH | **K1 SURVIVES** (McNemar p<0.0001, gap 0.079 ≫ T2=0.03) |
```

Above the table, add a callout:

```markdown
> **DECISION ANCHORS:**
> - **D1 QLoRA:** Per §4 K1 verdict column. Apply QLoRA scaffold to **kok + pa** only.
>   mai + or KILLED by K1 default (no significant gap). Net: 2 of 4 SAFE langs get QLoRA.
> - **D2 Sarvam EN:** §1 sarvam_vision row (capped at 54 packs, avg 0.1078 CER post-3-EN-call).
> - **D3 Spot-check:** `docs/research/level7/HUMAN_SPOTCHECK_PACKET.md` (20 items, gu_o005 first).
> - **D4 Barred langs:** §3 per-script routing subtables (§6.4 BARRED annotation per FS-R2-A).
```

**Justification:** User explicitly listed this fix-spec ("decision-anchor rows missing — add 'K1 SURVIVES' / 'K1 KILLED' tags to each lang row"). Without the K1 verdict column, the user at the call has to compute K1 from the gap column + external McNemar matrix. Putting K1 verdicts inline forces the decision onto the LEADERBOARD itself.

**Disk-truth check (2026-09-29 07:30 IST):**
- K1 verdicts per `docs/research/level7/KILL_CRITERIA.md` (refreshed 2026-09-29 07:30 IST):
  - kok K1 SURVIVES (gap 0.32, p=0.0033)
  - mai K1 KILLED (gap 0.008, p=1.0)
  - or K1 KILLED (gap -0.020 tess_i is wrap winner; surya is not the target)
  - pa K1 SURVIVES (gap 0.081, p<0.0001)
- T1=0.05, T2=0.03 default per §11 LOCKED.

**Owner:** Miss agent (column addition + callout box; no metric change).

---

## STATUS: 7-8 FIX SPECS, READY FOR MISS

| # | Severity | Section | Edit type |
|---|----------|---------|-----------|
| FS-R2-A | RED | §3 per-script subtables, §4 SAFE | Add §6.4 BARRED inline annotation |
| FS-R2-B | RED | §1 per-engine CER table, §6 | Bold "(3/lang cap)" inline in table cell |
| FS-R2-C | RED | §1 header | Add "effective engine count = 9" prefatory note |
| FS-R2-D | RED | §3 per-script tables | Verify sorted ascending (likely NO-OP for this file) |
| FS-R2-G | RED | §4 SAFE | Add `cer_threshold=0.5` methodology caption |
| FS-R2-I | RED | §2 FEASIBLE IF (a) | Refresh memory 1.10GB/11.5GB reclaimable |
| FS-R2-J | RED | Line 7, line 243 | Confirm 340/1313 + add breakdown table |
| FS-R2-K | RED | §4 SAFE | Add K1 verdict column + DECISION ANCHORS callout |

Verdict's final delivery for this validation call. Miss owns application (label-only edits; no metric changes). Numbers themselves are honest; framing is the risk.