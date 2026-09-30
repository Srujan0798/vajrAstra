<!-- RECOVERED 2026-09-30 from db part prt_0f196fd40001H00nJ35R0l7c4K (opencode read, 2026-09-30 14:43), read at 18:05; any later edits are lost -->
# Abstention Calibration Audit — H48 Post-Validation

**Date**: 2026-09-28 H48 (~18:00 IST)
**Auditor**: Verdict Agent (Santa-method H48 hostile pass)

---

## 1. Engine-by-Engine Honest-Empty Analysis

| Engine | Total Packs | Honest-Empty | % Empty | Expected per D4 (n<50 = no winner) | Flag |
|--------|-------------|--------------|---------|-----------------------------------|------|
| **rapidocr** | 1,370 | 486 | 35.5% | 7 langs with 100% empty (bn, pa, mni, sat, as, gu, or) + en=30 | **LOW-COVERAGE ENGINE** (>20% on n≥50 langs: bn 100%, pa 100%) |
| **surya** | 1,227 + 30 EN = 1,257 | 129 | 10.3% | sa=100% honest-empty (Surya 2 NO Ol Chiki) - CORRECT | sa=100% empty is CORRECT (Surya 2 NO Ol Chiki support) |
| **sarvam_vision** | 54 | 0 | 0% | 3/lang cap respected (54/18=3) | CAP RESPECTED |
| **paddleocr_indic** | 1,227 | 536 | 43.7% | 12 langs empty (gu, brx, doi, as, bn, etc.) | **LOW-COVERAGE ENGINE** (>20% on n≥50) |
| **rapidocr EN** | 30 | 30 | 100% | EN not in manifest | 0/30 empty (EN not in probe) |
| **easyocr** | 1,227 | 0 | 0% | All 18 langs have output | CLEAN |
| **tesseract_indic** | 1,257 | 1 | ~0% | Only 1 empty | CLEAN |
| **tesseract_bilingual** | 1,259 | 1 | ~0% | Only 1 empty | CLEAN |
| **openbharatocr** | 1,257 | 1 | ~0% | Exact dup of tesseract_indic | CLEAN |
| **tesseract_indic** | 1,257 | 1 | ~0% | Only 1 empty | CLEAN |
| **doctr** | 1,257 | 1 | ~0% | Only 1 empty | CLEAN |
| **indicphotoocr** | 1,257 | 2 | ~0% | Only 2 empty | CLEAN |
| **anuvaad_tesseract** | 1,257 | 647 | 51.5% | 10 langs empty (only Devanagari+Eng) | **LOW-COVERAGE ENGINE** |
| **sarvam_vision** | 54 | 0 | 0% | 3/lang cap = 54 calls | CAP RESPECTED |

---

## 2. Per-Language Abstention Summary (n≥50 only)

| Lang | rapidocr | paddleocr_indic | anuvaad_tesseract | surya | Flag |
|------|----------|-----------------|-------------------|-------|------|
| bn (n=100) | 100% empty | 100% empty | 100% empty | 0% | rapidocr + paddleocr + anuvaad = **LOW-COVERAGE** |
| pa (n=90) | 100% empty | 100% empty | 100% empty | 0% | rapidocr + paddleocr + anuvaad = **LOW-COVERAGE** |
| gu (n=20) | 100% empty | 100% empty | 100% empty | 0% | All three = **LOW-COVERAGE** |
| or (n=69) | 100% empty | 100% empty | 100% empty | 0% | All three = **LOW-COVERAGE** |
| as (n=19) | 100% empty | 100% empty | 100% empty | 0% | n<50 but all three empty |
| mni (n=20) | 100% empty | 100% empty | 100% empty | 100% | ALL FOUR empty |
| sat (n=20) | 100% empty | 100% empty | 100% empty | 100% | ALL FOUR empty |
| ne (n=37) | 54% empty | 100% empty | 100% empty | 0% | n<50 but high abstention |
| ks (n=100) | 0% | 0% | 100% empty | 0% | anuvaad = **LOW-COVERAGE** |

---

## 3. LOW-COVERAGE ENGINE FLAGS (>20% honest-empty on n≥50)

| Engine | Languages with >20% empty (n≥50) | Verdict |
|--------|----------------------------------|---------|
| **rapidocr** | bn 100%, pa 100%, gu 100%, or 100%, as 100% | **FLAG** |
| **paddleocr_indic** | bn 100%, pa 100%, gu 100%, or 100%, as 100%, brx 100%, doi 100% | **FLAG** |
| **anuvaad_tesseract** | bn 100%, pa 100%, gu 100%, or 100%, ks 100%, ur 100%, sd 100%, mni 100% | **FLAG** |

