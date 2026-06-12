# OpenAI-compatible API adapter

Runs the role loop against any endpoint that speaks the OpenAI-compatible chat completions API: local models served by vLLM, llama.cpp, Ollama, LM Studio, or any hosted service with the same surface. There is deliberately no orchestration script in this phase - you (or your own tooling) make one API call per role and carry the artifacts between calls, exactly as in the [manual adapter](../manual/README.md).

**Last verified:** 2026-06-12, against the chat completions request shape (`model`, `messages` with `system`/`user` roles).

## How it maps

One role run = one API call:

- **system message** - the full contents of the role file from `core/roles/`.
- **user message** - the input artifact(s) the role's Inputs section names, labeled with their contract IDs.
- **response** - the output artifact, to be carried (by you) into the next call.

Every call starts a fresh conversation: no shared history between roles, by design. The Human Gate (C4) is not an API call; you write it yourself.

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
- **Reviewers in parallel.** The four reviewer calls are independent: fire them concurrently if you like. Just never feed one reviewer's verdict to another.
