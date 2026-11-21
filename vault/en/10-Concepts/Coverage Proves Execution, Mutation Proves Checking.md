---
title: Coverage Proves Execution, Mutation Proves Checking
tags:
  - dev/testing
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/커버리지는-실행을,-돌연변이는-검사를-증명한다
created: 2026-11-21
sources: []
---

## Summary

100% line coverage only means the code **ran**, not that it was **checked** — judge tests by **mutation detection** (plant one defect at a time and see whether a test fails), and when you shrink a test suite, hold both coverage and the number of detected mutants invariant.

## Details

- Case: with 120 tests, 100% line coverage (1,043/1,043), 98.7% branch coverage and 14/14 mutants detected, an independent review still found five tests that could never fail. In the next assignment it found a test that never called the function its name promised and a test that still passed with a defect planted.
- Method: a pattern-substitution script injects one defect into the implementation at a time, rebuilds, and confirms that a test fails. Make sure each pattern hits only the intended line — the same digit sequence appeared in another table, so one mutant had been changing the wrong place.
- The mutant set is also a sample: when a review exposes a weakness, add mutants that target it (14 → 23, and 38 → 52 in the next assignment). When you add a new assertion, first run a mutant that only that assertion can catch, to prove it actually detects something.
- Shrink tests with both numbers held fixed: first measure which subset preserves them — 32 tests alone kept functions 46/46, lines 100%, branches 98.95% and mutants 23/23. Cutting 109 tests (2,551 lines) to 60 (1,430 lines) then left every number unchanged.
- Do not contort tests to cover unreachable defensive branches (for example a "mismatch" message that only runs if the implementation is wrong) by adding injection points. Show with mutants that the verdict code works, and document why the branch stays unexecuted.
- Mutants also expose bugs in the test code: one planted defect crashed the test runner through a comparison that skipped a length check. Re-measuring after a refactor surfaced two untested paths in moved code and a fault-injection test that missed an "ignore a failed file close" defect.
- Order of work: coverage finds code that never ran → mutation finds code that ran but nobody checked → whatever branches remain unexecuted get a written reason.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Switch Components Off on Purpose to Map Real-Data Loss]], [[Give Independent Reviewer Agents the Source, Not Your Conclusions]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]]
