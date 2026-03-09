# Contracts: AI-Native Product Development Framework

**Feature**: `002-ai-native-framework`
**Date**: 2026-02-08

This feature introduces no APIs, network protocols, or inter-service contracts. The "contracts" are the **file schemas** — structural agreements between the framework (commands that write files) and consumers (AI agents that read them).

## File Schema Contracts

These schemas are normative. Any command that writes a knowledge-base file MUST produce output conforming to these contracts. Any agent reading a knowledge-base file MAY assume conformance.

### Contract 1: Knowledge-Base File Schema

See [`data-model.md`](../data-model.md) — Entity 1 (Knowledge-Base File). Key invariants:

- YAML frontmatter MUST appear before any content
- `## Agent Summary` MUST be the first section after frontmatter, MUST be ≤150 words
- All top-level sections use `##`; all subsections use `###`; no deeper nesting

### Contract 2: Task Routing Table Schema

See [`data-model.md`](../data-model.md) — Entity 3 (Task Routing Table). Key invariants:

- `agents.md` MUST appear in every task category row
- Task category names MUST match the `required-by-tasks` values in file frontmatter exactly (case-sensitive)

### Contract 3: Vendor-Native Auto-Loader Content Contract

See [`data-model.md`](../data-model.md) — Entity 2 (Agent Config File). Key invariants:

- Every vendor file MUST reference `agents.md` as an always-load file
- Every vendor file MUST include the staleness check instruction
- Every vendor file MUST use only that vendor's supported path-reference syntax

### Contract 4: Dataflow Artifact Schema

See [`data-model.md`](../data-model.md) — Entity 4 (Dataflow Artifact). Key invariants:

- MUST include a `## Services` section and a `## Data Flows` table
- Flow table MUST have columns: From, To, Data, Direction, Notes
- Direction MUST use `→` (unidirectional) or `↔` (bidirectional)
