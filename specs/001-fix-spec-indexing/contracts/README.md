# Contracts: Fix Spec Indexing

**Feature**: `001-fix-spec-indexing`  
**Date**: 2026-04-01

This feature has no network API surface. Contracts are workflow and file-system behavior contracts.

## Contract 1: Index Resolution Contract

- The feature creation workflow must inspect `specs/` and consider only valid indexed feature directory names.
- The resolved next index must be deterministic for a given repository state.
- The resolved index must be one greater than the maximum existing valid index.

## Contract 2: Uniqueness Contract

- A newly created feature must not reuse an index already present in an existing indexed spec directory.
- Branch name and spec path outputs must include the same newly assigned index.

## Contract 3: Invalid Entry Handling Contract

- Non-feature or malformed directory names in `specs/` must not affect next-index calculation.
- Empty candidate sets must map to baseline first index behavior.

## Contract 4: Compatibility Contract

- Indexing behavior must preserve existing feature naming conventions and expected output shape (`BRANCH_NAME`, `SPEC_FILE`, `FEATURE_NUM`).
- Changes must reduce downstream prefix-collision failures without requiring immediate rewrites of all dependent scripts.
