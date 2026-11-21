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
- A failed regeneration leaves the old image behind: a console-capture script failed to resize the window (100 columns), yet with no error the old image stayed in place and looked "updated". Open the output and check that the picture itself changed, not just that the file exists.
- Render generated PDF reports to page images and review those too: caption text overlapped, a line under a table ran into the border, table and figure titles split across pages, and a subheading was stranded at the bottom of a page. The fixes in python-docx were no-row-split (`cantSplit`) and wrapping content in a single-cell table (page-break settings had no effect inside table cells).
- Render the README as well: a preview through GitHub's renderer, checked as an image, showed the first column of a Korean table wrapping vertically one character at a time — invisible to syntax checks. Invisible fixed-width spaces in the first header cell secured the width, and callouts, `<details>`, Mermaid, and a banner SVG were checked the same way.

## Sources

- 
