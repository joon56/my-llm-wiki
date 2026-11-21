---
title: Generate Change Reports From the Diff, Not From Memory
tags:
  - llm/agents
  - dev/workflow
  - dev/docs
status: distilled
publish: true
lang: en
translation: 10-Concepts/변경-보고는-기억이-아니라-diff에서-뽑는다
created: 2026-11-21
sources: []
---

## Summary

An agent's from-memory summary of "what I changed and what I checked" will miss things — **keep a backup before the work, generate the change list from a diff right before reporting**, and state separately the scope you checked, the result against any target you announced, and changes nobody asked for.

## Details

- Case: after reporting "I only translated the on-screen messages", the user asked "so you touched nothing else?" A diff against the backup showed two added comment sentences, five on-screen strings outside printf, a renamed test function, rewritten report sentences, and two deletions missing from the earlier report.
- Report the checked scope per file: mentioning only the three files that had problems made the user ask again whether the rest had been checked at all.
- Lead with the gap between an announced target and the result: after promising to cut the implementation to 1,100-1,300 lines, the work stopped at 2,034 lines, and that went unmentioned until the user asked.
- Counting and measuring scripts need verification too: the line counter treated code lines starting with `*` as comments and reported 1,321 lines (actually 1,336). The memory probe sampled periodically, missed the peak just before exit, and reported 4.4 MB (actually 5.1 MB).
- Check narrative claims against the original as well: "previous behavior" descriptions in the report were compared with the pre-refactor backup, and line numbers and test-spec tables were extracted from the source rather than copied by hand.
- Back negative claims ("I never deleted it") with evidence: for a zip that disappeared, the command history was first checked for any deletion, then the file was located (the user had moved it to another folder).
- The format that stuck: end each report with a "not requested" section and the path of the pre-change backup.

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Verify Background Process Termination by Checking the Port]], [[Remembered Environment State Is a Hypothesis - Measure Before Acting]], [[Verify Version Drift Between Planning Docs and Final Deliverables]]
