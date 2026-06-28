# Echorym Explorations

This repository is a documentation-first prototype scaffold for **Echorym**: an adaptive coherence-world system about relationship under uncertainty.

Echorym explores how intent, choice, memory, trust, signal integrity, resilience, and world-state co-evolve over time. It is not primarily a content-generation system. Generated content may eventually help express scenes, logs, diagrams, or simulations, but the central question is systemic: how do choices change relationships, weaken or repair signals, alter shared memory, and shift the world toward or away from coherence?

The project begins as a lightweight sandbox for experiments, environment traces, agents, evaluation signals, reproducibility, and reusable prototypes. The broader architecture treats those experiment loops as instruments for studying a living world model rather than as an end in themselves.

## Project goals

- Define the smallest useful Echorym world model: player state, world state, entities, events, memory traces, and coherence signals.
- Capture a clear definition of environments, agents, evaluation signals, and human decision gateways.
- Stand up a reproducible experiment loop: data -> model -> evaluation -> reflection.
- Track learnings in notes to converge toward stable interfaces, schemas, and prototype contracts.
- Provide a minimal scaffold that can grow into text prototypes, simulation work, agent experiments, visual worldbuilding, research applications, or a production-grade project later.

## Core premise

Prototype 0 begins with a simple loop:

1. A player enters with intent.
2. The world responds.
3. The player makes choices under uncertainty.
4. Trust, coherence, signal integrity, and resilience change.
5. The world remembers and evolves.

The purpose is not to maximize reward. The purpose is to observe how state, action, consequence, coherence, and memory interact across time.

## Coherence threshold model

Echorym uses threshold gates as interpretive markers for world-state transitions:

| Threshold | Gate |
| --- | --- |
| 0.376 | Pattern Emergence Gate |
| 0.618 | Resonance Gate |
| 0.786 | Topological Lock Gate |
| 0.886 | Phase Travel Gate |
| 1.000 | Unified Field Gate |

These gates are not fixed game levels. They are provisional markers for when local patterns become legible, relational resonance stabilizes, world topology begins to lock, phase movement becomes possible, or a coherent field is fully unified.

## Core data & artifacts

- **Environment traces**: state / action / consequence / coherence trajectories (JSONL or parquet), plus metadata such as seed, config, scenario, and schema version.
- **Agent events**: observation histories, intent declarations, action plans, intermediate reasoning, uncertainty markers, and logged metrics.
- **Evaluation outputs**: scorecards, coherence summaries, trust deltas, signal-integrity checks, resilience observations, and QA notes.
- **Configs**: run configurations for reproducibility, including scenario inputs, model settings, and evaluation criteria.
- **Memory traces**: durable records of meaningful events, relationship changes, unresolved tensions, and world-state consequences.

## Core models

- **Environment dynamics** model (or simulator abstraction)
- **Policy/Agent** model with a clean IO contract
- **Critic/Coherence** model or metric function
- Optional: **Reflection/Editor** models to revise plans and generate new hypotheses

## Why trajectories changed

The original sandbox framing included trajectory data for reproducible experiments. Echorym keeps that framing, but replaces reward-centered language with **state / action / consequence / coherence trajectories** because the project is not primarily about reward optimization.

In Echorym, an action matters because it changes relationships, trust, signal integrity, resilience, memory, and world-state. A superficially successful choice can still degrade coherence. A costly choice can preserve trust. The trajectory format should therefore preserve consequence and coherence, not collapse them into a single reward scalar.

## Repository map

- `docs/`: charter, roadmap, glossary, mechanics, world, research, and architecture notes.
- `schemas/`: JSON Schemas for the initial world, player, entity, event, and memory trace records.
- `prototypes/prototype-0-first-conduit/`: the first playable or simulatable scenario scaffold.
- `notes/`: working notes, questions, and decision fragments that are not yet stable.
- `experiments/`: future runnable scripts, notebooks, simulations, and evaluation runs.

## Sample milestones

1. **Bootstrap**: documentation scaffold, README, schemas, and Prototype 0 scenario notes.
2. **Baseline**: deterministic text prototype and hand-authored scenario trace.
3. **Data pipeline**: collect trajectories, log coherence metrics, and checkpoint results.
4. **Experimentation**: compare player, agent, and world-response policies under uncertainty.
5. **Reflection loop**: run a cycle of propose -> test -> analyze -> iterate.
6. **Interface hardening**: stabilize schemas, glossary, and prototype entrypoints.

### Next steps

- Review the initial schemas and decide which fields are required for Prototype 0.
- Write the first hand-authored scenario trace for The First Conduit.
- Define the first evaluation rubric for coherence, trust, signal integrity, and resilience.
- Decide when a prototype should become runnable code, and which engine or language, if any, is appropriate.
