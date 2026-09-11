Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# DN-quantum-world-stage1: a history pair as a real quantum state

Status: design note, week of 2026-09-06. First step on the staged path from classical simulation to a physically defensible quantum world.
Depends on: Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline, Experiments A–E), Baumgratz, Cramer & Plenio, PRL 113, 140401 (2014) for the l1-norm and relative entropy of coherence.
Artifact: `echorym_qstate.py` (runs standalone, numpy only).
Class IV boundary: unchanged. Nothing below is about neural, human, or narrative state.

## 1. Where the staged path stands

The coherence framework defined Echorym coherence operationally — bring two separated histories back together and measure whether their prior relationship affects the present — and placed that definition at Level 2, an operational analogue, with the `relative_phase_like_parameter` in `BranchRelation` flagged as explicitly non-physical. The Level 3 quantities are the standard resource-theory measures — l1-norm and relative entropy of coherence (Baumgratz et al. 2014) — tracked under open-system dynamics.

The gap between those two documents is the substrate. The framework's visibility V_E is defined over an unspecified "recombination-sensitive response R"; those measures are defined over a density matrix that Echorym does not yet have. The first stage of the path is therefore not coherence, superposition, interference, measurement, or decoherence as such. It is state: give the smallest Echorym object that carries relational structure — a history pair — a genuine quantum state, and then check whether the Level 2 definition and the Level 3 measure agree on it.

## 2. The concept

A history pair (A, B) is represented by a 2×2 density matrix ρ in the basis {|A⟩, |B⟩}:

    ρ = [[ p_A ,   ρ_AB ],
         [ ρ_AB*, p_B  ]]

The diagonal is state retention: how much weight each history still carries. The off-diagonal element ρ_AB is the only place relational coherence can live. This makes the framework's three-way distinction (retention, relational coherence, reconstruction efficiency) a property of the representation rather than a convention: two states with identical diagonals and different ρ_AB are "remembered identically" and "coherent differently", and there is no third place for the difference to hide.

The framework's Experiment A becomes a literal circuit: apply a relative phase φ between the histories, recombine on a balanced beamsplitter (Hadamard), read out P(A-port), scan φ, and take V_E = (R_max − R_min)/(R_max + R_min).

## 3. The formal identity that earns the step

For any qubit state the phase-scanned visibility is

    V_E = 2 |ρ_AB| .

The l1-norm of coherence in the same basis is C_l1(ρ) = 2|ρ_AB|. So

    V_E = C_l1(ρ)

identically — for equal and unequal populations alike, since the Hadamard response is R(φ) = ½ + |ρ_AB| cos(φ + arg ρ_AB) and R_max + R_min = 1 = p_A + p_B. The Level 2 recombination visibility and the Level 3 resource-theoretic coherence measure are the same number on this substrate, with no change to either definition. That is what "the analogue was earned" means concretely: the operational test the framework proposed is, on a real state, exactly the quantity the resource theory says to compute.

The relative entropy of coherence C_re does not coincide with V_E (it is convex in |ρ_AB| rather than linear; see the dephasing sweep), which is useful rather than inconvenient — it is a second, independent Level 3 measure that Echorym can now report alongside the one it already defined.

## 4. What the module verifies (numbers from `python3 echorym_qstate.py`)

Experiment A — equal-weight coherent pair: C_l1 = 1.000, V_E(scan) = 1.000.

Experiment B — same populations, relational structure erased (ρ_AB = 0): C_l1 = 0.000, V_E = 0.000. Memory without coherence is a diagonal density matrix; the framework's central claim that retention and coherence are separable is now a one-line construction.

Dephasing sweep (Experiment D shape): under a phase-damping channel ρ_AB → (1−γ)ρ_AB, V_E = 1−γ exactly, populations untouched throughout.

Which-history record (framework §10) as physics: entangle the pair with one environment qubit whose two record states have overlap 1−d, then trace the environment out. V_E = 1−d. No observer reads the record; its existence in the environment is sufficient to suppress recombination. This is the framework's "information capable of enforcing decoherence" category, and it is now distinguishable from "information stored somewhere" by whether the record state is orthogonal.

