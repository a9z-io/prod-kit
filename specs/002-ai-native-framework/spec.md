# Feature Specification: AI-Native Product Development Framework

**Feature Branch**: `002-ai-native-framework`
**Created**: 2026-02-08
**Status**: Draft
**Input**: User description: "AI-native product development framework — vendor-agnostic multi-agent product brain that organizes company, product, engineering, and architecture knowledge as structured Markdown files consumable by multiple AI agents (Cursor, Claude, Gemini, etc.) with agent-specific instruction files and a new set of /prodkit.* commands."

## Product Context *(mandatory)*

- **Product Constitution**: [`.specify/memory/constitution.md`](../../.specify/memory/constitution.md)
- **ICP / User**: Engineering team leads and product engineers at software companies who use AI coding agents daily and want those agents to reason consistently about product strategy, architecture, and engineering standards — without re-explaining context every session.
- **Problem / Value**: AI coding agents today have no shared, persistent understanding of a team's product strategy, architecture decisions, or engineering standards. Each session starts from zero, producing inconsistent output and requiring repeated manual context injection. Prod-Kit's AI-Native Framework gives every agent a single, structured, version-controlled knowledge base to reason against — enabling consistent, product-aligned code generation across vendors.
- **Primary KPIs impacted**: Time-to-value (first productive AI-assisted session); Activation (teams that complete full knowledge-base setup); Engagement (commands run per week per team); Retention (teams still using Prod-Kit 30 days after install).

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Bootstrap the Knowledge Base (Priority: P1)

An engineering lead joins a new product team. She runs a single command (`/prodkit.company`, `/prodkit.product`, etc.) and the framework scaffolds structured Markdown files for company identity, product strategy, engineering standards, security posture, and architecture. She fills in her team's specifics. From that point forward every AI agent on the team loads these files as context before generating code or plans.

**Why this priority**: This is the entry point to all value. Without the knowledge base, no other command or agent feature works. It delivers standalone value even before any agent-specific configuration is added.

**Independent Test**: Can be fully tested by running each `/prodkit.*` scaffold command in an empty repo, confirming each required Markdown file is created with the correct section structure, and verifying an AI agent can load it as context without errors.

**Acceptance Scenarios**:

1. **Given** an empty Spec-Kit repo with Prod-Kit overlay applied, **When** the user runs `/prodkit.company`, **Then** a `company.md` file is created under `.specify/memory/` with all required sections (Vision, Mission, Core Values, Strategic Goals, Target Customers) as editable stubs.
2. **Given** `company.md` already exists, **When** the user runs `/prodkit.company` again, **Then** the command preserves existing content and only adds missing sections, reporting which sections were added.
3. **Given** the user runs all scaffold commands in sequence, **When** each command completes, **Then** every file defined in the knowledge architecture exists at its canonical path with no placeholder section left blank.

---

### User Story 2 — Configure Per-Agent Instruction Files (Priority: P2)

A developer uses Cursor as her primary IDE and her colleague uses Claude Code. They both work on the same repo. Running `/prodkit.agents` generates vendor-native auto-loading files at the repo root — `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` — each using that vendor's supported context-injection syntax to reference the relevant Prod-Kit knowledge-base files. Every new agent session picks up Prod-Kit context automatically, with no manual action required.

**Why this priority**: Without vendor-native auto-loading files, the knowledge base exists but agents don't pick it up automatically. This unlocks the zero-friction, multi-vendor value proposition.

**Independent Test**: Can be fully tested by running `/prodkit.agents`, confirming `CLAUDE.md` and `.cursorrules` are created at repo root, then opening a new Cursor session and verifying it loads Prod-Kit knowledge-base files automatically.

**Acceptance Scenarios**:

1. **Given** the knowledge-base files exist, **When** the user runs `/prodkit.agents`, **Then** vendor-native auto-loading files (`CLAUDE.md`, `.cursorrules`, `GEMINI.md`) are created at repo root, each referencing the relevant knowledge-base files via that vendor's supported include syntax.
2. **Given** an agent config file already exists, **When** `/prodkit.agents` is run again, **Then** only missing files are added and existing files are not overwritten without an explicit `--force` flag.
3. **Given** a vendor's config file is open in the IDE, **When** a coding task is started, **Then** the agent correctly references `product.md`, `architecture.md`, and `engineering.md` before generating output.

---

### User Story 3 — Generate and Update Architecture Artifacts (Priority: P3)

A senior engineer needs to onboard a new AI agent with current system architecture. She runs `/prodkit.architecture` to scaffold `architecture.md` and `/prodkit.dataflowdiagram` to generate a machine-readable dataflow diagram from existing code or a provided description. The resulting artifacts are committed to the repo so every future agent session has accurate architecture context.

**Why this priority**: Architecture context is the highest-value input for preventing agents from generating structurally inconsistent code. It is lower priority than P1/P2 because those must exist first.

