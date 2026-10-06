# Claude Code adapter

This adapter maps the [core route](../../core/loop.md) to Claude Code role
subagents and the `/orc` command. The core remains the routing authority.
For a first exercise, use the Dutch [student walkthrough](../../teaching/praktijk/claude-code.md).
This page is technical installation and maintenance reference.

## Prerequisites and boundaries

You need Git, Python 3, Claude Code and an authenticated account that can run the
selected model. Check `claude --version` and `claude auth status`. Authentication
is not proof of available model access or quota. Use the official
[setup guide](https://code.claude.com/docs/en/setup) for installation and login.
Record the actual CLI version and resolved model from the run, not just an alias.

The model provider, Claude Code process and target repository are separate:
Claude Code reads files and executes permitted tools; the provider processes
model requests. Project instructions do not grant tool permissions. Check the
[permission rules](https://code.claude.com/docs/en/permissions) before execution.
Use a temporary exercise repository first. The human handles Git commits and
tracker writes in that exercise; the agent does not merge anything.

## Inspect the target before copying

At the target root, inspect existing `CLAUDE.md`, `AGENTS.md`, `.claude/rules/`,
`.claude/settings.json`, `.claude/settings.local.json`, `.mcp.json`, agent,
command and skill names. Include inherited user/managed instructions and hooks
in the review of the actual environment. Do not print credentials or entire
account configuration into evidence. Identify the project's norm files and
known test commands; keep them as the source of truth.

The copy below adds only this adapter's files. It stops on any destination
collision, including an existing installation. An existing skill named `orc`
also blocks installation because it can shadow the command. It does not edit
project instructions or grant permissions. Review hooks and name precedence
separately; a successful copy alone does not prove which definitions will run.

## Copy installation

Run from any directory. Set the source to this repository at the chosen commit
and the target to the exercise/project root. The source commit applies to core,
wrappers and command together. Do not mix versions.

```sh
LOOP_SOURCE=/path/to/agent-role-loop
LOOP_TARGET=/path/to/exercise
python3 - "$LOOP_SOURCE" "$LOOP_TARGET" <<'PY'
import hashlib, json, shutil, subprocess, sys
from pathlib import Path
source, target = (Path(x).resolve() for x in sys.argv[1:])
if source == target or not target.is_dir():
    raise SystemExit("Choose an existing, separate target directory")
files = {}
for p in (source / "adapters/claude-code/agents").glob("role-loop-*.md"):
    files[Path(".claude/agents") / p.name] = p
files[Path(".claude/commands/orc.md")] = source / "adapters/claude-code/commands/orc.md"
for p in (source / "core").rglob("*"):
    if p.is_file():
        files[Path(".claude/agent-role-loop/core") / p.relative_to(source / "core")] = p
marker = target / ".claude/agent-role-loop/install.json"
for relative in files:
    for parent in (target / relative).parents:
        if parent == target:
            break
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise SystemExit("No files copied; unsafe destination parent: " + str(parent))
conflicts = [str(p) for p in files if (target / p).exists() or (target / p).is_symlink()]
if marker.exists() or marker.is_symlink() or (target / ".claude/agent-role-loop").exists():
    conflicts.append(".claude/agent-role-loop")
if (target / ".claude/skills/orc").exists() or (target / ".claude/skills/orc").is_symlink():
    conflicts.append(".claude/skills/orc")
if conflicts:
    raise SystemExit("No files copied; resolve collisions first: " + ", ".join(conflicts))
if len(list((source / "adapters/claude-code/agents").glob("role-loop-*.md"))) != 9:
    raise SystemExit("Expected nine role wrappers; check source checkout")
if not (source / "core/loop.md").is_file() or any(not p.is_file() for p in files.values()):
    raise SystemExit("No files copied; incomplete source checkout")
version = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
directories = set()
for relative in files:
    parent = (target / relative).parent
    while parent != target:
        if not parent.exists():
            directories.add(str(parent.relative_to(target)))
        parent = parent.parent
for relative, original in files.items():
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original, destination)
manifest = {str(p): hashlib.sha256((target / p).read_bytes()).hexdigest() for p in files}
marker.write_text(json.dumps({"source_commit": version, "files": manifest,
    "created_directories": sorted(directories)}, indent=2) + "\n")
print("Copied", len(files), "files; manifest:", marker)
PY
```

Check `git diff` and `.claude/agent-role-loop/install.json`: existing unrelated
files should be unchanged. The manifest records copied bytes, not a claim that
a dirty source checkout equals its HEAD. Install from a clean checkout for a
released version; during development record the source diff and hashes too.
Start a new Claude Code session at the target root. Ensure `/orc` resolves to
this command and the `role-loop-*` agents resolve to the project definitions.
Managed or CLI agent definitions can override project agents; user skills/commands
can shadow the project command. The official
[subagent documentation](https://code.claude.com/docs/en/sub-agents) and
[command documentation](https://code.claude.com/docs/en/slash-commands) describe loading.

## Permissions and independent contexts

The wrappers use `omitClaudeMd: true` on the selected Claude Code version.
Supply the applicable norm paths, exact versions and decisions explicitly in
every role task. Managed policy still applies. Check support before using an
older version; silently ignoring this field invalidates an isolation claim.
Use ordinary fresh calls for initial reviewers and repair reviewers, never a
fork or a resumed reviewer. Builder context may be retained for targeted repair.

A subagent has its own conversation, but that does not prevent it from reading
accessible files. Keep transcripts and unrelated judgments outside its task
inputs and readable review sources. The reviewer tool lists omit Edit/Write;
Bash can still write files, so allow only the actual inspection/test commands
needed. Parent permission modes and rules also affect subagents. Do not describe
prompt instructions as an operating-system sandbox. No bypass mode is required.

## Run one work item

1. Save complete C0 and project norms in readable files, or pass an accessible
   issue reference. When tracker access is unavailable, provide the complete
   contract text and record its original source/version. A URL alone is insufficient.
2. Start Claude Code at the target root and run `/orc work-items/W1/C0.md`.
   Name the norm sources and the location for its contract files. C1 records
   selected responsibilities, reviewer assignments, versions and both counters.
3. For PLANNED, inspect concrete C2 and any selected C3. Only the human's actual
   C4 releases building. Keep that response and exact plan version. Do not
   reinterpret permission to use a tool as plan approval.
4. Give the builder the approved inputs. Execute the tests, save observations,
   and commit the product with the project's Git procedure. Pin this exact SHA
   in C5 before giving C5 core to fresh independent reviewers.
5. Keep all C6s. One selected reviewer gives the final verdict; multiple reviews
   follow core synthesis/arbitration rules. On BLOCK, persist the repair state
   before author repair and start a fresh repair reviewer with the explicit appendix.
6. SHIP means ready for the human's separate merge decision. Preserve unavailable
   observations and deferred nits; do not invent tracker actions or acceptance.

Updating an existing installation requires an inventory and a coherent version
replacement, not another blind copy. Existing work retains its pinned basis.

## Undo an unchanged installation

The rollback below checks all owned files before removing any. If an owned file
changed, stop and inspect it; do not discard it with this procedure. Unrelated
files and pre-existing directories are retained. A conflicting prior installation
was never overwritten, so no old installation needs restoring.

```sh
python3 - "$LOOP_TARGET" <<'PY'
import hashlib, json, sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
marker = root / ".claude/agent-role-loop/install.json"
if marker.is_symlink():
    raise SystemExit("No files removed; manifest is a symlink")
data = json.loads(marker.read_text())
for name in data["created_directories"]:
    relative = Path(name)
    owned = (name in [".claude", ".claude/agents", ".claude/commands", ".claude/agent-role-loop"] or
        name == ".claude/agent-role-loop/core" or name.startswith(".claude/agent-role-loop/core/"))
    if not owned or relative.is_absolute() or ".." in relative.parts:
        raise SystemExit("No files removed; invalid directory path: " + name)
    for p in [root / relative, *(root / relative).parents]:
        if p == root:
            break
        if p.is_symlink():
            raise SystemExit("No files removed; symlink in directory path: " + str(p))
for name in data["files"]:
    relative = Path(name)
    owned = (name == ".claude/commands/orc.md" or
        (relative.parent == Path(".claude/agents") and relative.name.startswith("role-loop-") and relative.suffix == ".md") or
        name.startswith(".claude/agent-role-loop/core/"))
    if not owned or relative.is_absolute() or ".." in relative.parts:
        raise SystemExit("No files removed; invalid manifest path: " + name)
    for p in [root / relative, *(root / relative).parents]:
        if p == root:
            break
        if p.is_symlink():
            raise SystemExit("No files removed; symlink in owned path: " + str(p))
for name, expected in data["files"].items():
    p = root / name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
        raise SystemExit("No files removed; changed/missing owned file: " + name)
for name in data["files"]:
    (root / name).unlink()
marker.unlink()
for name in sorted(data["created_directories"], key=lambda x: len(Path(x).parts), reverse=True):
    p = root / name
    if p.exists() and not any(p.iterdir()):
        p.rmdir()
print("Removed unchanged adapter files; unrelated content retained")
PY
```

## Verification record

The implementation run and its limits are recorded in
[onderzoek/32-uitvoering.md](../../onderzoek/32-uitvoering.md). A configuration
loading check, a provider execution and a student observation are different
kinds of evidence. Missing external access must remain unverified.
