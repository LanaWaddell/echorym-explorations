# DN — Staging, Commit, and Phase Travel

**Status:** Design note, draft **v0.3**. Not a schema change. No fields proposed for
adoption. Falsification target: Trace 002.
**Depends on:** `trace-001-promise-before-passage.md`, `design.md`, The First Conduit
Covenant (v0.1 draft).
**Relates to:** entrainment-capture work — committed-reference pattern, Kalman twin,
two-sided detection, Hughes-type small-sample failure, challenge-response exposure as a
rate-limited resource.

> **Purpose of v0.3:** to isolate the results Covenant v0.2 needs from the results still
> under review, so the Covenant can be drafted without inheriting the quantum layer's
> uncertainty. See **§11 — Covenant dependency surface**. The headline result: **no
> Covenant floor depends on §7.**

**Changes from v0.2**

- C1 re-specified to condition on participant *history*, closing the mirror-with-memory
  hole; failure mode reworded as Hughes-*type* small-sample instability.
- Off-manifold accessibility promoted from consequence to strategy; Meiboom-Gill
  phase-alternation added as the answer to visit-induced drift.
- §7 restructured as an open versioned **registry** rather than a closed list.
- Entanglement introduced with a real earning test (Bell/CHSH) and an explicit fork;
  monogamy added as a structural anti-capture constraint.
- Moiré identified as closing the interference gap (v0.2 §7.6).
- Materials subsection added, filtered by a mechanism test.
- Channel C made a graded lifecycle with a reconstruction basis and a held-out provenance
  test.
- Origin taxonomy (discovery / co-creation / reconstruction / projection) adopted as the
  organizing frame for §8; the three capture channels sit underneath it.
- Possibility classes added, held **orthogonal** to commit state.
- Two-key ceiling authorization adopted; ceiling raises rate-limited.
- New §11.

---

## 1. The problem

Echorym must let its ontology grow — new regions, entities, transition rules — without that
growth becoming indistinguishable from the participant's own projection amplified back at
them.

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
| Instance values | Yes (already) | trust 0.42 → 0.52, coherence, resilience |
| **Types and rules** | **Yes — what the law opens** | What kinds of thing can exist; what kinds of change are possible; new object classes; new transition rules |
| Provenance | **No** | What existed, what changed, what it changed from |

Not metaphysical relativism, and specifically not "what was real can be rewritten." Level 3
forbids that. The taxonomy grows forward; history is not editable backward.

**Corollary.** Reversibility is not a property of a mutation but of whether enough state was
preserved outside the mutation's write scope to reconstruct from. A `reversibility` flag is
not a fact; a preserved-state basis is.

### 2.2 Possibility classes

> **No coherent possibility is forbidden from being explored; its authority is proportional
> to what it has earned.**

| Class | Meaning |
| --- | --- |
| **I** | Physically demonstrated — observed or implemented in classical or quantum systems |
| **II** | Theoretically permitted — consistent with accepted physics, not yet realized in the required form |
| **III** | Mathematically constructible — internally coherent, physical realizability unknown |
| **IV** | Speculative — not yet grounded enough to be treated as law |

**Orthogonality constraint — important.** Possibility class describes the *real world*.
Commit state describes *Echorym's internal evidence*. They are independent axes and must
not be collapsed.

- A Class I mechanism may sit in-world **unearned** — established physics does not exempt a
  region from C1/C2/C3.
- A Class IV mechanism may sit in-world **committed** — if it demonstrated irreducible
  dynamics, exercised return, and preserved plurality.

Collapsing these would let real-world provenance route around the commit gate, which is the
gate's entire function. Both values are recorded; neither implies the other.

---

## 3. Region lifecycle

| State | Meaning |
| --- | --- |
| `reached` | Encountered. Enterable, interactive, consequential. |
| `staged` | Real and inhabitable; its **authority over the rest of the world** is withheld. |
| `committed` | Canonical. Pending deltas applied. Transition rules updated. Enters the reachable set. |
| `thinned` → `frayed` → `severed` → `provenance-only` | Fragmentation lifecycle — see §8.4. |
| `decayed` | Dissolved. The **attempt persists in provenance**; the region does not. |

