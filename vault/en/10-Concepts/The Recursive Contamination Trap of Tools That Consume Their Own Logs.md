---
title: The Recursive Contamination Trap of Tools That Consume Their Own Logs
tags:
  - dev/architecture
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/자기-로그를-다루는-도구의-재귀-오염-함정
created: 2026-07-26
sources: []
---

## Summary

Run a tool that consumes its own execution logs inside the environment where those logs accumulate, and the *work of building the tool* becomes new input for its next run. Without an explicit filter, self-referential contamination quietly accumulates.

## Details

- This wiki is the exact case: Claude Code session logs are converted into wiki content — but the "sessions spent building the wiki" are themselves logged, and flow back in on the next import. The wiki fills with stories about making the wiki.
- Left alone: meta-work logs dilute the real knowledge logs, the archive bloats meaninglessly, and every distill pass pays a recurring "this is just wiki-meta" triage cost.
- Countermeasures:
  - **Source filters**: exclude meta-work sessions at conversion time (project/path filters like `--project`)
  - **Triage rule**: extract any lessons from meta sessions once, then mark them `triaged` immediately
  - **Separate execution**: develop the tool where its logs don't accumulate, when possible
- Generalization: a classic trap for log collectors, monitoring, and backup tools — at design time, check whether the collector collects its own act of collecting.

## Sources

- (Korean source session is a local-only archive)
