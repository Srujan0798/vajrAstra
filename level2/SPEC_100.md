# 🎯 VAJRASTRA 100/10 MASTER SPECIFICATION
## The Ultimate Specification for Beating Sarvam AI & Reaching #1 in India

---

<div align="center">

![Status](https://img.shields.io/badge/Status-68%25%20Complete-orange)
![Seal](https://img.shields.io/badge/Seal-11%2F11_GREEN-brightgreen)
![Sarvam_Gap](https://img.shields.io/badge/Sarvam_Gap-3.5%C3%97_worse-red)
![Completion](https://img.shields.io/badge/Completion-68%25-yellow)

**VAJRASTRA 100/10 MASTER SPECIFICATION v1.0**  
*Single Source of Truth for Beating Sarvam AI & Reaching #1 in India*  

**Project:** vajrAstra South / Vaultstack AI / BHASHINI AksharDrishti  
**Auditor:** ETERNAL VALIDATOR (read-only, disk-truth only)  
**Date:** 2026-09-14  
**Standard:** 100/10 = Beat Sarvam AI per-language on our corpus  
**Completion Law:** Never claim "done" until Sarvam is #2 and Vaultstack is #1  
**Last Audit:** 2026-09-14 (Eternal Validator — disk-truth only)

---

</div>

---

## 📊 EXECUTIVE DASHBOARD

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1f77b4', 'edgeLabelBackground':'#f0f0f0'}}}%%
graph TB
    subgraph "CURRENT STATE [68%]"
        A[4000/4000 Packs Sealed] -->|11/11 Gates GREEN| B[LEVEL2_SEALED=TRUE]
        C[15/22 Pillars Done] --> D[68% Complete]
        E[Sarvam Gap: 3.5x CER] --> F[30-70pp Accuracy Gap]
    end
    
    subgraph "MISSING PILLARS [7/22]"
        G[P16: Accuracy ≥ Sarvam] -->|3.5x worse CER| H[Gap: 30-70pp]
        I[P17: Akshara Loss] -->|Missing| J[No schema/trainer]
        K[P18: SCST RL on CER] -->|Missing| L[No RL trainer]
        M[P19: SimPO/DPO] -->|Partial 126/50K| N[Need 50K+ pairs]
        O[P20: Learned Preproc] -->|Missing| P[OpenCV only]
        Q[P21: Layout Model] -->|Missing| R[400 L1 gold, no trainer]
        S[P22: Prod Serving] -->|Missing| T[No Triton/K8s/API]
    end
    
    subgraph "TARGET: 100/10"
        U[Beat Sarvam on All 4 Languages] --> V[CER < Sarvam per-lang]
        W[Production API] --> X[₹0.5/page, p99<2s]
        Y[100/10 ACHIEVED] --> Z[VAULTSTACK #1]
    end
    
    F --> U
    H --> U
    J --> U
    L --> U
    N --> U
    P --> U
    R --> U
    T --> U
    V --> X
    X --> Y
```

---

## 📊 EXECUTIVE DASHBOARD

```mermaid
graph LR
    subgraph "SEALED BENCHMARK [100%]"
        A1[4000/4000 Packs] -->|10 Engines × 400| A2[100% Coverage]
        A3[11/11 Gates GREEN] --> A4[LEVEL2_SEALED=TRUE]
        A5[Schema: 0 Violations] --> A6[Schema Clean]
        A7[Manifest 400/400 Valid] --> A8[Zero Locked PDFs]
    end
    
    subgraph "TRUTH LAYER [100%]"
        B1[Single-Writer: report.py] --> B2[One Truth]
        B3[Auto-Stamp: generated_at] --> B4[Freshness Guaranteed]
        B5[Seal Gates: 11/11 GREEN] --> B6[Seal Valid]
    end
    
    subgraph "HONESTY LAYER [100%]"
        C1[Engine Honesty: 10/10] --> C2[Alias/Wash Disclosed]
        C3[Provenance Stamped] --> C4[ocr_engine + engine_meta]
        C5[Gap: 7.1% Lower Bound] --> C6[Per-Script Table]
    end
    
    subgraph "COMPETITIVE GAP [2/10]"
        D1[Sarvam CER: ~0.12] --> D2[Our Best: ~0.43]
        D3[3.5× Worse on CER] --> D4[30-70pp Accuracy Gap]
        D5[0 Fine-Tuning] --> D6[0 Akshara Loss]
    end
    
    subgraph "TRAINING PIPELINE READY [80%]"
        E1[SFT: 3,728 pairs] --> E2[SimPO: 13/50K]
        E3[CER Rewards: 1,850] --> E4[CER_STAGE3B.json]
        E5[Akshara Boundaries] --> E6[Need 100K]
    end
```

---

## 🎯 THE 100/10 DEFINITION — 22 PILLARS (Live Audit)

| # | Pillar | Status | Verification Command | Gap to 100/10 |
|---|--------|--------|---------------------|---------------|
| **P1** | Benchmark 4,000/4,000 sealed | ✅ DONE | `python level2/seal_gen.py` → 11/11 GREEN | — |
| **P2** | One-writer report chain | ✅ DONE | `python level2/report.py` → single pass | — |
| **P3** | True consensus (family-deduped) | ✅ DONE | `cat reports/TRUE_CONSENSUS.json` | — |
| **P4** | Script-sliced leaderboards | ✅ DONE | `cat reports/LEADERBOARD_BY_SCRIPT.md` | — |
| **P5** | Engine honesty (alias/wash/limitation) | ✅ DONE | `grep quality_status models/*/RUN.md` | — |
| **P6** | Engine provenance stamped | ✅ DONE | `jq '.engine_meta' out/*/*/te_001.json` | — |
| **P7** | Manifest integrity + tag corrections | ✅ DONE | `python -c "import json; m=json.load(open('level2/pages_manifest.json')); print(len(m))"` | — |
| **P8** | Reproducibility (setup.sh smoke) | ✅ DONE | `bash scripts/setup_fresh_machine.sh --dry-run` | — |
| **P9** | Decision ledger | ✅ DONE | `wc -l level2/DECISIONS.log` | — |
| **P10** | Regression harness (auto-baseline) | ✅ DONE | `python level2/regression_test.py` | — |
| **P11** | CER vs PDF-layer per engine | ✅ DONE | `cat reports/CER_STAGE3B.json \| jq '.median_cer_per_engine'` | — |
| **P13** | Training-data exports (SFT/DPO) | ✅ DONE | `ls reports/training_data/` | — |
| **P14** | Gap slide with rigorous lower bound | ✅ DONE | `cat reports/GAP.md` | — |
| **P15** | Sep-16 package ready | ✅ DONE | `ls reports/SEP16_ONE_SCREEN.md reports/WHATSAPP_*.md` | — |

| # | Pillar | Status | Gap to 100/10 |
|---|--------|--------|---------------|
| **P16** | **Accuracy ≥ Sarvam per-language** | ❌ **GAP-3.5×** | Sarvam CER ~0.12 vs our best ~0.43 |
| **P17** | **Akshara-boundary aux loss (Stage 2)** | ❌ MISSING | No annotation schema, no trainer |
| **P18** | **SCST RL on CER (Stage 2b)** | ❌ MISSING | Rewards export exists; RL trainer absent |
| **P19** | **SimPO/DPO at scale (Stage 3b)** | ⚠️ PARTIAL | 126 pairs exist; need ≥50K + trainer |
| **P20** | **Learned preprocessing (Stage 0)** | ❌ MISSING | OpenCV binarize-only; deskew NOT implemented |
| **P21** | **Layout model (Stage 1, DocLayout-YOLO)** | ❌ MISSING | L1 boxes exist (400 gold) — no training harness |
| **P22** | **Production serving (API, latency, SLOs)** | ❌ MISSING | No Triton/K8s; no paid-API runs |

**Count: 15/22 pillars standing. 7 missing. Progress: 68% toward 100/10.**

---

## 📊 SARVAM DELTA TABLE — THE ONLY SCOREBOARD THAT MATTERS

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff4444', 'edgeLabelBackground':'#fff0f0'}}}%%
graph LR
    subgraph "SARVAM PUBLISHED ACCURACY"
        S1[Telugu: 87.7%] --> S2[Tamil: 93.4%]
        S3[Kannada: 89.9%] --> S4[Malayalam: 91.6%]
    end
    
    subgraph "OUR BEST ACCURACY"
        O1[Telugu: 57.0% -30.7pp] --> O2[Tamil: 36.7%]
        O3[Kannada: 19.1%] --> O4[Malayalam: 34.5%]
    end
    
    subgraph "GAP ANALYSIS"
        G1[Telugu: -30.7pp] --> G2[Tamil: -56.7pp]
        G3[Kannada: -70.8pp] --> G4[Malayalam: -57.1pp]
    end
    
    S1 -.->|GAP: -30.7pp| O1
    S2 -.->|GAP: -56.7pp| O2
    S3 -.->|GAP: -70.8pp| O3
    S4 -.->|GAP: -57.1pp| O4
```

| Script | Our Best CER (Engine) | Our Accuracy | Sarvam Published Acc | Gap (pp) | Verdict |
|--------|----------------------|--------------|----------------------|----------|---------|
| **Telugu** | 0.430 (surya) | 57.0% | 87.7% | **−30.7pp** | ❌ Not competitive |
| **Tamil** | 0.633 (surya) | 36.7% | 93.4% | **−56.7pp** | ❌ Not competitive |
| **Kannada** | 0.810 (surya)* | 19.1% | 89.9% | **−70.8pp** | ❌ Not competitive |
| **Malayalam** | 0.655 (indicphoto)* | 34.5% | 91.6% | **−57.1pp** | ❌ Not competitive |

> **Median CER (our best ensemble):** ~0.43 | **Sarvam published CER:** ~0.12 | **Gap: ~3.5× worse**
> **We are NOT competitive with Sarvam on accuracy. We have a BENCHMARK; Sarvam has a PRODUCT.**

---

## 🔴 P0 — IMMEDIATE FIXES (Execute First — Each ≤1h)

```mermaid
graph TD
    A[P0-1: Purge 14,600 Synth Renders] -->|`ls renders_shared/synth_* \| wc -l` → 14,600| B[Archive to _archive/synth_leak]
    B --> C[Regenerate renders_shared.sha1]
    C --> D[Acceptance: ls renders_shared \| wc -l == 400]
    
    E[P0-2: Archive GAP_ANALYSIS.md] -->|Two gap docs: 7.1% vs 9.9%| F[`mv reports/GAP_ANALYSIS.md _archive/`]
    F --> G[Acceptance: One gap file quotable]
    
    H[P0-3: Commit Tree (G10)] -->|git status --short shows 10 RUN.md + untracked| I[git add -A && git commit]
    I --> J[Acceptance: git status --porcelain clean]
    
    K[P0-4: Fix thin KeyError] -->|KeyError at verify_v2.py:216| L[Add "thin": 0 to agg init]
    L --> M[Acceptance: verify_v2 runs clean]
    
    N[P0-5: Delete dup functions] -->|verify_v2.py:131-155 dup jaccard/engine_text/schema_ok| O[sed -i '131,155d' verify_v2.py]
    O --> P[Acceptance: verify_v2 runs clean]
```

| # | Fix | Evidence | Fix Command | Acceptance | Lift |
|---|-----|----------|-------------|------------|------|
| **P0-1** | **Purge 14,600 synth renders** | `ls renders_shared/synth_* \| wc -l` → **14,600** | `mkdir -p _archive/synth_leak_20260914; mv renders_shared/synth_* _archive/synth_leak_20260914/; shasum renders_shared/*.png > renders_shared.sha1` | `ls renders_shared \| wc -l` == 400; verify_v2 manifest passes | Data truth 9.5→10 |
| **P0-2** | **Archive GAP_ANALYSIS.md** | `reports/GAP_ANALYSIS.md` (9.9%) vs `GAP.md` (7.1%) | `mv reports/GAP_ANALYSIS.md _archive/` | Exactly one gap file quotable | Reporting 8→9 |
| **P0-3** | **Commit tree (G10)** | `git status --short` shows 10 RUN.md + untracked | `git add -A && git commit -m "auto-regen + P0 fixes"` | `git status --porcelain` clean | Repro 8→9 |
| **P0-4** | **Fix thin KeyError** | KeyError at `verify_v2.py:216` | Add `"thin": 0` to agg init dict | verify_v2 runs clean | Code +0.5 |
| **P0-5** | **Delete dup functions** | `verify_v2.py:131-155` dup jaccard/engine_text/schema_ok | `sed -i '131,155d' level2/verify_v2.py` | verify_v2 runs clean | Code +1 |

---

## 📋 COMPLETE IMPROVEMENT REGISTER (100% Audited)

### P0 — CRITICAL (Do First — Blocks Everything)

| ID | Fix | Evidence | Fix Command | Acceptance | Status |
|----|-----|------------|-------------|------------|--------|
| **P0-1** | Purge 14,600 synth renders | `ls renders_shared/synth_* \| wc -l` → **14,600** | `mkdir -p _archive/synth_leak; mv renders_shared/synth_* _archive/; shasum renders_shared/*.png > renders_shared.sha1` | `ls renders_shared \| wc -l` == 400 | ✅ DONE |
| **P0-2** | Archive GAP_ANALYSIS.md | `ls reports/GAP_ANALYSIS.md` exists | `mv reports/GAP_ANALYSIS.md _archive/` | `! -f reports/GAP_ANALYSIS.md` | ⬜ |
| **P0-3** | Commit tree (G10) | `git status --short` shows 10 RUN.md | `git add -A && git commit -m "P0 fixes"` | `git status --porcelain` clean | ⬜ |
| **P0-4** | Fix thin KeyError | KeyError at `verify_v2.py:216` | Add `"thin": 0` to agg init dict | verify_v2 runs clean | ⬜ |
| **P0-5** | Delete dup functions | `verify_v2.py:131-155` dup jaccard/engine_text/schema_ok | `sed -i '131,155d' level2/verify_v2.py` | verify_v2 runs clean | ⬜ |

### P1 — QUALITY HARDENING (This Week)

| ID | Fix | Evidence | Fix Command | Acceptance | Lift |
|----|-----|----------|-------------|------------|------|
| **P1-1** | Quarantine verdict (H-queue) | `_quarantine/` has 4 files | H-queue decision in DECISIONS.log | +0.5 |
| **P1-2** | Wire regression_test.py into autoloop | `orchestrator.py` has autoloop | Add to `refresh_chain()` | +0.5 |
| **P1-3** | Formalize engines/ socket + README | `engines/README.md` missing | Create `engines/README.md` | +0.5 |
| **P1-4** | B21 render sha1 spot-audit | `renders_shared.sha1` exists | Quarterly cron job | +0.5 |
| **P1-5** | B22 regression alarm LIVE | `regression_test.py` exists | Add DASHBOARD banner on >2% CER delta | +0.5 |
| **P1-6** | Confidence harvest (V18) | paddle/doctr/rapid have confs | Add `confidence_mean` to packs | +0.5 |
| **P1-7** | 300-DPI probe → CLOSED | `300DPI_PROBE.md`: 0/10 recovered | Document in PROMPT.md | +0.5 |
| **P1-8** | Deskew — SKIPPED (documented) | Docstring claims deskew; only binarize | Document in PROMPT.md | +0.5 |
| **P1-9** | Latency trust fix | TIMING_PROBE.jsonl has 21 measurements | Republish LATENCY.md from probe | +0.5 |

---

## 📊 SARVAM DELTA TABLE — THE ONLY SCOREBOARD

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff4444', 'edgeLabelBackground':'#fff0f0'}}}%%
graph LR
    subgraph "SARVAM PUBLISHED ACCURACY"
        S1[Telugu: 87.7%] --> S2[Tamil: 93.4%]
        S3[Kannada: 89.9%] --> S4[Malayalam: 91.6%]
    end
    
    subgraph "OUR BEST ACCURACY"
        O1[Telugu: 57.0% -30.7pp] --> O2[Tamil: 36.7% -56.7pp]
        O3[Kannada: 19.1% -70.8pp] --> O4[Malayalam: 34.5% -57.1pp]
    end
    
    subgraph "GAP ANALYSIS"
        G1[Telugu: -30.7pp] --> G2[Tamil: -56.7pp]
        G3[Kannada: -70.8pp] --> G4[Malayalam: -57.1pp]
    end
    
    S1 -.->|GAP: -30.7pp| O1
    S2 -.->|GAP: -56.7pp| O2
    S3 -.->|GAP: -70.8pp| O3
    S4 -.->|GAP: -57.1pp| O4
```

| Script | Our Best CER (Engine) | Our Accuracy | Sarvam Published Acc | Gap (pp) | Verdict |
|--------|----------------------|--------------|----------------------|----------|---------|
| **Telugu** | 0.430 (surya) | 57.0% | 87.7% | **−30.7pp** | ❌ Not competitive |
| **Tamil** | 0.633 (surya) | 36.7% | 93.4% | **−56.7pp** | ❌ Not competitive |
| **Kannada** | 0.810 (surya)* | 19.1% | 89.9% | **−70.8pp** | ❌ Not competitive |
| **Malayalam** | 0.655 (indicphoto)* | 34.5% | 91.6% | **−57.1pp** | ❌ Not competitive |

> **Median CER (our best ensemble):** ~0.43 | **Sarvam published CER:** ~0.12 | **Gap: ~3.5× worse**
> **We are NOT competitive with Sarvam on accuracy. We have a BENCHMARK; Sarvam has a PRODUCT.**

---

## 📋 COMPLETE IMPROVEMENT REGISTER (100% Audited)

### P0 — CRITICAL (Do First — Blocks Everything)

| ID | Fix | Evidence | Fix Command | Acceptance | Status |
|----|-----|------------|-------------|------------|--------|
| **P0-1** | Purge 14,600 synth renders | `ls renders_shared/synth_* \| wc -l` → **14,600** | `mkdir -p _archive/synth_leak; mv renders_shared/synth_* _archive/; shasum renders_shared/*.png > renders_shared.sha1` | `ls renders_shared \| wc -l` == 400 | ✅ **DONE** |
| **P0-2** | Archive GAP_ANALYSIS.md | `ls reports/GAP_ANALYSIS.md` exists | `mv reports/GAP_ANALYSIS.md _archive/` | `! -f reports/GAP_ANALYSIS.md` | ⬜ |
| **P0-3** | Commit tree (G10) | `git status --short` shows 10 RUN.md + untracked | `git add -A && git commit -m "P0 fixes"` | `git status --porcelain` clean | ⬜ |
| **P0-4** | Fix thin KeyError | KeyError at `verify_v2.py:216` | Add `"thin": 0` to agg init dict | verify_v2 runs clean | ⬜ |
| **P0-5** | Delete dup functions | `verify_v2.py:131-155` dup jaccard/engine_text/schema_ok | `sed -i '131,155d' level2/verify_v2.py` | verify_v2 runs clean | ⬜ |

### P1 — QUALITY HARDENING (This Week)

| ID | Fix | Evidence | Fix Command | Acceptance | Lift |
|----|-----|----------|-------------|------------|------|
| **P1-1** | Quarantine verdict (H-queue) | `_quarantine/` has 4 files | H-queue decision in DECISIONS.log | +0.5 | ⬜ |
| **P1-2** | Wire regression_test.py into autoloop | `orchestrator.py` has autoloop | Add to `refresh_chain()` | +0.5 | ⬜ |
| **P1-3** | Formalize engines/ socket + README | `engines/README.md` missing | Create `engines/README.md` | +0.5 | ⬜ |
| **P1-4** | B21 render sha1 spot-audit | `renders_shared.sha1` exists | Quarterly cron job | +0.5 | ⬜ |
| **P1-5** | B22 regression alarm LIVE | `regression_test.py` exists | Add DASHBOARD banner on >2% CER delta | +0.5 | ⬜ |
| **P1-6** | Confidence harvest (V18) | paddle/doctr/rapid have confs | Add `confidence_mean` to packs | +0.5 | ⬜ |
| **P1-7** | 300-DPI probe → CLOSED | `300DPI_PROBE.md`: 0/10 recovered | Document in PROMPT.md | +0.5 | ⬜ |
| **P1-8** | Deskew — SKIPPED (documented) | Docstring claims deskew; only binarize | Document in PROMPT.md | +0.5 | ⬜ |
| **P1-9** | Latency trust fix | TIMING_PROBE.jsonl has 21 measurements | Republish LATENCY.md from probe | +0.5 | ⬜ |

---

## 🏗️ PHASE 1-5: THE 100/10 CLIMB ROADMAP

```mermaid
gantt
    title VAJRASTRA 100/10 ROADMAP
    dateFormat  YYYY-MM-DD
    axisFormat  %b
    
    section Phase α: Data Moat (M1-2)
    D1 Akshara annotation schema + segmenter     :active,    d1, 2026-09-15, 30d
    D2 Layout gold expansion (IndicDLP-42)       :d2,        after d1, 30d
    D3 Hard-case expansion (handwriting, stamps) :d3,        after d2, 30d
    
    section Phase β: Training (M3-6)
    T1 Stage-0 learned preprocess (-15% CER)     :t1,        2026-11-15, 30d
    T2 Stage-2 SFT + akshara aux loss            :t2,        after t1, 30d
    T3 Stage-2b SCST RL on CER                   :t3,        after t2, 30d
    T4 Stage-3 SFT + SimPO/DPO (50K pairs)       :t4,        after t3, 30d
    
    section Phase γ: Product (M7-9)
    S1 Distill ensemble → student (1/10th latency) :s1,       2027-02-15, 30d
    S2 Triton + K8s + SLOs live                 :s2,        after s1, 30d
    S3 Paid-API A/B: Sarvam vs student          :s3,        after s2, 30d
    
    section Phase δ: Win Condition
    W1 Beat Sarvam on our pages AND their pages  :w1,        2027-08-15, 30d
    W2 Beat Sarvam on 2 external benches         :w2,        after w1, 30d
    W3 Stranger reproduction from setup.sh       :w3,        after w2, 15d
```

---

## 🏗️ PHASE ARCHITECTURE OVERVIEW

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '10px'}}}%%
graph TB
    subgraph "PHASE α: DATA MOAT [M1-2]"
        D1[Akshara Annotation Schema] --> D1a[10K pages L2A-ready]
        D2[Layout Gold Expansion] --> D2a[400 pages → IndicDLP-42]
        D3[Hard-Case Expansion] --> D3a[Handwriting/Stamps/Forms]
    end
    
    subgraph PHASE β: TRAINING [M3-6]
        T1[Stage-0 Learned Preprocess] --> T1a[-15% CER on raw]
        T2[Stage-1 Layout + Akshara] --> T2a[mAP > 0.9, akshara IoU > 0.85]
        T3[Stage-2 SFT + Akshara Loss] --> T3a[CER < tess-fam 0.493]
        T4[Stage-2b SCST RL on CER] --> T4a[-10% CER vs SFT]
        T5[Stage-3 SFT + SimPO/DPO] --> T5a[JSON F1 > 0.9]
    end
    
    subgraph PHASE γ: PRODUCT [M7-9]
        S1[Distill Ensemble → Student] --> S1a[1/10th latency, 95% quality]
        S2[Triton + K8s + SLOs] --> S2a[p99 < 2s, 99.9% avail]
        S3[Paid-API A/B: Sarvam vs Student] --> S3a[Vinay pricing story]
    end
    
    subgraph PHASE δ: WIN CONDITION [M12]
        W1[Beat Sarvam on OUR pages] --> W1a[CER < Sarvam on our corpus]
        W2[Beat Sarvam on THEIR pages] --> W2a[CER < Sarvam on THEIR bench]
        W3[Stranger Reproduction] --> W3a[setup.sh reproduces 4000 packs]
    end
    
    D1 --> T1
    T1 --> T2
    T2 --> T3
    T3 --> T4
    T4 --> T5
    T5 --> S1
    S1 --> S2
    S2 --> S3
    S3 --> W1
    W1 --> W2
    W2 --> W3
```

---

## 🏗️ VAULTSTACK 4-STAGE PIPELINE — L2 DATA ENGINE WIRING

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '11px'}}}%%
graph LR
    subgraph "LEVEL 2 BENCHMARK ENGINE"
        L2A[4000 OCR Packs] --> L2B[Capture Ratios]
        L2C[Sarvam Delta Table] --> L2D[Gap Analysis 7.1%]
        L2E[CER_STAGE3B.json] --> L2F[4000 CER pairs]
        L2G[Training Exports] --> L2G1[SFT: 3,728 pairs]
        L2G2[SimPO: 13 pairs]
        L2G3[CER Rewards: 1,850]
        L2H[Disagreement Queue] --> L2H1[50 pages for human review]
    end
    
    subgraph VAULTSTACK 4-STAGE PIPELINE
        S0[Stage 0: OpenCV Preprocess] --> S1[Stage 1: DocLayout-YOLO LoRA]
        S1 --> S2[Stage 2: Parallel SFT]
        S2 --> S2a[TrOCR + Qwen3-VL + PaddleOCR-VL]
        S2a --> S2b[Akshara-boundary Aux Loss]
        S2b --> S3[Stage 2b: SCST RL on CER]
        S3 --> S4[Stage 3: IndicBERT/Airavata SFT]
        S4 --> S5[Stage 3b: SimPO/DPO]
        S5 --> S6[Benchmark: Sarvam/IndicDLP]
    end
    
    subgraph L2 DATA ENGINE FEEDS
        L2A -.->|Noisy corpus + gold anchors| S2
        L2F -.->|Per-page CER rewards| S3
        L2G1 -.->|SFT noisy→gold pairs| S4
        L2H1 -.->|Human review queue| S4
        L2D -.->|Gap slide: 7.1%| S6
    end
    
    L2A -.-> L2B
    L2C -.-> L2D
    L2E -.-> L2F
    L2G -.-> L2G1
    L2G -.-> L2G2
    L2G -.-> L2G3
    L2H -.-> L2H1
```

---

## 🏭 PRODUCTION SERVING ARCHITECTURE (P22)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '10px'}}}%%
graph TB
    subgraph CLIENT
        C[Client Request] --> GW[API Gateway]
    end
    
    subgraph SERVING INFRASTRUCTURE
        GW --> TRITON[Triton Inference Server]
        TRITON -->|Model Repository| MR[Model Repository]
        
        subgraph MODEL REPOSITORY
            MR --> M1[Cascade Router: INT8, 5ms]
            MR --> M2[Tesseract Ensemble: FP16, 50ms]
            MR --> M3[Surya Ensemble: FP16, 500ms]
            MR --> M4[Uncertainty Head: INT8, 5ms]
            MR --> M5[Post-proc LLM: INT4, 200ms]
        end
        
        TRITON --> Q[Redis Queue]
        Q --> WP[Worker Pool: Autoscaled GPU/CPU]
        WP --> RS[Result Store: S3 + DynamoDB]
        RS --> CB[Callback/Webhook]
    end
    
    subgraph OBSERVABILITY
        MON[Prometheus + Grafana] --> ALERT[SLO Alerts]
        LANG[Langfuse Traces] --> DEBUG[Debug Dashboard]
        SLO[SLO Dashboard] --> BURN[Error Budget Alerts]
    end
    
    GW -.-> MON
    TRITON -.-> MON
    Q -.-> MON
```

---

## 🎯 CI/CD CER REGRESSION GATE

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'fontSize': '10px'}}}%%
graph LR
    A[Git Push / PR] --> B[GitHub Actions]
    B --> C[Checkout + Setup]
    C --> D[Run Full Pipeline]
    D --> E[Run verify_v2.py]
    E --> F[Extract Metrics]
    F --> G{Compare vs Baseline}
    G -->|PASS| H[Update Baseline]
    G -->|FAIL| I[Block Merge + Alert]
    H --> J[Auto-update REGRESSION_BASELINE.json]
    I --> K[Alert: CER Regression > 0.5%]
    J --> L[Update Baseline]
    K --> M[Slack/GitHub Alert]
    
    style I fill:#ffcccc
    style K fill:#ffcccc
```

### Regression Gates (Auto-Block on Regression)

| Metric | Baseline | Threshold | Action |
|--------|----------|-----------|--------|
| Total Packs | 4000 | == 4000 | ✅ |
| Seal Gates Passed | 11 | == 11 | ✅ |
| Leakage Latin on Indic | 3% | ≤ 5% | ✅ |
| RapidOCR Wash Fraction | 25% | ≤ 30% | ✅ |
| Coverage ≥6 | 382 | ≥ 380 | ✅ |
| True Consensus | 38 | ≥ 30 | ✅ |
| Gap Lower Bound | 7.1% | ≤ 10% | ✅ |

---

## 📋 AGENT HANDOFF CARD (Copy-Paste Ready)

```markdown
MISSION: Execute next unchecked item from SPEC_100.md
EVIDENCE: Run item's Evidence command FIRST
FIX: Run item's Fix command
VERIFY: Run item's Acceptance command
LOG: DECISIONS.log ← "date | area | decision | why | owner"
CHECKBOX: IMPROVEMENTS_CURRENT_WORK.md ← flip [ ] → [x]
REGRESSION: python level2/regression_test.py → must PASS
COMMIT: git add -A && git commit -m "PX-Y: <description>"
BLOCKERS: If Evidence command fails → CLOSED-NOT-A-BUG (phantom)
NEVER: Edit reports/, models/, verify_v2.py, report.py, seal_gen.py, run_engine.py
```

### ACCEPTANCE GATES (Auto-Verified)

```bash
# Before any PR merge:
python level2/seal_gen.py        # 11/11 GREEN
python level2/regression_test.py # All 7 gates pass
python level2/verify_v2.py       # schema 0, CER present
```

---

## 📋 100/10 PILLAR CHECKLIST (Live Tracker)

| # | Pillar | Status | Verification | Blocker |
|---|--------|--------|--------------|---------|
| P1 | 4000/4000 sealed | ✅ | `seal_gen.py` 11/11 GREEN | — |
| P2 | One-writer report chain | ✅ | `report.py` single pass | — |
| P3 | True consensus (family-deduped) | ✅ | `TRUE_CONSENSUS.json` 38/21/1 | — |
| P4 | Script-sliced leaderboards | ✅ | `LEADERBOARD_BY_SCRIPT.md` 6 strata | — |
| P5 | Engine honesty | ✅ | `QUALITY_STATUS` + `ENGINE_LIMITATIONS` | — |
| P6 | Engine provenance stamped | ✅ | `engine_meta` + `provenance=ocr_engine` | — |
| P7 | Manifest integrity | ✅ | 400/400 valid | — |
| P8 | Reproducibility (setup.sh) | ✅ | `.setup_smoke_proven` | — |
| P9 | Decision ledger | ✅ | `DECISIONS.log` 35 entries | — |
| P10 | Regression harness | ✅ | `REGRESSION_BASELINE.json` | — |
| P11 | CER vs PDF-layer | ✅ | `CER_STAGE3B.json` writer-basis | — |
| P12 | Level-3 socket (stubs) | ✅ | `engines/level3_stub.py` + adapters | — |
| P13 | Training exports (SFT/DPO) | ✅ | `training_assets/` (1760/126/50) | — |
| P14 | Gap slide (7.1%) | ✅ | `GAP.md` lower bound | — |
| P15 | Sep-16 package | ✅ | `SEP16_ONE_SCREEN.md` ready | — |
| **P16** | **Acc ≥ Sarvam** | ❌ | **Sarvam 3.5× better** | **P16-1: Sarvam pages** |
| **P17** | **Akshara-boundary loss** | ❌ | **No schema/trainer** | **P17-1: Segmenter** |
| **P18** | **SCST RL on CER** | ❌ | **Rewards exported; no trainer** | **P18-1: SCST trainer** |
| **P19** | **SimPO/DPO at scale** | ⚠️ | 126 pairs → need 50K+ | **P19-1: Scale pairs** |
| **P20** | **Learned preprocess** | ❌ | **OpenCV only** | **P20-1: Learned preproc** |
| **P21** | **Layout model (YOLO)** | ❌ | **L1 gold 400p; no trainer** | **P21-1: YOLO trainer** |
| **P22** | **Production serving** | ❌ | **No Triton/K8s** | **P22-1: Triton/K8s** |

---

## 🎯 EXECUTION ORDER (Agent Orders)

### TODAY (P0 — Unblocks Everything)
```
[ ] P0-1 Purge 14,600 synth renders
[ ] P0-2 Archive GAP_ANALYSIS.md
[ ] P0-3 Commit tree (G10)
[ ] P0-4 Fix thin KeyError
[ ] P0-5 Delete dup functions in verify_v2.py
```

### THIS WEEK (P1 — Quality Hardening)
```
[ ] P1-1 Quarantine verdict (H-queue)
[ ] P1-2 Wire regression_test.py into autoloop
[ ] P1-3 engines/ socket + README
[ ] P1-4 B21 render sha1 spot-audit
[ ] P1-5 B22 regression alarm LIVE
[ ] P1-6 Confidence harvest
[ ] P1-7 300-DPI probe → CLOSED
[ ] P1-8 Deskew — SKIPPED (documented)
[ ] P1-9 Latency trust fix
```

### NEXT 2 WEEKS (P2 — Competitive Engineering)
```
[ ] P2-1 Acquire Sarvam comparison pages (CRITICAL)
[ ] P2-2 AKER vs CER verdict closure
[ ] P2-3 Bootstrap CIs on writer basis
[ ] P2-4 Distillation readiness
[ ] P2-5 Engine #11 candidate (PaddleOCR-VL 1.6)
[ ] P2-6 Surya lang-hint upstream watch
```

### 12-MONTH ROADMAP TO #1

| Month | Milestone | Target |
|-------|-----------|--------|
| 1 | Data moat: 500K pages; annotators hired | 100K pages labeled |
| 2 | Akshara boundaries 100K; L1 gold complete | 100K akshara boxes |
| 3 | Stage 0 learned preprocess trained | -15% CER |
| 4 | Stage 1 Layout + Akshara detector | mAP > 0.9 |
| 5 | Stage 2 SFT + akshara aux loss | CER < tess-fam |
| 6 | Stage 2b SCST RL on CER | -10% CER vs SFT |
| 7 | Stage 3/3b SFT + SimPO/DPO | JSON F1 > 0.9 |
| 8 | Cascade router trained | 98% routing accuracy |
| 9 | Distillation: ensemble → student | 95% quality, 10× speed |
| 10 | Triton + K8s + SLOs live | p99 < 2s, 99.9% avail |
| 11 | CI/CD CER regression gate live | Auto-block on Δ > 0.5% |
| 12 | **SARVAM BEATEN** | **CER < Sarvam on all 4** |

---

## 📋 AGENT HANDOFF CARD (Copy-Paste Ready)

```
MISSION: Execute next unchecked item from SPEC_100.md
EVIDENCE: Run item's Evidence command FIRST
FIX: Run item's Fix command
VERIFY: Run item's Acceptance command
LOG: DECISIONS.log ← "date | area | decision | why | owner"
CHECKBOX: IMPROVEMENTS_CURRENT_WORK.md ← flip [ ] → [x]
REGRESSION: python level2/regression_test.py → must PASS
COMMIT: git add -A && git commit -m "PX-Y: <description>"
BLOCKERS: If Evidence command fails → CLOSED-NOT-A-BUG (phantom)
NEVER: Edit reports/, models/, verify_v2.py, report.py, seal_gen.py, run_engine.py
```

### ACCEPTANCE GATES (Auto-Verified)

```bash
# Before any PR merge:
python level2/seal_gen.py        # 11/11 GREEN
python level2/regression_test.py # All 7 gates pass
python level2/verify_v2.py       # schema 0, CER present
```

---

## 🏁 COMPLETION SENTENCE (Mandatory)

> **This project is at 68/100 on the road to 100/10; completion is not claimed and cannot be claimed at this stage.**

---

## 📱 5-LINE WHATSAPP FOR VINAY

```
L2 SEALED: 10 engines × 400 = 4,000 packs. Zero schema errors.
Free-OSS gap: 7.1% volume (lower bound, per-script table attached).
Surya wins Telugu/Malayalam/Devanagari; EasyOCR wins Tamil/Kannada/Latin.
Level-3 adapters: Sarvam (₹0.5/page), Bhashini (ULCA TODO), Google/Azure/Textract stubs ready.
Next: Sarvam 400-page run → distillation → student model @ 1/10th latency.
```

---

## 🏁 FINAL WORD

**We have a world-class BENCHMARK. We do not have a PRODUCT.**

The benchmark is **sealed, honest, reproducible, and auditor-grade**. The seal gates are green. The data is clean. The training exports are ready for Vaultstack's 4-stage pipeline.

**But we are 3.5× worse than Sarvam on CER. We have 0 fine-tuning. We have 0 akshara-aware loss. We have 0 RL on CER. We have 0 production serving.**

**The benchmark is the floor. The product is the ceiling. We are on the floor.**

**Next milestone: Beat Sarvam on Telugu. Then Tamil. Then Kannada. Then Malayalam. Then we can talk about 100/10.**

---

*This SPEC is the single source of truth. Execute in order. Verify before believing. Never claim done.*

**SPEC_100.md v1.0** | **2026-09-14** | **ETERNAL VALIDATOR** | **Disk-Truth Only**

---

*End of SPEC_100.md*