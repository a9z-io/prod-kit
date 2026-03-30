---
description: "Task list for GH Flow Rebase on Main"
---

# Tasks: GH Flow Rebase on Main

**Input**: Design documents from `/specs/003-ghflow-rebase-main/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Locate and read the target file before making changes.

- [x] T001 Read `.claude/skills/prodkit-ghflow/SKILL.md` in full to understand current stage structure and identify the exact insertion point for Stage 0

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Resolve all design decisions and confirm the Stage 0 insertion point before writing any content.

**⚠️ CRITICAL**: Must complete before any user story implementation.

- [x] T002 Confirm the default branch detection command (`git symbolic-ref refs/remotes/origin/HEAD`) works in the local environment and note fallback behavior documented in `specs/003-ghflow-rebase-main/research.md`
- [x] T003 Confirm the divergence check command (`git rev-list --count HEAD..origin/<DEFAULT_BRANCH>`) syntax as documented in `specs/003-ghflow-rebase-main/research.md`

**Checkpoint**: Insertion point confirmed, all commands validated — user story implementation can begin.

---

## Phase 3: User Story 1 — Sync with Main Before Starting Workflow (Priority: P1) 🎯 MVP

**Goal**: Add Stage 0 to `SKILL.md` that fetches, checks divergence, prompts for rebase, and handles the rebase (success and failure).

**Independent Test**: Run `/prodkit.ghflow` on a branch that is behind `origin/main`. Verify the command pauses and asks for confirmation before rebasing. Verify that accepting performs the rebase and continues to Stage 1. Verify that declining shows a warning and continues without rebasing.

### Implementation for User Story 1

- [x] T004 [US1] Insert Stage 0 heading and step 0a (detect default branch via `git symbolic-ref`) into `.claude/skills/prodkit-ghflow/SKILL.md` immediately before Stage 1, including failure fallback (warn + skip sync)
- [x] T005 [US1] Add step 0b (fetch remote default branch with failure handling: warn + offer Continue/Abort) to Stage 0 in `.claude/skills/prodkit-ghflow/SKILL.md`
- [x] T006 [US1] Add step 0c (check if already on default branch → skip rebase silently) to Stage 0 in `.claude/skills/prodkit-ghflow/SKILL.md`
- [x] T007 [US1] Add step 0d (check divergence via `git rev-list --count HEAD..origin/<DEFAULT_BRANCH>` → if 0, skip rebase silently) to Stage 0 in `.claude/skills/prodkit-ghflow/SKILL.md`
- [x] T008 [US1] Add step 0e (user prompt: "N commit(s) behind — rebase? A/B/C") including rebase execution, success path, and conflict path (`git rebase --abort` + stop with guidance) to Stage 0 in `.claude/skills/prodkit-ghflow/SKILL.md`
- [x] T009 [US1] Update the Stage 0 entry in the Summary Output table at the bottom of `.claude/skills/prodkit-ghflow/SKILL.md` to reflect the sync step result (synced / skipped / failed)

**Checkpoint**: User Story 1 fully functional — Stage 0 sync + prompt + rebase complete.

---

## Phase 4: User Story 2 — Already Up-to-Date Silent Pass-Through (Priority: P2)

**Goal**: Verify that when a branch is already current, Stage 0 adds zero extra interaction.

**Independent Test**: Run `/prodkit.ghflow` on a branch freshly cut from `main`. Verify Stage 0 completes without any prompt and proceeds directly to Stage 1.

### Implementation for User Story 2

- [x] T010 [US2] Review step 0d in `.claude/skills/prodkit-ghflow/SKILL.md` to confirm the zero-count silent-pass condition is clearly stated and unambiguous (no prompt shown when `COMMITS_BEHIND == 0`)
- [x] T011 [US2] Review step 0c in `.claude/skills/prodkit-ghflow/SKILL.md` to confirm the "already on default branch" silent-pass condition is clearly stated

**Checkpoint**: US2 verified — no extra prompts on up-to-date branches.

---

## Phase 5: User Story 3 — Rebase Conflict Handling (Priority: P3)

**Goal**: Ensure the conflict path in step 0e clearly aborts the rebase, restores branch state, and stops with actionable guidance.

**Independent Test**: Review the conflict handling prose in `SKILL.md`. Confirm `git rebase --abort` is called before stopping, and the error message tells the developer to resolve conflicts manually then re-run.

### Implementation for User Story 3

- [x] T012 [US3] Review and harden the conflict-handling block in step 0e of `.claude/skills/prodkit-ghflow/SKILL.md` — confirm `git rebase --abort` is present, output includes conflict file names from git, and stop message is actionable
- [x] T013 [US3] Add an entry to the Error Handling table in `.claude/skills/prodkit-ghflow/SKILL.md` for the rebase-conflict scenario (trigger, action, user message)

**Checkpoint**: All three user stories complete — Stage 0 fully implemented.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Review the full Stage 0 insertion for consistency with the rest of the skill.

- [x] T014 [P] Review the complete Stage 0 section in `.claude/skills/prodkit-ghflow/SKILL.md` for consistent wording, action labels (A/B/C), and formatting matching Stages 1–5
- [x] T015 [P] Verify the existing Stage 1–5 content in `.claude/skills/prodkit-ghflow/SKILL.md` is unchanged (no accidental edits during Stage 0 insertion)
- [x] T016 Update `specs/003-ghflow-rebase-main/spec.md` status from `Draft` to `Implemented`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 completion — blocks all user stories
- **User Story Phases (3–5)**: All depend on Phase 2 completion; US1 must be complete before US2/US3 review (they review content written in US1)
- **Polish (Phase 6)**: Depends on Phases 3–5 completion

### User Story Dependencies

- **US1 (P1)**: Writes Stage 0 — core implementation; must complete first
- **US2 (P2)**: Reviews T007's zero-count condition (written in US1) — lightweight verification pass
- **US3 (P3)**: Reviews T008's conflict-handling block (written in US1) — lightweight hardening pass

### Parallel Opportunities

- T010 and T011 (US2) can run in parallel after T007 and T006 complete
- T012 and T013 (US3) can run in parallel after T008 completes
- T014 and T015 (Polish) can run in parallel after all user stories complete

---

## Parallel Example: User Story 1

```bash
# T004–T009 are sequential within US1 (each step builds on the previous).
# No parallel within US1 — all edits are to the same file, Stage 0 section.

