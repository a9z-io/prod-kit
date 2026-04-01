# Quickstart: Fix Spec Indexing

## Purpose

Ensure new feature creation assigns a unique, monotonic index from current `specs/` directory state to avoid duplicate-prefix collisions.

## Prerequisites

- Repository has Speckit scripts available under `.specify/scripts/bash/`.
- `specs/` directory exists (it may contain contiguous or non-contiguous indexed feature folders).

## Validation Scenarios

### Scenario 1: Contiguous Indexes

1. Ensure `specs/` has entries like `001-*`, `002-*`, `003-*`.
2. Run feature creation once.
3. Verify new feature index is `004`.

### Scenario 2: Non-Contiguous Indexes

1. Ensure `specs/` has entries like `001-*`, `003-*`, `007-*`.
2. Run feature creation once.
3. Verify new feature index is `008` (max-plus-one behavior).

### Scenario 3: Mixed Valid and Invalid Entries

1. Add non-matching folders under `specs/` (for example, `archive`, `tmp`, `notes`).
2. Run feature creation once.
3. Verify invalid names are ignored and next index is still derived from valid indexed entries only.

### Scenario 4: Empty Index Set

1. Use a clean repo state with no valid indexed feature folders.
2. Run feature creation once.
3. Verify baseline first index is used.

## Expected Outcomes

- No newly created feature duplicates an existing numeric prefix.
- Branch and spec outputs contain the same assigned index.
- Downstream prerequisite/setup commands no longer fail due to newly introduced duplicate prefixes.

## Execution Results (2026-04-01)

- Ran: `.specify/scripts/bash/check-prerequisites.sh --json --paths-only`
  - Result: Feature path resolution succeeds on `001-fix-spec-indexing` even with multiple `001-*` folders because exact branch directory match is preferred.
- Ran: `.specify/scripts/bash/create-new-feature.sh --json --number 1 --short-name "collision-test" "temporary collision check"`
  - Result: Command fails fast with `Error: Feature number '001' already exists in specs/. Use a different --number or omit --number.`
- Verified behavior: numeric prefix reuse is blocked, and normal flows can rely on script-managed sequential index assignment.
