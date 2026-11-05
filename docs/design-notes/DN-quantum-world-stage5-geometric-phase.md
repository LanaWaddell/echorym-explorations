Redaction status: cross-references and internal review notes edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05

# DN-quantum-world-stage5: geometric phase — the gauge-invariant phase of a closed path of polarization states

Status: design note, week of 2026-10-04. Fifth step on the staged path (state → coherence → superposition → interference → measurement → decoherence → later stages). This stage: the geometric phase of a closed path of polarization states, on the state set of the QKD-Aero substrate.
Depends on: DN-quantum-world-stage1-history-pair-state, DN-quantum-world-stage2-multiport-histories (triangle phases τ_jkl, alignability), DN-quantum-world-stage3-measurement-as-constraint, DN-quantum-world-stage4-decoherence-with-memory (decoherence functions D_jk, T11, T13, 4.4b), Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline; §13 `BranchRelation`, `EnvironmentRecord`), DN-staging-and-phase-travel-v0.4.1 (§13), quantum-qkd-aero docs/INTERFACES.md (decoy-state BB84 as the polarization substrate).
Artifact: `echorym_qstate.py`, Stage 5 block appended; runs standalone with numpy (`python3 echorym_qstate.py`, 3 min 12 s on one core in this run, of which the Stage 5 block is about 16 s; prints the verification table for Stages 1–5; the Stage 1–4 output is identical line for line to a run of the same file without the Stage 5 block — see A-9 for what that check does and does not cover).
Stop-condition check: this stage does not require a decision about which world-object the register represents. The register is a polarization qubit; a closed path of its states, the Poincaré sphere and the wave plates that move a state on it are defined at the physics level. Every substrate-side and world-side parameter the stage exposes is listed in §6 as unset rather than assumed.
Review: an adversarial pass on a first draft confirmed the printed numbers and found eight defects, all corrected here and in the module before filing: the solid-angle routine dropped the phase of a fan triangle with an antipodal edge (now cut from an auxiliary apex, with undefined cases returned as nan); the closed form for the interferometric phase was wrong by π for Ω/2 > π/2; the proofs of the two state-set corollaries did not cover loops with vanishing diagonals; the finite-shot extractor was claimed unbiased and is not; the vertex-noise bias was treated as contingent and is zero by theorem; the angle-wrapping helper quantised residuals; degenerate inputs returned a number instead of nan; and one sentence about alignability held only at full support. A-1 lists what the pass did not settle.
Results flagged up front: (i) gauge invariance, equality with half the enclosed solid angle and independence from the dynamical phase are theorems of this extractor (T14–T16); the contingent claim is whether a channel preserves the geometry of the loop (FC-3), which is stated here and not evaluated against any QKD-Aero channel. (ii) The four BB84 states lie on one great circle of the Poincaré sphere, so every loop built from them has geometric phase 0 or π; a continuous geometric phase needs a third basis or states prepared off the protocol's set (T15, 5.2). (iii) A single state sent through a channel gives a two-state path, whose geometric phase is zero (T14); "the geometric phase of the channel" needs at least three distinct states. (iv) Stage 2's triangle phases, which Stages 2 and 4 declined to call geometric phases, are geometric phases — of the purifying environment's branch states, not of the register's own path (T19). (v) One pre-registered claim is refuted: the finite-shot extractor is not unbiased. Its bias is b₂/S at every S, with b₂ = −0.14 for the generic loop tested and 0 for a loop on the measured axes (FC-1, T20); the first draft's run passed the claim only because it had too few trials to see the bias.
Class IV boundary: unchanged (§11).

## 1. Concept

Stages 1–4 dealt with the modulus of a relation: how much of ρ_jk survives recombination, observation and an environment. Stage 5 is about a phase that is not a relation between two histories at all but a property of a closed path — a state taken through a sequence of other states and brought back. The phase it returns with has a part that depends on how long the trip took and with what energy (the dynamical phase) and a part that depends only on the path traced in state space (the geometric phase). The second part is the subject of this stage, and it needs the density-matrix substrate of Stage 1 because it must be a number that does not change when any state on the path is multiplied by an arbitrary phase.

The operation added is the smallest object with that property: the phase of the product of overlaps round the loop. For a polarization qubit it equals minus half the solid angle the loop encloses on the Poincaré sphere. Four things follow. The phase is fixed by the loop's states alone, so it is insensitive to traversal speed and to energy offsets exactly, and to over-rotation only at third order. The decoy-state BB84 state set can show only a sign; the six-state set only multiples of π/4. The triangle phases that made a three-history register "frustrated" in Stage 2, and that Stage 4's environment imprinted on an alignable register, are this same quantity evaluated on the environment's record states. And the extraction is exactly immune to a fixed rotation, isotropic depolarisation and uniform loss, and generically first-order sensitive to the other things a polarization channel does — how sensitive depends on the loop, and a loop on the protocol's own states is blind to a channel aligned with the protocol's bases.

## 2. Formalization

Operation. For a sequence of states visited in order, ψ_0 → ψ_1 → … → ψ_{N−1} → ψ_0,

    γ = −arg B,     B = ⟨ψ_0|ψ_1⟩⟨ψ_1|ψ_2⟩ … ⟨ψ_{N−1}|ψ_0⟩ = Tr(P_0 P_1 … P_{N−1}),    P_k = |ψ_k⟩⟨ψ_k|,          (1)

