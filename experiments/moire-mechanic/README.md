# Moiré mechanic falsification test

Simulation scripts behind
[`docs/design-notes/RESULT-moire-mechanic-test.md`](../../docs/design-notes/RESULT-moire-mechanic-test.md):
two-register interference, dephasing sweep, N-region scaling law, CHSH.

- `moire_test.py` — original test suite. **Its F4 block is superseded by
  `moire_test2.py`** (it dephases after the final interference).
- `moire_test2.py` — corrected F4 block.
- `moire_test4.py` — density-matrix / concurrence checks.

The RESULT note documents the corrected thresholds: Bell at 1−1/√2,
entanglement at exactly 2/3, interference at 1 — the dephased state is a
Werner state, so all three are analytic.
