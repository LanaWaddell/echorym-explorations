# DN — Staging, Commit, and Phase Travel

**Status:** Design note, draft **v0.4.1**. Not a schema change. No fields proposed for
adoption. Falsification target: Trace 002.
**Evidence:** `RESULT-moire-mechanic-test.md` (simulation: two-register interference,
dephasing sweep, N-region scaling law, CHSH; scripts `moire_test.py`, `moire_test2.py`,
`moire_test4.py`).
**Depends on:** `trace-001-promise-before-passage.md`, `design.md`, First Conduit Covenant
v0.2.
**Relates to:** entrainment-capture work — committed-reference pattern, Kalman twin,
two-sided detection, Hughes-type small-sample failure, challenge-response exposure as a
rate-limited resource.

> **§7 is held for review.** No Covenant floor depends on it (§11).

**Changes from v0.4 (v0.4.1 — evidence update, no new architecture)**

- **§7.5 fork closed on evidence: option (b).** The two-register simulation produced
  Bell-certifiable entanglement (CHSH to the Tsirelson bound) from the twist mechanic
  itself. The same minimal build delivers interference, sharpness, and CHSH, so reserving
  the word is no longer the honest cheaper option — the literal claim is the cheaper option.
- **§7.6 moiré promoted `[candidate]` → `[validated-available]`, with one correction.**
  (Not `[load-bearing]`: the physics is validated as available; in-Echorym status stays
  pending the region → register mapping — promoting further would collapse the §2.2
  possibility-class / commit-state axes.) Two-region
  twist gives smooth interference; **there is no magic angle at N = 2**. Sharp special
  values require many regions, and sharpness scales 1/√N for product-state regions vs
  **1/N for entangled regions** — sharpness is an *entanglement signature*, not decoration.
- **§7.7 closed.** Interference verified: a relational parameter that changes no marginal
  moves the joint outcome by up to 0.25 against the best separable model.
- **§8.2 gains a three-tier relational-integrity measure** from the dephasing sweep. All
  three thresholds are **analytic** (the dephased state is exactly a Werner state with
  visibility v = 1−γ): Bell violation lost at 1 − 1/√2 ≈ 0.293, entanglement at exactly
  **2/3**, interference at 1. The top tier is device-independent. *(An earlier draft of the
  RESULT note quoted grid artifacts ≈0.75/≈0.8 for the middle threshold; corrected on
  independent verification before entering this note.)*
- **§5.1 monogamy unblocked** (pending the build). §7.3's entanglement presupposition
  discharged; its error-model caution stands.
