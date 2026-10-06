# Codex adapter

This is technical installation and maintenance reference. For a first exercise,
use the Dutch [student route](../../teaching/praktijk/codex.md).
The [core](../../core/loop.md) remains the routing authority. This adapter uses
ordinary project files and separate Codex CLI invocations, without a new SDK,
MCP server or native subagent configuration.

## Prerequisites and actual environment

You need Git, Python 3.10 or later for the shared exercise, Codex CLI and an account with model access. Check
`codex --version` and `codex login status`; login alone does not prove model
access or available quota. Use the official [Codex documentation](https://learn.chatgpt.com/docs/non-interactive-mode)
for CLI execution and [permission guidance](https://learn.chatgpt.com/docs/permissions)
for its access boundaries. Record the actual CLI/model/configuration used.
The provider handles model requests, Codex executes tools, and the target
repository supplies code and project norms. Claude settings do not grant Codex rights.

Before installation inspect existing AGENTS.md, AGENTS.override.md, nested
instructions, project norms/test commands, .codex/config.toml, execpolicy rules,
skills, hooks and MCP configuration. Include inherited user/managed settings.
Do not print credentials or full account configuration into evidence.
AGENTS discovery is rebuilt for each new run; see
[the instruction documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
New conversations still inherit those instructions. Keep author history and
unrelated reviewer judgments out of automatically loaded instruction files.

## Copy and inspect

Set the source to a coherent checkout of this repository and the target to a
separate existing exercise/project directory. Run with Python 3.9 or later:

```sh
LOOP_SOURCE=/path/to/agent-role-loop
LOOP_TARGET=/path/to/exercise
python3 "$LOOP_SOURCE/adapters/codex/install.py" install "$LOOP_TARGET"
```

The helper copies core plus entry.md, AGENTS.example.md and role-task.md into
`.codex/role-loop/`. It records source commit, copied hashes and created
directories in install.json. These are ordinary files, not permission-granting
Codex configuration. Existing installation or unsafe destination ancestors stop
before copying. Source HEAD identifies origin; hashes record the actual bytes
when a development checkout is dirty. Install released versions from a clean checkout.
An I/O failure during copying can leave a partial directory; inspect it rather
than retrying a blind overwrite. The helper is not a transactional package manager.

Inspect `git diff` and the manifest. Existing project instructions and config
must retain their bytes. The helper does not replace or edit AGENTS.md.
For a new exercise, inspect AGENTS.example.md and copy it to AGENTS.md only if
that file is absent and PROJECT.md contains the applicable norms. For an existing
AGENTS.md, review a targeted link to `.codex/role-loop/entry.md` as an ordinary
project-instruction change; preserve existing content. Check whether a higher
precedence override hides it. No global configuration change is needed.

Start a new invocation at the target root. Explicitly ask it to read the entry,
role and required contracts, even when the project entry also points there.
Use [role-task.md](role-task.md) as an input template: replace all uppercase
placeholders with exact work-item, norms, decisions, criteria and input paths.
No native `/orc` command or named Codex agent is installed by this helper.

## Execute one bounded item

The human orchestrates this route. Save C0 and norms in readable files; when a
tracker URL cannot be read, provide the full contract text with source/version.
A URL alone is not input. Use a fresh invocation for each selected role:

```sh
codex -a never exec -C "$LOOP_TARGET" -s read-only --ephemeral --json \
  -o /tmp/W1-C2.md - < /path/to/planner-task.txt
```

The task names core/roles/planner.md, C0/C1, project norms and C2 output.
`-a never` returns tool failures to the model instead of asking for tool approval;
it does not disable the sandbox. `--ephemeral` avoids persisted session rollouts;
it does not prevent file access or remove project instructions. `--json` exposes
actual command/file-change events; keep raw output out of published evidence.
Save the returned contract before continuing. Output-last-message is a CLI output
file, not permission for the model to modify project files.

For PLANNED the human decides C4 on the concrete C2 and any selected C3 before
building. A prior decision applies only to the same concrete choices, with its
source and comparison recorded. Tool permission is not C4. Then pass C1/C2/C4
and norms to the builder with `-s workspace-write`. Execute the planned tests,
save their actual results and let the human preserve the product commit.
Workspace-write grants broader writable access than a one-file role prompt;
keep the exercise isolated and inspect its diff. Do not use add-dir or a bypass
mode to make a failed action disappear.

Prepare C5 core with the exact product SHA and relevant objective evidence,
criteria, norms, decisions, limits and both persisted repair counters. Give a
NEW `codex exec -s read-only` invocation the strict reviewer role, C5 core and
assigned criteria. No resume/fork, author transcript or other initial verdict.
Read-only restricts writes; it does not make accessible author files unreadable.
Keep raw logs outside the exercise and identify allowed sources in the task.
Use `python3 -B` for Python tests that should not create bytecode cache.

One selected C6 is final; multiple reviews follow core rules. On BLOCK persist
criterion-linked blockers and repair state BEFORE author repair. Re-review is a
new invocation explicitly marked REPAIR with the updated C5 and its before/after
diff, prior blockers, previous unaffected coverage and counters. A new process
does not reset allowances. SHIP means ready for the human merge decision.
The human writes tracker feedback and board state in this first local route;
no native GitHub-review integration is claimed.

## Roll back an unchanged installation

```sh
python3 "$LOOP_SOURCE/adapters/codex/install.py" rollback "$LOOP_TARGET"
```

All owned paths and hashes are checked before any removal. Changed/missing files,
invalid manifest paths or symlinks stop rollback. Unrelated content and existing
directories remain. If you manually added an AGENTS link or copied the example
outside the owned directory, review and undo that change separately; the helper
does not remove project instructions. An existing installation was not overwritten,
so no backup restoration is claimed. Updates require inventory and coherent
version replacement, retaining existing work items' pinned norm basis.

## Verification

The actual implementation and its limits are recorded in
[onderzoek/33-uitvoering.md](../../onderzoek/33-uitvoering.md).
Configuration loading, model execution, independent agent reading and actual
student observations are separate evidence. Missing checks remain unavailable.
