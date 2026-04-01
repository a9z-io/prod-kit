# Contracts: Prodkit Create Diagram

**Feature**: `001-create-diagram-skill`  
**Date**: 2026-04-01

This feature has no HTTP API surface. Contracts are defined as command behavior and file schema agreements between producers (command/skill) and consumers (users and AI agents).

## Contract 1: Command Naming Contract

- Canonical command name: `prodkit.create diagram`.
- Canonical dataflow companion naming: `prodkit.dataflow`.
- Deprecated alias terminology: `prodkit.dataflowdiagram` (migration-only reference).

## Contract 2: Input Artifact Contract

- Accepted source artifact types: architecture output and dataflow output.
- Source artifact must be readable and non-empty.
- Unsupported artifact types must fail with actionable error feedback.

## Contract 3: Output Location Contract

- For architecture/dataflow-based invocations, output Mermaid file must be stored in the same directory as the source artifact.
- Output location must be returned in success feedback.

## Contract 4: Output Content Contract

- Generated artifact must contain Mermaid syntax.
- Successful artifacts must include at least one node and one relationship edge.
- Invalid conversion must not emit misleading success artifacts.

## Contract 5: Collision and Error Contract

- Existing files must not be overwritten silently.
- Command must apply deterministic non-overwrite naming or explicit overwrite behavior.
- Failures must report what is wrong and how to correct it.
