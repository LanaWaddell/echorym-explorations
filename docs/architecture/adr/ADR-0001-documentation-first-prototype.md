# ADR-0001: Documentation-First Prototype

## Status

Accepted

## Context

Echorym combines worldbuilding, adaptive systems, simulation, and experiment design. The project is still defining its core concepts and should not be locked to an engine, language, model provider, or runtime architecture too early.

## Decision

Begin with a documentation-first scaffold:

- Preserve the existing experiment-loop framing.
- Define core concepts in Markdown.
- Create starter JSON Schemas.
- Add sample data for Prototype 0.
- Keep implementation choices open.

## Consequences

This approach slows immediate game implementation but improves shared understanding, provenance, schema stability, and future reproducibility.

Future prototypes can add code once the smallest coherent loop is clear.

