Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# DN-quantum-world-register-commitment v0.1: what the register is

Status: draft, adversarial half. World-side blanks marked `[ECHO]`. Decision fields marked `[LANA]`.
Date: 2026-09-07.
Disclosure: private register until the coherence measurement framework and DN-staging-and-phase-travel-v0.4.1 are published. This note inherits the status of its most-restricted dependency.
Governs: Stage 2 of the quantum-world series. Stage 2 does not begin until §11 is filled.
Sources (internal, unpublished): DN-staging-and-phase-travel-v0.4.1 (§3, §4, §5, §6, §7, §13), RESULT-moire-mechanic-test, DN-quantum-world-stage1-history-pair-state, DN-quantum-world-placement, quantum-state-space-gates-and-circuits. Nothing quoted; everything relied on is restated here.
Class IV boundary: unchanged. Nothing below is about neural, human, or narrative state. Registers are mathematical objects; world meanings attached to them are interpretations, and this note is the place where those interpretations get committed to on purpose rather than by default.

---

## 0. What this note is

Open problem 3 of the staging note asks how a world-region's character becomes a register state. This note does not solve it. It does three narrower things: records what the world has *already* committed to about its register, in documents that predate the quantum-world series; shows that the series has so far built a register that only partly matches those commitments; and lays out the decision that Stage 2 forces, with the options, their costs, and what would reject each.

The Cowork question set of 2026-09-07 posed four commitment questions as if from a blank page. They are the right questions. But the staging note answers two of them and half-answers a third, so the world-side reviewer should start from those answers, not from nothing.

---

## 1. Finding: two registers already exist, and they are not the same object

**Register H (histories).** `echorym_qstate.py`, Stage 1. A single two-level system in basis {|A⟩, |B⟩}, where A and B are two alternative histories. Diagonal = retention; off-diagonal = relational coherence. Superposition means one thing is coherently in two histories. There is one subsystem and no entanglement is possible.

**Register R (regions).** `moire_test*.py`, RESULT note, staging note §7.5–§7.8. One qubit per region, two regions, a twist angle between them as the phase relation. Superposition means two regions hold a maintained phase relation; entanglement is possible and was verified (CHSH violation to the Tsirelson bound at θ = π). Diagonal of the joint state = reachability of each region, per §7.8.

These are not two views of one thing. Register H is a qudit-over-alternatives at dimension 2; Register R is a tensor product of local systems at N = 2. They coincide numerically only because both are small. Stage 2 as written in the placement note — "d histories, a qudit" — grows Register H. The world's verified interference and entanglement results live in Register R. If Stage 2 proceeds as planned, the series diverges from the only register the world has actually tested.

The placement note's own instruction — that the entanglement-to-geometry layer should build on the moiré RESULT rather than a fresh toy — applies one stage earlier than the note places it.

**Consequence.** The first decision is not "which of three structures" but "what is the relation between H and R." §3 gives four candidates, two of which are composites.

---

## 2. What the world has already committed to

Restated from the staging note, so this document stands alone. These are world-side facts, not physics, and any register must express them or the register is rejected.

