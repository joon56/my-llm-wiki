---
title: Sorting by a Sum Aggregate Lets Duplicate Rows Inflate Rankings
tags:
  - dev/db
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/집계-정렬-키에-Sum을-쓰면-중복-행이-순위를-부풀린다
created: 2026-10-05
sources: []
---

## Summary

If a leaderboard sorts by a join aggregate like `Sum(scores__score)`, then when one submission's score rows get stored twice, **the page shows 0.58 but the sort sees 1.16** — and a low score lands in first place.

## Details

- Observation: the public leaderboard's #1 showed 0.58, with a row of 0.65 teams right below it.
- Diagnosis: counted score objects per row via the public API -> every other row had 4 (one per metric), that row had 8 (the same values twice under different ids). The platform's sort code was `annotate(primary_col=Sum('scores__score', filter=Q(scores__column=primary_col)))`.
- Mechanism: on a 1:N relation, using Sum or Count as a sort key silently assumes "one value per submission per metric". The moment a duplicate row appears (e.g. a scoring retry), the value doubles. The display code shows a single value, so the mismatch never surfaces on screen.
- Defense: build sort keys from Max or a single-value lookup, or enforce a unique constraint on (submission, metric) first. Make sure the sorted value and the displayed value come from the same source.
- Habit: when displayed scores and sort order disagree, count the underlying rows before assuming some "hidden other score".
- Impact call: true ranks are unchanged; only the display shifts. If final results come from a different phase, it is harmless. When reporting, cite the submission id.

## Sources

- Distilled from private Claude Code session logs (not published).
