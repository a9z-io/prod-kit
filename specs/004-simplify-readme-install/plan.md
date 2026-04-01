# Implementation Plan: Simplify README Install Instructions

**Branch**: `004-simplify-readme-install` | **Date**: 2026-04-01 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `/specs/004-simplify-readme-install/spec.md`

## Summary

Revise README onboarding/install guidance to use the canonical `a9z-io/prod-kit` source, simplify wording for fast comprehension, and make the combined overlay command (`prodkit overlay --force --with-claude-commands --with-claude-skills`) the default recommendation. Keep concise fallback options for SSH/auth-constrained environments without overshadowing the default path.

## Technical Context

**Language/Version**: Markdown documentation updates  
**Primary Dependencies**: README content and existing command usage conventions in repo  
**Storage**: Repository documentation files (`README.md` and related command references)  
**Testing**: Manual doc validation by following commands from a clean shell context and verifying command coherence  
**Target Platform**: Users running shell commands for `uvx`/`uv tool` install and `prodkit overlay`  
**Project Type**: Single repository documentation refinement  
**Performance Goals**: Users identify and execute the default setup path in a single read-through  
**Constraints**: Preserve useful fallback guidance; avoid contradictory command examples; prioritize copy-paste usability  
**Scale/Scope**: README-focused updates with potential small supporting doc alignment

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Product Constitution exists**: Formal product constitution artifacts are not explicitly present in this repo, but the plan maintains explicit user/problem/value framing and measurable outcomes for this documentation feature.
- [x] **Purpose is explicit**: Spec defines target users, pain point (legacy/confusing instructions), and measurable success criteria.
- [x] **Scope is bounded**: Scope is constrained to README instruction simplification and default command standardization.
- [x] **Traceability**: Expected outcomes map to onboarding activation and faster time-to-value.
- [x] **Augmentation, not replacement**: Existing workflow remains; only documentation defaults and clarity are improved.
- [x] **Instrumentation decision recorded**: Success measured through doc validation scenarios and support-friction reduction; no runtime instrumentation required for this docs-only change.

## Project Structure

### Documentation (this feature)

```text
specs/004-simplify-readme-install/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── README.md
└── tasks.md
```

### Source Code (repository root)

```text
README.md
.claude/commands/
└── README.md                 # if wording alignment is needed
src/prodkit/overlay/claude/commands/
└── README.md                 # if wording alignment is needed
```

**Structure Decision**: Implement as documentation-first updates centered on `README.md`, with minimal companion doc alignment only where needed for consistency.

## Phase 0: Research

Research findings are captured in [research.md](./research.md), including:

1. Canonical repository source and URL format for default install examples.
2. Best-practice ordering of default vs fallback install instructions for readability.
3. Recommended default overlay command shape that includes both Claude commands and skills.
4. Guidance for retaining fallback install paths without confusing default onboarding flow.

## Phase 1: Design

Design artifacts:

- [data-model.md](./data-model.md)
- [contracts/README.md](./contracts/README.md)
- [quickstart.md](./quickstart.md)

Design approach:

- Treat README instruction blocks as a contract between maintainers and users.
- Define one clearly labeled default path and concise fallback variants.
- Ensure all default command examples are immediately executable and consistent.

## README Rewrite Plan

1. Keep install/upgrade flow scoped to `README.md` upgrade sections and avoid introducing new onboarding branches.
2. Place canonical source line (`https://github.com/a9z-io/prod-kit`) directly above the default overlay command block.
3. Present the combined default overlay command first:
   - `prodkit overlay --force --with-claude-commands --with-claude-skills`
4. Keep alternative variants concise and explicitly labeled as fallback:
   - `Fallback: SSH source`
   - `Fallback: HTTPS token auth`
5. Keep single-purpose optional command blocks (`commands only`, `skills only`) below the default command block.

## Post-Design Constitution Check

- [x] User value remains explicit and measurable.
- [x] Scope remains limited to onboarding/install documentation clarity.
- [x] Existing workflow is preserved and clarified, not replaced.
- [x] Validation remains practical and proportionate to documentation changes.
