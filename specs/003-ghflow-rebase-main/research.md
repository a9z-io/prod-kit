# Research: GH Flow Rebase on Main

**Branch**: `003-ghflow-rebase-main` | **Date**: 2026-03-30

---

## Decision 1: Default Branch Detection

**Decision**: Use `git symbolic-ref refs/remotes/origin/HEAD` and strip the `refs/remotes/origin/` prefix.

**Rationale**: This reads the remote's HEAD pointer, which is set when you clone or when you run `git remote set-head origin --auto`. It correctly reflects whatever branch name the remote uses (`main`, `master`, `develop`, etc.) without hardcoding. It works on all major git hosts.

**Alternatives considered**:
- Hardcode `main` — rejected: breaks repos using `master` or custom default branch names.
- `gh repo view --json defaultBranchRef` — rejected: adds a `gh` CLI dependency for a step where `gh` may not be needed (e.g., user just wants to commit locally).
- `git remote show origin | grep 'HEAD branch'` — rejected: requires a network call (`git remote show` contacts the remote); `symbolic-ref` is local and instant.

**Failure handling**: If `symbolic-ref` fails (e.g., remote HEAD not set), fall back to attempting `main` as a default, and if that also doesn't resolve, warn and skip the sync step entirely.

---

## Decision 2: Divergence Check After Fetch

**Decision**: Use `git rev-list --count HEAD..origin/<DEFAULT_BRANCH>` to count commits behind.

**Rationale**: After `git fetch`, `origin/<DEFAULT_BRANCH>` is updated locally. `rev-list --count HEAD..origin/<DEFAULT_BRANCH>` counts commits in origin's branch that are not in the current branch — i.e., how far behind the current branch is. Returns `0` when up-to-date, a positive integer otherwise. Fast, local, no network.

**Alternatives considered**:
- `git status -sb` / parse "behind N" — rejected: requires the local branch to have a tracking relationship set up; unreliable for newly-cut branches.
- `git merge-base --is-ancestor` — rejected: only returns boolean (behind or not), doesn't provide the count for user-facing messaging.
- `git log HEAD..origin/main --oneline | wc -l` — equivalent but noisier; `rev-list --count` is the canonical form.

---

## Decision 3: Rebase Abort on Conflict

**Decision**: On any rebase failure (non-zero exit code), immediately run `git rebase --abort` and stop the workflow with a clear message.

**Rationale**: `git rebase --abort` restores the branch to its exact pre-rebase state (HEAD, index, working tree). It is safe to call unconditionally after a failed rebase — it is a no-op if no rebase is in progress. This guarantees users never end up in a broken mid-rebase state (SC-003).

**Alternatives considered**:
- Let the user resolve conflicts in-place — rejected: the skill has no interactive conflict-resolution capability; leaving the repo in a mid-rebase state without guidance would be confusing and harmful.
- `git rebase --skip` on conflict — rejected: skipping commits silently drops the user's work.
- Stash + reset approach — rejected: more complex, and `rebase --abort` is the standard git mechanism designed exactly for this case.

---

## Decision 4: Network Failure Handling

**Decision**: If `git fetch` returns a non-zero exit code, capture the error output, display it to the user, and offer two choices: continue without syncing or abort.

**Rationale**: Network failures are transient and should not hard-block a local commit workflow. A developer who is offline or on a flaky connection should still be able to stage and commit — they can sync later. Defaulting to "continue" (with a warning) matches developer expectations for local git operations.

**Alternatives considered**:
- Hard-fail on fetch error — rejected: too disruptive for offline/airgapped scenarios.
- Silently continue — rejected: user should always be informed when the sync step was skipped; they may be relying on it for conflict-free PRs.
- Retry fetch automatically — rejected: adds latency and complexity; user is better positioned to know if the issue is transient.

---

## All NEEDS CLARIFICATION Resolved

No `[NEEDS CLARIFICATION]` markers were present in the spec. All design decisions above were derived from research into `git` internals and the existing skill's patterns.
