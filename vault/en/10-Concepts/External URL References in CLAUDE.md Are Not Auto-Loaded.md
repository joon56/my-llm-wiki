---
title: External URL References in CLAUDE.md Are Not Auto-Loaded
tags:
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/CLAUDE.md의-외부-URL-참조는-자동-로드되지-않는다
created: 2026-07-26
sources: []
---

## Summary

Writing "see this URL" as a link inside CLAUDE.md doesn't mean Claude Code automatically fetches it every session — if you want a rule to apply every time, inline the content directly into the file.

## Details

- At session start, CLAUDE.md only puts the **literal text written in the file** into context. A URL is just a string; it isn't auto-fetched.
- For a URL's content to actually take effect, the agent has to call WebFetch on it every time, and that isn't guaranteed — it also costs tokens and time.
- Selection criteria:
  - **Rules that should always apply** → inline the content into CLAUDE.md (summarized if long)
  - **Occasionally-needed references** → keep it as a URL, but explicitly instruct "fetch this when needed"
- The same principle applies broadly to skill files and agent instruction files — it's safest to assume external links in instruction files are dead references by default.

## Sources
-
