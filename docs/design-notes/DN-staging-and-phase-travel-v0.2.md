# DN — Staging, Commit, and Phase Travel

**Status:** Design note, draft **v0.2**. Not a schema change. No fields proposed for
adoption. This note exists to be argued with and falsified against Trace 002.
**Depends on:** `trace-001-promise-before-passage.md`, `design.md`, The First Conduit
Covenant (v0.1 draft).
**Relates to:** entrainment-capture work — committed-reference pattern, Kalman twin,
two-sided detection, Hughes constraint on off-manifold probes.

> **§7 (quantum layer) is explicitly held for review and is not baked in.** It is the
> section most likely to change. Everything downstream of it — budget units, rate law —
> depends on decisions not yet made.

**Changes from v0.1:** two capture channels replace the single instrument (v0.1 §9 was
defective); third channel added (fragmentation by neglect); C1 given a concrete estimator
and its failure mode; C3 gains a third outcome; the quantum layer is rebuilt as load-bearing
rather than metaphorical; commit decisions and intervention triggers separated into two
clocks; ceiling authorization reasoned from state provenance rather than phenomenology.

---

## 1. The problem

Echorym must let its ontology grow — new regions, entities, transition rules — without
that growth becoming indistinguishable from the participant's own projection amplified
back at them.

Two bounding failures:

- **Premature collapse.** Growth restricted by schema or external rule; the world branches
  inside a fixed container. Exploration becomes decorative.
- **Capture.** Growth unrestricted; the world stops being able to answer for itself.

Goal: maximise reachable novelty while keeping capture detectable *from outside the
participant's own judgement*.

---

## 2. Governing law

> **A mutation may change anything except the record of what it changed from.**

Ontology mutable. Provenance append-only. The single external constraint at the world
layer; everything else here is in-world dynamics.

### 2.1 What "ontology mutable" means — three levels

| Level | Mutable? | Content |
| --- | --- | --- |
| **Instance values** | Yes (already) | trust 0.42 → 0.52, coherence, resilience |
| **Types and rules** | **Yes — this is what the law opens** | What *kinds* of thing can exist; what kinds of change are possible; new object classes; new transition rules |
| **Provenance** | **No** | What existed, what changed, what it changed from |

This is not metaphysical relativism and specifically not "what was real can be rewritten."
Level 3 forbids that. The taxonomy grows forward; history is not editable backward.

**Corollary.** Reversibility is not a property of a mutation. It is a property of whether
enough state was preserved outside the mutation's write scope to reconstruct from. A
`reversibility` flag is not a fact; a preserved-state basis is.

---

## 3. Region lifecycle

| State | Meaning |
| --- | --- |
| `reached` | Encountered. Enterable, interactive, consequential. |
| `staged` | Real and inhabitable; its **authority over the rest of the world** is withheld. |
| `committed` | Canonical. Pending deltas applied. Transition rules updated. Enters the reachable set. |
| `decayed` | Dissolved. The **attempt persists in provenance**; the region does not. |

### 3.1 Staged is orthogonal to location

Staged is a property of the region, not of where the participant is. A staged region can
be inhabited, left, returned to. The participant can be standing in a committed region
while three others sit staged.

**Authority = effect outside itself.** Inside a staged region, full effect — nothing about
the lived experience is provisional. Outside, consequences accumulate as **pending deltas**
rather than applied changes.

*Worked example.* A region operates on the rule *memory propagates backward*. Staged: that
rule holds inside it, fully. It does **not** make memory propagate backward world-wide, and
the region cannot yet become a required waypoint between other regions. On commit, the rule
enters world law.

While staged: transition rules elsewhere unaltered; provenance logging heightened;
pre-mutation state preserved so the return path is real rather than asserted.

`decayed` is not erasure. Per Trace 001, the world remembers *consequential* behaviour, not
*successful* behaviour. Failure to commit is itself a memory trace.

---

## 4. Commit criteria

Local, transitional, and global respectively.

### C1 — Independent dynamics (local)

The region's behaviour is **not fully predictable from the participant's input**; it must
contribute its own state and memory.

**Estimator.** Conditional mutual information / transfer entropy:

```
I( response ; region_state | participant_action )
```

