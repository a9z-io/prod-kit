# Tasks: AI-Native Product Development Framework

**Branch**: `002-ai-native-framework`
**Input**: Design documents from `/specs/002-ai-native-framework/`
**Prerequisites**: plan.md ✅ | spec.md ✅ | research.md ✅ | data-model.md ✅ | contracts/ ✅

**KPI Instrumentation (Prod-Kit)**:
- SC-001 (30-min setup) and SC-003 (idempotency) are testable at delivery — validation tasks included.
- SC-002 (90% session consistency) and SC-005 (50% context reduction) are deferred to post-launch user research. Deferral task included per plan.

---

## Phase 1: Setup

**Purpose**: Ensure directory structure exists and the overlay command directory is ready.

- [x] T001 Confirm `.claude/commands/` directory exists in repo root (it does — existing commands are present)
- [x] T002 [P] Confirm `src/prodkit/overlay/claude/commands/` exists for overlay mirroring (from prior feature)

---

## Phase 2: Foundational

**Purpose**: Shared conventions all 10 commands depend on. Must be decided before authoring any command file.

**⚠️ CRITICAL**: All user story command files depend on the conventions established here.

- [x] T003 Confirm YAML frontmatter schema from `data-model.md` Entity 1: fields `file`, `version` (semver), `last-updated` (ISO 8601), `required-by-tasks` (list). Document any amendments in `data-model.md`.
- [x] T004 [P] Confirm `## Agent Summary` contract: first section after frontmatter, ≤150 words, answers: (1) domain covered, (2) 2–3 critical facts, (3) which sections have depth per task type.
- [x] T005 [P] Confirm routing table task categories: `coding`, `architecture-review`, `product-planning`, `security-audit`. Document the canonical `✓`-cell format from `data-model.md` Entity 3.
- [x] T006 [P] Confirm command file structure template used by all 10 commands: (1) User Input block, (2) Goal, (3) Target file path, (4) Idempotency rule, (5) Full file schema with stubs, (6) Post-write validation.

**Checkpoint**: Conventions locked — command authoring can proceed in parallel.

---

## Phase 3: User Story 1 — Bootstrap the Knowledge Base (Priority: P1) 🎯 MVP

**Goal**: Eight scaffold commands that create agent-optimized knowledge-base files with YAML frontmatter, `## Agent Summary`, and domain sections. Idempotent — re-running preserves existing content.

**Independent Test**: Run each command in a fresh test repo, confirm file created at correct path with correct structure, run again to confirm idempotency (no overwrites, "nothing to add" reported).

### Implementation

- [x] T007 [P] [US1] Author `.claude/commands/prodkit.company.md` — scaffolds `.specify/memory/company.md` with frontmatter (`required-by-tasks: [product-planning]`), Agent Summary stub, sections: Vision, Mission, Core Values, Strategic Goals, Target Customers
- [x] T008 [P] [US1] Author `.claude/commands/prodkit.marketing.md` — scaffolds `.specify/memory/marketing.md` with frontmatter (`required-by-tasks: [product-planning]`), Agent Summary stub, sections: Branding, Positioning, Messaging, ICP, Value Propositions
- [x] T009 [P] [US1] Author `.claude/commands/prodkit.product.md` — scaffolds `.specify/memory/product.md` with frontmatter (`required-by-tasks: [coding, architecture-review, product-planning, security-audit]`), Agent Summary stub, sections: Purpose, Scope, KPIs, Competition Analysis, Core Workflows, User Journeys, Feature Roadmap
- [x] T010 [P] [US1] Author `.claude/commands/prodkit.security.md` — scaffolds `.specify/memory/security.md` with frontmatter (`required-by-tasks: [coding, architecture-review, security-audit]`), Agent Summary stub, sections: Encryption Standards, Authentication, Authorization, Data Protection, Compliance Requirements
- [x] T011 [P] [US1] Author `.claude/commands/prodkit.engineering.md` — scaffolds `.specify/memory/engineering.md` with frontmatter (`required-by-tasks: [coding, architecture-review]`), Agent Summary stub, sections: Git Workflow, Branching Model, Code Review Standards, Coding Guidelines, Coding Style, Package Management, Frameworks, Databases, Approved Tools, Open Source Constraints
- [x] T012 [US1] Author `.claude/commands/prodkit.agents.md` — scaffolds `.specify/memory/agents.md` with frontmatter (`required-by-tasks: [coding, architecture-review, product-planning, security-audit]`), Agent Summary stub, Task Routing Table (4 task categories × 8 files), Staleness Policy, Agent Responsibilities, File Modification Rules, Conflict Resolution Priority

