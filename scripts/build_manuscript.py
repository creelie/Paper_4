"""Build direct-submission journal variants; no archives are created."""
from pathlib import Path
import argparse, shutil, subprocess

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--tex-bin',type=Path)
parser.add_argument('--variant',choices=['PRD','Annals-of-Physics'])
args=parser.parse_args()
tex=str(args.tex_bin/'pdflatex.exe') if args.tex_bin else shutil.which('pdflatex')
if not tex: raise SystemExit('Install TeX with REVTeX and elsarticle, or pass --tex-bin.')
logs=ROOT/'verification/current';logs.mkdir(exist_ok=True,parents=True)
variants=[args.variant] if args.variant else ['PRD','Annals-of-Physics']
for variant in variants:
    for i in (1,2,3):
        run=subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','main.tex'],
            cwd=ROOT/variant,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (logs/f'{variant}-tex-pass-{i}.txt').write_bytes(run.stdout)
        if run.returncode: raise SystemExit(f'TeX failed: verification/current/{variant}-tex-pass-{i}.txt')
    log=(ROOT/variant/'main.log').read_text(encoding='utf-8',errors='replace')
    errors=[s for s in ['Overfull \\hbox','Overfull \\vbox','There were undefined references',
        'There were undefined citations','Rerun to get cross-references right'] if s in log]
    if errors: raise SystemExit(variant+': resolve diagnostics: '+', '.join(errors))
    filename='Paper_4_PRD.pdf' if variant=='PRD' else 'Paper_4_Annals_of_Physics.pdf'
    shutil.copy2(ROOT/variant/'main.pdf',ROOT/filename)
    print('Built '+str(ROOT/filename))
