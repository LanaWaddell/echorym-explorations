Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# Echorym — Quantum Coherence Measurement Framework
## Research Note (v0.1-public)

**Status:** Published 2026-09-10 as the foundation note for the Echorym quantum-world series. Originally circulated as a research note for Claude review; the review was incorporated into DN-quantum-world-stage1-history-pair-state.md, where the visibility–C_l1 relation proposed in §5.1 is shown to be an identity for a qubit, not a falsifiable claim. Content below is otherwise unchanged from the reviewed draft.
**Author:** Lana Waddell (Bright Days Inc.). Drafting: Echo (ChatGPT) as translating instrument; adversarial review: Claude (Anthropic). Design decisions are the author's.
**Lane note:** Level 1 / 2 / 3 as used here maps to the metaphor / metric / implemented-model lanes of the Echorym lane table; Level 3 quantities exist only in the quantum-world series, not in Echorym's narrative or trust layers.
**Primary project:** Echorym  
**Purpose:** Explore whether experimental methods used to measure and preserve quantum coherence in rare-earth quantum memories can provide a rigorous measurement framework for coherence, decoherence, and recoherence inside Echorym.

---

## 1. Why this matters for Echorym

Echorym has increasingly treated **coherence**, **decoherence**, **collapse/capture**, and **recoherence** as distinct processes rather than as loose metaphors.

A useful experimental lesson from quantum-memory research is that:

> **State persistence is not the same thing as coherence.**

A system may retain information about a previous state while losing the relational structure that would allow different alternatives to interfere or recombine.

Conversely, only part of a state may remain recoverable while the surviving components still retain a highly coherent relationship.

For Echorym, this suggests that asking *“Does the system remember the earlier state?”* is insufficient.

A stronger operational question is:

> **If previously separated histories are brought back into a common state space, does their prior relationship measurably affect the present?**

That gives Echorym a possible route from a conceptual treatment of coherence to an **operationally measurable property of the simulation**.

---

## 2. Scientific anchor

The commonly circulated description that prompted this note appears to combine multiple quantum-memory results.

The relevant long-storage experiment was:

- **System:** ^151Eu³⁺:Y₂SiO₅ rare-earth-ion crystal
- **Publication:** *Nature Communications* (2021)
- **Result:** Optical coherence preserved for up to approximately one hour
- **Method:** Optical-to-spin-wave storage, magnetic-field optimization, and dynamical decoupling
- **Coherence test:** Interference between retrieved early/late temporal modes
- **One-hour interference visibility:** approximately 93%
- **Derived fidelity:** approximately 96%

The key point is not the record lifetime itself.

The important methodological point for Echorym is **how coherence was demonstrated**.

The researchers did not merely verify that a stored signal could later be retrieved. They arranged two previously distinguishable histories so that they became indistinguishable at readout and could interfere.

The visibility of that interference quantified how much of their phase relationship had survived.

This distinction is potentially foundational for Echorym.

---

# 3. Core distinction: memory versus coherence

Echorym should explicitly separate at least three variables.

## 3.1 State retention

**Question:** How much information about a prior state remains accessible?

Possible Echorym measures:

- state-vector similarity
- retained latent variables
- recoverable world-state information
- preserved commitments / promises / observations
- reconstruction accuracy
- branch retrievability

This is analogous to asking whether information remains stored.

---

## 3.2 Relational coherence

**Question:** Does the relationship between unresolved or previously separated alternatives remain intact?

This should not be inferred simply because both histories remain stored.

Instead, coherence should ideally be measured by a **recombination test**.

If two histories are later placed into overlapping conditions, does the resulting state depend on their previous relationship in a predictable way?

If yes, some form of operational coherence remains.

If no, the histories may still be remembered as records, but their relational coherence has been lost.

---

## 3.3 Retrieval / reconstruction efficiency

**Question:** How much of a previous state can actually be recovered or reconstructed?

This should remain distinct from fidelity/coherence.

A useful lesson from quantum memories is that **low retrieval efficiency can coexist with high coherence among the retrieved components**.

For Echorym:

