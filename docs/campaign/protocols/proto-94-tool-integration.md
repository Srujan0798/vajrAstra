---
name: proto-94-tool-integration
description: "Added 2026-09-30 — researched shortlist of models, datasets, MCP servers and agent tools worth installing/integrating now (Bodhan IndicOCR + MLX port, indic-ocr-bench, mlx-vlm LoRA, Hugging Face MCP, 600K-KS-OCR, SynthOCR-Gen, ECC, graphify, OpenCode council) with licence, size, the step each serves, install command and approval gate"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-30T09:25:44.779Z
---

# PROTO-94 — TOOLS TO INSTALL / INTEGRATE (each needs the boss's yes if it downloads; record approvals in proto-92)

| # | Tool / asset | What it gives us | Licence · size | Step it serves | How (after approval) | Gate |
|---|---|---|---|---|---|---|
| 1 | **Bodhan IndicOCR** `bodhan-ai/indic-ocr` | Strongest open Indic OCR (84.94 on Sarvam's bench); layout 33M + block recogniser 0.8B | Indic Open Model License v1.0 (commercial + fine-tune OK, attribution, hosted API needs written approval) | Plan v3 base (proto-89 §A) | HF download; `IndicOCR.from_pretrained(repo)` per card | U23 |
| 2 | **MLX port** `hari31416/indic-ocr-mlx-4bit` (8-bit, bf16 variants exist) | The block recogniser on Apple Silicon, 636 MB, ~391 ms/crop | same licence (derivative) | Day 1 speed + Day 3 QLoRA base | `mlx_vlm.load("hari31416/indic-ocr-mlx-4bit")` | U23 |
| 3 | **indic-ocr-bench** `sarvamai/indic-ocr-bench` | The benchmark the market quotes + official `metrics.py` | Apache-2.0; 6,909 test + 1,173 small_representative | Comparable number (proto-87 §A, proto-89 §A) | HF datasets; EVAL ONLY | U24 (= V1) |
| 4 | **mlx-vlm LoRA** (`mlx-vlm[train]`) | Local LoRA/QLoRA for Qwen2/3/3.5-VL | MIT (check) · already installed 0.7.4; the `[train]` extra adds `datasets` | Day 3 fine-tune | `python -m mlx_vlm.lora --model-path … --dataset … --lora-rank 16` | covered by the 2026-09-29 MLX approval if no new download; else U25 |
| 5 | **Hugging Face MCP** (official) | Agents search models, datasets, papers and Spaces from inside Claude Code | free; needs HF login | Research lanes, tool discovery | `claude mcp add hf-mcp-server -t http https://huggingface.co/mcp?login` | U26 |
| 6 | **600K-KS-OCR** (arXiv 2601.01088) | 602k synthetic Kashmiri word images | CC-BY-4.0 · ~10.6 GB | Kashmiri, the worst cell for everyone (Sarvam 54.82, Bodhan 48.04) | HF/links in the paper | U27 (optional) |
| 7 | **SynthOCR-Gen** (arXiv 2601.16113) | Synthetic OCR data generator for low-resource scripts | check licence first | Synthetic blocks for thin scripts | read the paper + repo licence before any install | proposal only |
| 8 | **ECC plugin** (enabled 2026-09-30) | 292 skills incl. verification-loop, unified-memory, deep-research, council-multi-model, living-docs-governance | installed | every step (proto-88) | new sessions load it | done |
| 9 | **graphify** | Repo knowledge graph for navigation, orphans, duplicates, concern nodes | installed | proto-72/73/77 | `/graphify … --update` when the bootstrap says STALE | none |
| 10 | **OpenCode `council-multi-model`** | Non-Claude reviewers for the plan (the lead's A3) | installed in OpenCode | multi-LLM review | run inside OpenCode with a non-Anthropic model | none |

## Research rule for new tools (so this list stays honest)
Every addition needs: the page opened (not a snippet), licence quoted, size, which protocol step it serves, and whether it downloads. `factchk` before adding; the boss's approval (proto-92) before installing.
Candidates to evaluate next, not yet verified: arXiv / Semantic Scholar MCP servers for the research lanes; a lightweight human-review page for the §6.4 re-check (U6) built as an Artifact instead of installing Label Studio.

Related: [[proto-89-plan-v3-bodhan-base]], [[proto-88-skill-routing]], [[proto-92-boss-decisions]]
