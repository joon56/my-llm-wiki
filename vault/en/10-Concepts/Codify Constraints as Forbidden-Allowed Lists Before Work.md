---
title: Codify Constraints as Forbidden-Allowed Lists Before Work
tags:
  - llm/prompting
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/작업-전-제약을-금지·허용-리스트로-명문화한다
created: 2026-08-04
sources: []
---

## Summary

Before starting a long constrained task, write the constraint out as an explicit forbidden/allowed list and agree on it — the agent then operates strictly inside that boundary for the entire multi-hour session.

## Details

- A prose constraint like "model architecture and loss are frozen; only input composition is free" leaves room for interpretation — before work begins, unpack it into a forbidden list and an allowed list and get agreement first.
- Example: forbidden = adding/removing layers, swapping the loss function, changing the optimizer / allowed = input feature combinations, preprocessing, data composition changes. Once items are listed explicitly, judgment calls become lookups.
- The agreed list becomes an immutable reference for the whole huge multi-turn session — the boundary stays sharp even as the context grows over hours.
- When an idea near the boundary comes up, the agent checks "does this hit the forbidden list?" instead of proceeding on its own, eliminating the cost of reverting constraint violations after the fact.
- The same principle applies to ambiguous instructions: when a request splits into interpretations A and B, present both side by side and ask, instead of silently picking one.
- Timing is the point — codify before the work, not correct after it. A few minutes of list-writing prevents large-scale rework late in the session.

## Sources
-