Directed and estimable from time series. Granger causality is the linear-Gaussian special
case; the Kalman twin's innovation test is a further special case of that.

**Known failure mode (Hughes, again).** MI estimators are sample-hungry and
upward-biased in high dimensions with few samples. Off-manifold regions are *by
construction* high-dimensional and sparsely visited — so the estimator is weakest exactly
where the test matters most. Same constraint as the off-manifold probe design.

Three partial mitigations:

1. Project onto a low-dimensional sufficient statistic — *but* this reintroduces the
   stale-baseline problem (§11.2).
2. Use the twin's approach where the reference distribution is analytic rather than
   estimated.
3. Accept wide early estimates that tighten with repeat transit. **Preferred** — the
   estimator sharpens under the same operation that maintains coherence (§7). Visiting is
   both the measurement and the maintenance.

*Direction of the test:* a region that is unusually easy to model is failing, not passing.
See §8.3.

### C2 — Return path exercised (transitional)

The return transit is **performed**, not claimed, during the provisional phase.

Timing constraint: the test is only available in the window where it is not yet needed.
After commit, reversal is a new mutation with its own provenance, not a cheap path.

What it measures is graded — see **return hysteresis**, §8.1.

### C3 — Plurality preserved (global)

The **reachable set elsewhere has not contracted** while the region was staged.

Sink signatures: previously available transitions elsewhere become unavailable; paths
between other regions route through the staged region; it becomes a mandatory waypoint;
response diversity in unrelated entities narrows.

A region may pass C1 and C2 and fail C3. **Independence is not benignity** — a genuinely
autonomous region can still absorb the world.

#### 4.1 Three outcomes, not two

| Outcome | When | Consequence |
| --- | --- | --- |
| **Commit with constraint** *(default)* | The sink property is traceable to a specific transition rule | Region commits; that rule is withheld and logged for later revisit. Preserves a rich discovery, removes the attractor property. |
| **Remain staged** | Evidence insufficient, or the participant chooses to hold it open | Not free: staging carries coherence cost and fragmentation exposure (§7.4). Indefinite staging is a decision with consequences — this is what stops "stage everything" being dominant. |
| **Decay** | The region cannot meet criteria and is not being maintained | Dissolves; attempt persists in provenance. |

#### 4.2 When the sink property *is* the discovery

Some regions are interesting *because* they concentrate routing — that is their character,
not a defect, and withholding the rule guts the find. Two in-world resolutions:

- **Compensation.** Commit the sink property, paired with a mandatory counter-structure
  that restores reachable-set size — an alternate route, a new anchor, a preserved
  bypass. The world answers concentration with an opened path rather than a prohibition.
- **Mandated internal exit.** Commit the sink property with a required anchor *inside* the
  region holding phase to the trunk. Attraction retained; return preserved.

Both are guardrails-as-dynamics rather than guardrails-as-refusal.

---

## 5. Commitment is not collapse

Committing a region **adds a basis state**. It is not a measurement.

- **Superposition** = multiple committed regions simultaneously reachable, phase relations
  maintained between them.
- **Collapse** = the reachable set contracts toward one.

> **Capture is `|reachable set| → 1`.**

Signal domination, interpretive closure, compulsive repetition, dependency loops,
irreversible identity loss are all special cases.

Superposition is **not** maintained by withholding commitment. Withheld commitment is the
fragile form; plural commitment with maintained transit is the durable form.

---

## 6. Transit between committed regions

Ordinary mode of play, not an exceptional operation.

| Criterion | Requirement | Failure meaning |
| --- | --- | --- |
| **T1 — Phase reference valid** | The anchor relating origin and destination is not stale | Transit still possible but lossy; divergence not measurable against a stale reference |
| **T2 — Coherence cost paid** | Draws on recoherence throughput (§7) | Cannot transit; region drifts further |
| **T3 — Memory continuity** | Something carries across | Without carry-over this is not travel but replacement — the identity-preservation criterion |
| **T4 — Origin remains reachable** | Departure does not remove the return | One-way transit is collapse, not travel |

**An anchor is a phase reference** — not stored coordinates but a *maintained relation*
against which divergence can be measured rather than merely undergone.

