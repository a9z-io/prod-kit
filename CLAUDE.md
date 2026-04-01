# prod-kit Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-01

## Active Technologies
- Markdown + YAML frontmatter (same as all prod-kit artifacts) + `git` (fetch, rebase, symbolic-ref, rev-list) — already required by the skill (003-ghflow-rebase-main)
- N/A — file-level edit to `SKILL.md` (003-ghflow-rebase-main)
- Markdown command/skill specifications + Mermaid text outpu + Existing slash-command workflow in `.claude/commands/`; existing skill system in `.claude/skills/` (create-diagram-skill)
- Repository files (`.claude/commands/*`, `.claude/skills/*`) and generated diagram artifact files colocated with source outputs (create-diagram-skill)
- Bash shell scripts and Markdown workflow docs + Existing Speckit scripts in `.specify/scripts/bash/` (`create-new-feature.sh`, `common.sh`, prerequisite/setup scripts) (004-fix-spec-indexing)
- Local repository file system (`specs/` directory names, generated spec files, branch names) (004-fix-spec-indexing)

- Markdown (command definitions and knowledge-base templates); YAML (frontmatter within Markdown files) + None — plain-text files consumed by Cursor slash-command engine and AI agents (002-ai-native-framework)

## Project Structure

```text
src/
tests/
```

## Commands

# Add commands for Markdown (command definitions and knowledge-base templates); YAML (frontmatter within Markdown files)

## Code Style

Markdown (command definitions and knowledge-base templates); YAML (frontmatter within Markdown files): Follow standard conventions

## Recent Changes
- 004-fix-spec-indexing: Added Bash shell scripts and Markdown workflow docs + Existing Speckit scripts in `.specify/scripts/bash/` (`create-new-feature.sh`, `common.sh`, prerequisite/setup scripts)
- create-diagram-skill: Added Markdown command/skill specifications + Mermaid text outpu + Existing slash-command workflow in `.claude/commands/`; existing skill system in `.claude/skills/`
- 003-ghflow-rebase-main: Added Markdown + YAML frontmatter (same as all prod-kit artifacts) + `git` (fetch, rebase, symbolic-ref, rev-list) — already required by the skill


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
