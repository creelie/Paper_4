# Hexagon submission fields

Submit a replacement version of 2610.00471v2; do not create a duplicate work.
Hexagon assigns the new version identifier. Existing record: https://hexagonmath.org/2610.00471v2

## Title

Residual-dimension obstructions for null-projected supersymmetric Yang-Mills theories

## Abstract (copy the complete block)

We prove necessary conditions for null-projected supersymmetric Yang--Mills theories with a Majorana--Weyl gaugino in signature $(s,t)$, under five explicit assumptions on the gaugino constraint, the transformation rules, the residual gauge field, the translation bracket and the absorption of the cubic gaugino terms. A real gaugino allows at most $\min(s,t)$ null vectors, the residual dimension must be two or ten, and $s-t$ must be $0$ or $\pm8$. The main step is a converse of the cubic gamma-matrix identity: if symmetric gamma matrices acting on $N$-component spinors in $d$ dimensions satisfy it, then $N=2(d-2)$. Consequently Nishino's construction does not transfer to the signatures $(11+8n)+3$ proposed by Rios, Marrani and Chester. In $27+3$ a real null frame has at most three vectors against Nishino's ten, the translation bracket allows only two, and with two the residual spinors have $4096$ components where absorption needs $48$. For unitary single-time theories with vanishing tensor charges on a massless multiplet, we also exclude every finite collection of scalar, spinor and vector polarizations when there are more than sixteen real supercharges. Theories outside the five assumptions are not decided.

## What changed from v2

Section 7.1 is new. It quotes the proposal of Rios, Marrani and Chester (Phys. Rev. D 99 (2019) 046004, Sec. III.A) to repeat Nishino's proof in the signatures (11+8n)+3, writes out Nishino's equations (4.3)-(4.15) with their numbers, and proves in Proposition 7.1 that the repetition fails for every rank k of a real null frame: k <= 3, so Nishino's rank 4n+2 (ten for 27+3) does not fit; the translation bracket allows only k = 2; and at k = 2 the transfer satisfies (N1)-(N4) but the cubic gaugino terms cannot be absorbed (4096 residual spinor components in 27+3 against 48, and 256 against 32 in 19+3). Table 1 and Figures 8 and 9 give the numbers. Remark 7.2 shows that a complex frame of rank ten works only with a complex gaugino. Remark 7.3 says what the axioms decide: no theory in 27+3 satisfies (N1)-(N5), the superalgebra (2.1) of Phys. Lett. B 808 (2020) 135674 contains no transformation rules and so cannot be checked against them, and theories outside the axioms are not decided. Appendix D checks every step in explicit gamma matrices of size 2^15 (24 checks). The abstract, introduction, conclusions and data availability were rewritten accordingly; the AI declaration moved from the paper to the provenance file. Sections 1-6 and Appendices A-C are otherwise unchanged.

## Subjects, tags and MSC2020

Primary subject: math-ph
Cross-list subjects: math.RT
Tags: supersymmetric Yang-Mills theory, null projection, Clifford algebras, Majorana-Weyl spinors, Fierz identity, spacetime signature
MSC2020 primary code: 81T60
MSC2020 additional codes: 81T13, 15A66, 81R25, 83E15
arXiv identifier: leave blank.

## Contributors (preserve this order)

Contributor 1: Deep Bhattacharjee
Affiliation: Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India
ORCID: 0000-0003-0466-750X

## Authorship and understanding selections

Text: A mix of human-written and AI-generated.
Human understanding: All parts of this contribution have been checked and understood by a human (full human understanding).
These are the author's own declarations; Deep confirms them by submitting.

## Provenance statement (copy this paragraph)

Claude Code assisted the original preparation. OpenAI Codex audited the proofs of the second version and assisted with the helicity-span argument, the null-frame current lemma, scope corrections and editing. For the third version, ChatGPT (OpenAI) wrote an independent audit of the signature transfer proposed by Rios, Marrani and Chester, and Claude Code assisted with Section 7.1, Proposition 7.1, Remarks 7.2 and 7.3, Appendix D, the program transfer_check.py, Figures 8 and 9, and the checks of every quotation and reference. The text is a mix of human-written and AI-generated writing. The author has checked and understood every part and takes responsibility for the content. The gamma-matrix programs are supplementary numerical checks; no Lean formalisation is claimed.

## Tools used

- Anthropic Claude / Claude Code
- OpenAI ChatGPT
- OpenAI Codex
- Python
- LaTeX / pdfLaTeX / TikZ

## Formalisation links

Leave blank; no proof-assistant development is claimed.

## Files and licence

Required source ZIP: NullProjectedSYM_v3-tex.zip
Reference PDF: NullProjectedSYM_v3.pdf (26 pages)
AI provenance upload: AI_PROVENANCE.md (outside the source ZIP)
Licence: CC BY 4.0, as for the existing record.
The ZIP holds main.tex, preamble.tex, abstract.tex, body.tex, bib.tex, seven figure PDFs in figures/, and the three Python programs in anc/ (clifford.py, verify.py, transfer_check.py). No directory entries, no empty files, no .md, .sh or .pdf copies of the paper. The bibliography is inline.

## Review before submitting

Main document main.tex, pdfLaTeX: pdflatex -jobname=output main.tex, three passes. The extracted ZIP builds with 0 errors, 0 overfull or underfull boxes and no undefined references. Confirm the rendered title, abstract, byline and references in the portal preview.

Source, programs and logs: https://github.com/creelie/Paper_4, release v1.5.0, archived as https://doi.org/10.5281/zenodo.23744833. The second version is release v1.3.0, https://doi.org/10.5281/zenodo.23672585; concept record https://doi.org/10.5281/zenodo.23612780.
