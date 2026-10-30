# Hexagon submission fields

Submit a replacement version of 2610.00471v3; do not create a duplicate work.
Hexagon assigns the new version identifier. Existing record: https://hexagonmath.org/2610.00471v3

## Title

Residual-dimension obstructions for null-projected supersymmetric Yang-Mills theories

## Abstract (copy the complete block)

We prove necessary conditions for null-projected supersymmetric Yang--Mills theories with a Majorana--Weyl gaugino in signature $(s,t)$, under five explicit assumptions on the gaugino constraint, the transformation rules, the residual gauge field, the translation bracket and the absorption of the cubic gaugino terms, and we show that they are sufficient when the residual dimension is ten. A real gaugino allows at most $\min(s,t)$ null vectors, the residual dimension must be two or ten, and $s-t$ must be $0$ or $\pm8$. The main step is a converse of the cubic gamma-matrix identity: if symmetric gamma matrices acting on $N$-component spinors in $d$ dimensions satisfy it, then $N=2(d-2)$. Conversely, Nishino's theories carry over to every signature with residual dimension ten that these conditions leave, among them $9+9$ and $9+17$. The signatures $(11+8n)+3$ proposed by Rios, Marrani and Chester are excluded: in $27+3$ a real null frame has at most three vectors against Nishino's ten, and no contraction of the source in the gauge field equation absorbs the cubic terms once the residual dimension is sixteen or more. For unitary single-time theories with vanishing tensor charges on a massless multiplet, we also exclude every finite collection of scalar, spinor and vector polarizations when there are more than sixteen real supercharges. Theories outside the five assumptions are not decided.

## What changed from v3

Two theorems are new. Theorem 5.12 (Section 5.4) shows that the conditions of the Main Theorem are sufficient when the residual dimension is ten: a complex isometry that keeps the total dimension and the rank of the null frame carries Nishino's equations to every signature with s+t-2k = 10 and s-t in {8, 0, -8}, and the transported theory keeps a Majorana-Weyl gaugino and satisfies N1-N5. Corollary 5.13 turns the Main Theorem into a classification for residual dimension at least three; in particular theories exist in 9+9 and 9+17, the members n = 1, 2 of the second degenerate family 9+(1+8n) of Rios, Marrani and Chester, and in no member with n >= 3. Theorem 7.3 (Section 7.2) drops N4 and allows any fixed tensor u in the source J ^ u that absorbs the cubic gaugino terms, with or without a constraint on the gaugino: the residual dimension is then at most 14, and at most 10 unless the frame has rank at least 54. Corollary 7.4 applies this to the families (9+8n)+1, (10+8n)+2, (11+8n)+3, (12+8n)+4 with n >= 1, whose real frames leave residual dimension at least 16, so no contraction of the source rescues them; this covers the spacelike contraction that v3 left open in a footnote. Appendix E checks both theorems in explicit gamma matrices (contraction_check.py, 32 checks), and Figures 7 and 11 are new. The citations of unrefereed preprints were removed: the arXiv paper of Truini, Marrani and Rios is replaced by its published version (Expo. Math. 43 (2025) 125621, with de Graaf), the arXiv preprint of Banerjee and two self-archived Zenodo copies of earlier versions are no longer cited, and the data availability section cites one concept record. The introduction, Section 7.3 (Scope), Remark 7.5, the conclusions and the proof map were updated, the second affiliation now names Heramba Chandra College, and a typo in Appendix A was fixed. Sections 2-4 and 6, Proposition 7.1, Remark 7.2 and Appendices B-D are unchanged; in Section 5 the paragraph on existence after Corollary 5.9 was replaced by Section 5.4.

## Subjects, tags and MSC2020

Primary subject: math-ph
Cross-list subjects: math.RT
Tags: supersymmetric Yang-Mills theory, null projection, Clifford algebras, Majorana-Weyl spinors, Fierz identity, spacetime signature
MSC2020 primary code: 81T60
MSC2020 additional codes: 81T13, 15A66, 81R25, 83E15
arXiv identifier: leave blank.

## Contributors (preserve this order)

Contributor 1: Deep Bhattacharjee
Affiliation: Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India; Formerly, University of Calcutta (Heramba Chandra College), 23/49 Gariahat Road, Golpark, Kolkata 700029, West Bengal, India
ORCID: 0000-0003-0466-750X

## Authorship and understanding selections

Text: A mix of human writing and AI-generated writing (ChatGPT-6.1 Sol Ultra; Claude Code with Opus 5.5, Ultracode; Claude Code with Fable 5.1, medium effort).
Human understanding: All parts of this contribution have been checked by the author and are understood by him (full human understanding).
These are the author's own declarations; Deep confirms them by submitting.

## Provenance statement (copy this paragraph)

Claude Code assisted the original preparation. OpenAI Codex audited the proofs of the second version and assisted with the helicity-span argument, the null-frame current lemma, scope corrections and editing. For the third version, ChatGPT-6.1 Sol Ultra (OpenAI) wrote an independent audit of the signature transfer proposed by Rios, Marrani and Chester, and Claude Code (Opus 5.5 with Ultracode, and Fable 5.1 at medium effort) assisted with Section 7.1, Proposition 7.1, Remarks 7.2 and 7.3, Appendix D, the program transfer_check.py and the checks of every quotation and reference; a second independent review, supplied by the author, led to four corrections of statement in Section 7. For the fourth version, Claude Code assisted with Theorem 5.12, Corollary 5.13, Theorem 7.3, Corollary 7.4, Appendix E, the program contraction_check.py, Figures 7 and 11, the replacement of unrefereed citations and the check of every reference. The text is a mix of human writing and writing generated by these tools. The author has checked and understood every part and takes responsibility for the content. The gamma-matrix programs are supplementary numerical checks; no Lean formalisation is claimed.

## Tools used

- OpenAI ChatGPT-6.1 Sol Ultra
- Anthropic Claude Code, Opus 5.5 (Ultracode)
- Anthropic Claude Code, Fable 5.1 (medium effort)
- OpenAI Codex
- Python
- LaTeX / pdfLaTeX / TikZ

## Formalisation links

Leave blank; no proof-assistant development is claimed.

## Files and licence

Required source ZIP: NullProjectedSYM_v4-tex.zip
Reference PDF: NullProjectedSYM_v4.pdf (31 pages)
AI provenance upload: AI_PROVENANCE.md (outside the source ZIP)
Licence: CC BY 4.0, as for the existing record.
The ZIP holds main.tex, preamble.tex, abstract.tex, body.tex, bib.tex, nine figure PDFs in figures/, and the four Python programs in anc/ (clifford.py, verify.py, transfer_check.py, contraction_check.py). No directory entries, no empty files, no .md, .sh or .pdf copies of the paper. The bibliography is inline.

## Review before submitting

Main document main.tex, pdfLaTeX: pdflatex -jobname=output main.tex, three passes. The extracted ZIP builds with 0 errors, 0 overfull or underfull boxes and no undefined references. Confirm the rendered title, abstract, byline and references in the portal preview.

Source, programs and logs: https://github.com/creelie/Paper_4, release v2.0.0; all versions under the concept record https://doi.org/10.5281/zenodo.23612780. The third version is release v1.6.0, https://doi.org/10.5281/zenodo.23746593.
