Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10

# Echorym — Stage 0 validation case: the BESIII Λ–Λ̄ spin density matrix

Status: pre-Stage-1 note (drafted 2026-09-07). Place before the Stage 1 plan.
Purpose: give the Stage 1 density-matrix machinery one physical, published, two-qubit state to reproduce before it is used on Echorym's own history pairs.

## Why this case

The BESIII measurement of |V_us| (Nature 657, 92–97, 2026; arXiv:2509.09266) uses spin-entangled Λ–Λ̄ pairs from e⁺e⁻ → J/ψ → ΛΛ̄. The quantum-state content of the pair is fully specified by two real production parameters, α_ψ and ΔΦ, plus the production angle θ. That makes it a one-parameter family of genuinely mixed two-qubit states with experimentally fixed coefficients, which is exactly what a first density-matrix module should be checked against.

This is a unit test, not a benchmark. It says nothing about recoherence, non-Markovian revival, or channel loss, and it must not be cited as support for any Echorym coupling claim (Class IV boundary applies).

## The state

Indices μ, ν ∈ {0, x, y, z}. The Λ helicity frame has ẑ along the Λ momentum in the c.m. system and ŷ normal to the production plane; the Λ̄ frame shares ŷ with ẑ reversed. In the Fäldt–Kupsc / Perotti form, the nonzero entries of C_μν(θ; α_ψ, ΔΦ) are:

    C_00 = 1 + α_ψ cos²θ
    C_02 = −C_20 = √(1 − α_ψ²) sinθ cosθ sinΔΦ
    C_11 = sin²θ
    C_13 = −C_31 = √(1 − α_ψ²) sinθ cosθ cosΔΦ
    C_22 = α_ψ sin²θ
    C_33 = −α_ψ − cos²θ

The two-qubit density matrix is

    ρ(θ) = (1 / 4 C_00) Σ_μν C_μν σ_μ ⊗ σ_ν

which is Hermitian, trace one, and rank two, since at fixed θ it is a mixture of the two J/ψ helicity amplitudes.

Published parameter values (BESIII, PRL 129, 131801, 2022), to be confirmed against the paper before use:

    α_ψ ≈ 0.475
    ΔΦ  ≈ 0.752 rad
    α_− ≈ 0.752   (Λ → pπ⁻ decay asymmetry, i.e. spin analyzing power)
    α_+ ≈ −0.756  (Λ̄ → p̄π⁺)

Sources to verify the matrix and signs against: Perotti, Fäldt, Kupsc, Leupold, Song, PRD 99, 056008 (2019); Batozskaya, Kupsc, Salone, Wiechnik, PRD 108, 016011 (2023). Frame conventions flip the signs of C_20, C_31, and C_33 between authors; the entries above are transcribed from memory of the Perotti form and are not to be trusted until checked.

## Checks the Stage 1 module must pass

1. ρ(θ) is positive semidefinite with trace one for all θ ∈ [0, π].
2. rank(ρ(θ)) = 2 for generic θ.
3. Λ polarization reproduces the published form: P_y(θ) = C_02 / C_00.
4. Concurrence C(ρ(θ)) > 0 across θ, which is the entanglement claim BESIII makes.
5. C_l1(ρ(θ)) computed in the σ_z ⊗ σ_z eigenbasis, reported as a curve over θ alongside concurrence, so the two measures can be compared on a state where both are known to be nontrivial.

Landmarks for sanity: at θ = 0 the polarization terms vanish and ρ is a purely σ_z–σ_z correlated state; at θ = π/4 the x–z correlation and the y polarization are maximal.

## Hooks for later stages

Measurement stage: the Λ → pπ decay is a spin analyzer with analyzing power α_− ≈ 0.75 rather than 1, so the observed angular distribution is ρ read out through an imperfect POVM. Keep this case available as the first example of a measurement that only partially resolves the state.

Decoherence stage: not applicable. This system has no environment channel to model; do not stretch it.

## Deliverable

One script (or notebook cell) that takes (α_ψ, ΔΦ, θ) and returns ρ, the five checks above, and the C_l1 and concurrence curves over θ. Ships with the Stage 1 package or immediately before it.
