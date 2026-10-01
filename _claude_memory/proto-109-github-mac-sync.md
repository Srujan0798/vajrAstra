---
name: proto-109-github-mac-sync
description: "2026-10-01 — two-way sync between the Mac (~/Desktop/South + ~/.claude memory) and GitHub branch boss/campaign-docs (the planner's exchange channel). Mac→GitHub = text-only snapshot push (never .env, data, weights); GitHub→Mac = path-scoped checkout of planner-owned files + memory copy. Agent 2 runs it at the start and end of every round."
metadata:
  node_type: memory
  type: project
---

# PROTO-109 — GITHUB ⇄ MAC SYNC (boss/campaign-docs is the exchange branch; main is never touched)

## Rules
- Only branch `boss/campaign-docs`. Never `main`, never force-push, never delete.
- Text only: md, txt, json, yaml, yml, js, py, tex.
- Never synced: `.env` or any key, `Datasets/`, `level2/out/`, `level2/benchmark/pages/`, model weights (`models_bodhan/`, `.deps/`), venvs.
- **Who owns what:**
  - The planner (cloud) owns `_claude_memory/*`, `docs/campaign/checkpoints/NEXT.md`, `docs/campaign/drafts/` and `docs/campaign/handoff_*`.
  - The agents (Mac) own everything else: W4.md, DISPATCH_LOG, code, reports.
- **On a conflict, the owner's copy wins.** Never overwrite the other side's files blindly.

## A. Mac → GitHub (Agent 2, end of every round)
```
cd ~/Desktop/South && git fetch -q origin boss/campaign-docs
git worktree add -f ~/bs_sync origin/boss/campaign-docs -B boss/campaign-docs
rsync -a --prune-empty-dirs --include='*/' --include='*.md' --include='*.txt' --include='*.json' --include='*.yaml' --include='*.yml' --include='*.js' --include='*.py' --include='*.tex' --exclude='*' docs product scripts ~/bs_sync/
rsync -a --prune-empty-dirs --exclude='out/' --exclude='benchmark/pages/' --exclude='models_bodhan/' --exclude='models/*/weights/' --include='*/' --include='*.md' --include='*.txt' --include='*.yaml' --include='*.py' --include='*.json' --exclude='*' level2 ~/bs_sync/
for d in _reports .ecc/memory; do [ -d "$d" ] && mkdir -p ~/bs_sync/$d && rsync -a --include='*/' --include='*.md' --exclude='*' $d/ ~/bs_sync/$d/; done
cp *.md ~/bs_sync/
rsync -a ~/.claude/projects/*South*/memory/ ~/bs_sync/_claude_memory/
cd ~/bs_sync && ! grep -rlE 'hf_[A-Za-z0-9]{30,}|sk_[A-Za-z0-9]{20,}' . && git add -A . && git add -f _reports .ecc/memory level2/research 2>&1 | tail -1; git commit -qm "mac sync $(date +%F_%H%M)" && git push -q origin boss/campaign-docs && git log --oneline -1
cd ~/Desktop/South && git worktree remove --force ~/bs_sync
```
- The `grep` line is the secret guard: if it prints a file name, STOP and do not push.
- The json include on level2 is for manifests and reports. Check `du -sh ~/bs_sync` stays under ~50 MB before the commit.

## B. GitHub → Mac (Agent 2, start of every round, after the planner says "pushed")
```
cd ~/Desktop/South && git fetch -q origin boss/campaign-docs
git checkout origin/boss/campaign-docs -- _claude_memory docs/campaign/checkpoints/NEXT.md docs/campaign/drafts docs/campaign/handoff_2026-10-01_v4_integration docs/campaign/protocols/proto-108-plan-v4-final.md
M=$(ls -d ~/.claude/projects/*South*/memory); mkdir -p "$M/_archive_2026-09-30"
rsync -a _claude_memory/ "$M/"
git restore --staged _claude_memory docs/campaign 2>&1 | tail -1
bash scripts/agent_bootstrap.sh --sync-only
```
- `git checkout <branch> -- <paths>` overwrites only those planner-owned paths. It touches no agent-owned file and does not change the current branch.
- `rsync` without `--delete` adds or updates memory files and deletes nothing.

## C. Check after each sync
- Mac: run `git log --oneline -1 origin/boss/campaign-docs` and `head -3 ~/.claude/projects/*South*/memory/MEMORY.md`.
- Log one W4.md line: `SYNC <A|B> <commit> <time>`.
