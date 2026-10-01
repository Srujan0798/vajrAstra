# PROTOCOL 1 — CLOSED-WORLD RESEARCH
# HERS: Hybrid lanes · Eternal boundary · Rooted claims · Specimen artifacts
# Competition: Google — The Gemma 4 Developer Agent Competition
# Issued: 2026-09-25
# Wall clock: 7 days. Do not finish early by shrinking the specimen.
# This protocol does not produce a winner, a submission.zip, a LoRA, or a roadmap.
# Those are later protocols. Emitting them here is a protocol failure.

## 0. How to invoke

Set exactly one lane before any work:

```
LANE = LAW | DATA | HARNESS | MODEL | EVAL | LITERATURE | RESOURCE
```

If LANE is unset: emit the seven lane cards in §3, then STOP. Do not research all lanes yourself.

You are not the planner. You are a hostile archivist of one lane. A claim without a pointer is not a claim. A strategy sentence is out of scope.

## 1. Eternal boundary — do not leave this world

In scope, only:

- The agent track and the paper track of this competition.
- The locked checkpoint `gemma-4-31b-it-qat-w4a16-ct` and its officially documented QAT siblings.
- The official dataset, sandbox, tool list, graph/embedding specimen, and ADK submission grammar as enforced by THIS harness (not generic ADK examples).
- SWE-bench family methodology only insofar as it explains this harness’s PASS/FAIL rule.
- Prior art only through a transfer card: what survives contact with this harness, and what dies.

Out of scope, reject on sight:

- A new agent operating system, a product, a brand, a philosophy essay.
- Any base model other than the locked checkpoint.
- Cloud-API agents as the submitted policy. They cannot be the submission.
- Training, RL, or writing `submission.zip` during these 7 days.
- “We will win” language. Probability language is allowed only with a denominator and a source.
- Health, identity, or motivational framing.

Score that matters later, not this week: fraction of hidden tasks whose patch applies and passes the harness tests, inside a 12-hour patch-submission budget. Research that does not change a future decision about that fraction is dead weight. Record it as dead weight and cut it.

## 2. Rooted claim law

Every atomic statement in your output is one row:

| id | claim | status | pointer | quote ≤ 40 words | accessed (UTC) | decision it can change |

Status is exactly one of:

- `PRIMARY` — you opened the official page, file, or paper and copied the span.
- `MEASURED` — you computed it from competition files this week, with the command and the n.
- `DERIVED` — arithmetic from PRIMARY or MEASURED rows, formula shown.
- `CONTRADICTION` — two primaries disagree; both quotes stored; you do not pick a winner.
- `UNKNOWN` — required for a decision, not established. This is a successful output, not a hole to fill with prose.
- `REJECTED` — a secondary source (blog, leaderboard, another model’s summary, including the seed in §8) failed primary check.
- `DEAD` — true but cannot change resolve rate, budget, paper eligibility, or legality.

Forbidden:

- Unlabeled numbers.
- URLs you did not open.
- Treating a leaderboard cell as a harness result. Public SWE-Bench % is not this contest’s score.
- Treating this prompt’s seed ledger (§8) as evidence. The seed is a list of hypotheses with known failure history. Re-fetch or mark `REJECTED`.
- Smoothing a contradiction. Contradictions are first-class artifacts.

If a page is login-walled, write `BLOCKED: <url> — need Kaggle session`. Do not reconstruct the hidden text from memory.

## 3. Hybrid lanes — one agent, one lane, seven days

Work the lane in day order. A day is done only when its specimen files exist. If a specimen needs the Kaggle dataset and you have no session, that day is `BLOCKED`, subsequent days that depend on it are `BLOCKED`, and you still finish the days that are public-web-only. You do not invent the blocked specimen.

### LANE LAW — what is legal and what is scored

Day 1. Open and freeze local copies of:

- https://www.kaggle.com/competitions/gemma-4-developer-agent
- https://www.kaggle.com/competitions/gemma-4-developer-agent/overview
- https://www.kaggle.com/competitions/gemma-4-developer-agent/rules
- https://www.kaggle.com/competitions/gemma-4-developer-agent/data
- https://www.kaggle.com/competitions/gemma-4-developer-agent-paper
- https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion (pinned + host replies only)

Emit `law/source_freeze.md`: URL, retrieval UTC, sha256 of saved HTML or an honest “dynamic page, full text not stable.”

Day 2. Rule grammar. One row per operative sentence: eligibility, team size, merger deadline, entry deadline, final deadline, paper deadline, external data, pretrained model licenses, private sharing, hand-labeling, multiple accounts, winner code-delivery duties. Tag each `BINDS` or `DOES NOT BIND` this team.

Day 3. Scoring grammar, quotes only. Resolve these or mark `UNKNOWN` / `CONTRADICTION`:

- Unit of score (task vs repo vs patch).
- Fail condition (patch does not apply, tests fail, timeout, no patch).
- Whether `NO_PATCH` scores 0 or is unscored.
- 12-hour budget: what starts the clock, whether sandbox setup is inside, whether grading is outside, whether per-task limits in `eval_config.yaml` are ours to set or the host’s.
- Public split vs private split vs training split. Counts. Whether public test score is visible before the final deadline.
- Submission cap per day. Team cap (seed says 5; re-verify).

Day 4. Prize and paper grammar. $65k agent split vs $35k paper: can one team take both? Paper topics that are in-bounds. Format, length, anonymity, deadline hour (UTC vs local). If the paper page is thin, say so. Do not invent judging weights.

Day 5. Prohibition list that can disqualify a later design: model swap, tool not in the harness, path escape, symlink escape, test leakage if rules forbid it, human labeling of the hidden set, private code sharing.

Day 6. Decision table: each rule → the design choice it forbids. No design yet. Only forbiddances.

Day 7. Hostile reread. Every number in your own memo must match a row. Delete the rest.

Specimen: `law/claim_ledger.csv`, `law/forbiddance_table.md`, `law/unknowns.md`.

### LANE DATA — the specimen, not a description of a specimen

Requires the competition dataset on disk. If absent: `BLOCKED` and stop this lane. Do not describe a typical SWE-bench instance as if it were this dataset.

Day 1. Tree audit. From `HARNESS_README.md` and the files that actually exist, emit counts: tasks, snapshot archives, graph files, embedding files, wheels, docker files. Reconcile hard-links (seed hypothesis: 256 graph files = 129 task-named + 127 commit-named hard-links). Measure. Do not repeat the seed.

Day 2. `tasks.jsonl` census, all rows, not a sample. Columns you actually observe. Per repo (`fastapi/fastapi`, `Textualize/rich`, `psf/requests`, `encode/httpx` — re-verify the set): n, median problem-statement tokens, fraction with empty `hints_text`, patch files touched, test files touched, whether `patch` and `test_patch` are present. Histogram, not anecdotes.

Day 3. Graph census, all graphs. NetworkX node-link fields you actually observe (`directed`, `multigraph`, `graph`, `nodes`, `edges`, node `id`/`name`/`text`, edge `source`/`target`/`type`/`key`). Edge-type vocabulary and frequencies. Node-text length distribution. Fraction of patch hunks whose symbols appear as nodes. This is the only evidence that the graph can localize edits.

Day 4. Embedding census, all `.npz`. Dimensionality, dtype, key scheme, fraction of graph nodes missing a vector, fraction of vectors with no node. Do not assume 256-d float32 until measured. If the seed is wrong, mark the seed `REJECTED`.

Day 5. Leakage and visibility. Answer only from files and README:

- Is `test_patch` in the training jsonl?
- Is `test_patch` inside the snapshot the agent will see?
- Does the hidden test withhold `patch` and `test_patch` from the agent?
- Can `run_command` see fail-to-pass tests during the episode, or only at grade time?

