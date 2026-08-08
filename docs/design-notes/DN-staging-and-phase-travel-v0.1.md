# DN — Staging, Commit, and Phase Travel

**Status:** Design note, draft v0.1. Not a schema change. No fields are proposed for
adoption here; this note exists to be argued with and to be tested against Trace 002.
**Depends on:** `trace-001-promise-before-passage.md`, `design.md`, The First Conduit
Covenant (v0.1 draft).
**Relates to:** entrainment-capture work (committed-reference pattern, Kalman twin,
two-sided detection).

---

## 1. The problem this addresses

Echorym must permit the world's ontology to grow — new regions, new entities, new
transition rules — without that growth becoming indistinguishable from the participant's
own projection amplified back at them.

Two failure modes bound the design:

- **Premature collapse.** Growth is restricted by schema or by external rule, so the world
  can only branch inside a fixed container. Exploration becomes decorative.
- **Capture.** Growth is unrestricted, and the world's responses become a function of the
  participant's input alone. The world stops being able to answer for itself.

The mechanism below is intended to maximise reachable novelty while keeping the second
failure mode *detectable from outside the participant's own judgement*.

---

## 2. Governing law

> **A mutation may change anything except the record of what it changed from.**

Ontology mutable. Provenance append-only. This is the single external constraint at the
world layer. Everything else in this note is in-world dynamics.

Corollary: reversibility is not a property of a mutation. It is a property of whether
enough state was preserved outside the mutation's write scope to reconstruct from. A
`reversibility` flag is therefore not a fact; a preserved-state basis is.

---

## 3. Region lifecycle

| State | Meaning |
| --- | --- |
| `reached` | Encountered. Enterable, interactive, consequential. |
| `staged` | Real and inhabitable; its **authority** over the rest of the world is withheld. |
| `committed` | Canonical. Pending deltas applied. Transition rules updated. Enters the reachable set. |
| `decayed` | Dissolved. The **attempt persists in provenance**; the region does not. |

**What is staged is authority, not existence.** The region is fully real the moment it is
reached — nothing about the lived experience is provisional. What is held provisional is
its power to rewrite the rules governing everything else.

Concretely, while staged:

- Effects on other regions accumulate as **pending deltas** rather than applied changes.
- Transition rules elsewhere are unaltered.
- Provenance logging is heightened.
- Pre-mutation state is preserved, so the return path is real rather than asserted.

`decayed` is not erasure. Consistent with Trace 001: the world remembers *consequential*
behaviour, not *successful* behaviour. Failure to commit is itself a memory trace.

---

## 4. Commit criteria

A staged region commits when it satisfies all three. The criteria are local,
transitional, and global respectively.

### C1 — Independent dynamics (local)

The region's behaviour is **not fully predictable from the participant's input**. It must
contribute its own state and memory to its responses.

Operational form: model the region's response as a function of (a) participant action
alone versus (b) participant action plus region state/history. If (a) predicts (b) to
within noise, the region is projection, not world.

*Note the direction of the test.* A region that is unusually easy to model is failing,
not passing. See §7.

### C2 — Return path exercised (transitional)

The return transit is **performed**, not claimed, during the provisional phase.

Timing constraint: the test is only available in the window where it is not yet needed.
After commit, reversal becomes a new mutation with its own provenance, not a cheap path.

What is measured is graded, not binary — see **return hysteresis**, §7.

### C3 — Plurality preserved (global)

The **reachable set elsewhere has not contracted** while the region was staged.

This criterion is about everything *except* the new region. Sink signatures:

- Previously available transitions elsewhere become unavailable.
- Paths between other regions begin routing through the staged region.
- The staged region becomes a mandatory waypoint.
- Response diversity in unrelated entities narrows.

A region may pass C1 and C2 and fail C3. Independence is not benignity: a genuinely
autonomous region can still absorb the world.

---

## 5. Commitment is not collapse

Committing a region **adds a basis state**. It is not a measurement.

- **Superposition** = multiple committed regions simultaneously reachable, with maintained
  phase relations between them.
- **Collapse** = the reachable set contracts toward one.

This gives the formal definition used throughout:

> **Capture is `|reachable set| → 1`.**

Signal domination, interpretive closure, compulsive repetition, dependency loops,
irreversible identity loss, and total interpretive closure are all special cases. C3 is
therefore not a secondary criterion; it is the direct anti-capture criterion, with C1 and
C2 as its local and transitional components.

Superposition is **not** maintained by withholding commitment. Withheld commitment is the
fragile form. The durable form is plural commitment with maintained transit.

---

## 6. Transit between committed regions

Transit is the ordinary mode of play, not an exceptional operation. Proposed criteria:

| Criterion | Requirement | Failure meaning |
| --- | --- | --- |
| **T1 — Phase reference valid** | The anchor relating origin and destination is not stale. | Transit still possible, but lossy. Divergence is not measurable against a stale reference. |
| **T2 — Coherence cost paid** | Transit draws on the recoherence budget (§7). | Cannot transit; region drifts further. |
| **T3 — Memory continuity** | Something carries across. | Without carry-over this is not travel — it is replacement. This is the identity-preservation criterion. |
| **T4 — Origin remains reachable** | Departure does not remove the return. | One-way transit is collapse, not travel. |

**An anchor is a phase reference.** Not stored coordinates — a *maintained relation*
against which divergence can be measured rather than merely undergone. This unifies four
objects that have been floating separately: the committed reference in the twin
architecture, the Threshold Stone holding the promise, the designated anchor in Covenant
§6, and the staging mechanism here.

It also explains the `what_it_preserves` / `what_it_constrains` pairing: maintaining phase
coherence with a reference costs freedom of movement. Real tradeoff, not design tax.

