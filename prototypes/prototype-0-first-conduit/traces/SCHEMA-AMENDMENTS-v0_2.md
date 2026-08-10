# Schema Amendments — v0.2 (Observations #2, #3, #4)

**Status:** Reviewed and approved by Lana, 2026-08-09. Precedes Trace 002 (*Trust Before Truth*) record drafting.
**Applies:** `SCHEMA_OBSERVATIONS.md` Tier 1 items #2, #3, #4, surfaced by Trace 001.
**Design constraint:** Every change is **additive**. All 18 Trace 001 records validate
unchanged (verified with `validate_trace.py` against the amended schemas — 0 failures).
No retro-migration; legacy fields are deprecated in documentation, not removed.
Records using the amended fields should declare `schema_version: "0.2.0"`; `"0.1.0"`
records remain valid indefinitely.

These are general-purpose amendments, not Trace 002 accommodations: #3 is the data
representation of the verify-before-trusting mechanic (every trace touches a signal);
#2 recurs in any world that tracks consequential behaviour over time; #4 makes the
standing rule — *no score is valid without a rationale* — part of the data contract
rather than a prose convention.

---

## #3 — Signal: knowledge vs. quality split (player_state, entity)

**Problem (from Trace 001):** a signal became *better understood without becoming less
corrupted* (provenance unknown → inferred; quality flat), and the single `integrity`
enum could not say so. The real move lived in prose.

**Change — `player_state.schema.json`, `known_signals[]` items:**

| Field | Type | Values | Axis |
| --- | --- | --- | --- |
| `provenance` *(new, optional)* | enum | `unknown` / `inferred` / `confirmed` | knowledge |
| `quality` *(new, optional)* | enum | `intact` / `degraded` / `corrupted` | condition |
| `interpretation_status` *(new, optional)* | enum | `partial` / `contested` / `clarified` | reading |
| `interpretation` *(unchanged)* | string | free text | rationale for the above |
| `integrity` *(deprecated, valid)* | enum | legacy combined axis | — |

`required` relaxed from `[signal_id, integrity]` to `[signal_id]` so new records are not
forced to populate a deprecated field. (Relaxing `required` is backward-compatible:
every existing record still validates.)

**Change — `entity.schema.json`, `state`:** optional `signal_provenance` and
`signal_quality` (same enums); `signal_integrity` deprecated in description, retained.

**Deliberately not changed:** `event.consequences.signal_integrity_delta` stays as the
legacy numeric meter. Provenance and quality are categorical axes; their movement is
recorded in the state records and explained via the new rationale fields (#4), not as
numeric deltas. If a future trace genuinely needs a quality delta, that is its own
observation.

## #2 — Trend on point-value enums (entity)

**Problem (hit in Trace 001 validation):** `resilience: "strained but stabilizing"`
failed — the enum holds a point value only; the trend was smuggled into `description`.

**Change — `entity.schema.json`, `state`:** optional `resilience_trend` (free string,
e.g. `"stabilizing"`, `"deteriorating"`, `"oscillating"`) alongside the untouched
`resilience` enum.

**Considered and not adopted:** the `{ value, trend, note }` object form from the
observation. `anyOf` mixed forms complicate validation tooling and produce two record
dialects; the sibling field is strictly additive and greppable. Revisit if trend fields
proliferate (that proliferation would itself be evidence for the object form).
`trust_posture` is already a free string and needs no amendment. `world_state.coherence`
already carries `notes`; left untouched to keep the diff minimal.

## #4 — Rationale fields on consequence deltas (event)

**Problem:** `consequences` holds numeric deltas with no rationale slot; the standing
rule was honoured by stuffing rationales into `world_state_changes` strings.

**Change — `event.schema.json`, `consequences`:** four optional string fields —
`coherence_rationale`, `trust_rationale`, `signal_integrity_rationale`,
`resilience_rationale` — one per delta, same naming stem.

`world_state_changes` keeps its Trace 001 role for changes that are not meter deltas
(obligations created, entities marked, protections established).

---

## Not touched

`world_state.schema.json`, `memory_trace.schema.json` — no Tier 1 observation lands on
them. Observations #5–#10 remain open by design: Trace 002 is expected to stress #5
(coherence multi-axis), #6 (dimensional trust — via the fracture), #7 (network status),
#8 (gateway options), #10 (trajectory object); those fields fall out of 002's evidence
per DN §14, using Trace 001's established prose conventions in the interim.

## Suggested PR housekeeping

- Annotate `SCHEMA_OBSERVATIONS.md` items #2, #3, #4 with
  `**Applied — v0.2 amendments (see SCHEMA-AMENDMENTS-v0_2.md).**` — append the
  annotation; do not rewrite the original observation text (append-only discipline).
- Optionally add `validate_trace.py` under `experiments/` or `traces/` — it validates
  any trace data folder against the current schemas and was used to verify this
  amendment (18/18 Trace 001 records pass; forward-compatibility and enum-rejection
  checks included).
- Suggested branch: `schema-amendments-tier1-trace-002-trust-before-truth`
  (descriptor + the trace these amendments precede, per convention — adjust as you see fit).
