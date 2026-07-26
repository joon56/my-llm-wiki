---
title: Verify Version Drift Between Planning Docs and Final Deliverables
tags:
  - dev/docs
  - research/writing
status: distilled
publish: true
lang: en
translation: 10-Concepts/계획-문서와-최종-산출물의-버전-드리프트를-검증하라
created: 2026-07-26
sources: []
---

## Summary

Don't quote planning documents like a README or DESIGN.md at face value — plans and final deliverables inevitably drift apart during development, so cross-check anything you cite against the latest output first.

## Details

- Real example: design doc v5 named a metric `ra_score`, but the final report v6 had renamed it to `any_accident` — citing the design doc alone would have referenced a value that no longer existed.
- Why drift happens: a planning document records "intent at the time" and then stops changing, while the deliverable keeps getting revised. Updating the doc to match the deliverable is almost always forgotten.
- Verification procedure: before using a fact (a number, a name, a structure) drawn from a planning document, re-confirm that same fact against the final deliverable (the latest file version, the actual run output). If they disagree, the deliverable is the truth.
- Same root problem as data architectures built around manual synchronization instead of a single source of truth — hand-synchronized copies inevitably diverge.

## Sources
-
