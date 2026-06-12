# C4 - Gate Decision

## Purpose

The human judgment between planning and building. The gate exists to stop confident automation from charging past judgment calls; it is the one contract in the loop that **must be filled in by a person**. The decision releases the Builder, sends the packet back, or stops the run, and it records the human decisions so downstream roles can rely on them without re-litigating.

## Schema

Required fields:

- **Decision** - `PROCEED` / `REVISE` / `STOP`.
- **Reason** - one short paragraph.

Conditional and optional fields (omit with `<none>`):

- **Required changes before build** - required when the decision is `REVISE`; numbered, addressed to the Planner.
- **Human decisions made** - answers to the packet's open questions and any scope or risk calls made at the gate.
- **Open questions still deferred** - questions explicitly judged safe to defer, so deferral is visible rather than silent.

The role description ([roles/human-gate.md](../roles/human-gate.md)) carries the checklist that grounds the decision: the goal is still right, the scope and non-goals are acceptable, the acceptance criteria are testable, the verification plan is credible, risky operations are reversible where possible, and the builder can execute without inventing requirements.

## Example

```md
Decision: PROCEED

Reason: Revised packet v2 reviewed; every AC now has a verification
step and the row-order question is answered below. Risk is low and
the change is a single revertible commit.

Required changes before build: <none>

Human decisions made:
- Date order in exports is not a documented guarantee; ID order is
  acceptable. Release note will mention it.

Open questions still deferred: <none>
```
