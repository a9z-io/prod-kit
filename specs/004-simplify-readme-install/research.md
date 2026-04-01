# Research: Simplify README Install Instructions

**Feature**: `004-simplify-readme-install`  
**Date**: 2026-04-01

## Decision 1: Canonical source repository in install commands

- **Decision**: Use `a9z-io/prod-kit` as the only default repository source in README install examples.
- **Rationale**: Reduces setup failures and confusion caused by obsolete `3leches` source references.
- **Alternatives considered**:
  - Keep both repos presented equally: rejected because it adds ambiguity for new users.
  - Keep old source in default and add note: rejected because default path should be correct and current.

## Decision 2: Default overlay command shape

- **Decision**: Document `prodkit overlay --force --with-claude-commands --with-claude-skills` as the primary default command.
- **Rationale**: Installs both common add-ons in one step and avoids partial setup.
- **Alternatives considered**:
  - Separate default commands for commands and skills: rejected due to increased cognitive load.
  - Keep base `prodkit overlay --force` as default: rejected because it does not satisfy the requested default behavior.

## Decision 3: Documentation readability structure

- **Decision**: Present one clear “default path” first, then concise fallback variants (SSH/token/manual copy) afterwards.
- **Rationale**: Most users need a copy-paste default; advanced variants should remain available but secondary.
- **Alternatives considered**:
  - Flatten all options into one long list: rejected as hard to scan.
  - Remove fallback variants entirely: rejected because constrained environments still need them.

## Decision 4: Legacy mention handling

- **Decision**: Remove legacy source from default command blocks and retain it only if needed as explicit historical context (not as active guidance).
- **Rationale**: Prevents accidental use of outdated commands while preserving maintainability context if needed.
- **Alternatives considered**:
  - Leave legacy commands unchanged: rejected because it conflicts with feature intent and user outcomes.

## Decision 5: Validation approach

- **Decision**: Validate via command-copy walkthrough from README sections and consistency checks across related docs.
- **Rationale**: This is a documentation behavior change; practical walkthrough validation is sufficient and fast.
- **Alternatives considered**:
  - Build tooling-level tests for README commands: rejected as out-of-scope for this docs-focused feature.
