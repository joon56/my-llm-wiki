---
title: Data Architecture That Generates Derivatives From a Single Source of Truth
tags:
  - dev/architecture
status: distilled
publish: true
lang: en
translation: 10-Concepts/단일-원본에서-파생물을-생성하는-데이터-아키텍처
created: 2026-07-26
sources: []
---

## Summary

When the same data has to be published in multiple formats (md, ics, rss, etc.), managing each format by hand will always drift out of sync — keep a single source of truth and generate everything else with a build script.

## Details

- The failure pattern: schedule data lives in a markdown table, a calendar (ics), and an RSS feed. Every edit has to touch all three, and a human will inevitably miss one. Over time you can't even tell which copy is authoritative.
- The fix:
  1. One structured file as the source (JSON/YAML/CSV) — the only thing a human edits directly
  2. Derivatives (md, ics, rss, html) are generated from the source by script — never edited by hand
  3. Wire generation into the build/commit step so derivatives auto-update whenever the source changes
- The moment you feel the urge to hand-edit a derivative is a design failure signal — that need should be folded back into the source schema instead.
- This wiki's own structure follows the same principle: session logs (source) → auto-converted archive → site build.

## Sources
-
