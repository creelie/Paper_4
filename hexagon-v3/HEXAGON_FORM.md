# Hexagon submission fields

Submit a replacement version of 2610.00471v2; do not create a duplicate work.
The new version identifier is assigned by Hexagon after submission and is not
asserted in advance. Existing record: https://hexagonmath.org/2610.00471v2

## Title

Residual-dimension obstructions for null-projected supersymmetric Yang-Mills theories

## Abstract - copy the complete block

We prove necessary residual-dimension conditions for null-projected supersymmetric Yang--Mills constructions with a Majorana--Weyl gaugino under five explicit assumptions on the projection, transformations, translation bracket and absorption of cubic fermion terms. A real gaugino bounds the null-frame rank by the Witt index, and the residual dimension must be two or ten. Consequently the difference between the numbers of spacelike and timelike directions must be zero or eight in absolute value. The main algebraic step is a converse for a cubic gamma-matrix identity, relating the spinor dimension to the vector dimension. This obstructs transferring Nishino's mechanism to the specified higher-dimensional signature families, including nineteen plus three and twenty-seven plus three. In twenty-seven plus three a real frame has at most three null vectors against Nishino's ten, the translation bracket allows only two, and with two the residual spinors have 4096 components where absorption needs 48. These are necessary conditions within the stated axioms; existence in every remaining signature is a separate question. For unitary single-time theories with vanishing tensor charges on a massless multiplet, we also give a helicity-span argument excluding any finite collection of scalar, spinor and vector polarizations when there are more than sixteen real supercharges. All general arguments are written in the text; explicit gamma-matrix computations serve as supplementary checks.

The block uses explicit TeX commands rather than macros defined only in main.tex.

## What changed from v2

Proposition 7.1 writes out the transfer of Nishino's construction from (11+4n)+(3+4n) to (11+8n)+3 proposed in Rios, Marrani and Chester, Phys. Rev. D 99 (2019) 046004, Sec. III.A, and proves that it fails for every rank k of a real null frame: k <= 3 (Nishino's rank 4n+2, ten for 27+3, does not fit), the translation bracket allows only k = 2, and at k = 2 the cubic gaugino terms cannot be absorbed (4096 residual spinor components in 27+3 against the 48 that absorption requires). Table 1 gives the numbers for 19+3 and 27+3. Remark 7.2 shows that a complex frame of rank ten makes the transfer consistent only with a complex gaugino. Remark 7.3 states what the axioms do and do not decide: no theory in 27+3 satisfies N1-N5; the superalgebra (2.1) of Phys. Lett. B 808 (2020) 135674 alone contains no transformation rules and so cannot be checked against them; theories outside the axioms are not decided. The abstract, introduction, conclusions, note, data availability and AI declaration were updated accordingly. Sections 1-6 and the appendices are otherwise unchanged.

## Subjects, tags and MSC2020

Primary subject: math-ph
Cross-list subjects: math.RT
Tags: supersymmetric Yang-Mills theory, null projection, Clifford algebras, Majorana-Weyl spinors, Fierz identity, spacetime signature
MSC2020 primary code: 81T60
MSC2020 additional codes: 81T13, 15A66, 81R25, 83E15
arXiv identifier: leave blank. No arXiv identifier is asserted.

## Contributors - preserve this order

Contributor 1: Deep Bhattacharjee
Affiliation: Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India
ORCID: 0000-0003-0466-750X

The affiliations are former affiliations, not assertions of current employment.

## Authorship and understanding selections

Text: A mix of human-written and AI-generated.
Human understanding: All parts of this contribution have been checked and understood by a human.
These are the selections the user supplied for v2 on 25 October 2026; confirm them for v3.

## Provenance statement - copy this paragraph

Claude Code assisted the original preparation. OpenAI Codex assisted proof auditing, the explicit helicity-span argument, the null-current lemma, scope corrections and editing. For the third version, ChatGPT (OpenAI) supplied an independent audit of the proposed signature transfer, and Claude Code assisted with Proposition 7.1, Remarks 7.2 and 7.3 and the checks of the cited sources. Explicit gamma-matrix programs supply supplementary numerical checks. The submitting author declares that all parts have been checked and understood by a human and takes responsibility for the content.
No general Lean formalisation is claimed. The proof is written in the manuscript; the gamma-matrix calculations are supplementary finite numerical checks.

## Tools used

- Anthropic Claude / Claude Code
- OpenAI Codex
- OpenAI ChatGPT
- Python
- LaTeX / pdfLaTeX / TikZ

Use the corresponding system/tool entry if available and Other for an unlisted
tool. Do not invent a model version for an entry that is not documented.

## Formalisation links

Leave the formalisation field blank; no formal proof assistant development is claimed.

## Files and licence

Required source ZIP: NullProjectedSYM_v3-tex.zip
Reference PDF: NullProjectedSYM_v3.pdf (24 pages)
AI provenance upload: AI_PROVENANCE.md (outside the source ZIP).
Licence selection: CC BY 4.0, matching the existing Hexagon manuscript record.
The source ZIP contains main.tex, preamble.tex, abstract.tex, body.tex, bib.tex,
ai-disclosure.tex and the five figure PDFs in figures/, nothing else (no
directory entries, no data or scripts). The bibliography is inline.

## Review before submitting

Use pdfLaTeX, main document main.tex: pdflatex -jobname=output main.tex, three
passes. The extracted ZIP was rebuilt on TeX Live 2023 (passes of 2.2 s, 1.8 s
and 1.9 s) with 0 errors, 0 overfull or underfull boxes and no undefined
references, and its extracted text matched NullProjectedSYM_v3.pdf. The v2
source built on TeX Live 2026 with the same packages. Confirm the rendered
title, abstract, byline, references and final portal preview. This packet does
not press the portal's Process or Submit button on the author's behalf.

The source and package are in the folder hexagon-v3 of
https://github.com/creelie/Paper_4 (release v1.4.0); v2 is release v1.3.0,
archived as https://doi.org/10.5281/zenodo.23672585 (concept record
https://doi.org/10.5281/zenodo.23612780).
