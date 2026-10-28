"""Explicit checks of Proposition 7.1: the transfer of Nishino's construction
from (11+4n)+(3+4n) to (11+8n)+3, in 30 dimensions (27+3 against its source
19+11) and in 22 dimensions (19+3), with Sezgin's 11+3 as the control.

The gamma matrices are those of clifford.py (Pauli products, scipy sparse,
size 2^15 = 32768 in thirty dimensions).  Nothing here is used as a proof;
the checks only confirm the written arguments in explicit matrices.

Every check prints PASS or FAIL; the exit status is 1 if any check fails.
"""
import math
import sys

import numpy as np
import scipy.sparse as sp

from clifford import Clifford

rng = np.random.default_rng(20261028)
RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""), flush=True)


def crand(n):
    return rng.standard_normal(n) + 1j * rng.standard_normal(n)


def real_frame(c, k):
    """n_i = (e_space + e_time)/sqrt2, m_i = (e_space - e_time)/sqrt2."""
    ns, ms, used = [], [], []
    for i in range(k):
        a, b = i, c.t + i            # timelike generator a, spacelike b
        ns.append(((c.G[b] + c.G[a]) / math.sqrt(2)).tocsr())
        ms.append(((c.G[b] - c.G[a]) / math.sqrt(2)).tocsr())
        used += [a, b]
    resid = [m for m in range(c.D) if m not in used]
    return ns, ms, resid


def complex_frame(c, k):
    """n_i = (e_a + i e_b)/sqrt2 with two spacelike generators a, b."""
    ns, ms, used = [], [], []
    sp_idx = list(range(c.t, c.D))
    for i in range(k):
        a, b = sp_idx[2 * i], sp_idx[2 * i + 1]
        ns.append(((c.G[a] + 1j * c.G[b]) / math.sqrt(2)).tocsr())
        ms.append(((c.G[a] - 1j * c.G[b]) / math.sqrt(2)).tocsr())
        used += [a, b]
    resid = [m for m in range(c.D) if m not in used]
    return ns, ms, resid


def maxabs(M):
    M = sp.csr_matrix(M)
    return abs(M).max() if M.nnz else 0.0


def frame_relations(c, ns, ms):
    I = sp.identity(c.dim, format="csr")
    err = 0.0
    for i in range(len(ns)):
        for j in range(len(ns)):
            err = max(err, maxabs(ns[i] @ ns[j] + ns[j] @ ns[i]),
                      maxabs(ms[i] @ ms[j] + ms[j] @ ms[i]),
                      maxabs(ns[i] @ ms[j] + ms[j] @ ns[i] - 2 * (i == j) * I))
    return err


def chir_proj(c, chir):
    v = np.zeros(c.dim)
    v[c.plus if chir == +1 else c.minus] = 1.0
    return sp.diags(v).tocsr()


def corner_projector(c, ns, ms, occupied=True):
    """prod_i P_up_i (occupied) or prod_i P_down_i (empty)."""
    P = sp.identity(c.dim, dtype=complex, format="csr")
    for n, m in zip(ns, ms):
        P = P @ ((0.5 * n @ m) if occupied else (0.5 * m @ n))
    return P.tocsr()


def clifford_ok(c):
    """Clifford relations, checked on all pairs with a random test vector."""
    x = crand(c.dim)
    err = 0.0
    Gx = [g @ x for g in c.G]
    for a in range(c.D):
        for b in range(a, c.D):
            y = c.G[a] @ Gx[b] + c.G[b] @ Gx[a] - 2 * c.eta[a] * (a == b) * x
            err = max(err, np.abs(y).max())
    return err / np.abs(x).max()


# ---------------------------------------------------------------------------
# 1. The translation bracket: which degrees are symmetric on Delta_+ x Delta_+
# ---------------------------------------------------------------------------
def check_bracket(s, t, expected_sym):
    c = Clifford(s, t)
    C, _ = c.charge_conjugation(+1, +1)
    P = c.plus
    sym, anti, zero = [], [], []
    for p in range(0, c.r + 1):
        M = C.copy()
        for a in range(p):
            M = M @ c.G[a]
        blk = M[P][:, P].tocsr()
        if maxabs(blk) < 1e-12:
            zero.append(p)
        elif maxabs(blk - blk.T) < 1e-12:
            sym.append(p)
        elif maxabs(blk + blk.T) < 1e-12:
            anti.append(p)
    r = c.r
    ok = (sym == expected_sym and sym == [p for p in range(r + 1) if p % 4 == r % 4]
          and anti == [p for p in range(r + 1) if p % 4 == (r - 2) % 4]
          and zero == [p for p in range(r + 1) if p % 2 != r % 2])
    report(f"({s},{t}): degrees symmetric on Delta+ x Delta+ = {sym}; antisymmetric = {anti}; "
           f"zero = even degrees", ok)
    return c


