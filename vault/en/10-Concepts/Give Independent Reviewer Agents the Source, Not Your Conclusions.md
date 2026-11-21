---
title: Give Independent Reviewer Agents the Source, Not Your Conclusions
tags:
  - llm/agents
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/독립-검토-에이전트에게는-결론이-아니라-원문을-준다
created: 2026-11-21
sources: []
---

## Summary

Tests, coverage and mutants all encode the author's assumptions — **give a separate agent with a narrowed scope only the source material and the code, not your conclusions**, and it will find real defects even after every self-check passes. Then verify each finding against the source before applying it.

## Details

- Case 1: after a large rewrite, a review commissioned "so my own judgment doesn't anchor it" found that a read error on the input was treated as end-of-file — so a truncated file could still report "decrypted == original: YES". The author had wrongly assumed the comparison step would catch it. An earlier review had already surfaced global mutable state that contradicted the design write-up, and tests that could never fail.
- Case 2: reviews ran in parallel with split scopes — (textbook conformance + arbitrary-input defects) / (test quality) / (report vs. code). They produced one more textbook misprint, 12 test gaps and one wrong number in the report.
- Confirm structural feedback by measuring: told that the generalized MixColumns did not match the pseudocode's shape, rewriting it as the textbook's four equations raised encryption from 21.5 to 63.8 MB/s and decryption from 6.4 to 38.0 MB/s.
- De-biased briefs: to verify a table transcription, the reviewer was asked to "transcribe it again" without being given the expected values, and the two readings were diffed mechanically (two S-boxes, 512 cells, all identical). Hand over your conclusion and all you get back is confirmation.
- Give reviewers their own isolated build tooling so they never touch the working tree; while reviews run, the main session does non-overlapping work such as report tooling.
- Re-check findings against the source and the code: of six findings, only one real defect plus some wording and comment fixes were applied; two were rejected with reasons. A claimed textbook error was accepted only after opening the original slide.
- State truthfully who reviewed: a report draft saying "handed to another reviewer" was corrected to "reviewed by a sub-agent of an AI coding tool" — it must not read as if a person did the review.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Split Web Research Into Verifier and Discovery Agents]], [[Coverage Proves Execution, Mutation Proves Checking]], [[A Validation Reference Must Come From a Source Independent of What It Checks]]
