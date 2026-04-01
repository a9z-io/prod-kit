# Quickstart: Prodkit Create Diagram

## Purpose

Generate Mermaid diagram artifacts from existing architecture or dataflow outputs and store diagrams beside their source files.

## Prerequisites

- You are in a repo with prod-kit commands available.
- You have an existing architecture or dataflow artifact file.
- The source file location is writable.

## Typical Flow

1. Ensure source artifacts exist (for example, output from `prodkit.architecture` or `prodkit.dataflow`).
2. Run `prodkit.create diagram` using the source artifact context/path.
3. Verify the command returns the generated diagram file path.
4. Open the generated file and confirm Mermaid syntax and expected relationships.

## Validation Checklist

- Diagram file is created in the same directory as the source artifact.
- Diagram includes at least one node and one edge.
- Re-running with existing output does not silently overwrite previous artifacts.
- Invalid or malformed input returns clear actionable error output.

## Naming Migration Note

- Use `prodkit.dataflow` as the canonical command name in docs and examples.
- Treat `prodkit.dataflowdiagram` as deprecated terminology during migration.

## Implementation Notes

- `prodkit.create diagram` is the diagram generation entry point for architecture and dataflow artifacts.
- Generated Mermaid files are written to the same directory as the source artifact.
- Existing target filenames are preserved via deterministic suffixing (`-1`, `-2`, ...), not silent overwrite.
- Validation failures must return actionable errors and must not claim output creation.

## Next Step

Run `/speckit.tasks` to generate an implementation task breakdown from this plan.
