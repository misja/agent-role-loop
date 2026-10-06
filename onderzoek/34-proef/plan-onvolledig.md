# C2 W1

**Contract**: Plan for W1 implementation of `alleen_beschikbaar` parameter in `lijst()`.

**Process**: PLANNED S route per C1. Human-supervised Vibe planner/builder. Norm/core 04c087cee43ef074f1e132686688cbf01014f2ce byte-identical. Project norm PROJECT.md at basis a201bb630740c5597a8c5e0c408f75b6b99265d6. Design0 delivery0 counters. No shell/task/connectors/Git; human tests and merge.

**Inputs**:
- C0: S1 default all books insertion order; S2 True only `uitgeleend_aan is None` same order; S3 empty/all-loaned returns `[]`; S4 filtering retains stored books and loan status
- C1: Planner/reviewer read_file+grep only; builder adds write_file+edit; S1-S4 to one fresh strict reviewer
- approved-design.md: Signature `def lijst(self, alleen_beschikbaar=False)`; True returns `[b for b in self._boeken if b.uitgeleend_aan is None]`; otherwise retain `return list(self._boeken)`; no other code/test/dependency change
- C4-source: Human PROCEED on #34 C2v1; https://github.com/misja/agent-role-loop/issues/34#issuecomment-6024662487 (plan) and #issuecomment-6024762858 (C4). Applies only to same concrete exercise choices, no merge approval.

**Implementation**:
```python
def lijst(self, alleen_beschikbaar=False):
    if alleen_beschikbaar:
        return [b for b in self._boeken if b.uitgeleend_aan is None]
    return list(self._boeken)
```

**Scope**: Modify `boekenplank.py` line 24-25 only. No changes to `controleer.py`, storage, CLI, dependencies, sorting or keyword-only interface.

**Preservation**: Insertion order preserved via `list(self._boeken)`; book loan status retained as comprehension does not mutate `self._boeken`.

**Reviewer Assignment**: S1-S4 assigned to one fresh strict reviewer per approved-design.md; #58 owns extra regressions.

**Verification**:
- Method: `test-first` via existing `controleer.py`
- Command: `python3 -B controleer.py werk volledig` (human-executed)
- Before: 1 pass, 3 TypeError, exit 1 (source: approved-design.md)
- After: 4 pass (S1-S4), exit 0 (source: approved-design.md)

**Comparison with Approved Design**: Implementation matches approved-design.md exactly. Signature, logic, and constraints are identical. No new S5/6, interface, scope, or risk changes introduced.

**Acceptance Criteria Met**:
- S1: `list(self._boeken)` returns books in insertion order `[1, 2, 3]`
- S2: Comprehension returns `[1, 3]` for `alleen_beschikbaar=True` (filtering book 2 loaned to Noor)
- S3: Empty list and all-loaned cases return `[]`
- S4: `self._boeken` unchanged after filtering call

**Sources**: All inputs, code, and test files read from `/tmp/arl34-smoke-0c2dckc3/`. Tests are human-executed; sources stated, not run.