| # | World commitment | Source | Register consequence |
|---|---|---|---|
| W1 | Committing a region **adds a basis state**; commitment is not a measurement. | §5 | The basis grows over time. The register must admit dimension growth at commit without rewriting prior state. |
| W2 | Superposition = multiple committed regions simultaneously reachable with maintained phase relations. Collapse = the reachable set contracts toward one. **Capture is \|reachable\| → 1.** | §5 | "Reachable set" must be a computable property of the state — a support, not a label. |
| W3 | An anchor is a maintained phase reference; divergence is measured against it, not merely undergone (T1). Stale reference → transit lossy. | §6 | Relative phase is *relative to an anchor*, so the register needs a designated reference state or subsystem. |
| W4 | Transit re-establishes a region's phase relation to the trunk. Visiting is both measurement and maintenance. Meiboom-Gill alternation is already invoked for refocusing pulses. | §6, §7 | Transit is a refocusing operation. Refocus already has a world referent. |
| W5 | Decoherence is ambient and continuous; coherence is throughput, not stock; regions sharing entities, signals, or rules are cheaper to hold in relation. | §7 | Environment coupling is always on; shared structure lowers the effective decay rate between specific pairs. |
| W6 | Observational modules enrolled against a region measurably degrade its phase relations (Trace 003 test). Pool-not-fact enrollment. | §7.10, §13.9 | A module is an environment subsystem with a record. Stage 1 already gave this form: V_E × (1 − d) per module. |
| W7 | Two regions overlapping at a slight relational twist produce a joint effect neither produces alone; effect dies exactly as the phase relation dephases; sharp special values require many *entangled* regions (width ∝ 1/N, not 1/√N). | §7.6, RESULT F4–F5 | Recombination has a world referent — region overlap — and its signature is a joint outcome not reproducible by any separable model with the same marginals. |
| W8 | Monogamy is wanted as structural anti-capture: a region cannot be maximally bound to everything. | §5.1 | Requires genuine subsystems. A single qudit has no monogamy. |
| W9 | Three-tier relational integrity: Bell violation (Werner threshold 0.293) → entanglement (0.75) → interference (1.0). Top tier device-independent. | RESULT | Requires a bipartite register with local measurements. |
| W10 | The exponential memory wall is absolute; scaling is many small independent cores, not one growing core. | key learnings | A full tensor product over all regions is not a runnable architecture beyond ~20 regions. |

W1 and W2 pull toward a qudit-over-regions (Register H with histories = regions). W7, W8, W9 require subsystems (Register R). W10 forbids the naive N-fold tensor product. No single candidate from the Cowork set satisfies all ten.

---

## 3. Candidates

Presented by decision variables, not as rivals. The variables: **(i)** number of subsystems; **(ii)** local dimension; **(iii)** whether a constraint subspace removes impossible combinations; **(iv)** how the basis grows at commit (W1); **(v)** how overlapping regions share degrees of freedom (W5, W7).

### A. Single qudit over regions

One register whose basis states are committed regions. |ψ⟩ = Σ_i c_i |region_i⟩. Reachable set = support of the diagonal. Capture = diagonal → one entry. Commit = append a basis vector.

- Expresses cleanly: W1, W2, W3 (anchor = a designated basis state or reference vector), W4 (transit = phase rotation toward the anchor).
- Cannot express: W7 as verified (moiré is bipartite), W8 (no subsystems, no monogamy), W9 (no local measurements).
- Cost: linear in number of regions. Immune to W10.
- Stage 2 under A: d-region qudit; multi-slit visibility bound. Exactly the placement note's Stage 2.
- **Rejection test:** any world event that requires a joint state of two regions not representable as one location in superposition — a correlated mutation, a shared memory duplicated in neither region — rejects A. The staging note §7.5 lists these as *earning conditions*, so A is rejected by the world's own criteria unless those conditions are dropped.

### B. One local system per region (tensor product)

Each region carries a local space (dimension ≥ 2); the joint register is their tensor product. Entanglement, monogamy, and Bell tests are native. This is Register R.

- Expresses cleanly: W7, W8, W9, W6 (a module couples to one factor).
- Strains: W1 (commit = adjoin a factor; fine), W2 (reachable set is not a support — it must be defined as e.g. which factors are in a "reached" state, requiring a constraint or a chosen local basis with world meaning), W10 (2^N).
- What the local basis *means* is unspecified. "Reached / not reached" is one candidate; "which history this region is in" is another; these are different worlds. `[ECHO]`
- Cost: exponential in N. Runnable to N ≈ 16–20 in numpy; the RESULT note ran N = 128 only for product and specific entangled families, not general states.
- Stage 2 under B: N-region extension of the moiré core; visibility–entanglement bound; the 1/N sharpness result re-derived as a coherence measure. Builds on existing verified code.
- **Rejection test:** if the joint basis contains combinations the world forbids (e.g. every region simultaneously "reached" when the world has one participant), and no constraint is written to remove them, B is rejected — the register would carry states with no world meaning and Stage 2's bounds would be bounds over nothing.

