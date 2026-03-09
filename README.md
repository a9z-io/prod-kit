# Prod‑Kit

Prod‑Kit is a **product-definition and delivery framework** built on top of GitHub’s
[Spec‑Kit](https://github.com/github/spec-kit). It preserves Spec‑Kit’s workflow, commands, and
mental model, while layering in structured product thinking so teams can move from
idea → product clarity → execution without losing context.

- **Spec‑Kit answers**: “What are we building?”
- **Prod‑Kit answers**: “Why this product, for whom, and how will we know it worked?”

## Table of Contents

- What you get
- Add Prod‑Kit on top of Spec‑Kit (overlay)
- Build the AI-native knowledge base
- Canonical product artifacts (what to add to your repo)
- Workflow (what changes vs what stays the same)
- Governance
- Upgrading (staying aligned with upstream Spec‑Kit)

## What you get

Prod‑Kit adds:

- A **Product Constitution** concept (durable truths that evolve slowly)
- **Product gates** that make “purpose, scope, KPIs, workflows” first-class alongside specs
- **Traceability** from strategy → product intent → specs → delivery → KPIs
- A recommended **artifact structure** for company, product, competition, KPIs, workflows, roadmap

Prod‑Kit does **not** replace Spec‑Kit phases; it augments them.

## Add Prod‑Kit on top of Spec‑Kit (overlay)

### Prerequisite: initialize Spec‑Kit in your project

In your target repo, install **Specify CLI** (from the Spec‑Kit repo) and initialize Spec‑Kit.

#### Option 1: Persistent install (recommended)

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init . --ai claude
```

To upgrade later:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

#### Option 2: One-time usage (no install)

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init . --ai claude
```

If you already ran `specify init`, you can skip this step.

### Overlay step: copy Prod‑Kit templates and constitution

Copy these files from this `prod-kit` repo into your Spec‑Kit project (same paths):

- `.specify/memory/constitution.md` (Prod‑Kit Constitution; merge if you already have one)
- `.specify/templates/spec-template.md` (adds mandatory **Product Context**)
- `.specify/templates/plan-template.md` (adds **Constitution Check** gates)
- `.specify/templates/tasks-template.md` (adds KPI instrumentation guidance)
- `.claude/commands/*.md` (optional; only if you want the command guidance alongside Claude)

After the overlay, your existing Spec‑Kit commands remain the same (`/speckit.*`), but the templates
and gates will now require product context and traceability.

## Build the AI-native knowledge base

Once the overlay is applied, Prod‑Kit ships ten `/prodkit.*` commands. Each one scaffolds a
structured, agent-optimized Markdown file in your repo — with YAML frontmatter, a mandatory
`## Agent Summary` section (≤150 words for fast agent loading), and all required domain sections.
All commands are **idempotent**: safe to re-run; existing content is never overwritten.

### Step 1 — Scaffold the knowledge base

```text
/prodkit.company       →  .specify/memory/company.md
/prodkit.marketing     →  .specify/memory/marketing.md
/prodkit.product       →  .specify/memory/product.md
/prodkit.security      →  .specify/memory/security.md
/prodkit.architecture  →  .specify/memory/architecture.md
/prodkit.engineering   →  .specify/memory/engineering.md
/prodkit.ai-native     →  .specify/memory/ai-native.md
/prodkit.agents        →  .specify/memory/agents.md  (+ vendor auto-loaders, see Step 2)
/prodkit.roadmap       →  .specify/memory/roadmap/roadmap.md
```

Fill in your team's specifics in each file. At minimum, complete the `## Agent Summary`
section so agents can route intelligently.

### Step 2 — Configure vendor-native auto-loading

Running `/prodkit.agents` also generates three files at your **repo root** that each vendor's
agent reads automatically at session start — zero manual context injection required per session:

| File | Vendor |
|------|--------|
| `CLAUDE.md` | Claude Code |
| `.cursorrules` | Cursor |
| `GEMINI.md` | Gemini |

Each file always loads `agents.md` (the routing table) and instructs the agent to load only
the knowledge-base files relevant to the current task type (`coding`, `architecture-review`,
`product-planning`, `security-audit`).

### Step 3 — Generate architecture artifacts

```text
/prodkit.dataflowdiagram   →  .specify/memory/architecture/dataflow-[name].md
```

Describe your services and data flows; the command generates a machine-readable artifact with
a `## Services` section and `## Data Flows` table that agents use for architecture review.

### Task routing (agents load only what they need)

`agents.md` contains a routing table so agents never load the full knowledge base when only a
subset is needed. The table ships pre-configured:

| Task type | Files loaded |
|---|---|
| `coding` | product, architecture, engineering, ai-native, agents |
| `architecture-review` | product, security, architecture, engineering, ai-native, agents |
| `product-planning` | company, marketing, product, agents |
| `security-audit` | product, security, architecture, engineering, agents |

See the full quickstart: [`specs/002-ai-native-framework/quickstart.md`](specs/002-ai-native-framework/quickstart.md)

---

## Canonical product artifacts (what to add to your repo)

Prod‑Kit expects a product-definition layer alongside feature specs. Default structure:

```text
company/
  profile.md              # company identity, vision, mission, strategic goals

product/
  constitution.md         # durable product truths (vision, ICP, value, success metrics)

competition/
  landscape.md            # competitors, differentiation, positioning notes

kpis/
  kpis.md                 # KPI definitions (activation/engagement/retention/expansion/TTV)
  dashboard.md            # dashboard link + ownership + review cadence (if applicable)

workflows/
  users.md                # personas, roles/permissions
  workflows.md            # 2–3 primary workflows + key edge cases
  technical-workflows.md  # system interactions/data flows/auth/permissions (when needed)

roadmap/
  roadmap.md              # outcome-based milestones, dependencies, trade-offs
```

Minimum viable setup to start using Prod‑Kit:

- `product/constitution.md`
- `kpis/kpis.md`
- `workflows/workflows.md`

## Quickstart: first product with Prod‑Kit

1. Create (or draft) your durable product truths:

   - `product/constitution.md`
   - `kpis/kpis.md`
   - `workflows/workflows.md`

2. Establish project governance (this repo’s constitution drives the gates):

```text
/speckit.constitution
```

3. Create your first spec (now includes mandatory Product Context):

```text
/speckit.specify <describe the feature in plain language>
```

4. Continue with the normal Spec‑Kit flow:

```text
/speckit.plan <tech stack + constraints>
/speckit.tasks
/speckit.implement
```

## Workflow (what changes vs what stays the same)

- **Clarify (augmented)**: you MUST make purpose explicit (who/why/why now/success) and record any
  new durable truths into the Product Constitution.
- **Specify (enhanced)**: specs MUST include Product Context + bounded scope + link to KPIs/workflows.
- **Plan (gated)**: plans MUST pass the Constitution Check (product constitution exists, traceability,
  instrumentation decision recorded).
- **Tasks (traceable)**: tasks remain grouped by user story and MUST include KPI instrumentation tasks
  (or explicit deferral + trigger).

## Governance

The non‑negotiable principles and required artifacts live in:

- `.specify/memory/constitution.md` (Prod‑Kit Constitution)

If you change templates/gates, update the constitution and keep them in sync.

## Upgrading (staying aligned with upstream Spec‑Kit)

Prod‑Kit is an overlay. Upgrades happen in **two layers**:

1) Upgrade **Spec‑Kit / Specify CLI** (upstream)
2) Re-apply/upgrade the **Prod‑Kit overlay file set**

