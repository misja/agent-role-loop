**C6 REPAIR — SHIP**

- **Reviewer and assignment:** Independent strict reviewer in this fresh invocation; sole owner of S1–S4. No criteria assigned elsewhere.
- **Mode and artifact:** Repair review of `328555e0e4ebec7e5bae82d23634b8e6a57be240`, against before-commit `49f810f3fe1ecdd9bc89e5f763c7a7cefbf6c4b7`. Input: `work-items/NEG/C5-repair-core.md`, including its explicit repair appendix. No author history or main-review judgments consulted.
- **Norm basis:** Role Loop `a9864c8a0b8cc0acab38d31d47a4582e0886966f`; installed entry, core loop, strict role, C5 and C6 hashes match the installation manifest. This verifies installed bytes, not a local Git lookup of the source commit. PROJECT norm `99158040251d49e0cc186ce5625d518b469fcf56` was read from Git and matches the working file. Applied the C4 authorization recorded in C5 for concrete plan `6017597771`.

| Criterion | Result | Newly examined evidence |
|---|---|---|
| S1 | Pass | Line 27 returns all stored books in insertion order; default-list test passes. Later default listing is also exercised by S4. |
| S2 | Pass | Line 26 selects only books whose loan is `None`, preserving order; supplied test passes. |
| S3 | Pass | Selection returns `[]` for empty and fully loaned collections; both supplied cases pass. |
| S4 | Pass | Line 26 returns a fresh selection without assigning storage or changing book fields; before/after state test passes. |

**Verification:** HEAD equals the repaired commit. `boekenplank.py` and `controleer.py` match that commit. The exact before/after diff contains only the declared one-line product repair.

Executed independently:

```text
python3 -B controleer.py werk volledig
4 tests passed; exit 0
```

- **Contract drift:** None. Optional parameter, default behavior and supplied tests remain unchanged.
- **Must fix / Should fix / Nice to have:** None.
- **Repair outcome:** Prior B1[S4] resolved. Filtering no longer removes loaned books from storage; dependent later default listings retain the original collection and loan values. All S1–S4 were re-examined. Appendix evidence about earlier S1–S3 passes and the negative run is **previously established**, not newly reproduced here.
- **Limits:** Evidence establishes the supplied criteria; no independent object-identity, deep-copy, student or production validation.
- **Persistent state:** As supplied in the appendix, design `0`, delivery `1` consumed before repair. No automatic round remains; counters were not changed.
- **Next action:** Human merge decision. No mutation or merge performed.