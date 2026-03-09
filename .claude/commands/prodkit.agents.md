# /prodkit.agents

## User Input

```text
$ARGUMENTS
```

## Goal

Two operations in one command:

1. **Scaffold `.specify/memory/agents.md`** — the routing table and staleness policy that all vendor-native auto-loaders reference.
2. **Generate vendor-native auto-loading files** — `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` at the repository root so each vendor's agent loads Prod-Kit context automatically at session start.

If any file already exists, preserve existing content (idempotency rules below).

## Operation 1 — Scaffold `agents.md`

### Target File

`.specify/memory/agents.md`

### Idempotency Rule

- **Does not exist** → create using the schema below.
- **Exists** → read, identify missing `##` sections, append only missing sections. Do NOT modify existing content. Report added sections or "nothing to add."

### File Schema

```markdown
---
file: agents.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review, product-planning, security-audit]
---

## Agent Summary

This file is the control plane for all AI agents working in this repository. Always load this
file first. It defines which knowledge-base files are required for each task type (routing
table), when to re-read a file (staleness policy), agent responsibilities, and how to handle
conflicts between agents. Every vendor-native auto-loading file references this document.

## Task Routing Table

Load only the files marked ✓ for the current task type. `agents.md` is always required.

| Task Category       | company | marketing | product | security | architecture | engineering | ai-native | agents |
|---------------------|---------|-----------|---------|----------|--------------|-------------|-----------|--------|
| coding              |         |           | ✓       |          | ✓            | ✓           | ✓         | ✓      |
| architecture-review |         |           | ✓       | ✓        | ✓            | ✓           | ✓         | ✓      |
| product-planning    | ✓       | ✓         | ✓       |          |              |             |           | ✓      |
| security-audit      |         |           | ✓       | ✓        | ✓            | ✓           |           | ✓      |

File paths (relative to repo root):
- company → `.specify/memory/company.md`
- marketing → `.specify/memory/marketing.md`
- product → `.specify/memory/product.md`
- security → `.specify/memory/security.md`
- architecture → `.specify/memory/architecture.md`
- engineering → `.specify/memory/engineering.md`
- ai-native → `.specify/memory/ai-native.md`
- agents → `.specify/memory/agents.md` ← this file

## Staleness Policy

Before beginning any task, check the `last-updated` field in the YAML frontmatter of each
required knowledge-base file (per the routing table above). If any file's `last-updated` date
is newer than your session-start date, re-read that file before proceeding.

## Agent Responsibilities

- Load `agents.md` at the start of every session.
- Consult the routing table to determine which additional files are required for the current task.
- Apply the staleness policy before loading any file.
- Follow the standards in the loaded files without deviation unless the user explicitly overrides.
- Do not modify knowledge-base files (`.specify/memory/*.md`) unless the user explicitly invokes a `/prodkit.*` scaffold command.

## File Modification Rules

- Knowledge-base files (`.specify/memory/**`) may only be modified via `/prodkit.*` scaffold commands or by the user directly.
- Vendor-native auto-loading files (`CLAUDE.md`, `.cursorrules`, `GEMINI.md`) may only be regenerated via `/prodkit.agents`.
- Spec files (`specs/**`) may only be modified via `/speckit.*` commands or by the user directly.

## Conflict Resolution Priority

When two or more loaded files contain conflicting guidance, apply this priority order:

1. `security.md` — security constraints always win
2. `engineering.md` — engineering standards apply to all code
3. `ai-native.md` — AI-native principles apply to system design
4. `architecture.md` — architectural decisions apply to structure
5. `product.md` — product scope decisions apply to features
6. `company.md`, `marketing.md` — context and framing only
```

Replace `YYYY-MM-DD` with today's date.

---

## Operation 2 — Generate Vendor-Native Auto-Loading Files

Generate the following three files at the **repository root**. If a file already exists, do NOT overwrite it unless the user has passed `--force` in the command arguments. Report skipped files with "SKIP [filename] (exists — use --force to regenerate)."

### `CLAUDE.md` (Claude Code)

Write to: `CLAUDE.md` at repository root.

```markdown
# Prod-Kit Context — Claude Code

This repository uses Prod-Kit, a vendor-agnostic AI product development framework.
Before beginning any task, load the Prod-Kit knowledge base using the routing rules below.

## Always Load

Read this file before every task:
- `.specify/memory/agents.md` — routing table, staleness policy, agent rules

## Task-Based Context Loading

Consult the Task Routing Table in `.specify/memory/agents.md` to determine which
knowledge-base files are required for the current task. Load only the required files.

Common task types and their required files:
- **Coding tasks**: product.md, architecture.md, engineering.md, ai-native.md
- **Architecture review**: product.md, security.md, architecture.md, engineering.md, ai-native.md
- **Product planning**: company.md, marketing.md, product.md
- **Security audit**: product.md, security.md, architecture.md, engineering.md

All file paths are relative to the repository root under `.specify/memory/`.

## Staleness Check

Before loading any knowledge-base file, check its `last-updated` frontmatter field.
If the date is newer than your session start date, re-read the file.

## Standards

Follow all standards defined in the loaded knowledge-base files. Do not modify
knowledge-base files directly — use `/prodkit.*` scaffold commands.
```

### `.cursorrules` (Cursor)

Write to: `.cursorrules` at repository root.

```markdown
# Prod-Kit Context — Cursor

This repository uses Prod-Kit, a vendor-agnostic AI product development framework.
Before beginning any task, load the Prod-Kit knowledge base using the routing rules below.

## Always Load

Read this file before every task:
- `.specify/memory/agents.md` — routing table, staleness policy, agent rules

## Task-Based Context Loading

Consult the Task Routing Table in `.specify/memory/agents.md` to determine which
knowledge-base files are required for the current task. Load only the required files.

Common task types and their required files:
- **Coding tasks**: product.md, architecture.md, engineering.md, ai-native.md
- **Architecture review**: product.md, security.md, architecture.md, engineering.md, ai-native.md
- **Product planning**: company.md, marketing.md, product.md
- **Security audit**: product.md, security.md, architecture.md, engineering.md

All file paths are relative to the repository root under `.specify/memory/`.

## Staleness Check

Before loading any knowledge-base file, check its `last-updated` frontmatter field.
If the date is newer than your session start date, re-read the file.

## Standards

Follow all standards defined in the loaded knowledge-base files. Do not modify
knowledge-base files directly — use `/prodkit.*` scaffold commands.
```

### `GEMINI.md` (Gemini)

Write to: `GEMINI.md` at repository root.

```markdown
# Prod-Kit Context — Gemini

This repository uses Prod-Kit, a vendor-agnostic AI product development framework.
Before beginning any task, load the Prod-Kit knowledge base using the routing rules below.

## Always Load

Read this file before every task:
- `.specify/memory/agents.md` — routing table, staleness policy, agent rules

## Task-Based Context Loading

Consult the Task Routing Table in `.specify/memory/agents.md` to determine which
knowledge-base files are required for the current task. Load only the required files.

Common task types and their required files:
- **Coding tasks**: product.md, architecture.md, engineering.md, ai-native.md
- **Architecture review**: product.md, security.md, architecture.md, engineering.md, ai-native.md
- **Product planning**: company.md, marketing.md, product.md
- **Security audit**: product.md, security.md, architecture.md, engineering.md

All file paths are relative to the repository root under `.specify/memory/`.

## Staleness Check

Before loading any knowledge-base file, check its `last-updated` frontmatter field.
If the date is newer than your session start date, re-read the file.

## Standards

Follow all standards defined in the loaded knowledge-base files. Do not modify
knowledge-base files directly — use `/prodkit.*` scaffold commands.
```

---

## Post-Write Validation

After both operations, confirm:
1. `.specify/memory/agents.md` exists with all six `##` sections, YAML frontmatter, and routing table with all four task categories and eight files.
2. `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` exist at repo root (or were reported as skipped).
3. Each vendor file contains: always-load instruction, routing instruction, staleness check instruction, standards instruction.
4. No existing content was overwritten without `--force`.
5. Report: files created, files skipped, outcome summary.
