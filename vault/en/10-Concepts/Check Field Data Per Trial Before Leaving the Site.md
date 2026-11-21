---
title: Check Field Data Per Trial Before Leaving the Site
tags:
  - research/measurement
  - dev/workflow
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/현장-데이터는-떠나기-전에-시행-단위로-점검한다
created: 2026-11-21
sources: []
---

## Summary

Even when the measurement method has been validated, **an individual trial can still fall short** — run integrity and pass/fail checks the moment each file arrives and call "redo" on site; files you did not check on site come back in the evening as the cost of a return visit.

## Details

- The check loop: from the phone in the field, attach the recording zip to a Claude Code session (/remote-control) → copy the attachment under `~/.claude/uploads/<session>/` into the raw-data folder with `cp -n` → confirm the sha256 matches (skip if the file already exists) → run the check script on several files at once → reply "received n" plus one line per trial (pass / redo + reason). The original in the recording app is deleted only after "received" appears.
- Rehearse the path the day before: resend a zip already received to confirm the matching sha256 skips the copy, and send an 8.7-second dummy recording with no steps to confirm the tool rejects it with "redo". Test both the happy path and the rejection path, so the tool can be trusted in the field.
- What the field check caught: the first leg-pendulum recordings had only 5, 5, and 9 continuous swing cycles against a minimum of 10. "Redo" went out at once with the cause — not the analysis, but a single push that let the leg stop within 9–12 s. The fix was "give a light push whenever it fades, 15+ swings (about 25 s)", and the earlier attempts were logged as valid=0.
- What was missed: walking files were held back until evening ("walking measurement was validated in the previous experiment, no need to send"). Only then did a ~4% mismatch show up between the hand-computed cadence of the baseline trial and the sensor value — every stage's stimulus tempo, chosen from that baseline, had shifted with it, and steps had to be recounted from video. A pendulum condition that still failed after retries meant coming back on the backup day.
- "Is the method valid?" and "is this trial intact?" are different questions: even if the method was confirmed earlier, recording gaps, sync-marker counts, step counts, and cycle counts must be checked per trial. Above all, cross-check any baseline trial that drives later stimuli against the sensor value before moving on.
- Look at the raw signal before an automatic "redo": the sync jumps were present in the raw signal of all 30 trials, yet the detector caught exactly three in only 11; one pendulum recording came out as 7 cycles because the analysis cut the swing short, while the signal showed about 14. If it is a detector failure rather than a performance failure, the answer is fixing the detector (with separate approval), not re-measuring.
- Say nothing about results in the field: knowing hypothesis results, stage summaries, or synchronization metrics mid-collection changes how the next trials are performed. Field replies carry integrity verdicts only.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Messenger Transfers Change Video FPS - Verify Frames Against a Filmed Clock]], [[Mark Sensor Recordings With Body Actions, Not Device Handling]], [[Verify Backup Creation Immediately After Running a Destructive Script]]
