---
title: Bridge Sessions With a Project Memory Directory
tags:
  - tool/claude-code
  - dev/workflow
status: distilled
publish: true
lang: en
translation: 10-Concepts/프로젝트-메모리-디렉토리로-세션-간-컨텍스트를-잇는다
created: 2026-08-04
sources: []
---

## Summary

Recording facts in Claude Code's project memory (`~/.claude/projects/<project>/memory/`) — one fact per file plus a MEMORY.md index — lets the next session start with the previous work's context already loaded.

## Details

- Location and structure: project memory lives at `~/.claude/projects/<project>/memory/`. Record **one fact per file** with frontmatter, and let `MEMORY.md` serve as the index over those files.
- MEMORY.md is the entry point loaded automatically at the start of each session — keep a core summary and links to each memory file there, and a new session immediately knows what the project is.
- Pattern observed in this session: the user asks "remember the previous work" → analyze the project folder → write three kinds of memory files — **project-state / key-findings / env-setup** — and update the index.
- Why split into files: facts split per file let the next session read only what it needs, and when a fact goes stale, only that file needs updating or deleting.
- Effect: the next session skips the "what did we do last time" excavation and continues work with project state, key findings, and environment setup preloaded.
- Best time to record is **right after a meaningful conclusion**, not at session end — the context survives even if the session is cut short.

## Sources

- 
