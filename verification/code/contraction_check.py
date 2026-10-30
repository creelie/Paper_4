"""Explicit checks of Theorems 7.3 and 5.12: absorption of the cubic gaugino terms by a
source J ^ u, for an arbitrary fixed multivector u, null or not.

For each case we take random gaugino values lambda^1, lambda^2 in the allowed
space (the full Weyl module, or the occupied corner K of a real null frame),
form the cubic operator  eps -> sum_mu gamma^mu lambda^2 (eps-bar gamma_mu lambda^1)
+ (1 <-> 2), restricted to the supersymmetry parameters eps (the full Weyl
module, or its empty corner), and test by least squares whether it equals
eps -> gamma(J ^ u) eps for some vector J.  The expected outcome of each case is
the one predicted by Theorem 7.3 and is fixed in advance.  For Theorem 5.12
the program also checks, in signatures with residual dimension ten, that the residual
bilinears of (N3) and (N4) are nonzero, that the translation bracket is symmetric, and
that Nishino's null source absorbs the cubic terms.

The gamma matrices are those of clifford.py.  Nothing here is used as a proof.
Every check prints PASS or FAIL; the exit status is 1 if any check fails.
"""
import math
import sys

import numpy as np
import scipy.sparse as sp

from clifford import Clifford

rng = np.random.default_rng(20261030)
RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""), flush=True)


def crand(n):
    return rng.standard_normal(n) + 1j * rng.standard_normal(n)


def product(c, mats):
    out = sp.identity(c.dim, dtype=complex, format="csr")
    for m in mats:
        out = out @ m
    return out.tocsr()


def real_frame(c, k):
    ns, ms, used = [], [], []
    for i in range(k):
        a, b = i, c.t + i
        ns.append(((c.G[b] + c.G[a]) / math.sqrt(2)).tocsr())
        ms.append(((c.G[b] - c.G[a]) / math.sqrt(2)).tocsr())
        used += [a, b]
    resid = [m for m in range(c.D) if m not in used]
    return ns, ms, resid


def subspace_basis(c, chir, projs):
    """Orthonormal basis (columns) of the chirality-chir part of the joint image of projs."""
    v = np.zeros(c.dim)
    v[c.plus if chir == +1 else c.minus] = 1.0
    P = sp.diags(v).tocsr()
    for Q in projs:
        P = (Q @ P).tocsr()
    Pd = P.toarray()
    u, svals, _ = np.linalg.svd(Pd)
    rank = int((svals > 1e-8).sum())
    return u[:, :rank]


def run_case(name, s, t, k, u_of, expect_solvable):
    """u_of(c, ns, resid) returns a list of (coef, list of sparse factors) giving gamma(J ^ u)
    as J ranges over a basis: it returns a function a -> sparse matrix gamma(e_a ^ u)."""
    c = Clifford(s, t)
    ns, ms, resid = real_frame(c, k)
    I = sp.identity(c.dim, format="csr")
    up = [(0.5 * n @ m).tocsr() for n, m in zip(ns, ms)]
    dn = [(0.5 * m @ n).tocsr() for n, m in zip(ns, ms)]
    # gaugino chirality +1 in the occupied corner; parameter chirality chosen by the pairing
    lam_basis = subspace_basis(c, +1, up)
    chosen = None
    for chie in (+1, -1):
        C, _ = c.charge_conjugation(chie, +1)
        if C is not None:
            chosen = (chie, C)
            break
    chie, C = chosen
    eps_basis = subspace_basis(c, chie, dn)
    gam = c.G
    eta = c.eta
    l1 = lam_basis @ crand(lam_basis.shape[1])
    l2 = lam_basis @ crand(lam_basis.shape[1])
    M = np.zeros((c.dim, eps_basis.shape[1]), dtype=complex)
    for mu in range(c.D):
        g1 = gam[mu] @ l1
        g2 = gam[mu] @ l2
        r1 = eps_basis.T @ (C @ g1)
        r2 = eps_basis.T @ (C @ g2)
        M += eta[mu] * (np.outer(g2, r1) + np.outer(g1, r2))
    size = np.abs(M).max()
    cols = []
    for a in range(c.D):
        Ga = u_of(c, ns, resid, a)
        cols.append((Ga @ eps_basis).reshape(-1))
    F = np.stack(cols, axis=1)
    y = M.reshape(-1)
    if size < 1e-12:
        resid_rel = 0.0
    else:
        coef, *_ = np.linalg.lstsq(F, y, rcond=None)
        resid_rel = np.linalg.norm(F @ coef - y) / np.linalg.norm(y)
    solvable = resid_rel < 1e-10
    report(f"{name}: absorption {'solvable' if expect_solvable else 'impossible'}",
           solvable == expect_solvable,
           f"D'={c.D - 2 * k}, |cubic|={size:.2e}, relative residual={resid_rel:.2e}")


def wedge_basis(c, a, factors_idx, ns=None, include_null=False):
    """gamma(e_a ^ e_{i1} ^ ... ) for orthonormal e_i, times the null product if requested."""
    if a in factors_idx:
        return sp.csr_matrix((c.dim, c.dim), dtype=complex)
    mats = [c.G[a]] + [c.G[i] for i in factors_idx]
    return product(c, mats)


def u_scalar(c, ns, resid, a):
    return c.G[a]


def u_spacelike(idx):
    def f(c, ns, resid, a):
        return wedge_basis(c, a, idx)
    return f


