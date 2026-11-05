Redaction status: cross-references and internal review notes edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05

# DN-quantum-world-stage2: d histories as a qudit — the visibility–coherence identity becomes a bound

Status: design note, week of 2026-09-13. Second step on the staged path (state → coherence → superposition → interference → measurement → decoherence → later stages). This stage: d histories held as one qudit, for which the visibility–coherence identity of Stage 1 becomes a bound.
Depends on: DN-quantum-world-stage1-history-pair-state, Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline, Experiment A).
Artifact: `echorym_qstate.py`, Stage 2 block appended; runs standalone with numpy (`python3 echorym_qstate.py`, about 2 min 20 s on one core, prints the verification table for Stages 1 and 2).
Stop-condition check: this stage does not require a decision about which world-object the register represents. A d-level register, its basis states and the balanced d-port recombiner are defined at the physics level exactly as Stage 1's qubit was; every world-side parameter the stage exposes is listed in §6 as unset rather than assumed.
Review: an adversarial pass on a first draft of this note confirmed the theorems, the optimiser and every printed number, and corrected two statements in the prose (the alignability claim now in §2 and §8, and the framing of the gap in §1); both corrections are incorporated and the checks that make them printed rather than inferred were added to the module (2.5b, 2.6 decomposition, 2.8).
Class IV boundary: unchanged (§11).

## 1. Concept

Stage 1 gave a history pair a real quantum state and showed that the framework's recombination visibility V_E is, on that substrate, identically the l1-norm of coherence: V_E = C_l1(ρ). Stage 2 asks what survives when more than two histories are held open at once. A register of d histories is a d × d density matrix; recombination is the balanced d-port transform F_d (the d-history generalisation of the 50/50 beamsplitter), with one adjustable phase per history; the response is the probability of one output port; V_E is taken over the full (d − 1)-phase scan.

The identity does not survive. For d ≥ 3 it is replaced by two inequalities, both theorems, and V_E becomes a witness of coherence bounded by min(1, C_l1) rather than a measure of it. The identity is lost on both sides of the phase scan. On the trough side, d ≥ 3 phases cannot put every pair of histories in antiphase at once, so R_min sits above the value the qubit reaches; this slack is present for every mixed register, alignable or not, and is the larger part of the shortfall. On the peak side, a register whose off-diagonal phases cannot be brought into phase simultaneously has a *frustration gap* Δ > 0 — a new quantity that is identically zero at d = 2, zero for every pure state, and nonzero for generic mixed states — and Stage 1's own inhomogeneous-dephasing construction already produces it once a third history is present.

## 2. Formalization

Register. ρ is a d × d density matrix in the history basis {|0⟩, …, |d−1⟩}. Populations ρ_jj are state retention; the off-diagonal elements ρ_jk (j ≠ k) are the only place relational coherence lives. The coherence measures are unchanged from Stage 1 and are applied to the larger matrix without modification:

    C_l1(ρ) = Σ_{j≠k} |ρ_jk|,        0 ≤ C_l1 ≤ d − 1,
    C_re(ρ) = S(diag(ρ)) − S(ρ),     diag(ρ) = ρ with its off-diagonals removed.

C_l1/(d − 1) is the normalised form, equal to 1 only for a maximally coherent state.

Recombination. Apply U_φ = diag(e^{iφ_0}, …, e^{iφ_{d−1}}), then the balanced d-port transform (F_d)_{jk} = d^{−1/2} e^{2πi jk/d} (F_2 is the Hadamard), and read the probability of port 0:

    R(φ) = ⟨u_φ| ρ |u_φ⟩,    |u_φ⟩ = d^{−1/2} Σ_j e^{−iφ_j} |j⟩
         = (1/d) [ 1 + Σ_{j≠k} e^{i(φ_j − φ_k)} ρ_jk ]
         = (1/d) [ 1 + 2 Σ_{j<k} |ρ_jk| cos(φ_j − φ_k + arg ρ_jk) ].                    (1)

R depends on ρ only through the off-diagonals, and on the phases only through their differences; φ_0 = 0 is a gauge choice. Its average over the torus is 1/d, so R_max ≥ 1/d > 0. The framework's visibility is

    V_E = (R_max − R_min)/(R_max + R_min),                                              (2)

with the extrema taken over the whole (d − 1)-torus of phase settings. The module locates the extrema by monotone phase-only ascent (w ← Mw/|Mw| elementwise, which is non-decreasing in w†Mw for positive semidefinite M by Cauchy–Schwarz on the PSD form) from 31 random restarts plus the all-in-phase point, then polishes each restart by Newton's method on the torus (pseudo-inverse Hessian, backtracking, improvements only); the minimum is obtained as the maximum of λ_max(ρ)·1 − ρ, which is PSD. No phase grid is used, so Stage 1's grid residual does not reappear as n^(d−1).