This unifies four objects previously floating separately: the committed reference in the
twin architecture, the Threshold Stone holding the promise, the designated anchor in
Covenant §6, and the staging mechanism here.

It also explains the `what_it_preserves` / `what_it_constrains` pairing: maintaining phase
coherence with a reference costs freedom of movement. A real tradeoff, not a design tax.

---

## 7. Coherence — the quantum layer

> **HELD FOR REVIEW.** Everything in this section is a candidate mapping. Each item is
> marked **[load-bearing]**, **[stipulated]**, or **[not yet earned]**.

Decoherence is ambient and continuous. Coherence is therefore a throughput problem, not a
stock problem: recoherence work per unit time against ambient decay across the committed
set.

### 7.1 Two rates, not one budget **[load-bearing]**

Amplitude damping (state loss, T1) and dephasing (relation loss, T2) are distinct, and
T2 ≤ 2·T1 — dephasing is typically far faster.

This maps directly onto the fragmentation failure: a region persists and remains
enterable (long T1) while its phase relation to the trunk decays (short T2). **Return
becomes lossy before anything is lost.**

- **Return hysteresis is a T2 measurement.**
- **Reachable-set contraction is a T1 measurement.**

The v0.1 "coherence budget" was wrong because it was a single scalar. There are two decay
processes with different rates and different observables.

### 7.2 Rate law — spin echo / CPMG **[load-bearing]**

Dephasing from static or slowly-varying inhomogeneity is refocusable by a pulse; fast
random noise is not. CPMG extends T2 by pulsing faster than the noise correlation time.

**Transit is the pulse.**

> **Rate law:** transit frequency must exceed the correlation frequency of the drift being
> suppressed.

Non-obvious falsifiable prediction: **frequent shallow revisits outperform rare deep ones**
for maintenance. This is testable in simulation and observable in play.

### 7.3 Currency and threshold — QEC **[load-bearing, with one caution]**

Quantum error correction: encode the logical state redundantly, measure **syndromes**
rather than the state itself, correct while below threshold.

- **Redundant encoding** = the same relation carried by multiple anchors, cross-referencing
  memory traces, shared structure between regions.
- **Syndrome measurement** = measure the relations *between* anchors, never the
  participant's state directly. This maps onto Covenant §1's floor with unusual precision:
  QEC supplies a principled reason why the relational measurement is the permissible one.
- **Threshold theorem** = a critical anchor redundancy above which recoherence outpaces
  decoherence.

> **Coherence budget = distance to threshold.** That is the currency question answered, if
> this mapping survives review.

*Caution:* QEC assumes an error model. Echorym's "error model" is participant behaviour,
which is adversarial-ish and non-stationary. The threshold result may not transfer cleanly.

### 7.4 Recoherence mechanisms

| Mechanism | Quantum analogue | Status |
| --- | --- | --- |
| **Transit** | Refocusing pulse | [load-bearing] — see 7.2 |
| **Cross-referencing memory traces** | Redundant encoding | [load-bearing] |
| **Obligations spanning regions** | Entanglement-like binding constraint | [not yet earned] — see 7.6 |
| **Anchor re-exercise** | Syndrome extraction / stabiliser measurement | [load-bearing] |
| **Shared structure between regions** | Correlated noise / decoherence-free subspace | [load-bearing] — regions sharing entities, signals, or rules are cheaper to hold in relation than fully alien ones |

Anchor density is a design lever: more anchors → cheaper maintenance, less freedom of
movement.

*Trace 001 note:* the promise is a coherence-maintaining structure, not only a narrative
device. **Calling a promise due is recoherence work.**

### 7.5 No-cloning **[stipulated]**

Anchors cannot be copied — only moved or referenced. Free to stipulate in Echorym,
unavailable in tissue. Worth taking precisely because it makes anchors scarce and therefore
consequential.

### 7.6 Where this is still decoration — the interference gap **[not yet earned]**

Without interference there is no superposition, only a probability distribution over
regions — a menu with a fancy name.

To make the mapping load-bearing, plural committed regions in maintained phase must
produce joint effects **neither produces alone**, with the phase relation determining
whether combination is constructive or destructive.

That is the missing piece. Until it exists, "superposition" in Echorym is doing less work
than the word implies. **This is the first thing to resolve when the quantum layer is
revisited.**

