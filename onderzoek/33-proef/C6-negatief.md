**C6 — Independent strict review**

- **Reviewer and assignment:** strict reviewer; sole owner of S1–S4. No criteria assigned elsewhere.
- **Mode and artifact:** INITIAL; designated commit `49f810f3fe1ecdd9bc89e5f763c7a7cefbf6c4b7`, base `3be0eaf3a734c1cb7094c3c137da9692700d976a`. Inspected the product files identified by C5 as matching that commit; commit correspondence was not independently verified because Git was prohibited.
- **Norm basis:** Role Loop `a9864c8a0b8cc0acab38d31d47a4582e0886966f`; PROJECT.md `99158040251d49e0cc186ce5625d518b469fcf56`, as pinned by C5. Read the required entry, loop, strict role, C5/C6 contracts, PROJECT.md, and designated W1 decision/design sources. Applied C5’s recorded authorization for the negative fixture and one bounded repair; no merge authorization.
- **Decision:** **BLOCK**.

All coverage below was **newly examined**.

| Criterion | Result | Evidence |
|---|---|---|
| S1: default lists all books in insertion order | pass | Line 27 returns the stored sequence as a list; supplied S1 test passes on an unfiltered collection. Subsequent listing corruption is covered by S4. |
| S2: True selects only loans equal to `None`, preserving order | pass | Line 26 uses `is None` and preserves iteration order; S2 test passes with book numbers `[1, 3]`. |
| S3: empty/all-loaned returns `[]` | pass | Comprehension produces an empty list in both cases; S3 test passes. |
| S4: filtering preserves storage and loan fields | **fail** | Line 26 replaces `self._boeken` with the filtered selection. S4 demonstrates disappearance of `(2, 'Atlas', 'Noor')` from subsequent default listing. |

**Objective verification:** ran `python3 -B controleer.py werk volledig`: four tests executed, S1–S3 passed, S4 failed, exit **1**. Inspected the supplied checks and product code. No independent before-revision run, identity/deep-copy proof, or student/production validation was established.

**Contract drift:** `<none>` undeclared. C5 explicitly declares the S4 invariant violation and its effect on subsequent default listing.

**Must fix — B1 (S4):** At [boekenplank.py:26](/tmp/arl33-smoke-3j2v4v41/boekenplank.py:26), calling `lijst(alleen_beschikbaar=True)` on a collection containing loaned books removes those books from stored state. The supplied regression at [controleer.py:43](/tmp/arl33-smoke-3j2v4v41/controleer.py:43) reproduces this loss. Required outcome: return the filtered selection while preserving the stored collection and all book/loan values; the full supplied suite must pass.

- **Should fix:** `<none>`.
- **Nice to have:** `<none>`.
- **Repair outcome:** `<none>`; initial review.
- **Next action:** the human orchestrator may initiate the recorded single bounded delivery repair, with counters persisted and a fresh repair review afterward. No mutation, repair, Git, tracker, or merge action was performed.