# C5 - Review Handoff

## Purpose

The Builder's reviewable account. Core carries the basis for judgment to every reviewer; extended material preserves useful author history without putting that history into initial independent review. Routing and repair limits are defined in [loop.md](../loop.md).

## Core handoff (all reviewers)

- **Artifact** - work-item reference, exact reviewable commit and base/diff reference, plus readable artifact locations.
- **Process and norm basis** - exact process and applicable project norm commits/versions and readable sources.
- **Scope and human decisions** - accepted C0/C1 or C2 basis; relevant human decisions, authorized deviations and deferred questions, each with source and artifact to which it applies; `<none>` where absent.
- **Diff summary** - 2 to 5 bullets.
- **Changed files or components** - list.
- **Acceptance criteria coverage and assignment** - each criterion ID, implementation location, verification evidence and responsible reviewer from the updated C1/C2 mapping.
- **Contracts touched** - APIs, types, events, schema, data, permissions and shared consumers; or `<none>`.
- **Objective verification evidence** - model, commands or manual steps, expected and observed outcomes, evidence locations and tested revision. Include relevant before/after proof and tests/checks added or updated; explain inapplicable before proof. State failures, unavailable checks and what was not established explicitly.
- **Deviations and follow-ups** - changes from the accepted basis with rationale and decision source; unresolved limitations and deliberately deferred work, or `<none>`.
- **Repair state** - persistent design/delivery counters and repair/continuation references. For repair review attach the explicit C6 repair appendix separately.

## Extended handoff (author history; full C5 for arbitration)

- **Exploration and discarded attempts** - relevant history, or `<none>`.
- **Additional logs and refactoring history** - readable sources, or `<none>`.

Evidence or decisions needed to judge a criterion must be in core, even if detailed logs also appear in extended. A missing observation is unavailable, not a claimed success.
