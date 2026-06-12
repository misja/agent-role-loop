# C6 - Reviewer Verdict

## Purpose

One reviewer's independent judgment of the core review handoff (C5). Four personas produce one verdict each, in isolation: none sees another's verdict before finishing its own. The verdict separates what must change from what could change, and traces every acceptance criterion to evidence.

## Schema

Required fields:

- **Decision** - `BLOCK` / `SHIP` / `SHIP WITH NITS`.
- **Acceptance criteria coverage** - per AC: `pass` or `fail`, plus the evidence relied on.
- **Contract drift** - mismatches between the declared "contracts touched" and what the diff actually changes; or `<none>`.

Optional fields (omit with `<none>`):

- **Must fix** - blocking findings; a `BLOCK` decision requires at least one.
- **Should fix** - high-value but non-blocking findings.
- **Nice to have** - cheap improvements and taste.

## Example

```md
Decision: SHIP WITH NITS

Must fix: <none>

Should fix:
- The keyset filter assumes strictly increasing IDs; add a one-line
  comment citing where that invariant is guaranteed.

Nice to have:
- _fetch_page() could take the page size as a parameter instead of
  reading the module constant.

Acceptance criteria coverage:
- AC1: pass - regression test inserts mid-export, asserts unique IDs.
- AC2: pass - single-page equality test.

Contract drift: <none>
```
