---
title: Measure the Evaluation Server Budget With a Fixed-Prediction Dummy Submission
tags:
  - ml/competition
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/평가-서버의-실행-예산은-고정-예측-더미-제출로-실측한다
created: 2026-11-21
sources: []
---

## Summary

Do not size your strategy on community-reported evaluation-server speeds; **first measure the real time budget with a dummy submission that fixes predictions to a constant and only logs load and generation times** (a baseline score comes free). Whether a usable signal fits inside that budget is a separate question, answered by a runtime test of the real artifacts.

## Details

- The starting belief: the community held that generation on the evaluation server was too slow to solve a problem several times at test time. Taken at face value, that left only one-forward-pass-per-case methods.
- Dummy design: predictions fixed to True, no problem text written to logs, only per-model load time, single forward time and concurrent sampling throughput recorded, submitted to a free unofficial queue. Since it is not trying to score, it spares the rate-limited official submissions.
- Result: throughput was several times the community figure, and the whole run used only about 9% of the time limit, leaving plenty of headroom per case. The same submission also produced the official all-positive baseline score.
- Strategy expansion: the spare time went to a module that solves each problem several times, with per-model concurrency and token caps fixed from the measurements. Stopping on a token cap rather than wall-clock time keeps features stable even if server speed varies a little.
- A second measurement turned the plan again: a runtime test with the real artifacts (14/14 valid, no timeouts) showed that for long-thinking models no sample finished within the token cap on any evaluation case. Sampling gave way to a probe that reads the hidden state at the cap, and in the final comparison the sampling signal was far weaker than the internal-state signal and added nothing when combined.
- Measure budget headroom and signal separately: a dummy submission only answers "how much can I run?" Whether that budget yields a usable signal has to be measured again with the real artifacts.
- Climb a cost-ordered verification ladder: an official-ingestion contract test with a tiny CPU model → check the training script by recovering a signal planted in synthetic data → a real-server run through the free queue → a rate-limited official submission.
- Free verification infrastructure can vanish without notice: when the official platform came back, the free queue's workers were withdrawn, the last real-server checks never ran, and the official upload became the first real-server run. Do not defer critical checks.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Switch Components Off on Purpose to Map Real-Data Loss]], [[Budget Remote Runtime by Resource-Type Multipliers and the Worst-Case Path]], [[Measure the Oracle Ceiling Before Implementing]]
