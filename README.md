# agent-role-loop

A portable, tool- and model-agnostic multi-agent workflow for engineering work, plus teaching material (in Dutch) that uses the same workflow to teach software engineering students about context isolation, interfaces, and proportional use of tooling.

A developer hands a change and its test results to a colleague, who checks whether the tests cover the reported problem. This workflow applies that separation of responsibilities to work with agents. The [teaching introduction](teaching/index.md) develops the example for students familiar with software engineering and web chat.

A program can call a language model through an API, supply its task context, execute permitted tool requests, and return their results to the model. A system that uses this cycle to choose and carry out steps towards a task is called an agent here. It can carry out different roles in separate sessions.

The loop:

```text
Work item -> Triage -> Planner -> Clarifier -> Human Gate -> Builder -> Reviewers (parallel) -> Reviewer Boss
```

## Why this exists

A builder's conversation may contain early assumptions, failed attempts, and decisions that no longer apply. Giving a reviewer that entire history can carry those assumptions into the review. The loop gives each role its own context and passes structured handoffs containing the requirements, results, and evidence needed for the next task. Missing requirements can still lead to an inadequate review.

This applies separation of concerns and information hiding to the work process. Handoff contracts form the stable interfaces; role prompts implement the responsibilities. Automated checks test predefined conditions, while agent reviewers assess the change and its evidence. Their findings need scrutiny too. A responsible human judges the goal, scope, and acceptable risk at the gate before building and decides whether the resulting change may be merged.

Compared to the original source material, this version generalizes three things:

1. **Triage first** - not every task deserves the full loop. Typos do not need a council.
2. **Parameterized verification** - test-first (red/green/refactor) is the default, but validation workflows and manual checks with expected results are first-class alternatives for data, infra, and prototype work.
3. **Work items are tracker-agnostic** - the input is plain Markdown, so it works with any issue tracker, or none at all. Keep it as files, as issue bodies on a board, or in any other medium.

## Repository layout

| Directory | Contents |
|---|---|
| `core/` | The portable heart: principles, the loop definition, handoff contracts (C0-C7), and role prompts. Deliberately free of any model, vendor, or platform name. |
| `adapters/` | How to run the loop on a specific platform: a coding-agent adapter, a manual procedure using separate chat windows, and example payloads for any OpenAI-compatible API endpoint (including local models). |
| `teaching/` | Lesson material in Dutch for software engineering students (HBO-ICT): lessons, exercises, and cases, built as a static site with Sphinx/MyST. |
| `docs/` | Sphinx build configuration for the teaching site. |

## Quickstart

**Use the loop on your own project (manual, any chat tool):** follow `adapters/manual/README.md`. You play the orchestrator: one fresh chat window per role, copy only the contract artifacts between them.

**Use the loop with a coding agent:** see `adapters/claude-code/README.md` for installable role definitions and an orchestrator command.

**Use the loop against a local or hosted OpenAI-compatible API:** see `adapters/openai-compatible/README.md` for per-role payload examples.

**Build the teaching site** (requires [uv](https://docs.astral.sh/uv/); dependencies live in the `docs` dependency group of `pyproject.toml` and are pinned in `uv.lock`):

```sh
make -C docs html
```

The Makefile runs `uv run sphinx-build` under the hood, so the environment is created and synced on first use.

The site is published automatically to GitHub Pages on every push to `main` (see `.github/workflows/docs.yml`). One-time repository setup: under *Settings -> Pages*, set the source to **GitHub Actions**.

## Scope and limits

The loop's sweet spot is small, medium, and large tasks. It is overkill for trivial fixes (that is what the Triage role is for) and not sufficient on its own for extra-large feature work, which needs to be split first. See `core/loop.md`.

## Credits

This repository builds directly on:

- Andrew "Watts" Watkins, [Context isolation in coding agent loops](https://depot.dev/blog/context-isolation-in-coding-agent-loops) (depot.dev, May 2026) - the article that describes the original loop and its rationale.
- The accompanying [gist with the original role prompts](https://gist.github.com/121watts/9b433d3e64c64cf6104f0c7f1775f376) - the basis for `core/roles/`, reused with gratitude per the author's invitation: "borrow the loop, steal the principle".
- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) (2025) - the finding that parallelization pays off only for genuinely independent subtasks, reflected in the parallel reviewers and sequential builder.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) for the entire repository; see [LICENSE](LICENSE) for the full text. Note that Creative Commons licenses are not designed for software, but this repository consists almost entirely of prose (prompts, contracts, lesson material); the few JSON payloads and config files are pragmatically covered by the same license.
