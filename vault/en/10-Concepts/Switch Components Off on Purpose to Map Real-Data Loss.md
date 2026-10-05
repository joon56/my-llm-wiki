---
title: Switch Components Off on Purpose to Map Real-Data Loss
tags:
  - ml/evaluation
  - ml/competition
status: distilled
publish: true
lang: en
translation: 10-Concepts/성분을-일부러-꺼서-실데이터-손실-지도를-얻는다
created: 2026-10-05
sources: []
---

## Summary

When your local validation cannot see the structure of the real data, submit a **probe that deliberately disables one component** of your best model (e.g. replace one item group's outputs with uniform vectors) — the score drop lets you back out what that component earns on real data.

## Details

- Situation: the local sandbox had random answers, so it could not show where loss came from on real data. Every lever measurable locally came back null — no material left to form the next hypothesis.
- Method: take the best model, swap only one subset's outputs (e.g. 156 gated items) for uniform vectors, and submit. Give up the ranking (the leaderboard keeps your best). If the subset's cell share and the uniform vector's own baseline score are known exactly from the schema, the drop yields **the per-cell skill of that subset** by arithmetic.
- Actual reading: on the other datasets gated cells were twice as easy as content cells, but on one dataset both had the same skill — the gate structure was leaking on real data. It also explained why a string of local experiments had been null: they were digging on the wrong axis.
- Rule 1: write the reading table (result range -> meaning -> next action) before submitting.
- Rule 2: if only the total is visible (sub-scores hidden when the best is not beaten), apply the probe to a single sub-score so that delta-total = delta-sub-score / count. Design the drop to be well above the rounding resolution.
- Rule 3: read only model-component contributions. Never build a probe that reveals data statistics (e.g. answer distributions) — that is a rules risk.
- Caution: creating a second account to get finer readings very likely violates one-person-one-account rules.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[More Features Can Lose - Group Ablation and Complementarity]]
