# Feature Specification: GH Flow Rebase on Main

**Feature Branch**: `003-ghflow-rebase-main`
**Created**: 2026-03-30
**Status**: Implemented
**Input**: User description: "Modify the prodkit-ghflow command so that it does a fetch and pull from git main and rebase to make sure changes are done on top of git main. This could be a manually ask before proceeding type of task."

## Product Context *(mandatory)*

- **Product Constitution**: `product/constitution.md`
- **ICP / User**: Developer using `prodkit-ghflow` to manage their git workflow within prod-kit projects
- **Problem / Value**: When running the ghflow command, changes may be based on a stale version of the main branch, causing merge conflicts or divergence when the PR is created. This feature ensures the developer's work is always rebased on top of the latest main, reducing integration friction and PR review overhead.
- **Primary KPIs impacted**: Time-to-value (faster, conflict-free PR creation); Developer Experience (fewer surprises at PR time)

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Sync with Main Before Starting Workflow (Priority: P1)

A developer runs `/prodkit.ghflow` and the command first fetches the latest state of the main branch, then asks the developer if they want to rebase their current branch on top of main before proceeding with the branch/commit/PR workflow.

**Why this priority**: This is the core feature request. Without syncing to main, branches may diverge and PRs will have unnecessary merge conflicts. This is the foundational safety net before any destructive git operations.

**Independent Test**: Can be fully tested by running `/prodkit.ghflow` on a branch that is behind main and verifying that the command pauses to ask the user before performing the rebase.

**Acceptance Scenarios**:

1. **Given** the developer's current branch is behind origin/main, **When** the developer runs `/prodkit.ghflow`, **Then** the command fetches the latest main, informs the developer of the divergence, and asks for confirmation before rebasing.
2. **Given** the developer confirms the rebase, **When** the rebase is performed, **Then** the branch is updated to include all commits from main before continuing with the commit/PR workflow.
3. **Given** the developer declines the rebase, **When** they choose to skip, **Then** the workflow continues without rebasing and the user is informed their branch may be behind main.

---

### User Story 2 - Already Up-to-Date (Priority: P2)

A developer runs `/prodkit.ghflow` and their branch is already up-to-date with main. The command should detect this and skip the rebase step without unnecessary prompts.

**Why this priority**: Reduces friction for the common case where a branch is already current. Unnecessary prompts degrade developer experience.

**Independent Test**: Can be tested by running `/prodkit.ghflow` on a branch freshly cut from main — should skip the rebase prompt and proceed directly to commit/PR workflow.

**Acceptance Scenarios**:

1. **Given** the developer's branch is already up-to-date with origin/main, **When** the developer runs `/prodkit.ghflow`, **Then** the command detects no divergence and proceeds to the commit/PR workflow without asking about rebase.

---

### User Story 3 - Rebase Conflict Handling (Priority: P3)

A developer runs `/prodkit.ghflow`, confirms the rebase, but the rebase encounters conflicts that cannot be auto-resolved. The command should stop, inform the developer of the conflict, and guide them to resolve it manually before retrying.

**Why this priority**: Edge case but critical for safety — silently failing a rebase or proceeding with a broken state would be worse than stopping and asking the user to intervene.

**Independent Test**: Can be tested by creating deliberate conflicting changes between the feature branch and main and running the command.

**Acceptance Scenarios**:

1. **Given** a rebase conflict exists, **When** the rebase is attempted and fails, **Then** the command halts, clearly reports the conflict, aborts the rebase to restore the original branch state, and instructs the developer to resolve conflicts manually before re-running.

---

### Edge Cases

- What happens when there is no `origin` remote configured? The command should detect this and skip the fetch/rebase step with a clear warning.
- What happens when the main branch name differs (e.g., `master` vs `main`)? The command should use the configured default branch name for the repository.
- What happens when the developer is already on the main branch when running the command? The command should skip the rebase step as there is nothing to rebase.
- How does the system handle a network failure during `git fetch`? It should report the failure and ask the developer whether to continue without syncing or abort.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The command MUST fetch the latest state of the remote main branch before proceeding with any git operations.
- **FR-002**: The command MUST compare the current branch against the latest main to determine if a rebase is needed.
- **FR-003**: If the current branch is behind main, the command MUST pause and ask the developer for explicit confirmation before performing the rebase.
- **FR-004**: If the developer confirms, the command MUST rebase the current branch on top of main before continuing with the commit/PR workflow.
- **FR-005**: If the developer declines the rebase, the command MUST continue the workflow without rebasing and display a warning that the branch may be behind main.
- **FR-006**: If the current branch is already up-to-date with main, the command MUST skip the rebase prompt and proceed directly.
- **FR-007**: If the rebase encounters conflicts, the command MUST abort the rebase, restore the branch to its pre-rebase state, and clearly instruct the developer to resolve conflicts manually.
- **FR-008**: The command MUST use the repository's configured default branch (not hardcode `main`) when determining the sync target.
- **FR-009**: If the fetch fails due to a network or remote issue, the command MUST inform the developer and ask whether to continue without syncing or abort the workflow.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developers running `/prodkit.ghflow` on a branch behind main are prompted before any rebase occurs — 100% of the time, no silent rebases.
- **SC-002**: When the branch is already current, the workflow completes without any additional prompts from the sync step — adding zero extra interaction steps.
- **SC-003**: When a rebase conflict occurs, the branch is always restored to its pre-rebase state — developers never end up in a broken rebase state after running the command.
- **SC-004**: The full ghflow workflow (fetch + rebase prompt + existing commit/PR steps) completes end-to-end in under 60 seconds for a typical branch with no conflicts.

## Assumptions

- The repository uses a standard remote named `origin`.
- The default branch name is discoverable from the repository's git configuration (e.g., `git symbolic-ref refs/remotes/origin/HEAD`).
- The developer has network access to the remote repository; a fetch failure is treated as a recoverable warning, not a hard stop.
- The existing `prodkit-ghflow` commit/PR confirmation steps remain unchanged — this feature only adds a sync step at the beginning.
- "Manually ask before proceeding" applies to the rebase operation specifically, as it modifies commit history and is not easily undone without knowledge of the original branch state.
