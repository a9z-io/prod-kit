# Data Model: Prodkit Create Diagram

**Feature**: `001-create-diagram-skill`  
**Date**: 2026-04-01

## Entity 1: Source Output Artifact

Represents an existing file used as input for diagram generation.

### Fields

- `artifact_type` (enum): `architecture` | `dataflow`
- `source_path` (string): absolute or repo-relative source file path
- `source_directory` (string): directory containing the source file
- `content` (string): textual source content
- `is_readable` (boolean): whether command runtime can read the file

### Validation Rules

- `artifact_type` must be one of the two supported values.
- `source_path` must exist and point to a readable file.
- `content` must be non-empty.

## Entity 2: Diagram Generation Request

Represents a user invocation of `prodkit.create diagram`.

### Fields

- `command_name` (string): expected canonical command identifier
- `source_artifact` (reference): `Source Output Artifact`
- `requested_output_name` (string, optional): preferred base output filename
- `allow_overwrite` (boolean, default false)
- `timestamp` (datetime): invocation time

### Validation Rules

- `command_name` must match canonical command naming.
- `source_artifact` must pass validation before generation starts.
- `allow_overwrite=false` requires non-destructive output naming.

## Entity 3: Mermaid Diagram Artifact

Represents the generated Mermaid output file.

### Fields

- `diagram_path` (string): final output file path
- `diagram_directory` (string): output directory, expected to match `source_directory`
- `diagram_content` (string): Mermaid text
- `source_reference` (reference): source artifact path and type
- `generation_status` (enum): `created` | `failed`
- `error_message` (string, optional): non-empty when `generation_status=failed`

### Validation Rules

- `diagram_directory` must equal source directory for architecture/dataflow input cases.
- `diagram_content` must include valid Mermaid block syntax with at least one node and edge for successful generation.
- `generation_status=failed` requires `error_message`.

## Relationships

- One `Diagram Generation Request` references one `Source Output Artifact`.
- One successful `Diagram Generation Request` produces one `Mermaid Diagram Artifact`.
- One `Source Output Artifact` can produce many `Mermaid Diagram Artifact` files over time.

## State Transitions

### Diagram Generation Request

`received` -> `validated` -> (`generated` | `failed`)

- `received` -> `validated` when source file checks pass.
- `validated` -> `generated` when Mermaid artifact is written successfully.
- `received` or `validated` -> `failed` on validation, parsing, or write errors.

### Mermaid Diagram Artifact

`pending` -> (`created` | `failed`)

- `pending` -> `created` when output file is written and content passes minimum validity checks.
- `pending` -> `failed` when conversion or write fails.
