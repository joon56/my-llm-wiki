---
title: Judge an Error Against the Slack the Analysis Already Absorbs
tags:
  - research/measurement
  - product/sensing
status: distilled
publish: true
lang: en
translation: 10-Concepts/오차는-분석이-흡수하는-여유와-비교해-판정한다
created: 2026-11-21
sources: []
---

## Summary

Decide which errors to control **by comparing them with the slack the analysis already absorbs — the windows it discards, the pass/fail tolerance, the detection radius — not by their absolute size**. Far below the slack: ignore it and keep the procedure simple. Comparable: measure and log it. Above it: change the procedure or the design.

## Details

- Wireless earphone latency (under 1 s) was ignored: the analysis drops 10 s on either side of every song boundary, and the synchronization metric uses only step intervals. Mandating wired earphones because "there is latency" would only have made the protocol heavier.
- Compare accumulating errors by their accumulated size: a 2 s gap between songs makes the fourth song start 6 s later than computed. The 10 s exclusion window absorbs that, but past 10 s the steps of one song bleed into the next song's segment. So measure it once — play three short songs back to back, time from the start of song 1 to the start of song 3, subtract the listed lengths of songs 1 and 2, and divide by 2.
- Compare relative errors with the tolerance: stopping 1 m off at each end of a 200 m segment is at most about 1%, well under the 5% tolerance of the distance check. Keep the cheap control instead — stop in front of the same landmark every time.
- Compare position precision with the detection radius: with a 20 m pass radius, phone GPS or photo EXIF (about 5 m) is enough, while a 10-character Plus Code (cells of about 14 m) is barely adequate and stays a last resort.
- Ignore errors inside spans the analysis throws away: start and finish positions can differ by a few meters because the first and last 20 s are excluded. Telling people which spots must be exact (the ends of the timed segment) and which need not be lightens the burden in the field.
- Exclusion windows also set the required recording length: after dropping 20 s at each end, a 2-minute metronome walk at 100 BPM leaves about 130 steps and a 3-minute walk about 230. Working back from the remaining sample count led to recommending 3 minutes instead of 2.
- Decision rule: error ≪ slack → ignore and simplify; error ≈ slack → measure and log; error > slack → change the procedure or design.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Validation Reference Must Come From a Source Independent of What It Checks]], [[Measure the Oracle Ceiling Before Implementing]]
