# Implementation Plan: Fix Spec Indexing

**Branch**: `001-fix-spec-indexing` | **Date**: 2026-04-01 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `/specs/001-fix-spec-indexing/spec.md`

## Summary

Update feature creation behavior so new spec folders always receive a unique next numeric prefix derived from the current `specs/` directory state. This prevents duplicate prefixes (such as multiple `001-*` folders) that currently break prerequisite/setup scripts and create ambiguous feature resolution.

## Technical Context

**Language/Version**: Bash shell scripts and Markdown workflow docs  
**Primary Dependencies**: Existing Speckit scripts in `.specify/scripts/bash/` (`create-new-feature.sh`, `common.sh`, prerequisite/setup scripts)  
**Storage**: Local repository file system (`specs/` directory names, generated spec files, branch names)  
**Testing**: Script-level manual validation by creating multiple features in repos with contiguous and non-contiguous prefixes  
**Target Platform**: macOS/Linux shell environments running Speckit scripts  
**Project Type**: Single repository script/workflow update  
**Performance Goals**: Next-index computation completes within one feature creation run and does not add user-visible delays  
**Constraints**: Must preserve existing branch/name conventions; must not create duplicate numeric prefixes; must remain deterministic for a given repo state  
**Scale/Scope**: Focused updates to feature creation/index resolution behavior and associated docs/tests

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Product Constitution exists**: Formal `product/constitution.*` artifacts are not present; this is an internal tooling-reliability improvement in prod-kit. Constitution intent is applied through explicit user value and measurable outcomes in the spec.
- [x] **Purpose is explicit**: Spec defines users, problem, expected value, and measurable success criteria.
- [x] **Scope is bounded**: Scope is limited to index derivation and feature creation naming consistency; no broader workflow replacement is included.
- [x] **Traceability**: Feature links directly to reliability and time-to-value outcomes by preventing duplicate-prefix failures in downstream commands.
- [x] **Augmentation, not replacement**: Change refines existing Speckit feature creation behavior within current workflow phases.
- [x] **Instrumentation decision recorded**: Validation will be done through deterministic creation scenarios; runtime instrumentation is deferred as unnecessary for this script-only change.

## Project Structure

### Documentation (this feature)

```text
specs/001-fix-spec-indexing/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── README.md
└── tasks.md
```

### Source Code (repository root)

```text
.specify/scripts/bash/
├── create-new-feature.sh
├── common.sh
├── check-prerequisites.sh
└── setup-plan.sh
```

**Structure Decision**: Keep implementation localized to existing Speckit bash scripts that perform feature resolution and creation. No new subsystem is required.

## Phase 0: Research

Research results are recorded in [research.md](./research.md), covering:

1. Canonical source of truth for next-index selection.
2. Handling invalid/non-indexed directory names.
3. Deterministic behavior under non-contiguous index histories.
4. Compatibility strategy for existing scripts that resolve feature directories by prefix.

## Phase 1: Design

Design outputs are:

- [data-model.md](./data-model.md)
- [contracts/README.md](./contracts/README.md)
- [quickstart.md](./quickstart.md)

Design approach:

- Define index resolution as a deterministic scan of `specs/` entries matching indexed naming.
- Ensure feature creation result carries one unique index across branch name and spec path.
- Prefer exact branch directory match when resolving feature paths from a shared numeric prefix.
- Preserve current user workflow while removing duplicate-prefix creation risk.

## Post-Design Constitution Check

- [x] User/problem/value and measurable outcomes remain explicit.
- [x] Scope remains constrained to indexing and naming reliability.
- [x] Existing Speckit workflow is augmented rather than replaced.
- [x] Validation approach remains clear and proportionate to script-level changes.
