# C5 core NEG: REPAIR review
Artifact repaired commit 328555e0e4ebec7e5bae82d23634b8e6a57be240; before49f810f3fe1ecdd9bc89e5f763c7a7cefbf6c4b7, original good basis3be0eaf3a734c1cb7094c3c137da9692700d976a. Product boekenplank.py only; controleer.py unmodified, worktree matches repaired commit.
Normbasis a9864c8a0b8cc0acab38d31d47a4582e0886966f; installed .codex/role-loop/core/loop.md, roles/reviewer-strict.md and C5/C6 contracts. Project norm PROJECT.md at99158040251d49e0cc186ce5625d518b469fcf56. Core source commit is not in this temporary Git history; installed source hashes and Codex orchestration byte check establish pinned origin, do not claim local git lookup succeeded.
Human C4 https://github.com/misja/agent-role-loop/issues/33#issuecomment-6017668277 on exact concrete plan6017597771; labeled negative+bounded repair expressly authorized. Same approved interface/invariants/-B/tests retained. No changed goal/scope/norm/risk or merge approval.
One strict reviewer owns all S1–S4; no C3/C7. S1 default all books ordered line27; S2 True only loan None ordered line26; S3 empty/all-loaned returns[] line26; S4 filtering retains storage/loans line26. Recheck dependencies involving later default calls and storage.
Diff summary:
- Filter now returns a fresh selection instead of assigning storage.
- Signature/default branch/tests retained; no other product file changed.
Changed files: boekenplank.py line26. Contracts touched: S4 restored; approved optional parameter unchanged. No storage/CLI/dependencies/test mutation. Deviations none; #58 owns additional regression criteria outside scope.
Actual builder command python3 -B controleer.py werk volledig before3pass/S4fail exit1, after4pass exit0. Codex saved this exact repaired SHA and independently reran same command after commit:4pass exit0. Evidence supports supplied criteria; no object-identity/deep-copy/student/production proof.
CLI0.160.0 model explicitly gpt-6.1-sol, new read-only invocation, approval never, ephemeral no resume/fork. Read-only Git inspection IS allowed (show/diff/status/rev-parse), no Git mutation or tracker/merge. Confirm code/tests correspond to this commit before testing.
Persistent NEG state: design0 delivery1 consumed BEFORE repair, work-items/NEG/repair-state.json. No further automatic round. Main W1/#33 counters unaffected.

## Explicit REPAIR appendix
Prior BLOCK source work-items/NEG/C6-initial.md, initial commit49f810f3fe1ecdd9bc89e5f763c7a7cefbf6c4b7. Prior B1[S4]: assigning filtered selection back to self._boeken loses loaned books, corrupts subsequent default listing. Required new selection returned without modifying stored collection/book loan state and full supplied suite green.
Previously established unaffected coverage: S1–3 initial pass from code inspection and own negative suite; S1 applies only before destructive filter and depends on B1. Recheck all four because storage dependencies matter; label any reused evidence as previously established. Prior reviewer did not independently verify Git correspondence because task wording was interpreted as all Git prohibited; root Codex saved exact fixture/worktree and testoutput. This new repair review explicitly permits read-only Git checks.
Before/after diff (root-confirmed exact revisions):
```diff
diff --git a/boekenplank.py b/boekenplank.py
index 2cbeb42..f1fe8cd 100644
--- a/boekenplank.py
+++ b/boekenplank.py
@@ -23,5 +23,5 @@ class Boekenplank:
 
     def lijst(self, alleen_beschikbaar=False):
         if alleen_beschikbaar:
-            self._boeken = [b for b in self._boeken if b.uitgeleend_aan is None]
+            return [b for b in self._boeken if b.uitgeleend_aan is None]
         return list(self._boeken)
```
No scope/shared dependency change. No author history or main-review verdict. Complete C6 REPAIR, disposition of B1/dependencies, tested commit/results/limits; no mutation or merge.
