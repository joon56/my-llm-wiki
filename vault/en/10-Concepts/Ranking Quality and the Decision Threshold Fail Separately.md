---
title: Ranking Quality and the Decision Threshold Fail Separately
tags:
  - ml/evaluation
  - ml/competition
status: distilled
publish: true
lang: en
translation: 10-Concepts/순위-성능과-판정-임계값은-따로-고장-난다
created: 2026-11-21
sources: []
---

## Summary

Even with strong cross-validated ranking (AUC), **a decision cutoff calibrated on a set whose difficulty and positive rate differ from the evaluation set skews predictions to one side and caps a balanced score at a low level** — when a score comes in below expectations, count the predicted-positive rate before blaming luck.

## Details

- Symptom: a binary classifier that cross-validated well beat the all-positive baseline by only two cases on a 21-case evaluation set that was half positive. The result sat inside the pre-registered band, and with 21 cases a single run carries about ±0.11 of noise, so the score alone could not separate bad luck from a defect.
- Diagnosis order: (1) execution failures or fallbacks → none. (2) mismatch between the training-data generation path and the evaluation path → ruled out, because both paths (vLLM and HF) finished the same problems within the token cap at the same rate. (3) the prediction distribution → only 3 of 21 cases predicted positive, and 0 of 11 for one model family. The cause was (3).
- Cause: the cutoff was fitted on the official training cases, which were easier than the evaluation set and 74% positive, so it landed far on the "easy" side of the reference point. Evaluation scores clustered around the reference point and nearly all fell on the negative side; class weighting that assumed a balanced evaluation set made the skew worse.
- Fix: keep the model and features and move only the cutoff to the design reference point (the center of each model's own score distribution). Training-case performance was essentially unchanged (balanced accuracy differed by 0.005), and on the same evaluation features it predicted 10 of 21 positive — a balanced split. The fixed version's actual evaluation score was not confirmed within the session.
- Corroboration: a simpler variant with lower cross-validated AUC predicted 9 of 21 positive, skewed less, and scored two cases higher on evaluation. Ranking quality and threshold placement are separate failure points.
- Prevention: before submitting, compute the predicted-positive rate on an unlabeled pool that resembles deployment and compare it with the expected rate. The score distribution of unlabeled inputs is visible at test time too, so it is fair to use for checking where the threshold sits.
- General rule: when the calibration set's prior or difficulty differs from the deployment set, the ranking can hold while the optimal threshold moves. Log the predicted-positive rate next to every score and this failure shows up immediately.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Effects Smaller Than the Leaderboard Resolution Cannot Be Read]], [[Build Training Data by Replicating the Evaluation Runtime Down to Its Defaults]]
