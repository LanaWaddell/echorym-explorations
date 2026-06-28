# Prototype 0 Scope

## Name

Prototype 0: The First Conduit

## Purpose

Prototype 0 tests the smallest living version of Echorym's core loop. It should prove that the system can represent relationship under uncertainty without requiring a full game implementation.

## Core loop

1. A player enters with intent.
2. The world responds.
3. The player makes choices under uncertainty.
4. Trust, coherence, signal integrity, and resilience change.
5. The world remembers and evolves.

## Scope frame

The First Conduit is a minimal encounter, not a vertical slice. It should be playable as a written scenario, inspectable as structured data, and expandable into later simulations.

## Layer responsibilities

### World layer

- Define the First Conduit as a place, threshold, or entity.
- Identify one player-facing response from the world.
- Include at least one anchor, dormant trust network, or memory-bearing element.
- Record what the world remembers after the player's choice.

### Mechanics layer

- Represent intent, uncertainty, choice, consequence, and memory.
- Track trust, coherence, signal integrity, and resilience changes.
- Use coherence gates only as interpretive markers, not level gates.
- Avoid reducing outcome quality to a reward score.

### Simulation/experiment layer

- Preserve initial state, choice, consequence, and final state.
- Produce at least one state / action / consequence / coherence trajectory.
- Keep sample data small enough for manual review.
- Make assumptions visible in notes or sample records.

### Research layer

- Capture research implications as questions, not settled claims.
- Flag external references for review before promotion.
- Use theory to clarify design, not to overrule prototype evidence.

## In scope

- One entry scene.
- One player intent declaration.
- One world response.
- One human decision gateway.
- One or two entities or world presences.
- One memory trace.
- A hand-authored sample world state.
- Qualitative evaluation notes.

## Out of scope

- Full game implementation.
- Engine selection.
- Visual style selection.
- AI model or provider selection.
- Persistent account systems.
- Procedural content pipeline.
- Complex AI agent orchestration.
- Production balancing.
- Full psychological simulation.

## Initial success criteria

Prototype 0 is successful when a reviewer can:

- Read the scenario and identify the player's intent.
- Explain what the world response reveals and withholds.
- Identify the decision gateway and the uncertainty involved.
- Trace how one choice changes trust, coherence, signal integrity, resilience, memory, and world-state.
- Inspect the sample data without needing a runtime.
- See how the prototype could become a text prototype, simulation, agent experiment, or visual worldbuilding artifact later.

## Open design questions

- Does the First Conduit respond to intent directly, through signal, or through an entity?
- What is the smallest useful memory trace?
- Which part of the encounter should remain ambiguous?
- How should a player repair a poor first signal?
- Should coherence begin exactly at the Pattern Emergence Gate or only approach it?
- What makes the world remember without making the system feel punitive?