- only 20% of an earlier state may remain recoverable;
- but that 20% may preserve very high relational fidelity.

Or:

- 95% of the state may be reconstructed;
- but the interaction structure between alternative histories may have decohered completely.

These are very different outcomes and should not collapse into one score.

---

# 4. Proposed Echorym coherence framework

## 4.1 Operational definition

Proposed working definition:

> **Echorym coherence is the degree to which multiple unresolved, diverged, or separately evolving histories retain sufficient relational structure that their later recombination produces a measurable history-dependent effect.**

This is deliberately narrower than ordinary semantic meanings of “coherence.”

It makes coherence testable.

---

## 4.2 Coherence is relational

A single isolated world state should not be described as coherent merely because it is stable.

Coherence becomes meaningful when defined across:

- histories
- branches
- agents
- state components
- observations
- environmental interactions
- memories
- promises / commitments
- latent alternatives

This suggests that Echorym should store not only states, but some representation of **relationships between possible states**.

---

# 5. Proposed measurements

## 5.1 Echorym coherence visibility

Inspired by interference visibility:

\[
V_E = \frac{R_{\max}-R_{\min}}{R_{\max}+R_{\min}}
\]

Where \(R\) is a defined recombination-sensitive response.

The exact form would depend on the simulation architecture.

Possible observables:

- probability of entering a particular region
- reconstruction score
- agent decision distribution
- world-state transition probability
- semantic similarity of the recombined state
- latent-state activation
- downstream trajectory divergence
- recurrence of previously inaccessible information
- degree of agreement between independent reconstruction pathways

This does **not** need to pretend the simulation contains physical quantum amplitudes.

Initially, \(V_E\) can be treated as an **operational coherence analogue**.

If future Echorym state representations use complex amplitudes or explicitly quantum-inspired evolution, the definition can be revised accordingly.

---

## 5.2 Coherence fidelity

A simple derived metric could be:

\[
F_E = \frac{1+V_E}{2}
\]

This is useful only if the underlying visibility experiment is well defined.

It should not become a generic “system quality” score.

---

## 5.3 State-retention horizon

Define:

\[
T_{R}
\]

as the characteristic duration / number of simulation steps over which a prior state remains meaningfully reconstructable.

This measures **memory retention**, not coherence.

---

## 5.4 Echorym coherence horizon

Define provisionally:

\[
T_{2,E}
\]

as the characteristic duration / interaction depth over which a defined relationship between alternative histories remains capable of producing a measurable recombination effect.

This would be one of the more direct analogues to quantum coherence lifetime.

Important:

- \(T_R\) and \(T_{2,E}\) should be measured separately.
- A long memory does not imply a long coherence time.
- A short retrievable memory does not necessarily imply poor relational coherence among surviving components.

---

## 5.5 Recoherence horizon

Define provisionally:

\[
T_{\mathrm{recohere},E}
\]

as the maximum separation time / interaction depth after which a valid refocusing or recombination operation can still restore measurable relational structure.

This may be particularly important for Echorym's capture spiral.

A system could pass through several stages:

**coherent alternatives → apparent decoherence → recoverable dephasing → irreversible capture**

The recoherence horizon would help distinguish the middle two regimes.

---

# 6. Proposed experiments inside Echorym

## Experiment A — Baseline branch interference

### Goal
Determine whether two deliberately separated histories can retain a measurable relational signature.

### Procedure
1. Initialize a shared state \(S_0\).
2. Create two histories, A and B.
3. Introduce controlled differences while keeping both unresolved.
4. Allow each to evolve independently.
5. Bring them into a common recombination region.
6. Vary a controlled relational parameter between A and B.
7. Measure a downstream response \(R\).
8. Calculate \(V_E\).

### Compare against
- one-history control
- randomly paired histories
- deliberately decohered histories
- histories whose records remain but relational metadata has been erased

### Key question
Does recombination retain information that cannot be explained merely by stored state history?

---

## Experiment B — Memory without coherence

### Goal
Demonstrate experimentally that state retention and coherence are separable.

### Procedure
1. Preserve full logs / memory of two branches.
2. Deliberately erase or randomize their relational state.
3. Recombine them.
4. Compare against branches where relational structure was preserved.

