# /prodkit.security

## User Input

```text
$ARGUMENTS
```

## Goal

Scaffold `.specify/memory/security.md` — the canonical security and compliance knowledge-base file. Agents load this file for `coding`, `architecture-review`, and `security-audit` tasks. If the file already exists, add only missing sections.

## Target File

`.specify/memory/security.md`

## Idempotency Rule

Before writing, check whether `.specify/memory/security.md` exists.
- **Does not exist** → create the full file using the schema below.
- **Exists** → read the file, identify which `##` sections are missing, and append only the missing sections. Do NOT modify any existing content. Report which sections were added (or "nothing to add" if all sections already present).

## File Schema

```markdown
---
file: security.md
version: 1.0.0
last-updated: YYYY-MM-DD
required-by-tasks: [coding, architecture-review, security-audit]
---

## Agent Summary

[Fill in ≤150 words: describe the security posture of this system. What are the 2–3 most critical security constraints an agent must know before generating any code or architecture? Name the compliance frameworks that apply and any non-negotiable security patterns (e.g., "all data encrypted at rest and in transit", "no secrets in code").]

## Encryption Standards

[Define encryption requirements for data at rest and data in transit.]

- **Data at rest**: [algorithm, key management approach]
- **Data in transit**: [protocol, minimum TLS version]
- **Key management**: [how keys are stored, rotated, and accessed]

## Authentication

[How users and services prove identity.]

- **User authentication**: [mechanism — e.g., OAuth 2.0 + PKCE, username/password + MFA]
- **Service-to-service authentication**: [mechanism — e.g., mTLS, signed JWTs, API keys]
- **Session management**: [session duration, refresh token policy]

## Authorization

[How access control is enforced.]

- **Model**: [RBAC / ABAC / PBAC]
- **Role definitions**: [list key roles and their access levels]
- **Principle of least privilege**: [how it is enforced — e.g., scoped tokens, row-level security]

## Data Protection

[How sensitive data is handled, stored, and deleted.]

- **PII handling**: [what constitutes PII in this system, how it is handled]
- **Data classification**: [classification tiers and handling requirements per tier]
- **Retention and deletion**: [retention periods and deletion mechanisms]
- **Secrets management**: [where secrets live — e.g., environment variables, secrets manager — and what is forbidden (e.g., no secrets in source code)]

## Compliance Requirements

[Regulatory and contractual compliance obligations.]

- **Frameworks**: [e.g., SOC 2 Type II, HIPAA, GDPR, PCI-DSS — list all that apply]
- **Current status**: [certified / in progress / not started per framework]
- **Key controls required**: [the top 3–5 controls that affect engineering decisions]
- **Audit logging**: [what must be logged, retention period, access controls on logs]
```

Replace `YYYY-MM-DD` with today's date.

## Post-Write Validation

After writing, confirm:
1. YAML frontmatter present with all four required fields.
2. `## Agent Summary` is first section after frontmatter, ≤150 words.
3. All five domain sections present: `## Encryption Standards`, `## Authentication`, `## Authorization`, `## Data Protection`, `## Compliance Requirements`.
4. No existing content overwritten.
5. Report outcome.
