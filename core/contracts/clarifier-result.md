# C3 - Clarifier Result

## Purpose

The Clarifier's verdict on a build packet (C2): is it unambiguous, grounded, and verifiable enough to hand to a builder? A `FAIL` is cheap here and expensive later, so the result errs toward strictness. The result either passes the packet to the Human Gate or returns it to the Planner with specific, numbered edits.

## Schema

Required fields:

- **Verdict** - `PASS` or `FAIL`.
- **Reason** - one short paragraph.

Conditional and optional fields (omit with `<none>`):

- **Requested edits** - numbered; required when the verdict is `FAIL`. Each edit names the packet section it applies to.
- **Questions for the planner** - ambiguities that need an answer, not a redesign.
- **Risks to acknowledge** - risks the packet should name even if the verdict is `PASS`.
- **Sign-off criteria** - what a revised packet must show for the next review to pass; required when the verdict is `FAIL`.

## Example

```md
Verdict: FAIL

Reason: The packet is grounded and the approach is sound, but AC2 has
no verification path and the row-order risk is unresolved.

Requested edits:
1. (Change 1, verification plan) Add a test or check covering AC2: a
   single-page export is byte-identical before and after the change.
2. (Risks) Resolve the row-order risk: name the consumers of the
   export, or scope the date-order guarantee out explicitly.

Questions for the planner:
1. Are order IDs strictly increasing for legacy imports too?

Risks to acknowledge: <none beyond the above>

Sign-off criteria:
- Every AC has a named verification step.
- Row-order dependency confirmed absent or declared out of scope.
```
