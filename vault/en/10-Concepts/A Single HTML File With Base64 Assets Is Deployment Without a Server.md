---
title: A Single HTML File With Base64 Assets Is Deployment Without a Server
tags:
  - dev/frontend
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/base64-내장-단일-HTML은-배포-없는-배포다
created: 2026-08-04
sources: []
---

## Summary

A single HTML file with every image, stylesheet, and script embedded inside it is "deployment without a server" — just send it over a messenger; no hosting required.

## Details

- 15 screenshots were resized and optimized with PIL, then embedded directly into the HTML as base64 data URIs.
- All CSS/JS inline as well — the result is a fully self-contained file with zero external requests.
- Outcome: one 712KB HTML file, shared as a messenger attachment with no server or hosting involved.
- Side benefit: the zero-external-request structure is also exactly what Artifact's CSP requires (external hosts blocked) — the same file works on both distribution paths.
- Trade-off: base64 encoding grows file size by roughly 33% per asset — always resize and compress images before embedding.
- When it fits: document-style deliverables in the hundreds-of-KB to few-MB range. Heavy media makes the file balloon and breaks the approach.

## Sources

- 
