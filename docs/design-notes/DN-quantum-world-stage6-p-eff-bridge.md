Redaction status: cross-references and internal review notes edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05

# DN-quantum-world-stage6: the p_eff bridge — a photon pair read as a signal interface would read it

Status: design note, week of 2026-10-11. Sixth step on the staged path (state → coherence → superposition → interference → measurement → decoherence → later stages). This stage: the p_eff bridge — a photon pair read as the substrate's signal interface would read it.
Author: Lana C. Waddell.
Depends on: DN-quantum-world-stage1-history-pair-state (V_E = C_l1; `dephase`; the record qubit), DN-quantum-world-stage2-multiport-histories (d-level registers, uniform dephasing, the invariance group of V_E), DN-quantum-world-stage3-measurement-as-constraint (the instrument of strength η), DN-quantum-world-stage4-decoherence-with-memory (`evolve_open`, D_jk(t)), DN-quantum-world-stage5-geometric-phase (the geometry-preserving class of channels; the frame conventions), Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline), DN-staging-and-phase-travel-v0.4.1 (§8.2 three-tier measure; §13), RESULT-moire-mechanic-test (the two-register table reproduced in T26), quantum-qkd-aero docs/INTERFACES.md and src/qkd/signals.py (the field names of `PhysicsSignals`, F = (1 + p)/2, S = 2√2·p) and docs/PHASE_2B5_BACKGROUND_LIGHT.md (p_eff = p_source·S/(S + B)).
Artifact: `echorym_qstate.py`, Stage 6 block appended; runs standalone with numpy (`python3 echorym_qstate.py`; 161 s elapsed for the final run on a two-core machine, of which the Stage 6 block is about a minute — 47 to 73 s when run alone; prints the verification table for Stages 1–6). Nothing earlier is rewritten: with the two Stage 6 insertions removed the file is the Stage 5 module, and the 330 lines of Stage 1–5 output are identical, line for line, with and without them.
Stop-condition check: this stage does not require a decision about which world-object the register represents. The register is the two-photon polarization state behind p_eff; its basis states, its two parts and its correlation matrix are defined at the physics level. What the stage does establish is that one further piece of structure — a factorisation of a register into parts — is needed before any of this stage's quantities has a world instance, and that no quantity of Stages 1–5 can supply or detect it (T26). That is listed for world-side review (W-1) and is not assumed.
Interface: the bridge is built at the state level against the public field names and formulas of `PhysicsSignals` (quantum-qkd-aero docs/INTERFACES.md, which defines chsh_margin = S − 2 and teleportation_margin = F − 2/3). Nothing is wired.
Review record: this note and the Stage 6 block were revised after two review passes — an adversarial pass on a first draft of the code block and its theorems, and a check of the draft note against the printed output. The corrections made between the first run and filing are listed in the last paragraph of §3.
Results flagged up front: (i) the bridge identity is a theorem: for a Werner pair, C_l1 in the H/V product basis, Stage 1's V_E on the heralded photon, and the Werner parameter are one number, and p_eff = p_source·R_s/(R_s + R_b) is the mixing rule for uniformly random accidental coincidences (T21, T22). (ii) "The" effective Werner parameter exists only for isotropic degradation. The CHSH value, the teleportation fidelity and the error rates read different functions of the pair's correlation matrix, ordered p_frame ≤ p_tel ≤ p_qber ≤ p_chsh for every pair (T23), and the coherence is a further reading that depends on the basis; a p read from CHSH over-states the teleportation fidelity of every pair that is not isotropic, and everything Stages 1, 3 and 4 do to one photon is not isotropic (T25). (iii) The tiers key → Bell → teleportation → entanglement → coherence are nested for every pair, so the order of the staging note's three-tier measure is a theorem; where each tier is lost is a property of the noise, and under history-basis dephasing of a perfect pair no tier separates from any other (T24). The staging note's entanglement threshold "γ ≈ 0.75" is 2/3 exactly for the model its test used (T26). (iv) A product register and a maximally entangled register can have identical C_l1, C_re, V_E, gap, triangle phases and populations: these quantities are invariant under every diagonal unitary of the register, the two registers differ by one, and so no recombination test of the series so far can tell them apart (T26). (v) Two pre-registered clauses are refuted: the plug-in CHSH estimate's rate of false violation falls with N (toward 0.92, not toward 0.5), and an unbiased fixed-setting CHSH estimate declares a violation at the threshold more than half the time (§4, FC-1). One statement pre-registered as a theorem is withdrawn because it is not one; the counts of this run do not contradict it (§4, FC-2).
Class IV boundary: unchanged (§11).

## 1. Concept

Stages 1–5 built coherence quantities on a toy register. The substrate that already computes something from a physical state is the photon-pair model behind `PhysicsSignals`, whose degradation is summarised by one number, the effective Werner parameter p_eff. Stage 6 builds it at the state level.

The operation added reads a two-qubit state the way a signal interface would: it returns the CHSH value, the teleportation fidelity, the error rates, a key fraction, the entanglement, Stage 1's coherence measures, and, for each reading, the Werner parameter that reading would imply. On a Werner pair all of them agree, and the number they agree on is Stage 1's coherence. That is the bridge in its exact form: the l1-coherence of the pair in the product basis is p, and when one photon is found in a diagonal state the other is left in a Stage 1 history pair whose recombination visibility V_E is p.

Off the Werner family the readings come apart, and how they come apart is the content of the stage. The CHSH value, the teleportation fidelity and the error rates are different functions of the three singular values of the pair's correlation matrix; the coherence is a function of the state in a chosen basis. The parameters they imply are ordered for every state, they coincide only when the degradation is isotropic, and the operations of Stages 1, 3 and 4 acting on one photon are never isotropic: they scale two singular values and leave the third. The same structure orders the tiers a pair can hold — key, Bell violation, teleportation advantage, entanglement, coherence — as a nested chain for every pair, with the positions of the thresholds belonging to the noise.

Two further results follow from reading earlier stages' registers as pairs. A four-history register has a pair reading only once its histories are grouped into two parts, and the series' register-level quantities cannot see the difference between a product register and an entangled one. And the settings-optimised CHSH value, estimated by plugging tomographic estimates into its closed form, is biased upward at the same order as its statistical error whenever the pair's second and third singular values coincide — which includes every isotropic pair.

## 2. Formalization

Register. A pair state ρ is a 4 × 4 density matrix in the product basis {|HH⟩, |HV⟩, |VH⟩, |VV⟩}, index 2a + b, with |H⟩ = |A⟩ and |V⟩ = |B⟩ of Stage 1 on each photon and Stage 5's axis convention (D/A on x, R/L on y, H/V on z). The reference state is |Φ⁺⟩ = (|HH⟩ + |VV⟩)/√2 and the Werner state is

    ρ_W(p) = p |Φ⁺⟩⟨Φ⁺| + (1 − p) 𝟙/4,        0 ≤ p ≤ 1.                                                  (1)

Operation. `pair_signals(ρ)` computes the correlation matrix T_ij = Tr(ρ σ_i ⊗ σ_j), the local Stokes vectors, the singular values s₁ ≥ s₂ ≥ s₃ of T, and from them

    S = 2 √(s₁² + s₂²)                          CHSH value maximised over settings (Horodecki, Horodecki and Horodecki 1995),
    f = ¼ (1 + s₁ + s₂ − sgn(det T) s₃)          fully entangled fraction, f = max ⟨ψ|ρ|ψ⟩ over maximally entangled ψ,
    F = (2f + 1)/3                              teleportation fidelity of the optimal standard protocol (Horodecki, Horodecki and Horodecki 1999),
    e_i = (1 − s_i)/2,  i = 1, 2                error rates in the two best matched bases,
    r = max(0, 1 − h(e₁) − h(e₂))               asymptotic one-way entanglement-based key fraction (h the binary entropy),          (2)

together with the concurrence (Wootters 1998), the smallest eigenvalue of the partial transpose, C_l1 and C_re in the basis given, the frame-fixed readings e_z = (1 − T_zz)/2, e_x = (1 − T_xx)/2 and ⟨Φ⁺|ρ|Φ⁺⟩ = ¼(1 + T_xx − T_yy + T_zz), and four effective Werner parameters

    p_chsh = S/(2√2),     p_qber = (s₁ + s₂)/2,     p_tel = (4f − 1)/3,     p_frame = (4⟨Φ⁺|ρ|Φ⁺⟩ − 1)/3.                (3)

The closed form for f: a maximally entangled state has no local Stokes vectors and correlation matrix −O with O a proper rotation, so ⟨ψ_O|ρ|ψ_O⟩ = ¼(1 − Tr(OᵀT)) and the maximum over proper rotations of Tr(Oᵀ(−T)) is s₁ + s₂ − sgn(det T) s₃. The module computes f a second way, as the largest eigenvalue of Re ρ in the magic basis, in which the maximally entangled states are the real unit vectors. S, f, F, e₁, e₂, r, the concurrence, p_chsh, p_qber and p_tel are invariant under local unitaries (settings-optimised); C_l1, C_re, e_z, e_x and p_frame are readings in the frame the state is given in. The two margin fields are returned as S − 2 and F − 2/3.

