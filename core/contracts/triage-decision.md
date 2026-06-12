# C1 - Triage Decision

## Purpose

The proportionality verdict on a work item (C0): does this work deserve the full loop, a lightweight path, or no loop at all? The decision is deliberately short. Its value is in routing, not analysis; analysis belongs to the Planner.

## Schema

Required fields:

- **Decision** - one of:
  - `FULL_LOOP` - enter the pipeline at the Planner.
  - `LIGHT` - skip planning and review; hand the work item to the Builder with a minimal packet. For XS work that is reversible and touches no contracts.
  - `REJECT` - the loop is the wrong tool. Either too small for any process, or too large (XL) and in need of splitting first.
- **Reason** - at most three sentences.
- **Size assessment** - `XS` / `S` / `M` / `L` / `XL`, confirming or overruling the requester's guess.

Conditional field:

- **Advice** - required when the decision is `REJECT`: what the requester should do instead (do it by hand, or split along which seams). Otherwise `<none>`.

## Example

```md
Decision: FULL_LOOP

Reason: A behavior bug in a customer-facing export with a plausible
root cause but no proof yet. Small enough for one packet, risky enough
to deserve review.

Size assessment: S (confirms requester's guess)

Advice: <none>
```
