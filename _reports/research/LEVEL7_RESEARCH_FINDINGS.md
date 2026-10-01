# LEVEL7_RESEARCH_FINDINGS.md — top 10 methods distilled from Lane A/B/C ledgers
# Source: docs/research/level7/{a,b,c}/ (984 Lane A records, 659 Lane B records, 436 Lane C records)
# Filter: relevance × recency × actionability ≥ 30/45 (5/5/5 records, deduplicated by topic)
# Date locked: 2026-09-29 04:23 IST (campaign clock end)
# Format per record: mechanism → result → mapping to 18-lang goal → SURVIVES/DIES/UNKNOWN

## Filter method

Lane A LEDGER.md has 984 records with 5/5/5 scores = 47 unique methods (rest are re-cites). Combined with Lane B (RLVR/OCR, self-improvement, multi-agent, tooling, elite repos = 659 records) and Lane C (NVIDIA/competition/data-strategy/tooling = 436 records), the top 10 actionable methods for our 18-language W6/W7 plan are listed below. Each maps to a PPT box from `docs/architecture/PPT_SPEC.md`.

---

## 1. **Sarvam Vision 2.1** — harness-with-VLM pattern (KEEP)

- **What**: 3B sovereign VLM, SFT→RLVR pipeline. Indic bench 87.39.
- **Result**: Best published score on Indic OCR; competitors trail by 3–6 points.
- **Map to 18-lang goal**: This is the **benchmark target**, not a routable pipeline. Every per-engine CER in probe22 is measured against Sarvam's methodology.
- **Decision**: SURVIVES — all W6 stages reference this.
- **Sources**: A6-008, A6-047, A6-098, A1-107 (press), SOURCES.md W1 row 1.
- **Constraint**: Cannot ship Sarvam weights; can only learn from the recipe.

## 2. **Chitrapathak-2 (Krutrim)** — fine-tune OCR-specialized VLM (KEEP)

- **What**: Fine-tunes Nanonets-OCR2-3B (Qwen2.5-VL backbone) for Indic; rotation-normalization + LoRA/full FT.
- **Result**: Telugu char ANLS 6.69 (Chitrapathak-2) vs 11.00 (Chitrapathak-1). 89.8% exact match on 9 Indian govt doc types. ~1.03 s/doc vLLM. **3–6× faster than Chitrapathak-1 LLaVA-from-scratch**.
- **Map to 18-lang goal**: Direct evidence that "fine-tune OCR-specialized VLM" beats "build from scratch". Maps to W6 Stage 2 (TrOCR-from-scratch → DROP, Qwen2.5-VL-3B / GLM-OCR-0.9B fine-tune → KEEP). Covers Odia directly (rival on our weak cell 80.01).
- **Decision**: SURVIVES — strongest published evidence for our "fine-tune, don't build" stance.
- **Sources**: A1-008, A1-009, A1-010, A6-004, A6-005, A6-097.

## 3. **PaddleOCR-VL-1.6** — region-aware progressive training (KEEP)

- **What**: 0.9B VLM; CPT 16.8M + SFT 7.3M + RL on under-optimized regions. Apache-2.0.
- **Result**: 96.33 on OmniDocBench v1.6 (SOTA). Ablation: CPT +0.69, SFT +0.63 more, RL only +0.08 (94.93→96.33). Architecture drop-in compatible with 1.5.
- **Map to 18-lang goal**: W6 sequencing evidence — **do NOT start with RL**. CPT→SFT→RL order matters. Region-mining could target OldScan 55.3 weak cell.
- **Decision**: SURVIVES — sequencing recipe is the locked W6 law.
- **Sources**: A1-001, A1-002, A1-016, A1-017, A1-053, A6-010, A6-011, A6-093.

## 4. **olmOCR-2** — RLVR with verifiable unit-test rewards (KEEP, conditional)

- **What**: VLM trained with RLVR; rewards are diverse binary unit tests (HTML element presence + read-order). 1 ep SFT then 1 ep GRPO. chrF++ 40.5 on Devanagari scans.
- **Result**: SOTA on olmOCR-Bench. Validates Sarvam's harness-with-VLM design.
- **Map to 18-lang goal**: Stage 3b schema-head pattern. **English-first design is a ceiling for Indic** (chrF++ 40.5 on Devanagari, not Indic-optimized). Cannot wrap olmOCR-2 directly as our Indic engine; can borrow the schema-validity unit-test pattern.
- **Decision**: SURVIVES for Stage 3b (schema head); DIES as direct Indic engine.
- **Sources**: A1-005, A1-006, A1-007, A1-100, A6-001, A6-002, A6-003, A6-054, A6-055.

