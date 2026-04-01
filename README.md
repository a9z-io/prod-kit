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
- Skills reference
- Mixing skills: end-to-end workflows
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
/prodkit.dataflow   →  .specify/memory/architecture/dataflow-[name].md
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

## Skills reference

Skills are Claude Code slash commands with full instruction sets. They are deployed into your
repo via `prodkit overlay --with-claude-skills` and become available as `/skill-name` in Claude Code.

### Spec‑Kit skills (from upstream)

| Skill | Command | What it does |
|-------|---------|-------------|
| `speckit-specify` | `/speckit.specify <description>` | Create or update a feature spec from plain-language description |
| `speckit-clarify` | `/speckit.clarify` | Ask up to 5 targeted clarification questions and encode answers into the spec |
| `speckit-plan` | `/speckit.plan <tech stack>` | Generate a technical implementation plan from the spec |
| `speckit-tasks` | `/speckit.tasks` | Break the plan into an ordered, dependency-aware task list |
| `speckit-implement` | `/speckit.implement` | Execute all tasks in `tasks.md` following TDD where applicable |
| `speckit-analyze` | `/speckit.analyze` | Cross-artifact consistency check across spec, plan, and tasks |
| `speckit-checklist` | `/speckit.checklist` | Generate a custom quality checklist for the current feature |
| `speckit-constitution` | `/speckit.constitution` | Create or update the project constitution |
| `speckit-taskstoissues` | `/speckit.taskstoissues` | Convert tasks into GitHub issues |

### Prod‑Kit skills

| Skill | Command | What it does |
|-------|---------|-------------|
| `prodkit-ghflow` | `/prodkit.ghflow [context]` | Full GitHub workflow: branch → stage → commit → push → PR, with confirmation at every step |

### `/prodkit.ghflow` — GitHub workflow skill

The `ghflow` skill walks through the complete branch-to-PR loop interactively.

**Basic usage — commit and PR what you have:**
```text
/prodkit.ghflow
```

**With a context hint (used to name the branch and commit):**
```text
/prodkit.ghflow fix checkout timeout on mobile
```

**With a ticket reference:**
```text
/prodkit.ghflow PROJ-42 add dark mode toggle
```

**What happens at each step:**

| Step | Action | Requires approval? |
|------|--------|--------------------|
| 1 | Inspect `git status`, `git diff`, current branch | No |
| 2 | Propose branch name (or skip if already on a feature branch) | Yes |
| 3 | Stage changes (`git add -A` or manually) | Yes |
| 4 | Propose conventional commit message | Yes |
| 5 | Commit | Yes |
| 6 | Push to origin | Yes |
| 7 | Propose PR title + body, create via `gh pr create` | Yes |

At every approval step you can accept, edit, or cancel — no action is taken without a confirmed response.

**Requirements:** `git` and `gh` CLI (authenticated). If `gh` is missing, the skill completes through push and provides manual PR instructions.

---

## Mixing skills: end-to-end workflows

Skills compose naturally. Here are common patterns that combine `/speckit.*`, `/prodkit.*`, and `/prodkit.ghflow`.

### Pattern 1 — Full feature from idea to PR

The complete spec-driven development loop, ending with a PR:

```text
# 1. Describe the feature — creates branch + spec.md
/speckit.specify add a CSV export button to the reports page

# 2. Clarify any ambiguities in the spec
/speckit.clarify

# 3. Generate a technical plan
/speckit.plan TypeScript, Next.js, Prisma

# 4. Break the plan into tasks
/speckit.tasks

# 5. Implement all tasks
/speckit.implement

# 6. Commit the implementation and open a PR
/prodkit.ghflow feat/csv-export — ready for review
```

### Pattern 2 — Quick fix to PR (no spec needed)

For small bugs or chores where a full spec is overkill:

```text
# Make your code changes, then:
/prodkit.ghflow fix null pointer in user settings page
```

The skill inspects the diff, proposes a branch name and commit message, and walks you through to a PR in one command.

### Pattern 3 — Spec + analysis quality gate before shipping

Add a consistency check before committing:

```text
/speckit.specify redesign the onboarding flow
/speckit.plan React, Node.js
/speckit.tasks
/speckit.analyze          ← catches gaps between spec, plan, and tasks
/speckit.implement
/prodkit.ghflow           ← branch + commit + PR
```

### Pattern 4 — Tasks to GitHub issues + PR

When you want GitHub issues tracking each task alongside a PR:

```text
/speckit.specify integrate Stripe billing
/speckit.plan
/speckit.tasks
/speckit.taskstoissues    ← creates a GitHub issue per task
/speckit.implement
/prodkit.ghflow integrate Stripe billing — closes #12 #13 #14
```

### Pattern 5 — Scaffold knowledge base then ship

Set up a new repo's AI context and commit it in one session:

```text
/prodkit.company
/prodkit.product
/prodkit.engineering
/prodkit.architecture
/prodkit.agents           ← generates CLAUDE.md, .cursorrules, GEMINI.md
/prodkit.ghflow chore: scaffold prod-kit knowledge base
```

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

Source repository: `https://github.com/a9z-io/prod-kit`

Default path (recommended):

```bash
uvx --from git+https://github.com/a9z-io/prod-kit.git prodkit overlay --force --with-claude-commands --with-claude-skills
```

Persistent install:

```bash
uv tool install prod-kit --from git+https://github.com/a9z-io/prod-kit.git
prodkit overlay --force --with-claude-commands --with-claude-skills
```

Fallback: SSH source (use when HTTPS auth prompts are blocked):

```bash
uvx --from git+ssh://git@github.com/a9z-io/prod-kit.git prodkit overlay --force --with-claude-commands --with-claude-skills
```

```bash
uv tool install prod-kit --from git+ssh://git@github.com/a9z-io/prod-kit.git
prodkit overlay --force --with-claude-commands --with-claude-skills
```

Fallback: HTTPS token auth (avoid putting tokens in shell history):

```bash
GITHUB_TOKEN=... uv tool install prod-kit --from "git+https://$GITHUB_TOKEN@github.com/a9z-io/prod-kit.git"
prodkit overlay --force --with-claude-commands --with-claude-skills
```

By default, `prodkit overlay` **skips** `.specify/memory/constitution.md` if it already exists (so
you can merge manually). To overwrite it (dangerous):

```bash
prodkit overlay --force --force-constitution
```

Default overlay behavior in this README:

```bash
prodkit overlay --force --with-claude-commands --with-claude-skills
```

Optional: commands only:

```bash
prodkit overlay --force --with-claude-commands
```

Optional: skills only:

```bash
prodkit overlay --force --with-claude-skills
```

#### Option 2: Copy/merge files manually

Re-apply/merge these overlay files into your Spec‑Kit project (same paths):

- `.specify/memory/constitution.md` (merge; keep your product-specific content)
- `.specify/templates/spec-template.md`
- `.specify/templates/plan-template.md`
- `.specify/templates/tasks-template.md`

Optional:

- `.claude/commands/*.md`
- `.claude/skills/*/SKILL.md`

If you’ve customized templates, upgrade by **merging** (not overwriting) and keep a small diff so
future upgrades are repeatable.

### Post-upgrade validation checklist

Validate that Prod‑Kit gates are still present:

- `/.specify/templates/spec-template.md` still contains mandatory **Product Context**
- `/.specify/templates/plan-template.md` still contains the **Constitution Check** gates
- `/.specify/templates/tasks-template.md` still prompts for KPI instrumentation vs explicit deferral

