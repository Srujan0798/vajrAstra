# W5 Freeze Window Plan

**Engine agent · 2026-09-29 (W5 freeze prep) · Freeze call after Wed 2026-10-01**

---

## 1. Timeline

| Date | Phase | Owner | Status |
|---|---|---|---|
| **2026-09-29 (Mon)** | Campaign clock end H48 (Level 7 research freeze). All 3 agents hand off disk state. | All | DONE — W6_HANDOFF.md shipped |
| **2026-09-30 (Tue)** | Quiet day. Optional: W5 micro-repair on sat+ks (D4 — only if freeze safety allows). | Verdict, Miss | TBD per user |
| **2026-10-01 (Wed)** | **Human lead returns.** Freeze call window opens. | User, all 3 agents | upcoming |
| **2026-10-01 + 1 day** | Wrap-only pipeline + QLoRA tools install decision (D1 stage-2 gate). | User | upcoming |
| **2026-10-01 + 2-3 days** | W6 QLoRA scaffold launch on SAFE langs (kok + pa priority). | Engine | upcoming |
| **2026-10-01 + 4-5 days** | W6 fine-tune + eval + leaderboard polish for hackathon submission. | All | upcoming |

---

## 2. Pre-freeze checklist (status as of 2026-09-29)

**Total items: 18** (14 PASS, 3 PENDING_USER_APPROVAL, 1 honest-empty) — refreshed 2026-09-29 16:22 IST after user APPROVED install + memory reclaim at the W5 freeze call. mlx-tune + mlx-vlm now PASS.

### Disk state (12 PASS)

- [x] **`sheet.csv` frozen at 12,324 rows.** Engine-side baseline locked (1,227 items × ~10 engines + sarvam 54).
- [x] **`manifest.json` at 1,283 items** (mr/pa/sd re-sourced to 100). 56 new items deferred to W6 freeze call re-run.
- [x] **11 engines scored, 0 error packs each.** rapidocr, tesseract_bilingual, tesseract_indic, openbharatocr, anuvaad_tesseract, indicphotoocr, surya, easyocr, paddleocr_indic, doctr, sarvam_vision.
- [x] **`level2/out/` sealed.** South 400 result untouched this session (and every prior session).
- [x] **`level2/reports/` sealed.** LEADERBOARD.md, CER_BY_SCRIPT.md not modified by this agent (engine-side leaderboard lives at `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md`).
- [x] **§6.4 GT verification locked.** BARRED list stands: ks 0%, mni 0%, ur 10%, sat 15%, mr 42.9%, ne PDF-tier. SAFE pending §6.2: as 100%, brx 95.8%, doi 100%, kok 100%, mai 90%, or 91.7%, pa 100%. VERIFY-FIRST: gu 85.7%, sd 85.7%.
- [x] **Lane A research closed** (984 records, ≥400 target met). Verdict's sample-check valid against this set.
- [x] **Lane C research closed** (436 records, ≥400 target met). Miss owns.
- [x] **Engine overlap documented.** tesseract_bilingual ≡ tesseract_indic ≡ openbharatocr on 340/1313 packs (byte-identical). Effective engine count 9 not 11.
- [x] **OCR processes cleared** (0 active). No zombie leak.
- [x] **EN sanity column at 0/30 for engine routing reasons** (rapidocr EN root-caused: `_RAPID_LANGV` lacks "en"). Fix spec in MISS_MONITOR; needs mlx-tune-style user approval to enable. Not a freeze blocker.
- [x] **QLoRA readiness re-verified** (this session): disk 17 GB ✓, Python 3.11.10 ✓, Xcode CLI ✓, git ✓.

### PENDING_USER_APPROVAL (3)

- [x] **`mlx-tune` clone + install** (D1 stage-2 QLoRA tool). **DONE 2026-09-29 16:22 IST** — cloned to `/tmp/mlx-tune`, `pip install -e .` succeeded (v0.6.0). Log: `level2/probe22/MLX_INSTALL_RESULT.md`.
- [x] **`mlx-vlm` install** (D1 stage-2 VLM serving). **DONE 2026-09-29 16:22 IST** — pip install v0.7.4, all transitive deps resolved. Log: `level2/probe22/MLX_INSTALL_RESULT.md`.
- [ ] **System memory headroom increase** (optional). User can quit Chrome / Brave / WhatsApp to free ~3.5 GB active RSS — see `MEMORY_AUDIT.md` §3 for PIDs. Manual, not auto-actionable. Memory reclaim via `purge` ran; PARTIAL (sudo required for full purge); reclaimable pool ~9.4 GB sufficient for 3-4B @ 4-bit run.
- [ ] **W6 micro-repair on sat+ks** (D4, 5-10 curated pages each). ONLY if W5 freeze is safe. D4 stands: mni/mr/ur no repair; ne PDF-tier stays BARRED.
- [ ] **W6 backbone download** (GLM-OCR 0.9B or Qwen2.5-VL-3B). Separate approval gate; NOT part of mlx-stack install (mlx-stack is the tool layer; backbone is the model weights).

