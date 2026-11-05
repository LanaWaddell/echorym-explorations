Redaction status: cross-references and internal review notes edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05

# DN-quantum-world-stage3: measurement as constraint — a which-history instrument of adjustable strength

Status: design note, week of 2026-09-20. Third step on the staged path (state → coherence → superposition → interference → measurement → decoherence → later stages). This stage: measurement as constraint — a which-history instrument of adjustable strength, with the coherence it leaves computed.
Depends on: DN-quantum-world-stage1-history-pair-state, DN-quantum-world-stage2-multiport-histories, Echorym_Quantum_Coherence_Measurement_Framework (Level 1/2/3 discipline, §10 observation kinds, §13 EnvironmentRecord), DN-quantum-world-register-commitment-v0_1 (the graded-observation ladder, §5).
Artifact: `echorym_qstate.py`, Stage 3 block appended; runs standalone with numpy (`python3 echorym_qstate.py`, about 2 min 10 s on one core, prints the verification table for Stages 1, 2 and 3; the Stage 1 and Stage 2 output is unchanged line for line).
Stop-condition check: this stage does not require a decision about which world-object the register represents. An instrument acting on the register in the history basis is defined at the physics level exactly as Stage 1's qubit and Stage 2's qudit were. Every world-side parameter the stage exposes — which variable an observation resolves, how strong each grade of observation is, whether a record is read — is listed in §6 as unset rather than assumed.
Result flagged up front: one of the two pre-registered falsifiable claims of this stage (FC-1, "a glimpse is the cheapest bit") is refuted by the run (§3, 3.8; §4). It is reported as refuted, not softened.
Class IV boundary: unchanged (§11).

## 1. Concept

Stages 1 and 2 gave histories a real state and a real recombination. Nothing yet observes the register. Stage 3 adds the one thing the coherence framework's §10 and the graded-observation ladder (glimpse → interaction → interrogation → commitment, DN-quantum-world-register-commitment-v0_1 §5) both call for and neither had: an observation that is a physical operation with a strength, whose effect on coherence is computed rather than asserted.

The operation is a which-history instrument on the register. It has two settings. The partition says which variable is resolved: the histories are grouped into blocks and the outcome names a block, so a coarse partition resolves "which of these groups" without resolving "which history within the group". The strength η ∈ [0, 1] says how sharply: η = 0 is no observation at all, η = 1 is the projective measurement of the block variable, and everything between is an unsharp measurement. Two things come out of it. If the record is read, the register is left in one of m conditional states, each with fewer effective histories than before — observation as constraint, the reachable state space shrinking rather than collapsing. If the record is not read, the register is left in the average of those states, which turns out to be exactly a dephasing of the relations that cross block boundaries and the identity on the relations inside a block.

Three results carry the stage. First, reading the record changes no ensemble-average quantity; the coherence lost to an observation is fixed by the record's existence, not by anyone consulting it — the framework's distinction between information "available to an agent" and information "capable of enforcing decoherence" is, on this substrate, no distinction at all on the average state, and a real distinction only on the conditional ones. Second, information gained and coherence lost are both monotone in η at a fixed partition, so the graded-observation ladder is a single parameter. Third, and against the design intuition, the information gained per unit of coherence lost is not largest for a glimpse: it is not monotone in η for generic registers, and for five or more histories a full projective observation can buy each bit more cheaply than a faint one.

## 2. Formalization

Register and partition. ρ is a d × d density matrix in the history basis; C_l1 and C_re are as in Stages 1–2. A partition P = {b_1, …, b_m} groups the history indices into m non-empty blocks; Π_b is the projector onto block b. The default partition is the singletons (m = d).

Instrument. The POVM is

    E_b = ((1 − η)/m) 1 + η Π_b,        Σ_b E_b = 1 for every η ∈ [0, 1],                       (1)

so the outcome channel is p(b | k) = (1 − η)/m + η [k ∈ b]: a symmetric-noise readout of the block variable. The instrument is taken in Lüders form, K_b = √E_b, which is diagonal and non-negative:

    p_b = Tr(E_b ρ),      ρ_b = K_b ρ K_b / p_b   (record read),      ρ′ = Σ_b K_b ρ K_b = Σ_b p_b ρ_b   (record not read).   (2)

At η = 0 every K_b = 1/√m and nothing happens; at η = 1, K_b = Π_b and the instrument is the projective measurement of the block variable.

Theorem T3 (what the unread instrument does). Since the K_b are diagonal, ρ′_kl = ρ_kl Σ_b (K_b)_kk (K_b)_ll. If k and l lie in the same block the two factors are equal and the sum is Σ_b p(b | k) = 1. If they lie in different blocks the sum is (m − 2)(1 − η)/m from the blocks containing neither, plus two terms √((1 − η)/m · ((1 − η)/m + η)). Hence

    ρ′_kl = ρ_kl                (k, l in the same block),
    ρ′_kl = f(η, m) ρ_kl        (otherwise),                                                   (3)
    f(η, m) = (m − 2)(1 − η)/m + (2/m) √((1 − η)(1 + (m − 1)η)),   f(η, 2) = √(1 − η²),   f = 1 − mη²/4 + O(η³).

