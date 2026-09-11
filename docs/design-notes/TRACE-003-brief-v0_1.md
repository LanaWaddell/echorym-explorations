Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# Trace 003 — plan/brief v0.1

**Status:** brief, not the Trace. Adversarial half. World-side blanks `[ECHO]`, decisions `[LANA]`.
**Date:** 2026-09-08.
**Fields:** project_layer = research; quantum_grounding = literal-quantum (companion run) + mechanic (Trace); evidence_status = proposed.
**Root dependencies:** trace-002-trust-before-truth v0.3 (canonical ending) → DN-staging-and-phase-travel v0.4.1 (§3, §4, §5, §6, §7.4, §7.5, §7.10, §9) → RESULT-moire-mechanic-test (2/3 correction pending) → DN-quantum-world-stage1 → register-commitment v0.1 → Claude/Echo roadmap-merge rounds 1–2.
**Provenance:** World design decisions in this document (the see-er token, the artifact/anchor, the coin-flip memory event, the return structure, the matched control, the entity-form basis, the reversibility principle, and all Q1–Q4 adoptions) originate with Lana — from her design vision, from Lana–Echo discussions she decides on, and from Lana–Claude discussions. Echo translates those decisions into building blocks that admit physics and tests; Claude reviews the translation adversarially. Where this document says "Echo's X", read "Lana's X, as translated by Echo." Neither AI is the author of the World.
**Disclosure:** private until Stage 1 and the commitment note are pushed. No TRACE-HiT mechanism.
**Standing rules inherited:** no score without a rationale (local rule 1); trust is relationally addressed (local rule 5); append-only; the alarm fires on shape; modules may be referenced as world objects only through the minimal encounter schema.

---

## 0. What this brief fixes, and what changed since the ledger last spoke

The ledger's Trace 003 (staging note §14, Trace 002 review) carries two tests: **§7.5 entanglement earning** and **§7.10 observational-module decoherence**, "and nothing else," with the Network's commitment explicitly barred from becoming one of its questions.

Echo's building blocks add a third test — **history recombination on the location register** (Q4) — and tie it to a return structure A₀ → B → A₁. That is the right test to run first, because it is the one the whole quantum-world series is waiting on, and because Trace 002's corrected ending makes the return structure *the same event* as the clean commit 003 already owes (see §3.2). But three tests in one Trace violates the scope rule we enforced twice on 002.

**Proposal:** Trace 003 tests (i) **recombination** and (ii) **module decoherence**, which turn out to share one observable (§6). The **entanglement earning test (§7.5) moves to Trace 004**, where the second region factor it needs (S2b cluster) will exist. This is a ledger amendment; it needs a dated line in the staging note's §14 and Lana's signature. `[LANA]`

Rationale for the swap, stated so it can be rejected: §7.5's earning test is Bell/CHSH between two *region factors*. Echo's Q1 commits one region qubit (the entity, Form A/B). A Bell test on one qubit is not a test. Adding a second region factor to 003 means also authoring the world structure that makes two entities quantumly bound (the cluster rule), which is the open question 003 is not supposed to be carrying.

---

## 1. Dependencies

| # | Dependency | Status | Blocks |
|---|---|---|---|
| D1 | G0 register commitment signed (candidate C; Q1–Q4 as adopted below) | open — this brief proposes the 003-local adoptions | everything |
| D2 | DN v0.5 (lifecycle / withheld-rule fields; moiré status adjudication; 2/3 correction) | open | recording 003's records in schema; 003 must express *staged region, criteria verdicts, pending deltas, withheld rule* routinely |
| D3 | Schema v0.3 amendments implementing D2 | open | validation of 003 records |
| D4 | Stage 1 code (`echorym_qstate.py`, d = 2, record, refocus) | done | the companion run (§6) needs **nothing beyond Stage 1**: the committed set entering 003 is the trunk alone; the new region B is the second basis state; d = 2 |
| D5 | S2a (d > 2) | not needed for 003 | — |
| D6 | Trace 002 v0.3 canonical ending (Network active, constrained, staged; gate held) | merged | the ambient baseline (§6.3) |
| D7 | Minimal module-encounter schema (module referenceable as a world object) | check — was scoped during 002 | the enrollment arm |

The brief can be finalized before D2/D3. **Prose drafting cannot start before D3**, because the mis-ending on 002 was written in exactly the structures D2/D3 make representable. Recommendation: finish this brief → DN v0.5 → schema v0.3 → prose.

---

## 2. Objective

Determine whether Echorym has an **in-world event whose outcome depends on the prior relation between two histories and not merely on the presence of both histories' components** — and whether **enrollment of an observational module against a region measurably degrades that relation**, with the staged Network's coherence cost separated from the module's.

