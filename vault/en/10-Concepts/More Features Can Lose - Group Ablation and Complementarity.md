---
title: More Features Can Lose - Group Ablation and Complementarity
tags:
  - ml/features
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/피처는-다-넣으면-진다-—-그룹-ablation과-상보성
created: 2026-08-04
sources: []
---

## Summary

Instead of cutting the top-N features by univariate ranking, choose feature sets by domain-group ablation — adding ALL features scored lower (val AUC 0.665) than a curated set (0.706). Complementarity beats individual strength.

## Details

- Context: a university assignment on NHIS sample-cohort health-insurance data (2,532 patients), predicting 2012 hospitalization. The model architecture was frozen; only data and features could change.
- Method: group ablation — start from a demographics baseline and add one domain group at a time to measure each group's marginal contribution, rather than ranking variables univariately and keeping the top N.
- Key result: demo+ALL (every feature) reached val AUC 0.665, lower than demo+util (utilization group only) at 0.706. Adding more features can actively hurt.
- Redundancy handling: utilization variables in the M_/D_ families carry overlapping information, so keep one representative per family.
- Keep complementary variables: domain features that rank low univariately but carry information no other group covers — past hospitalization history, the Charlson comorbidity index, special-case coverage — stay in.
- The Charlson index is a standard severity feature derived from ICD diagnosis codes, giving a compressed signal compared with raw code dummies.
- Lesson: the unit of feature selection is the group, not the variable, and the criterion is complementarity of the combination, not individual strength.

## Sources

- Related: [[The Train-Validation Metric Gap Signals Overfitting]]