The unread instrument is therefore a dephasing channel on inter-block relations and the identity on intra-block ones; for the singleton partition it is Stage 2's uniform dephasing with 1 − γ = f(η, d). f is non-increasing in η: f′ ≤ 0 is equivalent to g′ ≤ (m − 2)√g with g = (1 − η)(1 + (m − 1)η), which holds trivially where g′ ≤ 0 and, where g′ > 0 (η < (m − 2)/(2(m − 1))), squares to η ≤ (m − 2)/(m − 1), which is then satisfied. Reading the record cannot change ρ′, since ρ′ is by definition the outcome-average; every ensemble-average quantity — C_l1, C_re, V_E, populations — is the same whether the record is consulted or not.

Theorem T4 (coherence bookkeeping across outcomes). Because every K_b is diagonal and non-negative, no outcome rotates a phase, so |(ρ_b)_kl| = |ρ_kl| (K_b)_kk (K_b)_ll / p_b and

    Σ_b p_b C_l1(ρ_b) = C_l1(ρ′)   (exactly),        Σ_b p_b C_re(ρ_b) ≥ C_re(ρ′)   (convexity of C_re).       (4)

The l1 coherence is linear across the outcomes of this instrument; the relative entropy of coherence is not, and the read register carries at least as much C_re on average as the unread one.

Theorem T5 (information and the effective number of histories). Let K be the history variable with distribution q_k = ρ_kk and B the outcome. The outcome carries

    I(B; K) = H(p_B) − Σ_k q_k H(p(· | k)) = H(p_B) − h_m(η),                                    (5)

where h_m(η) is the entropy of one row (1 − η)/m + η δ of the channel (the same for every row). Two channels of the form (1) with parameters a and b compose to one with parameter ab, so the channel at η is a degradation of the channel at any η′ > η and, by data processing, I is non-decreasing in η for every ρ and every partition. Writing d_eff(ρ) = 2^{H(diag ρ)} for the effective number of histories the populations carry, and noting that diag(ρ_b) is the posterior of K given b,

    I(B; K) = log₂ d_eff(ρ) − E_b log₂ d_eff(ρ_b),                                              (6)

so the information gained is exactly the expected logarithmic reduction in the effective number of histories — the precise form of "observation reduces the reachable state space". For uniform populations I = log₂ m − h_m(η), which at small η is (m − 1)η²/(2 ln 2) + O(η³); more generally the chi-square expansion of (5) gives the same leading term for every q, because p_B ≈ 1/m at small η whatever the populations are.

Theorem T6 (d = 2; contact with Stage 1). For a qubit, (3) gives ρ′_AB = √(1 − η²) ρ_AB, which is Stage 1's `dephase(γ)` with γ = 1 − √(1 − η²), and also Stage 1's `couple_to_environment(δ)` with δ = γ, on every state. The outcome distributions conditioned on |A⟩ and |B⟩ are at trace distance D = ½ Σ_b |p(b | A) − p(b | B)| = η, and V_E′/V_E = √(1 − η²) by Stage 1's identity, so

    D² + (V_E′/V_E)² = 1:                                                                            (7)

the which-way duality relation (Englert 1996, Phys. Rev. Lett. 77, 2154) is saturated by this instrument. The conditional states on the equal-weight pure pair are pure, with populations (1 ± η)/2 and |ρ_AB| = √(1 − η²)/2.

Witness versus measure after an observation (for §3, 3.9). For the singleton partition ρ′ is uniform dephasing, so Stage 2's extrema transform without re-optimisation: R_max′ = 1/d + f(R_max − 1/d), R_min′ = 1/d + f(R_min − 1/d), and

    V_E′/V_E = f S / (2(1 − f)/d + f S),   S = R_max + R_min,                                        (8)

which exceeds the coherence ratio C_l1′/C_l1 = f if and only if S > 2/d. At d = 2, S = 1 = 2/d always (Stage 1). For d ≥ 3 the sign is a property of the state.

Pre-registered claim FC-1 (for §3, 3.8). The information gained per unit of coherence lost by an unread singleton observation, g_q(η) = I_q(η)/(1 − f(η, d)) (the factor C_l1 cancels), was claimed to be non-increasing in η — "a glimpse is the cheapest bit". Its endpoints are in closed form for every q: g(0⁺) = 2(d − 1)/(d ln 2) from the chi-square term, and g(1) = H(q) ≤ log₂ d. So even the endpoint inequality g(1) ≤ g(0⁺) holds for all q only when log₂ d ≤ 2(d − 1)/(d ln 2), i.e. for d ≤ 4; at d = 5 (2.322 > 2.308) a near-uniform register already violates it.

