---
description: Run the role loop using the recorded C1 route, human decisions and independent review.
argument-hint: [path-or-reference-to-work-item]
disable-model-invocation: true
---

You are the orchestrator. Read `.claude/agent-role-loop/core/loop.md` as the
canonical routing rule and the contracts it names. Keep current artifacts,
versions, decisions and repair counters; never import a role's transcript.
The work item is at: $ARGUMENTS

## Execution

1. **Intake and route.** Read C0 from the supplied file or accessible tracker
   reference. If unavailable, request the missing artifact. Read the project's
   applicable norms. Write C1 yourself using `core/roles/triage.md` under the
   installed core path; delegate to `role-loop-triage` only when useful. Record
   process/norm versions, risk, selected roles and criterion assignments.
   `REJECT` ends with advice. `LIGHT` goes to building with C0 + C1, subject to
   any required human decision. `PLANNED` goes to planning. Never silently
   reinterpret an old `FULL_LOOP` artifact with the new contracts.
2. **Plan when selected.** Give `role-loop-planner` C0 + C1 and relevant norms
   and decisions. Invoke `role-loop-clarifier` only when selected in C1, with its
   declared inputs. A failed plan may receive one automatic targeted repair and
   independent recheck, using the C3 repair attachment. Preserve the planner's
   context for repair if available; send no transcript to the clarifier. Further
   unresolved blockers require a bounded human continuation, split or stop.
3. **Human decision.** Present the concrete C2 and any C3, or C0 + C1 for a
   LIGHT decision required by the core. Record the human's actual C4 with its
   source. An existing applicable decision is valid input: do not ask again for
   the same approval. Never invent approval. `REVISE` returns to planning with
   the required edits; `STOP` ends the run. New scope or invalid evidence follows
   the replan rule and does not reset repair counters.
4. **Build.** Give `role-loop-builder` the route-specific inputs named by its
   core role, including C1 and pinned norms/decisions. For LIGHT this includes
   C0 + C1; do not manufacture empty C2/C3/C4. Record stop conditions for the
   human. Collect C5 with objective evidence and decisions in the core section.
5. **Independent review.** Start only the reviewers selected in C1, each in a
   fresh context with C5 core, readable norms and assigned criteria. They may
   run in parallel. No reviewer sees the author transcript, extended narrative
   or another initial verdict. Wait for every selected C6. If C2 added criteria,
   update the C1 assignment before review.
6. **Outcome.** One review: C6 is the final verdict. Multiple compatible reviews:
   synthesize C7 mechanically with sources, no new findings or dismissed
   blockers. Conflicting reviews: invoke `role-loop-reviewer-boss` with full C5
   and all selected C6 artifacts. Unresolved goal/risk choices go to the human.
7. **Repair or merge decision.** On BLOCK, give the author the concrete blockers
   and allow one automatic delivery repair including an independent recheck.
   The author may retain context. A reviewer starts independently in explicit
   repair mode with updated C5 core and the C6 repair attachment: repair diff,
   earlier blockers and unaffected coverage, labeled previously established.
   Reassess impacted dependencies; invalid evidence may require replanning and
   wider review. Further blockers go to the human. SHIP and SHIP WITH NITS mean
   ready for the human's merge decision; record follow-up work for nits.

## State and tooling

Store design and delivery repair counters with the work item, across sessions.
A budget limit never converts a blocker to approval. The core defines the limits;
this command maps them to subagent calls, without adding a separate route.

Pass each role its definition, exact artifacts, C1 where required and accessible
norm sources. Return contract artifacts only. If a selected role wrapper is
missing, report the missing file under `.claude/agents/`; do not silently omit
its responsibility. Use only tools and permissions actually available. Keep core,
command and wrappers from the same version when installing updates.
