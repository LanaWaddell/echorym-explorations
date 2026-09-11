# Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10
"""
echorym_qstate.py — Stage 1 of Echorym's staged path to a physically defensible
quantum world: give a history pair a real quantum state.

Scope (deliberately small):
  * A history pair (A, B) is represented by a 2x2 density matrix rho in the
    basis {|A>, |B>}. Populations on the diagonal are "state retention";
    the off-diagonal element is the ONLY place relational coherence lives.
  * Coherence is measured with the Baumgratz–Cramer–Plenio measures
    (l1-norm and relative entropy of coherence) in that basis.
  * The Echorym recombination experiment (Experiment A of the coherence
    framework) is implemented literally: apply a relative phase, recombine
    on a 50/50 beamsplitter (Hadamard), read out, scan the phase, and compute
    visibility V_E = (R_max - R_min)/(R_max + R_min).
  * Decoherence is a dephasing channel; "which-history record" is an
    environment qubit that becomes entangled with the pair and is traced out.
  * A refocusing operator is a unitary applied to the CURRENT state (it is
    not a checkpoint restore); it can undo a unitary phase kick, and it
    cannot undo tracing out an environment. That asymmetry is the point.

Falsifiable identity this module exists to check:
    for a qubit,  V_E  ==  C_l1(rho)  /  (2 * sqrt(p_A * p_B)) ... in general,
    and simply     V_E  ==  C_l1(rho)   when p_A = p_B = 1/2.

CORRECTION 2026-09-09 (appended; the two lines above are retained as the
record of what was originally written and are superseded by this note):
    For the balanced Hadamard readout implemented here, R(theta) =
    1/2 + Re(rho_AB * exp(-i theta)), so R_max + R_min = 1 for every state and
    V_E = 2|rho_AB| = C_l1(rho) FOR EVERY QUBIT STATE, not only at equal
    populations. visibility_predicted() already computes this correctly and
    the random-state check at the bottom already verifies it. The
    population-normalized formula above describes a different (two-slit,
    intensity-normalized) measurement and does not apply to this module.
    No code behaviour is changed by this note.
    Also stated explicitly: recombination_response() at one phase is a
    RESPONSE (a mixture gives 1/2, not 0); visibility() is contrast over a
    scan. Do not read one response as a visibility.
So the framework's Level-2 "visibility analogue" becomes a Level-3 quantum
coherence measure with no change of definition — only a change of substrate.

Class IV boundary: nothing here is about neural, human, or narrative state.
It is a two-level quantum system and its environment. Anything Echorym
later attaches to |A> and |B> is an interpretation layered on top.
"""
from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------------------
# Basic objects
# ---------------------------------------------------------------------------

KET_A = np.array([1.0, 0.0], dtype=complex)
KET_B = np.array([0.0, 1.0], dtype=complex)
HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)


def history_pair(p_a: float, coherence: complex) -> np.ndarray:
    """Density matrix for a history pair with population p_a on |A>,
    1-p_a on |B>, and off-diagonal element `coherence` (rho_AB).
    Raises if the result is not a valid state (positivity)."""
    p_b = 1.0 - p_a
    rho = np.array([[p_a, coherence], [np.conj(coherence), p_b]], dtype=complex)
    if abs(coherence) ** 2 > p_a * p_b + 1e-12:
        raise ValueError("|rho_AB|^2 must not exceed p_A p_B (positivity).")
    return rho


def pure_superposition(p_a: float, phase: float = 0.0) -> np.ndarray:
    """|psi> = sqrt(p_a)|A> + e^{i phase} sqrt(1-p_a)|B>, as a density matrix."""
    psi = np.sqrt(p_a) * KET_A + np.exp(1j * phase) * np.sqrt(1 - p_a) * KET_B
    return np.outer(psi, psi.conj())


def phase_gate(phi: float) -> np.ndarray:
    return np.diag([1.0, np.exp(1j * phi)]).astype(complex)


def apply_unitary(rho: np.ndarray, u: np.ndarray) -> np.ndarray:
    return u @ rho @ u.conj().T


# ---------------------------------------------------------------------------
# Coherence measures (Baumgratz, Cramer, Plenio 2014), reference basis {A, B}
# ---------------------------------------------------------------------------

def l1_coherence(rho: np.ndarray) -> float:
    off = rho - np.diag(np.diag(rho))
    return float(np.sum(np.abs(off)))


def _von_neumann_entropy(rho: np.ndarray) -> float:
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-15]
    return float(-np.sum(w * np.log2(w)))


def relative_entropy_coherence(rho: np.ndarray) -> float:
    diag = np.diag(np.diag(rho))
    return _von_neumann_entropy(diag) - _von_neumann_entropy(rho)


# ---------------------------------------------------------------------------
# Experiment A — recombination test, done literally
# ---------------------------------------------------------------------------

def recombination_response(rho: np.ndarray, phi: float) -> float:
    """Apply relative phase phi between the histories, recombine on a
    Hadamard, and report P(readout = 'A-port'). This is the response R."""
    out = apply_unitary(apply_unitary(rho, phase_gate(phi)), HADAMARD)
    return float(np.real(out[0, 0]))


def visibility(rho: np.ndarray, n_phase: int = 361) -> float:
    """V_E = (R_max - R_min)/(R_max + R_min) over a full phase scan."""
    phis = np.linspace(0, 2 * np.pi, n_phase)
    r = np.array([recombination_response(rho, phi) for phi in phis])
    return float((r.max() - r.min()) / (r.max() + r.min()))


def visibility_predicted(rho: np.ndarray) -> float:
    """Closed form for a qubit: V = 2|rho_AB| / (p_A + p_B) = 2|rho_AB|."""
    return float(2 * abs(rho[0, 1]))