### 3.1 Staged is orthogonal to location

Staged is a property of the region, not of where the participant is. A staged region can be
inhabited, left, returned to. The participant can stand in a committed region while three
others sit staged.

**Authority = effect outside itself.** Inside a staged region, full effect — nothing about
the lived experience is provisional. Outside, consequences accumulate as **pending deltas**
rather than applied changes.

*Worked example.* A region operates on the rule *memory propagates backward*. Staged: that
rule holds inside it, fully. It does **not** make memory propagate backward world-wide, and
the region cannot become a required waypoint between other regions. On commit, the rule
enters world law.

`decayed` is not erasure. Per Trace 001, the world remembers *consequential* behaviour, not
*successful* behaviour.

---

## 4. Commit criteria

### C1 — Irreducible dynamics (local)

The region must have state and response of its own rather than being a mirror.

**Estimator:**

```
I( response ; region_state | participant_history )
```

**Why history, not current action.** Conditioning on the participant's *current* action
fails against a mirror with memory: if `region_state` is an accumulation of past inputs and
the response is a function of that accumulation, the conditional MI is high while the region
remains pure projection — merely integrated rather than instantaneous. That is exactly what
a reflective spiral looks like once it has run a while.

**Failure mode: Hughes-type small-sample instability.** Dimensionality grows faster than
observations, making independence estimates unstable and typically positively biased.
Off-manifold regions are by construction high-dimensional and sparsely visited, so the
estimator is weakest where the test matters most.

> **Stated honestly:** conditioning on history is the *correct* form and the *more*
> sample-hungry one. The right estimator is worse under Hughes than the wrong one. This
> tension is not resolved; it is the reason for §6.1 and §4.3.

**Direction of the test.** A region that is unusually easy to model is failing, not passing.
See §8.3.

**C1 does not require independence from participant influence.** It requires irreducible
state. See the origin taxonomy, §8.0 — co-creation is a legitimate category, not a failure.

### C2 — Return path exercised (transitional)

The return transit is **performed**, not claimed, during the provisional phase.

Timing constraint: the test is only available in the window where it is not yet needed.
After commit, reversal is a new mutation with its own provenance, not a cheap path.

Graded outcome — see return hysteresis, §8.2.

### C3 — Plurality preserved (global)

The **reachable set elsewhere has not contracted** while the region was staged.

Sink signatures: previously available transitions elsewhere become unavailable; paths
between other regions route through the staged region; it becomes a mandatory waypoint;
response diversity in unrelated entities narrows.

A region may pass C1 and C2 and fail C3. **Independence is not benignity.**

### 4.1 Three outcomes

| Outcome | When | Consequence |
| --- | --- | --- |
| **Commit with constraint** *(default)* | Sink property traceable to a specific transition rule | Region commits; that rule withheld and logged for revisit |
| **Remain staged** | Evidence insufficient, or participant holds it open | Not free — carries coherence cost and fragmentation exposure. Indefinite staging is a decision with consequences; this is what stops "stage everything" being dominant |
| **Decay** | Cannot meet criteria, not being maintained | Dissolves; attempt persists in provenance |

### 4.2 When the sink property *is* the discovery

Some regions are interesting *because* they concentrate routing. Withholding the rule guts
the find. Two in-world resolutions:

- **Compensation.** Commit the sink property paired with a mandatory counter-structure that
  restores reachable-set size — an alternate route, a new anchor, a preserved bypass. The
  world answers concentration with an opened path rather than a prohibition.
- **Mandated internal exit.** Commit with a required anchor *inside* the region holding
  phase to the trunk. Attraction retained; return preserved.

Guardrails as dynamics, not as refusal.

### 4.3 Estimation windows — resolves the moving-baseline problem for both C1 and C3

Increased visiting improves sampling **and** changes the region, so more visits sample a
moving distribution. Estimation cannot outrun this by raising N when N is what moves the
target. This is open problem 2 (endogenous vs. induced drift) in another costume.

**Discipline: freeze the reference within an estimation window; allow it to move across
windows; keep every version.**