**Independent Test**: Can be fully tested by running `/prodkit.dataflowdiagram` with a description of two services and verifying a structured diagram artifact is created at the canonical path with correct service and flow nodes.

**Acceptance Scenarios**:

1. **Given** `architecture.md` does not exist, **When** the user runs `/prodkit.architecture`, **Then** a structured file is created with sections for System Overview, Service Boundaries, API Architecture, Event Flows, and Infrastructure Stack.
2. **Given** a description of system services, **When** the user runs `/prodkit.dataflowdiagram`, **Then** a machine-readable dataflow artifact is created showing services, data flows between them, and directionality.
3. **Given** `architecture.md` exists and code has changed, **When** the user runs `/prodkit.architecture --update`, **Then** the command prompts for changed sections and merges updates without overwriting unchanged content.

---

### User Story 4 — Define AI-Native Engineering Standards (Priority: P4)

A product architect wants to ensure all new features are designed for AI operability — meaning agents can discover, invoke, and reason about system capabilities. She runs `/prodkit.ai-native` to scaffold `ai-native.md`, which captures MCP interoperability rules, explicit workflow modeling requirements, structured data contract standards, and deterministic interface guidelines. These standards are then referenced by `engineering.md` and enforced in code review via agent checks.

**Why this priority**: AI-native standards enable the long-term vision of agent-driven development but require the foundational knowledge base (P1–P3) to exist first.

**Independent Test**: Can be fully tested by running `/prodkit.ai-native`, confirming `ai-native.md` is created with all seven core principle sections, and verifying that a coding agent asked to design a new feature references the AI-native constraints in its output.

**Acceptance Scenarios**:

1. **Given** `engineering.md` exists, **When** the user runs `/prodkit.ai-native`, **Then** `ai-native.md` is created with sections for all seven AI-native principles and a cross-reference to `engineering.md` is inserted.
2. **Given** `ai-native.md` exists, **When** an agent generates a new service design, **Then** the agent's output references at least MCP interoperability and structured data contract sections as constraints.
3. **Given** the user adds a custom AI-native principle, **When** `/prodkit.ai-native --validate` is run, **Then** the command confirms the principle is consistently referenced across `engineering.md` and `product.md`.

---

### Edge Cases

- What happens when a knowledge-base file is partially filled (some sections have content, others are stubs)? Commands must detect and report incomplete sections without overwriting completed ones.
- What happens when two agents have conflicting instructions in their config files? The `agents.md` file defines a conflict-resolution priority order; commands must enforce it.
- What happens when a scaffold command is run in a repo that does not have Prod-Kit overlay applied? The command must exit with a clear error directing the user to run `prodkit overlay` first.
- What happens when a dataflow diagram description is ambiguous (e.g., circular dependencies, unnamed services)? The command must list ambiguities and request clarification before generating the artifact.
- What happens when the repo uses a non-standard directory structure? All canonical paths must be configurable via a `.prodkit.toml` or equivalent config file.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The framework MUST provide a scaffold command for each knowledge-base file: `company.md`, `marketing.md`, `product.md`, `security.md`, `architecture.md`, `engineering.md`, `ai-native.md`, and `agents.md`.
- **FR-002**: Each scaffold command MUST create its target file with a YAML frontmatter block, a mandatory `## Agent Summary` section (≤150 words, auto-generated as a stub), and all required domain sections as editable stubs if the file does not exist.
- **FR-003**: Each scaffold command MUST preserve existing content when the target file already exists, adding only missing sections.
- **FR-004**: The framework MUST provide a `/prodkit.agents` command that generates vendor-native auto-loading files (`CLAUDE.md` at repo root, `.cursorrules` at repo root, `GEMINI.md` at repo root) that each vendor's agent reads automatically at session start, with `@file` references or equivalent include syntax pointing to the relevant Prod-Kit knowledge-base files.
- **FR-005**: Each vendor-native auto-loading file MUST use only that vendor's supported context-injection syntax so the agent loads knowledge-base content without any user action per session.
- **FR-006**: The framework MUST provide a `/prodkit.dataflowdiagram` command that generates a machine-readable dataflow artifact from a user-provided service description.
- **FR-007**: The framework MUST provide a `/prodkit.roadmap` command that scaffolds a `roadmap.md` file aligned to the product's KPI framework and milestones.
- **FR-008**: All knowledge-base files MUST use plain-text Markdown with a YAML frontmatter block containing `file` (canonical name), `version` (semver), `last-updated` (ISO date), and `required-by-tasks` (list of task-category tags matching the routing table in `agents.md`). All top-level sections MUST use `##` headings and subsections MUST use `###`, consistently across all files.
- **FR-009**: All canonical file paths MUST be configurable to support non-standard repository structures.
- **FR-010**: Each command MUST validate that the Prod-Kit overlay is present before executing and produce a clear error if it is not.
- **FR-011**: The `ai-native.md` file MUST include sections for all seven AI-native principles: AI-Readable Systems, MCP Interoperability, Explicit Workflow Modeling, Structured Data Contracts, Deterministic Interfaces, Observability for Agents, and AI Discoverability.
- **FR-012**: The `agents.md` file MUST define agent responsibilities, file-modification rules, conflict-resolution priority when multiple agents are active, a machine-readable task-type routing table that maps task categories (`coding`, `architecture-review`, `product-planning`, `security-audit`) to the required subset of knowledge-base files for that task, and a staleness policy instructing agents to re-read any knowledge-base file whose `last-updated` frontmatter date is newer than the agent's session-start timestamp.
- **FR-013**: The framework MUST provide a `prodkit.md` system constitution file enforcing vendor neutrality, open format, human+AI collaboration, repository-first knowledge, traceable architecture decisions, and agent-readable standards.

