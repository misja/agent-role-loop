# C2 - Build Packet

## Purpose

The Planner's output and the Builder's sole source of truth: an executable plan grounded in the work item (C0) and, where available, in repository facts. A good packet lets the Builder work without inventing requirements and lets the Clarifier and the Human Gate judge the plan without redoing the research. The packet is also where the verification model is chosen, per change, with motivation.

## Schema

Top-level sections, in order:

- **Summary** - one paragraph.
- **Goals** - numbered.
- **Non-goals** - what is explicitly out of scope.
- **Current state** - relevant facts as they are now; label unverified statements as assumptions.
- **Proposed approach** - the shape of the solution and the main design decisions, with rationale.
- **Acceptance criteria** - numbered and testable; carried over from C0 or derived (and then marked as derived).
- **Interfaces / contracts / data changes** - or `<none>`.
- **Changes** - one block per reviewable change (see below).
- **Risks** - or `<none>`.
- **Assumptions** - or `<none>`.
- **Open questions** - or `<none>`. Questions for the Human Gate go here.

Per change:

- **Goal** - one sentence.
- **Non-goals** - or `<none>`.
- **Files or components** - what will be touched; label guesses as assumptions.
- **Implementation checklist** - ordered checkboxes.
- **Verification plan** - one of:
  - `test-first` - name the failing test to write first (red), the expected failure, and the command.
  - `validation-workflow` - the scripted or stepwise check and its expected outcomes. **Motivation required** for not choosing test-first.
  - `manual-with-expected-results` - concrete steps, each with the result that counts as success. **Motivation required** for not choosing test-first.
- **Rollout / rollback** - or `<none>` for trivially reversible work.
- **Done when** - the objective completion condition, referencing acceptance criteria.

## Example

A packet for the C0 example (duplicate rows in CSV export), abbreviated to one change:

```md
## Summary
The export job pages through orders with offset pagination while new
orders arrive, shifting pages and duplicating rows. Switch the export
query to keyset pagination on order ID.

## Goals
1. Exports contain each order exactly once.

## Non-goals
- Changing the export file format.
- Performance work beyond the pagination fix.

## Current state
`export_orders()` pages with LIMIT/OFFSET ordered by creation date
(assumption: confirmed in repo). Orders inserted mid-export shift
subsequent pages.

## Proposed approach
Keyset pagination: order by ID, remember the last seen ID per page,
filter the next page on ID greater than that. No schema change.

## Acceptance criteria
1. Exporting a customer with 3+ pages of orders yields no duplicate order IDs.
2. Exporting a customer with a single page of orders is unchanged.

## Interfaces / contracts / data changes
<none>

### Change 1: keyset pagination in export query

**Goal:** replace offset pagination with keyset pagination in `export_orders()`.

**Non-goals:** <none>

**Files or components:** `exports/orders.py`, `tests/test_export_orders.py`

**Implementation checklist:**
- [ ] Add failing test: insert an order between page fetches, assert no duplicates.
- [ ] Replace OFFSET with keyset filter on order ID.
- [ ] Run full export test suite.

**Verification plan:** `test-first`
- Red: new test `test_no_duplicates_when_orders_arrive_mid_export`,
  expected to fail with a duplicate-ID assertion.
- Command: `pytest tests/test_export_orders.py`

**Rollout / rollback:** <none> (single revertible commit)

**Done when:** AC1 and AC2 pass in CI.

## Risks
- Keyset pagination changes row order from creation date to ID; verify
  no consumer depends on date order.

## Assumptions
- Order IDs are strictly increasing.

## Open questions
<none>
```