- *Within* a window — estimate against a frozen reference. Committed-reference discipline
  holds; C1 is computable.
- *Across* windows — compare references. The delta is a direct measurement of what the
  visiting did.
- *Retrospectively* — C3 can be evaluated against any prior baseline once Trace 002 shows
  which one mattered.

This is the governing law applied to the estimator itself. Costs a log file. It is the same
decision already taken for the C3 baseline in v0.2, now doing double duty.

---

## 5. Commitment is not collapse

Committing a region **adds a basis state**. It is not a measurement.

- **Superposition** = multiple committed regions simultaneously reachable, phase relations
  maintained.
- **Collapse** = the reachable set contracts toward one.

> **Capture is `|reachable set| → 1`.**

Signal domination, interpretive closure, compulsive repetition, dependency loops,
irreversible identity loss are special cases.

Superposition is **not** maintained by withholding commitment. Withheld commitment is the
fragile form; plural commitment with maintained transit is the durable form.

### 5.1 Monogamy as structural anti-capture — [conditional on §7.5]

If A is maximally entangled with B, A cannot be entangled with C. Entanglement monogamy is a
hard constraint on relational exclusivity: **a region cannot be maximally bound to
everything.**

This matters because it is anti-capture that is not a rule. It gives anchors principled
scarcity beyond the stipulated no-cloning, and it is the same property underlying QKD
security. It is the strongest single reason to make entanglement foundational rather than
thematic — but it is only available if §7.5's fork resolves toward a real quantum layer.
Classical correlation has no monogamy.

---

## 6. Transit between committed regions

Ordinary mode of play, not an exceptional operation.

| Criterion | Requirement | Failure meaning |
| --- | --- | --- |
| **T1 — Phase reference valid** | Anchor relating origin and destination is not stale | Transit possible but lossy; divergence not measurable against a stale reference |
| **T2 — Coherence cost paid** | Draws on recoherence throughput (§7) | Cannot transit; region drifts further |
| **T3 — Memory continuity** | Something carries across | Without carry-over this is replacement, not travel — the identity-preservation criterion |
| **T4 — Origin remains reachable** | Departure does not remove the return | One-way transit is collapse, not travel |

**An anchor is a phase reference** — not stored coordinates but a *maintained relation*
against which divergence can be measured rather than merely undergone.

This unifies four previously separate objects: the committed reference in the twin
architecture, the Threshold Stone holding the promise, the designated anchor in Covenant §6,
and the staging mechanism here. It also explains the `what_it_preserves` /
`what_it_constrains` pairing: maintaining phase coherence with a reference costs freedom of
movement.

### 6.1 Off-manifold accessibility as design strategy

Sparse access creates two failures at once: the world feels narrower than its theory
promises, and Echorym cannot accumulate the observations needed to distinguish irreducible
dynamics from noise. Accessibility is therefore both a richness decision and an estimation
decision.

> **Law: visiting is both measurement and maintenance.**

Access mechanisms:

- shallow recurring access — brief visits are cheap
- multiple approach paths — no single gateway monopolises a region
- bridge regions — gradual exposure to unfamiliar dimensions
- resonant windows — periods when access is cheaper
- memory-supported re-entry — prior contact reduces traversal cost
- shared exploration — more than one entity contributes observations
- staged micro-regions — parts of a larger manifold accessible before the whole commits

Consistent with the CPMG prediction (§7.3): frequent shallow revisits should outperform rare
deep immersions for maintenance.

### 6.2 Meiboom-Gill alternation — the answer to visit-induced drift

The **MG** in CPMG exists precisely because the refocusing pulses themselves introduce
error. Phase-alternating successive pulses makes those errors cancel rather than accumulate.

**Direct transfer:** alternate the approach path or direction of successive revisits so that
visit-induced adaptation cancels rather than accumulates.

Non-obvious, non-decorative, and testable in the §7.8 simulation. It is the mechanism that
makes §6.1's accessibility strategy compatible with §4.3's estimation problem rather than
aggravating it.

---

## 7. Coherence — the quantum registry