## 3. Verification

All numbers below are printed by `python3 echorym_qstate.py` (Stage 3 block). Every quantity is listed with its analytic expectation where one exists, its seed(s) and N, and its spread over seeds where an ensemble is involved. Numerical tolerance is double precision. Every numerical check agrees with its closed form to machine precision. One entry departs from its pre-registered expectation by far more than 2σ and is flagged: 3.8, where the expectation was "fraction monotone = 1" and the observed fraction is 0.71 ± 0.03 at d = 2 and ≤ 0.03 for d ≥ 3. That entry is a refutation of FC-1, not a numerical discrepancy; the printed statistics are the result.

3.0 Instrument correctness. 200 (state, partition, strength) triples, Hilbert–Schmidt-random states, d = 2..5, random partitions, seed 3. Expectation: Σ_b K_b†K_b = 1, p_b = Tr(E_b ρ), Σ_b p_b ρ_b = ρ′, unit trace, positive conditional states. Observed: max ‖Σ K†K − 1‖ = 3.33 × 10⁻¹⁶; max |p_b − Tr(E_b ρ)| = 0; max ‖Σ p_b ρ_b − ρ′‖ = 2.22 × 10⁻¹⁶; max |Tr − 1| = 4.44 × 10⁻¹⁶; smallest eigenvalue of any conditional state +1.84 × 10⁻⁷ (positive; the random states are full-rank with small eigenvalues, and K ρ K is positive whenever ρ is).

3.1 Theorem T3. 200 triples, d = 2..6, seed 31. Expectation: ρ′ equals ρ with every inter-block element scaled by f(η, m) and every intra-block element untouched. Observed max |deviation| = 1.11 × 10⁻¹⁶.

3.2 Theorem T6. 200 random qubit states and strengths, seed 32. Expectation: ρ′ = `dephase`(1 − √(1 − η²)) = `couple_to_environment`(same), D = η, D² + (V_E′/V_E)² = 1. Observed: max ‖ρ′ − dephase‖ = 2.22 × 10⁻¹⁶; max ‖ρ′ − couple_to_environment‖ = 3.33 × 10⁻¹⁶; max |D − η| = 1.11 × 10⁻¹⁶; max |D² + (V_E′/V_E)² − 1| = 6.66 × 10⁻¹⁶.

3.3 The ladder at d = 2, on Stage 1's Experiment A state (equal-weight pure pair). Analytic: I = 1 − h₂((1 + η)/2) bits; C_l1′ = V_E′ = √(1 − η²); conditional |ρ_AB| on outcome A = √(1 − η²)/2; E[d_eff] = 2^{h₂((1+η)/2)}. V_E′ is the Stage 2 optimiser's value on ρ′.

| η | I (bits) | C_l1′ | V_E′ | \|ρ_AB\|_A | E[d_eff] | C_re′ |
|---|---|---|---|---|---|---|
| 0 | 0.0000 | 1.0000 | 1.0000 | 0.5000 | 2.0000 | 1.0000 |
| 0.10 | 0.0072 | 0.9950 | 0.9950 | 0.4975 | 1.9900 | 0.9747 |
| 0.25 | 0.0456 | 0.9682 | 0.9682 | 0.4841 | 1.9378 | 0.8824 |
| 0.50 | 0.1887 | 0.8660 | 0.8660 | 0.4330 | 1.7548 | 0.6454 |
| 0.75 | 0.4564 | 0.6614 | 0.6614 | 0.3307 | 1.4576 | 0.3439 |
| 0.90 | 0.7136 | 0.4359 | 0.4359 | 0.2179 | 1.2196 | 0.1418 |
| 1.00 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 |

Analytic values identical to four decimals in every cell that has one; max |numeric − analytic| over the table = 7.77 × 10⁻¹⁶. For the unequal pair (p_A = 0.9) at η = 1: I = 0.4690 bits = H(0.9, 0.1) (expectation identical), C_l1′ = 0. Note the quadratic onset: at η = 0.1 the observation costs 0.5 % of the coherence and returns 0.007 bits.

3.4 Which variable is resolved. d = 4, the equal-weight pure register |ψ₄⟩, coarse partition {0,1},{2,3} against the singleton partition. Coarse analytic: |ρ′_01| = 0.25 at every η (untouched), |ρ′_02| = 0.25 √(1 − η²), C_l1′ = 1 + 2√(1 − η²), I = 1 − h₂((1 + η)/2), E[d_eff] = 2^{1 + h₂((1+η)/2)}, and V_E′ = 1 for every η (R_max′ = (1 + f)/2 by alignability, R_min′ = 0 because (1, −1, 1, −1)/2 is orthogonal to the support of ρ′). Singleton analytic: C_l1′ = 3 f(η, 4), I = 2 − h₄(η), E[d_eff] = 2^{h₄(η)}.

