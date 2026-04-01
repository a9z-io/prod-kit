# Feature Specification: Prodkit Create Diagram

**Feature Branch**: `001-create-diagram-skill`  
**Created**: 2026-04-01  
**Status**: Implemented  
**Input**: User description: "create a new command and skill called prodkit.create diagram which will create a mermaid diagram in a file. this can be used in conjunction with the output from prodkit.architecture and prodkit.dataflow and the output when used with these commands should be stored in same location."

## Product Context *(mandatory)*

- **Product Constitution**: `CLAUDE.md` in repository root
- **ICP / User**: Product engineers and AI-assisted developers using prod-kit command workflows
- **Problem / Value**: Users can generate architecture and dataflow text but still need to manually convert that output into diagrams. This feature reduces manual translation effort by producing a diagram artifact directly in the workflow.
- **Primary KPIs impacted**: Time-to-value, Engagement, Retention

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate diagram from command output (Priority: P1)

A user runs `prodkit.create diagram` with architecture or dataflow output and receives a Mermaid diagram file in the same location as the source output.

**Why this priority**: This is the core value of the feature and the minimum viable slice.

**Independent Test**: Can be fully tested by providing a representative architecture output file, running the command, and verifying that a Mermaid diagram file is created alongside the source file with diagram content.

**Acceptance Scenarios**:

1. **Given** a valid architecture output file, **When** the user runs `prodkit.create diagram` against it, **Then** a Mermaid diagram file is created in the same directory.
2. **Given** a valid dataflow output file, **When** the user runs `prodkit.create diagram` against it, **Then** a Mermaid diagram file is created in the same directory.

---

### User Story 2 - Use command consistently across sources (Priority: P2)

A user can run the same command for both architecture and dataflow outputs without learning separate workflows.

**Why this priority**: Consistency lowers cognitive load and improves adoption.

**Independent Test**: Can be tested by running the command once with architecture output and once with dataflow output and confirming both runs complete with the same command syntax and expected file placement.

**Acceptance Scenarios**:

1. **Given** either supported input type, **When** the user invokes the command, **Then** the command behavior is consistent in invocation and output placement.

---

### User Story 3 - Handle invalid or incomplete source content (Priority: P3)

A user receives clear feedback when the source content is missing, unreadable, or cannot be converted into a meaningful diagram.

**Why this priority**: Error clarity prevents user confusion and reduces support requests.

**Independent Test**: Can be tested by providing invalid or empty source inputs and confirming the command returns actionable error feedback and does not create misleading output files.

**Acceptance Scenarios**:

1. **Given** an empty or malformed source file, **When** the user runs the command, **Then** the system reports a clear error and does not produce a diagram file.

---

### Edge Cases

- Source output file exists but contains no components or relationships to diagram.
- Source output file path is valid but the user lacks write access to that location.
- A diagram file with the target name already exists in the same directory.
- Source content includes ambiguous relationships that cannot be confidently mapped into diagram links.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a command named `prodkit.create diagram`.
- **FR-002**: The system MUST provide a skill aligned to `prodkit.create diagram` that defines the diagram-generation workflow.
- **FR-003**: The command MUST accept input derived from `prodkit.architecture` output.
- **FR-004**: The command MUST accept input derived from `prodkit.dataflow` output.
- **FR-005**: For supported inputs, the system MUST generate a Mermaid diagram file containing valid Mermaid syntax.
- **FR-006**: When invoked with output from `prodkit.architecture` or `prodkit.dataflow`, the generated diagram file MUST be stored in the same directory as the source output.
- **FR-007**: The system MUST return a clear success response including the diagram file path after successful creation.
- **FR-008**: The system MUST return actionable error feedback when input is missing, unreadable, unsupported, or not convertible into a diagram.
- **FR-009**: The system MUST avoid overwriting an existing diagram file without explicit user intent or a deterministic naming rule that preserves prior output.
- **FR-010**: The command behavior MUST be documented so users understand supported inputs, output location behavior, and expected results.

### Key Entities *(include if feature involves data)*

- **Source Output Artifact**: The existing command output used as input, including artifact type (`architecture` or `dataflow`), source path, and textual content.
- **Diagram Generation Request**: The user action to create a diagram, including requested source artifact and destination context.
- **Mermaid Diagram Artifact**: The generated file that includes Mermaid content, file path, creation status, and source artifact reference.

### Assumptions

- `prodkit.architecture` and `prodkit.dataflow` outputs are durable files that can be referenced by path.
- The command executes in a context where source and destination paths are accessible to the user.
- A default naming convention for diagram files is acceptable as long as output location and overwrite behavior are predictable.
- `prodkit.dataflowdiagram` remains as a deprecated compatibility alias while canonical naming transitions to `prodkit.dataflow`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In at least 95% of valid runs, users receive a generated Mermaid diagram file in the same directory as the source artifact.
- **SC-002**: At least 90% of users can produce a first valid diagram from an existing architecture or dataflow artifact in one command attempt.
- **SC-003**: For invalid inputs, 100% of failed runs provide an actionable error message that states what must be corrected.
- **SC-004**: Compared with a manual baseline, median time to produce a shareable diagram decreases by at least 50%.

