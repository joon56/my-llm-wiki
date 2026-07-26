---
title: Verify Accessibility Contrast by Calculation Rather Than by Eye
tags:
  - dev/frontend
  - dev/accessibility
status: distilled
publish: true
lang: en
translation: 10-Concepts/접근성-대비는-계산으로-검증하지-눈으로-판단하지-않는다
created: 2026-07-26
sources: []
---

## Summary

Color contrast "looking fine" to the eye is not evidence of passing WCAG — verify it with a luminance calculation, and since text (4.5:1) and non-text UI elements (3:1) have different thresholds, manage their color tokens separately.

## Details

- The same color combination looks different depending on monitor, brightness, and individual eyesight. A visual pass is an unreproducible judgment.
- WCAG has two separate thresholds:
  - Regular text 4.5:1, large text 3:1 (WCAG 1.4.3)
  - Non-text UI elements like borders, icons, input outlines: 3:1 (WCAG 1.4.11)
- A common practical trap: reusing a gray that passes for text on a border, or vice versa — since the thresholds differ, one of the two ends up failing. Separating text and non-text color tokens from the start prevents this.
- Verification tools: your browser devtools' contrast checker, or computing relative luminance directly by formula. For CI, use an automated checker like axe-core.
- Generalization: the same principle as [[DOM Measurements Outrank Visual Overflow Judgments]] — measure, don't eyeball it.

## Sources
-
