# H-3: GitHub Issue Cleanup (draft for Srujan)

Per vajrAastra §8 and SOUTH_CANON §J, here is the draft issue cleanup text. 
Only you should apply these changes; do not push without explicit approval.

## Close these issues (fusion is disproven, G-B12 failed):

- **#2** L1-A Char-alignment fuser core: close — fusion best‑of‑N corpus unnecessary after G-B12 0/115 result.
- **#3** L1-B Fusion quality guards + leaderboard row: close — guards redundant without fusion.
- **#4** L1-C Wire fused corpus into seal + Stage‑3 SFT: close — corpus wiring blocked by G‑B12.

## Rewrite/restructure these:

- **#6** L2‑B LLM‑arbiter gold transcription (Gemini): rewrite — its output is another model’s guess, not “glyphs on page” gold (law §7, Aryan’s lane). Close pending native GT.
- **#7** L2‑C True CER leaderboard (accuracy, n=gold): rewrite — it should depend on human GT, not an unvalidated fuser. Law §8 forbids comparability across benchmarks.

## Fold/rescope these:

- **#5** L2‑A Stratified gold set (~40 pages): fold into T2 GT‑expansion queue. Label every such page PSEUDO; never gold. Circularity rule: a pseudo‑GT page may never rank an engine that contributed to it.
- **#8 / #9 / #10** Rescope to code‑only CI and verifier tests: 
  - #8: Make CI workflow run `level2/tests/run_tests.py` with VAJRA_CODE_ONLY=1; skip any pack‑schema checks when out/ absent (GitHub clone).
  - #9: Add schema/NFC validation as a T3 gate in the CI workflow (already implemented in run_tests.py T3).
  - #10: L10 guard test (T6 in run_tests.py) — protected files must not change unless PR title contains L10-OVERRIDE.
- **#11** Make the T1 headline: Sarvam on our pages, scored with our GT and CER method, per T1 protocol. Update issue title and description to reflect the 66‑page ₹33 gate (not ₹200 full run).

## Update epic:

- **#1** [Epic] Path to Ultimate: adjust the “fused output, accuracy spine, hardening” narrative to reflect that fusion is **disproven** (G‑B12: 0/115 beat best single; union worse than worst). The spine now is: (1) sealed basis CER medians, (2) corrected basis (n=101, mojibake gate), (3) own‑script pool (n=66, ta 53/te 5/kn 4/ml 4), (4) Sarvam 66‑page run (₹33, gate ₹2), (5) stratified bootstrap verdict. No novel backbone claim.

## Action required (your decisions, H‑1 / H‑2 / H‑3):

1. **H‑1**: Provide SARVAM_API_KEY + approve ₹2 gate → then ~₹33 for 66 own‑script pages.
2. **H‑2**: Name native reviewers for Kannada and Malayalam (ask Vinay). Without them, T2 lane‑2 is Telugu‑only.
3. **H‑3**: Execute the issue closures/rewrites above. No code may be merged, no money spent, no team messages sent without your approval.

— End of draft. Store in docs/campaign/; do not push without your sign‑off.