---
title: Verify Background Process Termination by Checking the Port
tags:
  - dev/debugging
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/백그라운드-종료-보고는-포트-확인으로-검증해야-한다
created: 2026-07-26
sources: []
---

## Summary

Don't take a tool's "success" report of killing a background process at face value — in watch-mode setups where a supervisor process spawns the actual server as a child, killing the supervisor can leave the child server alive, so verify termination by directly checking the listening port.

## Details

- Watch-mode tools like `nest start --watch` or `nodemon` have a two-layer structure: a supervisor (wrapper) process watches for file changes, while the actual server runs as a separate child process underneath it.
- If the termination tool only kills the wrapper, the child server keeps running, orphaned — still holding the port. The tool reports "terminated successfully," but the real server is still alive.
- Symptoms: restarting doesn't pick up code changes / `EADDRINUSE` port conflicts / the old process keeps responding.
- Verification: after terminating, check directly whether the port is free with `netstat -ano | findstr :3000` (Windows) or `lsof -i :3000` (macOS/Linux). If something's still there, grab the PID and kill it explicitly.
- Generalization: the truth about a process's state comes from the OS's port/process listing, not from a tool's response.

## Sources
-
