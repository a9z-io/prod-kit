# Implementation Plan: GH Flow Rebase on Main

**Branch**: `003-ghflow-rebase-main` | **Date**: 2026-03-30 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/003-ghflow-rebase-main/spec.md`

## Summary

Extend the `prodkit-ghflow` skill (`.claude/skills/prodkit-ghflow/SKILL.md`) with a new **Stage 0 — Sync with Main** that runs before the existing branch/commit/PR workflow. The stage fetches the remote default branch, checks whether the current branch is behind it, and prompts the user for confirmation before rebasing. The existing Stages 1–5 are preserved unchanged.

## Technical Context

**Language/Version**: Markdown + YAML frontmatter (same as all prod-kit artifacts)
**Primary Dependencies**: `git` (fetch, rebase, symbolic-ref, rev-list) — already required by the skill
**Storage**: N/A — file-level edit to `SKILL.md`
**Testing**: Manual walkthrough against a test repo; scenarios listed in spec
**Target Platform**: Any shell environment where `git` is installed (macOS, Linux, WSL)
**Project Type**: Single — plain-text skill file consumed by Claude Code
**Performance Goals**: No measurable latency requirement; `git fetch` network call is the only addition
**Constraints**: Must not alter or break existing Stages 1–5; no new tool dependencies
**Scale/Scope**: Single file modification (~80–120 lines added to one SKILL.md)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Product Constitution exists**: No formal `product/constitution.md` exists yet, but this feature is an internal tooling improvement to prod-kit itself — the constitution's traceability gate is acknowledged and deferred (consistent with the constitution's allowed omission pattern for early-stage or tooling-only changes).
- [x] **Purpose is explicit**: Spec answers who (developer using ghflow), what (sync to main before branching/committing), why (prevent diverged PRs and merge conflicts), and what success looks like (SC-001 through SC-004).
- [x] **Scope is bounded**: Scope is explicitly one file edit; out-of-scope is explicitly any change to Stages 1–5 behavior.
- [x] **Traceability**: Improvement to `prodkit-ghflow` → Developer Experience KPI (Time-to-value, fewer merge conflicts). Formal KPI files not yet present; deferred.
- [x] **Augmentation, not replacement**: Stage 0 layers onto the existing workflow without changing or reinterpreting any existing stage.
- [x] **Instrumentation decision recorded**: No runtime instrumentation applicable (plain Markdown skill). Deferred.

## Project Structure

### Documentation (this feature)

```text
specs/003-ghflow-rebase-main/
├── plan.md              # This file
├── research.md          # Phase 0 output
└── tasks.md             # Phase 2 output (/speckit.tasks — NOT created here)
```

### Source Code (repository root)

```text
.claude/skills/prodkit-ghflow/
└── SKILL.md             # Single file modified — Stage 0 inserted before Stage 1
```

No new files. No new directories. No changes outside `SKILL.md`.

---

## Phase 0: Research

### Unknowns & Research Tasks

| Unknown | Research Question | Resolution |
|---------|------------------|------------|
| Default branch detection | What is the most reliable cross-platform `git` command to detect the remote default branch name? | See research.md |
| Divergence check | What is the most accurate way to determine if the current branch is behind the default branch without requiring a checkout? | See research.md |
| Rebase abort safety | How does `git rebase --abort` restore state if conflicts arise mid-rebase? | See research.md |
| Network failure handling | How does `git fetch` signal failure and what exit codes should be handled? | See research.md |

---

## Phase 1: Design

### Stage 0 Insertion Point

Stage 0 is inserted at the **top of the skill**, before Stage 1 (Inspect Repo State). The existing stage numbers remain unchanged.

### Stage 0 Flow

```
Stage 0 — Sync with Main
│
├─ Step 0a: Detect default branch
│   git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null
│   → strips "refs/remotes/origin/" prefix → DEFAULT_BRANCH (e.g. "main")
│   → If command fails: warn "Cannot detect default branch" → skip sync, continue
│
├─ Step 0b: Fetch remote
│   git fetch origin <DEFAULT_BRANCH>
│   → On failure: warn user → offer [Continue without sync | Abort]
│   → If Abort: stop
│
├─ Step 0c: Check if on default branch
│   git rev-parse --abbrev-ref HEAD → CURRENT_BRANCH
│   → If CURRENT_BRANCH == DEFAULT_BRANCH: skip rebase (no prompt), continue
│
├─ Step 0d: Check divergence
│   git rev-list --count HEAD..origin/<DEFAULT_BRANCH>
│   → COMMITS_BEHIND = integer result
│   → If COMMITS_BEHIND == 0: skip rebase (no prompt), continue
│
└─ Step 0e: Prompt and rebase
    Present:
      "Your branch is N commit(s) behind <DEFAULT_BRANCH>.
       Rebase on top of origin/<DEFAULT_BRANCH> before continuing?
         A) Yes — rebase now
         B) No  — continue without rebasing (branch may be behind main)
         C) Cancel"

    → If A: git rebase origin/<DEFAULT_BRANCH>
             On success: report "Rebased onto origin/<DEFAULT_BRANCH>", continue
             On failure: git rebase --abort
                         report conflict details
                         stop with: "Rebase failed. Resolve conflicts manually, then re-run."
    → If B: warn "Continuing with branch behind <DEFAULT_BRANCH>."
             continue to Stage 1
    → If C: stop
```

### Key Design Decisions

1. **Default branch detection via `symbolic-ref`**: More reliable than hardcoding `main`; works across GitHub, GitLab, Bitbucket conventions. If it fails (e.g., no remote HEAD pointer), silently skip sync rather than blocking the workflow.

2. **`git rev-list --count HEAD..origin/DEFAULT`**: Accurate divergence check after fetch. Returns `0` when up-to-date, eliminating unnecessary prompts (User Story 2).

3. **`git rebase --abort` on failure**: Guarantees branch is restored to pre-rebase state. No partial-rebase state left behind (User Story 3 / SC-003).

4. **Skip prompt when already on default branch**: If the user is on `main` itself, rebasing is nonsensical. Silent pass-through.

5. **Prompt is manually-confirmed**: Rebase modifies commit history and is not automatically reversible by a non-git-expert. Matches the spec's intent: "manually ask before proceeding."

6. **Fetch failure is non-fatal by default**: Network issues should not block local commit workflows. User gets to choose to continue or abort.

### No Data Model Required

This feature has no persistent data entities. The only artifact modified is the skill's Markdown text.

### No Interface Contracts Required

This is a purely internal skill file. No external APIs, CLI flags, or user-facing schemas are introduced.
