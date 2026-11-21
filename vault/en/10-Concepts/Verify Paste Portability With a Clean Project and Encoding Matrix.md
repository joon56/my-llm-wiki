---
title: Verify Paste Portability With a Clean Project and Encoding Matrix
tags:
  - dev/workflow
  - tool/windows
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/붙여넣기-이식성은-빈-프로젝트와-인코딩-매트릭스로-검증한다
created: 2026-11-21
sources: []
---

## Summary

Code that must run after being pasted into someone else's IDE should not depend on project settings or source encoding — verify it by rebuilding in **a clean project that receives only the source files, crossed with re-saved encodings and build configurations**. That matrix catches defects nothing else reveals.

## Details

- Design: do not rely on project settings such as preprocessor definitions, `/utf-8` or extra include paths (put any required definitions at the top of each .c file). Non-ASCII strings that affect behavior use only `\uXXXX` escapes and wide APIs (`_wfopen`, `WriteConsoleW`); Korean text stays in comments.
- The matrix: a fresh minimal project with only the sources copied × {UTF-8 with BOM, re-saved as CP949, UTF-8 without BOM} × {Debug/Release × x64/Win32} = 12 combinations, each checked against the SHA-256 of the four output files and the test count. The final zip is also extracted into an empty folder on a short path and built from scratch — in a deeply nested folder the build hit the path-length limit.
- What it caught: `\uXXXX` escapes that Claude Code wrote through Edit/Write had been saved as literal Korean characters (apparently decoded somewhere along the tool path), and this only surfaced in the BOM-less UTF-8 copy. A script converted them back, and a "non-ASCII outside comments" scan became a standing check.
- Document non-ASCII you cannot remove as a known limitation: with a Korean file name in a line like `#include "../main_<name>_<id>.c"`, the BOM-less copy fails with C1083, so the guide says "save as UTF-8 with signature".
- Judge "build succeeded" by its artifacts: the problem only showed up because the clean build produced no executable — the script-generated .sln lacked its configuration-mapping section, so nothing was built. Check that the exe exists and that its outputs hash correctly.
- Verify environment claims against the toolset: "I installed VS2022" turned out to be VS2026 (v145) only, because the official default download had moved to the newest major version. Installing through a version-pinned link or a winget ID and then confirming the v143 toolset fixed it.
- Reproduce guides with the defaults users actually click through: "leave the location at its default" put the test project next to the main folder instead of inside it, which broke the `../` include. Recreating the user's layout in a copy confirmed the cause before the guide was fixed. The IDE's paste auto-format only changes whitespace (one Ctrl+Z right after pasting undoes it).

## Sources

- Distilled from private Claude Code session logs (not published).
- Related: [[Windows cp949 Encoding Pitfalls]], [[Paths and Scripts That Pass Through Bash on Windows Get Silently Mangled]], [[Verify Background Process Termination by Checking the Port]]
