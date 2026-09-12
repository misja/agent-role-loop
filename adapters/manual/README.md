# Manual adapter

Run the role loop using separate chat windows. You act as the orchestrator and
carry the contract artifacts between roles. The route and repair limits are
specified in [core/loop.md](../../core/loop.md); this page explains how to carry
out that route by hand.

## Preparation

Use a chat tool that can start fresh conversations. Keep the selected version
of `core/` available, including roles and contracts. Record the work item and
handoffs in a tracker or use the [handoff log template](handoff-log-template.md).
Markdown files are one storage option; issue bodies and linked comments can
carry the same fields. This repository uses GitHub for its work items.

Write C1 as the orchestrator, using [the triage role](../../core/roles/triage.md).
A separate triage conversation is optional. Record process and norm versions,
selected responsibilities and the independent reviewer assigned to every
acceptance criterion. Follow the selected route; do not fill unused contracts
with dummy answers.

## Carry out the selected responsibilities

For a new role, open a fresh conversation. Supply its role definition, the
inputs named there, and readable sources for the pinned norms and applicable
human decisions. Save its returned contract with the work item. Do not copy
conversation transcripts between roles.

| Responsibility | Conversation or action | Result |
|---|---|---|
| Planning, when selected | Planner with C0 + C1 and named sources | C2 |
| Plan review, when selected | Independent clarifier with declared inputs | C3 |
| Human decision, when required | You inspect the concrete packet and record your decision; no model decides for you | C4 |
| Building | Builder with LIGHT C0 + C1, or PLANNED C2 + C4, and the remaining inputs its role names | C5 |
| Independent review, every route | One fresh window per reviewer selected in C1, each with C5 core | C6 per reviewer |
| Outcome | One C6 stands on its own; combine compatible C6 artifacts mechanically; use the boss only for conflicting judgments | C6 or C7 |

For LIGHT, start building after C1 unless the core requires a human decision
first. For PLANNED, obtain C4 on the concrete plan before building. Keep an
existing applicable human decision with its source; it need not be requested
again. A human still decides whether to merge after review.

A chat without repository tools cannot apply changes or execute checks. Apply
its proposed patch and run the checks yourself, or use a coding agent for the
builder. Return actual observed evidence and mark checks you could not perform.

## Targeted repair

Keep the author's conversation available for a repair to the same artifact.
The reviewer uses a separate context in explicit repair mode with the contract's
repair attachment. Earlier unaffected coverage must be labeled previously
established, not tested again. Never show other initial verdicts during the
first independent assessment.

Record one design and one delivery repair counter with the work item. Each
permits at most one automatic repair and recheck. Further blockers require a
human decision to continue with a bounded assignment, split or stop. Reopening
a conversation does not reset either counter. Changes that invalidate evidence
follow the core's replan and wider-review rules.

## Updating an installation

Keep the process version with each work item. Install core and adapters together;
`PLANNED` replaces `FULL_LOOP` only for work using the new version. Continue
existing work against its recorded snapshot unless the human explicitly changes
that basis. Lower cost is an intended benefit of selecting responsibilities;
this adapter does not establish a measured saving.
