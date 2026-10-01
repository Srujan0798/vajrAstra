# W1 ROUND-2 FIX-SPECS — proto-64 meeting-day finish (2026-09-30)

**Author:** Sonnet lead (composition from `1G_verify.md` round-2 proposals, proto-62 rule 2, and lead measurements).
**Applies to:** `./VINAY_MEETING_PACKET.md` (root, the corrected one) only. `docs/campaign/DRAFT_RESEARCH_PLAN.md` is updated separately.
**Pre-image:** `_archive/pre_fix_2026-09-30/VINAY_MEETING_PACKET.md` (sha256 recorded in the apply log).
**Law:** Verdict specifies, Miss applies, Verdict re-verifies. Max 2 rounds. All OLD strings verified `count == 1` before writing this file.

---

### GT-01 · BLOCKER · `VINAY_MEETING_PACKET.md:119`
- **OLD (exact):**
```
- **Headline win:** Wrap-only routing (already on disk) **is competitive with Sarvam on the cells we measured (n=3/lang, directional)**, and Sarvam's own published weak cells are Kashmiri 54.82, Odia 80.01 and Santhali 53.91 — not Konkani, where Sarvam scores 97.41 on their Indic OCR Bench. Note Ol
```
- **NEW (exact):**
```
- **Headline, stated honestly:** On the **18 human-verified items** where Sarvam ran (9 `official_pair_txt` + 9 `sarvam_bench`), **Sarvam's CER is 2.5x lower than our best local engine** (0.171 vs 0.430). Our engines only lead on **PDF-text-layer GT (n=36)**, which may favour layout-literal output. Every one of our 21 item-level wins over Sarvam falls in that PDF-layer tier and **none** in either human-verified tier. n is 3 per language — directional, not a result. Sarvam's own published weak cells are Kashmiri 54.82, Odia 80.01 and Santhali 53.91 — not Konkani, where Sarvam scores 97.41 on their Indic OCR Bench. Note Ol
```
- **EVIDENCE:** `sheet.csv` x `manifest.json` `gt_source`, the 54 Sarvam-paired items, stratified by tier (lead re-measurement, agrees with proto-62's monitor table):
  `official_pair_txt` n=9 sarvam 0.064 / surya 0.535 / best-local 0.243 · `official_pdf_layer` n=36 sarvam 0.311 / surya 0.229 / best-local 0.229 · `sarvam_bench` n=9 sarvam 0.278 / surya 0.730 / best-local 0.617.
  Pooled over the two human-verified tiers: n=18, sarvam **0.1711**, best-local **0.4296**, ratio **2.51x**.
  Item-level `surya < sarvam` by tier: `{'official_pdf_layer': 21}` — and **nothing** in the other two tiers.
- **WHY:** This is the sentence Vinay reads first, and the pooled form of it is the most misleading claim in the packet. proto-62 rule 1 forbids pooled cross-tier comparisons. Every headline number in the campaign is computed from `sheet.csv`, so proto-61's meeting-day note applies: "CER as stored by the probe scoring pass; independent re-derivation is in progress."

### GT-02 · MAJOR · `VINAY_MEETING_PACKET.md:118` (the 1,227 / 1,283 sentence)
- **OLD (exact):** `**1,227 = scored base set; manifest = 1,283 (+56 unscored additions).**`
- **NEW (exact):** `**1,227 = scored base set; manifest = 1,283. The 56 extra manifest items are listed in `manifest_additions.json`, which is a SUBSET of `manifest.json` (exactly the 56 unscored items) — not 56 additional items, so the two files must never be added together.**`
- **EVIDENCE:** lead re-measurement — manifest image_ids 1,283; `manifest_additions.json` image_ids 56; **already present in manifest 56; genuinely new 0**; `additions == manifest-minus-scored` → `True`.
- **WHY:** `len(manifest) + len(additions)` = 1,339 and is wrong. Stated once, precisely, so nobody double-counts in the meeting.

### DP-01 · MAJOR · `VINAY_MEETING_PACKET.md:101,103,105,106` (anchors table — 4 dead paths)
- **OLD (exact):** `| \`W5_STRATEGY_OPTIONS.md\` | 3 ranked options + ranking rationale | — |`
- **NEW (exact):** `| \`docs/architecture/W5_STRATEGY_OPTIONS.md\` | 5 ranked options (A–E), ranks D first — Verdict edition | — |`
- **OLD (exact):** `| \`EVIDENCE_SUMMARY.md\` | Disk-truth findings + McNemar gaps | — |`
- **NEW (exact):** `| \`_reports/cleanup_cycle1/EVIDENCE_SUMMARY.md\` | Disk-truth findings + McNemar gaps | moved from repo root 2026-09-29 |`
- **OLD (exact):** `| \`LEVEL7_RESEARCH_FINDINGS.md\` | Top methods ranked (ScriptMoE, Chitrapathak-2, Sarvam 2.1) | — |`
- **NEW (exact):** `| \`_reports/research/LEVEL7_RESEARCH_FINDINGS.md\` | Top methods ranked (ScriptMoE, Chitrapathak-2, Sarvam 2.1) | moved from repo root 2026-09-29 |`
- **OLD (exact):** `| \`COMPUTE_BUDGET_ESTIMATE.md\` | $0 cost breakdown + memory budget | — |`
- **NEW (exact):** `| \`_reports/cleanup_cycle1/COMPUTE_BUDGET_ESTIMATE.md\` | $0 cost breakdown + memory budget | moved from repo root 2026-09-29 |`
- **EVIDENCE:** `ls EVIDENCE_SUMMARY.md LEVEL7_RESEARCH_FINDINGS.md COMPUTE_BUDGET_ESTIMATE.md W5_STRATEGY_OPTIONS.md` at repo root → all absent; the four replacements exist (verified 2026-09-30). Also `docs/research/level7/W5_STRATEGY_OPTIONS.md` is a DIFFERENT 3-option shortlist recommending A — the root path was ambiguous and is now disambiguated to the 5-option Verdict edition.
- **WHY:** Every "disk-truth anchor" Vinay is told he can verify was a dead path. He will follow a citation into nothing.

### DP-02 · MINOR · `VINAY_MEETING_PACKET.md:269,279` (reading order — 2 dead paths)
- **OLD (exact):** `4. **\`W5_STRATEGY_OPTIONS.md\`** (root) — 3 ranked options + ranking rationale.`
- **NEW (exact):** `4. **\`docs/architecture/W5_STRATEGY_OPTIONS.md\`** — 5 ranked options (A–E), ranks D first. (The 3-option shortlist recommending A is at `docs/research/level7/W5_STRATEGY_OPTIONS.md`.)`
- **OLD (exact):** `4. \`W5_STRATEGY_OPTIONS.md\` if a fuller ranking is wanted (10 min)`
- **NEW (exact):** `4. \`docs/campaign/DRAFT_RESEARCH_PLAN.md\` §5 if the option comparison is wanted (10 min)`
- **EVIDENCE:** the bare root path does not exist; the draft plan now carries the side-by-side option comparison.
- **WHY:** Last line of the reading order must point at something that exists.

### SM-01 · MAJOR · `VINAY_MEETING_PACKET.md:34` (the "tomorrow" stale pointer in the TL;DR)
- **OLD (exact):** `> Lead with the 3 strategic questions; the option picker is in \`W5_STRATEGY_OPTIONS.md\` if you want it after.`
- **NEW (exact):** `> Lead with the 3 strategic questions; the option picker is in \`docs/architecture/W5_STRATEGY_OPTIONS.md\` if you want it after. The draft research plan for cross-questioning is \`docs/campaign/DRAFT_RESEARCH_PLAN.md\`.`
- **EVIDENCE:** root `W5_STRATEGY_OPTIONS.md` absent; `docs/campaign/DRAFT_RESEARCH_PLAN.md` exists (15,181 B).
- **WHY:** The TL;DR is the first thing read and it pointed at a dead path plus omitted the document Vinay was actually asked to review.

---

## Round-2 status of the earlier 39 specs (1G_verify.md)

**Verified on disk 2026-09-30 by the lead: 0 of 39 have a live OLD string.** The residuals 1G_verify reported are all resolved:
`Tue 2026-09-30` ×2 → **0 hits** · `9/18` ×4 → **0 hits** · `Wed 2026-10-01` ×6 → **0 hits** · `Sat 2026-10-04` → **0 hits** ·
FS-50's introduced "7 of the 12 but lists 6" → the line now lists 7 (pa 0.145, brx 0.165, sa 0.175, mr 0.205, hi 0.220, or 0.259, sd 0.315) and the lead re-measured the band as **exactly 7 of 12** ·
the D4 backbone cell now reads "OmniDocBench table does not list it" ·
`pa NOT significant vs runner-up (p=1.00, n=90)` is already correct at 5 sites.
The Konkani claim no longer asserts Konkani is a Sarvam weak cell (line 119 now says "not Konkani, where Sarvam scores 97.41").
**Not re-verified by a second reviewer** — flag for the round-2 Verdict pass.

---

## APPLY LOG (proto-64, 2026-09-30)

Pre-image: `_archive/pre_fix_2026-09-30/VINAY_MEETING_PACKET.md`, sha256 `59919233c2bfe0adef5c80c315db71434e0ded25e3651369f50a98efdcd6eaa5`.

| spec | result |
|---|---|
| GT-01 GT-tier stratified headline | APPLIED (after correcting a truncated OLD string; the full line was re-read and replaced exactly) |
| GT-02 additions-is-a-subset | APPLIED at **both** sites (L89 and L118) — the same false claim appeared twice |
| DP-01 4 dead anchor paths | APPLIED ×4 |
| DP-02 2 dead reading-order paths | APPLIED ×2 |
| SM-01 TL;DR dead path + missing plan pointer | APPLIED |
| post-verify oracle disclosure (GT-01) | APPLIED after the 1F review found "best local engine" was an oracle |

**False-pattern sweep on the corrected packet:** `Beats Sarvam on 9/18` 0 · `beats Sarvam on 9/18` 0 · `Tue 2026-09-30` 0 · `Sat 2026-10-04` 0 · `Wed 2026-10-01` 0 · `9/18` 0.
**Residual UNRESOLVED, escalated to the boss (fix loop max 2 rounds reached):**
1. `K2` provenance conflict — our audit says pa p=1.00 vs tesseract_indic (n=90); `W6_QLORA_SPEC.md:75` says "p<0.0001 SURVIVES". Both cannot be true. Not asserted either way in the plan; tagged UNRESOLVED.
2. Pooled "10/18" — the lead's reproducible computation and directive A3 both give 10/18 (surya-always **and** best-fixed-per-language); one reviewer reported 8/18 from the same file and it did not reproduce. CONTRADICTION, unreproduced side recorded. The plan no longer relies on the pooled figure — it uses the GT-tier split.
3. GLM-OCR's presence in OmniDocBench v1.6 — two reviewers disagree (absent vs present at 94.71 rank 3). Tagged CONTRADICTION/UNKNOWN.
4. Indic-OCR pack contents for `sat`/`mni` never opened. UNKNOWN; blocks the U7 approval's value estimate.
