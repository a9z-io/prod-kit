# /prodkit.marketing

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/marketing.md` — the canonical marketing and positioning knowledge-base file. If the file already exists, add only missing sections (preserve all existing content).

## Target File

`.specify/memory/marketing.md`

## Idempotency Rule

Before writing, check whether `.specify/memory/marketing.md` exists.
- **Does not exist** → create the full file using the schema below.
- **Exists** → read the file, identify which `##` sections are missing, and append only the missing sections. Do NOT modify any existing content. Report which sections were added (or "nothing to add" if all sections already present).

## File Schema

```markdown
---
file: marketing.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [product-planning]
---

## Agent Summary

[Fill in ≤150 words: describe this product's market position and the two or three most critical messaging facts an AI agent needs before working on any product-planning task. Answer: how does this company position itself, who is its ideal customer, and what is the core value proposition?]

## Branding

[Brand identity: name, visual language principles, tone of voice, and brand personality. Describe what the brand should feel like to customers.]

## Positioning

[How the company is positioned in the market relative to alternatives. Complete this statement: "For [target customer], [company] is the [category] that [key benefit] because [reason to believe]."]

## Messaging

[Core messaging pillars — the 2–4 key messages used consistently across all customer-facing communication.]

- [Message 1]: [one sentence]
- [Message 2]: [one sentence]
- [Message 3]: [one sentence]

## Ideal Customer Profile (ICP)

[Detailed description of the ideal customer.]

- **Industry**: [primary industries]
- **Company size**: [employee range or revenue range]
- **Primary role / buyer**: [job title(s) of decision-maker]
- **Primary role / user**: [job title(s) of end user, if different]
- **Key pain point**: [the problem they experience that this product solves]
- **Trigger event**: [what causes them to seek a solution now]

## Value Propositions

[The distinct outcomes customers get from this product. List 3–5 concrete, customer-language value propositions.]

- [Value prop 1]
- [Value prop 2]
- [Value prop 3]
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All five domain sections present: `## Branding`, `## Positioning`, `## Messaging`, `## Ideal Customer Profile (ICP)`, `## Value Propositions`.
4. No existing content overwritten.
5. Report outcome.
