---
title: Read Large PDFs Token-Efficiently With a PyMuPDF Fallback
tags:
  - llm/pipeline
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/대용량-PDF는-PyMuPDF-폴백으로-토큰-효율적으로-읽는다
created: 2026-08-04
sources: []
---

## Summary

When the Read tool's PDF rendering fails (poppler missing), PyMuPDF (fitz) extracts full text cheaply and only selected pages get rendered as images — text-first, images-on-demand keeps token cost proportional to what you actually need.

## Details

- Situation: the Read tool's PDF page rendering failed because poppler was missing → PyMuPDF (`fitz`) served as the fallback.
- First pass: extract text from all 76 pages with `fitz` — text is far cheaper in tokens than images.
- Second pass: render as images only the pages where text is insufficient (tables, screenshots, layout-dependent content).
- Measured: only 28 of 76 pages were viewed as images — text extraction sufficed for the other 48.
- Principle: reading every page as an image makes token cost proportional to document size; text-first + images-on-demand makes it proportional to what you actually need to see.
- Caveat: text extraction can scramble structure (tables especially), so verify any extracted figure before quoting it.

## Sources

- 
