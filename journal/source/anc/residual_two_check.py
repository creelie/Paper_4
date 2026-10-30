"""Explicit checks of the theorem on residual dimension two and of the proposition on
several gauginos.

For a real null frame n_1..n_k with v = n_1 ^ ... ^ n_k we take Nishino's
transformations

    delta A_mu = a eps-bar gamma_mu lambda,
    delta lambda = Phi(F) eps,  Phi(F) = (1/4) gamma^{mu nu rho_1..rho_k} F_{mu nu} v_{rho_1..rho_k},

with lambda in the joint kernel K of the n-slashes and F in Lambda^2(span(n) + V'),
which is the constraint F(n_i, .) = 0.  For Grassmann parameters the commutators are
symmetric parts of explicit matrices (see the comments below).  The program checks

  (a) the constraints are preserved: Phi(F) eps lies in K for every eps;
  (b) closure on A: [delta_1, delta_2] A(Y) = kappa_A F(xi, Y) for Y in V' + span(n);
  (c) closure on lambda: [delta_1, delta_2] lambda is the same translation acting on lambda,
      on shell, and for D' = 2 also off shell (both sides vanish on shell when D' = 2,
      because xi points along the null direction in which the field equation differentiates);
  (d) the part of delta(gamma^mu D_mu lambda) quadratic in lambda: it vanishes for every
      eps when D' = 2, and is nonzero (and absorbed, see contraction_check.py) when D' = 10;
  (e) (N3) and (N4): the residual components of delta A and xi are nonzero, and the
      bracket is symmetric;
  (f) several gauginos: the cross term gamma^mu lambda_A (eps_B-bar gamma_mu lambda_B)
      vanishes identically when D' = 2 and not when D' = 10;
  (g) several gauginos for D' = 4, 6, 8, 10 in several signatures: the cross term is nonzero.

Signatures with D' = 2: (1,1), (2,2), (3,3), (4,4) with k = s - 1.  Controls with
D' = 10: (9,1) with k = 0, (10,2) with k = 1.  Nothing here is used as a proof.
"""
import math
import sys

import numpy as np
import scipy.sparse as sp

from clifford import Clifford, antisym_product

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


def gamma_wedge(mats):
    if not mats:
        return None
    return antisym_product(mats).toarray() if sp.issparse(mats[0]) else antisym_product(mats)


class Setup:
    def __init__(self, s, t, k):
        c = Clifford(s, t)
        self.c, self.k, self.D = c, k, c.D
        G = [g.toarray() for g in c.G]
        self.G = G
        self.eta = c.eta
        # real frame: n_i = (e_{t+i} + e_i)/sqrt2, m_i = (e_{t+i} - e_i)/sqrt2 (upper components)
        self.nvec, self.mvec, used = [], [], []
        for i in range(k):
            a, b = i, c.t + i
            nv = np.zeros(self.D); nv[a] = nv[b] = 1 / math.sqrt(2)
            mv = np.zeros(self.D); mv[b] = 1 / math.sqrt(2); mv[a] = -1 / math.sqrt(2)
            self.nvec.append(nv); self.mvec.append(mv); used += [a, b]
        self.resid = [m for m in range(self.D) if m not in used]
        self.Dp = len(self.resid)
        self.slash = lambda vec: sum(vec[m] * G[m] for m in range(self.D))
        self.ns = [self.slash(v) for v in self.nvec]
        # K: chirality +1 joint kernel of the n-slashes
        self.Kb = self._chiral_kernel(+1) if self.ns else np.eye(c.dim)[:, c.plus]
        # parameter chirality and the pairing C
        self.choose_pairing()

    def _chiral_kernel(self, chir):
        c = self.c
        idx = c.plus if chir == +1 else c.minus
        E = np.eye(c.dim)[:, idx]
        M = np.vstack([n @ E for n in self.ns])
        Z = null_space(M)
        return E @ Z

    def choose_pairing(self):
        c = self.c
        lam = self.Kb @ crand(self.Kb.shape[1])
        for chie in (+1, -1):
            idx = c.plus if chie == +1 else c.minus
            for C in c.C_candidates:
                C = C.toarray()
                Cinv = C.conj().T
                if not any(all(np.abs(C @ g @ Cinv - sg * g.T).max() < 1e-9 for g in self.G)
                           for sg in (1, -1)):
                    continue
                vals = [np.abs((C @ self.G[m] @ lam)[idx]).max() for m in self.resid]
                if max(vals) > 1e-8:
                    self.C, self.chie, self.Eps = C, chie, np.eye(c.dim)[:, idx]
                    return
        raise RuntimeError("no pairing")

    def Gamma_up(self, a, b):
        """gamma^{a b rho_1..rho_k} v_{rho_1..rho_k} as k! gamma(e^a ^ e^b ^ n_1 ^ ... ^ n_k)."""
        mats = [self.eta[a] * self.G[a], self.eta[b] * self.G[b]] + self.ns
        return math.factorial(self.k) * antisym_product([sp.csr_matrix(m) for m in mats]).toarray()

    def Xi_up(self, a):
        """gamma^{a rho_1..rho_k} v_{rho_1..rho_k}."""
        mats = [self.eta[a] * self.G[a]] + self.ns
        return math.factorial(self.k) * antisym_product([sp.csr_matrix(m) for m in mats]).toarray()

    def allowed_F(self):
        """Random real 2-form in Lambda^2(span(n) + V'), as the matrix F_ab = F(e_a, e_b)."""
        basis = [np.eye(self.D)[m] for m in self.resid] + self.nvec
        # lower-index covectors: F(e_a,e_b) = sum c_ij (w_i(e_a) w_j(e_b) - ...), with w = eta u
        F = np.zeros((self.D, self.D))
        for i in range(len(basis)):
            for j in range(i + 1, len(basis)):
                wi, wj = self.eta * basis[i], self.eta * basis[j]
                x = rng.standard_normal()
                F += x * (np.outer(wi, wj) - np.outer(wj, wi))
        return F


