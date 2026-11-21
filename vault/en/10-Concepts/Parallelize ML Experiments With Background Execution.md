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
- Remote jobs (cloud GPUs) produce no local completion notification, so launch a background "watcher that exits on an event": it collects results every 20 minutes and exits when a job finishes or a data batch arrives, and its completion notification wakes the agent (it must be a tracked background task for that to happen). Relaunch it after handling each event, and give it a timeout to catch remote machines that stop reporting.
- Counterexample: experiments that measure latency or throughput get distorted when run alongside other heavy work. With another project holding the GPU at 96%, the measurement was set to start automatically once the GPU read idle three checks in a row (waiting up to 6 hours), and resources in use by running work — a build folder a live server was reading, the GPU during a live demo — were left untouched.
- When you launch a job and end your reply, the user experiences it as a stall — one minute into a 12-minute check came "why did it stop?" When launching, say that the reply ends but the work continues and resumes automatically on the completion notification, along with the expected duration and what happens next.

## Sources
-