### Expected result
Both systems may “remember” what happened, while only one produces a history-sensitive recombination signature.

This would create an explicit Echorym distinction between:

- **remembered history**
- **operationally coherent history**

---

## Experiment C — Echo / refocusing experiment

This is one of the strongest candidates.

### Goal
Determine whether apparent decoherence represents irreversible information loss or merely reversible drift.

### Procedure
1. Initialize coherent alternatives.
2. Introduce environmental perturbations that cause divergence.
3. Apply a deliberately designed inversion / refocusing transformation.
4. Recombine histories.
5. Measure recovered \(V_E\).

### Interpretation

If coherence returns:

> The system was dephased but had not irreversibly decohered.

If coherence does not return:

> Relevant relational information has likely leaked into uncontrolled environmental degrees of freedom or been irreversibly transformed.

This gives Echorym a rigorous distinction between **loss** and **recoverable displacement**.

---

## Experiment D — Recoherence decay curve

Repeat Experiment C while increasing:

- separation duration
- environmental interaction count
- observation count
- coupling strength
- capture pressure
- memory alteration
- hidden-state divergence

Plot:

\[
V_E(t)
\]

before and after attempted refocusing.

This would allow empirical estimation of \(T_{2,E}\) and \(T_{\mathrm{recohere},E}\).

---

## Experiment E — Capture threshold

### Goal
Determine whether capture is associated with a measurable transition from recoverable divergence to irreversible decoherence.

Increase capture pressure gradually.

At each stage:

1. separate histories;
2. apply refocusing;
3. test recombination;
4. measure \(V_E\);
5. measure state retention independently.

Possible result:

There may be a threshold beyond which the system continues to retain explicit memories of alternatives but can no longer operationally recombine them.

That threshold could be a quantitative definition of **capture**.

---

# 7. Dynamical decoupling analogue

The quantum-memory work also suggests a useful control concept.

Dynamical decoupling does not simply isolate a system from its environment.

Instead, carefully timed interventions prevent environmental perturbations from accumulating into irreversible phase loss.

Possible Echorym analogue:

> **Maintain openness to the World while periodically restoring relational alignment among unresolved histories.**

This fits Echorym better than simply shielding the system from external interaction.

Potential mechanisms:

- periodic state re-referencing
- branch synchronization events
- relational checkpoints
- reversible coordinate transformations
- controlled history inversions
- anchor-mediated refocusing
- environment-aware compensation operations

This creates a distinction between:

### Isolation
Reduce environmental coupling.

### Error correction
Detect and repair explicit state corruption.

### Dynamical coherence maintenance
Allow coupling but periodically prevent perturbations from accumulating into irreversible relational loss.

These should remain conceptually separate.

---

# 8. Coherence-protected regimes / "sweet spots"

Rare-earth quantum memories can be operated at magnetic-field configurations where transition frequencies become unusually insensitive to environmental fluctuations.

Echorym could search for analogous regions of its own state space.

Define a coherence-sensitive observable \(C\) and environmental parameter \(x\).

Search for states where:

\[
\frac{\partial C}{\partial x} \approx 0
\]

Meaning:

small perturbations in the environment cause little first-order loss of coherence.

Potential Echorym interpretation:

> A coherent state does not need to be weakly coupled to the World; it may instead occupy a configuration that is intrinsically robust to ordinary perturbation.

This may be highly relevant to:

- stable human–AI coupling
- resilient agents
- anchors
- non-capture states
- reversible exploration
- long-lived superposition of possible trajectories

---

# 9. Connection to the capture spiral

This framework may sharpen the capture spiral considerably.

Current conceptual sequence could be refined into something like:

1. **Open superposition / unresolved possibility**
2. **Divergence**
3. **Dephasing**
4. **Recoverable decoherence-like behaviour**
5. **Recoherence window**
6. **Coherence horizon exceeded**
7. **Capture / effective irreversibility**
8. **Canonicalized history**

The critical distinction is between:

> **A branch becoming difficult to access**

and

> **A branch becoming incapable of coherent recombination with the active state.**