| η | coarse C_l1′ | coarse I | coarse E[d_eff] | coarse V_E′ | singleton C_l1′ | singleton I | singleton E[d_eff] | singleton V_E′ |
|---|---|---|---|---|---|---|---|---|
| 0 | 3.0000 | 0.0000 | 4.0000 | 1.0000 | 3.0000 | 0.0000 | 4.0000 | 1.0000 |
| 0.25 | 2.9365 | 0.0456 | 3.8756 | 1.0000 | 2.8435 | 0.1198 | 3.6814 | 0.9732 |
| 0.50 | 2.7321 | 0.1887 | 3.5095 | 1.0000 | 2.4271 | 0.4512 | 2.9257 | 0.8944 |
| 0.75 | 2.3229 | 0.4564 | 2.9151 | 1.0000 | 1.7271 | 1.0066 | 1.9909 | 0.7307 |
| 1.00 | 1.0000 | 1.0000 | 2.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 0.0000 |

Max |numeric − analytic| over the table = 8.88 × 10⁻¹⁶. The coarse observation at η = 1 removes two thirds of C_l1 and halves d_eff while V_E′ reads 1.0000 throughout: Stage 2's point that V_E is a witness, now with an observation as the cause.

3.5 Closed forms and small-η laws, uniform populations, singleton partition, d = 3, 4, 5. Expectation: I = log₂ d − h_d(η) exactly on a 101-point η grid; at η = 10⁻³, (1 − f)/(dη²/4) − 1 and I/((d − 1)η²/(2 ln 2)) − 1 both O(η) ≈ 10⁻³. Observed: max |I − (log₂ d − h_d)| = 6.66, 2.22, 8.88 × 10⁻¹⁶; (1 − f)/(dη²/4) − 1 = −4.99 × 10⁻⁴, −9.98 × 10⁻⁴, −1.50 × 10⁻³; I/((d − 1)η²/(2 ln 2)) − 1 = −3.33 × 10⁻⁴, −6.66 × 10⁻⁴, −9.98 × 10⁻⁴ (all within the expected order).

3.6 Monotonicity. 100 random (populations, partition) pairs, d = 2..5, seed 36, 201-point η grid. Expectation (T5): largest decrease of I(η) between grid points ≤ 0; observed −0.00 (no decrease anywhere). Expectation (T3, proof in §2): largest increase of f(η, m) for m = 2..8 ≤ 0; observed −1.25 × 10⁻⁵ (every step a decrease). Channel composition identity ‖C_a C_b − C_ab‖_max = 2.22 × 10⁻¹⁶ (expectation 0).

3.7 Theorem T4. 200 triples, d = 2..5, seed 37. Expectation: Σ_b p_b C_l1(ρ_b) = C_l1(ρ′) exactly; Σ_b p_b C_re(ρ_b) − C_re(ρ′) ≥ 0. Observed: max |difference| = 4.44 × 10⁻¹⁶; minimum of the C_re difference −9.99 × 10⁻¹⁶ (zero to machine precision; the bound is tight for some triples).

3.8 FC-1, "a glimpse is the cheapest bit" — refuted. Population vectors q ~ Dirichlet(1), 20 seeds (3800–3819) × 200 per d, 50-point η grid in [0.02, 1]; g_q(η) = I_q(η)/(1 − f(η, d)). Pre-registered expectation: fraction of q with g non-increasing = 1. Observed fraction (mean ± sd over seeds): d = 2: 0.7123 ± 0.0348; d = 3: 0.0228 ± 0.0120; d = 4: 0.0005 ± 0.0015; d = 5: 0.0000 ± 0.0000; largest increase seen between grid points +6.95 × 10⁻³, +1.07 × 10⁻², +1.32 × 10⁻², +2.06 × 10⁻² respectively — real, not rounding. Flagged: every d departs from the expectation by more than 2σ. The endpoint inequality g(1) ≤ g(0⁺), with g(0⁺) = 2(d − 1)/(d ln 2) = 1.4427, 1.9236, 2.1640, 2.3083 and g(1) = H(q): fraction satisfied 1.0000 for d = 2, 3, 4 (theorem, §2) and 0.9998 ± 0.0011 at d = 5, where the uniform register has g(1) = log₂ 5 = 2.3219 > g(0⁺). Interpretation of the shape: g starts at a population-independent value, and for generic (non-uniform) populations the middle of the ladder buys bits more cheaply than either end.

