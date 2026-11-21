---
title: Record Deliberate Omissions and Their Reasons Next to the Code
tags:
  - dev/workflow
  - dev/docs
  - product/mvp
status: distilled
publish: true
lang: en
translation: 10-Concepts/의도적으로-안-한-것은-이유와-함께-코드에-남긴다
created: 2026-11-21
sources: []
---

## Summary

Blanks in a roadmap read as "to-do" to the next worker, human or agent — **leave the decision, the reason, and what would break next to the code for anything deliberately left undone**, and when an improvement request arrives, start by auditing the plan against the code.

## Details

- The case: a smartwatch sensor app got the request "do every possible enhancement, then build a release package." Comparing the planning document's roadmap with the code showed everything — a signal-processing replacement, new metrics, a validation mode — was already implemented. Zero new lines of code; only build verification and packaging.
- The one remaining unapplied item (sensor batching) was a deliberate decision, with the reason in a code comment: batching would break real-time detection that has to trigger haptics within 1–2 s, and because the same listener serves both logging and detection, batching would gain nothing. Without that comment it would have looked like a missing item and been "completed", breaking the core feature.
- What to record: (1) the decision not to do it, (2) why, (3) which feature breaks if it is applied. Put it in a comment beside the relevant code or in a decision record, so anyone who opens the code meets it even if they never read the roadmap.
- Audit first: do not start implementing on an "enhance it" request; tabulate each planned item against the code. That prevents rebuilding finished work and "filling in" deliberate omissions.
- Classify the remaining items by what blocks them: code (done), experiments (validation sessions), data (no labels to train a classifier), hardware (a separate sensor device), dropped (refuted by literature or API limits). "Everything code can do is done; what remains needs experiments, hardware, and data" sets the next actions.
- Put the limits of the test environment in the same table: an emulator has no real sensors or GPS, so detection logic cannot be validated there. Keep the emulator for UI-flow demos and make real-device testing the top priority.
- Check deliverables against the docs too: the install guide mentioned only the watch app APK, so the phone companion APK was added to the release zip and the guide updated.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Verify Version Drift Between Planning Docs and Final Deliverables]], [[Each MVP Round Tests One Core Risk Hypothesis]], [[Passing Synthetic-Input Tests Is Not Real-World Readiness]]
