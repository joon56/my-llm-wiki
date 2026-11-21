---
title: Ask Only at Hard-to-Reverse Forks and Proceed on Disclosed Assumptions
tags:
  - llm/agents
  - dev/workflow
  - work/communication
status: distilled
publish: true
lang: en
translation: 10-Concepts/되돌리기-어려운-갈림길만-묻고-나머지는-가정을-공개한-채-진행한다
created: 2026-11-21
sources: []
---

## Summary

An agent that waits for approval at every section ends up being corrected for it. **Ask only about decisions that are hard to reverse or where preferences split — all at once, as options with a recommendation — then carry on to the end on a disclosed list of assumptions, keeping only pushes, publishing, and feature removal outside your autonomy.**

## Details

- Correction 1: after posting a design draft and finishing environment setup, the agent said "waiting for your feedback" twice, and the user replied, "Are you waiting for my feedback? Just go ahead with everything." From then on it worked to the end without questions, listed its decisions in the final report, and saved the preference as feedback memory so later sessions follow it too.
- What to ask: only forks that are hard to reverse or involve the user's resources or preferences. Eight items of meeting feedback produced just four questions (scope of the design drafts, file storage, whether to keep an existing feature, whether to rename the package as well), each with A/B(/C) options plus "(recommended)" and a reason.
- The remaining ~10 decisions were disclosed as assumptions: "I'll proceed like this without asking (tell me if not)". The user answered in four lines and chose against the recommendation twice (reusing an account they already had, preferring generality) — the four questions really were where preferences split. The disclosed assumptions passed without objection.
- Work that needs the user's hands (console settings, issuing tokens) is scheduled so it does not block: "Not urgent — only needed before that step; if it isn't done, that step waits and the rest goes ahead."
- Keep outside your autonomy: pushes, publishing to a public repo, external sharing, removing features. Every push was confirmed first, and whether to trim out-of-scope features went to the user as a table of "replaceable? / needed? / opinion".
- Correction 2: during a low-risk check (polling for an API-key restriction to propagate), the interim reports got wordy and the user replied, "So what are you doing now? ... let's just move on. I'm going to sleep." Cut reports to three lines — what I was doing / risk level / what you need to do (nothing) — and move the remaining checks to the background.
- It works for small tasks too: grouping 18 disk-cleanup candidates into "safe / needs your check / leave alone" and numbering them let the user decide in one line: "delete 1 through 13".

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Blank-Slate Questions Invite Silence - Ask With Options]], [[Codify Constraints as Forbidden-Allowed Lists Before Work]], [[Ask About Ambiguous Rules as a Pre-Approval Question]]
