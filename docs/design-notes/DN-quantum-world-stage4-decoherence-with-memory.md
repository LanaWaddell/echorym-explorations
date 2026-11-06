Redaction status: cross-references and internal review notes edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05

# DN-quantum-world-stage4: decoherence with memory — a structured environment kept as a quantum system

Status: design note, week of 2026-09-27. Fourth step on the staged path (state → coherence → superposition → interference → measurement → decoherence → later stages). This stage: decoherence with memory — a structured environment kept as a quantum system, tested against a Markovian control matched in decay.
Depends on: DN-quantum-world-stage1-history-pair-state, DN-quantum-world-stage2-multiport-histories, DN-quantum-world-stage3-measurement-as-constraint, Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline; §5.4–5.5 T_2,E and T_recohere,E; §7 dynamical-decoupling analogue; §10 the erased-record question; §12), DN-staging-and-phase-travel-v0.4.1 (§7.2 rate law, §7.10, §13).
Artifact: `echorym_qstate.py`, Stage 4 block appended; runs standalone with numpy (`python3 echorym_qstate.py`, about 2 min 6 s on one core, prints the verification table for Stages 1–4; the Stage 1, 2 and 3 output is unchanged line for line, checked by diff against the pre-Stage-4 run).
Stop-condition check: this stage does not require a decision about which world-object the register represents. An environment kept as a quantum system, coupled to the register's history variable, is defined at the physics level exactly as Stage 1's environment qubit was; every world-side parameter the stage exposes — what an environment mode is, how many there are, their own frequencies, whether the register can be reversed while coupled — is listed in §6 as unset rather than assumed.
Results flagged up front: (i) on this substrate at d = 2 a coherence revival and BLP information backflow are not independent evidence of memory — the coherence series and the BLP trace-distance series are the same series, |D(t)| (T7) — and the absence of any revival in the matched Markovian control is a theorem (T9); what is contingent is whether a given bath revives at all within a horizon, and it does here (FC-1). (ii) One pre-registered claim is refuted in its strict form: at d ≥ 3 a pair's backflow can be masked in C_l1(t) — 7.7 % of backflow episodes are invisible to the register-level measure (FC-2). (iii) The staging note's rate law "frequent shallow revisits outperform rare deep ones" holds only above the environment's dressed frequency; below it, adding pulses can make retention worse, to zero (FC-3, resonance).
Class IV boundary: unchanged (§11).

## 1. Concept

Stages 1 and 3 discarded the environment: Stage 1 traced out a record qubit at a fixed overlap, Stage 3 produced a classical record. Both were memoryless by construction, and both notes said so — no recoherence could be claimed because nothing in the model could return. Stage 4 keeps the environment as a quantum system for the whole run. The register is coupled to a bath of independent two-level environment modes through its history variable; each mode has its own Hamiltonian, so the record it holds is not frozen — the branch states of the environment move, and their overlap can grow again after it has shrunk. The register's reduced state is computed exactly at every time, together with the decoherence functions that carry all of the environment's effect.

Three things come out. First, the environment's memory is visible in the register: the l1 coherence falls and then partly returns, and a memoryless model matched to the same coherence horizon T_2 cannot do this. Second, at d = 2 the return of coherence, BLP information backflow and the failure of CP-divisibility are one and the same event in time, so at d = 2 they are not independent evidence of memory; they separate only at d ≥ 3, where a pair can recohere while the register-level measure keeps falling and where the dynamics can stop being divisible before any pair revives. Third, a reversal of the register while it is still coupled — the framework's refocusing operator acting on the current state, and the staging note's "transit is the pulse" — refocuses a static environment exactly and a dynamic one only partly, which gives T_2,E and T_recohere,E their first Level 3 estimates and gives the rate law its condition and its failure mode.

## 2. Formalization

