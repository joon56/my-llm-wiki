---
title: Offline HTML Copies May Lack Required Meta Tags
tags:
  - dev/frontend
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/오프라인-HTML-사본에는-메타태그가-빠져-있을-수-있다
created: 2026-08-04
sources: []
---

## Summary

The Artifact publish pipeline auto-injects `<meta charset>` and viewport tags, but copying the same HTML out as a standalone file drops both — whenever HTML leaves its original pipeline, check charset/viewport first.

## Details

- When publishing an Artifact, the pipeline automatically injects `<meta charset="utf-8">` and `<meta name="viewport">` — the page renders fine even if the author never wrote them.
- Copy the same HTML out as an offline standalone file and the injection is gone → the file ships missing both tags.
- Symptom 1: missing charset → Korean text renders as mojibake (garbled characters).
- Symptom 2: missing viewport → mobile renders a zoomed-out desktop layout.
- Lesson: the "same HTML" needs different boilerplate on different distribution paths. What a pipeline silently fills in only becomes visible the moment you leave that pipeline.
- Checklist: whenever HTML moves outside its original publish path, verify `<meta charset="utf-8">` and `<meta name="viewport" content="width=device-width, initial-scale=1">` are present.

## Sources

- 
