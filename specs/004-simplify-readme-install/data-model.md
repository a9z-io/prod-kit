# Data Model: Simplify README Install Instructions

**Feature**: `004-simplify-readme-install`  
**Date**: 2026-04-01

## Entity 1: Install Instruction Block

Represents a user-facing command block in README onboarding/install sections.

### Fields

- `section_name` (string): logical README section where command appears
- `command_text` (string): command shown to users
- `is_default` (boolean): whether this is the primary recommended path
- `source_repo_reference` (string): repository source used by the command
- `variant_type` (enum): `default` | `fallback`

### Validation Rules

- Exactly one default install path per install context.
- Default command must reference canonical repository source.
- Fallback blocks must be explicitly labeled as non-default.

## Entity 2: Overlay Command Recommendation

Represents recommended `prodkit overlay` invocation in README.

### Fields

- `base_command` (string): overlay invocation root
- `force_flag` (boolean): whether `--force` is included
- `include_claude_commands_flag` (boolean)
- `include_claude_skills_flag` (boolean)
- `is_default_recommendation` (boolean)

### Validation Rules

- Default recommendation must include both Claude flags.
- Default recommendation must be copy-paste executable.

## Entity 3: Install Variant

Represents optional setup paths for restricted environments.

### Fields

- `variant_name` (string): e.g., SSH, token-auth, manual copy
- `trigger_context` (string): when users should choose this variant
- `example_command` (string)
- `is_primary` (boolean): should be false for fallback variants

### Validation Rules

- Variants must not overshadow default path ordering.
- Variants must include concise context for when to use them.

## Relationships

- One README install section contains multiple `Install Instruction Block` entries.
- One `Overlay Command Recommendation` belongs to one default install instruction block.
- Multiple `Install Variant` entries may accompany a default block.

## State Transitions

### Install Guidance Flow

`drafted` -> `reviewed` -> `default-validated` -> `published`

- `drafted` when updated command text is written.
- `reviewed` when readability and consistency checks are completed.
- `default-validated` when command walkthrough confirms expected behavior.
- `published` when README updates are finalized.
