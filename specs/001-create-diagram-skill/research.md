# Research: Prodkit Create Diagram

**Feature**: `001-create-diagram-skill`  
**Date**: 2026-04-01

## Decision 1: Canonical command naming for dataflow workflow

- **Decision**: Use `prodkit.dataflow` as canonical command naming and treat `prodkit.dataflowdiagram` as deprecated terminology.
- **Rationale**: The shorter canonical name aligns with existing command naming conventions and avoids embedding output format details in command identity.
- **Alternatives considered**:
  - Keep `prodkit.dataflowdiagram` as canonical: rejected due to verbosity and naming inconsistency.
  - Support both indefinitely as equal names: rejected because it preserves ambiguity in docs and automation.

## Decision 2: Output location rule for generated diagrams

- **Decision**: For source artifacts produced by `prodkit.architecture` and `prodkit.dataflow`, always write Mermaid output to the same directory as the source file.
- **Rationale**: Co-location keeps related architecture artifacts together and satisfies the feature's primary user requirement.
- **Alternatives considered**:
  - Always write to a central diagrams directory: rejected because it separates output from context.
  - Write to current working directory: rejected because result location becomes non-deterministic.

## Decision 3: Mermaid validity baseline

- **Decision**: Require every generated artifact to include a valid Mermaid diagram block with at least one node and one relationship edge.
- **Rationale**: This provides a minimal quality baseline that prevents empty or structurally invalid outputs.
- **Alternatives considered**:
  - Allow empty placeholder diagrams: rejected because it can appear successful while delivering no practical value.
  - Require full semantic correctness validation: rejected for initial scope; too strict without concrete parser guarantees.

## Decision 4: Existing-file collision handling

- **Decision**: Use deterministic non-overwrite naming when the default output filename already exists (for example, suffixing `-1`, `-2`, etc.).
- **Rationale**: Prevents accidental data loss while preserving automation-friendly behavior.
- **Alternatives considered**:
  - Prompt user every time: rejected because it interrupts batch workflows.
  - Overwrite by default: rejected due to high risk of artifact loss.

## Decision 5: Contract style for this feature

- **Decision**: Treat file schemas and command interaction rules as the formal contracts (instead of HTTP API contracts).
- **Rationale**: This feature is command/skill and file-artifact based, with no service API surface.
- **Alternatives considered**:
  - Define synthetic REST endpoints: rejected because it adds artificial abstraction not present in actual feature behavior.