### Honest-empty (1)

- [ ] **Sarvam EN calls beyond 54-call cap** — D2 SKIPPED (no decision impact); EN column = 0/30 packs, 9 engines on EN. Permanent note in EN matrix.

---

## 3. Freeze call agenda (15-20 min human session)

**Total agenda items: 8** (all derived from locked decisions D1-D4 + campaign §11)

### Section A: Confirmation of disk truth (3 min)

1. **Engine view** — sheet.csv frozen at 12,324 rows, 0 errors, manifest 1,283 items, 11 engines scored. **Decision needed:** confirm 12,324-row lock holds, or run additional engine passes on the 56 new mr/pa/sd items now.

### Section B: W6 path (D1, 5 min)

2. **Wrap-only baseline** — locked D1 stage-1 deliverable. Surrogate: per-script routing in `LEADERBOARD_REFRESH_2026-09-29.md` §5 (surya primary everywhere except Ol Chiki where indicphotoocr wins). **Decision needed:** confirm wrap-only ships before QLoRA stage-2.

3. **QLoRA scaffold** — D1 stage-2 conditional on:
   - Phase 6 McNemar gap on SAFE langs (kok/mai/or/pa) — defaults T1=0.05, T2=3pt
   - User approves mlx + mlx-vlm + mlx-tune install
   - Memory holds at launch time (re-check `vm_stat` before any model load)
   - **Decision needed:** approve install now, or defer until after wrap-only ships?

4. **Kill criteria thresholds** — K1 (QLoRA McNemar p), K2 (micro-repair time gate), K3 (Wilson CI routing drop). Defaults: T1=0.05, T2=3pt, 6h repair window. **Decision needed:** user sets these at the call.

### Section C: Weak-cell attack plan (D4 + §11, 3 min)

5. **Santali (Ol Chiki, 53.91)** — total capability gap. Only indicphotoocr (0.504) and sarvam (0.41 cap) have any signal. D4 micro-repair (5-10 pages) is the only local lever. **Decision needed:** approve sat+ks micro-repair now, or defer?

6. **Kashmiri (Nastaliq, 54.82)** — partial capability. Rapidocr 71% Arabic share, tesseract-family ~40-42%. D4 micro-repair (5-10 pages) plus easyocr urdu.pth Nastaliq route. **Decision needed:** same as sat.

7. **Barred languages** — ks, mni, ur, sat, mr, ne-PDF-tier. All stay excluded from W6 fine-tune. Compete via wrap pipeline + official scoring. **Decision needed:** confirm no exceptions.

### Section D: Spot-check + Sarvam (D3, D2, 2 min)

8. **20-item human spot-check** (D3) — Verdict has packet ready; first item is gu_o005 (only W6-relevant). Rest are confirmation-only for already-barred langs. **Decision needed:** run at the call, or defer to post-call?

---

## 4. Post-freeze: W6 training tree (FEASIBLE NOW / FEASIBLE IF / INFEASIBLE)

### FEASIBLE NOW (zero user gate after freeze)

| Item | Verdict | Disk evidence | Engine owner |
|---|---|---|---|
| Wrap-only pipeline (D1 stage-1) | DELIVERABLE | per-script routing table, all 11 engines scored | Engine |
| Lane A/B/C research integration | DELIVERABLE | 984 + 346 + 436 records | Verdict (integration) |
| Per-engine kill from routing (K3) | AVAILABLE | Wilson CI upper bound > next-best point estimate → drop | Verdict (decision) |
| Sarvam 3 more EN calls (D2) | DEAD / moot | D2 SKIPPED; 3 calls saved | n/a |

### FEASIBLE IF (gated on user approval)

| Item | Trigger | Engine owner |
|---|---|---|
| Local QLoRA on SAFE langs | (a) Phase 6 McNemar-significant gap (T1=0.05); (b) ~~user approves mlx + mlx-tune + mlx-vlm install~~ **DONE 2026-09-29**; (c) memory holds at launch | Engine (QLoRA tools installed; scaffold prep-only done) |
| sat/ks micro-repair (5-10 pages) | W5 time permits after freeze; pages pass purge-era gates | Verdict (D4 owner) |
| W6 backbone download (GLM-OCR 0.9B) | User explicitly approves the model weights download (separate gate; mlx-stack is installed but weights are not) | Engine (after install) |
| 20-item spot-check at call (D3) | Verdict runs packet; user reviews | Verdict |
| Optional memory cleanup | User quits Chrome / Brave / WhatsApp manually | User (manual) |

