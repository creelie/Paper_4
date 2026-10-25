# Paper_4 — direct journal submission package

## Current upload package

[Paper_4 package](Paper_4%20package/README.md) contains the reviewed Hexagon/Overleaf source ZIP, the current PDF, AI provenance, complete Hexagon fields and supporting files for **Annals of Physics**. The package records the current proof/check scope and has no margin line numbers. No journal submission or acceptance is claimed. Version: 1.2.0.


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
`python scripts/verify.py`. `verification/current/` records the check run and
current page audits; `verification/previous/` separates historical engine/JHEP
staging logs. Optional figure regeneration is described in `VERIFICATION.md`.

Read `SUBMISSION-NOTES.md`, `PROOF-AUDIT.md` and `AUTHOR-DETAILS.md` before
using the corresponding journal letter. Annals of Physics highlights are in
`ANNALS-OF-PHYSICS-highlights.txt`. Both PDFs retain a detailed AI-use declaration.

`PACKAGE-METADATA.json` and `SHA256SUMS.txt` describe the single final ZIP.
Its creation is gated on published Zenodo status and exact checksums of both
archived PDFs. The code and editable files are also in the versioned GitHub
release: https://github.com/creelie/Paper_4 .
