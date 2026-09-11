Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# Trace 003 — plan/brief v0.3

**Status:** brief, not the Trace. Design locked; experimental contract revised. Remaining blanks `[ECHO]`, decisions `[LANA]`.
**Date:** 2026-09-09.
**Provenance:** World design decisions originate with Lana (from her design vision, Lana–Echo discussions she decides on, and Lana–Claude discussions). Echo translates into testable building blocks; Claude drafts and reviews adversarially; Astra-6 reviewed v0.2 (document and code inspection, no runs). Neither AI is the author of the World.
**Fields:** project_layer = research; quantum_grounding = literal-quantum (companion run) + mechanic (Trace); evidence_status = proposed.
**Root dependencies:** trace-002-trust-before-truth v0.3 → DN-staging-and-phase-travel v0.4.1 (§3, §4, §5, §6, §7.4, §7.5, §7.10, §9) → RESULT-moire-mechanic-test (2/3 correction) → DN-quantum-world-stage1 (V_E correction, this pass) → register-commitment v0.1 → roadmap-merge rounds 1–2 → brief v0.1–v0.2.
**Disclosure:** private until Stage 1 and the commitment note are pushed. No TRACE-HiT mechanism.
**Standing rules inherited:** no score without a rationale; trust is relationally addressed; append-only; the alarm fires on shape; modules referenced only through the minimal encounter schema.

**Change log v0.2 → v0.3.** Six corrections from Astra-6's review, all accepted; three world decisions by Lana. (1) Two passages: first journey commits B; second carries the hinge. (2) Access = phase-specific response at the return; no-hinge prediction is the flat baseline R = ½, read as *relationally absent*; hinge present = *phase-sensitive relational access*. (3) Enrollment creates an independent record d_M; entity record d_E is baseline in all arms. (4) "Hinge is exactly the off-diagonal" → "hinge is the proposed World referent for the off-diagonal"; earning is done by the fixed return rule and matched control. (5) Refocus mechanism specified: φ = Δω·τ from recorded clock readings; only the unitary displacement is refocusable. (6) Module claim narrowed to what one ratio identifies; staging drag reported as unmeasured; §7 fallback given its own observable. Stage 1 note and code docstring corrected in the same pass (V_E = 2|ρ_AB| = C_l1 for every qubit state). v0.1 and v0.2 retained.

---

## 0. Scope

Trace 003 tests (i) **recombination on the location register** (Q4) and (ii) **observational-module record formation** (§7.10, narrowed). The **§7.5 entanglement earning test is Trace 004's** (decided v0.2). 003 does not commit the Network, does not define return in general, does not define the see-er, does not test record removal.

One clarification for the ledger, so it is not recorded as a contradiction: the record mechanism in 003 is system–*environment* entanglement traced out — decoherence, already in Stage 1. Trace 004's deferred test is Bell/CHSH between two *region factors as system*. Different objects; no tension.

---

## 1. Dependencies

| # | Dependency | Status | Blocks |
|---|---|---|---|
| D1 | G0 register commitment signed (candidate C; Q1–Q4 as 003-local adoptions) | decided v0.2; §11 of the commitment note to be filled | everything |
| D2 | DN v0.5 (lifecycle / withheld-rule fields; 2/3 correction; fields in §6.6) | open | recording 003 in schema |
| D3 | Schema v0.3 implementing D2 | open | validation of 003 records |
| D4 | Stage 1 code + this pass's correction | done | companion run — d = 2 suffices |
| D5 | Minimal module-encounter schema | check | Arm M |
| D6 | Trace 002 v0.3 canonical ending | merged | the baseline (§6.5) |

Order: this brief → DN v0.5 → schema v0.3 → 003 prose. Prose does not start before D3.

---

## 2. Objective

Determine whether Echorym has an in-world event whose outcome depends on the **relation between two histories** — under a fixed return rule, against a matched control — and whether enrollment of an observational module against a region **forms a which-history record** that measurably suppresses that outcome.

