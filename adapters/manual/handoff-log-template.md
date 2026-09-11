# Handoff log: <work item title>

> Orchestrator: <name> | Started: <date> | Status: <in progress / ready for human merge / stopped>
>
> Store artifacts here or link to their exact tracker versions. Preserve prior
> versions and decisions. Omit sections the selected route does not use.

## C0 - Work Item

<!-- core/contracts/work-item.md -->

## C1 - Triage Decision

<!-- Orchestrator or optional triage role: LIGHT / PLANNED / REJECT.
     Include pinned process/norm versions, risk, role selection and every AC assignment. -->

## Repair state

- Design automatic repairs used: 0 / 1
- Delivery automatic repairs used: 0 / 1
- Human continuation/replan decisions and source: <none>

<!-- Counters persist across sessions. Record affected criteria and evidence validity. -->

## C2 - Build Packet (PLANNED)

<!-- Keep versioned packets and update C1 if criteria change. -->

## C3 - Clarifier Result (if selected)

<!-- Initial or repair mode; use the contract's repair attachment on recheck. -->

## C4 - Human Gate Decision (when required)

<!-- Record the actual human decision and its source, not an agent's approval.
     May refer to concrete C2 or LIGHT C0 + C1. -->

## C5 - Review Handoff

<!-- Mark core and extended sections. Core includes reviewed commit, norms,
     human decisions, criterion assignment and objective verification evidence. -->

## C6 - Selected Reviewer Verdicts

<!-- One per selected independent reviewer; first reviews cannot see one another.
     For repair: updated core, repair diff, prior blockers and unaffected coverage
     labeled previously established. -->

## C7 - Final Verdict (multiple reviewers only)

<!-- Mechanical synthesis of compatible verdicts by orchestrator, or arbitration
     by boss for conflicts. Wait for all selected C6s. Never discard blockers. -->

## Outcome and human merge decision

<!-- SHIP / SHIP WITH NITS means ready for human decision, not merged.
     Record actual decision, date, source and follow-up work items. -->