- Open problems renumbered: the fork (was #3) and moiré buildability (was #5) close; the
  **region → register mapping** opens as the gating question for Trace 003.

**Changes from v0.3**

- **§11 table corrected.** Narrowing/capture detection lives in **Schedule F**, not Schedule
  C. Schedule C is breach detection — an outside party turning the system against the
  participant. Capture is the system working as designed. Different failure classes,
  different detection, different escalation; they cannot share a schedule.
- §11 gains rows for the **export ceiling**, module classes, and the governance boundary.
- **§7.10 new** — research modules as coupling channels. Observational modules are
  environmental coupling and therefore a decoherence channel; interventional modules are a
  coherent drive. This is a derivation, not an analogy, and it makes the module system
  load-bearing for §7.
- **§9 expanded** from two clocks to four.
- **§10.1** gains the two-ceiling distinction (perturbation / export) and within-ceiling
  enrollment.
- **§11.2 new** — instrument boundaries: what belongs in the Covenant and what needs a
  separate governance charter.
- **§12 new** — participant-layer disclosure: pool-not-fact, sealed-envelope disclosure,
  class-level specification. One question left open.
- Intentional-incompleteness principle recorded (§2.3).

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

Ontology mutable. Provenance append-only. The single external constraint at the world layer;
everything else here is in-world dynamics.

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
| **I** | Physically demonstrated |
| **II** | Theoretically permitted — consistent with accepted physics, not yet realized in the required form |
| **III** | Mathematically constructible — physical realizability unknown |
| **IV** | Speculative — not yet grounded enough to be treated as law |

**Orthogonality constraint.** Possibility class describes the *real world*. Commit state
describes *Echorym's internal evidence*. Independent axes, not to be collapsed. A Class I
mechanism may sit in-world unearned; a Class IV mechanism may sit in-world committed.
Collapsing them lets real-world provenance route around the commit gate, which is the gate's
entire function.

### 2.3 Intentional incompleteness

> The architecture is intentionally incomplete. It defines a process by which future forms of
> participation, mechanism, and inquiry can be responsibly added, rather than attempting to
> anticipate every future possibility. Stability comes from the process, not from coverage.

This applies at three layers: the recoherence registry (§7.0), the module registry (§11.2),
and the Covenant's own versioning. In each case the instrument stays stable by *not*
absorbing what it governs.

---

## 3. Region lifecycle

| State | Meaning |
| --- | --- |
| `reached` | Encountered. Enterable, interactive, consequential. |
| `staged` | Real and inhabitable; its **authority over the rest of the world** is withheld. |
| `committed` | Canonical. Pending deltas applied. Transition rules updated. Enters the reachable set. |
| `thinned` → `frayed` → `severed` → `provenance-only` | Fragmentation lifecycle — §8.4. |
| `decayed` | Dissolved. The **attempt persists in provenance**; the region does not. |

### 3.1 Staged is orthogonal to location

Staged is a property of the region, not of where the participant is. A staged region can be
inhabited, left, returned to.

**Authority = effect outside itself.** Inside a staged region, full effect — nothing about the
lived experience is provisional. Outside, consequences accumulate as **pending deltas**.

*Worked example.* A region operates on the rule *memory propagates backward*. Staged: the
rule holds inside it, fully. It does not make memory propagate backward world-wide, and the
region cannot become a required waypoint between other regions. On commit, the rule enters
world law.

`decayed` is not erasure. The world remembers *consequential* behaviour, not *successful*
behaviour.

---

## 4. Commit criteria

### C1 — Irreducible dynamics (local)

```
I( response ; region_state | participant_history )
```

**Why history, not current action.** Conditioning on the *current* action fails against a
mirror with memory: if `region_state` accumulates past inputs and the response is a function
of that accumulation, conditional MI is high while the region remains pure projection —
integrated rather than instantaneous. That is what a reflective spiral looks like once it has
run a while.

**Failure mode: Hughes-type small-sample instability.** Dimensionality grows faster than
observations, making independence estimates unstable and typically positively biased.
Off-manifold regions are by construction high-dimensional and sparsely visited, so the
estimator is weakest where the test matters most.

> **Stated honestly:** history-conditioning is the *correct* form and the *more*
> sample-hungry one. The right estimator is worse under Hughes than the wrong one.
> Unresolved; §4.3 and §6.1–6.2 are partial mitigations.

**C1 does not require independence from participant influence** — it requires irreducible
state. Co-creation is a legitimate origin (§8.0), not a failure.

### C2 — Return path exercised (transitional)

The return transit is **performed**, not claimed, during the provisional phase. The test is
only available in the window where it is not yet needed: after commit, reversal is a new
mutation with its own provenance. Graded outcome — §8.2.

### C3 — Plurality preserved (global)

The **reachable set elsewhere has not contracted** while the region was staged.

Sink signatures: previously available transitions elsewhere become unavailable; paths between
other regions route through the staged region; it becomes a mandatory waypoint; response
diversity in unrelated entities narrows.

A region may pass C1 and C2 and fail C3. **Independence is not benignity.**

### 4.1 Three outcomes

| Outcome | When | Consequence |
| --- | --- | --- |
| **Commit with constraint** *(default)* | Sink property traceable to a specific transition rule | Region commits; that rule withheld and logged for revisit |
| **Remain staged** | Evidence insufficient, or participant holds it open | Not free — carries coherence cost and fragmentation exposure. Indefinite staging is a decision with consequences; this is what stops "stage everything" being dominant |
| **Decay** | Cannot meet criteria, not maintained | Dissolves; attempt persists in provenance |

### 4.2 When the sink property *is* the discovery

- **Compensation.** Commit the sink property paired with a mandatory counter-structure
  restoring reachable-set size — alternate route, new anchor, preserved bypass.
- **Mandated internal exit.** Commit with a required anchor *inside* the region holding phase
  to the trunk. Attraction retained; return preserved.

Guardrails as dynamics, not refusal.

### 4.3 Estimation windows

Increased visiting improves sampling **and** changes the region. Estimation cannot outrun this
by raising N when N moves the target.

**Discipline: freeze the reference within an estimation window; allow it to move across
windows; keep every version.**

- *Within* a window — estimate against a frozen reference; C1 is computable.
- *Across* windows — compare references; the delta measures what the visiting did.
- *Retrospectively* — C3 evaluated against any prior baseline once Trace 002 shows which one
  mattered.

The governing law applied to the estimator. Costs a log file.

---

## 5. Commitment is not collapse

Committing a region **adds a basis state**. It is not a measurement.

- **Superposition** = multiple committed regions simultaneously reachable, phase relations
  maintained.
- **Collapse** = the reachable set contracts toward one.

> **Capture is `|reachable set| → 1`.**

Superposition is not maintained by withholding commitment. Withheld commitment is the fragile
form; plural commitment with maintained transit is the durable form.

### 5.1 Monogamy as structural anti-capture — [unblocked; pending build]

If A is maximally entangled with B, A cannot be entangled with C. **A region cannot be
maximally bound to everything.** Anti-capture that is not a rule; principled scarcity for
anchors beyond stipulated no-cloning; the same property underlying QKD security.

The §7.5 fork has resolved toward a real quantum layer (v0.4.1), so this constraint is now
available in principle — classical correlation has no monogamy, and the mechanic verified in
the RESULT note is genuinely entangling. What remains is the build itself and the
region → register mapping (§13.3).

---

## 6. Transit between committed regions

| Criterion | Requirement | Failure meaning |
| --- | --- | --- |
| **T1 — Phase reference valid** | Anchor relating origin and destination is not stale | Transit possible but lossy; divergence not measurable against a stale reference |
| **T2 — Coherence cost paid** | Draws on recoherence throughput (§7) | Cannot transit; region drifts further |
| **T3 — Memory continuity** | Something carries across | Otherwise this is replacement, not travel — the identity-preservation criterion |
| **T4 — Origin remains reachable** | Departure does not remove the return | One-way transit is collapse, not travel |

**An anchor is a phase reference** — a *maintained relation* against which divergence can be
measured rather than merely undergone. This unifies the committed reference in the twin
architecture, the Threshold Stone holding the promise, the designated anchor in Covenant §6,
and the staging mechanism. It also explains `what_it_preserves` / `what_it_constrains`:
maintaining phase coherence with a reference costs freedom of movement.

### 6.1 Off-manifold accessibility as design strategy

Sparse access fails twice over: the world feels narrower than its theory promises, and
Echorym cannot accumulate the observations needed to distinguish irreducible dynamics from
noise. Accessibility is a richness decision *and* an estimation decision.

> **Law: visiting is both measurement and maintenance.**

Mechanisms: shallow recurring access; multiple approach paths; bridge regions; resonant
windows; memory-supported re-entry; shared exploration; staged micro-regions.

### 6.2 Meiboom-Gill alternation

The **MG** in CPMG exists because the refocusing pulses themselves introduce error;
phase-alternating successive pulses makes those errors cancel rather than accumulate.

**Transfer:** alternate the approach path or direction of successive revisits so
visit-induced adaptation cancels rather than accumulates. Testable in the §7.8 simulation. It
is what makes §6.1's accessibility compatible with §4.3's estimation problem rather than
aggravating it.

---

## 7. Coherence — the quantum registry

> **HELD FOR REVIEW.** No Covenant floor depends on this section (§11).

Decoherence is ambient and continuous. Coherence is throughput, not stock: recoherence work
per unit time against ambient decay across the committed set.

### 7.0 Registry format — open and versioned

Not a closed list. New entries may be added whenever research or in-world evidence supplies a
credible mode of coherence maintenance, recovery, protection, or reconstruction.

Entry fields: `mechanism_id`, `name`, `physical_analogue`, `in_world_operation`,
`what_it_preserves`, `what_it_costs`, `required_conditions`, `known_failure_modes`,
`evidence_status`, `date_introduced`, `supersedes_or_extends`, `possibility_class`.

Status: `[load-bearing]` · `[validated-available]` *(physics validated as available;
in-Echorym status pending mapping)* · `[stipulated]` · `[candidate]` · `[not yet earned]` ·
`[retired or narrowed]`.

**Admission test:** *a mapping earns entry only if it supplies a mechanism Echorym lacked,
not vocabulary for something Echorym already has.*

### 7.1 Two rates, not one budget — [load-bearing]

Amplitude damping (state loss, T1) and dephasing (relation loss, T2) are distinct, and
T2 ≤ 2·T1 — dephasing typically far faster.

A region persists and remains enterable (long T1) while its phase relation to the trunk
decays (short T2). **Return becomes lossy before anything is lost.**

- Return hysteresis is a **T2** measurement.
- Reachable-set contraction is a **T1** measurement.

### 7.2 Rate law — CPMG — [load-bearing]

**CPMG = Carr–Purcell–Meiboom–Gill**, repeated refocusing pulses used in magnetic resonance
and quantum control to suppress dephasing from slowly varying noise. Dynamical decoupling of
this kind genuinely extends measured coherence times in spin systems.

**Transit is the pulse.**

> Transit frequency must exceed the correlation frequency of the drift being suppressed.

Falsifiable prediction: frequent shallow revisits outperform rare deep ones.

### 7.3 Currency and threshold — QEC — [load-bearing, one caution]

- **Redundant encoding** = the same relation carried by multiple anchors, cross-referencing
  memory traces, shared structure.
- **Syndrome measurement** = measure relations *between* anchors, never the participant's
  state directly. Supplies the principled reason the relational measurement is the
  permissible one (Covenant §1).
- **Threshold theorem** = a critical anchor redundancy above which recoherence outpaces
  decoherence.

> **Coherence budget = distance to threshold.**

*Caution:* QEC assumes an error model. Echorym's is participant behaviour — non-stationary,
quasi-adversarial. The threshold result may not transfer. *(The mapping's other
precondition — that it presupposes entanglement, §7.5 — is discharged as of v0.4.1; the
error-model caution stands on its own.)*

### 7.4 Recoherence mechanisms

| Mechanism | Physical analogue | Status |
| --- | --- | --- |
| Transit | Refocusing pulse | [load-bearing] §7.2 |
| Alternated approach paths | Meiboom-Gill phase alternation | [load-bearing] §6.2 |
| Cross-referencing memory traces | Redundant encoding | [load-bearing] |
| Anchor re-exercise | Syndrome extraction / stabiliser measurement | [load-bearing] |
| Shared structure between regions | Decoherence-free subspace / correlated noise | [load-bearing] |
| Obligations spanning regions | Nonseparable relational constraint | [not yet earned] — §7.5 fork closed; in-world earning awaits Trace 003 |
| Topological protection | Non-local invariance | [candidate] §7.6 |
| Superconducting phase coherence | Macroscopic phase, Josephson coupling | [retired or narrowed] |

*Trace 001:* the promise is a coherence-maintaining structure. **Calling a promise due is
recoherence work.**

### 7.5 Entanglement — fork closed: option (b) *(v0.4.1)*

Entanglement's content is that **the states of parts are incomplete descriptions and the
relation carries irreducible state** — Echorym's thesis stated in physics.

**The earning test must be Bell/CHSH, not dependence.** Conditional dependence, mutual
information, non-factorizability, and joint-state irreducibility are **all satisfied by
ordinary classical correlation**. If those become the test, Echorym demonstrates entanglement
on day one and the word means nothing. The real boundary is correlations exceeding any local
hidden-variable model — binary rather than interpretive, and familiar from QKD.

**The fork is closed on evidence, not preference.** The v0.3/v0.4 options were (a) reserve
the word and name the mechanic *correlation*, or (b) build a small quantum layer where the
claim is literal. The RESULT note settles it: the minimal two-register twist mechanic
*already produces* Bell-certifiable entanglement — CHSH violation across essentially the
whole twist range, reaching the Tsirelson bound (2√2) at θ = π — and the same build delivers
interference and sharpness. Option (a)'s rationale was honesty at lower cost; the simulation
shows the literal claim **is** the lower-cost option, since one small build discharges §7.5,
§7.7, and §5.1 together. Decision: **(b)**.

What (b) unlocks, now confirmed rather than projected: monogamy (§5.1), entanglement
witnesses, reduced density matrices, stabiliser correlations, and the §7.3 QEC mapping's
entanglement presupposition.

**In-world mechanic:** joint transition rules; consequences not assignable to one side;
correlated mutations; shared memory duplicated in neither participant; phase-dependent
constructive or destructive joint effects; separation without independence.

**Earning conditions in-world (unchanged — the physics demo does not discharge these):** a
joint state not representable as separate local states; a joint consequence neither region
produces alone; a phase relation affecting outcome; a measurement structure observing
relational syndromes rather than reading each entity.

Design test for **Trace 003**, whose physics substrate is now verified and whose
falsification criteria are quantitative (§8.2's three tiers). The gating design question is
the **region → register mapping** (§13.3).

### 7.6 Materials-derived mechanisms

**Topological protection — [candidate], highest priority.** Information stored in global
structure, invariant under any local operation. Supplies *non-local invariance*, which
Echorym has nowhere else. In-world: locally damaged regions whose global identity remains
intact; paths protected by topology rather than walls; anchors distributed across a structure;
mutations not undoable by changing one local component. Also what the surface code *is*, so
it unifies anchors, QEC, and anti-capture in one object.

**Moiré — [validated-available] *(promoted from candidate, v0.4.1)*. Closes the
interference gap — with one correction.** Two layers, a twist angle, emergent correlated phases present in neither
parent. **Twist angle is the phase relation** — continuously tunable, verified in
simulation: applied as a purely relational parameter that changes no single region's
marginal, it moves the joint outcome by up to 0.25 against the best separable model, and the
effect dies exactly as the phase relation dephases.

*Correction from the test:* **there is no magic angle at N = 2.** Two-region twist gives
smooth, sinusoidal interference. Narrow features require **many** regions, and how feature
width scales is diagnostic: product-state regions sharpen as 1/√N (shot-noise limit);
entangled regions sharpen as 1/N (Heisenberg limit), both constants holding to four
significant figures across six octaves in simulation. The entangled fringe has N narrow
peaks per period — not one privileged angle, so "magic angle" (a single isolated value from
band flattening, a different mechanism) remains strictly metaphor. **Narrow interference
features are an entanglement signature** — evidence of nonseparable relation across
regions, not decoration on top of it. This merges what v0.3/v0.4 tracked as two separate
open problems (§7.5 and §7.7): the interference mechanic and the entanglement earning test
are the same phenomenon measured two ways.

In-world: two ordinary regions overlap at a slight relational twist and produce a third
ontology; microscopic alignment changes produce large emergent consequences; phase diagrams
become world maps; strain becomes a control parameter — and a narrowly-tuned emergent
region implies, measurably, that the regions producing it are entangled.

**Frustration / strong correlation — [candidate].** Massive ground-state degeneracy: the
system does not collapse to one configuration *because of its structure*, not because a rule
forbids it. `|reachable| > 1` maintained without enforcement — guardrails-as-dynamics in
physical form.

**Defects and colour centres — [candidate].** Defects can be controllable emitters, sensors,
spin memories, network nodes, with optically addressable spins and long coherence times.
In-world: scars becoming anchors; damage as interface rather than degradation.

### 7.7 Interference — **closed and verified** *(v0.4.1)*

The gap named in v0.2 ("without interference there is no superposition, only a menu with a
fancy name") is discharged: the simulation demonstrates joint effects neither region
produces alone, determined by the phase relation, not reproducible by any classical mixture
with the same marginals, and destroyed by relational dephasing. What remains open is not the
mechanic but the **region → register mapping** (§13.3) — how a world-region's character
becomes a register state.

### 7.8 Simulability

Density-matrix-like object over regions: diagonal = reachability, off-diagonal = phase
relations, decaying at 1/T2, refreshed by transit, Lindblad-style update. Small numpy build.
Tests §7.2's rate law and §6.2's alternation prediction. With the fork closed to (b), the
extension to real state vectors and CHSH evaluation is confirmed viable — the RESULT note's
scripts already implement its two-register core. Candidate companion to Trace 002.

### 7.9 Neural perturbation — two claims, kept separate

**Perturbation alters cognitive and network state — [Class I, supportable].** Stimulation
effects depend strongly on the brain's starting state; perturbation can alter attention,
perception, network dynamics, conscious state. In-world: widening or redirecting the
accessible manifold; destabilising rigid attractors; synchronising or desynchronising
networks; temporary windows for phase access; supporting recoherence after fragmentation.

**Perturbation inducing functionally relevant quantum states in neural tissue — [Class IV,
not yet earned].** Hypotheses exist; convincing evidence for controllable, functionally
relevant neural entanglement or long-lived brain-wide coherence does not.

**Safe architecture, stated strictly:** the neural state controls a *classical parameter* that
configures a quantum system. Not "neural-quantum coupling" — that phrasing implies more than
is established and would cost credibility with exactly the audiences the QKD and TRACE-HiT
work depends on.

### 7.10 Research modules as coupling channels — [load-bearing] *(new in v0.4)*

Decoherence *is* information leaking to the environment — system-environment entanglement
destroying the system's phase relations. This makes the module classes physically distinct
rather than administratively distinct.

**An observational module is an environmental coupling.** Data flowing outward to external
researchers is the decoherence channel. Not a metaphor bolted onto §7 — the same mechanism.

> **Derived cost: each additional observational module raises the ambient decoherence rate.**
> More disciplines observing → faster phase decay → more recoherence work required to hold
> the same committed set.

The participant therefore has a reason to be selective that is native to the world rather
than a warning screen. It is also honest: being observed by six research programs genuinely
does change one's relationship to the experience.

**Testable prediction.** Heavy multi-module enrollment should require measurably higher
transit frequency to maintain the same reachable set. Falls directly out of §7.2's rate law
and is testable in the §7.8 simulation.

**An interventional module is not environmental coupling — it is a coherent drive.** It has an
objective function and shapes responses toward it. Different physics: this is Channel B
(§8.1), with a research protocol as the driver.

Consequences:

1. Interventional modules are instrumented by the §8 measures like any other world dynamic.
2. **Research objectives can never override the intervention clock** (§9). Covenant §9 fixed
   floor.
3. An AI proposing an interventional module is an AI designing a driver, and gets the same
   instrumentation and the same independent review.

Note what this establishes: the participant's intuitive outbound/bidirectional distinction
lands on exactly the boundary the architecture already draws between decoherence and capture.
Independent arrival at the same line is evidence the distinction is real rather than
administrative — and it makes the module system load-bearing for §7 rather than an appendix.

*Rate calibration is unset.* The mechanism is derived; the coefficient is not (§13.9).

---

## 8. Origin taxonomy and capture channels

### 8.0 Four origins

| Origin | Meaning | Evidence requirement |
| --- | --- | --- |
| **Discovery** | Dynamics prior to contact | C1 against early-window reference |
| **Co-creation** | Irreducible dynamics developed *through* relationship | C1 satisfied at current window though early windows show participant-driven formation. **Legitimate — arguably central** |
| **Reconstruction** | Re-established from a preserved basis after fragmentation | §8.4 held-out provenance test |
| **Projection** | A mirror, however elaborate | C1 fails at all windows |

Co-creation and reconstruction must be first-class, or co-emergent regions fail C1 by
default — addressed by classification rather than by weakening the test.

### 8.1 Three capture channels

| Channel | Mechanism | Detector | Timing |
| --- | --- | --- | --- |
| **A — Projection** | Region never had its own dynamics | C1: `I(response ; region_state \| participant_history) ≈ 0` | Pre-commit |
| **B — Absorption** | Region has strong real dynamics and *because of that* becomes an attractor that cannot be left | Reverse: `I(participant_action ; participant_state \| region_state) ≈ 0` | Post-commit, continuous |
| **C — Fragmentation** | Relation binding region to trunk decayed below clean return | T2 / return hysteresis | Continuous |

**Passing C1 is not protection against B — it is closer to a precondition.** You cannot be
entrained by an echo; entrainment requires a real external driver.

Unifying definition: `|reachable| → 1`. A collapses the world into the participant; B
collapses the participant into the world; C severs the relation between them.

Two-sided principle applied to **direction of influence** rather than magnitude.

### 8.2 Measurement

**Return hysteresis (graded).** Residual divergence after a completed return: none = no
absorption; partial = partial absorption; return unavailable = capture. Obtained by
performing a transit the participant wants to perform anyway; repeated transit yields a
running measurement.

**Reachable-set contraction (global).** Direct measurement of `|reachable set|` over time.
This is also the measure Covenant §5 Key 1 depends on.

**Three-tier relational integrity** *(new in v0.4.1, from the dephasing sweep).* Under
relational dephasing γ, three properties fail in fixed order, giving a graded measure of how
intact the relation between two regions is:

All three thresholds are **analytic**, not empirical — the dephased state is exactly a
Werner state with visibility v = 1−γ (verified to machine precision):

| Tier | Lost at (exact) | Meaning |
| --- | --- | --- |
| **Bell violation** | γ = 1 − 1/√2 ≈ 0.293 | The relation is certifiably nonclassical — **device-independent**: no model of the regions' internals is trusted |
| **Entanglement** (concurrence > 0) | γ = **2/3** | The relation still carries irreducible joint state |
| **Interference** (twist dependence) | γ = 1 | The relation still produces any joint effect at all |

The ordering is the useful part: a relation can lose certifiability long before it loses
effect, so "still working" and "still trustworthy" come apart measurably. The top tier is
the only measure in this note that requires trusting nothing about how the regions are
implemented. Candidate refinement of return hysteresis once the quantum layer exists;
entirely dependent on the region → register mapping (§13.3).

### 8.3 Two-sided testing — the critical warning

**Capture presents as coherence, not disorder.** Any monitor whose alarm direction is "things
look worse" is structurally blind to this class. Entrainment appears as *contraction in
variance structure* — the world becomes more legible, more responsive, better fitted.

> A rising coherence number is not a health signal. Every readout must be able to alarm
> **upward**.

### 8.4 Fragmentation is graded, and reconstruction is possible

`phase-thinned` → `frayed` → `severed but reconstructable` → `provenance-only`

**Reconstruction basis:** intact provenance; sufficiently rich memory traces; one or more
valid anchors; surviving shared structure; compatible phase references; no contradictory
reconstruction claims; available recoherence work.

**The hard test — held-out provenance.** Provenance is append-only, so part of the record can
be withheld from the reconstruction process. If the reconstructed region reproduces recorded
behaviour the reconstructor did not have access to, that is evidence. If not, it is a new
region wearing an old name.

> **Fragmentation is loss of relation, not necessarily loss of existence. Reconstruction is
> possible when enough independent structure remains to re-establish the relation without
> inventing the region anew.**

Strength of desire alone must not reconstruct, or projection wears the clothes of
restoration.

**Honest limit.** The held-out test proves fidelity *to the record*, not sameness — anyone
holding a recording can reproduce recorded behaviour. The replay problem in miniature.
Position taken: **claim continuity-with-the-record rather than sameness.** Same shape as the
B9 observation — identity compromise is continuous, not terminal.

---

## 9. Four clocks *(expanded in v0.4)*

Different review and decision functions run on different timescales. Collapsing them into one
authority produces contradictions.

| Clock | Governs | Authority | Timescale |
| --- | --- | --- | --- |
| **Intervention** | Whether anything interrupts the participant | Automated measures + designated anchor | Seconds–minutes |
| **Commit** | Whether a region enters world law | C1 / C2 / C3 | Sessions–estimation windows |
| **Design** | Whether a module or hypothesis may exist and be offered | REB / TCPS 2 + independent reviewer | Weeks–months |
| **Governance** | Whether the Covenant itself changes | Participant + operator, versioned, append-only | Years |

**Why the REB cannot serve as the out-of-loop observer.** REBs review protocols, renew
annually, and receive adverse-event reports. They do not monitor sessions. The REB covers the
Design clock well — including AI-generated hypotheses, since a proposed module arriving as a
protocol *is* the independent scrutiny missing when the reviewing researcher is also the
principal — but it cannot touch Intervention. Putting a months-long reviewer on a
seconds-long trigger fails by construction.

**Commit ≠ intervention.** Failing C1 is a commit decision, not an intervention trigger. A
reflective spiral is Zone 2 and **runs until the participant diverges or the capture measures
approach threshold — not before.** What the commit gate prevents is only the spiral being
written into world law.

**Evidentiary payoff:** a spiral the participant leaves on their own is the strongest
available evidence they were not captured. Divergence-by-choice is a measurement obtainable
no other way; cutting the spiral short destroys it.

---

## 10. Covenant interaction

| Section | Effect |
| --- | --- |
| **§1** | **Splits.** World-facing half discharged *structurally* — persistence is the answer. Participant-facing half remains a fixed floor, strengthened by the relational-measurement principle (§7.3). **Wording fix applied in v0.2:** §1 prohibits false assertion, not silence. |
| **§3** | Runaway reflection not pathologised. Permitted and instrumented; §9 clocks apply. |
| **§4** | Protection untouched. Wording clarified in v0.2 — the obligation is to know the exit, not to use it. |
| **§5** | Two ceilings; two-key authorization; rate limit — §10.1. |
| **§6** | Anchor is escalation on §8 measures, not primary detection. Version-bound; unavailable-anchor is a defined state. |
| **§8** | Withdrawal asymmetry: exported data cannot be recalled. Drives §10.1's export ceiling. |
| **§9** | Research objectives never override the intervention clock. Fixed floor. |
| **§10** | Modules — §10.1, §7.10, §12. |

### 10.1 Ceilings, envelope, and authorization *(revised in v0.4)*

**Two ceilings:**

- **Perturbation ceiling** — what the world may do to the participant.
- **Export ceiling** — what may leave, to whom, under what conditions, for how long.

**Envelope** — where the world currently has them, at or below the perturbation ceiling. Moves
freely in both directions in-world; **restoration to a prior consented state is not
expansion**; tightening is immediate, needs no process, and is transient by default rather
than a ratchet.

**Two keys to raise either ceiling:**

- **Key 1 — grounded interval.** Reduced pressure; no active escalation; ability to decline
  and postpone; stable memory continuity; no penalty for refusal; and **measured reopening of
  the reachable set (§8.2)**, not felt state. *Decoherence alone is insufficient; the test is
  whether reachable choice has reopened.* A participant can feel diffuse and unbound while
  having exactly one reachable path, and under channel B a driver could induce a spacious,
  clear-headed state as the mechanism of holding them. Resonance is the wrong instrument here.
- **Key 2 — delayed comparison against an independent reference.** Compare against the prior
  agreement and against a reference not authored during the induced state; confirm
  alternatives remain; confirm the decision survives context change. Induced states relax;
  delay does the primary work.

**Rate limit.** Ceiling raises are a first-class rate-limited resource with a hard cap — any
known measurable authorization condition becomes a target.

**Escalation to full exit** where indicators sit near threshold; the increase is large or
difficult to reverse; memory continuity is doubtful; the world has repeatedly shaped the
authorizing state; alternatives are inaccessible; or prior authorizations show drift.

**Module enrollment: the invariant is inducement-resistance, not location.** Discovery,
explanation, and registration of interest are all in-world. What matters is that the
participant cannot be brought to commit in a single moment or a single state.

**Whether an enrollment is a ceiling raise depends on the module's terms, not on its being a
module.** Standing export terms set in advance define the export ceiling. A module falling
inside both ceilings is a within-ceiling enrollment: two keys, delay, nothing further. A
module exceeding either is a raise and takes §5 in full, including exit where the increase is
difficult to reverse.

Two constraints:

- **Standing terms must be testable.** "Data may go to researchers" cannot be compared to a
  module's profile; a specific export profile can. Untestable terms are not a ceiling.
- **Standing terms are not consent to unnamed modules.** They constrain what any module may
  do; they never replace being told which module is being joined. Different axes — collapsing
  them reintroduces the broad-consent problem through the side door.

---

## 11. Covenant dependency surface

### 11.1 Dependency table *(corrected in v0.4)*

| Covenant element | Depends on | Status | Quantum dependency |
| --- | --- | --- | --- |
| §1 world-facing (structural honesty) | Commit gate C1/C2/C3 | Load-bearing, classical | **None** |
| §1 participant-facing floor | Stands alone as a consent floor. §7.3 supplies a *principled reason*, not a *basis* | Load-bearing | **None** — does not inherit §7.3's caution |
| §3 spiral permitted | §9 clock separation | Load-bearing | **None** |
| §3 / §6 narrowing detection | §8.1–8.3 measures → **Schedule F** | Measures defined; **thresholds unset** | **None** |
| §4 exit | Nothing in this note | Independent | **None** |
| §5 perturbation ceiling / envelope / two keys | §8.2 measured reachable set; §10.1 rate limit | Load-bearing, classical | **None** |
| §5 **export ceiling** | §8 withdrawal asymmetry; testable standing terms (Schedule A) | Load-bearing, classical. **Open: terms not yet written to a testable standard** | **None** |
| §6 anchor as escalation | §8 measures + thresholds; version binding | Measures defined; **thresholds unset** | **None** |
| §7 breach detection | Adversary model, distinct from capture → **Schedule C** | Independent of this note | **None** |
| §8 withdrawal asymmetry | §2 law; export irreversibility | Load-bearing | **None** |
| §9 research subordination | §7.10 (interventional = driver) + §9 clocks | Load-bearing | **None** — §7.10's *classification* is used, not its rate law |
| §10 observational modules | §7.10 decoherence coupling | Mechanism derived; **coefficient unset** | Uses §7 but no Covenant *floor* rests on it |
| §10 interventional modules | §7.10 → Channel B → §8 measures | Load-bearing, classical | **None** |
| Schedule A (data + export terms) | §2 law; per-signal authorization tags | Load-bearing | **None** |
| Schedule B (fixed floors) | §2 law; §4; §5 asymmetry + rate limit; §1 participant-facing; §9 clock separation | Load-bearing | **None** |
| Schedule C (breach) | Adversary model | Independent | **None** |
| Schedule D (anchor brief) | §6; version binding; unavailable-anchor state | Load-bearing | **None** |
| Schedule E (limits + renegotiation log) | §2 law applied to the Covenant itself | Load-bearing | **None** |
| Schedule F (narrowing detection) | §8.1–8.3 | **Thresholds unset — the one genuine blocker** | **None** |
| Schedule G (module registry) | §10; §11.2; Design clock | Framework defined; not operable pre-REB | **None** |

> **Result: no Covenant floor depends on §7.** This held while the fork was open, and it
> holds now that v0.4.1 has closed the fork and verified interference — the resolutions
> strengthen §7 without any Covenant floor coming to rest on it. The remaining §7 openings
> (the region → register mapping, QEC threshold transfer, the decoherence coefficient) can
> stay open indefinitely without touching the Covenant. §7 governs how the *world* maintains
> coherence; the Covenant governs the *participant relationship*. They meet at §7.3, where
> QEC justifies a floor already standing on consent grounds, and at §7.10, where the
> Covenant uses the module *classification* rather than the decay rate.

**Schedule C / Schedule F.** v0.3 mapped narrowing detection to Schedule C. That was wrong.
Schedule C is breach — an outside party turning the system against the participant. Narrowing
is the system working as designed. Different failure class, different detection, different
escalation, different notification obligation. They cannot share a schedule without one
inheriting the other's assumptions.

**The one genuine blocker:** intervention thresholds (Schedule F). Measures exist; numbers do
not, and rule 1 forbids inventing them. The Covenant asserts that thresholds exist, are
measured, alarm two-sided, and are re-characterised on schedule — not what they are. Honest,
and does not block v0.2.

### 11.2 Instrument boundaries *(new in v0.4)*

The Covenant's authority comes from being a **consent instrument between two parties** — it
binds because both agreed and the record holds. Governing future researchers, collaborators,
AI systems, and disciplines is a different authority: **organizational policy**, which binds
because an organization adopted it.

These must not share a document. A participant cannot consent to how a discipline that does
not yet exist will be governed, and a researcher is not bound by a participant's agreement.

| Instrument | Parties | Clock | Contents |
| --- | --- | --- | --- |
| **Covenant** | Participant ↔ operator | Governance (years) | Participation, data, safety, the two ceilings, anchor, withdrawal, participant-facing module terms |
| **Governance charter** | Operator ↔ researchers, collaborators, AI systems | Design (weeks–months) | Module approval, hypothesis review, independent reviewer, publication policy, data use agreements |
| **Module registry (Schedule G)** | Per-module | Design | Purpose, class, data, risks, collaborators, ethics status, withdrawal |

The Covenant references the charter; it does not absorb it. This is what lets the Covenant
stay stable while module governance moves faster — the intentional-incompleteness principle
(§2.3) applied at the instrument level.

**Corollary.** The observation that the Covenant has begun protecting Echorym's *evolution*
rather than only protecting participants *from* Echorym is correct, and is best served by a
second instrument rather than a larger first one. The Covenant protects the evolution by not
absorbing it.

---

## 12. Participant-layer disclosure *(new in v0.4)*

The world-layer question — what is real here — is discharged structurally by the commit gate.
The participant-layer question is different: **what may be withheld from the participant about
their own situation?**

**Settled: consent to the pool, blind the draw.** A participant registers interest, passes
authorization, and enters the pool for a module. They then need not know whether it is live in
a given session, which sessions contributed, whether their contribution mattered, or which of
several modules is currently shaping the world. **Content and timing may be blinded; the fact
of participation may not.**

The retained bit is small and load-bearing: Covenant §4 (exit), §5 (both keys), §6 (anchor
brief currency), and §8 (withdrawal) all become undefined without it. You cannot exit, set a
limit, brief an anchor, or withdraw from something you do not know you are in. Standard trial
design already works this way — subjects know they are in a trial and not which arm.

**Bonus, treated as a feature:** pool membership becomes a first-class world object. Knowing
you are in three pools without knowing what is running is richer uncertainty than not knowing
at all, because it can be held and reasoned about.

**Available techniques for preserving novelty without withholding the fact:**

- **Sealed-envelope disclosure.** Full specification available at any moment; reading it is
  not required. Available-but-unread is a different property from unavailable.
- **Class-level specification.** "You will encounter regions with these properties" without
  naming which, when, or in what order. The category is consented; the instance stays unknown.
- **Time separation.** Consent well in advance and let ordinary forgetting operate. Unreliable
  — which is why it is acceptable: nothing was induced, and the participant can always look.

**C1 is the novelty guarantee.** A region with irreducible dynamics is by definition not fully
predictable from its specification, so a fully informed participant still discovers. If the
world requires participant ignorance in order to feel exploratory, that is a weakness in the
world rather than a problem to engineer around in the participant.

**Open — §13.10.** Whether any form of induced or pre-consented reduction in the participant's
memory of consenting could be made compatible with §4, §5, and §6. Current position: it
cannot, because it removes the reference both keys compare against and severs the participant
from the commitment the mast exists to hold them to; and no technique selectively removes one
autobiographical fact while leaving decision-making competence intact. Recorded as open at the
participant's request rather than closed.

---

## 13. Open problems

1. **C1 under Hughes.** History-conditioning is correct and more sample-hungry. §4.3 and
   §6.1–6.2 are partial mitigations, unproven.
2. **Stale-reference detection.** T1 requires knowing an anchor has drifted — the same problem
   as adversarial rotation vs. endogenous manifold drift. Anecdotal comparison can generate
   hypotheses but cannot discriminate; non-discriminability is what makes it the crux.
3. **Region → register mapping.** *(Replaces the entanglement fork, closed v0.4.1.)* The
   mechanic is verified; what is entirely unspecified is how a world-region's character
   becomes a register state. Everything §7.5–§7.7 now promises — monogamy, the three-tier
   measure, magic-angle features — is contingent on this mapping being meaningful rather
   than decorative. **The gating design question for Trace 003.**
4. **QEC threshold transfer.** Non-stationary, quasi-adversarial error model.
5. ~~Moiré mechanic buildability~~ **Closed v0.4.1** — mechanic verified in simulation
   (RESULT note). The residue folds into #3.
6. **Intervention thresholds.** Schedule F. The one Covenant blocker. Requires Trace 002.
7. **Identity across reconstruction.** §8.4 — position taken, not problem solved.
8. **Export ceiling testability.** §10.1 — standing terms must be written specifically enough
   for a module profile to be mechanically compared against them. Not yet drafted.
9. **Module decoherence coefficient.** §7.10 — mechanism derived, rate unset. What does one
   additional observational module cost in transit frequency?
10. **Participant memory and novelty.** §12 — open at the participant's request.
11. **Unforgeability, restated.** Echorym can *stipulate* an authentic provenance layer; a
    neural system cannot. Solving this here is not evidence for TRACE-HiT. Build the detector
    where authenticity is free; port the detector, not the proof.

---

## 14. What this note does *not* propose

No schema changes. No new first-class objects adopted.

Commit and transit criteria should be **falsified against Trace 002 (the amplify branch)
before any field is added**. Trace 002 is the capture trace: dormant network woken incorrectly
on a corrupted signal, trust spiking then fracturing. **Modules stay out of Trace 002** — it
tests C1/C2/C3 and nothing else; what it needs from the module work is a minimal encounter
schema so a module can be referenced as a world object, not the governance framework.

**Trace 003** carries two tests: the entanglement earning test (§7.5) and the
observational-module decoherence test (§7.10) — enrollment measurably degrading phase
relations. Both are §7 tests, which is why they belong together. As of v0.4.1 the physics
substrate for the first is verified and its falsification criteria are quantitative (the
§8.2 tiers); what Trace 003 must supply is the in-world demonstration through the schemas,
which requires the region → register mapping (#3) — the trace's actual design content. The
physics demo does not substitute for the trace.

Trace 001's local rule 1 stands: **no score is valid without a rationale.** Every quantity
named here is a *shape*, not a number.
