---
description: "Task list for Simplify README Install Instructions"
---

# Tasks: Simplify README Install Instructions

**Input**: Design documents from `/specs/004-simplify-readme-install/`  
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish update scope and target sections for README install simplification.

- [x] T001 Review install and upgrade sections in `README.md` and map current default vs fallback command blocks
- [x] T002 Capture required command/source replacements from `specs/004-simplify-readme-install/spec.md` into working notes in `specs/004-simplify-readme-install/quickstart.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create shared content rules so all user story edits stay consistent.

**⚠️ CRITICAL**: Must complete before user story implementation.

- [x] T003 Define canonical repository/source wording and command patterns in `specs/004-simplify-readme-install/contracts/README.md`
- [x] T004 [P] Define readability structure rules (default first, fallback second, concise labels) in `specs/004-simplify-readme-install/contracts/README.md`
- [x] T005 Create a section-level rewrite plan for `README.md` in `specs/004-simplify-readme-install/plan.md` with explicit default/fallback placement

**Checkpoint**: Shared documentation contracts are fixed; README edits can proceed safely.

---

## Phase 3: User Story 1 - Install from Correct Repository Quickly (Priority: P1) 🎯 MVP

**Goal**: Make default install instructions clearly point to the `a9z-io/prod-kit` source with no legacy source as primary guidance.

**Independent Test**: Follow README default install path from a clean shell and verify all default source references use `a9z-io/prod-kit`.

### Implementation for User Story 1

- [x] T006 [US1] Replace legacy default install source references in `README.md` with canonical `a9z-io/prod-kit` source guidance
- [x] T007 [US1] Update upgrade/install command examples in `README.md` to remove `3leches/prod-kit` as active default
- [x] T008 [P] [US1] Verify and align any related source references in `.claude/commands/README.md` and `src/prodkit/overlay/claude/commands/README.md`

**Checkpoint**: README default source path is current and unambiguous.

---

## Phase 4: User Story 2 - Run One Default Overlay Command for Both Add-ons (Priority: P2)

**Goal**: Ensure the default overlay command in README includes both Claude command and skill flags in one command.

**Independent Test**: Copy the default overlay command from README and confirm both `--with-claude-commands` and `--with-claude-skills` are present.

### Implementation for User Story 2

- [x] T009 [US2] Update default overlay command block in `README.md` to `prodkit overlay --force --with-claude-commands --with-claude-skills`
- [x] T010 [US2] Ensure command examples around overlay options in `README.md` preserve the combined command as the primary default path
- [x] T011 [P] [US2] Update quick validation guidance in `specs/004-simplify-readme-install/quickstart.md` to include the combined default command check

**Checkpoint**: One default command path installs both add-ons by default.

---

## Phase 5: User Story 3 - Understand Setup Steps Without Ambiguity (Priority: P3)

**Goal**: Make onboarding instructions easy to scan, with explicit default and concise fallback variants.

**Independent Test**: Read README install section once and verify default path is obvious and fallback variants are clearly labeled and brief.

### Implementation for User Story 3

- [x] T012 [US3] Restructure install/upgrade section flow in `README.md` so default path appears before optional variants
- [x] T013 [US3] Simplify wording in `README.md` to reduce cognitive load while preserving required fallback options
- [x] T014 [P] [US3] Add concise fallback labels in `README.md` for SSH/token/manual alternatives without competing with default path

**Checkpoint**: README setup flow is clear, concise, and minimally ambiguous.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Validate final documentation quality and sync spec artifacts with completed implementation.

- [x] T015 [P] Run quickstart validation scenarios in `specs/004-simplify-readme-install/quickstart.md` and record outcomes
- [x] T016 [P] Perform final readability and consistency review across modified docs in `README.md`, `.claude/commands/README.md`, and `src/prodkit/overlay/claude/commands/README.md`
- [x] T017 Update implementation status and assumption refinements in `specs/004-simplify-readme-install/spec.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Setup and blocks user story phases
- **User Stories (Phases 3-5)**: Depend on Foundational completion
- **Polish (Phase 6)**: Depends on user story completion

### User Story Dependencies

- **US1 (P1)**: Establishes canonical source correctness and should be completed first (MVP)
- **US2 (P2)**: Builds on corrected source/path wording from US1
- **US3 (P3)**: Final structure/readability polish after command content is stabilized

### Parallel Opportunities

- T004 can run in parallel with T003 after contracts section is started
- T008 can run in parallel with late US1 steps once README source defaults are finalized
- T011 can run in parallel with T010 after default overlay command is finalized
- T014 can run in parallel with T013 once section ordering is fixed
- T015 and T016 can run in parallel in Phase 6

---

## Parallel Example: User Story 2

```bash
# Parallelizable documentation validation after default command update:
Task T010: "Ensure surrounding README overlay examples preserve combined command as default"
Task T011: "Update quickstart validation checks for combined default command"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2
2. Complete US1 tasks (Phase 3)
3. Validate canonical source references are correct and legacy defaults removed
4. Stop and verify onboarding correctness

### Incremental Delivery

1. Deliver US1 for immediate correctness
2. Deliver US2 for one-command default behavior
3. Deliver US3 for readability and comprehension improvements
4. Run final polish and scenario validation

### Parallel Team Strategy

1. Contributor A: canonical source and default command edits in `README.md` (T006-T010)
2. Contributor B: fallback/readability restructuring and labels (T012-T014)
3. Contributor C: validation + cross-doc consistency + spec status updates (T008, T011, T015-T017)

---

## Notes

- Tasks intentionally focus on executable documentation updates with explicit file targets.
- No TDD test tasks were added because the spec requests documentation clarity outcomes, not code-level test suite changes.
- The combined overlay command with both Claude flags is the required default behavior across outputs.