### INFEASIBLE UNDER CURRENT RULES

| Item | Law | Reason |
|---|---|---|
| Cloud GPU rental | §0 hard rule 1 + standing no-money law | No budget, no approval |
| New backbone invention | §9 hard rule | Architecture research is locked |
| Fine-tune on barred langs | §6.4 lock + D4 | Garbage-GT or no signal |
| sarvam_fill in SFT/RLVR | §9 hard rule | Machine GT, never training data |
| Body-paid API runs beyond 54 calls | D2 + §6.8 | No budget |

---

## 5. W6 training (if D1 stage-2 launches)

| Step | Target | Tool | Time estimate |
|---|---|---|---|
| 1. mlx-stack + mlx-vlm + mlx-tune install | **DONE 2026-09-29** (mlx 0.32.3, mlx-vlm 0.7.4, mlx-tune 0.6.0, mlx-lm 0.31.3, mlx-embeddings 0.1.0, mlx-audio 0.5.7) | pip + git clone | ~10 min |
| 2. GLM-OCR 0.9B weights download | approved user gate | mlx_vlm.convert | ~5 min (4-bit) |
| 3. QLoRA scaffold on SAFE subset | kok + pa priority | mlx-tune | ~6 h compute |
| 4. Eval on probe22 (n=1280 items) | measure gap closure | metrics.py + sheet.csv | ~30 min |
| 5. Phase 6 estimator-law gates | McNemar + Wilson 95% CI | campaign §11 | ~15 min |
| 6. Leaderboard + report update | ship final W6 deliverable | all | ~30 min |

**Total wall time if D1 stage-2 launches:** ~7-8 h, fits in a single workday.

---

## 6. Risks and mitigations

| Risk | Mitigation |
|---|---|
| User does not return on Wed 2026-10-01 | Wrap-only ships regardless; QLoRA waits |
| mlx-tune install fails | Fallback: hand-rolled QLoRA script using mlx directly |
| Memory headroom insufficient at `vm_stat` re-check | Abort; user decides to quit apps; re-check; or defer |
| McNemar gap absent on SAFE langs | Kill QLoRA at the K1 gate (campaign §11); wrap-only ships |
| Micro-repair pages fail purge-era gates | Kill micro-repair at K2 (campaign §11) |
| Sat micro-repair reveals Ol Chiki is unsalvageable locally | Vision-LLM-only or W6 fine-tune target (sarvam or local QLoRA on sat GT) |

---

## 7. Honest-empty register

- **W5 timing is contingent on user's actual return date.** If user returns later than Wed 2026-10-01, all "Wed 2026-10-01 + N" rows shift with it.
- **Micro-repair (D4 sat+ks) is OPTIONAL.** D4 says "ONLY if W5 freeze is safe" — meaning the freeze is the higher-priority deliverable. Do not let micro-repair slip the freeze.
- **W6 backbone choice is GLM-OCR 0.9B primary.** `INTEGRATED-ELITE-STACK.md` line 29 records this. If user prefers Qwen2.5-VL-3B or MonkeyOCRv2 instead, swap at the freeze call — Verdict owns the spec.
- **The 20-item spot-check first item is gu_o005** because gu is the only W6-relevant VERIFY-FIRST language. Other items are confirmation-only — they do not change routing decisions because those languages are already barred or safe.

---

## 8. Cross-references

- `OCR_AGENT_MEMORY_FEED.md` §9, §10, §11 — process law, state, log
- `level2/probe22/AGENT_PROTOCOL.md` §0-§10 — execution law, §6.4 GT verdicts LOCKED
- `docs/research/LEVEL7_RESEARCH_CAMPAIGN.md` §1, §10, §11 — 3-agent ops, D1-D4 LOCKED, call prep
- `W6_HANDOFF.md` — earlier Engine handoff (this session)
- `level2/probe22/QLORA_READINESS.md` — disk + memory + tools gate (this session)
- `level2/probe22/MEMORY_AUDIT.md` — disk-truth memory snapshot (this session)
- `level2/probe22/MLX_INSTALL_PLAN.md` — install plan with user approval gate (this session)
- `level2/probe22/LEADERBOARD_REFRESH_2026-09-29.md` — engine-side leaderboard, polished this session
- `INTEGRATED-ELITE-STACK.md` — tool map

---

**End of plan.**