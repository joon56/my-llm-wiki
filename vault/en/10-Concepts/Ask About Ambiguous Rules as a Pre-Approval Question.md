---
title: Ask About Ambiguous Rules as a Pre-Approval Question
tags:
  - ml/competition
  - work/communication
status: distilled
publish: true
lang: en
translation: 10-Concepts/규칙이-애매한-기법은-사전-승인-질문으로-묻는다
created: 2026-10-05
sources: []
---

## Summary

When a technique sits in a grey zone of the competition rules, do not settle it by inference — ask the organizers, but **frame it as pre-approval ("is the method I plan to use allowed?"), not as a complaint ("another team seems to be cheating").**

## Details

- Situation: the top scores looked impossible without one technique (matching rows of the same respondent across survey rounds inside the dataset). But it was unclear whether the "re-identification attempt = disqualification" clause covered it. If banned, using it meant disqualification; if allowed, not using it meant a large gap — the whole remaining strategy hinged on one interpretation.
- Framing: wrong — "top teams seem to use this technique; isn't that cheating?" mentions other teams, rests on a guess, and looks like a false accusation if wrong. Right — "I'm considering this technique; is it allowed?" mentions neither the leaderboard nor other teams. It is the most common question type in competitions and marks you as a model participant.
- No downside if the premise is wrong: base the premise on public documents (survey design reports, schema descriptions), not on leaderboard reverse-engineering, and it is a reasonable reading. Even "respondents don't overlap" is useful (you skip building that module).
- Channel: if a public forum feels uncomfortable, start with private email — the answer is equally binding. Bundle any pending questions (e.g. a missing file).
- Outcome: the answer was "matching rows within the dataset, without extracting outside identities, is permitted" — the biggest lever opened legitimately.
- Boundary: clear violations that need no asking (e.g. a second account to dodge submission limits) are not what this is for.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[A Leaderboard Submission Is a Pre-Registered Experiment]]