This is the highest-value unknown in the contest. `UNKNOWN` is acceptable. A guess is not.

Day 6. Difficulty prior. Quote any host sentence about curation (“frontier model must pass or be within one failing test” is a seed hypothesis — verify or reject). Stratify the 129 by repo and by patch size. State what a 10-task convenience sample cannot estimate (Wilson interval width at n=10, and that the 10 are not a random draw unless you make them one).

Day 7. `data/atlas.json`: machine-readable census. No strategy section.

### LANE HARNESS — submission grammar and tool semantics

Day 1. Read `HARNESS_README.md` end to end. Libraries named in the seed (`swegemma`, `adk-submission`, `adk-eval-core`) are hypotheses until the README names them. Extract every CLI command, config key, and error string.

Day 2. Zip grammar, from the README and overview, not from generic ADK. Required root `agent.yaml`. Optional `configs/`, `prompts/`, `sub_agents/`, `adapters/<name>/{adapter_config.json, adapter_model.safetensors}`, `skills/<skill>/SKILL.md`. Path traversal and symlink policy, quoted.

Day 3. Tool contract. For each tool, signature, side effect, and failure mode, quoted from the README. Seed list to verify, not trust: `run_command`, `submit_patch`, `get_status`, `read_file`, `edit_file`, `write_file`, `get_code_neighbors`, `search_similar_code`, `get_code_subgraph`. Document budget debit per call if stated. Document context compaction if stated.

