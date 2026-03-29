---
name: prodkit-ghflow
description: Git workflow assistant that creates a branch, stages changes, proposes a
  conventional commit message, commits on approval, then creates a GitHub pull request.
  Covers the full branch → commit → PR loop with user confirmation at every destructive step.
compatibility: Requires git and gh (GitHub CLI) installed and authenticated
metadata:
  author: prod-kit
  source: .claude/skills/prodkit-ghflow/SKILL.md
---

# Prodkit GH Flow Skill

## User Input

```text
$ARGUMENTS
```

Optional: a short context hint or ticket/issue reference (e.g. "fix login bug" or "PROJ-123").
If provided, use it to inform branch name and commit message suggestions.

---

## Overview

Walk the user through the full GitHub workflow in five stages:

1. Inspect repo state
2. Create a feature branch (if needed)
3. Stage changes and propose a commit message
4. Commit on approval
5. Push and open a pull request on approval

**Always pause for explicit user confirmation before any destructive or shared-state action**
(creating a branch, committing, pushing, opening a PR). Never skip a confirmation step even
if the user has approved earlier steps.

---

## Stage 1 — Inspect Repo State

Run these commands and capture their output:

```bash
git status --short
git diff --staged
git diff
git log --oneline -5
git rev-parse --abbrev-ref HEAD
```

From the output, determine:

- **Current branch** (`CURRENT_BRANCH`)
- **Has staged changes**: whether `git diff --staged` is non-empty
- **Has unstaged changes**: whether `git diff` is non-empty
- **Is on default branch**: whether `CURRENT_BRANCH` is `main` or `master`
- **Has commits**: whether `git log` returns any output

If there are **no changes at all** (clean working tree, nothing staged):
- Report: "Nothing to commit — working tree is clean."
- Ask the user whether they want to create an empty branch or cancel.
- If cancel: stop here.

---

## Stage 2 — Branch

### 2a. Already on a feature branch

If `CURRENT_BRANCH` is not `main` or `master`, the user is already on a feature branch.

Report:
```
Already on branch: <CURRENT_BRANCH>
Skipping branch creation.
```

Set `WORKING_BRANCH = CURRENT_BRANCH` and proceed to Stage 3.

### 2b. On default branch — propose a new branch name

Derive a branch name:
- If `$ARGUMENTS` is non-empty, use it as the primary source.
- Otherwise, summarize the diff/status to infer intent.
- Format: `<type>/<short-kebab-description>` — e.g. `fix/login-timeout`, `feat/user-dashboard`, `chore/update-deps`.
- Keep it under 50 characters.
- Use only lowercase letters, numbers, and hyphens.

Present to the user:

```
Proposed branch: <branch-name>

Actions:
  A) Use this name
  B) Edit — type your preferred branch name
  C) Cancel
```

Wait for the user's response.

- If **A**: use the proposed name.
- If **B**: use the name the user provides (validate: lowercase, no spaces, no special chars except `-` and `/`).
- If **C**: stop.

Run:
```bash
git checkout -b <branch-name>
```

Confirm the branch was created:
```bash
git rev-parse --abbrev-ref HEAD
```

Report: `Created and checked out branch: <branch-name>`

Set `WORKING_BRANCH = <branch-name>`.

---

## Stage 3 — Stage Changes and Propose Commit Message

### 3a. Stage changes

If there are unstaged changes and no staged changes yet, ask:

```
Stage all changes? (git add -A)

  A) Yes, stage everything
  B) No, I'll stage manually — tell me when you're ready
  C) Cancel
```

- If **A**: run `git add -A`
- If **B**: wait for the user to say they're ready, then re-run `git diff --staged` to confirm something is staged
- If **C**: stop

If nothing ends up staged after this step, report an error and stop:
```
Nothing staged — no files selected for commit. Cancelling.
```

### 3b. Propose commit message

Read the final staged diff:
```bash
git diff --staged
```

Compose a commit message following the Conventional Commits format:
- First line: `<type>(<optional scope>): <short imperative summary>` — max 72 characters
- Optional body: wrap at 72 characters, explain *why* not *what*
- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `perf`, `style`

Present to the user:

```
Proposed commit message:

  <type>(<scope>): <summary>

  <optional body>

Actions:
  A) Use this message
  B) Edit subject line — type your preferred subject
  C) Write full message — type the complete commit message
  D) Cancel
```

Wait for the user's response and set `COMMIT_MESSAGE` accordingly.

---

## Stage 4 — Commit

Run:
```bash
git commit -m "<COMMIT_MESSAGE>"
```

On success, report:
```
Committed: <short hash> <subject line>
```

On failure, show the error output and stop. Do not retry automatically.

---

## Stage 5 — Push and Pull Request

### 5a. Confirm push

Ask:

```
Push branch <WORKING_BRANCH> to origin and open a pull request?

  A) Yes — push and create PR
  B) Push only — skip PR creation
  C) Cancel
```

Wait for the user's response.

- If **C**: stop (commit is already local, that's fine).

### 5b. Push

Run:
```bash
git push -u origin <WORKING_BRANCH>
```

On failure, show the error and stop. Common issues to mention:
- No `origin` remote configured
- Authentication / SSH key problems
- Branch already exists on remote with diverged history (suggest `--force-with-lease` cautiously)

### 5c. PR creation (if user chose A)

Compose PR title and body from the commit message and diff:

- **Title**: the commit subject line (or a refined version if the commit message is terse)
- **Body**:
  ```markdown
  ## Summary
  <2-4 bullet points describing what changed and why>

  ## Test plan
  <bullet checklist of things to verify before merging>

  🤖 Generated with [Claude Code](https://claude.ai/claude-code) via `/prodkit.ghflow`
  ```

Present the draft to the user:

```
Proposed PR:

  Title: <title>

  Body:
  ---
  <body>
  ---

Actions:
  A) Create PR with this content
  B) Edit title — type your preferred title
  C) Cancel
```

Wait for the user's response.

- If **B**: use the new title; keep the body as-is.
- If **C**: stop (push is already done).

Run:
```bash
gh pr create --title "<title>" --body "$(cat <<'PRBODY'
<body>
PRBODY
)"
```

On success, output the PR URL.

On failure (e.g. `gh` not installed or not authenticated):
- Report the error clearly.
- Provide the manual equivalent:
  ```
  gh pr create --title "<title>" --web
  ```
  or instruct the user to open a PR from the GitHub web UI.

---

## Error Handling

| Situation | Action |
|-----------|--------|
| `git` not found | Report: "git is not installed or not in PATH." Stop. |
| `gh` not found | Proceed through commit + push; warn at PR step that `gh` CLI is required. Provide web UI link. |
| `gh` not authenticated | Report `gh auth login` instruction. Stop at PR step. |
| Not a git repo | Report: "No git repository found in the current directory." Stop. |
| Merge conflict markers in diff | Warn user before staging: "Conflict markers detected — resolve conflicts before committing." Stop. |
| Detached HEAD | Warn: "Repo is in detached HEAD state. Create a named branch first." Stop. |

---

## Summary Output

After the workflow completes (or is cancelled at any stage), print a status summary:

```
── prodkit.ghflow summary ──────────────────────────
Branch:  <WORKING_BRANCH>          [created | existing]
Staged:  <N files changed>
Commit:  <hash> <subject>          [committed | skipped]
Push:    origin/<WORKING_BRANCH>   [pushed | skipped]
PR:      <URL>                     [opened | skipped]
────────────────────────────────────────────────────
```
