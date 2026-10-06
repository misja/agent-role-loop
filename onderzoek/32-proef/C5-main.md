# C5 core W1: initial review
Reviewable commit: fbab9c207dd1e08cef8d9566d49169c8c056895d
Basis: 33f88927165475fc2e6f8c513ef6f76741569969. Product: boekenplank.py only.
Normbasis core: b7aad138c18809c747a1e020590e0ad905903514; installed core/loop.md, core/contracts and core/roles are byte-identical readable sources. Project norm: PROJECT.md at basis commit.
Route PLANNED, one strict independent reviewer assigned all criteria below; no C3/C7. Design 0, delivery 0 consumed.
Human C4: work-items/W1/C4.md, actual akkoord on concrete C2 and V1–V4, https://github.com/misja/agent-role-loop/issues/32#issuecomment-6016426784. Approved: retain controleer.py; python3 -B avoids cache; ordinary optional parameter; derived AC5/6. No merge approval.
Criteria: S1 default returns all books in insertion order; S2 True returns only loan None in insertion order; S3 empty/all-loaned returns []; S4 filtering preserves collection and loan status; AC5 explicit False equals default; AC6 returned list containers are independent from stored collection. Same strict reviewer owns all six.
Change: optional alleen_beschikbaar=False; True returns a fresh filtered list, default retains original fresh-list behavior. No other product change.
Verification: builder observed initial full suite 1 pass/3 TypeError errors, exit1; after change 4 pass exit0. Extra AC5/6 checks initially TypeError, afterward M1 True / M2 True True exit0. Codex independently reran both approved commands on this commit content: same green outputs. Commands: python3 -B controleer.py werk volledig; python3 -B controleer_extra.py. Extra check is orchestration support implementing approved M1/M2, not a new human instruction. Supplied controleer.py unchanged. Python 3.14.8.
Limits: Claude parent combined shell commands were denied; individual builder tests ran. No production or student validation. Untracked work-items and controleer_extra.py are evidence/support, not product changes. Read exact commit using git show; do not read author transcripts or other judgments.
Requested C6: independent initial review all six criteria with objective evidence and limits; no mutation or merge.
