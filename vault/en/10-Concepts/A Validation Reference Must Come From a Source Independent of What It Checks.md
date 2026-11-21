---
title: A Validation Reference Must Come From a Source Independent of What It Checks
tags:
  - research/measurement
  - product/sensing
  - ml/evaluation
status: distilled
publish: true
lang: en
translation: 10-Concepts/검증-기준은-검증-대상과-독립된-출처에서-와야-한다
created: 2026-11-21
sources: []
---

## Summary

If the reference used to check a sensor or model output is produced **by the same sensor or the same pipeline, the two share their errors and the check loses its teeth** — build references from means that share no error source with what they check: map distances, manual counts, known inputs.

## Details

- The trap: in a sensor-based walking experiment, the plan was to measure the length of the timed segment from the phone's own GPS log. But that length was the reference for a check that "the GPS path length must be within 5% of the reference" — checking GPS against GPS passes even when both are wrong. Measure the reference with a map tool instead, clicking along the route actually walked.
- Two quantities derived from the same sensor can disagree badly: in the pilot recording, integrated Doppler speed gave 628 m while the GPS track gave 875–893 m, about 30% apart. Comparing them with each other cannot tell which is right; only a third, independent measurement (the whole route measured on a map) can settle it.
- Take reference points from the same source as the reference distance: marking the segment's start and end with phone GPS on site bakes about 5 m of error into the reference itself (median horizontal accuracy in the pilot was 4.75 m) — more than the trial-to-trial variation in where one stops (about 1 m in front of the same landmark). Pick the coordinates on the same map used for the distance, so both share the same points. Choose landmarks that also appear on the map, such as building corners or alley entrances.
- Give every metric its own independent reference: step detection against exactly 100 counted steps (±2 allowed), beat synchronization against a walk paced by a metronome (a known input), and segment speed as map distance ÷ the time taken to cross the segment.
- Wearable event detection has the same structure: a smartwatch pull-detection app is scored against an observer's manual button presses, matched to automatic detections within a ±2 s window, yielding sensitivity and specificity. Labels derived from the detector's own output cannot serve as the reference.
- Generalization: the first question in designing any validation is "which error sources does this reference share with the value under test?" It is the same principle as never evaluating a model on labels that model produced.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]], [[Infer Unmeasurable Phenomena from Combined Indirect Signals]], [[Judge an Error Against the Slack the Analysis Already Absorbs]]
