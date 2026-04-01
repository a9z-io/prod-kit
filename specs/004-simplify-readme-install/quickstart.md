# Quickstart: Simplify README Install Instructions

## Purpose

Validate that README install guidance is easy to follow, uses the correct repository source, and defaults to a single command that includes both Claude add-ons.

## Working Notes

- Replace all active default `3leches/prod-kit` install sources with `a9z-io/prod-kit`.
- Keep canonical prose source visible as `https://github.com/a9z-io/prod-kit`.
- Use `prodkit overlay --force --with-claude-commands --with-claude-skills` as the first/default overlay command block.
- Keep fallback variants concise and explicitly labeled (`Fallback: SSH`, `Fallback: HTTPS token auth`).

## Validation Scenarios

### Scenario 1: Default Source Correctness

1. Open `README.md` install section.
2. Identify the first/default install command block.
3. Confirm command source references `a9z-io/prod-kit`.
4. Confirm outdated `3leches/prod-kit` source is not presented as default.

### Scenario 2: Default Overlay Completeness

1. Find the default overlay command in `README.md`.
2. Verify command includes:
   - `--with-claude-commands`
   - `--with-claude-skills`
3. Confirm command is shown in one copy-paste-ready block.

### Scenario 3: Readability and Flow

1. Read the install section from top to bottom once.
2. Confirm one clear default path appears before fallback options.
3. Confirm fallback variants are labeled and concise.

### Scenario 4: Fallback Availability

1. Locate SSH/token/manual fallback examples (if present).
2. Confirm each variant states when it should be used.
3. Confirm default path remains visually primary.

## Expected Outcomes

- Users can execute default install with minimal decision-making.
- Default command path is current and complete.
- Documentation remains usable for constrained environments without confusing the primary path.

## Execution Results

- Scenario 1: PASS - default install/upgrade source references now point to `a9z-io/prod-kit`; no `3leches/prod-kit` default references remain.
- Scenario 2: PASS - default overlay command includes both `--with-claude-commands` and `--with-claude-skills`.
- Scenario 3: PASS - default command path appears before optional variants; fallback labels are concise.
- Scenario 4: PASS - fallback SSH and token-auth variants remain available and clearly secondary.
