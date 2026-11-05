# Redaction status: none (original wording) | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-09-10
# Redaction status (Stage 2–6 blocks): cross-references edited for the public copy | Disposition: PUBLIC — approved for echorym-explorations on Lana's push, 2026-11-05
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
# Stage 2 — superposition and interference beyond one pair (d histories)
# ---------------------------------------------------------------------------
#
# One added operation: multiport recombination of a d-level register.
#
#   * A register of d histories is a d x d density matrix rho in the basis
#     {|0>, ..., |d-1>}. l1_coherence() and relative_entropy_coherence()
#     above already work on it unchanged; C_l1 now ranges over [0, d-1].
#   * Recombination generalises the Hadamard to the balanced d-port
#     (discrete Fourier) transform F_d, with one adjustable phase per history.
#     The response R is P(readout = port 0):
#
#         R(phi) = <u_phi| rho |u_phi>,   |u_phi> = d^{-1/2} sum_j e^{-i phi_j}|j>
#                = (1/d) [ 1 + sum_{j != k} e^{i(phi_j - phi_k)} rho_jk ] .
#
#   * The framework's V_E = (R_max - R_min)/(R_max + R_min) is taken over
#     the full (d-1)-dimensional phase scan. Extrema are found by monotone
#     phase-only ascent with random restarts (no grid), so that Stage 1's
#     grid-resolution residual does not grow as n^(d-1).
#
# What the operation is for. At d = 2 it reproduces Stage 1 (V_E = C_l1).
# For d >= 3 the identity becomes a pair of inequalities (theorems, checked
# below, not claims):
#
#     (T1)  R_max - 1/d  <=  C_l1(rho)/d,   equality iff the off-diagonal
#           phases are alignable by a diagonal unitary (all pure states are);
#     (T2)  V_E  <=  min(1, C_l1(rho)),     equality at d = 2 for every state.
#
# The gap  Delta = (1 + C_l1)/d - R_max >= 0  is the "frustration" of the
# register: pairwise relations that cannot all be brought into phase at once.
# It is zero iff rho is alignable (all triangle phases arg(rho_jk rho_kl rho_lj)
# vanish, for full-support states). Alignability is preserved by diagonal
# unitaries, phase damping and real-overlap records, but NOT by convex mixing:
# Stage 1's Experiment C construction at d = 3 already produces Delta > 0 (2.8).
# The identity V_E = C_l1 is lost for d >= 3 mainly on the trough side, though:
# R_min cannot reach max(0, (1 - C_l1)/d) because d >= 3 phases cannot put every
# pair in antiphase at once; that slack is present for alignable states too and
# is the larger part of V_E's shortfall against min(1, C_l1) (2.6).
#
# Class IV boundary: unchanged. |0>..|d-1> are orthogonal basis states of a
# d-level system; anything Echorym attaches to them is an interpretation.


def fourier_recombiner(d: int) -> np.ndarray:
    """Balanced d-port (discrete Fourier) transform; F_2 == HADAMARD."""
    j = np.arange(d)
    return np.exp(2j * np.pi * np.outer(j, j) / d) / np.sqrt(d)


def multiport_response(rho: np.ndarray, phases: np.ndarray) -> float:
    """Apply per-history phases, recombine on F_d, report P(port 0).
    Done literally as a circuit, so it can be checked against the closed
    form <u_phi|rho|u_phi> used by the scan below."""
    d = rho.shape[0]
    u = np.diag(np.exp(1j * np.asarray(phases, dtype=float))).astype(complex)
    out = apply_unitary(apply_unitary(rho, u), fourier_recombiner(d))
    return float(np.real(out[0, 0]))


