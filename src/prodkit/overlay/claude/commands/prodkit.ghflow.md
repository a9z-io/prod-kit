---
description: Git workflow assistant — create a branch, stage changes, commit with a
  suggested conventional commit message, and open a GitHub pull request. Confirms
  with the user before each destructive step.
handoffs:
  - label: Run again
    agent: prodkit.ghflow
    prompt: Run the GitHub workflow again
---

## User Input

```text
$ARGUMENTS
```

Optional context hint or ticket reference (e.g. "fix login bug" or "PROJ-123").

## Goal

Walk through the full GitHub workflow:

1. Inspect the current repo state (branch, staged/unstaged changes)
2. Create a feature branch if on `main`/`master` (with approval)
3. Stage changes and propose a conventional commit message (with approval)
4. Commit (with approval)
5. Push and open a pull request via `gh` CLI (with approval)

Always pause for explicit user confirmation before creating a branch, committing,
pushing, or opening a PR. Never skip a confirmation even if earlier steps were approved.

Requires `git` and `gh` (GitHub CLI, authenticated). If `gh` is missing, complete the
branch/commit/push steps and provide manual PR instructions.
