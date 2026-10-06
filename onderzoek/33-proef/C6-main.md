**C6 — W1: SHIP**

- **Reviewer and assignment:** Independent strict reviewer; S1–S4.
- **Mode and artifact:** INITIAL; commit `3be0eaf3a734c1cb7094c3c137da9692700d976a`, compared with base `99158040251d49e0cc186ce5625d518b469fcf56`.
- **Norms and decisions:** Applied the installed strict role, loop and C5/C6 contracts, pinned PROJECT.md, and supplied C4 PROCEED. Read process sources match the installation manifest for `a9864c8a0b8cc0acab38d31d47a4582e0886966f`; that source commit is unavailable in local Git.

All coverage is **newly examined**:

| Criterion | Result | Evidence |
|---|---|---|
| S1 | Pass | Line 27 preserves default insertion order and returns a fresh list; supplied test passes. |
| S2 | Pass | Lines 25–26 filter with `uitgeleend_aan is None`, preserving order; supplied test passes. |
| S3 | Pass | Empty and entirely loaned collections return `[]`; supplied test passes. |
| S4 | Pass | Comprehension returns existing objects without state assignments; supplied test passes. |

No criteria are assigned elsewhere. Only `boekenplank.py` changed; the signature remains positional-compatible.

**Verification:** `python3 -B controleer.py werk volledig` independently produced four passes, exit 0. Both tested files match the reviewed commit byte-for-byte and match C5’s SHA-256 values. `controleer.py` also matches the base. Historical red evidence remains supplied evidence, not independently rerun.

- **Contract drift:** `<none>`
- **Must fix / Should fix / Nice to have:** `<none>`
- **Repair outcome:** `<none>` — initial review.
- **Next action:** Human merge decision.

No files were written; no Git/tracker mutation or merge occurred.