Not an objective: committing the Network; demonstrating entanglement; defining return in general; defining the see-er.

---

## 3. World-side referents, as adopted for 003 only

All of these are **003-local coordinates**, not the World's permanent ontology (Echo's guardrail, adopted verbatim).

### 3.1 Location register (histories)

Basis states = committed regions (W1). Entering 003: {|A⟩} = the trunk. 003 must add |B⟩ by a **clean commit** — B passes C1, C2, C3 during its provisional phase. This is the World's first criteria-earned commit and Trace 002's contrast case. The Network stays staged and contributes no basis state; its C1 evidence may accumulate *incidentally* in an estimation window (§4.3) opened by 003's ordinary traffic, and that window is recorded, but its verdict is not 003's question.

### 3.2 The return is the commit

C2 reads: *the return path is performed, not claimed, during the provisional phase.* Echo's A₀ → B → A₁ is C2 exercised. So the participant's return to A is not an extra event layered onto the commit — it is the commit's transitional criterion being met. If the return does not happen, B does not commit and 003 has one basis state and nothing to recombine. The clean commit and the return are one structure. This is the strongest single alignment between Echo's plan and the ledger and it should be stated in the Trace's purpose line.

T1–T4 apply to the return: T1 the artifact (§3.3) is the phase reference; T2 the coherence cost is paid from throughput and *logged*; T3 the memory trace (§3.5) is what carries across; T4 A remains reachable throughout (else the departure was collapse).

### 3.3 Anchor = the artifact

The participant deliberately leaves an artifact in A before passing through the door. It is the maintained phase reference against which B-divergence is measured (§6 of the staging note: an anchor is a maintained relation). Four anchor components apply (reference record, active bond, presentation surface, provenance link). 003-local mechanism only.

### 3.4 Phase angle (Q2, 003-local proposal)

Echo: φ(t) = φ₀ + ∫Δω dt + φ_control, Δω from the physics of the relation. What sets Δω in 003: **the clock-rate difference between region B and the anchor** (staging note §9, four clocks). Time spent in B under B's clock, measured against the artifact's clock in A, is the accumulated relational displacement. This is a world quantity that already exists in the ledger, is not a similarity score, is not trust, and is not assigned by hand. Refocus = anchor re-exercise (mechanism 4, §7.4) resets the reference. `[ECHO]` adopt / replace / reject.

### 3.5 The coin-flip event and the memory trace (Q4)

At the door, both histories are live: the participant does not know which becomes the lived path. The resulting **memory trace refers to both histories**. Under the mapping this is a state with support on |A⟩ and |B⟩ with a definite relative phase — a coherent superposition in the location register, not a mixture. The memory trace is the world object that *carries the off-diagonal*. Recombination is the later event (§3.6) whose outcome depends on that off-diagonal.

Rejection at the authoring stage: if the memory trace can be written as "memory of A" plus "memory of B" with no relational content that both share and neither contains alone, it is a mixture and 003 has no interference to test.

### 3.6 Recombination = the new capability at return

On return, the participant has a capability they did not have before leaving. Echo's condition — *operationally consequential, not symbolic* — is adopted. The mapping: the capability's presence/strength is the recombination output, and it must depend on the **relative phase between the A-history and the B-history** carried by the memory trace, not on the two component memories alone. This is the operational definition of coherence from the measurement framework, and V_E finally has a world referent if and only if this event can be authored without stipulation.

The `recombine` operation on the quantum side stays distinct (the mixing unitary whose output depends on prior relative phase); 003 tests whether the World has an event that legitimately instantiates it.

### 3.7 Region register (Q1, 003-local)

One entity, two mutually exclusive forms: |0⟩_E = Form A, |1⟩_E = Form B. Adopted for the first cluster. **Open question for 003:** what does the entity qubit *do* in this Trace, given that entanglement is deferred to 004? Two options:

- **(a) The entity is the which-history record.** The entity's form in B is correlated with whether the participant passed through — a record of strength d. Modules enrolled against B observe the entity; the record becomes inaccessible to refocus. This gives the entity qubit a load-bearing role in the §7.10 arm and uses Stage 1's record machinery exactly. Cost: it makes the entity an environment, not a system, for 003.
- **(b) The entity is seeded only.** Its two-form basis is declared in 003's records and exercised in 004. No quantum role in 003.

I recommend (a) because it gives the §7.10 test a concrete mechanism instead of a coefficient, and because "an observed entity carries the record" is honest about what enrollment does. `[ECHO]` decide; it is a world choice.