3.9 FC-2, the witness after an observation. Singleton partition, η = 0.5 (f = 0.8333 at d = 3, 0.8090 at d = 4), Hilbert–Schmidt-random states, 20 seeds (3900–3919) × 50 per d; (8) evaluated from Stage 2's extrema and, for 5 states per seed, checked against a re-optimised V_E(ρ′). Observed: fraction with S > 2/d (witness ratio above f) = 0.773 ± 0.074 at d = 3, 0.890 ± 0.033 at d = 4; median (V_E′/V_E)/f = 1.0135 ± 0.0023 and 1.0270 ± 0.0025; max |re-optimised − closed form| = 4.44 × 10⁻¹⁶ and 8.88 × 10⁻¹⁶ (expectation 0). The pentagon mixture of Stage 2 (2.8a) has S = 0.5424 < 2/3 and V_E′/V_E = 0.8027 < f = 0.8333: for a frustrated register the witness over-reports the coherence lost to an observation; for most generic registers it under-reports it by 1–3 %.

Stage 1 and Stage 2 tables: unchanged, line for line (checked by diff against the pre-Stage-3 run).

## 4. Checks

Correctness conditions — theorems and unit tests; cannot fail unless the code is wrong:

- CC-1. The instrument is a valid instrument: POVM completeness, p_b = Tr(E_b ρ), outcome-average equals ρ′, trace and positivity preserved (3.0). Failure would mean `observe` is not implementing (1)–(2).
- CC-2. Theorem T3 (3.1): the unread instrument scales inter-block relations by f(η, m) and leaves intra-block relations alone; f non-increasing (3.6, proof in §2); the small-η law 1 − f = mη²/4 + O(η³) (3.5).
- CC-3. Theorem T6 (3.2): at d = 2 the unread instrument coincides with Stage 1's dephasing channel and with Stage 1's which-history record on every state, D = η, and D² + (V_E′/V_E)² = 1. Failure would mean Stage 3 is not a strict extension of Stage 1.
- CC-4. Theorem T4 (3.7): C_l1 is linear across outcomes; C_re is convex across outcomes.
- CC-5. Theorem T5 (3.3–3.6): I = H(p_B) − h_m(η); I non-decreasing in η (channel composition (1 − ab)/m + ab δ checked directly); I = log₂ d_eff(ρ) − E_b log₂ d_eff(ρ_b); the closed-form ladders of 3.3 and 3.4 to machine precision.
- CC-6. The closed-form transform (8) of Stage 2's extrema under uniform dephasing agrees with a re-optimised V_E(ρ′) (3.9): a cross-check of the Stage 2 optimiser on a second family of states.
- CC-7. Every closed-form endpoint of FC-1 (g(0⁺) = 2(d − 1)/(d ln 2) for every q; g(1) = H(q); the d ≤ 4 endpoint theorem) is reproduced by the numerics (3.8, fraction 1.0000 for d ≤ 4).

Falsifiable claims — contingent; could fail with correct code:

- FC-1 (design claim, pre-registered, refuted). Claim: for an unread singleton observation the information gained per unit coherence lost, g_q(η), is non-increasing in η — the faintest observation is the cheapest way to learn a bit. Named failure mode: population dependence — the chi-square term makes g(0⁺) population-independent while H(q) and the shape of I(η) are not. Outcome (3.8): the claim fails for 29 % of population vectors at d = 2, for about 98 % at d = 3 and for essentially all at d ≥ 4, and its endpoint form fails for near-uniform registers at d ≥ 5. What happens to the stage: the qualitative sentence "a glimpse is cheap per bit" is withdrawn from every interpretation; the two monotonicity theorems (T3, T5) that make the ladder one parameter are untouched, since they concern I and C separately, not their ratio; §9 carries the withdrawal explicitly. What survives as a theorem: g(1) ≤ g(0⁺) for every q when d ≤ 4 (CC-7).
- FC-2 (ensemble claim). For generic mixed registers under the Hilbert–Schmidt measure, an unread observation is under-reported by the witness V_E — V_E′/V_E exceeds the true coherence ratio f for most states (77 % at d = 3, 89 % at d = 4; median excess 1.4 % and 2.7 %, 3.9). Named failure mode: ensemble misspecification — a world whose registers are frustrated in the sense of Stage 2 (S < 2/d, e.g. the pentagon mixture) has the opposite sign, and the witness over-reports the loss. If it fails: nothing in the theorems changes; the recommendation that d ≥ 3 reports carry C_l1/(d − 1) beside V_E (Stage 2, P-1) gains a second reason either way, since V_E′/V_E ≠ f in both directions.
- FC-3 (family claim). The world's observation events are describable within the symmetric-noise family (1) — one partition and one strength — so that the ladder is one parameter. Named failure mode: an observation whose readout errors are asymmetric across histories, or whose back-action is not diagonal in the history basis (a measurement in another basis, or one with feedback), lies outside (1); then T3's factor is not f(η, m), intra-block relations need not survive, and the ladder needs more than one parameter. If it fails: the instrument stays a valid Level 3 object and the theorems hold for it; what is lost is the claim that it models the world's observations, which is a W-side decision (§6, Appendix W-4) before it is a physics one.

