# /prodkit.roadmap

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/roadmap/roadmap.md` — the canonical outcome-based product roadmap. Milestones are aligned to product outcomes and KPIs, not feature lists. If the file already exists, add only missing sections.

## Target File

`.specify/memory/roadmap/roadmap.md`

## Idempotency Rule

- **Does not exist** → create the directory `.specify/memory/roadmap/` if needed, then create the file using the schema below.
- **Exists** → read, identify missing `##` sections, append only missing sections. Do NOT modify existing content. Report added sections or "nothing to add."

## File Schema

```markdown
---
file: roadmap.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [product-planning]
---

## Agent Summary

[Fill in ≤150 words: describe the current state of the roadmap. What are the 2–3 most critical
roadmap facts an agent needs for product-planning tasks? Include: the current milestone, the
primary outcome it targets, and the most important trade-off or dependency the team is managing.]

## Current Milestone

[Name and description of the milestone currently in progress.]

**Name**: [milestone name]
**Target outcome**: [the user or business outcome this milestone achieves — NOT a feature list]
**Target KPIs**: [which KPIs from `product.md` this milestone is intended to move]
**Target date**: [YYYY-MM-DD or quarter]
**Status**: [In progress / At risk / On track]

### Scope

[What is included in this milestone. Frame as capabilities or outcomes, not individual features.]

- [capability/outcome 1]
- [capability/outcome 2]

### Out of Scope

[What is explicitly deferred from this milestone.]

- [deferred item 1]
- [deferred item 2]

## Next Milestone

[Name and brief description of the milestone following the current one.]

**Name**: [milestone name]
**Target outcome**: [outcome — not a feature list]
**Target KPIs**: [KPIs this milestone moves]
**Dependencies**: [what must be true before this milestone can start]

## Future Bets

[Directional bets beyond the next milestone. Speculative — subject to change based on learnings.]

- **[Bet name]**: [one sentence on the outcome targeted and why it matters]
- **[Bet name]**: [one sentence]

## Trade-offs

[Explicit trade-offs the team has made in building this roadmap. Each trade-off should state what was chosen, what was deprioritized, and why.]

| Decision | What we chose | What we deprioritized | Rationale |
|----------|--------------|----------------------|-----------|
| [topic]  | [chosen path] | [deferred path] | [1–2 sentence rationale] |

## Dependencies

[External dependencies that could affect the roadmap — partner timelines, platform changes, compliance deadlines, etc.]

- **[Dependency]**: [what it is, which milestone it affects, current status]

## Milestones Archive

[Completed milestones with outcomes achieved. Add entries here as milestones close.]

| Milestone | Completed | Outcome achieved | KPI impact |
|-----------|-----------|-----------------|------------|
| [name] | [date] | [actual outcome] | [measured impact] |
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All seven sections present: Current Milestone, Next Milestone, Future Bets, Trade-offs, Dependencies, Milestones Archive.
4. Current Milestone and Next Milestone each express outcomes (not feature lists).
5. No existing content overwritten.
6. Report outcome.
