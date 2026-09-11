# C6 - Reviewer Verdict

## Purpose

One selected reviewer's independent judgment under [loop.md](../loop.md). With one reviewer this is the final verdict; with several it feeds C7. SHIP means ready for the human merge decision.

## Inputs and modes

Initial mode receives C5 core, the assigned criteria and applicable norms, with neither the author's transcript nor other reviewers' verdicts.

Repair mode starts in a fresh context with updated C5 core and an explicit appendix containing the repair diff (before/after revisions), previous criterion-linked blockers, previous coverage of unaffected criteria and the persistent repair state. Review the repair and affected dependencies. Reuse unaffected evidence only while its assumptions remain valid; label it previously established. Scope or dependency changes invalidating evidence require explicit replanning and, where needed, full review under the same persistent counters.

## Schema

- **Reviewer and assignment** - identity/perspective and assigned criterion IDs.
- **Mode and artifact** - `initial` or `repair`, reviewed commit, applicable norm basis and repair appendix sources when used.
- **Decision** - `BLOCK` / `SHIP` / `SHIP WITH NITS`.
- **Acceptance criteria coverage** - each assigned AC: `pass` or `fail`, with evidence and whether newly examined or previously established; list criteria assigned elsewhere explicitly. Unverified assigned criteria cannot pass.
- **Contract drift** - undeclared changes or `<none>`.
- **Must fix** - blockers with criterion IDs, concrete trigger/location, consequence and required outcome; BLOCK requires at least one, including a missing-evidence blocker where appropriate.
- **Should fix** - useful non-blocking findings or `<none>`.
- **Nice to have** - optional improvements or `<none>`.
- **Repair outcome** - disposition of each prior blocker, affected dependencies and limits of reused coverage; `<none>` for initial mode.
- **Next action** - human merge decision, bounded repair if allowance remains, or human continuation/split/stop decision. Never clear a blocker because of a budget or round limit.
