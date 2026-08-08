"""Corrected F3/F4: dephase DURING coupling, and use a non-degenerate observable."""
import numpy as np

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
    g = np.eye(4, dtype=complex)
    g[3, 3] = np.exp(1j * theta)
    return g


def dephase(rho, gamma):
    d = rho.shape[0]
    mask = np.full((d, d), 1.0 - gamma)
    np.fill_diagonal(mask, 1.0)
    return rho * mask


def run(theta, gamma):
    """Prepare -> twist -> DEPHASE (relation decays here) -> re-interfere."""
    psi = kron(H, H) @ np.array([1, 0, 0, 0], dtype=complex)
    psi = cphase(theta) @ psi
    rho = np.outer(psi, psi.conj())
    rho = dephase(rho, gamma)                 # T2 acting on the relation
    U = kron(H, H)
    return U @ rho @ U.conj().T


def expval(rho, op):
    return np.real(np.trace(rho @ op))


def marginals(rho):
    r = rho.reshape(2, 2, 2, 2)
    return np.trace(r, axis1=1, axis2=3), np.trace(r, axis1=0, axis2=2)


def concurrence(rho):
    Y = np.array([[0, -1j], [1j, 0]])
    YY = np.kron(Y, Y)
    R = rho @ YY @ rho.conj() @ YY
    ev = np.sqrt(np.clip(np.real(np.linalg.eigvals(R)), 0, None))
    ev = np.sort(ev)[::-1]
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])


print("=" * 78)
print("F3 (corrected): joint observable <ZZ> vs product of marginals <Z><Z>")
print("=" * 78)
print(f"{'twist':>9} {'<Z_A>':>9} {'<Z_B>':>9} {'<ZZ>':>9} {'<Z><Z>':>9} "
      f"{'EXCESS':>9} {'concur':>8}")
for th in np.linspace(0, np.pi, 9):
    rho = run(th, 0.0)
    ra, rb = marginals(rho)
    za, zb = expval(ra, Z), expval(rb, Z)
    zz = expval(rho, kron(Z, Z))
    print(f"{th/np.pi:>8.3f}pi {za:>9.4f} {zb:>9.4f} {zz:>9.4f} {za*zb:>9.4f} "
          f"{zz-za*zb:>9.4f} {concurrence(rho):>8.4f}")

print()
print("=" * 78)
print("F4 (corrected): dephasing applied to the RELATION during coupling")
print("=" * 78)
print(f"{'gamma':>7} {'P(00) contrast':>16} {'max |excess|':>14} "
      f"{'max concur':>12} {'twist dependence':>18}")
for g in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    p00, exc, con = [], [], []
    for th in np.linspace(0, np.pi, 61):
        rho = run(th, g)
        ra, rb = marginals(rho)
        za, zb = expval(ra, Z), expval(rb, Z)
        exc.append(abs(expval(rho, kron(Z, Z)) - za * zb))
        p00.append(np.real(rho[0, 0]))
        con.append(concurrence(rho))
    contrast = max(p00) - min(p00)
    print(f"{g:>7.2f} {contrast:>16.4f} {max(exc):>14.4f} {max(con):>12.4f} "
          f"{'YES' if contrast > 1e-6 else 'GONE':>18}")

print()
print("=" * 78)
print("F2b: quantum vs best classical (separable) model, at full coherence")
print("=" * 78)
gaps = []
for th in np.linspace(0, np.pi, 61):
    rho = run(th, 0.0)
    ra, rb = marginals(rho)
    cl = np.kron(ra, rb)
    gaps.append(np.real(rho[0, 0]) - np.real(cl[0, 0]))
print(f"  max separable-model error : {max(np.abs(gaps)):.4f}")
print(f"  at twist                  : {np.linspace(0,np.pi,61)[int(np.argmax(np.abs(gaps)))]/np.pi:.3f}pi")

# Does a classical model with a free correlation parameter fit?
print()
print("  Can ANY classical two-outcome model reproduce the full twist sweep?")
print("  (classical: P(00) must be linear in any mixing parameter; quantum is")
print("   cos^2 in theta/2 -> nonlinear. Checking curvature:)")
th = np.linspace(0, np.pi, 61)
p = np.array([np.real(run(t, 0.0)[0, 0]) for t in th])
print(f"  quantum P(00)(theta) fits cos^4(theta/4)+...: max|d2P/dth2| = "
      f"{np.max(np.abs(np.gradient(np.gradient(p, th), th))):.4f}  (0 would mean linear/classical)")