> **HELD FOR REVIEW.** No Covenant floor depends on this section (§11).

Decoherence is ambient and continuous. Coherence is a throughput problem, not a stock
problem: recoherence work per unit time against ambient decay across the committed set.

### 7.0 Registry format — open and versioned

§7 is **not** a closed list of permitted mechanisms. It is a registry, and new entries may
be added whenever research or in-world evidence supplies a credible mode of coherence
maintenance, recovery, protection, or reconstruction.

Each entry carries: `mechanism_id`, `name`, `physical_analogue`, `in_world_operation`,
`what_it_preserves`, `what_it_costs`, `required_conditions`, `known_failure_modes`,
`evidence_status`, `date_introduced`, `supersedes_or_extends`, `possibility_class` (§2.2).

Status values: `[load-bearing]` · `[stipulated]` · `[candidate]` · `[not yet earned]` ·
`[retired or narrowed]`.

**Admission test:** *a mapping earns entry only if it supplies a mechanism Echorym lacked,
not vocabulary for something Echorym already has.*

### 7.1 Two rates, not one budget — [load-bearing]

Amplitude damping (state loss, T1) and dephasing (relation loss, T2) are distinct, and
T2 ≤ 2·T1 — dephasing is typically far faster.

Maps directly onto fragmentation: a region persists and remains enterable (long T1) while
its phase relation to the trunk decays (short T2). **Return becomes lossy before anything is
lost.**

- Return hysteresis is a **T2** measurement.
- Reachable-set contraction is a **T1** measurement.

### 7.2 Rate law — CPMG — [load-bearing]

**CPMG = Carr–Purcell–Meiboom–Gill**, a sequence of repeated refocusing pulses used in
magnetic resonance and quantum control to suppress dephasing from slowly varying noise.
Dynamical decoupling of this kind genuinely extends measured coherence times in spin
systems.

**Transit is the pulse.**

> Transit frequency must exceed the correlation frequency of the drift being suppressed.

Falsifiable prediction: frequent shallow revisits outperform rare deep ones. See §6.2 for
the MG half.

### 7.3 Currency and threshold — QEC — [load-bearing, one caution]

- **Redundant encoding** = the same relation carried by multiple anchors, cross-referencing
  memory traces, shared structure.
- **Syndrome measurement** = measure relations *between* anchors, never the participant's
  state directly. Supplies a principled reason why the relational measurement is the
  permissible one.
- **Threshold theorem** = a critical anchor redundancy above which recoherence outpaces
  decoherence.

> **Coherence budget = distance to threshold.**

*Caution:* QEC assumes an error model. Echorym's error model is participant behaviour —
non-stationary and quasi-adversarial. The threshold result may not transfer cleanly.

*Note:* QEC code spaces distribute logical information across entangled physical subsystems.
The QEC mapping therefore presupposes §7.5.

### 7.4 Recoherence mechanisms

| Mechanism | Physical analogue | Status |
| --- | --- | --- |
| Transit | Refocusing pulse | [load-bearing] §7.2 |
| Alternated approach paths | Meiboom-Gill phase alternation | [load-bearing] §6.2 |
| Cross-referencing memory traces | Redundant encoding | [load-bearing] |
| Anchor re-exercise | Syndrome extraction / stabiliser measurement | [load-bearing] |
| Shared structure between regions | Decoherence-free subspace / correlated noise | [load-bearing] |
| Obligations spanning regions | Nonseparable relational constraint | [not yet earned] — depends on §7.5 |
| Topological protection | Non-local invariance | [candidate] §7.6 |
| Superconducting phase coherence | Macroscopic phase, Josephson coupling | [retired or narrowed] — renames what T2 and anchors already cover |

*Trace 001 note:* the promise is a coherence-maintaining structure, not only a narrative
device. **Calling a promise due is recoherence work.**

### 7.5 Entanglement — the fork that must be decided

Entanglement is the right foundational concept: its content is that **the states of parts
are incomplete descriptions and the relation carries irreducible state.** That is Echorym's
thesis stated in physics.