### 7.7 Simulability

A density-matrix-like object over regions: diagonal = reachability, off-diagonal = phase
relations, decaying at 1/T2, refreshed by transit, Lindblad-style update. Small numpy
build. It would test whether the rate law in 7.2 behaves as predicted.

**Candidate companion to Trace 002.**

### 7.8 Failure mode of over-expansion

Not collapse — **fragmentation**. Least-maintained relations thin first, so the periphery
degrades into regions still enterable but no longer cleanly returnable. That is capture.

Over-expansion and capture converge on the same failure from opposite directions.

---

## 8. Capture measurement

### 8.0 Three channels — corrects v0.1 §9

v0.1 claimed one instrument served both the commit gate and the anti-capture gate. **That
was wrong.** C1 sees only one channel.

| Channel | Mechanism | Detector | Timing |
| --- | --- | --- | --- |
| **A — Projection capture** | The region never had its own dynamics; it is the participant's echo wearing world-structure | C1: `I(response ; region_state \| participant_action) ≈ 0` | Pre-commit |
| **B — Absorption capture** | The region has strong, real, independent dynamics and *because of that* becomes an attractor that cannot be left | Reverse direction: `I(participant_action ; participant_state \| region_state) ≈ 0` | Post-commit, continuous |
| **C — Fragmentation by neglect** | Nothing hostile, nothing amplified; the relation binding a region to the trunk simply decayed below clean return | T2 / return hysteresis (§7.1) | Continuous |

**Passing C1 is not protection against B — it is closer to a precondition for it.** You
cannot be entrained by an echo; entrainment requires a real external driver.

Channel C explains the case v0.1 could not: a previously accessible region becoming
non-returnable without ever having been projection. The region did not change. The relation
did.

**Unifying definition holds across all three:** `|reachable| → 1`. A collapses the world
into the participant; B collapses the participant into the world; C severs the relation
between them.

**Two-sided principle, applied to direction of influence** rather than magnitude — the
direct transfer from the twin work.

### 8.1 Return hysteresis (graded)

Residual divergence after a completed return:

| Residual | Reading |
| --- | --- |
| None | No absorption |
| Partial | Partial absorption — returned, but not all the way |
| Return unavailable | Capture |

Obtained by performing a transit the participant wants to perform anyway. Repeated transit
across a plural committed set yields a **running** measurement rather than a one-off test.

### 8.2 Reachable-set contraction (global)

Direct measurement of `|reachable set|` over time. See §5.

### 8.3 Two-sided testing — the critical warning

From the entrainment work: **capture presents as coherence, not disorder.**

Any monitor whose alarm direction is "things look worse" is structurally blind to this
class. Entrainment appears as *contraction in variance structure* — the world becomes more
legible, more responsive, better fitted.

> A rising coherence number is not a health signal. Every coherence and trust readout in
> Echorym must be able to alarm **upward**.

### 8.4 Instrumentation constraints

- Held continuously by the system. The designated anchor is **escalation**, not primary
  detection.
- Under Covenant §1, capture proximity is a *measurement* and may be displayed. A number
  agreed to from grounded state is itself a mast against an in-the-moment reading.
- **Readout, not target.** Any displayed metric the world responds to becomes part of the
  loop it measures.

---

## 9. Two clocks — corrects v0.1 §9

Failing C1 is a **commit decision**, not an **intervention trigger**. v0.1 conflated them.

| Clock | Governs | Trigger |
| --- | --- | --- |
| **Commit clock** | Whether a region enters world law | C1 / C2 / C3 |
| **Intervention clock** | Whether anything interrupts the participant | §8 capture measures approaching threshold |

A reflective spiral is Zone 2 and **runs until the participant diverges or the capture
measures approach threshold — not before.** The spiral is part of exploration. What the
commit gate prevents is only the spiral being written into world law: Covenant §3's
disclosed hazard becoming permanent and load-bearing.

**Evidentiary payoff for permitting it:** a spiral the participant leaves on their own is
the strongest available evidence they were not captured. Divergence-by-choice is a
measurement obtainable no other way. Cutting the spiral short destroys the evidence.

---

## 10. Covenant interaction