# ---------------------------------------------------------------------------
# 2. Null frames, corners and the residual cubic term
# ---------------------------------------------------------------------------
def null_system(c, k, kind, label, expect_identity, bracket=True):
    ns, ms, resid = (real_frame if kind == "real" else complex_frame)(c, k)
    Dp = len(resid)
    err = frame_relations(c, ns, ms)
    Pocc = corner_projector(c, ns, ms, True)
    Pemp = corner_projector(c, ns, ms, False)
    dimK = int(round((Pocc @ chir_proj(c, +1)).diagonal().sum().real))
    expect_dimK = 2 ** (c.r - 1 - k)
    # annihilation: n_i K = 0, m_i Khat = 0
    x0 = Pocc @ crand(c.dim)
    e0 = Pemp @ crand(c.dim)
    ann = max(max(np.abs(n @ x0).max() for n in ns), max(np.abs(m @ e0).max() for m in ms))
    report(f"{label}: rank-{k} {kind} frame, n.n = m.m = 0, n_i.m_j = delta_ij; "
           f"dim K_+ = {dimK} = 2^{c.r - 1 - k}; residual D' = {Dp}",
           err < 1e-12 and dimK == expect_dimK and ann < 1e-10 * np.abs(x0).max())
    if kind != "real" or not bracket:
        return ns, ms, resid
    # Supersymmetry parameter and gaugino: Delta_+, lambda in K_+.
    eps_chir = +1 if c.r % 2 == 1 else -1
    C, _ = c.charge_conjugation(eps_chir, +1)
    Pe = chir_proj(c, eps_chir)
    T = sp.identity(c.dim, dtype=complex, format="csr")
    for n in ns:
        T = T @ n
    T = T.tocsr()

    def eps_hat():
        return Pemp @ (Pe @ crand(c.dim))

    a, b = eps_hat(), eps_hat()
    xa, xb = T @ a, T @ b
    # residual vector pairing G_mu(Ta, Tb) = B(a, gamma_mu T b)
    G = lambda u, w, mu: u @ (C @ (c.G[mu] @ w))
    # (N3): delta A_mu' = B(eps, gamma_mu' lambda) with lambda in K
    lam = Pocc @ (chir_proj(c, +1) @ crand(c.dim))
    dA = max(abs(eps_hat() @ (C @ (c.G[mu] @ lam))) for mu in resid)
    # (N4): xi^mu' = B(eps2, gamma^mu' T eps1) for unconstrained eps1, eps2,
    # nonzero and symmetric under 1 <-> 2
    e1, e2 = Pe @ crand(c.dim), Pe @ crand(c.dim)
    xi12 = np.array([e2 @ (C @ (c.G[mu] @ (T @ e1))) for mu in resid])
    xi21 = np.array([e1 @ (C @ (c.G[mu] @ (T @ e2))) for mu in resid])
    symm = np.abs(xi12 - xi21).max() / np.abs(xi12).max()
    report(f"{label}: delta A along V' and the translation xi^mu' do not vanish; "
           f"xi symmetric in eps1, eps2", dA > 1e-6 and np.abs(xi12).max() > 1e-6 and symm < 1e-10,
           f"max|dA|={dA:.2e}, max|xi|={np.abs(xi12).max():.2e}, asym={symm:.1e}")
    # cubic term Y = sum eta G_mu(x,x) gamma^mu x on the residual Weyl module
    Y = sum(c.eta[mu] * G(a, xa, mu) * (c.G[mu] @ xa) for mu in resid)
    rel = np.linalg.norm(Y) / (np.linalg.norm(a) * np.linalg.norm(xa) ** 2)
    holds = rel < 1e-10
    # weak identity: sum eta (y.G_mu x) gamma^mu x = j sum eta (x.G_mu x) gamma^mu y
    L = sum(c.eta[mu] * G(b, xa, mu) * (c.G[mu] @ xa) for mu in resid)
    R = sum(c.eta[mu] * G(a, xa, mu) * (c.G[mu] @ xb) for mu in resid)
    j = np.vdot(R, L) / np.vdot(R, R)
    res = np.linalg.norm(L - j * R) / np.linalg.norm(L)
    weak = res < 1e-10
    N = 2 ** (c.r - k - 1)
    report(f"{label}: residual Weyl module N = {N}, 2(D'-2) = {2 * (Dp - 2)}; "
           f"cubic identity holds = {holds}; identity (R) holds for some j = {weak}"
           + (f" (j = {j.real:+.4f})" if weak else ""),
           holds == expect_identity and weak == expect_identity and (N == 2 * (Dp - 2)) == expect_identity,
           f"|Y| rel {rel:.2e}, R residual {res:.2e}")
    return ns, ms, resid


