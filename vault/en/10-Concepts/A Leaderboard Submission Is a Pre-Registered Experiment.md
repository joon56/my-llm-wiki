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

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Switch Components Off on Purpose to Map Real-Data Loss]], [[Measure the Oracle Ceiling Before Implementing]]
