---
title: Each MVP Round Tests One Core Risk Hypothesis
tags:
  - product/mvp
status: distilled
publish: true
lang: en
translation: 10-Concepts/MVP-라운드는-핵심-리스크-가설-하나에-집중한다
created: 2026-07-26
sources: []
---

## Summary

An MVP round must narrow down to **one risk hypothesis under test**. Bolting an unvalidated side technology onto the same round mixes two hypotheses — and makes the results uninterpretable either way.

## Details

- The failure pattern: a round meant to test "does the core service work" also ships "let's collect sensor data while we're at it" → if results are bad, is it the service or the sensor UX? If good, what contributed? No way to tell.
- The principle: define each round as "which risk are we killing this time" in one sentence → include only the minimum features that test it. Side features join conditionally in a later round, after the core hypothesis survives.
- Cross-validation: this conclusion emerged independently from two separate analyses (an LLM analysis and a government startup-program guide) converging on the same judgment — not a coincidence.
- The filter question: "If we cut this feature, does this round's hypothesis become untestable?" If no — cut it.

## Sources

- Related: [[Infer Unmeasurable Phenomena from Combined Indirect Signals]]
