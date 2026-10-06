from pathlib import Path
import tempfile, subprocess, hashlib, json
src=Path(__file__).resolve().parents[2]
text=(src/'adapters/claude-code/README.md').read_text()
blocks=text.split("<<'PY'\n")[1:]
install,rollback=[x.split('\nPY\n```')[0] for x in blocks]
root=Path(tempfile.mkdtemp(prefix='arl32-install-check-'))
def run(code,args):return subprocess.run(['python3','-',*map(str,args)],input=code,text=True,capture_output=True)
def snapshot(p):return {str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in p.rglob('*') if f.is_file() and not f.is_symlink()}
checks=[]
for kind in ['clean','existing','collision','skill','skill-symlink','changed','symlink','directory-path']:
 p=root/kind;p.mkdir()
 if kind!='clean':
  (p/'.claude/agents').mkdir(parents=True);(p/'CLAUDE.md').write_text('Bestaande projectafspraak\n');(p/'.claude/agents/unrelated.md').write_text('Bestaande rol\n');(p/'.claude/settings.json').write_text('{"permissions":{"deny":["Bash(git push *)"]}}\n')
 if kind=='collision':(p/'.claude/agents/role-loop-builder.md').write_text('Eigen rol, behouden\n')
 if kind=='skill':(p/'.claude/skills/orc').mkdir(parents=True)
 if kind=='skill-symlink':
  (p/'.claude/skills').mkdir();(p/'.claude/skills/orc').symlink_to(p/'missing-skill')
 if kind=='symlink':
  (p/'.claude/agents').rename(p/'.claude/old-agents');(p/'.claude/agents').symlink_to(p/'.claude/old-agents',target_is_directory=True)
 before=snapshot(p);r=run(install,[src,p])
 if kind in ['collision','skill','skill-symlink','symlink']:
  assert r.returncode!=0,(kind,r.stdout);assert snapshot(p)==before;checks.append({'fixture':kind,'result':'stopped before writes; bytes preserved'});continue
 assert r.returncode==0,r.stderr
 for name,digest in before.items():assert snapshot(p)[name]==digest
 marker=json.loads((p/'.claude/agent-role-loop/install.json').read_text())
 assert all(hashlib.sha256((p/f).read_bytes()).hexdigest()==h for f,h in marker['files'].items())
 if kind=='directory-path':
  marker['created_directories'].append('../unrelated-empty-directory')
  (p/'.claude/agent-role-loop/install.json').write_text(json.dumps(marker))
  state=snapshot(p);r=run(rollback,[p]);assert r.returncode!=0;assert snapshot(p)==state
  checks.append({'fixture':kind,'result':'invalid directory rejected before any deletion'});continue
 if kind=='changed':
  (p/'.claude/commands/orc.md').write_text('Eigen wijziging\n');state=snapshot(p);r=run(rollback,[p]);assert r.returncode!=0;assert snapshot(p)==state;checks.append({'fixture':kind,'result':'rollback refused without deleting anything'});continue
 r=run(rollback,[p]);assert r.returncode==0,r.stderr;assert snapshot(p)==before
 checks.append({'fixture':kind,'result':'install/hash check/rollback pass; existing bytes preserved','owned_files':len(marker['files'])})
print(json.dumps({'directory':str(root),'checks':checks},indent=2))