## 5. **ScriptMoE** — script-aware mixture-of-experts (KEEP, conditional)

- **What**: PP-OCRv5 + MoE router on script ID.
- **Result**: F1 65.71 → 80.89 (+15 points) on Indic script-routing task.
- **Map to 18-lang goal**: Maps to Stage 1 (layout) and per-script engine routing. Our probe22 already validates the script-routing hypothesis — surya wins 9/12 ≥50-lang cells. The MoE part is overkill for wrap-only but useful if W6 QLoRA runs per-script adapters.
- **Decision**: SURVIVES (per-script routing is already locked); QLoRA per-script adapters are UNKNOWN cost-benefit.
- **Sources**: A6-007, A6-100, A2-022.

## 6. **Surya 2 (datalab-to)** — 650M single VLM, layout+OCR+tables (KEEP, primary)

- **What**: 650M single VLM; OCR + layout + reading order + tables unified. 91-lang internal 87.2 (38 langs ≥90). 83.3 olmOCR-bench. License: modified OpenRAIL-M (free for research/personal/<$5M startups).
- **Result**: Best non-API engine on our probe22 — **surya overall CER 0.3849, wins on 9/12 ≥50-lang cells**. **OldScan subscore 42.8** — confirms restoration lane (R4) is highest-leverage OldScan attack.
- **Map to 18-lang goal**: **Already shipped as Engine #1 in W6 wrap-only baseline**. License check needed before Vinay demo (OpenRAIL-M revenue cap <$5M is fine for hackathon). Devanagari latency is a real ceiling — surya 4–9 s/page English but 178 s on Hindi page.
- **Decision**: SURVIVES — primary wrap-only engine.
- **Sources**: A1-013, A1-014, A1-015, A1-044 (Ol Chiki NOT supported — sat is honest-empty), A1-088.

## 7. **Bodhan Indic OCR** — 33M layout + 0.8B Qwen3.5 block OCR (KEEP, watch)

- **What**: Bodhan AI Indic OCR suite; 33M layout + 0.8B Qwen3.5 block OCR.
- **Result**: **Santali 68.30 vs Sarvam 53.91** — Bodhan beats Sarvam on Santali. Reference competitor on weak cells (sat, ks).
- **Map to 18-lang goal**: Stage 0–2 specialist router; rival for ks (Nastaliq), sat (Ol Chiki) weak cells. Open-weight, ~2 GB model.
- **Decision**: SURVIVES for specialist attack on sat/ks; UNKNOWN whether Bodhan beats surya on the rest.
- **Sources**: A6-095, A6-096, SOURCES.md W1 row 1.

## 8. **Devanagari stress-test (Qwen3-VL-8B)** — Indic error taxonomy (KEEP)

- **What**: Qwen3-VL-8B on real Devanagari exam-scans stress test.
- **Result**: 75.2 CER on real scans; produces full error taxonomy (matra, halant, conjunct).
- **Map to 18-lang goal**: Maps directly to hi/mr/sa/ne/mai/kok/brx/doi (8 Devanagari langs). Confirms W6 fine-tune needs akshara-boundary auxiliary loss (PPT Spec Stage 2).
- **Decision**: SURVIVES — confirms Devanagari is the dominant script class (8/17 Indic langs).
- **Sources**: A6-006, A6-101, A5-015, A5-020, A5-023, A2-020.

## 9. **MinerU2.5-Pro** — data-centric region refinement (KEEP)

- **What**: Data-centric pipeline; region-mining for under-optimized regions.
- **Result**: Direct validation of the region-aware progressive training approach used by PaddleOCR-VL-1.6 (record 3).
- **Map to 18-lang goal**: W6 sequencing evidence (CPT→SFT→RL = region-refined). Potential OldScan 55.3 attack if region-mining finds similar "weak regions" on our pages.
- **Decision**: SURVIVES — recipe corroboration; concrete OldScan attack is UNKNOWN.
- **Sources**: A6-012, A6-086, A1-022, A1-026, A1-027.

