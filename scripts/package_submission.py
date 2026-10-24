"""Create the single author-packet ZIP only after confirmed DOI publication."""
from pathlib import Path
import datetime,hashlib,json,zipfile

ROOT=Path(__file__).resolve().parents[1]
NAME='Paper_4_direct_submission_v1.1.0.zip'
record=json.loads((ROOT/'provenance/zenodo-published-record.json').read_text(encoding='utf-8'))
assert record['state']=='done' and record['doi']=='10.5281/zenodo.23611588'
assert record['metadata']['version']=='1.1.0'
assert [x['name'] for x in record['metadata']['creators']]==['Bhattacharjee, Deep']
qa=json.loads((ROOT/'verification/current/page-audit.json').read_text(encoding='utf-8'))
assert qa['visual_review_completed']
for name in ['Paper_4_PRD.pdf','Paper_4_Annals_of_Physics.pdf']:
 pdf=ROOT/name
 entry=next(f for f in record['files'] if f['key']==name)
 digest=hashlib.md5(pdf.read_bytes()).hexdigest()
 assert entry['checksum']=='md5:'+digest
 audit=next(item for item in qa['formats'] if item['file']==name)
 assert audit['visual_review_completed'] and audit['pdf_md5']==digest
skip_suffix={'.aux','.log','.out','.blg','.rpi','.fls','.fdb_latexmk','.toc','.pyc','.exe'}
def include(path):
 rel=path.relative_to(ROOT)
 return (path.is_file() and not any(x in {'.git','.lake','__pycache__'} for x in rel.parts)
     and path.suffix not in skip_suffix and path.suffix!='.zip'
     and path.name not in {'SHA256SUMS.txt','main.pdf',NAME+'.sha256'})
text_suffix={'.md','.json','.txt','.tex','.bib','.bbl','.py','.cff','.patch','.yml','.sty'}
for p in ROOT.rglob('*'):
 if include(p) and (p.suffix in text_suffix or p.name in {'LICENSE','.gitattributes','.gitignore'} or p.name.endswith('LICENSE')):
  data=p.read_bytes()
  if b'\r\n' in data:p.write_bytes(data.replace(b'\r\r\n',b'\n').replace(b'\r\n',b'\n'))
metadata={'version':'1.1.0','doi':record['doi'],'authors':['Deep Bhattacharjee'],
 'repository':'https://github.com/creelie/Paper_4','primary_journal':'Physical Review D',
 'alternative_journal':'Annals of Physics','journal_targets':['Physical Review D','Annals of Physics'],
 'zenodo_record':'https://zenodo.org/records/23611588','zenodo_record_state':record['state'],
 'zenodo_publication_confirmed_before_packaging':True,'archived_pdf_checksum_matches':True,
 'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'arxiv_identifier':None,'arxiv_required_for_selected_direct_routes':False,
 'journal_submitted':False,'journal_accepted':False,
 'proof_scope':'Necessary obstructions under N1–N5; separate unitary helicity bound; no general existence or nonperturbative quantum construction claimed.'}
(ROOT/'PACKAGE-METADATA.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf-8',newline='\n')
files=sorted((p for p in ROOT.rglob('*') if include(p)),key=lambda p:p.relative_to(ROOT).as_posix())
sums=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix()+'\n' for p in files)
manifest=ROOT/'SHA256SUMS.txt';manifest.write_text(sums,encoding='utf-8',newline='\n');files.append(manifest)
output=ROOT/NAME
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
 for p in files:archive.write(p,'Paper_4/'+p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(output) as archive:
 assert archive.testzip() is None
 assert len(archive.namelist())==len(set(archive.namelist()))==len(files)
 assert not any(name.endswith('.zip') for name in archive.namelist())
 for line in sums.splitlines():
  expected,name=line.split('  ',1)
  assert hashlib.sha256(archive.read('Paper_4/'+name)).hexdigest()==expected,name
digest=hashlib.sha256(output.read_bytes()).hexdigest()
(ROOT/(NAME+'.sha256')).write_text(digest+'  '+NAME+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'zip':str(output),'files':len(files),'bytes':output.stat().st_size,
 'sha256':digest,'doi':record['doi'],'published_before_packaging':True}))