with γ ∈ (−π, π]. B is the Bargmann invariant of the sequence. An open path is closed by the last factor ⟨ψ_{N−1}|ψ_0⟩, which is the geodesic closure (Pancharatnam's rule; Samuel and Bhandari 1988). When two consecutive states are orthogonal, B = 0, the connecting geodesic is not unique and γ is undefined. `geometric_phase(path, purify, tol)` accepts kets or density matrices; with `purify=True` (default) a density matrix is replaced by the projector on its dominant eigenvector, with `purify=False` it is used as given; it returns γ, |B| and B, with γ = nan when |B| < tol or when a density matrix to be purified has no dominant eigenvector (its two largest eigenvalues within tol).

Polarization register. |H⟩ = |A⟩ and |V⟩ = |B⟩ of Stage 1; |D⟩, |A_pol⟩ = (|H⟩ ± |V⟩)/√2; |R⟩, |L⟩ = (|H⟩ ± i|V⟩)/√2. The Stokes vector is s = (⟨σ_x⟩, ⟨σ_y⟩, ⟨σ_z⟩), so H/V lie on the z axis, D/A on x and R/L on y. In the optical ordering (S₁, S₂, S₃) = (s_z, s_x, s_y), a cyclic relabelling that preserves orientation. A wave plate of retardance δ with fast axis at physical angle α is W(δ, α) = exp(−i(δ/2)(cos 2α σ_z + sin 2α σ_x)), a rotation of s by δ about (sin 2α, 0, cos 2α).

Theorem T14 (invariances, any dimension). (a) Gauge: |ψ_k⟩ → e^{iα_k}|ψ_k⟩ leaves B unchanged, since each state appears once as a ket and once as a bra. (b) A common unitary leaves every overlap unchanged. (c) B is cyclic. (d) Reversing the path conjugates B: γ → −γ. (e) A retraced path a → b → a with ⟨a|b⟩ ≠ 0 has B = |⟨a|b⟩|² > 0 and γ = 0; in particular every two-state path with non-orthogonal states has γ = 0 (for orthogonal states it is undefined). (f) Fan additivity: for any apex state p not orthogonal to any ψ_k,

    ∏_{k=0}^{N−1} B(p, ψ_k, ψ_{k+1}) = B(ψ_0, …, ψ_{N−1}) · ∏_k |⟨p|ψ_k⟩|²      (indices mod N),                    (2)

so a polygon's γ is the sum of its fan triangles' γ's mod 2π; with p = ψ_0 the same holds when the diagonals ⟨ψ_0|ψ_k⟩ do not vanish. (g) B depends on the rays only, so γ does not depend on the time parametrisation of the path or on any energy offset.

Theorem T15 (qubit: half the solid angle). For three pure qubit states with unit Stokes vectors a, b, c,

    Tr(P_a P_b P_c) = ¼ [ 1 + S + iT ],      S = a·b + b·c + c·a,      T = a·(b × c),                               (3)

and the oriented solid angle of the geodesic triangle a → b → c (positive when it runs anticlockwise seen from outside the sphere) satisfies Ω/2 = arg(1 + S + iT) (Van Oosterom and Strackee 1983, in the form that fixes Ω/2 on (−π, π) rather than its tangent). Hence γ = −Ω/2, and by (2) with an auxiliary apex the same holds for every geodesic polygon with no antipodal consecutive vertices, mod 2π. `half_solid_angle` evaluates the right-hand side from Stokes vectors, so comparing it with γ tests the identity (3); the evidence that the quantity is a solid angle is independent of (3): Girard's spherical excess (5.1), the octant counts (5.2) and the spherical-cap formula (5.3, 5.4). Corollaries, for loops of any length with B ≠ 0: the four BB84 kets {H, V, D, A} are real, so B is real and γ ∈ {0, π}; every non-zero overlap among the six kets {H, V, D, A, R, L} has phase 0, ±π/4, ±π/2 or π, so arg B and γ are multiples of π/4.

Theorem T16 (independence from the dynamical phase; laws for imperfect loops). For a cyclic evolution |ψ(T)⟩ = e^{iφ}|ψ(0)⟩ under any H(t), φ − φ_dyn = γ of the continuous path, with φ_dyn = −∫⟨H⟩dt (Aharonov and Anandan 1987). For H = E₀ + (ω/2) n·σ and a state at polar angle θ from n, the path is the circle of latitude about n traversed anticlockwise, φ_dyn = −(E₀ + (ω/2) cos θ)T and γ = −π(1 − cos θ). A latitude arc of length c departs from its geodesic chord by an area κ_g c³/12 with geodesic curvature κ_g = cot θ, which gives two asymptotic laws: the inscribed geodesic N-gon misses (2π)³ sin²θ cos θ/(12N²) of solid angle, so the sampled-path error is

    γ_N − γ = (2π)³ sin²θ cos θ / (24 N²) + O(N⁻⁴);                                                             (4)

and an over-rotation by a fraction ε of a turn, closed by the geodesic, changes γ by

    δγ = −(2πε)³ sin²θ cos θ / 24 + O(ε⁵),      while      δφ_dyn = −π cos θ · ε   (E₀ = 0),                     (5)

third order against first. A tilt of the axis by δθ changes both at first order: δγ = −π sin θ δθ, δφ_dyn = +π sin θ δθ. The geometric phase is insensitive to errors along the path and sensitive to errors of the path.

Theorem T17 (wave plates). For U = exp(−i(δ/2) n·σ) acting on a state with s ⊥ n, ⟨n·σ⟩ = 0 throughout, so the dynamical phase vanishes and the state moves along a great circle by parallel transport. |H⟩ through a quarter-wave plate Q at 45°, a half-wave plate at angle β and Q again returns to |H⟩ along three geodesic arcs, H → L → R → H. Since Q|H⟩ = |L⟩ and ⟨H|Q = ⟨R|, ⟨H|U|H⟩ = ⟨R|W(π, β)|L⟩ = −i e^{−2iβ}: the phase is −(π/2 + 2β) mod 2π, it is purely geometric (−Ω/2 of a lune of dihedral angle π/2 + 2β), and it changes by −2 δβ when the half-wave plate turns by δβ.

Theorem T18 (depolarised states: three readings). Let every vertex of a triangle have Stokes vector r·s with 0 < r ≤ 1. (E1) Purified: the dominant eigenvector has Stokes vector s, so γ_E1 = −Ω/2 for every r > 0; the same holds after a fixed unitary and a scalar loss factor. (E2) Raw trace, from (3) with a → ra etc.: γ_E2 = −atan2(r³T, 1 + r²S). (E3) Interferometric: the state ρ_r at the first vertex carried round the loop by the parallel-transporting unitary U has Tr(Uρ_r) = ½(1 + r)e^{−iΩ/2} + ½(1 − r)e^{+iΩ/2}, so γ_E3 = −atan2(r sin(Ω/2), cos(Ω/2)) with visibility ν = √(cos²(Ω/2) + r² sin²(Ω/2)) (Sjöqvist et al. 2000). The three coincide at r = 1 and differ generically for r < 1 (exceptions: E1 = E3 when Ω = π; all three agree when T = 0). E1 is undefined at r = 0.

Theorem T19 (triangle phases are geometric phases). Let ρ be any d × d register state and Σ_k |k⟩|a_k⟩ any purification of it (|a_k⟩ unnormalised, ⟨a_k|a_k⟩ = ρ_kk). Then ρ_jk = ⟨a_k|a_j⟩ and Stage 2's triangle phase, wherever the product is non-zero, is

    τ_jkl = arg(ρ_jk ρ_kl ρ_lj) = −arg(⟨a_j|a_k⟩⟨a_k|a_l⟩⟨a_l|a_j⟩) = γ(a_j → a_k → a_l),                          (6)

the geometric phase of the loop of environment branch states, independent of the purification because it depends only on their Gram matrix. Its invariance under diagonal unitaries of the register (Stage 2) is T14(a) for the branch states. For Stage 4, D_jk(t) = ⟨E_k(t)|E_j(t)⟩ with |E_k⟩ = W_k|ψ_E⟩, so the phase the environment adds to a three-history register is arg(D_01 D_12 D_20) = γ(E_0 → E_1 → E_2); for a product bath it is the sum over modes (T11), and each mode is a qubit, so by T15

    τ_env(t) = −½ Σ_i Ω_i(t)   (mod 2π),                                                                        (7)

Ω_i the solid angle of mode i's branch-state triangle on its own Bloch sphere. For |+⟩ modes with charges (1, 0, −1) each triangle lies on a great circle (the c → −c symmetry), Ω_i ∈ {0, ±2π}, which is T13's τ ∈ {0, π}. In these terms Stage 2's alignability reads: a register is alignable exactly when every loop of its branch states with non-vanishing Bargmann invariant — a closed walk of any length in the support graph — has zero geometric phase; triangles suffice only at full support (Stage 2's 4-cycle state, 2.5b, has every triangle invariant zero and a four-state loop with γ = π).

