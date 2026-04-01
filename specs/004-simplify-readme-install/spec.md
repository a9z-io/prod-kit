# Feature Specification: Simplify README Install Instructions

**Feature Branch**: `004-simplify-readme-install`  
**Created**: 2026-04-01  
**Status**: Implemented  
**Input**: User description: "update readme file and simplify instructions since git repo is no longer: git+https://github.com/3leches/prod-kit.git prodkit and is instead https://github.com/a9z-io/prod-kit . i want it to be really easy for users to read, understand and use. the default install command should also add both at once: prodkit overlay --force --with-claude-commands --with-claude-skills"

## Product Context *(mandatory)*

- **Product Constitution**: `CLAUDE.md` in repository root
- **ICP / User**: New and existing prod-kit users onboarding from README documentation
- **Problem / Value**: The README currently includes legacy repository references and more complex upgrade paths, which can confuse users and increase setup friction. This feature simplifies instructions and standardizes the default install flow.
- **Primary KPIs impacted**: Activation, Time-to-value, Retention

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Install from Correct Repository Quickly (Priority: P1)

A new user reads the README and runs the correct install command using the current `a9z-io/prod-kit` repository source.

**Why this priority**: Correct source URL and copy-paste-safe commands are the minimum requirement for successful onboarding.

**Independent Test**: Follow the updated README from a clean shell session and verify installation commands reference `a9z-io/prod-kit` and execute without using deprecated repository URLs.

**Acceptance Scenarios**:

1. **Given** a user on the README installation section, **When** they copy the default install command, **Then** it references `https://github.com/a9z-io/prod-kit` (or equivalent git URL form for that repo).
2. **Given** a user searching for old repository references, **When** they read installation guidance, **Then** legacy `3leches/prod-kit` install URLs are not presented as the active default path.

---

### User Story 2 - Run One Default Overlay Command for Both Add-ons (Priority: P2)

A user can apply the default overlay in one command that includes both Claude commands and Claude skills.

**Why this priority**: Reduces cognitive load and avoids partial setup states.

**Independent Test**: Execute the documented default overlay command and verify it includes both `--with-claude-commands` and `--with-claude-skills`.

**Acceptance Scenarios**:

1. **Given** a user following the default overlay path, **When** they run the command from README, **Then** the command includes `prodkit overlay --force --with-claude-commands --with-claude-skills`.

---

### User Story 3 - Understand Setup Steps Without Ambiguity (Priority: P3)

A user can quickly understand which commands are default, optional, and fallback.

**Why this priority**: Clear structure prevents decision paralysis and setup mistakes.

**Independent Test**: Read the updated README sections and verify defaults are clearly labeled, optional variants are concise, and the sequence is easy to follow.

**Acceptance Scenarios**:

1. **Given** a user reading setup instructions, **When** they scan the section headings and command blocks, **Then** they can distinguish default command path from optional alternatives in under one pass.

---

### Edge Cases

- Users copy commands from cached/outdated documentation snapshots.
- Users need SSH-based install examples due to restricted HTTPS authentication environments.
- README still contains old URLs in non-install sections that could be mistaken for active defaults.
- Users run only one add-on flag and expect both commands and skills to be installed.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The README installation instructions MUST use the `a9z-io/prod-kit` repository as the active default source.
- **FR-002**: The README MUST remove or clearly de-prioritize legacy install commands targeting `3leches/prod-kit`.
- **FR-003**: The README default overlay command MUST include both `--with-claude-commands` and `--with-claude-skills`.
- **FR-004**: The README MUST present a clear primary install path before optional alternatives.
- **FR-005**: The README MUST preserve at least one fallback install path for users with authentication or protocol constraints.
- **FR-006**: The README MUST keep command examples copy-paste-ready with minimal required edits.
- **FR-007**: The README MUST use concise wording that emphasizes what users should run first.
- **FR-008**: The README structure MUST make defaults and optional variants visually distinguishable.

### Key Entities *(include if feature involves data)*

- **Install Source Reference**: Canonical repository URL/source used in install examples.
- **Default Overlay Command**: Primary command users are expected to run for typical setup.
- **Install Variant**: Optional command path (e.g., protocol/auth fallback) for non-default environments.

### Assumptions

- The repository `a9z-io/prod-kit` is now the canonical source users should install from.
- Most users benefit from installing both Claude commands and Claude skills together by default.
- Optional/fallback install variants are still needed but should not overshadow the default path.

### Assumption Refinements (Implementation)

- Canonical prose source is now explicitly shown as `https://github.com/a9z-io/prod-kit` in the README upgrade section.
- Default overlay command examples now consistently use the combined flags path before optional variants.
- Legacy `3leches/prod-kit` references were removed from active install guidance.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of default README install examples reference the `a9z-io/prod-kit` repository.
- **SC-002**: 100% of default overlay command examples include both `--with-claude-commands` and `--with-claude-skills`.
- **SC-003**: New users can complete the documented default install path without consulting additional setup sections.
- **SC-004**: Support questions caused by legacy repository URL confusion decrease after README update rollout.

