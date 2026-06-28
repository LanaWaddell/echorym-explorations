# Data Model

## Purpose

The initial data model describes the minimum records needed to document and replay Prototype 0.

## Core records

- `world_state`: Current world coherence, active gates, regions, anchors, and global memory references.
- `entity`: A character, conduit, anchor, signal source, trust network, or other stateful world participant.
- `player_state`: Player intent, known signals, trust links, coherence state, and decision history.
- `event`: A meaningful observation, decision, response, or consequence.
- `memory_trace`: A durable record created or changed by events.

## Design rules

- Prefer explicit IDs over implicit text references.
- Preserve provenance and schema version.
- Record uncertainty rather than erasing it.
- Keep numeric scores optional where qualitative labels are more honest.
- Avoid encoding a reward scalar as the central outcome.