Those should not automatically be treated as the same event.

This could give the capture spiral a measurable threshold rather than only a narrative one.

---

# 10. Connection to observation

This also intersects with Echorym's observation architecture.

Observation may produce several different effects:

### Observation as state acquisition
Information is added without necessarily changing branch relationships.

### Observation as dephasing
The observation changes relational information while leaving all branches nominally available.

### Observation as which-history information
The environment or observer retains enough information to distinguish histories.

This may suppress later recombination even if the system itself retains both histories.

### Observation as capture
The observation causes one history to become operationally canonical and prevents valid recoherence.

These should potentially be modeled separately.

A particularly useful test:

> If the observer's which-history record is erased or made operationally inaccessible, can histories recohere?

This would help distinguish:

- information stored somewhere,
- information available to an agent,
- information capable of enforcing decoherence.

---

# 11. Anti-recoherence mechanism

The existing idea of an **anti-recoherence mechanism** becomes more precise under this framework.

Rather than simply preventing the system from "going backward," anti-recoherence could mean:

> **Maintaining sufficient which-history information in the wider system that previously diverged histories cannot again become operationally indistinguishable.**

Potential anti-recoherence mechanisms:

- persistent environmental records
- irreversible observer logs
- branch-specific anchors
- asymmetric memory updates
- canonicalization markers
- state-dependent permissions
- accumulated downstream dependencies
- environmental entanglement analogues
- irreversible semantic commitments

---

# 12. Relationship to the World

One potentially important philosophical/design implication:

Echorym should not necessarily define the World as a source of decoherence.

The World may serve several roles simultaneously:

- perturbation source
- memory reservoir
- observer
- which-history recorder
- coherence stabilizer
- refocusing medium
- coupling substrate
- capture mechanism

This fits the broader Echorym concept better than a simple:

**system = coherence**  
**environment = decoherence**

The interaction structure matters more than isolation.

---

# 13. Suggested architecture additions

Potential additions to the simulation architecture:

## BranchRelation object

Store relational information independently of branch state.

Possible fields:

```text
branch_a
branch_b
origin_state
relative_weight
relative_phase_like_parameter
shared_latent_structure
distinguishability
environmental_records
observer_records
coherence_score
last_recombination_test
recoherence_possible
capture_status
```

The `relative_phase_like_parameter` should remain explicitly non-physical unless/until Echorym implements actual complex-amplitude state evolution.

---

## CoherenceMonitor

Responsibilities:

- run controlled recombination tests
- calculate \(V_E\)
- estimate \(T_{2,E}\)
- estimate recoherence horizon
- track relational drift
- distinguish state loss from coherence loss
- detect capture thresholds

---

## RefocusingOperator

A reversible transformation intended to test whether apparent coherence loss is recoverable.

Important:

The operator should not simply restore a saved checkpoint.

It must operate on the **current evolved state**.

Otherwise it tests rollback, not recoherence.

---

## EnvironmentRecord

Track what information has escaped into the wider World.

Possible variables:

- who observed which branch
- what environmental traces were created
- whether traces remain accessible
- whether histories remain distinguishable
- whether the trace is reversible
- whether deletion actually removes operational distinguishability

This may become crucial to Echorym's observation and consent architecture.

---

# 14. Important scientific guardrail

Echorym should avoid claiming that its simulation-level coherence is automatically equivalent to physical quantum coherence.

Three levels should remain clearly distinguished:

### Level 1 — Quantum-inspired language
Useful analogy only.

### Level 2 — Operational coherence analogue
A measurable simulation property defined through branch recombination tests.

### Level 3 — Physical quantum coherence
Requires an actual quantum state representation and physically meaningful amplitude/phase evolution.

The proposed work initially belongs at **Level 2**.

This is stronger than metaphor while avoiding an unjustified physics claim.

---

# 15. Near-term implementation proposal

### Phase EC-1 — Definitions
Formalize:

- state retention
- branch distinguishability
- relational coherence
- recoherence
- capture
- irreversible history marking

### Phase EC-2 — Minimal two-history experiment
Build Experiment A with a deterministic environment.