Not a falsifiable claim, stated so it is not mistaken for one: "reading the record changes no ensemble-average quantity" is the definition of ρ′ in (2), a theorem, and cannot be falsified by any state or any instrument; what a world can decide is whether its observers act on the conditional state or on the average one, which is a modelling choice, not a test.

## 5. Level labels

- E_b, K_b, p_b, ρ_b, ρ′ (the instrument, its outcomes and its post-measurement states): Level 3 (physical operations and states of a d-level system).
- η (strength): Level 3 — a physical parameter of a real instrument (the meter coupling of §6). The five grade names — glimpse, interaction, interrogation, commitment, irreversible observation — are Level 1 labels for values of η that no note has set.
- The partition P: Level 3 as a set of projectors; "which variable is resolved" is its Level 1 reading.
- f(η, m), C_l1(ρ′), C_re(ρ′), C_l1(ρ_b), C_re(ρ_b): Level 3.
- I(B; K): Level 3 — the classical mutual information between a physical outcome and the population variable of a physical ensemble prepared in ρ. It is information about which history, in the statistical sense; it is not Holevo information about the register, which is a different Level 3 quantity not computed here.
- d_eff = 2^{H(diag ρ)}: Level 3 (a function of the density matrix). Its reading as "how many histories remain reachable" is Level 1 and is not identified with the staging note's reachable set (§10).
- D (trace distance of outcome distributions) and the duality relation (7): Level 3, valid at d = 2 for this instrument.
- V_E′: the framework's Level 2 analogue, which on this substrate is the Level 3 witness of Stage 2.
- The Dirichlet(1) population ensemble of 3.8 and the Hilbert–Schmidt ensemble of 3.9: Level 1 stand-ins for unknown world distributions.
- "Constraint", "read", "unread", "coarse": Level 1 labels for the Level 3 objects above.

## 6. Cost accounting

Computational scaling of the new operation. One application of `observe` costs O(m d²) for the m conditional states (the Kraus operators are diagonal, so each K ρ K is an elementwise scaling), O(m d) for the information, and O(m d³) if C_re of every conditional state is requested (one eigendecomposition per outcome). Ensemble size N enters linearly; a strength sweep with n_η points multiplies by n_η; time steps do not enter — the stage is static, and a dynamics with T observation events multiplies by T (and, if the events are read, requires one random draw per event, since the conditional trajectory is stochastic). The Stage 3 block adds about 40 s to the module, almost all of it in 3.9's 2200 Stage 2 optimisations; the instrument itself is microseconds per call.

Cost on a real substrate. A QKD-Aero polarization state is a two-level system and runs Stage 3 at d = 2 with m = 2 directly. A strength-η which-polarization measurement is one meter qubit prepared in |0⟩ and one controlled rotation by angle θ with η = cos θ — |A⟩|0⟩ → |A⟩(cos(θ/2)|0⟩ + sin(θ/2)|1⟩), |B⟩|0⟩ → |B⟩(sin(θ/2)|0⟩ + cos(θ/2)|1⟩) — followed by a meter readout; K_0 = diag(cos(θ/2), sin(θ/2)) and K_1 its swap are exactly the Kraus operators of (2). "Unread" means the meter result is discarded. Resolving D to ±ε needs about 1/ε² shots per input state, and V_E′ needs Stage 1's phase scan on the unread output, so one point of the ladder at ε = 0.01 is of order 10⁴ shots and a ten-point ladder of order 10⁵ — seconds at 10⁵ detections per second. On a gate-model device the same circuit is one ancilla, one controlled-R_y and a measurement, with 10³–10⁴ shots per setting; for d ≥ 3 with a coarse partition into m blocks, the meter needs ⌈log₂ m⌉ ancillas and one multi-controlled rotation per block. The systematics that matter: a symmetric meter error (an impure meter state) lowers η but keeps the instrument inside the family (1); an asymmetric meter error — different readout fidelity for |A⟩ and |B⟩ — takes it outside, which is FC-3's failure mode and must be characterised before a measured f is compared with (3). These are order-of-magnitude figures, not a design.

Parameters this stage needs from the world that no note has yet set: (i) the partition each kind of observation event resolves — which history-variable a glimpse, an interaction or an interrogation is about; (ii) the strength η of each grade, as numbers; (iii) whether an observation's record is read — whether the world's observers act on the conditional state ρ_b (a stochastic per-event trajectory) or the world only ever carries the average ρ′; (iv) whether the world's observations are within the symmetric-noise family (1) at all (FC-3); (v) what the framework's "observation as state acquisition" resolves — the physics can only add information about a variable without touching the relations one wants kept if that variable is a coarse partition of them (T3), so acquisition-without-dephasing is a statement about which partition is chosen, not about a fourth kind of operation.

