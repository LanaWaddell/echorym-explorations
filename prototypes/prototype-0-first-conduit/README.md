# Prototype 0: The First Conduit

## Purpose

Prototype 0 tests the smallest living version of Echorym's core loop:

1. A player enters with intent.
2. The world responds.
3. The player makes choices under uncertainty.
4. Trust, coherence, signal integrity, and resilience change.
5. The world remembers and evolves.

## What this prototype is

This is a design and data scaffold for a scenario that can be played manually, simulated in a notebook, or later implemented in code.

## What this prototype is not

It is not a full game, engine decision, AI product, or content pipeline.

## Files

- `design.md`: Mechanics and scenario design notes.
- `sample_scenario.md`: A small playable outline.
- `data/`: Sample JSON records that demonstrate the initial schemas.
- `traces/`: Complete, inspectable trajectories. **The canonical first trajectory is
  [`traces/trace-001-promise-before-passage.md`](traces/trace-001-promise-before-passage.md)**
  ("Promise Before Passage"), with its machine-readable records under
  `traces/data/trace-001-promise-before-passage/` and the schema issues it surfaced in
  [`traces/SCHEMA_OBSERVATIONS.md`](traces/SCHEMA_OBSERVATIONS.md).

## Canonical trace

Trace 001 — **Promise Before Passage** is the first complete Echorym loop. The player offers a
memory-binding promise as an anchor and uses it to let the calling signal clarify *without*
amplifying it. It is the reference example of relationship under uncertainty: the choice produces
benefit *and* binding, and the world remembers consequential behaviour rather than rewarding
desirable behaviour.

Two local rules established by that trace and carried forward:

1. **No score is valid without a rationale.** All trust/coherence/signal/resilience values are
   provisional interpretive estimates, not computed values.
2. **Gate values are orientation markers, not computed truths.** The system may move near, past,
   or away from a gate without snapping to it.

## Evaluation focus

The prototype should make it possible to inspect a state / action / consequence / coherence trajectory and ask whether the world response preserved or degraded trust, signal integrity, resilience, memory, and coherence.

