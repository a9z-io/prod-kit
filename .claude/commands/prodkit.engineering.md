# /prodkit.engineering

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/engineering.md` — the canonical engineering standards knowledge-base file. Agents load this for all `coding` and `architecture-review` tasks. If the file already exists, add only missing sections.

## Target File

`.specify/memory/engineering.md`

## Idempotency Rule

Before writing, check whether `.specify/memory/engineering.md` exists.
- **Does not exist** → create the full file using the schema below.
- **Exists** → read the file, identify which `##` sections are missing, and append only the missing sections. Do NOT modify any existing content. Report which sections were added (or "nothing to add" if all sections already present).

## File Schema

```markdown
---
file: engineering.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review]
---

## Agent Summary

[Fill in ≤150 words: describe the engineering environment. What are the 2–3 most critical facts an agent must know before writing code? Include primary language(s), the branching model, and the most important coding constraint (e.g., "all PRs require review", "no direct commits to main", "TypeScript strict mode required").]

## Git Workflow

[How the team uses Git.]

- **Branching model**: [e.g., GitHub Flow, Gitflow, trunk-based]
- **Branch naming**: [convention — e.g., `NNN-feature-name`]
- **Commit message format**: [convention — e.g., Conventional Commits]
- **PR process**: [required reviewers, checks, merge strategy]

## Branching Model

[Detailed branching rules.]

- **Main branch**: `main` (or `master`) — [protection rules]
- **Feature branches**: [naming pattern, lifetime, merge target]
- **Release branches**: [if applicable]
- **Hotfix branches**: [if applicable]

## Code Review Standards

[What constitutes an acceptable PR.]

- **Required reviewers**: [number and role]
- **Review SLA**: [expected turnaround]
- **Blocking criteria**: [what must be fixed before merge]
- **Non-blocking criteria**: [suggestions vs. required changes]

## Coding Guidelines

[Language-agnostic principles that apply to all code in this repo.]

- [Guideline 1 — e.g., "Functions must do one thing"]
- [Guideline 2 — e.g., "No magic numbers — use named constants"]
- [Guideline 3 — e.g., "Error paths must be explicitly handled"]

## Coding Style

[Formatting and style rules. Reference linter/formatter config where applicable.]

- **Formatter**: [tool + config file location]
- **Linter**: [tool + config file location]
- **Max line length**: [characters]
- **Naming conventions**: [variables, functions, classes, files]

## Package Management

[Dependency management rules.]

- **Package manager**: [npm / pip / cargo / uv / etc.]
- **Adding dependencies**: [process — e.g., "must be approved in PR, pinned to exact version"]
- **Updating dependencies**: [cadence and process]
- **Prohibited packages**: [any explicitly banned libraries]

## Frameworks

[Primary frameworks and their approved versions.]

| Framework | Version | Purpose |
|-----------|---------|---------|
| [Name]    | [semver constraint] | [what it is used for] |

## Databases

[Databases in use and usage rules.]

| Database | Version | Use case | Notes |
|----------|---------|----------|-------|
| [Name]   | [version] | [primary/cache/search] | [any constraints] |

## Approved Tools

[Tooling approved for use in this codebase.]

- **CI/CD**: [tool]
- **Monitoring**: [tool]
- **Secrets management**: [tool]
- **Feature flags**: [tool or "N/A"]
- **Error tracking**: [tool]

## Open Source Constraints

[Rules governing use of open-source dependencies.]

- **Permitted licenses**: [e.g., MIT, Apache 2.0, BSD]
- **Prohibited licenses**: [e.g., AGPL, GPL without exception]
- **Review process**: [how new OSS dependencies are approved]

## AI-Native Code Requirements

> See `.specify/memory/ai-native.md` for full AI-native engineering standards.

- All APIs must expose machine-readable schemas.
- All services must return structured, predictable responses.
- Workflows must be defined declaratively where possible.
- Capability names must be semantic and action-oriented (prefer `create_invoice()` over `process()`).
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All eleven domain sections present.
4. `## AI-Native Code Requirements` cross-references `ai-native.md`.
5. No existing content overwritten.
6. Report outcome.