Experiment C — recoverable dephasing versus loss, done as an ensemble. Five hundred pairs each receive a static, member-specific phase kick (inhomogeneous dephasing, the T2* situation). The ensemble-average state falls to V_E ≈ 0.56. Undoing each member's kick on its current state — a unitary refocus, not a checkpoint restore — returns V_E to 1.000. The same refocus applied after a full which-history record leaves V_E at 0.000. This is the spin-echo distinction the framework wanted, on real states: reversible drift is a unitary that has not left the system; irreversible decoherence is a trace.

Identity check: over 200 random valid states with arbitrary populations and phases, max |V_E(scan) − 2|ρ_AB|| = 3.4 × 10⁻⁵, which is the phase-grid resolution of the scan.

## 5. Falsifiable claim for this stage

Stage 1 is retained if the identity V_E = C_l1(ρ) holds under every unitary and every phase-damping channel applied to a history pair, and if a refocusing unitary recovers V_E after inhomogeneous dephasing but not after an orthogonal environment record. Failure mode: any construction in which V_E and C_l1 disagree, or in which the refocus recovers visibility from a traced state — either would mean the "recombination" or the "record" is being implemented as something other than a quantum operation, and the stage would be demoted back to Level 2.

## 6. What this stage does not claim

It does not claim that Echorym's histories, agents, or participants are quantum systems. |A⟩ and |B⟩ are two orthogonal basis states of a two-level system; any Echorym meaning attached to them is an interpretation layered on top, exactly as the framework's guardrail requires. It does not claim non-Markovian revival — the dephasing channel here is memoryless by construction, so no revival is possible, and demonstrating one is a later stage with its own claim. It does not touch the wall interface or the coupling layer.

## 7. Next stages on the path, in order

1. Superposition and interference beyond one pair: extend to d histories (a qudit) and check that the multi-slit visibility structure and C_l1 remain related by a known bound rather than an identity, which is where the framework's "branch similarity versus recombination sensitivity" question becomes sharp.
2. Measurement as constraint: replace the projective readout with a POVM of adjustable strength and show the framework's graded observation ladder (glimpse → interaction → interrogation → commitment) as a one-parameter family of instruments, with the post-measurement coherence computed rather than asserted.
3. Decoherence with memory: replace the phase-damping map with a structured environment (a small bath, or a Jaynes–Cummings-type single mode) and test the structured-environment claim (a non-Markovian revival that the BLP measure independently registers) — BLP information backflow coincides with a non-monotone segment in C_l1(t), and does not appear under a Markovian model with matched decay.
4. Only then, the geometric phase extractor from QKD-Aero polarization states, which needs the same density-matrix substrate to report a gauge-invariant number.

Each stage adds one operation to `echorym_qstate.py` and one row to the falsifiable-claims table; none rewrites what came before.

---

## Correction 2026-09-09 (appended; nothing above is altered)

**Source:** Astra-6 review of Trace 003 brief v0.2, code inspection of `echorym_qstate.py`; confirmed by Claude against the implementation.

**What was wrong.** This note and the module docstring state the identity as V_E = C_l1(ρ)/(2√(p_A p_B)) in general, reducing to V_E = C_l1 only at p_A = p_B = ½. That is the population-normalized two-slit form. It is not what the module implements.

**What is true for the implemented measurement.** The recombiner is a balanced Hadamard readout of one port. Its response is R(θ) = ½ + Re(ρ_AB e^{−iθ}), so R_max + R_min = 1 for every state and V_E = (R_max − R_min)/(R_max + R_min) = 2|ρ_AB|. Since C_l1(ρ) = 2|ρ_AB| for any qubit, **V_E = C_l1(ρ) for every qubit state, regardless of populations.** The `visibility_predicted` function (2|ρ_AB|) was already correct; the docstring and the "equal populations" caveat in this note were not. The 200-random-state check in the module already verified the corrected statement; the text lagged the code.

**Consequences.** The Level-2 → Level-3 identity is stronger than stated, not weaker. The S2 claim (V_E ≤ C_l1 becomes a strict inequality for d > 2 histories) is unaffected. A separate distinction now stated explicitly, per the same review: a **response** is one output probability at one phase (a mixture gives ½, not zero); a **visibility** is contrast over a phase scan. Trace 003 measures a response; the companion run supplies the visibility.