Theorem T1 (peak side). From (1), each term satisfies Re(e^{i(φ_j−φ_k)} ρ_jk) ≤ |ρ_jk|, so

    R_max − 1/d ≤ C_l1(ρ)/d,                                                             (3)

with equality if and only if there exist phases θ such that e^{i(θ_j − θ_k)} ρ_jk ≥ 0 for every j ≠ k with ρ_jk ≠ 0 — the state is *alignable* by a diagonal unitary (the torus is compact, so the supremum is attained). Every pure state is alignable (ρ_jk = c_j c_k*; take θ_j = −arg c_j). For a state with all off-diagonals nonzero, alignability is equivalent to the vanishing of every triangle phase

    τ_jkl = arg(ρ_jk ρ_kl ρ_lj),                                                          (4)

because the phases of ρ_jk then define a consistent assignment arg ρ_jk = θ_k − θ_j (the triangles generate all cycles of the complete graph). Full support is needed: a d = 4 state whose support graph is a 4-cycle can carry a cycle phase of π with every triangle product identically zero and still fail to be alignable (2.5b). τ_jkl is invariant under every diagonal unitary — it is exactly what a phase scan cannot remove. The frustration gap

    Δ(ρ) = (1 + C_l1)/d − R_max ≥ 0                                                      (5)

is zero iff ρ is alignable.

Alignability is a property of a single state, not a convex one. Diagonal unitaries, phase damping (all off-diagonals scaled by the same 1 − γ) and which-history records with real non-negative overlaps each preserve it. A convex mixture of alignable states need not be alignable: two copies of the equal-weight qutrit with relative kicks 0 and (0, 4π/5, 8π/5) mix to a state with τ = π exactly and Δ = 0.124 (2.8a), and a finite ensemble of equal-weight qutrits with independent static phase kicks — Stage 1's Experiment C construction with a third history — has τ ≠ 0 and Δ > 0 at every finite N, vanishing only as N → ∞ where independent kicks factorise (2.8b).

Theorem T1′ (trough side). By the same term-wise inequality R_min ≥ (1 − C_l1)/d, and by positivity of ρ, R_min ≥ 0; hence R_min ≥ max(0, (1 − C_l1)/d). The trough slack

    Δ_min(ρ) = R_min − max(0, (1 − C_l1)/d) ≥ 0                                           (5′)

is zero at d = 2 for every state (one pair can always be put in antiphase) and is generically positive for d ≥ 3 even when Δ = 0: the uniform-dephasing family (7) has Δ = 0 and Δ_min = γ/d − max(0, (1 − (d−1)(1−γ))/d) > 0 for 0 < γ < 1.

Theorem T2 (visibility bound). V_E in (2) is non-decreasing in R_max and non-increasing in R_min (∂V/∂R_max = 2R_min/(R_max + R_min)² ≥ 0, ∂V/∂R_min = −2R_max/(R_max + R_min)² ≤ 0). Substituting (3) and T1′: if C_l1 ≤ 1, V_E ≤ [(1 + C_l1) − (1 − C_l1)] / [(1 + C_l1) + (1 − C_l1)] = C_l1; if C_l1 > 1 the trough bound is R_min ≥ 0 and V_E ≤ 1; the two agree at C_l1 = 1. Hence

    V_E ≤ min(1, C_l1(ρ)).                                                               (6)

At d = 2 every state is alignable, C_l1 ≤ 1, and R_min = (1 − C_l1)/2 exactly, so (6) is the Stage 1 identity. The bound also holds for any *restricted* scan protocol (a subset of phase settings, e.g. a single relative phase), since restricting the scan can only lower R_max and raise R_min. The shortfall 1 − V_E/min(1, C_l1) decomposes into a peak-side part (what closing Δ would recover, computed by substituting R_max → (1 + C_l1)/d in (2)) and a trough-side remainder due to Δ_min; for generic mixed registers the trough-side part dominates (2.6).

