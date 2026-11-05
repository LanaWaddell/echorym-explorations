# Experiments

Use this folder for future runnable experiments, notebooks, scripts, and reproducible evaluation runs.

Early experiments should record:

- Scenario or dataset used
- Schema version
- Run configuration
- State / action / consequence / coherence trajectory output
- Evaluation notes
- Reflection and next steps

Local generated outputs should stay out of git unless they are small, reviewed examples.


## quantum-world/ — staged path to a physically defensible quantum layer

This directory holds the weekly stages that give Echorym a real quantum-state substrate, following the path: real quantum-state structure → coherence → superposition → interference → measurement → decoherence, with non-Markovian recoherence, geometric phase, and entanglement-to-geometry as later stages.

These experiments are physics-layer work governed by the coherence measurement framework and the Class IV boundary, not by Prototype 0. They do not modify `schemas/` and do not depend on the First Conduit trace. They sit under `experiments/` because that is where the repository places reproducible runs, and because the repository's rule that runnable code follows the proved loop applies to Echorym's runtime, not to the physics substrate the runtime will later read.

Contents:

- `echorym_qstate.py` — the running module. Each stage adds one operation; nothing earlier is rewritten. Runs standalone with numpy: `python3 echorym_qstate.py` prints the verification table for every stage completed so far.
- `DN-quantum-world-stage<N>-<slug>.md` — one design note per stage: the concept, the formalization, the falsifiable claim with its failure mode, the numbers from the run, and what the stage does not claim.

Stage 1 (2026-09-06): a history pair as a qubit density matrix. Verified that the coherence framework's recombination visibility V_E equals the l1-norm of coherence C_l1(ρ) identically, that memory without coherence is a diagonal ρ, that a which-history record suppresses V_E by (1 − d) without being read, and that a unitary refocus recovers inhomogeneous dephasing but not a traced-out record.

Stage 2 (2026-09-13): d histories as a qudit, recombined on the balanced d-port transform F_d with one phase per history. Verified that at d = 2 the operation reproduces Stage 1 to machine precision, and that for d ≥ 3 the identity becomes two theorems — R_max − 1/d ≤ C_l1/d, with equality exactly when the off-diagonal phases can be aligned by a diagonal unitary (all triangle phases arg(ρ_jk ρ_kl ρ_lj) zero), and V_E ≤ min(1, C_l1) — so that V_E saturates as d grows while C_l1/(d − 1) does not, making V_E a witness of coherence for d ≥ 3 rather than a measure of it.

Stage 3 (2026-09-20): measurement as constraint — a which-history instrument of adjustable strength η that resolves a chosen partition of the histories. Verified that the unread instrument leaves every relation inside a block untouched and scales every relation across blocks by a closed-form factor f(η, m) (at d = 2 it is Stage 1's dephasing and record channels, saturating D² + V² = 1), that reading the record changes no ensemble-average quantity, that information gained and coherence lost are each monotone in η so the graded-observation ladder is one parameter at a fixed partition, and that the pre-registered claim "a glimpse is the cheapest bit" (information per unit coherence lost non-increasing in η) is refuted for generic registers.

Stage 4 (2026-09-27): decoherence with memory — the environment kept as a quantum system (a bath of spin-½ modes with their own dynamics) coupled to the register's history variable, with a Markovian control matched at T_2. Verified that the register's coherence is ρ_jk(0) D_jk(t) exactly with D the Gram matrix of the environment branch states, that a structured bath revives C_l1 (20/20 seeds at n = 8) while the matched memoryless model cannot, that at d = 2 a coherence revival, BLP information backflow and the failure of CP-divisibility are the same event, so at d = 2 they are not independent evidence of memory, that at d ≥ 3 a pair's backflow can be masked in C_l1 (about 8 % of episodes) and divisibility fails before any pair revives, and that a register reversal while still coupled refocuses a static bath exactly and a dynamic one only partly (T_recohere/T_2 ≈ 2.9), with the staging note's rate law holding only above the environment's dressed frequency and failing to zero at resonance.

Stage 5 (2026-10-04): geometric phase — the gauge-invariant phase −arg(⟨ψ_0|ψ_1⟩⟨ψ_1|ψ_2⟩…⟨ψ_{N−1}|ψ_0⟩) of a closed path of states, on polarization states. Verified that it is unchanged by rephasing any state on the path, equals minus half the solid angle the path encloses on the Poincaré sphere, and is independent of the dynamical phase (theorems of the extractor, not claims); that the four BB84 states can show only 0 or π and the six-state set only multiples of π/4, and that a path of two states shows nothing; that Stage 2's triangle phases are geometric phases of the purifying environment's branch states, so the phase Stage 4's environment adds to three histories is minus half the solid angle of its record-state triangles; and that the extraction is exactly unchanged by a fixed rotation, isotropic depolarisation and uniform loss but first-order sensitive to basis-dependent dephasing, polarization-dependent loss and drift between vertices, with finite-shot spread c/√S and a bias b₂/S that vanishes only for loops on the measured axes (the pre-registered claim that the extractor is unbiased is refuted). No phase was extracted from any channel model: that test — whether a channel preserves the geometry of the loop — is stated and left open.

Stage 6 (2026-10-11): the pair bridge — a two-photon polarization state read as a physics-signal interface would read it (CHSH value, teleportation fidelity, error rates, entanglement, coherence), with the effective Werner parameter each reading implies. Verified that for a Werner pair the l1-coherence in the matched product basis, the recombination visibility V_E of the heralded photon and the Werner parameter are one number, and that mixing with uniformly random accidental coincidences multiplies it by the signal fraction (theorems); that off the Werner family the readings imply different parameters in a fixed order, p_frame ≤ p_tel ≤ p_qber ≤ p_chsh, so a parameter read from the CHSH value over-states the teleportation fidelity whenever the degradation is not isotropic — which dephasing, observation and a structured environment acting on one photon never are; that the key, Bell, teleportation, entanglement and coherence tiers are nested for every pair while the position of each threshold belongs to the noise (under dephasing of a perfect pair none separates from the others); that a four-history register has a pair reading only once its histories are grouped into two parts, and that C_l1, C_re, V_E, the frustration gap, the triangle phases and the populations are identical for a product register and a maximally entangled one, since the two differ by a diagonal unitary of the register; that a CHSH value maximised over settings after tomography is biased upward at the order of its own statistical error for isotropic pairs (declaring a violation at the threshold in 92 to 95 % of trials); and that the Bell tier of a pair whose one photon meets Stage 4's environment returns for small environments (20/20 seeds at 4 modes) and not for large ones (0/20 at 16). No interface was wired: the bridge is built at the state level against the public field names, and whether the substrate's pair state is isotropic is stated and left open.

Two quantities in this repository are not grounded by this series: `coherence.current` in the schemas and the five coherence-gate thresholds. C_l1 also runs from 0 to 1; they are different quantities until a stage derives one from the other, and none does. (From Stage 2 on, a register of d histories has raw C_l1 between 0 and d − 1; the quantity that runs from 0 to 1 is C_l1/(d − 1).)

Class IV boundary applies unchanged. |A⟩ and |B⟩ are basis states of a two-level system; any Echorym meaning attached to them is an interpretation layered on top.
