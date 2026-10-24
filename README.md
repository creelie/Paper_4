# Paper_4 — null-projected supersymmetric Yang–Mills theories

**Residual-dimension obstructions for null-projected supersymmetric Yang–Mills theories**

Sole author: **Deep Bhattacharjee**, matching the existing preprint.
Version 1.1.0. Target for evaluation: **Journal of High Energy Physics (JHEP)**.
Manuscript DOI: https://doi.org/10.5281/zenodo.23611588 .
Original preprint: https://hexagonmath.org/2610.00471v1 .

The main theorem gives necessary conditions for the precisely defined N1–N5
class: k ≤ min(s,t), residual dimension s+t−2k in {2,10}, and s−t in
{8,0,−8}. A separate theorem gives a massless helicity-span obstruction under
positive-energy unitarity and vanishing tensor charges. All general proofs are
written in the manuscript. Numerical checks supplement the proofs.

Existence and full dynamics in every permitted signature, other transformation
rules or field contents, and a nonperturbative quantum construction are outside
the proved results. This package does not assert a universal classification of
supersymmetric theories or a solution of the remaining Hodge/GSC problems.

## Files

- `Paper_4_JHEP.pdf`: the manuscript to review.
- `manuscript/main.tex`: master file with five vector figures and the full bibliography.
- `PROOF-AUDIT.md` and `VERIFICATION.md`: deductions, scope and verification provenance.
- `COVER-LETTER-JHEP.md` and `SUBMISSION-NOTES.md`: editable submission documents.
- `verification/code/`: original numerical programs and figure-generation source.
- `verification/current/`: this package's checks and build logs.
- `provenance/`: source identification and the published Zenodo record.

Build: `python scripts/build_manuscript.py` (TeX Live with `pdflatex` required).
Checks: `pip install -r verification/code/requirements.txt`, then
`python scripts/verify.py`. The scripts never treat floating-point samples as
proofs of identities for all spinors and signatures.

The single final ZIP is created only after confirming Zenodo publication and the
exact PDF checksum. See `PACKAGE-METADATA.json` and `SHA256SUMS.txt`.
No journal submission or acceptance is claimed. JHEP additionally requires an
arXiv identifier and a matching arXiv version; that identifier remains pending.
