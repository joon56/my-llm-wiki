---
title: A Leaderboard Submission Is a Pre-Registered Experiment
tags:
  - ml/evaluation
  - ml/competition
status: distilled
publish: true
lang: en
translation: 10-Concepts/리더보드-제출은-사전등록된-실험이다
created: 2026-10-05
sources: []
---

## Summary

Before submitting to a competition, write down and commit **the expected score band, a falsifiable core claim, and the next action for each result range (a reading table)** — only then does a noisy leaderboard result become information instead of post-hoc rationalization.

## Details

- Practice: for every submission, record in `SCORES.md` (a) the local score, (b) the expected leaderboard band, (c) which sub-scores should move and which **must not**, and (d) the next action per result range — commit, then submit.
- It becomes gradable: when the result lands, score it against the prediction ("3.5 of 4 predictions hit"). As hits accumulate, patterns like "conditioning gains on real data are 3-5x the local gain" graduate from guesses to established facts.
- It catches misfires: if you wrote "this change must not touch scores A and B", any movement there reads instantly as a bug signal.
- It resists noise: with a noisy leaderboard (Laplace noise, 0.01 rounding), any post-hoc story can be justified. A pre-set band makes the call mechanical: "inside the band = flat".
- Flat is information: if you wrote "if flat, close this axis" in advance, a non-improving submission is not a failure but a measurement that closes an axis.
- Pairs with a local adoption bar: only submit what cleared a pre-set local threshold (e.g. +0.005). Submissions verify; they do not explore.
- Carry the reading criteria verbatim into the final decision rules. A pre-registered rule — "drop a component whose standalone reading is below the existing standalone model" — went missing from the next day's list of final-edit rules, and a component that read 3 cells lower on two sub-scores nearly stayed in the final submission under an "otherwise unchanged" rule. When reading results, check them against the original registration text.
- The scarcer the slots, the more information each submission should carry. Changes aimed at separately scored sub-scores can share one submission, giving 2-3x the tests per slot, and the untouched sub-scores of same-day submissions serve as each other's controls. When few slots remain, replace diagnosis-only submissions with ones that get adopted if they win and still diagnose if they lose.
- Write the submission ledger at upload time: submission ID, file, hypothesis under test. This matters most when the daily limit is shared with another agent — afterwards, leaderboard entries could not be attributed to files, and the improved version's score never made it into the final report.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Switch Components Off on Purpose to Map Real-Data Loss]], [[Measure the Oracle Ceiling Before Implementing]]
