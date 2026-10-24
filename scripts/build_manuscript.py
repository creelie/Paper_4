"""Build the JHEP manuscript; no archives are created."""
from pathlib import Path
import argparse, shutil, subprocess

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--tex-bin',type=Path)
args=parser.parse_args()
tex=str(args.tex_bin/'pdflatex.exe') if args.tex_bin else shutil.which('pdflatex')
if not tex: raise SystemExit('Install TeX with jheppub support, or pass --tex-bin.')
logs=ROOT/'verification/current';logs.mkdir(exist_ok=True,parents=True)
for i in (1,2,3):
    run=subprocess.run([tex,'-interaction=nonstopmode','-halt-on-error','main.tex'],
        cwd=ROOT/'manuscript',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (logs/f'tex-pass-{i}.txt').write_bytes(run.stdout)
    if run.returncode: raise SystemExit(f'TeX failed: verification/current/tex-pass-{i}.txt')
log=(ROOT/'manuscript/main.log').read_text(encoding='utf-8',errors='replace')
errors=[s for s in ['Overfull \\hbox','Overfull \\vbox','There were undefined references',
    'There were undefined citations','Rerun to get cross-references right'] if s in log]
if errors: raise SystemExit('Resolve diagnostics: '+', '.join(errors))
shutil.copy2(ROOT/'manuscript/main.pdf',ROOT/'Paper_4_JHEP.pdf')
print('Built '+str(ROOT/'Paper_4_JHEP.pdf'))
