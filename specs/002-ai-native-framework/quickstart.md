# Quickstart: AI-Native Product Development Framework

**Feature**: `002-ai-native-framework`
**Date**: 2026-02-08

This guide shows how to set up a complete agent-optimized knowledge base in a Prod-Kit repository using the new `/prodkit.*` commands.

## Prerequisites

- Spec-Kit installed in your repo
- Prod-Kit overlay applied (`prodkit overlay` — see [README](../../README.md))

---

## Step 1 — Scaffold the Knowledge Base (P1)

Run each scaffold command once. Each creates a structured Markdown file with YAML frontmatter, an `## Agent Summary` stub, and all required sections. If a file already exists, only missing sections are added.

```
/prodkit.company       → .specify/memory/company.md
/prodkit.marketing     → .specify/memory/marketing.md
/prodkit.product       → .specify/memory/product.md
/prodkit.security      → .specify/memory/security.md
/prodkit.architecture  → .specify/memory/architecture.md
/prodkit.engineering   → .specify/memory/engineering.md
/prodkit.ai-native     → .specify/memory/ai-native.md
/prodkit.agents        → .specify/memory/agents.md  (+ vendor-native files, see Step 3)
/prodkit.roadmap       → .specify/memory/roadmap/roadmap.md
```

Fill in your team's specifics in each file. At minimum, complete the `## Agent Summary` section for each file so agents can route intelligently.

---

## Step 2 — Fill in the `## Agent Summary` Sections

Each generated file contains an `## Agent Summary` stub. This is the section agents read first — keep it under 150 words and answer:

1. What domain does this file cover?
2. Two or three most critical facts for any agent task
3. Which sections have depth for specific task types

**Example — `engineering.md` Agent Summary:**

```markdown
## Agent Summary

This file defines engineering standards for this repository. Agents working on
any coding task should follow the Git workflow (feature branches, PR required),
use the approved dependency list in the Package Management section, and apply
the coding style rules before generating code. Architecture decisions require
following the ADR process in the Code Review Standards section. This codebase
uses TypeScript + Node.js; see Frameworks for approved libraries.
```

---

## Step 3 — Configure Vendor-Native Auto-Loading (P2)

`/prodkit.agents` generates three files at the repo root that each vendor's agent reads automatically at session start:

| File | Vendor | Placement |
|------|--------|-----------|
| `CLAUDE.md` | Claude Code | Repo root |
| `.cursorrules` | Cursor | Repo root |
| `GEMINI.md` | Gemini | Repo root |

Each file:
- Always loads `agents.md` (routing table + staleness policy)
- Instructs the agent to consult the task routing table and load only the files required for the current task type
- Instructs the agent to check `last-updated` frontmatter before loading any file

After running `/prodkit.agents`, commit all three files. From that point forward, every new agent session automatically picks up Prod-Kit context — no manual action needed.

---

## Step 4 — Generate Architecture Artifacts (P3)

```
/prodkit.architecture                    → scaffold architecture.md
/prodkit.dataflowdiagram [description]   → generate dataflow artifact
```

For `/prodkit.dataflowdiagram`, describe your services and the data flowing between them. The command generates a structured artifact at `.specify/memory/architecture/dataflow-[name].md` with a `## Services` section and a `## Data Flows` table.

---

## Step 5 — Define AI-Native Standards (P4)

```
/prodkit.ai-native     → .specify/memory/ai-native.md
```

This scaffolds `ai-native.md` with all seven AI-native principles (AI-Readable Systems, MCP Interoperability, Explicit Workflow Modeling, Structured Data Contracts, Deterministic Interfaces, Observability for Agents, AI Discoverability) and inserts a cross-reference into `engineering.md`.

---

## Upgrading the Knowledge Base

When content changes (new services, updated engineering standards, etc.):

1. Edit the relevant knowledge-base file directly
2. Update `version` (bump MINOR for meaningful content changes, PATCH for corrections) and `last-updated` in the frontmatter
3. Update the `## Agent Summary` if key facts changed
4. Commit — agents will detect `last-updated` newer than session start and re-read automatically

---

## Validation Checklist

After initial setup, verify:

- [ ] All eight core files exist under `.specify/memory/`
- [ ] Every file has YAML frontmatter with all four required fields
- [ ] Every file has a completed `## Agent Summary` (no stub text remaining)
- [ ] `agents.md` routing table has all four task categories and correct file assignments
- [ ] `CLAUDE.md`, `.cursorrules`, and `GEMINI.md` exist at repo root
- [ ] Opening a new Cursor session shows Prod-Kit context loaded automatically
