# OpenAI-compatible API adapter

Runs the role loop against any endpoint that speaks the OpenAI-compatible chat completions API: local models served by vLLM, llama.cpp, Ollama, LM Studio, or any hosted service with the same surface. There is deliberately no orchestration script in this phase - you (or your own tooling) make one API call per role and carry the artifacts between calls, exactly as in the [manual adapter](../manual/README.md).

**Last verified:** 2026-06-12, against the chat completions request shape (`model`, `messages` with `system`/`user` roles).

## How it maps

A role can be invoked with the following request shape:

- **system message** - the full contents of the role file from `core/roles/`.
- **user message** - the input artifact(s) the role's Inputs section names, labeled with their contract IDs.
- **response** - the output artifact, to be carried (by you) into the next call.

Start independent roles with separate message histories. An author may retain
its own history for targeted repair. The Human Gate (C4) is a recorded human
decision, never a model response. Follow [core/loop.md](../../core/loop.md) for
role selection, criterion assignments and repair limits. Triage may be performed
by the orchestrator; only call roles selected in C1. One reviewer returns the
final C6; multiple compatible verdicts can be summarized mechanically in C7.
The boss call is only for conflicting verdicts.

## Examples

[`examples/`](examples/) contains one payload per agent role. The placeholders in angle brackets are to be replaced before sending; the payloads are valid JSON as they stand.

Send one like this:

```sh
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d @examples/planner.json
```

## Practical notes

- **Model choice per role.** Nothing requires one model for all roles. Triage is fine on a small fast model; the planner and the adversarial reviewer benefit from the strongest model you have.
- **Temperature.** The examples use a low temperature; these roles reward precision over creativity.
- **Context length.** The contracts are designed to be compact, which is what makes the loop workable on local models with modest context windows. If an artifact does not fit, that is usually a sign the work item is too big - re-triage rather than truncate.
- **No repository access.** A bare chat completion cannot read your repo. The planner must then label file-level statements as assumptions (its role prompt already requires this), and the builder produces patches for you to apply. If your serving stack supports tool calling, you can do better, but that is beyond this phase.
- **Reviewers in parallel.** The selected initial reviewer calls are independent and may run concurrently. Include decisions and objective evidence in C5 core, but no other initial verdicts. Repair calls use updated C5 core and the explicit C6 repair attachment.

## Version and repair state

Keep the process/norm version and design/delivery repair counters outside the
API conversation, with the work item. Apply the core's one automatic repair
limit per phase, including recheck. A new API request does not reset the counter;
remaining blockers require the human's bounded continuation, split or stop.
Do not mark unavailable checks as passed or earlier evidence as newly verified.

Update examples and core together. `PLANNED` belongs to the new contract version;
existing work using `FULL_LOOP` stays on its recorded snapshot unless the human
explicitly changes its basis. These JSON files are request templates, not an
orchestrator or a provider integration test.
