# Paper_4 — direct journal submission package

## Hexagon v4 package

[hexagon-v4](hexagon-v4/) holds the fourth version, replacing https://hexagonmath.org/2610.00471v3: `NullProjectedSYM_v4-tex.zip` (upload this; main.tex, pdfLaTeX; the five Python programs are in its `anc/` folder), `NullProjectedSYM_v4.pdf` (36 pages), `NullProjectedSYM_v4-arxiv.tar.gz`, `HEXAGON_FORM.md`, `AI_PROVENANCE.md`, and the unpacked source in `source/`.

The Main Theorem is now a classification: a theory with k null vectors exists if and only if s+t-2k = 10 and s-t in {8, 0, -8}, or s+t-2k = 2 and s = t (Corollary 5.15). Theorem 5.12 gives sufficiency for residual dimension ten (Nishino's theories carry over to every such signature; theories exist in 9+9 and 9+17), and Theorem 5.14 for residual dimension two (theories in every (k+1)+(k+1), with vanishing cubic terms and off-shell closure). Theorem 7.3 shows that no fixed tensor in the source of the gauge field equation absorbs the cubic gaugino terms once the residual dimension exceeds 14, without N4 and with or without a gaugino constraint, so no contraction rescues (11+8n)+3 and its companions with n >= 1; Proposition 7.5 shows that several gauginos with their own parameters do not either, and Remark 7.6 explains why no statement about the superalgebra alone can exclude every theory. Appendices E and F check these results with `verification/code/contraction_check.py` (32 checks) and `verification/code/residual_two_check.py` (50 checks); logs are in `verification/current/`, and Figures 7 and 11 are drawn by `verification/code/figures/make_v4_figures.py`. Citations of unrefereed preprints were replaced by published versions or removed. Version 2.1.0, DOI [10.5281/zenodo.23788708](https://doi.org/10.5281/zenodo.23788708), supersedes version 2.0.0, DOI [10.5281/zenodo.23787988](https://doi.org/10.5281/zenodo.23787988), an earlier package of this version; all versions are under the concept DOI [10.5281/zenodo.23612780](https://doi.org/10.5281/zenodo.23612780).

## Hexagon v3 package

[hexagon-v3](hexagon-v3/) holds the third version, replacing https://hexagonmath.org/2610.00471v2: `NullProjectedSYM_v3-tex.zip` (upload this; main.tex, pdfLaTeX; the three Python programs are in its `anc/` folder), `NullProjectedSYM_v3.pdf` (26 pages), `NullProjectedSYM_v3-arxiv.tar.gz`, `HEXAGON_FORM.md`, `AI_PROVENANCE.md`, and the unpacked source in `source/`.

Section 7.1 answers the proposal of Rios, Marrani and Chester (Phys. Rev. D 99 (2019) 046004, Sec. III.A; Phys. Lett. B 808 (2020) 135674) to repeat Nishino's proof in the signatures (11+8n)+3. It quotes the proposal, writes out Nishino's equations (4.3)-(4.15) of Nucl. Phys. B 523 (1998) 450, and proves (Proposition 7.1) that the repetition fails for every rank k of a real null frame: k <= 3, so Nishino's rank 4n+2 (ten in 27+3) does not fit; the translation bracket allows only k = 2; and at k = 2 the transfer satisfies N1-N4 while the cubic gaugino terms cannot be absorbed (4096 residual spinor components in 27+3 against 48, 256 against 32 in 19+3). Appendix D checks each step in explicit gamma matrices of size 2^15 with `verification/code/transfer_check.py` (24 checks; log in `verification/current/transfer-checks.txt`); Figures 8 and 9 are drawn by `verification/code/figures/make_transfer_figures.py`. Theories outside N1-N5 are not decided.

Version 1.6.0, DOI [10.5281/zenodo.23746593](https://doi.org/10.5281/zenodo.23746593), corrects four statements in Section 7 after an independent review: the opening of Section 7 says that the null contraction is the mechanism of the constructions studied, not the only possible one (a footnote gives a spacelike contraction outside N1-N5), and Proposition 7.1 assumes a nonzero coupling, states its conditions for all gaugino values allowed by the constraint and all parameters, and treats rank zero separately. The theorems and the conclusion of Proposition 7.1 are unchanged, and so are the programs. Version 1.5.0 has DOI [10.5281/zenodo.23744833](https://doi.org/10.5281/zenodo.23744833); the first v3 package was release v1.4.0, DOI [10.5281/zenodo.23744131](https://doi.org/10.5281/zenodo.23744131).

## Hexagon v2 package (amsart, single column)

[hexagon-v2](hexagon-v2/) holds the replacement version of https://hexagonmath.org/2610.00471v1 in the amsart single-column layout: `NullProjectedSYM_v2-tex.zip` (upload this; main.tex, pdfLaTeX), `NullProjectedSYM_v2.pdf` (22 pages, the reference build), `NullProjectedSYM_v2-arxiv.tar.gz`, `HEXAGON_FORM.md` (portal fields) and `AI_PROVENANCE.md` (for Hexagon's separate provenance field). The mathematics, abstract and AI declaration are those of the Annals of Physics package below; only the layout changed. The source compiles on TeX Live 2026 with `pdflatex -jobname=output main.tex` with no errors and no bad boxes. Version: 1.3.0, release https://github.com/creelie/Paper_4/releases/tag/v1.3.0, package DOI: [10.5281/zenodo.23672585](https://doi.org/10.5281/zenodo.23672585).

## Annals of Physics upload package

[Paper_4 package](Paper_4%20package/README.md) contains the reviewed Hexagon/Overleaf source ZIP, the current PDF, AI provenance, complete Hexagon fields and supporting files for **Annals of Physics**. The package records the current proof/check scope and has no margin line numbers. No journal submission or acceptance is claimed. Version: 1.2.0. Package DOI: [10.5281/zenodo.23629626](https://doi.org/10.5281/zenodo.23629626).


**Residual-dimension obstructions for null-projected supersymmetric Yang–Mills theories**

Sole author: **Deep Bhattacharjee**, preserving the public preprint byline.
Version **1.1.0**. Manuscript DOI: https://doi.org/10.5281/zenodo.23611588 .
Original preprint: https://hexagonmath.org/2610.00471v1 .

## Alternative targets

| Target | Manuscript | Editable source | Submission letter |
|---|---|---|---|
| Physical Review D — first target | `Paper_4_PRD.pdf` | `PRD/main.tex` (REVTeX 4.2) | `COVER-LETTER-PRD.md` |
| Annals of Physics — alternative | `Paper_4_Annals_of_Physics.pdf` | `Annals-of-Physics/main.tex` (elsarticle) | `COVER-LETTER-ANNALS-OF-PHYSICS.md` |

Both targets have direct file-upload routes that do not require an arXiv
identifier. Choose one journal at a time. No journal submission has been made.
The two PDFs present the same mathematical manuscript in alternative layouts;
they are not distinct papers or separate discoveries. Both carry the same DOI.

The main result supplies necessary conditions under the five explicit N1–N5
assumptions: k ≤ min(s,t), residual dimension s+t−2k in {2,10}, and s−t in
{8,0,−8}. A separate helicity-span result assumes positive-energy unitarity and
vanishing tensor charges. General proofs are written in full. Thirty-four
supplementary gamma-matrix checks passed; they are finite numerical diagnostics.
Existence in every permitted signature and a nonperturbative quantum theory
remain outside these results. No universal supersymmetry classification or
journal acceptance is claimed.

## Contents and reproduction

Each source directory is independently compilable: run `pdflatex main.tex`
three times there, or use `python scripts/build_manuscript.py` from this root.
TeX Live/MiKTeX with REVTeX, elsarticle and the listed standard packages is needed.
For numerical checks, install `verification/code/requirements.txt` and run
`python scripts/verify.py` (34 checks), `python verification/code/transfer_check.py` (24 checks), `python verification/code/contraction_check.py` (32 checks) and `python verification/code/residual_two_check.py` (50 checks). `verification/current/` records the check run and
current page audits; `verification/previous/` separates historical engine/JHEP
staging logs. Optional figure regeneration is described in `VERIFICATION.md`.

Read `SUBMISSION-NOTES.md`, `PROOF-AUDIT.md` and `AUTHOR-DETAILS.md` before
using the corresponding journal letter. Annals of Physics highlights are in
`ANNALS-OF-PHYSICS-highlights.txt`. Both PDFs retain a detailed AI-use declaration.

`PACKAGE-METADATA.json` and `SHA256SUMS.txt` describe the single final ZIP.
Its creation is gated on published Zenodo status and exact checksums of both
archived PDFs. The code and editable files are also in the versioned GitHub
release: https://github.com/creelie/Paper_4 .