---

## 7. Coherence as flow

Decoherence is **ambient and continuous**. Coherence is therefore a throughput problem,
not a stock problem: recoherence work per unit time against ambient decay across the
committed set.

### Recoherence mechanisms

1. **Transit.** Visiting a region re-establishes its phase relation to the trunk and to
   regions sharing structure with it. *Traversal is maintenance.* The mechanic that makes
   exploration worth doing is the same one that keeps the world legible.
2. **Cross-referencing memory traces.** A memory referencing two regions binds them.
3. **Obligations spanning regions.** A promise the world can call due holds the regions it
   spans in relation. Trace 001's promise is a coherence-maintaining structure, not only a
   narrative device — *calling a promise due is recoherence work.*
4. **Anchor re-exercise.** Refreshes phase for everything referenced to that anchor.
5. **Shared structure.** Regions sharing entities, signals, or rules are cheaper to hold in
   relation than fully alien ones.

Anchor density is a design lever: more anchors, cheaper maintenance, less freedom of
movement.

### Failure mode of over-expansion

Not collapse — **fragmentation**. The least-maintained relations thin first, so the
periphery degrades into regions that can still be entered but no longer cleanly returned
from. That is capture. Over-expansion and capture converge on the same failure from
opposite directions.

---

## 8. Capture measurement

### Return hysteresis (graded)

Residual divergence after a completed return:

| Residual | Reading |
| --- | --- |
| None | No absorption. |
| Partial | Partial absorption — returned, but not all the way. |
| Return unavailable | Capture. |

Obtained by performing the transit the participant wants to perform anyway. Repeated
transit across a plural committed set yields a **running** hysteresis measurement rather
than a one-off test.

### Reachable-set contraction (global)

Direct measurement of `|reachable set|` over time. See §5.

### Two-sided testing — the important warning

From the entrainment-capture work: **capture presents as coherence, not disorder.**

Any monitor whose alarm direction is "things look worse" is structurally blind to this
class. Entrainment appears as *contraction in variance structure* — the world becomes
more legible, more responsive, better fitted. A rising coherence number is therefore not
a health signal. Every coherence and trust readout in Echorym must be able to alarm
**upward**.

This is the single most important transfer from the twin work into this design.

### Instrumentation constraints

- Held continuously by the system; the designated anchor is **escalation**, not primary
  detection.
- Under Covenant §1, capture proximity is a *measurement* and may be displayed to the
  participant. A number agreed to from grounded state is itself a mast against an
  in-the-moment reading.
- **Readout, not target.** Any displayed metric the world responds to becomes part of the
  loop it measures.

---

## 9. The commit gate and the anti-capture gate are one instrument

C1 requires behaviour not predictable from participant input alone. Capture is defined as
world response becoming predictable from participant input alone.

Therefore a staged region that cannot meet C1 is, by construction, participant
projection — a reflective spiral that has taken on the appearance of world structure.
Committing it would write that spiral into canonical world law: Covenant §3's disclosed
hazard becoming permanent and load-bearing.

Staging is not a safety layer bolted onto world-building. It is the thing that
distinguishes a **discovered region** from an **elaborate echo**, using one reading.

---

## 10. Covenant interaction

| Section | Effect |
| --- | --- |
| **§1** | Splits. The world-facing half (what here is real) is discharged *structurally* — persistence is the answer; what was projection decays, what was real commits. Mystery preserved in the moment, honesty guaranteed over time. The participant-facing half (no authored or symbolic value presented as a measurement *of you*) remains a fixed floor. Wording fix needed: §1 prohibits false assertion, not silence — withholding, ambiguity, and refusal to answer are permitted. |
| **§3** | Runaway reflection is not pathologised. It is permitted and instrumented. C1 is what prevents a reflective spiral from being written into world law. |
| **§4** | Untouched. Exit to unaltered baseline remains external, continuous, non-adaptive. |
| **§5** | Ceiling vs. envelope distinction applies. Envelope moves freely in both directions in-world below the consented ceiling; restoration to a prior consented state is not expansion. Regions beyond the ceiling are enterable but held staged until a limit is defined from grounded state. |
| **§9** | Satisfied structurally rather than by assertion: staging exists to permit exploration, and its criteria are also its safety instrument. |

---

## 11. Open problems

1. **C1 estimator.** "Not predictable from participant input alone" needs a concrete
   estimator with a reference distribution. The twin work has one for the Gaussian case;
   Echorym's response space is not obviously that.
2. **Stale-reference detection.** T1 requires knowing an anchor has drifted. This is the
   same problem as adversarial rotation versus endogenous manifold drift — unresolved
   there, unresolved here.
3. **Recoherence budget units.** §7 is qualitatively right and quantitatively empty. What
   is the currency, and what sets the rate?
4. **C3 baseline.** Reachable-set comparison requires a stable pre-staging baseline. Under
   continuous world evolution, that baseline is itself moving. Committed-reference
   discipline says freeze it; world-building says it must move. Unresolved tension.
5. **Unforgeability, restated.** Echorym can *stipulate* an authentic provenance layer; a
   neural system cannot. Solving this here is not evidence for TRACE-HiT. Build the
   detector where authenticity is free; port the detector, not the proof.

---

## 12. What this note does *not* propose

No schema changes. No new first-class objects adopted. The commit criteria and transit
criteria above should be **falsified against Trace 002 (the amplify branch) before any
field is added**. Trace 002 is the capture trace: dormant network woken incorrectly on a
corrupted signal, trust spiking then fracturing. Author it, and the fields fall out of
evidence rather than anticipation.

Trace 001's local rule 1 stands: no score is valid without a rationale. Every quantity
named here is currently a *shape*, not a number.