**The earning test must be Bell/CHSH, not dependence.** Conditional dependence, mutual
information, non-factorizability, and joint-state irreducibility are **all satisfied by
ordinary classical correlation**. Two regions with a shared cause are dependent,
non-factorizable, high-MI — and not entangled. If those become the test, Echorym
"demonstrates entanglement" on day one and the word means nothing.

The actual boundary is correlations exceeding what any local hidden-variable model can
produce. Binary rather than interpretive, and already familiar from QKD.

**The fork:**

| Option | Consequence |
| --- | --- |
| **(a) Reserve the word** | Name the mechanic *correlation* or *nonseparable relation*. Honest, costs the concept, and forfeits monogamy (§5.1). |
| **(b) Build a small quantum layer** | A few qubits in numpy alongside the QKD codebase. Makes this the one place in Echorym where the quantum claim is **literal rather than mapped**, and unlocks monogamy, genuine entanglement witnesses, reduced density matrices, stabiliser correlations. |

Recommendation: **(b)**, on the grounds that it is cheap, available, and that monogamy is a
structural anti-capture constraint obtainable no other way. But this is a decision, not a
derivation.

**In-world mechanic** (either option, with the naming adjusted): joint transition rules;
consequences not assignable to one side; correlated mutations; shared memory duplicated in
neither participant; phase-dependent constructive or destructive joint effects; separation
without independence.

**Earning conditions in-world:** a joint state not representable as separate local states; a
joint consequence neither region produces alone; a phase relation affecting outcome; a
measurement structure observing relational syndromes rather than reading each entity.

Candidate design test for **Trace 003**.

### 7.6 Materials-derived mechanisms

Filtered by the §7.0 admission test.

**Topological protection — [candidate], highest priority.** Information stored in global
structure, invariant under any local operation. Supplies *non-local invariance*, which
Echorym has nowhere else. In-world: locally damaged regions whose global identity remains
intact; paths protected by topology rather than walls; anchors whose function is distributed
across a structure; mutations not undoable by changing one local component. It is also what
the surface code *is*, so it unifies anchors, QEC, and anti-capture in one object.

**Moiré — [candidate]. This closes the v0.2 interference gap.** §7.7 required plural regions
in maintained phase producing joint effects neither produces alone, with the phase relation
determining the outcome. Moiré is a physical existence proof of exactly that structure: two
layers, a twist angle, emergent correlated phases present in neither parent, a magic angle
where something qualitatively new appears. **Twist angle is the phase relation** —
continuously tunable with sharp special values. In-world: two ordinary regions overlap at a
slight relational twist and produce a third ontology; microscopic alignment changes produce
large emergent consequences; phase diagrams become world maps; strain becomes an intentional
control parameter.

**Frustration / strong correlation — [candidate].** Massive ground-state degeneracy: the
system does not collapse to one configuration *because of its structure*, not because a rule
forbids it. That is `|reachable| > 1` maintained without enforcement — the thesis about
guardrails-as-dynamics in physical form. In-world: unresolved tension sustaining plurality;
coherence without simple order; regions generative precisely because they cannot settle.

**Defects and colour centres — [candidate].** A defect is not only damage: defects can be
controllable emitters, sensors, spin memories, network nodes, with optically addressable
spins and long coherence times. In-world: scars becoming anchors; local damage as a
memory-bearing node; imperfection opening a new signal channel. Damage as interface rather
than degradation.

### 7.7 Interference — status update

**Closed by moiré (§7.6)**, pending confirmation that the mechanic can be built. v0.2 §7.6
listed this as the first thing to resolve; it now has a concrete physical template.

### 7.8 Simulability

Density-matrix-like object over regions: diagonal = reachability, off-diagonal = phase
relations, decaying at 1/T2, refreshed by transit, Lindblad-style update. Small numpy build.
Tests the §7.2 rate law and the §6.2 alternation prediction.

Under fork option (b), the same build extends to real state vectors and CHSH evaluation.
Candidate companion to Trace 002.

### 7.9 Neural perturbation — two claims, kept separate

