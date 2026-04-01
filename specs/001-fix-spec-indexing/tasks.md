---
description: "Task list for Fix Spec Indexing"
---

# Tasks: Fix Spec Indexing

**Input**: Design documents from `/specs/001-fix-spec-indexing/`  
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare script targets and validation fixtures for index resolution updates.

- [x] T001 Review current index derivation flow in `.specify/scripts/bash/create-new-feature.sh` and `.specify/scripts/bash/common.sh` to identify where duplicate-prefix creation can occur
- [x] T002 Define test fixture matrix in `specs/001-fix-spec-indexing/quickstart.md` for contiguous, non-contiguous, mixed-invalid, and empty-index scenarios

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement shared index parsing/resolution primitives used by feature creation and path-resolution scripts.

**⚠️ CRITICAL**: Must complete before user story implementation.

- [x] T003 Implement canonical valid-index parsing helper in `.specify/scripts/bash/common.sh` for `specs/` directory entries
- [x] T004 [P] Implement max-existing-plus-one index resolver in `.specify/scripts/bash/common.sh` with deterministic behavior for a fixed repo state
- [x] T005 Update `.specify/scripts/bash/create-new-feature.sh` to consume the shared resolver and assign a unique next index
- [x] T006 Update `.specify/scripts/bash/check-prerequisites.sh` and `.specify/scripts/bash/setup-plan.sh` to use the same parsing assumptions and reduce ambiguous prefix matching

**Checkpoint**: Shared index logic is centralized and feature creation no longer depends on ad hoc numbering assumptions.

---

## Phase 3: User Story 1 - Create Feature with Unique Next Index (Priority: P1) 🎯 MVP

**Goal**: Ensure every `/speckit.specify` run creates a uniquely indexed new feature folder and matching branch/spec outputs.

**Independent Test**: Run feature creation repeatedly in a repo with existing indexed features and verify each new result uses highest existing index plus one with no duplicates.

### Implementation for User Story 1

- [x] T007 [US1] Update feature-number selection path in `.specify/scripts/bash/create-new-feature.sh` to derive index from current `specs/` entries before branch/spec creation
- [x] T008 [US1] Ensure emitted `FEATURE_NUM`, `BRANCH_NAME`, and `SPEC_FILE` in `.specify/scripts/bash/create-new-feature.sh` use the same resolved index
- [x] T009 [P] [US1] Add/refresh guidance comments in `.specify/scripts/bash/create-new-feature.sh` documenting uniqueness guarantees and deterministic index behavior

**Checkpoint**: New feature creation is duplicate-safe and emits internally consistent indexed outputs.

---

## Phase 4: User Story 2 - Handle Existing Inconsistent History (Priority: P2)

**Goal**: Correctly compute the next index when prior history contains gaps or malformed non-feature directory names.

**Independent Test**: With `specs/` containing mixed valid/invalid names and index gaps, verify next index always resolves to max valid index plus one.

### Implementation for User Story 2

- [x] T010 [US2] Implement ignore rules for non-matching `specs/` entries in `.specify/scripts/bash/common.sh` so invalid names do not affect index calculation
- [x] T011 [US2] Add scenario coverage commands/examples in `specs/001-fix-spec-indexing/quickstart.md` for mixed and non-contiguous histories
- [x] T012 [P] [US2] Align prerequisite/setup expectations in `.specify/scripts/bash/check-prerequisites.sh` and `.specify/scripts/bash/setup-plan.sh` to avoid false feature-directory matches in mixed-history repos

**Checkpoint**: Index resolution remains correct with messy historical folder state.

---

## Phase 5: User Story 3 - Preserve Clear Naming and Traceability (Priority: P3)

**Goal**: Keep branch/spec naming traceable and unambiguous after index resolution changes.

**Independent Test**: For a newly created feature, verify branch name and spec path share the same unique index and are easy to map during subsequent workflow commands.

### Implementation for User Story 3

- [x] T013 [US3] Ensure branch/spec naming consistency checks are enforced in `.specify/scripts/bash/create-new-feature.sh` before final output
- [x] T014 [US3] Update feature-resolution behavior documentation in `specs/001-fix-spec-indexing/contracts/README.md` to reflect uniqueness and compatibility guarantees
- [x] T015 [P] [US3] Update plan/design notes in `specs/001-fix-spec-indexing/plan.md` and `specs/001-fix-spec-indexing/data-model.md` if implementation details require clarified resolver-state fields

**Checkpoint**: Naming traceability is explicit and consistent across generated artifacts.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification, docs synchronization, and readiness for implementation review.

- [x] T016 [P] Run quickstart validation scenarios in `specs/001-fix-spec-indexing/quickstart.md` and record outcomes in the same file
- [x] T017 [P] Review all touched scripts in `.specify/scripts/bash/` for deterministic behavior and backward-compatible output shape
- [x] T018 Mark implementation status and any refined assumptions in `specs/001-fix-spec-indexing/spec.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Phase 1 and blocks all user stories
- **User Stories (Phases 3-5)**: Depend on Phase 2 completion
- **Polish (Phase 6)**: Depends on completion of user story phases

### User Story Dependencies

- **US1 (P1)**: First deliverable and MVP; establishes duplicate-safe index creation
- **US2 (P2)**: Builds on shared resolver behavior for inconsistent history
- **US3 (P3)**: Adds traceability/documentation hardening once index behavior is stable

### Parallel Opportunities

- T004 can run in parallel with portions of T003 once helper interface is defined
- T009 can run in parallel with finalization of T007/T008
- T012 can run in parallel with T011 after T010 core logic is complete
- T015 can run in parallel with T014 after implementation behavior stabilizes
- T016 and T017 can run in parallel in Phase 6

---

## Parallel Example: User Story 2

```bash
# Parallelizable work after T010 core ignore logic is implemented:
Task T011: "Add mixed-history quickstart validation scenarios"
Task T012: "Align prerequisite/setup scripts with resolver assumptions"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2
2. Complete Phase 3 (US1)
3. Validate repeated feature creation produces unique monotonic indexes
4. Stop and review MVP impact on duplicate-prefix failures

### Incremental Delivery

1. Ship US1 for immediate duplicate-prevention value
2. Add US2 resilience for inconsistent historical repos
3. Add US3 traceability and documentation hardening
4. Final polish and validation scenarios

### Parallel Team Strategy

1. Contributor A: resolver and feature-creation script logic (T003-T009)
2. Contributor B: prerequisite/setup alignment (T006, T012)
3. Contributor C: docs/contracts/quickstart synchronization (T011, T014, T015, T016)

---

## Notes

- Tasks are implementation-ready and reference exact files.
- Tests are scenario-driven via quickstart validation because the spec does not require TDD test task generation.
- Output shape compatibility (`FEATURE_NUM`, `BRANCH_NAME`, `SPEC_FILE`) remains a cross-cutting requirement.
