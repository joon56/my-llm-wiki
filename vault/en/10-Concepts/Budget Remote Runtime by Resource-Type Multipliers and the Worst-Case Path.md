---
title: Budget Remote Runtime by Resource-Type Multipliers and the Worst-Case Path
tags:
  - ml/competition
  - dev/testing
  - infra/cloud
status: distilled
publish: true
lang: en
translation: 10-Concepts/원격-실행-시간은-자원-유형별-배율과-최악-경로로-잰다
created: 2026-11-21
sources: []
---

## Summary

The host differs from your machine in CPU speed, execution path, and data size, so **a local pass does not guarantee a remote pass** — budget time with a per-resource-type multiplier on the most expensive path, verify wiring with forced paths and zero-weight identity, and for one-shot submissions design how failure behaves.

## Details

- The failure: a package heavy on CPU tree training passed locally at 571 s (63% of the limit, 289 s of it tree training) and was rejected for a timeout on the host. Records already showed the host CPU running 2-2.6x slower than the local machine, but recent submissions had been GPU-bound, so "host ≈ local" was wrongly generalized.
- Keep a separate multiplier per resource type: a "host ≈ local" learned on GPU-bound work must not be applied to CPU-bound work. The lighter rebuild (tree models on 1 sub-score instead of 3, 2 folds instead of 5) cut tree training from 289 to 74 s and the total from 571 to 334 s.
- Time the conditional path: when an in-run check retrains models after *accepting* a candidate, local synthetic data always rejects, so only the reject path is ever timed. The projected host time on acceptance was 90-104% of the limit, a structure that times out exactly when things go well. Retraining one model instead of two brought it to 72-79%, and packages near the limit also got an elapsed-time cutoff (skip retraining past about 78% of the limit).
- Verify the wiring: with the new path's weight set to 0, the output must be bit-identical to the baseline (17,856 vectors identical, the hook called exactly once). Run once more in a forced-accept mode to confirm the accept path completes end to end.
- Rehearse the final conditions: run locally at the final phase's data size to catch errors that only appear there and to check time (1,117 s locally → 40-65% of the limit after the multiplier). Rehearse the one-shot final code path on the host during the development phase, where failures are free.
- Design the failure mode: if the final phase accepts exactly one success but lets failures retry, do not silently fall back to the baseline's output on an error or timeout — a silent fallback spends the only success on an inferior output. A person picks from the fallback chain (main → light fallback → baseline) after seeing the result; an internal cutoff with baseline output is only for a deadline-day reading submission with no time left to retry.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Measure the Evaluation Server Budget With a Fixed-Prediction Dummy Submission]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]], [[Fire-and-Forget Hooks Fail Silently]]
