# Handoff log: <work item title>

> Orchestrator: <your name> | Started: <date> | Status: in progress / shipped / stopped
>
> One log per work item. You are the orchestrator: every artifact that crosses a role boundary lands here, in order. If it is not in this log, it did not happen.

## C0 - Work Item

<!-- paste the work item; see core/contracts/work-item.md -->

## C1 - Triage Decision

<!-- from the triage window; FULL_LOOP continues below, LIGHT skips to C5, REJECT ends here -->

## C2 - Build Packet

<!-- from the planner window; on FAIL/REVISE rounds, keep each version: C2 v1, C2 v2, ... -->

## C3 - Clarifier Result

<!-- from the clarifier window; one per packet version -->

## C4 - Gate Decision

<!-- written by YOU, by hand, after the human-gate checklist; not by a model -->

## C5 - Review Handoff

<!-- from the builder; mark the core part and the extended part clearly,
     because the reviewers get only the core part -->

## C6 - Reviewer Verdicts

### Strict

### Pragmatic

### Adversarial

### Maintainability

<!-- four separate windows; do not let one reviewer see another's verdict -->

## C7 - Final Verdict

<!-- from the reviewer-boss window; on BLOCK, the next builder round continues below -->

## Outcome

<!-- shipped / stopped, date, and any follow-up work items spawned -->
