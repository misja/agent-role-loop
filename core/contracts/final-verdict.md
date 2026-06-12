# C7 - Final Verdict

## Purpose

The merged outcome of the review stage, produced by the Reviewer Boss from the four independent verdicts (C6) and the full review handoff (C5). It de-duplicates findings, resolves disagreements explicitly, and tells the Builder exactly what happens next. Priority rule, fixed: **correctness and safety first, then maintainability, then polish.**

## Schema

All fields of C6 (Decision, Must fix, Should fix, Nice to have, Acceptance criteria coverage, Contract drift), with findings de-duplicated and ordered by the priority rule, plus:

- **Reviewer disagreements** - each disagreement with its resolution and the reasoning; or `<none>`.
- **Builder next action** - one concrete instruction: what to do with the verdict (merge, fix the must-fix list and resubmit, or escalate to a human).

## Example

```md
Decision: SHIP WITH NITS

Must fix: <none>

Should fix:
- Comment the strictly-increasing-ID invariant at the keyset filter
  (strict + adversarial reviewers, merged).

Nice to have:
- Parameterize page size in _fetch_page() (maintainability reviewer).

Acceptance criteria coverage:
- AC1: pass - regression test, confirmed by all four reviewers.
- AC2: pass - single-page equality test.

Contract drift: <none>

Reviewer disagreements:
- Adversarial wanted BLOCK over legacy imports possibly violating the
  ID invariant; extended evidence shows the gate already decided this
  (decision recorded in C4) and the invariant is checked in the test
  fixture. Resolved to SHIP WITH NITS.

Builder next action:
- Apply the should-fix comment, then merge. Nits may move to a
  follow-up work item.
```
