---
title: Select Improvements the Leaderboard Cannot Read With an In-Submission Holdout
tags:
  - ml/evaluation
  - ml/competition
  - ml/overfitting
status: distilled
publish: true
lang: en
translation: 10-Concepts/리더보드가-못-읽는-개선은-제출물-안의-hold-out으로-고른다
created: 2026-11-21
sources: []
---

## Summary

When external scores are coarser than the effect, **move validation inside the run** — split the labeled rows from the real distribution that arrive at run time into a selection set (S) and a confirmation set (E), choose candidate transforms on S, and apply one only if its lower bound on E is above zero, so the worst case is the baseline's own output.

## Details

- Structure: run the baseline once, choose among candidate transforms (mixing weights, calibration/temperature, log pooling with external models, a copy share for exact-match rows) on S (1,000 respondents), and confirm on E (another 1,000). Apply only if the lower bound is above zero; otherwise emit the baseline output unchanged.
- What can skip the guard: under log score, averaging probabilities across seeds cannot do worse than the average single seed (Jensen's inequality). The expected loss is zero, so apply it unconditionally.
- Pitfall 1, mixed score types: candidate rankings mixed "optimistic" in-sample scores with "honest" cross-fitted scores, which systematically favored learned candidates. Rank every learned candidate by cross-fitted scores, and refit on more rows only after it passes confirmation.
- Pitfall 2, an unverified accept decision: local synthetic data has no real structure, so the guard always rejects and the accept path never runs. Build a simulation with injected structure (duplicated rows) to confirm that the guard actually accepts (positive lower bound on E) and that the final apply path runs — it checks the code, it does not estimate the effect.
- Match the threshold to the scoring: when the final phase is scored exactly, sub-step gains count, so the confirmation bar was relaxed from z 1.645 to 1.0, with the user told and the change kept reversible. Detection thresholds that may miss on real data get several stepped flags instead of a single cutoff.
- Boundary: never design a channel that carries guard decisions or private-data statistics out through the score. Under competition rules that can count as data exfiltration.
- Honest reporting: if no external reading confirmed the contribution, state in the write-up that you claim nothing about the size of the additions' contribution. Here all 24 development-phase variants stayed below one display step.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]], [[The Train-Validation Metric Gap Signals Overfitting]], [[Augmented Trials Add No Information - Simulation Is for Testing Code]]
