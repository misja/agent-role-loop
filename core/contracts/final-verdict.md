# C7 - Final Verdict

## Purpose

The outcome when multiple selected C6 reviews exist. For one reviewer C6 suffices. Under [loop.md](../loop.md), compatible reviews are synthesized by the orchestrator; unresolved substantive disagreement goes to the Reviewer Boss for arbitration with all C6s and full C5.

## Schema

Include C6 decision, criterion coverage, contract drift and prioritized must/should/nice findings, plus:

- **Mode and producer** - `synthesis` (orchestrator) or `arbitration` (Reviewer Boss).
- **Inputs** - exact C5 artifact/version and every selected C6; identify missing verdicts and wait rather than issuing a partial final decision.
- **Source traceability** - source reviewer and finding/criterion IDs for every combined finding and coverage claim.
- **Reviewer disagreements** - each disagreement, evidence, resolution and rationale; `<none>` for compatible synthesis. Unresolved goal/risk choices go to the human and remain blocking.
- **Next action** - human merge decision, repair under the recorded allowance, or human bounded continuation/split/stop. SHIP never means automatic merge.

Synthesis introduces no new findings and cannot discard or outvote blockers. Arbitration resolves arguments against evidence, with correctness and safety first, then maintainability, then polish. Record any contradiction found in the handoff or evidence explicitly. Retain unresolved blockers regardless of budget or round limits.
