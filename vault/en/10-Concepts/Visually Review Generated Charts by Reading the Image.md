---
title: Visually Review Generated Charts by Reading the Image
tags:
  - tool/claude-code
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/생성한-차트는-이미지로-읽어-시각-검토한다
created: 2026-08-04
sources: []
---

## Summary

Chart code that "runs without error" can still be visually broken — after matplotlib renders a PNG, the agent must Read the image itself, inspect it, and loop on fixes.

## Details

- The loop: render PNG with matplotlib → agent Reads the resulting image → spot defects like text overlap → fix the code → re-render. In the observed session, it converged in 2 iterations.
- Defect type caught: overlapping labels/text — a class of problem that exit codes and error-free execution can never detect.
- Principle: "it ran without errors" only verifies code validity; when the deliverable is an image, verification must happen at the image level.
- Bonus pattern — GitHub README light/dark theming: render a light/dark PNG pair and reference them via `<picture>` + a `prefers-color-scheme` media query in the README.
- The pattern is not chart-specific: diagrams, composited screenshots, and any visual output deserve the same read-back review.

## Sources

- 
