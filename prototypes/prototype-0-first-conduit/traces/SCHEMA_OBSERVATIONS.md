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
# Schema Observations — Trace 002 Addendum

Surfaced by authoring the canonical trace *Trust Before Truth*. **Append this section to
`SCHEMA_OBSERVATIONS.md`** (append-only: do not rewrite the Trace 001 items). Nothing here
is applied; all 26 Trace 002 records validate against the v0.2-amended schemas, with the
gaps below carried by the established prose conventions.

## Verdicts on the v0.2 amendments (first field deployment)

- **#3 (signal axes): earned its place immediately.** `provenance: confirmed` +
  `quality: corrupted` simultaneously true is the trace's entire premise, and it is now
  *data*, not prose (evt-202, both player_state records). The legacy `integrity` field
  was not used by any 002 record.
- **#2 (`resilience_trend`): used in four entity records** without prose-smuggling.
- **#4 (delta rationales): used throughout;** the two-readings requirement of local
  rule 3 (healthy reading + capture reading per rise) fits naturally in the rationale
  fields and would have been unmanageable inside `world_state_changes` strings.

## Evidence updates for open Tier 2 observations

### #5 (coherence multi-axis) — evidence strengthened
The bloom's coherence 0.55 **was genuinely reached under the measurement then in use**;
the fracture corrected its *meaning*, not the record — the measure had conflated local
alignment/reduced diversity with global coherence (append-only discipline applied to a
number). That conflation is precisely #5's case: local legibility rose while global
reachable-set diversity fell, and one scalar called "world coherence" carried both.
Second Trace in a row where the axes diverged; this time they diverged *adversarially*.

### #6 (dimensional trust) — evidence now decisive, and doubled
The fracture (evt-210) is the field's existence proof: recognition ~0.80 surviving
while interpretation ~0.20 and restraint ~0.15 collapse, aggregated into a scalar 0.44
that the record itself calls near-meaningless without its rationale. Per DN §14 this
field has now *fallen out of evidence*. Recommend promotion to Tier 1 for the next
amendment pass.

**The review doubled the evidence: trust is also relationally addressed.** The v0.1
draft slid a value from player→Conduit into player→Network and presented the numbers as
continuous — caught in review, fixed in v0.2 (Network trust born 0.48 provisional at
evt-203; Conduit trust held at 0.52 throughout). A trust value must always say *whose*
trust *in what*; the drafting error itself is the observation's best exhibit. Candidate
shape from review (evidence-for, not adoption-of):
`{source, target, dimension, value/posture, trend, rationale, evidence_event, confidence}`.

Design note: dimensions are not static — 002 used a different active set than 001's
(001: restraint/honesty/care; 002: recognition/interpretation/restraint/
signal-handling). A fixed dimension enum is likely the wrong shape; consider
`trust_dimensions: [{name, value, rationale}]` addressed per relationship.

### #7 (network/entity status) — evidence strengthened
The network's trajectory (dormant → stirring → synchronizing → active → constrained)
was carried entirely in `trust_posture` strings and `world_state_changes` prose across
five events. The world doc's richer state list remains unimplemented; 002 used most of it.

### #8 (gateway options) — evidence strengthened
Two gateways this trace (evt-204, evt-211), both stashing structured `options[]`
(id / description / risk / chosen) in the free `inputs` bag. The shape is now stable
across three gateways in two traces; it is ready to be a defined schema shape whenever
Tier 2 opens.

### #10 (trajectory object) — evidence strengthened, new requirement identified
The criteria evaluation (C1/C2/C3) is a *trajectory-level* judgment: it cites evidence
across seven events and two state snapshots, but no object binds them, so it lives only
in the narrative doc. If criteria evaluations are to be machine-checkable later, the
trajectory object needs an `evaluation` slot distinguishing **authored ground truth**
from **in-world measurement** (local rule 4) — that separation is now load-bearing and
has no data representation.

## New observations

### #11. Region lifecycle has no representation *(surfaced by design — the DN §14 test)*
Trace 002 is the trace that was supposed to make staging fields fall out of evidence,
and it did — twice. First: `staged`, the criteria verdicts, the re-test provenance,
and the withheld rule (evt-213) are all carried in prose; `world_state.regions` is a
bare string array that cannot say `underpulse-network-region` is *staged with an
identified withheld rule, pending deltas unapplied*. Second, and sharper: the review
cycle itself caught a v0.2 ending that committed the region while C1 was indeterminate
— DN §4.1 assigns insufficient evidence to remain-staged, and §2.2 bars authored
ground truth from routing around the commit gate. A schema-level region lifecycle
(with criteria verdicts attached) would have made that mis-ending *unwritable*, not
merely reviewable. Strongest possible evidence that the field design should now go
through the DN.

### #12. Withheld rules need a home
The world now contains a first-class governance object — a named, logged, revisitable
withheld rule (`recognition → amplification authority`) — that exists only as strings
in `world_state_changes` and entity descriptions. DN §4.1 makes "withheld and logged
for revisit" the *default* commit outcome, so this object will recur in every
commit-with-constraint. Candidate shape: a `withheld_rules[]` array on world_state
(`{rule_id, statement, withheld_at_event, revisit_condition}`), or a registry file per
the DN §7.0 registry pattern. Defer to the same DN-mediated pass as #11.

### #14. Anchors have components, and only one is capture-immune
The review separated the Threshold Stone into four components — **reference record**
(immutable, append-only), **active bond** (carries influence into the world),
**presentation surface** (what entities encounter), **provenance link** (relates active
form to reference). Trace 002's capture operated entirely on bond and surface; the
record's immunity is what made the capture measurable. This is a general anchor model
born inside a trace revision: the trace uses the distinction inline (prose only), but
the model needs a real home — a mechanics note (`docs/mechanics/anchor-model.md`) or a
DN §9 amendment — before any second anchor exists. Entity schema currently has no way
to say which component a relationship or capture touches; no field proposed until the
model has a home.

### #13. Baselines are load-bearing but only conventional
C3 was measured "against the preserved baseline" — which in practice means *the
initial_state folder*, by convention. That worked for a single-episode trace. Once
traces chain (003+), "the baseline" becomes ambiguous (trace open? estimation-window
freeze per DN §4.3? last commit?). No field proposal yet; flagging that the convention
will not survive multi-window estimation unchanged.

## Suggested order of operations (updated)

1. **#6** — promote to Tier 1; evidence decisive; shape question (fixed enum vs.
   dimension list) is the only open design point.
2. **#11 + #12 together, via the DN** — these are the staging/commit fields DN §14
   deferred until falsification; falsification is done. They should enter through a DN
   amendment (v0.5?) so the field design answers to the criteria evaluation, then land
   as schema amendments.
3. **#14** — write the anchor-model home (mechanics note or DN §9 amendment) before
   any second anchor is authored; the component distinction is already load-bearing
   in 002's canonical record.
4. **#5, #7, #8, #10** — one more trace of evidence each is cheap; none blocked 002.
5. **#13** — revisit when Trace 003's estimation windows are designed.
