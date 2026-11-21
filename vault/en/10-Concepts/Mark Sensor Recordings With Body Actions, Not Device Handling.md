---
title: Mark Sensor Recordings With Body Actions, Not Device Handling
tags:
  - product/sensing
  - research/measurement
  - dev/data
status: distilled
publish: true
lang: en
translation: 10-Concepts/센서-기록의-표시는-기기-조작이-아니라-몸-동작으로-남긴다
created: 2026-11-21
sources: []
---

## Summary

Instead of pulling out the device to annotate during a recording, **mark segments and sync points with actions that leave their own trace in the data (stops, still stands, jumps and a clap)** — but a marker only works if it is shaped and spaced so the detector reliably catches it.

## Details

- The problem: taking the phone out mid-recording to mark something (the app's annotation feature, a photo, a note) removes a "device handled" span from the analysis and changes the device's orientation in the pocket or pouch. So the recording app's annotation feature was not used.
- Segment marks: a 2-second stop at the start and end of the timed segment leaves two "step gaps" in the data, and the code uses the time between them (speed = segment length ÷ time between the two stops). It works like average-speed enforcement on a highway: no watch and no device handling needed.
- Baseline marks: stand still for 10 s at the start and end of each recording, and for 2 s before each jump. Taking the device out while standing shortens the baseline, so count the full 10 s first.
- Video-sensor sync: start a new recording for every trial and do three jumps and a clap in front of the camera before the trial. It acts as a slate that lines up acceleration peaks with video frames. Keep file names as recorded and pair files by recording start order.
- Failure 1 — markers the detector misses: the raw signals of all 30 walking trials contained three jumps, yet the detector caught exactly three in only 11. Rapid back-to-back jumps, or the device shifting in the pocket during flight, produced spiky signals. Putting the phone into the pouch also risks being mistaken for a jump.
- Failure 2 — a skipped baseline: the first jump, preceded by less than 1 s of stillness, was dropped from the analysis, so only two of three counted.
- The fix: write the marker's spacing and posture (interval between jumps, hands on hips, stillness then countermovement) into the protocol to match the detector's assumptions, and check the detection rate with test recordings before field day. Noting rough times after the recording (segment passed, device touched) narrows the search when detection fails.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Check Field Data Per Trial Before Leaving the Site]], [[Infer Unmeasurable Phenomena from Combined Indirect Signals]], [[Filling Unrecorded Conditions With Planned Values Fails Silently]]