Helpers added with the operation: `werner_state`, `effective_werner`, `with_accidentals`, `on_photon` (a one-photon channel given by Kraus operators), `relation_factor` (multiplies one photon's H/V relation by a complex D), `heralded_state`, `concurrence`, `pair_tiers`, `twist_register`.

Theorem T21 (mixing rule; p_eff). w ρ_W(p) + (1 − w) 𝟙/4 = ρ_W(wp), by (1). An isotropic depolarisation of either photon to Stokes length r (Stage 5's T18 channel) maps ρ_W(p) to ρ_W(rp), so Werner parameters multiply along a chain of isotropic degradations. If true coincidences arrive at rate R_s from a source ρ_W(p_source) and accidental coincidences at rate R_b are uniformly random in every setting, the coincidence-post-selected state is ρ_W(p_eff) with

    p_eff = p_source · R_s/(R_s + R_b),                                                                    (4)

the substrate's p_source·S/(S + B) (quantum-qkd-aero docs/PHASE_2B5_BACKGROUND_LIGHT.md) (the letter S is kept here for the CHSH value). Narrowing the coincidence window lowers R_b and raises p_eff. The rule is an identity given the model; whether accidentals are uniformly random in every setting is the substrate claim FC-3.

Theorem T22 (Werner readouts; the bridge identity). For ρ_W(p): T = diag(p, −p, p), the local Stokes vectors vanish, and

    S = 2√2 p,    f = (1 + 3p)/4,    F = (1 + p)/2,    e₁ = e₂ = e_z = e_x = (1 − p)/2,    concurrence = max(0, (3p − 1)/2),      (5)

so all four parameters of (3) equal p. The only off-diagonal elements of ρ_W(p) in the H/V product basis are ρ_{HH,VV} = p/2 and its conjugate, so

    C_l1(ρ_W(p)) = p.                                                                                      (6)

In another local product basis the coefficient matrix of |Φ⁺⟩ is a unitary divided by √2, with moduli (cos θ, sin θ, sin θ, cos θ)/√2, and the 𝟙 term contributes no off-diagonals, so C_l1 = p(1 + 2 sin 2θ) ∈ [p, 3p]: the Werner parameter is the smallest l1-coherence the pair has in any local product basis, reached in the matched (Schmidt) bases, and three times it is reached in mutually unbiased ones. Heralding: if photon A is found in |D⟩ (probability ½), photon B is left in p|D⟩⟨D| + (1 − p)𝟙/2, which is Stage 1's history pair with p_A = ½ and ρ_AB = p/2; by Stage 1's identity its recombination visibility is

    V_E(heralded) = C_l1(heralded) = p.                                                                    (7)

The framework's Level 2 visibility, earned at Level 3 in Stage 1, is on this substrate the Werner parameter. Thresholds in p: r > 0 iff h((1 − p)/2) < ½, p > 0.7799; S > 2 iff p > 1/√2; F > 2/3 iff entangled iff p > 1/3.

Theorem T23 (ordering, every two-qubit state).

    p_frame ≤ p_tel ≤ p_qber ≤ p_chsh.                                                                     (8)

Proof. ⟨Φ⁺|ρ|Φ⁺⟩ ≤ f by definition of f. p_tel ≤ (s₁ + s₂ + s₃)/3 ≤ (s₁ + s₂)/2 because s₃ ≤ (s₁ + s₂)/2. (s₁ + s₂)/2 ≤ √((s₁² + s₂²)/2) is the inequality between arithmetic and quadratic means. Equality p_tel = p_qber holds iff s₁ = s₂ = s₃ with det T ≤ 0; p_qber = p_chsh iff s₁ = s₂. Hence

    F ≤ ½ (1 + S/(2√2))    for every pair, with equality only for isotropic correlations:                  (9)

a Werner parameter read from the CHSH value over-states the teleportation fidelity of every pair whose degradation is not isotropic. The difference p_chsh − p_tel ≥ 0 is returned as `anisotropy`; it is zero iff s₁ = s₂ = s₃ and det T ≤ 0.

Theorem T24 (nesting of tiers, every two-qubit state).

    r > 0   ⟹   S > 2   ⟹   f > ½ (F > 2/3)   ⟹   entangled   ⟹   C_l1 > 0 in every product basis.          (10)

Proof. (i) h(x) ≥ 4x(1 − x) = 1 − (1 − 2x)², so h(e₁) + h(e₂) ≥ 2 − s₁² − s₂², and r > 0 forces s₁² + s₂² > 1. (ii) Averaging ρ with its spin-flipped image removes the local Stokes vectors and leaves T; the result is, up to local unitaries, Bell-diagonal, and when det T > 0 the positivity of its singlet weight reads s₁ + s₂ + s₃ ≤ 1, which excludes s₁² + s₂² > 1. So S > 2 forces det T ≤ 0, and then f = ¼(1 + s₁ + s₂ + s₃) ≥ ¼(1 + s₁² + s₂²) > ½. (iii) Separable states have f ≤ ½. (iv) A state diagonal in a product basis is separable. No converse holds (one state per gap in 6.4). Consequences: a tier can never be held while a later one in (10) is lost; along any evolution the tiers are lost in the order of (10) or together; the positions of the thresholds are not fixed by the pair and differ between noise families (6.4). The key tier is the tier of the one-way formula in (2), not of key distillability in general, for which two-way post-processing changes the threshold.

Theorem T25 (earlier stages acting on one photon). A history-basis relation factor D on photon B, ρ_{ab,a′b′} → ρ_{ab,a′b′} D_{bb′} with D₀₁ = D, is what Stage 1's `dephase` (D = 1 − γ), Stage 3's unread instrument (D = √(1 − η²)) and Stage 4's bath (D = D₀₁(t), complex) do to that photon. Acting on ρ_W(p) it gives singular values (p, p|D|, p|D|) with det T < 0, hence

    S = 2p √(1 + |D|²),   f = ¼(1 + p + 2p|D|),   e₁ = (1 − p)/2,   e₂ = (1 − p|D|)/2,
    concurrence = max(0, p|D| − (1 − p)/2),   C_l1 = V_E(heralded) = p|D|,                                  (11)

and p|D| = C_l1 ≤ p_tel = p(1 + 2|D|)/3 ≤ p_qber = p(1 + |D|)/2 ≤ p_chsh = p√((1 + |D|²)/2): under history-basis dephasing the coherence reads lower than every settings-optimised parameter and the CHSH value highest. (The frame-fixed p_frame is not in this chain: for D real and non-negative it equals p_tel, and for other phases of D it can fall below C_l1.) The phase of D is a rotation of photon B's frame about the H/V axis and changes only frame-fixed readings: e_x = (1 − p Re D)/2, so a real D that changes sign (Stage 4, T13) sends e_x above ½ while S, F, r and the concurrence are unchanged. For p = 1 and Stage 3's instrument, whose which-history distinguishability on photon B is η (Stage 3, T6),

    (S/2)² + η² = 2:                                                                                       (12)

the Bell value of the pair is fixed by how much which-history information about one photon exists, read or not. Stage 5's geometry-preserving class acts as expected: a fixed local unitary leaves s₁, s₂, s₃ unchanged and moves only the frame-fixed readings; isotropic depolarisation multiplies p by r (T21); polarization-dependent loss is outside the class.

Theorem T26 (a four-history register read as a pair). Take Stage 2's equal-weight register with amplitudes ½e^{iθ_ab}, and the factorisation of its four histories into two two-level parts by index = 2a + b. Its concurrence is 2|c₀₀c₁₁ − c₀₁c₁₀| = |sin(χ/2)| and, being pure, its singular values are (1, |sin(χ/2)|, |sin(χ/2)|), so

    concurrence = |sin(χ/2)|,    S = 2√(1 + sin²(χ/2)),    χ = θ₀₀ + θ₁₁ − θ₀₁ − θ₁₀ = arg(ρ_{00,01} ρ_{11,10}).   (13)

χ is the relative phase between the b-relation when a = 0 and the b-relation when a = 1. It is unchanged by local diagonal unitaries and removed by the diagonal unitary diag(1, 1, 1, e^{−iχ}) of the register. Stage 2's recombination scan ranges over all diagonal unitaries of the register, and C_l1, C_re, the populations and the triangle phases are invariant under them, so V_E, C_l1, C_re, Δ, τ_jkl and the populations are identical for the product register (χ = 0, |D⟩|D⟩) and the maximally entangled one (χ = π). The invariance group of the series' register-level quantities contains entangling gates; the quantity that separates the two registers exists only once the factorisation is given. χ is the twist angle of the two-register test in RESULT-moire-mechanic-test: (13) reproduces that note's table (concurrence 0, 0.383, 0.707, 0.924, 1 and S = 2.000, 2.141, 2.449, 2.723, 2.828 at twist 0, π/4, π/2, 3π/4, π). Under Stage 2's uniform dephasing γ the register is (1 − γ)|ψ⟩⟨ψ| + γ𝟙/4, which for χ = π is locally equivalent to ρ_W(1 − γ): C_l1/(d − 1) = 1 − γ = p, the Bell tier is lost at γ = 1 − 1/√2 = 0.2929, the key tier at 0.2201, teleportation and entanglement at γ = 2/3 exactly, coherence at γ = 1.

Estimators for §3 (6.7). With N coincidences in total: route V measures Z⊗Z and X⊗X with N/2 each and returns p̂ = (Ê_zz + Ê_xx)/2, unbiased with variance (1 − p²)/N exactly; route C measures the four CHSH settings with N/4 each and returns Ŝ, unbiased with variance 16(1 − p²/2)/N exactly, so p̂ = Ŝ/(2√2) has variance (2 − p²)/N — at least twice route V's; route T measures the nine Pauli settings with N/9 each and plugs T̂ into (2). For an isotropic pair the three singular values of T are degenerate, the plug-in selects the two largest of three perturbed values, and to first order Ŝ − S = (tr H − λ_min(H))/√2 with H = G + Gᵀ and G a 3 × 3 Gaussian matrix of entry variance 9(1 − T_ij²)/N: a bias of order N^{−1/2}, the same order as the spread. The same holds whenever s₂ = s₃.

## 3. Verification

All numbers below are printed by `python3 echorym_qstate.py` (Stage 6 block). Every quantity is listed with its analytic expectation where one exists, its seed(s) and N, and its spread over seeds where an ensemble is involved. Unless a standard error (SE) is named, ± is the standard deviation over the 20 seeds of the per-seed value. Every closed-form check agrees to rounding, with one stated exception: quantities that pass through the concurrence where it vanishes carry square-root rounding noise of order 10⁻⁸ (6.0, 6.6). Entries that depart by more than 2σ from an expectation are flagged; there are four groups, all in 6.7. (a) The route-C control was pre-registered at 0.5: observed 5.2, 2.9 and 1.3 standard errors above 0.5 at N = 900, 9 000, 90 000 — a refutation of the pre-registered value, not a numerical discrepancy: the exact binomial value is 0.50256, 0.50081, 0.50026, from which the observations are 1.2, 1.8 and 0.9 standard errors. (b) The rate of false violation of the plug-in estimate was pre-registered not to fall with N: it falls, 0.9480 → 0.9289 → 0.9220, each step many standard errors, toward the large-N limit 0.9185. (c) bias·√N of the plug-in estimate at N = 90 000 is 5.635 ± 0.007 against the large-N limit 5.544 ± 0.006, about ten standard errors above it; the differences from the limit at the three N are 0.894, 0.288, 0.091, falling by 3.10 and 3.17 per decade of N against √10 = 3.16, i.e. a next-order correction of relative size N^{−1/2}, not an error in the limit. (d) For the same reason sd·√N of the plug-in estimate at N = 900, 3.9613 ± 0.0176 (SE 0.0039), is about twelve standard errors below the limit 4.0103; at N = 9 000 and 90 000 it is within 2 SE of it. One theorem-level entry sits at the 2σ line and is reported for that reason: route V's bias at p = 0.9 is +1.85 × 10⁻⁵ ± 9.3 × 10⁻⁶, 2.0 standard errors from its exact expectation 0.

6.0 Correctness of the operation. 200 Hilbert–Schmidt-random two-qubit states, seed 6. Expectation 0 for each equality. max |f from singular values − f from the magic basis| = 5.55 × 10⁻¹⁶; no random maximally entangled state (200 per state) exceeds f (largest excess −4.03 × 10⁻⁴); max |S − ⟨CHSH⟩ at the settings built from the singular vectors of T| = 1.55 × 10⁻¹⁵ (the literal expectation of the CHSH operator); no random setting quadruple (200 per state) exceeds S (largest excess −5.30 × 10⁻²); concurrence > 0 against a negative partial transpose: 0 disagreements (151 of 200 states entangled); max change of S, f, concurrence, r, p_chsh, p_qber, p_tel under random local unitaries = 8.77 × 10⁻¹⁴. 2000 random pure product states placed in the entanglement tier: 0; the concurrence returned for them is as large as 5.7 × 10⁻⁹, which is why the tier is decided by the partial transpose. max |p_tel/p − 1| for ρ_W(p) at p = 10⁻³, 10⁻⁶, 10⁻⁹: 8.3 × 10⁻⁸ (the sign of det T is taken relative to s₁³). The two random-search bounds are one-sided and loose; the equality checks are the tests.

6.1 Theorem T21. 200 random (p_source ~ U(0.3, 1), R_s ~ U(1, 100), R_b ~ U(0, 30), r ~ U(0, 1)), seed 61. max ‖w ρ_W(p) + (1 − w)𝟙/4 − ρ_W(p_eff)‖ = 1.11 × 10⁻¹⁶ (an identity by construction of (1)); max ‖one-photon isotropic depolarisation (four Kraus operators, either photon) − ρ_W(rp)‖ = 1.67 × 10⁻¹⁶; max |p_chsh, p_qber, p_tel, p_frame, C_l1 − p_eff| = 6.66 × 10⁻¹⁶.

6.2 Theorem T22. Werner pairs; heralded V_E is Stage 2's optimiser applied to photon B's conditional state when photon A is found in |D⟩.

| p | S | F | e | r | concurrence | C_l1 | V_E (heralded) | tiers held |
|---|---|---|---|---|---|---|---|---|
| 1 | 2.8284 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | all five |
| 0.95 | 2.6870 | 0.9750 | 0.0250 | 0.6627 | 0.9250 | 0.9500 | 0.9500 | all five |
| 0.9 | 2.5456 | 0.9500 | 0.0500 | 0.4272 | 0.8500 | 0.9000 | 0.9000 | all five |
| 0.8 | 2.2627 | 0.9000 | 0.1000 | 0.0620 | 0.7000 | 0.8000 | 0.8000 | all five |
| 1/√2 | 2.0000 | 0.8536 | 0.1464 | 0 | 0.5607 | 0.7071 | 0.7071 | teleportation, entanglement, coherence |
| 0.5 | 1.4142 | 0.7500 | 0.2500 | 0 | 0.2500 | 0.5000 | 0.5000 | teleportation, entanglement, coherence |
| 1/3 | 0.9428 | 0.6667 | 0.3333 | 0 | 0 | 0.3333 | 0.3333 | coherence |
| 0.2 | 0.5657 | 0.6000 | 0.4000 | 0 | 0 | 0.2000 | 0.2000 | coherence |
| 0 | 0 | 0.5000 | 0.5000 | 0 | 0 | 0 | 0 | none |

Closed forms (5)–(7) identical to four decimals in every cell; max |numeric − closed form| over the table, including both frame-fixed error rates, the four effective parameters, the local Stokes vectors and the herald probability, = 2.44 × 10⁻¹⁵. Thresholds by bisection on the operation: key 0.7799 (expected 0.7799), Bell 0.7071 (1/√2), teleportation 0.3333 and entanglement 0.3333 (1/3). C_l1/p over random local product bases, p = 0.8, seeds 6200–6219, 200 bases per seed: smallest per seed 1.1695 ± 0.0979 (minimum 1.0323; theorem ≥ 1), largest per seed 2.9999 ± 0.0002 (maximum 3.0000; theorem ≤ 3); H/V ⊗ H/V basis 1.0000; H/V ⊗ D/A basis 3.0000.

6.3 Theorem T23. Three ensembles, 20 seeds × 500 states each: Hilbert–Schmidt-random (seeds 6300–6319), pairs built from the series' own channels — ρ_W(p), p ~ U(0.3, 1), a relation factor with |D| ~ U(0, 1) and random phase on photon B, post-selected loss imbalance κ ~ U(0, 0.5) on photon A, random local unitaries (seeds 6350–6369) — and random rank-2 states (seeds 6380–6399). Expectation: zero violations of (8).

| ensemble | violations | mean p_chsh − p_tel | mean p_chsh − p_qber | states with det T > 0 |
|---|---|---|---|---|
| Hilbert–Schmidt | 0 | 0.1307 ± 0.0019 | 0.0257 ± 0.0008 | 1462 of 10 000 |
| series channels | 0 | 0.0973 ± 0.0031 | 0.0415 ± 0.0017 | 0 of 10 000 |
| rank-2 | 0 | 0.1436 ± 0.0028 | 0.0337 ± 0.0015 | 617 of 10 000 |

6.4 Theorem T24. Same three ensembles, new seeds (6400–6419, 6450–6469, 6480–6499), 20 × 500. Expectation: zero inclusion violations; zero states with S > 2 and det T > 0; C_l1 > 0 for every entangled state in every product basis (20 random local bases per state).

| ensemble | inclusion violations | key | Bell | teleportation | entanglement | coherence | smallest C_l1 of an entangled state | S > 2 with det T > 0 |
|---|---|---|---|---|---|---|---|---|
| Hilbert–Schmidt | 0 | 0.001 ± 0.001 | 0.007 ± 0.004 | 0.548 ± 0.028 | 0.765 ± 0.018 | 1.000 | 0.4801 | 0 |
| series channels | 0 | 0.095 ± 0.012 | 0.161 ± 0.013 | 0.634 ± 0.018 | 0.638 ± 0.018 | 1.000 | 0.2687 | 0 |
| rank-2 | 0 | 0.128 ± 0.016 | 0.286 ± 0.025 | 0.905 ± 0.011 | 1.000 | 1.000 | 0.4432 | 0 |

(Fractions of states in each tier, mean ± sd over seeds. The Hilbert–Schmidt ensemble contains almost no key or Bell states, which is why the other two are used.) No converse: the product register |D⟩|D⟩ is coherent (C_l1 = 3) and not entangled (S = 2, f = ½ exactly); 0.3|Ψ⁻⟩⟨Ψ⁻| + 0.7|HH⟩⟨HH| is entangled (concurrence 0.3000) with f = 0.3500 ≤ ½; ρ_W(0.5) has f = 0.6250 and S = 1.4142; ρ_W(0.75) has S = 2.1213 and r = 0.

Where each tier is lost, as the value of the coherence parameter c at the loss (bisection on the operation for the first four columns; closed forms from (5) and (11) identical to four decimals; the coherence column is analytic, C_l1 = c, c and 0.95c):

| noise family | key | Bell | teleportation | entanglement | coherence |
|---|---|---|---|---|---|
| isotropic, ρ_W(c) | 0.7799 | 0.7071 | 0.3333 | 0.3333 | 0 |
| \|Φ⁺⟩ with relation factor c on one photon | 0 | 0 | 0 | 0 | 0 |
| ρ_W(0.95) with relation factor c on one photon | 0.4988 | 0.3287 | 0.0263 | 0.0263 | 0 |

Under history-basis dephasing of a perfect pair every tier is held until the coherence is exactly zero; the tiers separate only through the isotropic part of the degradation.

6.5 Theorem T25. (a) Literal checks, seed 65. Stage 1's `dephase` applied to the heralded photon against the relation factor 1 − γ applied to the pair, 100 random (p, γ, herald state): max deviation 6.21 × 10⁻¹⁷. Stage 3's instrument, by its own Kraus operators, on photon B against the relation factor √(1 − η²): 1.11 × 10⁻¹⁶. Stage 4's `evolve_open` on the pair as a four-history register whose charges depend only on photon B's history, against the relation factor D₀₁(t) of the two-level run, 10 tilted four-mode baths × 41 times: 1.05 × 10⁻¹⁵ (this tests the charge-to-index mapping; both sides use `evolve_open`), and against the literal joint evolution of pair and bath on 16 dimensions (n = 2): 1.39 × 10⁻¹⁵ (the independent check). Closed forms (11) and the frame-fixed e_x, e_z under a complex D, 100 draws: 1.55 × 10⁻¹⁵.

(b) Stage 3's ladder read by the pair, p = 1, instrument unread:

| η | S | (S/2)² + η² | F | e_x | r | concurrence | C_l1 = V_E (heralded) |
|---|---|---|---|---|---|---|---|
| 0 | 2.8284 | 2.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 |
| 0.10 | 2.8213 | 2.0000 | 0.9983 | 0.0025 | 0.9747 | 0.9950 | 0.9950 |
| 0.25 | 2.7839 | 2.0000 | 0.9894 | 0.0159 | 0.8824 | 0.9682 | 0.9682 |
| 0.50 | 2.6458 | 2.0000 | 0.9553 | 0.0670 | 0.6454 | 0.8660 | 0.8660 |
| 0.75 | 2.3979 | 2.0000 | 0.8871 | 0.1693 | 0.3439 | 0.6614 | 0.6614 |
| 0.90 | 2.1817 | 2.0000 | 0.8120 | 0.2821 | 0.1418 | 0.4359 | 0.4359 |
| 1.00 | 2.0000 | 2.0000 | 0.6667 | 0.5000 | 0.0000 | 0.0000 | 0.0000 |

Max |numeric − closed form| over the ladder = 6.55 × 10⁻¹⁵. (The r column equals Stage 3's C_re′ column for the same η: with e₁ = 0, r = 1 − h((1 − √(1 − η²))/2), which is the relative entropy of coherence of the equal-weight pair after the observation.)

(c) Settings-optimised against frame-fixed readings:

| pair | S | F | r | concurrence | e_z | e_x | C_l1 | p_frame | p_chsh − p_tel |
|---|---|---|---|---|---|---|---|---|---|
| ρ_W(0.95), D = +0.6 | 2.2158 | 0.8483 | 0.0804 | 0.5450 | 0.0250 | 0.2150 | 0.5700 | 0.6967 | 0.0867 |
| ρ_W(0.95), D = −0.6 | 2.2158 | 0.8483 | 0.0804 | 0.5450 | 0.0250 | 0.7850 | 0.5700 | −0.0633 | 0.0867 |
| ρ_W(0.95), photon B rotated 0.3 rad about y | 2.6870 | 0.9750 | 0.6627 | 0.9250 | 0.0462 | 0.0462 | 1.5115 | 0.9217 | 0.0000 |
| \|Φ⁺⟩, loss imbalance κ = 0.3 on photon B | 2.8063 | 0.9948 | 0.9338 | 0.9843 | 0.0000 | 0.0078 | 0.9843 | 0.9895 | 0.0026 |

A sign change of D is invisible to S, F, r and the concurrence and takes e_x from 0.215 to 0.785. A frame rotation leaves the settings-optimised readings at their ρ_W(0.95) values and raises both fixed-frame error rates; it also raises C_l1 in the fixed basis, from 0.95 to 1.51 — the basis-dependence of (6).

6.6 Theorem T26. (a) Product register (χ = 0) against twisted register (χ = π) under Stage 2's uniform dephasing:

| γ | C_l1 (both) | V_E (both) | S: χ = 0 / π | concurrence: χ = 0 / π | F: χ = 0 / π |
|---|---|---|---|---|---|
| 0 | 3.0000 | 1.0000 | 2.0000 / 2.8284 | 0 / 1.0000 | 0.6667 / 1.0000 |
| 0.2 | 2.4000 | 0.8889 | 1.6000 / 2.2627 | 0 / 0.7000 | 0.6333 / 0.9000 |
| 0.5 | 1.5000 | 0.6667 | 1.0000 / 1.4142 | 0 / 0.2500 | 0.5833 / 0.7500 |
| 0.7 | 0.9000 | 0.4615 | 0.6000 / 0.8485 | 0 / 0 | 0.5500 / 0.6500 |
| 0.9 | 0.3000 | 0.1818 | 0.2000 / 0.2828 | 0 / 0 | 0.5167 / 0.5500 |

Max difference between the two registers in C_l1, C_re, V_E, gap, triangle phases and populations = 2.22 × 10⁻¹⁶ (populations and C_l1 are equal by construction; V_E and the gap are computed by Stage 2's optimiser, and the V_E values printed equal Stage 2's closed form (1 − γ)/(1 − γ + γ/2) to the four decimals shown — a comparison made by hand, not by the module). Max difference between the χ = π register and ρ_W(1 − γ) in S, f, concurrence and r, and of C_l1/(d − 1) from 1 − γ: 8.88 × 10⁻¹⁶. (b) Concurrence and S at χ = 0, π/4, π/2, 3π/4, π: 0.0000, 0.3827, 0.7071, 0.9239, 1.0000 and 2.0000, 2.1414, 2.4495, 2.7229, 2.8284, against (13): max deviation 1.61 × 10⁻⁸ (the square-root noise of the concurrence at χ = 0). 100 random χ, seed 66: χ = arg(ρ_{00,01}ρ_{11,10}) and the concurrence unchanged by random local diagonal unitaries, and the concurrence removed with C_l1 unchanged by diag(1, 1, 1, e^{−iχ}): max deviation 2.14 × 10⁻⁸. (c) χ = π register under uniform dephasing, tiers lost at γ = 0.2201 (key), 0.2929 (Bell; 1 − 1/√2), 0.6667 (teleportation and entanglement; 2/3), 1 (coherence).

6.7 FC-1, finite statistics. 20 seeds × 20 000 trials throughout. Exact laws, p = 0.9, N = 3600, seeds 6700–6719: route V sd·√N = 0.4356 ± 0.0020 (√(1 − p²) = 0.4359), bias +1.85 × 10⁻⁵ ± 9.3 × 10⁻⁶ (SE over seeds; expectation 0); route C sd·√N = 1.0921 ± 0.0051 (√(2 − p²) = 1.0909), bias −6.32 × 10⁻⁶ ± 3.6 × 10⁻⁵; variance ratio C/V = 6.286 ((2 − p²)/(1 − p²) = 6.263). Plug-in estimate of S from nine-setting tomography (route T), seeds 6720 + 100j + s for the j-th N; bias ± SE over seeds; sd·√N mean ± sd over seeds:

| pair | N | bias of Ŝ | bias·√N | bias·N | sd·√N | P(Ŝ > 2) |
|---|---|---|---|---|---|---|
| isotropic, p = 1/√2 (S = 2) | 900 | +0.21459 ± 2.8 × 10⁻⁴ | 6.4377 | — | 3.9613 ± 0.0176 | 0.9480 ± 0.0019 |
| | 9 000 | +0.06148 ± 6.7 × 10⁻⁵ | 5.8321 | — | 4.0004 ± 0.0229 | 0.9289 ± 0.0019 |
| | 90 000 | +0.01878 ± 2.4 × 10⁻⁵ | 5.6348 | — | 4.0070 ± 0.0214 | 0.9220 ± 0.0016 |
| ρ_W(0.95) with \|D\| = 0.6, s = (0.95, 0.57, 0.57), S = 2.2158 | 900 | +0.13667 ± 2.1 × 10⁻⁴ | 4.1001 | 123.0 | 2.9572 ± 0.0138 | — |
| | 9 000 | +0.03205 ± 5.2 × 10⁻⁵ | 3.0403 | 288.4 | 2.7964 ± 0.0105 | — |
| | 90 000 | +0.00890 ± 1.9 × 10⁻⁵ | 2.6697 | 800.9 | 2.7565 ± 0.0187 | — |
| Bell-diagonal, s = (0.80, 0.74, 0.66), S = 2.1795 | 900 | +0.13274 ± 2.4 × 10⁻⁴ | 3.9821 | 119.5 | 3.7469 ± 0.0167 | — |
| | 9 000 | +0.01634 ± 6.0 × 10⁻⁵ | 1.5506 | 147.1 | 3.8142 ± 0.0205 | — |
| | 90 000 | +0.00164 ± 2.1 × 10⁻⁵ | 0.4933 | 148.0 | 3.8141 ± 0.0143 | — |

(P(Ŝ > 2): mean ± sd over seeds.) Large-N Gaussian limit for the isotropic pair (400 000 draws, seed 67; added after the first run): bias·√N → 5.5437 ± 0.0063 (SE over draws), sd·√N → 4.0103, P(Ŝ > 2) → 0.9185 (single run; no spread computed for these two). Route-C control at the threshold (integer counts; an atom at Ŝ = 2 is split evenly): 0.5033 ± 0.0028, 0.5022 ± 0.0032, 0.5009 ± 0.0031 (mean ± sd over seeds; SE = sd/√20) at N = 900, 9 000, 90 000; exact binomial values 0.50256, 0.50081, 0.50026 (every correlator has |E| = ½ at p = 1/√2, so the favourable count is Binomial(N, ¾); the leading skewness correction ½ + (2/√3)/(6√(2πN)) gives the same five decimals; both added after the first run). Pre-registered: (a) bias·√N constant within 15 % over the three N for the isotropic pair — holds (spread 13.5 %, monotone toward the limit). (b) P(Ŝ > 2) > 0.6 at each N — holds (the estimate written down before the run was 0.75; the observed rate is 0.92–0.95); "the rate does not fall with N" — fails. Control at 0.5 within 2 SE — fails at N = 900 and 9 000. The two rows not pre-registered show the scope: with s₂ = s₃ (every pair of (11)) the bias is still of order N^{−1/2}, bias·√N falling slowly toward its own limit; with three distinct singular values it crosses over to order N⁻¹ (bias·N → 148) once the statistical error per entry, 3/√N, is below the gaps between them.

6.8 FC-2, the Bell tier under Stage 4's bath on one photon. ρ_W(0.95); photon B's relation carries D(t) of a bath of n |+⟩ modes, g_i, ω_i ~ U(0.5, 1.5), T = 20 on 2001 points, seeds 6800 + 100n + s, 20 seeds per n. By (11) the Bell tier is held iff |D| > √(1/p² − 1) = 0.3287 and the key tier iff |D| > 0.4988.

| n | Bell tier lost and regained | key tier lost and regained | first loss of the Bell tier, t | largest \|D\| after its first minimum | fraction of horizon held: Bell | key |
|---|---|---|---|---|---|---|
| 4 | 20/20 | 17/20 | 0.718 ± 0.075 | 0.6557 ± 0.1547 (max 0.9848) | 0.1386 ± 0.0750 | 0.0779 ± 0.0576 |
| 8 | 3/20 | 2/20 | 0.514 ± 0.059 | 0.2038 ± 0.1461 (max 0.5953) | 0.0297 ± 0.0110 | 0.0222 ± 0.0059 |
| 16 | 0/20 | 0/20 | 0.374 ± 0.024 | 0.0047 ± 0.0059 (max 0.0284) | 0.0187 ± 0.0012 | 0.0148 ± 0.0009 |

The threshold rule against `pair_tiers` on the evolved pair at 21 times per seed: 0 disagreements. Nesting in time (T24: the key tier never held with the Bell tier lost; the key tier first lost no later than the Bell tier; the key tier held for no larger a fraction of the horizon): 0 violations in 60 seeds. Pre-registered counts for the Bell tier — n = 4: at least 15; n = 8: between 1 and 8; n = 16: 0 — all hold.

6.9 Stand-ins for FC-3 (the substrate claim is not evaluated). (a) Accidental coincidences from a partially polarised background: each side's background has Stokes vector π_b along H/V, so the accidental pair state is a product of two partially polarised states; R_s/(R_s + R_b) = 0.9, p_source = 0.98, p_eff = 0.8820. (b) A relation factor 1 − g on one photon of ρ_W(0.9); closed form for p_chsh − p_tel from (11) identical to four decimals.

| case | p_chsh | p_qber | p_tel | p_frame | C_l1 | e_z | e_x | p_chsh − p_tel |
|---|---|---|---|---|---|---|---|---|
| (a) π_b = 0 | 0.8820 | 0.8820 | 0.8820 | 0.8820 | 0.8820 | 0.0590 | 0.0590 | 0.0000 |
| (a) π_b = 0.2 | 0.8840 | 0.8840 | 0.8833 | 0.8833 | 0.8820 | 0.0570 | 0.0590 | 0.0007 |
| (a) π_b = 0.5 | 0.8946 | 0.8945 | 0.8903 | 0.8903 | 0.8820 | 0.0465 | 0.0590 | 0.0043 |
| (a) π_b = 0.8 | 0.9146 | 0.9140 | 0.9033 | 0.9033 | 0.8820 | 0.0270 | 0.0590 | 0.0112 |
| (b) g = 0.01 | 0.8955 | 0.8955 | 0.8940 | — | 0.8910 | — | — | 0.0015 |
| (b) g = 0.05 | 0.8778 | 0.8775 | 0.8700 | — | 0.8550 | — | — | 0.0078 |
| (b) g = 0.10 | 0.8562 | 0.8550 | 0.8400 | — | 0.8100 | — | — | 0.0162 |
| (b) g = 0.30 | 0.7768 | 0.7650 | 0.7200 | — | 0.6300 | — | — | 0.0568 |

In (a) the accidentals are a product state and uncorrelated between the sides, but they are no longer uniformly random: both sides' background is polarised along H/V, so the accidental pair has local Stokes vectors and contributes their product, π_b², to T_zz. That raises S and F, so p_chsh and p_tel read above the true mixing fraction 0.8820, while C_l1 and e_x, which the diagonal accidentals do not touch, stay at it. In (b) every reading falls and the coherence falls furthest.

Stage 1–5 tables: unchanged, line for line (330 lines; `diff` empty against a run of the Stage 5 module), and the Stage 1–5 numbers compared against the Stage 5 DN agree to the printed digits, including the two rounding-level residuals that note recorded (2.4: 7.02 × 10⁻¹⁶ at d = 3).

Corrections between the first run and filing. (1) The entanglement tier was first decided by the concurrence with a tolerance of 10⁻¹⁰ and misplaced pure product states; it is now decided by the partial transpose (6.0). (2) The sign of det T was first taken with an absolute cutoff, which dropped s₃ from f for ρ_W(p) with p ≲ 10⁻⁵; the cutoff is now relative. (3) "The key tier is regained in no more seeds than the Bell tier" was pre-registered as a consequence of nesting and is not one — a pair can lose and regain the key tier without losing the Bell tier — and is replaced by the three statements nesting does imply (6.8). (4) The second half of pre-registered clause FC-1(b) was first reported as holding without being tested; it fails. (5) The scope of the N^{−1/2} bias was first stated as "isotropic pairs"; it is s₂ = s₃, and a row for (11)'s family was added. (6) The route-C control was first compared in floating point; it is now counted in integers and compared with its exact binomial value. (7) An analytic key threshold typed as 0.4968 was wrong; the value is 0.4988 and is now computed from the entropy in the module. The pre-registration file's "0.497" carries the same slip.

## 4. Checks

Correctness conditions — theorems and unit tests; cannot fail unless the code is wrong:

- CC-1. The operation (6.0): f two ways; S against the literal CHSH operator at the optimal settings; concurrence against the partial transpose; local-unitary invariance of the settings-optimised readings; product states not placed in the entanglement tier; f on nearly maximally mixed pairs.
- CC-2. T21 (6.1): the mixing rule, isotropic depolarisation of one photon, and all readings returning p_eff.
- CC-3. T22 (6.2): the Werner readouts (5), the bridge identities (6) and (7) with V_E computed by Stage 2's optimiser on the heralded photon, the four thresholds, and C_l1 ∈ [p, 3p] over local product bases. Failure of (7) would mean either the heralding or Stage 1's identity is not what its note says.
- CC-4. T23 (6.3): zero violations of the ordering over 30 000 states in three ensembles, both signs of det T represented.
- CC-5. T24 (6.4, 6.8): zero inclusion violations over 30 000 states; no state with S > 2 and det T > 0; the four converse examples; the family thresholds against closed forms; nesting in time along 60 bath evolutions.
- CC-6. T25 (6.5): Stage 1's, Stage 3's and Stage 4's operations applied literally to one photon equal a relation factor on the pair; closed forms (11); (12) on the ladder; frame-fixed against settings-optimised readings.
- CC-7. T26 (6.6): the two registers indistinguishable by the six register-level quantities computed and distinguished by the pair readings; (13) to rounding; local-gauge invariance of χ; thresholds 1 − 1/√2 and 2/3. (That (13) also returns the values printed in RESULT-moire-mechanic-test is a consistency observation about that note, not a theorem.)
- CC-8. Exact estimator laws (6.7): routes V and C unbiased with variances (1 − p²)/N and 16(1 − p²/2)/N, and the route-C control against its exact binomial value. These are statistical checks of exact laws: the simulation agrees within 2.0 SE in every entry (largest: route V's bias, 2.0 SE; the control, 1.8 SE).
- CC-9. Stage 1–5 output unchanged by the addition (§3).

Falsifiable claims — contingent; could fail with correct code:

- FC-1 (the plug-in CHSH estimate at finite statistics; pre-registered; one clause holds, one holds in part, the control fails). Claim as pre-registered: for an isotropic pair at the Bell threshold, the estimate of S obtained by plugging nine-setting tomography into S = 2√(s₁² + s₂²) is biased upward with (a) bias·√N constant within 15 % over N = 900, 9 000, 90 000 and (b) more than 60 % of trials declaring S > 2 at each N, that rate not falling with N; control: the fixed-setting estimate declares S > 2 in half the trials. Outcome (6.7): (a) holds, 13.5 %, with the constant converging from above to 5.54; the first clause of (b) holds by a wide margin (0.92–0.95; the estimate made beforehand was 0.75); the second clause of (b) fails — the rate falls monotonically toward 0.9185, though never toward ½; the control fails — an unbiased estimator of S is not median-unbiased, and the exact rate is ½ + 0.077/√N. Named failure mode, as pre-registered: selection among degenerate singular values; as found: that mechanism, with a finite-N correction of relative size N^{−1/2} that the pre-registration did not anticipate, and binomial skewness in the control. What happens to the stage: any S or `chsh_margin` obtained by maximising over settings after the data are taken must be reported with its bias — 0.019 at N = 90 000 for an isotropic pair, against a spread of 0.013 — or replaced by a fixed-setting estimate, whose spread at equal N is smaller as well (3.46/√N against 4.01/√N); a Bell tier certified by the plug-in value is not certified. T21–T26 are untouched. This is a statement about a fully specified sampling model — its contingent part is the adequacy of leading-order reasoning, in the sense of Stage 5's FC-1.
- FC-2 (the Bell tier can return; pre-registered; holds). Claim: for a pair ρ_W(0.95) whose one photon is coupled to Stage 4's bath, the Bell tier is lost and later regained within T = 20 in at least 15 of 20 seeds at n = 4 modes, in between 1 and 8 of 20 at n = 8, and in none at n = 16. Outcome (6.8): 20, 3 and 0. Named failure mode: bath size and spectral density, as for Stage 4's FC-1 and FC-4 — the return is a finite-bath recurrence of |D| above 0.3287, and it disappears as the number of modes grows; a different frequency distribution or a longer horizon moves the counts. If it fails for a given environment: the Bell tier of that pair — the tier the staging note calls device-independent — once lost, stays lost on the horizon, and only the weaker tiers (which under (11) persist until |D| ≈ 0.03) carry the relation. No device-independent test is run here: S is computed from the model state. The claim is licensed by the environment model used — Stage 4's, kept as a quantum system — and by nothing else; no return is claimed for a classical record or for any channel of the substrate. A companion statement was pre-registered as a theorem — the key tier regained in no more seeds than the Bell tier — and is not one: a pair can lose and regain the key tier without losing the Bell tier. The counts of this run happen to satisfy it (17 against 20, 2 against 3, 0 against 0); it is withdrawn, not tested, and the three statements nesting does imply are checked in its place (CC-5).
- FC-3 (the substrate claim; stated, not evaluated). Claim: the pair state behind the `PhysicsSignals` fields is isotropic — its degradation is a mixture with uniformly random accidental coincidences and isotropic depolarisation only — so that one p_eff reproduces every pair-level field: `chsh_margin` = 2√2·p_eff − 2 and `teleportation_margin` = (1 + p_eff)/2 − 2/3. Named failure mode: any degradation that is not isotropic — basis-dependent dephasing, a partially polarised background, loss imbalance, a frame that drifts between the settings — after which the fields imply different values of p, in the fixed order of (8), by the amounts of 6.9 (0.016 between p_chsh and p_tel for a 10 % loss of one photon's relation; 0.011 for a background polarised to 0.8 at a 10 % accidental fraction). Outcome: not evaluated here; if the fields are computed from a single stored p the claim holds by construction and says nothing about any link. If it fails when tested: p_eff remains the mixing fraction of (4) and stops being a sufficient summary; the interface would need either the three singular values or the readings themselves, and p_chsh − p_tel is the first-order witness that it has failed.

On the classification: FC-1 and FC-2 are statements about fully specified models — FC-1 about how far leading-order reasoning describes a sampling scheme, FC-2 about whether a given family of finite baths returns above a level within a horizon — and are contingent in the sense Stage 4's FC-1 and Stage 5's FC-1 were, not in the sense of depending on a substrate. FC-3 is the only claim here whose truth depends on something outside the module (A-2(c)).

Not falsifiable claims, stated so they are not mistaken for ones: "C_l1 of a Werner pair equals p_eff" and "the heralded V_E equals p_eff" are T22; "p_eff = p_source·R_s/(R_s + R_b)" is T21 given uniformly random accidentals; "CHSH over-reads teleportation" is T23; "Bell violation is lost before entanglement" is T24 — the order of the staging note's three tiers cannot be falsified by any pair or any noise, and a test whose named failure is "entanglement lost before Bell violation" cannot fail; "recombination visibility cannot detect entanglement between parts of a register" is T26.

## 5. Level labels

- ρ (the pair state), T, the singular values, the local Stokes vectors: Level 3 (a two-qubit state and functions of it).
- S, f, F, e₁, e₂, e_z, e_x, the concurrence, the partial-transpose eigenvalue: Level 3. The key fraction r: Level 3 under its stated assumptions (asymptotic, one-way, error rates in two matched bases); it is not the decoy-state key rate of the substrate.
- C_l1, C_re of the pair: Level 3, basis-dependent; C_l1 equals p only in the matched product basis (T22).
- V_E on the heralded photon: the framework's Level 2 analogue, which Stage 1 identified with a Level 3 measure; on this substrate it is, for a Werner pair, the Werner parameter. No new Level 2 quantity is introduced.
- p in ρ_W(p), p_source, p_eff: Level 3 as parameters of a model state. As a statement about any actual link p_eff is Level 1 until calibrated; the substrate tags its uncalibrated constants as illustrative (quantum-qkd-aero docs/INTERFACES.md).
- p_chsh, p_qber, p_tel, p_frame and their differences: Level 3 (functions of Level 3 readings). "Effective Werner parameter" without a subscript names a quantity only for isotropic pairs.
- The tiers of (10): Level 3 properties of a state. "Tier", "held", "lost", "regained": Level 1 labels for them.
- χ: Level 3 once a factorisation of the register is given; without one it is a gauge quantity of the register (removable by a diagonal unitary) and has no level.
- `chsh_margin`, `teleportation_margin` as returned here: Level 3 under the assumed definitions S − 2 and F − 2/3; their identity with the contract's fields: Needs author confirmation.
- Estimators p̂ and Ŝ, their bias and spread: Level 3 statistics of Level 3 measurements under a stated sampling model.
- The Hilbert–Schmidt, series-channel and rank-2 ensembles, the U(·) ranges, the polarised-background model: Level 1 stand-ins for unknown substrate and world distributions.
- No trust quantity appears in this stage, and none is derived: every output of `pair_signals` is a physics-side reading.

## 6. Cost accounting

Computational scaling of the new operation. `pair_signals` acts on a fixed 4 × 4 matrix: nine correlators, one 3 × 3 singular value decomposition and three 4 × 4 eigenvalue problems, 0.30 ms per call measured in this run (2000 calls). Ensemble size and time steps enter linearly (one call per state, or per time when a relation factor D(t) is supplied; D(t) itself costs what Stage 4's `evolve_open` costs, O(n d) per time). The generalisation to two d-level parts has a (d² − 1) × (d² − 1) correlation matrix and no closed form for the CHSH value or for f beyond d = 2; it is not implemented. The Stage 6 block adds about a minute to the module, most of it the 20-seed, 20 000-trial ensembles of 6.7 and the 30 000-state ensembles of 6.3 and 6.4.

Cost on a real substrate. On a polarization pair, route V needs two matched analyser settings and (1 − p²)/ε² coincidences for ±ε on p: about 1.9 × 10³ at p = 0.9, ε = 0.01. The fixed-setting CHSH route needs (2 − p²)/ε², about 1.2 × 10⁴ — 6.3 times as many — with one side's two bases offset by 22.5° from the other's. The teleportation reading needs the third (circular) basis on both sides: p_frame = (T_xx − T_yy + T_zz)/3 from three settings, or the full f from nine. Nine-setting tomography gives every reading at once, with the settings-optimised S biased upward by about 5.5/√N for an isotropic pair (0.058 at N = 9 × 10³, larger than the 0.042 spread), so it does not certify a tier near its threshold at any N at which the bias is not subtracted. A BB84-type receiver pair with the same two bases on both sides can run route V; it cannot run a CHSH test without the offset bases (with H/V and D/A on both sides the CHSH combination is at most 2p), and cannot run the teleportation reading without the circular basis. On a gate-model device the test is two qubits, one entangling gate, and 10³–10⁴ shots per setting; the relation factor of T25 is one ancilla (Stage 3's meter) or Stage 4's ancilla bath on one qubit. The systematics that matter, from 6.5 and 6.9: a frame rotation by φ between the two sides moves no settings-optimised reading, moves the fixed-frame error rates and p_frame at second order (e_z = e_x = (1 − p cos φ)/2 for a rotation about the axis perpendicular to both bases) and the fixed-basis C_l1 at first order (p(1 + 2 sin φ)); a polarised background inflates S and F and leaves C_l1 and the unbiased-basis error rate at the true mixing fraction; loss imbalance and basis-dependent dephasing separate the four effective parameters in the order of (8). These are order-of-magnitude figures, not a design.

Parameters this stage needs that no note has yet set. Substrate side: (i) the definitions of `chsh_margin` and `teleportation_margin` in the contract; (ii) whether the pair-level fields are computed from one stored p or from a state — if from one p, FC-3 is true by construction and untestable; (iii) the accidental model: whether R_b is polarisation-independent, and how R_s and R_b depend on loss, coincidence window and sky background (the loss field enters p_eff only through R_s/(R_s + R_b)); (iv) which readings are settings-optimised and which are taken in a fixed frame, and how the frame is maintained; (v) p_source; (vi) the estimator route and the coincidences per pass; (vii) whether the interface's `qber` and `secure_key_rate`, which the substrate derives from decoy-state BB84, are to be related to the pair's e and r at all — they are different experiments, and this stage does not identify them. World side: (viii) whether any register has parts — a grouping of its histories into joint alternatives of two things — without which no tier above coherence is defined (T26); (ix) if it has, which tier a world relation is asked to hold, and whether its noise is isotropic, dephasing-like or mixed, since that decides whether the tiers separate at all (6.4); (x) whether a relation is read in a maintained frame or by its settings-optimised value.

## 7. Open-problems ledger (DN-staging-and-phase-travel-v0.4.1 §13)

1. C1 small-sample estimation — not touched: FC-1 is a finite-sample result for a CHSH plug-in estimate and transfers no estimator; it shares only the sign of the failure, an upward bias from maximising over estimated quantities.
2. Stale-reference detection — touched: a frame that has rotated on one side raises the fixed-frame error rates e_z and e_x, lowers p_frame, and leaves the settings-optimised readings (S, f) unchanged, while a real loss of correlation degrades both kinds, so p_tel − p_frame ≥ 0 separates a stale shared frame from degradation for a two-part state (6.5c); it does not say whose frame moved, and the discrimination between kinds of drift that makes the problem hard is not addressed.
3. Region → register mapping — sharpened: the mapping must supply a factorisation — which histories of a register are joint alternatives of which two parts — before entanglement, a Bell tier, monogamy or the three-tier measure is defined, and no recombination test of Stages 1–5 can supply or check it, because V_E, C_l1, C_re, the gap and the triangle phases are identical for a product register and a maximally entangled one (T26); the staging note's twist angle is, in register terms, the phase χ of (13), which is a gauge quantity until the parts are named.
4. QEC threshold transfer — not touched: no code, redundancy or error model appears, and the tier thresholds of 6.4 are not an error-correction threshold.
5. Moiré buildability (closed in v0.4.1) — touched: the two-register test's table is reproduced by the series module from (13), its dephasing is identified as the isotropic family with p = 1 − γ (T26), and its entanglement threshold is 2/3 exactly rather than the ≈ 0.75 the staging note records (P-21); nothing about buildability changes.
6. Intervention thresholds — not touched: the thresholds of 6.4 belong to noise families of a pair state and supply no number for any world threshold.
7. Identity across reconstruction — not touched: F is a state-transfer fidelity of a protocol, and no identity criterion is drawn from it.
8. Export ceiling testability — not touched: no export terms or module profiles appear in a pair state.
9. Module decoherence coefficient — touched: when the observed register is one part of a two-part relation, a module's relation factor D is readable from the other part's joint statistics — S = 2p√(1 + |D|²), e₂ = (1 − p|D|)/2 (T25) — so the coefficient has an operational readout that does not require access to the observed part alone, and, for p < 1, a module strong enough to bring |D| below √(1/p² − 1) removes the Bell tier while leaving entanglement in place. The rate remains unset.
10. Participant memory and novelty — not touched: no participant, memory or disclosure object appears.
11. Provenance authenticity (build the detector where authenticity is free) — not touched: no provenance layer or detector appears; every state here is prepared in the module.

## 8. What this stage does not claim

It does not claim that `PhysicsSignals` has been wired to anything: the field names and margin definitions follow the public interface, and no number in this note was produced by the substrate. It does not claim that the substrate's pair state is a Werner state (FC-3), or that its `qber`, `secure_key_rate`, `decoy_anomaly_score` or `loss_rate` are functions of the pair state — the first two come from a different experiment, the last two are not state-level quantities at all, and only `chsh_margin` and `teleportation_margin` are bridged. It does not claim that p_eff is a sufficient summary of a pair in general; T23 says when it is. It does not claim that C_l1 is basis-independent or that it measures entanglement: C_l1 = p holds in the matched product basis of a Werner pair, and a product state can have C_l1 = 3. It does not claim a trust quantity, a trust input, or any aggregation of these readings; the witness p_chsh − p_tel is a physics-side consistency statistic. It does not claim that the key fraction r is achievable by any implemented protocol or equal to any decoy-state rate, or that the key tier of (10) is the boundary of key distillability. It does not claim that any Echorym register has parts, that any world relation is a pair state, or that any world relation holds or loses a tier. It makes one recoherence-type claim, FC-2, and only in the sense the model licenses: the environment is Stage 4's bath kept as a quantum system, the return of the Bell tier is that bath's finite-size recurrence, and no return is claimed for a classical record, for Stage 3's instrument, or for any channel of the substrate; no new non-Markovianity measure is computed. It does not claim monogamy, although a pair whose photon entangles with a bath is the setting for it: the entanglement between photon and bath is not computed. It does not claim that the plug-in bias law holds for estimators other than the one simulated, or that the Gaussian limit's constant has a closed form. It does not derive or constrain the coherence-gate thresholds.

Proposed amendments, recorded here and not applied: (P-20) Coherence framework §13, `BranchRelation` (extends P-2 and P-16) — a relation object that is to carry entanglement needs a field naming the two parts; the gauge-invariant content then includes χ-type phases between conditional relations, which no recombination test reports (T26). (P-21) DN-staging-and-phase-travel-v0.4.1 §8.2 and RESULT-moire-mechanic-test — the entanglement tier is lost at γ = 2/3 exactly for the model tested (uniform off-diagonal dephasing of the twisted register is the isotropic family, p = 1 − γ); 0.75 is the first value on the test script's γ list (…, 0.5, 0.75, 1.0) at which the concurrence printed zero. The tier order is a theorem for every pair and extends to five tiers (10); the spacing is a property of the noise and vanishes for history-basis dephasing of a perfect pair (6.4). (P-22) quantum-qkd-aero docs/INTERFACES.md, `PhysicsSignals` — beside the field table, record which fields are functions of the pair state (two), which come from the prepare-and-measure protocol (two), and which are not state-level (two); and that F = (1 + p)/2 and S = 2√2·p hold together only for an isotropic state. (P-23) Stage 4's W-5 — a sign change of a real D is invisible to every settings-optimised pair reading and takes the fixed-frame error rate above ½ (6.5c): whether it counts as a revival is the same question as whether the relation is read in a maintained frame. (P-24) Any future extractor that reports a settings-optimised CHSH value from estimated correlations should report the fixed-setting value beside it (FC-1).


## 9. Narrative imports

- [interpretation] Physics → world. A pair holding the weaker tiers after losing the stronger (T24) ↔ the staging note's "still working" and "still trustworthy" coming apart: a relation between two parts that still produces joint effects after it has stopped being certifiable. The physics does not license identifying any world relation with a pair state, or any tier with a world property.
- [interpretation] Physics → world. A product register and an entangled register indistinguishable by every recombination test (T26) ↔ two sets of alternatives that look equally coherent whether or not what binds their parts is irreducible; the difference appears only to a reading that knows what the parts are. The physics does not license treating any world register as having parts.
- [interpretation] Physics → world. Fixed-frame readings failing while settings-optimised readings hold (6.5c) ↔ a relation that is intact and read through a reference that has moved. The physics does not license reading any world anchor as a polarization frame.
- [interpretation] Physics → world. The Bell tier returning for a small environment and not for a large one (FC-2) ↔ certifiability that can come back when few things hold the record and cannot when many do. The physics does not license this; the return is a recurrence of a finite spin bath.

## 10. Firewall

C_l1 and V_E — together with p_eff, the four effective Werner parameters, S, F, the error rates, r, the concurrence, χ and the tiers — are not identified with the schemas' `coherence.current` or with the five coherence-gate thresholds (0.376, 0.618, 0.786, 0.886, 1.000); they remain different quantities, no stage has derived one from the other, and the tier thresholds of this stage (0.7799, 0.7071, 1/3) are not gate values.

## 11. Class IV boundary statement

Nothing in this stage is about neural, human, or narrative state. The register is a two-photon polarization state (or, in T26, a four-level system with a chosen factorisation), the operations on it are one-photon channels and analyser settings, and every quantity reported is a function of a 4 × 4 density matrix or of coincidence counts simulated from it. Any Echorym meaning attached to a part, a tier, a frame, or a return is an interpretation layered on top and is labelled as such in §9. No neural–quantum coupling claim is made or implied, and no trust quantity is computed.

---

## Appendix A — Review requests

Adversarial review (what could be wrong):

- A-1. The interface. Check against the public `PhysicsSignals` contract and the quantum-qkd-aero code: the definitions of `chsh_margin` and `teleportation_margin`; whether CHSH is settings-optimised or evaluated at fixed settings; whether the teleportation fidelity is the fully-entangled-fraction form (2f + 1)/3 or computed for the fixed resource |Φ⁺⟩ (then it is (2⟨Φ⁺|ρ|Φ⁺⟩ + 1)/3, i.e. p_frame, and (8) places it lowest); the reference Bell state and the handedness convention (Stage 5's A-2); and whether p_eff multiplies a Werner state at all. Needs author confirmation.
- A-2. What the review pass did not settle. (a) T24's step (ii) is argued through the spin-flip average; write it out, including states with det T = 0. (b) The Gaussian-limit constant 5.54 and the limit for the s₂ = s₃ family are Monte Carlo values with no closed form; the s₂ = s₃ row has not reached its limit at N = 90 000 (bias·√N still falling), so "order N^{−1/2}" for that family rests on the argument in §2 and on bias·N growing, not on an observed plateau. (c) Whether FC-1 belongs under falsifiable claims or under a heading for range-of-validity statements about a specified model (Stage 5's A-1(c), carried).
- A-3. The key fraction. r = 1 − h(e₁) − h(e₂) uses the two best matched bases and ignores local Stokes vectors (a biased raw key), basis-sifting, finite-key effects and two-way post-processing. T24's first implication is a theorem about this formula. Decide whether a key tier belongs in the chain at all, or whether the chain should start at Bell.
- A-4. p_qber. Defined here as (s₁ + s₂)/2, the mean of the two best matched-basis correlations. An interface that reports one error rate in one basis reads s_i or T_ii instead, which is not ordered against p_tel in general (for (11), 1 − 2e₂ = p|D| lies below p_tel and 1 − 2e₁ = p above p_chsh). The ordering (8) is for the quantities as defined.
- A-5. Tolerances. `pair_tiers` uses 10⁻¹⁰ on r, S − 2, f − ½, the partial-transpose eigenvalue and C_l1; a state within 10⁻¹⁰ of a threshold is placed below it. The concurrence is returned with square-root noise of order 10⁻⁸ where it vanishes and is not used for the tier.
- A-6. Checks that are weaker than they look: 6.1's mixing identity is the definition (1) on both sides; 6.5's `evolve_open` comparison tests the charge mapping only; 6.6's equality of C_l1 and populations is by construction; 6.0's random-search bounds never approach equality. The independent checks are named beside each in §3.
- A-7. T26 compares registers under the scan group of Stage 2 (all diagonal unitaries). A recombination test with a different recombiner — one that is itself a product of two two-port recombiners — would have a smaller invariance group; check whether V_E under local recombination only can see χ, since that is the nearest thing to a register-level entanglement test the framework's Experiment A could become.
- A-8. FC-2 counts "lost and regained" on a 2001-point grid with a hard threshold; a tier regained for one grid step counts. The fractions of the horizon held are the more robust numbers.
- A-9. The polarised-background stand-in of 6.9(a) assumes both sides see background polarised along the same axis and that accidentals are a product state; a background polarised along D/A, or correlated between the sides, moves different readings.

World-side review (what the world must decide):

- W-1. Does any register have parts? Entanglement, the Bell tier, monogamy and the three-tier measure need a rule saying which histories are joint alternatives of which two things. Nothing in Stages 1–5 can supply it, and the same sixteen numbers |ρ_jk| describe a register with no relation between its parts and one that is maximally entangled (T26).
- W-2. If it has: which tier is a world relation asked to hold — key, Bell, teleportation, entanglement, or coherence only — and is the answer the same for every relation? The staging note's top tier is the Bell tier; (10) puts one tier above it and one between it and entanglement.
- W-3. What kind of noise does the world apply to a relation — isotropic, history-basis dephasing, or a mixture? Under dephasing alone the tiers do not separate for a perfect pair, and the three-tier measure has nothing to grade; its grading comes entirely from the isotropic part.
- W-4. Is a relation read in a maintained frame or by its best available settings? The two differ exactly when a reference has moved (6.5c), and a sign flip is visible only to the first.
- W-5. Substrate decisions that are the owner's: whether the pair-level fields are generated from one p or from a state; whether a third basis is available on both sides; which estimator route feeds `chsh_margin`; and whether p_eff should be accompanied by an isotropy witness (§6, i–vii).
- W-6. Whether the entanglement threshold recorded in the staging note should be corrected to 2/3 by an append block (P-21).
- W-7. The README's path names entanglement-to-geometry as a later stage; other candidates this stage exposes are a two-part register with its own recombination test (A-7), monogamy for a photon shared between a partner and a bath, and dynamics that are not pure dephasing. The order is the author's to set.

## Development record

| Model and version | Dates of use | Role |
|---|---|---|
| Claude, configured identifier `claude-fable-5-1` (the serving model can differ within a session) | 2026-10-11 (Calgary and UTC) | Drafted this note and the Stage 6 block of `echorym_qstate.py`; executed the module and the numerical checks reported in §3 (four complete runs of the Stage 6 block alone, one complete run of the project copy filed with Stage 5, three complete runs of the assembled module, one timing of the new operation) |
| Claude, same configured identifier, second instance | 2026-10-11 | Reviewed a first draft of the Stage 6 block adversarially and ran its own numerical checks (two scratch scripts); the note and the block were revised after that review |
| Claude, same configured identifier, third instance | 2026-10-11 | Checked the draft note against the printed output, the code and the earlier notes by hand, shell and project search; ran no numerical checks; the note was revised after that check |
| Claude, configured identifier `claude-opus-5-5` | 2026-11-05 | Edited this note for the public copy under the review of 2026-11-05 (cross-references, citations and internal review items; no result changed); executed the full module (Stages 1–6) before and after the edit and found its printed output unchanged |

Records for the Stage 1–5 blocks of the module and their notes: see those notes.

Author: Lana C. Waddell.
