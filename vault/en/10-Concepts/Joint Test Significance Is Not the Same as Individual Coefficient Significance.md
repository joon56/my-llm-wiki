---
title: Joint Test Significance Is Not the Same as Individual Coefficient Significance
tags:
  - research/statistics
  - research/writing
status: distilled
publish: true
lang: en
translation: 10-Concepts/결합-검정-유의성과-개별-계수-유의성은-다르다
created: 2026-07-26
sources: []
---

## Summary

A joint test on several coefficients together (e.g., a Wald test on a difference) coming back significant does not mean each individual coefficient inside it is significant on its own — writing it up as "A and B were each significant" overstates what the joint test actually showed.

## Details

- A joint test only answers "can we reject the hypothesis that these coefficients are all zero?" It's a signal about the combination as a whole, not about which coefficient produced the signal.
- Common mistake: a joint test on the difference between two groups comes back p<0.05, and the write-up quietly expands this to "Group A's effect was significant, and so was Group B's." One of the individual coefficients may not actually be significant.
- Correct phrasing: narrow the claim to exactly the unit that was tested — "the difference between the two coefficients was significant (joint Wald p=…); individually, only A was significant."
- Review habit: when transcribing statistical results, check sentence by sentence whether the test a sentence claims was performed is the test that was actually run.

## Sources
- Related: [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]]