| Section | Effect |
| --- | --- |
| **§1** | **Splits.** World-facing half (what here is real) discharged *structurally* — persistence is the answer: what was projection decays, what was real commits. Mystery preserved in the moment, honesty guaranteed over time. Participant-facing half (no authored or symbolic value presented as a measurement *of you*) remains a fixed floor. §7.3 supplies the principled version: measure relations between anchors, never the participant's state. **Wording fix:** §1 prohibits false assertion, not silence — withholding, ambiguity, and refusal to answer are permitted. As drafted it reads as a duty to annotate. |
| **§3** | Runaway reflection is not pathologised. Permitted and instrumented. Two clocks (§9) apply. |
| **§4** | Untouched. Exit to unaltered baseline remains external, continuous, non-adaptive. |
| **§5** | Ceiling vs. envelope — see §10.1. |
| **§6** | Anchor is escalation on §8 measures, not primary detection. |
| **§9** | Satisfied structurally rather than by assertion: staging exists to permit exploration, and its criteria are also its safety instrument. |

### 10.1 Ceiling vs. envelope, and authorizing a raise

- **Ceiling** — what the participant consented to be exposed to. Set from grounded state.
- **Envelope** — where the world currently has them, below the ceiling.

The envelope moves freely in both directions in-world. **Restoration to a prior consented
state is not expansion.** In-world narrowing should be transient by default — a refractory
period, not a ratchet. Regions beyond the ceiling are enterable but held **staged** until a
limit is defined from grounded state.

**Authorizing a raise: the argument is provenance-of-state, not phenomenology.**

Any state the world can produce is a state the world can *induce*. If the world can put the
participant into the state that authorizes raising the ceiling, the ceiling is not a mast.
Same reasoning as freezing the twin's baselines rather than rolling them.

**Delay does the primary work** — it tests a later state in a different context, and
induced states relax. Exit is therefore not strictly required as a discrete event; what is
required is *comparison across contexts separated in time*, at least one of which the world
did not produce.

**Open point (§11.5).** Whether an in-world felt-groundedness state can serve as one of
those comparison points is unresolved. The argument for: such a state is structurally
opposite to capture. The argument against: felt decoherence measures *coherence*, whereas
capture is defined on *reachability* — a participant can feel diffuse and unbound while
having exactly one reachable exit. Diffuseness is not plurality. Under channel B a driver
could plausibly induce a spacious, clear-headed state as the very mechanism of holding
someone. Resonance is a strong instrument for much of Echorym and specifically the wrong
one for this decision.

---

## 11. Open problems

1. **C1 estimator under Hughes.** §4/C1. Mitigation 3 preferred but unproven.
2. **Stale-reference detection.** T1 requires knowing an anchor has drifted. Same problem
   as adversarial rotation vs. endogenous manifold drift — unresolved there, unresolved
   here. Anecdotal comparison can generate hypotheses but cannot discriminate;
   non-discriminability is what makes it the crux.
3. **The interference gap.** §7.6. First thing to resolve when the quantum layer is
   revisited.
4. **C3 baseline — resolved by deferral.** Reachable-set comparison needs a pre-staging
   baseline, but continuous world evolution moves it. **Decision: keep the baseline moving
   and keep every version.** C3 can then be evaluated retrospectively against any prior
   baseline once Trace 002 shows which one mattered. The law applied to itself; costs a log
   file. Superposition discipline applied to the design decision.
5. **In-world groundedness for ceiling authorization.** §10.1. Open.
6. **QEC threshold transfer.** §7.3 caution — non-stationary, quasi-adversarial error
   model.
7. **Unforgeability, restated.** Echorym can *stipulate* an authentic provenance layer; a
   neural system cannot. Solving this here is not evidence for TRACE-HiT. Build the detector
   where authenticity is free; port the detector, not the proof.

---

## 12. What this note does *not* propose

No schema changes. No new first-class objects adopted.

Commit and transit criteria should be **falsified against Trace 002 (the amplify branch)
before any field is added**. Trace 002 is the capture trace: dormant network woken
incorrectly on a corrupted signal, trust spiking then fracturing. Author it, and the fields
fall out of evidence rather than anticipation.

Trace 001's local rule 1 stands: **no score is valid without a rationale.** Every quantity
named here is a *shape*, not a number.