### 3.8 See-er seed

Mechanic lane only. A change in what relations can be perceived on return: the participant senses that re-adjusting to the World is different; the capability may reveal itself immediately or later. No token, no UI, no reward. The candidate see-er observable for S3 — a non-local relational observable (cluster parity) as against a local read — is *recorded* in 003's design note as the S3 target; nothing in 003's prose asserts it. Guardrail: not a player class.

### 3.9 Governing principle to elevate

**A true return restores access to possibility, not a copy of the past.** Adopted as a core reversibility principle; goes into DN v0.5 input as a candidate governing statement alongside T4, with "recoverable reachability ≠ recoverable interference" as its physics-side form.

---

## 4. Quantum-side mapping (companion run)

| World object / event | Register object | Stage 1 operation | Level |
|---|---|---|---|
| Trunk A, new region B (after commit) | location basis {|A⟩, |B⟩} | `history_pair` d = 2 | 3 |
| Coin-flip memory trace | ρ with ρ_AB ≠ 0 | superposition with phase φ | 3 |
| Artifact | reference frame for φ | fixed anchor phase | 3 |
| Time in B under B's clock | φ(t) = ∫Δω dt | inhomogeneous phase kick, ensemble over Δω | 3 |
| Return transit / anchor re-exercise | refocus | `refocus` (Exp. C) | 3 |
| Entity form (option a) | environment record, strength d | `record` (Exp. B), V_E × (1 − d) | 3 |
| Module enrollment against B | record made inaccessible + additional ambient rate | trace-out; extra decay γ_module | 3 |
| Staged Network | ambient baseline drag | uniform extra decay γ_stage, present in all arms | 3 |
| New capability at return | recombination output | V_E of the final state | 2 (world) / 3 (register) |
| Capability strength | — | reported as V_E **with rationale**, never as a score | rule 1 |

Everything here runs on the Stage 1 module unchanged. The companion run is a fixture: parameters (φ, d, γ_module, γ_stage) are taken from the Trace's records, and the run's V_E ordering across arms is what the Trace's capability ordering must match. Neither substitutes for the other (staging note §14: the physics demo does not discharge the in-world earning).

---

## 5. Event skeleton (structure, not scenes)

