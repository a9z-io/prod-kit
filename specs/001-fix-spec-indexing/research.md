# Research: Fix Spec Indexing

**Feature**: `001-fix-spec-indexing`  
**Date**: 2026-04-01

## Decision 1: Source of truth for next index

- **Decision**: Derive the next feature index from existing indexed folder names in `specs/`, using the highest valid numeric prefix plus one.
- **Rationale**: The `specs/` directory is the most direct persisted record of created features and avoids drift from branch-only state.
- **Alternatives considered**:
  - Use only branch lists (local/remote): rejected because branches can be deleted or diverge from folder history.
  - Use only user-provided numbers: rejected because it allows accidental collisions.

## Decision 2: Valid entry matching rules

- **Decision**: Count only folder names that begin with a numeric prefix and separator in the expected feature naming pattern.
- **Rationale**: Prevents non-feature folders and malformed names from corrupting index calculations.
- **Alternatives considered**:
  - Parse any leading digit in any name: rejected as too permissive and error-prone.
  - Require strict full-name matching for a specific short-name only: rejected because index uniqueness must be global across features.

## Decision 3: Behavior when no indexed folders exist

- **Decision**: Start at the baseline first index when no valid indexed feature folders are present.
- **Rationale**: Preserves current onboarding behavior for clean repos while still enabling deterministic progression.
- **Alternatives considered**:
  - Start from arbitrary high defaults: rejected for readability and historical continuity.

## Decision 4: Non-contiguous index history

- **Decision**: Use max-existing-plus-one, not gap-filling.
- **Rationale**: Avoids accidental reuse of historical indexes and keeps monotonic ordering easy to reason about.
- **Alternatives considered**:
  - Fill the first missing gap: rejected because it can reintroduce ambiguity with old references.

## Decision 5: Compatibility with existing prerequisite/setup scripts

- **Decision**: Align feature creation so generated branch/spec indexes are unique by default, reducing prefix-collision failures in downstream scripts.
- **Rationale**: Existing scripts resolve by numeric prefix; preventing duplicate prefix creation avoids ambiguous matches and command failures.
- **Alternatives considered**:
  - Change all downstream scripts first: rejected for scope expansion and higher rollout risk.
