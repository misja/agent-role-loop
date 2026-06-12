# Manual adapter

Runs the role loop with nothing but separate chat windows and copy-paste. You are the orchestrator. This is the most portable adapter - it works with any chat-based model - and the primary form used in the teaching material, because it makes every handoff physically visible.

**Last verified:** 2026-06-12. This adapter has no platform dependencies to drift, only the convention that your chat tool can start a fresh conversation.

## The one rule

> One fresh chat window per role. The only thing that travels between windows is the contract artifact.

No "as I said earlier", no pasting transcripts, no keeping one mega-chat open. If a role seems to need something that is not in its input contract, that is a gap in the artifact - fix the artifact, do not smuggle context.

## What you need

- A chat tool that can start fresh conversations.
- The files in `core/` (roles and contracts), locally or open in a browser.
- The [handoff log template](handoff-log-template.md): one Markdown file per work item where you, the orchestrator, collect C0 through C7.

## Procedure

Setup, once per work item: copy `handoff-log-template.md` to something like `handoff-log-<work-item>.md` and fill in C0, your work item.

Then walk the pipeline. For every agent role the recipe is identical:

1. Open a **fresh** chat window.
2. Paste the role prompt (`core/roles/<role>.md`) as the first message or as the system prompt if your tool supports one.
3. Paste the input artifact(s) the role's **Inputs** section names - nothing else.
4. Copy the returned artifact into your handoff log. Close the window.

In pipeline order:

| Step | Role file | Paste in | Get back |
|---|---|---|---|
| 1 | `core/roles/triage.md` | C0 | C1 |
| 2 | `core/roles/planner.md` | C0, C1 | C2 |
| 3 | `core/roles/clarifier.md` | C2, C0 | C3 |
| 4 | **you, no chat window** - `core/roles/human-gate.md` | C2, C3 | C4 |
| 5 | `core/roles/builder.md` | C2, C4 | C5 |
| 6 | `core/roles/reviewer-strict.md`, `reviewer-pragmatic.md`, `reviewer-adversarial.md`, `reviewer-maintainability.md` - **four separate windows** | core part of C5 each | C6 x4 |
| 7 | `core/roles/reviewer-boss.md` | full C5, all four C6 | C7 |

Branches:

- C1 `REJECT`: stop; follow the advice field.
- C1 `LIGHT`: skip to step 5 with C0 + C1 as a minimal packet.
- C3 `FAIL`: back to step 2 in a fresh window, adding C3 to the planner's input. Third failure in a row: the loop is telling you the work item is the problem.
- C4 `REVISE`: back to step 2 with your required changes. C4 `STOP`: stop.
- C7 `BLOCK`: back to step 5 in a fresh window, adding the must-fix list.

Note on step 4: the Human Gate is you, on purpose. Read the checklist in `core/roles/human-gate.md` and write C4 by hand. If you catch yourself pasting C2 into a chat window and asking a model what to decide, you have automated away the only role that exists to protect your judgment.

Note on step 5: if the builder role runs in a chat window without repository access, it can only produce instructions and code blocks for you to apply. That is workable for small changes; for real codebases, do step 5 in a coding-capable agent and keep the chat windows for the other roles.

## On cost

A full loop spends six or more model conversations on one work item. With free or limited tiers, or local models, that is a real constraint - and the loop respects it by design: Triage exists to keep small work out of the pipeline, and the contracts keep every conversation short. If cost still bites, run the reviewers as two personas instead of four (strict + adversarial covers the most ground) and say so in the handoff log.
