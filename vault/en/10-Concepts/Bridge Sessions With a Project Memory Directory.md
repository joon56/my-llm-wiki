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
- Memory is keyed by path, and it goes stale. Move the project folder and it is treated as a new project — memory and `--resume` history disappear — so copy the old `projects/<path>` directory under the new path's name and fix absolute paths inside the memory files ([[Moving a Folder Breaks State Keyed by Its Path]]). An entry that recorded a one-off action as state ("npm cache lives on D:") no longer matched reality a week later: record how a change was applied (one-off vs. permanent), and measure before relying on it ([[Remembered Environment State Is a Hypothesis - Measure Before Acting]]).
- Record not just what got solved but also "failed, cause unknown" — the same day. The next day, "why did pairing fail yesterday?" got zero hits from a memory search in both Korean and English, so the cause could not be reconstructed and only a generic list of causes could be offered. A build trap solved in that same session (needing the IDE's bundled JBR instead of the system JVM) had been saved to a memory file right away so the next session would not repeat it.
- Don't bake state into handoff or startup prompts. A startup prompt that spelled out the current stage went stale after the first update. Have the prompt say only "read the 'current state' section of CLAUDE.md", update state in that one place, and confirm a new session is ready with "run the check script once on the test file, then reply only 'ready'".

## Sources

- 