### Upgrade Specify CLI (Spec‑Kit)

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

### Upgrade Spec‑Kit templates/commands in your repo

In a branch, refresh upstream Spec‑Kit templates (this may overwrite local edits):

```bash
specify init . --force --ai claude
```

Then re-apply the Prod‑Kit overlay file set (next section).

### Upgrade the Prod‑Kit overlay (this repo)

#### Option 1: Apply via `uv` (no manual copying)

One-time (recommended for upgrades):

```bash
uvx --from git+https://github.com/3leches/prod-kit.git prodkit overlay --force
```

Persistent install:

```bash
uv tool install prod-kit --from git+https://github.com/3leches/prod-kit.git
prodkit overlay --force
```

If the repo is private (or your environment can’t prompt for credentials) and you see an error like
`could not read Username for 'https://github.com': terminal prompts disabled`, use SSH instead:

```bash
uvx --from git+ssh://git@github.com/3leches/prod-kit.git prodkit overlay --force
```

```bash
uv tool install prod-kit --from git+ssh://git@github.com/3leches/prod-kit.git
prodkit overlay --force
```

Alternatively, authenticate HTTPS via a token (avoid putting tokens in shell history):

```bash
GITHUB_TOKEN=... uv tool install prod-kit --from "git+https://$GITHUB_TOKEN@github.com/3leches/prod-kit.git"
```

By default, `prodkit overlay` **skips** `.specify/memory/constitution.md` if it already exists (so
you can merge manually). To overwrite it (dangerous):

```bash
prodkit overlay --force --force-constitution
```

To also apply the optional agent guidance docs:

```bash
prodkit overlay --force --with-claude-commands
```

#### Option 2: Copy/merge files manually

Re-apply/merge these overlay files into your Spec‑Kit project (same paths):

- `.specify/memory/constitution.md` (merge; keep your product-specific content)
- `.specify/templates/spec-template.md`
- `.specify/templates/plan-template.md`
- `.specify/templates/tasks-template.md`

Optional:

- `.claude/commands/*.md`

If you’ve customized templates, upgrade by **merging** (not overwriting) and keep a small diff so
future upgrades are repeatable.

### Post-upgrade validation checklist

Validate that Prod‑Kit gates are still present:

- `/.specify/templates/spec-template.md` still contains mandatory **Product Context**
- `/.specify/templates/plan-template.md` still contains the **Constitution Check** gates
- `/.specify/templates/tasks-template.md` still prompts for KPI instrumentation vs explicit deferral