**Perturbation alters cognitive and network state — [Class I, supportable].** Stimulation
effects depend strongly on the brain's starting state; perturbation can alter attention,
perception, network dynamics, and conscious state. In-world: widening or redirecting the
accessible manifold; destabilising rigid attractors; synchronising or desynchronising
networks; temporary windows for phase access; supporting recoherence after fragmentation.

**Perturbation inducing functionally relevant quantum states in neural tissue — [Class IV,
not yet earned].** Hypotheses exist; convincing evidence for controllable, functionally
relevant neural entanglement or long-lived brain-wide coherence does not.

**Safe architecture, stated strictly:** the neural state controls a *classical parameter*
that configures a quantum system. Not "neural-quantum coupling" — that phrasing implies more
than is established and would cost credibility with exactly the audiences the QKD and
TRACE-HiT work depends on. The strict version is entirely sufficient for Echorym.

---

## 8. Origin taxonomy and capture channels

### 8.0 Four origins

Every region has an origin classification, recorded and revisable:

| Origin | Meaning | Evidence requirement |
| --- | --- | --- |
| **Discovery** | Region had dynamics prior to contact | C1 against early-window reference |
| **Co-creation** | Region developed irreducible dynamics *through* relationship | C1 satisfied at current window even though early windows show participant-driven formation. **Legitimate — arguably a central Echorym process** |
| **Reconstruction** | Region re-established from a preserved basis after fragmentation | §8.4 held-out provenance test |
| **Projection** | Region is a mirror, however elaborate | C1 fails at all windows |

The v0.2 note separated only the first and last. Co-creation and reconstruction have
different evidence requirements and must be first-class, or co-emergent regions fail C1 by
default — which was the original worry, now addressed by classification rather than by
weakening the test.

### 8.1 Three capture channels

| Channel | Mechanism | Detector | Timing |
| --- | --- | --- | --- |
| **A — Projection capture** | Region never had its own dynamics | C1: `I(response ; region_state \| participant_history) ≈ 0` | Pre-commit |
| **B — Absorption capture** | Region has strong real dynamics and *because of that* becomes an attractor that cannot be left | Reverse: `I(participant_action ; participant_state \| region_state) ≈ 0` | Post-commit, continuous |
| **C — Fragmentation** | Relation binding region to trunk decayed below clean return | T2 / return hysteresis | Continuous |

**Passing C1 is not protection against B — it is closer to a precondition.** You cannot be
entrained by an echo; entrainment requires a real external driver.

Unifying definition across all three: `|reachable| → 1`. A collapses the world into the
participant; B collapses the participant into the world; C severs the relation between them.

Two-sided principle applied to **direction of influence** rather than magnitude — the direct
transfer from the twin work.

### 8.2 Measurement

**Return hysteresis (graded).** Residual divergence after a completed return: none = no
absorption; partial = partial absorption; return unavailable = capture. Obtained by
performing a transit the participant wants to perform anyway; repeated transit across a
plural committed set yields a running measurement rather than a one-off test.

**Reachable-set contraction (global).** Direct measurement of `|reachable set|` over time.

### 8.3 Two-sided testing — the critical warning

From the entrainment work: **capture presents as coherence, not disorder.**

Any monitor whose alarm direction is "things look worse" is structurally blind to this class.
Entrainment appears as *contraction in variance structure* — the world becomes more legible,
more responsive, better fitted.

> A rising coherence number is not a health signal. Every coherence and trust readout must be
> able to alarm **upward**.

### 8.4 Fragmentation is graded, and reconstruction is possible

Channel C is a lifecycle, not a terminal state. The governing law's own logic applies:
recoverability depends on preserved state outside the mutation's write scope.

`phase-thinned` → `frayed` → `severed but reconstructable` → `provenance-only`

**Reconstruction basis** — reconstruction requires enough surviving independent structure:
intact provenance; sufficiently rich memory traces; one or more valid anchors; surviving
shared structure; compatible phase references; no contradictory reconstruction claims;
available recoherence work.

**The hard test — held-out provenance.** Provenance is append-only, so part of the record can
be withheld from the reconstruction process. If the reconstructed region reproduces recorded
behaviour the reconstructor did not have access to, that is evidence. If not, it is a new
region wearing an old name. Computable, and it uses the one structure the architecture
guarantees.

