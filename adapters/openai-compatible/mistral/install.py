"""Copy/undo only owned Mistral Vibe Role Loop files; preserve project configuration."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess

OWN = Path('.vibe/role-loop')

def safe_path(root, relative):
    if relative.is_absolute() or '..' in relative.parts:
        raise SystemExit('Invalid owned path: ' + str(relative))
    for part in [root / relative, *(root / relative).parents]:
        if part == root:
            break
        if part.is_symlink() or (part.exists() and part != root / relative and not part.is_dir()):
            raise SystemExit('Unsafe path: ' + str(part))
    return root / relative

def install(source, target):
    if not target.is_dir() or source == target:
        raise SystemExit('Choose a separate existing target directory')
    destination = safe_path(target, OWN)
    if destination.exists():
        raise SystemExit('Existing installation; no files copied')
    files = {OWN / name: source / 'adapters/openai-compatible/mistral' / name for name in ['entry.md', 'AGENTS.example.md', 'role-task.md']}
    for path in (source / 'core').rglob('*'):
        if path.is_file():
            files[OWN / 'core' / path.relative_to(source / 'core')] = path
    if not (source / 'core/loop.md').is_file() or any(not p.is_file() for p in files.values()):
        raise SystemExit('Incomplete source; no files copied')
    for name in files:
        safe_path(target, name)
    revision = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    created = set()
    for name in files:
        parent = (target / name).parent
        while parent != target:
            if not parent.exists():
                created.add(str(parent.relative_to(target)))
            parent = parent.parent
    for name, original in files.items():
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original, path)
    manifest = {'source_commit': revision, 'files': {str(name): hashlib.sha256((target / name).read_bytes()).hexdigest() for name in files}, 'created_directories': sorted(created)}
    (destination / 'install.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print('Copied', len(files), 'files;', destination / 'install.json')

def rollback(target):
    marker = safe_path(target, OWN / 'install.json')
    data = json.loads(marker.read_text())
    for name in data['files']:
        relative = Path(name)
        if not relative.is_relative_to(OWN) or relative == OWN / 'install.json':
            raise SystemExit('Invalid manifest ownership; nothing removed')
        path = safe_path(target, relative)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != data['files'][name]:
            raise SystemExit('Changed/missing owned file; nothing removed: ' + name)
    for name in data['created_directories']:
        relative = Path(name)
        if relative != Path('.vibe') and not relative.is_relative_to(OWN):
            raise SystemExit('Invalid directory ownership; nothing removed')
        safe_path(target, relative)
    for name in data['files']:
        (target / name).unlink()
    marker.unlink()
    for name in sorted(data['created_directories'], key=lambda n: len(Path(n).parts), reverse=True):
        path = target / name
        if path.exists() and not any(path.iterdir()):
            path.rmdir()
    print('Removed unchanged owned files; unrelated content retained')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['install', 'rollback'])
    parser.add_argument('target', type=Path)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    if args.action == 'install':
        install(args.source.resolve(), args.target.resolve())
    else:
        rollback(args.target.resolve())