def check_odd_ranks_vanish(c, label):
    """k = 1 and k = 3 give even-degree brackets, which vanish on Delta_+."""
    out = []
    eps_chir = +1 if c.r % 2 == 1 else -1
    C, _ = c.charge_conjugation(eps_chir, +1)
    Pe = chir_proj(c, eps_chir)
    for k in (1, 3):
        ns, ms, resid = real_frame(c, k)
        T = sp.identity(c.dim, dtype=complex, format="csr")
        for n in ns:
            T = T @ n
        e1, e2 = Pe @ crand(c.dim), Pe @ crand(c.dim)
        xi = max(abs(e2 @ (C @ (c.G[mu] @ (T @ e1)))) for mu in resid)
        out.append(xi)
    report(f"{label}: the translation bracket vanishes identically for k = 1 and k = 3",
           max(out) < 1e-10, f"max|xi| = {max(out):.1e}")


# ---------------------------------------------------------------------------
# 3. A complex frame of rank ten in 27+3: the occupied corner has no
#    Majorana spinor
# ---------------------------------------------------------------------------
def majorana_B(c):
    real = [g for g in c.G if maxabs(g - g.conj()) < 1e-12]
    imag = [g for g in c.G if maxabs(g + g.conj()) < 1e-12]
    for group in (imag, real):
        B = sp.identity(c.dim, dtype=complex, format="csr")
        for g in group:
            B = B @ g
        B = B.tocsr()
        Binv = B.conj().T.tocsr()                      # B is unitary
        if all(maxabs(B @ g.conj() @ Binv - g) < 1e-9 for g in c.G) \
                and maxabs(B @ B.conj() - sp.identity(c.dim)) < 1e-9:
            return B, Binv
    return None, None


def check_complex_majorana(c, k, label):
    ns, ms, _ = complex_frame(c, k)
    B, Binv = majorana_B(c)
    conj_ok = B is not None and all(maxabs(B @ n.conj() @ Binv - m) < 1e-9 for n, m in zip(ns, ms))
    Pocc = corner_projector(c, ns, ms, True)
    Z = np.column_stack([Pocc @ crand(c.dim) for _ in range(2 ** (c.r - k) + 8)])
    U, S, _ = np.linalg.svd(Z, full_matrices=False)
    rank = int((S > 1e-8 * S[0]).sum())
    K = U[:, :rank]
    # Majorana condition lambda = B conj(lambda) with lambda = K z:
    # K z - B conj(K) conj(z) = 0, a real-linear system in (Re z, Im z)
    BK = B @ K.conj()
    A = np.block([[K.real - BK.real, -K.imag - BK.imag],
                  [K.imag - BK.imag, K.real + BK.real]])
    sv = np.linalg.svd(A, compute_uv=False)
    null = int((sv < 1e-9 * sv[0]).sum())
    report(f"{label}: complex rank-{k} frame, B conj(n_i) B^-1 = m_i; occupied corner of "
           f"complex dimension {rank} contains {null} independent Majorana spinors",
           conj_ok and rank == 2 ** (c.r - k) and null == 0, f"smallest singular value {sv[-1]:.2e}")


def main():
    # Sezgin's 11+3 (Nishino n=0) as control, then the transferred signatures
    for s, t in [(11, 3), (19, 3), (27, 3), (19, 11)]:
        c = Clifford(s, t)
        report(f"Clifford relations in ({s},{t}), spinor dimension {c.dim}", clifford_ok(c) < 1e-12)
    c = check_bracket(27, 3, [3, 7, 11, 15])
    null_system(c, 2, "real", "(27,3)", False)
    null_system(c, 3, "real", "(27,3)", False, bracket=False)
    check_odd_ranks_vanish(c, "(27,3)")
    check_complex_majorana(c, 10, "(27,3)")
    c = check_bracket(19, 3, [3, 7, 11])
    null_system(c, 2, "real", "(19,3)", False)
    check_odd_ranks_vanish(c, "(19,3)")
    c = check_bracket(11, 3, [3, 7])
    null_system(c, 2, "real", "(11,3) [Sezgin]", True)
    c = check_bracket(19, 11, [3, 7, 11, 15])
    null_system(c, 10, "real", "(19,11) [Nishino n=2]", True)
    nfail = RESULTS.count(False)
    print(f"\n{len(RESULTS) - nfail} checks passed, {nfail} failed")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
