# /prodkit.company

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/company.md` — the canonical company identity knowledge-base file. If the file already exists, add only missing sections (preserve all existing content). Output is agent-optimized: YAML frontmatter + `## Agent Summary` + structured domain sections.

## Target File

`.specify/memory/company.md`

## Idempotency Rule

Before writing, check whether `.specify/memory/company.md` exists.
- **Does not exist** → create the full file using the schema below.
- **Exists** → read the file, identify which `##` sections are missing, and append only the missing sections. Do NOT modify any existing content. Report which sections were added (or "nothing to add" if all sections already present).

## File Schema

Write the following content (replacing `[stub]` markers with short placeholder text that prompts the user to fill in their specifics):

```markdown
---
file: company.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [product-planning]
---

## Agent Summary

[Fill in ≤150 words: describe this company's identity, its mission, and the two or three most critical strategic facts an AI agent needs before working on any product-planning task. Answer: what does this company do, who does it serve, and what are its 1–3 overriding strategic goals?]

## Vision

[The long-term aspirational outcome the company exists to achieve. One to two sentences.]

## Mission

[The day-to-day purpose — what the company does and for whom. One to two sentences.]

## Core Values

[List 3–6 principles that guide decision-making internally and externally.]

- [Value 1]: [brief description]
- [Value 2]: [brief description]
- [Value 3]: [brief description]

## Strategic Goals

[The 12–36 month outcomes the company is pursuing. Link to product and roadmap where applicable.]

- [Goal 1]
- [Goal 2]
- [Goal 3]

## Target Customers

[Who the company serves. Describe the primary customer segment(s) — industry, company size, role, and key pain point addressed.]
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter is present and contains all four required fields.
2. `## Agent Summary` is the first section after frontmatter and is ≤150 words (stub text is fine — the user will fill it in).
3. All five domain sections (`## Vision`, `## Mission`, `## Core Values`, `## Strategic Goals`, `## Target Customers`) are present.
4. No existing content was overwritten (if file previously existed).
5. Report: "`.specify/memory/company.md` created" or "`.specify/memory/company.md` updated — added: [section list]" or "`.specify/memory/company.md` — nothing to add."
