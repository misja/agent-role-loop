# Role Loop entry for Codex

This directory is ordinary project content, not native Codex agent configuration.
The routing authority is [core/loop.md](core/loop.md). Use the role and contract
sources there without rewriting them here. The human orchestrates the CLI route.

For each task, name its role source, contract inputs, applicable norm versions,
readable project rules and expected output. Use a fresh Codex invocation for an
initial reviewer and for a repair reviewer; do not resume or fork an earlier
reviewer. Initial input is C5 core plus assigned criteria and norms. In repair
mode the explicit appendix includes before/after diff, prior blockers, previous
unaffected coverage and persisted repair counters as core requires.

Keep project instructions neutral: no author transcript or unrelated verdicts.
A fresh conversation still loads instruction files and may read accessible
files. The role prompt is not an operating-system access control. Use explicit
sandbox permissions for the phase. Claude settings do not grant Codex rights.
The human saves contract output, product commits and tracker feedback, and
provides the actual human decisions; do not invent them or merge autonomously.
