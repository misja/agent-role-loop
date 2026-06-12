# Claude Code adapter

Runs the role loop inside [Claude Code](https://code.claude.com): one subagent per agent role, plus an `/orc` command that orchestrates the pipeline and stops at the Human Gate for your decision.

**Last verified:** 2026-06-12, against the official subagent and skills documentation. Platforms change faster than the core; if installation fails, check [code.claude.com/docs](https://code.claude.com/docs/en/sub-agents) and compare.

## How it maps

| Core concept | Claude Code mechanism |
|---|---|
| Role with its own context | Subagent (own context window, own system prompt) |
| Role prompt (`core/roles/*.md`) | Loaded by the subagent at the start of its run |
| Handoff contract | The only content passed in the subagent's task prompt and returned as its result |
| Orchestrator | The `/orc` command running in your main session |
| Human Gate | `/orc` stops and asks **you** for the C4 decision |

The orchestrator keeps its own context small on purpose: current stage, current artifact, decision, next action. Role transcripts stay inside the subagents.

## Installation

From the root of this repository, copy three things into the target project:

```sh
TARGET=/path/to/your/project
mkdir -p "$TARGET/.claude"
cp -r adapters/claude-code/agents   "$TARGET/.claude/"
cp -r adapters/claude-code/commands "$TARGET/.claude/"
mkdir -p "$TARGET/.claude/agent-role-loop"
cp -r core "$TARGET/.claude/agent-role-loop/"
```

The subagents read their role definitions from `.claude/agent-role-loop/core/`, so the third copy is not optional.

Subagents are loaded at session start: restart your Claude Code session after installing.

> Note: `.claude/commands/orc.md` is the classic custom-command form. Custom commands have been merged into skills; the same file works unchanged as `.claude/skills/orc/SKILL.md` if you prefer the skill layout.

## Usage

1. Write a work item (C0) as a Markdown file, following `core/contracts/work-item.md`. Convention: put work items in `work-items/`.
2. In Claude Code, run:

   ```text
   /orc work-items/fix-duplicate-export-rows.md
   ```

3. The command runs Triage -> Planner -> Clarifier, then **stops** and shows you the build packet (C2) and the clarifier result (C3). You reply with a C4 Gate Decision: `PROCEED`, `REVISE` (with required changes), or `STOP`.
4. On `PROCEED` it runs the Builder, then the four reviewers in parallel, then the Reviewer Boss, and reports the final verdict (C7).

## Notes

- The gate is not skippable. If you find yourself wanting to skip it, use Triage's `LIGHT` path instead: that is what it is for.
- Reviewers run as four parallel subagents that each receive only the core part of C5. Do not "help" them with extra context; their isolation is the point.
- Token cost: a full loop spends multiple subagent runs on one work item. Let Triage reject work that does not need the loop.
