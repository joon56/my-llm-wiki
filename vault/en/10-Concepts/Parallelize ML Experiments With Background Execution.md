---
title: Parallelize ML Experiments With Background Execution
tags:
  - tool/claude-code
  - dev/workflow
  - ml/training
status: distilled
publish: true
lang: en
translation: 10-Concepts/백그라운드-실행으로-ML-실험을-병렬화한다
created: 2026-08-04
sources: []
---

## Summary

Launching long training and sweep jobs detached with Claude Code Bash's `run_in_background` lets the conversation keep moving while completion notifications deliver results, so an hours-long batch of experiments can run in parallel inside a single session.

## Details

- Running a training job that takes tens of minutes in the foreground blocks the whole session for that duration. `run_in_background` detaches the job and returns control immediately.
- In practice, 15 long-running training and hyperparameter-sweep jobs were launched this way, fitting hours of experiment work into one session.
- When each job finishes, a completion notification is injected into the conversation automatically, so no result is missed — there is no need for a polling loop.
- The pattern: fire the jobs first → keep working on other things (code cleanup, docs, designing the next experiment) instead of waiting → harvest results as notifications arrive and fold them back in.
- Anti-pattern: polling with repeated `sleep`-then-check-logs cycles. Notifications are guaranteed to arrive, so polling only burns context and time.
- The payoff is largest for independent experiments (e.g. different hyperparameter combinations) — with no inter-job dependencies, everything can be launched at once.

## Sources
-
