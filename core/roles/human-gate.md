# Human Gate

## Role

**This is a role description for a person, not an agent prompt.** Every other role in this loop may be performed by an agent; this one may not. The gate exists to stop confident automation from charging past judgment calls, and automating it would optimize away exactly the protection it provides. That asymmetry is deliberate, and worth understanding: checks on goals, scope, and acceptable risk belong to whoever bears the consequences.

You are the judgment checkpoint between planning and building. You decide whether the packet gets built, gets revised, or stops here.

## Inputs

- C2 Build Packet
- C3 Clarifier Result
- Your own knowledge of intent, priorities, and acceptable risk - the one input no other role has

## Guardrails

- Do not rubber-stamp. If you have not read the packet's open questions, you have not gated.
- Do not redesign at the gate. If the approach is wrong, send it back with `REVISE` and say why; do not rewrite the packet yourself.
- Answer open questions explicitly or defer them explicitly. Silent deferral is the only forbidden move.
- Your decisions become part of the record (C4). Downstream roles will rely on them without asking again.

## Procedure

Walk the checklist:

1. Is the goal still the right goal?
2. Is the scope acceptable? Are the non-goals acceptable?
3. Are the acceptance criteria testable?
4. Is the verification plan credible - and where it is not `test-first`, is the motivation honest?
5. Are risky operations planned and reversible where possible?
6. Are the open questions answered (by you, now) or explicitly safe to defer?
7. Can the builder execute this without inventing requirements?

All yes -> `PROCEED`. Fixable gaps -> `REVISE` with numbered required changes. A question only the outside world can answer, or a goal that no longer holds -> `STOP`.

## Stop conditions

- You find yourself approving because the packet is long and well-formatted rather than because you agree with it. Stop, take a break, gate again.
- The decision hinges on something outside your authority -> `STOP` and name whose decision it is.

## Output

- C4 Gate Decision, filled in by you

## Why this is a human

A reviewer agent can check that acceptance criteria are testable; it cannot know whether the goal is still worth pursuing, whether this week is the wrong week to touch billing, or whether a risk that looks small on paper is unacceptable in your context. The gate is where accountability lives. Treat the five minutes it costs as the cheapest insurance in the loop.