**Checkpoint**: All six foundation KB file commands complete. US1 P1 independently testable — run all six in an empty repo and validate structure.

---

## Phase 4: User Story 2 — Configure Per-Agent Instruction Files (Priority: P2)

**Goal**: The `/prodkit.agents` command (in addition to scaffolding `agents.md`) generates three vendor-native auto-loading files at the repo root. Each uses the vendor's supported syntax to inject `agents.md` always-load plus routing-table-driven selective loading.

**Independent Test**: Run `/prodkit.agents` in a test repo with knowledge-base files present. Confirm `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` exist at repo root. Open a new Cursor session in the test repo and verify it references Prod-Kit files automatically.

### Implementation

- [x] T013 [US2] Extend `.claude/commands/prodkit.agents.md` (from T012) with the vendor-native file generation section:
  - `CLAUDE.md` at repo root: preamble, always-load `agents.md`, routing instruction, staleness check instruction (Claude plain-Markdown syntax)
  - `.cursorrules` at repo root: same instructions in Cursor-compatible syntax
  - `GEMINI.md` at repo root: same instructions in Gemini-compatible syntax
  - Idempotency: existing vendor files not overwritten without `--force` flag stated in command
- [x] T014 [US2] Author the canonical `CLAUDE.md` template content (preamble + `agents.md` always-load + routing instruction + staleness instruction) — this is the content the command writes to the user's repo root
- [x] T015 [P] [US2] Author the canonical `.cursorrules` template content (same structure, Cursor syntax)
- [x] T016 [P] [US2] Author the canonical `GEMINI.md` template content (same structure, Gemini syntax)

**Checkpoint**: Run `/prodkit.agents` end-to-end. Verify `CLAUDE.md`, `.cursorrules`, `GEMINI.md` generated at repo root with correct content and all three reference `agents.md` as always-load.

---

## Phase 5: User Story 3 — Generate and Update Architecture Artifacts (Priority: P3)

**Goal**: Two commands — `/prodkit.architecture` scaffolds `architecture.md` with structured sections; `/prodkit.dataflowdiagram` generates a machine-readable dataflow artifact from a user-provided description.

**Independent Test**: Run `/prodkit.dataflowdiagram` with a two-service description and verify a structured `.specify/memory/architecture/dataflow-[name].md` is created with `## Services` section and `## Data Flows` table matching the contract in `contracts/README.md`.

### Implementation

- [x] T017 [US3] Author `.claude/commands/prodkit.architecture.md` — scaffolds `.specify/memory/architecture.md` with frontmatter (`required-by-tasks: [coding, architecture-review]`), Agent Summary stub, sections: System Overview, Dataflow (pointer to dataflow artifacts), Service Boundaries, API Architecture, Event Flows, Infrastructure Stack. Includes `--update` mode instruction that merges changed sections without overwriting unchanged content.
- [x] T018 [US3] Author `.claude/commands/prodkit.dataflowdiagram.md` — generates `.specify/memory/architecture/dataflow-[name].md` from user description. Enforces dataflow artifact schema from `contracts/README.md` Contract 4: frontmatter, `## Agent Summary`, `## Services`, `## Data Flows` table (From / To / Data / Direction / Notes), `## Dependencies`, `## Open Questions`. Flags circular dependencies and unnamed services before generating.

**Checkpoint**: Both commands independently testable. Run `/prodkit.dataflowdiagram` with a known description and validate output against the contract schema.

---

## Phase 6: User Story 4 — Define AI-Native Engineering Standards (Priority: P4)

**Goal**: `/prodkit.ai-native` scaffolds `ai-native.md` with all seven AI-native principles and inserts a cross-reference into `engineering.md`.

**Independent Test**: Run `/prodkit.ai-native` in a test repo that has `engineering.md`. Confirm `ai-native.md` is created with all seven principle sections and `engineering.md` contains a cross-reference to `ai-native.md`.

### Implementation

- [x] T019 [US4] Author `.claude/commands/prodkit.ai-native.md` — scaffolds `.specify/memory/ai-native.md` with frontmatter (`required-by-tasks: [coding, architecture-review]`), Agent Summary stub, and sections for all seven principles:
  1. AI-Readable Systems (typed APIs, machine-readable schemas, semantic naming)
  2. MCP Interoperability (Capability→Tool, Workflow→Toolchain, Data model→Schema)
  3. Explicit Workflow Modeling (declarative workflow definitions, agent-inspectable steps)
  4. Structured Data Contracts (explicit schemas per entity, e.g., `invoice.schema.json`)
  5. Deterministic Interfaces (known inputs, outputs, and errors)
  6. Observability for Agents (logs, task status, workflow states, audit history)
  7. AI Discoverability (capability manifests, tool enumeration)
  
  Includes `--validate` mode that checks principle references are consistent across `engineering.md` and `product.md`. Inserts cross-reference bullet in `engineering.md` if not already present.

