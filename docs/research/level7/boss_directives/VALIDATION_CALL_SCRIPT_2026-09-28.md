# VALIDATION_CALL_SCRIPT_2026-09-28.md — 5-minute script for the boss

**Reading time**: 5 minutes.
**Time to make all 6 decisions**: <10 minutes.

---

## OPENING (30 sec, you read aloud)

> "OK — Level 7 48h research campaign, validation call, H44–48 window. 11 engines scored on probe22, effective 10. surya best local at CER 0.3849, wins 9/18 langs. Sarvam 0.2400 on 54-call subset is directional only. W6 feasible set: 459 items NOW, up to 801 with §6.4 verify. 6 decisions pending. I have orchestrator defaults applied. Here they are."

---

## 6 DECISIONS (you say YES or OVERRIDE for each)

### D1 — GPU budget for W6 local QLoRA?
**Orchestrator default**: **$0, wrap-only baseline**.
- Most conservative; no GPU dependency.
- mlx-tune + GLM-OCR stay on disk as references only.
- **OVERRIDE if**: you have GPU access + want local QLoRA on 459-item SFT set.
- **Decision**: ___

### D2 — Sarvam EN extension (3 calls over 54-cap)?
**Orchestrator default**: **Skip**.
- D2 already locked (sarvam_fill = probe-scoring only).
- EN data is harness-spec-mismatched per Engine's en_sanity_surya.json (all >5% CER).
- **OVERRIDE if**: you want to spend 3 Sarvam EN calls for completeness.
- **Decision**: ___

### D3 — 20-item human spot-check review?
**Orchestrator default**: **Defer to W6**.
- D3 already locked; spot-check is non-blocking.
- Available items: brx_o045 PASS, mr_o005 FAIL, ne_o038 FAIL, sd_o002 PASS, gu_o005 pending.
- **OVERRIDE if**: you want to review now.
- **Decision**: ___

### D4 — rapidocr EN fix-spec?
**Orchestrator default**: **APPROVED** (Fix Spec #4 applied 2026-09-28 21:13 IST to `run_probe.py` line 291).
- Added `_RAPID_LANGV["en"] = ("EN","PPOCRV4")`.
- Trivially reversible (one line).
- **OVERRIDE if**: you want to revert.
- **Decision**: ___

### D5 — Full Sarvam API run (1,227 items for valid "Beat 87.39" comparison)?
**Orchestrator default**: **Skip** (keep 54-call directional cap).
- Saves budget; "Beat 87.39" stays directional per OBITUARIES.md O-02..O-05.
- **OVERRIDE if**: you want to spend ~$15–30 on full Sarvam run.
- **Decision**: ___

### D6 — Sampling methodology?
**Orchestrator default**: **Accept current 1227-manifest with documented caveat**.
- Manifest = 1227 items (lock).
- True per-lang page-independence: only 7 langs hit 100 distinct pages (kok, ks, mai, mr, pa, sd, ur). Others range from 1 PDF (as/bn/hi/mni/sa/sat) to 90 (pa).
- Re-sampling for true independence requires new downloads → blocked by hard rule §0.1 (no downloads without explicit approval).
- **OVERRIDE if**: you want to approve downloads for the missing source PDFs.
- **Decision**: ___

---

## CLOSING (20 sec)

> "Locked. I'll apply any overrides to FINAL_VERDICT §8 + CALL_PACKET §5 and log §11. W5 freeze is Wed Oct 1. W6 training starts when you say go."

---

## CHEAT SHEET (if asked to justify any default)

- **Why wrap-only D1**: mlx-vlm on M2 Max 32GB fits Qwen2-VL-2B; but you haven't approved GPU budget; the 459-item SFT set trains in ~90 min if you approve. Wrap-only costs nothing and is honest-empty-correct.
- **Why skip Sarvam EN D2**: Sarvam's en_sanity_surya shows ALL engines fail EN (harness-spec mismatch). 3 extra calls give 1 datapoint.
- **Why defer spot-check D3**: D3 already locked for W6; 4 of 5 ceiling-sample items already verified on disk (brx_o045 PASS, mr_o005 FAIL, ne_o038 FAIL, sd_o002 PASS); only gu_o005 pending.
- **Why approve rapidocr EN D4**: one-line map; trivially reversible; unblocks 30 EN sanity packs for rapidocr.
- **Why skip full Sarvam D5**: 1227 calls × $0.01–0.03 = $12–37; OBITUARIES.md already locks all 4 per-lang Sarvam scores as DEAD-for-decisions.
- **Why accept sampling D6**: alternative is downloads (blocked); document the caveat instead.

---

*Built by orchestrator 2026-09-28 22:06 IST. Read aloud at the call. Make overrides by saying "D3 OVERRIDE: <your choice>" or similar.*
