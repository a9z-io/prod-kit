---
description: "Task list for Prodkit Create Diagram"
---

# Tasks: Prodkit Create Diagram

**Input**: Design documents from `/specs/001-create-diagram-skill/`  
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/ ✅, quickstart.md ✅

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare command/skill paths and establish canonical naming for implementation.

- [x] T001 Confirm target file set and ownership in `.claude/commands/`, `.claude/skills/`, and `src/prodkit/overlay/claude/commands/` for the new diagram workflow
- [x] T002 Create feature implementation notes in `specs/001-create-diagram-skill/quickstart.md` for canonical naming (`prodkit.dataflow`) and deprecated naming (`prodkit.dataflowdiagram`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create shared command/skill scaffolding required by all user stories.

**⚠️ CRITICAL**: Must complete before user story implementation.

- [x] T003 Create `.claude/commands/prodkit.create-diagram.md` with command contract, input expectations, output-location rule, and validation checklist
- [x] T004 [P] Create `src/prodkit/overlay/claude/commands/prodkit.create-diagram.md` mirroring `.claude/commands/prodkit.create-diagram.md`
- [x] T005 Create `.claude/skills/prodkit-create-diagram/SKILL.md` with staged workflow for source parsing, mermaid generation, path selection, and error handling
- [x] T006 Define deterministic non-overwrite naming behavior and success/error response format in `.claude/skills/prodkit-create-diagram/SKILL.md`

**Checkpoint**: Command + skill foundation exists and can be referenced by all user stories.

---

## Phase 3: User Story 1 - Generate Diagram from Command Output (Priority: P1) 🎯 MVP

**Goal**: Enable `prodkit.create diagram` to generate Mermaid files from architecture/dataflow source outputs in the same directory.

**Independent Test**: Provide one architecture output and one dataflow output, run the command, and verify Mermaid files are created in the same source directories with valid Mermaid syntax.

### Implementation for User Story 1

- [x] T007 [US1] Implement architecture-input handling rules and output colocation rules in `.claude/commands/prodkit.create-diagram.md`
- [x] T008 [US1] Implement dataflow-input handling rules and output colocation rules in `.claude/commands/prodkit.create-diagram.md`
- [x] T009 [US1] Add Mermaid artifact schema requirements (minimum node+edge validity) in `.claude/skills/prodkit-create-diagram/SKILL.md`
- [x] T010 [P] [US1] Mirror US1 command updates to `src/prodkit/overlay/claude/commands/prodkit.create-diagram.md`
- [x] T011 [US1] Add command usage examples for architecture/dataflow inputs in `.claude/commands/prodkit.create-diagram.md`

**Checkpoint**: US1 delivers end-to-end diagram generation for both supported source types.

---

## Phase 4: User Story 2 - Consistent Command Behavior Across Sources (Priority: P2)

**Goal**: Ensure the same invocation and naming conventions work consistently for architecture and dataflow workflows.

**Independent Test**: Run architecture and dataflow flows with the same command form and confirm consistent success messaging and output-path semantics.

### Implementation for User Story 2

- [x] T012 [US2] Rename canonical command references from `prodkit.dataflowdiagram` to `prodkit.dataflow` in `.claude/commands/prodkit.architecture.md`
- [x] T013 [US2] Rename canonical command references from `prodkit.dataflowdiagram` to `prodkit.dataflow` in `.claude/commands/prodkit.dataflowdiagram.md` and mark deprecated naming guidance
- [x] T014 [P] [US2] Mirror US2 rename/deprecation updates in `src/prodkit/overlay/claude/commands/prodkit.architecture.md` and `src/prodkit/overlay/claude/commands/prodkit.dataflowdiagram.md`
- [x] T015 [US2] Add canonical naming note and migration wording in `.claude/commands/README.md` and `src/prodkit/overlay/claude/commands/README.md`

**Checkpoint**: US2 ensures naming and behavior consistency across related command docs.

---

## Phase 5: User Story 3 - Clear Handling for Invalid/Incomplete Input (Priority: P3)

**Goal**: Provide actionable failures for missing, unreadable, malformed, or non-convertible source artifacts.

**Independent Test**: Run command against empty/malformed/non-readable sources and verify clear corrective error messages with no misleading output files.

### Implementation for User Story 3

- [x] T016 [US3] Add explicit error cases and user-facing remediation messages in `.claude/commands/prodkit.create-diagram.md`
- [x] T017 [US3] Add validation gates for missing payload, ambiguous relationships, and unsupported source format in `.claude/skills/prodkit-create-diagram/SKILL.md`
- [x] T018 [P] [US3] Mirror US3 command error-handling updates to `src/prodkit/overlay/claude/commands/prodkit.create-diagram.md`
- [x] T019 [US3] Add "no output on failure" rule and failure reporting contract in `.claude/skills/prodkit-create-diagram/SKILL.md`

**Checkpoint**: All user stories are independently functional and failure behavior is well-defined.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final consistency checks, status updates, and readiness for implementation execution.

- [x] T020 [P] Review all touched command files in `.claude/commands/` for terminology consistency (`prodkit.dataflow` canonical)
- [x] T021 [P] Review mirrored files in `src/prodkit/overlay/claude/commands/` for parity with `.claude/commands/`
- [x] T022 Validate `specs/001-create-diagram-skill/quickstart.md` steps against final command/skill behavior and update any drift
- [x] T023 Update `specs/001-create-diagram-skill/spec.md` status and assumptions to reflect implementation-ready decisions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Phase 1
- **User Stories (Phases 3-5)**: Depend on Phase 2 completion
- **Polish (Phase 6)**: Depends on completion of Phases 3-5

### User Story Dependencies

- **US1 (P1)**: Can start immediately after foundational phase; no dependency on other user stories
- **US2 (P2)**: Can run after foundational phase; references US1 command files for consistency
- **US3 (P3)**: Can run after foundational phase; extends validation and error behavior in same command/skill

### Parallel Opportunities

- T004 can run in parallel with T005 after T003
- T010 can run in parallel with T011 after T007-T009
- T014 can run in parallel with T015 after T012-T013
- T018 can run in parallel with T019 after T016-T017
- T020 and T021 can run in parallel in Phase 6

---

## Parallel Example: User Story 2

```bash
# Parallel rename and documentation work for US2
Task T014: "Mirror rename/deprecation updates in src/prodkit/overlay/claude/commands/*"
Task T015: "Update canonical naming note in .claude/commands/README.md and overlay README"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2
2. Complete Phase 3 (US1)
3. Validate architecture/dataflow diagram generation paths and Mermaid validity
4. Demo MVP

### Incremental Delivery

1. Ship US1 for core diagram generation
2. Add US2 for naming consistency and migration hygiene
3. Add US3 for robust error-handling behavior
4. Final polish and spec/quickstart synchronization

### Parallel Team Strategy

1. One contributor implements new command/skill core (T003-T011)
2. Another contributor handles naming migration and overlay parity (T012-T015)
3. Third contributor hardens validation/error handling (T016-T019)

---

## Notes

- All tasks follow required checklist format with IDs and file paths.
- Tests were not added as explicit tasks because the spec does not mandate TDD or a test-first workflow.
- `prodkit.dataflow` is treated as canonical; `prodkit.dataflowdiagram` remains as migration/deprecation terminology until fully retired.
