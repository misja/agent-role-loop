# C0 - Work Item

## Purpose

The input of the loop: a description of work to be done, in plain Markdown, independent of any issue tracker. A work item gives Triage enough to judge proportionality and gives the Planner enough to ground a plan. It states the desired outcome, not the implementation.

## Schema

Required fields:

- **Title** - one line, imperative ("Fix duplicate rows in CSV export").
- **Context** - why this work exists: the observed problem, the user need, or the motivating event. A short paragraph.
- **Desired outcome** - what is true when the work succeeds, stated as observable behavior.

Optional fields (omit with `<none>`):

- **Acceptance criteria** - numbered, testable statements. If `<none>`, the Planner derives them and the Human Gate confirms them.
- **Constraints** - hard boundaries: deadlines, technologies that must or must not be used, compatibility requirements.
- **Size guess** - the requester's estimate: `XS` / `S` / `M` / `L` / `XL`. Triage may overrule it.

## Example

```md
# Fix duplicate rows in CSV export

## Context
Support reports that monthly CSV exports sometimes contain the same
order twice. It happens only for customers with more than one page of
orders, which suggests the pagination in the export job.

## Desired outcome
An export contains every order exactly once, regardless of how many
pages the order list spans.

## Acceptance criteria
1. Exporting a customer with 3+ pages of orders yields no duplicate order IDs.
2. Exporting a customer with a single page of orders is unchanged.

## Constraints
<none>

## Size guess
S
```