1. Participant in A. Artifact placed (anchor established; provenance link recorded).
2. Door. Coin-flip event: both histories live; memory trace created with cross-history content. *(Stop-condition checkpoint 1: can this trace be written non-separably?)*
3. B reached. Estimation window opens on B (C1 sampling against a frozen reference). Time accrues under B's clock (φ accumulates).
4. Module enrollment against B, pool-not-fact. *(Arm-dependent; §6.)*
5. Return transit to A — C2 exercised; T1–T4 checked and recorded. Artifact re-exercised (refocus).
6. Recombination: the new capability appears / is altered / is absent. *(Stop-condition checkpoint 2: does the outcome's rationale reference the cross-history relation?)*
7. B's criteria verdicts recorded; B commits cleanly (or remains staged / decays — an outcome, not a failure of the Trace). C3 checked against the pre-003 reachable set.
8. Incidental: Network estimation window recorded; fallow crossing traffic recorded (whether it is bent again).

---

## 6. Falsifiers and controls

Three arms, one observable (capability at step 6 ↔ V_E in the companion run).

**6.1 Arm R — relation present.** Steps 1–7 as written; no module enrollment. Prediction: capability present; V_E high, reduced only by γ_stage.

**6.2 Arm C — matched control (Echo's).** Identical visible ingredients — returned World-state, artifact, entity, both component memories, door, return path — with the **cross-history relational component removed**: the memory trace is authored as two separate memories (mixture; ρ_AB = 0). Prediction: capability absent or altered. If the capability appears identically, the relation was not load-bearing and the mapping has earned nothing. This arm is what makes 003 a test rather than an illustration.

**6.3 Arm M — enrollment.** Arm R plus module enrollment against B (step 4), with the entity carrying the record under option (a). Prediction (§7.10): capability weakened in proportion to record strength d and to the added ambient rate — the same suppression as Arm C but *graded*, and recoverable by refocus only for the part that is inhomogeneous phase (γ_module), not for the part that is the record (d).

**6.4 The two-sided reading.** Per the 002 correction: in a Trace where decoherence is the expected signal, **apparent stability is the alarmable result**. If Arm M shows the capability intact under heavy enrollment, that is not good news; it is the reading that must be flagged (§7.10: a module that appears to cost nothing is the suspicious result).

**6.5 Baseline separation.** γ_stage (the staged Network's drag) is present in all three arms and is measured from Arm R's deficit against the no-staging reference. γ_module is Arm M's deficit against Arm R. If these cannot be separated in the records, open problem 9 (module coefficient) is confounded with staging drag and 003's §7.10 result is void — say so rather than report a number.

**6.6 What each arm needs from the schema (D2/D3).** Arm C needs the memory-trace record to carry a `relational_content` field (or equivalent) that can be null. Arm M needs the module-encounter reference and a record-strength field with rationale. Both are DN v0.5 inputs.

---

## 7. Stop condition

Unchanged from round 2, now with two checkpoints in the skeleton:

> If no Trace 003 event has an outcome that depends on prior relative history — either because the coin-flip memory trace cannot be written non-separably (checkpoint 1) or because the capability's rationale reduces to the component memories (checkpoint 2) — then the location-register off-diagonal remains mathematically valid but has **no earned world referent**. Stage 2a is filed as mathematics, `evidence_status: demoted (referent unassigned)`, and 003 is written as a module-decoherence Trace only.

Do not force the mapping. A 003 that stops here is a successful Trace with a negative result, and it is cheaper than a 003 that stipulates.

---

## 8. What 003 earns if it passes

- Q4 answered by demonstration: a Trace event instantiating `recombine`; V_E has a world referent.
- Q1 (003-local), Q2 (clock-rate proposal), Q3 (as adopted round 2), anchor-as-artifact — all exercised in records, still 003-local.
- The World's first criteria-earned commit; Trace 002's contrast case; the arc reached → staged-with-constraint → first permitted commit.
- §7.10's derived cost demonstrated in-world with a mechanism (record-carrying entity), and the coefficient (open problem 9) bounded rather than free.
- "Obligations spanning regions" (§7.4 row 6) stays **not earned** — 003 does not test it. Only 004 can.
- Recoverable reachability ≠ recoverable interference, demonstrated in records: Arm M returns, Arm M does not fully recohere.

## 9. What stays deferred

Entanglement earning (→ 004, needs S2b). Cluster rule (→ N-09a pilot after S2c/S3). See-er physics (→ S3). Erasure / record removal with restored coherence (→ S4; 003 does not attempt it). Network commitment (→ later Trace or interstitial record; background only). The general theory of return (003 earns one mechanism). N-09 decomposition-as-variable (horizon).

On Echo's N-09a scheduling note: agreed in principle — a pilot on 3–4 qubits computing a state-derived decomposition against a control decomposition, after S2c/S3, is cheap and does not require the deeper program. Scope it as one operation, one claim, like any stage. `[LANA]`

---

## 10. Changes needed to standing notes before prose

1. **Staging note §14 / queue:** dated amendment moving §7.5 earning test to Trace 004; 003 = recombination + §7.10. `[LANA]`
2. **Staging note lines 29, 573; RESULT lines 125–126:** appended 2/3 correction. (Already decided.)
3. **Commitment note §11:** candidate C; Q1–Q4 as 003-local adoptions (§3 above); Stage 2 order S2a/S2b/S2c; note that 003's companion needs only d = 2.
4. **Placement note §8:** S2a/S2b/S2c split; 003 companion run listed as a Stage 1 fixture, not a new stage.
5. **DN v0.5 inputs:** governing principle (§3.9); `relational_content` and record-strength fields (§6.6); estimation-window record for the Network; fallow-crossing traffic record.
6. **Novelty ledger:** N-09 entered (horizon); N-09a pilot scoped.
7. **003's purpose line** (for the prose header): *"Tests whether the World has an event whose outcome depends on the relation between two histories, and whether observation degrades that relation. Does not test entanglement. Does not decide the Network."*

---

## 11. Questions for Echo, blocking order

1. §3.7 — entity as record (a) or seeded only (b).
2. §3.4 — clock-rate difference as Δω: adopt, replace, or reject.
3. §3.5 — a first sketch (one paragraph, not scenes) of what the coin-flip memory trace *contains* that neither component memory contains alone. This is checkpoint 1 and it is the thing most likely to stop 003; better to find out now.
4. §3.6 — a first sketch of the capability and its rationale, written so that Arm C's version can be authored alongside it.
5. Whether the artifact's four anchor components can all be instantiated by one object, or whether the presentation surface lives elsewhere.

## 12. Decision fields `[LANA]`

- §7.5 earning test moved to Trace 004; 003 = recombination + §7.10: yes / no
- Entity role in 003 (a) / (b), after Echo's answer: ___
- N-09a pilot scoped after S2c/S3: yes / no
- Order: brief → DN v0.5 → schema v0.3 → 003 prose: yes / amend: ___
- Date: ___
