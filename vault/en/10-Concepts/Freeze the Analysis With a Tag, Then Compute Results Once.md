---
title: Freeze the Analysis With a Tag, Then Compute Results Once
tags:
  - research/statistics
  - ml/evaluation
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/분석은-동결-태그를-찍은-뒤-결과를-한-번만-계산한다
created: 2026-11-21
sources: []
---

## Summary

While data is still coming in, look only at quality metrics; commit every decision rule, fallback, and method change, then **freeze the analysis with a git tag and compute the results once** — any change after the freeze is reported with before-and-after results side by side.

## Details

- Separate QA from results during collection: in a sensor-based walking experiment, each incoming trial was checked only for sampling rate, gaps, GPS segment distance, and phone orientation, while outcome metrics (cadence change, beat synchronization, speed) were neither computed nor saved (runs went to a temp folder). The analyst was also a participant, so seeing interim results would have changed how the remaining trials were walked.
- Enforce the freeze in code: a guard refuses to compute results on real data without the freeze tag, and the bypass option writes `unfrozen=true` plus input-file hashes into `run_info.json`. Push the tag to the remote as evidence that the rules came before the results.
- Decide more than the formula in advance: ten ambiguous definitions, how to handle a trial that broke a rule (drop and re-run, decided without looking at that trial's outcome), the group verdict if participants drop out, the fallback if even the reserve day fails, and which stages the extra camera films. Choosing on the day biases you toward whatever you chose.
- Pilot recordings are not used for verdicts, so procedures, equipment, and still-open decisions may change based on them. Definitions and confirmed values, however, can only change before the first real trial; after that, the only move left is "fix it and redo that trial at the end".
- Exclude data that shaped the method: the jump-detection method was designed and validated on test recordings, so using those same recordings as official results would mean grading your own homework. Commit the finalized method before opening any field files, and save the pre-change synthetic outputs to compare before and after.
- Correct after the freeze in a fixed order — record the rule, recompute, publish a before/after table: when the actual music start time turned out to differ from the assumption, the correction rule was written down before looking at results, and the before/after numbers were reported together with whether the verdict held. Changing criteria or dropping participants after seeing results is declared invalid in advance.
- Report flaws in a frozen rule instead of fixing them: segments within one trial are not independent, so a p-value that counts segments as samples is more optimistic than a trial-level cluster-bootstrap confidence interval. Keep the verdict the rule gives, always report the interval alongside it, and choose the independent unit first in the next design.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]], [[Augmented Trials Add No Information - Simulation Is for Testing Code]], [[Filling Unrecorded Conditions With Planned Values Fails Silently]]
