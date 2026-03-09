# Phase 0 Research: AI-Native Product Development Framework

**Feature**: `002-ai-native-framework`
**Date**: 2026-02-08

All NEEDS CLARIFICATION items from the spec have been resolved via `/speckit.clarify`. This document captures the design decisions that follow from that session and the broader context required for implementation.

---

## Decision 1: Vendor-Native Auto-Loading File Formats

**Decision**: `/prodkit.agents` generates three files at the repository root using each vendor's native context-injection format.

| Vendor | File | Format | Context injection syntax |
|--------|------|--------|--------------------------|
| Claude Code | `CLAUDE.md` | Markdown | Plain prose instructions + relative file paths that Claude reads automatically from repo root |
| Cursor | `.cursorrules` | Markdown (legacy) or `.cursor/rules/*.mdc` (new) | `@file` references or plain instructions; `.cursorrules` at root is read automatically at session start |
| Gemini (Gemini Code Assist / CLI) | `GEMINI.md` | Markdown | Plain prose instructions + relative file paths read automatically from repo root |

**Rationale**: Vendor-native auto-loading eliminates the per-session manual context injection problem stated in the spec. Each vendor already has an established convention; generating into those conventions means zero user action after initial `/prodkit.agents` run.

**Alternatives considered**:
- A unified `prodkit-context.md` that users manually load — rejected because it requires action every session.
- `.cursor/rules/*.mdc` (new Cursor format) — deferred; `.cursorrules` is universally supported across Cursor versions including older installs.

---

## Decision 2: YAML Frontmatter Schema

**Decision**: Every knowledge-base file begins with a YAML frontmatter block:

```yaml
---
file: company.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review, product-planning, security-audit]
---
```

| Field | Type | Purpose |
|-------|------|---------|
| `file` | string | Canonical file name — agents use this to confirm they loaded the right file |
| `version` | semver string | Monotonically increases with meaningful content changes; agents can detect changes |
| `last-updated` | ISO 8601 date | Staleness check: agents re-read if this date is newer than session start |
| `required-by-tasks` | string list | Subset of routing table task categories this file is required for |

**Rationale**: Frontmatter is parseable in a single pass before the agent reads the file body. The four fields answer the three agent questions: "What is this file?", "Is it fresh?", and "Do I need it for my current task?"

**Alternatives considered**:
- HTML comments as semantic markers — rejected; less structured, harder to parse reliably.
- JSON sidecar files — rejected; splits human and machine content, adds file proliferation.

---

## Decision 3: `agents.md` Routing Table Structure

**Decision**: The routing table in `agents.md` is a Markdown table with task categories as rows and knowledge-base files as columns. Required files are marked with `✓`.

```markdown
## Task Routing Table

| Task Category      | company | marketing | product | security | architecture | engineering | ai-native | agents |
|--------------------|---------|-----------|---------|----------|--------------|-------------|-----------|--------|
| coding             |         |           | ✓       |          | ✓            | ✓           | ✓         | ✓      |
| architecture-review|         |           | ✓       | ✓        | ✓            | ✓           | ✓         | ✓      |
| product-planning   | ✓       | ✓         | ✓       |          |              |             |           | ✓      |
| security-audit     |         |           | ✓       | ✓        | ✓            | ✓           |           | ✓      |
```

**Rationale**: A Markdown table is natively readable by AI agents without JSON parsing. Agents can scan the row matching their current task type and identify required files in a single pass. This format is also human-auditable.

**Alternatives considered**:
- YAML task routing block in `agents.md` — viable but requires agents to parse YAML syntax inside Markdown; Markdown table is simpler.
- `prodkit-manifest.json` — rejected; external JSON file fragments the knowledge base and requires tooling.

---

## Decision 4: `## Agent Summary` Section Contract

**Decision**: Every knowledge-base file MUST contain `## Agent Summary` as the first section (after frontmatter). The section MUST be ≤150 words and MUST answer three questions:
1. What domain does this file cover?
2. What are the two or three most critical facts for an agent working on any task?
3. Which sections contain depth for the specific task types this file supports?

**Rationale**: Agents load the summary first during routing. The 150-word cap ensures the summary always fits in minimal context budget. The three-question structure makes summaries consistently useful rather than restatements of the file title.

**Alternatives considered**:
- Frontmatter `description` field — rejected; two-sentence description is too shallow for multi-domain files like `architecture.md`.
- `prodkit-summary.md` index — rejected; stale risk when individual files update without updating the index.

---

## Decision 5: Staleness Policy Expression

**Decision**: The staleness policy is written as explicit agent instructions in `agents.md`:

```markdown
## Staleness Policy

Before beginning any task, check the `last-updated` field in the frontmatter of each
required knowledge-base file (per the routing table above). If any file's `last-updated`
date is newer than your session start time, re-read that file before proceeding.
```

**Rationale**: Plain prose instructions in `agents.md` are consumed by all vendor agents without special syntax. The `last-updated` field (from Decision 2) provides the signal; this policy tells agents what to do with it.

**Alternatives considered**:
- `prodkit-lock.md` with last-seen versions — rejected; introduces state management overhead (requires updating the lock file on every file edit).
- No staleness tracking — rejected; silent stale context is a correctness risk in team settings.

---

## Decision 6: Command File Structure (Slash Commands)

**Decision**: Each `/prodkit.*` command file follows the same structure:
1. **User Input block** — captures arguments passed after the command
2. **Goal** — one-sentence intent statement
3. **File target** — canonical path of the file to create/update
4. **Idempotency rule** — explicit instruction to preserve existing sections
5. **File schema** — complete template the agent writes if the file doesn't exist (or uses to add missing sections)
6. **Validation** — what the agent confirms after writing

**Rationale**: Consistent command structure makes each command self-contained and independently testable. The idempotency rule is explicit rather than implied, preventing accidental overwrites.

**Alternatives considered**:
- Shared template files that commands reference by path — viable for a future CLI implementation, but adds indirection for the current slash-command delivery model.
