# Schema Observations for v0.2

Surfaced by authoring the canonical trace *Promise Before Passage*. This is the merged team
list — points raised by Echo and by Claude, plus the issues the trace hit during validation.
**Nothing here is applied to the schemas yet** (per the "do not overhaul schemas yet"
decision); every record in this trace validates against the *current* schemas. These are
decisions for Lana, ordered cheapest-first within two tiers.

## Standing rule adopted in this trace

> **No score is valid without a rationale.** All trust / coherence / signal / resilience values
> are provisional *interpretive* scores, not computed values. They make the trace inspectable and
> track movement over time; the meaning lives in the rationale, not the number. Future versions
> may replace or supplement numbers with dimensional models (below).

---

## Tier 1 — decide soon (cheap, already discussed, or hit during validation)

### 1. Keep the gates as orientation markers — don't harden them, don't drop them *(Echo + Claude, reconciled)*
Earlier I (Claude) suggested making `nearest_gate` a free string and moving the ladder out of the
data contract. Echo's amendment, adopted: **keep the named gates** — they're part of Echorym's
identity — but treat them explicitly as *orientation markers, not computed truths*. The standing
framing:
> Coherence scores are provisional interpretive estimates. Gate values are orientation markers,
> not computed truths. The system may move near, past, or away from a gate without snapping to it.

Concretely: the `nearest_gate` enum of *names* can stay; what must not happen is presenting the
*threshold numbers* as measured. This trace starts coherence at 0.38 (just past the 0.376 marker)
to embody that. **Minor note, not a fork:** Echo's earlier draft started exactly on 0.376; 0.38-just-past
carries the same intent. Optional later: relax `nearest_gate` to a free string if the five-name
enum ever feels constraining, but there is no urgency.

### 2. Resilience (and trust posture, and signal integrity) enums can't hold a *trend* *(hit in validation)*
The trace wanted `resilience: "strained but stabilizing"` and it failed validation — the enum
only allows a point value. The stabilizing *trend* had to be smuggled into the description. Same
shape as the coherence problem (#5). Minimal fix: allow a small object `{ value, trend, note }`
for resilience/trust_posture; or keep the enum and add an optional `*_trend` string.

### 3. Signal: knowledge vs quality are two axes in one field *(Claude + Echo agree)*
A signal can become *better understood without becoming less corrupted* — which is exactly what
happened in step 5/6 (provenance unknown→inferred; quality flat). The single `integrity` enum
(`unknown/low/partial/stable/high/corrupted`) fuses a *knowledge* axis and a *quality* axis, so
the trace had to leave `integrity: "partial"` unchanged and explain the real move in prose.
Recommended split:
```
signal_provenance: unknown | inferred | confirmed
signal_quality:    intact  | degraded | corrupted
signal_interpretation: partial | contested | clarified
```
This directly serves the "verify before trusting" mechanic, which is *about* the knowledge axis.

### 4. Event consequences need first-class rationale fields *(Claude + Echo agree)*
`event.consequences` holds numeric deltas but has no rationale slot, so the "no score without
rationale" rule is currently honored by stuffing rationales into `world_state_changes` strings —
it works but it's a hack. Recommendation: add an optional `rationale` string per delta, e.g.
`{ "coherence_delta": 0.05, "rationale": "intent/signal/memory aligned without erasing uncertainty" }`.

---

## Tier 2 — design direction (heavier; let the second trace force them)

### 5. Coherence is doing too many jobs *(Claude raised, Echo seconded)*
`coherence` simultaneously means legibility, stability, alignment, and signal/world/memory
intelligibility — and in step 5 these moved in *different directions* (learning the signal was
degraded raised legibility but not settledness). For v0.2, require a rationale on every coherence
change. For later: split into sub-axes such as `legibility`, `stability`, `alignment`,
`continuity`, each with its own value + rationale.

### 6. Trust should become dimensional, not a single scalar *(Echo's model, Claude endorses)*
The conduit's stance is *"you did not violate me — but I don't yet know whether you understand
what you touched."* A single number can't say that. Direction:
```
trust:
  restraint:      0.70
  honesty:        0.58
  care:           0.62
  competence:     unknown
  consistency:    unknown
  discretion:     unknown
  repair_capacity: unknown
```
In this trace the promise raised restraint/care/honesty but **not** competence or consistency.

### 7. "Dormant but protected" is real state *(Claude's distinction, Echo adopts)*
The Underpulse Network ends *dormant* in both initial and final state, but its **meaning**
changed — it was deliberately *protected from an incorrect wake*. That now lives only in a
`trust_posture` string ("dormant, provisionally protected"). The world doc already lists richer
states (`dormant/stirring/active/fragmented/corrupted/repaired/lost`); a first-class
`dormant_network_status` would let "stirring but protected" be state, not prose.

### 8. Decision gateway options need structured representation *(Claude raised, Echo seconded)*
The four offered options were stashed in `event.inputs` (a free `additionalProperties:true` bag)
because the event schema has no first-class place for "choices offered." Since gateways are the
heart of the loop, consider either a `decision_gateway.schema.json` or a defined `options[]`
shape on the event (id, description, risk, chosen).

### 9. Anchors may need first-class support *(Echo)*
This trace treats the promise as an anchor held by the Threshold Stone (anchor entity) *and*
recorded as a memory trace — it works but is ad hoc. Decide whether an anchor is an entity, a
memory trace, a relationship object, or its own schema.

### 10. A trajectory / episode schema to link events *(Echo)*
A full trajectory is an *ordered chain*, but nothing currently binds the sequence together except
folder convention and `source_event_id` back-references. Possible object:
```
trajectory:
  trajectory_id
  initial_state_ids
  event_sequence
  final_state_ids
  evaluation_notes
  schema_observations
```

---

## Suggested order of operations

1. **#1** (adopt the gate-as-orientation-marker framing in docs) and **#2** (trend on enums) — cheap; one is framing, one is validation-forced.
2. **#3** (signal provenance vs quality) — directly serves the core mechanic.
3. **#4** (rationale on deltas) — locks in "no score without rationale" properly.
4. Then **#5/#6** (dimensional coherence + trust) once Trace 002 (the *amplify* branch) stresses them.
5. **#7–#10** as the trace library grows.
