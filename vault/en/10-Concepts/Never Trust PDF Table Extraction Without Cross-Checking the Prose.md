---
title: Never Trust PDF Table Extraction Without Cross-Checking the Prose
tags:
  - dev/data
  - research/writing
status: distilled
publish: true
lang: en
translation: 10-Concepts/PDF-표-추출값은-본문-대조-없이-신뢰하지-않는다
created: 2026-07-26
sources: []
---

## Summary

PDF text-extraction tools like pdftotext scramble table columns — treat any number pulled from a table as provisional until you've cross-checked it against the surrounding prose.

## Details

- A table in a PDF is just a visual layout; it has no underlying row/column structure. Text extraction often garbles the reading order, so a number from an adjacent column gets glued onto the wrong one.
- Why it's dangerous: the scrambled output still looks like a plausible sequence of numbers, so there's no visual cue that anything went wrong. Quoting it directly means reporting the value of a different variable.
- How to verify: papers and reports often restate key figures in prose ("the coefficient was 0.42 and significant") — cross-check the extracted table value against that sentence. If there's no restatement, open the PDF and read the table by eye.
- Generalization: treat any data that has passed through a structure-losing conversion (table → text, layout → plain text) as provisional until it's been verified through an independent path.

## Sources
-
