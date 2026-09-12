# C1 - Triage Decision

## Purpose

The orchestrator's concise routing and responsibility record under [loop.md](../loop.md). A separate triage agent is optional.

## Schema

- **Decision** - `LIGHT`, `PLANNED` or `REJECT`.
- **Reason** - short rationale grounded in size, risk and uncertainty.
- **Size assessment** - `XS` / `S` / `M` / `L` / `XL`.
- **Process and norm basis** - exact commits/versions and readable locations for the process and applicable project norms.
- **Risks and dependencies** - affected contracts, safety boundaries and shared consumers, or `<none>`.
- **Responsibilities and executors** - planner, clarifier, builder and selected reviewer(s) as applicable; orchestrator performs triage unless assigned separately. Explain concrete uncertainty justifying extra roles or a separate factual inventory.
- **Criterion assignment** - each acceptance criterion ID mapped to a suitable reviewer; mark criteria still to be derived by C2 and complete assignments before review. A sole reviewer covers every criterion.
- **Repair state** - persistent work-item location, design and delivery automatic rounds consumed (each 0 or 1), and links to any repair or human continuation decisions. Existing counters survive session changes.
- **LIGHT execution basis** - concrete scope, acceptance criteria and verification steps with expected results and chosen model; otherwise `<none>`. No placeholder C2/C3/C4.
- **Human decisions required** - C4 before PLANNED building, or for LIGHT with irreversible effects or a new goal, contract or norm choice; identify existing applicable approvals and sources.
- **Advice** - required for REJECT (clarify or split); otherwise `<none>`.

## Example

```md
Decision: PLANNED
Reason: Bounded export behavior fix; one reviewer can cover both criteria.
Size assessment: S
Process and norm basis: <exact process commit and project norm commit + readable paths>
Risks and dependencies: export consumers may depend on row order
Responsibilities and executors: planner A (includes research), builder B,
  strict reviewer C; no separate clarification uncertainty identified
Criterion assignment: AC1 -> C; AC2 -> C
Repair state: <work-item record>; design 0, delivery 0
LIGHT execution basis: <none>
Human decisions required: C4 on concrete C2 before build
Advice: <none>
```