Theorem T20 (harmonicity; bias laws). Write a vertex as |b⟩ ∝ (1, ζ). In B = ⟨a|b⟩⟨b|c⟩⟨c|a⟩ the factor ⟨a|b⟩ is holomorphic in ζ, ⟨b|c⟩ antiholomorphic and the normalisation positive, so γ = −arg B is a harmonic function of ζ and, the stereographic map being conformal, of the vertex's position on the sphere, away from the points where B vanishes. Two consequences. (a) Noise that displaces a vertex isotropically about its true position produces no bias in γ (the mean-value property), so long as the displaced vertex does not reach a zero of B. (b) For Stokes tomography with independent components of variance (1 − s_i²)/S, the bias of γ̂ is

    E[γ̂] − γ = b₂/S + O(S⁻²),      b₂ = ½ Σ_{v,i} (∂²γ/∂s_{v,i}²)(1 − s_{v,i}²),                                    (8)

with the normalisation of ŝ included in γ(s). The bias comes from the anisotropy of the binomial covariance in the tangent plane and vanishes when it is isotropic there — in particular for a loop whose vertices are eigenstates of the measured axes, such as the octant H → D → R.

Estimators for §3. The finite-shot extractor measures each vertex's three Stokes components with S two-outcome shots per axis (ŝ_i = 2k/S − 1, k binomial with p = (1 + s_i)/2), normalises ŝ (E1) and evaluates γ̂ = −Ω̂/2. Linear error propagation gives sd(γ̂) = c/√S with c² = Σ_{v,i} (∂γ/∂s_{v,i})² (1 − s_{v,i}²); the bias is (8). Vertex-to-vertex channel noise rotates each vertex's Stokes vector by its own rotation vector ε_v ~ N(0, σ²·1); linearly sd(γ) = kσ with k² = Σ_v |s_v × ∇_v γ|², and the bias is zero by T20(a).

## 3. Verification

All numbers below are printed by `python3 echorym_qstate.py` (Stage 5 block). Angles are in radians. Every quantity is listed with its analytic expectation where one exists, its seed(s) and N, and its spread over seeds where an ensemble is involved. Every closed-form check agrees to rounding (≤ 2.1 × 10⁻¹³) or to the stated asymptotic order, and every ensemble statistic lies within 2 standard errors of its analytic value. Four entries depart by more than 2σ from a pre-registered expectation and are flagged: in 5.8 the generic loop's bias is 18.2, 8.7, 3.0 and 2.1 standard errors from zero at S = 100, 400, 1600 and 25 600. They are a refutation of the claim that the extractor is unbiased, not a numerical discrepancy: each is within 1.2 standard errors of the analytic bias b₂/S of (8).

5.0 Theorem T14. 200 random closed paths of Haar kets, d = 2..5, N = 3..8 states, seed 5. Expectation 0 for each. Observed maximum |change| of γ under per-state rephasing 7.49 × 10⁻¹⁵; under a common random unitary 1.62 × 10⁻¹⁴; under a cyclic shift 4.77 × 10⁻¹⁵; max |γ(reversed) + γ| = 3.72 × 10⁻¹⁵; ket input against projector input 1.15 × 10⁻¹⁴; retraced path a → b → a, max |γ| = 2.62 × 10⁻¹⁵; polygon against the sum of its fan triangles from its first vertex 2.55 × 10⁻¹⁵, from an auxiliary Haar-random apex 2.03 × 10⁻¹⁴.

