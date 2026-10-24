# Verification and limits

The general deductions are proved in the manuscript. The original programs
`verification/code/verify.py` and `clifford.py` were retained unchanged and run
through `scripts/verify.py` for this package. All 34 checks must pass for a
successful run; the exact output, versions and source hashes are recorded in
`verification/current/` and the same command runs in GitHub CI.

The computations test finite explicit gamma matrices and sampled spinors in
double precision. Least-squares residuals distinguish the displayed examples;
they do not prove universal identities or supply field-theory existence.
The figure/table residuals retain the archived reference run. New runs need not
reproduce each floating-point residual bit for bit across BLAS implementations.

For optional figure regeneration, install `verification/code/requirements-figures.txt`
and run `python verification/code/figures/make_figures.py --output-dir PATH`.
The original archived plot data and construction are retained; only the default
output path was adapted to this package and the explicit destination option
added. The distributed vector PDFs are the reference figures and have not been
replaced by a new experiment. Byte-identical regenerated PDFs are not promised
across Matplotlib/font versions. The two general-proof diagrams are inline TikZ.

No Lean formalization of the general field-theoretic theorem is claimed.
Historical engine tests and the preceding package's page audit are explicitly
separated in `verification/previous/`. Current PDF page rendering and diagnostics
are recorded separately. Cite the exact release rather than an evolving branch.
