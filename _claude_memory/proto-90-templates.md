---
name: proto-90-templates
description: "Copy-paste templates for the South campaign — wave checkpoint file, subagent report footer, fix-spec row, evidence record, DISPATCH_LOG entry, feed §11 log line, and the ≤10-line boss report"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:17:19.788Z
---

# TEMPLATES

## 1. Wave checkpoint — `docs/campaign/checkpoints/W<n>.md`
```markdown
# W<n> CHECKPOINT — <wave name>
Started: 2026-MM-DD HH:MM IST · Lead: Sonnet session <id if known> · Protocol: memory proto-<nn>…
## Pre-flight
<paste pre-flight outputs from proto-02, trimmed>
## Steps
- [ ] <step id> <name> — output: <path> — verified by: <subagent> — evidence: <command → result>
## Partial progress (for resume)
<step id>: <last completed sub-step>
## Deviations
PROTOCOL-DEVIATION: <what> — <evidence>
## Open issues / boss decisions needed
STATUS: IN PROGRESS | COMPLETE
```

## 2. Footer every subagent report must end with
```markdown
### Sources relied on
- file:line — what it supports
- URL (opened <date>) — what it supports
### UNRESOLVED
- <claim I could not verify> — what I tried
```

## 3. Fix-spec row (Verdict) — `level2/probe22/fix_specs/<name>.md`
```markdown
### FS-07 · BLOCKER · VINAY_MEETING_PACKET.md:124
- OLD (exact, occurs once): `…`
- NEW (exact): `…`
- EVIDENCE: `<command>` → `<output>`
- WHY: <one line>
```

## 4. Evidence record (research)
`ID · claim · tag (PRIMARY/MEASURED/DERIVED/CONTRADICTION/UNKNOWN/REJECTED/DEAD) · source (file:line or URL + date opened) · set/n/metric · decision it can change`

## 5. `DISPATCH_LOG.md` entry (append at wave end; Miss owns the file — the lead may append when no Miss subagent is running)
```markdown
## <date> <HH:MM IST> — W<n> <wave name> (Sonnet lead, protocol: memory proto files)
| step | owner | output | verified | status |
|---|---|---|---|---|
**Hard laws held:** no training, no downloads, no Sarvam calls, sealed dirs untouched (counts: out 4001 / reports 48 / probe22-out 13289 / arc 413), locked files untouched.
**Open:** <items> · **Boss decisions pending:** <U-ids>
```

## 6. `OCR_AGENT_MEMORY_FEED.md` §11 log line (append-only, never rewrite earlier lines)
`- 2026-MM-DD HH:MM (Sonnet lead, W<n>): <what happened in one sentence>; outputs <paths>; verified <yes/partial>; open <n>.`

## 7. Boss report (≤10 lines, plain words, send at every wave end)
```
W<n> <name>: COMPLETE | PARTIAL (<what was cut and why>)
Done: <3 lines max, each with the file>
Found: <the 1–3 facts that change a decision, each with n>
Not done / risks: <1–2 lines>
Need from you: <U-questions with the recommended answer> + <any paste request, e.g. ChatGPT prompt at docs/campaign/CHATGPT_EVAL_PROMPT.md>
Next: W<n+1> <name> starts unless you say stop.
```

Related: [[proto-00-runbook]], [[proto-02-preflight-and-checkpoints]], [[proto-91-verdict-cross-check]]
