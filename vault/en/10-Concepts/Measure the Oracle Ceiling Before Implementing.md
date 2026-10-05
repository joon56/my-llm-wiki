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

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Swapping the Model Class Beats Adding Knobs]]