def u_null_times(idx):
    """u = n_1 ^ ... ^ n_k ^ e_idx with e_idx residual and orthonormal.  For a basis vector e_a,
    gamma(e_a ^ u) is the antisymmetrised product; e_a is either residual (then it
    anticommutes with everything) or lies in the frame plane."""
    def f(c, ns, resid, a):
        vecs = [c.G[a]] + list(ns) + [c.G[i] for i in idx]
        # antisymmetrise only the e_a slot: the remaining factors are mutually orthogonal.
        # gamma(e_a ^ w) = (e_a w + (-1)^{deg w} w e_a)/2 for a product w of orthogonal vectors
        w = product(c, vecs[1:])
        deg = len(vecs) - 1
        return (0.5 * (c.G[a] @ w + (-1) ** deg * w @ c.G[a])).tocsr()
    return f


def axioms_case(name, s, t, k):
    """For a real frame of rank k with D' = 10: the residual bilinears of (N3) and (N4) are
    nonzero, the translation bracket is symmetric, and absorption is solvable."""
    c = Clifford(s, t)
    ns, ms, resid = real_frame(c, k)
    up = [(0.5 * n @ m).tocsr() for n, m in zip(ns, ms)]
    dn = [(0.5 * m @ n).tocsr() for n, m in zip(ns, ms)]
    lam_basis = subspace_basis(c, +1, up)
    chie = +1 if k % 2 == 0 else -1          # chi' = (-1)^k chi
    C = None
    for cand in c.C_candidates:
        Cinv = cand.conj().T.tocsr()
        for sign in (+1, -1):
            if all(abs(cand @ g @ Cinv - sign * g.T).max() < 1e-9 for g in c.G):
                blk = eps_test = None
                C = cand if C is None else C
    eps_basis = subspace_basis(c, chie, dn)
    T = product(c, ns)
    # (N3): residual components of eps-bar gamma_mu lambda
    l = lam_basis @ crand(lam_basis.shape[1])
    e1 = eps_basis @ crand(eps_basis.shape[1])
    e2 = eps_basis @ crand(eps_basis.shape[1])
    best = None
    for cand in c.C_candidates:
        n3 = max(abs(e1 @ (cand @ (c.G[mu] @ l))) for mu in resid)
        xi12 = np.array([e2 @ (cand @ (c.G[mu] @ (T @ e1))) for mu in resid])
        xi21 = np.array([e1 @ (cand @ (c.G[mu] @ (T @ e2))) for mu in resid])
        if n3 > 1e-8 and np.abs(xi12).max() > 1e-8:
            best = (n3, np.abs(xi12).max(), np.abs(xi12 - xi21).max())
            break
    ok = best is not None and best[2] < 1e-9 * max(1.0, best[1])
    report(f"{name}: (N3) and (N4) residual bilinears nonzero, bracket symmetric", ok,
           "no compatible pairing" if best is None else
           f"|dA'|={best[0]:.2e}, |xi'|={best[1]:.2e}, asymmetry={best[2]:.1e}")
    run_case(f"{name}, w = 1", s, t, k, u_null_times(()), True)


def main():
    # Unconstrained Weyl gaugino (k = 0).
    run_case("(9,1), u = 1", 9, 1, 0, u_scalar, True)
    run_case("(9,1), u = e_9", 9, 1, 0, u_spacelike((9,)), False)
    run_case("(5,5), u = 1", 5, 5, 0, u_scalar, True)
    run_case("(7,1), u = e_1..e_7", 7, 1, 0, u_spacelike(tuple(range(1, 8))), True)
    run_case("(7,1), u = 1", 7, 1, 0, u_scalar, False)
    run_case("(11,1), u = 1", 11, 1, 0, u_scalar, False)
    run_case("(11,1), u = e_1", 11, 1, 0, u_spacelike((1,)), False)
    run_case("(11,1), u = e_1..e_9", 11, 1, 0, u_spacelike(tuple(range(1, 10))), False)
    run_case("(11,3), u = e_3..e_12", 11, 3, 0, u_spacelike(tuple(range(3, 13))), False)
    run_case("(9,7), u = e_7", 9, 7, 0, u_spacelike((7,)), False)
    # Real null frames, u = n_1 ^ ... ^ n_k ^ w with w residual.
    run_case("(11,3), k=2, w = 1 (Sezgin)", 11, 3, 2, u_null_times(()), True)
    run_case("(11,3), k=2, w = e_13", 11, 3, 2, u_null_times((13,)), False)
    run_case("(11,3), k=1, w = 1", 11, 3, 1, u_null_times(()), False)
    run_case("(11,3), k=1, w = e_12", 11, 3, 1, u_null_times((12,)), False)
    run_case("(19,3), k=2, w = 1", 19, 3, 2, u_null_times(()), False)
    run_case("(19,3), k=2, w = e_21", 19, 3, 2, u_null_times((21,)), False)
    run_case("(19,3), k=3, w = e_12..e_21", 19, 3, 3, u_null_times(tuple(range(12, 22))), False)
    run_case("(19,3), k=1, w = e_14..e_21", 19, 3, 1, u_null_times(tuple(range(14, 22))), False)
    # Theorem 5.12: the signatures with D' = 10 reached by complex isometries.
    axioms_case("(9,1), k=0", 9, 1, 0)
    axioms_case("(5,5), k=0", 5, 5, 0)
    axioms_case("(1,9), k=0", 1, 9, 0)
    axioms_case("(7,7), k=2", 7, 7, 2)
    axioms_case("(2,10), k=1", 2, 10, 1)
    axioms_case("(3,11), k=2", 3, 11, 2)
    axioms_case("(9,9), k=4", 9, 9, 4)
    print(f"{sum(RESULTS)} checks passed, {len(RESULTS) - sum(RESULTS)} failed")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
