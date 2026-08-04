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

## Sources
- 
