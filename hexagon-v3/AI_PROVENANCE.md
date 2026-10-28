# AI provenance: Residual-dimension obstructions for null-projected supersymmetric Yang-Mills theories (third version)

Author and submitting contributor: Deep Bhattacharjee, ORCID 0000-0003-0466-750X.
Earlier versions: https://hexagonmath.org/2610.00471v1, https://hexagonmath.org/2610.00471v2
Source and programs: https://github.com/creelie/Paper_4 (release v1.5.0)

## Declarations

Writing: a mix of human-written and AI-generated text.
Understanding: full human understanding. All parts of this contribution have been
checked and understood by a human.

The understanding declaration is the author's own. It is not a statement by any AI
system that a human has read the work; the author confirms it by submitting.

## Who did what

**Deep Bhattacharjee** chose the problem and the direction of every version: the
null-projected setting, the five axioms (N1)-(N5) as the class of theories studied,
the decision to answer the 27+3 and 19+3 proposals of Rios, Marrani and Chester, and
the decision to write out the transfer of Nishino's construction in this version. He is
responsible for the mathematics, the citations and the claims, and confirms by
submitting that he has read and approved the manuscript.

**First version.** Claude Code (Anthropic) assisted the original preparation.

**Second version.** OpenAI Codex audited the proofs and assisted with the helicity-span
argument (Lemma 6.2), the null-frame current (Lemma A.1), corrections of scope and
editing.

**Third version.**
- ChatGPT (OpenAI) wrote an independent audit of whether the proposals of
  Phys. Rev. D 99 (2019) 046004 and Phys. Lett. B 808 (2020) 135674 fall under
  (N1)-(N5). It concluded that Nishino's unchanged real frame cannot be transferred
  to 27+3 or 19+3, that the rank-two alternative fails at the absorption step, and
  that the sources do not contain the field equations needed to decide other
  constructions. It also extracted the source texts and equation numbers.
- Claude Code checked that audit against the source PDFs (it was accurate) and
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

## What was checked, and what could not be

- Proofs: every step of Proposition 7.1 was re-derived by hand from Lemmas 2.2, 2.3,
  5.2, Proposition 2.1 and Theorems 3.3, 5.6; the numbers for 27+3 (D' = 26, N = 4096,
  j = -3/512, 4072 against 9/32) and 19+3 (D' = 18, N = 256 against 32) were
  recomputed.
- Programs: transfer_check.py, 24 checks passed, 0 failed (gamma matrices of size
  2^15 in 27+3, with Sezgin's 11+3 and Nishino's 19+11 as controls); verify.py,
  34 checks passed, 0 failed. These confirm the written proofs and do not replace them.
- Build: pdflatex -jobname=output main.tex, three passes, 0 errors, 0 overfull or
  underfull boxes, no undefined references; 26 pages.
- References: all 40 DOIs resolve to the cited works (38 in Crossref, the two Zenodo
  records in DataCite); all 23 arXiv identifiers match their titles and authors. Not verified online: Deligne, "Notes on spinors" (1999),
  which has no DOI and whose publisher page could not be reached from the session; the
  entry follows the printed volume. Lam's Graduate Studies in Mathematics 67 shows 2004
  in Crossref and 2005 on the printed book, and Lawson-Michelsohn's Spin Geometry shows
  1990 for its De Gruyter record against 1989 for the Princeton edition; the
  bibliography keeps the printed years.
- No general Lean formalisation is claimed. The gamma-matrix computations are finite
  numerical checks in double precision.

## Tools

Anthropic Claude (Claude Code); OpenAI ChatGPT; OpenAI Codex; Python (NumPy, SciPy,
Matplotlib); LaTeX (pdfLaTeX, TikZ). Exact model versions are not inferred from tool
names. AI systems are not listed as authors. No private prompts or chat transcripts
are included.