def _quad(m: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Re(w_r^dag m w_r) for each column r of w."""
    return np.real(np.einsum("ir,ij,jr->r", w.conj(), m, w))


def _unimodular_extremum(m: np.ndarray, rng: np.random.Generator,
                         restarts: int, iters: int, tol: float) -> float:
    """max_w (1/d) w^dag m w over unimodular vectors w (|w_j| = 1), for m
    positive semidefinite.

    Two phases, both vectorised over random restarts:
      1. Jacobi phase-only ascent  w <- m w / |m w|  (elementwise). For PSD m
         this is monotone (Cauchy–Schwarz on the PSD form), so it finds a
         basin; its convergence rate can approach 1 near a zero of the
         objective, so it is used only to locate basins.
      2. Newton polish on the (d-1)-torus (phi_0 fixed as gauge), with
         backtracking; accepted only when it improves. Quadratic convergence
         takes the located basin to machine precision.
    Random restarts guard against local maxima; the all-in-phase point is
    always included. Returns the best value found."""
    d = m.shape[0]
    w = np.exp(1j * rng.uniform(0, 2 * np.pi, size=(d, restarts)))
    w[:, 0] = 1.0                                   # include the all-in-phase point
    val = _quad(m, w)
    for _ in range(iters):                          # 1. Jacobi ascent
        mw = m @ w
        mag = np.abs(mw)
        w = np.where(mag > 1e-14, mw / np.maximum(mag, 1e-300), w)
        new = _quad(m, w)
        if np.max(new - val) < tol:
            val = new
            break
        val = new
    if d > 1:                                       # 2. Newton polish
        for _ in range(30):
            mw = m @ w                              # (d, R)
            z = w.conj() * mw                       # w_j^* (m w)_j
            grad = -2.0 * np.imag(z)                # df/dphi_j, f = w^dag m w, w = e^{-i phi}
            # Hessian: H_jk = 2 Re(w_j^* m_jk w_k) (j != k), H_jj = -sum_{k != j} H_jk
            h = 2.0 * np.real(np.einsum("ir,ij,jr->ijr", w.conj(), m, w))
            idx = np.arange(d)
            h[idx, idx, :] = 0.0
            h[idx, idx, :] = -h.sum(axis=1)
            hr = np.moveaxis(h[1:, 1:, :], -1, 0)   # (R, d-1, d-1), gauge phi_0 = 0
            gr = grad[1:, :].T                      # (R, d-1)
            # Newton step for a maximum; pseudo-inverse so that a decoupled history
            # (a zero row of off-diagonals, hence a singular reduced Hessian) is
            # handled per restart instead of aborting the polish.
            step = -np.einsum("rij,rj->ri", np.linalg.pinv(hr, rcond=1e-12), gr)
            step = np.concatenate([np.zeros((step.shape[0], 1)), step], axis=1).T  # (d, R)
            improved = np.zeros(w.shape[1], dtype=bool)
            scale = 1.0
            best_w, best_val = w.copy(), val.copy()
            for _bt in range(8):                    # backtracking
                cand = w * np.exp(-1j * scale * step)
                cval = _quad(m, cand)
                better = cval > best_val + 1e-15
                best_w[:, better] = cand[:, better]
                best_val[better] = cval[better]
                improved |= better
                scale *= 0.5
            if not improved.any():
                break
            w, val = best_w, best_val
    return float(val.max() / d)


def multiport_visibility(rho: np.ndarray, seed: int = 0, restarts: int = 32,
                         iters: int = 60, tol: float = 1e-13) -> dict:
    """Full (d-1)-phase scan of the multiport recombination response.
    Returns R_max, R_min, V_E, the l1 coherence, the frustration gap
    Delta = (1 + C_l1)/d - R_max, and the T1/T2 bound values."""
    rho = np.asarray(rho, dtype=complex)
    d = rho.shape[0]
    rng = np.random.default_rng(seed)
    lam_max = float(np.linalg.eigvalsh(rho).max())
    r_max = _unimodular_extremum(rho, rng, restarts, iters, tol)
    # min of w^dag rho w  ==  d*lam_max - max of w^dag (lam_max I - rho) w
    r_min = lam_max - _unimodular_extremum(lam_max * np.eye(d) - rho, rng,
                                           restarts, iters, tol)
    r_min = max(r_min, 0.0)
    c_l1 = l1_coherence(rho)
    denom = r_max + r_min
    v_e = (r_max - r_min) / denom if denom > 1e-15 else 0.0
    return {
        "d": d,
        "R_max": r_max,
        "R_min": r_min,
        "V_E": float(v_e),
        "C_l1": c_l1,
        "C_l1_normalised": c_l1 / (d - 1) if d > 1 else 0.0,
        "gap": (1.0 + c_l1) / d - r_max,                       # T1 (peak side): >= 0
        "gap_min": r_min - max(0.0, (1.0 - c_l1) / d),         # T1' (trough side): >= 0
        "bound_T2": min(1.0, c_l1),                            # T2: V_E <= this
    }


# ---------------------------------------------------------------------------
# Stage 3 — measurement as constraint: an instrument of adjustable strength
# ---------------------------------------------------------------------------
#
# One added operation: observe(rho, strength, partition) — a which-history
# measurement on the register, of adjustable strength eta in [0, 1], that
# resolves only a chosen coarse-graining (partition) of the histories.
#
#   * Outcomes are the blocks b of a partition of {0..d-1} into m blocks
#     (default: every history its own block, m = d).
#   * POVM:   E_b = (1-eta)/m * I + eta * Pi_b   (Pi_b projects onto block b),
#             sum_b E_b = I for every eta.  eta = 0 is no measurement at all;
#             eta = 1 is the projective measurement of the block variable.
#   * Instrument (Lüders form):  K_b = sqrt(E_b), diagonal and non-negative;
#             p_b   = Tr(E_b rho);
#             rho_b = K_b rho K_b / p_b            (record read: conditional state);
#             rho'  = sum_b K_b rho K_b = sum_b p_b rho_b   (record not read).
#
# Theorems checked below (not claims):
#
#   (T3) rho'_kl = rho_kl              if k and l lie in the same block (any eta);
#        rho'_kl = f(eta, m) rho_kl    otherwise, with
#        f(eta, m) = (m-2)(1-eta)/m + (2/m) sqrt((1-eta)(1+(m-1)eta)),
#        f(eta, 2) = sqrt(1 - eta^2),  f(eta, m) = 1 - m eta^2/4 + O(eta^3),
#        and f is non-increasing in eta (f' <= 0 reduces to eta <= (m-2)/(m-1)
#        wherever the sign is not already forced; see the Stage 3 DN §2).
#        The unread instrument is therefore a dephasing channel on the
#        inter-block relations and the identity on the intra-block ones, and
#        reading the record changes no ensemble-average quantity.
#   (T4) sum_b p_b C_l1(rho_b) = C_l1(rho')  (diagonal non-negative Kraus
#        operators rotate no phase, so no outcome can cancel another), and
#        sum_b p_b C_re(rho_b) >= C_re(rho')  (convexity of C_re).
#   (T5) Information about the history variable K ~ diag(rho) carried by the
#        outcome B:  I(B;K) = H(p_B) - h_m(eta),  h_m(eta) the entropy of one row
#        (1-eta)/m + eta*delta of the outcome channel.  I is non-decreasing in
#        eta for every rho, because two such channels with parameters a, b
#        compose to one with parameter ab, so the channel at eta is a
#        degradation of the channel at any eta' > eta.  Also
#        I(B;K) = log2 d_eff(rho) - E_b log2 d_eff(rho_b),  d_eff = 2^{H(diag rho)}
#        the effective number of histories carried by the populations.  For
#        uniform populations I = log2 m - h_m(eta) = (m-1) eta^2/(2 ln 2) + O(eta^3).
#   (T6) At d = 2 the unread instrument equals Stage 1's dephase(gamma) with
#        gamma = 1 - sqrt(1-eta^2) and Stage 1's couple_to_environment(gamma), on
#        every state; the outcome distributions conditioned on |A> and |B> sit at
#        trace distance D = eta, so D^2 + (V_E'/V_E)^2 = 1 — the which-way
#        duality relation (Englert 1996), saturated by this instrument.
#
# The graded-observation ladder (glimpse -> interaction -> interrogation ->
# commitment; DN-quantum-world-register-commitment-v0_1 section 5) is, on this
# substrate, the single parameter eta at a fixed partition: information gained
# and coherence lost are both monotone in eta (T5, T3). Which VARIABLE an
# observation resolves is the partition; resolving a coarse variable leaves
# the coherence inside every block untouched at every strength (T3).
#
# Not here: no recoherence (a classical record cannot be coherently erased and
# the environment is not kept as a quantum system in this stage), no dynamics,
# no measurement in any basis other than the history basis.
# Class IV boundary: unchanged.


def coherence_factor(strength: float, m: int) -> float:
    """f(eta, m) of (T3): the factor applied to every inter-block off-diagonal
    by the unread instrument with m outcomes. f(eta, 2) = sqrt(1 - eta^2)."""
    eta = float(strength)
    return (m - 2) * (1 - eta) / m + (2.0 / m) * np.sqrt((1 - eta) * (1 + (m - 1) * eta))


def _shannon_bits(p) -> float:
    p = np.asarray(p, dtype=float)
    p = p[p > 1e-15]
    return float(-np.sum(p * np.log2(p)))


def effective_histories(rho: np.ndarray) -> float:
    """d_eff = 2^{H(diag rho)}: the effective number of histories the
    populations still carry (d for uniform populations, 1 for a single one)."""
    return float(2.0 ** _shannon_bits(np.real(np.diag(rho))))


def outcome_channel(strength: float, partition: list) -> np.ndarray:
    """p(b | k) = (1-eta)/m + eta [k in b], as an (m, d) matrix."""
    m = len(partition)
    d = sum(len(b) for b in partition)
    eta = float(strength)
    ch = np.full((m, d), (1 - eta) / m)
    for i, blk in enumerate(partition):
        ch[i, list(blk)] += eta
    return ch


def _information_bits(q: np.ndarray, ch: np.ndarray) -> float:
    """I(B;K) in bits for populations q and outcome channel ch (m, d):
    H(p_B) - sum_k q_k H(p(.|k)). Tiny negative rounding is clamped to 0."""
    p = ch @ q
    h_cond = float(sum(q[k] * _shannon_bits(ch[:, k]) for k in range(len(q))))
    info = _shannon_bits(p) - h_cond
    return float(info) if abs(info) > 1e-14 else 0.0


def observe(rho: np.ndarray, strength: float, partition: list | None = None) -> dict:
    """The Stage 3 operation. A which-history instrument of strength eta in
    [0, 1] that resolves the block variable of `partition` (a list of lists of
    history indices covering {0..d-1} exactly once; default: singletons).

    Returns the outcome probabilities p_b, the conditional (read) states rho_b,
    the unread state rho', the information I(B;K) in bits the outcome carries
    about the history variable K ~ diag(rho), the effective history counts
    before and (expected, after reading) after, and the coherence bookkeeping
    of (T4)."""
    rho = np.asarray(rho, dtype=complex)
    d = rho.shape[0]
    if partition is None:
        partition = [[k] for k in range(d)]
    flat = sorted(k for blk in partition for k in blk)
    if flat != list(range(d)):
        raise ValueError("partition must cover every history index exactly once")
    eta = float(strength)
    if not 0.0 <= eta <= 1.0:
        raise ValueError("strength must lie in [0, 1]")
    m = len(partition)
    ch = outcome_channel(eta, partition)                  # (m, d): p(b|k)
    q = np.real(np.diag(rho))                             # populations
    p = ch @ q                                            # outcome probabilities
    kraus = [np.diag(np.sqrt(ch[i])).astype(complex) for i in range(m)]
    unnorm = [k @ rho @ k for k in kraus]
    unread = sum(unnorm)
    conditional = [u / p[i] if p[i] > 1e-15 else None for i, u in enumerate(unnorm)]
    # information about K (bits): I = H(p_B) - sum_k q_k H(p(.|k))
    info = _information_bits(q, ch)
    d_eff_after = float(sum(p[i] * effective_histories(c)
                            for i, c in enumerate(conditional) if c is not None))
    cl1_cond = float(sum(p[i] * l1_coherence(c) for i, c in enumerate(conditional) if c is not None))
    cre_cond = float(sum(p[i] * relative_entropy_coherence(c)
                         for i, c in enumerate(conditional) if c is not None))
    return {
        "d": d, "m": m, "strength": eta, "partition": [list(b) for b in partition],
        "p": p, "kraus": kraus, "conditional": conditional, "unread": unread,
        "information_bits": float(info),
        "d_eff_before": effective_histories(rho), "d_eff_after_expected": d_eff_after,
        "C_l1_before": l1_coherence(rho), "C_l1_unread": l1_coherence(unread),
        "C_l1_conditional_mean": cl1_cond,
        "C_re_before": relative_entropy_coherence(rho),
        "C_re_unread": relative_entropy_coherence(unread),
        "C_re_conditional_mean": cre_cond,
        "coherence_factor": coherence_factor(eta, m),
    }


def _h_row(strength: float, m: int) -> float:
    """h_m(eta): entropy (bits) of one row of the outcome channel."""
    eta = float(strength)
    row = np.full(m, (1 - eta) / m)
    row[0] += eta
    return _shannon_bits(row)


# ---------------------------------------------------------------------------
# Stage 4 — decoherence with memory: a structured environment kept as a
# quantum system, and a Markovian control with matched decay
# ---------------------------------------------------------------------------
#
# One added operation: evolve_open(rho, bath, times, pulses) — evolve the
# register in contact with an environment that is KEPT as a quantum system
# throughout (Stages 1 and 3 traced it out or replaced it by a classical
# record), and report the reduced register state at every time.
#
#   * The environment is a bath of n independent spin-1/2 modes. Mode i has
#     its own Hamiltonian -(omega_i/2) sigma_x^(i), starts in |+> (the ground
#     state of that Hamiltonian; a general pure state is allowed), and couples
#     to the register's history variable through
#         H = sum_k |k><k| (x) H_k,   H_k = sum_i [ -(omega_i/2) sigma_x^(i) + g_i c_k sigma_z^(i) ],
#     with c_k the "charge" of history k (default c_k = (d-1)/2 - k, so that
#     at d = 2 the two branches differ by g_i sigma_z^(i), as in Stage 1's
#     environment qubit).  omega_i = 0 is a STATIC bath (each mode a frozen
#     record); omega_i > 0 gives the bath its own dynamics — memory.
#   * Pure dephasing, exactly:  rho_jk(t) = rho_jk(0) D_jk(t),
#         D_jk(t) = Tr_E[ W_j(t) rho_E W_k(t)^dag ],   W_k(t) = e^{-i H_k t},
#     populations untouched (state retention is never lost in this stage;
#     only relations are).  For a product bath D_jk factorises over modes,
#     so n = 32 modes cost 32 two-by-two problems, not one 2^32 problem; the
#     factorised form is checked against the literal joint density matrix
#     for n <= 3 (4.0).  [D_jk(t)] is the Gram matrix of the environment
#     branch states W_k|psi_E>, hence positive semidefinite (T8 below).
#   * `pulses` are register-side permutations applied at chosen times WHILE
#     the register is still coupled — an echo. The reversal k -> d-1-k
#     negates every charge, so for a static bath a single reversal at T/2
#     returns D(T) = 1 exactly (T10); for a dynamic bath it does not.
#   * The Markovian control is the pure-dephasing semigroup with the same
#     charges,  rho_jk(t) = rho_jk(0) exp(-gamma (c_j - c_k)^2 t / 2),  with
#     gamma set so that C_l1 reaches C_l1(0)/e at the same time T_2 as the
#     structured model (matched decay). It is monotone by construction (T9).
#
# Theorems checked below (not claims):
#
#   (T7)  d = 2, any state: C_l1(t)/C_l1(0) = |D(t)|, and the trace distance
#         between the evolved states of |A>+|B> and |A>-|B> is |D(t)|.  So at
#         d = 2 a revival of the coherence measure and BLP information backflow
#         are the same number, not two independent registrations.
#   (T8)  The map rho -> rho o D(t) (Hadamard product) is completely positive
#         iff [D_jk(t)] is positive semidefinite; it always is here (Gram
#         matrix).  The intermediate map from t to t' is the Hadamard product
#         with M_jk = D_jk(t')/D_jk(t), CP iff M is PSD.  At d = 2, M is PSD
#         iff |D(t')| <= |D(t)|: CP-divisibility (RHP) and BLP backflow
#         coincide.  For d >= 3 the PSD condition on M is STRICTLY stronger
#         than "no pair's modulus increases" (a 3x3 matrix with unit diagonal
#         and off-diagonals 1, 1, 0 is not PSD), so CP-divisibility can fail
#         while every pair is still decaying (4.5).
#   (T9)  The Markovian control has zero backflow and zero revival for every
#         state: exp(-gamma (c_j - c_k)^2 t/2) is monotone in t.
#   (T10) Static bath (all omega_i = 0), any state, any T: one reversal pulse
#         at T/2 gives D(T) = 1 (the branch propagators commute and are
#         swapped, so they cancel).  Stage 1's refocus acted on the reduced
#         state after the environment had been discarded and could not do
#         this; the echo acts while the environment is still coherent.
#   (T11) Independent environments multiply: D = D^(1) D^(2) elementwise.
#   (T12) Short times: D_jk(t) = 1 - (1/2) Var(H_j - H_k) t^2 + O(t^3);
#         for |+> modes Var = sum_i g_i^2 (c_j - c_k)^2.
#   (T13) One mode, d = 2, |+>:  D(t) = 1 - (2 g^2/(g^2 + omega^2)) sin^2(Omega t),
#         Omega = sqrt(g^2 + omega^2)/2;  omega = 0 gives D = cos(g t).  D is real
#         for a pair of branches with opposite charges (every pair at d = 2); for
#         |c_j| != |c_k| it is complex, and the symmetry c -> -c of |+> modes gives
#         D_12 = conj(D_01) for charges (1, 0, -1), so that register's triangle
#         phase is arg(|D_01|^2 D_02), i.e. 0 or pi.
#
# Not here: no amplitude damping (populations never change), no bath-bath
# interactions, no thermal baths (pure initial modes only), no continuum
# spectral density; the BLP measure is computed exactly at d = 2 (T7) and
# as a per-pair lower bound for d >= 3.
# Class IV boundary: unchanged.

_SX = np.array([[0, 1], [1, 0]], dtype=complex)
_SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def spin_bath(couplings, frequencies, bloch=None) -> dict:
    """n independent environment modes: couplings g_i, frequencies omega_i,
    and initial pure states given by Bloch angles (theta_i, phi_i); default
    theta = pi/2, phi = 0, i.e. |+>, the ground state of -(omega/2) sigma_x."""
    g = np.atleast_1d(np.asarray(couplings, dtype=float))
    w = np.atleast_1d(np.asarray(frequencies, dtype=float))
    if g.shape != w.shape:
        raise ValueError("couplings and frequencies must have the same length")
    n = len(g)
    if bloch is None:
        bloch = np.tile([np.pi / 2, 0.0], (n, 1))
    bloch = np.asarray(bloch, dtype=float).reshape(n, 2)
    psi = np.stack([np.cos(bloch[:, 0] / 2),
                    np.exp(1j * bloch[:, 1]) * np.sin(bloch[:, 0] / 2)], axis=1)
    return {"g": g, "omega": w, "psi": psi.astype(complex)}


def register_charges(d: int) -> np.ndarray:
    """c_k = (d-1)/2 - k: at d = 2 the branches differ by g sigma_z (Stage 1's
    environment qubit); the reversal permutation k -> d-1-k negates c."""
    return (d - 1) / 2.0 - np.arange(d)


def reversal(d: int) -> np.ndarray:
    """The echo pulse: the register permutation k -> d-1-k (X at d = 2)."""
    return np.arange(d)[::-1]


def _branch_propagate(v, lam, vec, tau):
    """Advance the branch states v[i, k, :] by e^{-i H_ik tau} using the
    stored eigen-decomposition (lam, vec) of each 2x2 branch Hamiltonian."""
    if tau == 0.0:
        return v
    ph = np.exp(-1j * lam * tau)                                  # (n, d, 2)
    c = np.einsum("ikba,ika->ikb", vec.conj(), v)                 # vec^dag v
    return np.einsum("ikab,ikb->ika", vec, ph * c)


def evolve_open(rho: np.ndarray, bath: dict, times, pulses=(), charges=None) -> dict:
    """The Stage 4 operation. Evolve the register in contact with `bath` under
    H = sum_k |k><k| (x) H_k, keeping the environment as a quantum system, and
    return the reduced register state at every time in `times` (ascending),
    the decoherence functions D_jk(t), the label map orig[t] (which original
    history each current label carries, changed only by pulses), and the
    C_l1 / C_re time series.  `pulses` is a sequence of (time, permutation)
    register-side unitaries |k> -> |perm[k]| applied while coupled."""
    rho = np.asarray(rho, dtype=complex)
    d = rho.shape[0]
    if charges is None:
        charges = register_charges(d)
    charges = np.asarray(charges, dtype=float)
    times = np.asarray(times, dtype=float)
    if np.any(np.diff(times) < 0) or times[0] < 0:
        raise ValueError("times must be ascending and non-negative")
    g, w = bath["g"], bath["omega"]
    h = ((-0.5 * w)[:, None, None, None] * _SX[None, None]
         + (g[:, None] * charges[None, :])[:, :, None, None] * _SZ[None, None])   # (n, d, 2, 2)
    lam, vec = np.linalg.eigh(h)
    events = sorted(((float(t), np.asarray(p, dtype=int)) for t, p in pulses), key=lambda e: e[0])
    v = np.repeat(bath["psi"][:, None, :], d, axis=1)             # (n, d, 2): W_k |psi_i>
    orig = np.arange(d)
    out_rho = np.zeros((len(times), d, d), dtype=complex)
    out_D = np.zeros((len(times), d, d), dtype=complex)
    out_orig = np.zeros((len(times), d), dtype=int)
    t_seg, ei = 0.0, 0
    for ti, t in enumerate(times):
        while ei < len(events) and events[ei][0] <= t:            # apply pulses up to t
            tp, perm = events[ei]
            v = _branch_propagate(v, lam, vec, tp - t_seg)
            t_seg = tp
            v_new, orig_new = np.empty_like(v), np.empty_like(orig)
            v_new[:, perm, :] = v
            orig_new[perm] = orig
            v, orig = v_new, orig_new
            ei += 1
        vt = _branch_propagate(v, lam, vec, t - t_seg)
        overlap = np.einsum("ika,ija->ijk", vt.conj(), vt)         # [i, j, k] = <psi|W_k^dag W_j|psi>_i
        dmat = np.prod(overlap, axis=0)
        out_D[ti] = dmat
        out_rho[ti] = rho[np.ix_(orig, orig)] * dmat
        out_orig[ti] = orig
    return {"times": times, "rho": out_rho, "D": out_D, "orig": out_orig, "charges": charges,
            "C_l1": np.array([l1_coherence(r) for r in out_rho]),
            "C_re": np.array([relative_entropy_coherence(r) for r in out_rho])}


def backflow(series) -> float:
    """Sum of the increases of a series: BLP information backflow when the
    series is the trace distance of a state pair (at d = 2, |D(t)| for the
    pair |A>+|B>, |A>-|B>, and this is the exact BLP measure)."""
    inc = np.diff(np.asarray(series, dtype=float))
    return float(inc[inc > 0].sum())


def revival_amplitude(series) -> float:
    """Largest rise of a series above its running minimum: 0 iff monotone
    non-increasing."""
    x = np.asarray(series, dtype=float)
    return float((x - np.minimum.accumulate(x)).max())


def divisibility_defect(D_series) -> np.ndarray:
    """For each step t -> t+1, the smallest eigenvalue of the Hermitian ratio
    matrix M_jk = D_jk(t+1)/D_jk(t) (M_jj = 1).  Negative means the
    intermediate map is not completely positive (not CP-divisible there).
    Steps at which some |D_jk(t)| is below 1e-12 are reported as nan."""
    D = np.asarray(D_series)
    out = np.full(len(D) - 1, np.nan)
    for t in range(len(D) - 1):
        if np.abs(D[t]).min() < 1e-12:
            continue
        m = D[t + 1] / D[t]
        m = 0.5 * (m + m.conj().T)
        out[t] = np.linalg.eigvalsh(m).min()
    return out


def horizon(times, series, level=np.exp(-1.0)) -> float:
    """First time the series falls to `level` times its initial value, with
    linear interpolation; inf if it never does within the grid."""
    x = np.asarray(series, dtype=float)
    thr = level * x[0]
    idx = np.where(x <= thr)[0]
    if len(idx) == 0:
        return float("inf")
    i = idx[0]
    if i == 0:
        return float(times[0])
    t0, t1, x0, x1 = times[i - 1], times[i], x[i - 1], x[i]
    return float(t0 + (t1 - t0) * (x0 - thr) / (x0 - x1))


def markovian_control(rho: np.ndarray, charges, times, t2: float) -> dict:
    """Pure-dephasing semigroup rho_jk(t) = rho_jk(0) exp(-gamma (c_j-c_k)^2 t/2)
    with gamma chosen (bisection) so that C_l1(t2) = C_l1(0)/e: the memoryless
    model with the same coherence horizon as the structured one."""
    rho = np.asarray(rho, dtype=complex)
    c = np.asarray(charges, dtype=float)
    dc2 = (c[:, None] - c[None, :]) ** 2
    mag = np.abs(rho - np.diag(np.diag(rho)))
    target = l1_coherence(rho) * np.exp(-1.0)

    def cl1(gamma):
        return float(np.sum(mag * np.exp(-gamma * dc2 * t2 / 2)))
    lo, hi = 0.0, 1.0
    while cl1(hi) > target:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if cl1(mid) > target:
            lo = mid
        else:
            hi = mid
    gamma = 0.5 * (lo + hi)
    times = np.asarray(times, dtype=float)
    D = np.exp(-gamma * dc2[None] * times[:, None, None] / 2)
    rhos = rho[None] * D
    return {"gamma": gamma, "times": times, "rho": rhos, "D": D,
            "C_l1": np.array([l1_coherence(r) for r in rhos])}


def cpmg_pulses(n_pulses: int, total_time: float, d: int) -> list:
    """n reversal pulses at (k - 1/2) T/n, k = 1..n (Carr-Purcell timing)."""
    return [((k - 0.5) * total_time / n_pulses, reversal(d)) for k in range(1, n_pulses + 1)]


def _joint_evolve(rho, bath, times, pulses=(), charges=None):
    """Literal check of evolve_open: the full register (x) environment density
    matrix on d * 2^n dimensions, evolved by the joint unitary, pulses applied
    as register-side permutations, environment traced out at each time."""
    rho = np.asarray(rho, dtype=complex)
    d = rho.shape[0]
    if charges is None:
        charges = register_charges(d)
    n = len(bath["g"])
    dim_e = 2 ** n
    i2 = np.eye(2, dtype=complex)

    def kron_all(ops):
        out = np.array([[1.0]], dtype=complex)
        for o in ops:
            out = np.kron(out, o)
        return out
    h_e = sum(kron_all([i2] * i + [-0.5 * bath["omega"][i] * _SX] + [i2] * (n - i - 1)) for i in range(n))
    b = sum(kron_all([i2] * i + [bath["g"][i] * _SZ] + [i2] * (n - i - 1)) for i in range(n))
    psi_e = kron_all([bath["psi"][i].reshape(2, 1) for i in range(n)]).reshape(-1)
    h = np.zeros((d * dim_e, d * dim_e), dtype=complex)
    for k in range(d):
        proj = np.zeros((d, d)); proj[k, k] = 1
        h += np.kron(proj, h_e + charges[k] * b)
    lam, vec = np.linalg.eigh(h)
    joint = np.kron(rho, np.outer(psi_e, psi_e.conj()))
    events = sorted(((float(t), np.asarray(p, dtype=int)) for t, p in pulses), key=lambda e: e[0])

    def u_of(tau):
        return vec @ np.diag(np.exp(-1j * lam * tau)) @ vec.conj().T
    t_seg, ei, out = 0.0, 0, []
    for t in times:
        while ei < len(events) and events[ei][0] <= t:
            tp, perm = events[ei]
            u = u_of(tp - t_seg); joint = u @ joint @ u.conj().T; t_seg = tp
            pm = np.zeros((d, d), dtype=complex)
            for k in range(d):
                pm[perm[k], k] = 1
            pj = np.kron(pm, np.eye(dim_e))
            joint = pj @ joint @ pj.conj().T
            ei += 1
        u = u_of(t - t_seg)
        jt = u @ joint @ u.conj().T
        out.append(np.einsum("iaja->ij", jt.reshape(d, dim_e, d, dim_e)))
    return np.array(out)


# ---------------------------------------------------------------------------
# Stage 5 — geometric phase: the gauge-invariant phase of a closed path of
# states, on polarization states of the six-state (BB84 + circular) set
# ---------------------------------------------------------------------------
#
# One added operation: geometric_phase(path) — the Pancharatnam / Bargmann
# geometric phase of a closed sequence of states,
#
#     gamma = -arg( <psi_0|psi_1> <psi_1|psi_2> ... <psi_{N-1}|psi_0> ),
#
# for kets, or -arg Tr(rho_0 rho_1 ... rho_{N-1}) for density matrices (the
# same number when the rho_k are pure).  An open path is closed by the final
# overlap <psi_{N-1}|psi_0>, i.e. by the geodesic from its end to its start.
# Mixed inputs are, by default, replaced by their dominant eigenvector
# ("purify"): for a qubit this normalises the Stokes vector, so isotropic
# depolarisation drops out (T18).
#
# The register here is a polarization qubit in the convention of Stage 1's
# basis: |H> = |A>, |V> = |B>, |D>,|A_pol> = (|H> ± |V>)/sqrt2, |R>,|L> =
# (|H> ± i|V>)/sqrt2.  Its Stokes (Bloch) vector is s = (<sigma_x>, <sigma_y>,
# <sigma_z>): H/V on the z axis, D/A on x, R/L on y (the Poincaré sphere with
# this labelling of axes).
#
# Theorems checked below (not claims):
#
#   (T14) Invariances, any dimension: gamma is unchanged by a rephasing of
#         every state separately (gauge), by a common unitary, and by a cyclic
#         shift of the starting point; it changes sign under reversal of the
#         path; a path retraced (a -> b -> a, <a|b> != 0) has gamma = 0; and a
#         polygon's gamma is the sum of the gammas of its fan triangles round
#         any apex not orthogonal to a vertex (mod 2 pi).  It depends
#         only on the sequence of rays, so not on how fast or with what energy
#         the path was traversed.
#   (T15) Qubit: gamma = -Omega/2 (mod 2 pi), Omega the oriented solid angle of
#         the geodesic polygon of Stokes vectors (positive when the path runs
#         anticlockwise seen from outside the sphere).  Omega/2 is computed
#         from the Stokes vectors as arg(1 + S + iT) per triangle (Van
#         Oosterom–Strackee) and, independently, as half the spherical excess.
#         Corollaries: the four BB84 states {H, V, D, A} are real kets, so
#         every loop among them with nonzero invariant has gamma in {0, pi};
#         every nonzero overlap among the six states {H, V, D, A, R, L} has a
#         phase that is a multiple of pi/4, so every such loop has gamma a
#         multiple of pi/4.
#   (T16) Cyclic evolution under any Hamiltonian H(t) = E0(t) + (omega/2) n.sigma:
#         (total phase) - (dynamical phase) = gamma (Aharonov–Anandan), and the
#         sampled-path gamma converges to it as N^-2.  An over-rotation by a
#         fraction eps of a turn changes the dynamical phase at first order
#         (-pi cos(theta) eps) and gamma only at third order,
#         -(2 pi eps)^3 sin^2(theta) cos(theta)/24; a tilt of the axis by
#         d_theta changes both at first order, by -/+ pi sin(theta) d_theta.
#   (T17) Wave plates: a retarder acting on a state whose Stokes vector is
#         perpendicular to the retarder's axis moves it along a geodesic with
#         zero dynamical phase, so the phase of a closed quarter–half–quarter
#         sequence is purely geometric and changes by 2 d_beta when the half-
#         wave plate turns by d_beta.
#   (T18) Depolarised states (Stokes length r < 1) have three different
#         "geometric phases": (E1) the purified one, exactly -Omega/2 for every
#         r > 0; (E2) the raw trace -arg Tr(rho_1 rho_2 rho_3) =
#         -atan2(r^3 T, 1 + r^2 S) with T the triple product and S the sum of
#         the pairwise dot products of the unit Stokes vectors; (E3) the
#         interferometric one for a state carried round the loop by parallel
#         transport, -atan2(r sin(Omega/2), cos(Omega/2)) with visibility
#         sqrt(cos^2(Omega/2) + r^2 sin^2(Omega/2)) (Sjöqvist et al. 2000).
#   (T19) Stage 2's triangle phases are geometric phases.  For any register
#         state rho and any purification sum_k |k>|a_k>, rho_jk = <a_k|a_j> and
#             tau_jkl = arg(rho_jk rho_kl rho_lj) = gamma(a_j -> a_k -> a_l).
#         For Stage 4's product bath, the triangle phase the environment adds
#         to a three-history register is the sum over modes of the geometric
#         phases of the modes' branch-state triangles, i.e. minus half the
#         total solid angle of those triangles on the modes' own Bloch spheres;
#         for |+> modes with charges (1, 0, -1) each triangle lies on a great
#         circle, which is T13's tau in {0, pi}.
#
#   (T20) gamma is a harmonic function of each vertex's position on the sphere
#         (the argument of a holomorphic times an antiholomorphic function of
#         the vertex's stereographic coordinate).  So noise that is isotropic
#         about a vertex produces no bias, and the bias of the finite-shot
#         Stokes estimate is b2/S with b2 = (1/2) sum_i H_ii (1 - s_i^2): it
#         comes from the anisotropy of the binomial covariance and vanishes for
#         a loop whose vertices are eigenstates of the measured axes.
#
# Not here: no non-Abelian (Wilczek–Zee) holonomy, no adiabatic theorem, no
# claim about any physical channel — the channels below are stand-ins — and
# no wiring to any signal interface.
# Class IV boundary: unchanged.

import itertools

_SY = np.array([[0, -1j], [1j, 0]], dtype=complex)

POLARIZATION = {
    "H": KET_A.copy(),
    "V": KET_B.copy(),
    "D": (KET_A + KET_B) / np.sqrt(2),
    "A": (KET_A - KET_B) / np.sqrt(2),
    "R": (KET_A + 1j * KET_B) / np.sqrt(2),
    "L": (KET_A - 1j * KET_B) / np.sqrt(2),
}


def _wrap(x):
    """Wrap an angle (or array of angles) to (-pi, pi].  Angles already inside
    the interval are returned unchanged (no rounding is introduced)."""
    x = np.asarray(x, dtype=float)
    r = x - 2 * np.pi * np.round(x / (2 * np.pi))
    return np.where(r <= -np.pi, r + 2 * np.pi, r)


def _as_projector(state: np.ndarray, purify: bool) -> np.ndarray:
    s = np.asarray(state, dtype=complex)
    if s.ndim == 1:
        s = s / np.linalg.norm(s)
        return np.outer(s, s.conj())
    if purify:
        w, v = np.linalg.eigh(s)
        top = v[:, -1]
        return np.outer(top, top.conj())
    return s


def _dominance(state: np.ndarray) -> float:
    """Gap between the two largest eigenvalues of a density matrix, relative
    to its trace (1 for a pure state, 0 where 'the dominant eigenvector' is
    not defined); inf for a ket."""
    s = np.asarray(state, dtype=complex)
    if s.ndim == 1:
        return float("inf")
    w = np.linalg.eigvalsh(s)
    return float((w[-1] - w[-2]) / max(abs(np.trace(s).real), 1e-300))


def geometric_phase(path, purify: bool = True, tol: float = 1e-12) -> dict:
    """The Stage 5 operation. `path` is a sequence of states (kets, or density
    matrices) visited in order; the path is closed by returning from the last
    state to the first along the geodesic.  Returns
        gamma     = -arg Tr(P_0 P_1 ... P_{N-1})  in (-pi, pi],
        modulus   = |Tr(P_0 ... P_{N-1})|  (for pure P_k the product of the
                    overlap moduli),
        bargmann  = the complex invariant itself,
    with P_k the projector on state k (for a density matrix: its dominant
    eigenvector if purify=True, the matrix itself if purify=False).
    gamma is nan — undefined — when the modulus is below `tol` (two consecutive
    states orthogonal: the connecting geodesic is not unique) or when, with
    purify=True, some density matrix has no dominant eigenvector (its two
    largest eigenvalues closer than `tol`, e.g. a fully depolarised qubit)."""
    path = list(path)
    if len(path) < 2:
        raise ValueError("a path needs at least two states")
    projs = [_as_projector(s, purify) for s in path]
    defined = (not purify) or all(_dominance(s) > tol for s in path)
    acc = projs[0]
    for p in projs[1:]:
        acc = acc @ p
    b = complex(np.trace(acc))
    ok = defined and abs(b) > tol
    return {"gamma": float(_wrap(-np.angle(b))) if ok else float("nan"),
            "modulus": abs(b), "bargmann": b, "n_states": len(projs)}


def stokes_vector(state: np.ndarray) -> np.ndarray:
    """(<sigma_x>, <sigma_y>, <sigma_z>) of a qubit ket or density matrix."""
    rho = _as_projector(state, purify=False)
    return np.array([np.real(np.trace(rho @ s)) for s in (_SX, _SY, _SZ)])


_APEX_CANDIDATES = np.array([v for v in itertools.product((-1.0, 0.0, 1.0), repeat=3) if any(v)])
_APEX_CANDIDATES = _APEX_CANDIDATES / np.linalg.norm(_APEX_CANDIDATES, axis=1, keepdims=True)


def half_solid_angle(vectors, tol: float = 1e-12) -> float:
    """Omega/2 (mod 2 pi, in (-pi, pi]) for the geodesic polygon through the
    given Stokes vectors (normalised here), from Stokes vectors only.  The
    polygon is cut into the triangles (p, v_k, v_{k+1}) round an auxiliary apex
    p, each contributing, in the Van Oosterom–Strackee form,
        Omega/2 = arg( 1 + a.b + b.c + c.a + i a.(b x c) ).
    The apex is the one of 26 fixed directions farthest from the antipode of
    every vertex, so that no triangle has an (ill-defined) antipodal edge at
    the apex.  Returns nan if two consecutive vertices are antipodal (the
    polygon's own edge is then not unique) or no apex keeps every triangle
    well-defined."""
    v = np.asarray(vectors, dtype=float)
    v = v / np.linalg.norm(v, axis=-1, keepdims=True)
    nxt = np.roll(v, -1, axis=0)
    if np.min(1 + np.sum(v * nxt, axis=1)) < tol:
        return float("nan")
    p = _APEX_CANDIDATES[np.argmax(np.min(1 + _APEX_CANDIDATES @ v.T, axis=1))]
    z = (1 + v @ p + np.sum(v * nxt, axis=1) + nxt @ p) + 1j * (np.cross(v, nxt) @ p)
    if np.min(np.abs(z)) < tol:
        return float("nan")
    return float(_wrap(np.sum(np.angle(z))))


def retarder(retardance: float, angle: float) -> np.ndarray:
    """SU(2) matrix of a wave plate with the given retardance whose fast axis
    is at physical angle `angle` from horizontal: a rotation of the Stokes
    vector by `retardance` about the axis (sin 2a, 0, cos 2a).  Half-wave:
    retardance = pi; quarter-wave: pi/2."""
    n_sigma = np.cos(2 * angle) * _SZ + np.sin(2 * angle) * _SX
    return np.cos(retardance / 2) * np.eye(2) - 1j * np.sin(retardance / 2) * n_sigma


def rotation(axis, angle: float) -> np.ndarray:
    """exp(-i angle n.sigma / 2): rotates Stokes vectors by `angle` about n."""
    n = np.asarray(axis, dtype=float)
    n = n / np.linalg.norm(n)
    return np.cos(angle / 2) * np.eye(2) - 1j * np.sin(angle / 2) * (n[0] * _SX + n[1] * _SY + n[2] * _SZ)


def ket_from_stokes(s) -> np.ndarray:
    """A ket whose Stokes vector is s/|s| (gauge: real first component)."""
    s = np.asarray(s, dtype=float)
    s = s / np.linalg.norm(s)
    theta, phi = np.arccos(np.clip(s[2], -1, 1)), np.arctan2(s[1], s[0])
    return np.array([np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex)


def stokes_tomography(vectors, shots: int, rng: np.random.Generator) -> np.ndarray:
    """Finite-shot estimate of Stokes vectors: for each vector and each of the
    three axes, `shots` two-outcome measurements with P(+) = (1 + s_i)/2; the
    estimate is 2 k/shots - 1.  `vectors` has shape (..., 3)."""
    v = np.asarray(vectors, dtype=float)
    k = rng.binomial(shots, np.clip((1 + v) / 2, 0, 1))
    return 2.0 * k / shots - 1.0


def _half_solid_angle_batch(v: np.ndarray) -> np.ndarray:
    """Vectorised Omega/2 for triangles: v has shape (trials, 3, 3)."""
    v = v / np.linalg.norm(v, axis=-1, keepdims=True)
    a, b, c = v[:, 0], v[:, 1], v[:, 2]
    num = np.einsum("ti,ti->t", a, np.cross(b, c))
    den = 1 + np.einsum("ti,ti->t", a, b) + np.einsum("ti,ti->t", b, c) + np.einsum("ti,ti->t", c, a)
    return np.arctan2(num, den)


def _precession_path(theta: float, n_axis, omega: float, e0: float, turns: float, n_steps: int):
    """States of a qubit that starts at polar angle theta from the axis n and
    evolves under H = e0 + (omega/2) n.sigma for `turns` periods, sampled at
    n_steps + 1 equally spaced times (first and last included).  Returns
    (kets, total phase arg<psi_0|psi_T>, dynamical phase -int <H> dt)."""
    n = np.asarray(n_axis, dtype=float)
    n = n / np.linalg.norm(n)
    perp = np.cross(n, [0.0, 0.0, 1.0])
    if np.linalg.norm(perp) < 1e-9:
        perp = np.cross(n, [1.0, 0.0, 0.0])
    perp = perp / np.linalg.norm(perp)
    s0 = np.cos(theta) * n + np.sin(theta) * perp
    psi0 = ket_from_stokes(s0)
    t_total = turns * 2 * np.pi / omega
    kets = []
    for t in np.linspace(0.0, t_total, n_steps + 1):
        kets.append(np.exp(-1j * e0 * t) * (rotation(n, omega * t) @ psi0))
    total = float(np.angle(np.vdot(psi0, kets[-1])))
    dynamical = float(-(e0 + 0.5 * omega * np.cos(theta)) * t_total)
    return kets, total, dynamical


def _mode_branch_states(bath: dict, charges, t: float) -> np.ndarray:
    """Branch states e^{-i H_ik t}|psi_i> of every mode i for every history k
    under Stage 4's Hamiltonian, computed here from the closed form of a 2x2
    exponential (independently of evolve_open).  Shape (n, d, 2)."""
    out = np.zeros((len(bath["g"]), len(charges), 2), dtype=complex)
    for i, (g, w) in enumerate(zip(bath["g"], bath["omega"])):
        for k, c in enumerate(charges):
            hx, hz = -0.5 * w, g * c
            e = np.hypot(hx, hz)
            if e < 1e-300:
                u = np.eye(2, dtype=complex)
            else:
                u = np.cos(e * t) * np.eye(2) - 1j * np.sin(e * t) * (hx * _SX + hz * _SZ) / e
            out[i, k] = u @ bath["psi"][i]
    return out


# ---------------------------------------------------------------------------
# Stage 6 — the pair bridge: a two-photon polarization state read as the
# substrate's signal interface would read it, and the effective Werner
# parameter p_eff as the coherence of that state
# ---------------------------------------------------------------------------
#
# One added operation: pair_signals(rho) — take a two-qubit (pair) density
# matrix in the product basis {|HH>, |HV>, |VH>, |VV>} (|H> = |A>, |V> = |B>
# of Stage 1 on each photon; index 2a + b) and return every state-level
# quantity a physics-signal interface of the PhysicsSignals kind reads from
# such a pair, each with the effective Werner parameter it would imply:
#
#   * the correlation matrix T_ij = Tr(rho sigma_i (x) sigma_j), the local
#     Stokes vectors, and the singular values s1 >= s2 >= s3 of T;
#   * the CHSH value maximised over settings, S = 2 sqrt(s1^2 + s2^2)
#     (Horodecki, Horodecki and Horodecki 1995);
#   * the fully entangled fraction f = max_psi <psi|rho|psi> over maximally
#     entangled psi, f = (1 + s1 + s2 - sgn(det T) s3)/4, and the optimal
#     standard-protocol teleportation fidelity F = (2 f + 1)/3;
#   * the error rates e_i = (1 - s_i)/2 in the two best matched bases and the
#     asymptotic entanglement-based key fraction r = max(0, 1 - h(e_1) - h(e_2));
#   * the concurrence (Wootters 1998) and the smallest eigenvalue of the
#     partial transpose (negative iff the pair is entangled);
#   * Stage 1's C_l1 and C_re, in the product basis as given;
#   * frame-fixed readings against the reference |Phi+> = (|HH> + |VV>)/sqrt2:
#     e_z = (1 - T_zz)/2, e_x = (1 - T_xx)/2, the overlap <Phi+|rho|Phi+>;
#   * four effective Werner parameters, which are equal for a Werner state
#     and for no state whose correlations are not isotropic:
#       p_chsh = S/(2 sqrt2),  p_qber = (s1 + s2)/2,  p_tel = (4 f - 1)/3,
#       p_frame = (4 <Phi+|rho|Phi+> - 1)/3.
#
# The Werner state is rho_W(p) = p |Phi+><Phi+| + (1 - p) 1/4.
#
# Theorems checked below (not claims):
#
#   (T21) Mixing rule.  w rho_W(p) + (1 - w) 1/4 = rho_W(w p); an isotropic
#         depolarisation of either photon to Stokes length r gives rho_W(r p).
#         With true coincidences at rate R_s and accidental coincidences at
#         rate R_b that are uniformly random in every setting, w = R_s/(R_s + R_b)
#         and p_eff = p_source R_s/(R_s + R_b)  (signal over signal-plus-background;
#         the letter S is kept below for the CHSH value).
#   (T22) Werner readouts.  For rho_W(p): T = diag(p, -p, p), no local Stokes
#         vectors, S = 2 sqrt2 p, f = (1 + 3p)/4, F = (1 + p)/2, e = (1 - p)/2
#         in every matched basis, concurrence = max(0, (3p - 1)/2), and all
#         four effective parameters equal p.  Coherence: C_l1 = p in the H/V
#         product basis (one off-diagonal pair, rho_{HH,VV} = p/2); over all
#         local product bases C_l1 ranges over [p, 3p].  Heralding: when photon
#         A is found in |D>, photon B is left in Stage 1's history pair with
#         p_A = 1/2 and rho_AB = p/2, so Stage 1's V_E = C_l1 = p.
#   (T23) Ordering, every two-qubit state:  p_frame <= p_tel <= p_qber <= p_chsh,
#         with p_tel = p_qber iff s1 = s2 = s3 and det T <= 0, and
#         p_qber = p_chsh iff s1 = s2.  Hence F <= (1 + S/(2 sqrt2))/2: a Werner
#         parameter read from the CHSH value over-states the teleportation
#         fidelity of every pair whose correlations are not isotropic.
#   (T24) Nesting, every two-qubit state:  key fraction > 0  =>  S > 2  =>
#         f > 1/2 (F > 2/3)  =>  entangled (concurrence > 0)  =>  C_l1 > 0 in
#         every product basis.  No converse holds.  A tier can therefore never
#         be held while a later one in this list is lost; where each is lost is
#         a property of the noise, not of the pair.  The key tier is the tier of
#         the one-way formula r = 1 - h(e_1) - h(e_2) above, not of key
#         distillability in general.
#   (T25) Earlier stages acting on one photon of rho_W(p).  A history-basis
#         relation factor D on photon B (Stage 1's dephase with |D| = 1 - gamma,
#         Stage 3's unread instrument with |D| = sqrt(1 - eta^2), Stage 4's bath
#         with D = D_01(t)) gives singular values (p, p|D|, p|D|):
#         S = 2 p sqrt(1 + |D|^2), f = (1 + p + 2 p|D|)/4, e_1 = (1 - p)/2,
#         e_2 = (1 - p|D|)/2, concurrence = max(0, p|D| - (1 - p)/2), C_l1 = p|D|.
#         The phase of D rotates photon B's frame and changes only the
#         frame-fixed readings: e_x = (1 - p Re D)/2.  For p = 1 and Stage 3's
#         instrument (which-history distinguishability eta on photon B),
#         (S/2)^2 + eta^2 = 2.  Stage 5's geometry-preserving class (a fixed
#         local unitary, isotropic depolarisation) leaves the singular values
#         unchanged up to the factor r.
#   (T26) A four-history register read as a pair.  Stage 2's equal-weight
#         register with amplitudes (1/2) e^{i theta_ab} has, for the
#         factorisation index = 2a + b, concurrence |sin(chi/2)| and
#         S = 2 sqrt(1 + sin^2(chi/2)), chi = theta_00 + theta_11 - theta_01 -
#         theta_10 = arg(rho_{00,01} rho_{11,10}).  chi is unchanged by local
#         diagonal unitaries and removed by a general diagonal unitary of the
#         register, so C_l1, C_re, V_E, the gap and the triangle phases of
#         Stages 1-5 are the same for the product register (chi = 0) and the
#         maximally entangled one (chi = pi).  Under Stage 2's uniform
#         dephasing gamma the chi = pi register is locally equivalent to
#         rho_W(1 - gamma): C_l1/(d - 1) = 1 - gamma, Bell tier lost at
#         gamma = 1 - 1/sqrt2, entanglement at gamma = 2/3, coherence at 1.
#
# Not here: no trust quantity; no photon-number statistics, decoy states, loss
# or link budget (the pair state is post-selected on coincidence); no wiring
# to any interface — the field names below follow the public PhysicsSignals
# interface of quantum-qkd-aero (docs/INTERFACES.md).
# Class IV boundary: unchanged.

PHI_PLUS = (np.kron(KET_A, KET_A) + np.kron(KET_B, KET_B)) / np.sqrt(2)
_PAULIS = (_SX, _SY, _SZ)
# magic basis: maximally entangled states are exactly the real unit vectors in it (up to a global phase)
_MAGIC = np.stack([
    (np.kron(KET_A, KET_A) + np.kron(KET_B, KET_B)) / np.sqrt(2),
    1j * (np.kron(KET_A, KET_A) - np.kron(KET_B, KET_B)) / np.sqrt(2),
    1j * (np.kron(KET_A, KET_B) + np.kron(KET_B, KET_A)) / np.sqrt(2),
    (np.kron(KET_A, KET_B) - np.kron(KET_B, KET_A)) / np.sqrt(2),
], axis=1)


def werner_state(p: float) -> np.ndarray:
    """rho_W(p) = p |Phi+><Phi+| + (1 - p) 1/4."""
    return p * np.outer(PHI_PLUS, PHI_PLUS.conj()) + (1 - p) * np.eye(4) / 4


def effective_werner(p_source: float, signal: float, background: float) -> float:
    """p_eff = p_source R_s/(R_s + R_b) (T21): true coincidences at rate
    R_s = signal from a Werner source, accidental coincidences at rate
    R_b = background, uniformly random in every setting."""
    return float(p_source * signal / (signal + background))


def with_accidentals(rho: np.ndarray, signal: float, background: float) -> np.ndarray:
    """The coincidence-post-selected pair state when a fraction
    R_b/(R_s + R_b) of the coincidences are accidental and uniformly random in
    every setting."""
    w = signal / (signal + background)
    return w * np.asarray(rho, dtype=complex) + (1 - w) * np.eye(4) / 4


def on_photon(rho: np.ndarray, kraus, which: int = 1, normalise: bool = False) -> np.ndarray:
    """Apply a one-photon operation given by 2x2 Kraus operators to photon
    `which` (0 = A, 1 = B) of a pair state.  normalise=True divides by the
    trace (a filter that is post-selected, such as polarization-dependent
    loss with coincidence detection)."""
    rho = np.asarray(rho, dtype=complex)
    out = np.zeros((4, 4), dtype=complex)
    for k in kraus:
        k = np.asarray(k, dtype=complex)
        big = np.kron(k, np.eye(2)) if which == 0 else np.kron(np.eye(2), k)
        out += big @ rho @ big.conj().T
    return out / np.trace(out).real if normalise else out


def relation_factor(rho: np.ndarray, factor: complex, which: int = 1) -> np.ndarray:
    """Multiply photon `which`'s H/V relation by a complex factor D (|D| <= 1):
    rho_{ab,a'b'} -> rho_{ab,a'b'} D_{bb'} with D_01 = D, D_10 = D*, D_00 = D_11 = 1.
    This is what Stage 1's dephase, Stage 3's unread instrument and Stage 4's
    bath do to one photon of a pair."""
    m = np.array([[1.0, factor], [np.conj(factor), 1.0]], dtype=complex)
    r = np.asarray(rho, dtype=complex).reshape(2, 2, 2, 2)          # (a, b, a', b')
    r = r * (m[:, None, :, None] if which == 0 else m[None, :, None, :])
    return r.reshape(4, 4)


def heralded_state(rho: np.ndarray, ket_a: np.ndarray) -> tuple:
    """Photon A is found in |ket_a>: returns (probability, photon B's
    conditional 2x2 state) — a Stage 1 history pair when ket_a is fixed."""
    a = np.asarray(ket_a, dtype=complex)
    a = a / np.linalg.norm(a)
    bra = np.kron(a.conj().reshape(1, 2), np.eye(2))                # <a| (x) 1
    sub = bra @ np.asarray(rho, dtype=complex) @ bra.conj().T
    prob = float(np.trace(sub).real)
    return prob, (sub / prob if prob > 1e-15 else sub)


def concurrence(rho: np.ndarray) -> float:
    """Wootters concurrence of a two-qubit state."""
    rho = np.asarray(rho, dtype=complex)
    yy = np.kron(_SY, _SY)
    ev = np.linalg.eigvals(rho @ yy @ rho.conj() @ yy)
    lam = np.sort(np.sqrt(np.clip(np.real(ev), 0.0, None)))[::-1]
    return float(max(0.0, lam[0] - lam[1] - lam[2] - lam[3]))


def _binary_entropy(e: float) -> float:
    e = float(np.clip(e, 0.0, 1.0))
    return _shannon_bits([e, 1.0 - e])


def pair_signals(rho: np.ndarray) -> dict:
    """The Stage 6 operation.  Read a two-qubit pair state as a physics-signal
    interface would.  Settings-optimised quantities (S, f, F, e_1, e_2, key
    fraction, concurrence, p_chsh, p_qber, p_tel) are invariant under local
    unitaries; C_l1, C_re, e_z, e_x and p_frame are readings in the frame the
    state is given in, against the reference |Phi+>.  The two margins are
    S - 2 and F - 2/3 (definitions assumed here; see the Stage 6 DN)."""
    rho = np.asarray(rho, dtype=complex)
    if rho.shape != (4, 4):
        raise ValueError("pair_signals needs a 4x4 two-qubit density matrix")
    t = np.array([[np.real(np.trace(rho @ np.kron(si, sj))) for sj in _PAULIS] for si in _PAULIS])
    stokes_a = np.array([np.real(np.trace(rho @ np.kron(s, np.eye(2)))) for s in _PAULIS])
    stokes_b = np.array([np.real(np.trace(rho @ np.kron(np.eye(2), s))) for s in _PAULIS])
    sv = np.linalg.svd(t, compute_uv=False)                         # descending
    det_t = float(np.linalg.det(t))
    sign = 0.0 if abs(det_t) <= 1e-12 * sv[0] ** 3 else float(np.sign(det_t))     # relative: |det T| = s1 s2 s3
    chsh = 2.0 * float(np.sqrt(sv[0] ** 2 + sv[1] ** 2))
    fef = 0.25 * (1.0 + sv[0] + sv[1] - sign * sv[2])
    fef_magic = float(np.linalg.eigvalsh(np.real(_MAGIC.conj().T @ rho @ _MAGIC)).max())
    f_tel = (2.0 * fef + 1.0) / 3.0
    e1, e2 = (1.0 - sv[0]) / 2.0, (1.0 - sv[1]) / 2.0
    key = max(0.0, 1.0 - _binary_entropy(e1) - _binary_entropy(e2))
    f_frame = float(np.real(PHI_PLUS.conj() @ rho @ PHI_PLUS))
    pt_min = float(np.linalg.eigvalsh(rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)).min())
    return {
        "T": t, "stokes_a": stokes_a, "stokes_b": stokes_b, "singular_values": sv, "det_T": det_t,
        "chsh": chsh, "chsh_margin": chsh - 2.0,
        "fully_entangled_fraction": fef, "fully_entangled_fraction_magic": fef_magic,
        "teleportation_fidelity": f_tel, "teleportation_margin": f_tel - 2.0 / 3.0,
        "qber_best": (e1, e2), "key_fraction": key,
        "qber_z": (1.0 - t[2, 2]) / 2.0, "qber_x": (1.0 - t[0, 0]) / 2.0,
        "concurrence": concurrence(rho), "partial_transpose_min": pt_min,
        "C_l1": l1_coherence(rho), "C_re": relative_entropy_coherence(rho),
        "phi_plus_overlap": f_frame,
        "p_chsh": chsh / (2.0 * np.sqrt(2.0)), "p_qber": float((sv[0] + sv[1]) / 2.0),
        "p_tel": (4.0 * fef - 1.0) / 3.0, "p_frame": (4.0 * f_frame - 1.0) / 3.0,
        "anisotropy": chsh / (2.0 * np.sqrt(2.0)) - (4.0 * fef - 1.0) / 3.0,
    }


def pair_tiers(sig: dict, tol: float = 1e-10) -> tuple:
    """(key, Bell, teleportation, entanglement, coherence) as booleans (T24).
    The entanglement tier is decided by the partial transpose (a negative
    eigenvalue iff entangled, for two qubits), not by the concurrence: the
    concurrence takes square roots of eigenvalues and carries rounding noise of
    order 1e-8 on states where it vanishes."""
    return (sig["key_fraction"] > tol, sig["chsh"] > 2.0 + tol,
            sig["fully_entangled_fraction"] > 0.5 + tol, sig["partial_transpose_min"] < -tol, sig["C_l1"] > tol)


def twist_register(chi: float) -> np.ndarray:
    """Equal-weight four-history register with amplitudes (1, 1, 1, e^{i chi})/2:
    Stage 2's |psi_4> at chi = 0, the controlled-phase ('twist') state of the
    two-register interference test at general chi."""
    c = np.array([1.0, 1.0, 1.0, np.exp(1j * chi)], dtype=complex) / 2.0
    return np.outer(c, c.conj())


def _threshold(fn, lo: float, hi: float, iters: int = 80) -> float:
    """Bisection for the parameter at which a boolean tier fn(x) switches
    between lo (where fn is False) and hi (where fn is True)."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if fn(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Demonstration: Experiments A, B, C of the coherence framework, on real states
# ---------------------------------------------------------------------------

def _row(label: str, rho: np.ndarray) -> None:
    print(f"{label:<44s} pA={np.real(rho[0,0]):.3f}  |rho_AB|={abs(rho[0,1]):.3f}  "
          f"C_l1={l1_coherence(rho):.3f}  C_re={relative_entropy_coherence(rho):.3f}  "
          f"V_E(scan)={visibility(rho):.3f}  V_E(pred)={visibility_predicted(rho):.3f}")


def _row_d(label: str, res: dict) -> None:
    print(f"{label:<40s} d={res['d']}  R_max={res['R_max']:.4f}  R_min={res['R_min']:.4f}  "
          f"V_E={res['V_E']:.4f}  C_l1={res['C_l1']:.4f}  C_l1/(d-1)={res['C_l1_normalised']:.4f}  "
          f"gap={res['gap']:.2e}")


def _haar_pure(d: int, rng: np.random.Generator) -> np.ndarray:
    c = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    return c / np.linalg.norm(c)


def _hs_random_state(d: int, rng: np.random.Generator) -> np.ndarray:
    """Hilbert–Schmidt (Ginibre-induced) random full-rank density matrix."""
    g = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    rho = g @ g.conj().T
    return rho / np.trace(rho).real


def _dephase_d(rho: np.ndarray, gamma: float) -> np.ndarray:
    """d-level phase damping: every off-diagonal scaled by (1-gamma).
    Coincides with dephase() at d = 2 (checked in the table)."""
    return (1 - gamma) * rho + gamma * np.diag(np.diag(rho))


def _max_triangle_phase(rho: np.ndarray) -> float:
    """max over triples of |arg(rho_jk rho_kl rho_lj)|, ignoring triples whose
    product vanishes (np.angle(-0.0) would report pi for an absent relation)."""
    d = rho.shape[0]
    best = 0.0
    for j in range(d):
        for k in range(j + 1, d):
            for l in range(k + 1, d):
                prod = rho[j, k] * rho[k, l] * rho[l, j]
                if abs(prod) > 1e-30:
                    best = max(best, abs(np.angle(prod)))
    return best


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

    # -----------------------------------------------------------------------
    # Stage 2 — d histories: multiport recombination, bound instead of identity
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("Stage 2 — d histories as a qudit; multiport recombination\n")

    # 2.0 Correctness: circuit response == closed form; F_2 == HADAMARD;
    #     _dephase_d == dephase at d = 2.
    rng = np.random.default_rng(2)
    worst_circ = 0.0
    for d in (2, 3, 4, 5):
        for _ in range(50):
            rho = _hs_random_state(d, rng)
            ph = rng.uniform(0, 2 * np.pi, d)
            u = np.exp(-1j * ph) / np.sqrt(d)
            closed = float(np.real(u.conj() @ rho @ u))
            worst_circ = max(worst_circ, abs(multiport_response(rho, ph) - closed))
    print(f"2.0 circuit response vs closed form <u|rho|u>, 200 states d=2..5: "
          f"max |diff| = {worst_circ:.2e}")
    print(f"    ||F_2 - HADAMARD||_max = {np.abs(fourier_recombiner(2) - HADAMARD).max():.2e};  "
          f"||_dephase_d - dephase||_max at d=2 (gamma=0.37) = "
          f"{np.abs(_dephase_d(rho_uneq, 0.37) - dephase(rho_uneq, 0.37)).max():.2e}")

    # 2.0b Decoupled history: d = 3 with |2> carrying population but no coherence to
    #      the pair (rho_02 = rho_12 = 0). The reduced Hessian is singular (phi_2 is
    #      irrelevant); analytic R_max = (1 + 2|rho_01|)/3, R_min = (1 - 2|rho_01|)/3,
    #      V_E = 2|rho_01| = C_l1, gap = 0.
    rho_dec = np.zeros((3, 3), dtype=complex)
    rho_dec[:2, :2] = [[0.4, 0.3 * np.exp(0.7j)], [0.3 * np.exp(-0.7j), 0.4]]
    rho_dec[2, 2] = 0.2
    res = multiport_visibility(rho_dec)
    dev = max(abs(res["R_max"] - 1.6 / 3), abs(res["R_min"] - 0.4 / 3), abs(res["V_E"] - 0.6), abs(res["gap"]))
    print(f"2.0b decoupled third history (rho_02 = rho_12 = 0): V_E={res['V_E']:.4f} (expect 0.6000 = C_l1), "
          f"max |deviation| from analytic R_max, R_min, V_E, gap = {dev:.2e}")

    # 2.1 Regression to Stage 1 at d = 2: same 200 random qubit states (seed 0).
    rng = np.random.default_rng(0)
    worst_vs_pred, worst_vs_scan = 0.0, 0.0
    for _ in range(200):
        p = rng.uniform(0.05, 0.95)
        mag = rng.uniform(0, np.sqrt(p * (1 - p)))
        rho = history_pair(p, mag * np.exp(1j * rng.uniform(0, 2 * np.pi)))
        res = multiport_visibility(rho)
        worst_vs_pred = max(worst_vs_pred, abs(res["V_E"] - visibility_predicted(rho)))
        worst_vs_scan = max(worst_vs_scan, abs(res["V_E"] - visibility(rho)))
    print(f"2.1 d=2 regression, 200 random qubit states: max |V_E(multiport) - 2|rho_AB|| = "
          f"{worst_vs_pred:.2e};  max |V_E(multiport) - V_E(Stage-1 grid)| = {worst_vs_scan:.2e}")

    # 2.2 Equal-weight pure register, d = 2..6. Expect R_max=1, R_min=0, V_E=1,
    #     C_l1 = d-1, gap = 0.
    print("\n2.2 equal-weight pure register |psi_d> = d^-1/2 sum_j |j>   (expect R_max=1, R_min=0, "
          "V_E=1, C_l1=d-1, gap=0)")
    for d in (2, 3, 4, 5, 6):
        psi = np.ones(d, dtype=complex) / np.sqrt(d)
        _row_d(f"   d={d}", multiport_visibility(np.outer(psi, psi.conj())))

    # 2.3 Uniform dephasing of |psi_d>, d = 3 and d = 5. Analytic:
    #     R_max = 1-g+g/d, R_min = g/d, V_E = (1-g)/(1-g+2g/d), C_l1 = (d-1)(1-g).
    print("\n2.3 uniform dephasing of |psi_d>: V_E vs analytic (1-g)/(1-g+2g/d); C_l1 = (d-1)(1-g).")
    print("    At d=2 this is Stage 1's V_E = 1-g = C_l1; for d>=3 V_E and C_l1 separate.")
    worst_deph = 0.0
    for d in (3, 5):
        psi = np.ones(d, dtype=complex) / np.sqrt(d)
        rho0 = np.outer(psi, psi.conj())
        for g in (0.0, 0.25, 0.5, 0.75, 0.9, 1.0):
            res = multiport_visibility(_dephase_d(rho0, g))
            v_an = (1 - g) / (1 - g + 2 * g / d) if g < 1 else 0.0
            worst_deph = max(worst_deph, abs(res["V_E"] - v_an),
                             abs(res["R_max"] - (1 - g + g / d)), abs(res["R_min"] - g / d))
            ratio = f"{res['V_E'] / res['bound_T2']:.4f}" if res["bound_T2"] > 0 else "0/0 (undefined)"
            print(f"   d={d} gamma={g:.2f}  V_E={res['V_E']:.4f}  analytic={v_an:.4f}  "
                  f"C_l1={res['C_l1']:.4f}  min(1,C_l1)={res['bound_T2']:.4f}  V_E/min(1,C_l1)={ratio}")
    print(f"    max |numeric - analytic| over the sweep (R_max, R_min, V_E) = {worst_deph:.2e}")

    # 2.4 Haar-random pure states, d = 3,4,5: R_max = (sum|c_j|)^2/d exactly,
    #     R_min = max(0, |c|_max - sum_others)^2/d, gap = 0. 20 seeds x 100 states.
    print("\n2.4 Haar-random pure states (T1 equality; analytic R_max, R_min): 20 seeds x 100 states per d")
    for d in (3, 4, 5):
        per_seed = []
        for seed in range(20):
            rng = np.random.default_rng(1000 + seed)
            worst = 0.0
            for _ in range(100):
                c = _haar_pure(d, rng)
                res = multiport_visibility(np.outer(c, c.conj()), seed=seed)
                a = np.abs(c)
                r_max_an = a.sum() ** 2 / d
                r_min_an = max(0.0, a.max() - (a.sum() - a.max())) ** 2 / d
                worst = max(worst, abs(res["R_max"] - r_max_an), abs(res["R_min"] - r_min_an),
                            abs(res["gap"]))
            per_seed.append(worst)
        per_seed = np.array(per_seed)
        print(f"   d={d}: max |deviation| per seed — mean={per_seed.mean():.2e}  sd={per_seed.std():.2e}  "
              f"max={per_seed.max():.2e}")

    # 2.5 Alignable mixed states: rho = D rho_+ D^dag, rho_+ a mixture of pure states with
    #     non-negative real amplitudes (so every off-diagonal of rho_+ is >= 0). T1 must be
    #     an equality; all triangle phases arg(rho_jk rho_kl rho_lj) must vanish.
    print("\n2.5 alignable mixed states (T1 equality expected; triangle phases = 0): 20 seeds x 100 states, d=4")
    per_seed_gap, per_seed_tri = [], []
    for seed in range(20):
        rng = np.random.default_rng(2000 + seed)
        wg, wt = 0.0, 0.0
        for _ in range(100):
            d = 4
            rho_plus = np.zeros((d, d), dtype=complex)
            for _k in range(3):
                a = np.abs(rng.standard_normal(d)); a /= np.linalg.norm(a)
                rho_plus += rng.uniform(0.2, 1.0) * np.outer(a, a)
            rho_plus /= np.trace(rho_plus).real
            dphase = np.exp(1j * rng.uniform(0, 2 * np.pi, d))
            rho = np.diag(dphase) @ rho_plus @ np.diag(dphase).conj()
            res = multiport_visibility(rho, seed=seed)
            wg = max(wg, abs(res["gap"]))
            wt = max(wt, _max_triangle_phase(rho))
        per_seed_gap.append(wg); per_seed_tri.append(wt)
    per_seed_gap = np.array(per_seed_gap); per_seed_tri = np.array(per_seed_tri)
    print(f"   |gap| per seed: mean={per_seed_gap.mean():.2e} sd={per_seed_gap.std():.2e} "
          f"max={per_seed_gap.max():.2e};  max |triangle phase| = {per_seed_tri.max():.2e} rad")

    # 2.5b Support matters for the triangle criterion: d = 4 with support graph a 4-cycle
    #      (rho_02 = rho_13 = 0), four equal moduli m = 0.1 and cycle phase pi. Every triangle
    #      product vanishes, yet the state is not alignable. Analytic: the four cycle angles
    #      must sum to pi, so the loss is 4m(1 - cos(pi/4)) and gap = (2/d)*4m(1 - cos(pi/4)).
    rho_cyc = np.eye(4, dtype=complex) / 4
    mm = 0.1
    rho_cyc[0, 1] = rho_cyc[1, 2] = rho_cyc[2, 3] = mm
    rho_cyc[3, 0] = -mm
    rho_cyc = rho_cyc + rho_cyc.conj().T - np.diag(np.diag(rho_cyc))
    assert np.linalg.eigvalsh(rho_cyc).min() > 0
    res = multiport_visibility(rho_cyc)
    gap_cyc = (2 / 4) * 4 * mm * (1 - np.cos(np.pi / 4))
    print(f"2.5b 4-cycle support, cycle phase pi (no triangles): gap={res['gap']:.6f} (expect {gap_cyc:.6f});  "
          f"max triangle phase = {_max_triangle_phase(rho_cyc):.1e} — the criterion needs full support")

    # 2.6 Generic (Hilbert–Schmidt random) mixed states, d = 3,4,5: T1 gap >= 0 and
    #     T2 V_E <= min(1, C_l1) must hold for every state (0 violations). Ensemble
    #     statistics (contingent, reported with spread): fraction with gap > 1e-9,
    #     median normalised gap d*gap/C_l1, median V_E/min(1,C_l1).
    print("\n2.6 Hilbert–Schmidt random mixed states: bounds T1, T2 (0 violations required) and ensemble "
          "statistics; 20 seeds x 200 states per d")
    print("    shortfall = 1 - V_E/min(1,C_l1); its peak-side part is what closing the gap (R_max -> (1+C_l1)/d)")
    print("    would recover; the remainder is trough-side slack (R_min above max(0,(1-C_l1)/d)).")
    for d in (3, 4, 5):
        viol_t1 = viol_t2 = n_gap0 = 0
        frac_gap, med_ngap, med_ratio, max_tri_when_gap0 = [], [], [], 0.0
        m_short, m_peak = [], []
        gap0_list = []
        for seed in range(20):
            rng = np.random.default_rng(3000 + seed)
            gaps, ngaps, ratios, shorts, peaks = [], [], [], [], []
            for _ in range(200):
                rho = _hs_random_state(d, rng)
                res = multiport_visibility(rho, seed=seed)
                if res["gap"] < -1e-9:
                    viol_t1 += 1
                if res["V_E"] > res["bound_T2"] + 1e-9:
                    viol_t2 += 1
                gaps.append(res["gap"])
                ngaps.append(d * res["gap"] / res["C_l1"])
                ratios.append(res["V_E"] / res["bound_T2"])
                r_al = (1.0 + res["C_l1"]) / d                        # aligned peak
                v_al = (r_al - res["R_min"]) / (r_al + res["R_min"])
                shorts.append(1.0 - res["V_E"] / res["bound_T2"])
                peaks.append((v_al - res["V_E"]) / res["bound_T2"])
                if res["gap"] <= 1e-9:
                    n_gap0 += 1
                    gap0_list.append((res["gap"], _max_triangle_phase(rho)))
                    max_tri_when_gap0 = max(max_tri_when_gap0, _max_triangle_phase(rho))
            gaps = np.array(gaps)
            frac_gap.append(np.mean(gaps > 1e-9))
            med_ngap.append(np.median(ngaps))
            med_ratio.append(np.median(ratios))
            m_short.append(np.mean(shorts))
            m_peak.append(np.mean(peaks))
        frac_gap, med_ngap, med_ratio, m_short, m_peak = map(
            np.array, (frac_gap, med_ngap, med_ratio, m_short, m_peak))
        print(f"   d={d}: T1 violations={viol_t1}  T2 violations={viol_t2}  |  "
              f"frac(gap>1e-9)={frac_gap.mean():.3f}±{frac_gap.std():.3f}  "
              f"median d*gap/C_l1={med_ngap.mean():.4f}±{med_ngap.std():.4f}  "
              f"median V_E/min(1,C_l1)={med_ratio.mean():.4f}±{med_ratio.std():.4f}")
        print(f"         mean shortfall={m_short.mean():.4f}±{m_short.std():.4f}  of which peak-side (gap) part="
              f"{m_peak.mean():.4f}±{m_peak.std():.4f}  ({100*m_peak.mean()/m_short.mean():.1f}%);  "
              f"states with gap<=1e-9: {n_gap0} of 4000, max|tri phase| among them: {max_tri_when_gap0:.1e} rad"
              + ("" if not gap0_list else "  [" + ", ".join(f"gap={g:.1e},tau={t:.1e}" for g, t in gap0_list) + "]"))

    # 2.6b Quadratic onset of the gap at d = 3. For a full-support d=3 state whose single
    #      triangle phase tau = arg(rho_01 rho_12 rho_20) is small,
    #          gap = tau^2 / ( d * (1/|rho_01| + 1/|rho_12| + 1/|rho_20|) ) + O(tau^4).
    #      Built from an alignable rho_+ with one off-diagonal rotated by tau = 1e-3.
    print("\n2.6b quadratic onset of the gap, d=3, tau=1e-3: gap vs tau^2/(d*sum 1/|rho_jk|); 20 seeds x 50 states")
    rel = []
    tau = 1e-3
    for seed in range(20):
        rng = np.random.default_rng(4000 + seed)
        worst_rel = 0.0
        for _ in range(50):
            d = 3
            rho_plus = np.zeros((d, d), dtype=complex)
            for _k in range(3):
                a = np.abs(rng.standard_normal(d)) + 0.05; a /= np.linalg.norm(a)
                rho_plus += rng.uniform(0.2, 1.0) * np.outer(a, a)
            rho_plus /= np.trace(rho_plus).real
            rho_plus = 0.9 * rho_plus + 0.1 * np.eye(d) / d     # keep full rank, off-diagonals still >= 0
            rho = rho_plus.copy()
            rho[0, 1] *= np.exp(1j * tau); rho[1, 0] = np.conj(rho[0, 1])
            assert np.linalg.eigvalsh(rho).min() > 0, "perturbed state left the state space"
            res = multiport_visibility(rho, seed=seed)
            pred = tau ** 2 / (d * sum(1.0 / abs(rho[j, k]) for j, k in ((0, 1), (1, 2), (2, 0))))
            worst_rel = max(worst_rel, abs(res["gap"] - pred) / pred)
        rel.append(worst_rel)
    rel = np.array(rel)
    print(f"   max relative error per seed: mean={rel.mean():.2e}  sd={rel.std():.2e}  max={rel.max():.2e}  "
          f"(expected O(tau^2) ~ 1e-6)")

    # 2.7 Optimiser adequacy at d = 3: dense grid (360 x 360 over the two free phases)
    #     must never beat the ascent by more than the grid's own resolution.
    print("\n2.7 optimiser adequacy, d=3: dense 360x360 grid vs random-restart ascent, 40 HS-random states")
    rng = np.random.default_rng(7)
    grid = np.linspace(0, 2 * np.pi, 360, endpoint=False)
    p1, p2 = np.meshgrid(grid, grid, indexing="ij")
    w = np.stack([np.ones_like(p1), np.exp(-1j * p1), np.exp(-1j * p2)], axis=-1) / np.sqrt(3)  # (360,360,3)
    excess_max, excess_min = -np.inf, -np.inf
    for _ in range(40):
        rho = _hs_random_state(3, rng)
        r = np.real(np.einsum("abi,ij,abj->ab", w.conj(), rho, w))
        res = multiport_visibility(rho)
        excess_max = max(excess_max, r.max() - res["R_max"])   # grid beating ascent => positive
        excess_min = max(excess_min, res["R_min"] - r.min())
    print(f"   max(grid R_max - ascent R_max) = {excess_max:+.2e};  "
          f"max(ascent R_min - grid R_min) = {excess_min:+.2e}   (negative or ~0 means ascent is at least as good)")

    # 2.8 Non-alignable states arise from convex mixing alone. Diagonal unitaries, phase
    #     damping and real-overlap records each preserve alignability, but a mixture of
    #     alignable states need not be alignable. Stage 1's Experiment C construction
    #     (ensemble of members with different static phase kicks) at d = 3 is the example.
    #     (a) Two members of |psi_3> with kicks 0 and (0, 4pi/5, 8pi/5): rho_jk = (1/6)(1 + e^{i(k_j - k_k)}),
    #         so tau = arg prod = pi exactly, |rho_jk| = (2cos(2pi/5), 2cos(2pi/5), 2cos(pi/5))/6,
    #         C_l1 = (2/3)(2cos(2pi/5) + cos(pi/5)). With the two equal moduli m and the third M,
    #         the constrained maximum on the symmetric line alpha = beta is
    #         S* = 2 m cos a* - M cos 2a*, cos a* = m/(2M), giving gap = (2/3)(2m + M - S*).
    #     (b) N = 500 members with independent Gaussian kicks (sigma = 1.2) per history, 20 seeds:
    #         tau and gap are generically nonzero at finite N and vanish only as N -> infinity
    #         (independent kicks factorise: E e^{i(k_j - k_k)} = E e^{i k_j} E e^{-i k_k}).
    print("\n2.8 non-alignable states from convex mixing (Stage 1 Experiment C construction at d=3)")
    psi3 = np.ones(3, dtype=complex) / np.sqrt(3)
    rho0 = np.outer(psi3, psi3.conj())
    kick = np.diag(np.exp(1j * np.array([0.0, 4 * np.pi / 5, 8 * np.pi / 5])))
    rho_pent = 0.5 * (rho0 + kick @ rho0 @ kick.conj().T)
    res = multiport_visibility(rho_pent)
    m, M = 2 * np.cos(2 * np.pi / 5) / 6, 2 * np.cos(np.pi / 5) / 6
    ca = m / (2 * M)
    s_star = 2 * m * ca - M * (2 * ca ** 2 - 1)
    gap_an = (2 / 3) * (2 * m + M - s_star)
    c_an = 2 * (2 * m + M)
    print(f"   (a) two-member pentagon mixture: tau={_max_triangle_phase(rho_pent):.6f} (expect pi={np.pi:.6f});  "
          f"C_l1={res['C_l1']:.6f} (expect {c_an:.6f});  gap={res['gap']:.6f} (expect {gap_an:.6f});  "
          f"V_E={res['V_E']:.4f}  min(1,C_l1)={res['bound_T2']:.4f}")
    taus, gaps_c = [], []
    for seed in range(20):
        rng = np.random.default_rng(5000 + seed)
        kicks = rng.standard_normal((500, 3)) * 1.2
        rho_ens = sum(np.diag(np.exp(1j * k)) @ rho0 @ np.diag(np.exp(-1j * k)) for k in kicks) / 500
        res = multiport_visibility(rho_ens, seed=seed)
        taus.append(_max_triangle_phase(rho_ens)); gaps_c.append(res["gap"])
    taus, gaps_c = np.array(taus), np.array(gaps_c)
    print(f"   (b) 500-member independent-kick ensemble, 20 seeds: |tau| mean={taus.mean():.4f} sd={taus.std():.4f} "
          f"max={taus.max():.4f} rad;  gap mean={gaps_c.mean():.2e} sd={gaps_c.std():.2e} max={gaps_c.max():.2e} "
          f"(expect both -> 0 as N -> inf; nonzero at finite N)")

    print("\nStage 2 summary: at d=2 the multiport operation reproduces Stage 1's identity V_E = C_l1;")
    print("for d>=3 the identity is replaced by the theorems T1 (R_max - 1/d <= C_l1/d) and")
    print("T2 (V_E <= min(1, C_l1)), both checked above with zero violations, and V_E saturates")
    print("while C_l1/(d-1) does not — V_E is a bound-side witness of coherence for d>=3, not a measure of it.")

    # -----------------------------------------------------------------------
    # Stage 3 — measurement as constraint: instrument of adjustable strength
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("Stage 3 — measurement as constraint; a which-history instrument of strength eta\n")

    def _random_partition(d: int, rng: np.random.Generator) -> list:
        m = int(rng.integers(1, d + 1))
        labels = rng.integers(0, m, size=d)
        labels[rng.permutation(d)[:m]] = np.arange(m)      # every block non-empty
        return [list(np.where(labels == i)[0]) for i in range(m)]

    # 3.0 Correctness of the instrument: POVM completeness, p_b = Tr(E_b rho),
    #     sum_b p_b rho_b == rho', trace preservation, positivity of conditional states.
    rng = np.random.default_rng(3)
    w_povm = w_p = w_avg = w_tr = 0.0
    min_eig = np.inf
    n_tests = 0
    for d in (2, 3, 4, 5):
        for _ in range(50):
            rho = _hs_random_state(d, rng)
            part = _random_partition(d, rng)
            eta = rng.uniform(0, 1)
            res = observe(rho, eta, part)
            povm = sum(k.conj().T @ k for k in res["kraus"])
            w_povm = max(w_povm, np.abs(povm - np.eye(d)).max())
            ch = outcome_channel(eta, part)
            w_p = max(w_p, np.abs(res["p"] - ch @ np.real(np.diag(rho))).max())
            avg = sum(res["p"][i] * c for i, c in enumerate(res["conditional"]))
            w_avg = max(w_avg, np.abs(avg - res["unread"]).max())
            w_tr = max(w_tr, abs(np.trace(res["unread"]).real - 1.0),
                       max(abs(np.trace(c).real - 1.0) for c in res["conditional"]))
            min_eig = min(min_eig, min(np.linalg.eigvalsh(c).min() for c in res["conditional"]))
            n_tests += 1
    print(f"3.0 instrument correctness, {n_tests} (state, partition, eta) triples d=2..5, seed 3: "
          f"max ||sum K^dag K - I|| = {w_povm:.2e};  max |p_b - Tr(E_b rho)| = {w_p:.2e};  "
          f"max ||sum_b p_b rho_b - rho'|| = {w_avg:.2e};  max |Tr - 1| = {w_tr:.2e};  "
          f"min eigenvalue of any conditional state = {min_eig:+.2e}")

    # 3.1 (T3): rho'_kl = rho_kl inside a block, f(eta, m) rho_kl across blocks.
    rng = np.random.default_rng(31)
    w_t3 = 0.0
    for d in (2, 3, 4, 5, 6):
        for _ in range(40):
            rho = _hs_random_state(d, rng)
            part = _random_partition(d, rng)
            eta = rng.uniform(0, 1)
            res = observe(rho, eta, part)
            block_of = np.empty(d, dtype=int)
            for i, blk in enumerate(part):
                block_of[blk] = i
            same = block_of[:, None] == block_of[None, :]
            factor = np.where(same, 1.0, coherence_factor(eta, len(part)))
            w_t3 = max(w_t3, np.abs(res["unread"] - factor * rho).max())
    print(f"3.1 (T3) rho' == rho with inter-block elements scaled by f(eta,m), 200 triples d=2..6, seed 31: "
          f"max |deviation| = {w_t3:.2e}")

    # 3.2 (T6) d = 2: unread instrument == dephase(gamma) == couple_to_environment(gamma),
    #     gamma = 1 - sqrt(1 - eta^2); D = eta; D^2 + (V_E'/V_E)^2 = 1.
    rng = np.random.default_rng(32)
    w_deph = w_env = w_dual = w_D = 0.0
    for _ in range(200):
        p_a = rng.uniform(0.05, 0.95)
        mag = rng.uniform(0, np.sqrt(p_a * (1 - p_a)))
        rho = history_pair(p_a, mag * np.exp(1j * rng.uniform(0, 2 * np.pi)))
        eta = rng.uniform(0, 1)
        res = observe(rho, eta)
        gam = 1 - np.sqrt(1 - eta ** 2)
        w_deph = max(w_deph, np.abs(res["unread"] - dephase(rho, gam)).max())
        w_env = max(w_env, np.abs(res["unread"] - couple_to_environment(rho, gam)).max())
        ch = outcome_channel(eta, [[0], [1]])
        dist = 0.5 * np.abs(ch[:, 0] - ch[:, 1]).sum()
        w_D = max(w_D, abs(dist - eta))
        v_ratio = visibility_predicted(res["unread"]) / visibility_predicted(rho) if mag > 1e-6 else np.sqrt(1 - eta ** 2)
        w_dual = max(w_dual, abs(dist ** 2 + v_ratio ** 2 - 1.0))
    print(f"3.2 (T6) d=2, 200 random states and strengths, seed 32: max ||rho' - dephase(1-sqrt(1-eta^2))|| = {w_deph:.2e};  "
          f"max ||rho' - couple_to_environment(same)|| = {w_env:.2e};  max |D - eta| = {w_D:.2e};  "
          f"max |D^2 + (V_E'/V_E)^2 - 1| = {w_dual:.2e}")

    # 3.3 The ladder at d = 2 on the equal-weight coherent pair: one parameter eta.
    #     Analytic: I = 1 - h2((1+eta)/2) bits; C_l1' = V_E' = sqrt(1-eta^2); conditional
    #     |rho_01| = sqrt(1-eta^2)/2 with populations (1±eta)/2 (pure); E[d_eff] = 2^{h2((1+eta)/2)}.
    print("\n3.3 ladder at d=2, equal-weight coherent pair (Experiment A state):  I = information about "
          "which history (bits);")
    print("    C_l1' and V_E' after an unread observation; |rho_01|_A of the conditional state on outcome A; "
          "E[d_eff] expected effective histories after reading")
    print("    analytic: I = 1 - h2((1+eta)/2);  C_l1' = V_E' = sqrt(1-eta^2);  |rho_01|_A = sqrt(1-eta^2)/2;  "
          "E[d_eff] = 2^h2((1+eta)/2)")
    w_33 = 0.0
    for eta in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0):
        res = observe(rho_coh, eta)
        h2 = _shannon_bits([(1 + eta) / 2, (1 - eta) / 2])
        i_an, c_an, deff_an = 1 - h2, np.sqrt(1 - eta ** 2), 2 ** h2
        v_num = multiport_visibility(res["unread"])["V_E"]
        cond_a = abs(res["conditional"][0][0, 1])
        w_33 = max(w_33, abs(res["information_bits"] - i_an), abs(res["C_l1_unread"] - c_an),
                   abs(v_num - c_an), abs(cond_a - c_an / 2), abs(res["d_eff_after_expected"] - deff_an))
        print(f"   eta={eta:.2f}  I={res['information_bits']:.4f} ({i_an:.4f})  C_l1'={res['C_l1_unread']:.4f} "
              f"({c_an:.4f})  V_E'={v_num:.4f}  |rho_01|_A={cond_a:.4f} ({c_an/2:.4f})  "
              f"p_A={res['p'][0]:.4f}  E[d_eff]={res['d_eff_after_expected']:.4f} ({deff_an:.4f})  "
              f"C_re'={res['C_re_unread']:.4f}")
    res9 = observe(rho_uneq, 1.0)
    print(f"    max |numeric - analytic| over the table = {w_33:.2e};  unequal pair (pA=0.9) at eta=1: "
          f"I={res9['information_bits']:.4f} bits (= H(0.9,0.1) = {_shannon_bits([0.9, 0.1]):.4f}), C_l1'={res9['C_l1_unread']:.4f}")

    # 3.4 Which variable is resolved: d = 4, |psi_4>, coarse partition {0,1},{2,3} against the
    #     singleton partition. Coarse: intra-block |rho'_01| = 1/4 at every eta, inter-block
    #     1/4 sqrt(1-eta^2), C_l1' = 1 + 2 sqrt(1-eta^2), I = 1 - h2((1+eta)/2), E[d_eff] =
    #     2^{1 + h2((1+eta)/2)}, and V_E' = 1 for every eta (R_max = (1+f)/2, R_min = 0: the
    #     vector (1,-1,1,-1)/2 is orthogonal to the support of rho').
    #     Singleton: C_l1' = 3 f(eta,4), I = 2 - h4(eta), E[d_eff] = 2^{h4(eta)}.
    print("\n3.4 which variable is resolved: d=4, |psi_4>, coarse partition {0,1},{2,3} vs singletons")
    print("    coarse analytic: |rho'_01| = 0.25 (untouched), |rho'_02| = 0.25 sqrt(1-eta^2), C_l1' = 1 + 2 sqrt(1-eta^2), "
          "I = 1 - h2((1+eta)/2), E[d_eff] = 2^(1+h2), V_E' = 1")
    print("    singleton analytic: C_l1' = 3 f(eta,4), I = 2 - h4(eta), E[d_eff] = 2^h4(eta)")
    psi4 = np.ones(4, dtype=complex) / 2
    rho4 = np.outer(psi4, psi4.conj())
    w_34 = 0.0
    for eta in (0.0, 0.25, 0.5, 0.75, 1.0):
        rc = observe(rho4, eta, [[0, 1], [2, 3]])
        rs = observe(rho4, eta)
        h2 = _shannon_bits([(1 + eta) / 2, (1 - eta) / 2])
        h4 = _h_row(eta, 4)
        vc = multiport_visibility(rc["unread"])["V_E"]
        vs = multiport_visibility(rs["unread"])["V_E"]
        s = np.sqrt(1 - eta ** 2)
        w_34 = max(w_34, abs(abs(rc["unread"][0, 1]) - 0.25), abs(abs(rc["unread"][0, 2]) - 0.25 * s),
                   abs(rc["C_l1_unread"] - (1 + 2 * s)), abs(rc["information_bits"] - (1 - h2)),
                   abs(rc["d_eff_after_expected"] - 2 ** (1 + h2)), abs(vc - 1.0),
                   abs(rs["C_l1_unread"] - 3 * coherence_factor(eta, 4)), abs(rs["information_bits"] - (2 - h4)),
                   abs(rs["d_eff_after_expected"] - 2 ** h4))
        print(f"   eta={eta:.2f}  coarse: |rho'_01|={abs(rc['unread'][0,1]):.4f} |rho'_02|={abs(rc['unread'][0,2]):.4f} "
              f"C_l1'={rc['C_l1_unread']:.4f} I={rc['information_bits']:.4f} E[d_eff]={rc['d_eff_after_expected']:.4f} "
              f"V_E'={vc:.4f}  |  singleton: C_l1'={rs['C_l1_unread']:.4f} I={rs['information_bits']:.4f} "
              f"E[d_eff]={rs['d_eff_after_expected']:.4f} V_E'={vs:.4f}")
    print(f"    max |numeric - analytic| over the table = {w_34:.2e}")

    # 3.5 Closed forms and small-eta laws, uniform populations, singleton partition, d = 3, 4, 5:
    #     I = log2 d - h_d(eta) (exact); 1 - f = d eta^2/4 + O(eta^3), I = (d-1) eta^2/(2 ln 2) + O(eta^3).
    print("\n3.5 closed forms (uniform populations, singletons): I vs log2 d - h_d(eta) over an eta grid; "
          "small-eta laws at eta = 1e-3")
    for d in (3, 4, 5):
        psi = np.ones(d, dtype=complex) / np.sqrt(d)
        rho = np.outer(psi, psi.conj())
        w_i = max(abs(observe(rho, e)["information_bits"] - (np.log2(d) - _h_row(e, d)))
                  for e in np.linspace(0, 1, 101))
        e = 1e-3
        r_f = (1 - coherence_factor(e, d)) / (d * e ** 2 / 4) - 1
        r_i = observe(rho, e)["information_bits"] / ((d - 1) * e ** 2 / (2 * np.log(2))) - 1
        print(f"   d={d}: max |I - (log2 d - h_d)| over 101 eta values = {w_i:.2e};  "
              f"(1-f)/(d eta^2/4) - 1 = {r_f:+.2e};  I/((d-1) eta^2/(2 ln2)) - 1 = {r_i:+.2e}   (expect O(eta) ~ 1e-3)")

    # 3.6 Monotonicity (T5, T3): I(eta) non-decreasing for random populations and partitions;
    #     f(eta, m) non-increasing (both theorems). Checked on a 201-point grid; the channel-composition
    #     identity (1-ab)/m + ab*delta is checked directly.
    rng = np.random.default_rng(36)
    grid = np.linspace(0, 1, 201)
    worst_inc_I, worst_inc_f, w_comp = -np.inf, -np.inf, 0.0
    for d in (2, 3, 4, 5):
        for _ in range(25):
            q = rng.dirichlet(np.ones(d))
            rho = np.diag(q).astype(complex)
            part = _random_partition(d, rng)
            vals = np.array([observe(rho, e, part)["information_bits"] for e in grid])
            worst_inc_I = max(worst_inc_I, -np.diff(vals).min())      # largest decrease
            a, b = rng.uniform(0, 1, 2)
            m = len(part)
            # composition on the block alphabet: (1-a)/m + a delta after (1-b)/m + b delta
            ca = (1 - a) / m * np.ones((m, m)) + a * np.eye(m)
            cb = (1 - b) / m * np.ones((m, m)) + b * np.eye(m)
            cab = (1 - a * b) / m * np.ones((m, m)) + a * b * np.eye(m)
            w_comp = max(w_comp, np.abs(ca @ cb - cab).max())
    for m in (2, 3, 4, 5, 6, 8):
        f = np.array([coherence_factor(e, m) for e in grid])
        worst_inc_f = max(worst_inc_f, np.diff(f).max())               # largest increase
    print(f"\n3.6 monotonicity: largest decrease of I(eta) over 100 random (populations, partition) d=2..5, "
          f"201-point grid = {worst_inc_I:+.2e} (theorem: <= 0);  largest increase of f(eta,m), m=2..8 = "
          f"{worst_inc_f:+.2e} (theorem: <= 0);  channel composition ||C_a C_b - C_ab||_max = {w_comp:.2e}")

    # 3.7 (T4) coherence bookkeeping: sum_b p_b C_l1(rho_b) == C_l1(rho');  sum_b p_b C_re(rho_b) >= C_re(rho').
    rng = np.random.default_rng(37)
    w_l1, min_re = 0.0, np.inf
    for d in (2, 3, 4, 5):
        for _ in range(50):
            rho = _hs_random_state(d, rng)
            res = observe(rho, rng.uniform(0, 1), _random_partition(d, rng))
            w_l1 = max(w_l1, abs(res["C_l1_conditional_mean"] - res["C_l1_unread"]))
            min_re = min(min_re, res["C_re_conditional_mean"] - res["C_re_unread"])
    print(f"3.7 (T4) 200 triples, seed 37: max |sum p_b C_l1(rho_b) - C_l1(rho')| = {w_l1:.2e};  "
          f"min [sum p_b C_re(rho_b) - C_re(rho')] = {min_re:+.2e} (theorem: >= 0)")

    # 3.8 FC-1 "a glimpse is the cheapest bit" (pre-registered; see the DN for the verdict):
    #     information per unit coherence lost, g_q(eta) = I_q(eta) / (1 - f(eta, d)) (singleton
    #     partition; the factor C_l1 cancels), is non-increasing in eta. Endpoints in closed
    #     form for EVERY population vector q:  g(0+) = 2(d-1)/(d ln 2)  (the chi-square
    #     approximation of I is population-independent at leading order), g(1) = H(q) <= log2 d.
    #     So the endpoint inequality g(1) <= g(0+) holds for all q iff log2 d <= 2(d-1)/(d ln 2),
    #     i.e. for d <= 4 only. Contingent part (full monotonicity, general q): checked over
    #     20 seeds x 200 Dirichlet(1) population vectors per d on a 50-point eta grid.
    print("\n3.8 FC-1 information per unit coherence lost, g(eta) = I/(1-f): non-increasing in eta?  "
          "20 seeds x 200 random population vectors per d, 50-point eta grid in [0.02, 1]")
    print("    endpoints, any q: g(0+) = 2(d-1)/(d ln 2);  g(1) = H(q) <= log2 d  =>  g(1) <= g(0+) for all q iff d <= 4")
    grid = np.linspace(0.02, 1.0, 50)
    for d in (2, 3, 4, 5):
        one_minus_f = np.array([1 - coherence_factor(e, d) for e in grid])
        chans = [outcome_channel(e, [[k] for k in range(d)]) for e in grid]
        frac_mono, frac_end, worst_up = [], [], []
        g0 = 2 * (d - 1) / (d * np.log(2))
        for seed in range(20):
            rng = np.random.default_rng(3800 + seed)
            n_mono, n_end, wu = 0, 0, -np.inf
            for _ in range(200):
                q = rng.dirichlet(np.ones(d))
                g = np.array([_information_bits(q, ch) for ch in chans]) / one_minus_f
                inc = np.diff(g).max()
                wu = max(wu, inc)
                n_mono += inc <= 1e-9
                n_end += _shannon_bits(q) <= g0
            frac_mono.append(n_mono / 200); frac_end.append(n_end / 200); worst_up.append(wu)
        frac_mono, frac_end, worst_up = map(np.array, (frac_mono, frac_end, worst_up))
        print(f"   d={d}: fraction monotone on the grid = {frac_mono.mean():.4f}±{frac_mono.std():.4f}  "
              f"largest increase seen = {worst_up.max():+.2e};  fraction with g(1) <= g(0+) = "
              f"{frac_end.mean():.4f}±{frac_end.std():.4f};  g(0+)={g0:.4f}  uniform g(1)=log2 d={np.log2(d):.4f}")

    # 3.9 FC-2 what the witness V_E reports after an unread singleton observation. Since rho'
    #     is uniform dephasing with 1 - gamma = f, R_max' = 1/d + f(R_max - 1/d) and R_min' =
    #     1/d + f(R_min - 1/d) exactly (no re-optimisation), so
    #         V_E'/V_E = f S / (2(1-f)/d + f S),   S = R_max + R_min,
    #     which exceeds the coherence ratio C_l1'/C_l1 = f iff S > 2/d. d = 2 has S = 1 = 2/d
    #     (equality, Stage 1). For d >= 3 the sign is state-dependent: HS-random states, d=3,4,
    #     eta = 0.5, 20 seeds x 50 states; and the pentagon mixture of 2.8a (S < 2/d).
    #     The closed-form transform is also checked against a re-optimised V_E(rho').
    print("\n3.9 FC-2 witness vs measure after an unread observation (singletons, eta=0.5): "
          "V_E'/V_E vs C_l1'/C_l1 = f;  20 seeds x 50 HS-random states")
    for d in (3, 4):
        f = coherence_factor(0.5, d)
        frac_over, med_ratio, w_re = [], [], 0.0
        for seed in range(20):
            rng = np.random.default_rng(3900 + seed)
            over, ratios = 0, []
            for i in range(50):
                rho = _hs_random_state(d, rng)
                r = multiport_visibility(rho, seed=seed)
                s = r["R_max"] + r["R_min"]
                v_after = f * (r["R_max"] - r["R_min"]) / (2 * (1 - f) / d + f * s)
                ratios.append((v_after / r["V_E"]) / f)
                over += s > 2 / d
                if i < 5:
                    v_re = multiport_visibility(observe(rho, 0.5)["unread"], seed=seed)["V_E"]
                    w_re = max(w_re, abs(v_re - v_after))
            frac_over.append(over / 50); med_ratio.append(np.median(ratios))
        frac_over, med_ratio = np.array(frac_over), np.array(med_ratio)
        print(f"   d={d}: f={f:.4f};  fraction with S > 2/d (witness ratio above f) = {frac_over.mean():.3f}±{frac_over.std():.3f};  "
              f"median (V_E'/V_E)/f = {med_ratio.mean():.4f}±{med_ratio.std():.4f};  "
              f"max |re-optimised V_E' - closed form| (100 states) = {w_re:.2e}")
    r = multiport_visibility(rho_pent)
    f = coherence_factor(0.5, 3)
    s = r["R_max"] + r["R_min"]
    v_after = f * (r["R_max"] - r["R_min"]) / (2 * (1 - f) / 3 + f * s)
    print(f"   pentagon mixture (2.8a): S={s:.4f} < 2/3;  V_E'/V_E = {v_after / r['V_E']:.4f} < f = {f:.4f}: "
          f"the witness over-reports the loss there")

    print("\nStage 3 summary: an observation of strength eta that resolves the block variable of a")
    print("partition leaves every intra-block relation untouched and scales every inter-block")
    print("relation by f(eta,m) (T3); reading the record changes no ensemble-average quantity;")
    print("information gained and coherence lost are both monotone in eta (T5, T3), so the")
    print("graded-observation ladder is one parameter at fixed partition; at d=2 the unread")
    print("instrument is Stage 1's dephasing/record channel and saturates D^2 + V^2 = 1 (T6).")

    # -----------------------------------------------------------------------
    # Stage 4 — decoherence with memory: a structured environment kept coherent
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("Stage 4 — decoherence with memory; a structured environment kept as a quantum system\n")
    T_H, N_T = 20.0, 2001                       # horizon (units of 1/g_0) and grid
    t_grid = np.linspace(0.0, T_H, N_T)

    def _random_bath(n: int, rng: np.random.Generator, static: bool = False, bloch=None) -> dict:
        g = rng.uniform(0.5, 1.5, n)
        w = np.zeros(n) if static else rng.uniform(0.5, 1.5, n)
        return spin_bath(g, w, bloch=bloch)

    # 4.0 Correctness: the factorised operation against the literal joint density matrix
    #     (n = 3 modes, d = 2..4, tilted initial modes, one pulse), seed 4; the Gram property of
    #     D(t) (T8: min eigenvalue >= 0); trace and populations; (T11) product of two baths.
    rng = np.random.default_rng(4)
    w_joint = w_tr = w_pop = w_prod = 0.0
    min_gram = np.inf
    for d in (2, 3, 4):
        for _ in range(5):
            rho = _hs_random_state(d, rng)
            bath = _random_bath(3, rng, bloch=rng.uniform(0, np.pi, (3, 2)))
            tt = np.linspace(0, 6, 13)
            perm = reversal(d) if rng.uniform() < 0.5 else rng.permutation(d)
            pulses = [(2.3, perm)]
            res = evolve_open(rho, bath, tt, pulses=pulses)
            lit = _joint_evolve(rho, bath, tt, pulses=pulses)
            w_joint = max(w_joint, np.abs(res["rho"] - lit).max())
            w_tr = max(w_tr, np.abs(np.trace(res["rho"], axis1=1, axis2=2) - 1).max())
            pop = np.real(np.diagonal(res["rho"], axis1=1, axis2=2))
            w_pop = max(w_pop, np.abs(pop - np.real(np.diag(rho))[res["orig"]]).max())
            min_gram = min(min_gram, min(np.linalg.eigvalsh(D).min() for D in res["D"]))
            b1, b2 = _random_bath(2, rng), _random_bath(2, rng)
            b12 = spin_bath(np.concatenate([b1["g"], b2["g"]]), np.concatenate([b1["omega"], b2["omega"]]))
            r1, r2, r12 = (evolve_open(rho, b, tt) for b in (b1, b2, b12))
            w_prod = max(w_prod, np.abs(r1["D"] * r2["D"] - r12["D"]).max())
    print(f"4.0 factorised operation vs literal joint evolution, 15 (state, bath, pulse) triples d=2..4, n=3, seed 4: "
          f"max |deviation| = {w_joint:.2e};  max |Tr - 1| = {w_tr:.2e};  max |population change| = {w_pop:.2e};  "
          f"min eigenvalue of [D_jk(t)] = {min_gram:+.2e} (T8: >= 0);  (T11) max ||D^(1) D^(2) - D^(12)|| = {w_prod:.2e}")

    # 4.1 Contact with Stage 1 and closed forms. d = 2: at every t the reduced state equals Stage 1's
    #     couple_to_environment with distinguishability 1 - |D(t)| after the phase arg D(t) is
    #     removed. (T13) one mode: D = 1 - (2g^2/(g^2+w^2)) sin^2(Omega t), Omega = sqrt(g^2+w^2)/2;
    #     static, D = cos(g t). (T12) short-time law D = 1 - sum g_i^2 t^2/2 + O(t^4).
    rng = np.random.default_rng(41)
    w_s1 = 0.0
    for _ in range(50):
        p_a = rng.uniform(0.05, 0.95)
        mag = rng.uniform(0, np.sqrt(p_a * (1 - p_a)))
        rho = history_pair(p_a, mag * np.exp(1j * rng.uniform(0, 2 * np.pi)))
        bath = _random_bath(4, rng, bloch=rng.uniform(0, np.pi, (4, 2)))
        res = evolve_open(rho, bath, np.linspace(0, 8, 41))
        for r_t, D in zip(res["rho"], res["D"]):
            rot = apply_unitary(rho, phase_gate(np.angle(D[1, 0])))
            w_s1 = max(w_s1, np.abs(r_t - couple_to_environment(rot, 1 - abs(D[0, 1]))).max())
    g1, w1 = 0.7, 1.3
    res = evolve_open(rho_coh, spin_bath([g1], [w1]), t_grid)
    om = np.sqrt(g1 ** 2 + w1 ** 2) / 2
    d_an = 1 - 2 * g1 ** 2 / (g1 ** 2 + w1 ** 2) * np.sin(om * t_grid) ** 2
    w_t13 = np.abs(res["D"][:, 0, 1] - d_an).max()
    res_s = evolve_open(rho_coh, spin_bath([g1], [0.0]), t_grid)
    w_t13s = np.abs(res_s["D"][:, 0, 1] - np.cos(g1 * t_grid)).max()
    bath8 = _random_bath(8, np.random.default_rng(42))
    ts = np.array([0.0, 1e-2])
    d_short = evolve_open(rho_coh, bath8, ts)["D"][1, 0, 1].real
    rel_short = (1 - d_short) / (np.sum(bath8["g"] ** 2) * ts[1] ** 2 / 2) - 1
    print(f"4.1 d=2 contact with Stage 1: max ||rho(t) - couple_to_environment(phase-rotated rho, 1-|D(t)|)|| over "
          f"50 states x 41 times, seed 41 = {w_s1:.2e};  (T13) one mode g=0.7 w=1.3: max |D - closed form| = {w_t13:.2e}, "
          f"static: max |D - cos(g t)| = {w_t13s:.2e};  (T12) short-time law at t=1e-2, n=8: "
          f"(1-D)/(sum g^2 t^2/2) - 1 = {rel_short:+.2e} (expect O(t^2) ~ 1e-4)")

    # 4.2 The revival test. Equal-weight pair, n = 8 modes with
    #     g_i, w_i ~ U(0.5, 1.5), horizon T = 20, 2001 points, 20 seeds. Structured: T_2 (1/e time of
    #     C_l1), revival amplitude R (largest rise of C_l1/C_l1(0) above its running minimum), BLP
    #     backflow N (sum of increases of |D|; exact at d = 2 by T7). Control: the matched semigroup,
    #     R = N = 0 (T9). Also the time of the largest revival and the number of rises > 0.02.
    print("\n4.2 FC-1 revival test, d=2 equal-weight pair, n=8 modes, T=20, 20 seeds (4200-4219):")
    print("    structured bath vs Markovian control matched at T_2; R = revival amplitude of C_l1/C_l1(0), N = BLP backflow")
    t2s, amps, bfs, n_rev, t_rev, c_amps, c_bfs, gammas, gaps = [], [], [], [], [], [], [], [], []
    eps = 0.02
    for seed in range(20):
        rng = np.random.default_rng(4200 + seed)
        bath = _random_bath(8, rng)
        res = evolve_open(rho_coh, bath, t_grid)
        x = res["C_l1"] / res["C_l1"][0]
        t2 = horizon(t_grid, x)
        ctrl = markovian_control(rho_coh, res["charges"], t_grid, t2)
        t2s.append(t2); amps.append(revival_amplitude(x)); bfs.append(backflow(np.abs(res["D"][:, 0, 1])))
        c_amps.append(revival_amplitude(ctrl["C_l1"])); c_bfs.append(backflow(np.abs(ctrl["D"][:, 0, 1])))
        gammas.append(ctrl["gamma"])
        rise = x - np.minimum.accumulate(x)
        t_rev.append(t_grid[np.argmax(rise)])
        # count separate rises above eps
        above = rise > eps
        n_rev.append(int(np.sum(above[1:] & ~above[:-1]) + (1 if above[0] else 0)))
        if seed == 0:
            res0, ctrl0, x0 = res, ctrl, x
    t2s, amps, bfs, c_amps, c_bfs, gammas = map(np.array, (t2s, amps, bfs, c_amps, c_bfs, gammas))
    n_rev, t_rev = np.array(n_rev), np.array(t_rev)
    print(f"   T_2 = {t2s.mean():.4f} ± {t2s.std():.4f} (Gaussian estimate sqrt(2/sum g^2) ~ {np.mean([np.sqrt(2/np.sum(_random_bath(8, np.random.default_rng(4200+s))['g']**2)) for s in range(20)]):.4f});  "
          f"control gamma = {gammas.mean():.4f} ± {gammas.std():.4f} (= 2/T_2 at d=2, since (Delta c)^2 = 1)")
    print(f"   structured: R = {amps.mean():.4f} ± {amps.std():.4f} (min {amps.min():.4f}, max {amps.max():.4f});  "
          f"N = {bfs.mean():.4f} ± {bfs.std():.4f};  rises > {eps}: {n_rev.mean():.2f} ± {n_rev.std():.2f} per seed, "
          f"seeds with R > {eps}: {int(np.sum(amps > eps))}/20;  time of largest revival = {t_rev.mean():.2f} ± {t_rev.std():.2f}")
    print(f"   control:    R = {c_amps.max():.2e} (T9: 0);  N = {c_bfs.max():.2e} (T9: 0)")
    print("   seed 4200, C_l1(t)/C_l1(0): structured | control")
    for tq in (0.0, 0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 20.0):
        i = int(round(tq / T_H * (N_T - 1)))
        print(f"      t={tq:5.2f}   {x0[i]:.4f} | {ctrl0['C_l1'][i]:.4f}")

    # 4.3 (T7) at d = 2: C_l1(t)/C_l1(0) == |D(t)| == trace distance of the |A>±|B> pair, for
    #     random states and baths, seed 43; hence revival and backflow are one number at d = 2.
    rng = np.random.default_rng(43)
    w_t7 = 0.0
    for _ in range(20):
        p_a = rng.uniform(0.05, 0.95)
        mag = rng.uniform(0.05, np.sqrt(p_a * (1 - p_a)))
        rho = history_pair(p_a, mag * np.exp(1j * rng.uniform(0, 2 * np.pi)))
        bath = _random_bath(6, rng, bloch=rng.uniform(0, np.pi, (6, 2)))
        tt = np.linspace(0, 10, 101)
        res = evolve_open(rho, bath, tt)
        plus, minus = evolve_open(pure_superposition(0.5, 0.0), bath, tt), evolve_open(pure_superposition(0.5, np.pi), bath, tt)
        for i in range(len(tt)):
            td = 0.5 * np.abs(np.linalg.eigvalsh(plus["rho"][i] - minus["rho"][i])).sum()
            w_t7 = max(w_t7, abs(res["C_l1"][i] / res["C_l1"][0] - abs(res["D"][i, 0, 1])), abs(td - abs(res["D"][i, 0, 1])))
    print(f"\n4.3 (T7) d=2, 20 (state, bath) pairs x 101 times, seed 43: max |C_l1(t)/C_l1(0) - |D(t)|| and "
          f"max |trace distance(|A>+|B>, |A>-|B>) - |D(t)|| = {w_t7:.2e}")

    # 4.4 FC-2 masking at d = 3: equal-weight qutrit, charges (1, 0, -1), n = 8 modes, 20 seeds.
    #     Theorem direction: every rise of C_l1(t) is accompanied by a rise of some |D_jk| (0 violations
    #     required). Contingent direction: every pair-backflow episode (a rise of |D_jk| above eps)
    #     is visible as a rise of C_l1 somewhere inside it. Reported: fraction of pair episodes visible,
    #     and the total pair backflow that occurs while C_l1 is falling (masked backflow).
    print("\n4.4 FC-2 masking at d=3, equal-weight qutrit, charges (1,0,-1), n=8, 20 seeds (4400-4419):")
    psi3 = np.ones(3, dtype=complex) / np.sqrt(3)
    rho3 = np.outer(psi3, psi3.conj())
    viol_thm = 0
    frac_vis, masked, total_bf, n_epi = [], [], [], []
    for seed in range(20):
        rng = np.random.default_rng(4400 + seed)
        bath = _random_bath(8, rng)
        res = evolve_open(rho3, bath, t_grid)
        dc = np.diff(res["C_l1"])
        mods = [np.abs(res["D"][:, j, k]) for j, k in ((0, 1), (0, 2), (1, 2))]
        dm = np.array([np.diff(m) for m in mods])                  # (3, N_T-1)
        viol_thm += int(np.sum((dc > 1e-12) & ~np.any(dm > 0, axis=0)))
        vis, tot, mk, ne = 0, 0.0, 0.0, 0
        for m, dmm in zip(mods, dm):
            tot += dmm[dmm > 0].sum()
            mk += dmm[(dmm > 0) & (dc <= 0)].sum()
            rise = m - np.minimum.accumulate(m)
            above = rise > eps
            starts = np.where(above[1:] & ~above[:-1])[0] + 1
            for s in starts:                                         # episode: from the running-min point to s
                e = s
                while e + 1 < len(above) and above[e + 1]:
                    e += 1
                ne += 1
                vis += int(np.any(dc[max(s - 1, 0):e] > 1e-12))
        frac_vis.append(vis / ne if ne else np.nan); masked.append(mk / tot if tot > 0 else 0.0)
        total_bf.append(tot); n_epi.append(ne)
    frac_vis, masked, total_bf, n_epi = map(np.array, (frac_vis, masked, total_bf, n_epi))
    print(f"   theorem direction (C_l1 rise without any |D_jk| rise): {viol_thm} violations;  "
          f"pair-backflow episodes > {eps}: {n_epi.mean():.1f} ± {n_epi.std():.1f} per seed, fraction visible as a C_l1 rise = "
          f"{np.nanmean(frac_vis):.3f} ± {np.nanstd(frac_vis):.3f};  fraction of total pair backflow that occurs while C_l1 is falling = "
          f"{masked.mean():.3f} ± {masked.std():.3f}")

    # 4.4b The environment as a source of frustration (Stage 2's gap). The equal-weight qutrit is
    #      alignable (gap 0). Under |+> modes with charges (1,0,-1), D_12 = conj(D_01) and D_02 is real
    #      (T13), so tau(t) = arg(|D_01|^2 D_02) is 0 or pi — a sign change of the Delta c = 2 pair;
    #      under tilted modes the register acquires a continuous triangle phase tau(t) = arg(D_01 D_12 D_20).
    #      Reported: max_t tau and max_t gap over the horizon.
    rng = np.random.default_rng(44)
    bath_p = _random_bath(4, rng)
    bath_t = _random_bath(4, rng, bloch=rng.uniform(0.3, np.pi - 0.3, (4, 2)))
    tt = np.linspace(0, 10, 201)
    for label, bath in (("|+> modes", bath_p), ("tilted modes", bath_t)):
        res = evolve_open(rho3, bath, tt)
        taus_t = np.array([_max_triangle_phase(r) for r in res["rho"]])
        gaps_t = np.array([multiport_visibility(r, seed=0)["gap"] for r in res["rho"][::10]])
        strict = np.mean((taus_t > 1e-6) & (taus_t < np.pi - 1e-6))
        print(f"   4.4b {label:<13s}: max_t |tau(t)| = {taus_t.max():.4f} rad;  max_t gap = {gaps_t.max():.4f};  "
              f"fraction of times with |tau| > 1e-6: {np.mean(taus_t > 1e-6):.3f}, strictly between 0 and pi: {strict:.3f}  "
              f"(initial state alignable, gap 0)")

    # 4.5 (T8) CP-divisibility. d = 2: sign of the ratio-matrix defect agrees with the sign of the
    #     modulus change at every step (theorem). d = 3 (|+> modes; D_02 real, D_01 = conj(D_12)): number of steps that are
    #     not CP-divisible while NO pair modulus increases, and the onset time of non-divisibility
    #     against the first pair backflow; 20 seeds (4500-4519).
    rng = np.random.default_rng(45)
    disagree = 0
    for _ in range(10):
        bath = _random_bath(6, rng, bloch=rng.uniform(0, np.pi, (6, 2)))
        res = evolve_open(rho_coh, bath, np.linspace(0, 10, 501))
        defect = divisibility_defect(res["D"])
        dmod = np.diff(np.abs(res["D"][:, 0, 1]))
        ok = ~np.isnan(defect)
        disagree += int(np.sum((defect[ok] < -1e-12) != (dmod[ok] > 1e-12)))
    n_hidden, t_onset, t_bf, worst_def = [], [], [], []
    for seed in range(20):
        rng = np.random.default_rng(4500 + seed)
        bath = _random_bath(8, rng)
        res = evolve_open(rho3, bath, t_grid)
        defect = divisibility_defect(res["D"])
        dm = np.array([np.diff(np.abs(res["D"][:, j, k])) for j, k in ((0, 1), (0, 2), (1, 2))])
        any_up = np.any(dm > 1e-12, axis=0)
        ok = ~np.isnan(defect)
        n_hidden.append(int(np.sum(ok & (defect < -1e-9) & ~any_up)))
        i_on = np.where(ok & (defect < -1e-9))[0]
        i_bf = np.where(any_up)[0]
        t_onset.append(t_grid[i_on[0]] if len(i_on) else np.inf)
        t_bf.append(t_grid[i_bf[0]] if len(i_bf) else np.inf)
        pre = ok & (t_grid[:-1] < 0.3)                             # well before the first zero crossing
        worst_def.append(defect[pre].min())
    n_hidden, t_onset, t_bf, worst_def = map(np.array, (n_hidden, t_onset, t_bf, worst_def))
    print(f"\n4.5 (T8) d=2: steps where the CP-divisibility defect and the modulus change disagree in sign, "
          f"10 baths x 500 steps, seed 45: {disagree} (theorem: 0)")
    print(f"   d=3 (|+> modes): steps not CP-divisible while no pair modulus rises = {n_hidden.mean():.1f} ± {n_hidden.std():.1f} "
          f"of 2000 per seed (seeds with any: {int(np.sum(n_hidden > 0))}/20);  onset of non-divisibility t = {t_onset.mean():.4f} ± {t_onset.std():.4f} "
          f"vs first pair backflow t = {t_bf.mean():.4f} ± {t_bf.std():.4f};  onset earlier in {int(np.sum(t_onset < t_bf))}/20 seeds;  "
          f"most negative defect for t < 0.3 = {worst_def.mean():+.3e} ± {worst_def.std():.1e} (step dt = {T_H / (N_T - 1):.3f}; "
          f"leading order the rate matrix is a Gaussian kernel in the charges and M is PSD; the t^4 terms make the Delta c = 2 pair "
          f"decay faster than the kernel allows)")

    # 4.6 FC-4 bath-size trend: revival amplitude R (d=2, equal-weight pair, T=20) for n = 1..32,
    #     20 seeds each (4600 + n*100 + seed).
    print("\n4.6 FC-4 bath-size trend, d=2, revival amplitude R over T=20, 20 seeds per n:")
    for n in (1, 2, 4, 8, 16, 32):
        rr, tt2 = [], []
        for seed in range(20):
            rng = np.random.default_rng(4600 + 100 * n + seed)
            res = evolve_open(rho_coh, _random_bath(n, rng), t_grid)
            x = res["C_l1"] / res["C_l1"][0]
            rr.append(revival_amplitude(x)); tt2.append(horizon(t_grid, x))
        rr, tt2 = np.array(rr), np.array(tt2)
        t2_txt = f"{np.mean(tt2[np.isfinite(tt2)]):.3f}" if np.any(np.isfinite(tt2)) else "inf"
        print(f"   n={n:2d}: R = {rr.mean():.4f} ± {rr.std():.4f}  (min {rr.min():.4f}, max {rr.max():.4f});  "
              f"T_2 = {t2_txt} ({int(np.sum(~np.isfinite(tt2)))} seeds never reach 1/e)")

    # 4.7 Echo. (T10) static bath, one reversal at T/2: D(T) = 1 for random states, baths and T
    #     (seed 47). Dynamic bath (n=8, seeds 4700-4719): T_recohere (first T at which a single echo at
    #     T/2 leaves C_l1(T)/C_l1(0) <= 1/e) against T_2, and FC-3: retained coherence at T = 20 under
    #     n_p reversal pulses at Carr-Purcell timing, n_p = 0..128 — pre-registered: non-decreasing in
    #     n_p once the spacing T/n_p is below pi/(2 Omega_max), 2 Omega_i = sqrt(g_i^2 + w_i^2) the dressed
    #     mode frequency of (T13); here sqrt(2 x 1.5^2) = 2.12, spacing < 1.48, i.e. n_p >= 14 (16 is
    #     the next tested value).
    rng = np.random.default_rng(47)
    w_t10 = 0.0
    for _ in range(20):
        d = int(rng.integers(2, 5))
        rho = _hs_random_state(d, rng)
        n = int(rng.integers(1, 7))
        bath = _random_bath(n, rng, static=True, bloch=rng.uniform(0, np.pi, (n, 2)))
        tot = rng.uniform(1, 30)
        res = evolve_open(rho, bath, np.array([tot]), pulses=[(tot / 2, reversal(d))])
        w_t10 = max(w_t10, np.abs(res["D"][0] - 1).max())
    t_rec, t_2 = [], []
    t_scan = np.linspace(0.05, T_H, 400)
    for seed in range(20):
        rng = np.random.default_rng(4700 + seed)
        bath = _random_bath(8, rng)
        x_echo = np.array([evolve_open(rho_coh, bath, np.array([tot]), pulses=[(tot / 2, reversal(2))])["C_l1"][0]
                           for tot in t_scan])
        t_rec.append(horizon(np.concatenate([[0.0], t_scan]), np.concatenate([[1.0], x_echo])))
        t_2.append(horizon(t_grid, evolve_open(rho_coh, bath, t_grid)["C_l1"]))
    t_rec, t_2 = np.array(t_rec), np.array(t_2)
    print(f"\n4.7 (T10) static bath, one reversal at T/2, 20 random (d, state, bath, T), seed 47: max |D(T) - 1| = {w_t10:.2e}")
    print(f"   dynamic bath n=8, single echo at T/2: T_recohere = {t_rec.mean():.3f} ± {t_rec.std():.3f}  vs  "
          f"T_2 = {t_2.mean():.3f} ± {t_2.std():.3f};  ratio = {np.mean(t_rec / t_2):.2f} ± {np.std(t_rec / t_2):.2f}")
    print("   FC-3 retained C_l1(T=20)/C_l1(0) under n_p Carr-Purcell reversal pulses (mean ± sd over 20 seeds):")
    n_list = (0, 1, 2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 128)
    table = np.zeros((20, len(n_list)))
    for seed in range(20):
        rng = np.random.default_rng(4700 + seed)
        bath = _random_bath(8, rng)
        for j, n_p in enumerate(n_list):
            pulses = cpmg_pulses(n_p, T_H, 2) if n_p else []
            table[seed, j] = evolve_open(rho_coh, bath, np.array([T_H]), pulses=pulses)["C_l1"][0]
    for j, n_p in enumerate(n_list):
        print(f"      n_p={n_p:3d} (spacing {T_H / n_p if n_p else np.inf:6.3f}): {table[:, j].mean():.4f} ± {table[:, j].std():.4f}")
    above = [j for j, n_p in enumerate(n_list) if n_p >= 16]
    mono = np.all(np.diff(table[:, above], axis=1) >= -1e-9, axis=1)
    mono_all = np.all(np.diff(table, axis=1) >= -1e-9, axis=1)
    print(f"      seeds monotone non-decreasing for n_p >= 16: {int(mono.sum())}/20 (smallest step change there = "
          f"{np.diff(table[:, above], axis=1).min():+.2e});  over the whole range n_p = 0..128: {int(mono_all.sum())}/20")
    # single-frequency bath: the resonance. All omega_i = 1, g_i ~ U(0.5,1.5), n = 8, 20 seeds.
    print("   single-frequency bath (all omega_i = 1, g_i ~ U(0.5,1.5)): retained C_l1(T=20)/C_l1(0) vs n_p; dressed frequencies "
          "sqrt(g^2+1) in [1.1, 1.8], so a dip is expected for spacing in [1.7, 2.8] (n_p 7-12)")
    n_list2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64)
    table2 = np.zeros((20, len(n_list2)))
    for seed in range(20):
        rng = np.random.default_rng(4750 + seed)
        bath = spin_bath(rng.uniform(0.5, 1.5, 8), np.ones(8))
        for j, n_p in enumerate(n_list2):
            pulses = cpmg_pulses(n_p, T_H, 2) if n_p else []
            table2[seed, j] = evolve_open(rho_coh, bath, np.array([T_H]), pulses=pulses)["C_l1"][0]
    print("      " + "  ".join(f"n_p={n_p}: {table2[:, j].mean():.3f}±{table2[:, j].std():.3f}" for j, n_p in enumerate(n_list2)))

    print("\nStage 4 summary: with the environment kept as a quantum system the register's coherence is")
    print("rho_jk(t) = rho_jk(0) D_jk(t) exactly; for a structured bath |D| revives and the matched")
    print("Markovian control cannot (T9); at d=2 the coherence series, the BLP trace distance and |D(t)|")
    print("are one series (T7) and CP-divisibility fails exactly where it rises (T8); for d>=3 a pair's backflow can be masked in")
    print("C_l1 and CP-divisibility can fail before any pair revives; a register-side reversal while")
    print("coupled refocuses a static bath exactly (T10) and a dynamic one only partly.")

    # -----------------------------------------------------------------------
    # Stage 5 — geometric phase on polarization states
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("Stage 5 — geometric phase; the gauge-invariant phase of a closed path of polarization states\n")
    P = POLARIZATION

    def _random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
        q, r = np.linalg.qr(rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)))
        return q * (np.diag(r) / np.abs(np.diag(r)))

    def _gp(path, **kw) -> float:
        return geometric_phase(path, **kw)["gamma"]

    def _random_unit_vectors(shape, rng: np.random.Generator) -> np.ndarray:
        v = rng.standard_normal(tuple(shape) + (3,))
        return v / np.linalg.norm(v, axis=-1, keepdims=True)

    # 5.0 (T14) invariances of the operation, any dimension: 200 random closed paths of Haar kets,
    #     d = 2..5, N = 3..8, seed 5. Deviations are of wrapped phase differences.
    rng = np.random.default_rng(5)
    w_gauge = w_unit = w_cyc = w_rev = w_proj = w_retrace = w_fan = w_apex = 0.0
    for d in (2, 3, 4, 5):
        for _ in range(50):
            n_pts = int(rng.integers(3, 9))
            path = [_haar_pure(d, rng) for _ in range(n_pts)]
            g0 = _gp(path)
            w_gauge = max(w_gauge, abs(_wrap(_gp([np.exp(1j * rng.uniform(0, 2 * np.pi)) * k for k in path]) - g0)))
            u = _random_unitary(d, rng)
            w_unit = max(w_unit, abs(_wrap(_gp([u @ k for k in path]) - g0)))
            sh = int(rng.integers(1, n_pts))
            w_cyc = max(w_cyc, abs(_wrap(_gp(path[sh:] + path[:sh]) - g0)))
            w_rev = max(w_rev, abs(_wrap(_gp(path[::-1]) + g0)))
            w_proj = max(w_proj, abs(_wrap(_gp([np.outer(k, k.conj()) for k in path], purify=False) - g0)),
                         abs(_wrap(_gp([np.outer(k, k.conj()) for k in path], purify=True) - g0)))
            w_retrace = max(w_retrace, abs(_gp([path[0], path[1]])))
            fan = sum(_gp([path[0], path[k], path[k + 1]]) for k in range(1, n_pts - 1))
            w_fan = max(w_fan, abs(_wrap(fan - g0)))
            apex = _haar_pure(d, rng)
            fan_p = sum(_gp([apex, path[k], path[(k + 1) % n_pts]]) for k in range(n_pts))
            w_apex = max(w_apex, abs(_wrap(fan_p - g0)))
    print(f"5.0 (T14) invariances, 200 random closed paths of Haar kets, d=2..5, N=3..8, seed 5: max |change| under "
          f"per-state rephasing = {w_gauge:.2e};  common unitary = {w_unit:.2e};  cyclic shift = {w_cyc:.2e};  "
          f"max |gamma(reversed) + gamma| = {w_rev:.2e};  ket vs projector input = {w_proj:.2e};  "
          f"retraced path a->b->a: max |gamma| = {w_retrace:.2e};  polygon vs sum of fan triangles from its first "
          f"vertex = {w_fan:.2e}, from an auxiliary apex = {w_apex:.2e}")

    # 5.1 (T15) qubit: gamma = -Omega/2, Omega from the Stokes vectors alone (Van Oosterom–Strackee).
    #     Random geodesic polygons, N = 3..8 vertices, 20 seeds x 100 polygons.
    per_seed = []
    for seed in range(20):
        rng = np.random.default_rng(5100 + seed)
        worst = 0.0
        for _ in range(100):
            n_pts = int(rng.integers(3, 9))
            path = [_haar_pure(2, rng) for _ in range(n_pts)]
            half = half_solid_angle([stokes_vector(k) for k in path])
            worst = max(worst, abs(_wrap(_gp(path) + half)))
        per_seed.append(worst)
    per_seed = np.array(per_seed)
    print(f"5.1 (T15) qubit gamma against the Stokes-vector form arg(1 + S + iT) of eq. (2), 20 seeds x 100 random polygons "
          f"(N=3..8): max |gamma + Omega/2| per seed — mean={per_seed.mean():.2e}  sd={per_seed.std():.2e}  "
          f"max={per_seed.max():.2e}")

    def _spherical_excess(a, b, c) -> float:
        # Girard: area of a geodesic triangle = sum of its interior angles - pi (angles from tangent directions)
        def ang(p, q, r):
            tq, tr = q - (q @ p) * p, r - (r @ p) * p
            return np.arccos(np.clip(tq @ tr / (np.linalg.norm(tq) * np.linalg.norm(tr)), -1, 1))
        return ang(a, b, c) + ang(b, c, a) + ang(c, a, b) - np.pi

    per_seed, sign_bad = [], 0
    for seed in range(20):
        rng = np.random.default_rng(5150 + seed)
        worst = 0.0
        for _ in range(100):
            kets = [_haar_pure(2, rng) for _ in range(3)]
            a, b, c = (stokes_vector(k) for k in kets)
            g = _gp(kets)
            worst = max(worst, abs(abs(g) - _spherical_excess(a, b, c) / 2))
            sign_bad += int(np.sign(g) != -np.sign(a @ np.cross(b, c)))
        per_seed.append(worst)
    per_seed = np.array(per_seed)
    print(f"    independent geometry: |gamma| against half the spherical excess (sum of interior angles - pi), 20 seeds "
          f"(5150-5169) x 100 random triangles: max ||gamma| - E/2| per seed — mean={per_seed.mean():.2e}  "
          f"sd={per_seed.std():.2e}  max={per_seed.max():.2e};  triangles with sign(gamma) != -sign(a.(b x c)): {sign_bad}")

    # 5.2 Polarization loops. Analytic Omega from the octants of the Poincaré sphere the loop encloses
    #     (each octant pi/2). Corollaries of T15: BB84's four states are coplanar -> gamma in {0, pi};
    #     the six-state set -> gamma a multiple of pi/4. All loops without immediate repeats, length 3..5.
    print("\n5.2 polarization loops (H,V on z; D,A on x; R,L on y): gamma, analytic -Omega/2, modulus of the invariant")
    w_52 = 0.0
    for names, expect in ((("H", "D", "R"), -np.pi / 4), (("H", "R", "D"), np.pi / 4),
                          (("H", "D", "R", "A"), -np.pi / 2), (("H", "D", "R", "A", "L"), -3 * np.pi / 4),
                          (("H", "D", "V", "A"), np.pi), (("D", "R", "A", "L"), np.pi)):
        res = geometric_phase([P[x] for x in names])
        w_52 = max(w_52, abs(_wrap(res["gamma"] - expect)))
        print(f"   {'->'.join(names) + '->' + names[0]:<22s} gamma = {res['gamma']:+.6f}  expect {expect:+.6f}  "
              f"(= {expect / np.pi:+.2f} pi)   modulus = {res['modulus']:.4f}")
    res = geometric_phase([P["H"], P["D"], P["V"]])
    print(f"   H->D->V->H             modulus = {res['modulus']:.1e}: V and H are antipodal, the closing geodesic is not "
          f"unique and gamma is undefined")
    print(f"    max |gamma - expect| over the six loops = {w_52:.2e}")
    for label, names in (("BB84 four-state set {H,V,D,A}", "HVDA"), ("six-state set {H,V,D,A,R,L}", "HVDARL")):
        values, n_loops, n_undef, worst_q = set(), 0, 0, 0.0
        for length in (3, 4, 5):
            for seq in itertools.product(names, repeat=length):
                if any(seq[i] == seq[(i + 1) % length] for i in range(length)):
                    continue
                res = geometric_phase([P[x] for x in seq])
                if res["modulus"] < 1e-12:
                    n_undef += 1
                    continue
                n_loops += 1
                q = res["gamma"] / (np.pi / 4)
                worst_q = max(worst_q, abs(q - round(q)))
                values.add(int(round(q)) % 8)
        vals = ", ".join(f"{v}pi/4" for v in sorted(values))
        print(f"   {label}: {n_loops} loops with nonzero modulus ({n_undef} undefined): gamma values (mod 2 pi) = "
              f"{{{vals}}};  max distance from a multiple of pi/4 = {worst_q * np.pi / 4:.2e}")

    # 5.3 A smooth loop sampled at N points: the circle of latitude at polar angle theta about z.
    #     Continuum value -pi(1 - cos theta); the inscribed geodesic N-gon misses
    #     (2 pi)^3 sin^2(theta) cos(theta) / (12 N^2) of solid angle, so the error is half of that.
    theta0 = np.pi / 3
    exact = float(_wrap(-np.pi * (1 - np.cos(theta0))))
    c_pred = (2 * np.pi) ** 3 * np.sin(theta0) ** 2 * np.cos(theta0) / 24
    print(f"\n5.3 sampled circle of latitude, theta = pi/3: continuum gamma = -pi(1-cos theta) = {exact:+.6f};  "
          f"predicted error -> {c_pred:.4f}/N^2")
    for n_pts in (8, 16, 32, 64, 128, 256, 512):
        phis = 2 * np.pi * np.arange(n_pts) / n_pts
        path = [ket_from_stokes([np.sin(theta0) * np.cos(p), np.sin(theta0) * np.sin(p), np.cos(theta0)]) for p in phis]
        err = float(_wrap(_gp(path) - exact))
        print(f"   N={n_pts:4d}  gamma = {_gp(path):+.8f}  error = {err:+.3e}  error*N^2 = {err * n_pts ** 2:.4f}")

    # 5.4 (T16) independence from the dynamical phase. A qubit at polar angle theta from an axis n evolves
    #     for one period under H = e0 + (omega/2) n.sigma. Total phase arg<psi_0|psi_T>, dynamical phase
    #     -(e0 + (omega/2) cos theta) T, Aharonov–Anandan gamma = total - dynamical, and the operation's
    #     gamma on the sampled path (N = 2000), against -pi(1 - cos theta). 20 seeds.
    w_aa, w_path, dyn_all, tot_all = 0.0, 0.0, [], []
    for seed in range(20):
        rng = np.random.default_rng(5400 + seed)
        theta = rng.uniform(0.2, np.pi - 0.2)
        n_axis = _random_unit_vectors((), rng)
        omega, e0 = rng.uniform(0.5, 2.0), rng.uniform(-3.0, 3.0)
        kets, total, dyn = _precession_path(theta, n_axis, omega, e0, 1.0, 2000)
        ex = -np.pi * (1 - np.cos(theta))
        w_aa = max(w_aa, abs(_wrap(total - dyn - ex)))
        w_path = max(w_path, abs(_wrap(_gp(kets[:-1]) - ex)))
        dyn_all.append(dyn); tot_all.append(total)
    dyn_all = np.array(dyn_all)
    print(f"\n5.4 (T16) cyclic evolution under H = e0 + (omega/2) n.sigma, 20 seeds (5400-5419), random theta, n, omega, e0: "
          f"max |(total - dynamical) - (-pi(1-cos theta))| = {w_aa:.2e};  max |gamma(sampled path, N=2000) - same| = {w_path:.2e} "
          f"(leading-order maximum (2 pi)^3 (2/(3 sqrt 3))/(24 N^2) = {(2 * np.pi) ** 3 * 2 / (3 * np.sqrt(3)) / 24 / 2000 ** 2:.2e});  dynamical phases ranged over [{dyn_all.min():+.2f}, {dyn_all.max():+.2f}] rad")
    # one loop, twenty different Hamiltonians: same rays, different speeds and energies
    rng = np.random.default_rng(54)
    g_same, d_same = [], []
    for _ in range(20):
        kets, total, dyn = _precession_path(1.1, [0.3, -0.5, 0.8], rng.uniform(0.5, 2.0), rng.uniform(-3.0, 3.0), 1.0, 400)
        g_same.append(_gp(kets[:-1])); d_same.append(dyn)
    g_same, d_same = np.array(g_same), np.array(d_same)
    print(f"    one loop (theta=1.1) traversed under 20 different (omega, e0), seed 54: spread of gamma = "
          f"{g_same.max() - g_same.min():.2e};  spread of the dynamical phase = {d_same.max() - d_same.min():.2f} rad")
    # 5.4b over-rotation and tilt (T16): theta = pi/3, e0 = 0, N = 20000.
    th, n_fine = np.pi / 3, 20000
    k0, _, dyn0 = _precession_path(th, [0, 0, 1], 1.0, 0.0, 1.0, n_fine)
    g_ref = _gp(k0[:-1])
    print("    5.4b over-rotation by a fraction eps of a turn (theta = pi/3): change of gamma vs -(2 pi eps)^3 sin^2 cos/24; "
          "change of the dynamical phase vs -pi cos(theta) eps")
    for eps_r in (0.01, 0.02, 0.05, 0.1):
        k1, _, dyn1 = _precession_path(th, [0, 0, 1], 1.0, 0.0, 1.0 + eps_r, n_fine)
        dg = float(_wrap(_gp(k1) - g_ref))
        pred = -(2 * np.pi * eps_r) ** 3 * np.sin(th) ** 2 * np.cos(th) / 24
        print(f"       eps={eps_r:.2f}: d_gamma = {dg:+.3e} (predicted {pred:+.3e}, ratio {dg / pred:.4f});  "
              f"d_dynamical = {dyn1 - dyn0:+.4e} (predicted {-np.pi * np.cos(th) * eps_r:+.4e})")
    dth = 1e-4
    k2, _, dyn2 = _precession_path(th + dth, [0, 0, 1], 1.0, 0.0, 1.0, n_fine)
    print(f"       tilt d_theta = 1e-4: d_gamma/d_theta = {float(_wrap(_gp(k2[:-1]) - g_ref)) / dth:+.5f} "
          f"(expect -pi sin theta = {-np.pi * np.sin(th):+.5f});  d_dynamical/d_theta = {(dyn2 - dyn0) / dth:+.5f} "
          f"(expect +pi sin theta = {np.pi * np.sin(th):+.5f})")

    # 5.5 (T17) wave plates. |H> through a quarter-wave plate at 45 deg, a half-wave plate at angle beta, a
    #     quarter-wave plate at 45 deg returns to |H> (up to a phase). Each plate acts on a Stokes vector
    #     perpendicular to its own axis, so no dynamical phase accrues and the phase of <H|U|H> is
    #     geometric: it must equal the operation's gamma on the path through the plates (300 samples per
    #     plate) and -Omega/2 of that path, and move by 2 d_beta when the half-wave plate turns by d_beta.
    print("\n5.5 (T17) quarter–half–quarter wave-plate loop from |H>: phase of <H|U|H> vs gamma of the sampled path "
          "vs -Omega/2; beta = half-wave-plate angle")
    w_55 = w_perp = w_close = 0.0
    n_sub = 300
    phis_55 = []
    for beta_deg in (0, 15, 30, 45, 60, 75):
        beta = np.deg2rad(beta_deg)
        plates = [(np.pi / 2, np.pi / 4), (np.pi, beta), (np.pi / 2, np.pi / 4)]
        psi, path = P["H"].copy(), [P["H"].copy()]
        for ret, ang in plates:
            axis = np.array([np.sin(2 * ang), 0.0, np.cos(2 * ang)])
            start = psi.copy()
            for j in range(1, n_sub + 1):
                psi = retarder(ret * j / n_sub, ang) @ start
                path.append(psi.copy())
                w_perp = max(w_perp, abs(stokes_vector(psi) @ axis))
        u_tot = retarder(*plates[2]) @ retarder(*plates[1]) @ retarder(*plates[0])
        amp = np.vdot(P["H"], u_tot @ P["H"])
        w_close = max(w_close, abs(abs(amp) - 1))
        phi_tot = float(np.angle(amp))
        g_path = _gp(path[:-1])
        half = half_solid_angle([stokes_vector(k) for k in path[:-1]])
        w_55 = max(w_55, abs(_wrap(phi_tot - g_path)), abs(_wrap(g_path + half)))
        phis_55.append(phi_tot)
        print(f"   beta={beta_deg:2d} deg: arg<H|U|H> = {phi_tot:+.6f}  gamma(path) = {g_path:+.6f}  -Omega/2 = {-half:+.6f}")
    slopes = _wrap(np.diff(phis_55)) / np.deg2rad(15)
    print(f"    max |arg<H|U|H> - gamma(path)| and |gamma(path) + Omega/2| = {w_55:.2e} (the path is three geodesic arcs, so sampling adds no error; phases compared mod 2 pi);  "
          f"max ||<H|U|H>| - 1| = {w_close:.2e};  max |s . axis| along the path = {w_perp:.2e};  "
          f"d(phase)/d(beta) between rows = {slopes.min():+.6f} .. {slopes.max():+.6f} (|slope| = 2 expected)")

    # 5.6 (T18) depolarised states: three readings of "the geometric phase". Loops: the octant H->D->R
    #     (Omega = pi/2), a fixed generic triangle, and a wide triangle with Omega/2 > pi/2. E1 purified; E2 raw trace, closed form
    #     -atan2(r^3 T, 1 + r^2 S); E3 interferometric: the state rho_r at the first vertex carried round
    #     by the three geodesic rotations U, phase arg Tr(U rho_r) = -atan2(r sin(Omega/2), cos(Omega/2)), visibility
    #     |Tr(U rho_r)| = sqrt(cos^2(Omega/2) + r^2 sin^2(Omega/2)).
    tri_generic = np.array([[np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]
                            for t, p in ((0.4, 0.3), (1.3, 1.1), (1.0, 2.6))])
    tri_octant = np.array([stokes_vector(P[x]) for x in "HDR"])
    tri_wide = np.array([[np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]
                         for t, p in ((1.5, 0.0), (1.5, 2.1), (1.5, 4.2))])
    print("\n5.6 (T18) depolarised states (Stokes length r): E1 purified, E2 raw trace, E3 interferometric; numeric (closed form)")
    w_56 = 0.0
    for label, tri in (("octant H->D->R", tri_octant), ("generic triangle", tri_generic), ("wide triangle", tri_wide)):
        half = half_solid_angle(tri)
        t_tri = tri[0] @ np.cross(tri[1], tri[2])
        s_tri = tri[0] @ tri[1] + tri[1] @ tri[2] + tri[2] @ tri[0]
        u_loop = np.eye(2, dtype=complex)
        for a, b in ((0, 1), (1, 2), (2, 0)):
            u_loop = rotation(np.cross(tri[a], tri[b]), np.arccos(np.clip(tri[a] @ tri[b], -1, 1))) @ u_loop
        print(f"   {label}: Omega/2 = {half:+.6f}")
        for r in (1.0, 0.9, 0.5, 0.1):
            rhos = [0.5 * (np.eye(2) + r * (v[0] * _SX + v[1] * _SY + v[2] * _SZ)) for v in tri]
            e1 = _gp(rhos, purify=True)
            e2 = _gp(rhos, purify=False)
            e2_an = -np.arctan2(r ** 3 * t_tri, 1 + r ** 2 * s_tri)
            amp = np.trace(u_loop @ rhos[0])
            e3, vis = float(np.angle(amp)), abs(amp)
            e3_an = -np.arctan2(r * np.sin(half), np.cos(half))
            vis_an = np.sqrt(np.cos(half) ** 2 + r ** 2 * np.sin(half) ** 2)
            # E3 again from the operation: weights (1 ± r)/2 on the loop and on its antipodal image
            g_plus = _gp([ket_from_stokes(v) for v in tri])
            g_minus = _gp([ket_from_stokes(-v) for v in tri])
            amp_w = 0.5 * (1 + r) * np.exp(1j * g_plus) + 0.5 * (1 - r) * np.exp(1j * g_minus)
            w_56 = max(w_56, abs(_wrap(e1 + half)), abs(e2 - e2_an), abs(e3 - e3_an), abs(vis - vis_an),
                       abs(amp_w - amp))
            print(f"      r={r:.1f}: E1 = {e1:+.6f} ({-half:+.6f})   E2 = {e2:+.6f} ({e2_an:+.6f})   "
                  f"E3 = {e3:+.6f} ({e3_an:+.6f})  visibility = {vis:.6f} ({vis_an:.6f})")
    print(f"    max |numeric - closed form| over the table (including E3 rebuilt from the operation on the loop and its "
          f"antipodal image) = {w_56:.2e}")

    # 5.7 (T19) Stage 2's triangle phases are geometric phases of the purifying environment's branch states.
    #     (a) HS-random states, d = 3, 4, 5: rho = A A^dag, branch vectors a_k = k-th row of A, in a random
    #         isometric embedding of the environment; every triple j<k<l; 20 seeds x 50 states per d.
    #     (b) Stage 4 baths, equal-weight qutrit, charges (1, 0, -1), 201 times in [0, 10]: the phase
    #         arg(D_01 D_12 D_20) from evolve_open against the sum over modes of gamma(E_0 -> E_1 -> E_2),
    #         branch states computed independently of evolve_open, and against minus the summed half solid
    #         angles of the branch-state triangles on each mode's Bloch sphere.
    per_seed = []
    for seed in range(20):
        rng = np.random.default_rng(5700 + seed)
        worst = 0.0
        for d in (3, 4, 5):
            for _ in range(50):
                rho = _hs_random_state(d, rng)
                w_eig, v_eig = np.linalg.eigh(rho)
                a_mat = v_eig * np.sqrt(np.clip(w_eig, 0, None))            # rho = A A^dag
                iso = _random_unitary(d + 2, rng)[:, :d]                     # environment embedded in d+2 dims
                branch = a_mat @ iso.T                                       # rows: |a_k>
                for j, k, l in itertools.combinations(range(d), 3):
                    tau = np.angle(rho[j, k] * rho[k, l] * rho[l, j])
                    worst = max(worst, abs(_wrap(_gp([branch[j], branch[k], branch[l]]) - tau)))
        per_seed.append(worst)
    per_seed = np.array(per_seed)
    print(f"\n5.7 (T19) (a) triangle phase tau_jkl of a register state == gamma(a_j -> a_k -> a_l) of a purification's "
          f"branch states, HS-random states d=3,4,5, every triple, 20 seeds x 50 states per d: max |difference| per seed — "
          f"mean={per_seed.mean():.2e}  sd={per_seed.std():.2e}  max={per_seed.max():.2e}")
    tt5 = np.linspace(0, 10, 201)
    ch3 = register_charges(3)
    rng = np.random.default_rng(57)
    bath_plus = _random_bath(4, rng)
    bath_tilt = _random_bath(4, rng, bloch=rng.uniform(0.3, np.pi - 0.3, (4, 2)))
    for label, bath in (("|+> modes", bath_plus), ("tilted modes", bath_tilt)):
        res = evolve_open(rho3, bath, tt5)
        w_sum = w_omega = w_copl = w_reg = 0.0
        n_used, big = 0, 0.0
        for ti, t in enumerate(tt5):
            D = res["D"][ti]
            prod = D[0, 1] * D[1, 2] * D[2, 0]
            br = _mode_branch_states(bath, ch3, t)
            g_modes = [_gp([br[i, 0], br[i, 1], br[i, 2]]) for i in range(br.shape[0])]
            halves = [half_solid_angle([stokes_vector(br[i, k]) for k in range(3)]) for i in range(br.shape[0])]
            for i in range(br.shape[0]):
                s = [stokes_vector(br[i, k]) for k in range(3)]
                w_copl = max(w_copl, abs(s[0] @ np.cross(s[1], s[2])))
            if abs(prod) > 1e-9:
                n_used += 1
                tau_env = np.angle(prod)
                w_sum = max(w_sum, abs(_wrap(sum(g_modes) - tau_env)))
                w_omega = max(w_omega, abs(_wrap(-sum(halves) - tau_env)))
                r_t = res["rho"][ti]
                w_reg = max(w_reg, abs(_wrap(np.angle(r_t[0, 1] * r_t[1, 2] * r_t[2, 0]) - tau_env)))
                big = max(big, abs(_wrap(tau_env)))
        print(f"   (b) {label:<13s} n=4, seed 57, {n_used} of 201 times with |D_01 D_12 D_20| > 1e-9: "
              f"max |arg(D_01 D_12 D_20) - sum_i gamma_i| = {w_sum:.2e};  max |same + sum_i Omega_i/2| = {w_omega:.2e};  "
              f"register tau(t) - environment phase = {w_reg:.2e};  max |s_0.(s_1 x s_2)| over modes and times = {w_copl:.2e} "
              f"(0 means every branch triangle lies on a great circle);  max_t |tau| = {big:.4f}")

    # 5.8 FC-1 the extractor at finite statistics. Stokes tomography of each vertex with S shots per axis,
    #     Stokes vectors normalised (E1), gamma_hat = -Omega/2 of the estimated triangle. Pre-registered
    #     (before the first run): (i) |bias| <= 2 standard errors for S >= 1600, and (ii) sd * sqrt(S)
    #     within 10 % of the linear error-propagation value c for S >= 400. Added after adversarial
    #     review: the second-order bias b2/S, b2 = (1/2) sum_i H_ii (1 - s_i^2) (H the Hessian of gamma in
    #     the measured components; T20), and ten times the trials, so that (i) is tested with enough
    #     power to fail. 20 seeds x 20000 trials per S.
    def _phase_of_triangles(v):                                   # v: (trials, 3, 3) -> gamma
        return -_half_solid_angle_batch(v)

    def _jacobian(tri):                                           # d gamma / d (unnormalised Stokes components)
        jac, h = np.zeros((3, 3)), 1e-6
        for a in range(3):
            for b in range(3):
                up, dn = tri.copy(), tri.copy()
                up[a, b] += h; dn[a, b] -= h
                jac[a, b] = (_phase_of_triangles(up[None])[0] - _phase_of_triangles(dn[None])[0]) / (2 * h)
        return jac

    def _bias_coefficient(tri):                                   # b2 = (1/2) sum_i H_ii (1 - s_i^2)
        h, b2 = 1e-4, 0.0
        f0 = _phase_of_triangles(tri[None])[0]
        for a in range(3):
            for b in range(3):
                up, dn = tri.copy(), tri.copy()
                up[a, b] += h; dn[a, b] -= h
                hii = (_phase_of_triangles(up[None])[0] - 2 * f0 + _phase_of_triangles(dn[None])[0]) / h ** 2
                b2 += 0.5 * hii * (1 - tri[a, b] ** 2)
        return 0.0 if abs(b2) < 1e-6 else b2                      # finite-difference noise -> exact 0

    print("\n5.8 FC-1 finite-shot extraction (Stokes tomography, S shots per axis per vertex, normalised Stokes vectors): "
          "20 seeds (5800-5819) x 20000 trials")
    rng = np.random.default_rng(58)
    chk = stokes_tomography(np.tile(tri_generic, (100, 1, 1)), 400, rng)
    w_chk = max(abs(_wrap(_phase_of_triangles(chk[i:i + 1])[0] - _gp([ket_from_stokes(v) for v in chk[i]])))
                for i in range(100))
    print(f"    batch estimator vs the operation on 100 noisy triangles (seed 58): max |difference| = {w_chk:.2e}")
    fc1 = {}
    for label, tri in (("octant H->D->R", tri_octant), ("generic triangle", tri_generic)):
        g_true = _phase_of_triangles(tri[None])[0]
        jac = _jacobian(tri)
        c_lin = float(np.sqrt(np.sum(jac ** 2 * (1 - tri ** 2))))
        b2 = _bias_coefficient(tri)
        print(f"   {label}: gamma = {g_true:+.6f};  linear error propagation: sd = c/sqrt(S), c = {c_lin:.4f};  "
              f"second-order bias = b2/S, b2 = {b2:+.4f}")
        for shots in (100, 400, 1600, 6400, 25600):
            means, sds = [], []
            for seed in range(20):
                rng = np.random.default_rng(5800 + seed)
                est = stokes_tomography(np.tile(tri, (20000, 1, 1)), shots, rng)
                err = _wrap(_phase_of_triangles(est) - g_true)
                means.append(err.mean()); sds.append(err.std())
            means, sds = np.array(means), np.array(sds)
            se = means.std(ddof=1) / np.sqrt(20)
            fc1[(label, shots)] = (means.mean(), se, sds.mean() * np.sqrt(shots) / c_lin, (means.mean() - b2 / shots) / se)
            print(f"      S={shots:5d}: bias = {means.mean():+.2e} ± {se:.1e} (SE over seeds; {means.mean() / se:+.1f} SE from 0)   "
                  f"b2/S = {b2 / shots:+.2e} ({(means.mean() - b2 / shots) / se:+.1f} SE from b2/S)   "
                  f"sd = {sds.mean():.5f} ± {sds.std():.5f}   sd*sqrt(S) = {sds.mean() * np.sqrt(shots):.4f}  "
                  f"(ratio to c: {sds.mean() * np.sqrt(shots) / c_lin:.4f})")
    ok_bias = all(abs(b) <= 2 * se for (lab, s), (b, se, r, z) in fc1.items() if s >= 1600)
    ok_sd = all(abs(r - 1) <= 0.10 for (lab, s), (b, se, r, z) in fc1.items() if s >= 400)
    worst_z = max(abs(z) for (lab, s), (b, se, r, z) in fc1.items() if s >= 400)
    print(f"    pre-registered (i) |bias| <= 2 SE for S >= 1600: {'holds' if ok_bias else 'FAILS'};  "
          f"(ii) sd*sqrt(S) within 10 % of c for S >= 400: {'holds' if ok_sd else 'FAILS'};  "
          f"largest |bias - b2/S| for S >= 400 = {worst_z:.1f} SE")

    # 5.9 FC-2 channel noise that differs from vertex to vertex. Each vertex's Stokes vector is rotated by
    #     its own random rotation (rotation vector ~ N(0, sigma^2 I)); a rotation common to all three
    #     changes nothing (T14). Linear prediction: sd = sigma * sqrt(sum_v |s_v x grad_v gamma|^2).
    #     Pre-registered: sd/sigma within 10 % of the linear value for sigma <= 0.1; |bias| <= 2 SE for
    #     sigma <= 0.03. After adversarial review: the bias is zero by theorem (T20: gamma is harmonic in
    #     each vertex and the noise is isotropic about it), so the bias column is a correctness check; seeds
    #     are independent per sigma. 20 seeds x 20000 trials per sigma, generic triangle.
    def _rotate_batch(v, eps):                                    # Rodrigues, v and eps: (..., 3)
        ang = np.linalg.norm(eps, axis=-1, keepdims=True)
        ax = eps / np.where(ang > 0, ang, 1.0)
        return (v * np.cos(ang) + np.cross(ax, v) * np.sin(ang)
                + ax * np.sum(ax * v, axis=-1, keepdims=True) * (1 - np.cos(ang)))

    print("\n5.9 FC-2 vertex-to-vertex rotation noise of rms angle sigma per axis, generic triangle, "
          "20 seeds per sigma (5900 + 100 j + seed) x 20000 trials")
    g_true = _phase_of_triangles(tri_generic[None])[0]
    jac = _jacobian(tri_generic)
    k_lin = float(np.sqrt(np.sum(np.cross(tri_generic, jac) ** 2)))
    rng = np.random.default_rng(59)
    common = rng.standard_normal((2000, 1, 3)) * 0.3
    w_common = np.abs(_wrap(_phase_of_triangles(_rotate_batch(np.tile(tri_generic, (2000, 1, 1)), common)) - g_true)).max()
    print(f"    common rotation of all three vertices (rms 0.3 rad per axis, 2000 trials, seed 59): max |change| = "
          f"{w_common:.2e};  linear prediction for independent rotations: sd = k sigma, k = {k_lin:.4f}")
    fc2 = {}
    for j_sig, sigma in enumerate((0.01, 0.03, 0.1, 0.3)):
        means, sds = [], []
        for seed in range(20):
            rng = np.random.default_rng(5900 + 100 * j_sig + seed)
            eps_v = rng.standard_normal((20000, 3, 3)) * sigma
            err = _wrap(_phase_of_triangles(_rotate_batch(np.tile(tri_generic, (20000, 1, 1)), eps_v)) - g_true)
            means.append(err.mean()); sds.append(err.std())
        means, sds = np.array(means), np.array(sds)
        se = means.std(ddof=1) / np.sqrt(20)
        fc2[sigma] = (means.mean(), se, sds.mean() / sigma / k_lin)
        print(f"      sigma={sigma:.2f}: bias = {means.mean():+.2e} ± {se:.1e} ({means.mean() / se:+.1f} SE; T20: 0)   "
              f"sd = {sds.mean():.5f} ± {sds.std():.5f}   sd/sigma = {sds.mean() / sigma:.4f} (ratio to k: "
              f"{sds.mean() / sigma / k_lin:.4f})")
    ok_b2 = all(abs(b) <= 2 * se for s, (b, se, r) in fc2.items() if s <= 0.03)
    ok_s2 = all(abs(r - 1) <= 0.10 for s, (b, se, r) in fc2.items() if s <= 0.1)
    print(f"    pre-registered: |bias| <= 2 SE for sigma <= 0.03 (a theorem, T20): {'holds' if ok_b2 else 'FAILS'};  "
          f"sd/sigma within 10 % of k for sigma <= 0.1: {'holds' if ok_s2 else 'FAILS'}")

    # 5.10 FC-3 which channels preserve the geometry. (i) Geometry-preserving class: a fixed unitary, isotropic
    #      depolarisation to Stokes length r, and polarization-independent loss (a scalar factor), applied to
    #      every vertex — the purified gamma is unchanged (theorem; 200 random triangles, seed 510).
    #      (ii) Outside the class: H/V dephasing (Stage 1's dephase on the polarization qubit) and
    #      polarization-dependent loss K = diag(1, sqrt(1-kappa)). Sensitivities d gamma/d g and
    #      d gamma/d kappa at 0 over random triangles (20 seeds x 100, vertices at mutual angles in
    #      [30, 150] degrees), and the generic triangle's gamma as a function of g and kappa.
    rng = np.random.default_rng(510)
    w_class = 0.0
    for _ in range(200):
        kets = [_haar_pure(2, rng) for _ in range(3)]
        u = _random_unitary(2, rng)
        r_dep, loss = rng.uniform(0.05, 1.0), rng.uniform(0.01, 1.0)
        out = []
        for k in kets:
            rho = np.outer(u @ k, (u @ k).conj())
            out.append(loss * (r_dep * rho + (1 - r_dep) * np.eye(2) / 2))
        w_class = max(w_class, abs(_wrap(_gp(out) - _gp(kets))))
    print(f"\n5.10 FC-3 (i) fixed unitary + isotropic depolarisation + polarization-independent loss, 200 random triangles, "
          f"seed 510: max |change of purified gamma| = {w_class:.2e} (theorem: 0)")

    def _pdl(rho, kappa):
        k = np.diag([1.0, np.sqrt(1 - kappa)]).astype(complex)
        out = k @ rho @ k
        return out / np.trace(out).real

    def _gamma_after(tri, channel):
        return _gp([channel(_as_projector(ket_from_stokes(v), False)) for v in tri])

    print("     (ii) outside the class — generic triangle and octant, gamma after H/V dephasing g (Stage 1's dephase) "
          "and after polarization-dependent loss kappa:")
    for label, tri in (("generic triangle", tri_generic), ("octant H->D->R", tri_octant)):
        row_g = "  ".join(f"g={g:.2f}: {_gamma_after(tri, lambda r, g=g: dephase(r, g)):+.5f}" for g in (0.0, 0.01, 0.05, 0.1, 0.3, 0.9))
        row_k = "  ".join(f"k={k:.2f}: {_gamma_after(tri, lambda r, k=k: _pdl(r, k)):+.5f}" for k in (0.0, 0.01, 0.05, 0.1, 0.3, 0.9))
        print(f"        {label:<17s} dephasing: {row_g}")
        print(f"        {label:<17s} PDL:       {row_k}")
    med_g, med_k, h_fd = [], [], 1e-5
    for seed in range(20):
        rng = np.random.default_rng(51000 + seed)
        sg, sk, n_ok = [], [], 0
        while n_ok < 100:
            tri = _random_unit_vectors((3,), rng)
            dots = [tri[0] @ tri[1], tri[1] @ tri[2], tri[2] @ tri[0]]
            if max(dots) > np.cos(np.deg2rad(30)) or min(dots) < np.cos(np.deg2rad(150)):
                continue
            n_ok += 1
            base = _gamma_after(tri, lambda r: r)
            sg.append(abs(_wrap(_gamma_after(tri, lambda r: dephase(r, h_fd)) - base)) / h_fd)
            sk.append(abs(_wrap(_gamma_after(tri, lambda r: _pdl(r, h_fd)) - base)) / h_fd)
        med_g.append(np.median(sg)); med_k.append(np.median(sk))
    med_g, med_k = np.array(med_g), np.array(med_k)
    print(f"     sensitivity at 0, 20 seeds (51000-51019) x 100 random triangles: median |d gamma/d g| = "
          f"{med_g.mean():.4f} ± {med_g.std():.4f} rad per unit dephasing;  median |d gamma/d kappa| = "
          f"{med_k.mean():.4f} ± {med_k.std():.4f} rad per unit loss imbalance")

    print("\nStage 5 summary: the geometric phase of a closed path of states is one gauge-invariant number,")
    print("-arg of the Bargmann invariant; on a polarization qubit it is minus half the solid angle of the path")
    print("on the Poincaré sphere (T15) and is independent of the dynamical phase (T16); BB84's four states give")
    print("only 0 or pi and the six-state set only multiples of pi/4; Stage 2's triangle phases are geometric")
    print("phases of the purifying environment's branch states (T19); the extraction is unchanged by a fixed")
    print("unitary, isotropic depolarisation and uniform loss, and is generically changed at first order by")
    print("basis-dependent dephasing, polarization-dependent loss and vertex-to-vertex channel drift; its")
    print("finite-shot estimate has spread c/sqrt(S) and, off the symmetric loops, a bias b2/S.")

    # -----------------------------------------------------------------------
    # Stage 6 — the pair bridge: p_eff and the signal readings of a two-photon state
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("Stage 6 — the pair bridge; a two-photon polarization state read as a signal interface would read it\n")

    def _obs(n) -> np.ndarray:
        return n[0] * _SX + n[1] * _SY + n[2] * _SZ

    def _chsh_expectation(rho, a, a2, b, b2) -> float:
        op = np.kron(_obs(a), _obs(b) + _obs(b2)) + np.kron(_obs(a2), _obs(b) - _obs(b2))
        return float(np.real(np.trace(rho @ op)))

    def _partial_transpose_min(rho) -> float:
        r = rho.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
        return float(np.linalg.eigvalsh(r).min())

    def _noisy_pair(rng: np.random.Generator) -> np.ndarray:
        """A pair built from the series' own channels: Werner p ~ U(0.3, 1), a relation factor
        |D| ~ U(0, 1) with random phase on photon B, polarization-dependent loss kappa ~ U(0, 0.5)
        on photon A (post-selected), then random local unitaries."""
        rho = werner_state(rng.uniform(0.3, 1.0))
        rho = relation_factor(rho, rng.uniform(0, 1) * np.exp(1j * rng.uniform(0, 2 * np.pi)), 1)
        rho = on_photon(rho, [np.diag([1.0, np.sqrt(1 - rng.uniform(0, 0.5))])], 0, normalise=True)
        u = np.kron(_random_unitary(2, rng), _random_unitary(2, rng))
        return u @ rho @ u.conj().T

    def _rank2_pair(rng: np.random.Generator) -> np.ndarray:
        """Random rank-2 two-qubit state (4 x 2 Ginibre matrix): mostly entangled, often Bell-violating."""
        g = rng.standard_normal((4, 2)) + 1j * rng.standard_normal((4, 2))
        rho = g @ g.conj().T
        return rho / np.trace(rho).real

    # 6.0 Correctness of the operation. Hilbert–Schmidt-random two-qubit states, seed 6.
    #     (a) f: closed form from the singular values of T against the largest eigenvalue of Re(rho) in the
    #         magic basis, and against 200 random maximally entangled states per state (none may exceed f);
    #     (b) S: the Horodecki value against the literal expectation of the CHSH operator at the settings
    #         built from the singular vectors of T, and against 200 random setting quadruples (none may exceed);
    #     (c) concurrence > 0 iff the partial transpose has a negative eigenvalue;
    #     (d) invariance of the settings-optimised readings under random local unitaries;
    #     (e) 2000 random pure product states: none may be placed in the entanglement tier (the concurrence itself
    #         carries square-root rounding noise there, which is why the tier uses the partial transpose);
    #     (f) the closed form for f on nearly maximally mixed Werner pairs (p down to 1e-9), where det T underflows
    #         any absolute cutoff.
    rng = np.random.default_rng(6)
    w_f = w_s = w_lu = 0.0
    exc_f = exc_s = -np.inf
    ppt_disagree = n_ent = 0
    for _ in range(200):
        rho = _hs_random_state(4, rng)
        sig = pair_signals(rho)
        w_f = max(w_f, abs(sig["fully_entangled_fraction"] - sig["fully_entangled_fraction_magic"]))
        for _k in range(200):
            psi = np.kron(_random_unitary(2, rng), np.eye(2)) @ PHI_PLUS
            exc_f = max(exc_f, float(np.real(psi.conj() @ rho @ psi)) - sig["fully_entangled_fraction"])
        uu, ss, vvt = np.linalg.svd(sig["T"])
        th = np.arctan2(ss[1], ss[0])
        b1 = np.cos(th) * vvt[0] + np.sin(th) * vvt[1]
        b2 = np.cos(th) * vvt[0] - np.sin(th) * vvt[1]
        w_s = max(w_s, abs(_chsh_expectation(rho, uu[:, 0], uu[:, 1], b1, b2) - sig["chsh"]))
        vecs = rng.standard_normal((200, 4, 3))
        vecs /= np.linalg.norm(vecs, axis=-1, keepdims=True)
        for v in vecs:
            exc_s = max(exc_s, abs(_chsh_expectation(rho, *v)) - sig["chsh"])
        ent = sig["concurrence"] > 1e-9
        n_ent += int(ent)
        ppt_disagree += int(ent != (_partial_transpose_min(rho) < -1e-9))
        u = np.kron(_random_unitary(2, rng), _random_unitary(2, rng))
        sig2 = pair_signals(u @ rho @ u.conj().T)
        w_lu = max(w_lu, *(abs(sig2[k] - sig[k]) for k in ("chsh", "fully_entangled_fraction", "concurrence",
                                                         "key_fraction", "p_chsh", "p_qber", "p_tel")))
    n_prod_flag, noise_prod = 0, 0.0
    for _ in range(2000):
        prod = np.kron(_haar_pure(2, rng), _haar_pure(2, rng))
        sig_p = pair_signals(np.outer(prod, prod.conj()))
        n_prod_flag += int(pair_tiers(sig_p)[3])
        noise_prod = max(noise_prod, sig_p["concurrence"])
    w_small = max(abs(pair_signals(werner_state(p))["p_tel"] / p - 1) for p in (1e-3, 1e-6, 1e-9))
    print(f"6.0 operation correctness, 200 Hilbert–Schmidt-random two-qubit states, seed 6: "
          f"max |f(singular values) - f(magic basis)| = {w_f:.2e};  max (random maximally entangled overlap - f) = {exc_f:+.2e} (<= 0);  "
          f"max |S(Horodecki) - <CHSH> at the singular-vector settings| = {w_s:.2e};  max (|<CHSH>| at random settings - S) = {exc_s:+.2e} (<= 0);  "
          f"concurrence > 0 vs negative partial transpose: {ppt_disagree} disagreements ({n_ent} of 200 entangled);  "
          f"max change of S, f, concurrence, key fraction, p_chsh, p_qber, p_tel under random local unitaries = {w_lu:.2e};  "
          f"2000 random pure product states placed in the entanglement tier: {n_prod_flag} (largest concurrence returned for one: "
          f"{noise_prod:.1e}, rounding);  max |p_tel/p - 1| for rho_W(p), p = 1e-3, 1e-6, 1e-9: {w_small:.1e}")

    # 6.1 (T21) mixing rule. w rho_W(p) + (1-w) 1/4 == rho_W(wp); isotropic depolarisation of either photon to
    #     Stokes length r == rho_W(rp); p_eff = p_source R_s/(R_s+R_b) read back by all four effective parameters.
    rng = np.random.default_rng(61)
    w_mix = w_dep = w_read = 0.0
    for _ in range(200):
        p_s, sgl, bkg, r_dep = rng.uniform(0.3, 1), rng.uniform(1, 100), rng.uniform(0, 30), rng.uniform(0, 1)
        p_eff = effective_werner(p_s, sgl, bkg)
        rho = with_accidentals(werner_state(p_s), sgl, bkg)
        w_mix = max(w_mix, np.abs(rho - werner_state(p_eff)).max())
        a_dep = np.sqrt((1 + 3 * r_dep) / 4)
        b_dep = np.sqrt((1 - r_dep) / 4)
        kr = [a_dep * np.eye(2), b_dep * _SX, b_dep * _SY, b_dep * _SZ]      # Stokes vector -> r * Stokes vector
        for which in (0, 1):
            w_dep = max(w_dep, np.abs(on_photon(werner_state(p_s), kr, which) - werner_state(r_dep * p_s)).max())
        sig = pair_signals(rho)
        w_read = max(w_read, *(abs(sig[k] - p_eff) for k in ("p_chsh", "p_qber", "p_tel", "p_frame", "C_l1")))
    print(f"6.1 (T21) 200 random (p_source, R_s, R_b, r), seed 61: max ||w rho_W(p) + (1-w) 1/4 - rho_W(p R_s/(R_s+R_b))|| = {w_mix:.2e};  "
          f"max ||one-photon isotropic depolarisation - rho_W(r p)|| = {w_dep:.2e};  "
          f"max |p_chsh, p_qber, p_tel, p_frame, C_l1 - p_eff| = {w_read:.2e}")

    # 6.2 (T22) Werner readouts and the bridge identity C_l1 = V_E(heralded) = p.
    print("\n6.2 (T22) Werner pair rho_W(p): S = 2 sqrt2 p; F = (1+p)/2; e = (1-p)/2; key = 1 - 2 h(e); concurrence = max(0,(3p-1)/2); "
          "C_l1 (H/V basis) = p; heralded V_E (photon A found in |D>, Stage 1's scan on photon B) = p")
    w_62 = 0.0
    for p in (1.0, 0.95, 0.9, 0.8, 1 / np.sqrt(2), 0.5, 1 / 3, 0.2, 0.0):
        rho = werner_state(p)
        sig = pair_signals(rho)
        prob, cond = heralded_state(rho, POLARIZATION["D"])
        v_her = multiport_visibility(cond)["V_E"]
        e_an = (1 - p) / 2
        key_an = max(0.0, 1 - 2 * _binary_entropy(e_an))
        w_62 = max(w_62, abs(sig["chsh"] - 2 * np.sqrt(2) * p), abs(sig["teleportation_fidelity"] - (1 + p) / 2),
                   abs(sig["qber_z"] - e_an), abs(sig["qber_x"] - e_an), abs(sig["qber_best"][0] - e_an),
                   abs(sig["key_fraction"] - key_an), abs(sig["concurrence"] - max(0.0, (3 * p - 1) / 2)),
                   abs(sig["C_l1"] - p), abs(v_her - p), abs(visibility_predicted(cond) - p), abs(prob - 0.5),
                   abs(sig["p_chsh"] - p), abs(sig["p_qber"] - p), abs(sig["p_tel"] - p), abs(sig["p_frame"] - p),
                   np.abs(sig["stokes_a"]).max(), np.abs(sig["stokes_b"]).max())
        print(f"   p={p:.4f}  S={sig['chsh']:.4f}  F={sig['teleportation_fidelity']:.4f}  e={sig['qber_z']:.4f}  "
              f"key={sig['key_fraction']:.4f}  concurrence={sig['concurrence']:.4f}  C_l1={sig['C_l1']:.4f}  "
              f"V_E(heralded)={v_her:.4f}  tiers(key,Bell,tel,ent,coh)={''.join('Y' if x else '-' for x in pair_tiers(sig))}")
    print(f"    max |numeric - closed form| over the table (all readings, both error rates, four effective parameters, "
          f"local Stokes vectors, herald probability) = {w_62:.2e}")
    thr_key = _threshold(lambda p: pair_signals(werner_state(p))["key_fraction"] > 1e-12, 0.0, 1.0)
    thr_bell = _threshold(lambda p: pair_signals(werner_state(p))["chsh"] > 2.0, 0.0, 1.0)
    thr_tel = _threshold(lambda p: pair_signals(werner_state(p))["fully_entangled_fraction"] > 0.5, 0.0, 1.0)
    thr_ent = _threshold(lambda p: pair_signals(werner_state(p))["concurrence"] > 1e-12, 0.0, 1.0)
    print(f"    tier thresholds in p (bisection): key {thr_key:.4f} (h(e) = 1/2 at e = 0.1100, p = 0.7799);  Bell {thr_bell:.4f} "
          f"(1/sqrt2 = {1 / np.sqrt(2):.4f});  teleportation {thr_tel:.4f} and entanglement {thr_ent:.4f} (1/3)")
    # coherence over local product bases: C_l1 in [p, 3p]
    per_lo, per_hi = [], []
    p_c = 0.8
    for seed in range(20):
        rng = np.random.default_rng(6200 + seed)
        vals = []
        for _ in range(200):
            u = np.kron(_random_unitary(2, rng), _random_unitary(2, rng))
            vals.append(l1_coherence(u @ werner_state(p_c) @ u.conj().T) / p_c)
        per_lo.append(min(vals)); per_hi.append(max(vals))
    per_lo, per_hi = np.array(per_lo), np.array(per_hi)
    u_zx = np.kron(np.eye(2), HADAMARD)
    print(f"    C_l1/p over random local product bases, 20 seeds (6200-6219) x 200, p = 0.8: smallest per seed = "
          f"{per_lo.mean():.4f} ± {per_lo.std():.4f} (min {per_lo.min():.4f}; theorem >= 1), largest per seed = "
          f"{per_hi.mean():.4f} ± {per_hi.std():.4f} (max {per_hi.max():.4f}; theorem <= 3);  H/V (x) H/V basis: "
          f"{l1_coherence(werner_state(p_c)) / p_c:.4f};  H/V (x) D/A basis: "
          f"{l1_coherence(u_zx @ werner_state(p_c) @ u_zx.conj().T) / p_c:.4f}")

    # 6.3 (T23) ordering p_frame <= p_tel <= p_qber <= p_chsh. Two ensembles, 20 seeds x 500 states each:
    #     Hilbert–Schmidt-random two-qubit states (seeds 6300-6319) and pairs built from the series' own channels
    #     (seeds 6350-6369), and random rank-2 states (seeds 6380-6399). Violations must be zero; the gaps are
    #     ensemble statistics.
    print("\n6.3 (T23) ordering p_frame <= p_tel <= p_qber <= p_chsh, 20 seeds x 500 states per ensemble")
    for label, base, gen in (("Hilbert–Schmidt-random", 6300, lambda r: _hs_random_state(4, r)),
                             ("series-channel pairs", 6350, _noisy_pair), ("random rank-2", 6380, _rank2_pair)):
        viol, g_ct, g_cq, n_det = 0, [], [], 0
        for seed in range(20):
            rng = np.random.default_rng(base + seed)
            ct, cq = [], []
            for _ in range(500):
                sig = pair_signals(gen(rng))
                viol += int(sig["p_frame"] > sig["p_tel"] + 1e-10) + int(sig["p_tel"] > sig["p_qber"] + 1e-10) \
                    + int(sig["p_qber"] > sig["p_chsh"] + 1e-10)
                ct.append(sig["p_chsh"] - sig["p_tel"]); cq.append(sig["p_chsh"] - sig["p_qber"])
                n_det += int(sig["det_T"] > 1e-12)
            g_ct.append(np.mean(ct)); g_cq.append(np.mean(cq))
        g_ct, g_cq = np.array(g_ct), np.array(g_cq)
        print(f"   {label:<24s}: violations = {viol};  mean p_chsh - p_tel = {g_ct.mean():.4f} ± {g_ct.std():.4f};  "
              f"mean p_chsh - p_qber = {g_cq.mean():.4f} ± {g_cq.std():.4f};  states with det T > 0: {n_det} of 10000")

    # 6.4 (T24) nesting key => Bell => teleportation => entanglement => coherence. Same two ensembles (new seeds).
    #     For the coherence tier the theorem is 'in every product basis'; the tier is evaluated in the basis given and
    #     in 20 random local product bases per state. The three ensembles populate the tiers differently (the
    #     Hilbert–Schmidt one has almost no key or Bell states; the rank-2 one has many).
    print("\n6.4 (T24) nesting of tiers, 20 seeds x 500 states per ensemble: inclusion violations (must be 0) and tier populations")
    for label, base, gen in (("Hilbert–Schmidt-random", 6400, lambda r: _hs_random_state(4, r)),
                             ("series-channel pairs", 6450, _noisy_pair), ("random rank-2", 6480, _rank2_pair)):
        viol, pops, min_coh, n_bell_det = 0, [], np.inf, 0
        for seed in range(20):
            rng = np.random.default_rng(base + seed)
            cnt = np.zeros(5)
            for _ in range(500):
                rho = gen(rng)
                sig = pair_signals(rho)
                tiers = pair_tiers(sig)
                n_bell_det += int(tiers[1] and sig["det_T"] > 1e-12)
                cnt += np.array(tiers, dtype=float)
                viol += sum(int(tiers[i] and not tiers[i + 1]) for i in range(4))
                if tiers[3]:
                    for _k in range(20):
                        u = np.kron(_random_unitary(2, rng), _random_unitary(2, rng))
                        min_coh = min(min_coh, l1_coherence(u @ rho @ u.conj().T))
            pops.append(cnt / 500)
        pops = np.array(pops)
        txt = "  ".join(f"{nm} {pops[:, i].mean():.3f}±{pops[:, i].std():.3f}" for i, nm in
                        enumerate(("key", "Bell", "teleportation", "entanglement", "coherence")))
        print(f"   {label:<24s}: violations = {viol};  fraction of states in each tier: {txt};  smallest C_l1 of an "
              f"entangled state over 20 random local product bases = {min_coh:.4f} (> 0);  states with S > 2 and det T > 0: {n_bell_det}")
    # no converse: one explicit state per gap
    ex = [("coherent, not entangled: product register |D>|D>", twist_register(0.0)),
          ("entangled, f <= 1/2: 0.3 |Psi-><Psi-| + 0.7 |HH><HH|",
           0.3 * np.outer(_MAGIC[:, 3], _MAGIC[:, 3].conj()) + 0.7 * np.diag([1.0, 0, 0, 0]).astype(complex)),
          ("f > 1/2, S <= 2: rho_W(0.5)", werner_state(0.5)),
          ("S > 2, no key: rho_W(0.75)", werner_state(0.75))]
    for label, rho in ex:
        sig = pair_signals(rho)
        print(f"      {label:<58s} key={sig['key_fraction']:.4f}  S={sig['chsh']:.4f}  f={sig['fully_entangled_fraction']:.4f}  "
              f"concurrence={sig['concurrence']:.4f}  C_l1={sig['C_l1']:.4f}  tiers={''.join('Y' if x else '-' for x in pair_tiers(sig))}")
    # where the tiers are lost, by noise family, as the value of the H/V coherence C_l1 at the loss
    def _h_inv(y: float) -> float:                                  # e in [0, 1/2] with h(e) = y
        return _threshold(lambda e: _binary_entropy(e) > y, 0.0, 0.5)

    c_key_iso = 1 - 2 * _h_inv(0.5)
    c_key_95 = (1 - 2 * _h_inv(1 - _binary_entropy(0.025))) / 0.95
    print("    value of the coherence parameter at which each tier is lost, by noise family (bisection on the operation; closed forms in brackets):")
    fams = (("isotropic rho_W(c)", lambda c: werner_state(c),
             f"key {c_key_iso:.4f} (2 h(e) = 1), Bell {1 / np.sqrt(2):.4f}, tel and ent {1 / 3:.4f}"),
            ("Phi+ with relation factor c on one photon", lambda c: relation_factor(werner_state(1.0), c, 1),
             "all four at c = 0"),
            ("rho_W(0.95) with relation factor c on one photon", lambda c: relation_factor(werner_state(0.95), c, 1),
             f"key {c_key_95:.4f} (h(e_2) = 1 - h(0.025)), Bell {np.sqrt(1 / 0.95 ** 2 - 1):.4f}, tel and ent {0.05 / 1.9:.4f}"))
    for label, fam, an in fams:
        th = [_threshold(lambda c, i=i: pair_tiers(pair_signals(fam(c)))[i], 0.0, 1.0) for i in range(4)]
        print(f"      {label:<50s} key {th[0]:.4f}  Bell {th[1]:.4f}  teleportation {th[2]:.4f}  entanglement {th[3]:.4f}   [{an}]")

    # 6.5 (T25) earlier stages' operations acting on one photon of a pair.
    #     (a) literal checks: Stage 1's dephase on the heralded photon; Stage 3's instrument (its own Kraus operators)
    #         on photon B; Stage 4's evolve_open on the pair as a four-history register whose charges depend only on
    #         photon B's history, and the literal joint evolution with n = 2 modes; closed forms for S, f, e, concurrence.
    rng = np.random.default_rng(65)
    w_s1 = w_s3 = w_s4 = w_s4j = w_cf = 0.0
    for _ in range(100):
        p0, gam, eta = rng.uniform(0.4, 1), rng.uniform(0, 1), rng.uniform(0, 1)
        rho0 = werner_state(p0)
        # Stage 1: the channel on photon B commutes with heralding on photon A
        ket_a = _haar_pure(2, rng)
        w_s1 = max(w_s1, np.abs(heralded_state(relation_factor(rho0, 1 - gam, 1), ket_a)[1]
                                - dephase(heralded_state(rho0, ket_a)[1], gam)).max())
        # Stage 3: unread instrument on photon B
        kr = observe(rho_coh, eta)["kraus"]
        w_s3 = max(w_s3, np.abs(on_photon(rho0, kr, 1) - relation_factor(rho0, np.sqrt(1 - eta ** 2), 1)).max())
        # closed forms
        dabs = rng.uniform(0, 1)
        dfac = dabs * np.exp(1j * rng.uniform(0, 2 * np.pi))
        sig = pair_signals(relation_factor(rho0, dfac, 1))
        w_cf = max(w_cf, abs(sig["chsh"] - 2 * p0 * np.sqrt(1 + dabs ** 2)),
                   abs(sig["fully_entangled_fraction"] - (1 + p0 + 2 * p0 * dabs) / 4),
                   abs(sig["qber_best"][0] - (1 - p0) / 2), abs(sig["qber_best"][1] - (1 - p0 * dabs) / 2),
                   abs(sig["concurrence"] - max(0.0, p0 * dabs - (1 - p0) / 2)), abs(sig["C_l1"] - p0 * dabs),
                   abs(sig["qber_x"] - (1 - p0 * dfac.real) / 2), abs(sig["qber_z"] - (1 - p0) / 2))
    ch_b = np.array([0.5, -0.5, 0.5, -0.5])                       # charge of history (a, b) = charge of b
    for _ in range(10):
        p0 = rng.uniform(0.4, 1)
        rho0 = werner_state(p0)
        bath = _random_bath(4, rng, bloch=rng.uniform(0, np.pi, (4, 2)))
        tt = np.linspace(0, 8, 41)
        res_pair = evolve_open(rho0, bath, tt, charges=ch_b)
        d01 = evolve_open(rho_coh, bath, tt)["D"][:, 0, 1]
        for i in range(len(tt)):
            w_s4 = max(w_s4, np.abs(res_pair["rho"][i] - relation_factor(rho0, d01[i], 1)).max())
        bath2 = _random_bath(2, rng, bloch=rng.uniform(0, np.pi, (2, 2)))
        tt2 = np.linspace(0, 6, 7)
        w_s4j = max(w_s4j, np.abs(evolve_open(rho0, bath2, tt2, charges=ch_b)["rho"]
                                  - _joint_evolve(rho0, bath2, tt2, charges=ch_b)).max())
    print(f"\n6.5 (T25) one-photon operations on rho_W(p), seed 65: Stage 1 dephase on the heralded photon vs relation factor 1-gamma "
          f"on the pair, 100 (p, gamma, herald): max deviation = {w_s1:.2e};  Stage 3 instrument (its Kraus operators) on photon B vs "
          f"relation factor sqrt(1-eta^2): {w_s3:.2e};  Stage 4 evolve_open on the pair (charges of photon B only) vs relation factor "
          f"D_01(t), 10 baths x 41 times: {w_s4:.2e}, and vs the literal joint evolution (n = 2): {w_s4j:.2e};  closed forms for S, f, "
          f"e_1, e_2, concurrence, C_l1, e_x, e_z under a complex factor D, 100 draws: {w_cf:.2e}")
    #     (b) Stage 3's ladder read by the pair (p = 1): which-history distinguishability eta on photon B.
    print("    Stage 3 ladder on photon B of |Phi+> (unread): eta, S, (S/2)^2 + eta^2 (theorem: 2), F, e_x, key, concurrence, "
          "C_l1 = heralded V_E")
    w_lad = 0.0
    for eta in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0):
        rho = on_photon(werner_state(1.0), observe(rho_coh, eta)["kraus"], 1)
        sig = pair_signals(rho)
        v_her = multiport_visibility(heralded_state(rho, POLARIZATION["D"])[1])["V_E"]
        c = np.sqrt(1 - eta ** 2)
        w_lad = max(w_lad, abs((sig["chsh"] / 2) ** 2 + eta ** 2 - 2), abs(sig["teleportation_fidelity"] - (2 + c) / 3),
                    abs(sig["qber_x"] - (1 - c) / 2), abs(sig["C_l1"] - c), abs(v_her - c), abs(sig["concurrence"] - c),
                    abs(sig["key_fraction"] - (1 - _binary_entropy((1 - c) / 2))))
        print(f"      eta={eta:.2f}  S={sig['chsh']:.4f}  (S/2)^2+eta^2={(sig['chsh'] / 2) ** 2 + eta ** 2:.4f}  "
              f"F={sig['teleportation_fidelity']:.4f}  e_x={sig['qber_x']:.4f}  key={sig['key_fraction']:.4f}  "
              f"concurrence={sig['concurrence']:.4f}  C_l1={sig['C_l1']:.4f}  V_E(heralded)={v_her:.4f}")
    print(f"      max |numeric - closed form| over the ladder = {w_lad:.2e}")
    #     (c) frame-fixed against settings-optimised readings: a sign change of a real D (Stage 4, T13), a fixed
    #         rotation of photon B's frame (Stage 5's class), polarization-dependent loss (outside the class).
    rows = (("rho_W(0.95), D = +0.6", relation_factor(werner_state(0.95), 0.6, 1)),
            ("rho_W(0.95), D = -0.6", relation_factor(werner_state(0.95), -0.6, 1)),
            ("rho_W(0.95), photon B rotated 0.3 rad about y",
             on_photon(werner_state(0.95), [rotation([0, 1, 0], 0.3)], 1)),
            ("Phi+, loss imbalance kappa = 0.3 on photon B",
             on_photon(werner_state(1.0), [np.diag([1.0, np.sqrt(0.7)])], 1, normalise=True)))
    print("    settings-optimised readings (S, F, key, concurrence) against frame-fixed ones (e_z, e_x, C_l1, p_frame):")
    for label, rho in rows:
        sig = pair_signals(rho)
        print(f"      {label:<46s} S={sig['chsh']:.4f}  F={sig['teleportation_fidelity']:.4f}  key={sig['key_fraction']:.4f}  "
              f"concurrence={sig['concurrence']:.4f} | e_z={sig['qber_z']:.4f}  e_x={sig['qber_x']:.4f}  C_l1={sig['C_l1']:.4f}  "
              f"p_frame={sig['p_frame']:.4f} | p_chsh - p_tel = {abs(sig['anisotropy']) if abs(sig['anisotropy']) < 5e-13 else sig['anisotropy']:.4f}")

    # 6.6 (T26) a four-history register read as a pair. Stage 2's equal-weight register with one relative phase chi.
    #     (a) chi = 0 (product) against chi = pi (maximally entangled) under Stage 2's uniform dephasing gamma: every
    #         register-level quantity of Stages 1-5 identical; the pair readings different.
    #     (b) concurrence = |sin(chi/2)| and S = 2 sqrt(1 + sin^2(chi/2)) (the published two-register table);
    #         chi unchanged by local diagonal unitaries, removed by a general diagonal unitary.
    #     (c) thresholds under uniform dephasing at chi = pi.
    print("\n6.6 (T26) four-history register read as a pair: product register (chi = 0) against twisted register (chi = pi) under "
          "Stage 2's uniform dephasing gamma")
    w_reg = w_wer = 0.0
    for gam in (0.0, 0.2, 0.5, 0.7, 0.9):
        r0, r1 = _dephase_d(twist_register(0.0), gam), _dephase_d(twist_register(np.pi), gam)
        m0, m1 = multiport_visibility(r0), multiport_visibility(r1)
        w_reg = max(w_reg, abs(m0["V_E"] - m1["V_E"]), abs(m0["C_l1"] - m1["C_l1"]), abs(m0["gap"] - m1["gap"]),
                    abs(relative_entropy_coherence(r0) - relative_entropy_coherence(r1)),
                    abs(_max_triangle_phase(r0) - _max_triangle_phase(r1)), np.abs(np.diag(r0) - np.diag(r1)).max())
        s0, s1 = pair_signals(r0), pair_signals(r1)
        sw = pair_signals(werner_state(1 - gam))
        w_wer = max(w_wer, abs(s1["chsh"] - sw["chsh"]), abs(s1["fully_entangled_fraction"] - sw["fully_entangled_fraction"]),
                    abs(s1["concurrence"] - sw["concurrence"]), abs(s1["key_fraction"] - sw["key_fraction"]),
                    abs(s1["C_l1"] / 3 - (1 - gam)))
        print(f"   gamma={gam:.1f}: C_l1 = {m0['C_l1']:.4f} | {m1['C_l1']:.4f}   V_E = {m0['V_E']:.4f} | {m1['V_E']:.4f}   "
              f"S = {s0['chsh']:.4f} | {s1['chsh']:.4f}   concurrence = {s0['concurrence']:.4f} | {s1['concurrence']:.4f}   "
              f"F = {s0['teleportation_fidelity']:.4f} | {s1['teleportation_fidelity']:.4f}")
    print(f"    max difference between the two registers in C_l1, C_re, V_E, gap, triangle phases, populations = {w_reg:.2e};  "
          f"max difference between the chi = pi register and rho_W(1 - gamma) in S, f, concurrence, key fraction, and of "
          f"C_l1/(d-1) from 1 - gamma = {w_wer:.2e}")
    w_chi = w_loc = 0.0
    rng = np.random.default_rng(66)
    row = []
    for chi in np.linspace(0, np.pi, 5):
        sig = pair_signals(twist_register(chi))
        w_chi = max(w_chi, abs(sig["concurrence"] - abs(np.sin(chi / 2))),
                    abs(sig["chsh"] - 2 * np.sqrt(1 + np.sin(chi / 2) ** 2)))
        row.append(f"chi={chi / np.pi:.2f}pi: {sig['concurrence']:.4f}, {sig['chsh']:.4f}")
    for _ in range(100):
        chi = rng.uniform(0.1, np.pi)
        rho = twist_register(chi)
        al, be = rng.uniform(0, 2 * np.pi, 2), rng.uniform(0, 2 * np.pi, 2)
        loc = np.kron(np.diag(np.exp(1j * al)), np.diag(np.exp(1j * be)))
        rl = loc @ rho @ loc.conj().T
        w_loc = max(w_loc, abs(_wrap(np.angle(rl[0, 1] * rl[3, 2]) - chi)),
                    abs(pair_signals(rl)["concurrence"] - abs(np.sin(chi / 2))))
        gen_d = np.diag([1, 1, 1, np.exp(-1j * chi)])
        rg = gen_d @ rho @ gen_d.conj().T
        w_loc = max(w_loc, abs(pair_signals(rg)["concurrence"]), abs(l1_coherence(rg) - l1_coherence(rho)))
    print(f"    concurrence, S against |sin(chi/2)|, 2 sqrt(1 + sin^2(chi/2)): " + ";  ".join(row) + f";  max deviation = {w_chi:.2e}")
    print(f"    100 random chi, seed 66: chi = arg(rho_00,01 rho_11,10) and the concurrence unchanged by local diagonal unitaries, and the "
          f"concurrence removed (C_l1 unchanged) by the register's diagonal unitary diag(1,1,1,e^-i chi): max deviation = {w_loc:.2e}")
    fam = lambda g: _dephase_d(twist_register(np.pi), 1 - g)        # parameter = 1 - gamma so that tiers switch on going up
    th = [1 - _threshold(lambda c, i=i: pair_tiers(pair_signals(fam(c)))[i], 0.0, 1.0) for i in range(4)]
    print(f"    chi = pi register, uniform dephasing: tiers lost at gamma = key {th[0]:.4f} (0.2201), Bell {th[1]:.4f} "
          f"(1 - 1/sqrt2 = {1 - 1 / np.sqrt(2):.4f}), teleportation {th[2]:.4f} and entanglement {th[3]:.4f} (2/3 = {2 / 3:.4f}), "
          f"coherence at gamma = 1")

    # 6.7 FC-1 finite statistics. N coincidences in total.
    #     Route V: N/2 in Z(x)Z and N/2 in X(x)X, p_hat = (E_zz + E_xx)/2 — exact: unbiased, variance (1 - p^2)/N.
    #     Route C: N/4 in each of the four CHSH settings, S_hat = E1 + E2 + E3 - E4 — exact: unbiased, variance 16 (1 - p^2/2)/N.
    #     Route T: N/9 in each of the nine Pauli settings, T_hat, S_hat = 2 sqrt(s1^2 + s2^2) of T_hat (plug-in).
    #     Pre-registered for route T on an isotropic pair at the Bell threshold p = 1/sqrt2: bias * sqrt(N) constant within
    #     15 % over N = 900, 9000, 90000, and P(S_hat > 2) > 0.6 at each N; control: route C declares S > 2 in half the trials.
    def _corr_hat(e_true, n, size, rng):
        return 2.0 * rng.binomial(n, (1 + np.asarray(e_true)) / 2, size=size) / n - 1.0

    def _route_t(t_true, n_tot, trials, rng):
        t_hat = _corr_hat(np.broadcast_to(t_true, (trials, 3, 3)), n_tot // 9, None, rng)
        sv = np.linalg.svd(t_hat, compute_uv=False)
        return 2.0 * np.sqrt(sv[:, 0] ** 2 + sv[:, 1] ** 2)

    print("\n6.7 FC-1 finite statistics, 20 seeds x 20000 trials per N")
    p_chk, n_chk = 0.9, 3600
    sd_v, sd_c, b_v, b_c = [], [], [], []
    for seed in range(20):
        rng = np.random.default_rng(6700 + seed)
        pv = 0.5 * (_corr_hat(p_chk, n_chk // 2, 20000, rng) + _corr_hat(p_chk, n_chk // 2, 20000, rng))
        e = p_chk / np.sqrt(2)
        sc = sum(_corr_hat(e, n_chk // 4, 20000, rng) for _ in range(3)) - _corr_hat(-e, n_chk // 4, 20000, rng)
        pc = sc / (2 * np.sqrt(2))
        sd_v.append(pv.std()); sd_c.append(pc.std()); b_v.append(pv.mean() - p_chk); b_c.append(pc.mean() - p_chk)
    sd_v, sd_c, b_v, b_c = map(np.array, (sd_v, sd_c, b_v, b_c))
    print(f"   exact laws, p = 0.9, N = 3600, seeds 6700-6719: route V sd*sqrt(N) = {sd_v.mean() * 60:.4f} ± {sd_v.std() * 60:.4f} "
          f"(sqrt(1-p^2) = {np.sqrt(1 - p_chk ** 2):.4f}), bias = {b_v.mean():+.2e} ± {b_v.std(ddof=1) / np.sqrt(20):.1e};  "
          f"route C sd*sqrt(N) = {sd_c.mean() * 60:.4f} ± {sd_c.std() * 60:.4f} (sqrt(2-p^2) = {np.sqrt(2 - p_chk ** 2):.4f}), "
          f"bias = {b_c.mean():+.2e} ± {b_c.std(ddof=1) / np.sqrt(20):.1e};  variance ratio C/V = {(sd_c.mean() / sd_v.mean()) ** 2:.3f} "
          f"((2-p^2)/(1-p^2) = {(2 - p_chk ** 2) / (1 - p_chk ** 2):.3f})")
    p_thr = 1 / np.sqrt(2)
    t_iso = np.diag([p_thr, -p_thr, p_thr])
    lam_bd = np.array([0.80, 0.10, 0.07, 0.03])                    # Bell-diagonal weights (Phi+, Phi-, Psi+, Psi-)
    t_bd = np.diag([lam_bd[0] - lam_bd[1] + lam_bd[2] - lam_bd[3], -lam_bd[0] + lam_bd[1] + lam_bd[2] - lam_bd[3],
                    lam_bd[0] + lam_bd[1] - lam_bd[2] - lam_bd[3]])
    s_bd = 2 * np.sqrt(np.sort(np.abs(np.diag(t_bd)))[::-1][:2] @ np.sort(np.abs(np.diag(t_bd)))[::-1][:2])
    # large-N limit of route T for an isotropic pair (added after the first run, to give the observed constants an
    # expectation): T_hat = T + E with independent Gaussian entries, variance 9 (1 - T_ij^2)/N; to first order
    # s1^2 + s2^2 = 2 p^2 + p (tr H - lambda_min(H)), H = G + G^T, G = R^T E, R = T/p, so S_hat - S = (tr H - lambda_min(H))/sqrt2.
    rng = np.random.default_rng(67)
    g_lim = rng.standard_normal((400000, 3, 3)) * 3.0
    g_lim[:, [0, 1, 2], [0, 1, 2]] *= np.sqrt(1 - p_thr ** 2)
    h_lim = g_lim + np.transpose(g_lim, (0, 2, 1))
    x_lim = (np.trace(h_lim, axis1=1, axis2=2) - np.linalg.eigvalsh(h_lim)[:, 0]) / np.sqrt(2)
    print(f"   Gaussian large-N limit for the isotropic pair (400000 draws, seed 67): bias*sqrt(N) -> {x_lim.mean():.4f} ± "
          f"{x_lim.std() / np.sqrt(len(x_lim)):.4f};  sd*sqrt(N) -> {x_lim.std():.4f};  P(S_hat > 2) -> {np.mean(x_lim > 0):.4f};  "
          f"route C control, leading skewness correction (also added after the first run): 1/2 + (2/sqrt3)/(6 sqrt(2 pi N)) = "
          + ", ".join(f"{0.5 + (2 / np.sqrt(3)) / (6 * np.sqrt(2 * np.pi * n)):.5f}" for n in (900, 9000, 90000)))
    import math

    def _exact_control(n_tot: int) -> float:
        """Route C at p = 1/sqrt2: every correlator has |E| = 1/2, so the number B of 'favourable' coincidences is
        Binomial(N, 3/4) and S_hat > 2 iff B > 3N/4.  Returns P(B > 3N/4) + P(B = 3N/4)/2 exactly."""
        k = np.arange(3 * n_tot // 4, n_tot + 1)
        logp = np.array([math.lgamma(n_tot + 1) - math.lgamma(x + 1) - math.lgamma(n_tot - x + 1) for x in k]) \
            + k * np.log(0.75) + (n_tot - k) * np.log(0.25)
        pm = np.exp(logp)
        return float(pm[1:].sum() + 0.5 * pm[0])

    exact_c = {n: _exact_control(n) for n in (900, 9000, 90000)}
    print("   route C control at the threshold, exact (binomial): P(S_hat > 2) + half the atom = "
          + ", ".join(f"{exact_c[n]:.5f}" for n in (900, 9000, 90000)) + " for N = 900, 9000, 90000")
    t_25 = np.diag([0.57, -0.57, 0.95])                           # rho_W(0.95) with |D| = 0.6 (T25): s2 = s3
    s_25 = 2 * 0.95 * np.sqrt(1 + 0.36)
    fc1 = {}
    for label, t_true, s_true in (("isotropic, p = 1/sqrt2 (S = 2)", t_iso, 2.0),
                                  (f"rho_W(0.95) with |D| = 0.6, singular values (0.95, 0.57, 0.57) (S = {s_25:.4f}; not pre-registered)", t_25, s_25),
                                  (f"Bell-diagonal, singular values (0.80, 0.74, 0.66) (S = {s_bd:.4f}; not pre-registered)", t_bd, s_bd)):
        print(f"   route T (plug-in from nine-setting tomography), {label}:")
        for j_n, n_tot in enumerate((900, 9000, 90000)):
            bias, sds, rate, rate_c = [], [], [], []
            for seed in range(20):
                rng = np.random.default_rng(6720 + 100 * j_n + seed)
                s_hat = _route_t(t_true, n_tot, 20000, rng)
                bias.append(s_hat.mean() - s_true); sds.append(s_hat.std()); rate.append(np.mean(s_hat > 2.0))
                n4 = n_tot // 4                                    # control in integer counts: S_hat = 2 K/n - 2
                kk = rng.binomial(n4, 0.75, size=(3, 20000)).sum(axis=0) - rng.binomial(n4, 0.25, size=20000)
                rate_c.append(np.mean(kk > 2 * n4) + 0.5 * np.mean(kk == 2 * n4))
            bias, sds, rate, rate_c = map(np.array, (bias, sds, rate, rate_c))
            se_b = bias.std(ddof=1) / np.sqrt(20)
            fc1[(label, n_tot)] = (bias.mean() * np.sqrt(n_tot), rate.mean(), rate_c.mean(), rate_c.std(ddof=1) / np.sqrt(20))
            extra = (f"P(S_hat > 2) = {rate.mean():.4f} ± {rate.std():.4f};  route C control P(S_hat > 2) + half the atom at 2 = "
                     f"{rate_c.mean():.4f} ± {rate_c.std():.4f} (± here: sd over seeds)") if s_true == 2.0 else f"bias*N = {bias.mean() * n_tot:.2f}"
            print(f"      N={n_tot:6d}: bias = {bias.mean():+.5f} ± {se_b:.1e} ({bias.mean() / se_b:+.0f} SE);  bias*sqrt(N) = "
                  f"{bias.mean() * np.sqrt(n_tot):.4f};  sd*sqrt(N) = {sds.mean() * np.sqrt(n_tot):.4f} ± {sds.std() * np.sqrt(n_tot):.4f};  {extra}")
    iso = [fc1[(k, n)] for (k, n) in fc1 if k.startswith("isotropic")]
    scaled = np.array([x[0] for x in iso])
    ok_scale = (scaled.max() - scaled.min()) / scaled.mean() <= 0.15
    ok_rate = all(x[1] > 0.6 for x in iso)
    ok_ctrl = all(abs(x[2] - 0.5) <= 2 * x[3] for x in iso)
    ok_fall = iso[2][1] >= iso[0][1]
    z_ctrl = ", ".join(f"{(x[2] - 0.5) / x[3]:+.1f}" for x in iso)
    z_skew = ", ".join(f"{(x[2] - exact_c[n]) / x[3]:+.1f}" for x, n in zip(iso, (900, 9000, 90000)))
    print(f"    pre-registered (a) bias*sqrt(N) constant within 15 % over the three N (isotropic): spread "
          f"{100 * (scaled.max() - scaled.min()) / scaled.mean():.1f} % — {'holds' if ok_scale else 'FAILS'};  "
          f"(b) P(S_hat > 2) > 0.6 at each N: {'holds' if ok_rate else 'FAILS'}, and 'the rate does not fall with N': "
          f"{'holds' if ok_fall else 'FAILS'} ({iso[0][1]:.4f} -> {iso[1][1]:.4f} -> {iso[2][1]:.4f}, toward the Gaussian limit above);  "
          f"control, route C at 0.5 within 2 SE at each N: {'holds' if ok_ctrl else 'FAILS'} (SE from 0.5: {z_ctrl}; SE from the exact "
          f"binomial value: {z_skew})")

    # 6.8 FC-2 the Bell tier under Stage 4's bath on one photon. rho_W(0.95); photon B's H/V relation carries D(t) of a
    #     bath of n modes (g_i, w_i ~ U(0.5, 1.5), |+> modes), T = 20, 2001 points, seeds 6800 + 100 n + s. The Bell tier is
    #     held iff |D| > sqrt(1/p^2 - 1), the key tier iff |D| > the bisection value below (T25). Pre-registered: seeds in
    #     which the Bell tier is lost and later regained — n = 4: >= 15/20; n = 8: between 1 and 8; n = 16: 0.
    #     (The pre-registration also called 'key tier regained in no more seeds than the Bell tier' a theorem; it is not —
    #     a pair can lose and regain the key tier without ever losing the Bell tier — and is not tested as one.)
    p_src = 0.95
    d_bell = np.sqrt(1 / p_src ** 2 - 1)
    d_key = _threshold(lambda c: pair_signals(relation_factor(werner_state(p_src), c, 1))["key_fraction"] > 1e-12, 0.0, 1.0)
    print(f"\n6.8 FC-2 Bell tier under Stage 4's bath on one photon of rho_W(0.95), T = 20, 20 seeds per n: Bell tier held iff "
          f"|D| > {d_bell:.4f}, key tier iff |D| > {d_key:.4f}")
    fc2, w_tier, w_nest = {}, 0, 0
    for n in (4, 8, 16):
        regained_b = regained_k = 0
        held_b, held_k, t_loss, t_loss_k, peak_after = [], [], [], [], []
        for seed in range(20):
            rng = np.random.default_rng(6800 + 100 * n + seed)
            dser = evolve_open(rho_coh, _random_bath(n, rng), t_grid)["D"][:, 0, 1]
            mod = np.abs(dser)
            bell, keyt = mod > d_bell, mod > d_key
            first_b = int(np.argmax(~bell)) if (~bell).any() else None
            first_k = int(np.argmax(~keyt)) if (~keyt).any() else None
            regained_b += int(first_b is not None and bell[first_b:].any())
            regained_k += int(first_k is not None and keyt[first_k:].any())
            held_b.append(bell.mean()); held_k.append(keyt.mean())
            t_loss.append(t_grid[first_b] if first_b is not None else np.inf)
            t_loss_k.append(t_grid[first_k] if first_k is not None else np.inf)
            w_nest += int(np.any(keyt & ~bell)) + int(t_loss_k[-1] > t_loss[-1]) + int(held_k[-1] > held_b[-1])
            if first_b is not None:                                # largest |D| after the first local minimum that follows the loss
                up = np.where(np.diff(mod[first_b:]) > 0)[0]
                peak_after.append(mod[first_b + up[0]:].max() if len(up) else mod[-1])
            else:
                peak_after.append(np.nan)
            for i in range(0, N_T, 100):                           # the threshold rule against the operation itself
                tiers = pair_tiers(pair_signals(relation_factor(werner_state(p_src), dser[i], 1)))
                w_tier += int(tiers[1] != bool(bell[i])) + int(tiers[0] != bool(keyt[i]))
        held_b, held_k, t_loss, peak_after = map(np.array, (held_b, held_k, t_loss, peak_after))
        fc2[n] = (regained_b, regained_k)
        print(f"   n={n:2d}: Bell tier lost and regained in {regained_b}/20 seeds, key tier in {regained_k}/20;  first loss of the Bell tier "
              f"at t = {t_loss.mean():.3f} ± {t_loss.std():.3f};  largest |D| after its first minimum = {np.nanmean(peak_after):.4f} ± "
              f"{np.nanstd(peak_after):.4f} (max {np.nanmax(peak_after):.4f});  fraction of the horizon with the Bell tier held = {held_b.mean():.4f} ± {held_b.std():.4f}, "
              f"key tier = {held_k.mean():.4f} ± {held_k.std():.4f}")
    ok4, ok8, ok16 = fc2[4][0] >= 15, 1 <= fc2[8][0] <= 8, fc2[16][0] == 0
    print(f"    threshold rule vs pair_tiers on the evolved pair at 21 times per seed: {w_tier} disagreements;  pre-registered n = 4 (>= 15): "
          f"{'holds' if ok4 else 'FAILS'};  n = 8 (1..8): {'holds' if ok8 else 'FAILS'};  n = 16 (0): {'holds' if ok16 else 'FAILS'};  "
          f"nesting in time (T24: key tier never held with the Bell tier lost; key tier first lost no later; key tier held for no "
          f"larger a fraction): {w_nest} violations in 60 seeds.  (The counts of seeds that regain a tier are not ordered by any theorem.)")

    # 6.9 Stand-ins for FC-3 (the substrate claim is not evaluated here). What the readings do when the degradation is
    #     not isotropic: (a) accidental coincidences from a partially polarised background — each side sees background
    #     light with Stokes vector pi_b along H/V, so the accidental pair state is a product of two partially polarised
    #     states, w = R_s/(R_s+R_b) = 0.9, p_source = 0.98; (b) a relation factor 1 - g on one photon of rho_W(0.9).
    print("\n6.9 stand-ins for FC-3: readings of one pair under degradations that are not isotropic (p_eff = p_source R_s/(R_s+R_b) = 0.8820 in (a))")
    for pol in (0.0, 0.2, 0.5, 0.8):
        side = 0.5 * (np.eye(2) + pol * _SZ)
        rho = 0.9 * werner_state(0.98) + 0.1 * np.kron(side, side)
        sig = pair_signals(rho)
        print(f"   (a) background polarisation {pol:.1f}: p_chsh={sig['p_chsh']:.4f}  p_qber={sig['p_qber']:.4f}  p_tel={sig['p_tel']:.4f}  "
              f"p_frame={sig['p_frame']:.4f}  C_l1={sig['C_l1']:.4f}  e_z={sig['qber_z']:.4f}  e_x={sig['qber_x']:.4f}  "
              f"p_chsh - p_tel = {sig['anisotropy']:.4f}")
    for g in (0.0, 0.01, 0.05, 0.1, 0.3):
        sig = pair_signals(relation_factor(werner_state(0.9), 1 - g, 1))
        c = 1 - g
        an = 0.9 * (np.sqrt((1 + c ** 2) / 2) - (1 + 2 * c) / 3)
        print(f"   (b) relation factor 1 - g, g = {g:.2f}: p_chsh={sig['p_chsh']:.4f}  p_qber={sig['p_qber']:.4f}  p_tel={sig['p_tel']:.4f}  "
              f"C_l1={sig['C_l1']:.4f}  p_chsh - p_tel = {abs(sig['anisotropy']) if abs(sig['anisotropy']) < 5e-13 else sig['anisotropy']:.4f} (closed form {an:.4f})")

    print("\nStage 6 summary: for a Werner pair the coherence of Stage 1 is the effective Werner parameter — C_l1 in the H/V")
    print("product basis and the heralded V_E both equal p, and p_eff = p_source R_s/(R_s+R_b) is the mixing rule (T21, T22); the")
    print("CHSH value, teleportation fidelity and error rates each read a different function of the pair's correlation matrix and")
    print("agree with each other and with the coherence on one p only when the degradation is isotropic, with")
    print("p_frame <= p_tel <= p_qber <= p_chsh always (T23); key, Bell, teleportation, entanglement and coherence tiers are nested for")
    print("every pair, and where each is lost belongs to the noise (T24); C_l1, C_re, V_E, the gap and the triangle phases cannot tell")
    print("a product register from an entangled one, since the two differ by a diagonal unitary of the register (T26); the")
    print("plug-in CHSH estimate from tomography is biased upward at order N^-1/2 whenever the second and third singular values")
    print("of the correlation matrix coincide (isotropic pairs, and every pair of T25); and the Bell tier of a pair whose one photon")
    print("meets Stage 4's bath is lost and regained for small baths and not for large ones.")
