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

Two quantities in this repository are not grounded by this series: `coherence.current` in the schemas and the five coherence-gate thresholds. C_l1 also runs from 0 to 1; they are different quantities until a stage derives one from the other, and none does.

Class IV boundary applies unchanged. |A⟩ and |B⟩ are basis states of a two-level system; any Echorym meaning attached to them is an interpretation layered on top.