### Key Entities

- **Knowledge-Base File**: A structured Markdown document representing one domain of organizational knowledge (company, product, engineering, etc.). Has a YAML frontmatter block (`file`, `version`, `last-updated`, `required-by-tasks`), a canonical path, and required sections using strict `##`/`###` heading hierarchy.
- **Agent Config File**: A vendor-native auto-loading file (`CLAUDE.md`, `.cursorrules`, `GEMINI.md`) placed at repo root. Uses each vendor's supported include syntax to reference Prod-Kit knowledge-base files by path. Always injects `agents.md`; selective files are loaded per the task-type routing table defined in `agents.md`.
- **Scaffold Command**: A `/prodkit.*` command that creates or updates one knowledge-base or config file. Idempotent — safe to re-run.
- **Dataflow Artifact**: A structured Markdown or YAML document representing services, data flows, and directionality for a system. Machine-readable by AI agents.
- **System Constitution (`prodkit.md`)**: The governing document that defines Prod-Kit's non-negotiable principles for all files and agents in the repository.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A new team can complete full knowledge-base setup (all eight core files scaffolded and minimally filled) in under 30 minutes using only `/prodkit.*` commands.
- **SC-002**: An AI agent given only the `## Agent Summary` sections of the relevant knowledge-base files (selected via the task-type routing table) produces architecture-consistent code suggestions without the user providing additional system context in 90% of sessions.
- **SC-003**: All `/prodkit.*` scaffold commands are idempotent — re-running any command on a repo with existing content results in zero data loss and zero unintended overwrites in 100% of test cases.
- **SC-004**: Agent configuration files generated by `/prodkit.agents` are accepted without errors by each supported vendor's agent (Claude, Cursor, Gemini) in their standard context-loading flow.
- **SC-005**: Teams that complete the full knowledge-base setup report a measurable reduction in repeated context-injection overhead — target: 50% fewer manual context messages per AI coding session at 30 days post-setup.

### Clarifications

- **Vendor support scope**: Initial release targets Claude (claude.md), Cursor (cursor.md), and Gemini (gemini.md). OpenAI Codex support is deferred to a future release.
- **MCP integration depth**: The `ai-native.md` principles define what systems *should* expose; actual MCP server implementation for Prod-Kit tooling is out of scope for this spec and tracked separately.
- **Command delivery mechanism**: Commands are delivered as Cursor slash-commands (`.claude/commands/*.md` files) consistent with existing Prod-Kit patterns. A standalone CLI extension is out of scope for this spec.

### Session 2026-02-08

- Q: How do agents load knowledge-base files into context? → A: Auto-loaded via vendor-native root files — `/prodkit.agents` generates `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` at repo root, each referencing the relevant knowledge-base files by path using each vendor's native `@file` or include syntax. Zero user action required per session.
- Q: How do agents select which knowledge-base files to load for a given task? → A: Task-type routing table in `agents.md` — a machine-readable table maps task categories (e.g., `coding`, `architecture-review`, `product-planning`, `security-audit`) to the required subset of knowledge-base files. Vendor-native files always inject `agents.md`; agents consult the routing table to load only the relevant files for the active task.
- Q: What structure makes knowledge-base files reliably parseable by agents? → A: YAML frontmatter on every file containing `file`, `version`, `last-updated`, and `required-by-tasks` fields; plus strict `##` for all top-level sections and `###` for subsections throughout. Agents parse frontmatter to check freshness and routing tags without reading the full document.
- Q: How do agents handle large knowledge-base files without burning context budget? → A: Every knowledge-base file MUST have a mandatory `## Agent Summary` section (≤150 words) as its first section after frontmatter. Agents load this section first for routing decisions; the full file is loaded only when the task routing table specifies it as required for that task category.
- Q: How do agents know when a knowledge-base file has changed and must be re-read? → A: `agents.md` declares an explicit staleness policy: agents MUST re-read any knowledge-base file whose `last-updated` frontmatter date is newer than the current session-start timestamp. Vendor-native files instruct agents to check `last-updated` frontmatter before each task begins.
