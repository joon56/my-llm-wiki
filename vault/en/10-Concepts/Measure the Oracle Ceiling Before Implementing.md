---
title: Measure the Oracle Ceiling Before Implementing
tags:
  - ml/evaluation
  - ml/training
status: distilled
publish: true
lang: en
translation: 10-Concepts/구현-전에-oracle-천장부터-측정한다
created: 2026-10-05
sources: []
---

## Summary

Before building a new lever, measure **the gain you would get if the estimator were perfect (the ceiling)** with an oracle setup or an analytic calculation — if the ceiling is below the adoption bar, no estimator can pass, so skip the implementation.

## Details

- Case 1 (learned after building): partial matching on adjacent levels of a match key. Estimator v1 +0.0011, v2 +0.0013. Even the ceiling with forced optimal weights was +0.0025, below the +0.005 bar. The axis itself had a low cap — this experience became the rule.
- Case 2 (skipped by calculation): mixing in a per-country prior. With n of about 1-2k per cell, a pseudo-count W moves estimates only by W/(n+W), so the expected gain is about zero. Parked with zero lines of code.
- Case 3 (skipped by a probe): seed bagging. Score variance across 3 seeds was 0.0003 — averaging could not buy anything, confirmed before implementing.
- Procedure: hypothesis -> ceiling measurement (oracle setup or analytic calculation) -> implement an estimator only if ceiling >= bar -> local validation.
- The ceiling bounds the axis, not just this estimator: it proves that swapping estimators will not help, so you close the axis and move to the next hypothesis.
- Record the nulls: keep rejected experiments' assertions as strict xfail tests so nobody digs the same axis again.
- Case 4 (the measurement's own ceiling): in a sensor-based walking study, the decision rule was "at least 80% of steps within ±3% of the beat." Before the main runs, a "perfect sync" recording walked to a metronome showed mean cadence within 0.2% of the beat, yet only 47-50% of steps inside ±3% — step-interval variability alone (CV 5.2-5.7%) puts the bar out of reach (under a normal approximation, 80% inside ±3% needs a CV of 2.3% or less, decidable with zero code). The rule stayed as registered; an auxiliary criterion and a "measurement limit" note were added before any results were seen.
- Measure the floor too: a criterion that holds even with zero effect cannot discriminate. A comparison like "agreement is higher in the near-tempo condition than in the far one" held almost automatically even if steps did not change at all, and a metric that is zero by definition was still computed but reported as a "structural zero".
- Measure the ceiling as the residual after what the incumbent already absorbs. Even a candidate that looks like an official hint (new wording in the organizer's schema description) starts with whether the metric can see the change at all — when only per-cell probabilities are scored, fixing the parent-question structure barely moves the per-cell estimates. The defect was real, but the incumbent's soft path had already absorbed most of it, so the residual effect was far below the leaderboard resolution ([[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]]), and all three probes read unchanged.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Swapping the Model Class Beats Adding Knobs]], [[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]]
