# C5 core NEG: REPAIR review
Artifact: repaired commit e96df75c919981123fa8728a6238afb87d91e823; before 2b24d15d00b34e43b1b2020675d6bffd9c0e82fa; original good basis fbab9c207dd1e08cef8d9566d49169c8c056895d. Product boekenplank.py only. Worktree product/test match commit; tests unmodified.
Normbasis core b7aad138c18809c747a1e020590e0ad905903514, readable .claude/agent-role-loop/core/loop.md, roles/reviewer-strict.md, contracts/review-handoff.md and reviewer-verdict.md. Project norm PROJECT.md at 33f88927165475fc2e6f8c513ef6f76741569969.
Scope/human decisions: labeled negative fixture authorized by outer C4 https://github.com/misja/agent-role-loop/issues/32#issuecomment-6001713335; approved interface/invariants and -B command in exercise C4 https://github.com/misja/agent-role-loop/issues/32#issuecomment-6016426784. No merge approval. No changed scope or new goal. One strict reviewer owns S1–S4; AC5/6 supplementary builder checks only.
Diff summary:
- Filter returns a fresh selection rather than assigning self._boeken.
- Standard return and signature unchanged; stored collection/loan status preserved.
Changed files: boekenplank.py line26. Contracts touched: lijst optional parameter unchanged, S4 invariant restored. No CLI/storage/dependencies. Deviations none; follow-up optional id-regression test outside scope.
Coverage/assignment: strict reviewer S1 line27 all books insertion order; S2 line26 True loan None ordered; S3 line26 empty/all-loaned selection[]; S4 line26 no storage/loan mutation. Inspect dependent default behavior and numbering after filtering. Do not claim deep-copy identity tests.
Objective evidence: actual builder full suite before 3pass/S4fail exit1, after4pass exit0; extra M1 True/M2 assert fails before exit1, afterward M1 True/M2 True True exit0. Codex ran both separate commands again AFTER saving this exact commit: same green. python3 -B controleer.py werk volledig; python3 -B controleer_extra.py. These EXACT commands are allowed; no suffix/chaining or command variant required. Python3.14.8 measured earlier by Codex. Builder Git inspection and Python version commands denied; Codex verified actual diff/commit. No student/production validation. Raw builder transcript excluded.
Persistent repair state: work-items/NEG/repair-state.json, design0 delivery1 consumed BEFORE repair. No additional automatic round remains.

## Explicit C6 REPAIR appendix
Prior verdict source: work-items/NEG/C6-initial.md, BLOCK on before commit 2b24d15d00b34e43b1b2020675d6bffd9c0e82fa. This prior verdict is provided only under REPAIR mode; do not read author history or main W1 judgments.
Blocker1 [S4]: assigning filtered selection to self._boeken loses loaned books, makes future default list incomplete, risks duplicate numbering. Required return new list without storage mutation.
Blocker2 [S1–S4 proof]: weak suite excludes S4; require full-suite green on exact repaired commit.
Previously established initial coverage: S1 pass only in isolated use with S4-dependent caveat; S2/S3 static pass with C5 test evidence. Initial reviewer could not execute tests because it chose a nonallowed command without -B. No prior reviewer-runtime green claimed. Recheck all S1–4 on repaired code due storage dependencies; label reused initial evidence if any, do not call reused evidence newly examined.
Repair diff before->after:
```diff
-            self._boeken = [b for b in self._boeken if b.uitgeleend_aan is None]
+            return [b for b in self._boeken if b.uitgeleend_aan is None]
```
Exact diff available using git diff 2b24d15d00b34e43b1b2020675d6bffd9c0e82fa e96df75c919981123fa8728a6238afb87d91e823 -- boekenplank.py. No shared dependency/scope change. Requested complete C6 REPAIR outcome for both blockers and their dependencies, remaining limitations; no writes, resume or merge.
