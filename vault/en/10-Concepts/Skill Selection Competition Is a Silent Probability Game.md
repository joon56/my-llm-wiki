---
title: Skill Selection Competition Is a Silent Probability Game
tags:
  - tool/claude-code
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/스킬-선택-경쟁은-에러-없는-확률-게임이다
created: 2026-08-04
sources: []
---

## Summary

Installing multiple same-purpose skills never raises a "conflict" error — **the model just reads their descriptions and probabilistically picks one**, with no warning and no log.

## Details

- Example: `tdd` and `superpowers:test-driven-development` serve the same purpose, but since their names differ the system treats them as unrelated skills. Installing both produces no error, no warning, no log entry.
- Which skill fires is a probability game: the model reads each description and judges which fits the situation — there is no deterministic priority rule.
- Trigger breadth in the description shapes the odds: a broad trigger like "any bug" wins often, while a narrow one like "red-green-refactor" wins only when that exact phrasing appears. One broad-trigger skill can effectively shadow several narrow ones.
- Post-hoc check: search the conversation transcript for `Skill(...)` calls — the namespace prefix on the invoked skill name (e.g. `superpowers:`) reveals which one actually fired.
- Practical lesson: if you have duplicate same-purpose skills, check the transcript to see which one is winning, then remove the loser or rewrite descriptions so the competition disappears entirely.

## Sources
- 
