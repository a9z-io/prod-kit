# Data Model: AI-Native Product Development Framework

**Feature**: `002-ai-native-framework`
**Date**: 2026-02-08

This feature produces no database schema. The "data model" is the document schema — the structure every knowledge-base file and config file must conform to.

---

## Entity 1: Knowledge-Base File

A structured Markdown document representing one domain of organizational knowledge. Every knowledge-base file conforms to this schema.

### Structure

```
[YAML frontmatter]
## Agent Summary          ← mandatory, ≤150 words
## [Domain Section 1]     ← ## heading, domain-specific
### [Subsection]          ← ### heading where depth needed
## [Domain Section N]
```

### Frontmatter Schema

| Field | Type | Required | Constraints | Example |
|-------|------|----------|-------------|---------|
| `file` | string | yes | Canonical file name, matches filename | `company.md` |
| `version` | string | yes | Semantic version (MAJOR.MINOR.PATCH) | `1.0.0` |
| `last-updated` | string | yes | ISO 8601 date (YYYY-MM-DD) | `2026-02-08` |
| `required-by-tasks` | list of strings | yes | Subset of routing table task categories | `[coding, architecture-review]` |

### Heading Hierarchy Rules

- Top-level domain sections: `##` only
- Subsections: `###` only
- No deeper nesting (`####` and below) — agents parse heading structure; deeper nesting adds ambiguity
- `## Agent Summary` MUST appear before all domain sections

### Instances (one per scaffold command)

| File | Canonical Path | Task Tags | Primary Sections |
|------|---------------|-----------|-----------------|
| `company.md` | `.specify/memory/company.md` | `[product-planning]` | Vision, Mission, Core Values, Strategic Goals, Target Customers |
| `marketing.md` | `.specify/memory/marketing.md` | `[product-planning]` | Branding, Positioning, Messaging, ICP, Value Propositions |
| `product.md` | `.specify/memory/product.md` | `[coding, architecture-review, product-planning, security-audit]` | Purpose, Scope, KPIs, Competition Analysis, Core Workflows, User Journeys, Feature Roadmap |
| `security.md` | `.specify/memory/security.md` | `[coding, architecture-review, security-audit]` | Encryption Standards, Authentication, Authorization, Data Protection, Compliance |
| `architecture.md` | `.specify/memory/architecture.md` | `[coding, architecture-review]` | System Overview, Dataflow, Service Boundaries, API Architecture, Event Flows, Infrastructure Stack |
| `engineering.md` | `.specify/memory/engineering.md` | `[coding, architecture-review]` | Git Workflow, Branching Model, Code Review Standards, Coding Guidelines, Package Management, Approved Tools |
| `ai-native.md` | `.specify/memory/ai-native.md` | `[coding, architecture-review]` | AI-Readable Systems, MCP Interoperability, Explicit Workflow Modeling, Structured Data Contracts, Deterministic Interfaces, Observability for Agents, AI Discoverability |
| `agents.md` | `.specify/memory/agents.md` | `[coding, architecture-review, product-planning, security-audit]` | Agent Responsibilities, Task Routing Table, Staleness Policy, File Modification Rules, Conflict Resolution |
| `roadmap.md` | `.specify/memory/roadmap/roadmap.md` | `[product-planning]` | Milestones, Trade-offs, Dependencies |

---

## Entity 2: Agent Config File (Vendor-Native Auto-Loader)

A file placed at the repository root in each vendor's supported format. Read automatically by the vendor's AI agent at session start. References knowledge-base files by relative path.

### Instances

| Vendor | File | Location | Injection Syntax |
|--------|------|----------|-----------------|
| Claude Code | `CLAUDE.md` | Repo root | Plain Markdown instructions; relative file paths that Claude reads |
| Cursor | `.cursorrules` | Repo root | Plain Markdown instructions; `@` file references |
| Gemini | `GEMINI.md` | Repo root | Plain Markdown instructions; relative file paths |

### Required Content per File

Every vendor-native file MUST contain:
1. **Preamble** — one paragraph describing Prod-Kit and instructing the agent to use the knowledge base
2. **Always-load** — `agents.md` file reference (for routing table and staleness policy)
3. **Routing instruction** — explicit instruction to consult `agents.md` routing table before each task and load only the required file subset
4. **Staleness instruction** — explicit instruction to check `last-updated` frontmatter before loading any file

---

## Entity 3: Task Routing Table

A Markdown table inside `agents.md` that maps task categories to required knowledge-base file subsets. The authoritative source for agent context selection.

### Schema

```markdown
| Task Category       | company | marketing | product | security | architecture | engineering | ai-native | agents |
|---------------------|---------|-----------|---------|----------|--------------|-------------|-----------|--------|
| coding              |         |           | ✓       |          | ✓            | ✓           | ✓         | ✓      |
| architecture-review |         |           | ✓       | ✓        | ✓            | ✓           | ✓         | ✓      |
| product-planning    | ✓       | ✓         | ✓       |          |              |             |           | ✓      |
| security-audit      |         |           | ✓       | ✓        | ✓            | ✓           |           | ✓      |
```

### Constraints

- Task categories MUST match the `required-by-tasks` values used in file frontmatter
- `agents.md` MUST always appear in every task category row (it contains the routing table itself)
- New task categories may be added by users; existing categories must not be removed without updating all file frontmatter

---

## Entity 4: Dataflow Artifact

A structured Markdown document generated by `/prodkit.dataflowdiagram` representing services and data flows.

### Schema

```markdown
---
file: dataflow-[name].md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [architecture-review, coding]
---

## Agent Summary
[≤150 words: what system this describes, key services, primary flows]

## Services
- **[ServiceName]**: [one-sentence description, owns: [data], exposes: [interface]]

## Data Flows
| From | To | Data | Direction | Notes |
|------|----|------|-----------|-------|
| [Service A] | [Service B] | [payload] | → | [sync/async, protocol] |

## Dependencies
- [ServiceA] depends on [ServiceB] for [reason]

## Open Questions
- [Any ambiguities flagged during generation]
```

### Canonical path

`.specify/memory/architecture/dataflow-[descriptive-name].md`

---

## Entity 5: Scaffold Command File

A Cursor slash-command definition file (`.claude/commands/prodkit.*.md`) that when invoked creates or updates one knowledge-base file. Not user-facing data; part of the framework itself.

### Required Structure

1. User Input block
2. Goal statement
3. Target file path (canonical)
4. Idempotency rule
5. Complete file template (frontmatter + all sections as stubs)
6. Post-write validation steps

### State Transitions

```
[File does not exist] → command run → [File created with stubs]
[File exists, all sections present] → command run → [File unchanged, "nothing to add" reported]
[File exists, missing sections] → command run → [Missing sections added, existing preserved]
```
