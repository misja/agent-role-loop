# Triage

The orchestrator performs this responsibility; a separate agent is optional. Follow [loop.md](../loop.md) and produce [C1](../contracts/triage-decision.md), without designing the implementation.

1. Read C0 and applicable process/project norms. Record exact versions and readable locations.
2. Assess size, reversibility, affected contracts, safety boundaries and shared dependencies. Reject unclear work with clarification advice and XL work with splitting advice.
3. Select LIGHT for a small unambiguous correction with concrete criteria and verification; otherwise select PLANNED. If C0 lacks criteria, the planner derives them on PLANNED for human confirmation.
4. Name executors and assign every criterion to a suitable reviewer. Start with one reviewer for bounded work; substantial connected work starts with a clarifier and two relevant perspectives. Explain any deviation and the uncertainty that extra roles resolve. Research normally belongs to the planner.
5. Identify required human decisions and existing applicable approvals. Record persistent repair counters and their work-item location; do not reset an existing run.

Output C1. Route choices, human gates, independent review and repair limits are governed only by loop.md.
