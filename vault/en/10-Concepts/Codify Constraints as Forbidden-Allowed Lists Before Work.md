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
- Unattended runs need time boundaries as well. For an overnight run with an 08:00 deadline while the user slept, the rules were declared up front: stop starting new work at 07:30, finish verification and the report by 07:50, only passing work goes to `main` (anything unfinished stays on a branch), no paid services and no force push, anything needing human hands (a tunnel, a phone demo) is out of scope, and when blocked, log it and move on instead of asking. It finished at 07:29 with the blocked items handed to the morning report — and environment checks such as power/sleep settings belong on the pre-run list too.
- When two agents run in parallel in the same folder, settle the boundaries before work too: a subfolder per agent, a list of shared input files, and how the daily submission limit is split. A mid-run instruction to move "my files into a subfolder" ran into the other agent's instruction file referencing paths to be moved (`.venv` and the like) and the IDE's git watcher holding `.git`, so the rename failed (worked around by copy then delete). The same principle applies to subagents — [[Split Parallel Subagents by File Ownership and Keep Builds in the Main Session]].
- Always-on recording rules need a forbidden list as well. With only "write new facts to the knowledge base immediately", the agent wrote people-evaluation and staffing concerns from the conversation into a shared document and only told the user afterwards. Write the exception into the rule from the start: anything about people or personnel is recorded only after confirmation.

## Sources
-
