# Contracts: Simplify README Install Instructions

**Feature**: `004-simplify-readme-install`  
**Date**: 2026-04-01

This feature defines documentation behavior contracts rather than API contracts.

## Contract 1: Canonical Source Contract

- Default install command examples must reference the `a9z-io/prod-kit` repository source.
- Legacy `3leches/prod-kit` source references must not appear as active default guidance.
- Canonical source wording for prose references is `https://github.com/a9z-io/prod-kit`.
- Canonical `uv` command source pattern is `git+https://github.com/a9z-io/prod-kit.git`.

## Contract 2: Default Overlay Contract

- The default overlay recommendation must include:
  - `prodkit overlay --force --with-claude-commands --with-claude-skills`
- Default path must be clearly presented before optional alternatives.

## Contract 3: Readability Contract

- README install instructions must provide one clear first-run path.
- Optional variants (SSH/token/manual) must be concise and explicitly marked as fallback.
- Command blocks must be copy-paste-ready.
- Section ordering rule: `Default path` first, then `Persistent install`, then fallback variants.
- Fallback label rule: prefix optional variants with `Fallback:` so users do not confuse them with default steps.

## Contract 4: Consistency Contract

- Related docs should not contradict README default install guidance.
- If legacy references remain for historical context, they must be clearly non-default.
