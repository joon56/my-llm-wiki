---
title: A Pipeline That Turns YouTube Videos Into LLM-Readable Material
tags:
  - llm/pipeline
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/유튜브-영상을-LLM-학습-자료로-변환하는-파이프라인
created: 2026-08-04
sources: []
---

## Summary

An LLM cannot watch video directly, but yt-dlp captions (VTT) + ffmpeg scene-aware frame extraction + a timestamped transcript combine into material an LLM can "watch" sequentially.

## Details

- Step 1: pull captions (VTT) with `yt-dlp` first — far cheaper than downloading the full video, and the captions form the backbone of comprehension.
- Step 2: extract representative frames with `ffmpeg` using scene-change detection. Higher information density per frame than uniform-interval capture.
- Step 3: parse the VTT into a timestamped transcript; the LLM reads the frame images in order, cross-referencing the transcript.
- Practical pitfall 1: caption requests frequently hit 429 rate limits — retry logic is mandatory.
- Practical pitfall 2: videos without captions fall back to Whisper transcription.
- Observed result: 3 lecture videos (12/14/33 minutes) became documented knowledge within a single session.

## Sources

- 
