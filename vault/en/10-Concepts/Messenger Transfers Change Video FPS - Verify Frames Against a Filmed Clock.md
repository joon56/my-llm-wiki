---
title: Messenger Transfers Change Video FPS - Verify Frames Against a Filmed Clock
tags:
  - research/measurement
  - dev/data
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/메신저로-옮긴-영상은-fps가-바뀐다-—-프레임은-찍힌-시계로-검증한다
created: 2026-11-21
sources: []
---

## Summary

Video that passes through a messenger app **comes out with a different container, frame rate, and slow-motion structure, throwing frame-based measurements off by 4–8x** — rehearse before the real shoot by filming a stopwatch screen to verify the true fps frame by frame, and move analysis footage only as original files.

## Details

- Rehearsal design: put a 1/100 s stopwatch on another screen and film a 5-second clip per device and mode (normal 60 fps, slow motion at 120/240 fps). Read fps, frame count, duration, and resolution with ffprobe, then extract a few frames and compare them with the stopwatch digits. There is no need to film the actual movement.
- What KakaoTalk's "send to myself" did: all three files arrived as 30 fps .mp4 (1080p HEVC). The normal clip really was 30 fps (the setting was 60). In the 240 fps slow-motion clip, 240 frames spanned 1.00 s inside the slow section, so the captured frames survived — but frozen into a 30 fps file that plays 8x slower. The 120 fps clip showed 240 frames = 2.00 s, and its first and last 1–2 s ran at normal speed (33 ms per frame).
- The danger: converting frame counts to time with the file's 30 fps makes values like flight time wrong by 4–8x, and the playback speed changing at segment boundaries is a second trap. Log the capture fps on the data sheet, not the file metadata.
- Telling the cause: an original .MOV turning into .mp4, a lower fps, and slow motion baked into a normal file are the fingerprints of re-encoding. Sensor zips sent through the same messenger were only renamed (`TalkFile_…zip.zip`) and opened fine — generic files pass through untouched, media gets transformed.
- Cables have their own trap: with the iPhone's transfer setting on "Automatic", the copy broke off mid-conversion, leaving a 30 MB file without its trailing playback index (moov) or a 160×90 preview JPEG (7 KB) carrying a .MOV name. Switch to "Keep Originals"; if the problem persists, replug and tap "Trust" or use the OS photo import. Compare the received file size with the size on the device.
- Rules: move analysis footage as original files rather than through messengers, and do not delete originals from the capture device until the fps is verified. Check the first transferred file right away instead of trusting a memory that "files from that app opened fine before." The AAE sidecar of a slow-motion clip only marks the slowed section and is not needed.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Never Trust PDF Table Extraction Without Cross-Checking the Prose]], [[Verify Backup Creation Immediately After Running a Destructive Script]], [[Check Field Data Per Trial Before Leaving the Site]]