5.1 Theorem T15. (a) Identity (3): random geodesic polygons of Haar qubit kets, N = 3..8 vertices, seeds 5100–5119, 100 polygons per seed; expectation γ + Ω/2 = 0 mod 2π with Ω/2 from `half_solid_angle`. Observed max |γ + Ω/2| per seed: mean 3.80 × 10⁻¹⁵, sd 2.29 × 10⁻¹⁵, max 1.03 × 10⁻¹⁴. (b) Independent geometry: |γ| against half the spherical excess (sum of the triangle's interior angles, computed from tangent directions, minus π), seeds 5150–5169, 100 random triangles per seed. Observed max ||γ| − E/2| per seed: mean 1.29 × 10⁻¹⁴, sd 1.21 × 10⁻¹⁴, max 5.11 × 10⁻¹⁴; triangles whose sign of γ is not minus the sign of the triple product: 0 of 2000.

5.2 Polarization loops. Analytic Ω by counting enclosed octants (π/2 each):

| loop | γ observed | γ expected | modulus |B| |
|---|---|---|---|
| H → D → R → H | −0.785398 | −π/4 | 0.3536 |
| H → R → D → H | +0.785398 | +π/4 | 0.3536 |
| H → D → R → A → H | −1.570796 | −π/2 | 0.2500 |
| H → D → R → A → L → H | −2.356194 | −3π/4 | 0.1768 |
| H → D → V → A → H | +3.141593 | π | 0.2500 |
| D → R → A → L → D | +3.141593 | π | 0.2500 |

Max |γ − expected| over the six loops: 0.00 (exact in double precision). H → D → V → H has modulus 0: V and H are antipodal and γ is undefined. Enumeration of every loop of length 3, 4 or 5 without immediate repeats: the four-state set {H, V, D, A} has 32 loops with nonzero modulus (316 undefined) and γ ∈ {0, π} only; the six-state set has 1296 loops with nonzero modulus (2574 undefined) and γ takes all eight multiples of π/4 and nothing else (max distance from a multiple of π/4: 4.93 × 10⁻³²).

5.3 Sampled smooth loop: the circle of latitude at θ = π/3 about z, N equally spaced states. Continuum γ = −π(1 − cos θ) = −1.570796; predicted error (4) → 3.8758/N².

| N | 8 | 16 | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|---|---|
| error | +6.296 × 10⁻² | +1.529 × 10⁻² | +3.794 × 10⁻³ | +9.468 × 10⁻⁴ | +2.366 × 10⁻⁴ | +5.914 × 10⁻⁵ | +1.479 × 10⁻⁵ |
| error · N² | 4.0295 | 3.9134 | 3.8851 | 3.8781 | 3.8764 | 3.8759 | 3.8758 |

5.4 Theorem T16. Cyclic evolution under H = E₀ + (ω/2) n·σ for one period, seeds 5400–5419: θ ~ U(0.2, π − 0.2), n uniform on the sphere, ω ~ U(0.5, 2), E₀ ~ U(−3, 3). Expectation: (total phase) − (dynamical phase) = −π(1 − cos θ) mod 2π exactly; the operation on the path sampled at N = 2000 agrees to (4), whose leading-order maximum over θ is (2π)³·(2/(3√3))/(24N²) = 9.95 × 10⁻⁷. Observed: max |(total − dynamical) − (−π(1 − cos θ))| = 3.55 × 10⁻¹⁵; max |γ(sampled path) − same| = 9.95 × 10⁻⁷ (one seed has θ = 0.953, next to the maximising θ = 0.955, so the observed maximum sits at the bound); the dynamical phases ranged over [−21.84, +18.78] rad. One loop (θ = 1.1) traversed under 20 different (ω, E₀), seed 54, 400 samples: spread of γ = 1.33 × 10⁻¹⁵; spread of the dynamical phase = 36.51 rad.

5.4b Laws (5), θ = π/3, E₀ = 0, N = 20 000. Over-rotation: δγ = −3.876 × 10⁻⁶, −3.104 × 10⁻⁵, −4.875 × 10⁻⁴, −3.973 × 10⁻³ at ε = 0.01, 0.02, 0.05, 0.10 against predictions −3.876 × 10⁻⁶, −3.101 × 10⁻⁵, −4.845 × 10⁻⁴, −3.876 × 10⁻³ (ratios 1.0002, 1.0010, 1.0062, 1.0251, the departure growing as ε² as the next order requires); δφ_dyn = −1.5708 × 10⁻², −3.1416 × 10⁻², −7.8540 × 10⁻², −1.5708 × 10⁻¹, equal to −π cos θ · ε to the printed digits. Tilt δθ = 10⁻⁴: δγ/δθ = −2.72078 (expectation −π sin θ = −2.72070, finite-difference error O(δθ)); δφ_dyn/δθ = +2.72078 (expectation +2.72070).

5.5 Theorem T17. Quarter–half–quarter wave-plate loop from |H⟩, 300 samples per plate. For β = 0°, 15°, 30°, 45°, 60°, 75°: arg⟨H|U|H⟩ = −1.570796, −2.094395, −2.617994, −3.141593, +2.617994, +2.094395 (expectation −(π/2 + 2β) mod 2π, identical); the operation's γ on the sampled path and −Ω/2 of the sampled Stokes vectors give the same values mod 2π (β = 45° prints +3.141593 = −3.141593 mod 2π). Observed max |arg⟨H|U|H⟩ − γ(path)| and |γ(path) + Ω/2| = 3.11 × 10⁻¹⁵ (the path consists of geodesic arcs, so sampling adds no error to γ); max ||⟨H|U|H⟩| − 1| = 1.11 × 10⁻¹⁶ (the loop closes); max |s · axis| along the path = 3.99 × 10⁻¹⁶ (no dynamical phase); slope between rows = −2.000000 (expectation −2).

5.6 Theorem T18. Loops: the octant H → D → R (Ω/2 = 0.785398); a fixed generic triangle with vertices at (θ, φ) = (0.4, 0.3), (1.3, 1.1), (1.0, 2.6) (Ω/2 = 0.393181); a wide triangle at (1.5, 0), (1.5, 2.1), (1.5, 4.2) (Ω/2 = 2.775832 > π/2, the range in which the first draft's E3 form was wrong by π and was not tested).

| loop | r | E1 | E2 | E3 | visibility |
|---|---|---|---|---|---|
| octant | 1.0 | −0.785398 | −0.785398 | −0.785398 | 1.000000 |
| octant | 0.9 | −0.785398 | −0.629925 | −0.732815 | 0.951315 |
| octant | 0.5 | −0.785398 | −0.124355 | −0.463648 | 0.790569 |
| octant | 0.1 | −0.785398 | −0.001000 | −0.099669 | 0.710634 |
| generic | 1.0 | −0.393181 | −0.393181 | −0.393181 | 1.000000 |
| generic | 0.9 | −0.393181 | −0.322279 | −0.357280 | 0.985957 |
| generic | 0.5 | −0.393181 | −0.082494 | −0.204490 | 0.943350 |
| generic | 0.1 | −0.393181 | −0.000817 | −0.041454 | 0.924489 |
| wide | 1.0 | −2.775832 | −2.775832 | −2.775832 | 1.000000 |
| wide | 0.9 | −2.775832 | −2.546053 | −2.809652 | 0.987773 |
| wide | 0.5 | −2.775832 | −0.036228 | −2.952386 | 0.950821 |
| wide | 0.1 | −2.775832 | −0.000186 | −3.103312 | 0.934537 |

Closed forms identical to six decimals in every cell; max |numeric − closed form| over the table, including E3 rebuilt from the operation applied to the loop and to its antipodal image with weights (1 ± r)/2, = 2.22 × 10⁻¹⁵. At r = 0.9 the three readings of the octant loop already differ by up to 0.155 rad. For the wide loop E3 tends to −π, not to 0, as r → 0: with cos(Ω/2) < 0 the two eigenstate contributions leave a real negative amplitude.

5.7 Theorem T19. (a) Hilbert–Schmidt-random register states, d = 3, 4, 5, purified through ρ = AA† with the environment embedded by a random isometry into d + 2 dimensions; every triple j < k < l; seeds 5700–5719, 50 states per d per seed. Expectation: τ_jkl − γ(a_j → a_k → a_l) = 0. Observed max |difference| per seed: mean 4.27 × 10⁻¹⁴, sd 4.23 × 10⁻¹⁴, max 2.10 × 10⁻¹³. (b) Stage 4 baths, n = 4, g_i, ω_i ~ U(0.5, 1.5), seed 57, equal-weight qutrit, charges (1, 0, −1), 201 times in [0, 10]; branch states computed from the closed form of a 2 × 2 exponential, independently of `evolve_open`. |+⟩ modes: max |arg(D_01 D_12 D_20) − Σ_i γ_i| = 3.86 × 10⁻¹⁴; max |arg(D_01 D_12 D_20) + Σ_i Ω_i/2| = 2.66 × 10⁻¹⁴; register τ(t) minus the environment phase 4.44 × 10⁻¹⁶; max |s_0 · (s_1 × s_2)| over modes and times 5.58 × 10⁻¹⁶ (every branch triangle on a great circle); max_t |τ| = 3.1416. Tilted modes: 1.60 × 10⁻¹⁴; 1.64 × 10⁻¹⁴; 4.44 × 10⁻¹⁶; max |s_0 · (s_1 × s_2)| = 0.992 (triangles not on great circles); max_t |τ| = 3.1370. All 201 times had |D_01 D_12 D_20| > 10⁻⁹ in both cases.

5.8 FC-1, finite-shot extraction. Seeds 5800–5819, 20 000 trials per seed per S; bias is the mean of γ̂ − γ over trials, averaged over seeds, ± its standard error over the 20 seeds; sd is the per-seed trial standard deviation, mean ± sd over seeds. Batch estimator against the operation on 100 noisy triangles (seed 58): max |difference| 2.78 × 10⁻¹⁶. Analytic values: octant c = 1.2247 (= √(3/2)), b₂ = 0; generic triangle c = 0.6928, b₂ = −0.1415.

| loop | S | bias ± SE | SE from 0 | b₂/S | SE from b₂/S | sd | sd·√S | ratio to c |
|---|---|---|---|---|---|---|---|---|
| octant | 100 | −7.23 × 10⁻⁵ ± 1.9 × 10⁻⁴ | −0.4 | 0 | −0.4 | 0.12210 ± 0.00058 | 1.2210 | 0.9969 |
| | 400 | −1.61 × 10⁻⁴ ± 1.1 × 10⁻⁴ | −1.5 | 0 | −1.5 | 0.06122 ± 0.00037 | 1.2244 | 0.9997 |
| | 1600 | −4.11 × 10⁻⁵ ± 3.9 × 10⁻⁵ | −1.1 | 0 | −1.1 | 0.03064 ± 0.00013 | 1.2256 | 1.0007 |
| | 6400 | +8.88 × 10⁻⁶ ± 2.5 × 10⁻⁵ | +0.4 | 0 | +0.4 | 0.01533 ± 0.00007 | 1.2260 | 1.0010 |
| | 25600 | +9.92 × 10⁻⁶ ± 1.2 × 10⁻⁵ | +0.8 | 0 | +0.8 | 0.00767 ± 0.00004 | 1.2272 | 1.0020 |
| generic | 100 | −1.38 × 10⁻³ ± 7.6 × 10⁻⁵ | −18.2 (flagged) | −1.41 × 10⁻³ | +0.5 | 0.06991 ± 0.00043 | 0.6991 | 1.0090 |
| | 400 | −3.88 × 10⁻⁴ ± 4.4 × 10⁻⁵ | −8.7 (flagged) | −3.54 × 10⁻⁴ | −0.8 | 0.03465 ± 0.00016 | 0.6931 | 1.0004 |
| | 1600 | −8.25 × 10⁻⁵ ± 2.7 × 10⁻⁵ | −3.0 (flagged) | −8.84 × 10⁻⁵ | +0.2 | 0.01733 ± 0.00012 | 0.6933 | 1.0006 |
| | 6400 | −2.45 × 10⁻⁵ ± 1.3 × 10⁻⁵ | −1.8 | −2.21 × 10⁻⁵ | −0.2 | 0.00867 ± 0.00004 | 0.6936 | 1.0011 |
| | 25600 | −1.27 × 10⁻⁵ ± 6.1 × 10⁻⁶ | −2.1 (flagged) | −5.53 × 10⁻⁶ | −1.2 | 0.00433 ± 0.00002 | 0.6934 | 1.0008 |

Pre-registered (i) |bias| ≤ 2 SE for S ≥ 1600 — fails (generic loop, 3.0 SE at S = 1600 and 2.1 SE at S = 25 600). Pre-registered (ii) sd·√S within 10 % of c for S ≥ 400 — holds (largest departure 0.2 %; 0.9 % at S = 100). Largest |bias − b₂/S| for S ≥ 400: 1.5 SE (the octant row at S = 400, whose expectation is 0).

5.9 FC-2, vertex-to-vertex rotation noise, generic triangle, 20 seeds per σ (seed 5900 + 100j + s for the j-th σ, so the rows are independent), 20 000 trials per seed. A rotation common to all three vertices (rms 0.3 rad per axis, 2000 trials, seed 59): max |change| = 2.22 × 10⁻¹⁶ (T14(b): 0). Linear prediction k = 0.7522; bias expectation 0 (T20(a)).

| σ | bias ± SE | bias/SE | sd | sd/σ | ratio to k |
|---|---|---|---|---|---|
| 0.01 | +1.15 × 10⁻⁶ ± 1.4 × 10⁻⁵ | +0.1 | 0.00753 ± 0.00004 | 0.7532 | 1.0014 |
| 0.03 | +1.61 × 10⁻⁵ ± 3.5 × 10⁻⁵ | +0.5 | 0.02263 ± 0.00009 | 0.7542 | 1.0027 |
| 0.10 | −1.12 × 10⁻⁴ ± 1.4 × 10⁻⁴ | −0.8 | 0.07620 ± 0.00049 | 0.7620 | 1.0130 |
| 0.30 | +1.73 × 10⁻⁴ ± 4.6 × 10⁻⁴ | +0.4 | 0.25421 ± 0.00107 | 0.8474 | 1.1265 |

Pre-registered: |bias| ≤ 2 SE for σ ≤ 0.03 — holds, and is a theorem (T20(a)) at every σ; sd/σ within 10 % of k for σ ≤ 0.1 — holds (1.3 % at σ = 0.1; 12.7 % at σ = 0.3, outside the claimed range).

5.10 FC-3, which channels preserve the geometry. (i) A fixed random unitary, isotropic depolarisation to r ~ U(0.05, 1) and a scalar loss factor ~ U(0.01, 1) applied to every vertex of 200 random triangles, seed 510: max |change of the purified γ| = 4.26 × 10⁻¹⁴ (theorem T18: 0). (ii) Outside that class — H/V dephasing of strength g (Stage 1's `dephase` acting on the polarization qubit) and polarization-dependent loss K = diag(1, √(1 − κ)):

| loop | channel | 0 | 0.01 | 0.05 | 0.10 | 0.30 | 0.90 |
|---|---|---|---|---|---|---|---|
| generic | dephasing g | −0.39318 | −0.39078 | −0.38073 | −0.36715 | −0.30024 | −0.01489 |
| generic | loss imbalance κ | −0.39318 | −0.38987 | −0.37649 | −0.35945 | −0.28781 | −0.04390 |
| octant | dephasing g | −0.78540 | −0.78540 | −0.78540 | −0.78540 | −0.78540 | −0.78540 |
| octant | loss imbalance κ | −0.78540 | −0.78037 | −0.75976 | −0.73282 | −0.61073 | −0.09967 |

The octant loop is unmoved by H/V dephasing because its vertices sit on the channel's principal axes — a loop chosen on the protocol's own states cannot see that channel. Sensitivity at zero over random triangles with mutual vertex angles in [30°, 150°], seeds 51000–51019, 100 triangles per seed: median |dγ/dg| = 0.2001 ± 0.0241 rad per unit dephasing; median |dγ/dκ| = 0.3327 ± 0.0395 rad per unit loss imbalance (mean ± sd over seeds of the per-seed median).

Stage 1–4 tables: unchanged, line for line, against a run of the same module file without the Stage 5 block (221 lines, `diff` empty). Against the numbers recorded in the Stage 4 DN, every Stage 1–4 quantity checked agrees to the printed digits except rounding-level residuals in 2.4 (per-seed means 7.02, 6.41, 7.13 × 10⁻¹⁶ here against 7.00, 6.36, 7.10 × 10⁻¹⁶ recorded) and 3.9 (6.66 × 10⁻¹⁶ against 8.88 × 10⁻¹⁶ at d = 4), which depend on the linear-algebra library build and not on the code (A-9).

## 4. Checks

Correctness conditions — theorems and unit tests; cannot fail unless the code is wrong:

- CC-1. T14 (5.0): gauge invariance, unitary invariance, cyclicity, reversal antisymmetry, zero for a retraced path, fan additivity from a vertex and from an auxiliary apex, ket and projector inputs agreeing. Failure would mean `geometric_phase` is not computing (1).
- CC-2. T15 (5.1, 5.2): the identity (3) against Stokes vectors; |γ| equal to half the spherical excess and its sign fixed by the triple product; the six named polarization loops against octant counts; γ ∈ {0, π} for the four-state set and multiples of π/4 for the six-state set, by enumeration to length 5 and, for all lengths, by the reality of the BB84 kets and the π/4 phases of the six-state overlaps.
- CC-3. T16 (5.3, 5.4, 5.4b): total minus dynamical phase equals γ; γ unchanged across twenty Hamiltonians tracing the same loop; the N⁻² sampling law (4) with its constant; the third-order over-rotation law and first-order tilt law (5).
- CC-4. T17 (5.5): the wave-plate loop closes, accrues no dynamical phase, and its total phase is the operation's γ, equal to −(π/2 + 2β).
- CC-5. T18 (5.6, 5.10(i)): the three readings E1, E2, E3 and their closed forms, including a loop with Ω/2 > π/2; invariance of E1 under a fixed unitary, isotropic depolarisation and uniform loss.
- CC-6. T19 (5.7): τ_jkl = γ(a_j → a_k → a_l) for random register states and random purifications; (7) for Stage 4 baths with branch states computed independently; coplanarity of branch triangles for |+⟩ modes. Failure would mean either Stage 2's τ, Stage 4's D or this stage's operation is not what its note says.
- CC-7. T20 (5.8, 5.9): the finite-shot bias equals b₂/S within the Monte Carlo error at every S (largest departure 1.5 SE), including b₂ = 0 for the octant; isotropic vertex noise produces no bias at any σ tested. Common-mode rotation changes nothing (5.9); the batch estimator used for the ensembles equals the operation (5.8).
- CC-8. Stage 1–4 output unchanged by the addition (§3, last paragraph).

Falsifiable claims — contingent; could fail with correct code:

- FC-1 (the extractor at finite statistics, pre-registered; first clause refuted). Claim as pre-registered: from Stokes tomography with S shots per axis per vertex and normalised Stokes vectors, (i) γ̂ is unbiased within 2 standard errors for S ≥ 1600 and (ii) its spread is c/√S within 10 % for S ≥ 400. Outcome (5.8): (ii) holds for both loops down to S = 100. (i) is refuted: the estimator is biased at every S, by b₂/S with b₂ = −0.1415 for the generic loop and 0 for the octant (T20). The first draft's run, with 2000 trials per seed, passed (i); the adversarial pass computed b₂, and with ten times the trials the bias is 3.0 standard errors from zero at S = 1600. Named failure mode, as pre-registered: bias from the nonlinear step between counts and phase; as found: anisotropy of the binomial covariance in the tangent plane, which is why a loop on the measured axes shows none. What happens to the stage: the sentence "the extractor is unbiased" is withdrawn; the bias is small against the spread in a single estimate (ratio |b₂|/(c√S), 2 % at S = 100) but does not average away — pooling M estimates each of S shots leaves b₂/S while the spread falls to c/√(MS), so the bias dominates once M exceeds (c/b₂)²S ≈ 24 S for the generic loop — and an extractor used that way must subtract b₂/S or estimate the states by maximum likelihood before taking the solid angle. T14–T19 are untouched.
- FC-2 (range of the linear error law for drift between vertices, pre-registered). Claim: under independent small rotations of each vertex the spread of the extracted phase is kσ within 10 % for σ ≤ 0.1 rad, k from linear propagation (0.75 rad per rad for the generic loop). Outcome (5.9): holds; the linear law is 13 % low at σ = 0.3. The pre-registered companion clause, no detectable bias for σ ≤ 0.03, turned out to be a theorem at every σ (T20(a)) and is moved to CC-7. Named failure mode: curvature — second-order terms in the vertex displacements, which by T20 cannot shift the mean and show only as excess spread. If it fails at a substrate's actual drift: the per-loop error budget must be computed by simulation rather than by k, and the loop must be traversed faster than the channel drifts. The claim is specific to this loop and this isotropic noise model.
- FC-3 (the substrate claim; stated, not evaluated). Claim: the channel that carries the loop's states in the QKD-Aero simulation acts on them as a fixed unitary, an isotropic depolarisation and a polarization-independent loss, to within a tolerance set by the sensitivities of 5.10 — in which case the extracted γ equals that of the prepared loop. Named failure mode: the channel does not preserve the geometry of the state space — polarization-dependent loss, dephasing in a preferred basis, or a rotation that changes between the transmissions of different vertices — and the extracted phase then shifts at first order (median 0.33 rad per unit loss imbalance, 0.20 rad per unit dephasing, 0.75 rad per radian of vertex-to-vertex drift for the loops tested). Outcome: not evaluated; no channel interface was available to this run and none is assumed. If it fails when tested: the phase reported is a property of the distorted loop, the shift is itself a first-order channel diagnostic, and the stage's theorems stand; what is lost is the equality between the extracted and the prepared geometric phase.

On the classification: FC-1 and FC-2 are statements about a fully specified model — at which S and σ a leading-order law is adequate — and are contingent in the sense Stage 2's FC-2 (numerical adequacy) was, not in the sense of depending on a substrate. FC-3 is the only claim here whose truth depends on something outside the module (A-1).

Not falsifiable claims, stated so they are not mistaken for ones: gauge invariance of the extracted phase is T14; its equality with half the solid angle on the Poincaré sphere is T15; its independence from the dynamical phase is T16 together with T14(g). None of these can fail for any state, path or Hamiltonian in this model; the stage's contingent claim about channels is FC-3. "BB84 states give only 0 or π" is a corollary of T15, not an empirical finding. "Isotropic vertex noise does not bias γ" and "the tomographic bias is b₂/S" are T20.

## 5. Level labels

- The kets and density matrices of the path, the Bargmann invariant B, γ, |B|: Level 3 (states of a d-level system and a gauge-invariant function of them).
- Stokes vector s, the solid angle Ω, the Poincaré sphere: Level 3 for a polarization qubit.
- H, V, D, A, R, L and the wave plates W(δ, α): Level 3 (polarization states and SU(2) operations). The axis labelling and the sign convention of Ω are conventions, not quantities.
- Total phase, dynamical phase, the Hamiltonian E₀ + (ω/2) n·σ: Level 3 as a model of a cyclic evolution; no world process is identified with it.
- E1, E2, E3 for depolarised states and the visibility ν: Level 3; three different physical quantities, each with its own measurement.
- τ_jkl and τ_env(t) (T19): Level 3 (Stage 2's and Stage 4's quantities, now with a second description). The environment branch states |a_k⟩, |E_k⟩: Level 3 within Stage 4's model.
- The finite-shot estimator γ̂, its bias and spread, c, k and b₂: Level 3 statistics of a Level 3 measurement.
- The dephasing and loss-imbalance channels of 5.10, the U(·) parameter ranges, the Hilbert–Schmidt and Haar ensembles, the rotation-noise model: Level 1 stand-ins for unknown substrate and world distributions.
- No Level 2 operational analogue is introduced. The framework's V_E does not appear in this stage; ν in E3 is an interferometric visibility of a different experiment and is not V_E.
- "Loop", "return", "twist", "holonomy" used of anything other than (1): Level 1.

## 6. Cost accounting

Computational scaling of the new operation. `geometric_phase` on N states of dimension d multiplies N projectors: O(N d³) as written (O(N d) is possible for ket inputs); a mixed input with `purify=True` adds two eigendecompositions, O(d³), per state. Ensemble size enters linearly. Time steps enter as N, the number of sampled states on a smooth path, with sampling error falling as N⁻² (4); a path made of geodesic arcs has no sampling error at any N. The solid-angle route for qubits is O(N). The Stage 5 block adds about 16 s to the module, most of it the 20-seed, 20 000-trial ensembles of 5.8 and 5.9 and the 20 000-step paths of 5.4b.

Cost on a real substrate. On a QKD-Aero polarization state the direct route is Stokes tomography of each vertex: three analyser settings per vertex, S detections each, spread c/√S. Resolving γ to ±0.01 rad needs S ≈ (c/0.01)², i.e. about 1.5 × 10⁴ per setting for the octant loop and 4.8 × 10³ for the generic one, nine settings per triangle — of order 10⁵ detections, about a second at 10⁵ detections per second; at those S the bias b₂/S is below 3 × 10⁻⁵ rad and immaterial unless many low-S estimates are pooled (FC-1). Two things are not free. A BB84 receiver measures two bases (H/V and D/A); the third Stokes component needs a circular-basis analyser, without which only coplanar loops are resolvable and γ ∈ {0, π}. And the loop must consist of at least three distinct states: a single state before and after the channel is a two-state path with γ = 0 (T14(e)), so "the phase a state acquires in the channel" is not extractable from input and output alone — it needs either the intermediate states of the evolution or a loop of prepared states sent through the channel one after another. The interferometric route (E3) needs the two arms of an interferometer with the loop in one arm and gives γ_E3 with visibility ν, a different number from E1 when the state is depolarised. On a gate-model device the test is one qubit: three state preparations with tomography, at the same 10⁴-per-setting scale for ±0.01 rad, or a Hadamard test with one ancilla for the loop unitary. The systematics that matter, from 5.9 and 5.10: loss imbalance between polarizations (0.33 rad per unit, so 1 % imbalance moves γ by about 3 mrad), dephasing in a preferred basis (0.20 rad per unit), and channel rotation that changes between vertices (0.75 rad per radian); a rotation common to all vertices, depolarisation and uniform loss cost nothing. These are order-of-magnitude figures, not a design.

Parameters this stage needs that no note has yet set. Substrate side: (i) the state set from which loops are built — the protocol's four states, six states, or states prepared off the protocol; (ii) whether the channel interface exposes intermediate states of a state's evolution or only what arrives; (iii) which of E1, E2, E3 an extractor is to report for a depolarised state, since they differ at any r < 1; (iv) bounds on loss imbalance, basis-dependent dephasing and vertex-to-vertex drift for the channel model, without which FC-3 cannot be evaluated; (v) the handedness convention for R and L, which fixes the sign of every γ; (vi) the shots per setting and whether estimates are pooled, which decides whether b₂/S matters. World side: (vii) what a closed path of states of one register is in the world; (viii) whether any world quantity reads a loop phase, and whether direction of traversal matters to it; (ix) whether a record carrier's states can leave a single great circle, which decides whether triangle phases other than 0 and π ever occur (T19, 5.7(b)).

## 7. Open-problems ledger (DN-staging-and-phase-travel-v0.4.1 §13)

1. C1 small-sample estimation — not touched: FC-1 is a finite-sample result for Stokes tomography of a three-state loop, not for the C1 estimator, and transfers nothing to it.
2. Stale-reference detection — touched: a loop phase needs no phase reference between its states (T14(a)) and is blind to a rotation common to all of them (T14(b)) while first-order sensitive, without bias, to rotation that differs between them (FC-2, T20), so it is a reference-free quantity that registers drift during a loop; no detector is built and the discrimination between kinds of drift that makes the problem hard is not addressed.
3. Region → register mapping — sharpened: the mapping must now also say what a closed path of states of one register is in the world, how many distinct states it visits (two give nothing, coplanar ones give a sign only), and — through T19 — what the record states are whose loop phases appear as the triangle phases of three or more histories; until it does, γ has a polarization instance and no world instance.
4. QEC threshold transfer — not touched.
5. Moiré buildability (closed in v0.4.1) — not touched: the twist there is a relative phase between two registers; γ is a loop quantity of one register (or of one record carrier), and no relation between them is claimed.
6. Intervention thresholds — not touched.
7. Identity across reconstruction — not touched.
8. Export ceiling testability — not touched.
9. Module decoherence coefficient — touched: a module kept as a quantum system (Stage 4's reading) does two things to a register of three or more histories — it attenuates each relation by |D_jk| and it adds to each triangle of relations the geometric phase of its own record states (T19), additively across independent modules mod 2π — so the per-module object is a Gram matrix whose gauge-invariant content is the moduli and the loop phases; a module whose record states are qubit states on one great circle can add only a sign. The rate remains unset.
10. Participant memory and novelty — not touched.
11. Provenance authenticity (build the detector where authenticity is free) — not touched.

## 8. What this stage does not claim

It does not claim that a geometric phase has been extracted from the QKD-Aero channel: the states are prepared in the module, the channels of 5.10 are stand-ins, and FC-3 is stated and not evaluated. It supplies the extractor, its theorems, its statistics and the list of what a substrate must provide, and claims no more. It does not claim that the BB84 pipeline as it stands carries a continuous geometric phase — its four states cannot (T15). It does not claim that the geometric phase is robust in general: it is exactly insensitive to traversal speed and energy offsets, third-order sensitive to over-rotation, and first-order sensitive to errors of the path, to anisotropic channels and to drift between vertices. It does not claim that the finite-shot extractor is unbiased (FC-1). It does not claim a non-Abelian (Wilczek–Zee) holonomy, an adiabatic theorem, or anything about degenerate subspaces. It does not claim that the three readings of a depolarised state's phase are interchangeable, or choose among them. It does not claim that the triangle phases are a geometric phase of the register's own path: T19 identifies them with loops of the purifying environment's branch states, which exist as physical states only in a model that keeps the environment, as Stage 4's does. It makes no new claim of recoherence or non-Markovianity: 5.7(b) uses Stage 4's environment model to verify an identity about the phases of D_jk(t) and reports no revival, backflow or horizon. It does not claim that any world object traverses a loop or that a world record has a Bloch sphere. It does not touch p_eff or `PhysicsSignals` (Stage 6), and does not derive or constrain the coherence-gate thresholds.

Proposed amendments, recorded here and not applied: (P-16) Coherence framework §13, `BranchRelation` (extends Stage 2's P-2) — for three or more branches the gauge-invariant relational fields are the moduli |ρ_jk| and the loop phases, and the loop phases are geometric phases of the record states (T19), so they belong with `EnvironmentRecord` as much as with the branches. (P-17) Stage 2 DN §8 and Stage 4 DN §8 — the sentences declining to call τ_jkl a geometric phase are superseded by T19, with the qualification that the path is the environment's, not the register's. (P-18) Stage 2's W-4 and Stage 4's P-13 — a third characterisation of when a register is frustrated: when some loop of its record states with non-vanishing invariant has non-zero geometric phase (for qubit record states: encloses a solid angle that is not a multiple of 4π).

## 9. Narrative imports

- [interpretation] Physics → world. A state carried round a closed path returning with a phase fixed by the area enclosed and not by the time taken (T15, T16) ↔ a return that is not a retrace leaving a residue set by where the path went, not how long it took; a path retraced exactly (T14(e)) ↔ going out and back the same way leaving none. The physics does not license identifying any world transit with a path on a state space.
- [interpretation] Physics → world. Triangle phases as loop phases of record states (T19) ↔ three histories whose relations carry a twist that belongs to the geometry of what recorded them, and records confined to one great circle being able to flip a relation's sign but not to turn it. The physics does not license treating any world record as a state with a Bloch sphere.
- [interpretation] Physics → world. Four coplanar states giving only 0 or π (T15) ↔ a vocabulary of alternatives too flat to enclose anything. The physics does not license reading any world vocabulary this way.

## 10. Firewall

C_l1 and V_E — together with γ, |B|, Ω, the three depolarised-state readings, ν and the triangle phases — are not identified with the schemas' `coherence.current` or with the five coherence-gate thresholds (0.376, 0.618, 0.786, 0.886, 1.000); they remain different quantities, and no stage has derived one from the other.

## 11. Class IV boundary statement

Nothing in this stage is about neural, human, or narrative state. The register is a polarization qubit (or, in T14 and T19, a d-level system and its environment), a path is a finite sequence of its states, the wave plates and Hamiltonians are 2 × 2 unitaries and Hermitian matrices, and every quantity reported is a function of those states' overlaps or of Stokes vectors estimated from two-outcome counts. Any Echorym meaning attached to a loop, a return, an enclosed area, or a triangle phase is an interpretation layered on top and is labelled as such in §9. No neural–quantum coupling claim is made or implied.

---

## Appendix A — Review requests

Adversarial review (what could be wrong):

- A-1. What the first pass left open. (a) T20's harmonicity argument is given in one line and checked only through its two consequences (5.8, 5.9); write it out, including the behaviour at the zeros of B, and check that (8) needs only the diagonal of the Hessian (it does if the nine measured components are independent, which they are in `stokes_tomography` and need not be on a real analyser). (b) The O(S⁻²) term of the bias is not computed; the S = 100 row agrees with b₂/S to 0.5 SE, which bounds it loosely. (c) Whether FC-1 and FC-2 belong under "falsifiable claims" at all, or under a third heading for range-of-validity statements about a specified model; this note keeps the series' two headings and says which kind each claim is.
- A-2. Sign and orientation. γ = −Ω/2 with Ω positive for anticlockwise traversal seen from outside, under the axis assignment (s_x, s_y, s_z) = (D/A, R/L, H/V) and |R⟩ = (|H⟩ + i|V⟩)/√2. Optical handedness conventions differ; exchanging R and L flips the sign of every γ in 5.2 and 5.5. Check the convention against whatever the substrate uses before any number here is compared with it.
- A-3. `purify=True` takes the dominant eigenvector. For a qubit this is Stokes normalisation and is invariant under isotropic depolarisation; it is discontinuous where the two largest eigenvalues cross (the operation returns nan within `tol` of a crossing, and an arbitrary but finite answer just outside it), and for d > 2 it is one of several inequivalent mixed-state geometric phases (interferometric, Uhlmann). Decide which is wanted before the operation is used on mixed registers of d > 2.
- A-4. `half_solid_angle` cuts the polygon from an auxiliary apex chosen among 26 fixed directions as the one farthest from every vertex's antipode. For a path that covers the sphere densely no such apex may exist and the routine returns nan; it also returns nan when two consecutive vertices are antipodal, which is correct. Check the tolerance (10⁻¹²) and whether a path-dependent apex would be safer. The first draft's routine fanned from the first vertex and silently returned 0 for H → D → V → A; 5.5's β = 45° row passed then only by rounding.
- A-5. The constants in (4) and (5) come from the small-arc area κ_g c³/12; 5.3 confirms (4) to four digits and 5.4b confirms (5) to 2 × 10⁻⁴ at ε = 0.01, drifting to 2.5 % at ε = 0.1. Derive the next order or confirm the drift is ε².
- A-6. 5.10's sensitivities are medians over triangles restricted to mutual angles in [30°, 150°]; the unrestricted distribution is heavy-tailed near degenerate triangles, and the ensemble is a stand-in. The octant loop's blindness to H/V dephasing is exact and worth a second look as a design hazard: a loop on protocol states cannot diagnose a channel aligned with the protocol's bases.
- A-7. T19's orientation: D_jk = ⟨E_k|E_j⟩ (Stage 4's convention), so arg(D_01 D_12 D_20) = γ(E_0 → E_1 → E_2) and not its reverse; (6) has the same ordering. Check against Stage 2's definition of τ_jkl and the sign in 5.7.
- A-8. `geometric_phase` normalises kets silently and accepts unnormalised density matrices; with `purify=False` on mixed inputs the returned `modulus` is |Tr(ρ_0 … ρ_{N−1})|, not a product of overlap moduli, and the `tol` test applies to that trace.
- A-10. The Stage 1 module header still describes the identity as "falsifiable" and gives the superseded general-population form (carried from Stage 2's A-7 through Stage 4's A-9); nothing earlier was rewritten.

World-side review (what the world must decide):

- W-1. What is a closed path of states of one register in the world — which sequence of world conditions counts as leaving a state and returning to it — and does it ever visit three or more distinct states that are not coplanar? If not, Stage 5 has a polarization instance and no world instance.
- W-2. Does anything in the world read a loop phase? If so, which reading for a state that is not pure: the purified one, the raw trace, or the interferometric one with its visibility (T18)?
- W-3. Does direction of traversal matter in the world? γ changes sign under reversal and vanishes for a retrace.
- W-4. Are a record carrier's states (Stage 4's W-1) confined to a great circle, or free on the sphere? The first allows only sign flips of a triangle of relations; the second allows continuous triangle phases and therefore Stage 2's frustration from records alone.
- W-5. Substrate decisions that are the owner's, not the physics': whether a circular-basis analyser and off-protocol state preparation are added to the QKD-Aero simulation, whether its channel interface exposes intermediate states, the anisotropy and drift bounds of its channel model, and whether loop-phase estimates are pooled across low-count passes (§6, i–vi).

## Development record

| Model and version | Dates of use | Role |
|---|---|---|
| Claude, configured identifier `claude-fable-5-1` (the configured model of the weekly run that produced this note; the serving model can differ within a session) | 2026-10-04 (UTC; the note was filed at 06:56 UTC) | Drafted this note and the Stage 5 block of `echorym_qstate.py`. The session record was not found; whether the module was executed in that session: Needs author confirmation |
| Claude, configured identifier `claude-opus-5-5` | 2026-11-05 | Edited this note for the public copy under the review of 2026-11-05 (cross-references, citations and internal review items; no result changed); executed the full module (Stages 1–6) before and after the edit and found its printed output unchanged |

Author: Lana C. Waddell.
