# Feature Specification: Fix Spec Indexing

**Feature Branch**: `001-fix-spec-indexing`  
**Created**: 2026-04-01  
**Status**: Implemented  
**Input**: User description: "update the specify command so that when creating specs it first looks at the specs directory and finds the last index to then cretae the new index. this will allow a cleaner indexing and naming of spec folders. in the current specs folder there should not have been two 001 folders"

## Product Context *(mandatory)*

- **Product Constitution**: `CLAUDE.md` in repository root
- **ICP / User**: Maintainers and contributors using the Speckit feature workflow in this repository
- **Problem / Value**: New feature creation can produce duplicate numeric prefixes in `specs/`, which breaks downstream scripts and creates ambiguous feature resolution. This feature ensures each new spec directory gets a clean next index to keep workflow automation reliable.
- **Primary KPIs impacted**: Time-to-value, Reliability, Retention

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create Feature with Unique Next Index (Priority: P1)

A user runs `/speckit.specify` and always gets a new spec folder with the next unused numeric index based on the current `specs/` directories.

**Why this priority**: This directly addresses the core breakage and restores reliable feature initialization.

**Independent Test**: Create multiple feature specs in sequence and verify each new directory gets a strictly increasing numeric prefix with no duplicates.

**Acceptance Scenarios**:

1. **Given** existing spec folders with numeric prefixes, **When** a user runs `/speckit.specify`, **Then** the created spec folder uses the next highest prefix plus one.
2. **Given** a prefix already used by another feature, **When** a user runs `/speckit.specify`, **Then** the new feature does not reuse that prefix.

---

### User Story 2 - Handle Existing Inconsistent History (Priority: P2)

A user can still create a new feature index correctly even if prior spec folder naming history is uneven or contains legacy gaps.

**Why this priority**: Real repositories often contain historical inconsistencies; new behavior must remain deterministic.

**Independent Test**: With a `specs/` directory containing mixed prefixes and gaps, run `/speckit.specify` and verify the next index is calculated from the highest existing numeric prefix.

**Acceptance Scenarios**:

1. **Given** non-contiguous prior indexes, **When** a new spec is created, **Then** the new index is one greater than the maximum existing index.

---

### User Story 3 - Preserve Clear Naming and Traceability (Priority: P3)

A user gets consistently indexed spec folders that are easier to navigate and map to branches and workflow outputs.

**Why this priority**: Predictable indexing improves maintainability and reduces operator confusion.

**Independent Test**: Create a new feature and verify folder index, branch index, and generated references remain aligned and unambiguous.

**Acceptance Scenarios**:

1. **Given** a newly created feature, **When** users inspect generated branch and spec paths, **Then** the index is consistent and unique across created artifacts.

---

### Edge Cases

- The `specs/` directory contains non-feature folders that should be ignored by index calculation.
- Legacy folder names exist that do not match numeric-prefix naming conventions.
- The repository has no existing feature folders; first generated index should be the initial baseline.
- Multiple contributors create features around the same time and one creation occurs after another has already added a higher index.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST inspect existing feature folders under `specs/` before creating a new feature index.
- **FR-002**: The system MUST identify the highest existing numeric feature prefix among valid feature folder names.
- **FR-003**: The system MUST assign the next feature index as highest existing prefix plus one.
- **FR-004**: The system MUST avoid creating a feature folder whose numeric prefix is already present in `specs/`.
- **FR-005**: The system MUST ignore `specs/` entries that do not match the expected indexed feature naming pattern.
- **FR-006**: The system MUST produce branch and spec path outputs that use the same unique assigned index.
- **FR-007**: If no valid indexed feature folders exist, the system MUST create the first indexed feature using the baseline starting index.
- **FR-008**: The system MUST provide deterministic behavior so repeated runs on the same repository state produce the same computed next index.

### Key Entities *(include if feature involves data)*

- **Feature Index**: Numeric identifier prefix used in branch names and spec folder names.
- **Feature Directory Entry**: Existing `specs/` folder candidate evaluated during next-index calculation.
- **Feature Creation Result**: Output containing branch name, feature number, and spec file path.

### Assumptions

- Indexed feature folder names follow a numeric-prefix convention where a number appears at the start of the folder name.
- The workflow should derive new index values from current repository contents at creation time.
- Existing historical duplicates are not auto-migrated by this feature; this feature prevents new duplicates.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of newly created feature specs use a numeric prefix not currently used by any existing `specs/` feature folder.
- **SC-002**: In repositories with existing indexed features, the next created feature index matches maximum existing index plus one in at least 99% of creation attempts.
- **SC-003**: Incidents where prerequisite scripts fail due to duplicate active numeric prefixes are reduced to zero for features created after this change.
- **SC-004**: Maintainers can create three consecutive new feature specs without manual renaming or index correction.
