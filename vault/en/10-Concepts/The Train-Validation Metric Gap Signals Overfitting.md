---
title: The Train-Validation Metric Gap Signals Overfitting
tags:
  - ml/overfitting
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/train-val-지표-갭이-과적합의-신호다
created: 2026-08-04
sources: []
---

## Summary

The gap between train and validation AUC is the first diagnostic for overfitting — the baseline sat at train 0.83 vs val 0.57 (gap 0.257), essentially memorization, and a near-random val score means the fix is features and data, not the model.

## Details

- Context: NHIS hospitalization prediction (2,532 patients, model architecture frozen). The baseline scored train AUC 0.83, val AUC 0.57 — a gap of 0.257.
- Val AUC 0.57 is close to random (0.5): the model had memorized the training data while learning almost no generalizable signal.
- The prescription for this pattern (high train + near-random val) is better inputs, not model tuning — and indeed the problem was solved by enriching features while keeping the architecture fixed.
- After feature enrichment the gap shrank to 0.064, and final val AUC rose from 0.57 to 0.70.
- A falling train score during improvement is not regression — it means less memorization. Val rising while train falls is the right direction.
- Working habit: log three numbers per experiment — (train, val, gap) — not just val, so you can tell whether an improvement is better generalization or just stronger memorization.

## Sources

- Related: [[More Features Can Lose - Group Ablation and Complementarity]]
