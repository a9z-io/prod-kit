# /prodkit.product

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/product.md` — the canonical product strategy knowledge-base file. This is the most frequently loaded file (required by all four task categories). If the file already exists, add only missing sections.

## Target File

`.specify/memory/product.md`

## Idempotency Rule

Before writing, check whether `.specify/memory/product.md` exists.
- **Does not exist** → create the full file using the schema below.
- **Exists** → read the file, identify which `##` sections are missing, and append only the missing sections. Do NOT modify any existing content. Report which sections were added (or "nothing to add" if all sections already present).

## File Schema

```markdown
---
file: product.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review, product-planning, security-audit]
---

## Agent Summary

[Fill in ≤150 words: describe what this product does, who it serves, and the 2–3 most critical product facts an agent needs before any task. Mention the primary KPIs that define success and the one or two scope boundaries agents must never cross.]

## Purpose

[Why this product exists. One to three sentences answering: what problem does it solve, for whom, and what outcome does success look like for the customer?]

## Scope

[What is explicitly in scope and out of scope for this product.]

**In scope**:
- [capability 1]
- [capability 2]

**Out of scope**:
- [excluded capability 1]
- [excluded capability 2]

## KPIs

[The success metrics this product is measured against. Use the PLG framework where applicable.]

- **Activation**: [metric + target]
- **Engagement**: [metric + target]
- **Retention**: [metric + target]
- **Expansion**: [metric + target]
- **Time-to-value**: [metric + target]

## Competition Analysis

[Key direct and indirect competitors and how this product is differentiated.]

| Competitor | Category | Key strength | Our differentiation |
|------------|----------|--------------|---------------------|
| [Name]     | [Direct/Indirect] | [what they do well] | [why we win] |

## Core Workflows

[The 2–3 primary workflows users follow to get value. Step-by-step happy paths.]

### Workflow 1: [Name]

1. [Step 1]
2. [Step 2]
3. [Step 3]

### Workflow 2: [Name]

1. [Step 1]
2. [Step 2]

## User Journeys

[Key user journeys from first touch to core value. Focus on the moments that matter.]

- **[Journey name]**: [brief description of the journey and the "aha moment"]

## Feature Roadmap

[Current roadmap snapshot. Link to `roadmap/roadmap.md` for full detail.]

- **Now**: [what is being built or shipped]
- **Next**: [what is planned next]
- **Later**: [directional future bets]
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields; `required-by-tasks` contains all four task categories.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All seven domain sections present.
4. No existing content overwritten.
5. Report outcome.
