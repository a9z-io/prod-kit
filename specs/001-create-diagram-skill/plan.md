# Implementation Plan: Prodkit Create Diagram

**Branch**: `001-create-diagram-skill` | **Date**: 2026-04-01 | **Spec**: [spec.md](./spec.md)  
**Input**: Feature specification from `/specs/001-create-diagram-skill/spec.md`

## Summary

Add a new command and skill workflow for `prodkit.create diagram` that converts existing architecture and dataflow artifacts into Mermaid diagram files. The command must place output in the same directory as the source artifact when run against `prodkit.architecture` or `prodkit.dataflow` outputs. To align naming with current product intent, the legacy command name `prodkit.dataflowdiagram` is treated as deprecated and replaced by `prodkit.dataflow` in references and generated output guidance.

## Technical Context

**Language/Version**: Markdown command/skill specifications + Mermaid text output  
**Primary Dependencies**: Existing slash-command workflow in `.claude/commands/`; existing skill system in `.claude/skills/`  
**Storage**: Repository files (`.claude/commands/*`, `.claude/skills/*`) and generated diagram artifact files colocated with source outputs  
**Testing**: Manual command-run validation using representative architecture/dataflow source files and invalid-input cases  
**Target Platform**: Local development environments supported by prod-kit (macOS/Linux shell + Cursor/Claude command execution)  
**Project Type**: Single documentation-and-command project  
**Performance Goals**: Valid source inputs produce diagram artifacts in one command execution for at least 95% of runs  
**Constraints**: No overwrite without explicit handling; preserve existing command ecosystem conventions; maintain backward compatibility guidance for renamed command references  
**Scale/Scope**: New command definition, new skill, related docs updates, and diagram artifact contract documentation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Product Constitution exists**: Formal `product/constitution.*` artifact is not present in this repo; this feature is tooling-level within prod-kit. Constitution intent is still applied through explicit user/problem/value and KPI mapping in the feature spec.
- [x] **Purpose is explicit**: Spec defines users, problem, value, and measurable outcomes (`SC-001` to `SC-004`).
- [x] **Scope is bounded**: Scope is command+skill+artifact behavior; out-of-scope includes unrelated workflow overhauls.
- [x] **Traceability**: Feature ties to time-to-value and workflow clarity; impacts architecture/dataflow documentation workflows.
- [x] **Augmentation, not replacement**: Extends existing prod-kit command system; does not replace Speckit workflow phases.
- [x] **Instrumentation decision recorded**: Manual validation and measurable success criteria are specified; telemetry-level instrumentation remains deferred until implementation chooses measurement mechanics.

## Project Structure

### Documentation (this feature)

```text
specs/001-create-diagram-skill/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── README.md
└── tasks.md                # Created later by /speckit.tasks
```

### Source Code (repository root)

```text
.claude/commands/
├── prodkit.architecture.md
├── prodkit.dataflowdiagram.md      # legacy naming reference to be replaced/deprecated
├── prodkit.dataflow.md             # target canonical naming
└── prodkit.create-diagram.md       # new command

.claude/skills/
└── prodkit-create-diagram/
    └── SKILL.md                    # new skill workflow
```

**Structure Decision**: Keep all feature behavior in existing command/skill content paths to align with current prod-kit architecture.

## Phase 0: Research

Research outcomes are captured in [research.md](./research.md). All technical unknowns in this plan are resolved there, including:

1. Canonical naming strategy for replacing `prodkit.dataflowdiagram` references.
2. Deterministic output-path rules for co-locating Mermaid artifacts with source files.
3. Minimal-valid Mermaid output constraints for reliable artifact generation.
4. Non-destructive naming strategy when target diagram files already exist.

## Phase 1: Design

Design outputs are captured in:

- [data-model.md](./data-model.md)
- [contracts/README.md](./contracts/README.md)
- [quickstart.md](./quickstart.md)

### Design Notes

- Input handling is normalized around two source artifact types: architecture and dataflow.
- Output handling enforces same-directory placement for required invocation contexts.
- Naming migration treats `prodkit.dataflow` as canonical and `prodkit.dataflowdiagram` as deprecated terminology.
- Error handling is explicit for missing, unreadable, malformed, or non-convertible source content.

## Post-Design Constitution Check

- [x] Product intent remains explicit and traceable to user value.
- [x] Scope remains bounded to command/skill + artifact generation behavior.
- [x] No replacement workflow introduced; existing architecture/dataflow workflow is augmented.
- [x] Measurement approach remains defined via success criteria and manual verification.
