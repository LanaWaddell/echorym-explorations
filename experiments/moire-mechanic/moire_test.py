"""
Moire mechanic falsification test (Echorym DN v0.4, section 7.7)

CLAIM UNDER TEST:
  Two committed regions held in maintained phase produce joint effects that
  neither produces alone, with the phase relation (twist angle) determining
  whether combination is constructive or destructive, and with sharp special
  values (magic-angle analogue).

FALSIFIERS:
  F1. If joint outcomes do not depend on the twist angle -> mechanic is fake.
  F2. If a classical mixture with identical marginals reproduces the joint
      distribution -> "interference" is just correlation, mechanic is fake.
  F3. If joint observables equal the product of marginals -> no joint effect,
      mechanic is decorative.
  F4. If the effect survives full dephasing -> it is not coherence-dependent,
      so T2 / section 7.1 is not load-bearing for it.
  F5. If no mechanism produces SHARP special values -> the magic-angle part of
      the claim fails even if plain interference survives.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

# ---------- primitives ----------
I2 = np.eye(2, dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def cphase(theta):
    """Controlled-phase by theta. This IS the twist angle: a purely relational
    parameter. It is diagonal, so it changes NO single-region marginal."""
    g = np.eye(4, dtype=complex)
    g[3, 3] = np.exp(1j * theta)
    return g


def two_region_state(theta):
    """Region A and region B each enter in plural superposition, are coupled at
    relative twist theta, then re-interfered."""
    psi = np.array([1, 0, 0, 0], dtype=complex)      # |00>
    psi = kron(H, H) @ psi                            # each region made plural
    psi = cphase(theta) @ psi                         # the twist
    psi = kron(H, H) @ psi                            # interfere back
    return psi


def dephase(rho, gamma):
    """Relational dephasing: kills off-diagonal (phase) terms at strength gamma.
    gamma=0 fully coherent, gamma=1 fully dephased."""
    d = rho.shape[0]
    mask = np.full((d, d), 1.0 - gamma)
    np.fill_diagonal(mask, 1.0)
    return rho * mask


def expval(rho, op):
    return np.real(np.trace(rho @ op))


def marginals(rho):
    """Reduced density matrices for region A and region B."""
    r = rho.reshape(2, 2, 2, 2)
    rho_a = np.trace(r, axis1=1, axis2=3)
    rho_b = np.trace(r, axis1=0, axis2=2)
    return rho_a, rho_b


def concurrence(rho):
    Y = np.array([[0, -1j], [1j, 0]])
    YY = np.kron(Y, Y)
    R = rho @ YY @ rho.conj() @ YY
    ev = np.sqrt(np.clip(np.real(np.linalg.eigvals(R)), 0, None))
    ev = np.sort(ev)[::-1]
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])


# ---------- F1 / F3: does the twist do anything, and is it JOINT? ----------
print("=" * 74)
print("F1 + F3: twist-angle dependence, and joint vs. separable prediction")
print("=" * 74)
print(f"{'twist':>8} {'P(00)':>8} {'P(11)':>8} {'<X_A>':>8} {'<X_B>':>8} "
      f"{'<XX>':>8} {'<X><X>':>9} {'excess':>8} {'concur':>8}")

thetas = np.linspace(0, np.pi, 9)
for th in thetas:
    psi = two_region_state(th)
    rho = np.outer(psi, psi.conj())
    p = np.abs(psi) ** 2
    ra, rb = marginals(rho)
    xa, xb = expval(ra, X), expval(rb, X)
    xx = expval(rho, kron(X, X))
    print(f"{th/np.pi:>7.3f}pi {p[0]:>8.4f} {p[3]:>8.4f} {xa:>8.4f} {xb:>8.4f} "
          f"{xx:>8.4f} {xa*xb:>9.4f} {xx-xa*xb:>8.4f} {concurrence(rho):>8.4f}")

# ---------- F2: classical mixture with identical marginals ----------
print()
print("=" * 74)
print("F2: can a classical mixture with the SAME marginals reproduce it?")
print("=" * 74)
print(f"{'twist':>8} {'quantum P(00)':>15} {'classical P(00)':>17} {'gap':>10}")
for th in thetas:
    psi = two_region_state(th)
    rho = np.outer(psi, psi.conj())
    ra, rb = marginals(rho)
    rho_cl = np.kron(ra, rb)          # best separable model matching marginals
    q, c = np.abs(psi[0]) ** 2, np.real(rho_cl[0, 0])
    print(f"{th/np.pi:>7.3f}pi {q:>15.4f} {c:>17.4f} {q-c:>10.4f}")

# ---------- F4: is the effect coherence-dependent? ----------
print()
print("=" * 74)
print("F4: does relational dephasing destroy it? (T2 load-bearing?)")
print("=" * 74)
print(f"{'gamma':>8} {'contrast P(00)':>16} {'max concurrence':>17}")
for g in [0.0, 0.25, 0.5, 0.75, 1.0]:
    p00, con = [], []
    for th in np.linspace(0, np.pi, 41):
        psi = two_region_state(th)
        rho = np.outer(psi, psi.conj())
        # dephase at the coupling stage, then re-interfere
        mid = kron(H, H) @ np.diag(np.diag(cphase(th))) @ kron(H, H) @ \
              np.array([1, 0, 0, 0], dtype=complex)
        r_mid = np.outer(mid, mid.conj())
        psi2 = kron(H, H) @ cphase(th) @ kron(H, H) @ \
               np.array([1, 0, 0, 0], dtype=complex)
        r = np.outer(psi2, psi2.conj())
        r = dephase(r, g)
        p00.append(np.real(r[0, 0]))
        con.append(concurrence(r))
    print(f"{g:>8.2f} {max(p00)-min(p00):>16.4f} {max(con):>17.4f}")

# ---------- F5: sharp special values ----------
print()
print("=" * 74)
print("F5: SHARPNESS. product-state regions vs. entangled N-region states")
print("=" * 74)


def product_fringe(theta, n):
    """N independent regions, each acquiring phase theta. No entanglement."""
    return np.cos(theta / 2) ** (2 * n)


def ghz_fringe(theta, n):
    """N regions in a GHZ-type entangled state, phase theta each.
    Parity oscillates at N*theta -> N-fold narrower features."""
    return (1 + np.cos(n * theta)) / 2


def fwhm(f, n, span=np.pi):
    th = np.linspace(-span, span, 200001)
    y = f(th, n)
    y = (y - y.min()) / (y.max() - y.min())
    half = np.where(y >= 0.5)[0]
    # width of the central peak only
    c = np.argmin(np.abs(th))
    lo = c
    while lo > 0 and y[lo] >= 0.5:
        lo -= 1
    hi = c
    while hi < len(y) - 1 and y[hi] >= 0.5:
        hi += 1
    return th[hi] - th[lo]


print(f"{'N regions':>10} {'product FWHM':>14} {'entangled FWHM':>16} "
      f"{'sharpening':>12}")
for n in [1, 2, 4, 8, 16, 32]:
    wp, we = fwhm(product_fringe, n), fwhm(ghz_fringe, n)
    print(f"{n:>10} {wp:>14.4f} {we:>16.4f} {wp/we:>11.2f}x")

print()
print("scaling check (entangled): FWHM * N should be ~constant if 1/N")
for n in [2, 4, 8, 16, 32, 64]:
    print(f"   N={n:>3}  FWHM={fwhm(ghz_fringe, n):.6f}  FWHM*N={fwhm(ghz_fringe, n)*n:.4f}")
