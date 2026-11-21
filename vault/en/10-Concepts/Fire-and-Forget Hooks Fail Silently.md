---
title: Fire-and-Forget Hooks Fail Silently
tags:
  - tool/claude-code
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/fire-and-forget-훅은-침묵-실패한다
created: 2026-08-04
sources: []
---

## Summary

A fire-and-forget hook that posts events with the `fetch(url).catch(() => {})` pattern **silently drops every event when the receiver is down** — zero sessions recorded, zero errors shown.

## Details

- Real case: agentmemory's hooks POSTed events via `fetch(url).catch(() => {})`; while the daemon was down, every event was quietly discarded. Zero sessions recorded — and zero errors displayed anywhere.
- The diagnosis chain actually used (worth recording): check the port → MCP responds but returns empty data → read the hook source code → discover the process is only a shim → check the daemon startup log → confirm the binary is missing.
- The fire-and-forget trade-off: event delivery failures never block the agent's work, but in exchange the failure signal vanishes entirely.
- A fire-and-forget pipeline therefore **requires a separate external health signal** — e.g. a daemon port check, or a periodic "events captured in the last N minutes > 0" assertion.
- Generalization: for any code containing `.catch(() => {})`, the question to answer first is not "is failure acceptable" but "where will failure become visible."
- A second case is this wiki's own SessionEnd archive hook. It sat dead for about two months while everything looked calm — "nothing new to distill" — with zero errors logged. An earlier break had been caught only by comparing the newest archived date (7/26) with today, and the missed sessions were backfilled with the manual converter, but the root cause was not found until 2026-11-21.
- Root cause: the hook command used unquoted Windows backslash paths. Claude Code runs hooks through Git Bash, which consumed the backslashes as escapes, so the command died with `command not found` (exit 127) before the script even started — and the error log the script was built to write never got a single line. Zero log lines can mean "failed before running", not "healthy" ([[Paths and Scripts That Pass Through Bash on Windows Get Silently Mangled]]).
- Health signal: as the first step of every periodic run (e.g. the weekly distill), compare the newest output date (the latest archived session) with today; "nothing to do" can itself be the symptom of a dead collector. A database trigger making an async HTTP call (`pg_net` to a mail API) has the same shape — a wrong key name silently sends no mail — so on the first production run, one block inserted a test row, changed its status to fire the trigger, and deleted it, confirming that exactly one email actually arrived.

## Sources
- 