**Checkpoint**: Run `/prodkit.ai-native` and verify all seven sections present in `ai-native.md` and cross-reference appears in `engineering.md`.

---

## Phase 7: Roadmap Command (Supporting)

**Purpose**: The `/prodkit.roadmap` command rounds out the full knowledge-base scaffold set (FR-007). Grouped separately as it is not part of the four user stories but is a stated functional requirement.

- [x] T020 [US1] Author `.claude/commands/prodkit.roadmap.md` — scaffolds `.specify/memory/roadmap/roadmap.md` with frontmatter (`required-by-tasks: [product-planning]`), Agent Summary stub, sections: Milestones (outcome-aligned, not feature-aligned), Trade-offs, Dependencies and Sequencing. Sections align to the constitution's outcome-based roadmap requirement.

---

## Phase 8: Polish & Cross-Cutting

**Purpose**: Mirror files to overlay, validate idempotency, document, and record the KPI deferral.

- [x] T021 [P] Mirror all 10 authored command files from `.claude/commands/prodkit.*.md` to `src/prodkit/overlay/claude/commands/` so the `prodkit overlay` CLI deploys them to user repos
- [x] T022 [P] Validate SC-003 (idempotency): run each command twice in the same test repo directory and confirm zero unexpected changes on the second run
- [x] T023 [P] Validate SC-001 (time-to-setup): run all nine scaffold commands sequentially in a fresh repo and confirm total time is under 30 minutes
- [x] T024 [P] Update `README.md` to document the new `/prodkit.*` commands with a "Build the Knowledge Base" section and a link to `specs/002-ai-native-framework/quickstart.md`
- [x] T025 Record KPI deferral in `specs/002-ai-native-framework/plan.md` (already present) and confirm SC-002 / SC-005 measurement plan is documented with trigger: first five teams complete full knowledge-base setup
- [x] T026 [P] Run `specs/002-ai-native-framework/quickstart.md` validation checklist end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — blocks all command authoring
- **US1 (Phase 3)**: All T007–T012 can run in parallel after Phase 2
- **US2 (Phase 4)**: T013 depends on T012 (extends `prodkit.agents.md`); T014–T016 can run in parallel
- **US3 (Phase 5)**: T017 and T018 are independent, can run in parallel after Phase 2
- **US4 (Phase 6)**: T019 independent after Phase 2; can run in parallel with Phase 3–5
- **Roadmap (Phase 7)**: T020 independent after Phase 2; can run in parallel with all other phases
- **Polish (Phase 8)**: T021 depends on all command authoring complete; T022–T026 can run in parallel

### Parallel Opportunities

```
Phase 2 complete →
  ├── T007 (company)       ─┐
  ├── T008 (marketing)      │
  ├── T009 (product)        ├─ All US1 commands in parallel
  ├── T010 (security)       │
  ├── T011 (engineering)    │
  ├── T012 (agents base)   ─┘
  │
  ├── T017 (architecture)  ─┐ US3 in parallel
  ├── T018 (dataflow)      ─┘
  │
  ├── T019 (ai-native)      ← US4 in parallel
  └── T020 (roadmap)        ← supporting, in parallel

T012 complete →
  ├── T013 (agents vendor-native extension)
  ├── T014 (CLAUDE.md template)  ─┐ in parallel
  ├── T015 (.cursorrules template)├─ after T013
  └── T016 (GEMINI.md template)  ─┘
```

### User Story Dependencies

- **US1 (P1)**: Start after Phase 2; T007–T011 fully parallel; T012 sequential (authors the full `agents.md` base)
- **US2 (P2)**: T013 extends T012 output; T014–T016 parallel after T013
- **US3 (P3)**: Fully independent after Phase 2
- **US4 (P4)**: Fully independent after Phase 2

---

## Notes

- [P] = runs in parallel (no shared file conflicts)
- [US#] = maps task to user story for traceability
- All command files are Markdown — no compilation step, commit after each task
- Idempotency (T022) is a hard requirement for SC-003 — test before marking any command complete
- Each command file is independently deliverable and testable
- Deferral tasks (T025) are required by the Prod-Kit constitution for KPIs not measured at delivery