## 7. Open-problems ledger (DN-staging-and-phase-travel-v0.4.1 §13)

1. C1 small-sample estimation — not touched: no estimator, no participant data.
2. Stale-reference detection — not touched: no anchors or references appear in a static register.
3. Region → register mapping — sharpened: beyond Stage 2's (a)–(c), the mapping must now assign to every observation event a partition of the register (which variable it resolves) and a strength, and must say whether the observer's record is read; the framework's four observation kinds are settings of this triple (§9), and until it is assigned the instrument has a physics instance but no world instance.
4. QEC threshold transfer — not touched.
5. Moiré buildability (closed in v0.4.1) — not touched.
6. Intervention thresholds — not touched: η is a shape; no threshold number is supplied, and d_eff is not the reachable-set measure.
7. Identity across reconstruction — not touched.
8. Export ceiling testability — not touched.
9. Module decoherence coefficient — touched: an observational module that resolves a block variable at strength η multiplies the inter-block relations by f(η, m) and leaves the intra-block ones alone, whether or not it reads its data; Stage 1's record factor (1 − d) becomes f(η_i, m_i) for module i. The rate remains unset: η_i and m_i per module are world parameters (§6, i–ii).
10. Participant memory and novelty — not touched.
11. Provenance authenticity (build the detector where authenticity is free) — not touched.

## 8. What this stage does not claim

It does not claim that Echorym's observations, observers, participants or modules are quantum instruments, or that any world event is one of the outcomes b. It does not claim recoherence or non-Markovianity: the instrument produces a classical record, a classical record cannot be coherently erased, the environment is not kept as a quantum system in this stage, and the framework's §10 question ("if the record is erased, can histories recohere?") is therefore not answered here — it needs the environment kept coherent, which is Stage 4's model or later. It does not claim that reading is what decoheres — the opposite is shown (T3). It does not claim anything about measurements in a basis other than the history basis, about instruments with asymmetric noise or feedback (FC-3), or about the Holevo information of the register. It does not claim that d_eff → 1 is capture, or that the reachable set of the staging note is d_eff. It does not claim that the duality relation (7) has a d ≥ 3 form; none is stated. It does not claim that a glimpse is cheap per bit: that claim was tested and is withdrawn (FC-1). It does not set the grade values η, the partitions, or whether records are read. It does not estimate T_2,E or T_recohere,E, does not touch dynamics, and does not derive or constrain the coherence-gate thresholds.

Proposed amendments, recorded here and not applied: (P-4) Coherence framework §10 — the four observation kinds (acquisition, dephasing, which-history, capture) be re-expressed as settings of (partition, strength, record read or not): acquisition is a coarse partition at any strength (intra-block relations untouched, T3); dephasing and which-history are the same unread instrument at different strengths (T3, T6); "capture" at the physics level is η = 1 with the record read, which leaves d_eff = block size, and any further meaning is world-side. (P-5) Coherence framework §13, `EnvironmentRecord` — "whether traces remain accessible" and "whether histories remain distinguishable" are different fields with different physics: the second is (partition, η) and fixes the decoherence; the first fixes only which conditional state an agent holds. (P-6) The graded-observation ladder (DN-quantum-world-register-commitment-v0_1 §5) — its Level 3 form is one η per grade and one partition per observation event, with post-observation coherence given by (3) rather than by a score.

## 9. Narrative imports

- [interpretation] Physics → world. The outcome b of a strength-η observation on partition P ↔ what a participant learns from a glimpse, an interaction or an interrogation, with the partition as "what the observation is about" and η as "how much it settles". The physics does not license identifying any world event with an outcome or any grade with a value of η.
- [interpretation] Physics → world. d_eff falling from d toward the block size (6) ↔ "observation reduces the reachable state space rather than collapsing it". The physics does not license this; d_eff is a function of the populations of a d × d matrix, and the reachable set is a world object no stage has mapped.
- [interpretation] Physics → world. The unread instrument decohering exactly as much as the read one (T3) ↔ a which-history record that constrains recombination by existing, whether or not anyone consults it; an observer who reads it holds a sharper state but has not cost the world any more coherence. The physics does not license this reading of any world record.
- [interpretation] Physics → world, withdrawn. "A glimpse is cheap" as a per-bit statement is not supported (FC-1): a glimpse costs coherence quadratically in η, and for generic registers the middle of the ladder — and at d ≥ 5 even the full observation — learns each bit more cheaply than a faint one. The physics does not license the original intuition and this note records its withdrawal.

## 10. Firewall

C_l1, C_re, V_E (before or after an observation), f(η, m), I(B; K) and d_eff are not identified with the schemas' `coherence.current` or with the five coherence-gate thresholds (0.376, 0.618, 0.786, 0.886, 1.000); they remain different quantities, and no stage has derived one from the other.

## 11. Class IV boundary statement

