---
title: Block Temporal Leakage With a Feature Cutoff Rule
tags:
  - ml/data
  - ml/features
status: distilled
publish: true
lang: en
translation: 10-Concepts/시간-누수는-피처-기준-시점-규칙으로-원천-차단한다
created: 2026-08-04
sources: []
---

## Summary

Do not judge temporal leakage feature by feature — block it at the source with one explicit cutoff rule ("all features from before time T only"). A stated rule makes leakage auditable.

## Details

- Context: in the NHIS assignment predicting 2012 hospitalization, one rule was fixed up front — every feature uses data from 2010 or earlier (≤2010); the target is 2012.
- That single rule automatically excludes death records, 2012 claims, and any variable stamped with a future date.
- The alternative — asking "is this one leakage?" per feature — invites missed judgments and cannot be reconstructed later: nobody remembers which criterion filtered what.
- The payoff of an explicit cutoff is auditability: every feature can be checked with the same single question, "was it generated before the cutoff?"
- Leaving a gap between feature observation and prediction time (here, 2011) reproduces the deployment situation where only genuinely available data can be used.
- Generalization: in temporal or event prediction, leakage prevention should be a rule written into code and docs, not an intention to "be careful."

## Sources

- 
