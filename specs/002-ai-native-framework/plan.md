# Implementation Plan: AI-Native Product Development Framework

**Branch**: `002-ai-native-framework` | **Date**: 2026-02-08 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-ai-native-framework/spec.md`

## Summary

Deliver ten new `/prodkit.*` slash commands that scaffold a vendor-agnostic, agent-optimized knowledge base inside any Spec-Kit + Prod-Kit repository. Each command creates or updates a structured Markdown file with YAML frontmatter, a mandatory `## Agent Summary` section, and domain-specific content sections. A dedicated `/prodkit.agents` command generates vendor-native auto-loading files (`CLAUDE.md`, `.cursorrules`, `GEMINI.md`) that inject the right knowledge-base files into each AI agent's context automatically — with zero user action per session and a built-in staleness policy.

All deliverables are Markdown files (command definitions + knowledge-base templates). No runtime code is introduced beyond what the overlay CLI already ships.

## Technical Context

**Language/Version**: Markdown (command definitions and knowledge-base templates); YAML (frontmatter within Markdown files)
**Primary Dependencies**: None — plain-text files consumed by Cursor slash-command engine and AI agents
**Storage**: Repository files tracked in Git; canonical paths under `.specify/memory/`, `.specify/memory/workflows/`, `.specify/memory/competition/`, `.specify/memory/kpis/`, `.specify/memory/roadmap/`, and `agent-config/`
**Testing**: Manual validation — run each `/prodkit.*` command in a test repo and verify file creation, idempotency, and agent context loading
**Target Platform**: Any Git repository with Prod-Kit overlay applied; AI agents: Claude Code, Cursor, Gemini
**Performance Goals**: Each scaffold command completes within a single AI response turn; full knowledge-base setup under 30 minutes (SC-001)
**Constraints**: All files plain-text Markdown; YAML frontmatter at file top; `## Agent Summary` ≤150 words; no vendor-proprietary binary formats
**Scale/Scope**: 10 new command files; ~12 knowledge-base template files; 3 vendor-native auto-loading file templates

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Product Constitution exists**: Spec links to `.specify/memory/constitution.md` ✅
- [x] **Purpose is explicit**: ICP (engineering leads + product engineers using AI agents daily), problem (agents start from zero each session), value (consistent product-aligned output across vendors), KPIs (Time-to-value, Activation, Engagement, Retention) — all explicitly stated ✅
- [x] **Scope is bounded**: Clarifications section bounds vendor scope (Claude/Cursor/Gemini only), MCP implementation (standards only, no MCP server), and command delivery (slash-commands, no standalone CLI) ✅
- [x] **Traceability**: Spec references KPIs (Time-to-value, Activation, Engagement, Retention); commands will link to user workflows; architecture artifacts will link to technical-workflows ✅
- [x] **Augmentation, not replacement**: All ten `/prodkit.*` commands are new additions layered on top of existing Spec-Kit phases. No Spec-Kit command files are modified ✅
- [x] **Instrumentation decision recorded**: SC-002 (90% sessions consistent) and SC-005 (50% manual context reduction) are user-side metrics requiring post-launch user research. **Deferred**: measurement via voluntary team survey at 30-day cohort mark. Trigger: first five teams complete full knowledge-base setup. SC-001 (30-minute setup) and SC-003 (idempotency) are testable at delivery ✅

*Constitution Check passed. Proceeding to Phase 0.*

## Project Structure

### Documentation (this feature)

```text
specs/002-ai-native-framework/
├── plan.md              ← this file
├── research.md          ← Phase 0 output
├── data-model.md        ← Phase 1 output
├── quickstart.md        ← Phase 1 output
├── contracts/           ← Phase 1 output (file schemas)
└── tasks.md             ← Phase 2 output (/speckit.tasks)
```

### Source Files (repository root)

This feature delivers documentation and command files only — no application source code.

```text
.claude/commands/
├── prodkit.company.md          ← scaffold company.md
├── prodkit.product.md          ← scaffold product.md
├── prodkit.marketing.md        ← scaffold marketing.md
├── prodkit.security.md         ← scaffold security.md
├── prodkit.architecture.md     ← scaffold architecture.md
├── prodkit.engineering.md      ← scaffold engineering.md
├── prodkit.ai-native.md        ← scaffold ai-native.md
├── prodkit.agents.md           ← generate CLAUDE.md / .cursorrules / GEMINI.md
├── prodkit.dataflowdiagram.md  ← generate dataflow artifact
└── prodkit.roadmap.md          ← scaffold roadmap.md

.specify/memory/
├── company.md                  ← knowledge-base file (scaffolded by /prodkit.company)
├── marketing.md                ← knowledge-base file (scaffolded by /prodkit.marketing)
├── product.md                  ← knowledge-base file (scaffolded by /prodkit.product)
├── security.md                 ← knowledge-base file (scaffolded by /prodkit.security)
├── architecture.md             ← knowledge-base file (scaffolded by /prodkit.architecture)
├── engineering.md              ← knowledge-base file (scaffolded by /prodkit.engineering)
├── ai-native.md                ← knowledge-base file (scaffolded by /prodkit.ai-native)
├── agents.md                   ← routing table + staleness policy (scaffolded by /prodkit.agents)
├── kpis/kpis.md                ← KPI definitions
├── workflows/users.md          ← personas
├── workflows/workflows.md      ← critical workflows
├── competition/landscape.md    ← competitive landscape
└── roadmap/roadmap.md          ← outcome milestones (scaffolded by /prodkit.roadmap)

agent-config/
├── CLAUDE.md                   ← vendor-native auto-loader for Claude Code (at repo root)
├── .cursorrules                ← vendor-native auto-loader for Cursor (at repo root)
└── GEMINI.md                   ← vendor-native auto-loader for Gemini (at repo root)

src/prodkit/overlay/claude/commands/
└── (mirror of .claude/commands/prodkit.*.md — bundled for CLI deployment)
```

**Structure Decision**: Documentation-only feature using existing Prod-Kit overlay pattern. Command files go in `.claude/commands/` and are mirrored in `src/prodkit/overlay/claude/commands/` so they are deployed when users run `prodkit overlay`. No traditional application source code is introduced.

## Complexity Tracking

> No constitution violations. Table not required.
