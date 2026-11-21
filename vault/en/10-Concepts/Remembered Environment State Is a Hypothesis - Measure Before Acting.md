---
title: Remembered Environment State Is a Hypothesis - Measure Before Acting
tags:
  - tool/claude-code
  - llm/context
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/기억된-환경-상태는-가설이다-—-실측한-뒤-행동한다
created: 2026-11-21
sources: []
---

## Summary

Agent memory, the user's recollection, and numbers the user quotes are all hypotheses dated to when they were observed. **Confirm with a one-line measurement before changing the environment, and record in memory not just the state but how it was applied (one-off vs. persistent).**

## Details

- Case 1 — agent memory: while installing a CLI, `npm install --cache D:\...` was used once, yet memory recorded "the npm cache lives on D:". A week later, `npm config get cache` showed it was still on the default C: path, with 2.25 GB re-accumulated. Only then was it made persistent with `npm config set cache D:\... --location=user`.
- Case 2 — a number the user quoted: "C: has 3 GB left", but the measurement said 0.8 GB. That gap moved "clear Temp first" to the top of the plan — if C: hits zero mid-task, editor and agent writes start failing.
- Case 3 — the user's recollection: "there are a few Ollama models on C:" was checked exhaustively. PATH, running processes, `OLLAMA_*` environment variables, four default model locations, the registry's installed-programs list (similar tools included), and four levels deep on the other drive all came up empty, and the likely source of the memory — a conversation log from a few months earlier — was found and shown as well.
- Principle 1: when recording an environment fact in memory, write how it was applied (one-off flag / persistent setting / manual step) next to the state. A one-off action is not a state.
- Principle 2: before changing the environment based on memory or a user's statement, confirm with a one-line measurement (`npm config get cache`, `Get-PSDrive`). Memory tells you where to look; measurement decides what is true.
- Principle 3: a "not found" report lists where you checked and what you could not check. Here the report disclosed that a full search by model-file extensions was stopped for time, so "not found" was not overstated.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Bridge Sessions With a Project Memory Directory]], [[Passed Deadlines Get Extended - Schedule Facts Need Re-Verification]], [[Space Freed by Deleting Comes Back - Relocate Where It Accumulates]]
