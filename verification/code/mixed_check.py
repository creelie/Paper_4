"""Explicit checks of the theorems on mixed gauginos and on general gauge brackets.

Conventions are those of clifford.py (the program of the paper's appendices):
B(x, y) = x^T C y with C gamma C^{-1} = +-gamma^T, a real frame
n_i = (e_{t+i-1} + e_{i-1})/sqrt2, m_i = (e_{t+i-1} - e_{i-1})/sqrt2, and the
source term gamma(J ^ v) eps = sum_a J_a Xi^a eps with
Xi^a = k! gamma(e^a ^ n_1 ^ ... ^ n_k).

(A) Mixed gauginos.  For independent gauginos sigma in K_{chi_A}, y in K_{chi_B}
    and a parameter eps of chirality chi', the cross term

        X(eps) = sum_mu eta^{mu mu} gamma_mu sigma  B(eps, gamma_mu y)

    is compared with the best source term gamma(J ^ v) eps, J in C^D, fitted by
    least squares simultaneously for every eps in a basis of the parameter space.
    Prediction of the theorem: a solution exists exactly when D' in {4, 6} and
    sigma has the chirality of x = T eps, that is chi_A = (-1)^k chi'.  When it
    exists, the fitted residual part of J is proportional to G(sigma, y), the
    vector with components beta(sigma, gamma_mu y), beta(x, y) = B(T^{-1} x, y).

(D) General brackets.  For a single gaugino with sigma, y in K_chi, the
    anticommuting gaugino turns the part of the bracket f antisymmetric in its
    last two indices into S_+ and the symmetric part into S_-:

        S_+(eps) = gamma_mu sigma B(eps, gamma^mu y) + gamma_mu y B(eps, gamma^mu sigma),
        S_-(eps) = gamma_mu sigma B(eps, gamma^mu y) - gamma_mu y B(eps, gamma^mu sigma).

    Prediction: for D' = 10 the term S_+ is absorbed and S_- is not; for
    D' = 2 both vanish.

(E) Diagonal terms for D' = 4, 6.  For a single gaugino with a Lie bracket the
    cubic term S_+ vanishes identically when D' = 4 or 6, so the condition (M2)
    for a gaugino and a parameter that pair with each other holds with J = 0.

Nothing here is used as a proof; the checks confirm the written proofs.
"""
import itertools
import math
import os
import sys

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clifford import Clifford, antisym_product  # noqa: E402

rng = np.random.default_rng(20261030)
RESULTS = []


def report(name, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""), flush=True)


def crand(*shape):
    return rng.standard_normal(shape) + 1j * rng.standard_normal(shape)


def null_space(M, tol=1e-9):
    u, s, vh = np.linalg.svd(M)
    rank = int((s > tol * max(1.0, s.max() if s.size else 1.0)).sum())
    return vh[rank:].conj().T


class Setup:
    def __init__(self, s, t, k):
        c = Clifford(s, t)
        self.c, self.k, self.D = c, k, c.D
        self.G = [g.toarray() for g in c.G]
        self.eta = c.eta
        self.nvec, self.mvec, used = [], [], []
        for i in range(k):
            a, b = i, c.t + i
            nv = np.zeros(self.D); nv[a] = nv[b] = 1 / math.sqrt(2)
            mv = np.zeros(self.D); mv[b] = 1 / math.sqrt(2); mv[a] = -1 / math.sqrt(2)
            self.nvec.append(nv); self.mvec.append(mv); used += [a, b]
        self.resid = [m for m in range(self.D) if m not in used]
        self.Dp = len(self.resid)
        sl = lambda vec: sum(vec[m] * self.G[m] for m in range(self.D))
        self.ns = [sl(v) for v in self.nvec]
        self.ms = [sl(v) for v in self.mvec]
        self.K = {ch: self._kernel(self.ns, ch) for ch in (+1, -1)}
        self.Kh = {ch: self._kernel(self.ms, ch) for ch in (+1, -1)}
        self.Weyl = {+1: np.eye(c.dim)[:, c.plus], -1: np.eye(c.dim)[:, c.minus]}
        self.C = None
        for C in c.C_candidates:
            C = C.toarray()
            Ci = C.conj().T
            if any(all(np.abs(C @ g @ Ci - sg * g.T).max() < 1e-9 for g in self.G) for sg in (1, -1)):
                self.C = C
                break
        T = np.eye(c.dim, dtype=complex)
        for n in self.ns:
            T = T @ n
        self.T = T
        self.Xi = []
        for a in range(self.D):
            mats = [self.eta[a] * self.G[a]] + self.ns
            self.Xi.append(math.factorial(k) * antisym_product([sp.csr_matrix(m) for m in mats]).toarray())

    def _kernel(self, ops, ch):
        c = self.c
        E = np.eye(c.dim)[:, c.plus if ch == +1 else c.minus]
        if not ops:
            return E
        return E @ null_space(np.vstack([o @ E for o in ops]))

    def vec_pairing_nonzero(self, Eps, Y):
        """Is (eps, y) -> B(eps, gamma_mu y) nonzero for some residual mu?"""
        return max(np.abs(Eps.T @ self.C @ self.G[m] @ Y).max() for m in self.resid) > 1e-9