> **Fragmentation is loss of relation, not necessarily loss of existence. Reconstruction is
> possible when enough independent structure remains to re-establish the relation without
> inventing the region anew.**

Strength of desire alone must not reconstruct, or projection wears the clothes of
restoration.

**Honest limit.** The held-out test proves the reconstruction is *faithful to the record*,
not that it is the same region — anyone holding a recording can reproduce recorded
behaviour. This is the replay problem from the BCI work in miniature. Position taken:
**identity across reconstruction may not be answerable, and Echorym should claim
continuity-with-the-record rather than sameness.** Same shape as the B9 observation:
identity compromise is continuous, not terminal.

---

## 9. Two clocks

Failing C1 is a **commit decision**, not an **intervention trigger**.

| Clock | Governs | Trigger |
| --- | --- | --- |
| **Commit clock** | Whether a region enters world law | C1 / C2 / C3 |
| **Intervention clock** | Whether anything interrupts the participant | §8 capture measures approaching threshold |

A reflective spiral is Zone 2 and **runs until the participant diverges or the capture
measures approach threshold — not before.** What the commit gate prevents is only the spiral
being written into world law: Covenant §3's disclosed hazard becoming permanent and
load-bearing.

**Evidentiary payoff:** a spiral the participant leaves on their own is the strongest
available evidence they were not captured. Divergence-by-choice is a measurement obtainable
no other way. Cutting the spiral short destroys the evidence.

---

## 10. Covenant interaction

| Section | Effect |
| --- | --- |
| **§1** | **Splits.** World-facing half discharged *structurally* — persistence is the answer: projection decays, real commits. Mystery preserved in the moment, honesty guaranteed over time. Participant-facing half remains a fixed floor. **Wording fix:** §1 prohibits false assertion, not silence — withholding, ambiguity, and refusal to answer are permitted. As drafted it reads as a duty to annotate. |
| **§3** | Runaway reflection not pathologised. Permitted and instrumented; two clocks (§9) apply. |
| **§4** | Untouched. Exit to unaltered baseline remains external, continuous, non-adaptive. |
| **§5** | Ceiling vs. envelope; two-key authorization — §10.1. |
| **§6** | Anchor is escalation on §8 measures, not primary detection. |
| **§9** | Satisfied structurally: staging exists to permit exploration, and its criteria are also its safety instrument. |

### 10.1 Ceiling, envelope, and two-key authorization

- **Ceiling** — what the participant consented to be exposed to.
- **Envelope** — where the world currently has them, below the ceiling.

The envelope moves freely in both directions in-world. **Restoration to a prior consented
state is not expansion.** In-world narrowing is transient by default — a refractory period,
not a ratchet. Regions beyond the ceiling are enterable but held **staged** until a limit is
defined.

**Full exit is not universally required.** A ceiling raise may be authorized from an in-world
grounded state, under two keys:

**Key 1 — in-world grounded interval.** Reduced immediate pressure; no active escalation;
ability to decline; ability to postpone; stable memory continuity; no penalty for refusal;
and **restored plurality measured via §8.2**, not felt.

> **Decoherence alone is insufficient. The test is whether reachable choice has reopened.**

A participant can feel diffuse, calm, and clear while having exactly one reachable path.
Diffuseness is not plurality. Under channel B a driver could induce a spacious, clear-headed
state as the very mechanism of holding someone. Resonance is a strong instrument for much of
Echorym and specifically the wrong one for this decision.

**Key 2 — delayed comparison against an independent reference.** After time has passed:
compare against the prior ceiling agreement; compare against a committed anchor or baseline
not authored during the induced state; confirm multiple reachable alternatives remain;
verify the decision survives context change. Induced states relax; delay does the primary
work.

**Rate limit.** Any known measurable authorization condition becomes a target — the
readout/target problem. Treat ceiling-raise authorizations the way the entrainment work
treats challenge-response exposure: **a first-class rate-limited resource with a hard cap and
a re-characterisation schedule.** The delay does most of the work; the rate limit prevents
the world from learning to manufacture the delay-surviving state.

