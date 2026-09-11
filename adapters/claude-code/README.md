# Claude Code adapter

Runs the role loop inside [Claude Code](https://code.claude.com): subagents for the responsibilities selected in C1, plus an `/orc` command that follows [the core route](../../core/loop.md) and records required human decisions.

**Last verified:** 2026-06-12, against the official subagent and skills documentation. Platforms change faster than the core; if installation fails, check [code.claude.com/docs](https://code.claude.com/docs/en/sub-agents) and compare.

## How it maps

| Core concept | Claude Code mechanism |
|---|---|
| Role with its own context | Subagent (own context window, own system prompt) |
| Role prompt (`core/roles/*.md`) | Loaded by the subagent at the start of its run |
| Handoff contract | The only content passed in the subagent's task prompt and returned as its result |
| Orchestrator | The `/orc` command running in your main session |
| Human Gate | `/orc` records **your** C4 decision when required; an existing applicable decision remains valid |

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

3. The orchestrator records C1 and selects LIGHT or PLANNED. PLANNED produces
   C2 and, when selected, C3; you decide `PROCEED`, `REVISE` or `STOP` in C4.
   LIGHT uses C0 + C1 directly, with a human decision first when the core requires it.
4. The builder returns C5. The selected independent reviewers return C6. One C6
   is sufficient for a single reviewer; compatible multiple verdicts are summarized
   in C7. The Reviewer Boss is invoked only for unresolved review conflicts.
5. A blocker allows the bounded repair described in the core. A passing verdict
   leaves the merge decision to you.

## Notes

- Record process/norm versions and every acceptance criterion's reviewer in C1.
  Reviewers receive objective evidence and human decisions in C5 core, without
  author transcripts or other initial verdicts.
- Authors may retain context for targeted repair; independent rechecks use the
  C3/C6 repair attachment. Persist design/delivery repair counters with the work
  item. New sessions do not grant extra automatic repair rounds.
- Update core, wrappers and command together. Existing work keeps its pinned
  version; do not reinterpret old `FULL_LOOP` artifacts with new `PLANNED` rules.
- Work items may also live in a tracker. Pass an accessible reference to `/orc`
  or supply the complete artifact when tracker access is unavailable.
- This change checks consistency with the core. It does not revalidate Claude
  platform behavior or establish a measured token saving.
