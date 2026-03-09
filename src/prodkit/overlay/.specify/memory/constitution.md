<!--
This file is part of the Prod‑Kit overlay file set.

If a target repo already has a constitution, `prodkit overlay` will skip this file by default so
you can merge manually. Use `--force-constitution` only if you want to overwrite it.
-->

<!--
Sync Impact Report
- Version change: Unratified template → 1.0.0
- Modified principles: N/A (template → first ratified set)
- Added sections: Core Principles; Required Artifacts & Canonical Locations; Workflow & Quality Gates; Governance
- Removed sections: N/A (placeholders replaced)
- Templates requiring updates:
  - ✅ /Users/denni/git/truspark/prod-kit/.specify/templates/plan-template.md
  - ✅ /Users/denni/git/truspark/prod-kit/.specify/templates/spec-template.md
  - ✅ /Users/denni/git/truspark/prod-kit/.specify/templates/tasks-template.md
  - ✅ /Users/denni/git/truspark/prod-kit/.claude/commands/speckit.constitution.md
  - ⚠ /Users/denni/git/truspark/prod-kit/.claude/commands/speckit.plan.md (references template/command paths; review recommended)
- Deferred items:
  - TODO(RATIFICATION_DATE): original adoption date unknown for this constitution
-->

# Prod‑Kit Constitution

## Core Principles

### I. Product Constitution First (Durable Truths)
Every product MUST be anchored in a durable, slowly-changing Product Constitution before
technical specs evolve.

Non‑negotiables:
- A Product Constitution MUST exist for each product and MUST define: vision, ICP, value,
  differentiation, and measurable success metrics.
- Product Constitution updates MUST be treated as deliberate governance changes (not
  incidental edits during implementation).
- If a spec conflicts with the Product Constitution, the spec MUST change or the Product
  Constitution MUST be explicitly amended first.

Rationale: without durable intent and success definitions, downstream specs become guesswork
and execution loses context.

### II. Augmentation, Not Replacement (Spec‑Kit Compatible)
Prod‑Kit MUST extend Spec‑Kit’s workflow and mental model, not fork it.

Non‑negotiables:
- Prod‑Kit guidance MUST layer onto the existing phases (clarify → specify → plan → tasks →
  implement) and preserve their intent.
- Any new artifact, prompt, or schema MUST be additive and MUST not require changing or
  reinterpreting Spec‑Kit’s core outputs.
- Where Prod‑Kit introduces stronger requirements, it MUST do so as explicit “gates” and
  templates rather than bespoke parallel workflows.

Rationale: teams only benefit if product thinking is embedded in the workflow engineers
already trust.

### III. Opinionated Defaults, Explicit Overrides
Prod‑Kit MAY be opinionated (especially for PLG), but deviations MUST be explicit and
documented.

Non‑negotiables:
- Defaults (e.g., KPI framework, artifact structure, discovery prompts) MUST be documented.
- When a product deviates from defaults, the override MUST be captured in the Product
  Constitution (or an adjacent durable artifact) with a short rationale.
- “It depends” is not an output: if flexibility is needed, the decision + rationale MUST be
  recorded.

Rationale: flexibility without explicit decisions produces ambiguity and weak alignment.

### IV. Traceability (Strategy → Intent → Spec → Delivery → KPIs)
Every important artifact MUST link to its upstream intent and downstream measurement.

Non‑negotiables:
- Feature specs MUST reference the product’s Product Constitution and the success metrics
  they move.
- Plans and tasks MUST preserve links back to user stories and success metrics (not just
  code changes).
- KPI definitions MUST be treated as first‑class: if success is claimed, measurement MUST
  be defined (and instrumented unless explicitly deferred).

Rationale: traceability prevents “feature drift” and enables outcome-driven delivery.

### V. Reality Grounding (Users, Workflows, Competition)
Prod‑Kit MUST keep product intent grounded in real users, real workflows, and real market
constraints.

Non‑negotiables:
- Products MUST define primary personas and critical workflows (happy paths + key failure
  modes) before committing to delivery plans.
- Competitive context MUST be captured and updated over time (direct and indirect
  competitors, differentiation, and packaging/pricing signals where relevant).
- Roadmaps MUST be expressed as milestones aligned to outcomes, with explicit trade‑offs.

Rationale: product clarity comes from reality checks, not internal narratives.

## Required Artifacts & Canonical Locations

In a repo using Prod‑Kit, the product definition layer MUST exist alongside (not inside)
feature specs. Strong defaults:

```text
company/
  profile.md              # company identity, vision, mission, strategic goals

product/
  constitution.md         # durable product truths (vision, ICP, value, success metrics)

competition/
  landscape.md            # competitors, differentiation, positioning notes

kpis/
  kpis.md                 # KPI definitions (activation/engagement/retention/expansion/TTV)
  dashboard.md            # canonical dashboard link + ownership + review cadence (if applicable)

workflows/
  users.md                # personas, roles/permissions
  workflows.md            # 2–3 primary workflows + key edge cases
  technical-workflows.md  # system interactions/data flows/auth/permissions (when needed)

roadmap/
  roadmap.md              # outcome-based milestones, dependencies, trade-offs
```

Allowed variations:
- File format MAY be Markdown, YAML, or JSON, but locations MUST be consistent and linked
  from the product’s `product/constitution.*`.
- If an artifact is intentionally omitted (early stage), the omission MUST be recorded in
  `product/constitution.*` with a short rationale and a revisit trigger.

## Workflow & Quality Gates

Prod‑Kit augments the Spec‑Kit phases with product gates:

- Clarify (augmented “Purpose”):
  - MUST answer: who is this for (ICP), what problem/value, what success looks like, and
    why now.
  - Output MUST update (or create) the Product Constitution when new durable truths are
    discovered.

- Specify (enhanced boundaries):
  - MUST state scope and explicit out‑of‑scope.
  - MUST link to the Product Constitution and list which KPIs and workflows are impacted.

- Plan (constitution enforcement):
  - MUST include a Constitution Check section that fails fast when product intent, KPIs,
    or traceability are missing.

- Tasks (delivery traceability):
  - MUST keep tasks grouped by user story and include any required instrumentation tasks
    needed to validate success metrics.
  - If instrumentation is deferred, the tasks MUST include an explicit deferral item with
    rationale and a follow-up trigger.

## Governance

This constitution governs Prod‑Kit’s required behavior in templates and workflows.

Amendments:
- Amendments MUST be made via PR that explains the rationale and lists impacted templates
  and command guidance.
- Amendments MUST include a Sync Impact Report update (at the top of this file).

Versioning:
- This constitution follows Semantic Versioning (MAJOR.MINOR.PATCH).
  - MAJOR: breaking governance changes (principles removed/redefined)
  - MINOR: new principle/section or materially expanded guidance
  - PATCH: clarification/typos/non-semantic refinements

Compliance review expectations:
- Any PR modifying `.specify/templates/*` MUST confirm alignment with this constitution.
- Any PR that changes a required artifact, gate, or workflow MUST update both this file
  and the relevant templates/command docs.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): set original adoption date | **Last Amended**: 2026-02-08

