---
name: proto-13-w1c-mentor-playbook
description: "Step 1C (Miss subagent) — extract the lead's research method from the raw 2026-09-29 transcript, PPT and Sep-10 docx; build the current training-recipe mermaid flowchart; verify A1–A7 on disk; list where the repo diverges from what he asked"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:12:26.008Z
---

# STEP 1C — MENTOR PLAYBOOK (Miss subagent) → `docs/campaign/MENTOR_PLAYBOOK.md`

**Why:** the boss reports to the lead, who gave a method ("how we approach a problem") and asked for it to be executed; it has never been written down as an
actionable document. CO-083: "the PPTX and all details initially received from HIM — read and implement these strategies deeply."
**Writes only:** `docs/campaign/MENTOR_PLAYBOOK.md`.

## TASK block (paste)
You are the Miss agent. Extract the lead's playbook and hold the repo to it. Quote him exactly; never paraphrase inside quote marks.

**Sources (read fully):**
1. `MEETING_2026-09-29_STRUCTURED.md` — the RAW transcript is ONE very long line inside the first ``` block. Print it wrapped:
   `python3 -c "import textwrap;s=open('MEETING_2026-09-29_STRUCTURED.md').read();a=s.find('\`\`\`')+3;b=s.find('\`\`\`',a);print(textwrap.fill(s[a:b],180))"`.
   The structured part (D1–D7, A1–A7, timeline) was written by an agent — treat it as DERIVED; the raw transcript is PRIMARY.
2. `PPT_FULL_DUMP.md`, `PPT_VS_SPEC_DIFF.md`, `docs/architecture/PPT_SPEC.md`; the original deck `AksharDrishti_Hackathon_Proposal final.pptx` (root) — if you need to
   confirm a slide, read `ppt/slides/slide*.xml` via python zipfile and strip tags.
3. `_archive/cleanup_2026-09-28/root_clutter/sync - ocr - September 10.docx` (first meeting): python zipfile → `word/document.xml` → strip tags with regex.
   If unreadable, say so. Do not re-ask or re-litigate the 2026-09-25 meeting.
4. For the flowchart: `docs/architecture/PPT_SPEC.md`, `docs/research/W1_RECIPE_REFRESH.md`, `docs/research/level7/W6_QLORA_SPEC.md`, `docs/research/level7/KILL_CRITERIA.md`.

**Deliverable sections:**
1. **His method, as ordered steps.** For each step: his exact quote · what it concretely means for this project · compliance (YES / PARTIAL / NO / UNKNOWN) · file evidence.
   Steps you must cover (all from the raw transcript): (a) look at how others approached the problem first; (b) Consensus.app — "ten searches free daily… in two, three
   searches, you'll get all the gist" — search the repo for any evidence it was used: `grep -ril consensus --include='*.md' . | grep -v _archive | head`;
   (c) learn "how to train an OCR" as a **flowchart** of the process; (d) scan recent advancements/breakthroughs by labs and companies; (e) compare the methodology with
   what was already built (the PPT recipe "we did it a month, one and a half month back"); (f) ask OpenCode for the best steps, cross-check with Claude and ChatGPT, use
   multiple LLMs as evaluators, and accept "by the process mentioned, not by the AI mentioned"; (g) benchmark existing engines on all 22 languages, 5–10 samples each;
   (h) research existing models and "the best hybrid way of integrations", not a new model; (i) present the plan in a 15–20 min session, cross-question, then execute;
   (j) "no need of people, just AI… but correct methods, correct architecture, correct person who understands".
2. **The current training recipe as a mermaid flowchart** — built ONLY from the sources in item 4, each node annotated with its source file:line.
   Show: data (tiers, GT gates, barred languages) → preprocessing (OpenCV/restoration) → layout (DocLayout-YOLO per PPT) → recognition (engines / parallel SFT
   TrOCR + Qwen-VL + PaddleOCR-VL per PPT) → routing (per-language, `PER_LANG_ROUTING.md`) → training stages (SFT → RLVR/GRPO/SCST per PPT and W6 spec) →
   evaluation (probe22, metrics) → kill criteria (K1/K2). Mark which nodes are BUILT (on disk, ran), SPEC-ONLY, or PAUSED (W6 pause, feed §15).
   Use a ```mermaid fenced block. This is the flowchart the lead asked for first.
3. **A1–A7 status table**, re-verified on disk (planner's view to check, not trust): A1 research sprint PARTIAL (lots of research, no flowchart, no Consensus evidence);
   A2 PPT diff DONE (`PPT_VS_SPEC_DIFF.md`); A3 multi-LLM evaluation NOT DONE (planned as W4 in `docs/PLAN.md:23`, no artifact); A4 review deck PARTIAL (packet is a
   decision menu, not a draft plan); A5 22-language benchmark — data yes, table no, South scored n tiny (see [[proto-12-w1b-benchmark22]]); A6 Krishna/Aryan UNKNOWN (boss);
   A7 agent prompts STALE (Level-7 PROMPT files).
4. **Every constraint he set**, quoted: no novel backbone / hybrid integration; 22 languages, 5–10 samples; research before training; human review session before execution;
   multi-LLM evaluation; AI-only team.
5. **WHERE THE REPO DIVERGES FROM WHAT HE ASKED** — blunt, specific, with paths. Examples to test (not assume): packet framed as a 5-minute decision menu vs his
   15–20 min cross-question session; 18-language evidence vs his 22; QLoRA/GRPO training code (`src/training/`) appearing before his review session;
   research volume vs his "one hour, two-three searches" method; no flowchart; no multi-LLM evaluation. This section is what the boss uses tomorrow.
6. **What to bring to the session** (≤8 bullets) derived from 1–5.

Under 1,800 words (flowchart excluded). Final message: section 5 verbatim + path.

## Lead's acceptance check
Every quote must appear verbatim in the wrapped transcript (`grep -F`). Flowchart nodes each carry a source. Verdict cross-check per [[proto-91-verdict-cross-check]].

Related: [[proto-10-w1-overview]], [[proto-19-w1h-draft-research-plan]], [[proto-17-w1f-multi-llm-eval]]
