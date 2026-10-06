# Mistral through Vibe

Technical installation and maintenance reference. For the student walkthrough,
use [Een werkitem uitvoeren met Mistral](../../../teaching/praktijk/mistral.md).
This route uses Mistral as model provider, Vibe as CLI tool executor, and a separate
Git repository as project environment. A [bare compatible API call](../README.md)
receives messages; it does not acquire Vibe's file tools or permissions.

## Prerequisites and version

Use a disposable project with Python 3.10+ for the installer and books exercise,
Git, and a working Vibe CLI/account. Vibe itself has its own Python requirements;
follow the [official installation instructions](https://github.com/mistralai/mistral-vibe)
for your platform rather than installing it into the exercise's Python environment.
On 6 October 2026 the local CLI was `vibe 2.19.0`. Check `vibe --version` and
`vibe --help` on your machine. Authenticate through Vibe's supported account
setup; API-key users can use `vibe --setup`. Keep credentials in the supported
credential store, outside repository files and published logs. Credential presence
is not proof of successful model access or available quota.

Record configured model alias, actual API model name and provider separately.
The measured configuration used alias `mistral-medium-3.5`, API name
`mistral-vibe-cli-latest`, provider `mistral`, endpoint `https://api.mistral.ai/v1`.
An alias or `latest` does not identify immutable model weights. This is not a
provider benchmark. Actual run evidence and limits belong in
[the execution register](../../../onderzoek/34-uitvoering.md).

## Inspect before installation

Inventory AGENTS.md files and applicable ancestor/user instructions, project
norms/test commands, `.vibe/config.toml`, agent profiles, prompts, skills, hooks,
MCP servers, connectors, tool permissions and trusted folders. User profiles can
replace built-in names; inspect the effective `plan`/`accept-edits` definitions.
For the measured 2.19.0 route, user files are under `~/.vibe/` unless `VIBE_HOME`
points elsewhere. Inspect user and trusted-project `.vibe/config.toml`,
`agents/{plan,accept-edits}.toml`, `hooks.toml`, prompts/, skills/ and tools/;
also inspect extra paths named in config and user/project `.agents/skills`.
The [student preflight](../../../teaching/praktijk/mistral.md#1-projectafspraken-inventariseren-en-adapter-toevoegen)
provides a no-provider-launch path inspection command and a field checklist.
Look for `bypass_tool_permissions`, `agent_paths`, `tool_paths`, `skill_paths`,
`mcp_servers`, `system_prompt_id`, tool selection and `[tools...]` permissions.
Record applicable VIBE_* process overrides without printing credential values.

Trusted project content can change configuration discovery. Agent overrides apply
on top of base settings; a custom profile can replace a built-in name and change
even a CLI-selected tool allow-list. A hook is executable code run around events,
not a model tool, so inspect its event/command before assuming the allow-list
bounds all program actions. The measured route had no custom profiles or hooks.
If those or unexplained overrides exist, stop before the role invocation and
resolve their effect with the configuration owner; do not overwrite global
settings. Recheck effective tool metadata and permission bypass for actual runs.
Do not copy secrets from config or credential stores. A new conversation does
not erase this configuration. Keep author transcripts and unrelated judgments
outside project instructions and the reviewable working tree.

Choose a source checkout of this repository and a separate existing target.
In the examples, set these two variables to their **absolute** directories:

```sh
ROLE_LOOP_SOURCE=/absolute/path/to/agent-role-loop
EXERCISE=/absolute/path/to/exercise
python3 "$ROLE_LOOP_SOURCE/adapters/openai-compatible/mistral/install.py" install "$EXERCISE"
```

This copies the current core plus entry.md, AGENTS.example.md and role-task.md
into `.vibe/role-loop/`. These are ordinary files, not auto-loaded agent profiles.
The manifest records source HEAD, file hashes and directories created. Inspect
source changes before copying: HEAD provenance plus hashes does not imply the
source working tree was clean. Existing AGENTS/config are preserved byte for byte.
Conflicts and unsafe destination ancestors stop before copying. I/O interruption
can still leave partial files; installation is not a filesystem transaction.

Inspect `.vibe/role-loop/install.json`, compare copied core with the selected
source and review `git diff`/`git status`. In a new exercise without AGENTS.md,
inspect the copied example and copy it to AGENTS.md; create PROJECT.md with your
norms and test command first. In an existing project, add a reviewed reference to
`.vibe/role-loop/entry.md` in its own projectingang instead of replacing it.
That manual change is outside installer ownership.

For rollback:

```sh
python3 "$ROLE_LOOP_SOURCE/adapters/openai-compatible/mistral/install.py" rollback "$EXERCISE"
```

Rollback verifies all owned paths/hashes before deletion and stops if an owned
file changed or is missing. It removes unchanged owned files and only empty
owned directories, retaining unrelated content. Restore any manual AGENTS edit
separately using its recorded original/diff. Never remove the entire `.vibe`
directory: it may contain pre-existing configuration. Retain changed files until
you have reviewed why they differ.

## Explicit roles and tool boundaries

Fill every uppercase field in role-task.md. Provide actual C0/C1 and readable
project/process norm versions, not only URLs a role cannot fetch. Planner inputs
are C0+C1+repository facts; builder inputs are approved C2+C4 and norms; initial
review inputs are C5 core+assigned criteria+exact product+norms/decisions. The
human records decisions, saves outputs and performs Git/tracker operations.
Follow core/loop.md for route selection, criterion assignment and repair limits.

Use a fresh process for each role, never `--continue` or `--resume` for independent
review. In Vibe 2.19.0 the text replacement tool is `edit`, not `search_replace`.
The following explicit allow-lists exclude bash, task and external tools.
Inspect profiles and hooks first: tool allow-lists do not disable arbitrary hooks.
These per-process overrides disable automatic project-context injection and
connectors, without editing user config. Provide PROJECT.md and relevant code
explicitly in the task. AGENTS discovery still applies. The output JSON and Vibe
session logs may contain prompts/tools; store them outside the exercise and share
only selected objective evidence and contract outputs.

From the exercise directory, with planner-task.txt filled in:

```sh
VIBE_INCLUDE_PROJECT_CONTEXT=false VIBE_ENABLE_CONNECTORS=false \
  vibe --workdir . --trust --agent plan \
  --enabled-tools read_file --enabled-tools grep \
  --max-turns 40 --max-price 2 --output json \
  -p "$(cat planner-task.txt)" > /tmp/W1-planner.json
```

`--trust` permits this invocation to load inspected project content without
persisting trust. It is not a sandbox or a C4 decision. `--max-price` is a CLI
stop threshold in dollars, not a guarantee about billing/quotum. Limits and API
errors can stop a role before its contract is complete; inspect both exit status
and actual output. Vibe 2.19.0 emits a JSON list of messages; save the final assistant
message as the contract only after reading it. Do not treat a tool-call message
or a process exit0 alone as a complete contract.

After inspecting the response, extract its final assistant text, for example:

```sh
python3 - /tmp/W1-planner.json work-items/W1/C2.md <<'PYTHON'
import json, pathlib, sys
messages = json.loads(pathlib.Path(sys.argv[1]).read_text())
text = next(m["content"] for m in reversed(messages)
            if m["role"] == "assistant" and m.get("content"))
pathlib.Path(sys.argv[2]).write_text(text + "\n")
PYTHON
```

The extractor does not validate the contract; the human reads it before using it.
Use the same command for a reviewer with reviewer-task.txt and a new output
path. For a builder, change to `--agent accept-edits` and add exactly:

```sh
--enabled-tools write_file --enabled-tools edit
```

The allowed writes exceed the task's one-file scope; inspect the actual diff.
Read-only tool selection excludes edits but is not OS isolation or a guarantee
that only named inputs are readable. Vibe checks file access/trust and approvals;
we do not claim containment against malicious instructions. Keep the task in a
separate clean example with no production data, and inspect failures rather than
adding shell or `--auto-approve` to make them disappear.

The official [permissions page](https://docs.mistral.ai/vibe/code/safety-approvals-permissions)
and [configuration reference](https://docs.mistral.ai/vibe/code/cli/configuration-reference)
differed from local 2.19.0 help about programmatic default approval behavior on
the verification date. This route relies on explicit profiles and allow-lists,
not those defaults. Recheck installed behavior when upgrading.

## Human test/Git evidence and repair

The model cannot run tests or Git in this route. Before the builder, the human
runs the full suite on the unchanged basis and saves stdout/stderr/exitcode. After
the builder, inspect the diff and rerun the same command. Commit only the product
file. In C5 core put exact base/product commits, actual code snapshot from that
commit, full test output, supplied-suite hash, criteria and sources. This lets a
read-only reviewer compare the current file with committed content and judge
human-supplied evidence without pretending to execute tests.

For this books exercise, record evidence with ordinary human shell actions:

```sh
python3 -B controleer.py werk volledig > /tmp/W1-green.txt 2>&1
TEST_EXIT=$?
echo "$TEST_EXIT" > /tmp/W1-green-exit.txt
git diff -- boekenplank.py
git add boekenplank.py
git commit -m "Add optional availability filter"
git rev-parse HEAD
git show HEAD:boekenplank.py > /tmp/W1-committed-code.py
python3 -c 'import hashlib; print(hashlib.sha256(open("controleer.py", "rb").read()).hexdigest())'
```

Read the real output and require exit0 before committing an accepted product.
Copy the commit snapshot and the result/exit files into the designated C5 evidence
paths, with their source commit and command. The snapshot is content evidence,
not an independent Git lookup by the reviewer. Red evidence uses the same test
command before editing and records the basis SHA; retain exit1 rather than
turning a failure into a successful shell pipeline.

A builder's C5 draft must mark pending green evidence/commit as pending. Complete
it with actual observations before review. Keep maker logs and C2 narrative out
of initial review. A repair reviewer gets a separate explicit appendix with
before/after diff, prior blockers, previously established unaffected coverage
and persisted counters. Persist consumed allowance **before** author repair.
No new process resets it. SHIP releases a human merge decision, not automatic merge.

For a bare Mistral HTTP call instead, use the
[official chat-completion instructions](https://docs.mistral.ai/studio/conversations/chat-completion)
and [migration guide](https://docs.mistral.ai/resources/migration-guides), supplying
role/norm/file content yourself. That alternate route has not acquired repository
access or been exercised by the Vibe evidence. Missing account/provider steps
remain unverified; do not label a local fixture check as a completed Mistral run.