---

## 3. World-side referents (003-local coordinates, not permanent ontology)

### 3.1 Location register and the two passages

Basis states = committed regions (W1; staged regions contribute none — the 002 ruling stands). Entering 003: {|A⟩}.

**Passage 1 (commit):** A → B → A. The return performs C2 (return path exercised, not claimed). C1 is estimated in a window opened on B; C3 checked against the pre-003 reachable set. B commits cleanly — the World's first criteria-earned commit, Trace 002's contrast case. Register is now {|A⟩, |B⟩}, d = 2.

**Passage 2 (hinge):** the coin-flip departure, time in B, return. This is the recombination experiment, run only once A and B are both legitimate basis states. "Return is the commit" is preserved as the first return; the timing contradiction in v0.2 is removed by not asking the register to hold ρ_AB before B exists in it.

Two passages also separate the estimation windows: Passage 1's window is C1 sampling for B; Passage 2 opens an incidental window on the Network (background only) and records fallow-crossing traffic.

### 3.2 Anchor = the artifact

Placed in A before Passage 1. Maintained phase reference (staging note §6). Four components: reference record (holds the clock readings — see 3.3), active bond, presentation surface, provenance link. `[ECHO]` question 5 stands: one object or several.

### 3.3 Phase and refocus mechanism

φ = Δω·τ. Δω = the difference between B's dynamical clock rate and the anchor's, grounded in B's local dynamics (staging note §9), not a similarity score. τ = time spent in B on Passage 2, under B's clock. Both readings are written into the artifact's reference record at departure and return, so φ is *available* to the return transit. **Refocus = the return transit under anchor re-exercise applies −φ.** This is the Stage 1 `refocus(rho, kick_phase)` operation with a world source for `kick_phase`.

Only this unitary displacement is refocusable. Ambient environmental decoherence (staging drag, any decay not attributable to a recorded clock displacement) is **not** refocusable and the brief does not call it recoverable.

### 3.4 The hinge

The coin-flip memory trace carries the **hinge relation**: the relational information present while A and B were both live possibilities, not a memory of both completed histories. The hinge is the **proposed World referent for the off-diagonal ρ_AB**. It is *not itself evidence* that physical coherence exists; classical memories can also hold information absent from either summary. The earning is done by §6, not by the definition.

Checkpoint 1 (authoring): the hinge must be information that the outcome erases — not reconstructible from knowing which path was taken and what was found. Necessary, not sufficient.

### 3.5 The capability: relation-sensitive access

On return from Passage 2 the participant gains **relation-sensitive access** — the ability to perceive or act on a World relation not operationally available before. Two things are kept distinct:

- **Capability existence / depth** — emerges on return, belongs to the relationship, may grow over later Traces. Not a 003 success criterion; not written as permanently fixed at the return value.
- **Instantaneous response** — varies with phase and coherence; this is the 003 observable.

Rule adopted (longer-term): *a capability may belong to the relationship even when the current state of that relationship does not make the capability fully available.*

### 3.6 The 003 observable and its two readings

One predeclared observable: **the response at the Passage 2 return**, with the return phase set by the recorded B-clock displacement φ (3.3), recorded with rationale.

- **Hinge absent:** response sits at the flat classical baseline R = ½, phase-insensitive. World reading: **relationally absent** — the return happens, the components are all there, nothing about the A/B relation modulates access.
- **Hinge present:** response is **phase-sensitive**: R(φ) = ½ + Re(ρ_AB e^{−iφ}); the A/B relation modulates access above or below baseline depending on the clock displacement. World reading: **phase-sensitive relational access.**

So "present vs absent" is refined, not replaced: relationally absent vs phase-sensitive relational access. The full visibility scan (V_E = 2|ρ_AB|) is supplied by the companion run, not by the Trace; 003 measures one response at one declared phase.

### 3.7 Entity as record carrier (003-local)

