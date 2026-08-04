---
title: Always-Loaded Instruction Files Can Conflict
tags:
  - tool/claude-code
  - llm/context
status: distilled
publish: true
lang: en
translation: 10-Concepts/상시-로드되는-지침-파일끼리-충돌할-수-있다
created: 2026-08-04
sources: []
---

## Summary

When multiple always-loaded instruction layers stack up — CLAUDE.md, AGENTS.md, plugin hooks — **they can silently issue opposite directives**; nothing errors, the model just gets pulled in both directions.

## Details

- Real case: installing a third-party pack also dropped a `~/.claude/AGENTS.md` (8.4KB) demanding "maintain 80% coverage, always plan first, always delegate to subagents."
- The problem: the user's existing CLAUDE.md prescribed the exact opposite — a karpathy-style minimalism ("minimum code, use judgment"). Both files loaded every session, pulling the model in opposite directions.
- This conflict raises no error or warning. The only symptom is inconsistent, wobbling model behavior, which makes the root cause hard to trace.
- There are at least three always-loaded layers: user/project CLAUDE.md, AGENTS.md-style files installed by tools, and hooks or system-prompt injections registered by plugins. Each gets installed separately, so nobody ends up seeing the whole picture.
- Prevention: **audit what instruction files a tool installs and where before accepting it**, and after installing, check for new .md files under `~/.claude/`. Delete or merge any file that contradicts your existing philosophy.

## Sources
- 