### C. Composite: location register ⊗ region factors

A qudit for *where the participant is* (candidate A) tensored with a small local system per region (candidate B). The location qudit carries W1–W4; the region factors carry W7–W9. Modules (W6) couple to region factors. Overlap (W7) is a joint operation on two factors conditioned on the location register.

- Expresses: everything in §2 except W10, which it makes worse.
- This is what Stage 1 and the moiré core would be if they were one program: Stage 1 is the location qudit at d = 2, the moiré core is two region factors.
- Cost: d × 2^N. The W10 fix is the "many small cores" architecture — region factors are not one global tensor product but a set of small entangled clusters (pairs, triples) that share only classical correlation across clusters. This is a modelling decision with a world referent: which regions are *quantumly* bound (share structure, W5) and which are merely correlated.
- Stage 2 under C: two stages, not one. First, the location qudit to d regions (A's Stage 2). Second, the cluster structure over region factors. The order is a decision. `[LANA]`
- **Rejection test:** if cluster boundaries can't be assigned from world structure — if the choice of which regions are quantumly bound is arbitrary rather than derived from shared entities, signals, or rules — then the composite is decoration and C reduces to B with an unexplained cutoff.

### D. Algebraic: regions as subalgebras, not factors

Each region is assigned an algebra of observables A_i ⊂ B(H). Regions that share degrees of freedom have overlapping algebras. Entanglement structure lives in the inclusions and commutants. Overlap (W7) is the intersection A_i ∩ A_j. Independence of two traces is the statement that their algebras commute.

- Why it's on the table: it is the only candidate that handles W5/W7's *shared* degrees of freedom without double counting — the exact rejection clause the Cowork set attached to its candidate 3 — and it is the structure the observer-algebra layer already uses. The no-privileged-observer architecture's "truth constituted by agreement among independent traces" becomes a statement about commuting subalgebras, which is the first time that architecture would have a formal object.
- Cost: highest. Requires choosing H first (so D presupposes one of A–C as the Hilbert space), then specifying algebras. Nothing in the current codebase computes with algebras. A minimal build is: two overlapping qubit pairs, algebras generated by local Paulis, and a check that the reduced states on the shared qubit agree — one week of work, not a stage.
- Stage 2 under D: not reachable in one stage. D is a target for the observer-algebra layer that constrains how C's clusters may overlap, not a competitor to A–C for Stage 2.
- **Rejection test:** if every region's algebra is a full tensor factor (no overlaps), D collapses to B and adds nothing. D earns its place only if the world has regions that share degrees of freedom and the sharing has consequences the factor picture gets wrong.

### Adversarial reading of the four

A is rejected by the world's own entanglement earning conditions. B has a local basis with no assigned meaning and hits the memory wall. D is not buildable in a stage. C is the only candidate that expresses §2, at the cost of an extra modelling decision (cluster boundaries) that must be derived from world structure or it is arbitrary. The honest recommendation is C with D held as the constraint on C's overlap rule — and the honest warning is that C's cluster-boundary rule is a new open problem, not a solution to problem 3. It moves the unspecified part from "what is a register" to "which regions are quantumly bound," which is a smaller and more world-shaped question.

`[LANA]` Decision on A / B / C / D, and on the order of C's two stages.

---

## 4. The four commitment questions, with what is already answered

### Q1. Which concrete world alternatives are orthogonal basis states?

- Already committed (W1, W2): committed regions are basis states of *something*. Under A or C's location register, |region_i⟩ is "the participant is in region i."
- Blank: under B or C's region factors, what the local basis of one region means. Options with different consequences: (a) reached / not reached — then entanglement between regions is correlation in *whether* they are reached, which is a reachable-set statement and fits W2; (b) two rival characters of the region — then entanglement is correlation in *what the regions are*, which fits the moiré "third ontology" reading of W7 but makes the reachable set harder to define. `[ECHO]`
- Rejection: two world alternatives assigned orthogonal basis states that the world allows to be simultaneously and fully the case. Orthogonality means exclusivity; if the world has a state that is fully A and fully B, they are not orthogonal and the basis is wrong.

### Q2. What world operation changes a relative phase while preserving basis populations?

- Already committed (W3, W4): drift relative to an anchor is the phase kick; transit or anchor re-exercise is the refocus. The staging note invoked Meiboom-Gill alternation for exactly this, before Stage 1 existed. Stage 1's Experiment C is the physics of a claim the world already made.
- What Stage 1 adds: refocus requires knowing the kick. The world referent is T3, memory continuity — the participant (or the anchor) must carry the phase record for transit to refocus rather than replace. A transit without memory continuity is a *new* kick, not a refocus. This is a sharper statement of T3 than the staging note has.
- Blank: what world quantity is the phase *angle*. In the moiré core it is the twist. In the location register it is unspecified. `[ECHO]`
- Rejection: a transit that restores phase relation without any carried memory would violate the Stage 1 asymmetry and mean transit is a checkpoint restore, which §3 of the staging note forbids.

### Q3. What distinguishes an environment record from an ordinary stored log?

- Already answered by Stage 1, and should not be reopened: a record is environmental when (a) its record states are distinguishable (overlap < 1) and (b) it lies outside the reach of the refocusing operation. A log the participant can act on is inside; a module's observation held in the pool (W6) is outside. Orthogonality plus inaccessibility, not storage location.
- World consequence worth recording as `[interpretation]`: a record can be undone only by an operation that includes the record-holder — the quantum-eraser structure. Whether Echorym wants that rule is a design choice; the physics only makes it available.
- Blank: is the Network (staged, constrained, per Trace 002) inside or outside the refocus reach? This single answer determines whether Network-held information is a phase kick or a trace-out for the participant. `[ECHO]`

### Q4. What world event implements recombination, and which observable records its result?

- Half answered (W7): region overlap at a relational twist produces a joint outcome that no separable model reproduces. That is a recombination in Register R. Its observable is the joint outcome distribution against the best separable fit, which the RESULT note computed (contrast up to 0.25).
- Not answered for Register H / the location register: what event brings two *histories* of one participant back together such that their prior relation affects the present. The coherence framework defined coherence operationally as exactly this test, and no Trace event has been named as implementing it. This is the load-bearing blank. Without it V_E has no world referent and the location register is a bookkeeping device. `[ECHO]` — candidates to reject or adopt: a return transit to a region previously left (T4 exercised); a promise called due that spans two regions (recoherence mechanism 3); a memory trace referencing two regions (mechanism 2).
- Rejection: if every proposed recombination event can be predicted from the two histories' marginals alone, there is no interference in the world and the location register's off-diagonal is fiction. This is the same test as C1's independence test applied to relations instead of regions.

---

## 5. Term collisions to resolve before Stage 2

1. **"Commitment."** The staging note: committing a region adds a basis state and is *not* a measurement. The gates-and-circuits ladder: glimpse → interaction → interrogation → **commitment**, with commitment as the strongest measurement. These are two different operations sharing one word. Proposed: region-commit (basis growth) and participant-commitment (measurement). The planned Stage 3 (POVM ladder) will implement the second; it must not be read as the first.
2. **"Coherence."** Schema `coherence.current` on [0,1]; gate thresholds; C_l1 on [0,1]; V_E on [0,1]; the staging note's "coherence as throughput." Firewalled by the placement note. Restated here because Register C introduces a fifth: concurrence, on [0,1], between region factors. Five quantities on the unit interval named coherence. Each stage note names which it means, every time.
3. **"Reachable."** A world property of regions (W2) and, under B/C, a candidate local basis label (Q1a). If Q1a is adopted, "reachable set" becomes a computed support and the word does double duty; if Q1b, they separate. Decide with Q1.

---

## 6. External constraints on C and D

Stated as constraints to verify against source, not as results.

- **Spin-network no-go results (Otto et al.).** Constrain when a region of a spin-network state can be assigned an independent local register. Under C, this constrains which cluster boundaries are admissible; under D, which algebra inclusions. To be checked against the paper before C's cluster rule is written. `[CLAUDE — verify and restate]`
- **Observer algebras (Harlow-Usatyuk-Zhao; Engelhardt-Gesteau-Harlow; Geng-Jiang-Xu).** Supply D's formal structure and the sense in which an observer's algebra is a Heisenberg cut with a physics-side anchor. Relevant to Q3: the refocus reach *is* an algebra, and "inside / outside" is membership in it.
- **Quasi-probability negativity relocates, does not vanish.** Under C, negativity can be pushed between the location register and the region factors by choice of representation but not removed. Consequence: no cluster decomposition makes every region look classical. Consistent with the no-privileged-observer architecture and should be recorded as such, not rediscovered.

---

## 7. Consequence for Stage 2

Under the recommendation (C, D as overlap constraint):

- Stage 2 is **not** "d histories as a qudit" in isolation. It is: (2a) the location register to d regions, with the multi-slit visibility–C_l1 bound; and (2b) the N-region extension of the moiré core with concurrence and the 1/N sharpness result restated as coherence measures. The placement note §8 should record the change and its reason (this note).
- 2a and 2b can be built independently and joined later. The join — a controlled operation on region factors conditioned on the location register — is Stage 2c or folds into Stage 3.
- `echorym_qstate.py` and `moire_test*.py` become one module or two modules with a shared state representation. Append-only: neither is rewritten; a third file composes them.

`[LANA]` order of 2a / 2b, and whether the join is its own stage.

---

## 8. Cost accounting

| Item | A | B | C | D |
|---|---|---|---|---|
| State size | d | 2^N | d·2^N (or d·Σ 2^{n_k} with clusters) | as underlying H, plus algebra bookkeeping |
| Numpy ceiling | thousands | N ≈ 16 general; 128 for structured families | clusters ≤ 4 keep it trivial | small test cases only |
| New world parameters needed | none | local basis meaning | cluster-boundary rule | algebra assignment rule |
| Real-substrate cost | one qudit (polarization + path) | N entangled photons | not near-term | not near-term |
| Open problems moved, not solved | — | 3 → local basis | 3 → cluster rule | 3 → algebra rule |

Nothing here is free of a new unspecified rule. The honest measure is whether the new rule is more world-shaped than "what is a register." Cluster boundaries from shared structure (W5) is; algebra assignment is, but costs more to build.

---

## 9. What this note does not claim

It does not claim Echorym's regions, histories, or participants are quantum systems. It does not claim C is correct; it claims C is the only candidate that expresses §2 at a cost that can be paid in numpy. It does not derive gate thresholds from any quantity here. It does not touch the coupling layer. It does not resolve open problem 3; it relocates it to a cluster-boundary rule and says so.

---

## 10. Blanks for world-side review `[ECHO]`

1. Q1: the meaning of a region's local basis — reached/not-reached, or rival characters.
2. Q2: the world quantity that is the phase angle in the location register.
3. Q3: whether the Network is inside or outside the participant's refocus reach.
4. Q4: which Trace event is the recombination of two histories. This is the one that matters most.
5. Cluster rule for C: from the staging note's "regions sharing entities, signals, or rules" — what counts as shared, and is it binary or graded.
6. Whether the world wants the quantum-eraser rule (a record undone only with the record-holder's participation).

## 11. Decision record `[LANA]`

- Candidate: ___
- Q1–Q4 as adopted: ___
- Stage 2 order: ___
- Amendment to placement note §8: ___
- Date: ___