# ---------------------------------------------------------------------------
# Decoherence: dephasing channel, and an explicit which-history environment
# ---------------------------------------------------------------------------

def dephase(rho: np.ndarray, gamma: float) -> np.ndarray:
    """Phase-damping channel: rho_AB -> (1-gamma) rho_AB. Populations untouched.
    gamma=0 leaves the state alone; gamma=1 is a full which-history record."""
    out = rho.copy()
    out[0, 1] *= (1 - gamma)
    out[1, 0] *= (1 - gamma)
    return out


def couple_to_environment(rho: np.ndarray, distinguishability: float) -> np.ndarray:
    """Entangle the history pair with a single environment qubit that records
    which history was taken, with overlap <e_A|e_B> = 1 - distinguishability,
    then trace the environment out. Returns the reduced 2x2 state.

    This is the which-history record of framework §10, done as physics:
    the record need not be READ by anyone; its mere existence in the
    environment suppresses recombination."""
    d = float(np.clip(distinguishability, 0.0, 1.0))
    overlap = 1.0 - d
    e_a = np.array([1.0, 0.0], dtype=complex)
    e_b = np.array([overlap, np.sqrt(1 - overlap ** 2)], dtype=complex)
    # Isometry V: |A> -> |A>|e_A>, |B> -> |B>|e_B>
    v = np.zeros((4, 2), dtype=complex)
    v[:, 0] = np.kron(KET_A, e_a)
    v[:, 1] = np.kron(KET_B, e_b)
    joint = v @ rho @ v.conj().T          # 4x4 on (system ⊗ environment)
    joint = joint.reshape(2, 2, 2, 2)      # indices (s, e, s', e')
    return np.einsum("iaja->ij", joint)    # partial trace over the environment


# ---------------------------------------------------------------------------
# Refocusing: a unitary on the current state
# ---------------------------------------------------------------------------

def refocus(rho: np.ndarray, kick_phase: float) -> np.ndarray:
    """Undo a known unitary phase kick. Acts on the evolved state; it is not
    a rollback. If the loss was a trace-out, this does nothing to |rho_AB|."""
    return apply_unitary(rho, phase_gate(-kick_phase))


# ---------------------------------------------------------------------------
# Demonstration: Experiments A, B, C of the coherence framework, on real states
# ---------------------------------------------------------------------------

def _row(label: str, rho: np.ndarray) -> None:
    print(f"{label:<44s} pA={np.real(rho[0,0]):.3f}  |rho_AB|={abs(rho[0,1]):.3f}  "
          f"C_l1={l1_coherence(rho):.3f}  C_re={relative_entropy_coherence(rho):.3f}  "
          f"V_E(scan)={visibility(rho):.3f}  V_E(pred)={visibility_predicted(rho):.3f}")


if __name__ == "__main__":
    print("Stage 1 — history pair as a qubit density matrix\n")

    # Experiment A: coherent alternatives, equal weight
    rho_coh = pure_superposition(0.5)
    _row("A. equal-weight coherent pair", rho_coh)

    # Experiment B: memory without coherence — same populations, no off-diagonal
    rho_mem = history_pair(0.5, 0.0)
    _row("B. same populations, relational structure erased", rho_mem)

    # Unequal weights: retention differs from coherence in a second way
    rho_uneq = pure_superposition(0.9)
    _row("   unequal-weight coherent pair (pA=0.9)", rho_uneq)

    print("\nDephasing sweep (Experiment D shape): V_E tracks 1-gamma exactly")
    for g in (0.0, 0.25, 0.5, 0.75, 1.0):
        _row(f"   gamma={g:.2f}", dephase(rho_coh, g))

    print("\nWhich-history environment (framework §10), never read by anyone:")
    for d in (0.0, 0.3, 0.6, 1.0):
        _row(f"   distinguishability={d:.1f}", couple_to_environment(rho_coh, d))

    print("\nExperiment C — refocusing distinguishes recoverable dephasing from loss.")
    print("An ensemble of 500 pairs, each with its own static phase kick (inhomogeneous")
    print("dephasing, the T2* situation). The ensemble-average state loses visibility;")
    print("undoing each member's kick recovers it. A traced-out record does not recover.")
    rng = np.random.default_rng(1)
    kicks = rng.standard_normal(500) * 1.2   # expected |rho_AB| after kicks = 0.5*exp(-sigma^2/2) ~ 0.24
    members = [apply_unitary(rho_coh, phase_gate(k)) for k in kicks]
    _row("   ensemble average after kicks", sum(members) / len(members))
    refocused = [refocus(m, k) for m, k in zip(members, kicks)]
    _row("   ensemble average after per-member refocus", sum(refocused) / len(refocused))
    traced = [couple_to_environment(m, 1.0) for m in members]
    _row("   ensemble after full which-history record", sum(traced) / len(traced))
    traced_ref = [refocus(t, k) for t, k in zip(traced, kicks)]
    _row("   refocus attempt on traced ensemble", sum(traced_ref) / len(traced_ref))

    # Identity check
    rng = np.random.default_rng(0)
    worst = 0.0
    for _ in range(200):
        p = rng.uniform(0.05, 0.95)
        mag = rng.uniform(0, np.sqrt(p * (1 - p)))
        rho = history_pair(p, mag * np.exp(1j * rng.uniform(0, 2 * np.pi)))
        worst = max(worst, abs(visibility(rho) - visibility_predicted(rho)))
    print(f"\nIdentity V_E(scan) == 2|rho_AB| over 200 random states: max |diff| = {worst:.2e}")
    print("At pA = pB = 1/2 this is exactly V_E == C_l1(rho).")
