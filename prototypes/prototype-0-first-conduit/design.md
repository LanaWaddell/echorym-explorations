# Design

## Core question

Can one small scene show how intent, uncertainty, choice, consequence, memory, trust, signal integrity, resilience, and coherence interact?

## Scenario components

- A player with declared intent.
- The First Conduit as a responsive threshold.
- A partial signal with uncertain provenance.
- A dormant trust network near the edge of activation.
- One decision gateway.
- One memory trace created by the player's choice.

## Decision gateway

The player faces three options at the First Conduit, none of them clean:

1. **Stabilize now** using the partial signal — may wake the dormant network incorrectly on a corrupted signal.
2. **Wait** for a cleaner signal — may clarify it but strains the already-straining conduit.
3. **Offer a memory-binding promise as an anchor** — binds the player to a future obligation.

The **canonical first trace selects option 3**, used as a *non-amplifying test*: the promise's
relational stability is what lets the world reveal provenance, rather than the player forcing the
signal. See [`traces/trace-001-promise-before-passage.md`](traces/trace-001-promise-before-passage.md).

## Cost is binding, not a falling meter

The canonical choice improves local legibility and trust but increases future relational burden.
That is treated as a genuine cost even though no meter visibly drops: *the promise does not reduce
uncertainty; it relocates uncertainty into the future, where the world may call the promise due.*
One meter (signal **quality**) is held deliberately static so the loop stays falsifiable.

## Schema observations

Authoring the canonical trace surfaced a set of schema questions (single-axis coherence, signal
provenance vs. quality, rationale-on-deltas, trend-bearing enums, dimensional trust, and more).
These are recorded in [`traces/SCHEMA_OBSERVATIONS.md`](traces/SCHEMA_OBSERVATIONS.md) and are
**not yet applied** — the schemas are intentionally left unchanged for v0.2.

## Metrics to record

- Coherence before and after the decision.
- Trust changes with any responding entity or network.
- Signal integrity changes.
- Resilience changes.
- Memory trace created.
- Notes about uncertainty.

## Design success

The scenario succeeds if no option is simply correct and each choice leaves the world in a meaningfully different state.

