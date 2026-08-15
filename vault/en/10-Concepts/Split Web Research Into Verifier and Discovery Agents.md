---
title: Split Web Research Into Verifier and Discovery Agents
tags:
  - llm/agents
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/웹-리서치는-검증과-발굴-에이전트로-분리한다
created: 2026-08-14
sources: []
---

## Summary

For a periodically refreshed dataset, web research works best when **"fact-checking items you already track (verification)" and "finding items you don't (discovery)" run as separate agents** — both accuracy and parallelism improve.

## Details

- The two jobs have different shapes:
  - **Verifier agent**: give it the item list plus last-known values and ask only "did this change?" Spell out the source priority (official site > platform > news > blogs) and force it to answer "unconfirmed" when it can't verify — never to guess.
  - **Discovery agent**: give it a time window (e.g. announcements from the last 2-3 days) and an **exclusion list of IDs already tracked**. Without the exclusion list, most of what comes back is duplicates.
- Stating in the prompt that "your final message is raw data for a script, not prose for a human" makes the return value directly parseable for batch application.
- Stamping every item with `checked: <date>` lets the next round auto-select verification targets by "oldest-checked first."
- Items the agent reports as "unconfirmed" are worth retrying yourself in the main session — a different query or a direct fetch often breaks through.

## Sources

- Related: [[JS-Rendered Sites Are a Blind Spot for Static Fetch Verification]], [[Passed Deadlines Get Extended - Schedule Facts Need Re-Verification]], [[Parallelize ML Experiments With Background Execution]]
