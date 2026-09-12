# C4 - Gate Decision

## Purpose

The human judgment between planning and building. The gate exists to stop confident automation from charging past judgment calls; the decision **must come from a person**. The orchestrator may record that decision faithfully with its source, but cannot supply approval on the human’s behalf. The decision releases the Builder, sends the packet back, or stops the run, and it records the human decisions so downstream roles can rely on them without re-litigating.

## Schema

Required fields:

- **Artifact and source** - exact C2 version (and C3 if selected), or concrete C0 + C1 for LIGHT; human decision source and applicable norm basis.
- **Decision** - `PROCEED` / `REVISE` / `STOP`.
- **Reason** - one short paragraph.

Conditional and optional fields (omit with `<none>`):

- **Required changes before build** - required when the decision is `REVISE`; numbered, addressed to the responsible author, with the bounded continuation scope and persistent repair state.
- **Human decisions made** - answers to the packet's open questions and any scope or risk calls made at the gate.
- **Open questions still deferred** - questions explicitly judged safe to defer, so deferral is visible rather than silent.

The role description ([roles/human-gate.md](../roles/human-gate.md)) carries the checklist that grounds the decision: the goal is still right, the scope and non-goals are acceptable, the acceptance criteria are testable, the verification plan is credible, risky operations are reversible where possible, and the builder can execute without inventing requirements.

## Example

```md
Artifact and source: C2 v2, C3 PASS; <human decision source and norm basis>
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