The entity has two mutually exclusive forms; on Passage 2 its form is correlated with passage. It is the **baseline which-history record, strength d_E, present in every arm**. Not its permanent ontology; its possible role in entanglement is 004's.

### 3.8 Enrollment as record creation

Module enrollment against B (pool-not-fact) **creates an additional, independent record** of strength d_M — the module's log of the participant's presence in B — rather than reading or exporting the entity's record. Records compose multiplicatively on the off-diagonal: (1 − d_E)(1 − d_M). Export of an existing record beyond a joint-operation reach needs a joint unitary Stage 1 does not have → S4.

### 3.9 See-er seed, reversibility principle

Unchanged from v0.2: mechanic-lane seed only, no token/UI; *a true return restores access to possibility, not a copy of the past* → DN v0.5 input.

---

## 4. Quantum-side mapping (companion run, Stage 1 code)

| World | Register | Operation |
|---|---|---|
| A, B after Passage 1 | basis {|A⟩, |B⟩} | `history_pair`, d = 2 |
| Hinge memory trace | ρ_AB ≠ 0 (proposed referent) | `pure_superposition` |
| Artifact reference record | phase frame; holds φ | — |
| Time in B under B's clock | unitary kick φ = Δω·τ | `phase_gate(φ)` |
| Entity form ↔ passage | environment record d_E | `couple_to_environment(ρ, d_E)` |
| Module enrollment | second independent record d_M | `couple_to_environment(ρ, d_M)` |
| Staged Network | unmeasured ambient baseline γ_stage | `dephase(ρ, γ_stage)`, same in all arms |
| Return transit + anchor re-exercise | refocus by −φ | `refocus(ρ, φ)` |
| Response at return | R(φ) = ½ + Re(ρ_AB e^{−iφ}) | `recombination_response(ρ, φ)` |
| (companion only) visibility | V_E = 2\|ρ_AB\| = C_l1 | `visibility(ρ)` |

Parameters (φ, d_E, d_M, γ_stage) are read from the Trace's records. The companion's ordering of responses across arms is what the Trace's recorded responses must match. Neither substitutes for the other.

---

## 5. Event skeleton

**Passage 1.** (1) Artifact placed in A. (2) Transit to B; C1 window opens; B inhabited, staged. (3) Return to A — C2 performed; T1–T4 recorded. (4) C3 checked; B's verdicts recorded; B commits (or remains staged / decays — an outcome, not a failure).

**Passage 2.** (5) Door; coin-flip; hinge memory trace formed. *Checkpoint 1.* (6) B; entity form correlates with passage (d_E); τ accrues under B's clock; arm-dependent enrollment (d_M). (7) Return transit with anchor re-exercise (−φ); clock readings written to the reference record. (8) Response at return recorded. *Checkpoint 2: is the response's rationale derived from the fixed return rule applied to the hinge, not authored to fit?* (9) Incidental: Network window, fallow-crossing traffic.

---

## 6. Falsifiers and controls

**The fixed return rule.** One rule, written before any arm, unchanged across arms: *the response at return is the fixed recombination of the hinge memory trace with the present World-state at the recorded displacement.* Arms differ only in their inputs (hinge present/absent; d_M). The outcome of each arm is derived from the rule, not authored per arm. This is what removes the circularity Astra identified.

**Arm R — hinge present, no enrollment.** Predicted: phase-sensitive response, magnitude set by (1 − d_E)(1 − γ_stage).

**Arm C — matched control.** Same World-state, artifact, entity, both completed-history memories, door, return path, same rule, same φ; the hinge authored as *absent* (`hinge_content` null). Predicted: R = ½, phase-insensitive — relationally absent. If Arm C's response is phase-sensitive under the same rule, the mapping has earned nothing. If the author finds the rule *cannot* produce ½ for Arm C without changing the rule, that is checkpoint 2 failing.

**Arm M — hinge present, enrollment.** Arm R plus d_M. Predicted: same phase-sensitivity, amplitude reduced by (1 − d_M). Refocus recovers none of it (record, not displacement).