---

## 3. Surya sa=100% Honest-Empty — CORRECT

**Surya sa=100% honest-empty is CORRECT** — Surya 2 has NO Ol Chiki support (verified NOT in 91-lang benchmark). This is honest-empty by design, not a bug.

**Evidence**: Surya 2 official 91-language benchmark table does not include Ol Chiki (Santali script). `sa_d029` empty prediction confirmed by spot-check.

---

## 4. Sarvam Vision Cap — RESPECTED

| Metric | Value |
|--------|-------|
| Total calls | 54 |
| Cap | 3/lang × 18 langs = 54 |
| Status | **CAP RESPECTED** |

---

## 3. Per-Language CER Reliability (Abstention-Adjusted)

| Lang | Engine | Raw CER | Honest-Empty % | Reliability |
|------|--------|---------|----------------|-------------|
| bn | rapidocr | 1.000 | 100% | UNRELIABLE |
| bn | paddleocr_indic | 1.000 | 100% | UNRELIABLE |
| bn | anuvaad_tesseract | 1.000 | 100% | UNRELIABLE |
| pa | rapidocr | 1.000 | 100% | UNRELIABLE |
| pa | paddleocr_indic | 1.000 | 100% | UNRELIABLE |
| pa | anuvaad_tesseract | 1.000 | 100% | UNRELIABLE |
| gu | rapidocr | 1.000 | 100% | UNRELIABLE |
| gu | paddleocr_indic | 1.000 | 100% | UNRELIABLE |
| gu | anuvaad_tesseract | 1.000 | 100% | UNRELIABLE |
| or | rapidocr | 1.000 | 100% | UNRELIABLE |
| or | paddleocr_indic | 1.000 | 100% | UNRELIABLE |
| or | anuvaad_tesseract | 1.000 | 100% | UNRELIABLE |
| ks | anuvaad_tesseract | 1.000 | 100% | UNRELIABLE |

---

## 4. D4 Abstention Calibration Check

Per D4 (campaign §10): n<50 = no winner claim.

| Lang | n | Engines with >50% empty | Winner Claim Safe? |
|------|---|------------------------|-------------------|
| as (19) | 3 engines 100% empty | **NO** (n<50) |
| mni (20) | 4 engines 100% empty | **NO** (n<50) |
| sat (20) | 4 engines 100% empty | **NO** (n<50) |
| ne (37) | 3 engines high empty | **NO** (n<50) |
| gu (20) | 3 engines 100% empty | **NO** (n<50) |
| doi (27) | paddleocr 100% empty | **NO** (n<50) |
| brx (67) | paddleocr 100% empty | **CAUTION** (n≥50 but 1 engine empty) |
| ks (100) | anuvaad 100% empty | **CAUTION** (anuvadd only) |
| bn (100) | 3 engines 100% empty | **CAUTION** (3 engines) |
| pa (90) | 3 engines 100% empty | **CAUTION** (3 engines) |

**Conclusion**: No winner claims for n<50 cells (as, mni, sat, ne, gu, doi). For n≥50 cells with high abstention, winner claims should be suppressed or footnoted.

---

## 5. D4 Micro-Repair Check (sat/ks)

Per D4: micro-repair ONLY sat+ks (5-10 pages each) if W5 freeze-safe.

| Cell | Current State | Micro-Repair Feasible? |
|------|---------------|------------------------|
| sat | 0 engines emit Ol Chiki; all emit Latin gibberish | Only if tesseract sat.traineddata exists (404 upstream) + D4 curation |
| ks | rapidocr 71% Arabic share; easyocr urdu.pth available | Promising — easyocr urdu.pth loads cached arabic.pth with Urdu charset |

**Sat micro-repair blocked**: tesseract sat.traineddata DOES NOT EXIST upstream (404 across tessdata/best/fast).

---

## Summary

| Category | Count |
|----------|-------|
| Engines with >20% honest-empty on n≥50 | 3 (rapidocr, paddleocr_indic, anuvaad_tesseract) |
| Languages with n<50 (no winner claims) | 6 (as, mni, sat, ne, gu, doi) |
| Languages n≥50 with high abstention | 4 (bn, pa, gu, or) |
| Surya sa=100% empty | **CORRECT** (Surya 2 NO Ol Chiki) |
| Sarvam cap (54 calls) | **RESPECTED** |

**Recommendation**: Leaderboard must footnote LOW-COVERAGE engines and suppress winner claims for flagged cells per §6.7.

---

*Audit complete. Results logged to engine_health_log.jsonl.*