def run(name, s, t, k, expect_cubic_zero):
    S = Setup(s, t, k)
    D, G, eta, C = S.D, S.G, S.eta, S.C
    Eps, Kb = S.Eps, S.Kb
    Gam = {(a, b): S.Gamma_up(a, b) for a in range(D) for b in range(D) if a != b}
    Phi = lambda F: 0.25 * sum(Gam[(a, b)] * F[a, b] for (a, b) in Gam)
    Xi = [S.Xi_up(a) for a in range(D)]
    # (a) constraint preserved
    F = S.allowed_F()
    out = Phi(F) @ Eps
    viol = max(np.abs(n @ out).max() for n in S.ns) if S.ns else 0.0
    report(f"{name}: Phi(F) eps lies in K for F(n_i, .) = 0", viol < 1e-9 * max(1, np.abs(out).max()),
           f"|n-slash Phi(F) eps| = {viol:.1e}")
    # (e) N3, N4
    lam = Kb @ crand(Kb.shape[1])
    dA = max(np.abs(Eps.T @ C @ G[m] @ lam).max() for m in S.resid)
    Y = [Eps.T @ C @ Xi[a] @ Eps for a in range(D)]
    xires = max(np.abs(Y[m]).max() for m in S.resid)
    asym = max(np.abs(y - y.T).max() for y in Y)
    report(f"{name}: (N3), (N4) residual delta A and xi nonzero, xi symmetric",
           dA > 1e-8 and xires > 1e-8 and asym < 1e-9 * max(1, xires),
           f"|dA'|={dA:.2e}, |xi'|={xires:.2e}, asymmetry={asym:.1e}")
    # (b) closure on A.  [d1,d2]A(Y) = a eps2^T (X + X^T) eps1 with X = C Yslash Phi(F)
    # (Grassmann parameters); F(xi, Y) = c eps2^T Z_Y eps1 with Z_Y = sum_nu C Xi^nu F(e_nu, Y)
    Ys = [np.eye(D)[m] for m in S.resid] + S.nvec
    lhs, rhs = [], []
    for trial in range(3):
        F = S.allowed_F()
        P = Phi(F)
        for yv in Ys:
            X = Eps.T @ C @ S.slash(yv) @ P @ Eps
            Fy = F @ yv                          # F(e_nu, Y)
            Z = sum(Y[nu] * Fy[nu] for nu in range(D))
            lhs.append((X + X.T).ravel()); rhs.append(Z.ravel())
    lhs, rhs = np.concatenate(lhs), np.concatenate(rhs)
    kA = (rhs.conj() @ lhs) / (rhs.conj() @ rhs)
    resA = np.linalg.norm(lhs - kA * rhs) / np.linalg.norm(lhs)
    report(f"{name}: closure on A gives the translation by xi", resA < 1e-10 and abs(kA) > 1e-8,
           f"kappa_A = {kA.real:+.4f}{kA.imag:+.4f}i, relative residual {resA:.1e}")
    # (c) closure on lambda.  Allowed X_mu = D_mu lambda: X_mu in K and n_i^mu X_mu = 0, and
    # on shell also sum_mu eta^{mu mu} gamma_mu X_mu = 0.  For Grassmann parameters and gaugino,
    # [d1,d2] lambda has the coefficient tensor
    #   L(o, alpha, beta) = (1/2) sum_{mu nu} [Gam^{mu nu}_{o beta} (C gamma_nu X_mu)_alpha
    #                                           + Gam^{mu nu}_{o alpha} (C gamma_nu X_mu)_beta]
    # and the translation xi^mu X_mu the tensor R(o, alpha, beta) = -sum_mu Y^mu_{alpha beta} X_mu(o).
    # With these conventions Nishino's theories (the controls) give L = -kappa_A R on shell.
    nk = Kb.shape[1]
    for onshell in ((True, False) if expect_cubic_zero else (True,)):
        rows = [np.hstack([nv[m] * Kb for m in range(D)]) for nv in S.nvec]
        if onshell:
            rows.append(np.hstack([eta[m] * G[m] @ Kb for m in range(D)]))
        Nsp = null_space(np.vstack(rows)) if rows else np.eye(D * nk)
        L, R, scale = [], [], 0.0
        for trial in range(4):
            coef = Nsp @ crand(Nsp.shape[1])
            Xs = [Kb @ coef[m * nk:(m + 1) * nk] for m in range(D)]
            scale = max(scale, max(np.abs(x).max() for x in Xs))
            T = np.zeros((S.c.dim, Eps.shape[1], Eps.shape[1]), dtype=complex)
            for (mu, nu), Gm in Gam.items():
                A = Gm @ Eps
                b = Eps.T @ C @ G[nu] @ Xs[mu]
                T += 0.5 * (A[:, None, :] * b[None, :, None] + A[:, :, None] * b[None, None, :])
            Rt = -sum(Y[mu][None, :, :] * Xs[mu][:, None, None] for mu in range(D))
            L.append(T.ravel()); R.append(Rt.ravel())
        L, R = np.concatenate(L), np.concatenate(R)
        res = np.linalg.norm(L + kA * R) / (scale * np.sqrt(L.size))
        nR = np.linalg.norm(R) / (scale * np.sqrt(R.size))
        what = "on shell" if onshell else "off shell"
        report(f"{name}: closure on lambda {what} is the translation by xi",
               Nsp.shape[1] > 0 and res < 1e-12,
               f"allowed D lambda of dimension {Nsp.shape[1]}, |L + kappa_A R| = {res:.1e}, "
               f"|R| = {nR:.1e}")
    # (d) cubic term for every eps in the Weyl module of the parameter
    l1, l2 = Kb @ crand(nk), Kb @ crand(nk)
    M = sum(eta[m] * (np.outer(G[m] @ l2, (C @ G[m] @ l1) @ Eps) +
                      np.outer(G[m] @ l1, (C @ G[m] @ l2) @ Eps)) for m in range(D))
    size = np.abs(M).max()
    scale = np.abs(l1).max() * np.abs(l2).max()
    zero = size < 1e-10 * scale
    report(f"{name}: cubic gaugino term {'vanishes' if expect_cubic_zero else 'is nonzero'}",
           zero == expect_cubic_zero, f"D'={S.Dp}, |cubic| = {size:.1e}")
    # (f) several gauginos: sum_mu eta gamma_mu sigma (eps-bar gamma_mu y), sigma and y independent
    sg, y = Kb @ crand(nk), Kb @ crand(nk)
    Mx = sum(eta[m] * np.outer(G[m] @ sg, (C @ G[m] @ y) @ Eps) for m in range(D))
    sx = np.abs(Mx).max()
    report(f"{name}: cross term of two gauginos {'vanishes' if expect_cubic_zero else 'is nonzero'}",
           (sx < 1e-10) == expect_cubic_zero, f"|cross| = {sx:.1e}")


