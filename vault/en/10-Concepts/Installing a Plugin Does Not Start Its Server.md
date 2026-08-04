---
title: Installing a Plugin Does Not Start Its Server
tags:
  - tool/claude-code
  - tool/mcp
  - dev/debugging
status: distilled
publish: true
lang: en
translation: 10-Concepts/플러그인-설치와-서버-실행은-별개다
created: 2026-08-04
sources: []
---

## Summary

A plugin that depends on an external daemon **only works if that daemon separately exists and is running** — the plugin registers hooks and glue, it does not launch the server for you.

## Details

- agentmemory case: the Claude Code plugin's job ends at registering hooks and providing an MCP stdio shim. Actual storage is handled by a separate daemon (the iii engine, REST on port 3111, viewer on 3113), which must exist and be running on its own.
- The usual answer to "I installed the plugin, why is there no data?" is a **missing daemon** — in this case the iii-engine binary itself was absent, fixed by manually downloading it from GitHub releases.
- The usage model has three layers: (1) manual slash skills `/remember` `/recall` `/handoff`, (2) MCP tools the agent calls on its own, (3) hooks that auto-capture session events. All three layers point at the same daemon underneath.
- So when the daemon is down, all three layers go silently dead at once — often with no explicit error surfacing in any of them.
- Diagnostic order: before suspecting plugin configuration, first check that the daemon process and its port (3111) are alive. "Is it installed" and "is it running" are always two separate questions.

## Sources
- 
