---
name: proto-91-verdict-cross-check
description: "The generic Verdict cross-check every deliverable must pass before it counts — the reviewer prompt, the 10-point checklist (numbers, n, metric, sources, dates, scope, law), PASS/FAIL rules and the 2-round fix loop"
metadata:
  node_type: memory
  type: project
  originSessionId: 8e7ec69e-22b6-4702-a989-3397b9a99c1e
  modified: 2026-09-29T15:17:33.271Z
---

# VERDICT CROSS-CHECK (run on every deliverable; the reviewer is never the author)

## Dispatch
A fresh Sonnet subagent, role Verdict. Prompt = shared context block ([[proto-01-law-and-guardrails]] §F) + this block + the path of the deliverable + the path of the author's report.

## Reviewer block (paste)
> You are the Verdict agent reviewing `<deliverable>`. Your default is FAIL until evidence says PASS. Do not rewrite the document; list defects with exact fixes.
> Check, and report each as PASS/FAIL with evidence:
> 1. **Numbers:** pick every number (or at least 15 at random if there are more). Re-derive each from its cited source with a command or by opening the URL. Mismatch = FAIL.
> 2. **n and metric:** every performance number states its set, n and metric (CER mean/median, Sarvam score ≠ CER). Missing = FAIL.
> 3. **Comparisons:** every "wins/beats/best/SOTA" has same items + same metric + n ≥ 50 (D4) + a named test, or is labelled directional. Otherwise FAIL.
> 4. **Sources:** every URL was opened by the author (spot-open 3); every file:line exists and says what is claimed (spot-check 5). Invented = FAIL (severity BLOCKER).
> 5. **Quotes:** quoted text appears verbatim in the source (`grep -F`).
> 6. **Dates:** weekday matches the ISO date; uncertain dates are "TBC", not guessed.
> 7. **Scope:** the document does what its protocol file asked (compare against the protocol's section list); nothing required is missing, nothing duplicates a precursor's content.
> 8. **Law:** no writes to sealed/locked paths (`git status --short`), no training/downloads/Sarvam traces, no new md at root.
> 9. **Contradictions:** the deliverable does not contradict directive Part A or another Wave deliverable without saying so explicitly (CONTRADICTION tag).
> 10. **Honesty:** UNKNOWN/empty sections are stated as such, not filled with generic text.
> Output: a table `check · PASS/FAIL · evidence · exact fix` and an overall verdict: PASS / PASS-WITH-FIXES (list) / FAIL.

## Fix loop
Round 1: author (or Miss) applies the exact fixes → a reviewer (may be the same Verdict subagent via SendMessage) re-checks only the failed items.
Round 2: same. Still failing after round 2 → the item goes to the boss in the wave report as "unresolved, here is why"; the deliverable is marked PARTIAL.

## What the lead records in the checkpoint
`<step> verified: PASS | PASS-WITH-FIXES (n fixes, round k) | FAIL → escalated` + the reviewer's subagent id/description.

Related: [[proto-00-runbook]], [[proto-01-law-and-guardrails]], [[proto-90-templates]]
