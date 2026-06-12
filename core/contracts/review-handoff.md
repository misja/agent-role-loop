# C5 - Review Handoff

## Purpose

The Builder's account of what was built and how it was proven, in two parts with different audiences. The **core handoff** goes to every reviewer: just enough to judge the change on its own merits, with no build history attached. The **extended handoff** goes only to the Reviewer Boss: the evidence trail (red/green or its equivalent), deviations, and loose ends. Keeping the parts separate is what keeps the reviewers' contexts clean.

## Schema

### Core handoff (to all reviewers)

- **Diff summary** - 2 to 5 bullets.
- **Changed files or components** - list.
- **Acceptance criteria coverage** - the numbered ACs from the packet, each with where it was implemented.
- **Contracts touched** - API, types, events, schema, data, permissions - or `<none>`.

### Extended handoff (to the Reviewer Boss only)

- **Tests** - added or updated, with coverage notes; or the equivalent artifact of the chosen verification model.
- **Red evidence** - the failing test or check before the change, with the failure summary. For non-test-first models: the observed failing state.
- **Green evidence** - the passing command or check after the change.
- **Refactor after green** - or `<none>`.
- **Deviations** from the packet - or `<none>`; each with rationale.
- **Follow-ups not done** - discovered but deliberately left, or `<none>`.

## Example

```md
## Core handoff

### Diff summary
- Export query now uses keyset pagination on order ID instead of LIMIT/OFFSET.
- New regression test inserts an order mid-export and asserts unique IDs.
- Single-page export path untouched; covered by an equality test.

### Changed files or components
- exports/orders.py
- tests/test_export_orders.py

### Acceptance criteria coverage
1. No duplicates on 3+ pages - implemented in exports/orders.py
   (keyset filter), proven by test_no_duplicates_when_orders_arrive_mid_export.
2. Single-page export unchanged - proven by test_single_page_export_unchanged.

### Contracts touched
<none>

## Extended handoff

### Tests
2 added, 0 updated. Mid-export insertion and single-page equality.

### Red evidence
pytest tests/test_export_orders.py -> 1 failed:
AssertionError: order 4102 appears 2 times

### Green evidence
pytest tests/test_export_orders.py -> 14 passed

### Refactor after green
Extracted page-fetch closure into _fetch_page(); touched area only.

### Deviations
<none>

### Follow-ups not done
- Offset pagination in the admin order list has the same flaw;
  separate work item suggested.
```
