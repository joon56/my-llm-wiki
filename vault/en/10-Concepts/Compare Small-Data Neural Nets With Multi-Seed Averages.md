---
title: Compare Small-Data Neural Nets With Multi-Seed Averages
tags:
  - ml/evaluation
  - ml/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/소데이터-신경망-비교는-multi-seed-평균으로-한다
created: 2026-08-04
sources: []
---

## Summary

On small data, seed variance can exceed the effect you are measuring — a single-seed score (0.694) and a 3-seed mean (0.704) diverged enough to confuse conclusions, so every comparison was re-standardized to 3-seed averages.

## Details

- Context: while comparing feature-set experiments for NHIS hospitalization prediction (2,532 patients), the same configuration produced a single-seed val AUC of 0.694 versus a 3-seed mean of 0.704 — a 0.01 split.
- The problem: when differences between experiments are themselves around 0.01, one lucky or unlucky seed produces the same swing, so which configuration "wins" depends on the seed, not the configuration.
- The fix: all experiment comparisons were re-standardized to 3-seed averages, including re-running previously recorded single-seed scores to put them on the same footing.
- Principle: neural-net training is stochastic in initialization and shuffling, and this variance grows as data shrinks. When seed variance exceeds the effect size under comparison, a single-run score is noise.
- This is the experimental version of the statistics rule "claim only at the unit you tested" — one run of one seed does not license a claim about which configuration is better.
- Working rule: small-data experiment reports should state the number of seeds and the mean (and variance where possible).

## Sources

- Related: [[Joint Test Significance Is Not the Same as Individual Coefficient Significance]]
