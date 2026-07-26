---
title: Infer Unmeasurable Phenomena from Combined Indirect Signals
tags:
  - dev/data
  - product/sensing
status: distilled
publish: true
lang: en
translation: 10-Concepts/직접-측정-불가능한-현상은-간접-신호-조합으로-역추론한다
created: 2026-07-26
sources: []
---

## Summary

Phenomena with no direct sensor — emotions, olfactory experience — are inferred from the **traces of accompanying behavior**, using a **combination** of low-level signals (IMU posture, GPS stillness, time of day). A single sensor value only becomes meaningful when joined with context.

## Details

- Problem shape: no sensor measures "is the dog sniffing right now". But sniffing leaves traces — head lowered (IMU pitch), movement stopped (GPS speed 0), repeated at particular places and times.
- Principle: **capture the traces, not the cause.** Each signal alone is ambiguous (head down = sniffing? drinking? sleeping?), but three signals co-occurring narrows to a specific behavior.
- Design implications:
  - Choose sensors by working backwards: phenomenon → accompanying behavior → its physical trace → the sensor that captures that trace
  - Always store time and location context with the value — bare values accumulate as uninterpretable data
  - Start labeling with combination rules (heuristics); replace with a classifier once data accumulates
- Applies broadly: wearable activity recognition, churn-signal detection, server anomaly detection — anywhere with "no direct metric, but traces exist".

## Sources

- (Korean source session is a local-only archive)