def cross_only(name, s, t, k, trials=3):
    """(g) Several gauginos for D' >= 3: the cross term gamma^mu sigma (eps_B-bar gamma_mu y)
    is nonzero for independent sigma, y in K, so it cannot vanish identically."""
    S = Setup(s, t, k)
    G, eta, C, Eps, Kb = S.G, S.eta, S.C, S.Eps, S.Kb
    nk = Kb.shape[1]
    sizes = []
    for trial in range(trials):
        sg, y = Kb @ crand(nk), Kb @ crand(nk)
        Mx = sum(eta[m] * np.outer(G[m] @ sg, (C @ G[m] @ y) @ Eps) for m in range(S.D))
        sizes.append(np.abs(Mx).max() / (np.abs(sg).max() * np.abs(y).max()))
    report(f"{name}: D'={S.Dp}, cross term of two gauginos is nonzero", min(sizes) > 1e-6,
           f"least relative size {min(sizes):.2e}")


def main():
    run("(1,1), k=0", 1, 1, 0, True)
    run("(2,2), k=1", 2, 2, 1, True)
    run("(3,3), k=2", 3, 3, 2, True)
    run("(4,4), k=3", 4, 4, 3, True)
    run("(9,1), k=0 (control)", 9, 1, 0, False)
    run("(10,2), k=1 (control)", 10, 2, 1, False)
    for (s_, t_, k_) in [(3, 1, 0), (2, 2, 0), (3, 3, 1), (5, 1, 0), (3, 3, 0), (4, 4, 1),
                         (7, 1, 0), (5, 5, 1), (6, 6, 2), (9, 1, 0)]:
        cross_only(f"({s_},{t_}), k={k_}", s_, t_, k_)
    print(f"{sum(RESULTS)} checks passed, {len(RESULTS) - sum(RESULTS)} failed")
    sys.exit(0 if all(RESULTS) else 1)


if __name__ == "__main__":
    main()
