# AI provenance: Residual-dimension obstructions for null-projected supersymmetric Yang-Mills theories (fourth version)

Author and submitting contributor: Deep Bhattacharjee, ORCID 0000-0003-0466-750X.
Earlier versions: https://hexagonmath.org/2610.00471v1, https://hexagonmath.org/2610.00471v2, https://hexagonmath.org/2610.00471v3
Source: https://github.com/creelie/Paper_4 (release v2.2.0, https://doi.org/10.5281/zenodo.23789881; earlier packages of this version are release v2.1.1, https://doi.org/10.5281/zenodo.23789066, release v2.1.0, https://doi.org/10.5281/zenodo.23788708, and release v2.0.0, https://doi.org/10.5281/zenodo.23787988; all releases under the concept record https://doi.org/10.5281/zenodo.23612780; the third version is release v1.6.0, https://doi.org/10.5281/zenodo.23746593)

## Declarations

Writing: a mix of human writing and AI-generated text from ChatGPT-6.1 Sol Ultra
(OpenAI), Claude Code with Opus 5.5 (Ultracode) and Claude Code with Fable 5.1
(medium effort) (Anthropic).
Understanding: full human understanding. Every part of this contribution has been
checked by the author and is understood by him.

The understanding declaration is the author's own. It is not a statement by any AI
system that a human has read the work; the author confirms it by submitting.

## Who did what

**Deep Bhattacharjee** chose the problem and the direction of every version: the
null-projected setting, the five axioms (N1)-(N5) as the class of theories studied,
the decision to answer the 27+3 and 19+3 proposals of Rios, Marrani and Chester, and
the decision to write out the transfer of Nishino's construction in the third version, and the
decision to prove more of the open claims and to remove every citation of unrefereed
preprints in the fourth. He is
responsible for the mathematics, the citations and the claims, and confirms by
submitting that he has read and approved the manuscript.

**First version.** Claude Code (Anthropic) assisted the original preparation.

**Second version.** OpenAI Codex audited the proofs and assisted with the helicity-span
argument (Lemma 6.2), the null-frame current (Lemma A.1), corrections of scope and
editing.

**Third version.**
- ChatGPT-6.1 Sol Ultra (OpenAI) wrote an independent audit of whether the proposals of
  Phys. Rev. D 99 (2019) 046004 and Phys. Lett. B 808 (2020) 135674 fall under
  (N1)-(N5). It concluded that Nishino's unchanged real frame cannot be transferred
  to 27+3 or 19+3, that the rank-two alternative fails at the absorption step, and
  that the sources do not contain the field equations needed to decide other
  constructions. It also extracted the source texts and equation numbers.
- Claude Code (Opus 5.5 with Ultracode, and Fable 5.1 at medium effort) checked that audit against the source PDFs (it was accurate) and
  drafted, with the author, the new material: Section 7.1 with Proposition 7.1 and its
  four-step proof, Table 1, Remarks 7.2 and 7.3, Appendix D, the program
  transfer_check.py, Figures 8 and 9 and their generator make_transfer_figures.py,
  the new abstract and the corresponding changes to the introduction, conclusions and
  data availability.
- Claude Code checked every quotation in Section 7.1 word for word against the
  published PDFs of Rios, Marrani and Chester (2019, pp. 046004-4 and 046004-5;
  2020, p. 2 and footnote 2) and the author versions of Nishino (1998, eqs. (4.2)-(4.15))
  and Sezgin (1997); checked every DOI of the bibliography against Crossref, every
  arXiv identifier against arXiv and the Zenodo records against Zenodo; and rebuilt
  and read every page of the PDF.
- A second independent technical review of the third version, supplied by the author,
  re-derived the trace identities, the null ranks and the rank-two dimensions, reran
  both programs (24 and 34 checks passed), and found four statement-level points in
  Section 7. Claude Code checked each against the text, agreed with all four, and made
  the corrections: the opening of Section 7 no longer says that translations can arise
  only from null contractions (a footnote gives a spacelike contraction, outside
  (N1)-(N5)); the ten null vectors in Step 2 are tied to Nishino's own contraction;
  Proposition 7.1 now assumes a coupling g != 0 instead of deriving it from the gauge
  algebra, states that its conditions hold for all gaugino values allowed by (b) and
  all parameters, and treats rank zero separately. None of the four changes the
  theorems or the conclusion of Proposition 7.1.

**Fourth version.**
- Claude Code (Opus 5.5 with Ultracode, and Fable 5.1 at medium effort) proposed and
  drafted, with the author, Theorem 5.12 (the conditions of the Main Theorem are
  sufficient for residual dimension ten, by a frame-preserving complex isometry and a
  reality argument) with Corollary 5.13, and Theorem 7.3 (no fixed tensor u in a source
  J ^ u absorbs the cubic terms once the residual dimension exceeds 14, without (N4) and
  with or without a gaugino constraint) with Corollary 7.4; Appendix E, the program
  contraction_check.py, Figures 7 and 11 and their generator make_v4_figures.py.
- After the author asked to close the two questions that this version had left open,
  Claude Code proposed and drafted, with the author, Theorem 5.14 (Nishino's
  transformations give theories with residual dimension two in every (k+1)+(k+1), with
  vanishing cubic terms and off-shell closure) with Corollary 5.15 (the Main Theorem is a
  classification), Proposition 7.5 (several gauginos with their own parameters are
  impossible for residual dimension at least three) and Remark 7.16 (why no statement about
  the superalgebra alone can exclude every theory); Appendix F and the program
  residual_two_check.py; and, at the author's request, a shorter abstract that states the
  classification.
