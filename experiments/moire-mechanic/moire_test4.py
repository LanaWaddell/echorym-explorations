"""F5 scaling + CHSH via the analytic Horodecki criterion (no grid search).
S_max = 2*sqrt(m1 + m2), where m1,m2 are the two largest eigenvalues of
T^T T and T is the 3x3 correlation matrix T_ij = <sigma_i (x) sigma_j>."""
import numpy as np


def fwhm(y, th):
    y = (y - y.min()) / (y.max() - y.min())
    c = int(np.argmin(np.abs(th)))
    lo = c
    while lo > 0 and y[lo] >= 0.5:
        lo -= 1
    hi = c
    while hi < len(y) - 1 and y[hi] >= 0.5:
        hi += 1
    return th[hi] - th[lo]


th = np.linspace(-np.pi, np.pi, 400001)

print("=" * 76)
print("F5a: SCALING LAW - product-state regions vs entangled regions")
print("=" * 76)
print(f"{'N':>5} {'product FWHM':>14} {'x sqrt(N)':>11} | {'entangled FWHM':>15} {'x N':>9}")
for n in [2, 4, 8, 16, 32, 64, 128]:
    wp = fwhm(np.cos(th / 2) ** (2 * n), th)
    we = fwhm((1 + np.cos(n * th)) / 2, th)
    print(f"{n:>5} {wp:>14.5f} {wp*np.sqrt(n):>11.4f} | {we:>15.5f} {we*n:>9.4f}")
print()
print("  product   : FWHM x sqrt(N) constant -> width ~ 1/sqrt(N)   (shot-noise limit)")
print("  entangled : FWHM x N       constant -> width ~ 1/N         (Heisenberg limit)")

# ---------------- CHSH ----------------
I2 = np.eye(2, dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]], dtype=complex)
P = [X, Y, Z]


def cphase(t):
    g = np.eye(4, dtype=complex)
    g[3, 3] = np.exp(1j * t)
    return g


def state(t):
    return cphase(t) @ (np.kron(H, H) @ np.array([1, 0, 0, 0], dtype=complex))


def dephase(rho, g):
    m = np.full((4, 4), 1.0 - g)
    np.fill_diagonal(m, 1.0)
    return rho * m


def chsh_max(rho):
    T = np.array([[np.real(np.trace(rho @ np.kron(P[i], P[j])))
                   for j in range(3)] for i in range(3)])
    ev = np.sort(np.linalg.eigvalsh(T.T @ T))[::-1]
    return 2 * np.sqrt(max(0.0, ev[0] + ev[1]))


def concurrence(rho):
    YY = np.kron(Y, Y)
    R = rho @ YY @ rho.conj() @ YY
    ev = np.sort(np.sqrt(np.clip(np.real(np.linalg.eigvals(R)), 0, None)))[::-1]
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])


print()
print("=" * 76)
print("CHSH: is the twist-generated entanglement Bell-certifiable?")
print("=" * 76)
print(f"{'twist':>10} {'concurrence':>13} {'CHSH S_max':>12} {'violates 2?':>13}")
for t in np.linspace(0, np.pi, 9):
    rho = np.outer(state(t), state(t).conj())
    print(f"{t/np.pi:>9.3f}pi {concurrence(rho):>13.4f} {chsh_max(rho):>12.4f} "
          f"{'YES' if chsh_max(rho) > 2.0001 else 'no':>13}")
print(f"\n  Tsirelson bound = {2*np.sqrt(2):.4f}")

print()
print("=" * 76)
print("CHSH under relational dephasing (twist = pi, max entanglement)")
print("=" * 76)
print(f"{'gamma':>8} {'concurrence':>13} {'CHSH S_max':>12} {'violates 2?':>13}")
for g in [0.0, 0.15, 0.29, 0.3, 0.5, 0.75, 1.0]:
    rho = dephase(np.outer(state(np.pi), state(np.pi).conj()), g)
    print(f"{g:>8.2f} {concurrence(rho):>13.4f} {chsh_max(rho):>12.4f} "
          f"{'YES' if chsh_max(rho) > 2.0001 else 'no':>13}")