# After US1 completes, US2 and US3 reviews can run in parallel:
Task T010: "Review step 0d — zero-count silent-pass condition"
Task T011: "Review step 0c — already-on-default-branch condition"
Task T012: "Harden conflict-handling in step 0e"
Task T013: "Add rebase-conflict row to Error Handling table"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Read SKILL.md
2. Complete Phase 2: Validate commands
3. Complete Phase 3 (T004–T009): Write Stage 0 in full
4. **STOP and VALIDATE**: Manually run `/prodkit.ghflow` on a branch behind main
5. Ship MVP — core sync + rebase prompt is the primary value

### Incremental Delivery

1. Phase 1 + 2 → Ready to edit
2. Phase 3 (US1) → Stage 0 written, core feature functional
3. Phase 4 (US2) → Confirm silent pass-through works
4. Phase 5 (US3) → Confirm conflict path is safe and actionable
5. Phase 6 → Polish and mark complete

---

## Notes

- [P] tasks = different files or independent review, no blocking dependencies
- [Story] label maps each task to its user story for traceability
- T004–T009 are sequential edits to the same file — do not parallelize within US1
- Commit after T009 (Stage 0 complete) and after T013 (all stories done) at minimum
- No new files are created — this is a single-file edit to `.claude/skills/prodkit-ghflow/SKILL.md`