def absorb(S, lhs_cols, Eps):
    """Least-squares fit of lhs_cols (dim x n_eps) by sum_a J_a Xi^a Eps; relative residual and J."""
    A = np.stack([(S.Xi[a] @ Eps).ravel() for a in range(S.D)], axis=1)
    b = lhs_cols.ravel()
    J, *_ = np.linalg.lstsq(A, b, rcond=None)
    nb = np.linalg.norm(b)
    return (np.linalg.norm(A @ J - b) / nb if nb > 0 else 0.0), J, nb


def cross_cols(S, sg, y, Eps):
    C, G, eta = S.C, S.G, S.eta
    return sum(eta[m] * np.outer(G[m] @ sg, (C @ G[m] @ y) @ Eps) for m in range(S.D))


def check_mixed(s, t, k, eps_space="Khat"):
    S = Setup(s, t, k)
    found = 0
    for chi_e, chi_B, chi_A in itertools.product((+1, -1), repeat=3):
        Eps = S.Kh[chi_e] if eps_space == "Khat" else S.Weyl[chi_e]
        KB, KA = S.K[chi_B], S.K[chi_A]
        if not S.vec_pairing_nonzero(S.Kh[chi_e], KB):
            continue
        found += 1
        predicted = S.Dp in (4, 6) and chi_A == (-1) ** k * chi_e
        worst, cosmin = 0.0, 1.0
        for trial in range(3):
            sg = KA @ crand(KA.shape[1]); y = KB @ crand(KB.shape[1])
            res, J, nb = absorb(S, cross_cols(S, sg, y, Eps), Eps)
            if predicted:
                worst = max(worst, res)
                # G(sigma, y)_mu = B(T^{-1} sigma, gamma_mu y), residual components only;
                # T^{-1} sigma is any preimage in Khat of the chirality of sigma's partner
                Kh_src = S.Kh[(-1) ** k * chi_A]
                pre = Kh_src @ np.linalg.lstsq(S.T @ Kh_src, sg, rcond=None)[0]
                g = np.array([pre @ S.C @ S.G[m] @ y for m in S.resid])
                Jr = np.array([J[m] for m in S.resid])
                cos = abs(np.vdot(g, Jr)) / (np.linalg.norm(g) * np.linalg.norm(Jr))
                cosmin = min(cosmin, cos)
            else:
                worst = max(worst, 1.0 - res) if res < 1 else worst  # track closeness to zero
                worst = max(worst, 0.0)
                if trial == 0:
                    minres = res
                minres = min(minres, res)
        tag = f"({s},{t}) k={k} D'={S.Dp} chi'={chi_e:+d} chi_B={chi_B:+d} chi_A={chi_A:+d} eps in {eps_space}"
        if predicted:
            report(f"mixed {tag}: cross term absorbed, J residual parallel to G(sigma,y)",
                   worst < 1e-10 and cosmin > 1 - 1e-10,
                   f"residual {worst:.1e}, min |cos(J', G)| {cosmin:.12f}")
        else:
            report(f"mixed {tag}: cross term not absorbed", minres > 0.1,
                   f"least relative residual {minres:.3f}")
    report(f"mixed ({s},{t}) k={k}: at least one chirality pairing with B(eps, gamma y) != 0", found > 0,
           f"{found} configurations")


