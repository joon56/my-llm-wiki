---
title: Ratio Effect Metrics Shrink on Their Own as the Denominator Grows
tags:
  - research/statistics
  - research/measurement
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/비율형-효과-지표는-분모가-커지면-저절로-작아진다
created: 2026-11-21
sources: []
---

## Summary

A ratio metric that measures "what fraction of the gap to the target was closed" **shrinks whenever its denominator (the gap) grows, even if the response stays the same** — so it can falsely support a hypothesis like "the bigger the gap, the less people follow." Report the ratio next to the absolute change, and exclude conditions whose largest possible effect is smaller than the noise.

## Details

- Example metric: how strongly music tempo pulls walking cadence, R = (cadence with music − usual cadence) ÷ (song tempo − usual cadence). R = 1 means locked to the beat, 0 means no change. It has the same shape as normalized gain in education research ("what share of the gap was closed").
- The mechanism (hypothetical numbers): someone whose usual cadence is 100 steps/min speeds up by the same +6 at targets of 110, 120, and 140. R falls 0.60 → 0.30 → 0.15. The response is constant, yet it looks as if "larger tempo gaps pull less."
- Always fit a comparison model: "music makes you walk a fixed amount faster regardless of tempo" (constant shift, Δ = a) produces exactly the same decline in R. A falling R alone cannot separate the proportional model (Δ = b·(tempo − usual)) from the constant-shift model.
- Small denominators blow up the other way: if the target is only 2 steps/min above the usual cadence, a +6 change gives R = 3.0 (overshooting the beat), and ±2 steps/min of noise alone swings R by ±1.
- Compute the detection limit first: in that condition even perfect following changes cadence by only +2, while with trial-to-trial noise σ = 2 steps/min and 3 trials per condition the chance band is about ±3.3 (≈ 2σ√(2/n)) — the condition cannot be judged by design. Choose stimulus levels per person, from their own baseline, so that the largest possible effect exceeds the noise limit.
- Fix the definition before seeing results and report both: whether "being pulled" is measured as a ratio or as an absolute change can flip the direction of the conclusion. Even if the ratio is the headline metric, report the absolute change beside it.
- Check confounds that produce the same pattern: if conditions were recorded in different settings (route, day) and those differences line up with the hypothesized direction, a ratio that fits nicely may just be a setting effect.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Joint Test Significance Is Not the Same as Individual Coefficient Significance]], [[Augmented Trials Add No Information - Simulation Is for Testing Code]], [[Freeze the Analysis With a Tag, Then Compute Results Once]]
