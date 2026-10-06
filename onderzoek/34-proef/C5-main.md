# C5 W1 core — initial independent review
Artifact: W1, base a201bb630740c5597a8c5e0c408f75b6b99265d6, exact product d3f1125760d441a6d8624c4b7c47b9185b7a8e43. Human Git lookup saved exact committed boekenplank.py as work-items/W1/product-snapshot.py, bytes checked against current file. Reviewer has no Git tool; compare snapshots, don't claim independent Git execution.
Process/core norm 04c087cee43ef074f1e132686688cbf01014f2ce, readable .vibe/role-loop/core/loop.md, roles/reviewer-strict.md, contracts/review-handoff.md and reviewer-verdict.md in installed core. Project norm PROJECT.md at base above; readable current PROJECT.md unchanged.
Scope/decision: approved optional signature def lijst(self, alleen_beschikbaar=False), True returns fresh filtered comprehension, otherwise existing list(self._boeken). Human C4 https://github.com/misja/agent-role-loop/issues/34#issuecomment-6024762858 applies to concrete plan https://github.com/misja/agent-role-loop/issues/34#issuecomment-6024662487. Exact choices compared before build, no changed scope/norm/risk. Human merge not granted.
Diff summary: optional parameter; fresh filtered list; unchanged default copy. Changed file: boekenplank.py only. API extension as approved; no test/core/storage/dependency change.
Criteria/assignment all newly examined by this fresh strict reviewer: S1 default returns all books in insertion order; S2 True only uitgeleend_aan is None in order; S3 empty/all-loaned returns []; S4 filtering preserves stored books and loan status. Actual supplied suite readable controleer.py, SHA256 9c0e40321699cc0217ddc80ecbf9136b152dea23b5c63733c4d0998aee6adc6b, unchanged from base; identity/deep-copy/add-after-filter regressions not established (#58 separate).
Evidence: human test-red.txt on base before edits:1pass+3TypeErrors exit1. Human test-green.txt after Vibe edit, on exact committed bytes:4pass exit0. Reviewer may inspect code/tests and this actual output, but cannot execute shell/tests. No proposed command counts as observed test. Product diff source git diff base product -- boekenplank.py:
```diff
diff --git a/boekenplank.py b/boekenplank.py
index 2d95184..f1fe8cd 100644
--- a/boekenplank.py
+++ b/boekenplank.py
@@ -21,5 +21,7 @@ class Boekenplank:
         self._boeken.append(boek)
         return boek
 
-    def lijst(self):
+    def lijst(self, alleen_beschikbaar=False):
+        if alleen_beschikbaar:
+            return [b for b in self._boeken if b.uitgeleend_aan is None]
         return list(self._boeken)
```
Deviations: installed text replacement tool name edit instead of search_replace, same approved action; planner called verification manual because model lacks shell, actual human test-first red/green retained. Followups: #58 extra regressions; immutable weights behind latest not available; no student observations. Repair state W1 design0 delivery0; no prior verdict. Only this C5 core, named snapshots/test output/current code/tests/projectnorm/core needed; no C2/maker logs/other opinions. Complete C6, state limits.