**Identifiability.** The ratio of Arm M's modulation amplitude to Arm R's identifies d_M and nothing else. 003 makes **no claim about an ambient-rate increase from enrollment** (γ_module); that would need a duration sweep or an independently calibrated record, neither of which 003 has. Open problem 9's coefficient remains unbounded by this Trace. Staging drag γ_stage is present in all arms, is not identifiable without a no-staging reference outside 003, and is reported as an **unmeasured baseline**, not a number.

**Two-sided reading.** If Arm M's amplitude equals Arm R's under heavy enrollment — a module that appears to cost nothing — that is the alarmable result (§7.10), not a success.

**Schema needs (D2/D3):** `hinge_content` (nullable); `record_strength` with rationale on both the entity and the module encounter; a graded `response` field with the declared φ and rationale; clock readings on the artifact's reference record.

---

## 7. Stop condition and fallback

> If checkpoint 1 fails (no hinge that the outcome erases) or checkpoint 2 fails (no fixed rule under which Arm C sits at baseline and Arm R is phase-sensitive without authoring the answer), the location-register off-diagonal remains mathematically valid but has **no earned world referent**. Stage 2a: `evidence_status: demoted (referent unassigned)`.

Fallback for the module test is **not** "the same test without the hinge" — Astra is right that the module arm loses its observable with it. If the mapping fails, 003's module test uses the ledger's other prediction (§7.10): **heavier enrollment requires higher transit frequency to maintain the same reachable set.** Its observable is transit count over the Trace, not response at return. Weaker, independently justified, and must be predeclared as the fallback now, not chosen after.

---

## 8. Earned if it passes / deferred

Earned: Q4 by demonstration (a World event instantiating recombination under a fixed rule); the first criteria-earned commit; d_M formation demonstrated with a mechanism; the relationally-absent / phase-sensitive distinction in records; recoverable reachability ≠ recoverable interference (Arm M returns; Arm M does not fully recohere).

Not earned by 003: physical coherence *from* the hinge definition; obligations spanning regions (§7.4 row 6); entanglement (→ 004); γ_module; γ_stage; record removal (→ S4); see-er physics (→ S3); cluster rule (→ N-09a); capability growth (later Traces).

---

## 9. Changes to standing notes, this pass

1. **Stage 1 note:** appended correction — V_E = 2|ρ_AB| = C_l1(ρ) for every qubit state under the balanced recombiner, not only at p_A = p_B; the "equal populations" caveat is withdrawn. (`DN-quantum-world-stage1-history-pair-state.md`, correction block.)
2. **`echorym_qstate.py`:** docstring line stating the population-normalized identity corrected by an appended note; `visibility_predicted` was already right; no code behaviour changed.
3. **Roadmap-merge review §5 (S2 row):** "identity only at d = 2" stands; the inequality claim for d > 2 unaffected.
4. **Staging note §14:** dated amendment — §7.5 → Trace 004; 003 = recombination + §7.10 (record formation only).
5. **Commitment note §11:** fill with v0.2/v0.3 adoptions.
6. **Placement note §8:** S2a/S2b/S2c; 003 companion as Stage 1 fixture.
7. **DN v0.5 inputs:** reversibility principle; capability-belongs-to-the-relationship rule; fields in §6.

## 10. Open before prose

1. `[ECHO]` One paragraph: what the hinge *is* in this Trace and what about it the outcome erases (checkpoint 1).
2. `[ECHO]` The fixed return rule, written once, plus Arm C's derived outcome under it (checkpoint 2). Astra's closing recommendation — do this before anything else.
3. `[ECHO]` Artifact: one object or several for the four components.
4. `[LANA]` N-09a pilot scoped after S2c/S3: yes / no.
5. `[LANA]` Astra-6 retained as reviewer on register-level documents: yes / no.
6. `[LANA]` Date / sign-off on v0.3 as the locked contract: ___
