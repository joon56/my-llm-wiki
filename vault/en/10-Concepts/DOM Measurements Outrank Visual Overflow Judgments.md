---
title: DOM Measurements Outrank Visual Overflow Judgments
tags:
  - dev/frontend
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/시각적-오버플로-판단보다-DOM-측정값이-우선한다
created: 2026-07-26
sources: []
---

## Summary

Don't conclude that a layout clipped in a screenshot is a CSS overflow bug — headless browsers often have a minimum window-width floor that distorts narrow-viewport screenshots, so the judgment call should come from a DOM measurement like `scrollWidth === clientWidth`.

## Details

- Some headless Chrome environments have a floor on window width (roughly ~500px) below which the requested viewport can't actually shrink. Even if you request a 375px mobile screenshot, the real render happens in a wider window, making the screen look clipped or misaligned.
- Misdiagnosing this distortion as "a bug causing horizontal scroll on mobile" leads you to break CSS chasing a bug that doesn't exist.
- The correct check: in the browser console/script, verify `document.documentElement.scrollWidth === document.documentElement.clientWidth`. If they're equal, there's no horizontal overflow — the screenshot artifact is a rendering-environment issue, however odd it looks.
- Generalization: a visual artifact (screenshot) is indirect evidence tangled up with rendering-environment constraints. The primary evidence for a layout judgment is the measurement the DOM itself reports.

## Sources
- Related: [[Verify Accessibility Contrast by Calculation Rather Than by Eye]]
