# /prodkit.ai-native

## User Input

```text
$ARGUMENTS
```

Supports `--validate` flag: validates that AI-native principles are consistently referenced across `engineering.md` and `product.md`.

## Goal

Scaffold `.specify/memory/ai-native.md` — the AI-native engineering standards file defining the seven principles all systems built in this repo must follow. Also inserts a cross-reference into `engineering.md` if not already present. If the file already exists, add only missing sections.

## Target File

`.specify/memory/ai-native.md`

## Idempotency Rule

- **Does not exist** → create using the schema below.
- **Exists** → read, identify missing `##` sections (each principle is one `##` section), append only missing ones. Do NOT modify existing content. Report added sections or "nothing to add."

## File Schema

```markdown
---
file: ai-native.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review]
---

## Agent Summary

This file defines the AI-native engineering standards for this repository. All systems,
services, and features MUST be designed so they can be reasoned about, invoked, and
inspected by AI agents. Seven principles apply: AI-Readable Systems, MCP Interoperability,
Explicit Workflow Modeling, Structured Data Contracts, Deterministic Interfaces,
Observability for Agents, and AI Discoverability. Agents reviewing code or architecture
should verify compliance with these principles before approving changes.

## AI-Readable Systems

All systems MUST expose structure that AI agents can interpret without heuristics.

**Required**:
- APIs must have typed, machine-readable schemas (e.g., OpenAPI, gRPC proto, GraphQL SDL).
- Business logic must be explicit — no hidden side effects or undocumented state changes.
- Function and method names must be semantic and action-oriented (e.g., `create_invoice`, `approve_payment`, not `process` or `run_task`).
- All configuration must be declarative and documented.

**Avoid**:
- Ambiguous function names that require reading the implementation to understand intent.
- Undocumented side effects.
- Implicit state changes triggered by unrelated operations.

## MCP Interoperability

All major system capabilities SHOULD be accessible through MCP-compatible interfaces where applicable.

**Design guidelines**:
- Map capabilities to tools: each discrete action the system can perform should be a named tool.
- Map workflows to toolchains: a sequence of steps should be expressible as a sequence of tool invocations.
- Map data models to schemas: each entity should have an explicit, discoverable schema.
- Tool names must be semantic: `create_invoice()`, `approve_payment()`, `reconcile_transaction()` — not `process()`, `execute()`.

**When to apply**: New services and significant feature additions. Existing services are exempt unless being refactored.

## Explicit Workflow Modeling

All major product workflows MUST be defined as machine-readable, inspectable workflows.

**Required format** (Markdown in `workflows/workflows.md` or YAML in `workflows/`):
```yaml
workflow:
  name: [workflow_name]
  steps:
    - [step_1]
    - [step_2]
    - [step_3]
```

**Benefits**: Agents can inspect workflows, reason about step sequences, and automate them.

**Required**: Any workflow that spans more than two services or involves a human approval step must be explicitly modeled.

## Structured Data Contracts

All system data MUST have explicit, versioned schemas.

**Required**:
- Every entity exposed by an API or event must have a named schema file (e.g., `invoice.schema.json`, `customer.schema.json`).
- Schemas must include field names, types, required vs. optional, and validation constraints.
- Schema changes must follow semantic versioning: breaking changes increment MAJOR.

**Benefits**: Agents understand object structures, enabling safer automation and reliable reasoning.

**Schema location**: `schemas/` at service root or in a shared `contracts/` directory.

## Deterministic Interfaces

System interfaces MUST be predictable: agents must always know expected inputs, outputs, and possible errors.

**Required**:
- Every function, API endpoint, and event consumer must document: (1) required inputs and types, (2) expected outputs and types, (3) all error conditions and their representations.
- No silent failures — errors must be surfaced explicitly with structured error types.
- Avoid boolean-return functions for operations that can fail in multiple distinct ways; use result types or structured exceptions instead.

**Avoid**:
- Catch-all error handlers that swallow error details.
- APIs that return `200 OK` with an error message in the body.
- Non-deterministic behavior based on undocumented external state.

## Observability for Agents

Systems MUST expose telemetry that AI agents can inspect to reason about system state.

**Required**:
- Structured logs (JSON) at INFO level for all significant operations.
- Task and workflow state must be queryable (not just inferable from logs).
- Audit history for all state-changing operations must be retained and accessible.
- Agents must be able to answer: "Why did this workflow fail?", "What step is pending?", "What was the last successful run?"

**Minimum telemetry per service**:
- Request/response logs with correlation IDs.
- Workflow step transitions with timestamps.
- Error events with full context (not just stack traces).

## AI Discoverability

All system capabilities MUST be discoverable by AI agents without requiring human explanation.

**Required**:
- Each service must expose a capability manifest listing its available tools/operations.
- Capability manifests must be machine-readable (JSON or YAML).
- Example location: `tools/invoice_tools.json`, `tools/payment_tools.json`.
- Agents must be able to enumerate all available tools by reading the manifests.

**Minimum manifest fields per tool**:
- `name`: semantic, action-oriented name
- `description`: one sentence explaining what the tool does
- `inputs`: typed input schema
- `outputs`: typed output schema
- `errors`: list of possible error types
```

Replace `YYYY-MM-DD` with today's date.

## Cross-Reference Injection

After writing `ai-native.md`, check `.specify/memory/engineering.md`:
- If it contains an `## AI-Native Code Requirements` section with a reference to `ai-native.md` → do nothing.
- If it does NOT contain such a reference → append the following to `engineering.md`:

```markdown

## AI-Native Code Requirements

> See `.specify/memory/ai-native.md` for full AI-native engineering standards.

- All APIs must expose machine-readable schemas.
- All services must return structured, predictable responses.
- Workflows must be defined declaratively where possible.
- Capability names must be semantic and action-oriented.
```

## `--validate` Mode

If `--validate` is present in `$ARGUMENTS`:
1. Read `ai-native.md`, `engineering.md`, and `product.md`.
2. For each of the seven principles, check whether it is referenced (by name or concept) in both `engineering.md` and `product.md`.
3. Report a table:

| Principle | In engineering.md | In product.md |
|-----------|------------------|---------------|
| AI-Readable Systems | ✓ / ✗ | ✓ / ✗ |
| MCP Interoperability | ✓ / ✗ | ✓ / ✗ |
| ... | | |

4. For any ✗, suggest which section of the target file should reference the principle.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All seven principle sections present.
4. `engineering.md` cross-reference exists (or was added).
5. No existing content overwritten.
6. Report outcome.
