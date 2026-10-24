# Mathematical audit, 24 October 2026

## Exact result and hypotheses

The main theorem is a necessary obstruction for the class N1--N5 defined in the manuscript. The complexified gaugino value space is the full constrained Weyl corner. The gauge algebra is compact, non-abelian and a Lie algebra. The specified gauge variation and residual translation are nonzero. The translation bracket has the graded symmetry required by a supersymmetry anticommutator. The quadratic gaugino variation must be absorbed into the specified vector source for every allowed gaugino and parameter.

Within this class, a Majorana--Weyl gaugino gives k <= min(s,t), residual dimension s+t-2k in {2,10}, and s-t in {-8,0,8}. Passing these tests is not a sufficiency theorem. Several gauginos, further projections or smaller gaugino spaces, different transformations, additional fields and non-Lie extensions require separate analysis.

## Algebraic deductions checked

1. The real annihilator of a nonzero Majorana spinor is conjugation invariant and totally isotropic. Projection to each definite summand proves the real Witt bound.
2. The null-frame Clifford operators obey the fermionic oscillator relations. Their joint corners have residual Dirac-module structure; the spinor pairing couples opposite corners.
3. Projection of absorption to the occupied corner removes the null-direction terms. Nontrivial gauge variation and symmetric translation bracket identify a common residual Weyl module with a symmetric vector pairing.
4. The residual vector structure is explicitly transported through iota: Sigma_opp -> Sigma*. Both Clifford identities follow from cancellation of iota and its inverse.
5. Direct contraction fixes the residual current J^nu=-kappa(d-2)/N gamma^nu(S). This replaces an unnecessary multiplicity assertion. The gaugino tensors span the symmetric square, so absorption forces the displayed cubic identity.
6. Two contractions of that identity give N-(d-2)=-2j(d-2) and jN=-(d-2). Thus N=2(d-2), j=-1/2. Clifford-module divisibility leaves dimensions 3,4,6,10. For the residual Weyl module in dimension greater than two, only ten remains.
7. In residual dimension ten, the explicit source solves absorption for all parameters because both sides depend only on the empty-corner component. This solves absorption alone, without constructing the separate transformation Phi or full closure in every remaining signature.
8. The new null-current lemma proves the current is a wedge of the frame volume with a residual one-form by an oscillator occupancy argument. This supplies the comparison step for Nishino's source-current equation.
9. The auxiliary ordinary-SYM proposition now explicitly assumes dimension greater than two and a nondegenerate gaugino kinetic term. Without these hypotheses, a zero or total-derivative kinetic expression would not justify its conclusion. The main theorem separately allows residual dimension two.

## Independent single-time argument

The representation argument assumes positive-energy unitarity, one Majorana--Weyl set of supercharges and tensor charges that vanish on the massless multiplet. With S real supercharges, the active algebra has S/2 real generators, or S/4 complex creation operators, and at least 2^(S/4) states. A finite transverse helicity spectrum has span at least S/8. Scalar, spinor and vector polarizations have helicities in [-1,1], regardless of finite multiplicity, so S <= 16 is necessary for such a low-spin multiplet. At eighteen spacetime dimensions S=256, and the span is at least 32. This familiar extended-supersymmetry mechanism is attributed to the established representation literature; no new universal supersymmetry classification is claimed.

## Primary-source comparison and novelty limits

The audit inspected Nishino, hep-th/9708064v1, published in Nuclear Physics B 523 (1998) 450--464, especially the transformation, constraint, source and closure equations. It also inspected section III.A of Rios, Marrani and Chester, arXiv:1811.06101v3, published as Physical Review D 99 (2019) 046004. The revised comparison is restricted to a transfer satisfying N1--N5. The classification of Clifford modules and spinor pairings uses standard published references listed in the paper.

The exact general obstruction is the manuscript's proposed contribution. The helicity mechanism and ordinary dimension restrictions are established background. This audit does not certify absolute priority, exhaust all later citations or replace peer review. It removes unsupported claims of an exhaustive literature search and blanket exclusions of every possible theory in the specified signatures.

## Verification and trust

All 34 numerical checks in the original verification program passed in a fresh run. The log and exact source programs are included. They test explicit finite examples in double precision; no random or least-squares sample proves a general Clifford identity. Figure and table values remain the archived reference run, with the fresh run separately disclosed.

The Anaxia regression suite passed 320 tests with one skip, including the new helicity and scope checks. No full Lean formalisation of this field-theoretic theorem has been supplied. The engine's formal and human-review gates remain zero, and necessary-condition tests are not presented as existence certificates.

The PDF was rebuilt in JHEP style. All 27 current pages were rendered and visually inspected; the coordinate audit found no off-page words. The build has no overfull boxes or unresolved references. Formatting and computation do not certify journal acceptance.

## Paper_4 packaging update

The original sole byline is retained. The two summary passages that stated
residual dimension ten without its greater-than-two qualifier have been made
consistent with the theorem's explicit dimension-two exception. The numerical
appendix now gives the actual symmetric-square check range r=2,...,20.
References are ordered by first citation as required by JHEP. The archived
manuscript and current code release are cited separately, so the new PDF-only
Zenodo record is not described as a code archive.

These corrections do not supply an existence construction in every allowed
signature. The general theorem remains a written proof, not a Lean theorem.
The previously recorded 320-pass/one-skip Anaxia run is retained as historical
engine provenance; it was not rerun as a Paper_4 proof check and is not an
independent mathematical certificate. The final page count and current PDF QA
are recorded in `verification/current/page-audit.json`.
