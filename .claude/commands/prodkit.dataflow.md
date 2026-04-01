# /prodkit.dataflow

## User Input

```text
$ARGUMENTS
```

The user must provide a description of the services and data flows to diagram. If `$ARGUMENTS` is empty, ask: "Please describe the services involved and the data flowing between them. Include service names, what data moves between them, and direction (one-way or bidirectional)."

## Goal

Generate a machine-readable dataflow artifact at `.specify/memory/architecture/dataflow-[name].md` from the user's description. The artifact is consumed by AI agents for architecture-review and coding tasks.

## Naming Migration

- Canonical command name: `/prodkit.dataflow`
- Deprecated alias: `/prodkit.dataflowdiagram` (retain as compatibility alias during migration)

## Pre-Generation Validation

Before generating, scan the user's description for:
- **Unnamed services**: any service referred to only as "it" or "the system" -> ask for a name.
- **Ambiguous direction**: flows where direction is unclear -> ask for clarification.
- **Circular dependencies**: if Service A depends on B and B depends on A, flag it: "Circular dependency detected between [A] and [B] - is this intentional? Describe the coordination mechanism."
- **Missing payload description**: flows where what data moves is unspecified -> ask for a brief payload description.

List all ambiguities and ask the user to resolve them before generating. Do not generate with unresolved ambiguities.

## Target File

`.specify/memory/architecture/dataflow-[name].md`

Derive `[name]` from the user's description (2-4 words, hyphenated, lowercase). Example: if the user describes invoice processing flows, use `dataflow-invoice-processing.md`. If a file with that name already exists, ask the user whether to overwrite or use a different name.

## File Schema

```markdown
---
file: dataflow-[name].md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [architecture-review, coding]
---

## Agent Summary

[<=150 words: describe what system this dataflow covers, the key services involved, the primary
data flows, and any critical constraints (e.g., "all flows are async", "Service A is the
single source of truth for invoice state"). Agents reading this summary should understand the
system boundary and main data paths without reading the full file.]

## Services

[One entry per service. Include what it owns and what it exposes.]

- **[ServiceName]**: [one-sentence description]. Owns: [data it is authoritative for]. Exposes: [interface type - REST API / gRPC / events / library call].

## Data Flows

[One row per flow. Direction: `->` for unidirectional, `<->` for bidirectional.]

| From | To | Data | Direction | Protocol | Notes |
|------|----|------|-----------|----------|-------|
| [Service A] | [Service B] | [payload description] | -> | [HTTP/gRPC/event/etc.] | [sync/async, triggers, SLA] |

## Dependencies

[Explicit service dependencies - which service requires another service to function.]

- [ServiceA] depends on [ServiceB] for [reason - e.g., "payment authorization"]
- [ServiceB] depends on [ServiceC] for [reason - e.g., "customer profile lookup"]

## Open Questions

[Any unresolved questions about this dataflow that were flagged during generation.]

- [Question 1]
```

Replace `YYYY-MM-DD` with today's date. Fill `[name]` with the derived artifact name.

Generate `## Agent Summary`, `## Services`, `## Data Flows`, and `## Dependencies` from the user's description. Populate `## Open Questions` with any remaining uncertainties.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, <=150 words.
3. `## Services` lists every service mentioned in the user's description.
4. `## Data Flows` table has all required columns and at least one row per described flow.
5. `## Dependencies` reflects the implied dependency graph from the flows.
6. `## Open Questions` is present (may be empty if all ambiguities resolved).
7. Report: "`.specify/memory/architecture/dataflow-[name].md` created."

Also confirm whether `architecture.md` exists - if yes, suggest adding a reference to the new dataflow file in the `## Dataflow` section of `architecture.md`.