Nothing in this stage is about neural, human, or narrative state. The register is a d-level quantum system, the instrument is a set of Kraus operators on it, the outcome is a classical variable, and every quantity reported is a function of a d × d density matrix and of that variable's distribution. Any Echorym meaning attached to an outcome, a partition, a strength, or the effective number of histories is an interpretation layered on top and is labelled as such in §9. No neural–quantum coupling claim is made or implied.

---

## Appendix A — Review requests

Adversarial review (what could be wrong):

- A-1. The symmetric-noise family (1) is a choice. Check whether a Gaussian-pointer instrument (continuous outcome) or an asymmetric-readout instrument would change any theorem other than the specific factor f(η, m); in particular whether T4's linearity of C_l1 across outcomes and T5's data-processing monotonicity survive for every basis-diagonal instrument (they should, since both proofs use only diagonality and non-negativity of the K_b — but say so or find the counterexample).
- A-2. The proof that f(η, m) is non-increasing (§2) squares an inequality and tracks the sign case; check the case split at η = (m − 2)/(2(m − 1)) and that the reduction to η ≤ (m − 2)/(m − 1) is right, since 3.6 verifies it only on a grid.
- A-3. I(B; K) is classical information about the population variable. Decide whether the world's "which-history information" is that, or the Holevo quantity χ of the ensemble {p_b, ρ_b}, which also counts what the outcome says about the coherences; the two coincide only when the conditional states commute.
- A-4. The endpoint g(0⁺) = 2(d − 1)/(d ln 2) for every q rests on the chi-square expansion with p_B ≈ 1/m; check the O(η³) terms do not depend on q in a way that changes the d ≤ 4 endpoint theorem for very skewed populations (3.8 finds no exception, but the ensemble is Dirichlet(1)).
- A-5. d_eff = 2^{H(diag ρ)} is one of several "effective number" definitions (the inverse participation ratio 1/Σρ_kk² is another). The identity (6) is specific to the Shannon form; state whether any downstream use depends on the choice.
- A-6. In 3.9 the sign rule S > 2/d is derived from (8); check the derivation, and whether the 77 % / 89 % fractions are stable under a different random-state measure (Bures, rank-restricted).
- A-10. The README entry's standing sentence "C_l1 also runs from 0 to 1" (Stage 2's A-10) is still uncorrected; only the Stage 3 line was appended this week.
- A-11. `observe` clamps a mutual information of magnitude below 10⁻¹⁴ to zero so that η = 0 prints 0.0000 rather than −0.0000; confirm this cannot mask a real negative (it cannot, since I ≥ 0 is a theorem, but the clamp should be seen).

World-side review (what the world must decide):

- W-1. Partitions: for each kind of observation event, which variable of the register is resolved — one history, a group of histories, or a coarse property that leaves a whole block of relations untouched? This is the field that gives "acquisition without dephasing" a meaning (§6, v).
- W-2. Grade values: what η is a glimpse, an interaction, an interrogation, a commitment? The physics fixes only that these are ordered and that information and coherence cost are both monotone in them; it supplies no numbers, and rule 1 forbids inventing them.
- W-3. Read or unread: do the world's observers hold conditional states (a stochastic trajectory, one random draw per observation) or does the world carry the average? Every ensemble-average quantity is the same either way; the conditional trajectory is what "constraint" looks like from inside.
- W-4. Family: are the world's observations symmetric-noise, basis-diagonal instruments (FC-3)? If any observation feeds back into the register or has asymmetric errors, the ladder is not one parameter and the modelling needs to say so.
- W-5. Whether an observational module's record is a read or an unread instrument (problem 9): the coherence cost is the same, but the module's data product differs — the unread module holds nothing an agent can condition on.
- W-6. Whether the framework's "capture" is to be tied to η = 1 with a read record (d_eff → block size) or kept as a world-level notion with no instrument-level counterpart; P-4 proposes the former as the physics-level reading only.
- W-7. Whether "a glimpse is cheap" should survive anywhere in the design vocabulary now that its per-bit form is refuted (FC-1): a glimpse is cheap in absolute coherence cost (quadratic in η) and not cheap per bit learned; the two statements should not be conflated in world text.

## Development record

| Model and version | Dates of use | Role |
|---|---|---|
| Claude, configured identifier `claude-fable-5-1` (the configured model of the weekly run that produced this note; the serving model can differ within a session) | 2026-09-20 (UTC; the note was filed at 06:35 UTC) | Drafted this note and the Stage 3 block of `echorym_qstate.py`. The session record was not found; whether the module was executed in that session: Needs author confirmation |
| Claude, configured identifier `claude-opus-5-5` | 2026-11-05 | Edited this note for the public copy under the review of 2026-11-05 (cross-references, citations and internal review items; no result changed); executed the full module (Stages 1–6) before and after the edit and found its printed output unchanged |

Author: Lana C. Waddell.