## 10. **DocRes (CVPR 2024)** — generalist document restoration (KEEP)

- **What**: Generalist model for unifying document image restoration tasks.
- **Result**: CVPR 2024. Maps directly to R4 OldScan attack — restoration pre-pass before OCR.
- **Map to 18-lang goal**: Wrap-only Stage 0 enhancement. R4 lock says Otsu is cheap baseline; DocRes-head pilot n≤8 is the next ablation (per A0-006 R4 mandate). Adoption bar: median ΔCER ≤ -0.03 vs Otsu, 95% bootstrap CI, ≥2/3 frozen engines.
- **Decision**: SURVIVES for wrap-only Stage 0; DIBCO is Latin/Greek-only so no transfer.
- **Sources**: A6-039, A4-001, A4-025, A6-053, A6-110, A3-076.

---

## Methods that DID NOT make the top-10 (DIES/UNKNOWN shortlist)

| Method | Verdict | Note |
|---|---|---|
| LLaVA-NeXT OCR from scratch | **DIES** | Chitrapathak-1 ANLS 11.00 vs Chitrapathak-2 ANLS 6.69 — 3–6× slower AND less accurate. PPT Spec Stage 2 "TrOCR from scratch" is REFUTED. |
| IndicTrans2 / Airavata / MuRIL / OpenHathi / CALM | **NOT OUR TIER** | LLM tier, not OCR tier. OCR tier is Surya/Bodhan/Sarvam/Chitrapathak. |
| OldDeepSeek-OCR-3B / Chandra-OCR-8B / LightOnOCR-1B / Nanonets-OCR2-3B | **DIES for Indic** | Oct-2025 inflection open-source pool is SOTA-competitive for English; Indic results not published. Base models only — fine-tune to add Indic (Stage 2). |
| IndicConformer / IndicWav2Vec / IndicBERTv2 | **DIES** | Speech / NLP tier. |
| Krutrim-2-12B / Cloud OCR APIs | **DIES** | Wrong tier (LLM / paid); no Indic-OCR result published. |
| Mistral OCR 3 (79.1 OmniDocBench) | **DIES** | English-first; no Indic transfer. |
| HunyuanOCR / Tencent-DB-Agent | **WATCH** | License risk flag (Tencent Hunyuan Community License not pure OSS). |

---

## Final method ranking (for Vinay)

**Locked W6 recipe (5 methods)**: Sarvam harness-with-VLM pattern → Chitrapathak-2 fine-tune → PaddleOCR-VL-1.6 region-aware sequencing → olmOCR-2 schema-validity RL → DocRes restoration pre-pass.

**Already-shipped wrap-only baseline (3 methods)**: Surya 2 (primary engine), per-script routing (ScriptMoE evidence), restoration pre-pass (DocRes/Otsu).

**Conditional (depends on Vinay)**: Bodhan specialist (sat/ks), QLoRA per-script adapters (UNKNOWN cost-benefit, GLM-OCR 0.9B primary candidate).

**DIES**: LLaVA-from-scratch, Indic-only base models not fine-tuned, paid APIs beyond Sarvam 54-cap, novel backbones.

---

**Source files (every claim ties to a file):**

- Lane A: `docs/research/level7/a/LEDGER.md` (984 records)
- Lane B: `docs/research/level7/b/{b1_rlvr_ocr,b2_self_improving_agents,b3_multi_agent_orchestration,b4_agent_tooling,b5_elite_repos}/` (659 records)
- Lane C: `docs/research/level7/c/{c1,c2,c3,c4}/` (436 records)
- Synthesis: `docs/research/level7/FINAL_VERDICT_2026-09-27.md`, `INTEGRATED-ELITE-STACK.md`
- Boss anchors: `R1_SOTA_MECHANISM_TEARDOWN.md`, `R2_NASTALIQ_FORENSICS.md`, `R3_OLCHIKI_MAYEK_SYNTHETIC.md`, `R4_OLDSCAN_RESTORATION.md`, `R7_W6_TRAINING_TREE.md`, `W1_RECIPE_REFRESH.md`, `SOURCES.md`

**All counts from disk.**