### Phase EC-3 — Controlled decoherence
Introduce increasing environmental records and branch distinguishability.

### Phase EC-4 — Refocusing
Implement the first `RefocusingOperator`.

### Phase EC-5 — Coherence curves
Measure:

\[
V_E(t), \quad T_{2,E}, \quad T_{\mathrm{recohere},E}
\]

### Phase EC-6 — Capture integration
Test whether the capture spiral corresponds to an experimentally identifiable loss of recoherence.

### Phase EC-7 — Observation integration
Connect which-history records, observer state, and disclosure-on-delay mechanisms.

---

# 16. Questions for Claude

Please review this framework critically rather than assuming the quantum analogy is valid.

## Conceptual

1. Is the proposed distinction between **state retention**, **relational coherence**, and **reconstruction efficiency** sufficiently clear?

2. Does the proposed operational definition of Echorym coherence actually measure something non-trivial, or could the same behaviour arise from ordinary hidden-state memory?

3. What additional control experiments would distinguish true relational effects from simple deterministic state dependence?

4. Is \(T_{2,E}\) useful terminology, or would borrowing `T2` risk implying a stronger physical equivalence than intended?

5. What should the native Echorym terminology be for:
   - coherence horizon
   - recoherence horizon
   - which-history record
   - refocusing operation
   - capture threshold?

## Mathematical

6. Is interference-style visibility \(V_E\) a sensible generic metric here?

7. What classes of observable \(R\) would make the recombination experiment maximally informative?

8. Should the framework use:
   - complex amplitudes,
   - probability distributions,
   - latent-state geometry,
   - information-theoretic measures,
   - causal graphs,
   - or a combination?

9. Could mutual information, conditional mutual information, fidelity, KL/JS divergence, or another information-theoretic quantity provide a stronger coherence analogue?

10. How could we distinguish:
    - branch similarity,
    - branch correlation,
    - retained mutual information,
    - and genuine recombination sensitivity?

## Architecture

11. Is a separate `BranchRelation` object the right abstraction?

12. What state must be preserved to make a legitimate recoherence experiment possible without simply replaying saved history?

13. How should environmental which-history records be represented?

14. Should observation, memory, environment, and capture all write into one shared relational ledger, or remain separate systems?

15. What is the smallest viable implementation that could falsify the idea before we build too much infrastructure?

## Capture spiral

16. Could the capture spiral be formally modeled as a transition from:
    - coherent alternatives
    - to recoverable dephasing
    - to irreversible distinguishability?

17. Can we identify a measurable critical point at which recoherence becomes impossible?

18. Would capture be better represented as:
    - a threshold,
    - a continuous loss of recoverability,
    - a phase-transition-like phenomenon,
    - or a state-dependent process?

## Scientific validity

19. Where does the analogy to physical quantum coherence become misleading?

20. Which parts are legitimately transferable as **experimental methodology** even if the underlying system remains classical?

21. What wording should be used in public-facing documentation to clearly distinguish operational simulation coherence from physical quantum coherence?

---

# 17. Working thesis

The strongest transferable insight from quantum-memory coherence experiments is:

> **Do not determine whether alternatives remain coherent by asking whether they are still remembered. Bring them back together and test whether the relationship between them can still affect the present.**

If that principle survives critical review, it could provide Echorym with:

- a measurable definition of coherence,
- a measurable definition of recoherence,
- a way to distinguish reversible drift from irreversible capture,
- a rigorous experimental role for observation and environmental records,
- and a quantitative foundation for the capture spiral.

That would move coherence in Echorym from primarily conceptual language toward an experimentally testable property of the simulation.

---

## References / starting points

- Ma et al., *One-hour coherent optical storage in an atomic frequency comb memory*, **Nature Communications** (2021).
- Long-lived spin-coherence work in Eu³⁺:Y₂SiO₅, including later multi-hour demonstrations, as relevant background for coherence protection and dynamical decoupling.
- Relevant concepts: atomic frequency comb memory, spin-wave storage, interference visibility, dynamical decoupling, ZEFOZ transitions, spin echo, which-path information, decoherence, recoherence.