Environment and coupling. The register is a d × d density matrix ρ in the history basis with charges c_k = (d − 1)/2 − k (so that at d = 2 the two branches differ by g σ_z, as Stage 1's environment qubit did). The environment is a bath of n independent modes, mode i a spin-½ with Hamiltonian −(ω_i/2) σ_x^(i), initial pure state |ψ_i⟩ (default |+⟩, the ground state of its own Hamiltonian), and coupling g_i c_k σ_z^(i) to history k. The joint Hamiltonian is

    H = Σ_k |k⟩⟨k| ⊗ H_k,      H_k = Σ_i [ −(ω_i/2) σ_x^(i) + g_i c_k σ_z^(i) ].                          (1)

ω_i = 0 is a static bath (each mode a frozen record); ω_i > 0 gives the bath its own dynamics. Because H is block-diagonal in the history basis the evolution is pure dephasing, exactly:

    ρ_jk(t) = ρ_jk(0) D_jk(t),      D_jk(t) = Tr_E[ W_j(t) ρ_E W_k(t)† ],      W_k(t) = e^{−iH_k t},        (2)

and populations never change: state retention is never lost in this stage, only relations are. For a product bath D_jk factorises, D_jk(t) = Π_i ⟨ψ_i| W_k^(i)(t)† W_j^(i)(t) |ψ_i⟩, so n = 32 modes cost 32 two-by-two problems; the factorised form is checked against the literal joint density matrix on d·2^n dimensions for n = 3 (4.0). [D_jk(t)] is the Gram matrix of the environment branch states W_k|ψ_E⟩ and is therefore positive semidefinite (T8). Its diagonal is 1, and |D_jk| = 1 − (distinguishability of the branch records), so at d = 2 the reduced state at time t is exactly Stage 1's `couple_to_environment` with distinguishability 1 − |D(t)| after the phase arg D(t) is removed (4.1).

Pulses. A pulse at time t_p is a register-side permutation π applied to the joint state, |k⟩ → |π(k)⟩, while the register is still coupled. The reversal k → d − 1 − k negates every charge. After the pulse the branch that was labelled k continues under H_{π(k)}, so the propagators become ordered products; the module tracks the label map and reports ρ_jk(t) = ρ_{σ(j)σ(k)}(0) D_jk(t) with σ the accumulated relabelling. An even number of reversals restores the populations to their original labels.

Markovian control. The memoryless comparison is the pure-dephasing semigroup with the same charges,

    ρ_jk^M(t) = ρ_jk(0) exp(−γ (c_j − c_k)² t/2),                                                            (3)

with γ fixed by bisection so that C_l1^M(T_2) = C_l1(0)/e at the same time T_2 as the structured model (matched decay). (3) is the Lindblad dephasing with jump operator √γ Σ_k c_k |k⟩⟨k|; its rate matrix is a Gaussian kernel in the charges and so every intermediate map is completely positive.

Theorem T7 (d = 2). For any qubit state C_l1(t)/C_l1(0) = |D(t)|, and the trace distance between the evolved states of |A⟩+|B⟩ and |A⟩−|B⟩ is |D(t)| (their difference is σ_x, which the map sends to D|A⟩⟨B| + h.c., of trace norm 2|D|). For any other pair the trace distance is √(Δp² + |Δc|²|D|²) with |Δc| ≤ 1, so its increase over any interval is at most the increase of |D|; the BLP measure is therefore exactly the sum of the increases of |D(t)|, attained by the |±⟩ pair. At d = 2 the coherence series C_l1(t)/C_l1(0), the BLP trace-distance series and |D(t)| are one series; a revival of one is a revival of the others. The scalar summaries R (largest rise above the running minimum) and N (sum of all rises) summarise that one series differently and are not equal.

Theorem T8 (divisibility). ρ → ρ ∘ D(t) (Hadamard product) is completely positive iff [D_jk(t)] is positive semidefinite, which it always is here. The intermediate map from t to t′ is the Hadamard product with M_jk = D_jk(t′)/D_jk(t) and is completely positive iff M is positive semidefinite. At d = 2, M = [[1, r], [r*, 1]] with r = D(t′)/D(t) has eigenvalues 1 ± |r|, so the map is CP-divisible at a step iff |D| does not increase there: CP-divisibility (the RHP criterion) and BLP backflow coincide with each other and with the revival of C_l1. For d ≥ 3 the condition "M PSD" is strictly stronger than "no pair's modulus increases": the 3 × 3 matrix with unit diagonal and off-diagonals (1, 1, 0) is not PSD. To first order in a step, M = J + δt·L with J the all-ones matrix and L_jk = d ln D_jk/dt, and M is PSD iff L is positive semidefinite on the complement of the all-ones vector; for real D at d = 3 with decay rates a_jk = −d ln D_jk/dt this is the condition that the rate matrix a be conditionally negative definite, i.e. that the square roots of the three rates satisfy the triangle inequality; to first order the step is not CP-divisible iff √a_jk > √a_jl + √a_kl for some pair (Schoenberg's criterion for three points; the exact finite-step eigenvalue lags this slightly, which is why the t = 0.02 entry of 4.5 is still positive). When D is complex the phase rates enter M as well; the module tests the exact Hermitian M and the triangle form is the real special case. At short times a_jk ∝ (c_j − c_k)² (T12), so √a ∝ |Δc| and the charges (1, 0, −1) sit exactly on the boundary (three collinear points); the t⁴ corrections make the Δc = 2 pair decay faster than the collinear bound allows, so divisibility fails long before any pair revives (4.5).

Theorem T9 (control). (3) is monotone in t for every pair, so the control has zero revival and zero backflow for every state, and is CP-divisible.

Theorem T10 (static echo). If every ω_i = 0 the H_k commute, a reversal at T/2 swaps the branch propagators, and W_j(T) = W_k(T) for every pair: D(T) = 1 for every state, bath and T. Stage 1's `refocus` acted on the reduced state after the environment had been discarded and could not do this; the echo acts while the environment is still coherent.

Theorem T11 (independent environments multiply). Two baths acting on the same register give D = D^(1) D^(2) elementwise.

Theorem T12 (short times). D_jk(t) = 1 − ½ Var(H_j − H_k) t² + O(t³), the cubic term being purely imaginary so that |D| = 1 − ½ Var t² + O(t⁴); for |+⟩ modes Var = Σ_i g_i² (c_j − c_k)². The Gaussian estimate of the 1/e time at d = 2 is √(2/Σ_i g_i²).

Theorem T13 (one mode, d = 2, |+⟩). D(t) = 1 − (2g²/(g² + ω²)) sin²(Ωt) with 2Ω = √(g² + ω²) the dressed mode frequency; ω = 0 gives D = cos(gt). D is real for a pair of branches with opposite charges (the σ_z and σ_y expectations vanish in |+⟩), which is every pair at d = 2, so it can change sign; a pair with |c_j| ≠ |c_k| has complex D even for |+⟩ modes. For charges (1, 0, −1) the symmetry c → −c of |+⟩ modes gives D_12 = D_01*, so the register's triangle phase is arg(|D_01|² D_02) ∈ {0, π}: a sign change of the Δc = 2 pair gives a triangle phase of π (Stage 2, (4)) and a frustration gap. For modes not in |+⟩ the symmetry is broken and the register acquires a continuous triangle phase arg(D_01 D_12 D_20) — the environment can create Stage 2's frustration in an alignable register by dynamics alone (4.4b).

Horizons. T_2 is the first time C_l1(t)/C_l1(0) ≤ 1/e (linear interpolation on the grid). T_recohere is the first T at which a single reversal at T/2 leaves C_l1(T)/C_l1(0) ≤ 1/e. Revival amplitude R is the largest rise of C_l1(t)/C_l1(0) above its running minimum (zero iff the series is non-increasing); backflow N is the sum of the increases of |D(t)| (the BLP measure at d = 2 by T7; a per-pair lower bound at d ≥ 3). Pulses at Carr–Purcell timing are n_p reversals at (k − ½)T/n_p.

## 3. Verification

All numbers below are printed by `python3 echorym_qstate.py` (Stage 4 block). Units: g_0 = 1 sets the coupling scale; couplings and frequencies are drawn g_i, ω_i ~ U(0.5, 1.5) unless stated; the horizon is T = 20 on a 2001-point grid (δt = 0.01). Every quantity is listed with its analytic expectation where one exists, its seed(s) and N, and its spread over seeds where an ensemble is involved. Every closed-form check agrees to machine precision. Two entries depart from their pre-registered expectation by more than 2σ and are flagged: 4.4 (FC-2, fraction of pair-backflow episodes visible in C_l1: expected 1, observed 0.923 ± 0.062 per seed, i.e. 5.5 standard errors below 1 over 20 seeds) and 4.7 (FC-3 in its unconditional form: expected monotone in n_p, observed monotone in 0/20 seeds over the whole range; the conditional form holds 20/20). Both are refutations of contingent claims, not numerical discrepancies.

4.0 Correctness. 15 (state, bath, pulse) triples: Hilbert–Schmidt-random states, d = 2, 3, 4, n = 3 modes with random initial Bloch angles, one pulse at t = 2.3 (the reversal or a random permutation), 13 times in [0, 6], seed 4. Expectation: the factorised operation equals the literal joint density-matrix evolution on d·8 dimensions; unit trace; populations equal to the initial ones up to the label map; [D_jk(t)] positive semidefinite (T8); D for a 4-mode bath equals the product of the D's of its two 2-mode halves (T11). Observed: max |deviation| = 2.11 × 10⁻¹⁵; max |Tr − 1| = 2.66 × 10⁻¹⁵; max |population change| = 1.44 × 10⁻¹⁵; min eigenvalue of [D_jk(t)] = −5.66 × 10⁻¹⁶ (machine zero); max ‖D^(1)D^(2) − D^(12)‖ = 2.23 × 10⁻¹⁶.

4.1 Contact with Stage 1 and closed forms. d = 2, 50 random qubit states × 41 times in [0, 8], 4 tilted modes, seed 41. Expectation: ρ(t) = `couple_to_environment`(phase-rotated ρ, 1 − |D(t)|). Observed max deviation 2.11 × 10⁻¹⁵. (T13) one mode, g = 0.7, ω = 1.3, 2001 times: max |D − closed form| = 5.57 × 10⁻¹⁶; static (ω = 0): max |D − cos(gt)| = 3.51 × 10⁻¹⁶. (T12) n = 8 (seed 42), t = 10⁻²: (1 − D)/(Σg_i² t²/2) − 1 = −2.70 × 10⁻⁴ (expectation O(t²) ≈ 10⁻⁴).

4.2 The revival test. Equal-weight pair (Stage 1's Experiment A state), n = 8, seeds 4200–4219. Structured bath: T_2 = 0.4917 ± 0.0536 (expectation from the short-time Gaussian, √(2/Σg_i²) averaged over the same baths: 0.4994); revival amplitude R = 0.2011 ± 0.1598 (min 0.0513, max 0.6230); BLP backflow N = 0.4919 ± 0.3784; separate rises above 0.02: 4.45 ± 2.29 per seed; seeds with R > 0.02: 20/20; time of the largest revival 8.44 ± 4.88. Markovian control matched at T_2: γ = 4.1163 ± 0.4504 (at d = 2 this is 2/T_2 exactly, since (Δc)² = 1); R = 0 and N = 0 for every seed (T9; printed 0.00 × 10⁰). Seed 4200, C_l1(t)/C_l1(0), structured against control:

| t | 0 | 0.25 | 0.5 | 1 | 2 | 3 | 4 | 6 | 8 | 12 | 16 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| structured | 1.0000 | 0.7372 | 0.2839 | 0.0024 | 0.0000 | 0.0002 | 0.0307 | 0.0013 | 0.0017 | 0.0010 | 0.0000 | 0.0000 |
| control | 1.0000 | 0.5720 | 0.3272 | 0.1071 | 0.0115 | 0.0012 | 0.0001 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

Matched at T_2 ≈ 0.49, the Gaussian short-time law keeps the structured coherence above the exponential before T_2 and below it just after; later the structured curve returns above the control repeatedly (at t = 4 it is 0.0307 against the control's 0.0001) — the curves cross many times, not once.

4.3 Theorem T7. 20 (state, bath) pairs × 101 times in [0, 10], random qubit states with |ρ_AB| ≥ 0.05, 6 tilted modes, seed 43. Expectation: C_l1(t)/C_l1(0) = |D(t)| and the trace distance of the |±⟩ pair = |D(t)|. Observed max |deviation| for both: 6.66 × 10⁻¹⁶.

4.4 FC-2, masking at d = 3. Equal-weight qutrit, charges (1, 0, −1), n = 8, seeds 4400–4419, full grid. Theorem direction: a rise of C_l1 without a rise of any |D_jk| — 0 violations. Contingent direction: pair-backflow episodes (a rise of some |D_jk| above 0.02 over its running minimum) 16.5 ± 6.9 per seed; fraction of episodes during which C_l1 rises at some step: 0.923 ± 0.062 (expectation 1 — flagged, refuted); fraction of the total pair backflow that occurs while C_l1 is falling: 0.049 ± 0.018.

4.4b The environment as a source of frustration. Equal-weight qutrit (alignable, gap 0), n = 4, 201 times in [0, 10], seed 44; Stage 2's `multiport_visibility` gap evaluated every tenth time. |+⟩ modes: max_t |τ(t)| = π (3.1416) from sign changes of D_02; max_t gap = 0.1294; fraction of times with |τ| > 10⁻⁶ = 0.458, none strictly between 0 and π (τ ∈ {0, π}, as T13 says). Tilted modes: max_t |τ(t)| = π; max_t gap = 0.0303; fraction of times with |τ| > 10⁻⁶ = 0.995, strictly between 0 and π = 0.995.

4.5 Theorem T8. d = 2: 10 tilted 6-mode baths × 500 steps in [0, 10], seed 45 — steps at which the sign of the CP-divisibility defect (smallest eigenvalue of M) disagrees with the sign of the modulus change: 0 (theorem). d = 3, |+⟩ modes (D_02 real, D_01 = D_12*), equal-weight qutrit, n = 8, seeds 4500–4519: steps not CP-divisible while no pair modulus rises = 390.7 ± 37.6 of 2000 per seed (20/20 seeds have some); onset of non-divisibility t = 0.0635 ± 0.0057 against the first pair backflow at t = 0.5885 ± 0.0557 — earlier in 20/20 seeds; most negative defect for t < 0.3 (before any zero crossing) = −4.095 × 10⁻³ ± 1.3 × 10⁻³ at δt = 0.01, far above rounding. An independent static-bath check with three modes (g = 1.0, 0.8, 1.2, D_01 = D_12 = Π cos g_i t, D_02 = Π cos 2g_i t) gives the smallest eigenvalue of M(t, t + 0.01) as +4.6 × 10⁻⁸, −4.0 × 10⁻⁶, −4.1 × 10⁻⁵, −3.8 × 10⁻⁴, −1.5 × 10⁻³ at t = 0.02, 0.05, 0.1, 0.2, 0.3: the t⁴ onset predicted in §2.

4.6 FC-4, the bath-size trend. d = 2, equal-weight pair, T = 20, 20 seeds per n (seed 4600 + 100n + s):

| n | R (mean ± sd) | min | max | T_2 (finite seeds) |
|---|---|---|---|---|
| 1 | 0.7768 ± 0.2544 | 0.3092 | 1.0000 | 1.460 (5 seeds never reach 1/e) |
| 2 | 0.9487 ± 0.0509 | 0.7687 | 0.9996 | 0.871 |
| 4 | 0.5903 ± 0.1611 | 0.1756 | 0.8031 | 0.710 |
| 8 | 0.1591 ± 0.1413 | 0.0161 | 0.6187 | 0.478 |
| 16 | 0.0081 ± 0.0111 | 0.0002 | 0.0467 | 0.348 |
| 32 | 0.0000 ± 0.0002 | 0.0000 | 0.0009 | 0.237 |

R is not monotone from n = 1 (a single mode with ω > g never reaches zero, so its "revival" above the running minimum is smaller than a two-mode product that does); from n = 2 it falls monotonically, by factors 0.62, 0.27, 0.05 and about 0.004 per doubling — faster than geometrically — and is below 0.02 at n = 16.

4.7 Echo and horizons. (T10) 20 random (d ∈ {2, 3, 4}, state, static bath of 1–6 tilted modes, T ∈ [1, 30]), seed 47, one reversal at T/2: max |D(T) − 1| = 1.11 × 10⁻¹⁵. Dynamic bath, n = 8, equal-weight pair, seeds 4700–4719: T_recohere (single reversal, 400-point scan of T in [0.05, 20]) = 1.402 ± 0.094 against T_2 = 0.489 ± 0.044; ratio 2.88 ± 0.15. FC-3, retained C_l1(20)/C_l1(0) under n_p Carr–Purcell reversals (same seeds):

| n_p | 0 | 1 | 2 | 4 | 6 | 8 | 12 | 16 | 24 | 32 | 48 | 64 | 128 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| spacing | ∞ | 20 | 10 | 5 | 3.33 | 2.5 | 1.67 | 1.25 | 0.83 | 0.63 | 0.42 | 0.31 | 0.16 |
| retained | 0.0170 ± 0.0548 | 0.0261 ± 0.0357 | 0.0416 ± 0.0703 | 0.0060 ± 0.0075 | 0.0095 ± 0.0240 | 0.0131 ± 0.0213 | 0.1748 ± 0.1582 | 0.6146 ± 0.1279 | 0.9159 ± 0.0249 | 0.9700 ± 0.0092 | 0.9940 ± 0.0020 | 0.9981 ± 0.0006 | 0.9999 ± 0.0000 |

Pre-registered condition: spacing below π/(2Ω_max) with 2Ω_i = √(g_i² + ω_i²) ≤ √(2 × 1.5²) = 2.12, i.e. spacing < 1.48, n_p ≥ 14 (16 is the next tested value). Seeds monotone non-decreasing for n_p ≥ 16: 20/20 (smallest step change +8.73 × 10⁻⁴); over the whole range n_p = 0..128: 0/20 (flagged: the unconditional form is refuted — n_p = 2 → 4 loses coherence in the mean). Single-frequency bath (all ω_i = 1, g_i ~ U(0.5, 1.5), n = 8, seeds 4750–4769), dressed frequencies √(g² + 1) ∈ [1.1, 1.8], dip expected for spacing in [1.7, 2.8], n_p 7–12: retained = 0.013 ± 0.040 (n_p = 0), 0.094 ± 0.139 (1), 0.042 ± 0.132 (2), 0.034 ± 0.044 (3), 0.002 ± 0.004 (4), 0.008 ± 0.014 (5), 0.026 ± 0.067 (6), 0.013 ± 0.044 (7), 0.000 ± 0.000 (8), 0.103 ± 0.094 (10), 0.179 ± 0.095 (12), 0.808 ± 0.092 (16), 0.993 ± 0.001 (24), 0.995 ± 0.000 (32), 0.999 ± 0.000 (64). The minimum at n_p = 8 (spacing 2.5) is inside the predicted window and is zero to three decimals in every seed: pulses timed to the environment's own period erase the coherence entirely.

Stage 1, 2 and 3 tables: unchanged, line for line (diff against the pre-Stage-4 run).

## 4. Checks

Correctness conditions — theorems and unit tests; cannot fail unless the code is wrong:

- CC-1. The factorised operation equals the literal joint evolution, with pulses, for d = 2..4 (4.0); trace and populations preserved; [D_jk(t)] PSD (T8); independent baths multiply (T11). Failure would mean `evolve_open` is not implementing (1)–(2).
- CC-2. Contact with Stage 1 at d = 2 (4.1): the reduced state is Stage 1's record channel at distinguishability 1 − |D(t)| up to a phase. Failure would mean Stage 4 is not a strict extension of Stage 1.
- CC-3. Closed forms T12 and T13 (4.1), and the theorem T7 identities (4.3).
- CC-4. T9: the matched control has zero revival and zero backflow (4.2). T10: a static bath is refocused exactly by one reversal (4.7).
- CC-5. T8 at d = 2: the CP-divisibility defect and the modulus change agree in sign at every step (4.5). The theorem direction of 4.4 (a rise of C_l1 needs a rise of some |D_jk|): 0 violations.
- CC-6. The revival-amplitude and backflow functionals return 0 on monotone series and the horizon functional interpolates (exercised by the control in 4.2 and by T10 in 4.7).

Falsifiable claims — contingent; could fail with correct code:

- FC-1 (pre-registered revival claim for this bath). A structured bath of n = 8 modes with g_i, ω_i ~ U(0.5, 1.5) produces, for the equal-weight pair within T = 20, at least one revival of C_l1 above 0.02 — which by T7 is BLP backflow. (That the memoryless control matched at T_2 produces none is T9, not part of the claim.) Outcome (4.2): 20/20 seeds, R = 0.20 ± 0.16. Named failure mode: bath size and spectral density — R falls faster than geometrically with n (4.6) and is below 0.02 at n = 16, so a world whose environments have many modes per register, or a horizon shorter than the modes' recurrence, shows no revival at all even though the dynamics is not CP-divisible. If it fails: the Markovian half (T9) and the identity of revival, backflow and non-divisibility at d = 2 (T7, T8) are untouched; what is lost is the existence claim at that bath size, and the stage would report R = 0 and the divisibility defect as the only witness of memory. At d = 2 revival and backflow are not independent evidence (T7); independent evidence needs d ≥ 3 or a dynamics that is not pure dephasing.
- FC-2 (masking at d ≥ 3, pre-registered, refuted in its strict form). Claim: every pair-backflow episode is visible as a rise of the register-level C_l1(t). Outcome (4.4): 92.3 ± 6.2 % of episodes are visible; 4.9 ± 1.8 % of the total pair backflow occurs while C_l1 is falling. Named failure mode: C_l1 is a sum over pairs, and one pair's revival is hidden when another pair's decay is faster at that moment. What happens to the stage: the register-level measure is retained as the headline quantity with the stated caveat; the per-pair moduli |D_jk(t)| (equivalently the per-pair C_l1 of Stage 2's P-2 relation object) are the quantities that see every backflow, and §8 proposes reporting them.
- FC-3 (the rate law, DN-staging-and-phase-travel-v0.4.1 §7.2, in Level 3 form). Claim as pre-registered: retained coherence at fixed T is non-decreasing in the number of reversal pulses once the pulse spacing is below π/(2Ω_max). Outcome (4.7): holds in 20/20 seeds for n_p ≥ 16, the first tested value above the threshold n_p ≥ 14; the unconditional reading ("more pulses, more retained") fails in 20/20 seeds, and a single-frequency bath shows the mechanism — pulses at spacing near π/(2Ω) drive the coherence to zero. Named failure mode: resonance between the pulse rate and the environment's dressed frequency. If the conditional form fails (a bath with couplings so non-uniform that the dressed frequencies exceed the stated bound): the condition moves, the law's shape does not; if the mechanism is absent in the world (no coherent environment dynamics), reversal at any rate refocuses exactly (T10) and the law is vacuous.
- FC-4 (trend). R decreases with n for n ≥ 2 (4.6). Established within n ≤ 32 by the spreads; the claim beyond that, and for other coupling and frequency distributions, is the contingent part. Named failure mode: a bath with commensurate frequencies (a single mode, or modes in rational ratio) revives fully at its recurrence time whatever n is. If it fails: nothing in the theorems changes; the qualitative sentence "more environment, less return" is retracted for that bath class.
- FC-5 (horizon ratio). For this bath family T_recohere/T_2 = 2.88 ± 0.15: a single reversal at mid-course roughly triples the time over which the equal-weight pair can be brought back above 1/e. Named failure mode: the ratio depends on ω_i/g_i; for ω_i → 0 it diverges (T10), for ω_i ≫ g_i the echo does nothing. If it fails: the number is replaced, the definitions in §2 stand.

Not falsifiable claims, stated so they are not mistaken for ones: "the Markovian control shows no revival" is T9; "at d = 2 the coherence revival, the BLP backflow and the failure of CP-divisibility coincide" is T7 with T8; "a static bath is refocused exactly by a reversal" is T10. None can be falsified by any state or bath in this model.

## 5. Level labels

- ρ(t), D_jk(t), the environment modes, W_k(t), the joint state: Level 3 (physical states and operators of a d-level system and n spin-½ modes).
- g_i, ω_i, |ψ_i⟩, n, the charges c_k: Level 3 as parameters of a real Hamiltonian; which world-thing supplies them is Level 1 until the mapping of §6 is made.
- C_l1(t), C_re(t): Level 3. R (revival amplitude) and N (backflow): Level 3 functionals of Level 3 series; N is the BLP non-Markovianity measure at d = 2 (T7) and a per-pair lower bound on it at d ≥ 3.
- The CP-divisibility defect (smallest eigenvalue of M): Level 3; its sign is the RHP criterion for this dephasing family.
- T_2 (1/e time of C_l1) and T_recohere (1/e time under a single mid-course reversal): Level 3 instances of the framework's Level 2 T_2,E and T_recohere,E, on this substrate only; the framework's definitions in terms of "interaction depth" are not instantiated.
- γ (control rate) and the control itself: Level 3 (a Lindblad semigroup), as a comparison model, not as anything the world does.
- The reversal pulse: Level 3 (a register unitary while coupled). "Echo", "transit", "refocusing", "revisit": Level 1 labels for it.
- τ(t) and the gap under the environment (4.4b): Level 3 (Stage 2's quantities). "The environment twists the relations": Level 1.
- The U(0.5, 1.5) coupling and frequency ensembles and the single-frequency bath: Level 1 stand-ins for unknown world distributions.
- "Memory", "structured", "revival", "masked", "resonance": Level 1 labels for the Level 3 facts they name.

## 6. Cost accounting

Computational scaling of the new operation. With a product bath, one time point costs O(n d) two-by-two propagations plus O(n d²) for the pairwise overlaps and their product — for n = 32, d = 3 and 2001 time points, 0.05 s. Each pulse is a relabelling, O(n d), plus one propagation to the pulse time. Ensemble size N enters linearly; a pulse-count sweep with p values multiplies by p, and the T_recohere scan multiplies by the number of trial horizons (400 here, each a two-time run). The literal check `_joint_evolve` costs O((d 2^n)³) per time point and is used only at n = 3. The Stage 4 block adds about 25 s to the module, most of it in the 4.7 sweeps and the 4.4b gap evaluations (one Stage 2 optimisation per sampled time). Non-product baths (interacting modes, thermal states) would need the joint form and scale as 2^n; a continuum spectral density would replace the product by an integral and is not implemented.

Cost on a real substrate. A QKD-Aero polarization state is a two-level register; what Stage 4 needs beside it is a coherent environment with its own dynamics. A static birefringent element in the channel is the ω = 0 case — its record is refocused exactly by one polarization reversal (T10), so the QKD-Aero substrate can run the static half of the stage but not the dynamic half unless a controllable coherent auxiliary mode (a time-bin or path degree of freedom coupled through a tunable element) is added; the free-space channel's atmospheric model is a classical fluctuating field and produces inhomogeneous dephasing, not the entangled record of (2). On a gate-model device the test is one register qubit and n ancilla qubits with ZZ couplings g_i and transverse fields ω_i, Trotterised; the coherence series needs register tomography at each of n_t times (10³–10⁴ shots per point; two initial states for the BLP pair), so a 200-point series is of order 10⁶ shots, and a pulse sweep multiplies that by the number of pulse counts; the echo is one X gate. The systematics that matter: Trotter error competes with the t⁴ onset of non-divisibility (4.5) and must be below 10⁻³ in D to see it; ancilla decoherence to the outside adds a Markovian factor (T11) that lowers R and must be characterised separately. These are order-of-magnitude figures, not a design.

Parameters this stage needs from the world that no note has yet set: (i) what an environment mode is — which world-thing holds a which-history record coherently rather than as a classical log; (ii) n, how many such modes a register is coupled to, since R falls faster than geometrically with n (4.6); (iii) each mode's own frequency ω_i — the memory time of the record — and its coupling g_i, since the ratio decides whether an echo does anything (T10 versus FC-5); (iv) the mode's initial state, since |+⟩ modes give real D and only sign-type frustration while tilted modes give continuous triangle phases (4.4b); (v) whether the world can reverse a register while it is coupled — whether the staging note's "transit" is a register-side permutation or something else — and at what rate, since the rate law has a threshold (FC-3); (vi) the horizon T over which a return counts as a return.

## 7. Open-problems ledger (DN-staging-and-phase-travel-v0.4.1 §13)

1. C1 small-sample estimation — not touched: no estimator, no participant data.
2. Stale-reference detection — not touched: the reversal is a pulse, not a reference, and nothing here detects drift of a reference.
3. Region → register mapping — sharpened: beyond Stages 2–3's (a)–(c) and the observation triple, the mapping must now say what an environment mode is, how many a region has, what sets each mode's own frequency, and whether transit is a register-side reversal (§6, i–v); until it does, the revival, the echo and the resonance have physics instances and no world instance.
4. QEC threshold transfer — not touched.
5. Moiré buildability (closed in v0.4.1) — not touched.
6. Intervention thresholds — not touched: T_2 and T_recohere are shapes with numbers only for a stand-in bath; no threshold is supplied.
7. Identity across reconstruction — not touched.
8. Export ceiling testability — not touched.
9. Module decoherence coefficient — sharpened: an observational module kept as a quantum system is a bath, and independent modules multiply their decoherence functions exactly (T11), so the "coefficient" is a function D^(m)(t) per module, not a rate; its Markovian rate 1/T_2 exists only after coarse-graining and misdescribes both the short-time Gaussian and the return (4.2). The §7.2 rate law now has a Level 3 form with a condition and a failure mode (FC-3): transit at a rate above every module's dressed frequency retains coherence, transit near it destroys it. The rate itself stays unset: g_i and ω_i per module are world parameters.
10. Participant memory and novelty — not touched.
11. Provenance authenticity (build the detector where authenticity is free) — not touched.

## 8. What this stage does not claim

It does not claim that Echorym's environment, World, modules or observers are spin baths, or that any world event is a pulse. It claims recoherence and non-Markovianity only in the sense the model licenses: the environment is kept as a quantum system, the return of |D| is the environment's branch states re-overlapping under their own Hamiltonian, and the BLP and RHP quantities are computed on that model — no revival is claimed for any classical record, for Stage 3's instrument, or for any world process. It does not claim that the framework's §10 question is answered for the world: the physics-level answer is that recoherence follows from coherent environment dynamics or from a register-side reversal while coupled, and that deleting a classical copy of a record does nothing (4.2, 4.7; Stage 3 T3); whether any world record is coherent is §6 (i). It does not claim amplitude damping, thermal baths, interacting baths or a continuum spectral density; the bath is finite and pure, so every revival here is a finite-size recurrence, and the FC-4 trend is what stands between this model and the limit in which recurrences vanish. It does not claim that the BLP measure at d ≥ 3 is computed — only a per-pair lower bound is. It does not claim a geometric phase: the triangle phases of 4.4b are Stage 2's τ, and their relation to the environment branch states is left to Stage 5. It does not set n, g_i, ω_i, the horizon, or the transit rate. It does not derive or constrain the coherence-gate thresholds.

Proposed amendments, recorded here and not applied: (P-8) Coherence framework §5.4–5.5 — T_2,E and T_recohere,E have Level 3 instances on this substrate: the 1/e time of C_l1 and the first horizon at which a single mid-course reversal fails to hold C_l1 above 1/e; the ratio is a property of the environment's memory (FC-5). (P-9) Coherence framework §7 (dynamical-decoupling analogue) — record the condition and the failure mode: periodic re-alignment retains coherence only above the environment's own frequency, and near it makes the loss complete (FC-3). (P-10) Coherence framework §10 — the erased-record question has a physics-level answer: histories recohere when the record's carrier evolves coherently back toward indistinguishability or when the register is reversed while still coupled; erasing a classical copy is neither. (P-13) Stage 2's W-4 — a structured environment with modes not in a σ_x eigenstate is a second world-candidate process, besides convex mixing, that gives the frustration gap an instance (4.4b).

## 9. Narrative imports

- [interpretation] Physics → world. The environment's branch states re-overlapping under their own dynamics (4.2) ↔ the framework's §12 "World as refocusing medium": a record that fades not because anyone erased it but because its carrier moved on. The physics does not license identifying any world record with an environment mode.
- [interpretation] Physics → world. A reversal of the register while still coupled (T10, 4.7) ↔ the staging note's "transit is the pulse", and T_recohere/T_2 ≈ 3 ↔ how much longer a relation can be held recoverable by one mid-course return. The physics does not license this; the reversal is a permutation of basis states.
- [interpretation] Physics → world. The resonance (FC-3) ↔ revisits timed to the drift's own rhythm making the loss complete rather than preventing it, and the rate law's condition ↔ "revisit faster than the environment turns over". The physics does not license reading any revisit schedule this way.
- [interpretation] Physics → world. A masked pair revival (FC-2) ↔ one relation quietly recovering while the register as a whole appears to keep losing coherence. The physics does not license it; C_l1 is a sum over off-diagonals of a matrix.
- [interpretation] Physics → world. The environment twisting an alignable register into a frustrated one (4.4b) ↔ a World that does not merely erase relations but rotates them against each other. The physics does not license it; τ(t) is the phase of a product of three Gram-matrix entries.

## 10. Firewall

C_l1(t), C_re(t), |D_jk(t)|, R, N, the divisibility defect, T_2 and T_recohere are not identified with the schemas' `coherence.current` or with the five coherence-gate thresholds (0.376, 0.618, 0.786, 0.886, 1.000); they remain different quantities, and no stage has derived one from the other.

## 11. Class IV boundary statement

Nothing in this stage is about neural, human, or narrative state. The register is a d-level quantum system, the environment is a set of spin-½ modes with a Hamiltonian, the pulses are permutations of basis states, and every quantity reported is a function of a d × d density matrix, of the Gram matrix of environment branch states, or of the time at which such a function crosses a level. Any Echorym meaning attached to a mode, a revival, a pulse, or a horizon is an interpretation layered on top and is labelled as such in §9. No neural–quantum coupling claim is made or implied.

---

## Appendix A — Review requests

Adversarial review (what could be wrong):

- A-1. T7's BLP argument bounds the increase of √(Δp² + |Δc|²|D|²) by |Δc| times the increase of |D| and uses |Δc| ≤ 1; check the bound for pairs whose coherences have different phases (|Δc| is the modulus of a complex difference) and that no pair with Δp ≠ 0 can exceed the |±⟩ pair over an interval on which |D| passes through zero.
- A-2. T8's first-order criterion (L PSD on the complement of the all-ones vector) is derived for a single step; check that the exact criterion (M PSD) is what `divisibility_defect` computes when D has complex entries (M is Hermitised as (M + M†)/2 — confirm this is the right object rather than an artefact), and check the d = 3 real-rate triangle criterion √a_jk > √a_jl + √a_kl against the exact eigenvalue, since 4.5 verifies only that the sign and the t⁴ onset agree.
- A-3. `divisibility_defect` reports nan wherever some |D_jk| < 10⁻¹², and the ratio matrix is ill-conditioned near zero crossings of a real D; decide whether the 390.7 ± 37.6 non-divisible steps per seed in 4.5 should be reported net of the steps adjacent to zero crossings, and whether P-divisibility (a weaker criterion) is the one the framework wants.
- A-4. The Markovian control is matched by one scalar γ to the C_l1 horizon; at d ≥ 3 this cannot match every pair. Check whether a per-pair matching that stays completely positive exists (it requires the rate matrix to be conditionally negative definite) and whether the comparison in 4.2 should be repeated at d = 3.
- A-5. The revival amplitude R counts a rise above the running minimum, which for a real D that crosses zero counts the rise after the crossing; decide whether a crossing counts as a "revival" of coherence in the sense the framework intends, or whether |D| passing through zero and back is better described as a phase flip. 4.6's n = 1 anomaly is a symptom of this definition.
- A-6. The masked-backflow episode detector in 4.4 uses a 0.02 threshold and calls an episode visible if C_l1 rises at any step inside it; check sensitivity to the threshold and to the grid, and whether "visible" should require a rise of C_l1 above its own running minimum rather than any positive step.
- A-7. The resonance in 4.7 is at Carr–Purcell timing with instantaneous pulses; a finite-width pulse or a different timing (equal spacing from t = 0) would move the dip. Confirm the predicted window uses the right dressed frequency (2Ω_i = √(g_i² + ω_i²) from T13) and that the T13 closed form is for charges ±½, not ±1.
- A-8. T13's realness holds only for branch pairs with opposite charges; at d = 3 with charges (1, 0, −1) D_01 and D_12 are complex conjugates of each other and D_02 is real (the c → −c symmetry of |+⟩ modes). An earlier draft of this note said D was real for all |+⟩ pairs; the adversarial pass caught it (max |Im D_01| = 0.209 at seed 4400). Check that nothing in 4.5's prose still relies on realness of D_01, and whether the triangle criterion has a clean complex generalisation.

World-side review (what the world must decide):

- W-1. What carries a which-history record coherently? Stage 3's records were classical and could not return; this stage's return exists only for a record whose carrier has its own coherent dynamics. If nothing in the world is such a carrier, Stage 4 describes no world process and the revival claim has no world instance.
- W-2. How many environment modes per register, and with what spread of frequencies? R falls faster than geometrically with n (4.6); a world with many observers per region has no return on any horizon, which is itself a design statement.
- W-3. Is transit a register-side reversal while coupled? If yes, the rate law (FC-3) and T_recohere (FC-5) apply and the world must set the transit rate against the environment's frequencies; if transit is something else, the echo results do not transfer.
- W-4. Which quantity should the world's CoherenceMonitor report at d ≥ 3 — the register-level C_l1(t), which can miss a pair's return (FC-2), the per-pair |D_jk(t)|, or the divisibility defect, which registers memory before any return (4.5)?
- W-5. Does a sign change of a real D — coherence passing through zero and returning with the opposite phase — count as a revival in the world's sense (A-5)?
- W-6. Whether an observational module's record (problem 9) is to be modelled as a coherent environment mode with a memory time (this stage) or as Stage 3's classical instrument; the coherence cost differs only in whether it can return.
- W-7. What horizon T defines "return": recurrences exist at every finite n, and the difference between a memoryless world and a world with memory is whether the horizon reaches them.

## Development record

| Model and version | Dates of use | Role |
|---|---|---|
| Claude, configured identifier `claude-fable-5-1` (the configured model of the weekly run that produced this note; the serving model can differ within a session) | 2026-09-27 (UTC; the note was filed at 06:46 UTC) | Drafted this note and the Stage 4 block of `echorym_qstate.py`. The session record was not found; whether the module was executed in that session: Needs author confirmation |
| Claude, configured identifier `claude-opus-5-5` | 2026-11-05 | Edited this note for the public copy under the review of 2026-11-05 (cross-references, citations and internal review items; no result changed); executed the full module (Stages 1–6) before and after the edit and found its printed output unchanged |

Author: Lana C. Waddell.
