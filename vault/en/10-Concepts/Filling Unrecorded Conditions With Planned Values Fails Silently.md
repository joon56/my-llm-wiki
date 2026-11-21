---
title: Filling Unrecorded Conditions With Planned Values Fails Silently
tags:
  - research/measurement
  - dev/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/신호에-안-남는-조건을-계획값으로-채우면-조용히-틀린다
created: 2026-11-21
sources: []
---

## Summary

If conditions the sensors cannot record (when the music started, which song came first) are filled in from the schedule or from defaults, **the analysis goes wrong while every quality check passes** — collect such conditions as actual values on every trial and mark filled-in values as assumptions.

## Details

- Case: the analysis of a sensor-based walking experiment assumed the music started 3 s after recording began (the default) and that the first song followed the assignment table. In reality the walker always pressed play near the end of the 10-second standing period (18-38 s) and always started from song 1, so the song boundaries of all eight music trials were off by 15-35 s.
- Quality checks only see what the signal recorded: those eight trials passed every check on sampling, gaps, GPS distance, and phone orientation. Playback timing and song order leave no trace in the sensors, so no check could catch them; the problem surfaced only after the analysis freeze, when the walker mentioned in passing that the music always went on as the standing period ended.
- Changing the procedure does not change the behavior: the same problem had already been found in the pre-check (music started with a headset button while standing leaves no start time in the data), and the rule was changed to "play from the phone screen right after starting the recording", yet the old habit persisted. Even after writing down that song order cannot be verified from the sensors, the first-song column had still been filled from the assignment table.
- A wrong planned value takes the design down with it: because the first song never changed, song order (time spent walking) and tempo rose together. Counterbalancing broke, mixing "speeding up as the walk goes on" with "following the tempo".
- Remedy: collect unobservable conditions as per-trial fields on the log sheet (first song, playback moment, times the phone was touched). Mark cells filled from defaults or the schedule as assumptions and ask the person who ran the trial to confirm them, and write any correction rule before looking at results (here: set the playback moment to each trial's detected departure time).
- For anything the signal does record, trust the signal over hand-copied values: exported file names carry UTC times, so copying them dates morning recordings to the previous day, and one teammate renamed files to condition names before uploading. Files were therefore linked by the start epoch stored inside each recording and the log-sheet time (±90 s), not by name.
- Convenience bulk values are planned values too: a proposal to set every log-sheet start time to "19:00" was declined because it contradicted the actual start times (the time cross-check would fail). Past temperatures with no observed value were left blank — a blank beats a plausible number.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Freeze the Analysis With a Tag, Then Compute Results Once]], [[Mark Sensor Recordings With Body Actions, Not Device Handling]], [[Verify Version Drift Between Planning Docs and Final Deliverables]]