- After the author asked again to close the remaining open questions, a second Claude Code
  session drafted Theorems 7.6 and 7.11, Corollaries 7.7 and 7.12, Lemma 7.13, Proposition
  7.14 and Remark 7.15 (mixed gauginos, any bilinear gauge bracket, nonlinear rules and
  auxiliary fields) with the program mixed_check.py. Claude Code in this session re-derived
  every step, added Lemma 7.8 and Proposition 7.9 (the converse for residual dimension four
  and six, by representation theory) and twelve checks of the diagonal terms, corrected three
  statements that went beyond the proofs, moved the checks to Appendix G and updated the
  abstract. The corresponding changes were made to the introduction, Section 7.7,
  Remarks 7.16 and 7.17, the conclusions and the proof map.
- Claude Code identified the citations of unrefereed preprints (Truini-Marrani-Rios,
  arXiv:1909.00357; Banerjee, arXiv:2401.13706; two self-archived Zenodo copies of
  earlier versions), replaced the first by its published version (Expo. Math. 43 (2025)
  125621, checked in Crossref and on the publisher's abstract, which states that the Magic
  Star algebras are not Lie algebras), and removed the others; every remaining arXiv
  entry also carries a journal reference.
- The theorems of the fourth version did not use any material supplied from outside the
  session.

## What was checked, and what could not be

- Proofs: every step of Proposition 7.1, in its corrected statement, was re-derived by hand from Lemmas 2.2, 2.3,
  5.2, Proposition 2.1 and Theorems 3.3, 5.6; the numbers for 27+3 (D' = 26, N = 4096,
  j = -3/512, 4072 against 9/32) and 19+3 (D' = 18, N = 256 against 32) were
  recomputed.
- Programs: transfer_check.py, 24 checks passed, 0 failed (gamma matrices of size
  2^15 in 27+3, with Sezgin's 11+3 and Nishino's 19+11 as controls); verify.py,
  34 checks passed, 0 failed. These confirm the written proofs and do not replace them.
- Fourth version: every step of Theorems 5.12 and 7.3 was re-derived by hand, including the
  Fierz contraction sum over mu of gamma^mu gamma(omega) gamma_mu = (-1)^p (D'-2p) gamma(omega),
  the degree sets P' and the counts binom(12,2) = 66 and binom(14,3) = 364;
  contraction_check.py, 32 checks passed, 0 failed (absorption for arbitrary
  contractions, and the axioms in 9+1, 5+5, 1+9, 7+7, 2+10, 3+11 and 9+9 with residual
  dimension ten).
- Theorem 5.14 and Proposition 7.5 were re-derived by hand: the reduction of Phi(F) epsilon
  to c F(l+, l-) T epsilon, the vanishing of the cubic terms because gamma(l+) annihilates
  the gaugino space, the two commutators 2abc theta2 theta1 D_{l+} lambda and
  2abc theta2 theta1 F(l+, l-), and the invariant subspace W in Proposition 7.5;
  residual_two_check.py, 50 checks passed, 0 failed (the axioms and off-shell closure in
  1+1, 2+2, 3+3 and 4+4, Nishino's theories in 9+1 and 10+2 as controls, and nonzero
  cross terms of two gauginos for residual dimensions 4, 6, 8 and 10).
- Theorems 7.6 and 7.11, Lemmas 7.8 and 7.13 and Propositions 7.9 and 7.14 were re-derived
  by hand: the projection of the cross term to the occupied corner, the chirality step, the
  trace u = j G(sigma, y) with j = -(D'-2)/N, the swap that forces j^2 = 1 and N = D'-2, the
  separation of the symmetric and antisymmetric parts of a bracket, the case analysis of
  pi_2(delta E), and the decompositions (3,2), (2,3) for sl2 + sl2 and Sym^2 4 x 4 = 20 + 20
  for sl4; mixed_check.py, 122 checks passed, 0 failed.
- Build: pdflatex -jobname=output main.tex, three passes, 0 errors, 0 overfull or
  underfull boxes, no undefined references; 41 pages. Every page was rendered and read.
- References: all 40 DOIs resolve to the cited works (39 in Crossref, the Zenodo concept
  record in DataCite); all 21 arXiv identifiers match their titles and authors, and each
  of them belongs to a published work. Not verified online: Deligne, "Notes on spinors" (1999),
  which has no DOI and whose publisher page could not be reached from the session; the
  entry follows the printed volume. Lam's Graduate Studies in Mathematics 67 shows 2004
  in Crossref and 2005 on the printed book, and Lawson-Michelsohn's Spin Geometry shows
  1990 for its De Gruyter record against 1989 for the Princeton edition; the
  bibliography keeps the printed years. The reference added in version 2.2.0, Fulton and
  Harris, Representation Theory (GTM 129), resolves in Crossref (doi:10.1007/978-1-4612-0979-9).
- No general Lean formalisation is claimed. The gamma-matrix computations are finite
  numerical checks in double precision.

## Tools

OpenAI ChatGPT-6.1 Sol Ultra; Anthropic Claude Code with Opus 5.5 (Ultracode) and
with Fable 5.1 (medium effort); OpenAI Codex (second version); Python (NumPy, SciPy,
Matplotlib); LaTeX (pdfLaTeX, TikZ). The model versions are as declared by the author. AI systems are not listed as authors. No private prompts or chat transcripts
are included.
