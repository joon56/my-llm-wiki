---
title: Compare Tool Profiles by Install-Plan Diff, Not Module Names
tags:
  - dev/tooling
  - tool/claude-code
  - llm/agents
status: distilled
publish: true
lang: en
translation: 10-Concepts/프로필-비교는-모듈명이-아니라-install-plan-diff로-한다
created: 2026-08-04
sources: []
---

## Summary

Choosing between profiles like minimal vs developer should be done by diffing their actual install plans (file lists), not by reading module names and guessing.

## Details

- Compared the minimal and developer profiles by dumping each one's actual install plan via `--dry-run` and diffing the results.
- Finding 1: minimal turned out to be a strict subset of developer — the worry "will minimal miss something?" was settled with data, not intuition.
- Finding 2: the misfire-prone modules were already included in minimal — avoiding the developer profile would not have removed the misfires.
- Finding 3: developer's extras covered unused stacks such as Perl, F#, and ArkTS — in this environment, pure token cost with zero benefit.
- Lesson: a name like "developer" carries no information. Names are marketing; the file list is the fact.
- Reusable pattern: whenever picking among profiles/editions/tiers, dump each option's output list, diff them, and judge only whether the set difference has value for you.

## Sources

- 