def check_bracket(s, t, k):
    S = Setup(s, t, k)
    for chi in (+1, -1):
        KL = S.K[chi]
        for chi_e in (+1, -1):
            if not S.vec_pairing_nonzero(S.Kh[chi_e], KL):
                continue
            Eps = S.Kh[chi_e]
            rp, rm, sp_, sm_ = [], [], [], []
            for trial in range(3):
                sg = KL @ crand(KL.shape[1]); y = KL @ crand(KL.shape[1])
                a1, a2 = cross_cols(S, sg, y, Eps), cross_cols(S, y, sg, Eps)
                Sp, Sm = a1 + a2, a1 - a2
                r1, _, n1 = absorb(S, Sp, Eps); r2, _, n2 = absorb(S, Sm, Eps)
                scale = np.abs(sg).max() * np.abs(y).max()
                rp.append(r1); rm.append(r2); sp_.append(n1 / scale); sm_.append(n2 / scale)
            tag = f"({s},{t}) k={k} D'={S.Dp} chi={chi:+d} chi'={chi_e:+d}"
            if S.Dp == 10:
                report(f"bracket {tag}: antisymmetric f absorbed (Nishino), symmetric f not",
                       max(rp) < 1e-10 and min(rm) > 0.1 and min(sm_) > 1e-6,
                       f"residuals {max(rp):.1e} and {min(rm):.3f}")
            elif S.Dp == 2:
                report(f"bracket {tag}: both terms vanish", max(sp_) < 1e-10 and max(sm_) < 1e-10,
                       f"sizes {max(sp_):.1e}, {max(sm_):.1e}")


def check_diagonal(s, t, k):
    S = Setup(s, t, k)
    for chi in (+1, -1):
        KL = S.K[chi]
        for chi_e in (+1, -1):
            if not S.vec_pairing_nonzero(S.Kh[chi_e], KL):
                continue
            Eps = S.Weyl[chi_e]
            sizes = []
            for trial in range(3):
                sg = KL @ crand(KL.shape[1]); y = KL @ crand(KL.shape[1])
                Sp = cross_cols(S, sg, y, Eps) + cross_cols(S, y, sg, Eps)
                sizes.append(np.abs(Sp).max() / (np.abs(sg).max() * np.abs(y).max()))
            report(f"diagonal ({s},{t}) k={k} D'={S.Dp} chi={chi:+d} chi'={chi_e:+d}: cubic term vanishes",
                   max(sizes) < 1e-12, f"size {max(sizes):.1e}")


def check_pure_trace(Dp_list):
    """j = -(D'-2)/N from the trace, and j^2 = 1 only for D' = 4, 6 (integers)."""
    sols = [Dp for Dp in Dp_list if (Dp - 2) == 2 ** (Dp // 2 - 1)]
    report("N = D' - 2 with N = 2^{D'/2-1} has the solutions D' = 4, 6 among even 4 <= D' <= 64",
           sols == [4, 6], f"solutions {sols}")


def main():
    check_pure_trace(list(range(4, 65, 2)))
    for (s, t, k) in [(2, 2, 0), (3, 1, 0), (3, 3, 1), (4, 4, 2),
                      (3, 3, 0), (5, 1, 0), (4, 4, 1),
                      (4, 4, 0), (5, 5, 1),
                      (9, 1, 0), (5, 5, 0), (10, 2, 1),
                      (6, 6, 0), (8, 8, 0), (9, 9, 2)]:
        check_mixed(s, t, k)
    for (s, t, k) in [(2, 2, 0), (3, 3, 1), (3, 3, 0), (4, 4, 1)]:
        check_mixed(s, t, k, eps_space="Weyl")
    for (s, t, k) in [(9, 1, 0), (10, 2, 1), (5, 5, 0), (6, 6, 1), (1, 1, 0), (2, 2, 1), (3, 3, 2)]:
        check_bracket(s, t, k)
    for (s, t, k) in [(2, 2, 0), (3, 3, 1), (4, 4, 2), (3, 3, 0), (4, 4, 1), (5, 5, 2)]:
        check_diagonal(s, t, k)
    print(f"{sum(RESULTS)} checks passed, {len(RESULTS) - sum(RESULTS)} failed")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
