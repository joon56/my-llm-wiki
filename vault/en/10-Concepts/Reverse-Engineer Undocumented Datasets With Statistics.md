---
title: Reverse-Engineer Undocumented Datasets With Statistics
tags:
  - ml/data
  - dev/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/미문서-데이터셋은-통계로-리버스-엔지니어링한다
created: 2026-08-04
sources: []
---

## Summary

For 218 undocumented columns, meanings were hypothesized from statistical clues — value ranges, zero ratios, inverse transforms — and then confirmed by asking the user explicit multiple-choice questions. The LLM proposes hypotheses; the human confirms domain truth.

## Details

- Context: the NHIS sample-cohort assignment came with 218 columns and no documentation — names alone did not reveal meanings.
- Statistical clue 1 — value ranges: the range and distribution of values separates ages, monetary amounts, codes, and flags.
- Statistical clue 2 — zero ratios: a column dominated by zeros is likely a sparse event (e.g., whether a particular type of care occurred).
- Statistical clue 3 — inverse transforms: applying an exp inverse transform to one column revealed a natural monetary scale, identifying it as "log(monthly cost)" — undoing candidate transforms is a powerful identification tool.
- Confirmation step: instead of silently proceeding on the statistical guesses, they were presented to the user as explicit multiple-choice questions for confirmation — far safer than assuming.
- Division of labor: the LLM generates hypotheses fast; the human adjudicates them with domain knowledge. This loop is the basic workflow for undocumented data.

## Sources

- Related: [[Bridge Joins Connect Tables Without Shared Keys]]
