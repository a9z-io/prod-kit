# Data Model: Fix Spec Indexing

**Feature**: `001-fix-spec-indexing`  
**Date**: 2026-04-01

## Entity 1: Specs Directory Entry

Represents a candidate directory under `specs/` considered during index derivation.

### Fields

- `name` (string): directory basename
- `is_directory` (boolean): whether entry is a directory
- `matches_index_pattern` (boolean): whether name starts with a valid numeric prefix pattern
- `parsed_index` (integer, optional): extracted numeric index when pattern matches

### Validation Rules

- Entry is considered for indexing only when `is_directory=true` and `matches_index_pattern=true`.
- `parsed_index` must be a positive integer.

## Entity 2: Feature Index Resolver State

Represents the computed state used to choose the next feature index.

### Fields

- `candidate_indexes` (list of integer): parsed indexes from valid entries
- `max_existing_index` (integer, optional): highest value in `candidate_indexes`
- `source_priority` (string): index selection preference order (`specs-first`, `branches-fallback`)
- `next_index` (integer): selected new index

### Validation Rules

- If `candidate_indexes` is empty, `next_index` must be baseline first index.
- If `candidate_indexes` is non-empty, `next_index` must equal `max_existing_index + 1`.

## Entity 3: Feature Creation Output

Represents generated identifiers returned after feature creation.

### Fields

- `feature_num` (string): zero-padded index output
- `branch_name` (string): created feature branch
- `spec_file` (string): generated spec path

### Validation Rules

- `feature_num` must correspond to `next_index`.
- `branch_name` and `spec_file` must contain the same resolved index.
- Output index must not collide with any existing indexed spec directory at creation time.

## Relationships

- Many `Specs Directory Entry` records feed one `Feature Index Resolver State`.
- One `Feature Index Resolver State` produces one `Feature Creation Output`.

## State Transitions

### Index Resolution Flow

`scan_entries` -> `filter_valid_entries` -> `compute_next_index` -> `emit_creation_output`

- `scan_entries` collects raw `specs/` candidates.
- `filter_valid_entries` excludes non-matching entries.
- `compute_next_index` derives deterministic next index using specs-first, branches-fallback.
- `emit_creation_output` returns branch/spec metadata using resolved index.
