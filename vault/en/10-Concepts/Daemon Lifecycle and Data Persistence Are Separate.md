---
title: Daemon Lifecycle and Data Persistence Are Separate
tags:
  - dev/tooling
  - tool/claude-code
status: distilled
publish: true
lang: en
translation: 10-Concepts/데몬-생명주기와-데이터-영속성은-분리된다
created: 2026-08-04
sources: []
---

## Summary

In any daemon-backed tool, process state and data state are independent axes — `stop` kills only the process while data stays on disk, and status-check commands must never mutate anything.

## Details

- agentmemory's `stop` terminates only the background process. Stored memories remain on disk under `~/.agentmemory/`, so restarting brings everything back intact.
- `status` is a pure query — even when the daemon is down, it reports and never starts it for you. Verify per tool that "check commands don't mutate".
- Background daemons stay alive until reboot unless explicitly killed — "it will shut itself down when the session ends" is a wrong assumption.
- Generalized mental model: for any daemon-backed tool, always separate two questions — (1) is the process running? (2) where does the data live?
- Practical consequence: to actually remove data, use the data directory or a deletion API, not `stop`; conversely, to just free resources temporarily, `stop` alone is enough and loses nothing.
- A third axis is stdio inheritance. Piping the output of a CLI that spawns a daemon on first run (agent-browser and the like) into `| tail` hangs the command: the daemon inherits stdout, so the pipe never closes. Detach the first run with `> /dev/null 2>&1 < /dev/null` and pin a session name (`AGENT_BROWSER_SESSION`).
- When cleaning up, sort what is running into three groups: (1) processes using real resources (emulator, qemu — `adb emu kill`, then force-kill leftovers); (2) idle daemons waiting to speed up the next build (Gradle, the Kotlin compile daemon, the adb server — `gradlew --stop`, `adb kill-server`); (3) IDE-owned processes (language servers — the IDE respawns them, so leave them). Tell which group a java process belongs to from its CommandLine in `Get-CimInstance Win32_Process`.
- Shutting down can create data: an emulator auto-saves a quickboot snapshot on exit, rewriting gigabytes to disk (2.0GB for a single watch AVD). To prevent it, launch with `-no-snapshot-save` or disable quickboot in config.ini (at the cost of a cold boot 20-30 seconds slower).

## Sources

- 
