"""Run the supplementary gamma-matrix checks and preserve the exact output."""
from pathlib import Path
import hashlib,json,platform,subprocess,sys
import numpy,scipy

ROOT=Path(__file__).resolve().parents[1]
code=ROOT/'verification/code'
out=ROOT/'verification/current';out.mkdir(exist_ok=True,parents=True)
result=subprocess.run([sys.executable,'-u','verify.py'],cwd=code,
    stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(out/'numerical-checks.txt').write_bytes(result.stdout)
text=result.stdout.decode('utf-8',errors='replace')
assert result.returncode==0 and '34 checks passed, 0 failed' in text,text[-3000:]
record={'python':platform.python_version(),'numpy':numpy.__version__,
    'scipy':scipy.__version__,'platform':platform.platform(),'checks_passed':34,
    'checks_failed':0,'general_proof_formalized':False,
    'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [code/'verify.py',code/'clifford.py']}}
(out/'environment.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('34 supplementary numerical checks passed; the written general proofs are separate.')
