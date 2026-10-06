"""Verify owned installation/rollback and preservation using isolated fixtures."""
from pathlib import Path
import hashlib,json,subprocess,tempfile
src=Path(__file__).resolve().parents[2]
root=Path(tempfile.mkdtemp(prefix='arl33-install-check-'))
def snapshot(p):return {str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in p.rglob('*') if f.is_file() and not f.is_symlink()}
def run(action,p):return subprocess.run(['python3',str(src/'adapters/codex/install.py'),action,str(p)],capture_output=True,text=True)
checks=[]
for kind in ['clean','existing','collision','symlink','changed','missing','directory-path','owned-path']:
 p=root/kind;p.mkdir()
 if kind!='clean':
  (p/'.codex').mkdir();(p/'AGENTS.md').write_text('Existing project instruction\n');(p/'CLAUDE.md').write_text('Existing Claude instruction\n');(p/'.codex/config.toml').write_text('approval_policy="on-request"\n')
 if kind=='collision':(p/'.codex/role-loop').mkdir()
 if kind=='symlink':(p/'.codex/role-loop').symlink_to(p/'missing-target',target_is_directory=True)
 before=snapshot(p);r=run('install',p)
 if kind in ['collision','symlink']:
  assert r.returncode!=0;assert snapshot(p)==before;checks.append({'fixture':kind,'result':'stop before writes, existing bytes preserved'});continue
 assert r.returncode==0,r.stderr
 marker=p/'.codex/role-loop/install.json';data=json.loads(marker.read_text())
 assert all(hashlib.sha256((p/f).read_bytes()).hexdigest()==h for f,h in data['files'].items())
 assert all(snapshot(p)[f]==h for f,h in before.items())
 if kind in ['changed','missing','directory-path','owned-path']:
  if kind=='changed':(p/'.codex/role-loop/entry.md').write_text('User change\n')
  if kind=='missing':(p/'.codex/role-loop/entry.md').unlink()
  if kind=='directory-path':data['created_directories'].append('../foreign');marker.write_text(json.dumps(data))
  if kind=='owned-path':data['files']['AGENTS.md']=before['AGENTS.md'];marker.write_text(json.dumps(data))
  state=snapshot(p);r=run('rollback',p);assert r.returncode!=0;assert snapshot(p)==state;checks.append({'fixture':kind,'result':'rollback refuses before deletion'});continue
 r=run('rollback',p);assert r.returncode==0,r.stderr;assert snapshot(p)==before
 checks.append({'fixture':kind,'result':'install/hash/rollback pass, existing bytes preserved','owned_files':len(data['files'])})
print(json.dumps({'directory':str(root),'checks':checks},indent=2))