Closed forms used for verification. For a pure state with amplitudes c_j: R(φ) = (1/d)|Σ_j e^{iφ_j} c_j|², so R_max = (Σ_j |c_j|)²/d and R_min = max(0, |c|_max − Σ_{others} |c_j|)²/d (zero when the moduli satisfy the polygon inequality). For the equal-weight state |ψ_d⟩ = d^{−1/2} Σ_j |j⟩ under uniform phase damping (every off-diagonal scaled by 1 − γ; identical to Stage 1's `dephase` at d = 2), ρ = (1 − γ)|ψ_d⟩⟨ψ_d| + γ·1/d and

    R_max = 1 − γ + γ/d,   R_min = γ/d,   V_E = (1 − γ)/(1 − γ + 2γ/d),   C_l1 = (d − 1)(1 − γ).   (7)

At d = 2, (7) gives V_E = 1 − γ = C_l1. For d ≥ 3 the two separate, and as d → ∞ at fixed γ < 1, V_E → 1 while C_l1/(d − 1) = 1 − γ is unchanged: a single bright output port says less and less about how coherent any one pair of histories is. For the two-member pentagon mixture of 2.8a, ρ_jk = (1/6)(1 + e^{i(κ_j − κ_k)}), so the moduli are (2cos(2π/5), 2cos(2π/5), 2cos(π/5))/6 =: (m, m, M), C_l1 = 2(2m + M), τ = π, and on the symmetric line of the constrained maximum, cos a* = m/(2M), S* = 2m cos a* − M cos 2a*, Δ = (2/3)(2m + M − S*). Quadratic onset of the gap at d = 3: Δ = (2/3)·min Σ_{pairs} |ρ_jk|(1 − cos α_jk) subject to Σ α_jk = τ (the φ's cancel around the cycle); a Lagrange multiplier gives α_jk ∝ 1/|ρ_jk| and

    Δ = τ² / ( 3 · Σ_{pairs} 1/|ρ_jk| ) + O(τ⁴)        (d = 3, one triangle).                 (8)

## 3. Verification

All numbers below are printed by `python3 echorym_qstate.py` (Stage 2 block). Every reported quantity is listed with its analytic expectation where one exists, its seed(s) and N, and its spread over seeds where an ensemble is involved. Numerical tolerance is double precision (~10⁻¹⁶ per operation). No entry departs from its expectation by more than 2σ; no entry departs at all beyond machine precision except where the quantity is an ensemble statistic with no closed form (2.6, 2.8b), where the spread is the result.

2.0 Correctness of the operation. Circuit response `multiport_response` versus the closed form (1) over 200 Hilbert–Schmidt-random states, d = 2..5, seed 2: max |difference| = 2.22 × 10⁻¹⁶ (expectation 0). ‖F_2 − HADAMARD‖_max = 8.66 × 10⁻¹⁷ (expectation 0). ‖d-level dephasing − Stage 1 `dephase`‖_max at d = 2, γ = 0.37: 1.39 × 10⁻¹⁷ (expectation 0).

2.0b Decoupled history. d = 3 with |2⟩ carrying population 0.2 but no coherence to the pair (ρ_02 = ρ_12 = 0; |ρ_01| = 0.3). The phase φ_2 is irrelevant and the reduced Hessian is singular, which is the case the pseudo-inverse in the Newton polish exists for. Expectation: R_max = 1.6/3, R_min = 0.4/3, V_E = 0.6 = C_l1, Δ = 0. Observed V_E = 0.6000; max |deviation| over the four quantities 4.44 × 10⁻¹⁶.

2.1 Regression to Stage 1. The same 200 random qubit states as Stage 1's identity check (seed 0): max |V_E(multiport) − 2|ρ_AB|| = 8.88 × 10⁻¹⁶ (expectation 0; the new optimiser removes Stage 1's grid residual); max |V_E(multiport) − V_E(Stage 1 grid)| = 3.36 × 10⁻⁵ (expectation: Stage 1's own grid residual, reported in the Stage 1 DN as 3.4 × 10⁻⁵ — identical).

2.2 Equal-weight pure register, d = 2..6. Expected R_max = 1, R_min = 0, V_E = 1, C_l1 = d − 1, Δ = 0. Observed: R_max = 1.0000, R_min = 0.0000, V_E = 1.0000, C_l1 = 1, 2, 3, 4, 5 and C_l1/(d−1) = 1.0000 for every d; Δ = −5.55, −4.44, −2.22, −6.66, −8.88 × 10⁻¹⁶ for d = 2..6 (machine zero).

2.3 Uniform dephasing of |ψ_d⟩, d = 3 and d = 5, γ ∈ {0, 0.25, 0.5, 0.75, 0.9, 1}. Observed V_E against (7): d = 3: 1.0000, 0.8182, 0.6000, 0.3333, 0.1429, 0.0000; d = 5: 1.0000, 0.8824, 0.7143, 0.4545, 0.2174, 0.0000; analytic values identical to four decimals. Max |numeric − analytic| over R_max, R_min and V_E across the sweep: 6.66 × 10⁻¹⁶. The ratio V_E/min(1, C_l1) at d = 3 runs 1.0000, 0.8182, 0.6000, 0.6667, 0.7143 (γ = 1 is 0/0, undefined); at d = 5: 1.0000, 0.8824, 0.7143, 0.4545, 0.5435. The bound (6) is tight only at γ = 0, and every state in this family has Δ = 0: the whole shortfall here is trough-side.

2.4 Haar-random pure states, d = 3, 4, 5; seeds 1000–1019, N = 100 per seed per d (6000 states). Expectation: T1 equality (Δ = 0) and the pure-state closed forms for R_max and R_min. Observed per-seed maximum |deviation| (over R_max, R_min, Δ): d = 3 mean 7.00 × 10⁻¹⁶, sd 8.92 × 10⁻¹⁷, max 8.88 × 10⁻¹⁶; d = 4 mean 6.36 × 10⁻¹⁶, sd 6.30 × 10⁻¹⁷, max 7.77 × 10⁻¹⁶; d = 5 mean 7.10 × 10⁻¹⁶, sd 9.44 × 10⁻¹⁷, max 8.88 × 10⁻¹⁶.

2.5 Alignable mixed states, d = 4; seeds 2000–2019, N = 100 per seed (2000 states). Construction: ρ = D ρ₊ D†, ρ₊ a three-term mixture of pure states with non-negative real amplitudes (all off-diagonals ≥ 0), D a random diagonal unitary. Expectation: Δ = 0 and all four triangle phases zero. Observed |Δ| per seed: mean 4.61 × 10⁻¹⁶, sd 3.96 × 10⁻¹⁷, max 5.55 × 10⁻¹⁶; max |τ_jkl| = 3.87 × 10⁻¹⁶ rad.

2.5b Support matters. d = 4, support graph a 4-cycle (ρ_02 = ρ_13 = 0), four equal moduli m = 0.1, cycle phase π (positivity asserted). Expectation: every triangle product zero, yet Δ = (2/4)·4m(1 − cos(π/4)) = 0.058579 because the four cycle angles must sum to π. Observed Δ = 0.058579; max triangle phase 0.0.

2.6 Hilbert–Schmidt-random full-rank mixed states, d = 3, 4, 5; seeds 3000–3019, N = 200 per seed per d (12 000 states). Expectation for the theorems: zero violations of T1 (Δ ≥ −10⁻⁹) and T2 (V_E ≤ min(1, C_l1) + 10⁻⁹). Observed: 0 violations of either, at every d. Ensemble statistics (no closed form; mean ± sd over the 20 seeds of the per-seed value):

| d | fraction with Δ > 10⁻⁹ | median d·Δ/C_l1 | median V_E / min(1, C_l1) | mean shortfall 1 − V_E/min(1, C_l1) | peak-side part of shortfall |
|---|---|---|---|---|---|
| 3 | 0.999 ± 0.002 | 0.0230 ± 0.0053 | 0.8756 ± 0.0090 | 0.1378 ± 0.0059 | 0.0082 ± 0.0013 (5.9 %) |
| 4 | 1.000 ± 0.000 | 0.0930 ± 0.0063 | 0.8561 ± 0.0089 | 0.1523 ± 0.0049 | 0.0099 ± 0.0005 (6.5 %) |
| 5 | 1.000 ± 0.000 | 0.1490 ± 0.0095 | 0.8860 ± 0.0039 | 0.1244 ± 0.0029 | 0.0113 ± 0.0006 (9.1 %) |

Over 90 % of V_E's under-reading of the bound is trough-side slack (5′); the frustration gap accounts for 6–9 %. Among the 4000 d = 3 states, 4 had Δ ≤ 10⁻⁹, with (Δ, τ) = (1.1 × 10⁻¹¹, 2.3 × 10⁻⁵), (6.3 × 10⁻¹⁰, 1.8 × 10⁻⁴), (1.3 × 10⁻¹⁰, 9.1 × 10⁻⁵), (4.5 × 10⁻¹⁰, 2.4 × 10⁻⁴); each pair is consistent with the quadratic onset (8). At d = 4 and 5 no state had Δ ≤ 10⁻⁹.

2.6b Quadratic onset (8), d = 3, τ = 10⁻³; seeds 4000–4019, N = 50 per seed. Construction: full-rank alignable ρ₊ (mixture plus 0.1·1/3) with one off-diagonal rotated by τ; positivity asserted for every state. Observed max relative error |Δ − prediction|/prediction per seed: mean 5.51 × 10⁻⁸, sd 1.23 × 10⁻⁸, max 8.36 × 10⁻⁸ (expectation: O(τ²) ≲ 10⁻⁶).

2.7 Optimiser adequacy, d = 3, seed 7, 40 Hilbert–Schmidt-random states. A dense 360 × 360 grid over the two free phases is compared with the ascent: max (grid R_max − ascent R_max) = −6.43 × 10⁻⁸; max (ascent R_min − grid R_min) = −3.38 × 10⁻⁷. Both negative (expectation ≤ 0, magnitude of order the 1° grid's second-order resolution): the grid never found a better extremum than the ascent.

2.8 Non-alignable states from convex mixing (Stage 1's Experiment C construction at d = 3). (a) Two-member pentagon mixture of |ψ_3⟩ with kicks 0 and (0, 4π/5, 8π/5). Expectation: τ = π, C_l1 = (2/3)(2cos(2π/5) + cos(π/5)) = 0.951367, Δ = 0.124226 from the symmetric-line formula in §2. Observed τ = 3.141593, C_l1 = 0.951367, Δ = 0.124226; V_E = 0.9402 against min(1, C_l1) = 0.9514 — here the bound is nearly tight despite a 12 % frustration gap, because R_min is small. (b) 500-member ensemble of |ψ_3⟩ with independent Gaussian static kicks (σ = 1.2) per history — Stage 1's Experiment C parameters — seeds 5000–5019. Expectation: τ and Δ nonzero at finite N and → 0 as N → ∞. Observed |τ| mean 0.1929, sd 0.1100, max 0.4074 rad; Δ mean 4.22 × 10⁻⁴, sd 4.13 × 10⁻⁴, max 1.51 × 10⁻³.

Stage 1 table: unchanged, line for line, from the Stage 1 DN (Experiment C ensemble V_E = 0.563; identity residual 3.36 × 10⁻⁵).

## 4. Checks

Correctness conditions — theorems and unit tests; cannot fail unless the code is wrong:

- CC-1. `multiport_response` equals the closed form (1) for every state and phase setting (2.0). Failure would mean the circuit is not implementing U_φ then F_d.
- CC-2. F_2 = HADAMARD and the d-level dephasing coincides with Stage 1's `dephase` at d = 2 (2.0); at d = 2 the multiport V_E equals 2|ρ_AB| for every state (2.1). Failure would mean Stage 2 is not a strict extension of Stage 1.
- CC-3. Theorem T1: Δ ≥ 0 for every state (2.6, zero violations over 12 000 states) with equality for every pure state (2.4), every alignable mixed state (2.5) and the decoupled-history state (2.0b). Failure would mean either the extremum search returned a value above the true maximum (impossible for a feasible point) or C_l1 is mis-computed.
- CC-4. Theorem T2: V_E ≤ min(1, C_l1) for every state (2.6, zero violations); equality at d = 2 (2.1); the closed form (7) under uniform dephasing to machine precision (2.3).
- CC-5. Alignability ⇔ vanishing triangle phases on full-support states: Δ = 0 with τ = 0 in 2.5; Δ > 0 accompanies τ ≠ 0 in 2.6; the quadratic onset (8) holds to 10⁻⁷ relative at τ = 10⁻³ (2.6b); the full-support hypothesis is necessary (2.5b, analytic Δ reproduced to six decimals).
- CC-6. Optimiser soundness: every returned R_max (R_min) is the value at a feasible phase setting, so a bug can only under-state R_max or over-state R_min; neither can manufacture a violation of T1 or T2. The equality checks 2.0b, 2.2, 2.4, 2.5, 2.5b, 2.8a and the grid comparison 2.7 are what detect an optimiser that stops short.
- CC-7. Non-convexity of alignability: the pentagon mixture has τ = π and the analytic Δ (2.8a). Failure would mean either the triangle-phase or the constrained-maximum arithmetic is wrong.

Falsifiable claims — contingent; could fail with correct code:

- FC-1a (the design claim of the stage). For generic mixed registers the framework's V_E under-reads min(1, C_l1) by a margin far above numerical tolerance — mean shortfall 12–15 % for d = 3, 4, 5 under the Hilbert–Schmidt measure (2.6), and 40 % at d = 3, γ = 0.5 in the alignable family (7). Named failure mode: ensemble misspecification — if the registers the world produces are nearly pure, R_min ≈ 0 and T2 is nearly tight (V_E ≈ 1 whenever C_l1 ≥ 1), and V_E would serve as a proxy after all. If it fails: the recommendation in §8 (report C_l1/(d − 1) alongside V_E for d ≥ 3) stands as harmless, but the argument that V_E is *insufficient* is withdrawn; T1, T1′ and T2 are untouched.
- FC-1b. Generic mixed registers are frustrated: Δ > 0 in ≥ 99.9 % of Hilbert–Schmidt-random states at d = 3, 4, 5 (2.6), and finite inhomogeneous-dephasing ensembles of three or more histories are frustrated at every finite N (2.8b). Named failure mode: the world's mixing processes might be of the alignability-preserving kind only (diagonal unitaries, uniform dephasing, real-overlap records applied to alignable states), or its ensembles effectively infinite, in which case Δ = 0 throughout Echorym and the peak side of T1 is always an equality. If it fails: Δ becomes a quantity the register *can* have but never does in the world; §8's proposal P-2 loses its gauge-invariant fields; nothing else changes.
- FC-2 (numerical adequacy beyond the tested case). The random-restart ascent with Newton polish finds the global extrema for d ≤ 5. Verified against a dense grid at d = 3 only (2.7) and against closed forms wherever they exist; for Hilbert–Schmidt-random states at d = 4, 5 it is an extrapolation. Named failure mode: a multi-basin landscape at higher d that 32 restarts miss, under-stating R_max and hence over-stating Δ and under-stating V_E. If it fails: the 2.6 statistics at d = 4, 5 become one-sided (lower bounds on V_E, upper bounds on Δ); the theorems are unaffected (CC-6).
- FC-3 (trend). The median normalised gap d·Δ/C_l1 grows with the number of histories (0.023 → 0.093 → 0.149 for d = 3 → 5), i.e. generic registers become more frustrated as d grows. Within d ≤ 5 this is established by the spreads; the claim beyond d = 5 is the contingent part. Named failure mode: non-monotone behaviour beyond d = 5, or dependence on the random-state measure. If it fails: the qualitative sentence "more histories, more frustration" is retracted; nothing else in the stage depends on it. The companion ratio V_E/min(1, C_l1) is already *not* monotone in d (0.876, 0.856, 0.886), so no trend claim is made for it.

Not a falsifiable claim, stated so it is not mistaken for one: the Stage 1 identity V_E = C_l1 at d = 2 is a theorem, and its d ≥ 3 replacement by T1/T1′/T2 is a theorem. Neither can be falsified by any state.

## 5. Level labels

- ρ (d × d density matrix), C_l1, C_re, C_l1/(d − 1): Level 3 (physical quantities of a d-level system).
- R(φ), R_max, R_min: Level 3 (output-port probabilities of a physical circuit).
- V_E: the framework's Level 2 operational analogue. On this substrate it is a Level 3 quantity (a function of Level 3 probabilities), but for d ≥ 3 it is a *witness* bounded by the Level 3 measure, not the measure itself; only at d = 2 does the Level 2 definition coincide with the Level 3 measure.
- Δ (frustration gap), Δ_min (trough slack), τ_jkl (triangle phases): Level 3.
- d (number of histories in one register): a parameter, Level 1 until the region → register mapping fixes it.
- "Frustration", "alignable", "slack": Level 1 labels for the Level 3 quantities Δ, τ and Δ_min; they carry no meaning beyond (4)–(5′).
- The Hilbert–Schmidt ensemble of 2.6: a Level 1 stand-in for an unknown world distribution of states, not a model of anything Echorym does. The ensembles of 2.8 are Stage 1's own construction and carry whatever level Stage 1 gave it (Level 3 states; Level 2 as a model of "inhomogeneous dephasing").

## 6. Cost accounting

Computational scaling of the new operation. One response evaluation is O(d²). The scan costs, per extremum, O(R·I_J·d²) for the Jacobi ascent (R = 32 restarts, I_J ≤ 60 iterations) plus O(R·I_N·d³) for the Newton polish (I_N ≤ 30 batched (d−1)×(d−1) pseudo-inverses), two extrema per state; in the harness this is a few milliseconds per state at d ≤ 6, dominated by Python overhead. Ensemble size N enters linearly. Time steps do not enter — the stage is static; a dynamics sweep with T steps multiplies the cost by T. A grid scan would instead cost O(n^(d−1)·d²), exponential in the number of histories, which is why the optimiser is used and why FC-2 exists. The whole module runs in about 2 min 20 s on one core.

Cost on a real substrate. A QKD-Aero polarization state is a two-level system: it can run Stage 2 only at d = 2, where it adds nothing to Stage 1. For d ≥ 3 the register must be carried in a d-mode encoding (path, time-bin or spatial modes) through a balanced d-port multiport with d − 1 controllable phase shifters. Resolving one response R to ±ε needs about R(1 − R)/ε² ≤ 1/(4ε²) detection events per phase setting; a full n-point-per-phase scan therefore needs ~n^(d−1)/(4ε²) events — for d = 3, n = 36, ε = 0.01 about 3 × 10⁶ events, i.e. tens of seconds at 10⁵ detections per second — and an adaptive (ascent-style) scan needs a comparable number of settings without the exponential factor. The systematic that matters is multiport imbalance, which enters R_max at first order; phase-shifter noise enters only at second order because R_max is stationary in the phases. Since the normalised gap for typical states is 2–15 % (2.6), the multiport must be balanced to better than ~1 % before a measured Δ means anything. On a gate-model device the same test is a qutrit (or two-qubit-encoded) Fourier gate with virtual phase gates and 10³–10⁴ shots per setting for ε ~ 0.01. These are order-of-magnitude figures, not a design.

Parameters this stage needs from the world that no note has yet set: (i) d — how many histories one register holds, and whether "d histories" is one d-level register or a collection of pairs (the two are different objects with different coherence bounds); (ii) the scan protocol — whether the world's recombination can vary all d − 1 relative phases or only one (T2 holds either way; only the full scan reaches equality at d = 2); (iii) the readout — one port or the full output distribution; (iv) the world's mixing processes — which of them are alignability-preserving (diagonal unitaries, uniform dephasing, real-overlap records) and which are convex mixtures of differently-kicked members, since only the latter give Δ a world instance; (v) the distribution of registers the world actually produces, without which FC-1a/b cannot be evaluated against anything but a stand-in ensemble.

## 7. Open-problems ledger (DN-staging-and-phase-travel-v0.4.1 §13)

1. C1 small-sample estimation — not touched: this stage has no estimator and no participant data.
2. Stale-reference detection — not touched: no anchors or reference drift appear in a static register.
3. Region → register mapping — sharpened: the register now has d basis states, and the mapping must additionally decide (a) d, (b) whether the world varies one relative phase or d − 1, and (c) which world processes are convex mixtures of differently-phased members (these, and only these, produce a frustrated register); until (c) is answered, Δ has a physics instance (2.8) but no world instance.
4. QEC threshold transfer — not touched.
5. Moiré buildability (closed in v0.4.1) — not touched.
6. Intervention thresholds — not touched; nothing here supplies a threshold or a number for one.
7. Identity across reconstruction — not touched.
8. Export ceiling testability — not touched.
9. Module decoherence coefficient — touched: at d ≥ 3 a which-history record acts pairwise — it multiplies each ρ_jk by its own overlap ⟨e_k|e_j⟩, so a single per-module distinguishability becomes a d × d overlap matrix per module; if those overlaps are real and non-negative the record preserves alignability (T1 stays an equality), and if they are complex it does not. The rate remains unset.
10. Participant memory and novelty — not touched.
11. Provenance authenticity (build the detector where authenticity is free) — not touched.

## 8. What this stage does not claim

It does not claim that Echorym's histories, regions, agents or participants are quantum systems, or that any of them is one of the d basis states. It does not claim that V_E is wrong — it shows V_E is a valid witness (T2) that is a measure only at d = 2, and recommends, as a proposal, that any d ≥ 3 report carry C_l1/(d − 1) beside V_E. It does not claim that the frustration gap occurs in Echorym: the gap has a physics instance inside the series (Stage 1's inhomogeneous-dephasing construction at d = 3, 2.8), but whether any world process is a convex mixture of that kind is open problem 3(c). It does not claim that Δ is the reason V_E ≠ C_l1 for d ≥ 3; the larger reason is trough-side slack, which alignable states share. It does not claim that the triangle phases τ_jkl are a geometric phase, a holonomy, or an input to Stage 5; their only established property here is invariance under diagonal unitaries. It does not claim recoherence or non-Markovianity: the stage has no dynamics and no environment; the uniform dephasing in 2.3 and the ensembles in 2.8 are static families of states, not processes, and Stage 1's refocus is not applied to them here. It does not touch measurement (Stage 3) or a structured environment (Stage 4). It does not estimate T_2,E or T_recohere,E. It does not derive or constrain the coherence-gate thresholds. The quadratic onset (8) is derived for d = 3 with one triangle; no general-d small-τ law is claimed.

Proposed amendments, recorded here and not applied: (P-1) Coherence framework §5.1 — when the recombination test involves more than two histories, V_E should be labelled a witness and C_l1/(d − 1) reported as the Level 3 measure, with V_E ≤ min(1, C_l1) stated as the relation between them. (P-2) Coherence framework §13, `BranchRelation` — a relation object for more than two branches cannot carry one `relative_phase_like_parameter`; the physical content is the set of off-diagonals ρ_jk (or, gauge-invariantly, their moduli plus the cycle phases of the support graph, which for full support are the triangle phases τ_jkl).

## 9. Narrative imports

- [interpretation] Physics → world. d basis states with all populations nonzero ↔ d histories or regions "held open at once"; C_l1 → 0 with the diagonal intact ↔ histories that are remembered but can no longer be recombined — the framework's memory-versus-coherence distinction, now for more than two. The physics does not license identifying any world object with a basis state.
- [interpretation] Physics → world. A nonzero frustration gap Δ ↔ a set of pairwise relations that cannot all be honoured at once (a triangle of relations with a net twist), arising when differently-drifted copies of the same alternatives are pooled. The physics does not license this; Δ is a property of a d × d matrix, and no world process has been identified as the pooling.
- [interpretation] Physics → world. V_E → 1 as d grows at fixed dephasing (7) ↔ a caution that a bright recombination response says less about any single relation the more alternatives are in play. The physics does not license reading any world response this way.

## 10. Firewall

C_l1 (in either its raw or its normalised form), V_E, Δ, Δ_min and τ_jkl are not identified with the schemas' `coherence.current` or with the five coherence-gate thresholds (0.376, 0.618, 0.786, 0.886, 1.000); they remain different quantities, and no stage has derived one from the other.

## 11. Class IV boundary statement

Nothing in this stage is about neural, human, or narrative state. |0⟩ … |d−1⟩ are orthogonal basis states of a d-level quantum system, F_d is a unitary on it, and every quantity reported is a function of a d × d density matrix. Any Echorym meaning attached to the basis states, to the phases, to the gap, or to the response is an interpretation layered on top and is labelled as such in §9. No neural–quantum coupling claim is made or implied.

---

## Appendix A — Review requests

Adversarial review (what could be wrong):

- A-1. Alignability ⇔ zero triangle phases is proved for full-support states; 2.5b shows the hypothesis is necessary. Check whether the module's 2.6 classification (Δ > 10⁻⁹) could mislabel a nearly-zero-support state, and whether P-2's "cycle phases of the support graph" is the right general object.
- A-2. The optimiser (FC-2): 31 random restarts plus the in-phase point, Jacobi then Newton. Look for a d = 4 or 5 state with two near-degenerate basins where the reported R_max is a local maximum; the grid comparison exists only at d = 3. (A first review with 512–1024 restarts on 60 generic and 300 two-basin d = 5 states found no improvement above 10⁻⁹; this is recorded, not relied on.)
- A-3. The Newton polish removes the global-phase gauge by fixing φ_0 = 0 and uses a pseudo-inverse (rcond 10⁻¹²) so that a singular reduced Hessian (2.0b) does not abort it. Check whether a *nearly* singular Hessian could produce a large step rejected at every backtracking level and leave that restart at its Jacobi value.
- A-4. The Hilbert–Schmidt ensemble is a choice; the FC-1a/b statistics would differ under Bures or rank-restricted measures. Decide whether any ensemble belongs in the DN at all, or whether 2.6 should report only the zero-violation counts and the decomposition.
- A-5. (7) and 2.8 treat "uniform dephasing" and the kick ensembles as state families; confirm the DN nowhere reads them as processes (rule: no recoherence or non-Markovianity claim).
- A-6. The pentagon-mixture Δ (2.8a) is computed on the symmetric line α = β; the optimiser agreed to six decimals, which is evidence the symmetric point is the global constrained maximum, not a proof. Prove or exhibit a counterexample.
- A-10. The README entry's standing sentence "C_l1 also runs from 0 to 1" is true of Stage 1 only; after Stage 2 the raw C_l1 runs to d − 1 and it is C_l1/(d − 1) that runs 0 to 1. Only the Stage 2 line was appended this week, per the one-line rule; the sentence should be corrected when the README is next edited.

World-side review (what the world must decide):

- W-1. d: how many histories can one register hold, and is a "region with d alternatives" one d-level register or d − 1 pairs? The coherence bounds differ (C_l1 ≤ d − 1 versus ≤ 1 per pair).
- W-2. Which relational parameters can the world vary in a recombination — one relative phase, or all d − 1? T2 holds regardless; tightness at d = 2 needs the full scan.
- W-3. What is read out — one port (R as here) or the whole output distribution? The framework's V_E is one-port; the full distribution carries more of ρ.
- W-4. Which world processes are convex mixtures of differently-phased members (pooling of drifted copies, aggregation across participants or sessions), as opposed to alignability-preserving operations? Only the former give the frustration gap a world instance; the answer decides whether P-2's gauge-invariant fields are needed.
- W-5. Whether the framework's V_E should remain the headline quantity for d ≥ 3 or be replaced by C_l1/(d − 1) as P-1 proposes — a naming decision with consequences for every downstream note.
- W-6. What distribution of registers the world produces, so that FC-1a/b can be evaluated against something other than a stand-in ensemble.

## Development record

| Model and version | Dates of use | Role |
|---|---|---|
| Claude, configured identifier `claude-fable-5-1` (the configured model of the weekly run that produced this note; the serving model can differ within a session) | 2026-09-13 (UTC; the note was filed at 07:03 UTC) | Drafted this note and the Stage 2 block of `echorym_qstate.py`. The session record was not found; whether the module was executed in that session, and whether a second instance reviewed the draft as the Review line above states: Needs author confirmation |
| Claude, configured identifier `claude-opus-5-5` | 2026-11-05 | Edited this note for the public copy under the review of 2026-11-05 (cross-references, citations and internal review items; no result changed); executed the full module (Stages 1–6) before and after the edit and found its printed output unchanged |

Author: Lana C. Waddell.
