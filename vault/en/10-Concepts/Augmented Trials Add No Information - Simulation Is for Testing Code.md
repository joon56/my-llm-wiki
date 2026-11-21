---
title: Augmented Trials Add No Information - Simulation Is for Testing Code
tags:
  - ml/data
  - ml/evaluation
  - research/statistics
status: distilled
publish: true
lang: en
translation: 10-Concepts/증강한-회차는-정보를-늘리지-않는다-—-시뮬레이션은-코드-점검용이다
created: 2026-11-21
sources: []
---

## Summary

Simulated trials spun out of one or two real recordings **add rows but no information**, so they cannot serve as evidence for a hypothesis — use simulation to test the analysis code and preview figures, and compute the numbers a decision needs directly from real data and a noise estimate.

## Details

- A common way to fill missing trials: take a real sensor recording of the same condition and stretch or compress only its time axis by a factor s. Cadence and speed scale by 1/s, while step count, route, and waveform stay identical. Here s was drawn log-normally around the measured value, with a spread σ (1.7%) estimated from the only pair of repeated measurements available.
- Information does not grow: simulated trials replicate the pattern of the real ones, so 15 trials still carry the information of 1–2. Any trend visible in the augmented set was already in the real data; a trend that was not there can only come from the random draw.
- Numbers ride on the random seed: if the simulated baseline trials happen to come out slow, the baseline drops and every effect computed against it moves with it. A number whose conclusion flips when you change the seed is not evidence.
- Variance gets underestimated: step-level structure (pauses, turns, step-to-step variation) is copied from the original, so variability metrics look far closer to the original than genuine repeats would. The spread that real repetition would show is missing, which makes results look more precise than they are.
- The proper use is testing code: check that all 19 simulated files open with the project's reader, that the sample interval matches the original, that each trial's cadence hits its target, and that the step frequency measured from the accelerometer also changed by 1/s (proof that the transform touched the signal, not just the metadata).
- Answer decision questions from real data: with trial-to-trial noise σ and n trials per condition, the smallest mean difference distinguishable from chance is roughly 2σ√(2/n) (σ = 1.7 steps/min and n = 3 give about 2.8 steps/min). To check whether the analysis code reaches the right verdict, build a separate synthetic test set with planted ground truth, unrelated to the real recordings.
- Isolate and label: prefix the files with `sim-`, write `SIMULATED` into the metadata's device name and ID fields (fields the pipeline does not use), and keep them out of the real-data folder. They share the raw format, so once mixed there is no way to tell them apart. The moment generation parameters are tuned toward an expected conclusion, the simulation stops being a test tool and becomes fabricated data.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Ratio Effect Metrics Shrink on Their Own as the Denominator Grows]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]], [[Compare Small-Data Neural Nets With Multi-Seed Averages]]