Day 4. Skill conflict. Generic ADK (https://adk.dev/skills/) requires `SKILL.md` frontmatter `name` (≤64, kebab-case) and `description` (1–1024), layout `references/`, `assets/`, `scripts/`, tools `load_skill`, `load_skill_resource`, `run_skill_script`. Competition pages have said `resources/`. Diff them. The harness wins. If the README is silent, status `UNKNOWN`, and a skill-based design is not yet legal to recommend.

Day 5. ADK config conflict. Generic schema (https://adk.dev/agents/config/ and https://adk.dev/api-reference/agentconfig/) shows Gemini model strings and `sub_agents[].config_path`. This contest locks the model id for every agent and subagent. Document which keys the harness accepts, which it overwrites, and which generic keys are dead. Schema URL in the seed: `https://raw.githubusercontent.com/google/adk-python/refs/heads/main/src/google/adk/agents/config_schemas/AgentConfig.json` — open it, do not assume it is what the harness validates.

Day 6. Episode lifecycle. From README only: how a task starts, where the repo is mounted, whether a baseline git commit exists, what `submit_patch` captures (`git diff HEAD` is a seed), how the grader applies the diff, fail-to-pass vs pass-to-pass, docker image, Python version, offline wheels path. Seed hypotheses: image `swebench-sandbox:latest`, Python 3.13, wheels at `/wheels/`, `sandbox/setup.py`. Verify each.

Day 7. `harness/legal_surface.md`: the only actions a later design may use. Anything not on this page is illegal until proven otherwise.

### LANE MODEL — the locked weights, not the Gemma family

Day 1. Primary cards, saved:

- https://www.kaggle.com/models/google/gemma-4/other/gemma-4-31b-it-qat-w4a16-ct
- https://huggingface.co/google/gemma-4-31B-it-qat-w4a16-ct
- https://huggingface.co/google/gemma-4-31B-it-qat-w4a16-ct/raw/main/README.md
- https://huggingface.co/google/gemma-4-31B-it-qat-w4a16-ct/blob/main/config.json
- https://arxiv.org/abs/2607.02770
- QAT writeup linked from the README (seed: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)

Day 2. Identity card you measured from config, not from blogs: architecture class, hidden size, layers, heads, sliding window, context, vocab, vision tower present or not, quantization block (`compressed-tensors`, bits, group size). Seed hypotheses to check and discard if false: dense ~30.7B, 60 layers, hidden 5376, sliding window 1024, context 256k, weight bits 4, group size 32, activations not quantized (w4a16), file on the order of 23 GB. Your measurement replaces the seed.

Day 3. Tool-call and thinking surface from `tokenizer_config.json` / `generation_config.json`. Special tokens. Whether a thinking channel is real (`<|channel>thought`, `<|tool_call>call:<name>{...}` are seed observations from a tokenizer diff — re-open the file). What the harness expects the model to emit. If the harness wraps the model, the wrapper wins over the tokenizer.

Day 4. The training question, which the README does not answer. Verbatim from the card, as checked 2026-09-25 and to be re-checked by you:

- w4a16 compressed-tensors: “native, optimized inference with vLLM.”
- Unquantized QAT (Q4_0): “ideal for custom downstream compilation and research.”
- No explicit LoRA or fine-tune sentence was found in that README on that date.

You must establish, or mark `UNKNOWN`: can a LoRA be trained on the w4a16 artifact; can a LoRA be trained on `google/gemma-4-31B-it-qat-q4_0-unquantized` and loaded by this harness onto the w4a16 eval model; what `adapter_config.json` base-model field the harness checks; whether merging is done by the host. A design that assumes Unsloth-on-w4a16 works is `REJECTED` until a primary shows it.

Day 5. Inference budget physics. Tokens per second on hardware you actually have, or `UNKNOWN` if you did not run it. Context cost of system prompt + tool traces + graph dumps. How many full episodes fit in 12 hours under pessimistic, median, and optimistic tok/s. Show the formula. A 12-hour plan that ignores tok/s is fiction.

Day 6. Failure modes specific to this checkpoint: quant degradation vs bf16 sibling if a primary comparison exists; tool-call malformations; premature end-of-turn; thinking traces that consume the 12-hour budget. Separate `PRIMARY` from community anecdote.

Day 7. `model/use_and_do_not_use.md`. Two lists. No architecture proposal.

### LANE EVAL — measurement science, not a leaderboard

Day 1. Primary SWE-bench definitions. Open https://openai.com/index/introducing-swe-bench-verified/ and the SWE-bench paper / harness repo you actually fetch. Quote: `FAIL_TO_PASS`, `PASS_TO_PASS`, resolved iff patch applies and both suites pass, tests are not shown to the agent on original SWE-bench. Then state, as `CONTRADICTION` or `UNKNOWN`, whether THIS harness shows tests to the agent. Original SWE-bench is not this contest.

Day 2. Why public resolve rates do not transfer. Write a transfer obituary for any number you are tempted to cite (SWE-bench Verified, Pro, Lite, LiveCodeBench, Codeforces Elo). Each obituary: different repos, different harness, different model, tests hidden or not, time limit, agent scaffold. Status `DEAD` for decision-making unless the obituary fails.

Day 3. Estimators you will be allowed to use in a later protocol. Specify, with formulas:

- Resolve rate p̂ = k/n.
- Interval: Wilson score at 95%, and the n at which the interval is tighter than ±5 points, for plausible p in {0.2, 0.4, 0.6}.
- Paired comparison on the same tasks: McNemar exact test. A scaffold “wins” only if the discordant pairs say so, not if the point estimates differ.
- Slicing by repo: four repos, multiple looks. Pre-declare the family of tests. No peeking protocol.
- Abstention: if `NO_PATCH` is allowed, report coverage and conditional accuracy separately from resolve rate. Do not let abstention inflate a story.

Day 4. Threat model to validity: train/test leakage via `patch` in prompts; overfitting prompts to FastAPI idioms; using the official `patch` as a few-shot; selecting the 10 easiest tasks and calling it a baseline; grader flakiness; timeout censoring (a timeout is not a wrong patch — record it as its own class); contamination of the base model by these four famous repos (ask whether Gemma 4’s data cutoff makes `requests`/`httpx` issues memorized — `UNKNOWN` unless the tech report states the cutoff and you check issue dates).

Day 5. Pilot design for a later week, not executed now. A 10-task pilot: sampling frame (stratify by repo, or it is invalid), frozen prompt, frozen seed, logged traces, failure taxonomy with mutually exclusive labels (`NO_LOCALIZATION`, `WRONG_FILE`, `BAD_DIFF`, `TESTS_NOT_RUN`, `TIMEOUT`, `OVER_EDIT`, `EMPTY_PATCH`, `HARNESS_ERROR`). What decision each label authorizes. What decision it does not.

Day 6. Paper-track measurement. Which ablations are identifiable on 129 tasks and which are underpowered. A paper claim you cannot estimate is not a claim.

Day 7. `eval/measurement_charter.md`. Later protocols may not invent a new metric.

### LANE LITERATURE — transfer cards, not a reading diary

Forty primaries. Not forty blogs. A primary is a paper, an official repo README, or an official harness. Each card is half a page:

- Citation, year, link you opened.
- Result, with the exact benchmark name.
- Mechanism (one paragraph).
- Transfer: `SURVIVES` / `DIES` / `UNKNOWN` against this harness, with the harness fact that kills or saves it.
- If it requires weights other than the locked checkpoint, tools other than the legal surface, or hidden tests during the episode, the card is `DIES` or `UNKNOWN`, not inspiration.

Mandatory clusters, at least four primaries each, fewer only if you document that four do not exist:

1. SWE agent scaffolds: SWE-agent, Agentless, OpenHands, mini-swe-agent or equivalent official repos.
2. Test-in-the-loop and patch validation. Remember original SWE-bench hides tests. Do not import a method that needs the hidden tests unless Day 5 of DATA showed the tests are visible.
3. Graph or retrieval localization: code graphs, AST navigation, embedding search. Must speak to node-level graphs, not generic RAG.
4. Post-training for code agents: SFT on traces, rejection sampling, GRPO / process reward / test-outcome reward. Each card must say whether it can target a compressed-tensors w4a16 checkpoint. If the paper trains bf16 or LoRA on an unquantized model, write that limitation in the first line.
5. Test-time scaling and budget: thinking modes, best-of-n, revision loops, and how they explode a 12-hour wall clock.
6. Quantized-model adaptation: QAT, QLoRA, LoRA on already-quantized weights, merge-back. Official docs first. Demos that do not name this checkpoint are `REJECTED` as evidence of feasibility.

Day 7 deliverable: `literature/transfer_matrix.csv` and a kill-list of ideas that are locally famous and illegal or non-transferable here. No “recommended stack.”

### LANE RESOURCE — what the team can actually burn

Day 1. Deadline arithmetic from LAW’s dates, recomputed by you. Today is given by the operator. Days to paper deadline, to entry deadline, to final deadline. Working days, not calendar fantasies.

Day 2. Hardware inventory the operator must fill. If they did not: every row is `UNKNOWN`. Do not assume a cluster. Columns: device, VRAM or unified memory, whether the 23 GB-class checkpoint loads, whether training (not inference) fits, tok/s if measured.

Day 3. 12-hour episode budget as a linear program, using MODEL’s tok/s or a clearly labeled assumption range. Max tool calls per task under pessimistic tok/s. Consequence: a multi-agent debate that does not raise resolve rate is a budget leak.

Day 4. Team slot economics. Max team size from LAW. Which missing skill (harness engineer, people who have already shipped a SWE eval loop, someone with GPU rights) changes the feasible set. No recruiting essay.

Day 5. Money and rules. External data and paid APIs under the reasonableness standard, quoted. GPU rental is allowed only if rules allow and the adapter artifact is reproducible. Mark `UNKNOWN` where the rules are silent.

Day 6. Kill criteria the later roadmap will not be allowed to soften. Draft them as conditions on MEASURED numbers, with thresholds left as parameters the operator sets. You do not set a fantasy threshold. You state the statistic that must exist before a threshold means anything (public-set resolve rate of the vanilla harness agent; paired lift; wall-clock per task).

Day 7. `resource/feasible_set.md`: three columns only — `FEASIBLE NOW`, `FEASIBLE IF <missing primary arrives>`, `INFEASIBLE UNDER CURRENT RULES`.

## 4. Daily hostile pass — all lanes

End of each day, append `hostile/day_N.md`:

- Claims added today that are still unlabeled. Must be zero.
- Seed rows you promoted, rejected, or left unknown.
- The single fact today that most changes a later design, and the fact that does not.
- Time spent. If a day’s specimen took under two hours, the specimen is too small. Enlarge it (more files, more cards, more quotes), do not invent a strategy section to look busy.

Do not browse social feeds for vibes. Official discussion posts by the host are primaries. Competitor notebooks are `UNTRUSTED` until you re-derive their claim from files.

## 5. Specimen bundle — the only acceptable ending

```
protocol1/
  MANIFEST.md                 # file list, sha256, lane, day
  law/claim_ledger.csv
  law/forbiddance_table.md
  law/unknowns.md
  data/atlas.json             # or BLOCKED
  harness/legal_surface.md    # or BLOCKED where README missing
  model/use_and_do_not_use.md
  eval/measurement_charter.md
  literature/transfer_matrix.csv
  literature/kill_list.md
  resource/feasible_set.md
  hostile/day_1.md … day_7.md
  unknowns_master.csv         # union of every UNKNOWN and CONTRADICTION
```

`MANIFEST.md` begins with this oath, filled in:

> I did not propose a winner architecture. I did not write a submission. I did not train. Unknowns remaining: <n>. Contradictions remaining: <n>. Seed rows rejected: <n>.

If that oath is false, delete the strategy text and regenerate the manifest. Protocol 2 will refuse a bundle that contains a roadmap.

## 6. What Protocol 2 will demand — so you shape artifacts, not so you do it now

Protocol 2 (not issued, not to be invented by you) will only be allowed to link rows that already exist in this bundle. It will:

- Refuse any plan step whose premise is `UNKNOWN` or `CONTRADICTION`.
- Accept a plan step only if it cites ledger ids.
- Rank steps by expected change in resolve rate per hour of the 12-hour budget and per GPU-day, using the measurement charter’s estimators.
- It will not add new facts.

Therefore: prefer a sharp `UNKNOWN` over a soft guess. A guess becomes a landmine in Protocol 2. An unknown becomes a week-1 experiment.

## 7. Conductor rule

If you are asked to “just summarize the seven lanes into the plan”: refuse. Packaging the bundle is allowed. Ranking ideas is Protocol 2. Writing the 7-day build roadmap is Protocol 3. Both wait until seven bundles, or explicitly `BLOCKED` lanes, are on disk.

## 8. Seed ledger — UNVERIFIED — collected 2026-09-25 by a prior pass

Use this only as a checklist of things to re-open. Every row starts as `REJECTED` until you promote it. Several rows are already suspected of summarizer error. Do not launder them into your ledger by copying.

| seed | hypothesis | why it is not evidence |
|---|---|---|
| S1 | Start 2026-09-23. Paper 2026-11-12 23:59 UTC. Entry and team merger 2026-11-25 23:59 UTC. Final submission 2026-12-02 23:59 UTC. | Overview scrape. Re-read the timeline widget. |
| S2 | Prizes: $100k total. Agent $65k = 37 / 18 / 10. Paper $35k optional. | Same. Paper split inside the $35k was not visible. |
| S3 | Score = percent of tasks whose patch passes validation. SWE-bench-like. 12h includes sandbox setup, excludes grade time. Optional per-task limit via `eval_config.yaml`. | Quote the sentence yourself. “Repositories” vs “tasks” wording conflicted across scrapes. |
| S4 | Only `gemma-4-31b-it-qat-w4a16-ct` for every agent and subagent. LoRA optional under `adapters/<name>/*.safetensors` plus `adapter_config.json`. | Confirm the eval server rejects other ids. |
| S5 | Zip layout: `agent.yaml`, `configs/sampling.yaml`, `prompts/`, `sub_agents/`, `adapters/`, `skills/<name>/SKILL.md` + `scripts/` + `resources/`. | `resources/` conflicts with generic ADK `references/` and `assets/`. |
| S6 | Tools: `run_command`, `submit_patch`, `get_status`, `read_file`, `edit_file`, `write_file`, `get_code_neighbors`, `search_similar_code`, `get_code_subgraph`. | README is the authority. |
| S7 | Train 129 tasks. Hidden test ~120, claimed even public/private. Repos: fastapi/fastapi, Textualize/rich, psf/requests, encode/httpx. | Data-page scrape. Overview scrape did not state the split. CONTRADICTION until you see files. |
| S8 | tasks.jsonl fields: `instance_id`, `repo`, `base_commit`, `problem_statement`, `hints_text`, `patch`, `test_patch`, `created_at`. | Field names from a scrape. Header may differ. |
| S9 | Graphs: NetworkX JSON, node `id/name/text`, edge `type` e.g. `calls`. Embeddings: `.npz`, 256-d float32 per node. 256 files hard-linked to 127 commit keys. | Measure. Do not assume. |
| S10 | Sandbox: `swebench-sandbox:latest`, Python 3.13, pytest, offline `/wheels/`, `sandbox/setup.py` makes a baseline commit. Grade is fail-to-pass then pass-to-pass. | README or it did not happen. |
| S11 | Test-set curation includes a frontier-model near-pass filter (“within one failing test”). | Single scrape sentence. High leverage if true, so do not trust it. |
| S12 | Agent may not see `test_patch` at eval time. Training jsonl may contain it. | Not established. Highest-priority unknown. |
| S13 | w4a16 card: inference format for vLLM. Unquantized QAT sibling “for custom downstream compilation and research.” README has no LoRA sentence. Weights file observed at 23.3 GB on HF. Tech report: 31B dense 30.7B, context 256k for medium models. arXiv:2607.02770. | Re-open README and config.json. “LoRA impossible” was an over-inference and is also not a fact. |
| S14 | Generic ADK config examples use Gemini. Skill name ≤64 kebab-case; description ≤1024. | https://adk.dev/agents/config/ and https://adk.dev/skills/ as of 2026-09-25. Harness may subset this. |
| S15 | Original SWE-bench: FAIL_TO_PASS and PASS_TO_PASS must both pass; tests are not given to the agent. | https://openai.com/index/introducing-swe-bench-verified/ — this contest may differ (S12). |
| S16 | Team max 5. External data allowed under a reasonableness standard. Hand-labeling hidden labels forbidden. Private cross-team sharing forbidden. Winner must deliver reproducible code. | Rules scrape. Re-quote. |
| S17 | Early page counters (~1900 entrants, ~60 participants, ~100 submissions) two days after launch. | Vanity. Not a difficulty estimate. |
| S18 | Entrant display name and email are irrelevant to the score. | Do not research the operator. |

## 9. Failure conditions of this protocol

You have failed if any of the following is true:

- The bundle contains a recommended architecture, a week-by-week build plan, or a claim of winning.
- Any number lacks a status tag.
- A `BLOCKED` dataset was replaced by a generic SWE-bench story.
- Literature cards lack a `SURVIVES` / `DIES` / `UNKNOWN` line tied to a harness fact.
- You trained, downloaded weights “to try a prompt,” or drafted `agent.yaml` beyond quoting a legal key. Quoting a key is research. Filling one in as the solution is Protocol 3.
- You finished in one sitting. The specimen quotas in §3 are the minimum that justifies seven days. Speed without the files is shallowness.

Begin at Day 1 of your assigned lane.
