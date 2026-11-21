---
title: Effects Smaller Than the Leaderboard Resolution Cannot Be Read
tags:
  - ml/evaluation
  - ml/competition
status: distilled
publish: true
lang: en
translation: 10-Concepts/리더보드-눈금보다-작은-효과는-제출해도-읽히지-않는다
created: 2026-11-21
sources: []
---

## Summary

A leaderboard with noise and rounding **cannot read effects smaller than its display step, and when the baseline sits on a rounding boundary even identical code lands in different bins** — compute (expected effect ÷ step) before spending a slot, and measure the noise floor first with an identical-code resubmission (an A/A test).

## Details

- The cost: in a survey prediction competition, candidates whose expected local effect was 1/40 to 1/500 of the display step (0.01) kept being submitted. Over seven weeks, 11 submissions gave 9 ties, 2 drops, and 0 gains, and the 24 sprint uploads that followed added zero readable gains — "unreadable" was settled before any of them went in.
- The surprise: a submission that changed only sub-score A dropped the untouched sub-score B by one bin, even though locally the 130k+ outputs on B's path were bit-identical to the baseline. B's true value sat just above a rounding boundary (closer than half the noise standard deviation), so noise alone put it in the lower bin about one or two times in five.
- Diagnosis: count past readings of identical or equivalent code to locate the true value (13 upper-bin vs 3 lower-bin readings out of 16 → near the boundary). Resubmitting the untouched original the next day (A/A) brought it back to the upper bin and confirmed the previous day's "drop" as noise.
- Fix the reading table: a pre-registered rule such as "one bin down = adverse" misfires on a baseline that straddles a boundary. If a same-day identical-code control dropped too, withhold judgment.
- Same principle locally: the official scorer's local printout also carried noise, so the same prediction vectors printed different values. Compare bit identity of the raw prediction vectors and the exact pre-noise log score, not displayed numbers.
- Decision rule: spend reading slots only on big swings aimed at one full step or more (e.g. a model-class swap), and do not try to verify sub-step candidates on the leaderboard.
- Scoring asymmetry: if the final phase is scored exactly, with no noise or rounding, sub-step gains still count toward the ranking. Filter such gains with validation inside the submission and stack them only into the final package.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Measure the Oracle Ceiling Before Implementing]], [[Select Improvements the Leaderboard Cannot Read With an In-Submission Holdout]]