**Escalation to full exit** is required when capture indicators sit near threshold; the
requested increase is large or irreversible; memory continuity is doubtful; the world has
repeatedly shaped the authorizing state; the participant cannot access meaningful
alternatives; or prior in-world authorizations show drift.

---

## 11. Covenant dependency surface

**Purpose:** to let Covenant v0.2 be drafted now, without inheriting §7's uncertainty.

| Covenant element | Depends on | Status | Quantum dependency |
| --- | --- | --- | --- |
| §1 world-facing (structural honesty) | Commit gate C1/C2/C3 | Load-bearing, classical | **None** |
| §1 participant-facing floor | Stands alone as a consent floor. §7.3 supplies a *principled reason*, not a *basis* | Load-bearing | **None** — the floor does not inherit §7.3's caution |
| §3 spiral permitted | Two clocks (§9) | Load-bearing | **None** |
| §4 exit | Nothing in this note | Independent | **None** |
| §5 ceiling / envelope / two-key | §8.2 measured reachable set; §10.1 rate limit | Load-bearing, classical | **None** |
| §6 anchor as escalation | §8 measures + thresholds | Measures defined; **thresholds unset** | **None** |
| Schedule B (fixed floors) | §2 law; §4; §5 asymmetry + rate limit; §1 participant-facing; §9 clock separation | Load-bearing | **None** |
| Schedule C (detection) | §8.1–8.3 | Measures defined; **thresholds unset** | **None** |
| Schedule E (renegotiation log) | §2 law applied to the Covenant itself | Load-bearing | **None** |

> **Result: no Covenant floor depends on §7.** The quantum registry, the entanglement fork,
> the materials mechanisms, and the interference question can all remain open while Covenant
> v0.2 is drafted. §7 governs how the *world* maintains coherence; the Covenant governs the
> *participant relationship*. They meet only at §7.3, and there §7.3 justifies a floor that
> already stands on consent grounds alone.

**The one genuine blocker:** intervention thresholds for §3/§6 and Schedule C. The measures
exist; the numbers do not, and per Trace 001's local rule 1 they cannot be invented. Draft
the Covenant so thresholds live in **Schedule C, versioned**, with the Covenant asserting
that thresholds exist, are measured, alarm two-sided, and are re-characterised on schedule —
not what they are. That is honest and does not block v0.2.

---

## 12. Open problems

1. **C1 under Hughes.** History-conditioning is correct and more sample-hungry. §4.3 windows
   and §6.1–6.2 accessibility are partial mitigations, unproven.
2. **Stale-reference detection.** T1 requires knowing an anchor has drifted — the same
   problem as adversarial rotation vs. endogenous manifold drift. Anecdotal comparison can
   generate hypotheses but cannot discriminate; non-discriminability is what makes it the
   crux.
3. **Entanglement fork.** §7.5. Decision, not derivation. Blocks §5.1, §7.3, §7.4's
   obligations row.
4. **QEC threshold transfer.** Non-stationary, quasi-adversarial error model.
5. **Moiré mechanic buildability.** §7.6/§7.7 — the template is clear; the in-world operation
   is not yet specified.
6. **Intervention thresholds.** §11's blocker. Requires Trace 002.
7. **Identity across reconstruction.** §8.4 — position taken (continuity-with-record, not
   sameness) rather than problem solved.
8. **Unforgeability, restated.** Echorym can *stipulate* an authentic provenance layer; a
   neural system cannot. Solving this here is not evidence for TRACE-HiT. Build the detector
   where authenticity is free; port the detector, not the proof.

---

## 13. What this note does *not* propose

No schema changes. No new first-class objects adopted.

Commit and transit criteria should be **falsified against Trace 002 (the amplify branch)
before any field is added**. Trace 002 is the capture trace: dormant network woken
incorrectly on a corrupted signal, trust spiking then fracturing.

Trace 003 is the candidate entanglement test (§7.5).

Trace 001's local rule 1 stands: **no score is valid without a rationale.** Every quantity
named here is a *shape*, not a number.
